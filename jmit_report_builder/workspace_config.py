"""
JMIT Report Builder - Sidebar and workspace configuration
"""

def get_report_builder_sidebar():
	"""Return sidebar for report builder workspace"""
	return {
		'label': 'Report Builder',
		'items': [
			{
				'type': 'doctype',
				'doctype': 'JMIT Report',
				'label': 'Reports'
			}
		]
	}
