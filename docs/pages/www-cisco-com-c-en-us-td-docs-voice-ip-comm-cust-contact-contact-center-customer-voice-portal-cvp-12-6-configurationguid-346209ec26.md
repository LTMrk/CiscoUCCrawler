---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-346209ec26
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1252-operations-console.html
retrieved_at: 2026-08-21T06:52:23.462290+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

Chapter: Operations Console

## Chapter: Operations Console

# Operations Console

## Sign In to Operations Console

### Before you begin

Install Operations Console from the Unified CVP software CD.

Make a note of the password for the
                                       		  default Administrator account that you  created during the installation.

By default, the Operations Console session expires after 60  minutes. Relogin to Operations Console after the session expires.

Step 1

From the web browser, enter
                                       https:// ServerIP :9443/oamp, where ServerIP is the IP address or hostname of the machine on which the Operations
                                       Console is installed.

The main Unified CVP window
                                          opens.

Step 2

Enter your user ID in the Username field.

Enter Administrator , which is the default user
                                          account.

Step 3

In the Password field, enter your password.

If you are logging in to the default Administrator
                                          account, enter the password that was set for this account
                                          during installation.

If the user ID or password is invalid, the Operations Console
                                          Server displays the message, "Invalid Username or password."
                                          Enter your user ID and password again and click OK .

The main Cisco Unified Customer Voice Portal window
                                          opens.

Step 4

Check your security policy and, if needed,
                                       change the settings to a less restrictive level.

Default security settings can prevent users from using the
                                          Operations Console.

## Sign Out of Operations Console

From the Operations Console header, click Sign out .

The Login page of Unified Customer Voice
                              Portal window appears.

## Operations Console
                        	 Menus and Options

Menu

Options

Use To

System

Control
                                          					 Center

View the
                                          					 status of the Cisco Unified CVP environment in a network control center. View
                                          					 the status and statistics by Device Type or Device Pools, logical groups of
                                          					 devices in the Cisco Unified CVP solution. Initiate Start, Shutdown, or
                                          					 Graceful Shutdown actions on devices in the Control Center.

Device
                                          					 Pool

Create,
                                          					 modify, and delete device pool names and descriptions for logical groups of
                                          					 devices (for example, all devices located in a geographical region).

Import
                                          					 System Configuration

Import a
                                          					 previously-saved Operations Console Server configuration file and apply it to
                                          					 the current system.

Export
                                          					 System Configuration

Save and
                                          					 export all configuration information for the Operations Console Server to a
                                          					 single file on your local computer.

You can
                                          					 later use this file to restore an Operations Console Server during disaster
                                          					 recovery.

Location

Add, edit,
                                          					 synchronize, and delete Unified CM location information.

SIP Server
                                          					 Groups

Configure
                                          					 server groups for SIP and view Call Server deployment status.

Web
                                          					 Services

Configure
                                          					 Diagnostic Portal servlet credentials.

Dialed
                                          					 Number Pattern

Configure
                                          					 the Dialed Number Patterns for a destination. You can define the dialed numbers
                                          					 for the Error Tone, Ring Tone, and other destinations.

IOS
                                          					 Configuration

IOS
                                          					 Template Management - Add, Delete, Edit, Copy, and View an IOS template
                                          					 configuration pushed to an IOS gateway. The template contains the IOS commands
                                          					 required for use in a Unified CVP deployment.

IOS
                                          					 Template Deployment - Deploy a gateway configuration template to an IOS
                                          					 gateway. The template provisions the gateway and substitutes any variables in
                                          					 the template with the source devices that are chosen when it is deployed.

Courtesy
                                          					 Callback

Configure
                                          					 allowed and denied dialed numbers, maximum callbacks per number, and Call
                                          					 Server deployment.

Device
                                          					 Management

Unified
                                          					 CVP Call Server

Configure Call Server general and infrastructure settings; specify call services settings for each deployment model; associate
                                          Call Servers with device pools and the SIP Proxy Server.

