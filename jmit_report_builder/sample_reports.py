"""
JMIT Report Builder - Sample Reports
Pre-configured example reports for demonstration
"""

SAMPLE_SALES_REPORT = {
	"report_name": "Sample Sales Report",
	"description": "Monthly sales analysis by customer with subtotals",
	"data_source": "SQL Query",
	"query_type": "SQL",
	"report_query": """
		SELECT 
			DATE_FORMAT(si.posting_date, '%Y-%m') as month,
			si.customer,
			si.customer_name,
			COUNT(si.name) as invoice_count,
			SUM(si.grand_total) as total_amount
		FROM `tabSales Invoice` si
		WHERE si.docstatus = 1
		GROUP BY DATE_FORMAT(si.posting_date, '%Y-%m'), si.customer
		ORDER BY month DESC, customer ASC
	""",
	"columns": [
		{
			"field_name": "month",
			"display_label": "Month",
			"field_type": "Date",
			"width": 15,
			"alignment": "Center"
		},
		{
			"field_name": "customer",
			"display_label": "Customer Code",
			"field_type": "Text",
			"width": 20,
			"alignment": "Left"
		},
		{
			"field_name": "customer_name",
			"display_label": "Customer Name",
			"field_type": "Text",
			"width": 25,
			"alignment": "Left"
		},
		{
			"field_name": "invoice_count",
			"display_label": "Invoices",
			"field_type": "Number",
			"width": 12,
			"alignment": "Right"
		},
		{
			"field_name": "total_amount",
			"display_label": "Total Amount",
			"field_type": "Currency",
			"width": 20,
			"alignment": "Right",
			"format": "###,##0.00"
		}
	],
	"grouping_fields": [
		{
			"field_name": "month",
			"sort_order": "Descending"
		},
		{
			"field_name": "customer",
			"sort_order": "Ascending"
		}
	],
	"subtotal_config": [
		{"field": "invoice_count", "operation": "SUM"},
		{"field": "total_amount", "operation": "SUM"}
	],
	"filters": [],
	"enabled": True
}

SAMPLE_INVENTORY_REPORT = {
	"report_name": "Sample Inventory Report",
	"description": "Warehouse inventory levels and movements",
	"data_source": "SQL Query",
	"query_type": "SQL",
	"report_query": """
		SELECT 
			item.name as item_code,
			item.item_name,
			bin.warehouse,
			bin.actual_qty,
			bin.reserved_qty,
			(bin.actual_qty - bin.reserved_qty) as available_qty,
			item.valuation_rate,
			(bin.actual_qty * item.valuation_rate) as inventory_value
		FROM `tabBin` bin
		JOIN `tabItem` item ON bin.item_code = item.name
		WHERE bin.actual_qty > 0
		ORDER BY bin.warehouse, item.name
	""",
	"columns": [
		{
			"field_name": "item_code",
			"display_label": "Item Code",
			"field_type": "Text",
			"width": 15
		},
		{
			"field_name": "item_name",
			"display_label": "Item Name",
			"field_type": "Text",
			"width": 25
		},
		{
			"field_name": "warehouse",
			"display_label": "Warehouse",
			"field_type": "Text",
			"width": 15
		},
		{
			"field_name": "actual_qty",
			"display_label": "On Hand",
			"field_type": "Number",
			"width": 12,
			"alignment": "Right"
		},
		{
			"field_name": "reserved_qty",
			"display_label": "Reserved",
			"field_type": "Number",
			"width": 12,
			"alignment": "Right"
		},
		{
			"field_name": "available_qty",
			"display_label": "Available",
			"field_type": "Number",
			"width": 12,
			"alignment": "Right"
		},
		{
			"field_name": "valuation_rate",
			"display_label": "Unit Cost",
			"field_type": "Currency",
			"width": 12,
			"alignment": "Right"
		},
		{
			"field_name": "inventory_value",
			"display_label": "Total Value",
			"field_type": "Currency",
			"width": 15,
			"alignment": "Right"
		}
	],
	"grouping_fields": [
		{
			"field_name": "warehouse",
			"sort_order": "Ascending"
		}
	],
	"subtotal_config": [
		{"field": "actual_qty", "operation": "SUM"},
		{"field": "reserved_qty", "operation": "SUM"},
		{"field": "inventory_value", "operation": "SUM"}
	],
	"filters": [
		{
			"field_name": "warehouse",
			"operator": "=",
			"filter_type": "User Prompt",
			"mandatory": False
		}
	],
	"enabled": True
}

