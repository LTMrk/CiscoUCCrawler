---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-4a398fb400
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1252-reporting-server-configuration.html
retrieved_at: 2026-08-21T06:52:36.877136+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

Chapter: Reporting Server Configuration

## Chapter: Reporting Server Configuration

# Reporting Server Configuration

## Configure
                        	 Reporting Server

### Before you begin

Configure a
                                    				Call Server to associate with a Reporting Server. To configure a Call Server,
                                    				see Configure Call Server .

You can
                                                				  associate a Call Server with only one Reporting Server.

Collect the
                                    				following information about the Reporting Server and Reporting Database during
                                    				the installation of Unified CVP software:

Hostname
                                          					 of the Call Servers that are associated with the Reporting Server.

Hostname
                                          					 and IP address of the server on which the Reporting Database resides.

Password
                                          					 for the Reporting Database user.

Step 1

On the Unified
                                       			 CVP Operations Console, select Device
                                             				  Management > Unified CVP Reporting Server .

Step 2

Click Add
                                          				New to add a new Reporting Server or click Use As
                                          				Template to use an existing template to configure the new Reporting
                                       			 Server.

Step 3

Click the
                                       			 following tabs and configure the settings based on your call flow model:

General tab.
                                             				  For more information, see General Settings .

Reporting
                                                					 Properties tab. For more information, see Reporting Properties Settings .

Device Pool tab. For more information about adding, deleting, and editing device pool, see Add or Remove Device From Device Pool .

Infrastructure tab. For more information, see Infrastructure Settings .

Step 4

Click Save
                                          				and Deploy to deploy the changes to the Reporting Server page.
                                       			 Click Save to save the settings in the Operations Server
                                       			 database and configure the Reporting Server later.

## Reporting Server Settings

### General
                           	 Settings

Configure settings that identify the Reporting Server, associate it
                                 		  with one or more Call Servers, and enable or disable security on the General tab.

Field

Description

Default

Value

Restart Required

IP Address

The IP address of the Reporting Server.

None

Valid IP address

Yes

Hostname 1

The hostname/IP address of the Reporting Server machine.

None

Valid DNS name, which can include letters of the alphabet and
                                             					 numbers 0 through 9.

Yes

Description

An optional text description for the Reporting Server.

None

Up to 1024 characters.

No

Enable Secure Communication with the Operations Console

Select to enable secure communications between the Operations
                                             					 Console and the Reporting Server component. The Reporting Server is accessed
                                             					 using SSH and files are transferred using HTTPS.

You must configure secure communications before you enable this option. See Administration Guide for
                                                      				  Cisco Unified Customer Voice Portal .

Off

On or Off

No

Device Version

Lists the release and build number for this device.

None

None

No

Associate Call Servers

Select one or more Call Servers to associate with the
                                             					 Reporting Server. You must select at least one Call Server. Call data for all
                                             					 SIP and VXML calls that are handled by this Call Server are stored in the
                                             					 Reporting Database. Click the right arrow to add a Call Server to the Selected
                                             					 pane.

Click the left arrow to remove a Call Server from the Selected
                                             					 pane.

None

A Call Server can be associated with only one Reporting
                                             					 Server.

No

### Reporting Properties Settings

Configure Reporting Server settings on the Reporting Properties tab.

Field

Description

Default

Range

Restart Required

Configuration

Enable Reporting

Enables the Reporting Server to receive call data
                                             from the associated Call Server.

Yes

Yes or No

Yes

Max. File Size (MB):

Defines the maximum size of the file that is used to
                                             record the data feed messages during a database
                                             failover. This size can be limited by the
                                             amount of free disk space.

100

1 through 250 MB

No

### Infrastructure Settings

The Reporting Server publishes statistics on the number of
                                 		  reporting events that it receives from the Unified CVP VXML Server, the SIP Service,
                                 		  and the IVR Service. It also publishes the  number of times the Reporting
                                 		  Server writes data to the Reporting Database. You can configure the interval at
                                 		  which the Reporting Server publishes these statistics, the maximum log file and
                                 		  directory size, and the details for recording syslog messages on the Reporting
                                 		  Server Infrastructure tab.

Field

Description

Default

Value

Restart Required

Configuration: Thread Management

Maximum Threads

(Required) The maximum thread pool size in the Reporting
                                             					 Server Java Virtual Machine.

