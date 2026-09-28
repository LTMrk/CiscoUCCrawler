---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-features-guide-uccx-b-125-ab6d64fa18
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/features/guide/uccx_b_1251su1features-guide/uccx_b_1252features-guide_chapter_0110.html
retrieved_at: 2026-08-16T21:19:14.758077+00:00
---

Cisco Unified Contact Center Express Features Guide, Release 12.5.1 SU1

# Cisco Unified Contact Center Express Features Guide, Release 12.5.1 SU1

Updated: February 1, 2021

Chapter: Desktop Chat

## Chapter: Desktop Chat

# Desktop Chat

## Desktop Chat

Desktop Chat is a XMPP browser based chat, which is powered by Cisco Instant Messaging and Presence (IM&P) service. Desktop
                              Chat allows agents, supervisors, and Subject Matter Experts (SMEs) within the organization to chat with each other.

For more details see, https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html .

Instant Messaging and Presence (IM&P) provides presence and chat capabilities within the Unified CM platform. The Desktop
                              Chat interface is hosted by the Finesse Agent desktop and requires a separate log in to the IM&P service.

Desktop Chat does not support Cisco Mobile Remote Agent /VPN based access to the IM&P server. Desktop Chat requires direct
                                          access to the IM&P server to connect to the chat service.

## Cisco Instant Messaging and Presence (IM&P)

IM&P incorporates the Jabber platform and supports XMPP protocol and can track the user's presence via multiple devices. IM&P
                              pulls its user list from users who have been enabled for chat capabilities, from Unified CM (or LDAP if LDAP integration is
                              enabled). Only Unified CM users enabled for chat capability can login to IM&P.

### Identity, Presence, Jabber

A User is identified in the IM&P service with a unique identity which is in the form of username@FQDN.com .

A user is described in terms of the identity of the user, presence status, (available, unavailable, or busy) and the presence
                              capabilities of the user.

The presence status of the user is not related to the Agent Status and has to be managed independently by the user post login.

Cisco IM&P service combines the presence status of user across multiple devices and publishes them for subscribers who have
                              added the contact in their contact list.

IM&P supports a composed presence for the users, which is derived from the state matrix of all the devices that the agent
                              is logged into. Cisco IM&P takes sources of presence from the XMPP client for the user, on-hook and off-hook status from CUCM,
                              and in a meeting status from Microsoft Exchange to generate the users overall composed presence. Desktop Chat displays the
                              composed presence of the user. For details about how to arrive at the composed presence, refer to the Cisco IM&P User Guide at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-user-guide-list.html .

Irrespective of the deployment type, the Desktop Chat requires an explicit login using the IM&P identity of the user after
                              logging into the Finesse Desktop.

SSO is not supported with Desktop Chat and thus an explicit login is required in SSO mode.

Desktop Chat presence indicates the availability of users to communicate across the configured devices.

Desktop Chat availability will also be reflected in the combined IM&P presence of the user.

Logging into Desktop Chat, by default sets the users state as available.

An agent logging into Desktop Chat can thus be seen as available in Jabber or other XMPP platforms connected with IM&P and
                              can communicate with these users.

File transfer is supported only for users communicating using Desktop Chat. For more information on the supported file types
                                          and the maximum size of file attachments see, Desktop Properties CLIs section in the Cisco Unified Contact Center Express Administration and Operations Guide .

Example for Desktop Chat availability:

A Desktop Chat user can be logged into the Desktop Chat and Jabber at the same time. Incoming chats will be relayed to all
                              the logged in clients including Desktop Chat. However, Desktop Chat does not support Multi-Device-Messaging. So messages being
                              sent from other XMPP clients like Jabber will not be displayed within the Desktop Chat. Once alternate clients are used to
                              respond to incoming chats, further messages are not shown in Desktop Chat until the user starts responding using the Desktop
                              Chat.

For more information on network designs, refer to the Solution Reference Network Design guide https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html .

