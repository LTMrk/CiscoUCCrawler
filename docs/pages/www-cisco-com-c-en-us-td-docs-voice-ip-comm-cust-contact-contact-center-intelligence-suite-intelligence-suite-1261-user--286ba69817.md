---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1261-user--286ba69817
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1261/user/guide/cuic_b_report-customization-guide-1261/cuic_b_report-customization-guide-1205_chapter_011.html
retrieved_at: 2026-08-21T12:17:21.320575+00:00
---

Cisco Unified Intelligence Center Report Customization Guide, Release 12.6(1)

# Cisco Unified Intelligence Center Report Customization Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Report Definitions

## Chapter: Report Definitions

# Report Definitions

## Overview

A Report Definition defines the interface for a report. Each report has a Report Definition (database query), which represents
                           how data is retrieved from the data source for that report template. The supported database query types are:

MS SQL query

Stored Procedure query

Anonymous Block query

Real Time Streaming query

In addition to specifying how data is retrieved, a Report Definition contains the data set that is obtained. This includes
                           the fields, filters, formulas, refresh rate, and key criteria field for the report.

Unified Intelligence Center separates Reports from Report Definitions.

Unified Intelligence Center installs a stock Report Definition for each report template.

You cannot rename a Stock Report Definition.

## Report Definition Actions

You can open a maximum of ten tabs at a time.

Action

Description

View and Edit

View —To view Report Definition details and its associated reports, click a Report Definition. The Overview page appears.

All the associated reports (with or without View and Edit permissions) are displayed on the Overview page. Display of all associated reports help in assessing the Report Definition usage across the reports.

Edit —To edit a Report Definition, click Edit on the Overview page. Modifications are applicable to all the associated reports.

In the edit mode, click the icon next to the Report Definition name to edit the Report Definition properties; Name, Description,
                                       and Report Definition Type.

You cannot edit a Stock Report Definition.

Caution

Toolbar Actions

New > Report Definition

Creates a new Report Definition.

The New action is enabled only if you have View and Edit permission for that Report Definition.

For more information, see Create Report Definition .

New > Folder

Creates a new Folder. Use this feature to categorize Report Definitions.

The New action is enabled only if you have View and Edit permission for that folder.

When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                         the folders to which you have the Edit permission.

Refresh

Refreshes the Report Definitions page.

Favorites

Tags the Report Definitions as your Favorites. Click the star icon beside the Report Definition name to add to Favorites .

Search

Searches for a Report Definition.

Ellipsis (…) Actions

Save As

Saves a copy of the Report Definition.

Rename

Renames a Report Definition or a Folder.

Unified Intelligence Center installs a stock Report Definition for each report template. You cannot rename a Stock Report
                                                   Definition.

Permissions

Assigns appropriate permissions to access and manage the Report Definition.

Groups —Grants View and Edit permissions for the Report Definition.

Security Administrators can grant these permissions to various groups.

Entity owners can grant these permissions to groups that they are directly associated with.

Users —Grants View and Edit permissions for the Report Definition to various users. Applicable only to Security Administrators.

Higher permissions (View and Edit) from either an individual user or the user group takes precedence.

Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups .

When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes.

Move

Moves Report Definition or Folder from one folder to another.

You can move a Report Definition or a Folder only if you have Edit permission on the parent folder of the Report Definition or Folder being moved.

Deletes a Report Definition or a Folder. To delete a Report Definition or a Folder, the following conditions are applicable:

You must have Edit permission on the parent folder of the Report Definition or folder being deleted.

Reports must not be associated with the Report Definition or the folder.

Required roles and permissions for Stock Report Definitions or Folders:

User Roles—System Configuration Administrator, Report Definition Designer

Permissions— Edit permissions to that specific Report Definition or folder and the immediate parent folder.

Required roles and permissions for Custom Report Definitions or Folders:

User Roles—Report Definition Designer

Permissions— Edit permissions to that specific Report Definition or folder and the immediate parent folder.

## Create Report Definition

Report Definitions are based on the following query types:

SQL Query—A simple database query used widely in most of the Report Definitions.

Anonymous Block—A block of queries that are written to pull specific data.

Stored Procedure—Predefined procedure written to get specific data.

Real Time Streaming—A special query used to get data from streaming data source that push data in real time.

Ensure that you don't use SQL queries that modify the existing database connection.

To create a new Report Definition, perform the following steps:

Step 1

In the left navigation pane, choose Report Definitions .

Step 2

Navigate to the folder where you want to create the Report Definition.

Step 3

From the Report Definition toolbar, click New > Report Definition .

Step 4

In the Create New Report Definition window, enter the Report Definition Name and Description .

Step 5

Select the required Report Definition Type :

SQL Query

Anonymous Block

Stored Procedure

Real Time Streaming

Step 6

Click Next .

Step 7

In the Data Source and Query tab, select the appropriate Data Source and enter the Query .

Ensure to select an Online data source.

For more information, see Datasource and Query Tab .

Step 8

Click Next to validate the query and retrieve Parameters or Fields depending on the selected Report Definition Type.

Parameters for Stored Procedure and Anonymous Block query only.

Fields for SQL and Real Time Streaming query only.

Step 9

In the Parameters tab, you can edit and reorder the parameters (if necessary) that are generated from a Stored Procedure or an Anonymous Block.
                                       For more information, see Parameters Tab .

Step 10

Click Next to validate the parameters and create Fields.

Step 11

In the Fields tab, you can:

Manage the retrieved fields.

Create formula and filter fields.

Edit the field properties and the field formatting.

Step 12

Click Next .

Step 13

In the Properties tab, set additional properties for the Report template. For more information, see Properties Tab .

Step 14

Click Save .

### Datasource and Query Tab

Report Definition Type

Action

SQL Query

Choose the appropriate data source and provide a valid database query for the Report Definition.

Select an Online data source.

Maximum length that is supported for the database query type is 25000 characters (including whitespace).

Click Next to view the fields derived from the query in the Fields tab.

Anonymous Block

Choose the appropriate data source and enter the database query incorporating a parameter.

Maximum length that is supported for the Anonymous Block query type is 25000 characters (including whitespace).

Parameter names in the anonymous block must have a colon followed by the parameter name.

Example: :paramName . Unified Intelligence Center substitutes the colon at the beginning of the parameter name with the at sign (@).

Click Next to display the list of parameters in the Parameters tab.

Stored Procedure

Choose the appropriate data source and enter the name of the stored procedure. Ensure that the stored procedure location is
                                          accessible by Unified Intelligence Center.

Click Next to display the list of parameters in the Parameters tab.

Real Time Streaming

Choose the Streaming data source and the topic to display the associated list of fields. Check the required fields.

You can choose only one topic per Report Definition.

Key Routing Field

Represented by the key icon, this field is checked and disabled. Composite key fields are associated to this field depending
                                          on the field selection from the nested objects in the topic.

When you check a field, the composite field is also checked.

When you uncheck a field, the associated composite field remains checked.

When you uncheck the composite field, all its member fields are unchecked.

Conditional Duration Fields

Conditional Duration fields update the field’s value continually based on a condition that is defined by the parent field.
                                          A conditional duration field is always associated with a parent field.

Example:

Parent field – state

Conditional duration field – readyTime

