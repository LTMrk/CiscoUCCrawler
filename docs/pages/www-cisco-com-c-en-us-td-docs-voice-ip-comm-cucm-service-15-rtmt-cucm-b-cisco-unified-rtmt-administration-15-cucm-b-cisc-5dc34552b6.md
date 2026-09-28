---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-15-rtmt-cucm-b-cisco-unified-rtmt-administration-15-cucm-b-cisc-5dc34552b6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/15/rtmt/cucm_b_cisco-unified-rtmt-administration-15/cucm_b_cisco-unified-rtmt-administration-1251su2_chapter_0100.html
retrieved_at: 2026-08-17T00:24:17.943240+00:00
---

Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 15 and SUs

# Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 15 and SUs

Updated: August 6, 2026

Chapter: Cisco Unified Analysis Manager

## Chapter: Cisco Unified Analysis Manager

# Cisco Unified Analysis Manager

## Cisco Unified Analysis Manager Preferences

Use the Unified Analysis Manager dropdown menu to set preferences for:

### FTP Server Setup

This function allows you to configure a FTP Server which you can then use to export information to. These servers can be Cisco
                                 TAC FTP servers. This information can include things such as logs, trace files, and system call trace information.

By default, the Cisco TAC FTP server will be pre-populated. You can modify this configuration for the default FTP server.

The FTP Server option allows you to manage the configured servers. You can perform the following operations:

Add a new FTP server

Edit an existing FTP server

Delete FTP servers

Test the connection of an FTP server

Cisco TAC has two FTP servers you can configure for exporting files:

ftp-rtp.cisco.com

ftp-sj.cisco.com

On both servers, files should be uploaded to the /incoming directory.

#### Access FTP Server Options

The following procedure explains how to access the FTP Server Options:

Step 1

From the Unified Analysis Manager drop-down menu, select AnalysisManager > Preferences .

The Preferences window displays. Click FTP Server .

Step 2

The FTP Servers screen displays with a list of configured servers and buttons to Add , Edit , or Delete a server. The Test Connection button allows you to test connectivity to a server.

Step 3

Use the buttons to select the option you want.

#### Add or Edit FTP Server

Follow this procedure to add an FTP Server or edit an existing configuration:

Step 1

From the Unified Analysis Manager drop-down menu, select AnalysisManager > Preferences . The Preferences window appears. Click FTP Server .

Step 2

The FTP Servers screen displays with a list of configured servers and buttons to Add , Edit , or Delete a server. The Test Connection button allows you to test connectivity to a server.

Step 3

Click the Add button to add a server or the Edit button to edit an existing configuration. The Add FTP Server screen appears.

Step 4

In the Name/IP Address field, enter the name or the IP address of the FTP server you are adding.

Step 5

In the Protocol field, select either the FTP or SFTP protocol, depending on the type of server you are connecting to. Use SFTP if you are
                                             connecting to a Cisco TAC server.

Step 6

In the User Name and Password fields, enter the username and password that gives you access to the server.

Step 7

In the Port field, enter the port number on the server that you will be using.

Step 8

In the Destination Directory field, enter the path for the directory to which you will be exporting files. If you are adding a Cisco TAC server, use the /incoming directory.

Step 9

Click the OK button to add the server. You can use the Cancel button to end the operation without adding the FTP server.

### Set Up Mail Server

This option allows you to configure a mail server for the purpose of notifying a set of user configured recipients on the
                                 status of Unified Analysis Manager operations such as trace and log collections and file transfers.

You must configure at least one mail server in order to be able to send a notification.

You can configure a maximum of two mail servers.

You can only use mail servers configured with this option for Unified Analysis Manager notifications. For RTMT notifications,
                                                   you must configure a separate mail server.

#### Add or Edit Mail Server

The following procedure explains how to add a Mail Server or edit an existing configuration:

Step 1

From the Unified Analysis Manager drop-down menu, select AnalysisManager > Preferences .

The Preferences window displays. Click Mail Server .

Step 2

The Mail Servers screen appears with a list of configured servers and buttons to Add , Edit , or Delete a server. The Test  Connectivity button allows you to test connectivity to a server. The Refresh button allows you to reload the server.

Step 3

Click the Add button to add a server or the Edit button to edit an existing configuration. On clicking the Add button, the Add Mail Server screen appears.

Step 4

In the Name/IP Address field, enter the name or the IP address of the Mail server you are adding.

Step 5

In the Port No. field, enter the port number on the server that you will be using.

Step 6

Click Save button to save the settings or the Cancel button to end the operation without adding the Mail server. The Test Connection button allows you to test connectivity to a server.

### Set Trace Collection Directory

Follow this procedure to use the Trace Collection option under Preferences to set a directory for trace logs:

Step 1

From the Unified Analysis Manager drop-down menu, select AnalysisManager > Preferences .

The Preferences window appears. Click Trace Collection .

Step 2

The Trace Collection screen appears. Enter the directory you want to use for traces logs in the Download Directory box, or use the Browse button to locate the directory. Optionally, you can click the Default button to select the default dirctory.

Step 3

Click Save .

## Cisco Unified
                        	 Analysis Manager Limitations

Please
                              		  consider the following limitations when you use the Unified Analysis Manager.

The maximum
                                    				number of call records that the CallSearch Report can display is 500.

The maximum
                                    				number of call records that the Call Track Report can display is 100.

Since there is
                                    				no globally unique callID to use, Unified Analysis Manager uses link-by-link
                                    				approach to trace the call. If any record for a call is missing in one of the
                                    				products in the call path, the link will be broken for the rest of the chain
                                    				and the tracking will not be complete.

Call records are
                                    				not stored in the database orderly based on any particular column. When running
                                    				Call Search Report, the number of returned records is limited to 500. The 500
                                    				records that are retrieved may not be the earliest (based on originating time,
                                    				connection time, or disconnect time) in the specified time range. To make sure
                                    				all of the call records within the specified time range are retrieved, you need
                                    				to shorten the time range until the returned number of records is less than
                                    				500.

The Unified
                                    				Analysis Manager option is not displayed when the Unified RTMT is
                                    				connected to a Cisco Unity
                                       				  Connection or IM and
                                       				  Presence node, because these products do not have a Call Record
                                    				database.

When you use the Unified RTMT to connect to a Unified Communications Manager node, you can add nodes to include Cisco Unity Connection and IM and Presence nodes in the Unified Analysis Manager.

Call Tracking
                                    				does not support tracking of SIP Unified Outbound Option calls from Unified CCE
                                    				and Unified IME to Cisco IOS gateways.

Call Tracking
                                    				does not support direct call tracking of call paths using a GED-125 protocol
                                    				from Unified CCE to Unified CVP.

Unified Communications Manager needs to be in the call path for tracking calls from Unified Communications Manager.

Call tracking only supports single branch tracking from Unified Communications Manager.

No Call Detail Records (CDR) are generated for calls on the MGCP gateway, because the gateway does not implement call control
                                    and Q.931 is tunneled to the Unified Communications Manager for signaling. The CDR is available only on the Unified Communications
                                    Manager.

With ACS
                                    				servers, Unified Analysis Manager is used only for call tracing, and then used
                                    				only if you want to include gateway records and information in the tracing
                                    				data. If you do not have an ACS server or a supported hardware/software version
                                    				of the ACS server, most of Unified Analysis Manager functions in your
                                    				deployment will continue to work; however, your gateway information will not be
                                    				included in your call traces.

## Cisco Unified Analysis Manager Setup

The Administration option on the Unified Analysis Manager menu allows you to import device and group configurations from a .csv file to the
                              Unified Analysis Manager tool.

### Import Device and Group Settings

Follow this procedure to import device and group configuration from a .csv file into the Unified Analysis Manager.

Step 1

From the Unified Analysis Manager menu, select Administration > Import .

Step 2

Select the .csv configuration file that you want to import.

Step 3

Click the Import button.

The selected file appears.

### Scheduled Trace and Log Collection Job Status Display

This function allows you to display status of scheduled trace setting and log collection jobs. Jobs can be scheduled using
                                 the Unified Analysis Manager Tools. Once a device is added to a group, you can schedule trace setting and log collections
                                 jobs on the device.

A scheduled job is linked to the machine it is configured on, and the job cannot be run on a different machine. If the machine
                                 on which a job was scheduled is not usable for any reason, the old job can be cloned and saved as a new job with new parameters
                                 to be run on the new machine.

