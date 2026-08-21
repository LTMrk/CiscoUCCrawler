---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-administration-guide-1251su4-cucm-b-test-admingu-f88e32866d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_administration-guide-1251su4/cucm_b_test-adminguide_chapter_0100001.html
retrieved_at: 2026-08-21T16:01:51.255516+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: April 8, 2025

Chapter: Cisco Unified Reporting

## Chapter: Cisco Unified Reporting

# Cisco Unified Reporting

## Consolidated Data
                        	 Reporting

The Cisco Unified
                                 			 Reporting web application, which is accessed at the Cisco Unified Communications
                                 			 Manager and Cisco
                                 			 Unified Communications Manager IM and Presence Service consoles,
                              		  generates consolidated reports for troubleshooting or inspecting cluster data.

Unless stated
                                          			 otherwise, the information, notes, and procedures in this guide apply to Unified Communications Manager and the IM and
                                             				Presence Service .

This tool
                              		  provides an easy way to take a snapshot of cluster data. The tool gathers data
                              		  from existing sources, compares the data, and reports irregularities. When you
                              		  generate a report in Cisco Unified
                                 			 Reporting , the report combines data from one or more sources on one
                              		  or more servers into one output view. For example, you can view a report that
                              		  shows the hosts file for all servers in the cluster.

The Cisco Unified
                                 			 Reporting web application deploys to all nodes in a cluster at
                              		  installation time. Reports are generated from database records.

On Cisco Business Edition
                                             				5000 servers, the Cisco Unified
                                             				Reporting application captures data for Unified Communications Manager only. Due to size constraints,
                                          			 the application does not capture data for Cisco Unity
                                             				Connection . You can use the tool to gather important information
                                          			 about your Unified Communications Manager installation.

### Data Sources Used to Generate Reports

The application captures information from any of the
                                 		  following sources on the publisher node and each subscriber node.

RTMT counters

CDR_CAR
                                       			  ( Unified Communications Manager only)

Unified Communications Manager DB ( Unified Communications Manager only)

IM and Presence DB ( IM and Presence Service only)

disk files

OS API calls

network API calls

prefs

CLI

RIS

The report includes data for all active clusters that
                                 		  are accessible at the time that you generate the report. If the database on the
                                 		  publisher node is down, you can generate a report for the active nodes. The Report Descriptions report in the System Reports
                                 list provides the information sources for a report.

### Supported Output
                           	 Format

## System
                        	 Requirements

### Cisco Tomcat
                              		  Service

Cisco Unified Reporting runs as an application on the
                              		  Cisco Tomcat service, which activates when you install Unified Communications Manager and the IM and
                                 			 Presence Service . Ensure that these products are running on all nodes
                              		  in the cluster.

### HTTPS

The report subsystem
                              		  gathers information from other nodes by using an RPC mechanism via HTTPS.
                              		  Ensure the HTTPS port is open and the Cisco Tomcat service is running on the
                              		  node to successfully generate a report.

To enable HTTPS, you
                              		  must download a certificate that identifies the node during the connection
                              		  process. You can accept the node certificate for the current session only, or
                              		  you can download the certificate to a trust folder (file) to secure the current
                              		  session and future sessions with that node. The trust folder stores the
                              		  certificates for all your trusted sites. For more information about HTTPS, see
                              		  the "Introduction" chapter in the Cisco Unified
                                 			 Communications Manager Administration Guide .

To access the
                              		  application, you access the Administration interface in a browser window. Cisco Unified
                                 			 Reporting uses HTTPS to establish a secure connection to the browser.

### Required Access
                           	 Permissions

The Cisco Unified Reporting application uses the Cisco Tomcat service to authenticate users before allowing access to the web application. Only authorized
                                 users can access the Cisco Unified Reporting application. For Unified Communications Manager , by default, only administrator users in the Standard CCM Super Users group can access Cisco Unified Reporting to view and create reports.

