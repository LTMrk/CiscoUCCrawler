---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-maintain-and-operate-guid-c60753ec7d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/maintain_and_operate/guide/uccx_b_1251su1admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_011000.html
retrieved_at: 2026-08-16T21:39:52.362833+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)SU1

Updated: January 31, 2021

Chapter: Extend and Connect

## Chapter: Extend and Connect

# Extend and Connect

## Overview of Extend and Connect

With the Extend and Connect feature, Unified Contact Center Express agents and supervisors can work from a remote location
                              using any device.

This feature gives the user (agent or supervisor) the flexibility to answer or make calls using devices that are connected
                              to the PSTN or to mobile or other PBX networks. Extend and Connect functions by leveraging CTI remote device and persistent
                              connection features of Cisco Unified Communications Manager (CUCM).

You can enable the Extend and Connect feature through the Cisco Jabber client by selecting only the Extend mode. This feature
                              provide the following connections:

CTI remote device—CTI remote devices are Unified CCX off-cluster devices for users that can be connected to any of the third-party
                                    networks, such as PSTN, mobile, or PBX.

Persistent connection—Unified CCX users use this feature to set up a persistent call connection to remote destination. The
                                    advantage of this connection is that call establishment to the remote destination is much faster.

For information about Extend and Connect feature, see Features and Services Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/10_0_1/ccmfeat/CUCM_BK_F3AC1C0F_00_cucm-features-services-guide-100/CUCM_BK_F3AC1C0F_00_cucm-features-services-guide-100_chapter_010111.html .

For more information about remote destination, see Cisco Unified Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

### Server
                           	 Configuration

To use the Extend
                                 		  and Connect, follow these server configuration steps:

Step 1

Perform the
                                          			 preinstallation tasks for IM and Presence nodes.

Step 2

Configure the
                                          			 Cisco IM and Presence node details on Call Manager before you install Cisco IM
                                          			 and Presence. From Cisco Unified CM Administration on the publisher node,
                                          			 choose System > Server > Server
                                                				  Type and then choose CUCM IM and
                                             				Presence .

For information about server setup, see the Cisco Unified
                                                      				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 3

Install Cisco
                                          			 IM and Presence as a Call Manager subscriber.

Step 4

Activate and
                                          			 start all the Cisco IM and Presence services in Cisco Unified
                                             				Serviceability .

Step 5

Create
                                          			 Presence Redundancy groups in Call Manager.

Choose System > Presence Redundancy
                                                      						Groups > Add New .

Select
                                                				  Cisco IM and Presence, which you installed from the Presence
                                                   					 Server drop-down list.

Step 6

Create UC
                                          			 services for CTI and IM Presence services in Call Manager.

Step 7

Set up the
                                          			 service profile in Call Manager.

Step 8

Set up the end
                                          			 user in Call Manager.

Perform the
                                             				following steps:

Navigate
                                                				  to User
                                                      						Management > End User .

Click the
                                                				  User ID that you want to set up.

In the Service
                                                   					 Settings section, select Enable User for Unified CM IM and Presence (Configure IM and
                                                   					 Presence in the associated UC Service Profile) and then in UC
                                                   					 Service Profile , select the profile that you created.

In the Mobile Information section, select Enable Mobility .

In Permission
                                                   					 Information , add Standard CCM End user and Standard CTI enabled .

Navigate
                                                				  to User
                                                      						Management > Assign Presence End Users.

Click the
                                                				  User ID that you want to set up and then choose Assign Selected Users .

Step 9

Set up the
                                          			 trunk in Call Manager.

Step 10

Add the route
                                          			 pattern in Call Manager to route the calls to the remote device.

Step 11

Configure the
                                          			 Presence Gateway configuration on IM and Presence.

### Persistent
                           	 Connection

Unified CCX makes
                                 		  a persistent connection call to the agent's remote phone when an agent logs in
                                 		  to the agent desktop.

After establishing
                                 		  the persistent connection, the call remains connected until the Maximum Call
                                 		  Duration timer expires or until the agent logs out, provided that no other
                                 		  problems occur in the remote destination network. You must specify to match the
                                 		  time on the Maximum Call Duration timer with your company shift time or specify
                                 		  more than your company shift time. If the persistent connection gets
                                 		  disconnected, it retries until the connection is established.

#### Add Customized
                                 		  Announcement for Persistent Connection Call

When an agent
                                 		  answers persistent connection call, make an announcement to the agent
                                 		  indicating that the persistent connection must be retained so that further
                                 		  calls from or to customers are established over persistent connection.