Jobs running on a device can have one of the following states:

Scheduled: A job is scheduled within Unified Analysis Manager; however it has not started

Running: A job that is currently either setting traces or collecting logs

Completed: A job that is done

Pending: A job that has completed one run of collecting logs and is waiting to start the next run.

Aborted: A job that has stopped abnormally due to an unexpected error

Canceled: A job that has stopped due to a cancel operation by the user.

The Job Status screen gives a system view of all the jobs in Unified Analysis Manager. For jobs that have multiple runs, the
                                 status and time of the last run is also shown in this page.

The following operations can be performed on a job:

View Details: Use this option to get more detailed view of the job.

Cancel: Use this option to cancel a job. The Cancel operation can only be done on the machine that the job is running or scheduled
                                       on. This option cannot be used for jobs that are in the Completed/Aborted/Canceled state.

Clone: Use this option to select any job and save it as a new job. The job being cloned from can be in any state. This option
                                       allows you to change any attribute of the job before saving. Cloning a job does not impact the attributes of the job being
                                       cloned.

### Upload and Transfer Files to FTP Server

This option allows you to transfer files to a configured FTP server and send an email to interested parties. You can use this
                                 option to transfer some files to another machine so they can be viewed by others.

This screen allows you to specify the files and folders to be transferred as well as any annotations to accompany those files.

Follow this procedure to transfer files to an FTP server:

Step 1

From the Unified Analysis Manager menu, select Administration > Upload Files .

The Upload Files screen appears.

Step 2

In the Case ID field, enter the number that Cisco TAC has assigned to the case.

Step 3

Use the drop-down list box in the Send to Server field to select the FTP server you are sending the file to.

Step 4

Use the Notes box to provide any additional information about the file.

Step 5

Use the Send Email Notifications check box if you want to add the email addresses to send a notification that the file is uploaded. To add multiple email
                                          addresses, add the mail ids separated by comma. The mail addresses can be only the < username > or it can be of the format username@domain.com .

Step 6

In the bottom section of the screen, in the Files to upload box, select the files you want to transfer. Use the Add or Remove buttons to select or deselect files from the system. The files selected will be zipped by default and then uploaded. The
                                          name of the zipped file will be of the format <case id>_uploadedfile.zip .

Step 7

Click the OK button to transfer the file.

## Cisco Unified Analysis Manager Tools

This chapter provides information about the Unified Analysis Manager,  which provides a set of tools that allows you to perform
                           management tasks for specific devices and groups of devices.

### Analyze Call Path Tool

The Analyze Call Path tool allows you to trace a call between multiple Cisco Unified Communications products. In order to
                                 trace a call using the Analyze Call Path tool, a node must be defined in Unified Analysis Manager and the node must belong
                                 to a group.

All nodes that you define are assigned to the AllNodes group by default. Use the Node Groups function if you want to assign
                                             the node to a different group. See the topics related to the Analyze Call Path setup for more information on configuring a
                                             Call Record Repository before using the Analyze Call Path function.

Step 1

From the Unified Analysis Manager menu, select Tools > Analyze Call Path .

The Analyze Call Path Information window appears.

Step 2

Click the Continue button. The Search Criteria window appears.

Step 3

Enter the number where the call originated in the Calling Number field. The default is an asterisk (*) which is a wildcard that will trace all numbers for the node.

Step 4

Enter the number where the call terminated in the Called Number field. The default is an asterisk (*) which is a wildcard that will trace all numbers for the node.

Step 5

Use the Termination Cause drop-down list box to select the reason for the call termination; either Abandoned, Dropped, Failed or all three.

Step 6

Use the Start Time field to enter the start time for the trace.

Step 7

Use the Duration field to indicate the length of the time period you want to trace.

Step 8

Use the Time Zone drop-down list box to select the time zone where you are tracing calls.

Step 9

Use the Filter Nodes by Group drop-down list box to select the group of nodes that you want to trace.

Step 10

Use the and Node Type drop-down list box to select specific types of nodes that you want to trace.

When you have selected the Group and Node, information displays for each node. You can then use the check box for each node
                                             listed to select or deselect the node.

The limit for the number of nodes that you can select at a time is 20.

Step 11

Click the Run button to begin the trace. The trace results display on the bottom of the window. If you selected multiple nodes, a tab is
                                          displayed for each node. Click the tab to display information for that node.

Step 12

When the call record information appears, you can click the View Full Path button to see the complete call path. You can click the View Record Details button to see the information about the call. Use the Save Results button to save the reports.

#### Analyze Call Path Setup Considerations

Caution

The Analyze Call Path Tool might not work correctly if your computer is set to a language other than English.

When using the Analyze Call Path tool, there are configuration considerations for each product that the Unified Analysis Manager
                                    manages.

The Analyze Call Path tool does not include information for Cisco Unity Connection and IM and Presence servers.

##### Cisco Unified
                                 	 Communications Manager

The following information applies when configuring the Analyze Call Path for Unified Communications Manager:

Version Support—Unified Analysis Manager supports Release 8.0(1) and above for Unified Communications Manager.

Call Record
                                             				Repository—Use the first node (publisher) as the Call Record Repository with
                                             				the HTTPS protocol and the default port 8443.

User Group and
                                             				Access Permissions— Users should belong to a user group whose role contains
                                             				read and update permissions required to access Call Records for the following
                                             				resources:

SOAP Call
                                                   					 Record APIs

SOAP
                                                   					 Control Center APIs

SOAP
                                                   					 Diagnostic Portal Database Service

SOAP Log
                                                   					 Collection API

SOAP
                                                   					 Performance Informations APIs

SOAP
                                                   					 Realtime Informations and Control Center APIs

New resources "SOAP Diagnostic Portal Database Service" and "SOAP Call Record APIs" added on an upgrade should not
                                                               						have the read and update permissions by default due to security reasons for
                                                               						existing users. Users need to create or copy the role to custom resources and
                                                               						update the required permissions for above mentioned resources as needed. See
                                                               						the Administration Guide
                                                                     							 for Cisco Unified Communications Manager for additional details.

Configuring NTP—Each product installed in the solution should be configured to point to same set of external NTP clock sources.
                                             NTP is required to be configured on all nodes that involve calls for SCT features. For Unified Communications Manager, use
                                             the utils ntp config CLI command to configure NTP.

Enable Call Record Logging—In Cisco Unified Communications Manager Administration, go to the Service Parameter Configuration
                                             window, and choose the Cisco CallManager Service . Enable the CDR Enabled Flag and the CDR Log Calls with Zero Duration Flag parameters. Restart the Cisco CallManager service for change-notification to take effect immediately. Repeat this procedure for all nodes in the Unified Communications
                                             Manager cluster.

You can
                                                         				  verify that flags are set as desired at https://<HOSTNAME:PORT>/ccmadmin/vendorConfigHelp.do

CDR CAR
                                             				Loader—Ensure your CDR Analysis and Reporting (CAR) Loader is set to Continuous
                                                				  Loading 24/7 . To verify this:

Go to the Cisco Unified
                                                      						Serviceability and select Tools > CDR Analysis and Reporting
                                                         						  (CAR) page. The CAR page opens in a new browser.

Go to System > Scheduler > CDR Load
                                                         						  page .

Verify if Loader is not disabled and that Continuous Loading 24/7 is enabled. This allows CDR records that are generated from Unified Communications Manager nodes to be loaded into the CAR
                                                   database as soon as they arrive to Unified Communications Manager first node (publisher).

If call records are not found on the Unified Communications Manager, it is possible that the CAR Loader failed or is having
                                                   a delay loading the latest CDR records. If this occurs, go to the CAR System > Database > Manual Purge page and click the Table Information button. Check for the oldest and latest CDR records that are available in the CAR database. If records are not set to the
                                                   latest date, go to System > Log Screens > Event Log and select CDR Load to check its recent run status to see if there were any Unsuccessful runs. If CDR Load failure is found, collect CAR Scheduler
                                                   traces to provide to Cisco Support for troubleshooting.

Raw Call Record Details—For information about Raw Call Record details help for Unified Communications Manager, see the Cisco Unified Communications Manager Call Detail Records Administration Guide .

##### Cisco Unified Contact Center Express

