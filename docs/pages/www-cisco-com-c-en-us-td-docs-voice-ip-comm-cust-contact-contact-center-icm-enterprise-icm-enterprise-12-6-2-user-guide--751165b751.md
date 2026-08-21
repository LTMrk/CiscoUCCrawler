---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-guide--751165b751
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/guide/ucce_b_cisco-unified-contact-center-enterprise-reporting-user-guide-release1262/ucce_b_cisco-unified-contact-center-enterprise-1261_chapter_010.html
retrieved_at: 2026-08-21T11:59:27.239822+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(2)

Updated: May 4, 2023

Chapter: Dashboards

## Chapter: Dashboards

# Dashboards

## Overview

In Cisco Unified Intelligence Center , Dashboard is an interface that allows you to add reports, web pages (URLs), web widgets, and notes in a consolidated view.

All actions on the Dashboards interface are based on your role and on the user permissions for Dashboards and for Folders.

### Access Dashboards

From the left navigation pane, click Dashboards to access the list of all the available Dashboards. This list includes the dashboards that you have created and the dashboards
                              created by other users on which you have View permissions.

You must be assigned with the Dashboard Designer role to create Dashboards.

To view Dashboards created by other users, you must have View permissions for the dashboard and its parent folder.

Cisco Unified Intelligence Center does not provide a default Dashboard.

### Run Dashboards

To run a Dashboard, click the Dashboard name. When the Dashboard is in the run mode, use the toolbar to:

Edit the Dashboard.

Refresh the Dashboard data.

Maximize the Dashboard view.

Press Esc to restore the original view.

### Before You Upgrade

Cisco Unified Intelligence Center 12.5 supports a maximum of ten widgets per Dashboard. Hence, for Dashboards with more than ten widgets in versions before 12.5 , ensure to split those Dashboards with a maximum of ten widgets each before upgrade.

Consider a Dashboard with 15 widgets in Unified Intelligence Center versions before 12.5 . Before upgrading to version 12.5 , use the Save As feature to clone the Dashboard and manage the widgets up to ten per Dashboard.

### Unsupported Widgets

The Cisco Unified Intelligence Center 12.5 interface for Dashboards does not support the following widgets:

Schedule Report widgets

URL widgets containing Dashboard permalinks (Nested Dashboards)

### Migration Limitations

To address injection vulnerabilities, the Custom Widget feature in Dashboards is disabled by default. If any custom widgets were added to the Dashboards in versions earlier to Unified Intelligence Center 12.5, those widgets are visible in the read-only mode post upgrade to
                                 version 12.5. You can opt to retain or delete them.

To enable the Custom Widget feature, use the CLI set cuic properties dashboard-customwidget-enabled and set the parameter value to "on". For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

## Dashboard Actions

The following table lists various actions that you can perform from the Dashboard.

You can open a maximum of ten tabs at a time.

Action

Description

The New Dashboard wizard allows you to:

Provide Dashboard properties; Name and Description.

Add widgets to the Dashboard.

For more information, see Add Widgets to Dashboard .

When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                   the folders on which you have the Edit permission.

Toolbar actions

Refreshes the Dashboards page.

To easily access your Dashboards, you can tag Dashboards as Favorites.

Click the star icon beside the Dashboard name to add to Favorites.

Searches for a particular Dashboard.

Add, remove, and modify widgets.

Click the icon next to the Dashboard name to edit the Dashboard properties; name and description.

After editing the Dashboard, click Save .

Saves a copy of the Dashboard.

Renames a Dashboard or a Folder.

Moves Dashboard or Folder from one folder to another.

You can move a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being moved.

Deletes a Dashboard or a Folder.

You can delete a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being deleted.

Assigns appropriate permissions to access and manage the Dashboard.

Groups —Grants View and Edit permissions for the Dashboard to various groups.

Security Administrators can grant these permissions to various groups.

Entity owners can grant these permissions to groups that they are directly associated with.

Users —Grants View and Edit permissions for the Dashboard to various users. Applicable only to Security Administrators.

Higher permissions (View and Edit) from either an individual user or the user group takes precedence.

Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups .

When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes.