## Cisco IM&P Deployment Considerations

Finesse is configured to the primary and secondary IM&P chat servers through the Cisco Finesse Administration interface.

Desktop Chat automatically discovers the appropriate IM&P node, configured for the user, by connecting to the configured servers
                              and connects to the appropriate nodes in IM&P. This resolution is only performed for the first time chat is loaded and subsequently
                              uses the same nodes, until the browser cache is cleared by the user.

Desktop Chat does not use DNS_SRV* records unlike Jabber and cannot automatically configure itself based on the network configurations.
                                          The explicit chat URI configuration from Administrative pages is required for chat server discovery.

For details on Cisco IM&P deployment, see Unified CM Solution Reference Network Design guide at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/srnd/collab12/collab12/presence.html .

See Configuration and Administration of the IM and Presence Service on Cisco Unified Communications Manager guide for details about the following:

How to install and configure IM&P services.

How to configure IM&P to enable chat services for end users.

How to configure clusters and high availability deployment.

How to configure IM&P Federation.

## Cisco IM&P Design Considerations

Finesse browser makes a separate connection to Cisco IM&P over HTTPS, after it retrieves the chat server URI from the Finesse
                              server. This requires separate certificates to be accepted if self-signed certificates are employed, in an HTTPS deployment.

The chat interaction happens over XMPP protocol, on the HTTP connection with long polling or BOSH established with Cisco IM&P.

There are no other interactions between Finesse server and browser for chat related capabilities, except for retrieving the
                              Cisco IM&P server configurations.

Chat log persistence is available with the browser during the desktop session.

User search capabilities require Unified CM LDAP integration. In its absence, remote contacts have to be manually added by
                              the user.

If the user is an existing Jabber user, the same contacts are shared between the Desktop Chat and Jabber which are also persisted
                              across sessions.

There are no limits on the number of ongoing chats or the contacts in Desktop Chat apart from the restrictions or guidelines
                              advised by Cisco IM&P. For the limit on the number of ongoing chats or the contacts and how to configure the Cisco IM&P server
                              for chat, see the IM&P Solution Reference Networking Guide .

Desktop Chat requires the Cisco IM and Presence certificates to be trusted. For more information on accepting certificates,
                                          see the Accept Security Certificates section, in the Common Tasks chapter of Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html .

## Bandwidth and Latency Considerations for Cisco IM&P

Cisco IM&P service is closely integrated with Unified CM and it depends on Unified CM for user management and service enabling
                              and authentication.

Cisco IM&P can be deployed as a cluster to guarantee availability and the users must be pre-configured to specific node pairs
                              within the cluster. Details of Cisco IM&P installation and cluster deployment can be found here https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html .

For more details on the latency requirements for IM&P server refer, Unified CM SRND at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html .

The maximum latency supported between Finesse and IM&P nodes is 200 ms.

## Cisco IM&P High Availability Considerations

Failover is supported for Desktop Chat and any Cisco IM&P node failure results in automatic connection to the node pair peer,
                              as configured for the user.

### Desktop Chat Failover

The following table lists the desktop chat failover scenarios:

Failover Type

Desktop Chat Behavior

Cisco IM&P server failover

The desktop chat status is retained, and all active chat sessions are lost.

Finesse service failover

The desktop chat status is retained, and all active chat sessions are lost.

Unified CCX server failover

The desktop chat status and all chat sessions are retained.

See  the Cisco Finesse Administration Guide for failover details with Desktop Chat.

## Desktop Chat Server Settings

Desktop Chat is an XMPP browser based chat, which is powered by Cisco Instant Messaging and Presence (IM&P) service. It provides
                              presence and chat capabilities within the Unified CM platform. For more details, see Configuration and Administration of the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

