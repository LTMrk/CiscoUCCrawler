---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-150-user-g-9dc7c2fa57
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_150/user/guide/cuic_b_1501_user-guide/cuic_m_1501_reports.html
retrieved_at: 2026-08-21T04:42:34.123489+00:00
---

Cisco Unified Intelligence Center User Guide, Release 15.0(1)

# Cisco Unified Intelligence Center User Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Reports

## Chapter: Reports

# Reports

## Overview

Reports show data returned by Report Definitions (database query). The database queries extract this data and can be displayed
                           in various Report Views—as grids and charts.

Users with the Report Designer user role can click the Reports from the navigation page to open the Reports page.

All actions on the Reports interface are based on user role and on the user's object permissions for reports and for folders.

For more information about creating or editing a report, see Create Reports .

### Stock Reports

Cisco provides stock report templates to use with Unified Intelligence Center . You can download Stock reports from Cisco.com. Stock report templates display data that has been saved in the Unified CCE database.

After installing Unified Intelligence Center , you can import stock templates using the Import feature and customize the stock reports to suit your business requirements. You can clone the imported stock templates using
                              the Save As option and customize.

Stock reports have one default grid view. Few stock reports also have a chart view.

Localization of stock report templates is not supported.

The available stock report templates are:

Audit Trail —view the sequence of audit records of the transactions related to create, update, modify, and delete that are performed on
                                    the entities of a Unified Intelligence Center server.

By default, only System Administrators can access and view this report. System Administrator can give permissions to other
                                    Unified Intelligence Center users to use this report.

Group Access Detail —view access rights of groups that use Unified Intelligence Center resources such as Dashboards, Reports, and other resources.

Resource Ownership and Access —view access rights of users and about ownership status of users who use Unified Intelligence Center resources such as Dashboards,
                                    Reports, and other entities.

User's Audit Log —view the audit log data of users such as, Logged In User Detail (name and role), Event Detail, Updated Column, User Detail,
                                    and other modified details.

For more information, click the "?" icon (Template Help) from the report in the run mode.

## Report Actions

The following table lists various actions that you can perform from the Reports.

You can open a maximum of ten tabs at a time.

Report-level actions

New

Creates a new report in the selected folder.

You cannot create reports inside the Stock folder. You can only import reports into the Stock folder. To edit or customize
                                                   reports, clone the report and edit the cloned version.

Folder

When you move or save the folders to a different location, the drop-down lists all the folders including the disabled folders.
                                                   You can navigate to subfolders with Edit permissions.

You cannot create folders inside the Stock folder.

Toolbar actions

Refresh

Refreshes the Reports page.

Applies to all folder levels (root, sub folder, and report).

Favorites

To easily access your reports, you can tag Reports as your Favorites.

Click the star icon beside the Report name to add to Favorites.

Search

Searches for a particular the Report.

Import

Imports a report.

To import a report, you need the Report Designer, Report Definition Designer, and Value List Collection Designer roles and
                                       the Edit permission on the target folder where you want to import these reports.

For more information, see Import Reports .

Applies to all folder levels (root, subcategory, and report).

Ellipsis(…) actions

Edit

Edits the Report details. In the edit mode, you can add, modify, and delete report details, views and thresholds, and filters.

After editing the Report, click Finish .

You cannot edit a Stock report.

Save As

Saves a copy of the report with a different name.

By default, the reporting users do not have permission to create a subfolder in the Reports root folder. To get permissions,
                                                         contact your administrator.

You cannot perform the Save As action to move contents (reports or folders) into the Stock folder and its subfolders.

Parentheses (( ))

Angle brackets (<,>)

Forward slash (/)

Question mark (?)

