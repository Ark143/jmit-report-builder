"""
JMIT Report Builder Utility Functions
Helper functions for report generation, formatting, and processing
"""
import frappe
from datetime import datetime
import json

def format_currency(value, precision=2):
	"""Format value as currency"""
	try:
		return f"${float(value):,.{precision}f}"
	except:
		return value

def format_percentage(value, precision=2):
	"""Format value as percentage"""
	try:
		return f"{float(value):.{precision}f}%"
	except:
		return value

def format_date(value, format='%Y-%m-%d'):
	"""Format date value"""
	try:
		if isinstance(value, str):
			date_obj = datetime.strptime(value, '%Y-%m-%d')
		else:
			date_obj = value
		return date_obj.strftime(format)
	except:
		return value

def validate_sql_query(query):
	"""
	Validate SQL query for security and syntax
	"""
	dangerous_keywords = ['DROP', 'DELETE', 'TRUNCATE', 'INSERT', 'UPDATE', 'ALTER']
	query_upper = query.upper().strip()
	
	for keyword in dangerous_keywords:
		if query_upper.startswith(keyword):
			return False, f"Query cannot start with {keyword}"
	
	if not query_upper.startswith('SELECT') and not query_upper.startswith('CALL'):
		return False, "Query must start with SELECT or CALL"
	
	return True, "Query is valid"

def get_report_statistics(data):
	"""
	Generate statistics for report data
	"""
	if not data or len(data) == 0:
		return {}
	
	stats = {
		'total_rows': len(data),
		'generated_at': datetime.now().isoformat(),
		'numeric_fields': {},
		'text_fields': {}
	}
	
	# Analyze first record to determine field types
	first_record = data[0]
	
	for key, value in first_record.items():
		if not key.startswith('_'):
			try:
				float(value)
				stats['numeric_fields'][key] = {
					'min': None,
					'max': None,
					'sum': 0,
					'count': 0
				}
			except (TypeError, ValueError):
				stats['text_fields'][key] = {
					'unique_values': set()
				}
	
	# Calculate statistics
	for record in data:
		for field in stats['numeric_fields']:
			try:
				val = float(record.get(field, 0) or 0)
				stats['numeric_fields'][field]['sum'] += val
				stats['numeric_fields'][field]['count'] += 1
				
				if stats['numeric_fields'][field]['min'] is None or val < stats['numeric_fields'][field]['min']:
					stats['numeric_fields'][field]['min'] = val
				
				if stats['numeric_fields'][field]['max'] is None or val > stats['numeric_fields'][field]['max']:
					stats['numeric_fields'][field]['max'] = val
			except (TypeError, ValueError):
				pass
	
	# Calculate averages
	for field in stats['numeric_fields']:
		if stats['numeric_fields'][field]['count'] > 0:
			stats['numeric_fields'][field]['avg'] = stats['numeric_fields'][field]['sum'] / stats['numeric_fields'][field]['count']
	
	return stats

def export_report_config(report_doc):
	"""
	Export report configuration as JSON
	"""
	config = {
		'report_name': report_doc.report_name,
		'description': report_doc.description,
		'data_source': report_doc.data_source,
		'query_type': report_doc.query_type,
		'report_query': report_doc.report_query,
		'enabled': report_doc.enabled,
		'columns': [],
		'grouping_fields': [],
		'filters': [],
		'subtotal_config': report_doc.subtotal_config
	}
	
	# Add columns
	for col in report_doc.columns:
		config['columns'].append({
			'field_name': col.field_name,
			'display_label': col.display_label,
			'field_type': col.field_type,
			'width': col.width,
			'alignment': col.alignment,
			'format': col.format,
			'visible': col.visible
		})
	
	# Add grouping fields
	for grp in report_doc.grouping_fields:
		config['grouping_fields'].append({
			'field_name': grp.field_name,
			'sort_order': grp.sort_order
		})
	
	# Add filters
	for flt in report_doc.filters:
		config['filters'].append({
			'field_name': flt.field_name,
			'operator': flt.operator,
			'filter_value': flt.filter_value,
			'filter_type': flt.filter_type,
			'mandatory': flt.mandatory
		})
	
	return config

def import_report_config(config_json):
	"""
	Import report from JSON configuration
	"""
	try:
		config = json.loads(config_json) if isinstance(config_json, str) else config_json
		
		report_doc = frappe.get_doc({
			'doctype': 'JMIT Report',
			'report_name': config.get('report_name'),
			'description': config.get('description', ''),
			'data_source': config.get('data_source'),
			'query_type': config.get('query_type', 'SQL'),
			'report_query': config.get('report_query'),
			'enabled': config.get('enabled', True),
			'subtotal_config': config.get('subtotal_config', '[]')
		})
		
		# Add columns
		for col in config.get('columns', []):
			report_doc.append('columns', {
				'field_name': col.get('field_name'),
				'display_label': col.get('display_label'),
				'field_type': col.get('field_type'),
				'width': col.get('width'),
				'alignment': col.get('alignment'),
				'format': col.get('format'),
				'visible': col.get('visible', True)
			})
		
		# Add grouping fields
		for grp in config.get('grouping_fields', []):
			report_doc.append('grouping_fields', {
				'field_name': grp.get('field_name'),
				'sort_order': grp.get('sort_order', 'Ascending')
			})
		
		# Add filters
		for flt in config.get('filters', []):
			report_doc.append('filters', {
				'field_name': flt.get('field_name'),
				'operator': flt.get('operator'),
				'filter_value': flt.get('filter_value'),
				'filter_type': flt.get('filter_type', 'Static'),
				'mandatory': flt.get('mandatory', False)
			})
		
		return report_doc
	except Exception as e:
		frappe.throw(f"Error importing report configuration: {str(e)}")

def clone_report(source_report_name, new_report_name):
	"""
	Clone an existing report
	"""
	try:
		source_report = frappe.get_doc('JMIT Report', source_report_name)
		config = export_report_config(source_report)
		config['report_name'] = new_report_name
		
		new_report = import_report_config(config)
		new_report.insert()
		
		frappe.msgprint(f"Report cloned successfully to '{new_report_name}'")
		return new_report
	except Exception as e:
		frappe.throw(f"Error cloning report: {str(e)}")
