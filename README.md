# JMIT Report Builder - ERPNext v15 App

A powerful Crystal Report clone for ERPNext v15 with advanced reporting capabilities including grouping, subtotals, stored procedures, and SQL views support.

## Features

✨ **Advanced Report Designer**
- Intuitive drag-and-drop interface similar to Crystal Reports
- Support for multiple data sources (SQL, Stored Procedures, Database Views)
- Real-time query preview

🎯 **Grouping & Aggregation**
- Multiple-level grouping
- Automatic subtotal calculation (SUM, AVG, COUNT, MAX, MIN)
- Customizable group headers and footers

💾 **Data Source Support**
- Direct SQL queries
- Stored procedures
- Database views
- Parameterized queries

📊 **Export Capabilities**
- Export to PDF
- Export to Excel (XLSX)
- Export to CSV
- Formatted output with grouping preserved

🔧 **Advanced Features**
- Query builder with table/column explorer
- Multiple filter types (static, user prompt, parameters)
- Field formatting options
- User-based access control

## Installation

### Prerequisites
- ERPNext v15
- Frappe Framework
- Python 3.8+
- MySQL/MariaDB

### Install via Bench

```bash
# Navigate to your bench directory
cd /path/to/bench

# Add the app
bench get-app jmit_report_builder /path/to/jmit_report_builder

# Install the app
bench install-app jmit_report_builder

# Restart bench
bench start
```

### Install via GitHub

```bash
bench get-app jmit-report-builder https://github.com/jmittech/jmit-report-builder.git
bench install-app jmit_report_builder
```

## Usage

### Creating a New Report

1. Navigate to **JMIT Report Builder** > **New Report**
2. Fill in the report details:
   - **Report Name**: Name your report
   - **Description**: Add details about the report
   - **Data Source Type**: Choose SQL Query, Stored Procedure, or Database View

3. **Configure Data Source**:
   - Enter your SQL query or stored procedure name
   - Click "Preview Query" to test the query

4. **Add Columns**:
   - Click "Add Column" to add fields to your report
   - Set display labels, data types, and formatting

5. **Setup Grouping** (Optional):
   - Click "Add Grouping" to group by specific fields
   - Set sort order (Ascending/Descending)
   - Grouping supports multiple levels

6. **Configure Subtotals**:
   - Set subtotal operations (SUM, AVG, COUNT, MAX, MIN)
   - Subtotals calculate automatically based on grouping

7. **Add Filters**:
   - Click "Add Filter" to add filter conditions
   - Set filter type: Static, User Prompt, or Report Parameter
   - Mark as mandatory if required

8. **Save Report**:
   - Click "Save Report"
   - Report is now available for execution

### Running a Report

1. Open the saved report
2. Fill in any required filter values
3. Click "Preview" to see the report data
4. Click "Export" to download in desired format

### Using the Report Designer UI

Access the report designer via:
- Menu: **JMIT Report Builder** > **Report Designer**
- Quick access: Ctrl+Shift+R

The designer provides a real-time interface to:
- Write and preview SQL queries
- Add/remove columns
- Configure grouping and filters
- Preview final output
- Export data

## API Documentation

### Report Management

#### Get Report
```python
GET /api/resource/JMIT Report/{report_name}
```

#### Create Report
```python
POST /api/method/jmit_report_builder.api.report.create_report
Parameters:
  - report_config: JSON configuration object
```

#### Update Report
```python
PUT /api/method/jmit_report_builder.api.report.update_report
Parameters:
  - report_name: Name of report
  - report_config: JSON configuration object
```

#### List Reports
```python
GET /api/method/jmit_report_builder.api.report.list_reports
Optional Parameters:
  - filters: JSON filter conditions
```

#### Delete Report
```python
DELETE /api/method/jmit_report_builder.api.report.delete_report
Parameters:
  - report_name: Name of report to delete
```

### Query Execution

#### Execute Query with Grouping & Subtotals
```python
POST /api/method/jmit_report_builder.api.query_engine.execute_query
Parameters:
  - query_config: {
      "query": "SELECT ...",
      "query_type": "SQL|STORED_PROCEDURE|VIEW",
      "grouping_fields": ["field1", "field2"],
      "subtotal_fields": [
        {"field": "amount", "operation": "SUM"},
        {"field": "qty", "operation": "AVG"}
      ],
      "filters": [
        {"field": "date", "operator": "=", "value": "2024-01-01"}
      ]
    }
```