Desktop Chat connects to Cisco IM&P servers over port 5280 from the browser hosting the agent desktop. IM&P server visibility
                              and port accessibility needs to be ensured if clients intend to use this feature. The Desktop Chat gadget configures the IM&P
                              host BOSH URL’s used by the desktop to communicate with the IM&P server over BOSH HTTP.

IM&P has a clustered design, where users are distributed across multiple nodes in the cluster. The Desktop Chat initially
                              discovers the IM&P nodes that a user has configured, caches this information and communicates with the actual server for subsequent
                              login, until the browser cache is cleared. To spread the initial discovery load, it is advisable to configure the nodes in
                              a round robin fashion if the deployment has more than one Finesse cluster. For example, if there are 5 IM&P nodes configure
                              Finesse cluster A with node 1 & 2, Finesse cluster B with nodes 3 & 4, and so on.

Node availability should be considered while configuring the IM&P URL. The secondary node will be available for discovery
                              in scenarios where the first node is not reachable. The secondary node will be connected for discovery only if the primary
                              node is unreachable.

For the URL to be configured, refer Cisco Unified Presence Administration service, in System, Service Parameters . Choose the required IM&P server, select Cisco XCP Web Connection Manager. The URL binding path is listed against the field HTTP Binding Path . The full URL to be configured in Finesse is https://<hostname>:5280/URL-binding-path .

Use the Desktop Chat Server Settings to configure chat settings for the Finesse desktop. The following table describes the
                              fields on the Desktop Chat Server Settings gadget.

Field

Explanation

Primary Chat Server

Enter the IM&P primary server URL of Desktop Chat.

Secondary Chat Server

Enter the IM&P secondary server URL of Desktop Chat.

Save: Saves your configuration changes

Revert: Retrieves the most recently saved server settings

For Desktop Chat to work without any issues, ensure the following services are running on IM&P:

Cisco Presence Engine

Cisco XCP Text Conference Manager

Cisco XCP Web Connection Manager

Cisco XCP Connection Manager

Cisco XCP Directory Service

Cisco XCP Authentication Service

Cisco XCP File Transfer Manager

Desktop Chat requires the Cisco IM and Presence certificates to be trusted. To start the Desktop Chat without experiencing
                                          an exception, you must add the certificate to the browser trust store, or configure IM and Presence with CA-signed certificate,
                                          or push self-signed certificate through group policies in supported browsers. For more information on accepting certificates,
                                          see the Accept Security Certificates section, in the Common Tasks chapter of Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html .

For more information on adding certificates to the browser trust store, see Certificate Management.

## Use Desktop Chat

The Desktop Chat allows agents or supervisors to chat internally with other users on the Finesse desktop and with users outside
                              the contact center. The agent state on the Desktop Chat is different from the Voice or Digital Channels state.

For more details on how to sign in to Desktop Chat, managing contacts, groups, the chat window, how to change state for Desktop
                              Chat, and how to sign out of Desktop Chat see, Finesse Agent and Supervisor Desktop User Guide for Unified CCX .

### Sign In to Desktop Chat

In the Finesse desktop, click the Desktop Chat icon ( ).

Enter your username and password in the appropriate fields and click Sign In .

Click the certificate link. A new browser tab opens for the certificate that
                                          you must accept. A certificate error appears in the address bar.

If you are using self-signed certificates, you get the certificate acceptance
                                                      window.

To accept the certificates in Internet Explorer, refer to the section Accept Security Certificates > Step 2 > Substep d onward.

To accept the certificates in Firefox, refer to the section Accept
                                                      Security Certificates > Step 4 onwards.

To accept the certificates in Chrome and Edge
                                                      Chromium , refer to the section Accept Security
                                                      Certificates > Step 5 onwards.

The Accept Security Certificates topic is in the Cisco Finesse Agent and
                                                               Supervisor Desktop User Guide for Cisco Unified Contact Center
                                                               Express .

### Add Contact