Displays the Dashboard permalink.

You can access permanent hyperlink only from a web browser. You cannot access it from an application such as Microsoft Excel
                                                   to pull data or display a Dashboard.

For more information, see Permalink for a Dashboard .

## Add Widgets to Dashboard

You can add Reports, Web pages, Notes, and Custom Widgets to a Dashboard. In addition, you can resize and reposition the widgets
                              to suit your needs. The default widget size depends on the available space on the Dashboard canvas.

You can add a maximum of ten widgets per Dashboard.

To add widgets to the Dashboard, perform the following steps:

Step 1

From the left navigation pane, click Dashboards .

Step 2

In the Dashboards tab,

To add widgets to a new Dashboard, click New > Dashboard .

To add widgets to an existing Dashboard, click the ellipsis icon beside the required Dashboard and click Edit .

Step 3

On the Dashboard canvas, click on the plus icon.

Step 4

In the Add Widgets dialog box, add the required widgets:

Widget Type

Steps

Report View

Click the Report View icon.

In the Add Report View dialog box, select the Report and the Views from the corresponding drop-down list.

Click Done .

For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report.

The Manage filters and the View filter information icons appear only when you hover on the report widget.

For Grid view reports, you can increase or decrease the font size of the report data.

The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation.

In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria.

Drilldown reports are not supported.

Click the Note icon.

In the Add a Note dialog box, enter Note Title and Note Body .

Click Done .

Web page

Click the Web page icon.

In the Add a Web page dialog box, enter Web URL , the address of the web page that you want to display on the Dashboard.

Click Done .

Limitations for web page widget:

The websites enabled with "X-Frame-Options", will not be displayed on the Dashboard.

The web URLs provided without prefixing a protocol (HTTPS) will by default use the protocol of the Cisco Unified Intelligence
                                                                  Center application.

When Cisco Unified Intelligence Center is in HTTPS mode, you cannot configure HTTP based widget URLs in Dashboard.

You cannot add Dashboard permalink as web page widget.

For information on viewing report permalinks in Dashboards as web page widgets, see View Report Permalinks in Dashboards .

Custom Widget

Click the Custom Widget icon.

In the Add Custom Widget dialog box, enter Widget Title and Code Snippet .

In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on.

Maximum Limit: 1000 characters.

Click Done . The embedded code appears on the Dashboard.

By default, this widget type is disabled. You can enable the Custom Widget feature using the CLI set cuic properties dashboard-customwidget-enabled on .

For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

Step 5

Click Save .

## Run a Report from the Dashboard

Running a report from the Dashboard depends on the Skip filter during the report execution check box during the report filter selection:

If this check box is checked for a report, the system bypasses the filter and runs that report using the default filter.

If this check box is unchecked for a report, for the first access, the system prompts you to choose a Filter to run that report.

The Skip filter during the report execution check box is not checked for any of the stock reports. If you do not want a Dashboard report to require filter selection
                                                   upon first use, you must create a new report, set the default filter, and check the Skip filter during the report execution check box.

The Filter prompt displays the corresponding icon to denote the type of report view, such as, Grid, Chart, Pie, and so on.

In both these scenarios, from the ellipsis icon on the Report widget header you can access Filter to edit the filter criteria.

Click the Filter button to display the filter criteria in the Filter Data dialog box based on the following validations:

Displays the filter criteria screens based on the selected report query type.

Populates with the default filter criteria if the default filter is set for that report.

Edit Filter Data

You can edit the report filter data from the Dashboard in the following two ways:

Run mode —Click the filter icon on the report widget header.

Edit mode —Click the ellipsis icon and select Filter from the available menu options.

Modify the required filter criteria and click Run . The report refreshes reflecting the modified filter criteria.

When you edit the report filter for a Dashboard during Create, Edit, or Run mode, the filter settings are stored in the browser
                                       cache and is specific to the individual user. Hence, the next time you sign in and run the Dashboard, the report widget uses
                                       the filter information stored in the browser cache and generates the report (without prompting you to update the filter criteria).
                                       The browser cache is retained up to 30 days.

