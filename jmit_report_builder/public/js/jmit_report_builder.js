/**
 * JMIT Report Builder - Main JavaScript Module
 * Crystal Report-like report builder for ERPNext v15
 */

class JMITReportBuilder {
	constructor() {
		this.currentReport = null;
		this.reportData = null;
		this.init();
	}

	init() {
		console.log('JMIT Report Builder initialized');
		this.setupEventListeners();
	}

	setupEventListeners() {
		// Setup global event listeners if needed
		document.addEventListener('jmit:report-loaded', (e) => {
			this.onReportLoaded(e.detail);
		});
	}

	/**
	 * Create a new report
	 */
	async createReport(reportConfig) {
		try {
			const response = await frappe.call({
				method: 'jmit_report_builder.api.report.create_report',
				args: {
					report_config: JSON.stringify(reportConfig)
				},
				async: false
			});

			if (response.message && response.message.success) {
				frappe.msgprint('Report created successfully');
				return response.message;
			} else {
				frappe.throw('Failed to create report');
			}
		} catch (error) {
			frappe.throw(`Error creating report: ${error.message}`);
		}
	}

	/**
	 * Load report for editing
	 */
	async loadReport(reportName) {
		try {
			const response = await frappe.call({
				method: 'jmit_report_builder.api.report.get_report',
				args: {
					report_name: reportName
				},
				async: false
			});

			if (response.message && response.message.success) {
				this.currentReport = response.message.data;
				return this.currentReport;
			}
		} catch (error) {
			frappe.throw(`Error loading report: ${error.message}`);
		}
	}

	/**
	 * Execute report query
	 */
	async executeReport(queryConfig) {
		try {
			const response = await frappe.call({
				method: 'jmit_report_builder.api.query_engine.execute_query',
				args: {
					query_config: JSON.stringify(queryConfig)
				},
				async: true
			});

			if (response.message && response.message.success) {
				this.reportData = response.message.data;
				return this.reportData;
			} else {
				frappe.throw('Failed to execute query');
			}
		} catch (error) {
			frappe.throw(`Query execution error: ${error.message}`);
		}
	}

	/**
	 * Preview query
	 */
	async previewQuery(query) {
		try {
			const response = await frappe.call({
				method: 'jmit_report_builder.api.query_engine.preview_query',
				args: {
					query: query
				},
				async: false
			});

			if (response.message && response.message.success) {
				return response.message.data;
			}
		} catch (error) {
			frappe.throw(`Preview error: ${error.message}`);
		}
	}

	/**
	 * Get available tables
	 */
	async getAvailableTables() {
		try {
			const response = await frappe.call({
				method: 'jmit_report_builder.api.query_engine.get_available_tables',
				async: false
			});

			if (response.message && response.message.success) {
				return response.message.data;
			}
		} catch (error) {
			frappe.throw(`Error fetching tables: ${error.message}`);
		}
	}

	/**
	 * Get table columns
	 */
	async getTableColumns(tableName) {
		try {
			const response = await frappe.call({
				method: 'jmit_report_builder.api.query_engine.get_table_columns',
				args: {
					table_name: tableName
				},
				async: false
			});

			if (response.message && response.message.success) {
				return response.message.data;
			}
		} catch (error) {
			frappe.throw(`Error fetching columns: ${error.message}`);
		}
	}

	/**
	 * Export report to PDF
	 */
	async exportToPDF(reportName) {
		try {
			const response = await frappe.call({
				method: 'jmit_report_builder.api.export.export_to_pdf',
				args: {
					report_name: reportName,
					data: JSON.stringify(this.reportData)
				},
				async: true
			});

			if (response.message && response.message.success) {
				frappe.msgprint('PDF exported successfully');
				return response.message;
			}
		} catch (error) {
			frappe.throw(`PDF export error: ${error.message}`);
		}
	}

	/**
	 * Export report to Excel
	 */
	async exportToExcel(reportName) {
		try {
			const response = await frappe.call({
				method: 'jmit_report_builder.api.export.export_to_excel',
				args: {
					report_name: reportName,
					data: JSON.stringify(this.reportData)
				},
				async: true
			});

			if (response.message && response.message.success) {
				frappe.msgprint('Excel exported successfully');
				return response.message;
			}
		} catch (error) {
			frappe.throw(`Excel export error: ${error.message}`);
		}
	}

	/**
	 * Export report to CSV
	 */
	async exportToCSV(reportName) {
		try {
			const response = await frappe.call({
				method: 'jmit_report_builder.api.export.export_to_csv',
				args: {
					report_name: reportName,
					data: JSON.stringify(this.reportData)
				},
				async: true
			});

			if (response.message && response.message.success) {
				frappe.msgprint('CSV exported successfully');
				return response.message;
			}
		} catch (error) {
			frappe.throw(`CSV export error: ${error.message}`);
		}
	}

	/**
	 * Render report data as table
	 */
	renderReportTable(containerId, data) {
		if (!data || data.length === 0) {
			$(`#${containerId}`).html('<p>No data available</p>');
			return;
		}

		let html = '<table class="table table-striped table-hover"><thead><tr>';
		
		// Headers
		const headers = Object.keys(data[0]);
		headers.forEach(header => {
			if (!header.startsWith('_')) {
				html += `<th>${header}</th>`;
			}
		});
		html += '</tr></thead><tbody>';

		// Data rows
		data.forEach(row => {
			if (row._type === 'GROUP_HEADER') {
				html += '<tr class="group-header">';
				headers.forEach(header => {
					if (!header.startsWith('_') && header in row._group_key) {
						html += `<td><strong>${row._group_key[header]}</strong></td>`;
					} else if (!header.startsWith('_')) {
						html += '<td></td>';
					}
				});
				html += '</tr>';
			} else if (row._type === 'SUBTOTAL') {
				html += '<tr class="subtotal">';
				headers.forEach(header => {
					if (!header.startsWith('_')) {
						const subtotalKey = `${header}_subtotal`;
						const value = row[subtotalKey] !== undefined ? row[subtotalKey] : '';
						html += `<td><strong>${value}</strong></td>`;
					}
				});
				html += '</tr>';
			} else {
				html += '<tr>';
				headers.forEach(header => {
					if (!header.startsWith('_')) {
						html += `<td>${row[header] || ''}</td>`;
					}
				});
				html += '</tr>';
			}
		});

		html += '</tbody></table>';
		$(`#${containerId}`).html(html);
	}

	onReportLoaded(detail) {
		console.log('Report loaded:', detail);
	}
}

// Global instance
let jmitReportBuilder = null;

// Initialize on page ready
frappe.ready(function() {
	jmitReportBuilder = new JMITReportBuilder();
});
