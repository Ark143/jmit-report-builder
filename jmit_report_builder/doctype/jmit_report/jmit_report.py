"""
JMIT Report DocType Class
Main report definition and management
"""
import frappe
from frappe.model.document import Document

class JMITReport(Document):
	def validate(self):
		"""Validate report configuration"""
		if not self.report_name:
			frappe.throw("Report name is required")
		
		if not self.report_query:
			frappe.throw("Report query is required")
		
		# Validate query syntax
		self.validate_query_syntax()
	
	def validate_query_syntax(self):
		"""Validate SQL query syntax"""
		try:
			query = self.report_query.strip()
			
			if self.query_type == 'SQL':
				if not query.upper().startswith('SELECT'):
					frappe.throw("SQL query must start with SELECT")
			elif self.query_type == 'STORED_PROCEDURE':
				if not query.upper().startswith('CALL'):
					frappe.throw("Stored procedure call must start with CALL")
		except Exception as e:
			frappe.throw(f"Query validation error: {str(e)}")
	
	def on_update(self):
		"""Called after report is updated"""
		frappe.msgprint(f"Report '{self.report_name}' updated successfully")

def on_update(doc, method):
	"""Hook for document update"""
	pass