The following information applies when configuring the Analyze Call Path for Unified CCX:

Version Support—Unified Analysis Manager supports Unified CCX version 8.0(1) and later.

Call Record Repository—The Call Record Repository used for Unified CCX is either (or both in the case of a High Availability
                                             system) of the Unified CCX nodes. The database is active on both nodes and the data is replicated. The JDBC user is uccxsct and the password is the encrypted version of the TFTP password. The password is typically set by the Unified CCX administrator.

Default user for adding Unified CCX Call Record Repository—The Informix user for adding (and connecting to) Unified CCX Call
                                             Record Repository is: uccxsct . You can reset the default install time password for above user in the Unified CCX Application Administration > Tools > Password Management page. Typically, the Unified CCX administrator will reset to the desired password and pass it on to the Unified Analysis
                                             Manager administrator.

User Group and Access Permissions—Unified CCX does not require any additional user group and access permission to access Call
                                             Records. The access permissions of the uccxsct user is set by Unified CCX install for read access to specific tables. No external
                                             settings are required.

Configuring NTP—To configure NTP for Unified CCX, go to OS Administration > Settings > NTP Server .

Enable Call Record Logging—Unified CCX always generates Call Records by default, so no configuration is required to enable
                                             logging of Call Records.

##### Cisco Unified Intelligent Contact Management Enterprise/Cisco Unified Contact Center Enterprise

The following information applies when configuring the Analyze Call Path for Cisco Unified Intelligent Contact Management
                                       Enterprise (Unified ICME) and Unified CCE:

Version Support—Unified Analysis Manager supports Release 8.0(1) and above for Unified ICME and Unified CCE.

Call Record Repository—The Call Record Repository used for Unified ICME is either AW-HDS-DDS or HDS-DDS. The server used for
                                             Unified CCE is HDS/AW Database (port 1433).

User Group and Access Permissions—For Release 8.0(1), the recommended user group and access permissions that are required
                                             to access Call records are the Windows only Authentication for SQL Server. This is done by using the User List tool from the Configuration Manager and creating a user with the right access privileges.

Configuring NTP—Configuration for Time Synchronization of Unified CCE servers is based on Microsoft Windows Time Services.
                                             When setting up the Unified CCE router component, retain the default settings of the "Disable ICM Time Synchronization" box as checked. With the recommended default setting, the time synchronization for Unified CCE servers is provided by the
                                             Windows Time Service, which automatically synchronizes the computer's internal clock across the network. The time source for
                                             this synchronization varies, depending on whether the computer is in an Active Directory domain or a workgroup. For additional
                                             information on setting up Windows Time Service, refer to the Microsoft Windows Time Service Technical Reference documentation
                                             at: http://technet.microsoft.com/en-us/library/cc773061(WS.10).aspx .

Enable Call Record Logging—To check that Call Record logging is enabled, first be sure that the Unified Analysis Manager service
                                             on Unified CCE is enabled. Using the web setup, you need to install the AW-HDS-DDS or HDS-DDS servers with Administration
                                             and Data Server roles. Once you install these roles using the web setup, the call records are available by default.

Raw Call Record Details—To find help for the Raw Call Record details, refer to the Schema Help which you can access from the
                                             Unified CCE Administration Tool group on either the AW-HDS-DDS or HDS-DDS server. You can also refer to the United CCE Database
                                             Schema Handbook for a specific release at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html .

If you are using RTMT to monitor Cisco Unified Contact Center Enterprise, you must open the following file and change the
                                                   value for ReadTimeout to 360: <RTMT_INSTALLATION_FOLDER_PATH>/conf/rtmt.xml . If you don't change the value, RTMT will not be able to collect OPC logs because RTMT's default timeout value is greater
                                                   than the time it takes to collect OPC logs.

##### Cisco Unified Customer Voice Portal

The following information applies when configuring the Analyze Call Path for Unified CVP:

Version Support—United Analysis Manager supports Unified CVP Release 8.0(1) and above.

Call Record Repository—Unified CVP uses the Unified CVP Reporting Server for the Call Record Repository.

User Group and Access Permissions—Unified CVP uses Unified CVP OAMP to set user group and access permissions required to access
                                             Call Records:

All users trying to access Unified CVP records from the Unified CVP database need to be created through Unified CVP OAMP.

Unified CVP Reporting users need to be granted the Unified CVP Reporting role in Unified CVP OAMP.

User passwords may expire if security hardening is installed on the Unified CVP Reporting Server. SNMP monitor displays alerts
                                                   when this happens.

Configuring NTP—Configuration for Time Synchronization of the Unified CVP servers is based on Microsoft Windows Time Services.
                                             For additional information on setting up Windows Time Service, refer to the Microsoft Windows Time Service Technical Reference
                                             documentation at http://technet.microsoft.com/en-us/library/cc773061(WS.10).aspx .

Enable Call Record Logging—To ensure that Call Record logging is enabled, do the following:

Unified CVP Reporting Server is not installed nor configured by default. Customers and Partners will have to install a Unified
                                                   CVP Reporting Server to use the Analyze Call Path tool with Unified CVP.

Unified CVP Database schema needs to be laid down by the Unified CVP_database_config.bat file. This file needs to be run by
                                                   the user after Unified CVP Reporting Server installation is completed.

Once a Unified CVP Reporting Server is installed, it needs to be configured through Unified CVP OAMP and a Unified CVP Call
                                                   Server needs to be associated with the Unified CVP Reporting Server.

Follow the Unified CVP CAG and RPT guidelines for configuring the Unified CVP Reporting Server, Unified CVP VXML Server, and
                                                   Unified CVP Call Servers.

Unified CVP data retention is 30 days, by default. You can customize this value through Unified CVP OAMP. Unless you back
                                                   up the database, data will be purged at the end of data retention day. Backed up Unified CVP data is not accessible unless
                                                   it is imported back into the database.

Unified CVP VXML Server filters need to be configured on Unified CVP OAMP. Refer to the Unified CVP OAMP guide for configuring
                                                   these filters.

Raw Call Record Details—For information relating to Raw Call Record details, refer to the Unified CVP Reporting Guide for version7.0(2) .

##### Cisco Access Control Server and Cisco IOS Gateway

The following information applies when configuring the Analyze Call Path for Cisco Access Control (ACS) Servers and Cisco
                                       IOS Gateways:

Version Support—Unified Analysis Manager supports ACS Release 5.1.

Call Record Repository—To assign a Call Record Repository, one of the acs servers can be configured as a "collector" node.

User Group and Access Permissions—To set user group and access permissions, after the ACS server is installed, in ssh/telnet
                                             access, enter acsadmin as the username and default as the password, You will be prompted to change the password.

Configuring NTP—To configure an NTP server on an ACS server, use cli: ntp server <NTP server IP/host> .

Enable Web View—Execute the CLI command acs config-web-interface view enable to enable web view. It is disabled by default.

Cisco IOS gateways as ACS network devices or AAA clients—You need to configure ACS network device to have the correct Radius
                                             secret, which is the same secret as the one on the IOS gateway.

From acsadmin, access Network Devices Group > Network Devices and AAA clients to add the Cisco IOS gateway as the ACS network device or AAA client.

For IOS configurations:

Use the CLI to configure NTP server: ntp server <NTP server IP/host>

Configure Cisco IOS gateway as a Radius client of the ACS server. Sample CLIs are below:

```
aaa new-model!
!
aaa group server radius acs
server 172.27.25.110 auth-port 1812 acct-port 1813
!
aaa authentication login h323 group acs
aaa authorization exec h323 group acs
aaa accounting connection h323 start-stop group acs
aaa session-id common
gw-accounting aaa
radius-server host 172.27.25.110 auth-port 1812 acct-port 1813
radius-server key cisco
radius-server vsa send accounting
radius-server vsa send authentication
```

Be sure you have local login access to your Cisco IOS gateways.

Enable Call Record Logging—To check that Call Records logging is enabled:

aaa accounting connection h323 start-stop group acs

aaa session-id common

gw-accounting aaa

radius-server host 172.27.25.110 auth-port 1812 acct-port 1813

radius-server key cisco

radius-server vsa send accounting

### Nodes

### Node Management

Once configured, a supported node is added to the Unified Analysis Manager database and will appear on the supported Unified
                                 Analysis Manager node list. You can identify a Unified Analysis Manager node in one of three ways:

