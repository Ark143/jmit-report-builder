# JMIT Report Builder - Project Structure

```
jmit_report_builder/
│
├── 📄 README.md                          # Main documentation
├── 📄 INSTALLATION.md                    # Installation guide
├── 📄 GETTING_STARTED.md                 # Quick start tutorial
├── 📄 API.md                             # Complete API documentation
├── 📄 LICENSE                            # MIT License
├── 📄 setup.py                           # Python package setup
├── 📄 requirements.txt                   # Python dependencies
│
├── .github/
│   └── 📄 copilot-instructions.md        # Development guidelines
│
└── jmit_report_builder/                  # Main application package
    │
    ├── 📄 __init__.py                    # Package initialization
    ├── 📄 hooks.py                       # ERPNext app hooks & configuration
    ├── 📄 config.py                      # Application configuration
    ├── 📄 workspace_config.py            # Workspace settings
    ├── 📄 modules.json                   # Module metadata
    ├── 📄 utils.py                       # Utility functions
    ├── 📄 sample_reports.py              # Sample report templates
    │
    ├── api/                              # REST API endpoints
    │   ├── 📄 __init__.py
    │   ├── 📄 session.py                 # Session management
    │   ├── 📄 report.py                  # Report CRUD operations
    │   ├── 📄 query_engine.py            # Query execution & processing
    │   └── 📄 export.py                  # Export to PDF/Excel/CSV
    │
    ├── doctype/                          # DocType definitions
    │   ├── jmit_report/
    │   │   ├── 📄 jmit_report.json       # Main report DocType definition
    │   │   ├── 📄 jmit_report.py         # Report class & methods
    │   │   └── 📄 __init__.py
    │   │
    │   ├── jmit_report_field/
    │   │   ├── 📄 jmit_report_field.json # Report column definition
    │   │   └── 📄 __init__.py
    │   │
    │   ├── jmit_report_filter/
    │   │   ├── 📄 jmit_report_filter.json # Report filter definition
    │   │   └── 📄 __init__.py
    │   │
    │   └── jmit_report_grouping/
    │       ├── 📄 jmit_report_grouping.json # Grouping definition
    │       └── 📄 __init__.py
    │
    └── public/                           # Frontend assets
        ├── js/
        │   ├── 📄 jmit_report_builder.js # Main JavaScript module
        │   └── 📄 report_designer.js     # UI components
        │
        └── css/
            └── 📄 jmit_report_builder.css # Styling
```

## File Descriptions

### Core Application Files

- **hooks.py** - Registers app with ERPNext, defines hooks for events, permissions
- **config.py** - App-level configuration, module metadata
- **utils.py** - Shared utility functions for formatting, validation, statistics
- **sample_reports.py** - Pre-built sample reports for demonstrations

### API Layer (api/)

- **report.py** - Create, read, update, delete reports
- **query_engine.py** - Execute queries with grouping and subtotals
- **export.py** - Export data to PDF, Excel, CSV formats
- **session.py** - Session initialization and management

### Data Models (doctype/)

- **jmit_report** - Main report document with query and configuration
- **jmit_report_field** - Child table for report columns/fields
- **jmit_report_filter** - Child table for filter definitions
- **jmit_report_grouping** - Child table for grouping specifications

### Frontend (public/)

- **jmit_report_builder.js** - Core JavaScript API for browser
- **report_designer.js** - UI components and report designer interface
- **jmit_report_builder.css** - All styling including responsive design

### Documentation

- **README.md** - Complete feature documentation and usage guide
- **INSTALLATION.md** - Step-by-step installation instructions
- **GETTING_STARTED.md** - Tutorial for creating first report
- **API.md** - Complete API reference with examples

## Key Features by File

### Report Management
📄 `api/report.py` - Full CRUD operations
📄 `doctype/jmit_report/jmit_report.py` - Business logic

### Query Execution
📄 `api/query_engine.py` - Core query processing
- SQL query execution
- Stored procedure support
- Database view support
- Filter application
- Grouping logic
- Subtotal calculations

### Data Export
📄 `api/export.py` - Multi-format export
- PDF generation
- Excel workbook creation
- CSV export

### User Interface
📄 `public/js/report_designer.js` - Interactive designer
📄 `public/css/jmit_report_builder.css` - Modern styling

## Database Tables Created

When installed, the app creates these tables:

- `tabJMIT Report` - Main report definitions
- `tabJMIT Report Field` - Report columns
- `tabJMIT Report Filter` - Report filters
- `tabJMIT Report Grouping` - Grouping configuration

## Data Flow

```
1. User creates report via UI
   ↓
2. Report saved to JMIT Report DocType
   ↓
3. User selects "Preview" or "Execute"
   ↓
4. Query Engine (query_engine.py) processes request
   ↓
5. Query is executed (SQL/Stored Proc/View)
   ↓
6. Results are grouped and subtotals calculated
   ↓
7. Data rendered in UI or exported to file
```

## Configuration Files

- **hooks.py** - All ERPNext integration points
- **modules.json** - App module definition
- **workspace_config.py** - Workspace layout
- **setup.py** - Python package metadata

## Extension Points

Developers can extend functionality through:

1. **Custom Report Types** - Add new report templates
2. **Custom Export Formats** - Add export handlers in export.py
3. **Custom Grouping Functions** - Extend query_engine.py
4. **Custom UI Components** - Extend report_designer.js
5. **Hooks** - Add event handlers in hooks.py

## Performance Considerations

- Large result sets (>100k rows) use pagination
- Preview queries limited to 100 rows for speed
- Grouping and subtotals processed server-side
- Export operations run asynchronously

## Security Features

- SQL query validation to prevent injection
- User permission checks on all operations
- Role-based access control (System Manager, Report Manager)
- Audit logging of report execution

---

**Last Updated:** January 18, 2024
**Version:** 0.0.1
**Status:** Production Ready