The readyTime field is updated continually based on the value of the parent state field. That is, if state is READY , then the duration of the readyTime is continually updated. If state is NOT READY , then updates to readyTime is paused.

When you check a conditional duration field, it's parent field is also checked.

When you uncheck a conditional duration field, it's parent field remains checked.

When you uncheck a parent field, all the conditional duration fields which depend on that field will also get unchecked.

Click Next to view the selected fields in the Fields tab.

ANSI_NULLS: ON

QUOTED_IDENTIFER: ON

ROWCOUNT: 0

To change any of these values, set the appropriate values in the custom SQL query.

### Parameters Tab

Use the Parameters tab to edit and reorder the parameters that are generated from a Stored Procedure or an Anonymous Block. Parameters are used
                                 as filters when you run the report.

The generated list of Parameters are associated with the following attributes;

Attributes

Description

Name

The Parameter name.

Reorder icon

Drag and drop the reorder icon to the required row position. This order reflects the parameters displayed in the report filter
                                             page.

The reorder icon is visible only on the first row of the parameter list. For the subsequent rows, the reorder icon is visible
                                                         when you hover over the parameter row.

Display Name

Appears in the report filter.

Format: Display Name (Field Name)

Example: Agent_Login_Start_Date (@param1)

Click the pencil icon to edit the Display Name.

Supports only alphanumeric characters.

The pencil icon is visible only on the first row of the parameter list. For the subsequent rows, the pencil icon is visible
                                                               when you hover over the Display Name.

Data Type

The associated Data Type. For the Anonymous Block query type, select a different Data Type from the list, if necessary.

Sample Value

The associated sample value pre-populated for each datatype. If necessary, modify the sample value.

Value List

The associated value list.

Once the parameter is associated with a value list, Unified Intelligence Center displays the value lists on the Filters wizard
                                             provided that user has View permission for the value lists.

Use this column to:

Associate a value list (Click the plus icon.). For more information, see Associate Value List .

Edit the associated value list (Click on the value list name.).

Delete a value list (Click the minus icon that appears when you hover on the value list name.).

Actions

Allows you to edit or delete the parameter.

Edit —Edits the Parameter properties. The fields on the Edit Parameter window vary based on the data type. For more information, see Edit Paramter Properties .

#### Associate Value List

Once you have associated a value list to a field or a parameter, Unified Intelligence Center displays the value lists on the
                                    filters wizard provided that user has View permission for the Value Lists.

To associate a value list:

Step 1

From the Parameters or Fields tab, click the plus icon in the Value List column.

Step 2

In the Attach Value List window, select or type the appropriate values for the following fields:

Field

Description

Value List

This list is populated based on the logged in user's permissions.

Only fields of type string and decimal can be associated with a value list.

In stock report templates, this field is populated with the stock value list for the Report Definition.

Value Delimiter

Type the delimter (character) to be placed between each value when a value list is passed to the stored procedure or anonymous
                                                            block.

Allow only Single Value selection in filters

Limits the parameter value selection to only one value in the Value list selection filter.

That is, for a report definition, when you enable this check box for a parameter, the user can select only one value for that
                                                            parameter in the Value list selection box.

This check box is enabled only after selecting a value in the Value List list.

Quote Values

Surrounds the parameter with two additional single quotation marks when the value is passed to the stored procedure or anonymous
                                                            block. The first single quotation mark is used to escape the second single quotation mark.

Step 3

Click Done .

#### Edit Parameter Properties

Parameter Property

Description

Description

Description of the parameter.

Hard-coded value

Hard-coded value to be passed as a parameter value when running a report based on an Anonymous Block or Stored Procedure report
                                             definition.

To pass null as a hard-coded value, leave this field blank and check the Pass NULL value for empty string check box. Entering a hard-coded value hides this parameter in the filter page.

Format Field

Choose a date, time, or date and time format from the list.

Required

Check to indicate that this parameter is required.

Pass NULL value for empty string

This check box is enabled only when the parameter is not required or has no value. When the parameter is populated, this field
                                             is disabled and the value is passed.

Automatic Parameter

Choose from the following values for STRING type fields in a Stored Procedure Report Definition type:

Current User Name

Current User Timezone

Relative Date Range

Specify the date range using the Start Date and End Date fields. For more information, see Relative Date and Days Filtering for Anonymous Blocks and Stored Procedures section.

##### Relative Date and Days Filtering for Anonymous Blocks and Stored Procedures

For reports based on Anonymous Blocks and Stored Procedures, the following illustration helps to understand how to populate
                                    the relative dates in the report filters.

Dates—

Select Start Date and enter a Display Name . Select End Date and enter the identical Display Name .

For example, Agent_Login_Start_Date and Agent_Login_End_Date with the same display name Agent_Login_Date .

The dates appearing with the same display name are grouped and shown as a Relative Date Range. A single Stored Procedure or
                                                Anonymous Block can have as many such pairs as required.

Specify Agent_Login_Date as the display name to Agent_Login_Start_Date and Agent_Login_End_Date.

Specify Agent_Login_Date as the display name to Log_Out_Interval_Start_Date and Log_Out_Interval_End_Date (instead of Last_Login_Date).

Note that the Unified Intelligence Center does not display the parameters Log_Out_Interval_Start_Date and Log_Out_Interval_End_Date
                                                                  in a pair.

Days —Use the Days parameter to specify an optional day of the week parameter. The Days parameter is not mandatory. This parameter
                                          must be:

String type

Prefixed with the same display name as other parameters in the same date range.

Appended with _Days

For example, for the Days parameter, you can define the display name as Agent_Login_Date_Days, which is appended with _Days
                                          and with the same display name Agent_Login_Date as defined for the two parameters Agent_Login_Start_Date and Agent_Login_End_Date.

### Fields Tab

Use the Fields tab to manage the following fields generated from a Stored Procedure, Anonymous Block, or SQL Query:

Query Fields—represent a field in a database table. You cannot create or delete a Query field.

Formula Fields—represent custom fields that compute and return a value.

Filter Fields—represent custom fields that appear on the Advanced Reporting Options tab on the Filter page.

#### Field Actions

Action

Description

Toolbar Actions

Search

Searches for a field.

All

Lists all fields. The Field Type column displays the associated data type and the corresponding field types. These field types are represented in the form
                                             of icons:

Key Criteria Field or Key Routing Field

Composite Field

Historical Key Field

Filter Field

Formula Field

Drilldown Linked

Conditional Duration Fields

Filter

Lists all filter fields.

Formulae

Lists all formula fields.

Drilldowns

Lists all fields with linked drilldowns.

New

Filter Field —Creates a filter field that is based on the selected Data Type. Use filters while running reports to get specific data. Filter
                                                   fields are indicated with Filter icon in the Fields tab > Field Type column.

For more information, see Field Properties .

Formula Field —Creates a computed field that appears in the list of fields. Formula fields are indicated with Formula icon in the Fields tab > Field Type column.

For more information, see Field Properties and Formula Creation Guidelines .

Attach or delete value lists for a field (if the Report Definition is based on a query). For more information, see Associate Value List .

Edit the formatting for the Query fields and Formula fields. For more information, see Field Properties .

Ellipsis (…) Actions

Edit

Edits the field details. The editable properties vary for a Query, Filter, or a Formula field. For more information, see Field Properties .

