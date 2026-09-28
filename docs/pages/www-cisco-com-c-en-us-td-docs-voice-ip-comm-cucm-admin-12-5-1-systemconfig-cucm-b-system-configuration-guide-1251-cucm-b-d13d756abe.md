---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-d13d756abe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0110110.html
retrieved_at: 2026-08-16T17:33:20.429627+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure CTI Applications

## Chapter: Configure CTI Applications

# Configure CTI Applications

## CTI Applications Overview

You can use Computer Telephony Integration (CTI) to take advantage of computer-processing functions while making, receiving,
                           and managing telephone calls. CTI applications allow you to perform such tasks as retrieving customer information from a database
                           using a caller ID, or to work with the information gathered by an Interactive Voice Response (IVR) system to route a customer’s
                           call, along with their information, to the appropriate customer service representative.

Applications that want to terminate media for calls at route points must specify the media and port for the call on a per-call
                           basis. CTI applications can terminate media on CTI ports and CTI route points using either static or dynamic IP addresses
                           and port numbers.

This chapter describes how to configure Cisco Unified Communications Manager to work with CTI applications. For information
                           about how to configure specific applications, see the Feature Configuration Guide for Cisco Unified Communications Manager.

Some of the Cisco CTI applications available are:

Cisco IP Communicator:  A desktop application which  turns your computer into a full-feature telephone with the added advantages
                                 of call tracking, desktop collaboration, and one-click dialing from online directories.

Cisco Unified Communications Manager Auto-Attendant: Works with Unified Communications Manager to receive calls on specific
                                 telephone extensions and to allow the caller to choose an appropriate extension.

Cisco Web Dialer: Allows Cisco IP Phone users to make calls from web and desktop applications.

Cisco Unified Communications Manager Assistant: Enables managers and their assistants to work together more effectively. The
                                 feature comprises a call-routing service, enhancements to phone capabilities for the manager and the assistant, and assistant
                                 console interfaces that are primarily used by the assistant.

To determine which Unified Communications Manager CTI applications support SIP IP phones, see the application-specific documentation.

### CTI Route Points Overview

A CTI route point virtual device can receive multiple, simultaneous calls for application-controlled redirection. You can
                              configure one or more lines on a CTI route point that users can call to access the application. Applications can answer calls
                              at a route point and can also redirect calls to a CTI port or IP phone. When a CTI application requests to redirect a call
                              by using the Redirect API, Cisco Unified Communications Manager uses the configuration for the line/device calling search
                              space for the redirected party.

With CTI route points you can:

Answer a call

Make and receive multiple active calls

Redirect a call

Hold a call

Unhold a call

Drop a call

### CTI Redundancy on Cisco Unified Communications Manager

When a Unified Communications Manager node in a cluster fails, the CTIManager recovers the affected CTI ports and route points
                              by reopening these devices on another Unified Communications Manager node. If an application has a phone device open, the
                              CTIManager also reopens the phone when the phone fails over to a different Unified Communications Manager. If the Cisco IP
                              Phone does not fail over to a different Unified Communications Manager, the CTIManager cannot open the phone or a line on
                              the phone. The CTIManager uses the Unified Communications Manager group that is assigned to the device pool to determine which
                              Unified Communications Manager to use to recover the CTI devices and phones that the applications opened.

### CTI Redundancy on CTIManager

When a CTIManager fails, the applications that are connected to the CTIManager can recover the affected resources by reopening
                              these devices on another CTIManager. An application determines which CTIManager to use on the basis of CTIManagers that you
                              defined as primary and backup when you set up the application (if supported by the application). When the application connects
                              to the new CTIManager, it can reopen the devices and lines that previously opened. An application can reopen a Cisco IP Phone
                              before the phone rehomes to the new Unified Communications Manager; however, it cannot control the phone until the rehoming
                              completes.

The applications do not rehome to the primary CTIManager when it comes back in service. Applications fail back to the primary
                                          CTIManager if you restart the application or if the backup CTIManager fails.

### CTI Redundancy for Application Failure

When an application (TAPI/JTAPI or an application that directly connects to the CTIManager) fails, the CTIManager closes
                              the application and redirects unterminated calls at CTI ports and route points to the configured call forward on failure (CFOF)
                              number. The CTIManager also routes subsequent calls into those CTI ports and route points to the configured Call Forward No
                              Answer (CFNA) number until the application recovers and reregisters those devices.

