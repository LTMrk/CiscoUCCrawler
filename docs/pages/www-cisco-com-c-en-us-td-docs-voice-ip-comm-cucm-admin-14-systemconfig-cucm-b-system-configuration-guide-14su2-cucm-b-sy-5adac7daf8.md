---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14-systemconfig-cucm-b-system-configuration-guide-14su2-cucm-b-sy-5adac7daf8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14/systemConfig/cucm_b_system-configuration-guide-14su2/cucm_b_system-configuration-guide-14_chapter_011000.html
retrieved_at: 2026-08-16T16:33:19.412148+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: August 7, 2026

Chapter: Integrate Cisco Applications

## Chapter: Integrate Cisco Applications

# Integrate Cisco Applications

## Cisco Unity Connection

As you start configuring your voicemail and messaging system, be aware of the options that you have for adding users, enabling
                           features, and integrating Cisco Unified Communications Manager with Cisco Unity Connection.

When integrated with Cisco Unified Communications Manager, Cisco Unity Connection (the voicemail and messaging system) provides
                           voice-messaging features for users that you configure manually, through AXL services, or through LDAP integration. After receiving
                           voice messages in their mailboxes, users receive message-waiting lights on their phones. Users can retrieve, listen to, reply
                           to, forward, and delete their messages by accessing the voice-messaging system with an internal or external call.

Your system supports both directly connected and gateway-based messaging systems. Directly connected voice-messaging systems
                           communicate with Cisco Unified Communications Manager by using a packet protocol. A gateway-based voice-messaging system connects
                           to Cisco Unified Communications Manager through analog or digital trunks that then connect to Cisco gateways.

Call forward to personal greeting

Call forward to busy greeting

Caller ID

Easy message access (a user can retrieve messages without entering an ID; Cisco Unity Connection identifies a user based on
                                    the extension from which the call originated; a password may be required)

Identified user messaging (Cisco Unity Connection automatically identifies a user who leaves a message during a forwarded
                                    internal call, based on the extension from which the call originated)

Message waiting indication (MWI)

The configuration of a secure SIP trunk integration between a Cisco Unified Communications Manager and Cisco Unity Connection
                                    server requires that the Cisco Unified Communications Manager cluster is configured in mixed mode.

Cisco Unified Communications Manager interacts with Cisco Unity Connection through one of the following interfaces:

SIP Trunk—You can integrate Cisco Unity Connection and Unified Communications Manager by using SIP. Instead of multiple SCCP
                                 ports involved with traditional integrations, SIP uses a single trunk per Unity Connection server. The SIP integration eliminates
                                 the requirement to configure directory numbers for Voicemail Ports and message-waiting indicators (MWI).

SCCP Protocol—You configure the interface to directly connected voice-messaging systems by creating voicemail ports. These
                                 establish a link between Unified Communications Manager and Cisco Unity Connection.

To handle multiple, simultaneous calls to a voice-messaging system, you create multiple voicemail ports and place the ports
                                 in a line group and the line group in a route/hunt list.

Cisco Unified Communications Manager generates SCCP messages, which are translated by Cisco Unity Connection. The voicemail
                                 system sends message-waiting indications (MWIs) by calling a message-waiting on and off number.

When you configure security for voicemail ports and Cisco Unity SCCP devices, a TLS connection (handshake) opens for authenticated
                                 devices after each device accepts the certificate of the other device; likewise, the system sends SRTP streams between devices;
                                 that is, if you configure the devices for encryption.

When the device security mode is set to authenticated or encrypted, the Cisco Unity TSP connects to Cisco Unified Communications
                                 Manager through the Unified Communications Manager TLS port. When the security mode is nonsecure, the Cisco Unity TSP connects
                                 to Cisco Communications Manager through the Unified Communications Manager SCCP port.

For more information about configuring Cisco Unity Connection to integrate with your system, see the Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection or the Cisco Unified Communications Manager SIP Trunk Integration Guide for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html .

### Enable PIN
                           	 Synchronization

Use this procedure to enable PIN synchronization so that the end users can log in to Extension Mobility, Conference Now, Mobile
                                 Connect, and the Cisco Unity Connection Voicemail using the same PIN.

The pin synchronization between Cisco Unity Connection and Cisco Unified Communications Manager is
                                             			 successful, only when Cisco Unified Communications Manager publisher
                                             			 database server is running and completes its database replication. Following
                                             			 error message is displayed when the pin synchronization fails on Cisco Unity
                                             			 Connection: Failed to update PIN on CUCM. Reason: Error getting the
                                                				pin.

If the PIN Synchronization is enabled and the end user changes the pin, then pin is updated in Cisco Unified Communications Manager . This happens only when the pin update is successful in at least one of the configured Unity Connection Application servers.

