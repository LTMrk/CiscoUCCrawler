---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-release-gui-62d8bc6658
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/release/guide/rcct_b_cce-solution-rns-12-6/cfin_m_1261_finesse-release-notes.html
retrieved_at: 2026-08-16T19:38:19.531115+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

# Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

Updated: May 14, 2021

Chapter: Cisco Finesse

## Chapter: Cisco Finesse

# Cisco Finesse

## New Features

### Locked Out Users (ES02 Update)

A new CLI utils finesse locked_out_users list has been added to view the list of locked out users. For more information on the CLI, see the Finesse Administration guide .

### Desktop Interface APIs (ES02 Update)

Three new APIs have been introduced, which are primarily used for Finesse desktop development. The APIs are as follows:

Desktop Configuration

Languages List

Verify Desktop and Third-Party URLs

For more information on the APIs, see the Cisco Finesse Desktop Interface API Guide .

### Agent Device Selection

When agents and supervisors need to use different devices that are configured with the same extension, the administrator must
                                 enable the Agent Device Selection feature for them. Agents and supervisors can select one of the endpoints (Desk Phone with
                                 Extension Mobility, Desk Phone without Extension Mobility, Jabber, and so on) on the shared Automatic Call Distribution (ACD)
                                 lines as the active device while signing in to Finesse desktop. This informs the solution to ignore the other devices and
                                 use the indicated device as the only source for call interaction. This allows effective control of the call irrespective of
                                 from where the user connects to the system. The user can switch the device based on where they are working, across shifts
                                 in an office, moving from one office to another across various locations, or working from home.

When the user signs in with the desired extension, the device selection screen displays a list of devices that share the same
                                 extension. If the required device is not listed, the user can refresh the list of devices (if the required device is not listed)
                                 and select the device that has to be used as the active device for the current desktop session.

For more information about how to enable or disable the feature, see the Agent Administration Tasks section in Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

For more information on device selection, see the Agent Device Selection section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html .

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge). For information about supported versions, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Agent PG Maintenance Mode

This release supports peripheral gateway (PG) maintenance mode, which allows the Cisco Finesse server to reconnect to the alternate PG
                                 without interrupting the current operations. When the Agent PG maintenance mode is initiated, Finesse desktop users and the Finesse IPPA users do not see any interruption during sign in, state operations, or call operations.

This feature is supported with Unified CCE deployments 12.6(1) and above.

For more information see Agent PG Maintenance Mode section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html

### Finesse Maintenance Mode

This release supports transitioning live Cisco Finesse nodes into a maintenance mode
                                 for performing administrative tasks, without causing any disruption to contact
                                 center activities. This feature is implemented in an automatic phased migration of
                                 the Cisco Finesse desktops from the primary node to the secondary node with minimal
                                 disruption to the agent activities.

This feature is supported with Unified CCE deployments 12.6(1) and above.

For more information, see Finesse Maintenance Mode section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html

### Multi-Tab Gadgets

Finesse desktop supports accessing multiple gadgets through tabs within a single gadget called Multi-Tab gadget. The Multi-Tab
                                 gadget allows the desktop to render more gadgets in a single desktop view and thus allows the contact center to efficiently
                                 utilize the desktop area. It enables more information to be presented to the agent in a concise and readily accessible manner,
                                 without forcing the user to scroll the page or switch the Finesse gadget container to see additional information.

The Multi-Tab gadget can host most gadgets supported by Cisco Finesse desktop. Multiple instances of Multi-Tab gadget containing
                                 different groups of gadgets are also supported, which helps users to stack groups of gadgets as required to customize their
                                 desktop.

Manage Chat and Email gadget (Finesse Agent desktop and Supervisor desktop)

Advanced Supervisor Capabilities gadget (Finesse Supervisor desktop)

The Multi-Tab gadget functionality supports the maximize and collapse options when configured as a page-level gadget or as
                                 a desktop container tab level gadget in the default layout setting.

For more information about this feature, see Multi-Tab Gadgets section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html

For more information about configuration, see Configure Multi-Tab Gadgets section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html

### Agent Answers