## CTI Applications Prerequisites

You must have device pools configured  before you can configure Cisco Unified Communications Manager for CTI Applications.

Add and configure  IP phones for each CTI application. For further information on adding and configuring IP Phones see, Cisco
                              Unified IP Phones.

Configure the end users and application users that will use CTI applications.

Computer Telephony Integration (CTI) provides IP address information through the JTAPI and TAPI interfaces, which can support
                              IPv4 and IPv6 addresses. If you want to support IPv6 addresses, make sure that your applications are using a JTAPI /TAPI client
                              interface version that supports IPv6.

## Configure CTI
                        	 Applications Task Flow

To configure Cisco Unified Communications Manager for CTI applications follow these tasks.

Step 1

Activate the CTIManager Service

Activate the CTIManager service on the appropriate servers, if not already activated.

Step 2

Configure CTIManager and Cisco Unified Communications Manager Service Parameters

Configure CTIManager
                                          		  advanced clusterwide service parameters that are used in
                                          		  conjunction with the CTI Super Provider capability.

Step 3

To configure CTI Route Points perform the following procedure:

Configure one or more CTI route point virtual devices which can receive multiple, simultaneous calls for application-controlled
                                          redirection.

Step 4

Configure CTI Device Directory Number

Configure the directory number for the CTI device.

Step 5

Associate Devices with Groups

Associate all devices that the application will use for application users and end users with the appropriate Cisco Unified
                                          Communications Manager group (via the device pool).

Step 6

Add End Users and Application Users

Allow a CTI application to control any CTI-controllable devices that are configured in the Cisco Unified Communications Manager
                                          system by adding the end users and application users to the Standard CTI Enabled user group.

Step 7

(Optional) Configure CTI Redundancy for Application Failure

To define the interval
                                          		  at which CTIManager expects to receive a message from an application within
                                          		  two consecutive intervals.

### Activate the CTIManager Service

Step 1

On Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

Choose the node from the Server drop-down list.

Step 3

Check the Cisco CTIManager check box in the CM Services section.

Step 4

Click Save .

### Configure
                           	 CTIManager and Cisco Unified Communications Manager Service Parameters

Configure CTIManager
                                 		  advanced clusterwide service parameters that are used in
                                 		  conjunction with the CTI Super Provider capability.

If the
                                             			 configured limits are exceeded, CTI generates alarms, but the applications
                                             			 continue to operate with the extra devices.

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters .

Step 2

Choose the node from the Server drop-down list.

Step 3

Choose Cisco CTIManager (Active) from the Service drop-down list.

Step 4

On the Service Parameter Configuration window, click Advanced .

Step 5

In the Maximum Devices Per Provider field, enter the maximum number of devices that a single CTI application can open. The default is 2000 devices.

Step 6

In the Maximum Devices Per Node field, enter the maximum number of devices that all CTI applications can open on any CTIManager
                                          node in the Unified Communications Manager system. The default is 800 devices.

Step 7

Click Save .

### Configure CTI Route Points Task Flow

Step 1

Configure CTI Route Points

Add a new, or modify an existing CTI route point.

Step 2

Configure New Call Accept Timer

Configure the New Call Accept Timer so that when a call arrives at a route point, the application will handle (accept, answer,
                                             redirect) it within the time specified.

Step 3

Configure Simultaneous Active Calls

Configure the number of simultaneous active calls on the route point.

Step 4

Optional : Synchronize CTI Route Point

Synchronize a CTI route point with the most recent configuration changes, which applies any outstanding configuration settings
                                             in the least intrusive manner possible. (For example, a reset/restart may not be required on some affected devices.)

#### Configure CTI Route Points

Add a new, or modify an existing CTI route point.

Step 1

From Cisco Unified CM Administration, click Device > CTI Route Point .

Step 2

Perform one of the following tasks:

- Click Add New , to add a new gateway.

- Click Find and select a CTI route point from the resulting list to modify the settings for an existing CTI route point, enter search
                                                criteria.

Step 3

Configure the fields in the CTI Route Point Configuration window. For more information on the fields and their configuration options, see the system Online Help..

Step 4

Click Save .

#### Configure New Call Accept Timer

Configure the New Call Accept Timer so that when a call arrives at a route point, the application will handle (accept, answer,
                                    redirect) it within the time specified.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

Choose the node from the Server drop-down list.

Step 3

Choose Cisco CallManager (Active) from the Service drop-down list.