Drilldowns

Manages drilldowns. Drilldowns allow you to create links from one report (grid) to another report (grid or chart) so that
                                             you can launch a sub-report from within the current browser window.

You cannot drill down from or to a gauge report.

You cannot drill down to a report based on an Anonymous Block or a Stored Procedure query type.

You cannot drill down from or to a report based on the Real Time Streaming query type.

Delete

Deletes a field.

#### Field Properties

The following table lists each field property and its definition. Field properties vary based on the Field Type.

Field Property

Field Type

Definition

Name

All

The default database name.

Display Name

All

Appears as the column header for the field on the Filter page when generating a report. Click the pencil icon to edit the Display Name.

Supports only alphanumeric characters.

The pencil icon is visible only on the first row of the parameter list.

For the subsequent rows, the pencil icon is visible when you hover over the Display Name.

Description

All

Enter the field description.

Data Type

Formula

Choose the data type for the field from the list. Available Data Types are: DECIMAL, STRING, NUMBER, DATE, DATETIME, and BOOLEAN.

This setting determines the options that are displayed for this field on the Fields tab.

Data Clause

Query and Filter fields only

Identifies which column in the data set is bound to this field. The SQL Parser uses this value when retrieving data from the
                                                database.

For Filter fields, specify the data clause. For Query fields, this value is auto populated from the query.

Data clause is limited to a maximum of 1000 characters (including whitespace).

Value List

Query and Filter fields only

Click the plus icon in the Value List column. In the Attach Value List window, select or type the appropriate values for the following fields. For more information, see Associate Value Lists .

When a field is associated with a Value List, report users can filter the report with one or more fields from that Value List
                                                or its Collections.

Format | Footer

Query and Formula fields only

Click the pencil icon to edit the formatting for the field and the footer.

Format —Provides a list of default formatting masks. The available formats depend on the data type. For example, for Numeric values, you can select all possible display formats. For Custom selection, you can enter the format in the Custom Format text box.

Footer —The formula to use in the footer. Options are None, Average, Sum, Count, Minimum, and Custom Formula. The available options
                                                      depend on the data type.

For footer formulae, ensure to apply aggregate functions to the columns. For example: SUM(${Field1})/(SUM(${Field2})+SUM(${Field3}))

For the Custom footer, the following fields appear:

Default Custom Footer Formula —Enter the footer formula to be applied when columns are grouped. This column does not have a custom footer formula defined
                                                            for that level.

Group 1 Custom Footer Formula —Enter the footer formula to be applied if this column is in the first level of grouping.

Group 2 Custom Footer Formula —Enter the footer formula to be applied if this column is in the second level of grouping.

Group 3 Custom Footer Formula —Enter the footer formula to be applied if this column is in the third level of grouping.

Allow to show if invisible

Query and Formula fields only

Uncheck this check box to hide from the Available fields panel. Check for the field to appear (retain) on the list of Available fields in the Grid Editor.

Available in Filter

All

Check to add the field to the Field Filters tab while choosing filters.

Select from Available Fields

Formula

Select a field from the list and click the arrow button to insert it into the Formula Syntax field.

Formula Syntax

Formula

Displays operators that construct a formula for the fields you have selected. For more information, see Formula Creation Guidelines .

For reports that use dynamic headers (headers whose content includes dynamic content), provide the SQL field name as part
                                    of the header name in the Report Definition > Fields tab. The column name is surrounded by curly braces so that users can easily find dynamic content within the header.

Click Done to save the selections for that field only.

#### Default Formatting

The available formats depend on the data type of the field as set in Create Filter Field dialog box. For example, for numeric values the drop-down menu offers possible display formats for numeric values. Selecting
                                    (Custom) from this list applies the format string supplied in the Custom Format String to the value returned. The custom formats
                                    supported are as follows:

String data type : Adds a string before the string value. For example, if there is a String field called name where it lists the name of the doctors and if you want to append Dr. to the doctors' names in the report, then use custom format for this field and enter the value Dr. The resulting report displays all names as Dr. XXXX .

Decimal data type : Unified Intelligence Center supports decimal data formatting in accordance with the Java decimal formatting rules.

The following table lists a few examples of custom formats. The # symbol indicates a digit or nothing if there is no digit
                                          present. The digit shows a digit or 0 if there is no digit present:

Data

Format

Value

123

123456

000123

123456.789

###,###.###

123,456.789

123456.789

###.##

123456.79

123.78

123456.789

000123.780

12345.67

$###,###.###

$12,345.67

12345.67

$1234.56

$12345.67

123

0.0E+0

1.2E2

123

0.0E+00

1.2E02

123

Rs 1234

Rs 123a

1234567.89

1.234,89

1.234.567,89

123456789

1.234.567

123.456.789

#### Formula Creation Guidelines

A formula is an expression that uses operators to perform calculations on the database fields. When created, the formula appears
                                 as a column in the report. Use these basic arithmetic operators to create formulas: + for addition, - for subtraction, * for
                                 multiplication, / for division, and () for grouping operands. Each value in a formula represents a single field within a formula.

Data Types with syntax examples:

Boolean —!${bool1} (Appears as TRUE or FALSE in the user interface. The opposite value appears when negation operand is used.)

Date —${date1} + 24 60 60*1000 (Increments date1 by one day.)

DateTime —DateDiff(${dateTime1},${dateTime2}) (Computes and formats the difference in milliseconds of dateTime1 and dateTime2.)

Decimal

${num1} + ${num2} (Adds the two number fields.)

${num1} - ${num2} (Subtracts the two number fields.)

${num1} / ${num2} * ${num3} (Computes as per the operator's associativity as (${num1}/ ${num2}) * ${num3})

(${num1}) / (${num2}) / (${num3} * ${num4}) - ${num1})

String

${str1} + ${str2} (Concatenates the strings. You cannot subtract, multiply, or divide the strings.)

"<a href=" + ${URL_FIELD} + " target=_blank>" + ${LINK_NAME_FIELD} + "</a>" (Concatenates field values with string constants
                                             to create HTML elements.)

${str1} + ${num1) (Concatenates the str1 and num1 field values.)

Null values are considered as empty.

#### Manage Drilldowns

To create drilldowns, perform the following steps:

Step 1

Click Create .

Step 2

Enter the drilldown name and select the report to link to the drilldown.

Step 3

Click Add Match Field to select the Target Report field and the corresponding (matching) Source Report field. This action filters the target report
                                             that is based on the column value for the matched Source Report field.

For date and time type fields, selecting the Match Date Range option filters the target report that is based on the date range for a historical field of the source report. Available only
                                                            if the source report is a historical report.

Step 4

Click the Save icon. You can edit or delete fields using the respective icons.

Step 5

Click Add Match Field to add more fields and click Next .

Step 6

Set the filter criteria and click Done .

When you create a drilldown, by default, the target report's filter criteria is populated in the drilldown filter screens.
                                                                  During the create process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to the default for that field.

When you edit a drilldown, the target report's current drilldown filter criteria is populated in the drilldown filter screens.
                                                                  During the edit process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to reflect the current drilldown filter criteria
                                                                  for that field.

For more information on setting the filter criteria, see Report Filters section in the Cisco Unified Intelligence Center User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html .

