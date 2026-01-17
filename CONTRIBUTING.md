# Contributing to JMIT Report Builder

Thank you for your interest in contributing to JMIT Report Builder! We welcome contributions from the community.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## How to Contribute

### Reporting Bugs

Before creating a bug report, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**
- **Include your environment details** (OS, Python version, ERPNext version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and expected behavior**
- **Explain why this enhancement would be useful**

### Pull Requests

- Fill in the required template
- Follow the Python/JavaScript style guides
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

## Development Setup

### Prerequisites

- Python 3.8+
- ERPNext v15+
- Frappe Framework v15+
- MySQL/MariaDB 5.7+
- Git

### Local Development

1. **Fork the repository**
   ```bash
   # On GitHub, click "Fork"
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/jmit-report-builder.git
   cd jmit-report-builder
   ```

3. **Create a development branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

4. **Set up development environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

5. **Make your changes**
   - Write your code
   - Follow the style guide
   - Add tests for new features
   - Update documentation

6. **Test your changes**
   ```bash
   # Run tests
   bench run-tests jmit_report_builder
   ```

7. **Commit your changes**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

8. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Create a Pull Request**
   - Go to GitHub
   - Click "New Pull Request"
   - Fill in the template
   - Submit for review

## Style Guides

### Python Style Guide

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines:

```python
# Good
def calculate_subtotal(records, field_name, operation):
    """Calculate subtotal for records."""
    if operation == 'SUM':
        return sum(r.get(field_name, 0) for r in records)
    return 0

# Bad
def calc_sub(records, field, op):
    if op == 'SUM':
        return sum([r.get(field, 0) for r in records])
    return 0
```

**Guidelines:**
- Use descriptive variable names
- Write docstrings for functions and classes
- Keep lines under 79 characters (100 for comments)
- Use 4 spaces for indentation
- Use meaningful comments

### JavaScript Style Guide

Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript):

```javascript
// Good
class ReportBuilder {
  constructor(containerId) {
    this.container = $(`#${containerId}`);
    this.reportConfig = {};
  }

  async executeReport(queryConfig) {
    try {
      const response = await this.callApi(queryConfig);
      return response.data;
    } catch (error) {
      console.error('Report execution failed:', error);
      throw error;
    }
  }
}

// Bad
class reportbuilder {
  constructor(id) {
    this.cont = $(id);
    this.cfg = {};
  }
  execute(config) {
    return this.callApi(config);
  }
}
```

**Guidelines:**
- Use `const` by default, `let` when needed
- Use arrow functions `=>`
- Use meaningful variable names
- Add JSDoc comments for complex functions
- Use template literals for strings

### SQL Query Guidelines

```sql
-- Good: Clear, readable, commented
SELECT 
    si.name as invoice_id,
    si.customer,
    SUM(si.grand_total) as total_amount
FROM `tabSales Invoice` si
WHERE si.docstatus = 1
GROUP BY si.customer
ORDER BY total_amount DESC

-- Bad: Hard to read
SELECT name, customer, grand_total FROM tabSalesInvoice WHERE docstatus=1
```

**Guidelines:**
- Use backticks for table/column names
- Use aliases for clarity
- Format with proper indentation
- Add comments for complex logic

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

**Types:**
- `feat:` A new feature
- `fix:` A bug fix
- `docs:` Documentation only changes
- `style:` Changes that don't affect code meaning
- `refactor:` Code change that neither fixes a bug nor adds a feature
- `perf:` Code change that improves performance
- `test:` Adding or updating tests
- `chore:` Changes to build process, dependencies, etc.

**Examples:**
```
feat: add export to CSV functionality
fix: prevent SQL injection in query builder
docs: update API documentation
refactor: simplify grouping logic
test: add unit tests for query engine
chore: update dependencies
```

## Testing

### Writing Tests

```python
# test_query_engine.py
import frappe
from jmit_report_builder.api.query_engine import apply_grouping_and_subtotals

def test_grouping_and_subtotals():
    """Test grouping and subtotal calculation."""
    data = [
        {'customer': 'A', 'amount': 100},
        {'customer': 'A', 'amount': 200},
        {'customer': 'B', 'amount': 150}
    ]
    
    result = apply_grouping_and_subtotals(
        data,
        ['customer'],
        [{'field': 'amount', 'operation': 'SUM'}]
    )
    
    assert len(result) > 0
    assert any(r.get('_type') == 'GROUP_HEADER' for r in result)
    assert any(r.get('_type') == 'SUBTOTAL' for r in result)
```

### Running Tests

```bash
# Run all tests
bench run-tests jmit_report_builder

# Run specific test
bench run-tests jmit_report_builder.api.test_query_engine
```

## Documentation

- Update README.md for feature additions
- Update API.md for API changes
- Add docstrings to all functions
- Include examples in documentation
- Update CHANGELOG.md

## Review Process

1. **Code Review**
   - At least one maintainer review required
   - All tests must pass
   - No merge conflicts

2. **Feedback**
   - Be respectful and constructive
   - Suggest improvements positively
   - Discuss trade-offs

3. **Approval & Merge**
   - PR approved by maintainers
   - Branch squashed and merged
   - Feature branch deleted

## Release Process

1. Update version in:
   - `jmit_report_builder/__init__.py`
   - `setup.py`
   - `README.md`

2. Update CHANGELOG.md with changes

3. Create git tag:
   ```bash
   git tag -a v0.0.2 -m "Release version 0.0.2"
   git push origin v0.0.2
   ```

4. Create GitHub Release with changelog

5. Update PyPI package (for maintainers)

## Additional Notes

### Performance Considerations

- Optimize queries for large datasets
- Cache results when appropriate
- Minimize database calls
- Test with realistic data volumes

### Security Considerations

- Always validate user input
- Prevent SQL injection
- Check permissions before operations
- Don't commit sensitive data
- Use environment variables for secrets

### Documentation Considerations

- Keep documentation up to date
- Include code examples
- Add troubleshooting sections
- Document edge cases
- Provide clear error messages

## Questions?

- Open an issue with the `question` label
- Email: support@jmit.com
- Check existing documentation

## License

By contributing to JMIT Report Builder, you agree that your contributions will be licensed under its MIT License.

---

Thank you for contributing to JMIT Report Builder! 🎉