For Cisco Unified Communications Manager and IM and Presence Service , users in the Standard CUReporting Authentication role can access Cisco Unified Reporting .

As an authorized user, you can use the Cisco Unified Reporting user interface to view reports, generate new reports, or download reports.

For Unified Communications Manager , administrator users in the Standard CCM Super Users group can access administrative applications in the Unified Communications Manager Administration navigation menu, including Cisco Unified Reporting , with a single sign-on to one of the applications.

## UI
                        	 Components

The following figure
                              		  shows the UI components for Cisco
                                 			 Unified Reporting .

Upload,
                                       				Download, Generate icons

Report List

Report Details

The report
                                          			 categories, available reports, and report data vary, depending on release.

### Sign In From
                           	 Administration Interface

Perform either of
                                 		  the following steps to sign in to Cisco
                                    			 Unified Reporting from the Administration interface.

For Unified Communications Manager , select Cisco
                                          				  Unified Reporting from the navigation menu in the Cisco Unified CM
                                       				Administration interface.

For the IM and
                                          				  Presence Service , select Cisco
                                          				  Unified IM and Presence Reporting from the navigation menu in the
                                       				Cisco Unified CM IM and
                                          				  Presence Administration interface.

#### Before you begin

## Supported
                        	 Reports

This
                              		  section details the supported reports for Cisco
                                 			 Unified Communications Manager and Cisco
                                 			 Unified Communications Manager IM and Presence Service . You can
                              		  identify a report in Cisco Unified
                                 			 Reporting by the report name and the date-and-time stamp. Cisco Unified
                                 			 Reporting stores a local copy of the most recent report for you to
                              		  view.

### Unified Communications Manager Reports

The following
                                    		  table describes the types of system reports that appear in Cisco Unified
                                       			 Reporting after you install Unified Communications
                                       			 Manager .

Report

Description

UCM Users with Out-Of-Date Credential Algorithm

Provides a list of end users' whose passwords or PINs are stored and hashed using SHA1.

Report Descriptions

Provides troubleshooting and detailed information about the reports that appear.

Security
                                                					 Diagnostic Tool

Provides a
                                                					 summary view of information about security components.

Unified CM
                                                					 Cluster Overview

The Unified Communications Manager or IM and Presence Service versions that are installed in
                                                         						  the cluster

The
                                                         						  hostname or IP address of all nodes in the cluster

A
                                                         						  summary of hardware details

Unified CM
                                                					 Data Summary

Provides a
                                                					 summary of data that exists in the Unified Communications Manager database, according to the
                                                					 structure of the menus in Unified Communications Manager Administration. For example, if
                                                					 you configure three credential policies, five conference bridges, and ten
                                                					 shared-line appearances, you can see that type of information in this report.

Unified CM
                                                					 Database Replication Debug

Provides
                                                					 debugging information for database replication.

Tip

Unified CM
                                                					 Database Status

Provides a
                                                					 snapshot of the health of the Unified Communications Manager database. Generate this report
                                                					 before an upgrade to ensure that the database is healthy.

Unified CM
                                                					 Device Counts Summary

Provides the
                                                					 number of devices by model and protocol that exist in the Unified Communications Manager database.

Unified CM
                                                					 Device Distribution Summary

Provides a
                                                					 summary of how devices are distributed throughout the cluster; for example,
                                                					 this report shows which devices are associated with the primary, secondary, and
                                                					 tertiary nodes.

Unified CM
                                                					 Directory URI and GDPR Duplicates

Provides a
                                                					 detailed list of duplicated User Directory URIs, Learned Directory URIs,
                                                					 Learned Numbers, and Learned Patterns on the system.

Unified CM
                                                					 Extension Mobility

Provides a
                                                					 summary of Cisco Extension
                                                   						Mobility usage; for example, the number of phones that have a Cisco Extension
                                                   						Mobility user logged in to them, the users that are associated with Cisco Extension
                                                   						Mobility , and so on.

Unified CM
                                                					 GeoLocation Policy