500

100 to1000

Yes

Advanced

Statistics Aggregation Interval

The Reporting Server publishes statistics at this interval.

30 minutes

10 to1440

Yes

Log File Properties

Max Log File Size

(Required) Maximum size of the log file in megabytes.

To increase the log file size, go to C:\Cisco\CVP\conf , open log4j.xml file and  update the MaxFileSize value as shown:

```
<param name="MaxFileSize" value=" 10000000 "/>
```

Save the file and restart Reporting Server to deploy the changes.

10 MB

1 through 100 MB.

Yes

Max Log Directory Size

(Required) Maximum size of the directory containing Reporting
                                             					 Server log files.

20,000 MB

500 to 500,000 MB.

Max Log File Size is less than Max Log Directory Size.

Max Log Directory Size cannot be greater than
                                             					 500,000 MB.

Yes

Configuration: Primary Syslog Settings

Primary Syslog Server

Hostname or IP address of Primary Syslog Server to send syslog events
                                             					 from a CVP Application.

None

Valid IP address or hostname.

No

Primary Syslog Server Port Number

Port number of Primary Syslog Server.

None

Any available port number. Valid port numbers are integers
                                             					 between 1 and 65,535.

No

Primary Backup Syslog Server

Hostname or IP address of the Primary Backup Syslog Server to send
                                             					 syslog events from a CVP Application when the Syslog Server cannot be reached.

None

Valid IP address or hostname.

No

Primary Backup Syslog Server Port Number

Port number of Primary Backup Syslog Server.

None

Any available port number. Valid port numbers are integers
                                             					 between 1 and 65,535.

No

Configuration: Secondary Syslog Settings

Secondary Syslog Server

Hostname or IP address of Secondary Syslog Server to send syslog events
                                             					 from a CVP Application.

None

Valid IP address or hostname.

No

Secondary Syslog Server Port Number

Port number of Secondary Syslog Server.

None

Any available port number. Valid port numbers are integers
                                             					 between 1 and 65,535.

No

Secondary Backup Syslog Server

Hostname or IP address of the Secondary Backup Syslog Server to send
                                             					 syslog events from a CVP Application when the Syslog Server cannot be reached.

None

Valid IP address or hostname.

No

Secondary Backup Syslog Server Port Number

Port number of Secondary Backup Syslog Server.

None

Any available port number. Valid port numbers are integers
                                             					 between 1 and 65,535.

No

## IP Address Modification

This section describes how to change the IP address of Call Server, VXML Server, and the Reporting Server. Follow this sequence
                              for changing the IP Address of the devices:

Reporting Server

VXML Server

Call Server

OAMP Server

Step 1

Select the device from the Operations Console to change the IP address.

Step 2

From the menu bar of the device, select the device and click Use As Template .

Step 3

Assign the new IP address to the device and change the Host Name temporarily, which you will revert in Step 8, and click Save .

Do not click the Save and Deploy option until you have changed the physical server to the new IP address.

Step 4

Delete the device from the Operations Console before changing the IP address of the server.

Step 5

Configure the new IP address on the local server.

Step 6

Go to C:\Cisco\CVP\bin\UpdateRMIServerIP\updatermiserverip.bat and double-click the batch file to update the IP address in the windows registry and the wrapper.conf file.

Step 7

From the Operations Console, select the device and change the Host Name to the original one. Click Save and Deploy for the device. (Restart the server if network-related message is seen).

Step 8

Restart the server.

Make sure to change the configuration of VXML Application, Gateway, VVB, ICM PIM, Proxy, and CUCM to reflect the new Call
                                                            Server IP address.

Associate Reporting Server to the Call Server.

Delete the existing Media Server and create a new one with the Call Server IP address and deploy the Media Server.

### What to do next

| Note | You can
                                                				  associate a Call Server with only one Reporting Server. |
|---|---|

| Step 1 | On the Unified
                                       			 CVP Operations Console, select Device
                                             				  Management > Unified CVP Reporting Server . |
|---|---|
| Step 2 | Click Add
                                          				New to add a new Reporting Server or click Use As
                                          				Template to use an existing template to configure the new Reporting
                                       			 Server. |