SAMPLE_PURCHASE_REPORT = {
	"report_name": "Sample Purchase Report",
	"description": "Purchase order analysis by supplier",
	"data_source": "SQL Query",
	"query_type": "SQL",
	"report_query": """
		SELECT 
			po.name as po_number,
			po.supplier,
			sup.supplier_name,
			po.posting_date,
			po.delivery_date,
			po.grand_total,
			po.status
		FROM `tabPurchase Order` po
		JOIN `tabSupplier` sup ON po.supplier = sup.name
		WHERE po.docstatus = 1
		ORDER BY po.posting_date DESC
	""",
	"columns": [
		{
			"field_name": "po_number",
			"display_label": "PO Number",
			"field_type": "Text",
			"width": 15
		},
		{
			"field_name": "supplier",
			"display_label": "Supplier Code",
			"field_type": "Text",
			"width": 15
		},
		{
			"field_name": "supplier_name",
			"display_label": "Supplier Name",
			"field_type": "Text",
			"width": 25
		},
		{
			"field_name": "posting_date",
			"display_label": "PO Date",
			"field_type": "Date",
			"width": 12
		},
		{
			"field_name": "delivery_date",
			"display_label": "Expected Delivery",
			"field_type": "Date",
			"width": 15
		},
		{
			"field_name": "grand_total",
			"display_label": "Amount",
			"field_type": "Currency",
			"width": 15,
			"alignment": "Right"
		},
		{
			"field_name": "status",
			"display_label": "Status",
			"field_type": "Text",
			"width": 12
		}
	],
	"grouping_fields": [
		{
			"field_name": "supplier",
			"sort_order": "Ascending"
		}
	],
	"subtotal_config": [
		{"field": "grand_total", "operation": "SUM"}
	],
	"filters": [
		{
			"field_name": "supplier",
			"operator": "=",
			"filter_type": "User Prompt",
			"mandatory": False
		},
		{
			"field_name": "status",
			"operator": "=",
			"filter_type": "Static",
			"filter_value": "Submitted"
		}
	],
	"enabled": True
}

def create_sample_reports():
	"""
	Create sample reports in the database
	"""
	import frappe
	
	sample_reports = [
		SAMPLE_SALES_REPORT,
		SAMPLE_INVENTORY_REPORT,
		SAMPLE_PURCHASE_REPORT
	]
	
	for config in sample_reports:
		try:
			# Check if report already exists
			if frappe.db.exists('JMIT Report', config['report_name']):
				frappe.logger().info(f"Report '{config['report_name']}' already exists")
				continue
			
			# Create report doc
			doc = frappe.get_doc({
				'doctype': 'JMIT Report',
				'report_name': config['report_name'],
				'description': config.get('description', ''),
				'data_source': config.get('data_source'),
				'query_type': config.get('query_type', 'SQL'),
				'report_query': config.get('report_query'),
				'subtotal_config': frappe.as_json(config.get('subtotal_config', [])),
				'enabled': config.get('enabled', True)
			})
			
			# Add columns
			for col in config.get('columns', []):
				doc.append('columns', col)
			
			# Add grouping fields
			for grp in config.get('grouping_fields', []):
				doc.append('grouping_fields', grp)
			
			# Add filters
			for flt in config.get('filters', []):
				doc.append('filters', flt)
			
			doc.insert()
			frappe.logger().info(f"Created sample report: {config['report_name']}")
			
		except Exception as e:
			frappe.logger().error(f"Error creating sample report {config['report_name']}: {str(e)}")
