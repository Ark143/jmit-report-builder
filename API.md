# JMIT Report Builder - API Documentation

## Overview

The JMIT Report Builder provides a comprehensive REST API for creating, managing, and executing reports programmatically. All endpoints support JSON request/response format.

## Base URL

```
https://your-erpnext-domain/api/method/jmit_report_builder.api
```

## Authentication

All API requests require authentication via:
- **Session Cookie** (for web-based requests)
- **API Key** (for external integrations)
- **Bearer Token** (for OAuth)

### Example Header
```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

## Report API

### 1. Create Report

**Endpoint:** `POST /api/method/jmit_report_builder.api.report.create_report`

**Parameters:**
```json
{
  "report_config": {
    "report_name": "Sales Summary",
    "description": "Monthly sales analysis",
    "data_source": "SQL Query",
    "query_type": "SQL",
    "report_query": "SELECT * FROM `tabSales Invoice`",
    "columns": [...],
    "grouping_fields": [...],
    "filters": [...]
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Report created successfully",
  "report_name": "Sales Summary"
}
```

**Example cURL:**
```bash
curl -X POST https://your-site.com/api/method/jmit_report_builder.api.report.create_report \
  -H "Authorization: token YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "report_config": {
      "report_name": "Test Report",
      "query_type": "SQL",
      "report_query": "SELECT * FROM `tabCustomer` LIMIT 10"
    }
  }'
```

### 2. Get Report

**Endpoint:** `GET /api/resource/JMIT Report/{report_name}`

**Parameters:**
```
report_name: string (required)
```

**Response:**
```json
{
  "data": {
    "name": "Sales Summary",
    "report_name": "Sales Summary",
    "description": "Monthly sales analysis",
    "data_source": "SQL Query",
    "query_type": "SQL",
    "report_query": "...",
    "columns": [...],
    "grouping_fields": [...],
    "filters": [...],
    "enabled": true,
    "modified": "2024-01-18 10:30:00"
  }
}
```

**Example:**
```bash
curl https://your-site.com/api/resource/JMIT%20Report/Sales%20Summary \
  -H "Authorization: token YOUR_API_KEY"
```

### 3. List Reports

**Endpoint:** `GET /api/method/jmit_report_builder.api.report.list_reports`

**Optional Parameters:**
```json
{
  "filters": {
    "enabled": 1,
    "data_source": "SQL Query"
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "name": "Sales Summary",
      "report_name": "Sales Summary",
      "data_source": "SQL Query",
      "query_type": "SQL",
      "modified": "2024-01-18 10:30:00"
    }
  ]
}
```

### 4. Update Report

**Endpoint:** `PUT /api/method/jmit_report_builder.api.report.update_report`

**Parameters:**
```json
{
  "report_name": "Sales Summary",
  "report_config": {
    "description": "Updated description",
    "enabled": true
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Report updated successfully"
}
```

### 5. Delete Report

**Endpoint:** `DELETE /api/method/jmit_report_builder.api.report.delete_report`

**Parameters:**
```
report_name: string (required)
```

**Response:**
```json
{
  "success": true,
  "message": "Report deleted successfully"
}
```

## Query Execution API

### 1. Execute Query

**Endpoint:** `POST /api/method/jmit_report_builder.api.query_engine.execute_query`

Executes a query with grouping, subtotals, and filters.

**Parameters:**
```json
{
  "query_config": {
    "query": "SELECT * FROM `tabSales Invoice` WHERE docstatus = 1",
    "query_type": "SQL",
    "grouping_fields": ["customer", "posting_date"],
    "subtotal_fields": [
      {"field": "grand_total", "operation": "SUM"},
      {"field": "name", "operation": "COUNT"}
    ],
    "filters": [
      {
        "field": "posting_date",
        "operator": ">=",
        "value": "2024-01-01"
      },
      {
        "field": "customer",
        "operator": "=",
        "value": "CUST-001"
      }
    ]
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "customer": "ABC Corp",
      "posting_date": "2024-01-01",
      "grand_total": 10000,
      "name": 5,
      "_type": "GROUP_HEADER"
    },
    {
      "customer": "ABC Corp",
      "posting_date": "2024-01-01",
      "grand_total": 5000,
      "name": "INV-001"
    },
    {
      "customer": "ABC Corp",
      "posting_date": "2024-01-01",
      "grand_total": 5000,
      "_type": "SUBTOTAL",
      "grand_total_subtotal": 10000,
      "name_subtotal": 2
    }
  ],
  "count": 150
}
```

**Aggregate Operations:**
- `SUM`: Sum of values
- `AVG`: Average value
- `COUNT`: Record count
- `MAX`: Maximum value
- `MIN`: Minimum value

**Filter Operators:**
- `=`: Equal
- `!=`: Not equal
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal
- `<=`: Less than or equal
- `LIKE`: Pattern match
- `IN`: Value in list
- `NOT IN`: Value not in list

### 2. Preview Query

**Endpoint:** `GET /api/method/jmit_report_builder.api.query_engine.preview_query`

Returns first 10 rows for query validation.

**Parameters:**
```
query: string (required) - SQL query
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "name": "INV-001",
      "customer": "ABC Corp",
      "grand_total": 5000
    },
    {
      "name": "INV-002",
      "customer": "ABC Corp",
      "grand_total": 5000
    }
  ],
  "total_count": 150
}
```

**Example:**
```bash
curl "https://your-site.com/api/method/jmit_report_builder.api.query_engine.preview_query?query=SELECT%20*%20FROM%20%60tabCustomer%60%20LIMIT%2010" \
  -H "Authorization: token YOUR_API_KEY"