Importing node and group configuration from a configuration file.

Manually entering node and group information with the Unified Analysis Manager screens.

Discovering Unified Analysis Manager nodes from a seed node. A seed node is one that can return information about all the
                                       nodes within a deployment. Once discovered, the nodes can then be added to the node inventory. This option saves you from
                                       manually entering details of these nodes.

For Unified Communications Manager, the first node (publisher) is the seed node. For Cisco Unified Customer Voice Portal (Unified
                                 CVP), the Cisco Unified CVP OAMP server is the seed node.

This option allows you to perform Add/Edit/Delete and Discover operations on nodes. All configured Unified Analysis Manager
                                 nodes (manually entered, imported from a file, or discovered) will be displayed in the list of nodes.

You can use the Nodes option to perform the following functions:

Add—The Add button allows you to manually enter a new node.

Edit—The Edit button allows you to edit a node that has already been configured.

Delete—The Delete button allows you to delete one or more nodes.

Discover—You can use the Discover option, which applies only to a seed node. Use the Discover button to send a query to the
                                       seed node, which then returns information about all the nodes within that deployment that the seed node is aware of. Once
                                       discovered, the nodes are automatically added to the node inventory.

Test Connectivity—The Test Connectivity button allows you to test connectivity to the node using the configured access information.

#### Display Node Summary

The Node summary screen displays all of the nodes currently configured with the Unified Analysis Manager application. Use
                                    the following procedure to access the Node summary screen.

Step 1

From the Unified Analysis Manager menu, select Inventory > Nodes .

Step 2

The Node summary screen displays with a list of configured nodes and buttons to Add , Edit , Delete , Discover . The Test Connection button allows you to test connectivity to a node. Nodes are listed by Name and Product Type .

#### Add or Edit a Node

The following procedure explains how to add a node or edit an existing configuration:

Step 1

From the Unified Analysis Manager menu, select Inventory > Nodes .

The Nodes window appears.

Step 2

Click the Add button to add a node or select a node from the list and click the Edit button to edit an existing configuration. The Add or Edit Node screen appears.

Fields on this screen that are marked with an asterisk (*) are required fields.

Step 3

Use the Product Type drop-down list box to select a product.

Step 4

In the IP/Host Name field, enter the hostname or the IP address of the node you are adding or editing.

Step 5

In the Transport Protocol field, select the protocol you want to use. Options for this field depend on the Product Type you selected.

Step 6

In the Port Number field, enter the port number on the node that you will be using.

Step 7

In the User Name and Password fields, enter the username and password that gives you access to the node. Reenter the password in the Confirm Password field.

Step 8

In the Description field, you can optionally provide a brief description of the node you are adding.

Step 9

In the Associated Call Record Repositories and Associated Trace File Repositories fields, use the drop down list to select the respective servers you want to use for the node.

Step 10

Use the Associated Group check boxes if you want to add the node to an existing group.

Step 11

If you have a NAT or Terminal Server configuration, use the Advanced button to display the Add Node-Advanced screen. Enter the appropriate information in the Alternate IP/Hostname and Alternate Port fields.

Step 12

Click the Save button to add the node. You can use the Cancel button to end the operation without adding the node.

### Group Management

Within Unified Analysis Manager, you can create groups and add nodes to these groups. Once the nodes are added to a group,
                                 the user can perform a set of functions (for example, Trace Collection and Trace Setting) at a group level. A single node
                                 can belong to multiple groups. Nested groups will not be supported. Copying a group will not be supported.

The AllNodes group is added by default when a node is added in Unified Analysis Manager. Any nodes added to Unified Analysis Manager are
                                             part of the AllNodes group by default. The AllNodes group cannot be edited or deleted.

The number of groups you can have is limited to 20 and the number of nodes in a group (with the exception of the AllNodes
                                             group) is 20.

You can use the Group option to perform the following functions:

Add—Use the Add button to create a group. Once a Group is created, you can add nodes to the group.

Edit—Use the Edit button to select and edit group information. The Edit function also allows you add or delete the node members
                                       of the group. You can change which nodes belong to a group by adding or deleting nodes from that group.

Delete—Use the Delete button to delete a Group. This function deletes that group from the Unified Analysis Manager. However,
                                       this function does not delete the individual nodes in the group from the Unified Analysis Manager. Nodes must be deleted individually
                                       using the Edit button.

#### Add or Edit Group

The following procedure explains how to add a group or edit an existing configuration:

Step 1

From the Unified Analysis Manager menu, select Inventory > Node Groups .

Step 2

The Groups window displays. Click the Add button to add a group or select a group from the list and click the Edit button to edit an existing configuration. The Add or Edit Group screen displays.

Step 3

Use the Group Name field to enter the name of the group.

Step 4

Use the Group Description field to enter a brief description of the group.

Step 5

The Select Nodes section contains a list of each configured node. To add a node to the group, highlight the node in the list and click the Add button.

Step 6

When you have finished selecting nodes for the group, click the Add button to add the group or the Update button if you are editing the group content. You can use the Cancel button to end the operation without adding or editing the group.

### Trace File Repository Management

This option allows you to perform Add/Edit/Delete operations on trace file repositories for the Unified Analysis Manager.
                                 Managed nodes typically use the trace file repository to off load its trace and log files. The Unified Analysis Manager can
                                 then connect to the trace file repository to collect logs and traces.

You can use the Trace File Repository option to perform the following functions:

Add—The Add button allows you to manually enter a new server.

Edit —The Edit button allows you to edit a server that has already been configured.

Delete—The Delete button allows you to delete one or more servers.

Test Connectivity—The Test Connectivity button allows you to test connectivity to a server using the configured access information.

#### Add or Edit Trace File Repository

The following procedure explains how to add a Trace File Repository or edit an existing configuration:

Step 1

From the Unified Analysis Manager menu, select Inventory > Trace File Repositories .

Step 2

The Trace File Repositories window displays with a list of configured servers. Click the Add button to add a new server or highlight a server on the list and click the Edit button to edit an existing configuration.

Step 3

In the IP/Host Name field, enter the hostname or the IP address of the server you are adding.

Step 4

In the Transport Protocol field, use the drop-down list to select the protocol you want to use, either SFTP or FTP.

Important

Step 5

In the Port Number field, enter the port number on the server that you will be using.

Step 6

In the User Name and Password fields, enter the username and password that gives you access to the server. Reenter the password in the Confirm Password field.

Step 7

In the Description field, you can optionally provide a brief description of the server you are adding.

Step 8

In the Associated Nodes field, use the check boxes to select the nodes that will have access to the server.

Step 9

If you have a NAT or Terminal Server configuration, use the Advanced button to display the Add Trace File Repository-Advanced screen. Enter the appropriate information in the Alternate IP/Hostname and Alternate Port fields.

Step 10

Click the Add button to add the server or Edit to update the configuration. You can use the Cancel button to end the operation without adding the server.

### Call Record Repository Management

This option allows you to perform Add/Edit/Delete operations on call record repositories for the Unified Analysis Manager.
                                 Managed nodes typically see the Call Record Repository to store the call data in a database. The Unified Analysis Manager
                                 can then connect to the Call Record Repository to obtain detailed call data.

You can use the Call Record Repository option to perform the following functions:

Add: Allows you to manually enter a new server.

Edit: Allows you to edit a server that has already been configured.

Delete: Allows you to delete one or more servers.

Test Connectivity: Allows you to test connectivity to a server using the configured access information.

#### Add or Edit Call Record Repository

Follow this procedure to add a call record repository or edit an existing configuration:

Step 1

From the Unified Analysis Manager menu, select Inventory > Call Record Repositories .

Step 2

The Call Record Repositories window appears with a list of configured servers. Click the Add button to add a new server or highlight a server on the list and click the Edit button to edit an existing configuration.

Step 3

Use the Repository Type drop down list to select the product type for the node that will be accessing the server.

Step 4

In the Hostname field, enter the name of the server you are adding.

Step 5

In the JDBC Port field, enter the port number on the server that you will be using.

Step 6

In the JDBC User Name and JDBC Password fields, enter the username and password that gives you access to the server. Re-enter the password in the Confirm Password field.

Step 7

In the Description field, you can optionally provide a brief description of the node you are adding.

Step 8

