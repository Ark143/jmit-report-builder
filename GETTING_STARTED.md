# JMIT Report Builder - Getting Started Guide

## Your First Report - Step by Step

In this guide, we'll create a simple **Monthly Sales by Customer** report.

### Step 1: Create a New Report

1. Go to **JMIT Report Builder** → **Reports**
2. Click **+ New**
3. Fill in the report details:

```
Report Name: Monthly Sales Report
Description: Sales analysis by customer with monthly breakdown
Data Source Type: SQL Query
Query Type: SQL
```

### Step 2: Write Your Query

In the **Report Query** field, paste this SQL query:

```sql
SELECT 
    MONTH(si.posting_date) as month,
    YEAR(si.posting_date) as year,
    si.customer,
    si.customer_name,
    COUNT(si.name) as invoice_count,
    SUM(si.grand_total) as total_sales,
    AVG(si.grand_total) as avg_invoice
FROM `tabSales Invoice` si
WHERE si.docstatus = 1
GROUP BY YEAR(si.posting_date), MONTH(si.posting_date), si.customer
ORDER BY year DESC, month DESC, si.customer ASC
```

Click **Preview Query** to see sample data.

### Step 3: Add Report Columns

Click **Add Column** multiple times to add these columns:

| Field Name | Display Label | Field Type | Width | Alignment |
|---|---|---|---|---|
| month | Month | Number | 10 | Center |
| year | Year | Number | 10 | Center |
| customer | Customer | Text | 15 | Left |
| customer_name | Customer Name | Text | 25 | Left |
| invoice_count | # of Invoices | Number | 12 | Right |
| total_sales | Total Sales | Currency | 15 | Right |
| avg_invoice | Avg Invoice | Currency | 15 | Right |

### Step 4: Setup Grouping

Click **Add Grouping** and add:

1. Field: `year` → Sort Order: **Descending**
2. Field: `month` → Sort Order: **Descending**
3. Field: `customer` → Sort Order: **Ascending**

### Step 5: Configure Subtotals

In the **Subtotal Configuration** field, paste this JSON:

```json
[
  {"field": "invoice_count", "operation": "SUM"},
  {"field": "total_sales", "operation": "SUM"},
  {"field": "avg_invoice", "operation": "AVG"}
]
```

### Step 6: Add Filters (Optional)

Click **Add Filter** to add:

| Field Name | Operator | Filter Value | Filter Type |
|---|---|---|---|
| customer | = | (leave empty) | User Prompt |

This allows the report user to filter by specific customer.

### Step 7: Save Report

1. Click **Save**
2. You'll be redirected to the saved report

### Step 8: Run the Report

1. Open the report you just created
2. If you added filters, fill in the filter values
3. Click **Preview** button
4. The report will display with grouping and subtotals!

### Step 9: Export Results

1. Click **Export** button
2. Choose format: **PDF**, **Excel**, or **CSV**
3. File will be downloaded automatically

## Understanding the Output

Your report will show:

### Group Header Rows
- Highlighted in blue
- Shows the grouping values (Year, Month, Customer)
- Indicates the record count in that group

### Data Rows
- Regular data rows with all column values

### Subtotal Rows
- Highlighted in gray
- Shows:
  - Sum of invoice counts
  - Sum of total sales
  - Average invoice amount

### Example Output Structure:
```
2024 | 01 | CUST-001 | ABC Corp        | 5 | $50,000 | $10,000
                                    [Data rows...]
SUBTOTAL:                           | 5 | $50,000 | $10,000

2024 | 01 | CUST-002 | XYZ Ltd         | 3 | $30,000 | $10,000
                                    [Data rows...]
SUBTOTAL:                           | 3 | $30,000 | $10,000

GRAND TOTAL:                        | 8 | $80,000 | $10,000
```

## Common Report Types

### 1. Inventory Report

```sql
SELECT 
    item.name as item_code,
    bin.warehouse,
    bin.actual_qty,
    bin.reserved_qty,
    (bin.actual_qty - bin.reserved_qty) as available
FROM `tabBin` bin
JOIN `tabItem` item ON bin.item_code = item.name
```

### 2. Purchase Report

```sql
SELECT 
    po.name,
    po.supplier,
    po.posting_date,
    po.grand_total
FROM `tabPurchase Order` po
WHERE po.docstatus = 1
```

### 3. Customer Report

```sql
SELECT 
    customer.name,
    customer.customer_name,
    COUNT(si.name) as total_invoices,
    SUM(si.grand_total) as total_value
FROM `tabCustomer` customer
LEFT JOIN `tabSales Invoice` si ON customer.name = si.customer
GROUP BY customer.name
```

## Tips & Tricks

### 1. Use Backticks for Table Names
```sql
-- ✓ Correct
SELECT * FROM `tabSales Invoice`

-- ✗ Wrong
SELECT * FROM tabSales Invoice
```

### 2. Filter by Date Range
```sql
WHERE si.posting_date BETWEEN '2024-01-01' AND '2024-12-31'
```

### 3. Using LIKE for Text Search
```sql
WHERE si.customer_name LIKE '%ABC%'
```

### 4. Combining Multiple Groups
```
Grouping 1: company
Grouping 2: branch
Grouping 3: department
```

### 5. Multiple Subtotal Operations
```json
[
  {"field": "qty", "operation": "SUM"},
  {"field": "amount", "operation": "SUM"},
  {"field": "rate", "operation": "AVG"},
  {"field": "id", "operation": "COUNT"}
]
```

## Frequently Asked Questions

### Q: Why is my query returning no results?

**A:** 
- Check if table name spelling is correct with backticks
- Verify WHERE conditions
- Test query in database directly
- Check docstatus (usually 1 for submitted documents)

### Q: How do I include all records even with 0 amounts?

**A:** Use LEFT JOIN instead of JOIN:
```sql
LEFT JOIN `tabSales Invoice` si ON customer.name = si.customer
```

### Q: Can I use multiple tables?

**A:** Yes! Join them in your query:
```sql
SELECT *
FROM `tabSales Invoice` si
JOIN `tabCustomer` c ON si.customer = c.name
JOIN `tabSalesInvoiceItem` ii ON si.name = ii.parent
```

### Q: How do I format currency values?

**A:** Set Field Type to **Currency** in column configuration:
```
Field Name: grand_total
Field Type: Currency
Format: ###,##0.00
```

### Q: Can I use stored procedures?

**A:** Yes! Set Data Source to **Stored Procedure** and enter the procedure name.

## Next Steps

1. ✅ Create your first report (you just did!)
2. 📚 Read [README.md](../README.md) for full documentation
3. 🚀 Explore advanced features like stored procedures
4. 📊 Create dashboards with report data
5. 📧 Schedule reports for email delivery

## Need Help?

- Check [README.md](../README.md) for comprehensive documentation
- Review [API.md](API.md) for developer documentation
- Search existing reports for examples
- Contact support@jmit.com

Happy reporting! 📊