For PIN Synchronization to take effect, administrators must force the users to change their PIN after successfully enabling
                                             the feature.

#### Before you begin

This procedure assumes that you already have your application server connection to Cisco Unity Connection setup. If not, for
                                 more information on how to add a new application server, see the Related Topics section.

To enable PIN Synchronization feature, you need to first upload a valid certificate for the Cisco Unity Server connection
                                 from the Cisco Unified OS Administration page to the Cisco Unified Communications Manager tomcat-trust. For more information
                                 on how to upload the certificate, see the "Manage Security Certificates" chapter in the Administration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

The user ID in the Cisco
                                    			 Unity Connection Server must match the user ID in Cisco
                                    			 Unified Communications Manager .

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Application
                                                				  Servers .

Step 2

Select the
                                          			 application server that you set up for Cisco
                                             				Unity Connection .

Step 3

Check the Enable
                                             				End User PIN Synchronization check box.

Step 4

Click Save .

## Cisco Expressway

Cisco Unified Communications Manager integrates with Cisco Expressway to provide Cisco Unified Communications Mobile and Remote
                              Access. Cisco Unified Communications Mobile and Remote Access is a core part of the Cisco Collaboration Edge Architecture.
                              It allows endpoints such as Cisco Jabber to have their registration, call control, provisioning, messaging and presence services
                              provided by Cisco Unified Communications Manager (Unified CM) when the endpoint is not within the enterprise network. The
                              Expressway provides secure firewall traversal and line-side support for Unified CM registrations.

The overall solution provides the following functions:

Off-premises access—A consistent experience outside the network for Cisco Jabber and EX/MX/SX Series clients

Security—Secure business-to-business communications

Cloud services—Enterprise grade flexibility and scalable solutions providing rich Webex integration and Service Provider offerings

Gateway and interoperability services—Media and signaling normalization, and support for non-standard endpoints.

For deployment details, refer to the Mobile and Remote Access Through Cisco Expressway Deployment Guide at https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html .

## Cisco Emergency Responder

Cisco Emergency Responder (Emergency Responder) helps you manage emergency calls in your telephony network so that you can
                              respond to these calls effectively and so that you can comply with local ordinances concerning the handling of emergency calls.
                              In North America, these local ordinances are called “enhanced 911,” or E911. Other countries and locales have similar ordinances.

Because emergency call ordinances can differ from location to location within a country, region, state, or even metropolitan
                              area, Emergency Responder gives you the flexibility to configure your emergency call configuration to specific local requirements.
                              However, ordinances differ from location to location, and security requirements differ from company to company, so you must
                              research your security and legal needs before deploying Emergency Responder.

For details on how to install Cisco Emergency Responder and integrate it with Cisco Unified Communications Manager, refer
                              to Cisco Emergency Responder Administration Guide at https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/products-maintenance-guides-list.html

### Feature Support from Cisco Unified Communications Manager

The following Cisco Unified Communications Manager features support integrations with Cisco Emergency Responder. For details
                              on how to configure these features on Cisco Unified Communications Manager, refer to the Feature Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

Location Awareness

Emergency Handler

## Cisco Paging Server

Cisco Unified Communications Manager can be configured to integrate with Cisco Paging Server to provide basic paging services
                              for Cisco IP Phones and a variety of endpoints. The Cisco Paging Server product is offered through the InformaCast Virtual
                              Appliance and offers the following deployment options:

Basic Paging—Provides phone-to-phone and group live audio paging to Cisco IP Phones. All users of the system can participate
                                    in making and receiving basic pages.

Advanced Notifications—Provides a full-featured emergency notification solution that gives you the ability to reach an unlimited
                                    number of phones with text and live or pre-recorded audio messages

For more information and documentation on Cisco Paging Server, see https://www.cisco.com/c/en/us/products/unified-communications/paging-server/index.html .

### Configuration

For details on how to configure Cisco Unified Communications Manager for Basic Paging or Advanced Notifications, see the "Paging"
                              chapter of the Feature Configuration Guide for Cisco Unified Communications Manager .

## Cisco Unified Contact Center Enterprise

You can use Cisco Unified Contact Center Enterprise (Unified CCE) in your system to integrate intelligent call routing, network-to-desktop
                           computer telephony integration (CTI), and multichannel contact management to contact center agents over an IP network. Unified
                           CCE combines software IP automatic call distribution (ACD) with Cisco Unified Communications so that you can rapidly deploy
                           an advanced, distributed contact center.

For detailed tasks about how to configure Unified CCE to integrate with your system, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

## Cisco Unified Contact Center Express

