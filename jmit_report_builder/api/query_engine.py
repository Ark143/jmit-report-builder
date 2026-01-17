"""
Query Execution Engine - Executes SQL, stored procedures, and views
"""
import frappe
from frappe.decorators import whitelist
import json

@whitelist()
def execute_query(query_config):
	"""
	Execute a query with grouping and subtotals
	query_config: {
		'query': 'SELECT ... FROM ...',
		'query_type': 'SQL|STORED_PROCEDURE|VIEW',
		'grouping_fields': ['field1', 'field2'],
		'subtotal_fields': [{'field': 'amount', 'operation': 'SUM'}],
		'filters': [{'field': 'date', 'operator': '=', 'value': '2024-01-01'}]
	}
	"""
	try:
		config = json.loads(query_config) if isinstance(query_config, str) else query_config
		
		query = config.get('query', '')
		query_type = config.get('query_type', 'SQL')
		grouping_fields = config.get('grouping_fields', [])
		subtotal_fields = config.get('subtotal_fields', [])
		filters = config.get('filters', [])
		
		# Apply filters
		query = apply_filters(query, filters)
		
		# Execute query based on type
		if query_type == 'SQL':
			results = frappe.db.sql(query, as_dict=True)
		elif query_type == 'STORED_PROCEDURE':
			results = execute_stored_procedure(query, filters)
		elif query_type == 'VIEW':
			results = frappe.db.sql(f"SELECT * FROM {query}", as_dict=True)
		else:
			results = []
		
		# Apply grouping and subtotals
		if grouping_fields:
			results = apply_grouping_and_subtotals(results, grouping_fields, subtotal_fields)
		
		return {
			'success': True,
			'data': results,
			'count': len(results) if results else 0
		}
	except Exception as e:
		frappe.logger().error(f"Query execution error: {str(e)}")
		return {
			'success': False,
			'message': str(e)
		}

def apply_filters(query, filters):
	"""
	Apply WHERE filters to the query
	"""
	if not filters:
		return query
	
	where_conditions = []
	for f in filters:
		field = f.get('field', '')
		operator = f.get('operator', '=')
		value = f.get('value', '')
		
		if operator == '=':
			where_conditions.append(f"{field} = '{value}'")
		elif operator == '!=':
			where_conditions.append(f"{field} != '{value}'")
		elif operator == '>':
			where_conditions.append(f"{field} > {value}")
		elif operator == '<':
			where_conditions.append(f"{field} < {value}")
		elif operator == 'LIKE':
			where_conditions.append(f"{field} LIKE '%{value}%'")
		elif operator == 'IN':
			values = "', '".join(value.split(','))
			where_conditions.append(f"{field} IN ('{values}')")
	
	if where_conditions:
		where_clause = " AND ".join(where_conditions)
		if "WHERE" in query.upper():
			query = query.replace(" WHERE", f" WHERE {where_clause} AND")
		else:
			query += f" WHERE {where_clause}"
	
	return query

def execute_stored_procedure(proc_name, params):
	"""
	Execute a stored procedure
	"""
	try:
		result = frappe.call('frappe.client.sql', query=f"CALL {proc_name}()", as_dict=True)
		return result
	except Exception as e:
		frappe.logger().error(f"Stored procedure error: {str(e)}")
		return []

def apply_grouping_and_subtotals(data, grouping_fields, subtotal_fields):
	"""
	Apply grouping and calculate subtotals
	"""
	if not data or not grouping_fields:
		return data
	
	from collections import defaultdict
	
	grouped_data = defaultdict(list)
	
	# Group the data
	for record in data:
		key = tuple(record.get(field, '') for field in grouping_fields)
		grouped_data[key].append(record)
	
	# Build result with grouping headers and subtotals
	result = []
	for group_key, records in grouped_data.items():
		# Add group header
		group_header = {
			'_type': 'GROUP_HEADER',
			'_group_key': dict(zip(grouping_fields, group_key)),
			'_record_count': len(records)
		}
		result.append(group_header)
		
		# Add records
		result.extend(records)
		
		# Add subtotals
		if subtotal_fields:
			subtotal_row = {
				'_type': 'SUBTOTAL',
				'_group_key': dict(zip(grouping_fields, group_key))
			}
			
			for subtotal_field in subtotal_fields:
				field_name = subtotal_field.get('field')
				operation = subtotal_field.get('operation', 'SUM')
				
				if operation == 'SUM':
					subtotal_row[f'{field_name}_subtotal'] = sum(float(r.get(field_name, 0) or 0) for r in records)
				elif operation == 'AVG':
					values = [float(r.get(field_name, 0) or 0) for r in records if r.get(field_name)]
					subtotal_row[f'{field_name}_subtotal'] = sum(values) / len(values) if values else 0
				elif operation == 'COUNT':
					subtotal_row[f'{field_name}_subtotal'] = len(records)
				elif operation == 'MAX':
					subtotal_row[f'{field_name}_subtotal'] = max([float(r.get(field_name, 0) or 0) for r in records])
				elif operation == 'MIN':
					subtotal_row[f'{field_name}_subtotal'] = min([float(r.get(field_name, 0) or 0) for r in records])
			
			result.append(subtotal_row)
	
	return result

@whitelist()
def preview_query(query):
	"""
	Preview query results without full processing
	"""
	try:
		query = str(query).strip()
		if not query:
			return {'success': False, 'message': 'Query cannot be empty'}
		
		# Limit results for preview
		if 'LIMIT' not in query.upper():
			query += ' LIMIT 100'
		
		results = frappe.db.sql(query, as_dict=True)
		return {
			'success': True,
			'data': results[:10],  # Show first 10 rows
			'total_count': len(results)
		}
	except Exception as e:
		return {
			'success': False,
			'message': str(e)
		}

@whitelist()
def get_available_tables():
	"""
	Get list of available database tables and views
	"""
	try:
		tables = frappe.db.sql("""
			SELECT TABLE_NAME 
			FROM information_schema.TABLES 
			WHERE TABLE_SCHEMA = DATABASE()
			ORDER BY TABLE_NAME
		""", as_dict=True)
		
		return {
			'success': True,
			'data': [t.get('TABLE_NAME') for t in tables]
		}
	except Exception as e:
		return {
			'success': False,
			'message': str(e)
		}

@whitelist()
def get_table_columns(table_name):
	"""
	Get columns and their data types for a specific table
	"""
	try:
		columns = frappe.db.sql(f"""
			SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE
			FROM information_schema.COLUMNS
			WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = %s
			ORDER BY ORDINAL_POSITION
		""", (table_name,), as_dict=True)
		
		return {
			'success': True,
			'data': columns
		}
	except Exception as e:
		return {
			'success': False,
			'message': str(e)
		}