#### Preview Query
```python
GET /api/method/jmit_report_builder.api.query_engine.preview_query
Parameters:
  - query: SQL query string (limited to 100 rows for preview)
```

#### Get Available Tables
```python
GET /api/method/jmit_report_builder.api.query_engine.get_available_tables
Returns: List of all database tables and views
```

#### Get Table Columns
```python
GET /api/method/jmit_report_builder.api.query_engine.get_table_columns
Parameters:
  - table_name: Name of the table
Returns: Column names and data types
```

### Export Functions

#### Export to PDF
```python
POST /api/method/jmit_report_builder.api.export.export_to_pdf
Parameters:
  - report_name: Name of report
  - data: JSON array of report data
```

#### Export to Excel
```python
POST /api/method/jmit_report_builder.api.export.export_to_excel
Parameters:
  - report_name: Name of report
  - data: JSON array of report data
```

#### Export to CSV
```python
POST /api/method/jmit_report_builder.api.export.export_to_csv
Parameters:
  - report_name: Name of report
  - data: JSON array of report data
```

## JavaScript API

### Initialize Report Builder

```javascript
// Automatically initialized on page load
// Access via global instance: jmitReportBuilder

// Create a new report
const reportConfig = {
  'report_name': 'Sales Report',
  'data_source': 'SQL Query',
  'query_type': 'SQL',
  'report_query': 'SELECT * FROM `tabSales Invoice`',
  'grouping_fields': ['customer'],
  'columns': [
    {'field_name': 'name', 'display_label': 'Invoice ID'},
    {'field_name': 'customer', 'display_label': 'Customer'},
    {'field_name': 'grand_total', 'display_label': 'Total'}
  ]
};

jmitReportBuilder.createReport(reportConfig);
```

### Load Report
```javascript
const report = await jmitReportBuilder.loadReport('Sales Report');
console.log(report);
```

### Execute Report
```javascript
const queryConfig = {
  'query': 'SELECT * FROM `tabSales Invoice` WHERE docstatus = 1',
  'query_type': 'SQL',
  'grouping_fields': ['customer'],
  'subtotal_fields': [
    {'field': 'grand_total', 'operation': 'SUM'}
  ]
};

const data = await jmitReportBuilder.executeReport(queryConfig);
```

### Export Report
```javascript
// Export to PDF
await jmitReportBuilder.exportToPDF('Sales Report');

// Export to Excel
await jmitReportBuilder.exportToExcel('Sales Report');

// Export to CSV
await jmitReportBuilder.exportToCSV('Sales Report');
```

### Render Report Table
```javascript
jmitReportBuilder.renderReportTable('container-id', reportData);
```

### Query Utilities
```javascript
// Get available tables
const tables = await jmitReportBuilder.getAvailableTables();

// Get table columns
const columns = await jmitReportBuilder.getTableColumns('tabSales Invoice');

// Preview query
const preview = await jmitReportBuilder.previewQuery('SELECT * FROM `tabSales Invoice` LIMIT 10');
```

## Report Configuration Examples

### Example 1: Sales Report with Grouping
```json
{
  "report_name": "Monthly Sales by Customer",
  "data_source": "SQL Query",
  "query_type": "SQL",
  "report_query": "SELECT DATE_FORMAT(posting_date, '%Y-%m') as month, customer, SUM(grand_total) as total, COUNT(*) as invoice_count FROM `tabSales Invoice` WHERE docstatus = 1 GROUP BY month, customer",
  "columns": [
    {"field_name": "month", "display_label": "Month", "field_type": "Date"},
    {"field_name": "customer", "display_label": "Customer", "field_type": "Text"},
    {"field_name": "total", "display_label": "Total", "field_type": "Currency"},
    {"field_name": "invoice_count", "display_label": "Count", "field_type": "Number"}
  ],
  "grouping_fields": [
    {"field_name": "month", "sort_order": "Ascending"},
    {"field_name": "customer", "sort_order": "Ascending"}
  ],
  "subtotal_config": [
    {"field": "total", "operation": "SUM"},
    {"field": "invoice_count", "operation": "SUM"}
  ]
}
```