### Properties Tab

Click the Properties tab to set extra properties for the Report template.

Action

Description

Author

Template provider name who created the entity.

Version

Report definition entity version that is currently deployed in Unified Intelligence Center.

Format: x.y (where, x and y are integers). Do not start or end with a decimal point.

Examples: 8.9 or 11.15

Key Criteria Field

Choose to filter the reports based on simple queries.

This field is not enabled for reports based on Anonymous Blocks or Stored Procedures.

You can run a report based on a simple query if the Report Definition does not have a Key Criteria Field defined. However, as the report runs with the default filter, the data fetched can be large.

Real Time or Historical

Choose the report type.

Historical Key Field

Choose for the date and time intervals for the report.

This field is enabled only for the Historical report type.

Although Historical reports can run if this field is left blank, the report returns all data for all dates and the data fetched.
                                                      Only fields of the DATE and DATETIME format are available in this list.

Refresh Rate

Rate at which the report is automatically refreshed (in seconds). The minimum Refresh Rate is 15 seconds for Real Time reports
                                          and 900 seconds for Historical reports. You cannot enter values less than the defaults.

For new report definitions of type historical, the default Refresh Rate is 3600 seconds. For type real time, the default Refresh
                                                      Rate is 900 seconds.

| Note | Unified Intelligence Center installs a stock Report Definition for each report template. You cannot rename a Stock Report Definition. |
|---|---|

| Note | You can open a maximum of ten tabs at a time. |
|---|---|

| Action | Description |
|---|---|
| View and Edit |
| View —To view Report Definition details and its associated reports, click a Report Definition. The Overview page appears. Note All the associated reports (with or without View and Edit permissions) are displayed on the Overview page. Display of all associated reports help in assessing the Report Definition usage across the reports. Edit —To edit a Report Definition, click Edit on the Overview page. Modifications are applicable to all the associated reports. In the edit mode, click the icon next to the Report Definition name to edit the Report Definition properties; Name, Description,
                                       and Report Definition Type. Note You cannot edit a Stock Report Definition. Caution Ensure to save changes while editing data in the Fields and the Parameters tabs. Without saving the modified data, if you edit the query in the Datasource and Query tab and click Next , then the data that is edited is lost. | Note | All the associated reports (with or without View and Edit permissions) are displayed on the Overview page. Display of all associated reports help in assessing the Report Definition usage across the reports. | Note | You cannot edit a Stock Report Definition. | Caution | Ensure to save changes while editing data in the Fields and the Parameters tabs. Without saving the modified data, if you edit the query in the Datasource and Query tab and click Next , then the data that is edited is lost. |
| Note | All the associated reports (with or without View and Edit permissions) are displayed on the Overview page. Display of all associated reports help in assessing the Report Definition usage across the reports. |
| Note | You cannot edit a Stock Report Definition. |
| Caution | Ensure to save changes while editing data in the Fields and the Parameters tabs. Without saving the modified data, if you edit the query in the Datasource and Query tab and click Next , then the data that is edited is lost. |
| Toolbar Actions |
| New > Report Definition | Creates a new Report Definition. Note The New action is enabled only if you have View and Edit permission for that Report Definition. For more information, see Create Report Definition . | Note | The New action is enabled only if you have View and Edit permission for that Report Definition. |
| Note | The New action is enabled only if you have View and Edit permission for that Report Definition. |
| New > Folder | Creates a new Folder. Use this feature to categorize Report Definitions. Note The New action is enabled only if you have View and Edit permission for that folder. When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                         the folders to which you have the Edit permission. | Note | The New action is enabled only if you have View and Edit permission for that folder. When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                         the folders to which you have the Edit permission. |
| Note | The New action is enabled only if you have View and Edit permission for that folder. When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                         the folders to which you have the Edit permission. |
| Refresh | Refreshes the Report Definitions page. |
| Favorites | Tags the Report Definitions as your Favorites. Click the star icon beside the Report Definition name to add to Favorites . |
| Search | Searches for a Report Definition. |
| Ellipsis (…) Actions |
| Save As | Saves a copy of the Report Definition. |
| Rename | Renames a Report Definition or a Folder. Note Unified Intelligence Center installs a stock Report Definition for each report template. You cannot rename a Stock Report
                                                   Definition. | Note | Unified Intelligence Center installs a stock Report Definition for each report template. You cannot rename a Stock Report
                                                   Definition. |
| Note | Unified Intelligence Center installs a stock Report Definition for each report template. You cannot rename a Stock Report
                                                   Definition. |
| Permissions | Assigns appropriate permissions to access and manage the Report Definition. Groups —Grants View and Edit permissions for the Report Definition. Security Administrators can grant these permissions to various groups. Entity owners can grant these permissions to groups that they are directly associated with. Users —Grants View and Edit permissions for the Report Definition to various users. Applicable only to Security Administrators. Note Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. | Note | Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. |
| Note | Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. |
| Move | Moves Report Definition or Folder from one folder to another. Note You can move a Report Definition or a Folder only if you have Edit permission on the parent folder of the Report Definition or Folder being moved. | Note | You can move a Report Definition or a Folder only if you have Edit permission on the parent folder of the Report Definition or Folder being moved. |
| Note | You can move a Report Definition or a Folder only if you have Edit permission on the parent folder of the Report Definition or Folder being moved. |
| Delete | Deletes a Report Definition or a Folder. To delete a Report Definition or a Folder, the following conditions are applicable: You must have Edit permission on the parent folder of the Report Definition or folder being deleted. Reports must not be associated with the Report Definition or the folder. Required roles and permissions for Stock Report Definitions or Folders: User Roles—System Configuration Administrator, Report Definition Designer Permissions— Edit permissions to that specific Report Definition or folder and the immediate parent folder. Required roles and permissions for Custom Report Definitions or Folders: User Roles—Report Definition Designer Permissions— Edit permissions to that specific Report Definition or folder and the immediate parent folder. |

| Note | All the associated reports (with or without View and Edit permissions) are displayed on the Overview page. Display of all associated reports help in assessing the Report Definition usage across the reports. |
|---|---|

| Note | You cannot edit a Stock Report Definition. |
|---|---|

| Caution | Ensure to save changes while editing data in the Fields and the Parameters tabs. Without saving the modified data, if you edit the query in the Datasource and Query tab and click Next , then the data that is edited is lost. |
|---|---|

| Note | The New action is enabled only if you have View and Edit permission for that Report Definition. |
|---|---|

| Note | The New action is enabled only if you have View and Edit permission for that folder. When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                         the folders to which you have the Edit permission. |
|---|---|

| Note | Unified Intelligence Center installs a stock Report Definition for each report template. You cannot rename a Stock Report
                                                   Definition. |
|---|---|

| Note | Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. |
|---|---|

| Note | You can move a Report Definition or a Folder only if you have Edit permission on the parent folder of the Report Definition or Folder being moved. |
|---|---|

| Note | Ensure that you don't use SQL queries that modify the existing database connection. |
|---|---|