Provides a
                                                					 list of records from the GeoLocation Logical Partitioning Policy Matrix.

Unified CM
                                                					 GeoLocation Policy with Filter

Provides a
                                                					 list of records from the GeoLocation Logical Partitioning Policy Matrix for the
                                                					 selected GeoLocation policy.

Unified CM
                                                					 Lines Without Phones

Provides a
                                                					 list of lines that are not associated with a phone.

Unified CM
                                                					 Multi-Line Devices

Provides a
                                                					 list of phones with multiple line appearances.

Unified CM
                                                					 Phone Category

Provides a
                                                					 listing of phone models in a given category for use with the Universal Device
                                                					 Templates. When enabling self provisioning for a user, you may choose to allow
                                                					 any or all of these categories of phones by providing a template for each
                                                					 category.

Unified CM
                                                					 Phone Feature List

Provides a
                                                					 list of supported features for each device type in Unified Communications Manager Administration.

Unified CM
                                                					 Phone Locale Installers

Provides a
                                                					 list of Cisco Unified IP Phone firmware versions supported by the installed
                                                					 Phone Locale Packages.

Unified CM
                                                					 Phones With Mismatched Load

Provides a
                                                					 list of all phones that have a mismatched firmware load.

Unified CM
                                                					 Phones Without Lines

Provides a
                                                					 list of all phones in the Unified Communications Manager database that do not have lines
                                                					 that are associated with them.

Unified CM
                                                					 Shared Lines

Provides a
                                                					 list of all phones in the Unified Communications Manager database with at least one
                                                					 shared-line appearance.

Unified CM
                                                					 Table Count Summary

Provides a
                                                					 database-centric view of data. This report is useful for administrators or AXL
                                                					 API developers that understand database schema.

Unified CM
                                                					 User Device Count

Provides
                                                					 information about associated devices; for example, this report lists the number
                                                					 of phones with no users, the number of users with one phone, and the number of
                                                					 users with more than one phone.

Unified CM
                                                					 Users Sharing Primary Extensions

Provides a
                                                					 list of users that share a primary extension on the system.

Unified CM
                                                					 VG2XX Gateway

Provides a
                                                					 summary of gateway endpoint security profiles.

Unified CM
                                                					 Voice Mail

Provides a
                                                					 summary of voice-messaging-related configuration in Unified Communications Manager Administration; for example,
                                                					 this report lists the number of configured voicemail ports, the number of
                                                					 message waiting indicators, the number of configured voice messaging profiles,
                                                					 the number of directory numbers that are associated with voice message
                                                					 profiles, and so on.

Unified
                                                					 Confidential Access Level Matrix

Provides
                                                					 all information about the Confidential Access Level Matrix.

### IM and Presence Service Reports

The following table describes the types of system reports
                                 		  that display in Cisco Unified Reporting after you install the IM and Presence Service on Unified Communications Manager.

From Release 10.0(1), the IM and Presence cluster information is available from the Cisco Unified Communications Manager node.
                                             From Cisco Unified Communications Manager, select Cisco Unified Reporting > System Reports > Unified CM Cluster Overview .

You can view and generate any of the report types in the following table.

Report

Description

IM and Presence Database Replication Debug

Provides debugging information for database replication.

Tip

IM and Presence Database Status

Provides a snapshot of the health of the IM and Presence Service database. Generate this report before an upgrade to ensure that the database is healthy.

IM and Presence Table Count Summary

Provides a database-centric view of data. This report proves useful for administrators or AXL API developers that understand
                                             the database schema.

IM and Presence User Sessions Report

Provides a list of all active users signed-in sessions with one or more devices.

Presence Configuration Report

- Users that are synced from Cisco Unified Communications Manager

Users that are enabled for IM and Presence Service

Users that are enabled for Microsoft remote call control

Users that are enabled for calendaring information in IM and Presence Service

Click View Details to see the list of users in sortable columns.