Unified
                                          					 CVP Reporting Server

Configure
                                          					 Reporting Server general and infrastructure settings, associate Reporting
                                          					 Servers with Call Servers, specify reporting properties, and associate
                                          					 Reporting Servers with device pools.

Perform Reporting database administration: schedule database backups and purges; manage database and reporting user names
                                          and passwords.

Unified
                                          					 CVP VXML Server

Configure VXML Server general and infrastructure settings; specify primary and backup Call Servers; enable VXML Server reporting
                                          and specify VoiceXML data filters; associate VXML Servers with device pools; and transfer scripts to a VXML Server.

Unified
                                          					 CVP VXML Server (standalone)

Configure VXML Server (standalone) general settings; associate VXML Server (standalone) with device pools; and transfer scripts
                                          to a VXML Server (standalone).

Gatekeeper

Configure
                                          					 a Gatekeeper and add this device to the Device Pool.

Gateway

Configure Gateway general settings; associate Gateways with device pools; run a subset of IOS commands; view gateway statistics;
                                          and transfer files.

Virtualized Voice Browser

Configure VVB general settings and associate VVB with device
                                          					 pools.

Device
                                          					 Past Configurations

Review
                                          					 and Restore past device configurations.

Media
                                          					 Server

Configure Media Server general settings and associate a Media
                                          					 Server with device pools.

Unified
                                          					 CM

Configure Unified CM general settings; specify the URL to the Unified CM Device Administration page; and associate
                                          					 the Unified CM with
                                          					 device pools.

Unified
                                          					 ICM

Configure ICM Server general settings and associate the ICM
                                          					 Server with device pools.

SIP
                                          					 Proxy Server

Configure SIP Proxy Server general settings; specify the URL to
                                          					 the SIP Proxy Server Device Administration page; and associate the SIP Proxy
                                          					 Server with device pools.

Unified
                                          					 IC

Configure CUIS Server general settings and associate the CUIS
                                          					 Server with device pools.

Device
                                          					 Past Configurations

Review
                                          					 and Restore past device configurations.

Device
                                          					 Versions

View
                                          					 version information for the Call Server, Reporting Server, VXML Server, and
                                          					 VXML Server (standalone).

User
                                          					 Management

User
                                          					 Roles

Create,
                                          					 modify, and delete user roles. Assign SuperUser, Administrator, or Read Only
                                          					 access privileges to roles.

User
                                          					 Groups

Create,
                                          					 modify, and delete user groups. Assign roles to user groups.

Users

Manage
                                          					 Unified CVP users, and assign them to groups and roles.

Bulk
                                          					 Administration

File
                                          					 Transfer

Transfer script files to multiple devices at a time. The File Transfer submenu consists of the following options:

Scripts and Media

VXML Applications

SNMP

V1/V2c

Configure the SNMP agent that runs on the Unified CVP device to
                                          					 use the V1/V2 SNMP protocol to communicate with an SNMP management station; add
                                          					 and delete SNMP V1/V2c community strings; configure a destination to receive
                                          					 SNMP notifications from an SNMP management station; and associate community
                                          					 strings with the device.

The V1/V2c submenu consists of the following options:

Community String

Notification Destination

V3

Configure the SNMP agent that runs on the Unified CVP device to
                                          					 use the V3 SNMP protocol to communicate with an SNMP management station; add
                                          					 and delete SNMP users and set their access privileges; configure a destination
                                          					 to receive SNMP notifications from an SNMP management station; and associate
                                          					 SNMP users with devices.

The V3 submenu consists of the following options:

User

Notification Destination

System
                                          					 Group

Configure the MIB2 System Group system contact and location
                                          					 settings, and associate the MIB2 System Group with devices. The System Group submenu consists of the MIB2 option.

Tools

SNMP
                                          					 Monitor

Launch
                                          					 the SNMP Monitor application in a new browser window.

Configure

Display
                                          					 the URLs that launch the SNMP Monitor.