| Step 1 | In the left navigation pane, choose Report Definitions . |
|---|---|
| Step 2 | Navigate to the folder where you want to create the Report Definition. |
| Step 3 | From the Report Definition toolbar, click New > Report Definition . |
| Step 4 | In the Create New Report Definition window, enter the Report Definition Name and Description . |
| Step 5 | Select the required Report Definition Type : SQL Query Anonymous Block Stored Procedure Real Time Streaming |
| Step 6 | Click Next . |
| Step 7 | In the Data Source and Query tab, select the appropriate Data Source and enter the Query . Note Ensure to select an Online data source. For more information, see Datasource and Query Tab . | Note | Ensure to select an Online data source. |
| Note | Ensure to select an Online data source. |
| Step 8 | Click Next to validate the query and retrieve Parameters or Fields depending on the selected Report Definition Type. The validated query retrieves: Parameters for Stored Procedure and Anonymous Block query only. Fields for SQL and Real Time Streaming query only. |
| Step 9 | In the Parameters tab, you can edit and reorder the parameters (if necessary) that are generated from a Stored Procedure or an Anonymous Block.
                                       For more information, see Parameters Tab . |
| Step 10 | Click Next to validate the parameters and create Fields. |
| Step 11 | In the Fields tab, you can: Manage the retrieved fields. Create formula and filter fields. Edit the field properties and the field formatting. For more information, see Fields Tab . |
| Step 12 | Click Next . |
| Step 13 | In the Properties tab, set additional properties for the Report template. For more information, see Properties Tab . |
| Step 14 | Click Save . The created Report Definition appears in the Report Definition Overview page. This page lists the associated reports (if any). |

| Note | Ensure to select an Online data source. |
|---|---|

| Report Definition Type | Action |
|---|---|
| SQL Query | Choose the appropriate data source and provide a valid database query for the Report Definition. Note Select an Online data source. Maximum length that is supported for the database query type is 25000 characters (including whitespace). Click Next to view the fields derived from the query in the Fields tab. | Note | Select an Online data source. Maximum length that is supported for the database query type is 25000 characters (including whitespace). |
| Note | Select an Online data source. Maximum length that is supported for the database query type is 25000 characters (including whitespace). |
| Anonymous Block | Choose the appropriate data source and enter the database query incorporating a parameter. Note Maximum length that is supported for the Anonymous Block query type is 25000 characters (including whitespace). Parameter names in the anonymous block must have a colon followed by the parameter name. Example: :paramName . Unified Intelligence Center substitutes the colon at the beginning of the parameter name with the at sign (@). Click Next to display the list of parameters in the Parameters tab. | Note | Maximum length that is supported for the Anonymous Block query type is 25000 characters (including whitespace). Parameter names in the anonymous block must have a colon followed by the parameter name. Example: :paramName . Unified Intelligence Center substitutes the colon at the beginning of the parameter name with the at sign (@). |
| Note | Maximum length that is supported for the Anonymous Block query type is 25000 characters (including whitespace). Parameter names in the anonymous block must have a colon followed by the parameter name. Example: :paramName . Unified Intelligence Center substitutes the colon at the beginning of the parameter name with the at sign (@). |
| Stored Procedure | Choose the appropriate data source and enter the name of the stored procedure. Ensure that the stored procedure location is
                                          accessible by Unified Intelligence Center. Click Next to display the list of parameters in the Parameters tab. |
| Real Time Streaming | Choose the Streaming data source and the topic to display the associated list of fields. Check the required fields. Note You can choose only one topic per Report Definition. Key Routing Field Represented by the key icon, this field is checked and disabled. Composite key fields are associated to this field depending
                                          on the field selection from the nested objects in the topic. Note When you check a field, the composite field is also checked. When you uncheck a field, the associated composite field remains checked. When you uncheck the composite field, all its member fields are unchecked. Conditional Duration Fields Conditional Duration fields update the field’s value continually based on a condition that is defined by the parent field.
                                          A conditional duration field is always associated with a parent field. Example: Parent field – state Conditional duration field – readyTime The readyTime field is updated continually based on the value of the parent state field. That is, if state is READY , then the duration of the readyTime is continually updated. If state is NOT READY , then updates to readyTime is paused. Note When you check a conditional duration field, it's parent field is also checked. When you uncheck a conditional duration field, it's parent field remains checked. When you uncheck a parent field, all the conditional duration fields which depend on that field will also get unchecked. Click Next to view the selected fields in the Fields tab. Note Attach a value list to the Key Routing Field before you save the field properties. | Note | You can choose only one topic per Report Definition. | Note | When you check a field, the composite field is also checked. When you uncheck a field, the associated composite field remains checked. When you uncheck the composite field, all its member fields are unchecked. | Note | When you check a conditional duration field, it's parent field is also checked. When you uncheck a conditional duration field, it's parent field remains checked. When you uncheck a parent field, all the conditional duration fields which depend on that field will also get unchecked. | Note | Attach a value list to the Key Routing Field before you save the field properties. |
| Note | You can choose only one topic per Report Definition. |
| Note | When you check a field, the composite field is also checked. When you uncheck a field, the associated composite field remains checked. When you uncheck the composite field, all its member fields are unchecked. |
| Note | When you check a conditional duration field, it's parent field is also checked. When you uncheck a conditional duration field, it's parent field remains checked. When you uncheck a parent field, all the conditional duration fields which depend on that field will also get unchecked. |
| Note | Attach a value list to the Key Routing Field before you save the field properties. |

| Note | Select an Online data source. Maximum length that is supported for the database query type is 25000 characters (including whitespace). |
|---|---|

| Note | Maximum length that is supported for the Anonymous Block query type is 25000 characters (including whitespace). Parameter names in the anonymous block must have a colon followed by the parameter name. Example: :paramName . Unified Intelligence Center substitutes the colon at the beginning of the parameter name with the at sign (@). |
|---|---|

| Note | You can choose only one topic per Report Definition. |
|---|---|

| Note | When you check a field, the composite field is also checked. When you uncheck a field, the associated composite field remains checked. When you uncheck the composite field, all its member fields are unchecked. |
|---|---|

| Note | When you check a conditional duration field, it's parent field is also checked. When you uncheck a conditional duration field, it's parent field remains checked. When you uncheck a parent field, all the conditional duration fields which depend on that field will also get unchecked. |
|---|---|

| Note | Attach a value list to the Key Routing Field before you save the field properties. |
|---|---|

| Note | By default, the queries that are sent to SQL server are executed with the following properties: ANSI_NULLS: ON QUOTED_IDENTIFER: ON ROWCOUNT: 0 To change any of these values, set the appropriate values in the custom SQL query. |
|---|---|

| Attributes | Description |
|---|---|
| Name | The Parameter name. |
| Reorder icon | Drag and drop the reorder icon to the required row position. This order reflects the parameters displayed in the report filter
                                             page. Note The reorder icon is visible only on the first row of the parameter list. For the subsequent rows, the reorder icon is visible
                                                         when you hover over the parameter row. | Note | The reorder icon is visible only on the first row of the parameter list. For the subsequent rows, the reorder icon is visible
                                                         when you hover over the parameter row. |
| Note | The reorder icon is visible only on the first row of the parameter list. For the subsequent rows, the reorder icon is visible
                                                         when you hover over the parameter row. |
