## JMIT Report Builder - Quick Reference Card

### 🎯 Core Concepts

| Concept | Description |
|---------|-------------|
| **Report** | Main document containing query and configuration |
| **Query** | SQL, stored procedure, or view |
| **Columns** | Fields to display in report output |
| **Grouping** | Group results by one or more fields |
| **Subtotal** | Aggregate calculation per group (SUM, AVG, etc.) |
| **Filters** | Conditions to limit data returned |
| **Export** | Download report as PDF, Excel, or CSV |

---

### 📊 Aggregate Operations

| Operation | Use Case | Example |
|-----------|----------|---------|
| **SUM** | Total values | Total sales amount |
| **AVG** | Average value | Average invoice size |
| **COUNT** | Record count | Number of invoices |
| **MAX** | Maximum value | Highest order amount |
| **MIN** | Minimum value | Lowest order amount |

---

### 🔍 Filter Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equal | customer = 'ABC Corp' |
| `!=` | Not equal | status != 'Cancelled' |
| `>` | Greater than | amount > 1000 |
| `<` | Less than | date < '2024-01-01' |
| `>=` | Greater or equal | qty >= 10 |
| `<=` | Less or equal | price <= 100 |
| `LIKE` | Pattern match | name LIKE '%Smith%' |
| `IN` | In list | status IN ('Active','Pending') |
| `NOT IN` | Not in list | category NOT IN ('Test','Draft') |

---

### 📝 Common SQL Queries

**Customer Sales Report**
```sql
SELECT customer, SUM(amount) as total, COUNT(*) as count
FROM `tabSales Invoice`
WHERE docstatus = 1
GROUP BY customer
```

**Inventory Status**
```sql
SELECT item_code, warehouse, actual_qty, reserved_qty
FROM `tabBin`
WHERE actual_qty > 0
ORDER BY warehouse, item_code
```

**Purchase Analysis**
```sql
SELECT supplier, posting_date, grand_total
FROM `tabPurchase Order`
WHERE docstatus = 1
ORDER BY supplier, posting_date
```

---

### 🚀 Quick Start

1. **Create Report**
   - Go to JMIT Report → New
   - Enter report name
   - Select data source type

2. **Write Query**
   - Enter SQL/procedure/view
   - Click Preview Query
   - Verify results

3. **Configure Output**
   - Add columns
   - Set grouping
   - Add subtotals
   - Set filters

4. **Save & Run**
   - Click Save
   - Open report
   - Click Preview
   - Export if needed

---

### 💻 JavaScript API Examples

**Create Report**
```javascript
await jmitReportBuilder.createReport({
  report_name: 'My Report',
  query_type: 'SQL',
  report_query: 'SELECT * FROM `tabCustomer`'
});
```

**Execute Report**
```javascript
const data = await jmitReportBuilder.executeReport({
  query: 'SELECT * FROM `tabSales Invoice`',
  grouping_fields: ['customer'],
  subtotal_fields: [{field: 'grand_total', operation: 'SUM'}]
});
```

**Export Report**
```javascript
await jmitReportBuilder.exportToPDF('My Report');
await jmitReportBuilder.exportToExcel('My Report');
await jmitReportBuilder.exportToCSV('My Report');
```

---

### 🔌 REST API Quick Commands

**Create Report**
```bash
curl -X POST https://your-site.com/api/method/jmit_report_builder.api.report.create_report \
  -H "Authorization: token API_KEY" \
  -d '{"report_config": {...}}'
```

**Execute Query**
```bash
curl -X POST https://your-site.com/api/method/jmit_report_builder.api.query_engine.execute_query \
  -H "Authorization: token API_KEY" \
  -d '{"query_config": {...}}'
```

**Get Tables**
```bash
curl https://your-site.com/api/method/jmit_report_builder.api.query_engine.get_available_tables \
  -H "Authorization: token API_KEY"
```

---

### 📐 Report Configuration Template

```json
{
  "report_name": "My Report",
  "description": "Report description",
  "data_source": "SQL Query",
  "query_type": "SQL",
  "report_query": "SELECT * FROM `table`",
  "columns": [
    {"field_name": "name", "display_label": "Name"}
  ],
  "grouping_fields": [
    {"field_name": "category", "sort_order": "Ascending"}
  ],
  "subtotal_config": [
    {"field": "amount", "operation": "SUM"}
  ],
  "filters": [
    {"field_name": "status", "operator": "=", "filter_type": "Static"}
  ],
  "enabled": true
}
```

---

### 🎨 CSS Classes

| Class | Purpose |
|-------|---------|
| `.report-designer` | Main container |
| `.designer-header` | Header section |
| `.designer-body` | Body content |
| `.group-header` | Group header row |
| `.subtotal` | Subtotal row |
| `.form-group` | Form field |
| `.btn` | Button |
| `.panel` | Panel container |

---

### ⚙️ Configuration Files

| File | Purpose |
|------|---------|
| `hooks.py` | ERPNext integration |
| `config.py` | App configuration |
| `modules.json` | Module metadata |
| `utils.py` | Utility functions |

---

### 🔐 Permissions

| Role | Can Do |
|------|--------|
| **System Manager** | Everything |
| **Report Manager** | Create/edit/delete/run reports |
| **Other Users** | View only (if granted) |

---

### 📂 File Locations

| Item | Path |
|------|------|
| Main code | `jmit_report_builder/` |
| API endpoints | `jmit_report_builder/api/` |
| Data models | `jmit_report_builder/doctype/` |
| Frontend JS | `jmit_report_builder/public/js/` |
| Styles | `jmit_report_builder/public/css/` |
| Docs | Root directory `.md` files |

---

### 🐛 Troubleshooting Quick Fixes

| Issue | Solution |
|-------|----------|
| Query errors | Test in database first |
| No data | Check WHERE conditions |
| Permission denied | Assign Report Manager role |
| Slow report | Add LIMIT clause, use filters |
| Table not found | Use backticks: `` `tabName` `` |

---

### 📚 Documentation Map

| Need | See File |
|------|----------|
| Setup instructions | INSTALLATION.md |
| First report tutorial | GETTING_STARTED.md |
| API reference | API.md |
| Full features | README.md |
| Project structure | PROJECT_STRUCTURE.md |
| This reference | QUICK_REFERENCE.md |

---

### 🎯 Report Design Best Practices

✅ **DO**
- Use backticks for table names
- Test queries before saving
- Name columns descriptively
- Start simple, add complexity
- Use filters to limit data
- Document report purpose

❌ **DON'T**
- Use DELETE/DROP in queries
- Skip WHERE conditions
- Create too many grouping levels
- Forget to save changes
- Use generic names like "Report"
- Over-complicate queries

---

### 💡 Pro Tips

1. **Preview Early** - Always preview query before adding grouping
2. **Use Filters** - Reduce data with filters for performance
3. **Group Wisely** - Max 3-4 grouping levels for readability
4. **Name Clearly** - Use descriptive field labels
5. **Export Often** - Practice exporting to ensure formatting works
6. **Clone Reports** - Use sample reports as templates
7. **Test Subtotals** - Verify subtotal calculations are correct

---

### 🚦 Getting Help

1. Read the main **README.md**
2. Check **GETTING_STARTED.md** for tutorials
3. Review **API.md** for developer docs
4. Check **INSTALLATION.md** for setup issues
5. Search existing reports for examples

---

**JMIT Report Builder v0.0.1** | MIT License | [Documentation](README.md)