Use the Nodes Available for Association to select the nodes that will have access to the server.

Step 9

If you have a NAT or Terminal Server configuration, use the Advanced button to display the Add Call Record Repository-Advanced screen. Enter the appropriate information in the Alternate Hostname and Alternate Port fields.

Step 10

Click the Add button to add the server or Edit to update the configuration. You can use the Cancel button to end the operation without adding the server.

### Define Trace Templates

If you have large number of nodes in a group, the Unified Analysis Manager provides templates as a shortcut for selecting
                                 components to change trace levels. You can also use templates to establish the new trace levels for nodes. You can also use
                                 template for collecting logs and trace files.

You can use the Templates option to perform the following functions:

Add—The Add button allows you to create a new template. When adding a template you should note that you are doing so for node
                                       types and not actual nodes. For a given node type, there is a known fixed set of components and services.

Edit—The Edit button allows you to edit an existing template.

Clone—The Clone button allows you to save an existing template as a new template without replacing the original one.

Delete—The Delete button allows you to delete a template.

Import—Use the Import button to import predefined templates from a flat file.

Export—Use the Export button to export a template to a flat file.

#### Add or Edit Template

The following procedure explains how to add a template or edit an existing configuration:

Unified Analysis Manager has default templates which cannot be edited or deleted.

Step 1

From the Unified Analysis Manager menu, select Inventory > Templates .

Step 2

The Templates window displays. Click the Add button to add a template or select a template from the list and click the Edit button to edit an existing configuration. The Add or Edit Template screen displays.

Step 3

Use the Name field to enter the name of the template.

Step 4

Use the Description field to enter a brief description of the group.

Step 5

The Product Types section contains a list of products supported by the Unified Analysis Manager. When you select a product from this list,
                                             the associated components display in the Component Name field.

Step 6

For each component displayed, you can apply a trace level by using the drop down list in the Trace Level field.

Not all components are available for setting trace levels with this screen.

Step 7

You can indicate if you want to collect trace logs for the component by checking the box in the Collect field.

Step 8

Click the Add button to add the template or Edit to update the configuration. You can use the Cancel button to end the operation without adding the server.

### Call
                           	 Definitions

The following
                                 		  table defines the types of call termination.

Call Type

Call Termination Explanation

Failed call

The call is not connected for any reason other than user hang-up
                                             					 before the connection is completed.

Abandoned call

The call is not connected because the user hangs up after
                                             					 initiating the call.

Dropped call

The call is disconnected after connection for any reason other
                                             					 than user hanging up.

The following
                                 		  table lists the products that support the failed, abandoned, and dropped calls.

Call Type

Unified Communications
                                             					 Manager

Unified CCE

Unified CVP

Unified CCX

Failed Call

Supported

Supported

Supported

Supported

Abandoned call

Supported

Supported

Not Supported

Supported

Dropped Called

Supported

Supported

Not Supported

Supported

### Trace Collection

Unified Analysis Manager allows you to collect log and trace files from services of supported devices. There are three ways
                                 you can collect logs and trace files:

Collect Traces Now— Collect Traces Now option allows you to collect trace files based on a selection of services on a device
                                       or group of devices for any period of time that has occurred in the past.

Schedule Trace Collection— Schedule Trace Collection option allows you to collect trace files based on a selection of services
                                       on a device or group of devices for any period of time in the future.

Schedule Trace Settings and Collections—Schedule Trace Settings and Collection option allows you to collect trace files from
                                       the present into the future and also specify the trace levels to be used during the scheduled time.

#### Collect Traces Now

The Collect Traces Now option allows you to collect trace files based on a selection of services on a device or group of devices
                                    for any period of time that has occurred in the past.

Step 1

From the Unified Analysis Manager menu, select Tools > Collect Traces Now .

The Collect Traces Now window displays.

Step 2

Select either the Group to display a list of supported groups or the Node for a list of supported devices. Select the groups
                                             or devices that you want to collect traces for.

Step 3

Use the Select the template to dropdown list to select the template containing the trace levels you want to use. Alternately, you can click the Customize button if you want to customize new trace levels for the group or device.

Step 4

Use the Start Time and End Time fields to select the collection time period.

Step 5

Use the Referenced Time Zone field to select the time zone for the collection time period.

Step 6

You can optionally click the View Summary button to view the Collection Summary window. This window contain a list of the components associated with the node.

Step 7

Click the OK button to start the trace. When the trace is completed, the window displays a Status Summary and Status Details for the trace.
                                             The Status Details provide the path to the directory to which the log was sent.

#### Schedule Trace Collection

Use the Schedule Trace Collection option if you want to collect trace files for any period of time from the present into the
                                    future.

Step 1

From the Unified Analysis Manager menu, select Tools > Schedule Trace Collection .

The Schedule Trace Collection window appears.

Step 2

Select either the Group to display a list of supported groups or the Node for a list of supported devices. Select the groups
                                             or devices that you want to collect traces for.

Step 3

Use the Select the template to dropdown list to select the template containing the trace levels you want to use. Alternately, you can click the Customize button if you want to collect traces for specific components.

Step 4

Use the Start Time and End Time fields to select the collection time period.

Step 5

Use the Referenced Time Zone field to select the time zone for the collection time period.

Step 6

Use the Collect Traces Every dropdown field to indicate the frequency of the collection.

Step 7

Optionally, you can choose to have an email notification sent regarding the trace collection. To do that, click the Send Email Notification to check box and enter the email address in the text box.

Step 8

You can optionally click the View Summary button to view the Collection Summary window. This window contains a list of the components associated with the node.

Step 9

Click the OK button to start the trace. When the trace is scheduled, the window displays a Status Summary and Status Details for the trace.
                                             When the trace is completed, a report is written to your log file and, if email information was provided, a system-generated
                                             email is sent.

#### Schedule Trace Settings and Collection

Use the Schedule Trace Settings and Collection option if you want to collect trace files for any period of time from the present
                                    into the future and, in addition, also specify the trace levels to be used during the scheduled time. If you change trace
                                    settings with this option, trace levels are restored to their default settings after the collection period is over.

Step 1

From the Unified Analysis Manager menu, select Tools > Schedule Trace Collection .

The Schedule Trace Collection window appears.

Step 2

Select either the Group to display a list of supported groups or Node, for a list of supported devices. Select the groups
                                             or devices that you want to collect traces for.

Step 3

Use the Select the template to drop-down list to select the template containing the trace levels you want to use. Alternately, you can click the Customize button if you want to customize new trace levels for the group or device. This option also allows you to collect traces for
                                             specific components.

Step 4

Use the Start Time and End Time fields to select the collection time period.

Step 5

Use the Referenced Time Zone field to select the time zone for the collection time period.

Step 6

Use the Collect Traces Every drop-down field to indicate the frequency of the collection.

Step 7

Optionally, you can choose to have an email notification sent regarding the trace collection. To do that, click the Send Email Notification to check box and enter the email address in the text box.

Step 8

You can optionally click the View Summary button to view the Collection Summary window. This window contains a list of the components associated with the node.

Step 9

Click the OK button to start the trace. When the trace is scheduled, the window displays a Status Summary and Status Details for the trace.
                                             When the trace is completed, a report is written to your log file and, if email information was provided, a system-generated
                                             email is sent.

### Set Trace Levels

Use the Set Trace Level option to assign trace levels for a group of devices or individual devices. You can assign trace levels
                                 using a template or you can customize trace levels. Trace levels can be set for the following Cisco Unified Communications
                                 components:

- Unified Communications Manager: Allows setting trace levels for Unified Communications Manager and Common Trace Components.

- IM and Presence : Allows setting trace levels for Unified Presence and Common Trace Components.

- Cisco Unity Connection : Allows setting trace level for Cisco Unity Connection and Common Trace Components.

- Cisco Unified Contact Center Express: Allows setting trace level only for Common Trace Components.

The following table describes the general trace level settings for the Cisco Unified Communications components that are managed
                                 by Unified Analysis Manager.

Trace Level

Guidelines

Expected Volume of Traces

Default

This level should include all traces generated in abnormal paths. This level is intended for coding error traces and error
                                             s traces that normally should not occur.

Choose Detailed as Default trace level.

Minimum Traces expected

Warning

This level should include traces for system-level operations. This should include all traces generated by "State Transitions" within components.