IM and Presence Cluster Overview

Provides an overview of the IM and Presence Service cluster. This report, for example, tells you which IM and Presence Service version is installed in the cluster, the hostname or IP address of all nodes in the cluster, a summary of hardware details,
                                             and so on.

Presence Limits Warning Report

Provides information about users that have met or exceeded the configuration limits for the maximum number of contacts or
                                             watchers.

Click View Details to see the list of users in sortable columns.

Presence Usage Report

Provides usage information for logged-in XMPP clients and third-party APIs.

Click View Details to see the list of XMPP clients and third-party APIs in sortable columns.

Report Descriptions

Provides troubleshooting and detailed information about the reports that display. This report provides descriptions for the
                                             report, for each information group, and for each data item, as well as the data sources, symptoms of related problems, and
                                             remedies.

### View Report
                           	 Descriptions

Cisco Unified
                                    			 Reporting provides report help. The Report Descriptions link provides
                                 		  descriptions for the report, for each information group, and for each data
                                 		  item, as well as the data sources, symptoms of related problems, and remedies.

You may still need
                                             			 to contact TAC for additional help on report problems.

Step 1

Select System
                                             				Reports .

Step 2

Select the Report
                                             				Descriptions link in the list of reports.

Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report.

Step 3

Select the Generate
                                             				Report icon.

The report
                                             				generates and is displayed.

### Generate New
                           	 Report

You can
                                 		  generate and view a new report.

#### Before you begin

Ensure
                                 		  that the Cisco Tomcat service is running on at least one node and you are using
                                 		  a supported web browser to view the report.

The application
                                 		  notifies you if a report will take excessive time to generate or consume
                                 		  excessive CPU time. A progress bar displays while the report generates. The new
                                 		  report displays, and the date and time updates.

Step 1

Select System
                                             				Reports from the menu bar.

Step 2

Select a report.

Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report.

Step 3

Select the Generate
                                             				Report (bar chart) icon in the Reports window.

Step 4

Select
                                          			 the View
                                             				Details link to expose details for a section that does not
                                          			 automatically appear.

#### What to do next

If the report shows
                                 		  an unsuccessful data check for an item, select the Report
                                    			 Descriptions report and review the troubleshooting information and
                                 		  possible remedies. Because the report descriptions report is dynamically
                                 		  generated from the database, you can also generate a new report descriptions
                                 		  report.

### View Saved
                           	 Report

You can
                                 		  view a copy of an existing report.

During a fresh
                                                				install or upgrade, the Cisco Unified
                                                   				  Reporting application does not save a local copy of the most recent
                                                				report.

#### Before you begin

Ensure that the
                                 		  Cisco Tomcat service is running on at least one node and you are using a
                                 		  supported web browser to view the report.

Step 1

Select System
                                             				Reports from the menu bar.

Step 2

Select the
                                          			 report that you want to view from the reports list.

Step 3

Select the link
                                          			 for the report name (dated and time stamped).

Step 4

Select the View
                                             				Details link for details for a section that does not automatically
                                          			 appear.

#### What to do next

Download a new or
                                 		  saved report.

If the report shows
                                 		  an unsuccessful data check for an item, select the Report
                                    			 Descriptions report and review the troubleshooting information for
                                 		  possible remedies.

### Download New
                           	 Report

To
                                 		  download a new report, you store it locally on your hard drive. Downloading a
                                 		  report downloads the raw XML data file to your hard drive.

Step 1

Generate the new
                                          			 report.

Step 2

After the new
                                          			 report appears, select the Download
                                             				Report (green arrow) icon in the Reports window.

You do not
                                                         				  need to click the View
                                                            					 Details link for report details before you download the document.
                                                         				  The data are captured in the downloaded file.

Step 3

Select Save to save the file to the location on your disk
                                          			 that you designate.

To change the
                                             				filename or the location where your file is stored on your hard disk, enter a
                                             				new location or rename the file (optional). A progress bar shows the download
                                             				in progress.