Step 4

In the CTI New Call Accept Timer field, specify the time that you want to allow for a call to be answered. The default value is 4.

Step 5

Click Save .

#### Configure Simultaneous Active Calls

Configure the number of simultaneous active calls on the route point.

If you are planning to use a TAPI application to control CTI port devices by using the Cisco CallManager Telephony Service
                                                Provider (TSP), you may only configure one line per CTI port device.

Step 1

From Cisco Unified CM Administration, click Call Routing > Directory Number .

Step 2

On the Directory Number Configuration window, click Add New .

Step 3

Fill in the required fields.

Step 4

Click Save .

#### Synchronize CTI Route Point

Synchronize a CTI route point with the most recent configuration changes, which applies any outstanding configuration settings
                                    in the least intrusive manner possible. (For example, a reset/restart may not be required on some affected devices.)

Step 1

From Cisco Unified CM Administration, click Device > CTI Route Point .

Step 2

On the Find and List CTI Route Points window, click Find to display the list of CTI route points.

Step 3

Check the check boxes next to the CTI route points that you want to synchronize. To choose all CTI route points in the window,
                                             check the check box in the matching records title bar.

Step 4

Click Apply Config to Selected .

Step 5

Click OK .

### Configure CTI
                           	 Device Directory Number

Configure the directory number for the CTI device.

Step 1

From Cisco Unified CM
                                          			 Administration, choose Call Routing > Directory
                                                				  Number .

Step 2

On the Find and List Directory Numbers window, click Add New .

Step 3

On the Directory Number Configuration window, and enter the required fields.

Step 4

Click Save .

### Associate Devices with Groups

Associate all devices that the application will use for application users and end users with the appropriate Cisco Unified
                                 Communications Manager group (via the device pool).

Step 1

From Cisco Unified CM Administration, click User Management > Application User .

Step 2

On the Find and List Application Users window, click Add New . This brings you to the Application User Configuration window.

Step 3

In the Device Information pane, associate your devices by moving them from the Available Devices list to the Controlled Devices
                                          list.

Step 4

Click Save .

Step 5

To Associate Devices for end users, click User Management > End User .

Step 6

Repeat steps 2 - 4.

### Add End Users and Application Users

Allow a CTI application to control any CTI-controllable devices that are configured in the Cisco Unified Communications Manager
                                 system by adding the end users and application users to the Standard CTI Enabled user group.

Step 1

From Cisco Unified CM Administration, click User Management > User Settings > Access Control Group .

Step 2

On the Find and List Access Control Groups window, click Find to display the current list of access control groups.

Step 3

Click Standard CTI Enabled , this brings you to the Access Control Group Configuration window for this group. Ensure all CTI users are in the Standard
                                          CTI Enabled user group. See  Access Control Group Configuration Options, for  a full list of available groups and their capabilities.

Step 4

If you want to add end users, click Add End Users to Group or, if you want to add application users, click Add App Users to Group .

Step 5

Click Find , to display the list of current users.

Step 6

Check the users you want to assign to the  Standard CTI Enabled user group.

Step 7

Click Add Selected .

#### Access Control Group Configuration Options

The CTI application must support the specified user group to which it is assigned.

Cisco recommends that users who are associated with the Standard CTI Allow Control of All Devices user group also be associated
                                                with the Standard CTI Secure Connection user group.

You must add the particular device under Controlled Devices for all the roles, listed in the following table, to work properly.

Field

Description

Standard CTI Allow Call Monitoring

This user group allows an application to monitor calls.

Standard CTI Allow Call Park Monitoring

This user group allows an application to receive a notification when calls are parked/unparked to all Call Park directory
                                                numbers.

Standard CTI Allow Call Recording

This user group allows an application to record calls.

Standard CTI Allow Calling Number Modification

This user group allows an application to modify the calling party number in supported CTI applications.

Standard CTI Allow Control of All Devices

This user group allows an application to control or monitor any CTI-controllable device in the system.

Standard CTI Allow Reception of SRTP Key Material

This user group allows an application to receive information that is necessary to decrypt encrypted media streams. This group
                                                typically gets used for recording and monitoring purposes.

Standard CTI Enabled

This user group, which is required for all CTI applications, allows an application to connect to Cisco Unified Communications
                                                Manager and to access CTI functionality.

Standard CTI Secure Connection