| Step 3 | Click the
                                       			 following tabs and configure the settings based on your call flow model: General tab.
                                             				  For more information, see General Settings . Reporting
                                                					 Properties tab. For more information, see Reporting Properties Settings . Device Pool tab. For more information about adding, deleting, and editing device pool, see Add or Remove Device From Device Pool . Infrastructure tab. For more information, see Infrastructure Settings . |
| Step 4 | Click Save
                                          				and Deploy to deploy the changes to the Reporting Server page.
                                       			 Click Save to save the settings in the Operations Server
                                       			 database and configure the Reporting Server later. |

| Field | Description | Default | Value | Restart Required |
|---|---|---|---|---|
| IP Address | The IP address of the Reporting Server. | None | Valid IP address | Yes |
| Hostname 1 | The hostname/IP address of the Reporting Server machine. | None | Valid DNS name, which can include letters of the alphabet and
                                             					 numbers 0 through 9. | Yes |
| Description | An optional text description for the Reporting Server. | None | Up to 1024 characters. | No |
| Enable Secure Communication with the Operations Console | Select to enable secure communications between the Operations
                                             					 Console and the Reporting Server component. The Reporting Server is accessed
                                             					 using SSH and files are transferred using HTTPS. You must configure secure communications before you enable this option. See Administration Guide for
                                                      				  Cisco Unified Customer Voice Portal . | Off | On or Off | No |
| Device Version | Lists the release and build number for this device. | None | None | No |
| Associate Call Servers | Select one or more Call Servers to associate with the
                                             					 Reporting Server. You must select at least one Call Server. Call data for all
                                             					 SIP and VXML calls that are handled by this Call Server are stored in the
                                             					 Reporting Database. Click the right arrow to add a Call Server to the Selected
                                             					 pane. Click the left arrow to remove a Call Server from the Selected
                                             					 pane. | None | A Call Server can be associated with only one Reporting
                                             					 Server. | No |

| Field | Description | Default | Range | Restart Required |
|---|---|---|---|---|
| Configuration |  |
| Enable Reporting | Enables the Reporting Server to receive call data
                                             from the associated Call Server. | Yes | Yes or No | Yes |
| Max. File Size (MB): | Defines the maximum size of the file that is used to
                                             record the data feed messages during a database
                                             failover. This size can be limited by the
                                             amount of free disk space. | 100 | 1 through 250 MB | No |
|  |  |

| Field | Description | Default | Value | Restart Required |
|---|---|---|---|---|
| Configuration: Thread Management |  |
| Maximum Threads | (Required) The maximum thread pool size in the Reporting
                                             					 Server Java Virtual Machine. | 500 | 100 to1000 | Yes |
| Advanced |  |
| Statistics Aggregation Interval | The Reporting Server publishes statistics at this interval. | 30 minutes | 10 to1440 | Yes |
| Log File Properties |  |
| Max Log File Size | (Required) Maximum size of the log file in megabytes. Note To increase the log file size, go to C:\Cisco\CVP\conf , open log4j.xml file and  update the MaxFileSize value as shown: <param name="MaxFileSize" value=" 10000000 "/> Save the file and restart Reporting Server to deploy the changes. | Note | To increase the log file size, go to C:\Cisco\CVP\conf , open log4j.xml file and  update the MaxFileSize value as shown: <param name="MaxFileSize" value=" 10000000 "/> Save the file and restart Reporting Server to deploy the changes. | 10 MB | 1 through 100 MB. | Yes |
| Note | To increase the log file size, go to C:\Cisco\CVP\conf , open log4j.xml file and  update the MaxFileSize value as shown: <param name="MaxFileSize" value=" 10000000 "/> Save the file and restart Reporting Server to deploy the changes. |
| Max Log Directory Size | (Required) Maximum size of the directory containing Reporting
                                             					 Server log files. Note If you modify the value to a setting that is below the default
                                                      					 value, the log entries
                                                      					 might be lost,  which can affect troubleshooting. | Note | If you modify the value to a setting that is below the default
                                                      					 value, the log entries
                                                      					 might be lost,  which can affect troubleshooting. | 20,000 MB | 500 to 500,000 MB. Max Log File Size is less than Max Log Directory Size. Max Log Directory Size cannot be greater than
                                             					 500,000 MB. | Yes |
| Note | If you modify the value to a setting that is below the default
                                                      					 value, the log entries
                                                      					 might be lost,  which can affect troubleshooting. |