The file
                                             				downloads to your hard disk.

Step 4

After the
                                          			 download completes, select Open to open the XML report.

Do not change
                                                         				  the contents in the XML file, or your report may not appear properly on the
                                                         				  screen.

#### What to do next

To view a
                                 		  downloaded report file in your browser, upload the file to your node.

For technical
                                             			 assistance, you can attach the downloaded file in an e-mail or upload the file
                                             			 to another node.

### Download Saved
                           	 Report

To
                                 		  download saved reports, you download the report and store it locally on your
                                 		  hard drive. Downloading a report downloads the raw XML data file to your hard
                                 		  disk.

Step 1

Open and view
                                          			 the details of the existing report.

Step 2

Select the Download
                                             				Report (green arrow) icon in the Reports window.

Step 3

Select Save to save the file to the location on your disk
                                          			 that you designate.

To change the
                                             				filename or the location where your file is stored on your hard disk, enter a
                                             				new location or rename the file (optional). A progress bar shows the download
                                             				in progress.

The file
                                             				downloads to your hard disk.

Step 4

After the
                                          			 download completes, select Open to open the XML report.

Do not
                                                            					 change the contents in the XML file, or your report may not appear properly.

#### What to do next

To view a
                                 		  downloaded report file in your browser, upload the file to your node.

For technical
                                                				assistance, you can attach the downloaded file in an e-mail or upload the file
                                                				to another node.

### Upload
                           	 Report

To view a
                                 		  downloaded report in your browser window, you must upload the report to the
                                 		  nodetand,.

#### Before you begin

Download a
                                 		  report to your hard drive.

Step 1

Select System
                                             				Reports from the menu bar.

Step 2

Access any
                                          			 report to display the Upload
                                             				Report (blue arrow) icon in the Reports window.

Step 3

Select the Upload
                                             				Report icon.

Step 4

To locate the
                                          			 .xml file, select Browse to navigate to its location on your hard
                                          			 drive.

Step 5

Select Upload .

Step 6

Select Continue to display the uploaded file in the browser
                                          			 window.

#### What to do next

You can
                                 		  compare an uploaded report and a newly generated report side-by-side during an
                                 		  upgrade.

| Note | Unless stated
                                          			 otherwise, the information, notes, and procedures in this guide apply to Unified Communications Manager and the IM and
                                             				Presence Service . |
|---|---|

| Note | On Cisco Business Edition
                                             				5000 servers, the Cisco Unified
                                             				Reporting application captures data for Unified Communications Manager only. Due to size constraints,
                                          			 the application does not capture data for Cisco Unity
                                             				Connection . You can use the tool to gather important information
                                          			 about your Unified Communications Manager installation. |
|---|---|

| Note | For Unified Communications Manager , administrator users in the Standard CCM Super Users group can access administrative applications in the Unified Communications Manager Administration navigation menu, including Cisco Unified Reporting , with a single sign-on to one of the applications. |
|---|---|

| Note | The report
                                          			 categories, available reports, and report data vary, depending on release. |
|---|---|

| Report | Description |
|---|---|
| UCM Users with Out-Of-Date Credential Algorithm | Provides a list of end users' whose passwords or PINs are stored and hashed using SHA1. |
| Report Descriptions | Provides troubleshooting and detailed information about the reports that appear. |
| Security
                                                					 Diagnostic Tool | Provides a
                                                					 summary view of information about security components. |
| Unified CM
                                                					 Cluster Overview | Provides an overview of the Unified Communications Manager cluster. This report includes
                                                					 the following details: The Unified Communications Manager or IM and Presence Service versions that are installed in
                                                         						  the cluster The
                                                         						  hostname or IP address of all nodes in the cluster A
                                                         						  summary of hardware details |
| Unified CM
                                                					 Data Summary | Provides a
                                                					 summary of data that exists in the Unified Communications Manager database, according to the
                                                					 structure of the menus in Unified Communications Manager Administration. For example, if
                                                					 you configure three credential policies, five conference bridges, and ten
                                                					 shared-line appearances, you can see that type of information in this report. |