Cisco Unified Contact Center Express (Unified CCX) provides your system with the features of a large contact center packaged
                           into a single- or dual-server deployment. Unified CCX scales up to 400 concurrent agents, 42 supervisors, 150 agent groups,
                           and 150 skill groups. It includes email, chat, outbound calling, inbound calling, workforce optimization, and reporting.

Unified CCX works with Unified Communications Manager , which manages all contact center calls on behalf of Unified CCX. When a call is placed to your help desk, your call system
                           recognizes that the number is destined for the Unified CCX application server. With this configuration, Unified CCX receives
                           the incoming call and handles the request based on the extension number that was dialed. The script plays prompts, collects
                           digits and, if necessary, uses the information from the caller to select an appropriate agent. If an assigned agent is not
                           available, the call is put into an appropriate queue and a recorded message or music is streamed to the caller. As soon as
                           an agent is available, Unified CCX instructs Unified Communications Manager to call the agent’s phone.

When the agent picks up, relative call context is provided in the agent’s desktop application. This step ensures that agents
                           have the proper information in front of them to support the customer.

For detailed tasks about how to configure Unified CCX to integrate with your system, see the Cisco Unified CCX Administration Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html .

## Advanced QoS APIC-EM Controller

The APIC-EM Controller provides a centralized system for managing network traffic so that you always have the bandwidth to
                              maintain communications, even in congested networks. You can configure Cisco Unified Communications Manager to use the APIC-EM
                              Controller to manage SIP media flows thereby providing the following benefits:

Centralizes QoS management, thereby eliminating the need for endpoints to assign DSCP values.

Applies differential QoS treatment for different media flows. For example, you can prioritize audio over video to ensure that
                                    basic audio communication is always maintained, even when network bandwidth is low.

External QoS setting in the SIP Profile allows you to target which users will use the APIC-EM. For example, you may have Cisco
                                    Jabber users use the APIC-EM to manage media flows, while Cisco Unified IP Phone users use the DSCP settings in Cisco Unified
                                    Communications Manager.

### Configuration Details

For additional details, including information on how to configure Cisco Unified Communications Manager to integrate with an
                              APIC_EM Controller, refer to the "Configure QoS with APIC-EM Controller" chapter of the Feature Configuration Guide for Cisco Unified Communications Manager .

## Configure Cisco WebDialer Servers

Configure Cisco WebDialer application servers as an alternative to the List of WebDialers service parameter, which limits the number of characters that you can enter. After you add a Cisco WebDialer application
                              server in the Application Server Configuration window, the server appears in the List of WebDialers field in the Service Parameter Configuration window for the Cisco WebDialer Web Service. For complete details about configuring Cisco WebDialer, see the Feature Configuration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

Step 1

From Cisco Unified CM Administration, choose System > Application Server .

Step 2

Click Add New .

Step 3

From the Application Server Type drop-down list, choose Cisco Web Dialer , and then click Next .

Step 4

In the Hostname or IP Address field, enter the hostname or IP address of the WebDialer server.

Step 5

From the Redirector Node drop-down list, choose < None > or a specific Unified Communications Manager node.

< None > indicates the WebDialer Server would apply to all nodes.

Step 6

Click Save .

Step 7

From Cisco Unified Serviceability, choose Tools > Control Center - Feature Services

Step 8

Click the Cisco WebDialer Web Service radio button.

Step 9

Click Restart .

| Note | The pin synchronization between Cisco Unity Connection and Cisco Unified Communications Manager is
                                             			 successful, only when Cisco Unified Communications Manager publisher
                                             			 database server is running and completes its database replication. Following
                                             			 error message is displayed when the pin synchronization fails on Cisco Unity
                                             			 Connection: Failed to update PIN on CUCM. Reason: Error getting the
                                                				pin. |
|---|---|

| Note | For PIN Synchronization to take effect, administrators must force the users to change their PIN after successfully enabling
                                             the feature. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Application
                                                				  Servers . |
|---|---|
| Step 2 | Select the
                                          			 application server that you set up for Cisco
                                             				Unity Connection . |
| Step 3 | Check the Enable
                                             				End User PIN Synchronization check box. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Application Server . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Application Server Type drop-down list, choose Cisco Web Dialer , and then click Next . |
| Step 4 | In the Hostname or IP Address field, enter the hostname or IP address of the WebDialer server. |
| Step 5 | From the Redirector Node drop-down list, choose < None > or a specific Unified Communications Manager node. < None > indicates the WebDialer Server would apply to all nodes. |
| Step 6 | Click Save . |
| Step 7 | From Cisco Unified Serviceability, choose Tools > Control Center - Feature Services |
| Step 8 | Click the Cisco WebDialer Web Service radio button. |
| Step 9 | Click Restart . |