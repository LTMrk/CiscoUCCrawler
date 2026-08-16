---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-reference-guide-uccx-b-125repor-fd996e84eb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/reference/guide/uccx_b_125report-developers-guide/uccx_b_125report-developers-guide_chapter_010.html
retrieved_at: 2026-08-16T21:04:12.089626+00:00
---

Cisco Unified Contact Center Express Report Developer Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Report Developer Guide, Release 12.5(1)

## Results

Updated: February 7, 2020

Chapter: Create Custom Reports

## Chapter: Create Custom Reports

# Create Custom Reports

## Overview

You can create new reports with the Unified Intelligence Center that is embedded with Unified CCX. To create new custom Historical
                              reports, you need not install a Standalone Unified Intelligence Center.

## How to Create
                        	 Custom Reports

The following
                              		  table describes the task flow to create a new Historical report:

Sequence

Task

Where
                                          					 performed

Reference

1

Create
                                          					 Unified CCX datasource

Standalone Unified Intelligence Center

See Create Unified CCX Data Source .

See the "Standalone Cisco Unified Intelligence Center Configuration" section of the Cisco Unified Contact Center Express Administration and Operations Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html .

This is an optional step and is required only when Standalone CUIC is being used to create the custom reports.

2

Create
                                          					 custom stored procedure

Unified
                                          					 CCX

See Create Custom Stored Procedure .

3

Create
                                          					 report definition

Unified Intelligence Center embedded in Unified CCX

See the "Create or edit report definitions" section of the Cisco Unified Intelligence Center Report Customization Guide , located at:

https://www.cisco.com/en/US/products/ps9755/products_user_guide_list.html .

4

Export
                                          					 custom report

Unified Intelligence Center embedded in Unified CCX

See the "Export reports, report definitions, and categories" section of the Cisco Unified Intelligence Center Report Customization Guide , located at:

https://www.cisco.com/en/US/products/ps9755/products_user_guide_list.html .

5

Import
                                          					 custom report to Unified CCX

Unified
                                          					 Intelligence Center embedded in Unified CCX

See the "Import Reports" section of the Cisco Unified Contact
                                                   				  Center Express Report User Guide , located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_user_guide_list.html .

6

Set
                                          					 permissions to the new custom report

Unified
                                          					 Intelligence Center embedded in Unified CCX

See the "Manage user permissions" section of the Cisco Unified Contact Center Express Administration and Operations Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html .

## Create Unified CCX
                        	 Data Source

Create a Unified CCX data source on the Standalone Unified Intelligence Center server that points to the Unified CCX server.

Set the
                                       			 password for the Historical Reporting User.

Log in to
                                             				  Cisco Unified Contact Center Express Administration using the Unified CCX
                                             				  username and password.

Select Tools > Password
                                                   						Management .

In the
                                             				  Historical Reporting User field, set the password, and click Save .

Record
                                       			 settings of the existing Unified CCX data source.

Log in to
                                             				  Unified Intelligence Center on the Unified CCX server.

In the
                                             				  left pane, click Data Sources .

The Data Sources page opens in a separate tab in the
                                                					 right pane.

Select the
                                             				  Unified CCX data source and click Edit .

Record the
                                             				  settings in the page so that you can refer to this data later.

Configure a data source on the Standalone  Unified Intelligence Center server to point to the Unified CCX server.

Log in to the Standalone Unified Intelligence Center using credentials that has report designer permissions.

In the left pane, click Data Sources .

Click Create to create a new data source.

Set the parameters as per the settings you recorded in Step 2d .

Click Test Connection and verify the settings.

## Create Custom
                        	 Stored Procedure

The Unified CCX
                              		  database schema details are described in the Database
                                 			 Schema Guide for Cisco Unified CCX and Cisco Unified IP IVR , located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-technical-reference-list.html .

Connect to the
                                       			 db_cra database using the uccxhruser username and password.

Create a stored procedure using third-party tools such as SQuirrel SQL Client and AGS Server Studio.

Assign
                                       			 execution privileges for the stored procedure to uccxHrUserRole using the following command:

### Example:

### What to do next

See the task flow table in How to Create Custom Reports .

| Sequence | Task | Where
                                          					 performed | Reference |
