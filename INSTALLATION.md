# JMIT Report Builder - Installation Guide

## Prerequisites

- **ERPNext v15** or later
- **Frappe Framework** v15
- **Python** 3.8 or higher
- **MySQL** or **MariaDB** 5.7+
- **Bench** installed and initialized

## Installation Steps

### Step 1: Clone or Download the App

```bash
# Option A: Clone from GitHub
cd /path/to/your/bench
bench get-app jmit-report-builder https://github.com/jmittech/jmit-report-builder.git

# Option B: Or add from local path
bench get-app jmit_report_builder /path/to/jmit_report_builder
```

### Step 2: Install the App

```bash
bench install-app jmit_report_builder
```

### Step 3: Run Migrations

```bash
bench migrate
```

### Step 4: Build Front-end Assets

```bash
bench build
```

### Step 5: Start Bench

```bash
bench start
```

## Post-Installation

### 1. Create Sample Reports (Optional)

```python
# In bench console
bench console
# Then run:
from jmit_report_builder.sample_reports import create_sample_reports
create_sample_reports()
```

### 2. Assign Permissions

1. Go to **Settings** → **User** → Select User
2. Add role **"Report Manager"** to user (or keep **System Manager**)
3. Save and reload page

### 3. Access Report Builder

1. Go to **Search** or **Awesome Bar** (Ctrl+K)
2. Search for **"JMIT Report"**
3. Click on **New** to create your first report

## Verify Installation

### Check if App is Installed

```bash
bench list-apps
```

You should see `jmit_report_builder` in the list.

### Check Database Tables

```bash
# In MySQL/MariaDB console
SHOW TABLES LIKE 'tabJMIT%';
```

You should see:
- `tabJMIT Report`
- `tabJMIT Report Field`
- `tabJMIT Report Filter`
- `tabJMIT Report Grouping`

### Access via Browser

1. Open ERPNext Desk
2. Go to **JMIT Report Builder** module
3. You should see **Reports** list

## Troubleshooting

### App Not Appearing

```bash
# Clear cache
bench clear-cache

# Restart
bench restart
```

### Database Errors

```bash
# Reset app database
bench reinstall-app jmit_report_builder
```

### Permission Issues

- Ensure user has **System Manager** or **Report Manager** role
- Check role assignment in **Settings** → **User**

### Query Errors

- Test SQL queries in database directly first
- Ensure correct table and column names with backticks
- Check user database permissions

## Uninstallation

```bash
bench uninstall-app jmit_report_builder
```

## Updating

```bash
# Pull latest changes
cd apps/jmit_report_builder
git pull origin main

# Migrate if needed
cd /path/to/bench
bench migrate

# Rebuild
bench build

# Restart
bench restart
```

## Support

For issues during installation:
1. Check error messages carefully
2. Review logs in `bench_folder/logs/`
3. Check GitHub issues
4. Contact support@jmit.com

## Next Steps

After installation, check out:
- [README.md](../README.md) - Full documentation
- [Getting Started Guide](GETTING_STARTED.md) - Tutorial for first report
- [API Documentation](API.md) - For developers