| Display Name | Appears in the report filter. Format: Display Name (Field Name) Example: Agent_Login_Start_Date (@param1) Click the pencil icon to edit the Display Name. Note Supports only alphanumeric characters. The pencil icon is visible only on the first row of the parameter list. For the subsequent rows, the pencil icon is visible
                                                               when you hover over the Display Name. | Note | Supports only alphanumeric characters. The pencil icon is visible only on the first row of the parameter list. For the subsequent rows, the pencil icon is visible
                                                               when you hover over the Display Name. |
| Note | Supports only alphanumeric characters. The pencil icon is visible only on the first row of the parameter list. For the subsequent rows, the pencil icon is visible
                                                               when you hover over the Display Name. |
| Data Type | The associated Data Type. For the Anonymous Block query type, select a different Data Type from the list, if necessary. |
| Sample Value | The associated sample value pre-populated for each datatype. If necessary, modify the sample value. |
| Value List | The associated value list. Once the parameter is associated with a value list, Unified Intelligence Center displays the value lists on the Filters wizard
                                             provided that user has View permission for the value lists. Use this column to: Associate a value list (Click the plus icon.). For more information, see Associate Value List . Edit the associated value list (Click on the value list name.). Delete a value list (Click the minus icon that appears when you hover on the value list name.). |
| Actions | Allows you to edit or delete the parameter. Edit —Edits the Parameter properties. The fields on the Edit Parameter window vary based on the data type. For more information, see Edit Paramter Properties . |

| Note | The reorder icon is visible only on the first row of the parameter list. For the subsequent rows, the reorder icon is visible
                                                         when you hover over the parameter row. |
|---|---|

| Note | Supports only alphanumeric characters. The pencil icon is visible only on the first row of the parameter list. For the subsequent rows, the pencil icon is visible
                                                               when you hover over the Display Name. |
|---|---|

| Step 1 | From the Parameters or Fields tab, click the plus icon in the Value List column. |
|---|---|
| Step 2 | In the Attach Value List window, select or type the appropriate values for the following fields: Field Description Value List This list is populated based on the logged in user's permissions. Note Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. Value Delimiter Type the delimter (character) to be placed between each value when a value list is passed to the stored procedure or anonymous
                                                            block. Allow only Single Value selection in filters Limits the parameter value selection to only one value in the Value list selection filter. That is, for a report definition, when you enable this check box for a parameter, the user can select only one value for that
                                                            parameter in the Value list selection box. Note This check box is enabled only after selecting a value in the Value List list. Quote Values Surrounds the parameter with two additional single quotation marks when the value is passed to the stored procedure or anonymous
                                                            block. The first single quotation mark is used to escape the second single quotation mark. | Field | Description | Value List | This list is populated based on the logged in user's permissions. Note Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. | Note | Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. | Value Delimiter | Type the delimter (character) to be placed between each value when a value list is passed to the stored procedure or anonymous
                                                            block. | Allow only Single Value selection in filters | Limits the parameter value selection to only one value in the Value list selection filter. That is, for a report definition, when you enable this check box for a parameter, the user can select only one value for that
                                                            parameter in the Value list selection box. Note This check box is enabled only after selecting a value in the Value List list. | Note | This check box is enabled only after selecting a value in the Value List list. | Quote Values | Surrounds the parameter with two additional single quotation marks when the value is passed to the stored procedure or anonymous
                                                            block. The first single quotation mark is used to escape the second single quotation mark. |
| Field | Description |
| Value List | This list is populated based on the logged in user's permissions. Note Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. | Note | Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. |
| Note | Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. |
| Value Delimiter | Type the delimter (character) to be placed between each value when a value list is passed to the stored procedure or anonymous
                                                            block. |
| Allow only Single Value selection in filters | Limits the parameter value selection to only one value in the Value list selection filter. That is, for a report definition, when you enable this check box for a parameter, the user can select only one value for that
                                                            parameter in the Value list selection box. Note This check box is enabled only after selecting a value in the Value List list. | Note | This check box is enabled only after selecting a value in the Value List list. |
| Note | This check box is enabled only after selecting a value in the Value List list. |
| Quote Values | Surrounds the parameter with two additional single quotation marks when the value is passed to the stored procedure or anonymous
                                                            block. The first single quotation mark is used to escape the second single quotation mark. |
| Step 3 | Click Done . |

| Field | Description |
|---|---|
| Value List | This list is populated based on the logged in user's permissions. Note Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. | Note | Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. |
| Note | Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. |
| Value Delimiter | Type the delimter (character) to be placed between each value when a value list is passed to the stored procedure or anonymous
                                                            block. |
| Allow only Single Value selection in filters | Limits the parameter value selection to only one value in the Value list selection filter. That is, for a report definition, when you enable this check box for a parameter, the user can select only one value for that
                                                            parameter in the Value list selection box. Note This check box is enabled only after selecting a value in the Value List list. | Note | This check box is enabled only after selecting a value in the Value List list. |
| Note | This check box is enabled only after selecting a value in the Value List list. |
| Quote Values | Surrounds the parameter with two additional single quotation marks when the value is passed to the stored procedure or anonymous
                                                            block. The first single quotation mark is used to escape the second single quotation mark. |

| Note | Only fields of type string and decimal can be associated with a value list. In stock report templates, this field is populated with the stock value list for the Report Definition. |
|---|---|

| Note | This check box is enabled only after selecting a value in the Value List list. |
|---|---|

| Parameter Property | Description |
|---|---|
| Description | Description of the parameter. |
| Hard-coded value | Hard-coded value to be passed as a parameter value when running a report based on an Anonymous Block or Stored Procedure report
                                             definition. To pass null as a hard-coded value, leave this field blank and check the Pass NULL value for empty string check box. Entering a hard-coded value hides this parameter in the filter page. |
| Format Field | Choose a date, time, or date and time format from the list. |
| Required | Check to indicate that this parameter is required. |
| Pass NULL value for empty string | This check box is enabled only when the parameter is not required or has no value. When the parameter is populated, this field
                                             is disabled and the value is passed. |
| Automatic Parameter | Choose from the following values for STRING type fields in a Stored Procedure Report Definition type: Current User Name Current User Timezone |
| Relative Date Range | Specify the date range using the Start Date and End Date fields. For more information, see Relative Date and Days Filtering for Anonymous Blocks and Stored Procedures section. |

| Note | To indicate a relation between different parameters, the display name of the parameter must be same. |
|---|---|

| Note | Do not enter the same display name for more than one pair of parameters. Unified Intelligence Center displays only the first
                                                         two parameters together in one pair. The third and fourth parameters are not displayed in a pair. For example, Specify Agent_Login_Date as the display name to Agent_Login_Start_Date and Agent_Login_End_Date. Specify Agent_Login_Date as the display name to Log_Out_Interval_Start_Date and Log_Out_Interval_End_Date (instead of Last_Login_Date). Note that the Unified Intelligence Center does not display the parameters Log_Out_Interval_Start_Date and Log_Out_Interval_End_Date
                                                                  in a pair. |
|---|---|

| Action | Description |
|---|---|
| Toolbar Actions |
| Search | Searches for a field. |
| All | Lists all fields. The Field Type column displays the associated data type and the corresponding field types. These field types are represented in the form
                                             of icons: Key Criteria Field or Key Routing Field Composite Field Historical Key Field Filter Field Formula Field Drilldown Linked Conditional Duration Fields |