|---|---|---|---|
| 1 | Create
                                          					 Unified CCX datasource | Standalone Unified Intelligence Center | See Create Unified CCX Data Source . See the "Standalone Cisco Unified Intelligence Center Configuration" section of the Cisco Unified Contact Center Express Administration and Operations Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html . Note This is an optional step and is required only when Standalone CUIC is being used to create the custom reports. | Note | This is an optional step and is required only when Standalone CUIC is being used to create the custom reports. |
| Note | This is an optional step and is required only when Standalone CUIC is being used to create the custom reports. |
| 2 | Create
                                          					 custom stored procedure | Unified
                                          					 CCX | See Create Custom Stored Procedure . |
| 3 | Create
                                          					 report definition | Unified Intelligence Center embedded in Unified CCX | See the "Create or edit report definitions" section of the Cisco Unified Intelligence Center Report Customization Guide , located at: https://www.cisco.com/en/US/products/ps9755/products_user_guide_list.html . |
| 4 | Export
                                          					 custom report | Unified Intelligence Center embedded in Unified CCX | See the "Export reports, report definitions, and categories" section of the Cisco Unified Intelligence Center Report Customization Guide , located at: https://www.cisco.com/en/US/products/ps9755/products_user_guide_list.html . |
| 5 | Import
                                          					 custom report to Unified CCX | Unified
                                          					 Intelligence Center embedded in Unified CCX | See the "Import Reports" section of the Cisco Unified Contact
                                                   				  Center Express Report User Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_user_guide_list.html . |
| 6 | Set
                                          					 permissions to the new custom report | Unified
                                          					 Intelligence Center embedded in Unified CCX | See the "Manage user permissions" section of the Cisco Unified Contact Center Express Administration and Operations Guide , located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html . |

| Note | This is an optional step and is required only when Standalone CUIC is being used to create the custom reports. |
|---|---|

| Note | Do not create a data source in the Unified Intelligence Center  that is bundled with Unified CCX. This scenario is not supported. |
|---|---|

| Step 1 | Set the
                                       			 password for the Historical Reporting User. Log in to
                                             				  Cisco Unified Contact Center Express Administration using the Unified CCX
                                             				  username and password. Select Tools > Password
                                                   						Management . In the
                                             				  Historical Reporting User field, set the password, and click Save . |
|---|---|
| Step 2 | Record
                                       			 settings of the existing Unified CCX data source. Log in to
                                             				  Unified Intelligence Center on the Unified CCX server. In the
                                             				  left pane, click Data Sources . The Data Sources page opens in a separate tab in the
                                                					 right pane. Select the
                                             				  Unified CCX data source and click Edit . Record the
                                             				  settings in the page so that you can refer to this data later. |
| Step 3 | Configure a data source on the Standalone  Unified Intelligence Center server to point to the Unified CCX server. Log in to the Standalone Unified Intelligence Center using credentials that has report designer permissions. In the left pane, click Data Sources . Click Create to create a new data source. Set the parameters as per the settings you recorded in Step 2d . Note The database user name should be uccxhruser and the password should match the password you set in Step 1c . Click Test Connection and verify the settings. Tip If an error is prompted, verify that the settings are correct and try again. | Note | The database user name should be uccxhruser and the password should match the password you set in Step 1c . | Tip | If an error is prompted, verify that the settings are correct and try again. |
| Note | The database user name should be uccxhruser and the password should match the password you set in Step 1c . |
| Tip | If an error is prompted, verify that the settings are correct and try again. |

| Note | The database user name should be uccxhruser and the password should match the password you set in Step 1c . |
|---|---|

| Tip | If an error is prompted, verify that the settings are correct and try again. |
|---|---|

| Note | Perform the following steps for both Unified CCX nodes, if applicable. |
|---|---|

| Step 1 | Connect to the
                                       			 db_cra database using the uccxhruser username and password. |
|---|---|
| Step 2 | Create a stored procedure using third-party tools such as SQuirrel SQL Client and AGS Server Studio. |
| Step 3 | Assign
                                       			 execution privileges for the stored procedure to uccxHrUserRole using the following command: Example: grant execute on <your procedure name> to 'uccxHrUserRole'; |