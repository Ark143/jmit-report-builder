app_name = "jmit_report_builder"
app_title = "JMIT Report Builder"
app_publisher = "JMIT"
app_description = "Crystal Report Clone for ERPNext v15 with advanced grouping, subtotals, stored procedures, and SQL views"
app_email = "info@jmit.com"
app_license = "MIT"
app_version = "0.0.1"
app_icon = "icon.png"
app_color = "#2563eb"
source = "https://github.com/Ark143/jmit-report-builder"
category = "Tools"

# Hooks
on_session_start = [
	"jmit_report_builder.api.session.on_session_start"
]

doc_events = {
	"JMIT Report": {
		"on_update": "jmit_report_builder.doctype.jmit_report.jmit_report.on_update",
		"validate": "jmit_report_builder.doctype.jmit_report.jmit_report.validate"
	}
}

# Fixtures
fixtures = [
	"jmit_report_builder.doctype.jmit_report",
	"jmit_report_builder.doctype.jmit_report_field",
	"jmit_report_builder.doctype.jmit_report_filter",
	"jmit_report_builder.doctype.jmit_report_grouping"
]

# API Endpoints
api_methods = {
	"jmit_report_builder.api.report": {
		"create": "create_report",
		"read": "get_report",
		"read_all": "list_reports",
		"update": "update_report",
		"delete": "delete_report"
	}
}

# Website
has_website = False

# Web Assets
web_asset_folders = ["public"]

# Roles
roles = [
	{"role_name": "Report Manager", "doctype": "Role"}
]