Inclusion into this group requires that the application has a secure (TLS) CTI connection to Cisco Unified Communications
                                                Manager and that the Cisco Unified Communications Manager cluster has security enabled.

### Configure CTI
                           	 Redundancy for Application Failure

To define the interval at which CTI Manager expects to receive a message from an application within two consecutive intervals.

Step 1

From Cisco Unified CM
                                          			 Administration, choose System > Service
                                                				  Parameters .

Step 2

Choose the node from the Server drop-down list.

Step 3

Choose Cisco CTIManager (Active) from the Service drop-down list.

Step 4

On the Service Parameter Configuration window, click Advanced .

Step 5

In the Application Heartbeat Minimum Interval field, enter the time for the minimum interval. The default is 5.

Step 6

In the Application Heartbeat Maximum Interval field, enter the time for the maximum interval. The default is 3600.

Step 7

Click Save .

| Note | To determine which Unified Communications Manager CTI applications support SIP IP phones, see the application-specific documentation. |
|---|---|

| Note | The applications do not rehome to the primary CTIManager when it comes back in service. Applications fail back to the primary
                                          CTIManager if you restart the application or if the backup CTIManager fails. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate the CTIManager Service | Activate the CTIManager service on the appropriate servers, if not already activated. |
| Step 2 | Configure CTIManager and Cisco Unified Communications Manager Service Parameters | Configure CTIManager
                                          		  advanced clusterwide service parameters that are used in
                                          		  conjunction with the CTI Super Provider capability. |
| Step 3 | To configure CTI Route Points perform the following procedure: | Configure one or more CTI route point virtual devices which can receive multiple, simultaneous calls for application-controlled
                                          redirection. |
| Step 4 | Configure CTI Device Directory Number | Configure the directory number for the CTI device. |
| Step 5 | Associate Devices with Groups | Associate all devices that the application will use for application users and end users with the appropriate Cisco Unified
                                          Communications Manager group (via the device pool). |
| Step 6 | Add End Users and Application Users | Allow a CTI application to control any CTI-controllable devices that are configured in the Cisco Unified Communications Manager
                                          system by adding the end users and application users to the Standard CTI Enabled user group. |
| Step 7 | (Optional) Configure CTI Redundancy for Application Failure | To define the interval
                                          		  at which CTIManager expects to receive a message from an application within
                                          		  two consecutive intervals. |

| Step 1 | On Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | Choose the node from the Server drop-down list. |
| Step 3 | Check the Cisco CTIManager check box in the CM Services section. |
| Step 4 | Click Save . |

| Note | If the
                                             			 configured limits are exceeded, CTI generates alarms, but the applications
                                             			 continue to operate with the extra devices. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | Choose the node from the Server drop-down list. |
| Step 3 | Choose Cisco CTIManager (Active) from the Service drop-down list. |
| Step 4 | On the Service Parameter Configuration window, click Advanced . |
| Step 5 | In the Maximum Devices Per Provider field, enter the maximum number of devices that a single CTI application can open. The default is 2000 devices. |
| Step 6 | In the Maximum Devices Per Node field, enter the maximum number of devices that all CTI applications can open on any CTIManager
                                          node in the Unified Communications Manager system. The default is 800 devices. |
| Step 7 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure CTI Route Points | Add a new, or modify an existing CTI route point. |
| Step 2 | Configure New Call Accept Timer | Configure the New Call Accept Timer so that when a call arrives at a route point, the application will handle (accept, answer,
                                             redirect) it within the time specified. |
| Step 3 | Configure Simultaneous Active Calls | Configure the number of simultaneous active calls on the route point. |
| Step 4 | Optional : Synchronize CTI Route Point | Synchronize a CTI route point with the most recent configuration changes, which applies any outstanding configuration settings
                                             in the least intrusive manner possible. (For example, a reset/restart may not be required on some affected devices.) |

| Step 1 | From Cisco Unified CM Administration, click Device > CTI Route Point . |
|---|---|
| Step 2 | Perform one of the following tasks: Click Add New , to add a new gateway. Click Find and select a CTI route point from the resulting list to modify the settings for an existing CTI route point, enter search
                                                criteria. |
| Step 3 | Configure the fields in the CTI Route Point Configuration window. For more information on the fields and their configuration options, see the system Online Help.. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | Choose the node from the Server drop-down list. |
| Step 3 | Choose Cisco CallManager (Active) from the Service drop-down list. |
| Step 4 | In the CTI New Call Accept Timer field, specify the time that you want to allow for a call to be answered. The default value is 4. |
| Step 5 | Click Save . |