| Unified CM
                                                					 Database Replication Debug | Provides
                                                					 debugging information for database replication. Tip For this report, generation may spike CPU and take up to 10
                                                         					 seconds per node in the cluster. | Tip | For this report, generation may spike CPU and take up to 10
                                                         					 seconds per node in the cluster. |
| Tip | For this report, generation may spike CPU and take up to 10
                                                         					 seconds per node in the cluster. |
| Unified CM
                                                					 Database Status | Provides a
                                                					 snapshot of the health of the Unified Communications Manager database. Generate this report
                                                					 before an upgrade to ensure that the database is healthy. |
| Unified CM
                                                					 Device Counts Summary | Provides the
                                                					 number of devices by model and protocol that exist in the Unified Communications Manager database. |
| Unified CM
                                                					 Device Distribution Summary | Provides a
                                                					 summary of how devices are distributed throughout the cluster; for example,
                                                					 this report shows which devices are associated with the primary, secondary, and
                                                					 tertiary nodes. |
| Unified CM
                                                					 Directory URI and GDPR Duplicates | Provides a
                                                					 detailed list of duplicated User Directory URIs, Learned Directory URIs,
                                                					 Learned Numbers, and Learned Patterns on the system. |
| Unified CM
                                                					 Extension Mobility | Provides a
                                                					 summary of Cisco Extension
                                                   						Mobility usage; for example, the number of phones that have a Cisco Extension
                                                   						Mobility user logged in to them, the users that are associated with Cisco Extension
                                                   						Mobility , and so on. |
| Unified CM
                                                					 GeoLocation Policy | Provides a
                                                					 list of records from the GeoLocation Logical Partitioning Policy Matrix. |
| Unified CM
                                                					 GeoLocation Policy with Filter | Provides a
                                                					 list of records from the GeoLocation Logical Partitioning Policy Matrix for the
                                                					 selected GeoLocation policy. |
| Unified CM
                                                					 Lines Without Phones | Provides a
                                                					 list of lines that are not associated with a phone. |
| Unified CM
                                                					 Multi-Line Devices | Provides a
                                                					 list of phones with multiple line appearances. |
| Unified CM
                                                					 Phone Category | Provides a
                                                					 listing of phone models in a given category for use with the Universal Device
                                                					 Templates. When enabling self provisioning for a user, you may choose to allow
                                                					 any or all of these categories of phones by providing a template for each
                                                					 category. |
| Unified CM
                                                					 Phone Feature List | Provides a
                                                					 list of supported features for each device type in Unified Communications Manager Administration. |
| Unified CM
                                                					 Phone Locale Installers | Provides a
                                                					 list of Cisco Unified IP Phone firmware versions supported by the installed
                                                					 Phone Locale Packages. |
| Unified CM
                                                					 Phones With Mismatched Load | Provides a
                                                					 list of all phones that have a mismatched firmware load. |
| Unified CM
                                                					 Phones Without Lines | Provides a
                                                					 list of all phones in the Unified Communications Manager database that do not have lines
                                                					 that are associated with them. |
| Unified CM
                                                					 Shared Lines | Provides a
                                                					 list of all phones in the Unified Communications Manager database with at least one
                                                					 shared-line appearance. |
| Unified CM
                                                					 Table Count Summary | Provides a
                                                					 database-centric view of data. This report is useful for administrators or AXL
                                                					 API developers that understand database schema. |
| Unified CM
                                                					 User Device Count | Provides
                                                					 information about associated devices; for example, this report lists the number
                                                					 of phones with no users, the number of users with one phone, and the number of
                                                					 users with more than one phone. |
| Unified CM
                                                					 Users Sharing Primary Extensions | Provides a
                                                					 list of users that share a primary extension on the system. |