Agent Answers feature provides relevant suggestions and recommendations in real time
                                 for the agent to consider. The suggestions and recommendations are based on the
                                 ongoing conversation between the caller and the agent.

Agent Answers can be configured within the Multi-Tab gadget.

For more information about contact center AI gadgets, see Contact Center AI Gadgets in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html .

For more information on how to configure Agent Answers gadget, see section Add
                                    Agent Answers Gadgets in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html

### Custom Logon Messages

The custom messages appear in a pop-up box during the sign in process. The user has to acknowledge this message to proceed
                                 further. It is not mandatory to have custom messages. Administrators can set up the login messages in the Cisco Unified OS
                                 Administration console. For more information, see Configure Custom Logon Messages section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Change IP Address and Hostname

This release allows the administrator to change the IP address or hostname or domain name of the Cisco Finesse cluster nodes
                                 in your deployment.

For more information, see the Manage IP Address and Hostname chapter in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Supported Content Security Policy Directives

This release allows the administrator to use the following CLI commands to view, add, or delete the frame-access sources in
                                 the response header of Cisco Finesse. This ensures that only the configured sources can embed the Cisco Finesse in an iFrame
                                 within their HTML pages.

utils finesse frame_access_allowed_list add [source1,source2]

utils finesse frame_access_allowed_list delete

utils finesse frame_access_allowed_list list

For more information, see Supported Content Security Policy Directives section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Set Commands

The following CLIs have been introduced in this release :

Log Configuration

The administrator can use the following CLIs to add, delete, update, or view the logger configuration in the system for Finesse.

Secure XMPP Socket Port 5223

The administrator can set the utils finesse set_property webservices enableExternalNotificationPortAccess to true to enable the external access to the Cisco Finesse Notification Service XMPP port (5223).

Restricting Access to the External XMPP Notification Port 5223

The administrator can restrict the IP addresses from accessing the TCP-based XMPP notification port (5223) available for external
                                    client connectivity. The administrator can add, delete, or view the configured IP addresses using the following CLIs:

utils finesse notification external_port_access {add|delete|list}

For more information see, the Service Properties section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

CUIC Gadget URL

The administrator can use the following release-specific CLIs to change the .jsp references of Cisco Unified Intelligence
                                    Center (CUIC) gadgets to .xml in the Finesse desktop layout.

utils finesse layout updateCuicGadgetUrl 12.5.1

utils finesse layout updateCuicGadgetUrl 12.6.1+

For more information see, the Upgrade section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

The administrators can view the list of connected users in the current Finesse
                                    					server.

utils finesse show_connected_users summary

utils finesse show_connected_users detail

### REST APIs

The following APIs have been added.

Device—Get List of Devices for Extension—This API allows a user to retrieve the list of devices associated with an extension.

Finesse MaintenanceMode—This API allows the user to request Finesse to move to maintenance mode. The following are the new
                                       Finesse MaintenanceMode APIs:

Finesse MaintenanceMode—Get

Finesse MaintenanceMode—Update

ConnectedUsersInfo — This API allows the user to request for the details of
                                       						the connected users information. The following are the new Connected
                                       						APIs:

ConnectedUserInfo—Summary

ConnectedUserInfo—Get Connected Users Information

#### jQuery

The jQuery version hosted by Finesse has been upgraded from 3.4.1 to 3.5.1.

For more information, see REST API Developer Guide at https://developer.cisco.com/docs/finesse/#!javascript-library .

#### API Authentication changes for VPN-Less Deployment (ES02 Update)

For changes related to the authentication model when running in VPN-Less deployment, refer to the Cisco Unified Contact Center Enterprise Features Guide . The authentication changes made for VPN-Less deployment, primarily impacts third-party desktops and external API access.
                                 It does not impact the Finesse user authentication model and the functionality of the default desktop.

#### SystemInfo API (ES02 Update)

SystemInfo API is now authenticated when accessed via VPN-Less proxy. For alternatives to be used in non-authenticated mode,
                                 refer to the Cisco Finesse Desktop Interface API Guide .

### Restricting Access to the External XMPP Notification Port 5223