Medium Volume of Traces Expected when component is used

Informational

This should include traces that can be used in the lab for debugging difficult problems of the component.

High Volume of Traces Expected when component is used

Debug

This level should include detailed debug information or high volume of messages which are primarily used for debugging.

Very High Volume of Traces Expected when component is used

Step 1

From the Unified Analysis Manager menu, select Tools > Set Trace Level .

The Set Trace Level window appears.

Step 2

Select either the Group to display a list of supported groups or the Node for a list of supported devices. Select the groups
                                          or devices that you want to collect traces for.

Step 3

From the Select the template drop-down list box, select the template containing the trace levels that you you want to use. Alternately, you can click
                                          the Customize button if you want to customize trace levels for the group or device. If you choose the Customize option, the Design Preview dialog displays with a list of supported devices. Choose the device you want and use the Selected Components fields to set the trace levels.

Step 4

Click View Changes to see any changes made to traces levels for the node. Click OK to set the level and exit the screen.

### View Configuration

Use the View Configuration option to view configuration information related to a node. You can collect the version and configuration
                                 information and view it in a browser or save the results.

Step 1

From the Unified Analysis Manager menu, select Tools > View Configuration .

The View Configuration window appears and displays a list of nodes.

Step 2

Select a node and click the Next button to display the Selected Components screen. This screen lists the Version, Platform, License and other category configuration information for the product.

Step 3

Click Finish to collect the configuration information.

The summary window appears. Users can view the collected information in a browser or save the collected configuration information
                                             using the Save As button.

## Cisco Unified Analysis Manager Troubleshooting

The following table provides a list of errors that you may see when testing Unified Analysis Manager connectivity to a node
                              and the suggested action for correcting the errors.

No.

Error Code

Message

Corrective Action

1

NOT_AUTHORIZED_CODE

Username or password is not correct

Enter the correct username and password.

2

MISSING_SERVICE_CODE

Missing Service

The requested web service was not found. Check to see if the web service is down on the target application.

3

SERVER_BUSY_CODE

Server is busy

Check to see if there are any other ongoing jobs running on the server. If so, wait until the job is done. If not, wait a
                                          few minutes and try again.

4

INVALID_PORT_CODE

Invalid Port

The specified port may be syntactically incorrect or may be out of range.

5

CONNECTION_FAILED_CODE

Not connected to the specified node

Verify that you have entered the correct address for this node. If the address is correct, then verify that the node is up
                                          and that it is reachable.

6

NOT_SUPPORTED_CODE

Not supported

This version of the specified product is not supported for this release. Upgrade this product to a supported version.

7

CERTIFICATE_HANDLING_ERROR_CODE

SSL handshake failed. The client and server could not negotiate desired level of security

Verify that you have accepted the certificate that was sent to the client from the server.

8

GENERAL_CONNECTION_ERROR_CODE

An internal error has occurred

Save the recent Unified Analysis Manager log files and contact Unified Analysis Manager support for help.

| Note | On both servers, files should be uploaded to the /incoming directory. |
|---|---|

| Step 1 | From the Unified Analysis Manager drop-down menu, select AnalysisManager > Preferences . The Preferences window displays. Click FTP Server . |
|---|---|
| Step 2 | The FTP Servers screen displays with a list of configured servers and buttons to Add , Edit , or Delete a server. The Test Connection button allows you to test connectivity to a server. |
| Step 3 | Use the buttons to select the option you want. |

| Step 1 | From the Unified Analysis Manager drop-down menu, select AnalysisManager > Preferences . The Preferences window appears. Click FTP Server . |
|---|---|
| Step 2 | The FTP Servers screen displays with a list of configured servers and buttons to Add , Edit , or Delete a server. The Test Connection button allows you to test connectivity to a server. |
| Step 3 | Click the Add button to add a server or the Edit button to edit an existing configuration. The Add FTP Server screen appears. |
| Step 4 | In the Name/IP Address field, enter the name or the IP address of the FTP server you are adding. |
| Step 5 | In the Protocol field, select either the FTP or SFTP protocol, depending on the type of server you are connecting to. Use SFTP if you are
                                             connecting to a Cisco TAC server. |
| Step 6 | In the User Name and Password fields, enter the username and password that gives you access to the server. |
| Step 7 | In the Port field, enter the port number on the server that you will be using. |
| Step 8 | In the Destination Directory field, enter the path for the directory to which you will be exporting files. If you are adding a Cisco TAC server, use the /incoming directory. |
| Step 9 | Click the OK button to add the server. You can use the Cancel button to end the operation without adding the FTP server. |

| Note | You can configure a maximum of two mail servers. You can only use mail servers configured with this option for Unified Analysis Manager notifications. For RTMT notifications,
                                                   you must configure a separate mail server. |
|---|---|

| Step 1 | From the Unified Analysis Manager drop-down menu, select AnalysisManager > Preferences . The Preferences window displays. Click Mail Server . |
|---|---|
| Step 2 | The Mail Servers screen appears with a list of configured servers and buttons to Add , Edit , or Delete a server. The Test  Connectivity button allows you to test connectivity to a server. The Refresh button allows you to reload the server. |
| Step 3 | Click the Add button to add a server or the Edit button to edit an existing configuration. On clicking the Add button, the Add Mail Server screen appears. |
| Step 4 | In the Name/IP Address field, enter the name or the IP address of the Mail server you are adding. |
| Step 5 | In the Port No. field, enter the port number on the server that you will be using. |
| Step 6 | Click Save button to save the settings or the Cancel button to end the operation without adding the Mail server. The Test Connection button allows you to test connectivity to a server. |

| Step 1 | From the Unified Analysis Manager drop-down menu, select AnalysisManager > Preferences . The Preferences window appears. Click Trace Collection . |
|---|---|
| Step 2 | The Trace Collection screen appears. Enter the directory you want to use for traces logs in the Download Directory box, or use the Browse button to locate the directory. Optionally, you can click the Default button to select the default dirctory. |
| Step 3 | Click Save . |

| Step 1 | From the Unified Analysis Manager menu, select Administration > Import . |
|---|---|
| Step 2 | Select the .csv configuration file that you want to import. |
| Step 3 | Click the Import button. The selected file appears. |

| Step 1 | From the Unified Analysis Manager menu, select Administration > Upload Files . The Upload Files screen appears. |
|---|---|
| Step 2 | In the Case ID field, enter the number that Cisco TAC has assigned to the case. |
| Step 3 | Use the drop-down list box in the Send to Server field to select the FTP server you are sending the file to. |
| Step 4 | Use the Notes box to provide any additional information about the file. |
| Step 5 | Use the Send Email Notifications check box if you want to add the email addresses to send a notification that the file is uploaded. To add multiple email
                                          addresses, add the mail ids separated by comma. The mail addresses can be only the < username > or it can be of the format username@domain.com . |
| Step 6 | In the bottom section of the screen, in the Files to upload box, select the files you want to transfer. Use the Add or Remove buttons to select or deselect files from the system. The files selected will be zipped by default and then uploaded. The
                                          name of the zipped file will be of the format <case id>_uploadedfile.zip . |
| Step 7 | Click the OK button to transfer the file. |

| Note | All nodes that you define are assigned to the AllNodes group by default. Use the Node Groups function if you want to assign
                                             the node to a different group. See the topics related to the Analyze Call Path setup for more information on configuring a
                                             Call Record Repository before using the Analyze Call Path function. |
|---|---|

| Step 1 | From the Unified Analysis Manager menu, select Tools > Analyze Call Path . The Analyze Call Path Information window appears. |
|---|---|
| Step 2 | Click the Continue button. The Search Criteria window appears. |
| Step 3 | Enter the number where the call originated in the Calling Number field. The default is an asterisk (*) which is a wildcard that will trace all numbers for the node. |
| Step 4 | Enter the number where the call terminated in the Called Number field. The default is an asterisk (*) which is a wildcard that will trace all numbers for the node. |
| Step 5 | Use the Termination Cause drop-down list box to select the reason for the call termination; either Abandoned, Dropped, Failed or all three. |
| Step 6 | Use the Start Time field to enter the start time for the trace. |
| Step 7 | Use the Duration field to indicate the length of the time period you want to trace. |
| Step 8 | Use the Time Zone drop-down list box to select the time zone where you are tracing calls. |
| Step 9 | Use the Filter Nodes by Group drop-down list box to select the group of nodes that you want to trace. |
| Step 10 | Use the and Node Type drop-down list box to select specific types of nodes that you want to trace. When you have selected the Group and Node, information displays for each node. You can then use the check box for each node
                                             listed to select or deselect the node. Note The limit for the number of nodes that you can select at a time is 20. | Note | The limit for the number of nodes that you can select at a time is 20. |