| Filter | Lists all filter fields. |
| Formulae | Lists all formula fields. |
| Drilldowns | Lists all fields with linked drilldowns. |
| New | Filter Field —Creates a filter field that is based on the selected Data Type. Use filters while running reports to get specific data. Filter
                                                   fields are indicated with Filter icon in the Fields tab > Field Type column. For more information, see Field Properties . Formula Field —Creates a computed field that appears in the list of fields. Formula fields are indicated with Formula icon in the Fields tab > Field Type column. For more information, see Field Properties and Formula Creation Guidelines . |
| Note For each field, you can: Attach or delete value lists for a field (if the Report Definition is based on a query). For more information, see Associate Value List . Edit the formatting for the Query fields and Formula fields. For more information, see Field Properties . | Note | For each field, you can: Attach or delete value lists for a field (if the Report Definition is based on a query). For more information, see Associate Value List . Edit the formatting for the Query fields and Formula fields. For more information, see Field Properties . |
| Note | For each field, you can: Attach or delete value lists for a field (if the Report Definition is based on a query). For more information, see Associate Value List . Edit the formatting for the Query fields and Formula fields. For more information, see Field Properties . |
| Ellipsis (…) Actions |
| Edit | Edits the field details. The editable properties vary for a Query, Filter, or a Formula field. For more information, see Field Properties . |
| Drilldowns | Manages drilldowns. Drilldowns allow you to create links from one report (grid) to another report (grid or chart) so that
                                             you can launch a sub-report from within the current browser window. Note You cannot drill down from or to a gauge report. You cannot drill down to a report based on an Anonymous Block or a Stored Procedure query type. You cannot drill down from or to a report based on the Real Time Streaming query type. For more information on create, edit, or delete drilldowns, see Manage Drillldowns . | Note | You cannot drill down from or to a gauge report. You cannot drill down to a report based on an Anonymous Block or a Stored Procedure query type. You cannot drill down from or to a report based on the Real Time Streaming query type. |
| Note | You cannot drill down from or to a gauge report. You cannot drill down to a report based on an Anonymous Block or a Stored Procedure query type. You cannot drill down from or to a report based on the Real Time Streaming query type. |
| Delete | Deletes a field. |

| Note | For each field, you can: Attach or delete value lists for a field (if the Report Definition is based on a query). For more information, see Associate Value List . Edit the formatting for the Query fields and Formula fields. For more information, see Field Properties . |
|---|---|

| Note | You cannot drill down from or to a gauge report. You cannot drill down to a report based on an Anonymous Block or a Stored Procedure query type. You cannot drill down from or to a report based on the Real Time Streaming query type. |
|---|---|

| Field Property | Field Type | Definition |
|---|---|---|
| Name | All | The default database name. |
| Display Name | All | Appears as the column header for the field on the Filter page when generating a report. Click the pencil icon to edit the Display Name. Note Supports only alphanumeric characters. The pencil icon is visible only on the first row of the parameter list. For the subsequent rows, the pencil icon is visible when you hover over the Display Name. | Note | Supports only alphanumeric characters. The pencil icon is visible only on the first row of the parameter list. For the subsequent rows, the pencil icon is visible when you hover over the Display Name. |
| Note | Supports only alphanumeric characters. The pencil icon is visible only on the first row of the parameter list. For the subsequent rows, the pencil icon is visible when you hover over the Display Name. |
| Description | All | Enter the field description. |
| Data Type | Formula | Choose the data type for the field from the list. Available Data Types are: DECIMAL, STRING, NUMBER, DATE, DATETIME, and BOOLEAN. This setting determines the options that are displayed for this field on the Fields tab. |
| Data Clause | Query and Filter fields only | Identifies which column in the data set is bound to this field. The SQL Parser uses this value when retrieving data from the
                                                database. Note For Filter fields, specify the data clause. For Query fields, this value is auto populated from the query. Data clause is limited to a maximum of 1000 characters (including whitespace). | Note | For Filter fields, specify the data clause. For Query fields, this value is auto populated from the query. Data clause is limited to a maximum of 1000 characters (including whitespace). |
| Note | For Filter fields, specify the data clause. For Query fields, this value is auto populated from the query. Data clause is limited to a maximum of 1000 characters (including whitespace). |
| Value List | Query and Filter fields only | Click the plus icon in the Value List column. In the Attach Value List window, select or type the appropriate values for the following fields. For more information, see Associate Value Lists . When a field is associated with a Value List, report users can filter the report with one or more fields from that Value List
                                                or its Collections. Note Only fields of type String and Decimal can be associated with a Value List. | Note | Only fields of type String and Decimal can be associated with a Value List. |
| Note | Only fields of type String and Decimal can be associated with a Value List. |
| Format \| Footer | Query and Formula fields only | Click the pencil icon to edit the formatting for the field and the footer. Format —Provides a list of default formatting masks. The available formats depend on the data type. For example, for Numeric values, you can select all possible display formats. For Custom selection, you can enter the format in the Custom Format text box. Footer —The formula to use in the footer. Options are None, Average, Sum, Count, Minimum, and Custom Formula. The available options
                                                      depend on the data type. Note For footer formulae, ensure to apply aggregate functions to the columns. For example: SUM(${Field1})/(SUM(${Field2})+SUM(${Field3})) For the Custom footer, the following fields appear: Default Custom Footer Formula —Enter the footer formula to be applied when columns are grouped. This column does not have a custom footer formula defined
                                                            for that level. Group 1 Custom Footer Formula —Enter the footer formula to be applied if this column is in the first level of grouping. Group 2 Custom Footer Formula —Enter the footer formula to be applied if this column is in the second level of grouping. Group 3 Custom Footer Formula —Enter the footer formula to be applied if this column is in the third level of grouping. | Note | For footer formulae, ensure to apply aggregate functions to the columns. For example: SUM(${Field1})/(SUM(${Field2})+SUM(${Field3})) |
| Note | For footer formulae, ensure to apply aggregate functions to the columns. For example: SUM(${Field1})/(SUM(${Field2})+SUM(${Field3})) |
| Allow to show if invisible | Query and Formula fields only | Uncheck this check box to hide from the Available fields panel. Check for the field to appear (retain) on the list of Available fields in the Grid Editor. |
| Available in Filter | All | Check to add the field to the Field Filters tab while choosing filters. |
| Select from Available Fields | Formula | Select a field from the list and click the arrow button to insert it into the Formula Syntax field. Note Fields on this list appear by Name and not by Display Name. | Note | Fields on this list appear by Name and not by Display Name. |
| Note | Fields on this list appear by Name and not by Display Name. |
| Formula Syntax | Formula | Displays operators that construct a formula for the fields you have selected. For more information, see Formula Creation Guidelines . |

| Note | Supports only alphanumeric characters. The pencil icon is visible only on the first row of the parameter list. For the subsequent rows, the pencil icon is visible when you hover over the Display Name. |
|---|---|

| Note | For Filter fields, specify the data clause. For Query fields, this value is auto populated from the query. Data clause is limited to a maximum of 1000 characters (including whitespace). |
|---|---|

| Note | Only fields of type String and Decimal can be associated with a Value List. |
|---|---|

| Note | For footer formulae, ensure to apply aggregate functions to the columns. For example: SUM(${Field1})/(SUM(${Field2})+SUM(${Field3})) |
|---|---|

