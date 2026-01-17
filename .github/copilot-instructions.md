# JMIT Report Builder - ERPNext App Development

## Project Overview
JMIT Report Builder is a Crystal Report clone integrated with ERPNext v15, providing advanced reporting capabilities with grouping, subtotals, stored procedures, and SQL views support.

## Key Features
- Advanced report designer with drag-and-drop interface
- Grouping and sub-total calculations
- Support for stored procedures and SQL views
- Database query builder
- Export to multiple formats (PDF, Excel, CSV)
- Real-time report preview
- User-friendly UI similar to Crystal Reports

## Development Progress

- [x] Project scaffolding
- [x] Directory structure creation
- [ ] DocType definitions
- [ ] Report builder backend logic
- [ ] Database/SQL utilities
- [ ] Frontend UI components
- [ ] API endpoints
- [ ] Testing and validation

## Architecture

### Backend (Python/Frappe)
- **api/**: REST API endpoints for report operations
- **doctype/**: Custom DocTypes for report definitions and configurations
- **utils/**: Helper functions for SQL, grouping, and subtotals

### Frontend (JavaScript/HTML/CSS)
- **public/js/**: Report builder UI and logic
- **public/css/**: Styling components

## Building and Running
```bash
cd jmit_report_builder
bench get-app jmit_report_builder .
bench install-app jmit_report_builder
bench start
```

## Documentation
See README.md for detailed setup and usage instructions.