| Configuration: Primary Syslog Settings |  |
| Primary Syslog Server | Hostname or IP address of Primary Syslog Server to send syslog events
                                             					 from a CVP Application. | None | Valid IP address or hostname. | No |
| Primary Syslog Server Port Number | Port number of Primary Syslog Server. | None | Any available port number. Valid port numbers are integers
                                             					 between 1 and 65,535. | No |
| Primary Backup Syslog Server | Hostname or IP address of the Primary Backup Syslog Server to send
                                             					 syslog events from a CVP Application when the Syslog Server cannot be reached. | None | Valid IP address or hostname. | No |
| Primary Backup Syslog Server Port Number | Port number of Primary Backup Syslog Server. | None | Any available port number. Valid port numbers are integers
                                             					 between 1 and 65,535. | No |
| Configuration: Secondary Syslog Settings |
| Secondary Syslog Server | Hostname or IP address of Secondary Syslog Server to send syslog events
                                             					 from a CVP Application. | None | Valid IP address or hostname. | No |
| Secondary Syslog Server Port Number | Port number of Secondary Syslog Server. | None | Any available port number. Valid port numbers are integers
                                             					 between 1 and 65,535. | No |
| Secondary Backup Syslog Server | Hostname or IP address of the Secondary Backup Syslog Server to send
                                             					 syslog events from a CVP Application when the Syslog Server cannot be reached. | None | Valid IP address or hostname. | No |
| Secondary Backup Syslog Server Port Number | Port number of Secondary Backup Syslog Server. | None | Any available port number. Valid port numbers are integers
                                             					 between 1 and 65,535. | No |

| Note | To increase the log file size, go to C:\Cisco\CVP\conf , open log4j.xml file and  update the MaxFileSize value as shown: <param name="MaxFileSize" value=" 10000000 "/> Save the file and restart Reporting Server to deploy the changes. |
|---|---|

| Note | If you modify the value to a setting that is below the default
                                                      					 value, the log entries
                                                      					 might be lost,  which can affect troubleshooting. |
|---|---|

| Step 1 | Select the device from the Operations Console to change the IP address. |
|---|---|
| Step 2 | From the menu bar of the device, select the device and click Use As Template . |
| Step 3 | Assign the new IP address to the device and change the Host Name temporarily, which you will revert in Step 8, and click Save . Note Do not click the Save and Deploy option until you have changed the physical server to the new IP address. | Note | Do not click the Save and Deploy option until you have changed the physical server to the new IP address. |
| Note | Do not click the Save and Deploy option until you have changed the physical server to the new IP address. |
| Step 4 | Delete the device from the Operations Console before changing the IP address of the server. |
| Step 5 | Configure the new IP address on the local server. |
| Step 6 | Go to C:\Cisco\CVP\bin\UpdateRMIServerIP\updatermiserverip.bat and double-click the batch file to update the IP address in the windows registry and the wrapper.conf file. |
| Step 7 | From the Operations Console, select the device and change the Host Name to the original one. Click Save and Deploy for the device. (Restart the server if network-related message is seen). |
| Step 8 | Restart the server. Note Make sure to change the configuration of VXML Application, Gateway, VVB, ICM PIM, Proxy, and CUCM to reflect the new Call
                                                            Server IP address. Associate Reporting Server to the Call Server. Delete the existing Media Server and create a new one with the Call Server IP address and deploy the Media Server. | Note | Make sure to change the configuration of VXML Application, Gateway, VVB, ICM PIM, Proxy, and CUCM to reflect the new Call
                                                            Server IP address. Associate Reporting Server to the Call Server. Delete the existing Media Server and create a new one with the Call Server IP address and deploy the Media Server. |
| Note | Make sure to change the configuration of VXML Application, Gateway, VVB, ICM PIM, Proxy, and CUCM to reflect the new Call
                                                            Server IP address. Associate Reporting Server to the Call Server. Delete the existing Media Server and create a new one with the Call Server IP address and deploy the Media Server. |

| Note | Do not click the Save and Deploy option until you have changed the physical server to the new IP address. |
|---|---|

| Note | Make sure to change the configuration of VXML Application, Gateway, VVB, ICM PIM, Proxy, and CUCM to reflect the new Call
                                                            Server IP address. Associate Reporting Server to the Call Server. Delete the existing Media Server and create a new one with the Call Server IP address and deploy the Media Server. |
|---|---|