Every time you run the report, the filter data in the browser cache is validated for permissions. If there is a permission
                                       mismatch, an error message appears that the filter you selected before is no longer valid and select the filters again.

Also, if any other user sign-in to the same browser, that user cannot view your filter settings.

The filter settings stored in your browser cache are cleared only:

If you have not used the Dashboard for the last 30 days.

If you manually clear the cache.

For more information on Report Filters, see Report Filters .

| Note | You must be assigned with the Dashboard Designer role to create Dashboards. To view Dashboards created by other users, you must have View permissions for the dashboard and its parent folder. Cisco Unified Intelligence Center does not provide a default Dashboard. |
|---|---|

| Note | You can open a maximum of ten tabs at a time. |
|---|---|

| Action | Description |
|---|---|
| Dashboard-level actions |
| New |
| Dashboard | Creates a new Dashboard. The New Dashboard wizard allows you to: Provide Dashboard properties; Name and Description. Add widgets to the Dashboard. For more information, see Add Widgets to Dashboard . |
| Folder | Creates a new Folder. Use this feature to categorize Dashboards. Note When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                   the folders on which you have the Edit permission. | Note | When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                   the folders on which you have the Edit permission. |
| Note | When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                   the folders on which you have the Edit permission. |
| Toolbar actions |
| Refresh | Refreshes the Dashboards page. |
| Favorites | To easily access your Dashboards, you can tag Dashboards as Favorites. Click the star icon beside the Dashboard name to add to Favorites. |
| Search | Searches for a particular Dashboard. |
| Ellipsis (…) actions |
| Edit | Edits the Dashboard details. In the edit mode, you can: Add, remove, and modify widgets. Click the icon next to the Dashboard name to edit the Dashboard properties; name and description. After editing the Dashboard, click Save . |
| Save As | Saves a copy of the Dashboard. |
| Rename | Renames a Dashboard or a Folder. |
| Move | Moves Dashboard or Folder from one folder to another. Note You can move a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being moved. | Note | You can move a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being moved. |
| Note | You can move a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being moved. |
| Delete | Deletes a Dashboard or a Folder. Note You can delete a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being deleted. | Note | You can delete a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being deleted. |
| Note | You can delete a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being deleted. |
| Permissions | Assigns appropriate permissions to access and manage the Dashboard. Groups —Grants View and Edit permissions for the Dashboard to various groups. Security Administrators can grant these permissions to various groups. Entity owners can grant these permissions to groups that they are directly associated with. Users —Grants View and Edit permissions for the Dashboard to various users. Applicable only to Security Administrators. Note Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. | Note | Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. |
| Note | Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. |
| Permalinks | Displays the Dashboard permalink. Note You can access permanent hyperlink only from a web browser. You cannot access it from an application such as Microsoft Excel
                                                   to pull data or display a Dashboard. For more information, see Permalink for a Dashboard . | Note | You can access permanent hyperlink only from a web browser. You cannot access it from an application such as Microsoft Excel
                                                   to pull data or display a Dashboard. |
| Note | You can access permanent hyperlink only from a web browser. You cannot access it from an application such as Microsoft Excel
                                                   to pull data or display a Dashboard. |

| Note | When you move or save the folders to a different location, the drop-down lists all the folders. You can only navigate into
                                                   the folders on which you have the Edit permission. |
|---|---|

| Note | You can move a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being moved. |
|---|---|

| Note | You can delete a Dashboard or a Folder only if you have Edit permission on the parent folder of the Dashboard or Folder being deleted. |
|---|---|

| Note | Higher permissions (View and Edit) from either an individual user or the user group takes precedence. Only the first 200 records (alphabetical order) are displayed in the Members or Groups panel. To view more records, see Configure > Groups . When you modify a permission and want to switch between Groups and Users tabs, you will be prompted to either save or discard the changes. |
|---|---|

| Note | You can access permanent hyperlink only from a web browser. You cannot access it from an application such as Microsoft Excel
                                                   to pull data or display a Dashboard. |
|---|---|

| Note | You can add a maximum of ten widgets per Dashboard. |
|---|---|