If the agent's
                                 		  remote device supports Caller ID display, it displays EC
                                    			 Mode as the caller name, which indicates a persistent connection
                                 		  call.

By default, the
                                 		  Cisco Unified Communications Manager has announcements created. Unified CCX,
                                 		  through JTAPI communication to Cisco Unified Communications Manager, calls the
                                 		  announcement ID UCCX Persistent
                                    			 Connection Prompt . You must create the UCCX Persistent
                                    			 Connection Prompt customized announcement ID.

To add the customized announcement ID, see the"Upload customized announcement" procedure in the Cisco Unified
                                          				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . Enter UCCX Persistent Connection Prompt in the Announcement Identifier field.

Add a customized prompt to the created UCCX Persistent Connection Prompt, click Upload Files and select the desired prompt (.wav file).

When the announcement is played, the Caller ID information on agent's remote phone changes to Voice Connect .

If no announcement ID is created, Cisco Unified Communications Manager does not play any announcement to the agent when the
                                                   persistent call is answered.

#### Incoming Call
                                 		  Notification

An agent can
                                 		  configure a sound alert to notify an incoming call when the customer calls are
                                 		  routed through Persistent Connection Calls of the agents.

To receive the
                                 		  sound alert, in Cisco Unified Communications Manager, configure the
                                 		  Announcement ID as UCCX Customer
                                    			 Call Prompt . When the Announcement ID is configured, Unified CCX plays the
                                 		  announcement before the call is routed to a desktop. If you do not configure an
                                 		  Announcement ID, Unified CCX does not play an announcement, and then the agent
                                 		  relies on desktop signal for an incoming call.

## Server Configuration

To use the Extend and Connect, follow these server configuration steps:

Step 1

Perform the preinstallation tasks for IM and Presence nodes.

Step 2

Configure the Cisco IM and Presence node details on Call Manager before you install Cisco IM and Presence. From Cisco Unified
                                       CM Administration on the publisher node, choose System > Server > Server Type and then choose CUCM IM and Presence .

For information about the server setup, see "Manage the Server" in Cisco Unified
                                                   				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 3

Install Cisco IM and Presence as a Call Manager subscriber.

Step 4

Activate and start all the Cisco IM and Presence services in Cisco Unified Serviceability .

Step 5

Create Presence Redundancy groups in Call Manager.

Choose System > Presence Redundancy Groups > Add New .

Select Cisco IM and Presence, which you installed from the Presence Server drop-down list.

Step 6

Create UC services for CTI and IM Presence services in Call Manager.

Step 7

Set up the service profile in Call Manager.

Step 8

Set up the end user in Call Manager.

Perform the following steps:

Navigate to User Management > End User .

Click the User ID that you want to set up.

In the Service Settings section, select Enable User for Unified CM IM and Presence (Configure IM and Presence in the associated UC Service Profile) and then in UC Service Profile , select the profile that you created.

In the Mobile Information section, select Enable Mobility .

In Permission Information , add Standard CCM End user and Standard CTI enabled .

Navigate to User Management > Assign Presence End Users.

Click the User ID that you want to set up and then choose Assign Selected Users .

Create a CTI Remote Device.

Associate Jabber and CTI Remote device to end user.

Associate the CTI Remote device to UCCX RmCm application user.

Step 9

Set up the trunk in Call Manager.

Step 10

Add the route pattern in Call Manager to route the calls to the remote device.

Step 11

Configure the Presence Gateway configuration on IM and Presence.

### Example

For an example about how to configure Extend and Connect for Unified CCX, see https://www.cisco.com/c/en/us/support/docs/contact-center/unified-contact-center-express/215536-configure-extend-and-connect-feature-for.html .

## Persistant Connection

Unified CCX makes a persistent connection call to the agent's remote phone when an agent logs in to the agent desktop.

After establishing the persistent connection, the call remains connected until the Maximum Call Duration timer expires or
                              until the agent logs out, provided that no other problems occur in the remote destination network. You must specify to match
                              the time on the Maximum Call Duration timer with your company shift time or specify more than your company shift time. If
                              the persistent connection gets disconnected, it retries until the connection is established.

### Add Customized Announcement for Persistent Connection Call

When an agent answers persistent connection call, make an announcement to the agent indicating that the persistent connection
                              must be retained so that further calls from or to customers are established over persistent connection.

If the agent's remote device supports Caller ID display, it displays EC Mode as the caller name, which indicates a persistent connection call.