Help

Contents

Display
                                          					 the table of contents for the help system.

This
                                          					 Page

Display
                                          					 help of the current screen.

About

Display
                                          					 the version of the help system.

## System-Level Operation States

The Operations Console provides status information of for each device. A
                              device can be in one of the states as listed in the following table.

State

Reasons

Success

Indicates that the operation was successful.

Pending

Indicates that the operation has not yet been run.

In Progress

Indicates that the operation is in progress.

Failed

The reasons for a failed
                                             deployment state are listed
                                          below:

Unable to locate IP address in the database

General database failure

The call server was not deployed

Unknown error

Notification error: Contact administrator

Could not write to properties file

The Call Server device is using an unknown
                                                version of the Unified CVP software

The Call Server device is using an older
                                                version of the Unified CVP software

Configuration not removed from the database

This failure has multiple
                                                reasons:

Could not write to properties file

Device has not been deployed

General failure

Unable to access the Database

The reasons for a failed
                                             synchronization state are listed
                                          below:

Device is inaccessible

Authentication failure

Web service is not available on the device

General database error

General error

Unknown host address

SOAP service error

## IP Address Modification

This procedure describes how to change the IP address of the OAMP Server.

### Before you begin

You must have completed the IP address change of the following devices in this sequence:

Reporting Server

VXML Server

Call Server

Step 1

Configure the new IP address on the OAMP Server network card.

Step 2

Go to C:\Cisco\CVP\bin\UpdateRMIServerIP\updatermiserverip.bat . Double-click the batch file to update the IP address in the windows registry and the wrapper.conf file.

Step 3

Restart the server.

| Note | By default, the Operations Console session expires after 60  minutes. Relogin to Operations Console after the session expires. |
|---|---|

| Step 1 | From the web browser, enter
                                       https:// ServerIP :9443/oamp, where ServerIP is the IP address or hostname of the machine on which the Operations
                                       Console is installed. The main Unified CVP window
                                          opens. |
|---|---|
| Step 2 | Enter your user ID in the Username field. Enter Administrator , which is the default user
                                          account. |
| Step 3 | In the Password field, enter your password. If you are logging in to the default Administrator
                                          account, enter the password that was set for this account
                                          during installation. If the user ID or password is invalid, the Operations Console
                                          Server displays the message, "Invalid Username or password."
                                          Enter your user ID and password again and click OK . The main Cisco Unified Customer Voice Portal window
                                          opens. |
| Step 4 | Check your security policy and, if needed,
                                       change the settings to a less restrictive level. Default security settings can prevent users from using the
                                          Operations Console. |

| Menu | Options | Use To |
|---|---|---|
| System | Control
                                          					 Center | View the
                                          					 status of the Cisco Unified CVP environment in a network control center. View
                                          					 the status and statistics by Device Type or Device Pools, logical groups of
                                          					 devices in the Cisco Unified CVP solution. Initiate Start, Shutdown, or
                                          					 Graceful Shutdown actions on devices in the Control Center. |
| Device
                                          					 Pool | Create,
                                          					 modify, and delete device pool names and descriptions for logical groups of
                                          					 devices (for example, all devices located in a geographical region). |
| Import
                                          					 System Configuration | Import a
                                          					 previously-saved Operations Console Server configuration file and apply it to
                                          					 the current system. |
| Export
                                          					 System Configuration | Save and
                                          					 export all configuration information for the Operations Console Server to a
                                          					 single file on your local computer. You can
                                          					 later use this file to restore an Operations Console Server during disaster
                                          					 recovery. |
| Location | Add, edit,
                                          					 synchronize, and delete Unified CM location information. |
| SIP Server
                                          					 Groups | Configure
                                          					 server groups for SIP and view Call Server deployment status. |
| Web
                                          					 Services | Configure
                                          					 Diagnostic Portal servlet credentials. |