You can restrict the IP addresses from accessing the TCP-based XMPP notification port (5223) available for external client
                                 connectivity. You can add, delete, or view the configured IP addresses only when the enableExternalNotificationPortAccess property is enabled on all the Finesse nodes in the cluster. For more information about restricting the access to the port,
                                 see the Restricting Access to the External XMPP Notification Port 5223 section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

## Updated Features

### Reports (ES02 Update)

Historical and Realtime report gadgets are supported in supervisor desktop. The Stock reports can be viewed in the supervisor
                                 desktop. To configure custom reports as gadgets, you must run the CLI set cuic properties allow-proxy-custom-report command. The report execution dataset size for Historical and Realtime reports can be configured using the CLI set cuic properties vpnless-response-size-ht command. For more information, see the CUIC Administration guide .

### Drop Participants from Conference

The release allows an agent or a supervisor, who is the participant in a conference call, to drop other agents, supervisors,
                                 or non-agents from the conference call. The administrator can customize the desktop property value ( enableDropParticipantFor and dropParticipant ) of this feature through the desktop layout:

Default layout ( Desktop Layout )

Team-specific layouts ( Manage Team Resources > Desktop Layout )

Alternatively, the administrator can also set the permission using the CLI utils finesse set_property webservices enableDropParticipantFor or the Dialog—Drop Participant from Conference API.

For more information on how to set the permissions, see Drop Participants from Conference section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html and REST API Developer Guide at https://developer.cisco.com/docs/finesse/#!javascript-library .

### Dual-Tone Multi-Frequency (DTMF) Updates

This release throttles the number of back-to-back DTMF requests that can be sent by the desktop, to prevent CTI errors. The
                                 administrator can configure the number of outstanding DTMF requests and the timeout duration. The administrator can customize
                                 the desktop property value ( pendingDTMFThresholdCount and dtmfRequestTimeoutInMs ) of this feature through the desktop layout:

Default layout ( Desktop Layout )

Team-specific layouts ( Manage Team Resources > Desktop Layout )

Alternatively, the administrator can also use the following CLIs:

utils finesse set_property desktop pendingDTMFThresholdCount <value>

utils finesse set_property desktop dtmfRequestTimeoutInMs <value>

### Changes in REST APIs

The following changes are made to the payloads.

User APIs—The following fields are added to the payload:

deviceSelection—Indicates whether the CTI device selection is enabled for the agent.

activeDeviceId—A unique ID of the active device associated with the extension to which the agent is signed in.

Devices—Information about the list of devices associated with an extension.

skillTargetId—Indicates the unique identifier for the skill target assigned to the agent in the Unified CCE database.

services—Indicates the services that are configured for a user.

Dialog—Drop Participant from Conference—This API allows an agent or supervisor to make a request to drop other participants
                                       from a conference based on the permission set by the administrator. The following fields are added to the payload:

ccaiConfigId—Unique configuration ID that is created by the AI service.

services—Indicates the services that are configured for a user.

Single Sign-On APIs—The optional parameters are added in the Fetch Access Token and Refresh Existing Access Token APIs

SystemInfo APIs—The following fields are added to the payload:

ctiTimeInMMode—The total time (in seconds) that the CTI server is in maintenance mode.

ctiMMode—Indicates whether the CTI server is in maintenance mode.

ctiServers—Information about the list of CTI servers that the Cisco Finesse is connected to.

finesseTimeInMMode—The total time (in seconds) that the Finesse server is in maintenance mode.

finesseMMode—Indicates whether the Finesse server is in maintenance mode.

For more information, see REST API Developer Guide at https://developer.cisco.com/docs/finesse/#!rest-api-dev-guide .

### Changes in JavaScript APIs

The following changes are made to the payloads.

Gadget Configuration—Added the skillTargetId  field which refers to the skill ID of the user.

User—The following functions are added:

getSkillTargetId—Retrieves the Id for the skill target assigned to the user in the Unified CCE database.

isDeviceSelectionEnabled—Retrieves whether the device selection is enabled for the user.

getServices—Retrieves the list of services that are configured for the user.

SystemInfo—The following functions are added:

getCtiMMode—Retrieves the CTI server in maintenance mode.

