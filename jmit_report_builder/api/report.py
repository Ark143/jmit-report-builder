"""
Report Builder API - Core Report Operations
Handles report creation, modification, and retrieval
"""
import frappe
from frappe.decorators import whitelist
import json

@whitelist()
def get_report(report_name):
	"""
	Get report configuration by name
	"""
	try:
		report = frappe.get_doc('JMIT Report', report_name)
		return {
			'success': True,
			'data': report.as_dict()
		}
	except frappe.DoesNotExistError:
		return {
			'success': False,
			'message': f'Report {report_name} not found'
		}

@whitelist()
def create_report(report_config):
	"""
	Create a new report
	"""
	try:
		config = json.loads(report_config) if isinstance(report_config, str) else report_config
		
		report = frappe.get_doc({
			'doctype': 'JMIT Report',
			'report_name': config.get('report_name'),
			'data_source': config.get('data_source'),
			'query_type': config.get('query_type', 'SQL'),
			'report_query': config.get('report_query'),
			'grouping_fields': config.get('grouping_fields', []),
			'columns': config.get('columns', []),
			'filters': config.get('filters', [])
		})
		
		report.insert()
		return {
			'success': True,
			'message': 'Report created successfully',
			'report_name': report.name
		}
	except Exception as e:
		return {
			'success': False,
			'message': str(e)
		}

@whitelist()
def update_report(report_name, report_config):
	"""
	Update an existing report
	"""
	try:
		config = json.loads(report_config) if isinstance(report_config, str) else report_config
		report = frappe.get_doc('JMIT Report', report_name)
		
		for key, value in config.items():
			if hasattr(report, key):
				setattr(report, key, value)
		
		report.save()
		return {
			'success': True,
			'message': 'Report updated successfully'
		}
	except Exception as e:
		return {
			'success': False,
			'message': str(e)
		}

@whitelist()
def delete_report(report_name):
	"""
	Delete a report
	"""
	try:
		frappe.delete_doc('JMIT Report', report_name)
		return {
			'success': True,
			'message': 'Report deleted successfully'
		}
	except Exception as e:
		return {
			'success': False,
			'message': str(e)
		}

@whitelist()
def list_reports(filters=None):
	"""
	List all reports with optional filters
	"""
	try:
		query_filters = filters if filters else {}
		reports = frappe.get_list('JMIT Report', filters=query_filters, fields=['name', 'report_name', 'data_source', 'query_type', 'modified'])
		return {
			'success': True,
			'data': reports
		}
	except Exception as e:
		return {
			'success': False,
			'message': str(e)
		}