If you have Cisco Jabber on your desktop, then the first time you sign in to Desktop Chat, you will see your Cisco Jabber
                                 contact list in the Desktop Chat window. If you do not have Cisco Jabber, your contact list will be empty.

To add a contact:

In the empty contact list, enter the agent name or ID in the Search field.

In the existing contact list, click the icon at the end of the group and click Add .

From the Recent Chats group, click the icon at the end of the required chat and click Add .

In the Add Contact window, you can choose to change the display name.

From the Add to Group drop-down, either choose an existing group or create a new group to add the contact.

Click Add .

### Edit Contact

In the Contact list, click the icon at the end of the required contact.

From the drop-down, click Edit .

In the Edit Contact window, modify the display name or the group.

While modifying the group for the contact, you can either add the contact to existing groups or create a new group.

Click Save .

### Move Contact

To move a single Contact:

Click the icon at the end of the required contact.

From the drop-down, click Move .

In the Select Destination window, select an existing group or create a new group.

Click Move .

To move multiple contacts:

Press and hold the Ctrl key and select the required contacts.

On the Contact list header, click Move .

In the Select Destination window, select existing groups or create a new group.

Click Move .

### Delete Contact

To delete a single contact:

In the Contact list, click the icon at the end of the required contact.

From the drop-down, click Delete .

In the confirmation prompt, click Delete to remove the contact from that group.

To delete multiple contacts:

Press and hold the Ctrl key and select the required contacts.

On the Contact list header, click Delete .

In the confirmation prompt, click Delete to remove the contact from that group.

### Edit Group

In the contact list, click the icon at the end of the required group.

From the drop-down list, click Edit .

In the Group window, modify the group name.

Click Save .

### Delete Group

In the Contact list, click the icon at the end of the required group.

From the drop-down, click Delete .

In the confirmation prompt, click Delete .

### Chat Window

When you receive an incoming chat request, a chat window pops up with the display name of the agent in the chat window header.
                                 If the Cisco Finesse desktop window or tab is inactive, Finesse displays a notification with the chat details. Click the toaster
                                 notification to restore the Cisco Finesse desktop.

You can move the chat window to any location on the screen but cannot maximize it to the full screen.

You can chat with agents logged in to the Desktop Chat. You cannot send messages to the signed out agents.

The Desktop Chat window provides the following functionalities:

Typing area: Type your message in the typing area. Right-click to perform basic clipboard operations.

The typing awareness indicator shows when the other participant is typing.

Multiple chats:

All agents are displayed in the chat tabs at the bottom of the chat window.

The chat tab area displays up to three active chats. To view more than three active chats, click the icon.

For each chat tab, the unread chat notification is shown in a badge next to the display name. The badge disappears when that
                                             chat tab is active.

When you hover over the status on any chat tab next to the display name, you get the option to close that chat tab.

Click the chat window header to minimize or maximize the chat window.

When minimized, the chat window header shows the total number of chats that have unread messages.

Click X on the chat window header and confirm to close all chats.

Chat history: The Desktop Chat window stores the chat history only for a particular session. If you sign out or the browser
                                       is refreshed or closed, the chat history is lost.

Resize chat window: Click the button on the chat window header to increase the chat window frame size and the button to restore the frame size.

Attachments:

The administrator should have enabled attachment support for you to send and receive attachments.

To send an attachment:

Click the Send a file button and navigate to the file you want to send.

Click OK .

When you receive an attachment, you are prompted to Accept and Decline the attachment. Click Accept to download the attachment or click Decline to reject it.

The file name and file size are displayed in the attachment header.

The attachments are downloaded in the downloads folder of the browser.

You cannot open the attachment from the chat window.

The supported file types and maximum attachment size are configured by your administrator.

You can send or receive attachments only from the users using Desktop Chat.

### Change Your Desktop Chat State

Click the drop-down arrow beside your current state in the Desktop Chat window.

Choose the appropriate state from the list.

