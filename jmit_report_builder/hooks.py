{
	"app_name": "JMIT Report Builder",
	"app_title": "JMIT Report Builder",
	"app_publisher": "JMIT",
	"app_description": "Crystal Report Clone for ERPNext v15 with advanced grouping, subtotals, stored procedures, and SQL views",
	"app_email": "info@jmit.com",
	"app_license": "MIT",
	"app_version": "0.0.1",
	"app_icon": "icon.png",
	"app_color": "#2563eb",
	"source": "https://github.com/jmittech/jmit-report-builder",
	"category": "Tools",
	"on_session_start": [
		"jmit_report_builder.api.session.on_session_start"
	],
	"doc_events": {
		"JMIT Report": {
			"on_update": "jmit_report_builder.doctype.jmit_report.jmit_report.on_update",
			"validate": "jmit_report_builder.doctype.jmit_report.jmit_report.validate"
		}
	},
	"permission": [
		{
			"doctype": "JMIT Report",
			"name": "JMIT Report",
			"actions": ["all"],
			"roles": ["System Manager", "Report Manager"]
		}
	],
	"has_website": false,
	"website_context": {},
	"homepage": "app/jmit-report-builder-home"
}