getCtiTimeInMMode—Retrieves the total time (in seconds) that the CTI server is in maintenance mode.

getCtiServers—Retrieves the list of CTI servers that Cisco Finesse is connected to.

getfinesseMMode—Indicates whether the Finesse server is in maintenance mode.

getfinesseTimeInMMode—The total time (in seconds) that the Finesse server is in maintenance mode.

For more information, see Cisco Finesse JavaScript APIs chapter in REST API Developer Guide at https://developer.cisco.com/docs/finesse/#!javascript-library .

### Serviceability Improvements

This release provides the following serviceability improvements:

Trace level logging support ( utils finesse log )

Fine-grained logging control for critical services ( utils finesse log )

ConnectedUsersInfo API to retrieve the list of users signed in to a specific node

Finesse Maintenance Mode Services ( utils finesse maintenance initiate and utils finesse maintenance status )

For more information about logging improvements and Finesse Maintenance Mode Services, refer to the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

For more information about the ConnectedUsersInfo API, see the ConnectedUsersInfo section in the Cisco Finesse Web Services Developer and JavaScript Guide at https://developer.cisco.com/docs/finesse/ .

#### Connected Agents Gadget

This release introduces the Connected Agents gadget for administrators that lists all the agents currently signed in to Cisco
                                    Finesse. You can use this gadget to determine which agents are signed in to the Publisher and the Subscriber. You can use
                                    this gadget also to filter the client types and identify the client type through which an agent has signed in.

For more information, see the Manage Connected Agents section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

## Important Notes

Finesse desktop now connects to the Notification service using WebSocket or BOSH with https port 8445 instead of 7443. The
                                    advantage is that it reduces the number of certificates that needs to be accepted by the desktop during log in.

Third-party client software can connect to the Notification service using WebSocket or BOSH with either 7443 or 8445 https
                                    port.

The Phonebook container width is increased to 170 pixels in the desktop UI so that more characters are shown without the ellipsis.
                                    Any contact name exceeding the preset width (170 pixels) will have an ellipsis and a tool tip next to it to show the full
                                    name.

With the upgrade to Tomcat 9, the "reason phrase" parameter, which provides additional information about the http response
                                    according to the status code, is not sent. If the third-party applications that use Finesse APIs build their logic based on
                                    the "reason phrase" parameter, the logic will fail.

Cisco Finesse provides Java Management Extensions (JMX) counters with associated threshold values that can be used to monitor
                                    the health of the Finesse. For more information, see the JMX Counter Thresholds section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

The following are some of the new restrictions due to Java version upgrade and CiscoJCE provider:

Expired certificates are not supported. All the components in Unified CCE should contain valid certificates.

Gadget hosting server's certificate must contain "Digital Signature" as one of the KeyUsage purposes.

## Deprecated Features

### Notifications over BOSH (Long Polling)

In this release, support for notifications over BOSH (long polling) is deprecated. Applications that require notifications
                              are recommended to use WebSocket-based notifications (Finesse desktop) or notifications over direct XMPP (over TCP).

The usage of port 7443 is deprecated and the port 8445 should be used instead. For the details on how to use port 8445 for
                              WebSocket notifications, refer to the Managing Notifications in Third-Party Applications section of the Cisco Finesse Web Services Developer and JavaScript Guide .

## Removed and Unsupported Features

### Internet Explorer 11

In this release, support for Internet Explorer version 11 is removed. Edge Chromium (Microsoft Edge) is the replacement.

For information about supported versions, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### CLIs

The following CLIs are removed:

utils finesse trace enable

utils finesse trace disable

utils finesse trace status

utils finesse notification logging status

## Third Party Software Impacts

None.

| Note | This feature is supported with Unified CCE deployments 12.6(1) and above. |
|---|---|

| Note | This feature is supported with Unified CCE deployments 12.6(1) and above. |
|---|---|

| Note | The Multi-Tab gadget cannot host the following gadgets: Manage Chat and Email gadget (Finesse Agent desktop and Supervisor desktop) Advanced Supervisor Capabilities gadget (Finesse Supervisor desktop) |
|---|---|

| Note | Agent Answers can be configured within the Multi-Tab gadget. |
|---|---|