If your status in set to Do Not Disturb and you receive a chat message, the message is displayed only if your chat window
                                             is active. If the chat window is closed or minimized, the Desktop Chat icon blinks and you will only see the minimized chat
                                             window header with the number of chat tabs that have unread messages.

### Sign Out of Desktop Chat

Click the drop-down arrow beside your current state in the Desktop Chat window

From the displayed list, click Sign Out .

| Note | Desktop Chat does not support Cisco Mobile Remote Agent /VPN based access to the IM&P server. Desktop Chat requires direct
                                          access to the IM&P server to connect to the chat service. |
|---|---|

| Note | File transfer is supported only for users communicating using Desktop Chat. For more information on the supported file types
                                          and the maximum size of file attachments see, Desktop Properties CLIs section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
|---|---|

| Note | Desktop Chat does not use DNS_SRV* records unlike Jabber and cannot automatically configure itself based on the network configurations.
                                          The explicit chat URI configuration from Administrative pages is required for chat server discovery. |
|---|---|

| Note | Desktop Chat requires the Cisco IM and Presence certificates to be trusted. For more information on accepting certificates,
                                          see the Accept Security Certificates section, in the Common Tasks chapter of Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html . |
|---|---|

| Failover Type | Desktop Chat Behavior |
|---|---|
| Cisco IM&P server failover | The desktop chat status is retained, and all active chat sessions are lost. |
| Finesse service failover | The desktop chat status is retained, and all active chat sessions are lost. |
| Unified CCX server failover | The desktop chat status and all chat sessions are retained. |

| Field | Explanation |
|---|---|
| Primary Chat Server | Enter the IM&P primary server URL of Desktop Chat. |
| Secondary Chat Server | Enter the IM&P secondary server URL of Desktop Chat. |

| Important | For Desktop Chat to work without any issues, ensure the following services are running on IM&P: Cisco Presence Engine Cisco XCP Text Conference Manager Cisco XCP Web Connection Manager Cisco XCP Connection Manager Cisco XCP Directory Service Cisco XCP Authentication Service Cisco XCP File Transfer Manager |
|---|---|

| Note | Desktop Chat requires the Cisco IM and Presence certificates to be trusted. To start the Desktop Chat without experiencing
                                          an exception, you must add the certificate to the browser trust store, or configure IM and Presence with CA-signed certificate,
                                          or push self-signed certificate through group policies in supported browsers. For more information on accepting certificates,
                                          see the Accept Security Certificates section, in the Common Tasks chapter of Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html . For more information on adding certificates to the browser trust store, see Certificate Management. |
|---|---|

| Step 1 | In the Finesse desktop, click the Desktop Chat icon ( ). |
|---|---|
| Step 2 | Enter your username and password in the appropriate fields and click Sign In . |
| Step 3 | Click the certificate link. A new browser tab opens for the certificate that
                                          you must accept. A certificate error appears in the address bar. Note If you are using self-signed certificates, you get the certificate acceptance
                                                      window. To accept the certificates in Internet Explorer, refer to the section Accept Security Certificates > Step 2 > Substep d onward. To accept the certificates in Firefox, refer to the section Accept
                                                      Security Certificates > Step 4 onwards. To accept the certificates in Chrome and Edge
                                                      Chromium , refer to the section Accept Security
                                                      Certificates > Step 5 onwards. Note The Accept Security Certificates topic is in the Cisco Finesse Agent and
                                                               Supervisor Desktop User Guide for Cisco Unified Contact Center
                                                               Express . | Note | If you are using self-signed certificates, you get the certificate acceptance
                                                      window. | Note | The Accept Security Certificates topic is in the Cisco Finesse Agent and
                                                               Supervisor Desktop User Guide for Cisco Unified Contact Center
                                                               Express . |
| Note | If you are using self-signed certificates, you get the certificate acceptance
                                                      window. |
| Note | The Accept Security Certificates topic is in the Cisco Finesse Agent and
                                                               Supervisor Desktop User Guide for Cisco Unified Contact Center
                                                               Express . |