| Note | The limit for the number of nodes that you can select at a time is 20. |
| Step 11 | Click the Run button to begin the trace. The trace results display on the bottom of the window. If you selected multiple nodes, a tab is
                                          displayed for each node. Click the tab to display information for that node. |
| Step 12 | When the call record information appears, you can click the View Full Path button to see the complete call path. You can click the View Record Details button to see the information about the call. Use the Save Results button to save the reports. |

| Note | The limit for the number of nodes that you can select at a time is 20. |
|---|---|

| Caution | The Analyze Call Path Tool might not work correctly if your computer is set to a language other than English. |
|---|---|

| Note | New resources "SOAP Diagnostic Portal Database Service" and "SOAP Call Record APIs" added on an upgrade should not
                                                               						have the read and update permissions by default due to security reasons for
                                                               						existing users. Users need to create or copy the role to custom resources and
                                                               						update the required permissions for above mentioned resources as needed. See
                                                               						the Administration Guide
                                                                     							 for Cisco Unified Communications Manager for additional details. |
|---|---|

| Note | You can
                                                         				  verify that flags are set as desired at https://<HOSTNAME:PORT>/ccmadmin/vendorConfigHelp.do |
|---|---|

| Note | If you are using RTMT to monitor Cisco Unified Contact Center Enterprise, you must open the following file and change the
                                                   value for ReadTimeout to 360: <RTMT_INSTALLATION_FOLDER_PATH>/conf/rtmt.xml . If you don't change the value, RTMT will not be able to collect OPC logs because RTMT's default timeout value is greater
                                                   than the time it takes to collect OPC logs. |
|---|---|

| Step 1 | From the Unified Analysis Manager menu, select Inventory > Nodes . |
|---|---|
| Step 2 | The Node summary screen displays with a list of configured nodes and buttons to Add , Edit , Delete , Discover . The Test Connection button allows you to test connectivity to a node. Nodes are listed by Name and Product Type . |

| Step 1 | From the Unified Analysis Manager menu, select Inventory > Nodes . The Nodes window appears. |
|---|---|
| Step 2 | Click the Add button to add a node or select a node from the list and click the Edit button to edit an existing configuration. The Add or Edit Node screen appears. Note Fields on this screen that are marked with an asterisk (*) are required fields. | Note | Fields on this screen that are marked with an asterisk (*) are required fields. |
| Note | Fields on this screen that are marked with an asterisk (*) are required fields. |
| Step 3 | Use the Product Type drop-down list box to select a product. |
| Step 4 | In the IP/Host Name field, enter the hostname or the IP address of the node you are adding or editing. |
| Step 5 | In the Transport Protocol field, select the protocol you want to use. Options for this field depend on the Product Type you selected. |
| Step 6 | In the Port Number field, enter the port number on the node that you will be using. |
| Step 7 | In the User Name and Password fields, enter the username and password that gives you access to the node. Reenter the password in the Confirm Password field. |
| Step 8 | In the Description field, you can optionally provide a brief description of the node you are adding. |
| Step 9 | In the Associated Call Record Repositories and Associated Trace File Repositories fields, use the drop down list to select the respective servers you want to use for the node. |
| Step 10 | Use the Associated Group check boxes if you want to add the node to an existing group. |
| Step 11 | If you have a NAT or Terminal Server configuration, use the Advanced button to display the Add Node-Advanced screen. Enter the appropriate information in the Alternate IP/Hostname and Alternate Port fields. |
| Step 12 | Click the Save button to add the node. You can use the Cancel button to end the operation without adding the node. |

| Note | Fields on this screen that are marked with an asterisk (*) are required fields. |
|---|---|

| Note | The AllNodes group is added by default when a node is added in Unified Analysis Manager. Any nodes added to Unified Analysis Manager are
                                             part of the AllNodes group by default. The AllNodes group cannot be edited or deleted. |
|---|---|

| Note | The number of groups you can have is limited to 20 and the number of nodes in a group (with the exception of the AllNodes
                                             group) is 20. |
|---|---|

| Step 1 | From the Unified Analysis Manager menu, select Inventory > Node Groups . |
|---|---|
| Step 2 | The Groups window displays. Click the Add button to add a group or select a group from the list and click the Edit button to edit an existing configuration. The Add or Edit Group screen displays. |
| Step 3 | Use the Group Name field to enter the name of the group. |
| Step 4 | Use the Group Description field to enter a brief description of the group. |
| Step 5 | The Select Nodes section contains a list of each configured node. To add a node to the group, highlight the node in the list and click the Add button. |
| Step 6 | When you have finished selecting nodes for the group, click the Add button to add the group or the Update button if you are editing the group content. You can use the Cancel button to end the operation without adding or editing the group. |

| Step 1 | From the Unified Analysis Manager menu, select Inventory > Trace File Repositories . |
|---|---|
| Step 2 | The Trace File Repositories window displays with a list of configured servers. Click the Add button to add a new server or highlight a server on the list and click the Edit button to edit an existing configuration. |
| Step 3 | In the IP/Host Name field, enter the hostname or the IP address of the server you are adding. |
| Step 4 | In the Transport Protocol field, use the drop-down list to select the protocol you want to use, either SFTP or FTP. Important From Release 14SU3 onwards, FTP server is no longer supported. We recommend that you use SFTP server for scheduled trace collections. | Important | From Release 14SU3 onwards, FTP server is no longer supported. We recommend that you use SFTP server for scheduled trace collections. |
| Important | From Release 14SU3 onwards, FTP server is no longer supported. We recommend that you use SFTP server for scheduled trace collections. |
| Step 5 | In the Port Number field, enter the port number on the server that you will be using. |
| Step 6 | In the User Name and Password fields, enter the username and password that gives you access to the server. Reenter the password in the Confirm Password field. |
| Step 7 | In the Description field, you can optionally provide a brief description of the server you are adding. |
| Step 8 | In the Associated Nodes field, use the check boxes to select the nodes that will have access to the server. |
| Step 9 | If you have a NAT or Terminal Server configuration, use the Advanced button to display the Add Trace File Repository-Advanced screen. Enter the appropriate information in the Alternate IP/Hostname and Alternate Port fields. |
| Step 10 | Click the Add button to add the server or Edit to update the configuration. You can use the Cancel button to end the operation without adding the server. |

| Important | From Release 14SU3 onwards, FTP server is no longer supported. We recommend that you use SFTP server for scheduled trace collections. |
|---|---|

| Step 1 | From the Unified Analysis Manager menu, select Inventory > Call Record Repositories . |
|---|---|
| Step 2 | The Call Record Repositories window appears with a list of configured servers. Click the Add button to add a new server or highlight a server on the list and click the Edit button to edit an existing configuration. |
| Step 3 | Use the Repository Type drop down list to select the product type for the node that will be accessing the server. |
| Step 4 | In the Hostname field, enter the name of the server you are adding. |
| Step 5 | In the JDBC Port field, enter the port number on the server that you will be using. |
| Step 6 | In the JDBC User Name and JDBC Password fields, enter the username and password that gives you access to the server. Re-enter the password in the Confirm Password field. |
| Step 7 | In the Description field, you can optionally provide a brief description of the node you are adding. |
| Step 8 | Use the Nodes Available for Association to select the nodes that will have access to the server. |
| Step 9 | If you have a NAT or Terminal Server configuration, use the Advanced button to display the Add Call Record Repository-Advanced screen. Enter the appropriate information in the Alternate Hostname and Alternate Port fields. |
| Step 10 | Click the Add button to add the server or Edit to update the configuration. You can use the Cancel button to end the operation without adding the server. |

| Note | Unified Analysis Manager has default templates which cannot be edited or deleted. |
|---|---|