```

### 3. Get Available Tables

**Endpoint:** `GET /api/method/jmit_report_builder.api.query_engine.get_available_tables`

**Response:**
```json
{
  "success": true,
  "data": [
    "tabCustomer",
    "tabSales Invoice",
    "tabSales Invoice Item",
    "tabItem",
    "tabWarehouse",
    ...
  ]
}
```

### 4. Get Table Columns

**Endpoint:** `GET /api/method/jmit_report_builder.api.query_engine.get_table_columns`

**Parameters:**
```
table_name: string (required)
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "COLUMN_NAME": "name",
      "DATA_TYPE": "varchar",
      "IS_NULLABLE": "NO"
    },
    {
      "COLUMN_NAME": "customer",
      "DATA_TYPE": "varchar",
      "IS_NULLABLE": "NO"
    },
    {
      "COLUMN_NAME": "grand_total",
      "DATA_TYPE": "decimal",
      "IS_NULLABLE": "YES"
    }
  ]
}
```

## Export API

### 1. Export to PDF

**Endpoint:** `POST /api/method/jmit_report_builder.api.export.export_to_pdf`

**Parameters:**
```json
{
  "report_name": "Sales Summary",
  "data": [
    {"name": "INV-001", "customer": "ABC Corp", "amount": 5000},
    {"name": "INV-002", "customer": "ABC Corp", "amount": 5000}
  ]
}
```

**Response:**
```json
{
  "success": true,
  "file_type": "pdf",
  "data": "base64_encoded_pdf_content"
}
```

### 2. Export to Excel

**Endpoint:** `POST /api/method/jmit_report_builder.api.export.export_to_excel`

**Parameters:**
```json
{
  "report_name": "Sales Summary",
  "data": [...]
}
```

**Response:**
```json
{
  "success": true,
  "file_type": "xlsx",
  "filename": "Sales Summary_20240118_103000.xlsx"
}
```

### 3. Export to CSV

**Endpoint:** `POST /api/method/jmit_report_builder.api.export.export_to_csv`

**Parameters:**
```json
{
  "report_name": "Sales Summary",
  "data": [...]
}
```

**Response:**
```json
{
  "success": true,
  "file_type": "csv",
  "filename": "Sales Summary_20240118_103000.csv",
  "content": "name,customer,amount\nINV-001,ABC Corp,5000\n..."
}
```

## Error Handling

All API endpoints return standard error responses:

```json
{
  "success": false,
  "message": "Error description",
  "exception": "ExceptionType"
}
```

**Common HTTP Status Codes:**
- `200`: Success
- `400`: Bad Request (invalid parameters)
- `401`: Unauthorized (missing/invalid authentication)
- `403`: Forbidden (insufficient permissions)
- `404`: Not Found (resource doesn't exist)
- `500`: Server Error

## Rate Limiting

API requests are rate-limited to prevent abuse:
- **Default**: 100 requests per minute per user
- **Bulk Operations**: Contact support for higher limits

## Pagination

For list endpoints, use standard pagination:

```
?limit_page_length=50&limit_start=0
```

## Sorting

Sort list results by field:

```
?order_by=modified desc
```

## Code Examples

### Python

```python
import requests
import json

BASE_URL = "https://your-site.com"
API_KEY = "your_api_key"

headers = {
    "Authorization": f"token {API_KEY}",
    "Content-Type": "application/json"
}

# Create report
payload = {
    "report_config": {
        "report_name": "API Test Report",
        "query_type": "SQL",
        "report_query": "SELECT * FROM `tabCustomer` LIMIT 10"
    }
}

response = requests.post(
    f"{BASE_URL}/api/method/jmit_report_builder.api.report.create_report",
    headers=headers,
    json=payload
)

print(response.json())
```

### JavaScript

```javascript
const apiKey = 'your_api_key';
const baseUrl = 'https://your-site.com';

const queryConfig = {
  query: "SELECT * FROM `tabSales Invoice` WHERE docstatus = 1",
  query_type: "SQL",
  grouping_fields: ["customer"],
  subtotal_fields: [
    {field: "grand_total", operation: "SUM"}
  ]
};

fetch(`${baseUrl}/api/method/jmit_report_builder.api.query_engine.execute_query`, {
  method: 'POST',
  headers: {
    'Authorization': `token ${apiKey}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({query_config: queryConfig})
})
.then(r => r.json())
.then(data => console.log(data));
```

### PHP

```php
<?php
$apiKey = 'your_api_key';
$baseUrl = 'https://your-site.com';

$config = [
    'report_name' => 'PHP Test Report',
    'query_type' => 'SQL',
    'report_query' => 'SELECT * FROM `tabCustomer`'
];

$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => "$baseUrl/api/method/jmit_report_builder.api.report.create_report",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: token ' . $apiKey,
        'Content-Type: application/json'
    ],
    CURLOPT_POSTFIELDS => json_encode(['report_config' => $config])
]);

$response = curl_exec($ch);
$result = json_decode($response, true);
print_r($result);
?>
```

## Best Practices

1. **Always validate input** before sending to API
2. **Use filters** to limit data returned
3. **Cache results** to reduce API calls
4. **Handle errors gracefully** with try-catch blocks
5. **Use appropriate timeouts** for long-running queries
6. **Document API keys** securely (never commit to version control)
7. **Log API calls** for debugging purposes
8. **Test with preview** before running full queries

## Changelog

### v0.0.1
- Initial API release
- Report CRUD operations
- Query execution with grouping/subtotals
- Export functionality
- Filter and search support

## Support

For API support:
- Email: api-support@jmit.com
- Documentation: https://docs.jmit.com/report-builder
- GitHub Issues: https://github.com/jmittech/jmit-report-builder/issues