| Unified CM
                                                					 VG2XX Gateway | Provides a
                                                					 summary of gateway endpoint security profiles. |
| Unified CM
                                                					 Voice Mail | Provides a
                                                					 summary of voice-messaging-related configuration in Unified Communications Manager Administration; for example,
                                                					 this report lists the number of configured voicemail ports, the number of
                                                					 message waiting indicators, the number of configured voice messaging profiles,
                                                					 the number of directory numbers that are associated with voice message
                                                					 profiles, and so on. |
| Unified
                                                					 Confidential Access Level Matrix | Provides
                                                					 all information about the Confidential Access Level Matrix. |

| Tip | For this report, generation may spike CPU and take up to 10
                                                         					 seconds per node in the cluster. |
|---|---|

| Note | From Release 10.0(1), the IM and Presence cluster information is available from the Cisco Unified Communications Manager node.
                                             From Cisco Unified Communications Manager, select Cisco Unified Reporting > System Reports > Unified CM Cluster Overview . |
|---|---|

| Report | Description |
|---|---|
| IM and Presence Database Replication Debug | Provides debugging information for database replication. Tip For this report, generation may spike CPU and take up to 10 seconds per node in the cluster. | Tip | For this report, generation may spike CPU and take up to 10 seconds per node in the cluster. |
| Tip | For this report, generation may spike CPU and take up to 10 seconds per node in the cluster. |
| IM and Presence Database Status | Provides a snapshot of the health of the IM and Presence Service database. Generate this report before an upgrade to ensure that the database is healthy. |
| IM and Presence Table Count Summary | Provides a database-centric view of data. This report proves useful for administrators or AXL API developers that understand
                                             the database schema. |
| IM and Presence User Sessions Report | Provides a list of all active users signed-in sessions with one or more devices. |
| Presence Configuration Report | Provides configuration information about IM and Presence Service users. Users that are synced from Cisco Unified Communications Manager Users that are enabled for IM and Presence Service Users that are enabled for Microsoft remote call control Users that are enabled for calendaring information in IM and Presence Service Click View Details to see the list of users in sortable columns. |
| IM and Presence Cluster Overview | Provides an overview of the IM and Presence Service cluster. This report, for example, tells you which IM and Presence Service version is installed in the cluster, the hostname or IP address of all nodes in the cluster, a summary of hardware details,
                                             and so on. |
| Presence Limits Warning Report | Provides information about users that have met or exceeded the configuration limits for the maximum number of contacts or
                                             watchers. Click View Details to see the list of users in sortable columns. |
| Presence Usage Report | Provides usage information for logged-in XMPP clients and third-party APIs. Click View Details to see the list of XMPP clients and third-party APIs in sortable columns. |
| Report Descriptions | Provides troubleshooting and detailed information about the reports that display. This report provides descriptions for the
                                             report, for each information group, and for each data item, as well as the data sources, symptoms of related problems, and
                                             remedies. |

| Tip | For this report, generation may spike CPU and take up to 10 seconds per node in the cluster. |
|---|---|

| Note | You may still need
                                             			 to contact TAC for additional help on report problems. |
|---|---|

| Step 1 | Select System
                                             				Reports . |
|---|---|
| Step 2 | Select the Report
                                             				Descriptions link in the list of reports. Note Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report. | Note | Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report. |
| Note | Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report. |
| Step 3 | Select the Generate
                                             				Report icon. The report
                                             				generates and is displayed. |

| Note | Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report. |
|---|---|

| Step 1 | Select System
                                             				Reports from the menu bar. |
|---|---|
| Step 2 | Select a report. Note Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report. | Note | Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report. |
| Note | Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report. |
| Step 3 | Select the Generate
                                             				Report (bar chart) icon in the Reports window. |
| Step 4 | Select
                                          			 the View
                                             				Details link to expose details for a section that does not
                                          			 automatically appear. |

| Note | Re-enter your Cisco
                                                            					 Unified Communications Manager Administration login credentials if
                                                         				  you are prompted to re-login when you select an IM and
                                                            					 Presence Service report. |