Quotes (")

Any scripts; JavaScript

Clone Report Definition

If you want to create a copy of the Report Definition that is associated with the report being saved:

Click the Clone Report Definition check box.

Enter the new Report Definition Name and select the Report Definition Location.

Click Save .

The new report gets associated to the cloned Report Definition.

Rename

Renames a folder or a report.

You cannot rename a Stock folder or a Stock report.

Applies to the root-level folder.

Move

Moves Report or Folder from one folder to another.

You can move a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being moved.

You cannot move custom folders or reports from within the Stock folder (and its subfolders) to other locations and the other
                                                         way.

Set Default Filters

Creates report filters.

For more information, see Report Filters .

You can also set the default filter by checking the Set as Default check box in the Choose Filter dialog box during the report run mode.

Add Help

Hosts the help page for Report Templates. For more information, see Add Template Help .

Delete

Deletes a report or a folder.

You can delete a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being deleted.

Stock folder cannot be deleted. Stock report can be deleted.

Assigns appropriate permissions to access and manage the Report.

Groups —Grants View and Edit permissions for the Report.

Security Administrators can grant these permissions to various groups.

Entity owners can grant these permissions to groups that they are directly associated with.

Users —Grants View and Edit permissions for the Report to various users. Applicable only to Security Administrators.

Higher permissions (View and Edit) from either an individual user or the user group takes precedence.

Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups .

When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes.

Permalinks

Displays the Report permalink. For more information, see Permalink for a Report .

You can access permanent hyperlink only from a web browser.

Export

Export any custom report or report folders. Reports and report folders are exported in a ZIP file format. To export a report
                                       or a report folder, you need the REPORT DESIGNER role. For more information, see Export Reports and Folders .

## Add Template
                        	 Help

You can configure
                              		  individual help files to each Cisco Unified Intelligence Center report. You can
                              		  either host the help page separately and point the report to it or create and
                              		  upload the help page along with the report.

This help
                              		  content is specific to the report and can contain explanation on:

How to use
                                    				the report

Field
                                    				description

Details of
                                    				the relationship between the fields

How to
                                    				interpret the report data or

Any other
                                    				report related information

You can upload only files in ZIP formats. ZIP files can contain multiple HTML files. The HTML page contents support rich text
                              including images.

Help files don't support videos and other interactive content. To prevent security risks like Cross-Site Scripting (XSS),
                                          ensure that any HTML files that you upload are free of harmful scripts.

To configure the
                              		  help page for a report, perform the following steps:

Step 1

From the left
                                       			 navigation pane, click Reports .

Step 2

Click the
                                       			 Ellipsis icon (…) next to the report row for which you want to create the help
                                       			 page and click Add
                                          				Help .

Step 3

In the Add
                                          				Help dialog box,

If you
                                                					 want to set an external help page as the report help, select the URL option and enter the external URL location.

If you want to upload the help file, select the Choose file option and click Browse to upload a ZIP file (with HTML files).

Step 4

After
                                       			 uploading the file, click Save .

## Report Filters

### Filter
                           	 Types

Report filters in Unified Intelligence Center are used to present selective data. You can define the filter to filter the data that you want to display in the report.
                              There are two ways to view the Filter page.

Before the report is generated: You can set and refine the default filter values using the Actions > Set Default Filter option.

After the report is generated: You can refine the filter values using the filter icon.

You cannot view filters if the Report Designer has selected the Skip filter during the report processing check box during the report filter selection.

Cisco Unified Intelligence Center supports the following types of report filters:

Date &
                                    			 Time

Key Criteria

Field Filters

Parameters

Filter parameters are displayed based on the selected query type in the Report Definition for that report.

Report Definition Query Type

Applicable Filter Tabs

Database Query

Date & Time, Key Criteria, Field Filters

Live Data or Real Time Streaming

Key Criteria, Field Filters

Anonymous Block

Parameters

Stored Procedure

Parameters

### Date & Time

Cisco Unified Intelligence Center uses the browser locale to display the Date & Time format in the filter page. If Cisco Unified Intelligence Center does not support the browser locale language, then the locale selected in the Cisco Unified Intelligence Center application is used.

To configure Date and Time filters for a report, perform the following steps:

Step 1

After creating the report, click Set Default Filter from the ellipsis Actions .

Step 2

In the Date & Time filter wizard, select the Date Range and Time Range options.

The options available in the Date Range and Time Range filter are predefined.

Selection of the Custom option allows you to customize the Date Range and Time Range details.

You can select the days of the week (Days > Custom) only if the time interval spans more than a day.

For reports that are based on the query type Anonymous Block, you cannot select days of the week. For more information, see Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html .

Step 3

Check the Skip filter during the report execution check box if you want to skip filter selection during the running of report.

In the Choose Filter dialog box (report run mode), you can check the Set as Default check box to set the report filter as the default.

Step 4

Click Next .

### Key Criteria

Use the Key Criteria tab in the filter to select value lists or collections. A collection is a pre-configured group of values.

To configure Key Criteria filters, perform the following steps:

Step 1

After creating the report, click Set Default Filter from the ellipsis Actions .

Step 2

In the Date & Time filter wizard, select the Date Range and Time Range options and click Next .

Step 3

In the Key Criteria filter wizard, select the collections or values from the Available selection box.

Do not set multiple filter parameters; set any one filter parameter.

Step 4

Use the arrows to move the selected collections or values to the Selected selection box.

Step 5

You can also select multiple collections or values.

Step 6

Click Next .

### Field Filters

Use the Field Filters tab to filter any field in the report. Based on the selected field type (date, numeric/decimal, boolean, or string), different
                                 operators are available. For example, you can filter calls in queue for greater than two minutes or on all agents in the hold
                                 state to filter out the less important information.

Only for SQL Query based reports.

To filter a text, date, boolean, or a decimal field.

To configure Field Filters, perform the following steps:

Step 1

After creating the report, click Set Default Filter from the ellipsis Actions .

Step 2

In the Date & Time filter wizard, select the Date Range and Time Range options and click Next .

Step 3

In the Key Criteria filter wizard, select the collections or values from the Available selection box and click Next .

Step 4

In the Field Filters wizard, select the filter according to the following criteria.

Filter criteria/operators depend on the selected field type (date, numeric/decimal, boolean, or string).

For Date , the options available in Date Range filter are predefined. Using the Date Range drop-down list, select from Custom, Today,
                                                   Yesterday, This Week, Last Week, This Month, Last Month, Year to Date, or Last Year.

Only Custom will allow the user to customize the Calendar, Time Range and Days certain days of the week.

For Decimal , select an Operator from Equal To, Not Equal To, Less Than, Less Than or Equal To, or Greater Than and then enter a value;
                                                   for example, Operator = Greater Than and Value = 16.5.

For String , select an Operator from Equal To, Not Equal To, or Matches and then enter a value for the string; for example, Operator
                                                   = Matches and Value = Team Green.

If you select Matches as the Operator, you must specify an SQL pattern to match the string field. The system appends the wild
                                                         card character % automatically to the beginning and end of the string. You can also use any SQL wild card pattern in between
                                                         the string.

If the filter field is associated with a Value List , then specify any value or move one, all, or some items in the list to the Selected column to filter.

Use only the Matches operator to filter the report data records with leading or trailing spaces. Do not use the Equal To or
                                                               Not Equal To operators in such scenarios as Unified Intelligence Center trims the filter criteria before running the SQL query
                                                               and hence does not fetch the matching results.

For Boolean , select True or False from the Operator list.

Step 5

Using the Operator drop-down list, select the criteria.

If you select Matches operator, you can use any Microsoft SQL wildcard pattern to filter the data. The wildcard character % is added to the beginning and end of every string that is used to filter the data.

Step 6

In the Value field, enter a value against which the data in the field will be filtered.

Step 7

Click Run .

## Report Types

There are three types of reports based on the query types:

Historical report

Real-time report

Live Data report

Report Components

These reports consist of the following components:

Data Source

The Data Source defines the sources that contain the data for the report. Unified Intelligence Center supports three types
                                 of data sources: Microsoft SQL Server, IBM Informix, and Streaming. The data source should be pre-configured for you. If it
                                 is not, contact your administrator to configure the appropriate data source.

Additional data sources are not supported.

Report Definitions

Each report has a Report Definition, which represents how data is retrieved from the data source for that report template.
                                 In addition to specifying how data is retrieved (by a simple MS SQL query, stored procedure query, real time streaming or
                                 an anonymous block query), a report definition contains the dataset that is obtained. This includes the fields, filters, formulas,
                                 refresh rate, and key criteria field for the report.

Reports

Reports show data returned by Report Definitions. This data is extracted by database queries.

Time Zone Conversions

The time zone conversion happens if there is a difference between the user and the data source time zones.

Daylight savings time consideration for Database Query Reports : The Daylight savings time offset at the start of the date range is considered for the time zone conversion when the report
                                 is filtered. If the daylight savings change occurs somewhere in between the filter date and time ranges, the time zone offsets
                                 will not be computed properly if the user and the data source are in different time zones. In this case, you will have to
                                 split the time filter such that separate report invocations are run before and after the daylight savings time change.

The daylight savings time offset depends on the latest system time zone library.

Daylight savings start date or end date may (when the data is recorded) create an additional row (in the report output) due
                                             to the time zone value change in the SQL database. This applies to any template report, as well as for any query type (Anonymous
                                             block, Database Query, Stored Procedure, Real Time Streaming) that these template reports would use. For confirmation that
                                             SQL had time zone value change, use the Report Options icon from the report summary page and run the SQL command in AW node
                                             to validate the change in the time zone.

Example 1:

User time zone: Australia/Sydney

Data source time zone: America/New_York

Daylight savings time changes: +1 hour for Sydney at 2013-10-06 02:00 a.m. DST +1 hour is already on for New York

Filter selected by the user: 2013-10-06 to 2013-10-06, 12:00 a.m. to 11:59 p.m.

Query formed in data source time zone: 2013-10-05 10:00:00 a.m. to 2013-10-06 09:59:59 a.m.

Report displayed in user time zone: 2013-10-06 12:00 a.m. to 2013-10-07 12:59 a.m.

In this case, the report will display an extra hour of data as Sydney Daylight savings time is off at the start of the date
                                 range and on at the end of the date range.

Example 2:

User time zone: Australia/Sydney

Data source time zone: America/New_York

Daylight savings time changes: +1 hour on for Sydney at 2013-10-06 02:00 a.m. DST +1 hour is already on for New York

Filters selected : 2013-10-06 to 2013-10-10, 03:00 a.m. to 11:59 p.m.

Query formed in data source timezone: 2013-10-05 12:00:00 p.m to 2013-10-06 08:59:59 a.m.

Report displayed in user time zone: 2013-10-06 03:00 a.m. to 2013-10-06 11:59 p.m.

In this case, the conversion happens as expected as there is no Daylight savings time change in between the date ranges.

Example 3:

User time zone: America/New_York

Data source time zone: IST

Daylight savings time changes: +1 hour DST at 2013-03-03 02:00 a.m. and off at 2013-11-03 02:00 a.m. for New York. No Daylight
                                    savings time changes for IST.

Filter selected by the user : 2013-11-03 to 2013-11-03, 01:30 a.m. to 05:30 p.m.

Query formed in data source time zone: 2013-11-03 11:00:00 a.m. to 2013-11-03 02:59:59 a.m.

Report displayed in user time zone: 2013-11-03 01:30 a.m. to 2013-11-03 04:30 p.m.

In this case, the report will display one hour less of data as New York Daylight savings time is on at the start of the date
                                 range and off at the end of the date range.

Report Views

A report can be presented in multiple formats (grid and charts). Each view can have its own set of fields. A single report
                                 can have multiple views.

Report Help

You can attach a help page specifically for your report. For more information, see Add Template Help .

### Historical and Real Time Reports

Historical report —Retrieves data from the historical data source. Reports are populated with interval data that has a default refresh rate
                              of 15 minutes. Historical reports have an upper limit of 8000 rows.

Real-time report —Retrieves data from the real-time data source. Reports are populated with interval data that has a default refresh rate of
                              15 seconds. Real-time reports have an upper limit of 3000 rows.

While running Cisco Unified Intelligence Center Historical and Real-Time Reports you can:

Filter data in a report

Change the view of a report from a grid to a gauge or a chart

You can select one of the predefined grid, gauge, or chart views.

For more information on creating/editing views, see Report Views .

Modify reports

### Live Data Reports

Live Data report —Receives data from streaming data source. Live Data reports supports only grid view.

Live Data reports do not automatically respond to changes in the system time. If the server or client time is changed or adjusted,
                                          the report must be refreshed to accurately display the duration field values. For example, during a daylight saving time (DST)
                                          change, active live data reports do not display correct values in the duration field. Live data reports must be refreshed
                                          to update.

## Manage Reports

### Create Reports

All actions on the Reports interface are based on user role and on the user's object permissions for reports and for categories.

By default, reporting users do not have permission to create a subfolder in Reports . An Administrator can create a subfolder and grant access.

To create a new report, perform the following steps:

Step 1

In the left navigation pane, choose Reports .

Step 2

Navigate to the folder where you want to create the report.

Step 3

From the Reports toolbar, click New > Report .

To edit an existing report, navigate to the report, click the ellipsis icon beside the report and click Edit .

Step 4

In the Create New Report window, enter the Report Name and Description .

The report name must be unique to Cisco Unified Intelligence Center.

Step 5

Click Next .

Step 6

In the Basic Details tab, enter or select the report details.

Use the arrows to select the appropriate Report Definition.

Step 7

Click Next .

Step 8

In the Manage Views tab, create the report views and click Next .

For more information, see Report Views .

Step 9

In the Thresholds tab, create report thresholds and click Finish .

For more information, see Report Thresholds .

### Report Views

There are two types of report views:

Grid View

Chart View

Do not delete the Report Definition fields that are currently associated with any of the manually created report views. If
                                          deleted, you must reapply the Data Fields for all the manually created report views to save the report.

For default grid views, the deleted field is removed automatically from the Data Fields list retaining any other fields in
                                          the Selected Field list. Hence, no additional action is required to save the report.

#### Create a Grid View

Grids are tabular presentations of the data in rows and columns. By default, all Cisco stock reports have a grid view. For
                                    custom reports, a default grid is created from the SQL query in the Report Definition.

You can create a Grid View while creating or editing a report.

To create a Grid View, perform the following steps:

Step 1

Create or edit a report.

Step 2

Enter the report details in the Basic Details screen and click Next .

You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report .

Step 3

You can edit the default view ( Actions column > Edit View ) or click Create New > Grid view to create a new grid view.

The Edit Grid View or the New Grid View screen appears depending on your selection for edit or create.

Step 4

Enter the Name and Description in the respective fields.

Maximum length allowed for the grid view Name : 50 characters.

Step 5

From the Font selection box, you can select the font size from the list to display the grid data.

Step 6

Use the arrow buttons to select fields from the Available value list box to move to the Selected field list.

Step 7

You can use the following features to improve grid view display:

Header —Use this feature to add (+) or delete (-) a header for the selected fields. This helps in categorizing the field set.

You cannot save the view with empty headers.

Post upgrade to Cisco Unified Intelligence Center 12.0 or later , any empty headers that exist in the report views in prior releases are not migrated.

Edit icon—In the Selected value list box, click the Edit icon (hover on the field value) if you want to edit the Display Name and Column Width for the selected field and click Done .

For Header fields, you can only edit the Display Name.

Sort Grid by Field —Select the Sort Grid by Field check box to sort the selected report columns in either Ascending or Descending order. Selecting this check box enables the drop-down list to be populated with the values from the Selected value list box. You can select only one value for sorting.

Step 8

Click Save .

Step 9

Click Finish .

#### Create a Chart
                              	 View

Cisco Unified Intelligence Center supports the following chart types:

Bar —Bar charts display discontinuous events and show the differences between events rather than trends. Bar charts are oriented
                                          vertically and can be stacked horizontally or clustered one below the other.

Pie/Donut —Pie charts display quantities as proportions of a whole. The circle (pie) represents 100% of the data, with each quantity
                                          represented as a wedge of the appropriate size. Pie charts take decimal or numeric fields only. A pie chart cannot have more
                                          than 50 wedges. An error occurs if your data set and chart editor selections generate a pie chart with more than 50 wedges.

A doughnut chart is another display representation of a pie chart.

Column —Column charts display discontinuous events and show the differences between events rather than trends. Column charts are
                                          oriented horizontally and can be stacked vertically or clustered side by side.

Dial Gauge/Numeric —A gauge chart displays the dial representation of the report results as per the defined threshold.

The Numeric chart displays the report results in a number format highlighted as per the defined threshold.

Line charts —Line charts display continuous quantities over time against a common scale. Use the Line charts to show trends.

Live Data reports do not support chart view.

In the vertically oriented charts, for Cyrillic characters, the data labels in the Horizontal Axis field may be hidden or
                                                      garbled. This is a known limitation. Hence, for Cyrillic characters, use the horizontally oriented charts.

To create a Chart View, perform the following steps:

Step 1

Create or edit a report.

Step 2

Enter the report details in the Basic Details screen and click Next .

You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report .

Step 3

Click Create New > Chart view .

Step 4

In the Create New Chart View screen, click the required chart type. For more information, see Chart Types .

Step 5

Enter the Chart Information; Name , Description and click Next .

Maximum length allowed for the chart view Name : 50 characters.

For Cartesian type charts (Bar, Column, and Line), select the Group Data check box to group data:

By a field —Select this option to create a chart view where the vertical axis shows fields with footer formula configured for line or
                                                                  column chart and horizontal axis with footer formula for bar chart.

By label field —Select this option to create a chart view where the vertical axis shows fields of decimal data type for Line or Column chart.
                                                                  In Bar chart, the horizontal axis shows fields of decimal type.

For Pie charts, you can only Group Data by Label Field .

Step 6

In the Add Data Fields screen, select the Label Field from the drop-down list and Data Fields from the list box and click Next .

Step 7

In the Preview and Format screen, enter or select appropriate information based on the selected chart type.

For more information, see Chart Types .

Date and Time

Boolean

Step 8

Click Save .

##### Chart Types

Chart Type

Chart Information

Add Data Fields

Preview and Format

Bar

Yes

Yes

Yes

Column

Yes

Yes

Yes

Line

Yes

Yes

Yes

Gauge/Numeric

No

Yes

Yes

To set the chart view for Dial Gauge/Numeric, perform the following steps:

Enter the Range . By default, min is 0 and max is 100.

Define the zones.

When the chart value is within any of the defined thresholds,

The gauge pointer points to the corresponding color set in the threshold.

The Numeric text is displayed in the corresponding color set in the threshold.

You can select Dial Gauge or Numeric view for this report. If you select the Numeric view, the values are displayed in decimals by default. To display these values as whole numbers, check the Round up the value to the next whole number check box.

Click Save .

Pie

Yes

Yes

Yes

You can select Pie or Donut as the display type for this report.

### Report Thresholds

You can set a threshold indicator for a field to display if the field value meets the threshold condition. There are nine
                                 colors instead of the color palette for the threshold color selection in this release. Threshold indicators can be set only
                                 for view type Grid and Chart > Gauge .

For setting field threshold indicators for a Chart > Gauge view, see Create a Chart View .

For setting field threshold indicators for a Grid view, perform the following steps:

Step 1

From the Manage Views screen , after adding the report views, click Next .

Step 2

Select a view to which you want to set the threshold and select the field name from the Create new threshold list.

Step 3

Select a field operator and set a condition from the Operator list.

Operator

Description

Matches

The Matches operator accepts Regular Expressions.

Note that the Regular Expressions does not support:

Flags (i, g, m, n, y), OR/AND any combinations of these flags.

Leading and trailing forward slash (/).

Example:

Valid Pattern → \w+\s

Invalid Pattern → /\w+\s/g

(As it contains leading and trailing forward slash (/) and a "g" flag.)

String fields; Always, Equal, Not Equal

Decimal fields; Always, Equal, Not Equal, Greater Than, Less Than, Greater Than Equal To, Less Than or Equal To, Between

In Report Definition, if the %format is defined for any field, then while setting the thresholds for that field, ensure to
                                                      enter the decimal format of the percentage to render the condition in the report.

For example:

In Report Definition, if %format is defined for the field "SL" (Service Level) and you want to apply thresholds to this field
                                                      to indicate "Red" if SL is less than 60%, set the following:

Define the threshold for the SL field.

Set the Operator to Less Than.

Enter the percentage value as 0.60 .

Select “Red” in the No Fill drop-down.

Click Done .

Step 4

Choose the options from No Fill and edit the threshold fields.

You can set conditions on the same or different fields:

condition on same field: threshold and condition on the same field.

condition on different field: threshold for a field, based on the condition on the different field.

multi conditions on same field: apply threshold for a field based on the condition on different fields.

Caution

When you upgrade to Unified Intelligence Center version 11.6 or later, all the threshold colors are retained for reports that
                                                         are created in the earlier versions. But, when you modify the threshold, all the old threshold color selection are lost within
                                                         the report. Hence, you must reconfigure the threshold color selection for that report.

For existing reports, perform the above mentioned steps to add more thresholds.

To edit an existing threshold from a report run already, click Report options and select Manage Thresholds.

Step 5

Format the text in the field to appear when it matches the threshold condition. Use the following options:

Text Bold —Select this check box to highlight the report field in bold.

Text/Background Color —Select a color from the drop-down for the text/background color in the field.

Text Substitute —Enter a new string if you want the text in the field to be replaced with it when it matches the threshold condition.

Syntax to add an html hyperlink as text substitute: < a href=https://www.cisco.com target=_blank>cisco</a>

Syntax to add an empty space as text substitute: &nbsp;

Image Location —Enter the URL path of the image if you want the text to be replaced with an image.

Supports only image URLs reachable from Unified Intelligence Center server. Maximum size limit allowed for the image is 5MB.

Step 6

Click Done .

Step 7

Click Finish .

## Run Report

### Report Actions - Run Mode

The following table lists all the menu items and actions you can perform when you run a report.

Edit View

Displays the Edit View dialog box. You can modify the current report view and click Done to instantly view the modified view.

Save View As

Clones the existing report view. In the Save View dialog box, enter the Name and Description for the cloned view and click Save . The report page refreshes with the cloned view.

Create Chart View

For the report that is run, you can directly create a chart view if you have Edit permissions. After you create the chart view, the report page refreshes with the newly created chart view and gets listed
                                          in the view list.

This feature is disabled for Live Data reports.

For more information, see Create a Chart View .

Group By

Add/remove/update grouping configurations for the current view (columns). Cisco Unified Intelligence Center grid reports support
                                          up to three levels of grouping.

If you are grouping the column with Date or Date time data type, you can group records on a Daily/Weekly/Monthly basis.

For more information, see Group By .

Manage Thresholds

Sets a threshold indicator for a field to display if the field value meets the threshold condition. Threshold indicators can
                                          be set only for views of type Grid and Gauge.

For more information, see Report Thresholds .

SQL

Displays the SQL code used to run this report.

Export

Exports the already run grid report data into your local disk in a .xls x format.

When you export a report to an Excel file format, to read the exported report, the client system’s locale must match with
                                                            the browser’s locale (where you had exported the report).

When reports are exported to excel in Report viewer, the custom formatting of DECIMAL data type is not applied.

Report consists of predefined formats for Date and Time. When a report is exported to Microsoft Excel, only five predefined
                                                            Date and Time formats are supported. The supported formats are:

dd/mm/yy

mmm-yy

h:mm AM/PM

h:mm:ss AM/PM

mm/dd/yyyy hh:mm:ss

If you have exported a report with a Date and Time format which is not supported by Excel, Excel's General format is applied by default.

Run or Pause the report

Click to run or pause the report respectively.

Report running times out after three minutes. Rerun the report by modifying the filter, and if the problem persists, contact
                                                      your administrator.

Print Report

Prints the report using your default printer.

Reports in chart view supports only landscape mode in A3 size paper for printing.

Manage Filters

Displays Choose Filter dialog box to modify filter criteria for this report.

For more information, see Report Filters .

Refresh

Refreshes the Report page.

View Filter Information

Displays the filter information of the report.

Online Help

Displays the configured template help. You can configure template help for the report from the Reports page > Add Help .

For more information, see Add Template Help .

Only Thresholds

Enable this toggle button to view only rows with matching threshold values in the report.

By default, this check box is unchecked for every report.

This button is disabled for the grouped view.

### Group By

For a report that is run, use the Group By option to add/remove/update grouping configurations for the current view. Cisco Unified Intelligence Center grid reports
                                 support up to three levels of grouping.

If you’re grouping the column with Date or Date Time data type, you can group records on a Daily/Weekly/Monthly basis.

Live data reports don’t support grouping.

Grouped fields cannot be hidden.

To group the report data, perform the following steps:

Step 1

From the report that is run, click the Report options icon and select the Group By option.

Step 2

In the Group By dialog box, specify the Number of Levels you want to group the report.

Cisco Unified Intelligence Center grid reports support up to three levels of grouping.

Step 3

To group the report data by values in a particular column, select the required column name from the Grouped By list.

None—The report data is grouped by the absolute date or date time values.

Daily—The report data is grouped by day.

Weekly—The report data is grouped by week.

Monthly—The report data is grouped by month.

Enable the Show Summary Only toggle button to display only the summary row in the report.

For example, if you group by Agent Team and enable the Show Summary Only toggle button, only the summary data row for each team is displayed.

Step 4

Click Save .

For the grouped view, the Only Thresholds check box is disabled.

Thresholds aren’t displayed in a grouped field and on summary rows.

You cannot perform a drill-down from a report with grouped fields.

### Concurrent Reports

Two hundred Cisco Unified Intelligence Center users can concurrently run the following reports (without XML permalinks):

Two real-time reports with 100 rows and 10 columns each.

Two historical reports with 2000 rows and 10 columns each.

If Live Data is supported by the deployment, two Live Data reports with 100 rows and 10 columns each.

If XML permalinks are included, 30 users in addition to the 200 users specified above ̶̶ each running one real-time XML permalink
                              and one historical XML permalink ̶̶ are supported. This action results in 7200 real-time XML permalink executions per hour
                              and 60 historical XML permalink executions per hour, approximately.

## Import Reports

You can import the Unified Intelligence Center report, which is in either .xml or .zip file format.

The imported report retrieves data for the following entities:

Report

Report Definition

Value Lists

Views

Thresholds

Drilldowns

Template Help

Each report template help folder has a size limit of 3 MB. If the folder size exceeds this limit, the system does not load
                                                      the help content.

You cannot import Report Filters and Collections.

You cannot use the same names for the custom Value List, Report, or Report Definition that exist in the stock report templates.
                                                      If the same names are used, it leads to the stock report template import failure.

To import reports, perform the following steps:

Step 1

In the left navigation pane, choose Reports .

Step 2

In the Reports listing page, click Import .

Step 3

Click Browse to select the file (.xml or .zip format) to be imported.

The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB.

Step 4

Select the required file and click Open .

Step 5

Select the file location from the Save to Folder list to save the file.

Step 6

Click Upload .

Step 7

Select a Data Source for the Report Definition only if the Report Definition for the report being imported is not defined
                                       in the Unified Intelligence Center.

Step 8

Select a Data Source for the Value List that is defined in the Report Definition.

Selection of a Data Source for the Value List is mandatory:

If the Value List does not use the same Data Source as the Report Definition.

For Real Time Streaming Report Definitions.

Step 9

Select the files to import or overwrite.

Overwrite—If the report being imported exists in the Unified Intelligence Center.

Import—If the report being imported is the new set of report files.

Step 10

Click Import .

If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder.

Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                            Intelligence Center, report templates continue to work in the upgraded version.

Importing manually edited XMLs is not supported.

## Export Reports and Folders

You can export any custom or stock report or report folders from the Unified Intelligence Center. Reports and report folders
                              are exported in a ZIP file format.

When you export a folder, the reports in the folder are grouped as ZIP files. The grouping is based on the data source that
                              is used by the report definition and the value lists.

For customized reports, you must update the version numbers of the value list and report definition before you export the
                                                report. Else, the export will not overwrite the existing reports.

While exporting folders, ensure that all the Value Lists in the report definitions or folders point to the same data source
                                                respectively.

Caution

Do not modify the exported report (XML file) for customization purposes. However, if necessary, you can modify only the EntityVersion
                                          of the Report, Report Definition, and ValueList.

When you export a report, the following data that is associated with the report are exported:

Report

Report Definition

Value Lists

Views

Thresholds

Drilldowns

Template Help (if not bundled, an empty folder is created in the zip file)

Report Filters and Collections are not exported along with the report.

To export a report or a folder, perform the following steps:

Step 1

From the left navigation panel, click Reports .

Step 2

Navigate to the report or the report folder that you want to export and click the ellipsis icon beside the report and click Export .

If necessary, you can rename the report or the report folder. Do not change the file extension (Reports or report folder:
                                                      zip).

Step 3

Click OK .

| Note | All actions on the Reports interface are based on user role and on the user's object permissions for reports and for folders. |
|---|---|

| Note | Localization of stock report templates is not supported. |
|---|---|

| Note | You can open a maximum of ten tabs at a time. |
|---|---|

| Action | Description |
|---|---|
| Report-level actions |
| New |
| Report | Creates a new report in the selected folder. Note You cannot create reports inside the Stock folder. You can only import reports into the Stock folder. To edit or customize
                                                   reports, clone the report and edit the cloned version. | Note | You cannot create reports inside the Stock folder. You can only import reports into the Stock folder. To edit or customize
                                                   reports, clone the report and edit the cloned version. |
| Note | You cannot create reports inside the Stock folder. You can only import reports into the Stock folder. To edit or customize
                                                   reports, clone the report and edit the cloned version. |
| Folder | Creates a new Folder. Use this feature to categorize reports. Note When you move or save the folders to a different location, the drop-down lists all the folders including the disabled folders.
                                                   You can navigate to subfolders with Edit permissions. Note You cannot create folders inside the Stock folder. | Note | When you move or save the folders to a different location, the drop-down lists all the folders including the disabled folders.
                                                   You can navigate to subfolders with Edit permissions. | Note | You cannot create folders inside the Stock folder. |
| Note | When you move or save the folders to a different location, the drop-down lists all the folders including the disabled folders.
                                                   You can navigate to subfolders with Edit permissions. |
| Note | You cannot create folders inside the Stock folder. |
| Toolbar actions |
| Refresh | Refreshes the Reports page. Applies to all folder levels (root, sub folder, and report). |
| Favorites | To easily access your reports, you can tag Reports as your Favorites. Click the star icon beside the Report name to add to Favorites. |
| Search | Searches for a particular the Report. |
| Import | Imports a report. To import a report, you need the Report Designer, Report Definition Designer, and Value List Collection Designer roles and
                                       the Edit permission on the target folder where you want to import these reports. For more information, see Import Reports . Note Applies to all folder levels (root, subcategory, and report). | Note | Applies to all folder levels (root, subcategory, and report). |
| Note | Applies to all folder levels (root, subcategory, and report). |
| Ellipsis(…) actions |
| Edit | Edits the Report details. In the edit mode, you can add, modify, and delete report details, views and thresholds, and filters. After editing the Report, click Finish . Note You cannot edit a Stock report. | Note | You cannot edit a Stock report. |
| Note | You cannot edit a Stock report. |
| Save As | Saves a copy of the report with a different name. Note By default, the reporting users do not have permission to create a subfolder in the Reports root folder. To get permissions,
                                                         contact your administrator. You cannot perform the Save As action to move contents (reports or folders) into the Stock folder and its subfolders. Note The report description does not support the following special characters: Parentheses (( )) Angle brackets (<,>) Forward slash (/) Question mark (?) Quotes (") Any scripts; JavaScript | Note | By default, the reporting users do not have permission to create a subfolder in the Reports root folder. To get permissions,
                                                         contact your administrator. You cannot perform the Save As action to move contents (reports or folders) into the Stock folder and its subfolders. | Note | The report description does not support the following special characters: Parentheses (( )) Angle brackets (<,>) Forward slash (/) Question mark (?) Quotes (") Any scripts; JavaScript |
| Note | By default, the reporting users do not have permission to create a subfolder in the Reports root folder. To get permissions,
                                                         contact your administrator. You cannot perform the Save As action to move contents (reports or folders) into the Stock folder and its subfolders. |
| Note | The report description does not support the following special characters: Parentheses (( )) Angle brackets (<,>) Forward slash (/) Question mark (?) Quotes (") Any scripts; JavaScript |
| Clone Report Definition | If you want to create a copy of the Report Definition that is associated with the report being saved: Click the Clone Report Definition check box. Enter the new Report Definition Name and select the Report Definition Location. Click Save . The new report gets associated to the cloned Report Definition. |
| Rename | Renames a folder or a report. Note You cannot rename a Stock folder or a Stock report. Note Applies to the root-level folder. | Note | You cannot rename a Stock folder or a Stock report. | Note | Applies to the root-level folder. |
| Note | You cannot rename a Stock folder or a Stock report. |
| Note | Applies to the root-level folder. |
| Move | Moves Report or Folder from one folder to another. Note You can move a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being moved. You cannot move custom folders or reports from within the Stock folder (and its subfolders) to other locations and the other
                                                         way. | Note | You can move a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being moved. You cannot move custom folders or reports from within the Stock folder (and its subfolders) to other locations and the other
                                                         way. |
| Note | You can move a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being moved. You cannot move custom folders or reports from within the Stock folder (and its subfolders) to other locations and the other
                                                         way. |
| Set Default Filters | Creates report filters. For more information, see Report Filters . Note You can also set the default filter by checking the Set as Default check box in the Choose Filter dialog box during the report run mode. | Note | You can also set the default filter by checking the Set as Default check box in the Choose Filter dialog box during the report run mode. |
| Note | You can also set the default filter by checking the Set as Default check box in the Choose Filter dialog box during the report run mode. |
| Add Help | Hosts the help page for Report Templates. For more information, see Add Template Help . |
| Delete | Deletes a report or a folder. Note You can delete a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being deleted. Stock folder cannot be deleted. Stock report can be deleted. | Note | You can delete a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being deleted. Stock folder cannot be deleted. Stock report can be deleted. |
| Note | You can delete a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being deleted. Stock folder cannot be deleted. Stock report can be deleted. |
| Permissions | Assigns appropriate permissions to access and manage the Report. Groups —Grants View and Edit permissions for the Report. Security Administrators can grant these permissions to various groups. Entity owners can grant these permissions to groups that they are directly associated with. Users —Grants View and Edit permissions for the Report to various users. Applicable only to Security Administrators. Note Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. | Note | Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. |
| Note | Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. |
| Permalinks | Displays the Report permalink. For more information, see Permalink for a Report . Note You can access permanent hyperlink only from a web browser. | Note | You can access permanent hyperlink only from a web browser. |
| Note | You can access permanent hyperlink only from a web browser. |
| Export | Export any custom report or report folders. Reports and report folders are exported in a ZIP file format. To export a report
                                       or a report folder, you need the REPORT DESIGNER role. For more information, see Export Reports and Folders . |

| Note | You cannot create reports inside the Stock folder. You can only import reports into the Stock folder. To edit or customize
                                                   reports, clone the report and edit the cloned version. |
|---|---|

| Note | When you move or save the folders to a different location, the drop-down lists all the folders including the disabled folders.
                                                   You can navigate to subfolders with Edit permissions. |
|---|---|

| Note | You cannot create folders inside the Stock folder. |
|---|---|

| Note | Applies to all folder levels (root, subcategory, and report). |
|---|---|

| Note | You cannot edit a Stock report. |
|---|---|

| Note | By default, the reporting users do not have permission to create a subfolder in the Reports root folder. To get permissions,
                                                         contact your administrator. You cannot perform the Save As action to move contents (reports or folders) into the Stock folder and its subfolders. |
|---|---|

| Note | The report description does not support the following special characters: Parentheses (( )) Angle brackets (<,>) Forward slash (/) Question mark (?) Quotes (") Any scripts; JavaScript |
|---|---|

| Note | You cannot rename a Stock folder or a Stock report. |
|---|---|

| Note | Applies to the root-level folder. |
|---|---|

| Note | You can move a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being moved. You cannot move custom folders or reports from within the Stock folder (and its subfolders) to other locations and the other
                                                         way. |
|---|---|

| Note | You can also set the default filter by checking the Set as Default check box in the Choose Filter dialog box during the report run mode. |
|---|---|

| Note | You can delete a Report or a Folder only if you have Edit permission on the parent folder of the Report or Folder being deleted. Stock folder cannot be deleted. Stock report can be deleted. |
|---|---|

| Note | Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. |
|---|---|

| Note | You can access permanent hyperlink only from a web browser. |
|---|---|

| Note | Help files don't support videos and other interactive content. To prevent security risks like Cross-Site Scripting (XSS),
                                          ensure that any HTML files that you upload are free of harmful scripts. |
|---|---|

| Step 1 | From the left
                                       			 navigation pane, click Reports . |
|---|---|
| Step 2 | Click the
                                       			 Ellipsis icon (…) next to the report row for which you want to create the help
                                       			 page and click Add
                                          				Help . |
| Step 3 | In the Add
                                          				Help dialog box, If you
                                                					 want to set an external help page as the report help, select the URL option and enter the external URL location. If you want to upload the help file, select the Choose file option and click Browse to upload a ZIP file (with HTML files). |
| Step 4 | After
                                       			 uploading the file, click Save . Note When you run the report, click the "?" icon (Template Help) on the Reports toolbar to view the configured help file. | Note | When you run the report, click the "?" icon (Template Help) on the Reports toolbar to view the configured help file. |
| Note | When you run the report, click the "?" icon (Template Help) on the Reports toolbar to view the configured help file. |

| Note | When you run the report, click the "?" icon (Template Help) on the Reports toolbar to view the configured help file. |
|---|---|

| Note | You cannot view filters if the Report Designer has selected the Skip filter during the report processing check box during the report filter selection. |
|---|---|

| Report Definition Query Type | Applicable Filter Tabs |
|---|---|
| Database Query | Date & Time, Key Criteria, Field Filters |
| Live Data or Real Time Streaming | Key Criteria, Field Filters |
| Anonymous Block | Parameters |
| Stored Procedure | Parameters |

| Note | Cisco Unified Intelligence Center uses the browser locale to display the Date & Time format in the filter page. If Cisco Unified Intelligence Center does not support the browser locale language, then the locale selected in the Cisco Unified Intelligence Center application is used. |
|---|---|

| Step 1 | After creating the report, click Set Default Filter from the ellipsis Actions . |
|---|---|
| Step 2 | In the Date & Time filter wizard, select the Date Range and Time Range options. The options available in the Date Range and Time Range filter are predefined. Selection of the Custom option allows you to customize the Date Range and Time Range details. You can select the days of the week (Days > Custom) only if the time interval spans more than a day. For reports that are based on the query type Anonymous Block, you cannot select days of the week. For more information, see Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html . |
| Step 3 | Check the Skip filter during the report execution check box if you want to skip filter selection during the running of report. Note In the Choose Filter dialog box (report run mode), you can check the Set as Default check box to set the report filter as the default. | Note | In the Choose Filter dialog box (report run mode), you can check the Set as Default check box to set the report filter as the default. |
| Note | In the Choose Filter dialog box (report run mode), you can check the Set as Default check box to set the report filter as the default. |
| Step 4 | Click Next . |

| Note | In the Choose Filter dialog box (report run mode), you can check the Set as Default check box to set the report filter as the default. |
|---|---|

| Note | Key Criteria fields are predefined filters and are displayed in the filter screen if they are defined in the Report Definition. |
|---|---|

| Step 1 | After creating the report, click Set Default Filter from the ellipsis Actions . |
|---|---|
| Step 2 | In the Date & Time filter wizard, select the Date Range and Time Range options and click Next . |
| Step 3 | In the Key Criteria filter wizard, select the collections or values from the Available selection box. Note Do not set multiple filter parameters; set any one filter parameter. | Note | Do not set multiple filter parameters; set any one filter parameter. |
| Note | Do not set multiple filter parameters; set any one filter parameter. |
| Step 4 | Use the arrows to move the selected collections or values to the Selected selection box. |
| Step 5 | You can also select multiple collections or values. |
| Step 6 | Click Next . |

| Note | Do not set multiple filter parameters; set any one filter parameter. |
|---|---|

| Note | You can configure Field Filters in reports: Only for SQL Query based reports. To filter a text, date, boolean, or a decimal field. |
|---|---|

| Step 1 | After creating the report, click Set Default Filter from the ellipsis Actions . |
|---|---|
| Step 2 | In the Date & Time filter wizard, select the Date Range and Time Range options and click Next . |
| Step 3 | In the Key Criteria filter wizard, select the collections or values from the Available selection box and click Next . |
| Step 4 | In the Field Filters wizard, select the filter according to the following criteria. Filter criteria/operators depend on the selected field type (date, numeric/decimal, boolean, or string). For Date , the options available in Date Range filter are predefined. Using the Date Range drop-down list, select from Custom, Today,
                                                   Yesterday, This Week, Last Week, This Month, Last Month, Year to Date, or Last Year. Only Custom will allow the user to customize the Calendar, Time Range and Days certain days of the week. For Decimal , select an Operator from Equal To, Not Equal To, Less Than, Less Than or Equal To, or Greater Than and then enter a value;
                                                   for example, Operator = Greater Than and Value = 16.5. For String , select an Operator from Equal To, Not Equal To, or Matches and then enter a value for the string; for example, Operator
                                                   = Matches and Value = Team Green. If you select Matches as the Operator, you must specify an SQL pattern to match the string field. The system appends the wild
                                                         card character % automatically to the beginning and end of the string. You can also use any SQL wild card pattern in between
                                                         the string. If the filter field is associated with a Value List , then specify any value or move one, all, or some items in the list to the Selected column to filter. Note Use only the Matches operator to filter the report data records with leading or trailing spaces. Do not use the Equal To or
                                                               Not Equal To operators in such scenarios as Unified Intelligence Center trims the filter criteria before running the SQL query
                                                               and hence does not fetch the matching results. For Boolean , select True or False from the Operator list. | Note | Use only the Matches operator to filter the report data records with leading or trailing spaces. Do not use the Equal To or
                                                               Not Equal To operators in such scenarios as Unified Intelligence Center trims the filter criteria before running the SQL query
                                                               and hence does not fetch the matching results. |
| Note | Use only the Matches operator to filter the report data records with leading or trailing spaces. Do not use the Equal To or
                                                               Not Equal To operators in such scenarios as Unified Intelligence Center trims the filter criteria before running the SQL query
                                                               and hence does not fetch the matching results. |
| Step 5 | Using the Operator drop-down list, select the criteria. Note If you select Matches operator, you can use any Microsoft SQL wildcard pattern to filter the data. The wildcard character % is added to the beginning and end of every string that is used to filter the data. | Note | If you select Matches operator, you can use any Microsoft SQL wildcard pattern to filter the data. The wildcard character % is added to the beginning and end of every string that is used to filter the data. |
| Note | If you select Matches operator, you can use any Microsoft SQL wildcard pattern to filter the data. The wildcard character % is added to the beginning and end of every string that is used to filter the data. |
| Step 6 | In the Value field, enter a value against which the data in the field will be filtered. |
| Step 7 | Click Run . |

| Note | Use only the Matches operator to filter the report data records with leading or trailing spaces. Do not use the Equal To or
                                                               Not Equal To operators in such scenarios as Unified Intelligence Center trims the filter criteria before running the SQL query
                                                               and hence does not fetch the matching results. |
|---|---|

| Note | If you select Matches operator, you can use any Microsoft SQL wildcard pattern to filter the data. The wildcard character % is added to the beginning and end of every string that is used to filter the data. |
|---|---|

| Note | Additional data sources are not supported. |
|---|---|

| Note | The daylight savings time offset depends on the latest system time zone library. |
|---|---|

| Note | Daylight savings start date or end date may (when the data is recorded) create an additional row (in the report output) due
                                             to the time zone value change in the SQL database. This applies to any template report, as well as for any query type (Anonymous
                                             block, Database Query, Stored Procedure, Real Time Streaming) that these template reports would use. For confirmation that
                                             SQL had time zone value change, use the Report Options icon from the report summary page and run the SQL command in AW node
                                             to validate the change in the time zone. |
|---|---|

| Note | You can select one of the predefined grid, gauge, or chart views. For more information on creating/editing views, see Report Views . |
|---|---|

| Note | Live Data reports do not automatically respond to changes in the system time. If the server or client time is changed or adjusted,
                                          the report must be refreshed to accurately display the duration field values. For example, during a daylight saving time (DST)
                                          change, active live data reports do not display correct values in the duration field. Live data reports must be refreshed
                                          to update. |
|---|---|

| Note | By default, reporting users do not have permission to create a subfolder in Reports . An Administrator can create a subfolder and grant access. |
|---|---|

| Step 1 | In the left navigation pane, choose Reports . |
|---|---|
| Step 2 | Navigate to the folder where you want to create the report. |
| Step 3 | From the Reports toolbar, click New > Report . To edit an existing report, navigate to the report, click the ellipsis icon beside the report and click Edit . |
| Step 4 | In the Create New Report window, enter the Report Name and Description . Note The report name must be unique to Cisco Unified Intelligence Center. | Note | The report name must be unique to Cisco Unified Intelligence Center. |
| Note | The report name must be unique to Cisco Unified Intelligence Center. |
| Step 5 | Click Next . |
| Step 6 | In the Basic Details tab, enter or select the report details. Note Use the arrows to select the appropriate Report Definition. | Note | Use the arrows to select the appropriate Report Definition. |
| Note | Use the arrows to select the appropriate Report Definition. |
| Step 7 | Click Next . |
| Step 8 | In the Manage Views tab, create the report views and click Next . For more information, see Report Views . |
| Step 9 | In the Thresholds tab, create report thresholds and click Finish . For more information, see Report Thresholds . The newly created report is listed in the Reports page. |

| Note | The report name must be unique to Cisco Unified Intelligence Center. |
|---|---|

| Note | Use the arrows to select the appropriate Report Definition. |
|---|---|

| Note | Do not delete the Report Definition fields that are currently associated with any of the manually created report views. If
                                          deleted, you must reapply the Data Fields for all the manually created report views to save the report. For default grid views, the deleted field is removed automatically from the Data Fields list retaining any other fields in
                                          the Selected Field list. Hence, no additional action is required to save the report. |
|---|---|

| Note | Grouping and font size is not supported in Live Data reports. |
|---|---|

| Step 1 | Create or edit a report. |
|---|---|
| Step 2 | Enter the report details in the Basic Details screen and click Next . The Manage Views screen appears with a default grid view. Note You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report . | Note | You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report . |
| Note | You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report . |
| Step 3 | You can edit the default view ( Actions column > Edit View ) or click Create New > Grid view to create a new grid view. The Edit Grid View or the New Grid View screen appears depending on your selection for edit or create. |
| Step 4 | Enter the Name and Description in the respective fields. Note Maximum length allowed for the grid view Name : 50 characters. | Note | Maximum length allowed for the grid view Name : 50 characters. |
| Note | Maximum length allowed for the grid view Name : 50 characters. |
| Step 5 | From the Font selection box, you can select the font size from the list to display the grid data. |
| Step 6 | Use the arrow buttons to select fields from the Available value list box to move to the Selected field list. |
| Step 7 | You can use the following features to improve grid view display: Header —Use this feature to add (+) or delete (-) a header for the selected fields. This helps in categorizing the field set. Note You cannot save the view with empty headers. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , any empty headers that exist in the report views in prior releases are not migrated. Edit icon—In the Selected value list box, click the Edit icon (hover on the field value) if you want to edit the Display Name and Column Width for the selected field and click Done . Note For Header fields, you can only edit the Display Name. Sort Grid by Field —Select the Sort Grid by Field check box to sort the selected report columns in either Ascending or Descending order. Selecting this check box enables the drop-down list to be populated with the values from the Selected value list box. You can select only one value for sorting. | Note | You cannot save the view with empty headers. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , any empty headers that exist in the report views in prior releases are not migrated. | Note | For Header fields, you can only edit the Display Name. |
| Note | You cannot save the view with empty headers. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , any empty headers that exist in the report views in prior releases are not migrated. |
| Note | For Header fields, you can only edit the Display Name. |
| Step 8 | Click Save . The Report Views screen appears. |
| Step 9 | Click Finish . |

| Note | You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report . |
|---|---|

| Note | Maximum length allowed for the grid view Name : 50 characters. |
|---|---|

| Note | You cannot save the view with empty headers. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , any empty headers that exist in the report views in prior releases are not migrated. |
|---|---|

| Note | For Header fields, you can only edit the Display Name. |
|---|---|

| Note | Live Data reports do not support chart view. In the vertically oriented charts, for Cyrillic characters, the data labels in the Horizontal Axis field may be hidden or
                                                      garbled. This is a known limitation. Hence, for Cyrillic characters, use the horizontally oriented charts. |
|---|---|

| Step 1 | Create or edit a report. |
|---|---|
| Step 2 | Enter the report details in the Basic Details screen and click Next . The Manage Views screen appears with a default grid view. Note You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report . | Note | You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report . |
| Note | You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report . |
| Step 3 | Click Create New > Chart view . |
| Step 4 | In the Create New Chart View screen, click the required chart type. For more information, see Chart Types . |
| Step 5 | Enter the Chart Information; Name , Description and click Next . Note Maximum length allowed for the chart view Name : 50 characters. For Cartesian type charts (Bar, Column, and Line), select the Group Data check box to group data: By a field —Select this option to create a chart view where the vertical axis shows fields with footer formula configured for line or
                                                                  column chart and horizontal axis with footer formula for bar chart. By label field —Select this option to create a chart view where the vertical axis shows fields of decimal data type for Line or Column chart.
                                                                  In Bar chart, the horizontal axis shows fields of decimal type. Note For Pie charts, you can only Group Data by Label Field . | Note | Maximum length allowed for the chart view Name : 50 characters. For Cartesian type charts (Bar, Column, and Line), select the Group Data check box to group data: By a field —Select this option to create a chart view where the vertical axis shows fields with footer formula configured for line or
                                                                  column chart and horizontal axis with footer formula for bar chart. By label field —Select this option to create a chart view where the vertical axis shows fields of decimal data type for Line or Column chart.
                                                                  In Bar chart, the horizontal axis shows fields of decimal type. | Note | For Pie charts, you can only Group Data by Label Field . |
| Note | Maximum length allowed for the chart view Name : 50 characters. For Cartesian type charts (Bar, Column, and Line), select the Group Data check box to group data: By a field —Select this option to create a chart view where the vertical axis shows fields with footer formula configured for line or
                                                                  column chart and horizontal axis with footer formula for bar chart. By label field —Select this option to create a chart view where the vertical axis shows fields of decimal data type for Line or Column chart.
                                                                  In Bar chart, the horizontal axis shows fields of decimal type. |
| Note | For Pie charts, you can only Group Data by Label Field . |
| Step 6 | In the Add Data Fields screen, select the Label Field from the drop-down list and Data Fields from the list box and click Next . |
| Step 7 | In the Preview and Format screen, enter or select appropriate information based on the selected chart type. For more information, see Chart Types . Note For the following Data Fields, the Column Type (Stacked and Grouped) feature is unavailable. Date and Time Boolean | Note | For the following Data Fields, the Column Type (Stacked and Grouped) feature is unavailable. Date and Time Boolean |
| Note | For the following Data Fields, the Column Type (Stacked and Grouped) feature is unavailable. Date and Time Boolean |
| Step 8 | Click Save . |

| Note | You can access Report permalinks only after completing the report creation. Report permalinks allow you to share your report
                                                            with other users and view reports of other users. For more information, see Permalink for a Report . |
|---|---|

| Note | Maximum length allowed for the chart view Name : 50 characters. For Cartesian type charts (Bar, Column, and Line), select the Group Data check box to group data: By a field —Select this option to create a chart view where the vertical axis shows fields with footer formula configured for line or
                                                                  column chart and horizontal axis with footer formula for bar chart. By label field —Select this option to create a chart view where the vertical axis shows fields of decimal data type for Line or Column chart.
                                                                  In Bar chart, the horizontal axis shows fields of decimal type. |
|---|---|

| Note | For Pie charts, you can only Group Data by Label Field . |
|---|---|

| Note | For the following Data Fields, the Column Type (Stacked and Grouped) feature is unavailable. Date and Time Boolean |
|---|---|

| Chart Type | Chart Information | Add Data Fields | Preview and Format |
|---|---|---|---|
| Bar | Yes | Yes | Yes |
| Column | Yes | Yes | Yes |
| Line | Yes | Yes | Yes |
| Gauge/Numeric | No | Yes Note To configure a Gauge chart, Report Definition must have at least one decimal field with a footer configured. | Note | To configure a Gauge chart, Report Definition must have at least one decimal field with a footer configured. | Yes To set the chart view for Dial Gauge/Numeric, perform the following steps: Enter the Range . By default, min is 0 and max is 100. Define the zones. When the chart value is within any of the defined thresholds, The gauge pointer points to the corresponding color set in the threshold. The Numeric text is displayed in the corresponding color set in the threshold. You can select Dial Gauge or Numeric view for this report. If you select the Numeric view, the values are displayed in decimals by default. To display these values as whole numbers, check the Round up the value to the next whole number check box. Click Save . |
| Note | To configure a Gauge chart, Report Definition must have at least one decimal field with a footer configured. |
| Pie | Yes | Yes Note To configure a Pie chart, Report Definition must have at least one decimal field configured. | Note | To configure a Pie chart, Report Definition must have at least one decimal field configured. | Yes You can select Pie or Donut as the display type for this report. |
| Note | To configure a Pie chart, Report Definition must have at least one decimal field configured. |

| Note | To configure a Gauge chart, Report Definition must have at least one decimal field with a footer configured. |
|---|---|

| Note | To configure a Pie chart, Report Definition must have at least one decimal field configured. |
|---|---|

| Step 1 | From the Manage Views screen , after adding the report views, click Next . The Thresholds screen appears. |
|---|---|
| Step 2 | Select a view to which you want to set the threshold and select the field name from the Create new threshold list. The screen refreshes with a new panel for the selected field name. |
| Step 3 | Select a field operator and set a condition from the Operator list. Operator Description Matches The Matches operator accepts Regular Expressions. Note that the Regular Expressions does not support: Flags (i, g, m, n, y), OR/AND any combinations of these flags. Leading and trailing forward slash (/). Example: Valid Pattern → \w+\s Invalid Pattern → /\w+\s/g (As it contains leading and trailing forward slash (/) and a "g" flag.) String fields; Always, Equal, Not Equal Decimal fields; Always, Equal, Not Equal, Greater Than, Less Than, Greater Than Equal To, Less Than or Equal To, Between In Report Definition, if the %format is defined for any field, then while setting the thresholds for that field, ensure to
                                                      enter the decimal format of the percentage to render the condition in the report. For example: In Report Definition, if %format is defined for the field "SL" (Service Level) and you want to apply thresholds to this field
                                                      to indicate "Red" if SL is less than 60%, set the following: Define the threshold for the SL field. Set the Operator to Less Than. Enter the percentage value as 0.60 . Select “Red” in the No Fill drop-down. Click Done . | Operator | Description | Matches | The Matches operator accepts Regular Expressions. Note that the Regular Expressions does not support: Flags (i, g, m, n, y), OR/AND any combinations of these flags. Leading and trailing forward slash (/). Example: Valid Pattern → \w+\s Invalid Pattern → /\w+\s/g (As it contains leading and trailing forward slash (/) and a "g" flag.) | String fields; Always, Equal, Not Equal Decimal fields; Always, Equal, Not Equal, Greater Than, Less Than, Greater Than Equal To, Less Than or Equal To, Between | In Report Definition, if the %format is defined for any field, then while setting the thresholds for that field, ensure to
                                                      enter the decimal format of the percentage to render the condition in the report. For example: In Report Definition, if %format is defined for the field "SL" (Service Level) and you want to apply thresholds to this field
                                                      to indicate "Red" if SL is less than 60%, set the following: Define the threshold for the SL field. Set the Operator to Less Than. Enter the percentage value as 0.60 . Select “Red” in the No Fill drop-down. Click Done . |
| Operator | Description |
| Matches | The Matches operator accepts Regular Expressions. Note that the Regular Expressions does not support: Flags (i, g, m, n, y), OR/AND any combinations of these flags. Leading and trailing forward slash (/). Example: Valid Pattern → \w+\s Invalid Pattern → /\w+\s/g (As it contains leading and trailing forward slash (/) and a "g" flag.) |
| String fields; Always, Equal, Not Equal Decimal fields; Always, Equal, Not Equal, Greater Than, Less Than, Greater Than Equal To, Less Than or Equal To, Between | In Report Definition, if the %format is defined for any field, then while setting the thresholds for that field, ensure to
                                                      enter the decimal format of the percentage to render the condition in the report. For example: In Report Definition, if %format is defined for the field "SL" (Service Level) and you want to apply thresholds to this field
                                                      to indicate "Red" if SL is less than 60%, set the following: Define the threshold for the SL field. Set the Operator to Less Than. Enter the percentage value as 0.60 . Select “Red” in the No Fill drop-down. Click Done . |
| Step 4 | Choose the options from No Fill and edit the threshold fields. Note You can set conditions on the same or different fields: condition on same field: threshold and condition on the same field. condition on different field: threshold for a field, based on the condition on the different field. multi conditions on same field: apply threshold for a field based on the condition on different fields. Caution When you upgrade to Unified Intelligence Center version 11.6 or later, all the threshold colors are retained for reports that
                                                         are created in the earlier versions. But, when you modify the threshold, all the old threshold color selection are lost within
                                                         the report. Hence, you must reconfigure the threshold color selection for that report. For existing reports, perform the above mentioned steps to add more thresholds. Note Threshold configuration supports upto 30 thresholds for a field. To edit an existing threshold from a report run already, click Report options and select Manage Thresholds. | Note | You can set conditions on the same or different fields: condition on same field: threshold and condition on the same field. condition on different field: threshold for a field, based on the condition on the different field. multi conditions on same field: apply threshold for a field based on the condition on different fields. | Caution | When you upgrade to Unified Intelligence Center version 11.6 or later, all the threshold colors are retained for reports that
                                                         are created in the earlier versions. But, when you modify the threshold, all the old threshold color selection are lost within
                                                         the report. Hence, you must reconfigure the threshold color selection for that report. | Note | Threshold configuration supports upto 30 thresholds for a field. |
| Note | You can set conditions on the same or different fields: condition on same field: threshold and condition on the same field. condition on different field: threshold for a field, based on the condition on the different field. multi conditions on same field: apply threshold for a field based on the condition on different fields. |
| Caution | When you upgrade to Unified Intelligence Center version 11.6 or later, all the threshold colors are retained for reports that
                                                         are created in the earlier versions. But, when you modify the threshold, all the old threshold color selection are lost within
                                                         the report. Hence, you must reconfigure the threshold color selection for that report. |
| Note | Threshold configuration supports upto 30 thresholds for a field. |
| Step 5 | Format the text in the field to appear when it matches the threshold condition. Use the following options: Text Bold —Select this check box to highlight the report field in bold. Text/Background Color —Select a color from the drop-down for the text/background color in the field. Text Substitute —Enter a new string if you want the text in the field to be replaced with it when it matches the threshold condition. Syntax to add an html hyperlink as text substitute: < a href=https://www.cisco.com target=_blank>cisco</a> Syntax to add an empty space as text substitute: &nbsp; Image Location —Enter the URL path of the image if you want the text to be replaced with an image. Note Supports only image URLs reachable from Unified Intelligence Center server. Maximum size limit allowed for the image is 5MB. | Note | Supports only image URLs reachable from Unified Intelligence Center server. Maximum size limit allowed for the image is 5MB. |
| Note | Supports only image URLs reachable from Unified Intelligence Center server. Maximum size limit allowed for the image is 5MB. |
| Step 6 | Click Done . |
| Step 7 | Click Finish . |

| Operator | Description |
|---|---|
| Matches | The Matches operator accepts Regular Expressions. Note that the Regular Expressions does not support: Flags (i, g, m, n, y), OR/AND any combinations of these flags. Leading and trailing forward slash (/). Example: Valid Pattern → \w+\s Invalid Pattern → /\w+\s/g (As it contains leading and trailing forward slash (/) and a "g" flag.) |
| String fields; Always, Equal, Not Equal Decimal fields; Always, Equal, Not Equal, Greater Than, Less Than, Greater Than Equal To, Less Than or Equal To, Between | In Report Definition, if the %format is defined for any field, then while setting the thresholds for that field, ensure to
                                                      enter the decimal format of the percentage to render the condition in the report. For example: In Report Definition, if %format is defined for the field "SL" (Service Level) and you want to apply thresholds to this field
                                                      to indicate "Red" if SL is less than 60%, set the following: Define the threshold for the SL field. Set the Operator to Less Than. Enter the percentage value as 0.60 . Select “Red” in the No Fill drop-down. Click Done . |

| Note | You can set conditions on the same or different fields: condition on same field: threshold and condition on the same field. condition on different field: threshold for a field, based on the condition on the different field. multi conditions on same field: apply threshold for a field based on the condition on different fields. |
|---|---|

| Caution | When you upgrade to Unified Intelligence Center version 11.6 or later, all the threshold colors are retained for reports that
                                                         are created in the earlier versions. But, when you modify the threshold, all the old threshold color selection are lost within
                                                         the report. Hence, you must reconfigure the threshold color selection for that report. |
|---|---|

| Note | Threshold configuration supports upto 30 thresholds for a field. |
|---|---|

| Note | Supports only image URLs reachable from Unified Intelligence Center server. Maximum size limit allowed for the image is 5MB. |
|---|---|

| Action | Description |
|---|---|
| Report options |
| Edit View | Displays the Edit View dialog box. You can modify the current report view and click Done to instantly view the modified view. |
| Save View As | Clones the existing report view. In the Save View dialog box, enter the Name and Description for the cloned view and click Save . The report page refreshes with the cloned view. |
| Create Chart View | For the report that is run, you can directly create a chart view if you have Edit permissions. After you create the chart view, the report page refreshes with the newly created chart view and gets listed
                                          in the view list. Note This feature is disabled for Live Data reports. For more information, see Create a Chart View . | Note | This feature is disabled for Live Data reports. |
| Note | This feature is disabled for Live Data reports. |
| Group By | Add/remove/update grouping configurations for the current view (columns). Cisco Unified Intelligence Center grid reports support
                                          up to three levels of grouping. If you are grouping the column with Date or Date time data type, you can group records on a Daily/Weekly/Monthly basis. For more information, see Group By . |
| Manage Thresholds | Sets a threshold indicator for a field to display if the field value meets the threshold condition. Threshold indicators can
                                          be set only for views of type Grid and Gauge. For more information, see Report Thresholds . |
| SQL | Displays the SQL code used to run this report. |
| Export | Exports the already run grid report data into your local disk in a .xls x format. Note When you export a report to an Excel file format, to read the exported report, the client system’s locale must match with
                                                            the browser’s locale (where you had exported the report). When reports are exported to excel in Report viewer, the custom formatting of DECIMAL data type is not applied. Report consists of predefined formats for Date and Time. When a report is exported to Microsoft Excel, only five predefined
                                                            Date and Time formats are supported. The supported formats are: dd/mm/yy mmm-yy h:mm AM/PM h:mm:ss AM/PM mm/dd/yyyy hh:mm:ss If you have exported a report with a Date and Time format which is not supported by Excel, Excel's General format is applied by default. | Note | When you export a report to an Excel file format, to read the exported report, the client system’s locale must match with
                                                            the browser’s locale (where you had exported the report). When reports are exported to excel in Report viewer, the custom formatting of DECIMAL data type is not applied. Report consists of predefined formats for Date and Time. When a report is exported to Microsoft Excel, only five predefined
                                                            Date and Time formats are supported. The supported formats are: dd/mm/yy mmm-yy h:mm AM/PM h:mm:ss AM/PM mm/dd/yyyy hh:mm:ss If you have exported a report with a Date and Time format which is not supported by Excel, Excel's General format is applied by default. |
| Note | When you export a report to an Excel file format, to read the exported report, the client system’s locale must match with
                                                            the browser’s locale (where you had exported the report). When reports are exported to excel in Report viewer, the custom formatting of DECIMAL data type is not applied. Report consists of predefined formats for Date and Time. When a report is exported to Microsoft Excel, only five predefined
                                                            Date and Time formats are supported. The supported formats are: dd/mm/yy mmm-yy h:mm AM/PM h:mm:ss AM/PM mm/dd/yyyy hh:mm:ss If you have exported a report with a Date and Time format which is not supported by Excel, Excel's General format is applied by default. |
| Report menu |
| Run or Pause the report | Click to run or pause the report respectively. Note Report running times out after three minutes. Rerun the report by modifying the filter, and if the problem persists, contact
                                                      your administrator. | Note | Report running times out after three minutes. Rerun the report by modifying the filter, and if the problem persists, contact
                                                      your administrator. |
| Note | Report running times out after three minutes. Rerun the report by modifying the filter, and if the problem persists, contact
                                                      your administrator. |
| Print Report | Prints the report using your default printer. Note Reports in chart view supports only landscape mode in A3 size paper for printing. | Note | Reports in chart view supports only landscape mode in A3 size paper for printing. |
| Note | Reports in chart view supports only landscape mode in A3 size paper for printing. |
| Manage Filters | Displays Choose Filter dialog box to modify filter criteria for this report. For more information, see Report Filters . |
| Refresh | Refreshes the Report page. |
| View Filter Information | Displays the filter information of the report. |
| Online Help | Displays the configured template help. You can configure template help for the report from the Reports page > Add Help . For more information, see Add Template Help . |
| Only Thresholds | Enable this toggle button to view only rows with matching threshold values in the report. By default, this check box is unchecked for every report. Note This button is disabled for the grouped view. | Note | This button is disabled for the grouped view. |
| Note | This button is disabled for the grouped view. |

| Note | This feature is disabled for Live Data reports. |
|---|---|

| Note | When you export a report to an Excel file format, to read the exported report, the client system’s locale must match with
                                                            the browser’s locale (where you had exported the report). When reports are exported to excel in Report viewer, the custom formatting of DECIMAL data type is not applied. Report consists of predefined formats for Date and Time. When a report is exported to Microsoft Excel, only five predefined
                                                            Date and Time formats are supported. The supported formats are: dd/mm/yy mmm-yy h:mm AM/PM h:mm:ss AM/PM mm/dd/yyyy hh:mm:ss If you have exported a report with a Date and Time format which is not supported by Excel, Excel's General format is applied by default. |
|---|---|

| Note | Report running times out after three minutes. Rerun the report by modifying the filter, and if the problem persists, contact
                                                      your administrator. |
|---|---|

| Note | Reports in chart view supports only landscape mode in A3 size paper for printing. |
|---|---|

| Note | This button is disabled for the grouped view. |
|---|---|

| Note | Live data reports don’t support grouping. Grouped fields cannot be hidden. |
|---|---|

| Step 1 | From the report that is run, click the Report options icon and select the Group By option. |
|---|---|
| Step 2 | In the Group By dialog box, specify the Number of Levels you want to group the report. Depending on the number of levels selected, the Level, Grouped By, Sub Group, and Show Expanded columns are activated. Cisco Unified Intelligence Center grid reports support up to three levels of grouping. |
| Step 3 | To group the report data by values in a particular column, select the required column name from the Grouped By list. If you select a date or date and time value from the list, you can select any one of the following from the Sub Group column: None—The report data is grouped by the absolute date or date time values. Daily—The report data is grouped by day. Weekly—The report data is grouped by week. Monthly—The report data is grouped by month. By default, the Show Expanded option is selected and you can uncheck the option if necessary. The Show Expanded column allows you to view the reports that are run with the group expanded. Enable the Show Summary Only toggle button to display only the summary row in the report. For example, if you group by Agent Team and enable the Show Summary Only toggle button, only the summary data row for each team is displayed. Note If any of the fields have a footer formula defined in the report definition, then a group level summary is also displayed
                                                      for such fields using that formula. | Note | If any of the fields have a footer formula defined in the report definition, then a group level summary is also displayed
                                                      for such fields using that formula. |
| Note | If any of the fields have a footer formula defined in the report definition, then a group level summary is also displayed
                                                      for such fields using that formula. |
| Step 4 | Click Save . Note For the grouped view, the Only Thresholds check box is disabled. Thresholds aren’t displayed in a grouped field and on summary rows. You cannot perform a drill-down from a report with grouped fields. | Note | For the grouped view, the Only Thresholds check box is disabled. Thresholds aren’t displayed in a grouped field and on summary rows. You cannot perform a drill-down from a report with grouped fields. |
| Note | For the grouped view, the Only Thresholds check box is disabled. Thresholds aren’t displayed in a grouped field and on summary rows. You cannot perform a drill-down from a report with grouped fields. |

| Note | If any of the fields have a footer formula defined in the report definition, then a group level summary is also displayed
                                                      for such fields using that formula. |
|---|---|

| Note | For the grouped view, the Only Thresholds check box is disabled. Thresholds aren’t displayed in a grouped field and on summary rows. You cannot perform a drill-down from a report with grouped fields. |
|---|---|

| Note | Each report template help folder has a size limit of 3 MB. If the folder size exceeds this limit, the system does not load
                                                      the help content. You cannot import Report Filters and Collections. You cannot use the same names for the custom Value List, Report, or Report Definition that exist in the stock report templates.
                                                      If the same names are used, it leads to the stock report template import failure. |
|---|---|

| Step 1 | In the left navigation pane, choose Reports . |
|---|---|
| Step 2 | In the Reports listing page, click Import . |
| Step 3 | Click Browse to select the file (.xml or .zip format) to be imported. Note The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB. | Note | The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB. |
| Note | The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB. |
| Step 4 | Select the required file and click Open . |
| Step 5 | Select the file location from the Save to Folder list to save the file. |
| Step 6 | Click Upload . Once the file is successfully uploaded, the table gets populated with the corresponding report template, current available
                                       version, and incoming version of the files being imported. |
| Step 7 | Select a Data Source for the Report Definition only if the Report Definition for the report being imported is not defined
                                       in the Unified Intelligence Center. |
| Step 8 | Select a Data Source for the Value List that is defined in the Report Definition. Note Selection of a Data Source for the Value List is mandatory: If the Value List does not use the same Data Source as the Report Definition. For Real Time Streaming Report Definitions. | Note | Selection of a Data Source for the Value List is mandatory: If the Value List does not use the same Data Source as the Report Definition. For Real Time Streaming Report Definitions. |
| Note | Selection of a Data Source for the Value List is mandatory: If the Value List does not use the same Data Source as the Report Definition. For Real Time Streaming Report Definitions. |
| Step 9 | Select the files to import or overwrite. Overwrite—If the report being imported exists in the Unified Intelligence Center. Import—If the report being imported is the new set of report files. |
| Step 10 | Click Import . Note If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder. Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                            Intelligence Center, report templates continue to work in the upgraded version. Importing manually edited XMLs is not supported. | Note | If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder. Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                            Intelligence Center, report templates continue to work in the upgraded version. Importing manually edited XMLs is not supported. |
| Note | If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder. Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                            Intelligence Center, report templates continue to work in the upgraded version. Importing manually edited XMLs is not supported. |

| Note | The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB. |
|---|---|

| Note | Selection of a Data Source for the Value List is mandatory: If the Value List does not use the same Data Source as the Report Definition. For Real Time Streaming Report Definitions. |
|---|---|

| Note | If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder. Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                            Intelligence Center, report templates continue to work in the upgraded version. Importing manually edited XMLs is not supported. |
|---|---|

| Note | For customized reports, you must update the version numbers of the value list and report definition before you export the
                                                report. Else, the export will not overwrite the existing reports. While exporting folders, ensure that all the Value Lists in the report definitions or folders point to the same data source
                                                respectively. |
|---|---|

| Caution | Do not modify the exported report (XML file) for customization purposes. However, if necessary, you can modify only the EntityVersion
                                          of the Report, Report Definition, and ValueList. |
|---|---|

| Note | Report Filters and Collections are not exported along with the report. |
|---|---|

| Step 1 | From the left navigation panel, click Reports . |
|---|---|
| Step 2 | Navigate to the report or the report folder that you want to export and click the ellipsis icon beside the report and click Export . Note If necessary, you can rename the report or the report folder. Do not change the file extension (Reports or report folder:
                                                      zip). | Note | If necessary, you can rename the report or the report folder. Do not change the file extension (Reports or report folder:
                                                      zip). |
| Note | If necessary, you can rename the report or the report folder. Do not change the file extension (Reports or report folder:
                                                      zip). |
| Step 3 | Click OK . The exported file is downloaded into your specified local folder. |

| Note | If necessary, you can rename the report or the report folder. Do not change the file extension (Reports or report folder:
                                                      zip). |
|---|---|