| Dialed
                                          					 Number Pattern | Configure
                                          					 the Dialed Number Patterns for a destination. You can define the dialed numbers
                                          					 for the Error Tone, Ring Tone, and other destinations. |
| IOS
                                          					 Configuration | IOS
                                          					 Template Management - Add, Delete, Edit, Copy, and View an IOS template
                                          					 configuration pushed to an IOS gateway. The template contains the IOS commands
                                          					 required for use in a Unified CVP deployment. IOS
                                          					 Template Deployment - Deploy a gateway configuration template to an IOS
                                          					 gateway. The template provisions the gateway and substitutes any variables in
                                          					 the template with the source devices that are chosen when it is deployed. |
| Courtesy
                                          					 Callback | Configure
                                          					 allowed and denied dialed numbers, maximum callbacks per number, and Call
                                          					 Server deployment. |
| Device
                                          					 Management | Unified
                                          					 CVP Call Server | Configure Call Server general and infrastructure settings; specify call services settings for each deployment model; associate
                                          Call Servers with device pools and the SIP Proxy Server. |
| Unified
                                          					 CVP Reporting Server | Configure
                                          					 Reporting Server general and infrastructure settings, associate Reporting
                                          					 Servers with Call Servers, specify reporting properties, and associate
                                          					 Reporting Servers with device pools. Perform Reporting database administration: schedule database backups and purges; manage database and reporting user names
                                          and passwords. |
| Unified
                                          					 CVP VXML Server | Configure VXML Server general and infrastructure settings; specify primary and backup Call Servers; enable VXML Server reporting
                                          and specify VoiceXML data filters; associate VXML Servers with device pools; and transfer scripts to a VXML Server. |
| Unified
                                          					 CVP VXML Server (standalone) | Configure VXML Server (standalone) general settings; associate VXML Server (standalone) with device pools; and transfer scripts
                                          to a VXML Server (standalone). Note A VXML Server (standalone) handles calls that arrive through a VoiceXML gateway . (No statistics are provided when the VXML Server is configured this way.) Also, you cannot configure a database to and capture
                                                   data from VXML Server (standalone) applications. | Note | A VXML Server (standalone) handles calls that arrive through a VoiceXML gateway . (No statistics are provided when the VXML Server is configured this way.) Also, you cannot configure a database to and capture
                                                   data from VXML Server (standalone) applications. |
| Note | A VXML Server (standalone) handles calls that arrive through a VoiceXML gateway . (No statistics are provided when the VXML Server is configured this way.) Also, you cannot configure a database to and capture
                                                   data from VXML Server (standalone) applications. |
| Gatekeeper | Configure
                                          					 a Gatekeeper and add this device to the Device Pool. |
| Gateway | Configure Gateway general settings; associate Gateways with device pools; run a subset of IOS commands; view gateway statistics;
                                          and transfer files. |
| Virtualized Voice Browser | Configure VVB general settings and associate VVB with device
                                          					 pools. |
| Device
                                          					 Past Configurations | Review
                                          					 and Restore past device configurations. |
| Media
                                          					 Server | Configure Media Server general settings and associate a Media
                                          					 Server with device pools. Note A
                                                   					 Media Server administers the media files that contain messages and prompts
                                                   					 callers hear. | Note | A
                                                   					 Media Server administers the media files that contain messages and prompts
                                                   					 callers hear. |
| Note | A
                                                   					 Media Server administers the media files that contain messages and prompts
                                                   					 callers hear. |
| Unified
                                          					 CM | Configure Unified CM general settings; specify the URL to the Unified CM Device Administration page; and associate
                                          					 the Unified CM with
                                          					 device pools. |
| Unified
                                          					 ICM | Configure ICM Server general settings and associate the ICM
                                          					 Server with device pools. |
| SIP
                                          					 Proxy Server | Configure SIP Proxy Server general settings; specify the URL to
                                          					 the SIP Proxy Server Device Administration page; and associate the SIP Proxy
                                          					 Server with device pools. |