By default, the Cisco Unified Communications Manager has announcements created. Unified CCX, through JTAPI communication to
                              Cisco Unified Communications Manager, calls the announcement ID UCCX Persistent Connection Prompt . You must create the UCCX Persistent Connection Prompt customized announcement ID.

To add the customized announcement ID, see "Media Resources" in the Cisco Unified
                                       				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Enter UCCX Persistent Connection Prompt in the Announcement Identifier field.

Add a customized prompt to the created UCCX Persistent Connection Prompt, click Upload Files and select the desired prompt (.wav file).

When the announcement is played, the Caller ID information on agent's remote phone changes to Voice Connect .

If no announcement ID is created, Cisco Unified Communications Manager does not play any announcement to the agent when the
                                                persistent call is answered.

### Incoming Call Notification

An agent can configure a sound alert to notify an incoming call when the customer calls are routed through Persistent Connection
                              Calls of the agents.

To receive the sound alert, in Cisco Unified Communications Manager, configure the Announcement ID as UCCX Customer Call Prompt . When the Announcement ID is configured, Unified CCX plays the announcement before the call is routed to a desktop. If you
                              do not configure an Announcement ID, Unified CCX does not play an announcement, and then the agent relies on desktop signal
                              for an incoming call.

| Step 1 | Perform the
                                          			 preinstallation tasks for IM and Presence nodes. See "Perform pre-installation tasks for IM and Presence nodes" section in Installing Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
|---|---|
| Step 2 | Configure the
                                          			 Cisco IM and Presence node details on Call Manager before you install Cisco IM
                                          			 and Presence. From Cisco Unified CM Administration on the publisher node,
                                          			 choose System > Server > Server
                                                				  Type and then choose CUCM IM and
                                             				Presence . For information about server setup, see the Cisco Unified
                                                      				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 3 | Install Cisco
                                          			 IM and Presence as a Call Manager subscriber. For information about Cisco IM and Presence installation, see Installing Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
| Step 4 | Activate and
                                          			 start all the Cisco IM and Presence services in Cisco Unified
                                             				Serviceability . For information about activating services, see the "Activate services" section in Installing Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
| Step 5 | Create
                                          			 Presence Redundancy groups in Call Manager. Choose System > Presence Redundancy
                                                      						Groups > Add New . Select
                                                				  Cisco IM and Presence, which you installed from the Presence
                                                   					 Server drop-down list. For information about the Presence redundancy group setup, see the "Presence redundancy group setup" section in Cisco Unified
                                                         				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 6 | Create UC
                                          			 services for CTI and IM Presence services in Call Manager. Note You must select CTI and IM Presence services. For information about creating UC services, see the "Add CTI service" section in Cisco Unified
                                                   				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . | Note | You must select CTI and IM Presence services. |
| Note | You must select CTI and IM Presence services. |
| Step 7 | Set up the
                                          			 service profile in Call Manager. Note You must specify CTI and IM Presence service that you created in step 6. For information about Service profile setup, see the "Service profile setup" section in Cisco Unified
                                                   				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . | Note | You must specify CTI and IM Presence service that you created in step 6. |
| Note | You must specify CTI and IM Presence service that you created in step 6. |
| Step 8 | Set up the end
                                          			 user in Call Manager. Perform the
                                             				following steps: Navigate
                                                				  to User
                                                      						Management > End User . Click the
                                                				  User ID that you want to set up. In the Service
                                                   					 Settings section, select Enable User for Unified CM IM and Presence (Configure IM and
                                                   					 Presence in the associated UC Service Profile) and then in UC
                                                   					 Service Profile , select the profile that you created. In the Mobile Information section, select Enable Mobility . In Permission
                                                   					 Information , add Standard CCM End user and Standard CTI enabled . Navigate
                                                				  to User
                                                      						Management > Assign Presence End Users. Click the
                                                				  User ID that you want to set up and then choose Assign Selected Users . |
| Step 9 | Set up the
                                          			 trunk in Call Manager. For information about the Trunk setup, see the "Trunk setup" section in Cisco Unified
                                                   				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 10 | Add the route
                                          			 pattern in Call Manager to route the calls to the remote device. For information about route pattern setup, see the "Route pattern setup" section in Cisco Unified
                                                   				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 11 | Configure the
                                          			 Presence Gateway configuration on IM and Presence. For information about configuring Presence Gateway on IM and Presence, see the "Configure Presence Gateway configuration on
                                          IM and Presence" section in Cisco Unified
                                                   				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |

| Note | You must select CTI and IM Presence services. |
|---|---|

