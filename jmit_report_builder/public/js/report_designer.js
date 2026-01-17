/**
 * JMIT Report Builder - UI Components
 * Provides UI utilities and components for report building
 */

class ReportDesigner {
	constructor(containerId) {
		this.container = $(`#${containerId}`);
		this.reportConfig = {};
		this.init();
	}

	init() {
		this.setupUI();
	}

	setupUI() {
		this.container.html(`
			<div class="report-designer">
				<div class="designer-header">
					<h3>Report Designer</h3>
					<div class="btn-group">
						<button class="btn btn-primary" id="btn-preview">Preview</button>
						<button class="btn btn-success" id="btn-save">Save Report</button>
						<button class="btn btn-info" id="btn-export">Export</button>
					</div>
				</div>
				
				<div class="designer-body">
					<div class="row">
						<div class="col-md-6">
							<div class="panel panel-default">
								<div class="panel-heading">
									<h5>Data Source</h5>
								</div>
								<div class="panel-body">
									<div class="form-group">
										<label>Query Type:</label>
										<select id="query-type" class="form-control">
											<option value="SQL">SQL Query</option>
											<option value="STORED_PROCEDURE">Stored Procedure</option>
											<option value="VIEW">Database View</option>
										</select>
									</div>
									<div class="form-group">
										<label>Query:</label>
										<textarea id="report-query" class="form-control" rows="6" placeholder="Enter your SQL query here..."></textarea>
									</div>
									<button class="btn btn-sm btn-info" id="btn-preview-query">Preview Query</button>
								</div>
							</div>
						</div>
						
						<div class="col-md-6">
							<div class="panel panel-default">
								<div class="panel-heading">
									<h5>Columns</h5>
								</div>
								<div class="panel-body">
									<div id="columns-list"></div>
									<button class="btn btn-sm btn-primary" id="btn-add-column">Add Column</button>
								</div>
							</div>
						</div>
					</div>
					
					<div class="row" style="margin-top: 20px;">
						<div class="col-md-6">
							<div class="panel panel-default">
								<div class="panel-heading">
									<h5>Grouping</h5>
								</div>
								<div class="panel-body">
									<div id="grouping-list"></div>
									<button class="btn btn-sm btn-primary" id="btn-add-grouping">Add Grouping</button>
								</div>
							</div>
						</div>
						
						<div class="col-md-6">
							<div class="panel panel-default">
								<div class="panel-heading">
									<h5>Filters</h5>
								</div>
								<div class="panel-body">
									<div id="filters-list"></div>
									<button class="btn btn-sm btn-primary" id="btn-add-filter">Add Filter</button>
								</div>
							</div>
						</div>
					</div>
				</div>
				
				<div class="designer-preview" id="report-preview" style="margin-top: 20px; display: none;">
					<div class="panel panel-default">
						<div class="panel-heading">
							<h5>Preview</h5>
							<button class="btn btn-sm btn-default pull-right" id="btn-close-preview">Close</button>
						</div>
						<div class="panel-body" id="preview-data"></div>
					</div>
				</div>
			</div>
		`);

		this.attachEventListeners();
	}

	attachEventListeners() {
		$('#btn-preview').on('click', () => this.preview());
		$('#btn-save').on('click', () => this.saveReport());
		$('#btn-export').on('click', () => this.showExportOptions());
		$('#btn-preview-query').on('click', () => this.previewQuery());
		$('#btn-add-column').on('click', () => this.addColumn());
		$('#btn-add-grouping').on('click', () => this.addGrouping());
		$('#btn-add-filter').on('click', () => this.addFilter());
		$('#btn-close-preview').on('click', () => this.closePreview());
	}

	async previewQuery() {
		const query = $('#report-query').val();
		if (!query) {
			frappe.msgprint('Please enter a query');
			return;
		}

		try {
			const results = await jmitReportBuilder.previewQuery(query);
			const preview = $('<div class="alert alert-info"><strong>Query Results (First 10 rows):</strong></div>');
			jmitReportBuilder.renderReportTable('preview-data', results);
			$('#report-preview').show();
		} catch (error) {
			frappe.throw(`Preview failed: ${error.message}`);
		}
	}

