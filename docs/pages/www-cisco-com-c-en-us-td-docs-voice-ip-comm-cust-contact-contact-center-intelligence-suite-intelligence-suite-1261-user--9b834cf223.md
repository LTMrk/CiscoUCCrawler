---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1261-user--9b834cf223
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1261/user/guide/cuic_b_report-customization-guide-1261/cuic_b_report-customization-guide-1205_chapter_010.html
retrieved_at: 2026-08-21T16:15:44.796460+00:00
---

Cisco Unified Intelligence Center Report Customization Guide, Release 12.6(1)

# Cisco Unified Intelligence Center Report Customization Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Report
	 Customization in Unified Intelligence Center

## Chapter: Report
	 Customization in Unified Intelligence Center

- Report                              	 Customization in Unified Intelligence Center

- Before You Begin

- What Can You Customize

# Report
                     	 Customization in Unified Intelligence Center

This chapter describes the different aspects of developing and
                        		customizing a report in Unified Intelligence Center.

## Before You Begin

Ensure that you have adequate permissions to create or modify the Reports, Report Definitions, Value Lists, and Collections.

Understand how permissions are set for folders, sub-folders, and imported components. You can do either of the following:

Contact the administrator.

If you have access to the Configure feature, see Configure chapter.

If you are creating or designing reports for any particular solution, be aware of the specific guidelines for accessing data
                           from the solution. See the respective solution's reporting guide for detailed information.

For Mac users, set the following:

Issue

Setting

Keyboard Accessibility in Firefox

Navigate to System Preferences > Keyboard > Shortcuts > Full keyboard Access  > enable the All controls option.

Report Views > Column alignment

Navigate to System Preferences > General > Show Scroll bars > select the When Scrolling option.

## What Can You Customize

You can customize the following components of the Unified Intelligence Center report. Each section describes the level of
                           customization available for each of the components of a report.

### Report Definition

Customizing the Report Definition affects the kind of data present in the report.

You can configure the query used to fetch data from the data source. The fields are then created on the basis of the query.
                              Each field can be configured to hold a particular type of data. You can also format the field based on the data type in the
                              field. Multiple reports can use a single Report Definition.

### Drilldowns

Drilldowns allow you to create links from one report (grid) to another report (grid or chart) so that you can launch a sub-report
                              from within the current browser window. You cannot use this feature for a gauge report. You can create the drilldown link
                              for any field in a report that is not a grouped field.

Drilldowns will work only for target reports of type SQL query.

Report widgets in Dashboards does not support the drilldown report feature.

The advantage of drilldowns is that you do not have to configure a query to fetch and format certain data if it is already
                              available in another report. You can create any number of drilldowns for a particular Report Definition.

### Value List

Value Lists are based on database queries and contain all reportable items of the same type.

### Collection

Collections are subsets of Value Lists that can be created to control the amount of data shown to specific users and user
                              groups.

### View

A view is a data presentation. A report can have multiple views using same or different fields. For more information on Report
                              Views, see Cisco Unified Intelligence Center User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html .

### Multiple Report Views on Gadget

To configure multiple report views on the Cisco Finesse Desktop gadget toolbar, see Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

| Issue | Setting |
|---|---|
| Keyboard Accessibility in Firefox | Navigate to System Preferences > Keyboard > Shortcuts > Full keyboard Access  > enable the All controls option. |
| Report Views > Column alignment | Navigate to System Preferences > General > Show Scroll bars > select the When Scrolling option. |

| Note | Drilldowns will work only for target reports of type SQL query. Report widgets in Dashboards does not support the drilldown report feature. |
|---|---|

| Note | For Historical Gadgets, only one view is supported. |
|---|---|