| Unified
                                          					 IC | Configure CUIS Server general settings and associate the CUIS
                                          					 Server with device pools. |
| Device
                                          					 Past Configurations | Review
                                          					 and Restore past device configurations. |
| Device
                                          					 Versions | View
                                          					 version information for the Call Server, Reporting Server, VXML Server, and
                                          					 VXML Server (standalone). |
| User
                                          					 Management | User
                                          					 Roles | Create,
                                          					 modify, and delete user roles. Assign SuperUser, Administrator, or Read Only
                                          					 access privileges to roles. |
| User
                                          					 Groups | Create,
                                          					 modify, and delete user groups. Assign roles to user groups. |
| Users | Manage
                                          					 Unified CVP users, and assign them to groups and roles. |
| Bulk
                                          					 Administration | File
                                          					 Transfer | Transfer script files to multiple devices at a time. The File Transfer submenu consists of the following options: Scripts and Media VXML Applications |
| SNMP | V1/V2c | Configure the SNMP agent that runs on the Unified CVP device to
                                          					 use the V1/V2 SNMP protocol to communicate with an SNMP management station; add
                                          					 and delete SNMP V1/V2c community strings; configure a destination to receive
                                          					 SNMP notifications from an SNMP management station; and associate community
                                          					 strings with the device. The V1/V2c submenu consists of the following options: Community String Notification Destination |
| V3 | Configure the SNMP agent that runs on the Unified CVP device to
                                          					 use the V3 SNMP protocol to communicate with an SNMP management station; add
                                          					 and delete SNMP users and set their access privileges; configure a destination
                                          					 to receive SNMP notifications from an SNMP management station; and associate
                                          					 SNMP users with devices. The V3 submenu consists of the following options: User Notification Destination |
| System
                                          					 Group | Configure the MIB2 System Group system contact and location
                                          					 settings, and associate the MIB2 System Group with devices. The System Group submenu consists of the MIB2 option. |
| Tools | SNMP
                                          					 Monitor | Launch
                                          					 the SNMP Monitor application in a new browser window. |
| Configure | Display
                                          					 the URLs that launch the SNMP Monitor. |
| Help | Contents | Display
                                          					 the table of contents for the help system. |
| This
                                          					 Page | Display
                                          					 help of the current screen. |
| About | Display
                                          					 the version of the help system. |

| Note | A VXML Server (standalone) handles calls that arrive through a VoiceXML gateway . (No statistics are provided when the VXML Server is configured this way.) Also, you cannot configure a database to and capture
                                                   data from VXML Server (standalone) applications. |
|---|---|

| Note | A
                                                   					 Media Server administers the media files that contain messages and prompts
                                                   					 callers hear. |
|---|---|

| State | Reasons |
|---|---|
| Success | Indicates that the operation was successful. |
| Pending | Indicates that the operation has not yet been run. |
| In Progress | Indicates that the operation is in progress. |
| Failed | The reasons for a failed
                                             deployment state are listed
                                          below: Unable to locate IP address in the database General database failure The call server was not deployed Unknown error Notification error: Contact administrator Could not write to properties file The Call Server device is using an unknown
                                                version of the Unified CVP software The Call Server device is using an older
                                                version of the Unified CVP software Configuration not removed from the database This failure has multiple
                                                reasons: Could not write to properties file Device has not been deployed General failure Unable to access the Database |
| The reasons for a failed
                                             synchronization state are listed
                                          below: Device is inaccessible Authentication failure Web service is not available on the device General database error General error Unknown host address SOAP service error |

| Note | If you make any configuration changes after your initial deployment of any
                                       System-level configuration tasks, deploy the changed configuration
                                       again. |
|---|---|

| Step 1 | Configure the new IP address on the OAMP Server network card. |
|---|---|
| Step 2 | Go to C:\Cisco\CVP\bin\UpdateRMIServerIP\updatermiserverip.bat . Double-click the batch file to update the IP address in the windows registry and the wrapper.conf file. |
| Step 3 | Restart the server. |