| Note | You must specify CTI and IM Presence service that you created in step 6. |
|---|---|

| Note | The agent must
                                          		  first answer the persistent connection call and then change the status to Ready
                                          		  in the agent desktop to answer the incoming call. |
|---|---|

| Note | Add a customized prompt to the created UCCX Persistent Connection Prompt, click Upload Files and select the desired prompt (.wav file). When the announcement is played, the Caller ID information on agent's remote phone changes to Voice Connect . If no announcement ID is created, Cisco Unified Communications Manager does not play any announcement to the agent when the
                                                   persistent call is answered. |
|---|---|

| Note | Configure UCCX Customer
                                             			 Call Prompt in the English language in Cisco Unified Communications
                                          		  Manager. |
|---|---|

| Step 1 | Perform the preinstallation tasks for IM and Presence nodes. See "Preinstall Tasks for the IM and Presence Service" section in Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
|---|---|
| Step 2 | Configure the Cisco IM and Presence node details on Call Manager before you install Cisco IM and Presence. From Cisco Unified
                                       CM Administration on the publisher node, choose System > Server > Server Type and then choose CUCM IM and Presence . For information about the server setup, see "Manage the Server" in Cisco Unified
                                                   				  Communications Manager Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 3 | Install Cisco IM and Presence as a Call Manager subscriber. For information about Cisco IM and Presence installation, see "Installation Tasks" in Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
| Step 4 | Activate and start all the Cisco IM and Presence services in Cisco Unified Serviceability . For information about activating services, see the "Configure the IM and Presence Publisher" section in Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
| Step 5 | Create Presence Redundancy groups in Call Manager. Choose System > Presence Redundancy Groups > Add New . Select Cisco IM and Presence, which you installed from the Presence Server drop-down list. For information about the Presence redundancy group setup, see the "Configure Presence Redundancy Groups" section in System Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html . |
| Step 6 | Create UC services for CTI and IM Presence services in Call Manager. Note You must select CTI and IM Presence services. For information about creating UC services, see the "Add CTI service" section in System Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html . | Note | You must select CTI and IM Presence services. |
| Note | You must select CTI and IM Presence services. |
| Step 7 | Set up the service profile in Call Manager. Note You must specify CTI and IM Presence service that you created in step 6. For information about the Service profile setup, see the "Configure Service Profile" section in System Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html . | Note | You must specify CTI and IM Presence service that you created in step 6. |
| Note | You must specify CTI and IM Presence service that you created in step 6. |
| Step 8 | Set up the end user in Call Manager. Perform the following steps: Navigate to User Management > End User . Click the User ID that you want to set up. In the Service Settings section, select Enable User for Unified CM IM and Presence (Configure IM and Presence in the associated UC Service Profile) and then in UC Service Profile , select the profile that you created. In the Mobile Information section, select Enable Mobility . In Permission Information , add Standard CCM End user and Standard CTI enabled . Navigate to User Management > Assign Presence End Users. Click the User ID that you want to set up and then choose Assign Selected Users . Create a CTI Remote Device. Associate Jabber and CTI Remote device to end user. Associate the CTI Remote device to UCCX RmCm application user. |
| Step 9 | Set up the trunk in Call Manager. For information about the Trunk setup, see the "Configure Cisco Unified Communications Manager for IM and Presence Service"
                                       section in Configuration and Administration of the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html . |
| Step 10 | Add the route pattern in Call Manager to route the calls to the remote device. For information about the route pattern setup, see the "Configure Advanced Routing" section in Configuration and Administration of the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html . |
| Step 11 | Configure the Presence Gateway configuration on IM and Presence. For information about configuring Presence Gateway on IM and Presence, see the "Configure the Presence Gateway" section in Configuration and Administration of the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html . |

| Note | You must select CTI and IM Presence services. |
|---|---|

| Note | You must specify CTI and IM Presence service that you created in step 6. |
|---|---|

| Note | The agent must first answer the persistent connection call and then change the status to Ready in the agent desktop to answer
                                       the incoming call. |
|---|---|

| Note | Add a customized prompt to the created UCCX Persistent Connection Prompt, click Upload Files and select the desired prompt (.wav file). When the announcement is played, the Caller ID information on agent's remote phone changes to Voice Connect . If no announcement ID is created, Cisco Unified Communications Manager does not play any announcement to the agent when the
                                                persistent call is answered. |
|---|---|

| Note | Configure UCCX Customer Call Prompt in the English language in Cisco Unified Communications Manager. |
|---|---|