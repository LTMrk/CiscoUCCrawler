---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-abc3d1736a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0110011.html
retrieved_at: 2026-08-16T17:33:05.361436+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Cisco Unity Connection for Voicemail and Messaging

## Chapter: Configure Cisco Unity Connection for Voicemail and Messaging

# Configure Cisco Unity Connection for Voicemail and Messaging

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

## Cisco Unity
                        	 Connection for Voicemail and Messaging Configuration Task Flow

Step 1

Configure Cisco Unity Connection for Voicemail and
                                       			 messaging.

To configure Cisco Unity Connection , see the Cisco Unified Communications Manager SCCP Integration
                                             				  Guide for Cisco Unity Connection or the Cisco Unified Communications Manager SIP Trunk Integration
                                             				  Guide for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html

Step 2

Enable PIN Synchronization

Optional. Use this procedure to enable a common PIN
                                          				synchronization so that

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

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Cisco Unity Connection for Voicemail and
                                       			 messaging. | To configure Cisco Unity Connection , see the Cisco Unified Communications Manager SCCP Integration
                                             				  Guide for Cisco Unity Connection or the Cisco Unified Communications Manager SIP Trunk Integration
                                             				  Guide for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-and-configuration-guides-list.html |
| Step 2 | Enable PIN Synchronization | Optional. Use this procedure to enable a common PIN
                                          				synchronization so that |

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