### Example 2: Inventory Report with Filters
```json
{
  "report_name": "Warehouse Inventory Status",
  "data_source": "SQL Query",
  "query_type": "SQL",
  "report_query": "SELECT item_name, warehouse, actual_qty, reserved_qty, ordered_qty FROM `tabStock Balance` WHERE item_name LIKE %s AND warehouse = %s",
  "columns": [
    {"field_name": "item_name", "display_label": "Item"},
    {"field_name": "warehouse", "display_label": "Warehouse"},
    {"field_name": "actual_qty", "display_label": "On Hand"},
    {"field_name": "reserved_qty", "display_label": "Reserved"},
    {"field_name": "ordered_qty", "display_label": "Ordered"}
  ],
  "filters": [
    {"field_name": "item_name", "operator": "LIKE", "filter_type": "User Prompt"},
    {"field_name": "warehouse", "operator": "=", "filter_type": "User Prompt", "mandatory": true}
  ]
}
```

### Example 3: Using Stored Procedure
```json
{
  "report_name": "Customer Analysis",
  "data_source": "Stored Procedure",
  "query_type": "STORED_PROCEDURE",
  "report_query": "CALL get_customer_analytics()",
  "columns": [
    {"field_name": "customer_id", "display_label": "Customer ID"},
    {"field_name": "customer_name", "display_label": "Name"},
    {"field_name": "total_orders", "display_label": "Total Orders"},
    {"field_name": "total_spent", "display_label": "Total Spent", "field_type": "Currency"}
  ],
  "grouping_fields": [
    {"field_name": "customer_id", "sort_order": "Descending"}
  ]
}
```

## Supported Aggregate Functions

- **SUM**: Sum all values in a group
- **AVG**: Calculate average value
- **COUNT**: Count records in a group
- **MAX**: Get maximum value
- **MIN**: Get minimum value

## Filter Operators

- `=`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to
- `LIKE`: Pattern matching
- `IN`: Value in list
- `NOT IN`: Value not in list

## Troubleshooting

### Query Errors
- Ensure SQL syntax is correct
- Use backticks for table/column names: `` `table_name` ``
- Test queries in database first

### Permission Issues
- Ensure user has "Report Manager" or "System Manager" role
- Check report access permissions

### Export Issues
- Ensure data is loaded (preview the report first)
- Check sufficient disk space for file generation
- Verify column formatting is correct

### Performance
- For large datasets (>100k rows), use filters to limit results
- Consider using stored procedures for complex queries
- Create database indexes on commonly filtered fields

## Permissions

Required roles:
- **System Manager**: Full access to all reports
- **Report Manager**: Access to create and manage reports

### Assigning Permissions

```python
# Via Frappe Desk
Settings > User > [Select User] > Roles > Add "Report Manager"
```

## File Structure

```
jmit_report_builder/
├── jmit_report_builder/
│   ├── __init__.py
│   ├── hooks.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── report.py           # Report CRUD operations
│   │   ├── query_engine.py     # Query execution & grouping
│   │   ├── export.py           # Export functionality
│   │   └── session.py          # Session management
│   ├── doctype/
│   │   ├── jmit_report/        # Main report DocType
│   │   ├── jmit_report_field/  # Report columns
│   │   ├── jmit_report_filter/ # Report filters
│   │   └── jmit_report_grouping/ # Grouping configuration
│   └── public/
│       ├── js/
│       │   ├── jmit_report_builder.js  # Main JS module
│       │   └── report_designer.js      # UI components
│       └── css/
│           └── jmit_report_builder.css # Styling
├── setup.py
├── requirements.txt
└── README.md
```

## Development

### Running Tests
```bash
bench run-tests jmit_report_builder
```

### Building Documentation
```bash
# Documentation is in README.md
```

### Contributing
Pull requests welcome! Please ensure:
- Code follows PEP 8 standards
- New features include tests
- Documentation is updated

## License

MIT License - See LICENSE file

## Support

For issues, feature requests, or questions:
- GitHub Issues: https://github.com/jmittech/jmit-report-builder/issues
- Email: support@jmit.com

## Changelog

### v0.0.1 - Initial Release
- Basic report creation and management
- SQL query support
- Grouping and subtotals
- Export to PDF, Excel, CSV
- Stored procedures support
- Database views support
- Report designer UI
- Filter management

## Roadmap

- [ ] Advanced charting and visualization
- [ ] Email delivery of reports
- [ ] Report scheduling
- [ ] Collaborative report building
- [ ] Report templates
- [ ] Mobile app support
- [ ] Real-time dashboard integration
- [ ] Advanced conditional formatting

---

**JMIT Report Builder** - Making powerful reporting accessible to ERPNext users.