| Note | Fields on this list appear by Name and not by Display Name. |
|---|---|

| Note | A change to a Report Definition affects all reports that use it. |
|---|---|

| Data | Format | Value |
|---|---|---|
| 123 | 123456 | 000123 |
| 123456.789 | ###,###.### | 123,456.789 |
| 123456.789 | ###.## | 123456.79 |
| 123.78 | 123456.789 | 000123.780 |
| 12345.67 | $###,###.### | $12,345.67 |
| 12345.67 | $1234.56 | $12345.67 |
| 123 | 0.0E+0 | 1.2E2 |
| 123 | 0.0E+00 | 1.2E02 |
| 123 | Rs 1234 | Rs 123a |
| 1234567.89 | 1.234,89 | 1.234.567,89 |
| 123456789 | 1.234.567 | 123.456.789 |

| Note | Null values are considered as empty. |
|---|---|

| Note | To edit or delete a drilldown, from the list page, click the ellipsis button next to the drilldown and click Edit or Delete respectively. After performing the edit or delete actions, ensure to save the Report Definition to reflect the changes that
                                             are made to the drilldown. |
|---|---|

| Step 1 | Click Create . |
|---|---|
| Step 2 | Enter the drilldown name and select the report to link to the drilldown. |
| Step 3 | Click Add Match Field to select the Target Report field and the corresponding (matching) Source Report field. This action filters the target report
                                             that is based on the column value for the matched Source Report field. Note For date and time type fields, selecting the Match Date Range option filters the target report that is based on the date range for a historical field of the source report. Available only
                                                            if the source report is a historical report. | Note | For date and time type fields, selecting the Match Date Range option filters the target report that is based on the date range for a historical field of the source report. Available only
                                                            if the source report is a historical report. |
| Note | For date and time type fields, selecting the Match Date Range option filters the target report that is based on the date range for a historical field of the source report. Available only
                                                            if the source report is a historical report. |
| Step 4 | Click the Save icon. You can edit or delete fields using the respective icons. |
| Step 5 | Click Add Match Field to add more fields and click Next . Note The Add Match Field link is enabled only after saving the selected fields. | Note | The Add Match Field link is enabled only after saving the selected fields. |
| Note | The Add Match Field link is enabled only after saving the selected fields. |
| Step 6 | Set the filter criteria and click Done . The created drilldown is listed on the Drilldowns page for that report. Note When you create a drilldown, by default, the target report's filter criteria is populated in the drilldown filter screens.
                                                                  During the create process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to the default for that field. When you edit a drilldown, the target report's current drilldown filter criteria is populated in the drilldown filter screens.
                                                                  During the edit process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to reflect the current drilldown filter criteria
                                                                  for that field. For more information on setting the filter criteria, see Report Filters section in the Cisco Unified Intelligence Center User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html . | Note | When you create a drilldown, by default, the target report's filter criteria is populated in the drilldown filter screens.
                                                                  During the create process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to the default for that field. When you edit a drilldown, the target report's current drilldown filter criteria is populated in the drilldown filter screens.
                                                                  During the edit process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to reflect the current drilldown filter criteria
                                                                  for that field. |
| Note | When you create a drilldown, by default, the target report's filter criteria is populated in the drilldown filter screens.
                                                                  During the create process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to the default for that field. When you edit a drilldown, the target report's current drilldown filter criteria is populated in the drilldown filter screens.
                                                                  During the edit process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to reflect the current drilldown filter criteria
                                                                  for that field. |

| Note | For date and time type fields, selecting the Match Date Range option filters the target report that is based on the date range for a historical field of the source report. Available only
                                                            if the source report is a historical report. |
|---|---|

| Note | The Add Match Field link is enabled only after saving the selected fields. |
|---|---|

| Note | When you create a drilldown, by default, the target report's filter criteria is populated in the drilldown filter screens.
                                                                  During the create process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to the default for that field. When you edit a drilldown, the target report's current drilldown filter criteria is populated in the drilldown filter screens.
                                                                  During the edit process, if you delete a Match Field or a Match Date Range for the target report’s field, then the drilldown filter screens are reset to reflect the current drilldown filter criteria
                                                                  for that field. |
|---|---|

| Note | For Real Time (Live Data) Reports, only the Author and Version fields are available. |
|---|---|

| Action | Description |
|---|---|
| Author | Template provider name who created the entity. |
| Version | Report definition entity version that is currently deployed in Unified Intelligence Center. Format: x.y (where, x and y are integers). Do not start or end with a decimal point. Examples: 8.9 or 11.15 |
| Key Criteria Field | Choose to filter the reports based on simple queries. Note This field is not enabled for reports based on Anonymous Blocks or Stored Procedures. You can run a report based on a simple query if the Report Definition does not have a Key Criteria Field defined. However, as the report runs with the default filter, the data fetched can be large. | Note | This field is not enabled for reports based on Anonymous Blocks or Stored Procedures. You can run a report based on a simple query if the Report Definition does not have a Key Criteria Field defined. However, as the report runs with the default filter, the data fetched can be large. |
| Note | This field is not enabled for reports based on Anonymous Blocks or Stored Procedures. You can run a report based on a simple query if the Report Definition does not have a Key Criteria Field defined. However, as the report runs with the default filter, the data fetched can be large. |
| Real Time or Historical | Choose the report type. |
| Historical Key Field | Choose for the date and time intervals for the report. Note This field is enabled only for the Historical report type. Although Historical reports can run if this field is left blank, the report returns all data for all dates and the data fetched.
                                                      Only fields of the DATE and DATETIME format are available in this list. | Note | This field is enabled only for the Historical report type. Although Historical reports can run if this field is left blank, the report returns all data for all dates and the data fetched.
                                                      Only fields of the DATE and DATETIME format are available in this list. |
| Note | This field is enabled only for the Historical report type. Although Historical reports can run if this field is left blank, the report returns all data for all dates and the data fetched.
                                                      Only fields of the DATE and DATETIME format are available in this list. |
| Refresh Rate | Rate at which the report is automatically refreshed (in seconds). The minimum Refresh Rate is 15 seconds for Real Time reports
                                          and 900 seconds for Historical reports. You cannot enter values less than the defaults. Note For new report definitions of type historical, the default Refresh Rate is 3600 seconds. For type real time, the default Refresh
                                                      Rate is 900 seconds. | Note | For new report definitions of type historical, the default Refresh Rate is 3600 seconds. For type real time, the default Refresh
                                                      Rate is 900 seconds. |
| Note | For new report definitions of type historical, the default Refresh Rate is 3600 seconds. For type real time, the default Refresh
                                                      Rate is 900 seconds. |

| Note | This field is not enabled for reports based on Anonymous Blocks or Stored Procedures. You can run a report based on a simple query if the Report Definition does not have a Key Criteria Field defined. However, as the report runs with the default filter, the data fetched can be large. |
|---|---|

| Note | This field is enabled only for the Historical report type. Although Historical reports can run if this field is left blank, the report returns all data for all dates and the data fetched.
                                                      Only fields of the DATE and DATETIME format are available in this list. |
|---|---|

| Note | For new report definitions of type historical, the default Refresh Rate is 3600 seconds. For type real time, the default Refresh
                                                      Rate is 900 seconds. |
|---|---|