|---|---|

| Note | During a fresh
                                                				install or upgrade, the Cisco Unified
                                                   				  Reporting application does not save a local copy of the most recent
                                                				report. |
|---|---|

| Step 1 | Select System
                                             				Reports from the menu bar. |
|---|---|
| Step 2 | Select the
                                          			 report that you want to view from the reports list. |
| Step 3 | Select the link
                                          			 for the report name (dated and time stamped). |
| Step 4 | Select the View
                                             				Details link for details for a section that does not automatically
                                          			 appear. |

| Step 1 | Generate the new
                                          			 report. |
|---|---|
| Step 2 | After the new
                                          			 report appears, select the Download
                                             				Report (green arrow) icon in the Reports window. Note You do not
                                                         				  need to click the View
                                                            					 Details link for report details before you download the document.
                                                         				  The data are captured in the downloaded file. | Note | You do not
                                                         				  need to click the View
                                                            					 Details link for report details before you download the document.
                                                         				  The data are captured in the downloaded file. |
| Note | You do not
                                                         				  need to click the View
                                                            					 Details link for report details before you download the document.
                                                         				  The data are captured in the downloaded file. |
| Step 3 | Select Save to save the file to the location on your disk
                                          			 that you designate. To change the
                                             				filename or the location where your file is stored on your hard disk, enter a
                                             				new location or rename the file (optional). A progress bar shows the download
                                             				in progress. The file
                                             				downloads to your hard disk. |
| Step 4 | After the
                                          			 download completes, select Open to open the XML report. Note Do not change
                                                         				  the contents in the XML file, or your report may not appear properly on the
                                                         				  screen. | Note | Do not change
                                                         				  the contents in the XML file, or your report may not appear properly on the
                                                         				  screen. |
| Note | Do not change
                                                         				  the contents in the XML file, or your report may not appear properly on the
                                                         				  screen. |

| Note | You do not
                                                         				  need to click the View
                                                            					 Details link for report details before you download the document.
                                                         				  The data are captured in the downloaded file. |
|---|---|

| Note | Do not change
                                                         				  the contents in the XML file, or your report may not appear properly on the
                                                         				  screen. |
|---|---|

| Note | For technical
                                             			 assistance, you can attach the downloaded file in an e-mail or upload the file
                                             			 to another node. |
|---|---|

| Step 1 | Open and view
                                          			 the details of the existing report. |
|---|---|
| Step 2 | Select the Download
                                             				Report (green arrow) icon in the Reports window. |
| Step 3 | Select Save to save the file to the location on your disk
                                          			 that you designate. To change the
                                             				filename or the location where your file is stored on your hard disk, enter a
                                             				new location or rename the file (optional). A progress bar shows the download
                                             				in progress. The file
                                             				downloads to your hard disk. |
| Step 4 | After the
                                          			 download completes, select Open to open the XML report. Note Do not
                                                            					 change the contents in the XML file, or your report may not appear properly. | Note | Do not
                                                            					 change the contents in the XML file, or your report may not appear properly. |
| Note | Do not
                                                            					 change the contents in the XML file, or your report may not appear properly. |

| Note | Do not
                                                            					 change the contents in the XML file, or your report may not appear properly. |
|---|---|

| Note | For technical
                                                				assistance, you can attach the downloaded file in an e-mail or upload the file
                                                				to another node. |
|---|---|

| Step 1 | Select System
                                             				Reports from the menu bar. |
|---|---|
| Step 2 | Access any
                                          			 report to display the Upload
                                             				Report (blue arrow) icon in the Reports window. |
| Step 3 | Select the Upload
                                             				Report icon. |
| Step 4 | To locate the
                                          			 .xml file, select Browse to navigate to its location on your hard
                                          			 drive. |
| Step 5 | Select Upload . |
| Step 6 | Select Continue to display the uploaded file in the browser
                                          			 window. |