	addColumn() {
		const columnHtml = `
			<div class="column-row form-group">
				<input type="text" class="form-control" placeholder="Column Name">
				<button class="btn btn-sm btn-danger" onclick="this.parentElement.remove()">Remove</button>
			</div>
		`;
		$('#columns-list').append(columnHtml);
	}

	addGrouping() {
		const groupingHtml = `
			<div class="grouping-row form-group">
				<input type="text" class="form-control" placeholder="Field Name">
				<select class="form-control">
					<option>Ascending</option>
					<option>Descending</option>
				</select>
				<button class="btn btn-sm btn-danger" onclick="this.parentElement.remove()">Remove</button>
			</div>
		`;
		$('#grouping-list').append(groupingHtml);
	}

	addFilter() {
		const filterHtml = `
			<div class="filter-row form-group">
				<input type="text" class="form-control" placeholder="Field Name">
				<select class="form-control">
					<option>=</option>
					<option>!=</option>
					<option>></option>
					<option><</option>
					<option>LIKE</option>
				</select>
				<input type="text" class="form-control" placeholder="Value">
				<button class="btn btn-sm btn-danger" onclick="this.parentElement.remove()">Remove</button>
			</div>
		`;
		$('#filters-list').append(filterHtml);
	}

	preview() {
		const query = $('#report-query').val();
		const queryType = $('#query-type').val();
		
		if (!query) {
			frappe.msgprint('Please enter a query');
			return;
		}

		const queryConfig = {
			query: query,
			query_type: queryType,
			grouping_fields: this.getGroupingFields(),
			filters: this.getFilters()
		};

		jmitReportBuilder.executeReport(queryConfig).then(data => {
			jmitReportBuilder.renderReportTable('preview-data', data);
			$('#report-preview').show();
		}).catch(error => {
			frappe.throw(`Preview error: ${error}`);
		});
	}

	saveReport() {
		frappe.new_doc('JMIT Report', undefined, (frm) => {
			frm.set_value('report_name', 'New Report ' + new Date().getTime());
			frm.set_value('report_query', $('#report-query').val());
			frm.set_value('query_type', $('#query-type').val());
		});
	}

	showExportOptions() {
		const dialog = new frappe.ui.Dialog({
			title: 'Export Report',
			fields: [
				{
					label: 'Export Format',
					fieldname: 'export_format',
					fieldtype: 'Select',
					options: 'PDF\nExcel\nCSV',
					default: 'PDF'
				}
			],
			primary_action_label: 'Export',
			primary_action: (values) => {
				this.handleExport(values.export_format);
				dialog.hide();
			}
		});
		dialog.show();
	}

	handleExport(format) {
		if (!jmitReportBuilder.reportData) {
			frappe.msgprint('Please run preview first');
			return;
		}

		const reportName = 'CustomReport_' + new Date().getTime();
		
		if (format === 'PDF') {
			jmitReportBuilder.exportToPDF(reportName);
		} else if (format === 'Excel') {
			jmitReportBuilder.exportToExcel(reportName);
		} else if (format === 'CSV') {
			jmitReportBuilder.exportToCSV(reportName);
		}
	}

	closePreview() {
		$('#report-preview').hide();
	}

	getGroupingFields() {
		const fields = [];
		$('.grouping-row').each(function() {
			const field = $(this).find('input').val();
			if (field) fields.push(field);
		});
		return fields;
	}

	getFilters() {
		const filters = [];
		$('.filter-row').each(function() {
			const inputs = $(this).find('input');
			const select = $(this).find('select');
			filters.push({
				field: inputs.eq(0).val(),
				operator: select.val(),
				value: inputs.eq(1).val()
			});
		});
		return filters;
	}
}

// Export for use in other modules
window.ReportDesigner = ReportDesigner;