| Step 1 | From the left navigation pane, click Dashboards . |
|---|---|
| Step 2 | In the Dashboards tab, To add widgets to a new Dashboard, click New > Dashboard . To add widgets to an existing Dashboard, click the ellipsis icon beside the required Dashboard and click Edit . |
| Step 3 | On the Dashboard canvas, click on the plus icon. |
| Step 4 | In the Add Widgets dialog box, add the required widgets: Widget Type Steps Report View Displays an existing report on the Dashboard. Click the Report View icon. In the Add Report View dialog box, select the Report and the Views from the corresponding drop-down list. Click Done . Note For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. Note Adds notes to the Dashboard. Click the Note icon. In the Add a Note dialog box, enter Note Title and Note Body . Click Done . Web page Displays a web page on the Dashboard. Click the Web page icon. In the Add a Web page dialog box, enter Web URL , the address of the web page that you want to display on the Dashboard. Click Done . Limitations for web page widget: The websites enabled with "X-Frame-Options", will not be displayed on the Dashboard. The web URLs provided without prefixing a protocol (HTTPS) will by default use the protocol of the Cisco Unified Intelligence
                                                                  Center application. When Cisco Unified Intelligence Center is in HTTPS mode, you cannot configure HTTP based widget URLs in Dashboard. You cannot add Dashboard permalink as web page widget. For information on viewing report permalinks in Dashboards as web page widgets, see View Report Permalinks in Dashboards . Custom Widget Adds custom widgets to the Dashboard. Click the Custom Widget icon. In the Add Custom Widget dialog box, enter Widget Title and Code Snippet . Note In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. Click Done . The embedded code appears on the Dashboard. By default, this widget type is disabled. You can enable the Custom Widget feature using the CLI set cuic properties dashboard-customwidget-enabled on . For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html . | Widget Type | Steps | Report View | Displays an existing report on the Dashboard. Click the Report View icon. In the Add Report View dialog box, select the Report and the Views from the corresponding drop-down list. Click Done . Note For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. | Note | For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. | Note | Adds notes to the Dashboard. Click the Note icon. In the Add a Note dialog box, enter Note Title and Note Body . Click Done . | Web page | Displays a web page on the Dashboard. Click the Web page icon. In the Add a Web page dialog box, enter Web URL , the address of the web page that you want to display on the Dashboard. Click Done . Limitations for web page widget: The websites enabled with "X-Frame-Options", will not be displayed on the Dashboard. The web URLs provided without prefixing a protocol (HTTPS) will by default use the protocol of the Cisco Unified Intelligence
                                                                  Center application. When Cisco Unified Intelligence Center is in HTTPS mode, you cannot configure HTTP based widget URLs in Dashboard. You cannot add Dashboard permalink as web page widget. For information on viewing report permalinks in Dashboards as web page widgets, see View Report Permalinks in Dashboards . | Custom Widget | Adds custom widgets to the Dashboard. Click the Custom Widget icon. In the Add Custom Widget dialog box, enter Widget Title and Code Snippet . Note In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. Click Done . The embedded code appears on the Dashboard. By default, this widget type is disabled. You can enable the Custom Widget feature using the CLI set cuic properties dashboard-customwidget-enabled on . For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html . | Note | In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. |
| Widget Type | Steps |
| Report View | Displays an existing report on the Dashboard. Click the Report View icon. In the Add Report View dialog box, select the Report and the Views from the corresponding drop-down list. Click Done . Note For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. | Note | For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. |
| Note | For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. |
| Note | Adds notes to the Dashboard. Click the Note icon. In the Add a Note dialog box, enter Note Title and Note Body . Click Done . |
| Web page | Displays a web page on the Dashboard. Click the Web page icon. In the Add a Web page dialog box, enter Web URL , the address of the web page that you want to display on the Dashboard. Click Done . Limitations for web page widget: The websites enabled with "X-Frame-Options", will not be displayed on the Dashboard. The web URLs provided without prefixing a protocol (HTTPS) will by default use the protocol of the Cisco Unified Intelligence
                                                                  Center application. When Cisco Unified Intelligence Center is in HTTPS mode, you cannot configure HTTP based widget URLs in Dashboard. You cannot add Dashboard permalink as web page widget. For information on viewing report permalinks in Dashboards as web page widgets, see View Report Permalinks in Dashboards . |