| Note | If you are using self-signed certificates, you get the certificate acceptance
                                                      window. |
|---|---|

| Note | The Accept Security Certificates topic is in the Cisco Finesse Agent and
                                                               Supervisor Desktop User Guide for Cisco Unified Contact Center
                                                               Express . |
|---|---|

| Step 1 | To add a contact: In the empty contact list, enter the agent name or ID in the Search field. Note When you enter the text to search, the Search field pre populates relevant results in a drop-down. From the results list,
                                                            hover over the required contact and click the icon. In the existing contact list, click the icon at the end of the group and click Add . From the Recent Chats group, click the icon at the end of the required chat and click Add . | Note | When you enter the text to search, the Search field pre populates relevant results in a drop-down. From the results list,
                                                            hover over the required contact and click the icon. |
|---|---|---|---|
| Note | When you enter the text to search, the Search field pre populates relevant results in a drop-down. From the results list,
                                                            hover over the required contact and click the icon. |
| Step 2 | In the Add Contact window, you can choose to change the display name. |
| Step 3 | From the Add to Group drop-down, either choose an existing group or create a new group to add the contact. |
| Step 4 | Click Add . The contact is added to your existing or newly created group. |

| Note | When you enter the text to search, the Search field pre populates relevant results in a drop-down. From the results list,
                                                            hover over the required contact and click the icon. |
|---|---|

| Step 1 | In the Contact list, click the icon at the end of the required contact. |
|---|---|
| Step 2 | From the drop-down, click Edit . |
| Step 3 | In the Edit Contact window, modify the display name or the group. While modifying the group for the contact, you can either add the contact to existing groups or create a new group. |
| Step 4 | Click Save . |

| Step 1 | To move a single Contact: Click the icon at the end of the required contact. From the drop-down, click Move . In the Select Destination window, select an existing group or create a new group. Click Move . |
|---|---|
| Step 2 | To move multiple contacts: Press and hold the Ctrl key and select the required contacts. On the Contact list header, click Move . In the Select Destination window, select existing groups or create a new group. Click Move . |

| Step 1 | To delete a single contact: In the Contact list, click the icon at the end of the required contact. From the drop-down, click Delete . In the confirmation prompt, click Delete to remove the contact from that group. |
|---|---|
| Step 2 | To delete multiple contacts: Press and hold the Ctrl key and select the required contacts. On the Contact list header, click Delete . In the confirmation prompt, click Delete to remove the contact from that group. |

| Step 1 | In the contact list, click the icon at the end of the required group. |
|---|---|
| Step 2 | From the drop-down list, click Edit . |
| Step 3 | In the Group window, modify the group name. |
| Step 4 | Click Save . |

| Step 1 | In the Contact list, click the icon at the end of the required group. |
|---|---|
| Step 2 | From the drop-down, click Delete . |
| Step 3 | In the confirmation prompt, click Delete . The group is removed with all the contacts in it. |

| Note | You can chat with agents logged in to the Desktop Chat. You cannot send messages to the signed out agents. |
|---|---|

| Note | The administrator should have enabled attachment support for you to send and receive attachments. |
|---|---|

| Note | You can send or receive attachments only from the users using Desktop Chat. |
|---|---|

| Step 1 | Click the drop-down arrow beside your current state in the Desktop Chat window. |
|---|---|
| Step 2 | Choose the appropriate state from the list. |

| Note | If your status in set to Do Not Disturb and you receive a chat message, the message is displayed only if your chat window
                                             is active. If the chat window is closed or minimized, the Desktop Chat icon blinks and you will only see the minimized chat
                                             window header with the number of chat tabs that have unread messages. |
|---|---|

| Step 1 | Click the drop-down arrow beside your current state in the Desktop Chat window |
|---|---|
| Step 2 | From the displayed list, click Sign Out . |