| Step 1 | From the Unified Analysis Manager menu, select Inventory > Templates . |
|---|---|
| Step 2 | The Templates window displays. Click the Add button to add a template or select a template from the list and click the Edit button to edit an existing configuration. The Add or Edit Template screen displays. |
| Step 3 | Use the Name field to enter the name of the template. |
| Step 4 | Use the Description field to enter a brief description of the group. |
| Step 5 | The Product Types section contains a list of products supported by the Unified Analysis Manager. When you select a product from this list,
                                             the associated components display in the Component Name field. |
| Step 6 | For each component displayed, you can apply a trace level by using the drop down list in the Trace Level field. Note Not all components are available for setting trace levels with this screen. | Note | Not all components are available for setting trace levels with this screen. |
| Note | Not all components are available for setting trace levels with this screen. |
| Step 7 | You can indicate if you want to collect trace logs for the component by checking the box in the Collect field. |
| Step 8 | Click the Add button to add the template or Edit to update the configuration. You can use the Cancel button to end the operation without adding the server. |

| Note | Not all components are available for setting trace levels with this screen. |
|---|---|

| Call Type | Call Termination Explanation |
|---|---|
| Failed call | The call is not connected for any reason other than user hang-up
                                             					 before the connection is completed. |
| Abandoned call | The call is not connected because the user hangs up after
                                             					 initiating the call. |
| Dropped call | The call is disconnected after connection for any reason other
                                             					 than user hanging up. |

| Call Type | Unified Communications
                                             					 Manager | Unified CCE | Unified CVP | Unified CCX |
|---|---|---|---|---|
| Failed Call | Supported | Supported | Supported | Supported |
| Abandoned call | Supported | Supported | Not Supported | Supported |
| Dropped Called | Supported | Supported | Not Supported | Supported |

| Step 1 | From the Unified Analysis Manager menu, select Tools > Collect Traces Now . The Collect Traces Now window displays. |
|---|---|
| Step 2 | Select either the Group to display a list of supported groups or the Node for a list of supported devices. Select the groups
                                             or devices that you want to collect traces for. |
| Step 3 | Use the Select the template to dropdown list to select the template containing the trace levels you want to use. Alternately, you can click the Customize button if you want to customize new trace levels for the group or device. |
| Step 4 | Use the Start Time and End Time fields to select the collection time period. |
| Step 5 | Use the Referenced Time Zone field to select the time zone for the collection time period. |
| Step 6 | You can optionally click the View Summary button to view the Collection Summary window. This window contain a list of the components associated with the node. |
| Step 7 | Click the OK button to start the trace. When the trace is completed, the window displays a Status Summary and Status Details for the trace.
                                             The Status Details provide the path to the directory to which the log was sent. |

| Step 1 | From the Unified Analysis Manager menu, select Tools > Schedule Trace Collection . The Schedule Trace Collection window appears. |
|---|---|
| Step 2 | Select either the Group to display a list of supported groups or the Node for a list of supported devices. Select the groups
                                             or devices that you want to collect traces for. |
| Step 3 | Use the Select the template to dropdown list to select the template containing the trace levels you want to use. Alternately, you can click the Customize button if you want to collect traces for specific components. |
| Step 4 | Use the Start Time and End Time fields to select the collection time period. |
| Step 5 | Use the Referenced Time Zone field to select the time zone for the collection time period. |
| Step 6 | Use the Collect Traces Every dropdown field to indicate the frequency of the collection. |
| Step 7 | Optionally, you can choose to have an email notification sent regarding the trace collection. To do that, click the Send Email Notification to check box and enter the email address in the text box. |
| Step 8 | You can optionally click the View Summary button to view the Collection Summary window. This window contains a list of the components associated with the node. |
| Step 9 | Click the OK button to start the trace. When the trace is scheduled, the window displays a Status Summary and Status Details for the trace.
                                             When the trace is completed, a report is written to your log file and, if email information was provided, a system-generated
                                             email is sent. |

| Step 1 | From the Unified Analysis Manager menu, select Tools > Schedule Trace Collection . The Schedule Trace Collection window appears. |
|---|---|
| Step 2 | Select either the Group to display a list of supported groups or Node, for a list of supported devices. Select the groups
                                             or devices that you want to collect traces for. |
| Step 3 | Use the Select the template to drop-down list to select the template containing the trace levels you want to use. Alternately, you can click the Customize button if you want to customize new trace levels for the group or device. This option also allows you to collect traces for
                                             specific components. |
| Step 4 | Use the Start Time and End Time fields to select the collection time period. |
| Step 5 | Use the Referenced Time Zone field to select the time zone for the collection time period. |
| Step 6 | Use the Collect Traces Every drop-down field to indicate the frequency of the collection. |
| Step 7 | Optionally, you can choose to have an email notification sent regarding the trace collection. To do that, click the Send Email Notification to check box and enter the email address in the text box. |
| Step 8 | You can optionally click the View Summary button to view the Collection Summary window. This window contains a list of the components associated with the node. |
| Step 9 | Click the OK button to start the trace. When the trace is scheduled, the window displays a Status Summary and Status Details for the trace.
                                             When the trace is completed, a report is written to your log file and, if email information was provided, a system-generated
                                             email is sent. |

| Trace Level | Guidelines | Expected Volume of Traces |
|---|---|---|
| Default | This level should include all traces generated in abnormal paths. This level is intended for coding error traces and error
                                             s traces that normally should not occur. Note Choose Detailed as Default trace level. | Note | Choose Detailed as Default trace level. | Minimum Traces expected |
| Note | Choose Detailed as Default trace level. |
| Warning | This level should include traces for system-level operations. This should include all traces generated by "State Transitions" within components. | Medium Volume of Traces Expected when component is used |
| Informational | This should include traces that can be used in the lab for debugging difficult problems of the component. | High Volume of Traces Expected when component is used |
| Debug | This level should include detailed debug information or high volume of messages which are primarily used for debugging. | Very High Volume of Traces Expected when component is used |

| Note | Choose Detailed as Default trace level. |
|---|---|

| Step 1 | From the Unified Analysis Manager menu, select Tools > Set Trace Level . The Set Trace Level window appears. |
|---|---|
| Step 2 | Select either the Group to display a list of supported groups or the Node for a list of supported devices. Select the groups
                                          or devices that you want to collect traces for. |
| Step 3 | From the Select the template drop-down list box, select the template containing the trace levels that you you want to use. Alternately, you can click
                                          the Customize button if you want to customize trace levels for the group or device. If you choose the Customize option, the Design Preview dialog displays with a list of supported devices. Choose the device you want and use the Selected Components fields to set the trace levels. |
| Step 4 | Click View Changes to see any changes made to traces levels for the node. Click OK to set the level and exit the screen. |

| Step 1 | From the Unified Analysis Manager menu, select Tools > View Configuration . The View Configuration window appears and displays a list of nodes. |
|---|---|
| Step 2 | Select a node and click the Next button to display the Selected Components screen. This screen lists the Version, Platform, License and other category configuration information for the product. |
| Step 3 | Click Finish to collect the configuration information. The summary window appears. Users can view the collected information in a browser or save the collected configuration information
                                             using the Save As button. |

| No. | Error Code | Message | Corrective Action |
|---|---|---|---|
| 1 | NOT_AUTHORIZED_CODE | Username or password is not correct | Enter the correct username and password. |
| 2 | MISSING_SERVICE_CODE | Missing Service | The requested web service was not found. Check to see if the web service is down on the target application. |
| 3 | SERVER_BUSY_CODE | Server is busy | Check to see if there are any other ongoing jobs running on the server. If so, wait until the job is done. If not, wait a
                                          few minutes and try again. |
| 4 | INVALID_PORT_CODE | Invalid Port | The specified port may be syntactically incorrect or may be out of range. |
| 5 | CONNECTION_FAILED_CODE | Not connected to the specified node | Verify that you have entered the correct address for this node. If the address is correct, then verify that the node is up
                                          and that it is reachable. |
| 6 | NOT_SUPPORTED_CODE | Not supported | This version of the specified product is not supported for this release. Upgrade this product to a supported version. |
| 7 | CERTIFICATE_HANDLING_ERROR_CODE | SSL handshake failed. The client and server could not negotiate desired level of security | Verify that you have accepted the certificate that was sent to the client from the server. |
| 8 | GENERAL_CONNECTION_ERROR_CODE | An internal error has occurred | Save the recent Unified Analysis Manager log files and contact Unified Analysis Manager support for help. |