| Custom Widget | Adds custom widgets to the Dashboard. Click the Custom Widget icon. In the Add Custom Widget dialog box, enter Widget Title and Code Snippet . Note In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. Click Done . The embedded code appears on the Dashboard. By default, this widget type is disabled. You can enable the Custom Widget feature using the CLI set cuic properties dashboard-customwidget-enabled on . For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html . | Note | In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. |
| Note | In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. |
| Step 5 | Click Save . |

| Widget Type | Steps |
|---|---|
| Report View | Displays an existing report on the Dashboard. Click the Report View icon. In the Add Report View dialog box, select the Report and the Views from the corresponding drop-down list. Click Done . Note For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. | Note | For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. |
| Note | For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. |
| Note | Adds notes to the Dashboard. Click the Note icon. In the Add a Note dialog box, enter Note Title and Note Body . Click Done . |
| Web page | Displays a web page on the Dashboard. Click the Web page icon. In the Add a Web page dialog box, enter Web URL , the address of the web page that you want to display on the Dashboard. Click Done . Limitations for web page widget: The websites enabled with "X-Frame-Options", will not be displayed on the Dashboard. The web URLs provided without prefixing a protocol (HTTPS) will by default use the protocol of the Cisco Unified Intelligence
                                                                  Center application. When Cisco Unified Intelligence Center is in HTTPS mode, you cannot configure HTTP based widget URLs in Dashboard. You cannot add Dashboard permalink as web page widget. For information on viewing report permalinks in Dashboards as web page widgets, see View Report Permalinks in Dashboards . |
| Custom Widget | Adds custom widgets to the Dashboard. Click the Custom Widget icon. In the Add Custom Widget dialog box, enter Widget Title and Code Snippet . Note In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. Click Done . The embedded code appears on the Dashboard. By default, this widget type is disabled. You can enable the Custom Widget feature using the CLI set cuic properties dashboard-customwidget-enabled on . For more information, see Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html . | Note | In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. |
| Note | In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. |

| Note | For a Report widget, you can click the icons on the widget header to view the existing filter information, manage filters,
                                                                        and play or pause the running of report. The Manage filters and the View filter information icons appear only when you hover on the report widget. For Grid view reports, you can increase or decrease the font size of the report data. The default font size is set to 10. Post upgrade to Cisco Unified Intelligence Center 12.0 or later , this setting overrides the font size set during the grid view creation. In the edit mode, from the Report widget header, use the ellipsis icon to access Filter and modify the filter criteria. Drilldown reports are not supported. |
|---|---|

| Note | In the Code Snippet box, you can enter any markup/code snippet of the widget that you want to show on the Dashboard. For example, HTML, XML RSS
                                                                        feed, JavaScript, and so on. Maximum Limit: 1000 characters. |
|---|---|

| Note | The Skip filter during the report execution check box is not checked for any of the stock reports. If you do not want a Dashboard report to require filter selection
                                                   upon first use, you must create a new report, set the default filter, and check the Skip filter during the report execution check box. The Filter prompt displays the corresponding icon to denote the type of report view, such as, Grid, Chart, Pie, and so on. In both these scenarios, from the ellipsis icon on the Report widget header you can access Filter to edit the filter criteria. |
|---|---|

| Note | When you edit the report filter for a Dashboard during Create, Edit, or Run mode, the filter settings are stored in the browser
                                       cache and is specific to the individual user. Hence, the next time you sign in and run the Dashboard, the report widget uses
                                       the filter information stored in the browser cache and generates the report (without prompting you to update the filter criteria).
                                       The browser cache is retained up to 30 days. Every time you run the report, the filter data in the browser cache is validated for permissions. If there is a permission
                                       mismatch, an error message appears that the filter you selected before is no longer valid and select the filters again. Also, if any other user sign-in to the same browser, that user cannot view your filter settings. The filter settings stored in your browser cache are cleared only: If you have not used the Dashboard for the last 30 days. If you manually clear the cache. |
|---|---|