| Note | If you are planning to use a TAPI application to control CTI port devices by using the Cisco CallManager Telephony Service
                                                Provider (TSP), you may only configure one line per CTI port device. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, click Call Routing > Directory Number . |
|---|---|
| Step 2 | On the Directory Number Configuration window, click Add New . |
| Step 3 | Fill in the required fields. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, click Device > CTI Route Point . |
|---|---|
| Step 2 | On the Find and List CTI Route Points window, click Find to display the list of CTI route points. |
| Step 3 | Check the check boxes next to the CTI route points that you want to synchronize. To choose all CTI route points in the window,
                                             check the check box in the matching records title bar. |
| Step 4 | Click Apply Config to Selected . |
| Step 5 | Click OK . |

| Step 1 | From Cisco Unified CM
                                          			 Administration, choose Call Routing > Directory
                                                				  Number . |
|---|---|
| Step 2 | On the Find and List Directory Numbers window, click Add New . |
| Step 3 | On the Directory Number Configuration window, and enter the required fields. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, click User Management > Application User . |
|---|---|
| Step 2 | On the Find and List Application Users window, click Add New . This brings you to the Application User Configuration window. |
| Step 3 | In the Device Information pane, associate your devices by moving them from the Available Devices list to the Controlled Devices
                                          list. |
| Step 4 | Click Save . |
| Step 5 | To Associate Devices for end users, click User Management > End User . |
| Step 6 | Repeat steps 2 - 4. |

| Step 1 | From Cisco Unified CM Administration, click User Management > User Settings > Access Control Group . |
|---|---|
| Step 2 | On the Find and List Access Control Groups window, click Find to display the current list of access control groups. |
| Step 3 | Click Standard CTI Enabled , this brings you to the Access Control Group Configuration window for this group. Ensure all CTI users are in the Standard
                                          CTI Enabled user group. See  Access Control Group Configuration Options, for  a full list of available groups and their capabilities. |
| Step 4 | If you want to add end users, click Add End Users to Group or, if you want to add application users, click Add App Users to Group . |
| Step 5 | Click Find , to display the list of current users. |
| Step 6 | Check the users you want to assign to the  Standard CTI Enabled user group. |
| Step 7 | Click Add Selected . |

| Note | The CTI application must support the specified user group to which it is assigned. |
|---|---|

| Note | Cisco recommends that users who are associated with the Standard CTI Allow Control of All Devices user group also be associated
                                                with the Standard CTI Secure Connection user group. |
|---|---|

| Note | You must add the particular device under Controlled Devices for all the roles, listed in the following table, to work properly. |
|---|---|

| Field | Description |
|---|---|
| Standard CTI Allow Call Monitoring | This user group allows an application to monitor calls. |
| Standard CTI Allow Call Park Monitoring | This user group allows an application to receive a notification when calls are parked/unparked to all Call Park directory
                                                numbers. |
| Standard CTI Allow Call Recording | This user group allows an application to record calls. |
| Standard CTI Allow Calling Number Modification | This user group allows an application to modify the calling party number in supported CTI applications. |
| Standard CTI Allow Control of All Devices | This user group allows an application to control or monitor any CTI-controllable device in the system. |
| Standard CTI Allow Reception of SRTP Key Material | This user group allows an application to receive information that is necessary to decrypt encrypted media streams. This group
                                                typically gets used for recording and monitoring purposes. |
| Standard CTI Enabled | This user group, which is required for all CTI applications, allows an application to connect to Cisco Unified Communications
                                                Manager and to access CTI functionality. |
| Standard CTI Secure Connection | Inclusion into this group requires that the application has a secure (TLS) CTI connection to Cisco Unified Communications
                                                Manager and that the Cisco Unified Communications Manager cluster has security enabled. |

| Step 1 | From Cisco Unified CM
                                          			 Administration, choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | Choose the node from the Server drop-down list. |
| Step 3 | Choose Cisco CTIManager (Active) from the Service drop-down list. |
| Step 4 | On the Service Parameter Configuration window, click Advanced . |
| Step 5 | In the Application Heartbeat Minimum Interval field, enter the time for the minimum interval. The default is 5. |
| Step 6 | In the Application Heartbeat Maximum Interval field, enter the time for the maximum interval. The default is 3600. |
| Step 7 | Click Save . |