---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-messageservice-cmgt-b-spark-hybrid-m-1ca2ae251d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/messageservice/cmgt_b_spark-hybrid-message-deployment-guide/cmgt_b_spark-hybrid-message-deployment-guide_chapter_00.html
retrieved_at: 2026-08-16T15:37:48.029587+00:00
---

Deployment Guide for Hybrid Message

# Deployment Guide for Hybrid Message

Updated: October 4, 2018

Chapter: Cisco Webex Hybrid Message Service Overview

## Chapter: Cisco Webex Hybrid Message Service Overview

# Cisco Webex Hybrid Message Service Overview

## Hybrid Message Components and Users

Hybrid Message connects your Unified Communications Manager IM and Presence Service ( IM and Presence Service ) to Webex to enable interoperability with Webex App .

This deployment provides interoperability between your on-premises Jabber deployment and Webex App users. This is different to the interoperability between cloud-based Jabber deployments and Webex App users (see https://help.webex.com/article/nzx9su0 for more on that deployment).

On the left of the diagram is your on-premises deployment of Cisco Jabber and IM and Presence Service . On the right is your organization in Webex , with your Webex App users. You manage this organization using Control Hub .

The Hybrid Message enables interoperability between these two groups of users. The components that make Hybrid Message possible are the message connector , hosted on Cisco Expressway infrastructure on your premises, and the Message Service, running in the Webex cloud.

Licensing and Entitlement Factors Affecting Interoperability

We assume that all users are previously licensed for Cisco Jabber, with Jabber registered to Cisco Unified Communications
                                 Manager IM and Presence.

You need any paid-for Webex app offer for your organization. You can order this through Cisco Commerce Workspace.

You also need to have access to Cisco Webex Control Hub, with administrator privileges for your organization (you get these
                                 as part of the ordering process).

You should import all Jabber users into Control Hub and grant them all the "Message Free" entitlement. This entitles all the Jabber users to the basic Webex App messaging functionality.

There are no additional paid license requirements for this basic messaging. Having this entitlement for all users improves
                                 interoperability between those who are enabled for Hybrid Message and those who are only licensed for Jabber.

Hybrid Message can only work between users who are in the same organization in Control Hub . The service does not enable Webex App users to communicate with Jabber users outside of their organization.

Users who are enabled for Hybrid Message can use Jabber or Webex App to chat with all other users in the organization, irrespective of whether the recipient is using Webex App or Jabber.

Users who are not enabled for the Hybrid Message can use Jabber to chat with all other users in the organization. They can use Webex App to chat with users who are enabled for Hybrid Message , but the messages are not copied to the recipients' Jabber clients.

## User Interactions

This diagram shows the progression of your user population as you implement Hybrid Message Service. At the start, all users
                           are on Cisco Jabber (point 1 on diagram). The diagram then shows the tasks that you perform to get to the destination, where
                           you have Hybrid Message Service enabled for some of your users (Point 3).

Now there are four ways to send chat messages:

A user without Message Service uses Webex

A user without Message Service uses Cisco Jabber

A user with Message Service uses Webex

A user with Message Service uses Cisco Jabber

The recipients can also use those four ways to receive chat messages, which means 16 possible interactions. You can expect eight of them to work because they are interactions between
                           the same clients (Jabber to Jabber or Webex to Webex—point 2). Of the remaining eight interop scenarios, we expect three cases
                           to fail:

The sender is using Webex but is not enabled for Hybrid Message Service. The sender uses Webex to start a direct space with
                           the recipient. The recipient is using Jabber, so does not see the messages in Webex.

If the sender were enabled for Hybrid Message Service, the Webex chat messages would be copied to IM and Presence and sent
                           from the Jabber account. But, because the sender is not enabled for Hybrid Message Service, the messages are not copied to
                           IM and Presence, and so the recipient will not see them unless they use Webex.

The sender is using Webex but is not enabled for Hybrid Message Service. The sender uses Webex to start a direct space with
                           the recipient. The recipient is enabled for Hybrid Message Service but is using Jabber, so does not see the messages.

This behavior is expected. We designed the service this way to reduce load, because we anticipate that you will enable Hybrid
                           Message Service for the "early adopters" in your organization, and that they will use Webex as their primary chat client.

The sender is using Jabber and starts a chat with the recipient’s Jabber contact. The recipient is using Webex and does not
                           see the Jabber conversation. The recipient is not enabled for Hybrid Message Service, so those Jabber messages are not copied
                           and sent to Webex.

The recipient remains unaware of the conversation unless they use Jabber. In that case, if offline storage is disabled, the
                           recipient may never see the conversation.

## Deployment Models

### Choosing a Deployment Model

Consider the following factors when choosing how you deploy Hybrid Message :

Scale: How many IM and Presence Service users do you expect to serve? Will you need to add nodes / clusters to improve the capacity of the service to meet that requirement?

We support 195,000 users per organization across multiple Expressway clusters.

We also support up to 5,000 Message Service users per Small Expressway, up to 6,500 users per Medium Expressway, and up to
                                    15,000 users per Large Expressway. This gives a maximum number of 75,000 on a cluster of 6 Expressways, because the capacity
                                    of one node is reserved for redundancy. See https://help.webex.com/article/nv5p67g for an explanation of the Message Service capacity.

Availability: How important is service availability to you? Do you need to deploy redundant nodes / clusters to ensure continuous
                                    service in the event of a failure?

Geography: Global distribution of users means that you may have data centres in multiple timezones. Latency may be a factor
                                    to consider when choosing where to deploy your connector hosts.

In each deployment scenario, remember that:

Each Expressway cluster has up to six nodes, including the primary.

You must register the primary node of each Expressway cluster with Webex .

To connect an Expressway cluster to an IM and Presence Service cluster, enter the publisher's details on the primary node of the relevant Expressway cluster. This action connects all nodes
                                          of the Expressway cluster with all nodes of the IM and Presence Service cluster (diagrams show only the primary to publisher connections, for clarity).

You must not connect all Expressway clusters to all IM and Presence Service clusters. We do not support this scenario, because the potential benefit from redundancy is outweighed by the risk of overloading
                                          the solution.

You must not associate multiple Expressway connector clusters with one IM and Presence Service cluster (even though your IM and Presence Service cluster may be able to home more message and presence users than your Expressway cluster can support). We do not support
                                          this scenario.

You may connect multiple IM and Presence Service clusters to each Expressway connector cluster.

We support up to 5 IM and Presence Service clusters per Expressway connector cluster.

You can use Resource Groups in Control Hub to define your organization's geography, and then assign Expressway resources to different resource groups that represent
                                          locations.

The set of users you assign to each resource group should correspond to the users in all IM and Presence Service clusters served by the Expressways in those resource groups.

### One Expressway Connector Cluster to One IM and Presence Service Cluster

This is the recommended deployment option. It requires an Expressway connector cluster per IM and Presence Service cluster. If you have more than one site, you can repeat the configuration in each datacentre (For example, two datacenters
                              shown below).

### One Expressway Connector Cluster to Multiple IM and Presence Service Clusters

This deployment option requires one Expressway connector cluster across the whole IM and Presence Service deployment. This option is simple to configure and manage, but scalability and latency could be concerns if you have many
                              users and/or wide geographical distribution.

### Meshing is Not Supported

There is a performance impact for each message connector that connects to an IM and Presence Service cluster. For that reason, we do not support multiple Expressway clusters connecting to one IM and Presence Service cluster. By extension, meshing the connectors with the IM and Presence Service clusters is not supported.

## Scope of Deployment Features

Webex for Government environment

Hybrid Message service is available in the Webex for Government environment.

Instant Messaging Compliance

Hybrid Message can work with IM and Presence Service that is configured for compliance. Webex App does not support compliance and Webex App to Webex App messaging is possible for blocked Jabber users.

Message encryption

Supported (mandated) between your premises and Webex .

Messages from IM and Presence Service to Webex App are encrypted by the message connector .

Messages from Webex App to IM and Presence Service are decrypted by the message connector .

message connector makes TCP connections to IM and Presence Service nodes. TLS is not supported on these connections.

Multiple on-premises domains

message connector works with multiple XMPP domains.

Coresidency with other Hybrid Services

The Message Connector supports coresidency with other Expressway-based Hybrid Services ( Hybrid Calling and Hybrid Calendar ). Coresidency reduces the number of Hybrid Message users carried by the connector host.

See https://help.webex.com/article/nv5p67g for details of coresidency and capacity.

Data Security / Key Management System

The Hybrid Message is compatible with Hybrid Data Security .

We normally use the Webex Key Management System (KMS) for securing Hybrid Message , but you have the option to use an on-premises instance of KMS with Hybrid Message .

See https://www.cisco.com/go/hybrid-data-security for details of Hybrid Data Security deployment.

Coresidency with Mobile and Remote Access (MRA)

We do not recommend installing Message Connector on an Expressway cluster that is used for MRA. However, if you do choose
                                          to do this, we will only support up to 100 Message Service users per node, to a maximum of 500 per cluster.

Deployment scale

We currently support up to 195,000 users per organization enabled for Hybrid Message , across multiple Expressway clusters.

This limit applies to the subset of users in your organization that use Hybrid Message . It does not affect the number of users that you enable for Webex App ; you should import all your Jabber users to Webex .

See https://help.webex.com/article/nv5p67g for details of Hybrid Message scale and coresidency.

You can deploy up to 5 IM and Presence Service clusters with one Expressway connector cluster.

We do not recommend using multiple connector clusters with one IM and Presence Service cluster.

XMPP or SIP messaging federation between the Jabber deployment and another domain

Hybrid Message service works when you have interdomain federation between the IM and Presence Service and a third-party messaging provider.

This means that when a contact in a federated organization sends a message to a Hybrid Message user, the message appears to that user in both Jabber and the Webex App .

XMPP or SIP federation with Hybrid Message service is not supported in the Webex for Government environment.

High availability and failover of IM and Presence Service nodes

The Message Connector is aware of the high availability setting on Presence Redundancy Groups. It responds automatically to failover / fallback
                                          events.

Webex for Government: Hybrid Message to enable interoperability between Webex App and Jabber

Hybrid Message is a service that enables interoperability between Jabber users and Webex App users. This service provides
                                          an option for migrating users from Jabber, connected to IM & Presence on your premises, to Webex App.

Users who are enabled for this service can use the Webex App to read and respond to messages from Jabber users.

## Contacts

message connector supports Webex App contacts. message connector does nothing with Jabber contacts.

Existing contacts will not be transitioned across from Jabber to Webex.

## Direct Messaging Interactions (One to One)

All Hybrid Message users can use Webex App to send messages to all Webex App users in their organization.

All Hybrid Message users can use Jabber to send messages to all Webex App users in their organization.

Webex App users who are not entitled for Hybrid Message cannot send messages to the Jabber clients of other users.

If both parties are Hybrid Message users, they can see the full to/from conversation in both clients.

"Is Typing" status is supported. The user interface shows an indicator to one user when the other user has read a conversation
                                 or recently sent a message. The indicator will last for 5 minutes, even for spaces where the user is inactive.

Read receipts are supported. To users, this means that the unread messages count is synchronized between Jabber and Webex App .

When the Webex App user deletes a message from the 1:1 space, the Jabber user is notified that " Username used Webex App to delete a previously posted message". The corresponding Jabber message is not deleted.

Plain text only. Webex App markdown is not converted to Jabber rich text. Jabber rich text is not converted to Webex App markdown.

Editing messages in Webex App is supported. When a Message Service user edits a message in Webex App , the original version of the message is deleted in Webex App . The Message Connector sends the edited message to Unified CM IM and Presence.

The recipient on Jabber sees the edited message as a new message, they also receive a notification " Username used Webex App to delete a previously posted message." However, they can disregard the delete notification, as they still see the original
                                 version of the message in Jabber.

Webex App doesn't tell the user that the original message is still visible in Jabber - even though the original message is no longer
                                 visible in Webex App .

## Offline Storage

Offline storage affects one to one messaging interactions from Hybrid Message users.

The expected behavior, when a Hybrid Message -entitled Webex App user sends a message to another Webex App user, is for the sender's Jabber to also send that message to the recipient's Jabber. If the recipient is not using Jabber
                           then, depending on the state of offline storage, one of the following will happen:

Offline storage is enabled on IM and Presence Service : The message is stored and will be sent if the recipient signs in to Jabber.

Offline storage is not enabled on IM and Presence Service : The message is discarded and the sender will see a "Message could not be delivered" error, if they are using versions before
                                 12.5.

In this case, the sender and recipient may both have seen that this message has been delivered, because they're using Webex App . This is expected behavior but it could confuse users.

Offline storage is governed by the Suppress offline instant messaging setting on IM and Presence Service .

There is a known issue with offline messaging. When a Message Service user comes back online in Webex, stored messages are
                                       replayed in Webex but they may be out of sequence. The same messages are replayed in sequence in the user's Jabber client.

## Group Messaging

Not supported. Webex App spaces are not converted to Jabber group chats. Jabber group chats are not converted to Webex App spaces.

The following is a list of known behaviors when users try group messaging interoperability. Note that there is usually no
                           indication of a problem, which could cause confusion for your users.

When Jabber users are creating group chats, or inviting contacts to group chats, they will be able to browse and select from Webex App users who are entitled for Hybrid Message . However, when they try to add these contacts to the group chat, the Webex App users are not added. Jabber users are added to the group chat as normal. There is no UI feedback to indicate a problem.

If a Jabber user, who is entitled for Hybrid Message , switches to using Webex App , that user is immediately removed from the active rosters in all group chats with other Jabber users.

Webex App users can add any Webex App -only or Hybrid Message users to spaces. For Hybrid Message users who are using Jabber, there is no indication that they have been added to the Webex App space. The only indication of this problem is to the other users in the space; there will be no read receipts from the affected Hybrid Message users.

If a Hybrid Message user was once using Jabber to participate in a persistent group chat, and then switches to use Webex for their messaging
                                 interactions, their Active status in Webex is translated to Available presence in the persistent group chat. The other Jabber
                                 users may assume that the user is following the conversation. However, if the apparently Available user doesn't open Jabber,
                                 they may never be aware of later posts in that persistent conversation.

## Presence Translation

We have taken a minimal approach to presence translation, based on the premise that the Hybrid Message Service is a transitionary
                           arrangement to facilitate migration from Jabber to Webex App . Our design does not account for users indefinitely using both clients, because the way Unified CM IM and Presence calculates
                           the composed presence can result in Jabber users seeing unexpected presence status of their contacts.

### Presence of Jabber client, as seen by Webex App user

Presence is not translated from Cisco Jabber to Webex App .

This limitation has a consequence on the Do Not Disturb behavior: when a user manually resets their Jabber presence from "Do
                                          Not Disturb" back to "Available", the corresponding Webex App status does not change. This is confusing because typically this action would reset the presence on all of the user's logged
                                          in clients/devices.

### Presence of Webex App app, as seen by Jabber user

Partially supported from Webex App to Cisco Jabber.

How it works:

message connector polls Webex once every 10 minutes for all users' presence status. It submits this to Unified CM IM and Presence Service as device presence (meaning inferred by the device/client, as opposed to manually changed by the user).

This approach has predictable results if Hybrid Message Service users are using either Webex App or Jabber but, in a migration scenario, we expect people to be using both clients.

When a user has more than one client or device that submits device presence, IM and Presence Service gives priority to the
                              most recent update for that user, and displays that presence to all the subscribing Jabber users.

Whenever a user manually changes their Jabber status, IM and Presence Service gives priority to the manual presence. In this
                              case, the device presence - whether from Webex App or Jabber - is not shown to other Jabber users.

The following table lists some of the presence states that Jabber users could see when you have Hybrid Message Service users.
                              This is a best effort at mapping the possible scenarios because we cannot exhaustively test all possible interactions that
                              occur in your environment:

Presence of a user, as seen by another Jabber user

How that presence was established by IM and Presence Service

Available

The contact's presence indicator is green.

The contact is only using Jabber, and Jabber has determined that the user is Available .

The contact is using Jabber and Webex App , and Jabber has determined that the user is Available . IM and Presence Service received that presence update more recently than presence from the same user's Webex App app.

Jabber users do not see this presence for a user who is only using Webex App .

Available @ Webex

The contact's presence indicator is green, and displays text "@ Webex".

The contact is only using Webex App , and was Active on Webex App within the last 10 minutes.

The contact is using Jabber and Webex App , and was Active on Webex App within the last 10 minutes. IM and Presence Service received that presence update more recently than device presence from
                                                the same user's Jabber client.

Jabber users do not see this presence for a user who is only using Jabber.

Available with custom message

The contact is only using Jabber, and has manually changed their presence status.

The contact is using Jabber and Webex App , and has manually changed their presence status in Jabber. IM and Presence Service prefers the manually edited presence from
                                                Jabber over the device presence update from the same user's Webex App app.

Jabber users do not see this presence for a user who is only using Webex App .

Away

The contact's presence indicator is amber.

The contact is only using Jabber, and Jabber has determined that the user is Away .

The contact is using Jabber and Webex App , and Jabber has determined that the user is Away . IM and Presence Service received that presence update more recently than presence from the same user's Webex App app.

Jabber users do not see this presence for a user who is only using Webex App .

Away @ Webex

The contact's presence indicator is amber, and displays text "@ Webex".

The contact is only using Webex App , and was Active more than 10 minutes ago, but within the last 72 hours. In Webex App this displays as, for example, " Active 2 hours ago " or " Active yesterday ".

The contact is using Jabber and Webex App , and was Active on Webex App more recently than they were Available in Jabber. IM and Presence Service received the Webex App device presence more than 10 minutes ago but within the last 72 hours. Also, it received that presence update more recently
                                                than it received device presence from the same user's Jabber client.

Jabber users generally do not see this presence for other users who are only using Jabber. Note that users who are enabled
                                                for Hybrid Message Service, but are not actually using Webex App , still have their presence composed as if they were using Webex App . In most cases their Jabber presence takes precedence, but it is possible that they can show as Away "@ Webex"; for example,
                                                if they are out of office and their calendars are integrated with Cisco Webex.

Away @ Webex can also mean that the user is Out of Office in Webex App . Webex App shows an Airplane overlay on that user's profile picture.

Out of Office status in Webex App is provided by integration with user calendars. If the user's Webex App app is not integrated with their calendar, there is no Out of Office status in Webex App .

If a Webex App user is using Webex App while their calendar reports Out of Office, their Webex App status could change back to Active. This would correctly be translated to Available in that user's Jabber presence.

Webex App user is not sharing status (the Show statuses box is unchecked in Webex App settings).

Webex App users can choose to hide their status, which also prevents them from seeing status of other Webex App users. A Jabber user always sees these buddies as Away.

The Message Connector will never destroy the user's XMPP session while the user is in an Away state. If the user is not showing
                                                their status, their session will persist even if they have not used Webex App within the previous 72 hours.

Away with custom message

The contact is only using Jabber, and has manually changed their presence status.

The contact is using Jabber and Webex App , and has manually changed their presence status in Jabber. IM and Presence Service prefers the manually edited presence from
                                                Jabber over the device presence update from the same user's Webex App app.

Jabber users do not see this presence for a user who is only using Webex App .

Do Not Disturb

The contact's presence indicator is red.

This is a user level setting, which means that all the user's logged in clients/devices - including phones where applicable
                                          - have the "Do Not Disturb" status.

The contact is using Jabber and has manually changed status to Do Not Disturb .

If the user is also using Webex App , their Webex App presence is unaffected because Message Connector does not translate presence from Jabber to Webex App .

Also, IM and Presence Service always prefers the manual DND from Jabber over the device presence from Webex App .

The contact is using Webex App and has manually changed status to Do not disturb: for a period between 30 minutes and 24 hours .

If a Webex App user has turned on "Do not disturb", then Webex App shows other Webex App users a crescent Moon overlay on that user's profile picture.

The contact is using both clients and has manually changed status to Do not disturb: for a period between 30 minutes and 24 hours .

This status persists in both clients until the period expires in Webex App , or until the user changes it in Webex App .

A user who is using both clients cannot reset their Do Not Disturb status by changing their presence in Jabber (they can use Webex App , or wait for the DND to expire in Webex App ). This is because the Message Connector does not translate presence from Jabber to Webex App .

Offline

The contact's presence indicator is gray.

The other user has not used Webex App or Jabber within the last 72 hours. The message connector destroys the XMPP session it was holding for the offline user's Webex App .

You can see the count of inactive Hybrid Message users, on a particular message connector host, at Applications > Hybrid Services > Message Service > Message Service Status .

Read about Webex app availability:

Webex | See People's Availability ( https://help.webex.com/wghlt5 )

Webex | Stop Sharing Your Status ( https://help.webex.com/nkzs6wl )

## File Transfer

Webex App users can share files with Jabber users. When a file is attached to a 1:1 space in Webex App , the Jabber user gets a link to that file.

The Jabber user gets a message if the Webex App user deletes a file from the 1:1 space.

A Jabber user cannot send files to Webex App users.

When a Jabber user is communicating with a Webex App user, Jabber's file transfer and screen capture options are disabled.

However, if the IM and Presence Service has Managed File Transfer (MFT) enabled, the user's Jabber options for these features appear to be usable. In this case,
                                 if the Jabber user tries to send a file, the Webex app user receives a notification that a file has been sent in Jabber.

If the Webex user is not logged in to Jabber when the file is sent, they do not receive the file.

This behavior affects the recipient whether they are using Jabber on-premises (registered to IM and Presence), or Jabber registered
                                 to Webex.

## Migration Considerations

If you're using Hybrid Message Service to gradually migrate your user base from Cisco Jabber to Webex, the following issues
                           and mitigations may help your planning.

Admin-generated invitations to join Webex: One requirement to make Hybrid Message Service work is to have all your Jabber users in Cisco Webex, imported by CSV or by
                                 Hybrid Directory Service. When you import users, they will all get invitations to start using Webex, which you may want to
                                 prevent. If your organization is SSO-enabled in Control Hub, you can suppress the email invite behavior before you import
                                 the users. See https://help.webex.com/article/g5ey83 .

Unfortunately, you cannot suppress these initial email invitations unless your organization is SSO-enabled.

Suppressing the email invitations will help to mitigate unintended early access to Webex.

User-generated invitations to join Webex: Cisco Webex normally invites users (by email) to start using the Webex app, if they are already in Cisco Webex but not yet
                                 using the app. When you enable Hybrid Message Service, this "self subscribe" behavior is automatically disabled for your organization.

The reason we designed it this way is because whenever a Message Service user messages another Jabber user, Webex generates
                                 an email to invite the recipient to start using the Webex app. This amounts to spam for any Jabber user who is not yet using
                                 Webex.

Unintended early access to Webex: One requirement to make Hybrid Message Service work is to have all your Jabber users in Cisco Webex, imported by CSV or by
                                 Hybrid Directory Service. You may not want these users to start using Webex just yet but, if they are synchronized with Directory
                                 Service and also have SSO enabled, there is no technical reason to prevent them from using the Webex app. This could lead
                                 to interoperability problems for those users who are not enabled for Hybrid Message Service.

For example:

A Hybrid Message user, talking to another user in Webex, can only see their own half of the conversation when looking at it in Jabber. The
                                       other user will also appear to be Offline in Jabber (even though they are Active in Webex).

In the same scenario, if the Hybrid Message user tries to use Jabber to continue the conversation, the messages go to the other user in Webex, but that user's responses
                                       do not come back to Jabber.

If you are following a migration plan that requires users to stay on Jabber, despite technically being able to use Webex,
                                 you may want to prevent client installations or advise your users of potential interoperability issues.

A user's Jabber ID (JID) is not the same as a user's Webex UID: The Webex UID must be the user's email address but the Jabber ID does not have to be the email address, even though it looks
                                 like one.

Do not search for a user's JID when you are in Webex. Use the JID (or name) to search for users in the Jabber client. Use
                                 the email address (or name) to search for users in Webex.

Offline message suppression: Users who start chatting to each other using Webex will still have access to Cisco Jabber. If a user is online with both
                                 clients, the Hybrid Message Service tries to deliver messages with both clients. If the recipient is offline in Jabber, the
                                 sender could receive misleading offline messages from IM and Presence service.

To mitigate this issue:

Sign in to Cisco Unified CM IM and Presence Administration and go to Messaging > Settings .

Clear the box labeled Suppress offline instant messaging and click Save .

There is a known issue with offline messaging. When a Message Service user comes back online in Webex, stored messages are
                                       replayed in Webex but they may be out of sequence. The same messages are replayed in sequence in the user's Jabber client.

## Message Flows and Security

We encrypt all instant messages that we transmit across the public internet using the Key Management Service (KMS). By default, Webex App customers use the KMS in the Webex cloud, but the Hybrid Message also supports Hybrid Data Security , which provides on-premises KMS.

### Messages from Cisco Jabber to Webex App

The sender sends a message from the Jabber client. The message goes to IM and Presence Service , which sends on to the Jabber client of the recipient. This is the normal IM and Presence Service flow, which you can make secure if you want to (beyond the scope of this document).

If the recipient is a dual user, entitled for Hybrid Message , then the message may also go to the message connector on the Expressway.

It will not go to message connector if the recipient has not recently been active on Webex App ; to save processing and memory resources, we assume that the user will not answer in Webex App if they have not been active for more than 72 hours.

You can choose to secure the connections between the IM and Presence Service cluster and the Expressway cluster hosting the message connector .

The message connector interacts with the Key Management Service (via the cloud-based messaging service) to request an encryption key. The messaging
                                    service retrieves the key for an existing space, or a new key if this is the first message for a new space (aka "conversation"
                                    or "room"), and passes the key back to the message connector .

The message connector creates a new conversation in Webex , if necessary, and posts the encrypted message to that conversation.

This encryption is not optional and requires no configuration.

Webex securely sends the message to the recipient's Webex App client. Description of the mechanism is beyond the scope of this document.

### Messages from Webex App to Cisco Jabber

The Webex App app connects to Webex which provides a server certificate to authenticate itself. The app maintains this connection while the user is active. The
                              app interacts with the Key Management Service to dynamically generate encryption keys for each user and each space (aka "conversation"
                              or "room").

The sender uses Webex App to message the recipient. The Webex App app encrypts the message and sends it to Webex . Webex makes the encrypted message available to the recipient's Webex App client. This is the normal Webex App message flow; it is always secure, but description of the mechanism is beyond the scope of this document.

The Webex cloud checks its messaging service database to see if the sender and recipient are entitled to use Hybrid Message , and where to route the message towards the recipient.

The Webex cloud sends the encrypted message to the message connector .

The message connector interacts with the Key Management Service (via the cloud-based messaging service) to request the decryption key for the Webex App space.

The message connector decrypts the message and sends it to IM and Presence Service .

IM and Presence Service tries to route the message onwards to the Jabber client of the recipient.

When the message is read, the connector detects the read receipt and sends it back to Webex , so that the users' unread messages are consistent across their messaging clients.

## Hybrid Message Connections

## Message Service Ports

Purpose

Src. IP

Src. Ports

Protocol

Dst. IP

Dst. Ports

Basic messaging

Webex App clients

Ephemeral

TCP

Webex hosts

443

Persistent HTTPS registration

Connector host Expressway

30000-35999

TLS

Webex hosts

443

XMPP (IM and Presence)

Connector host Expressway

30000-35999

TCP

Unified CM IM and Presence publisher

7400

AXL queries (Administrative XML Layer)

Connector host Expressway

30000-35999

TCP

Unified CM IM and Presence publisher

8443

Messaging and Presence

Cisco Jabber clients

Ephemeral

TCP

Unified CM IM and Presence publisher

5222

| Note | This deployment provides interoperability between your on-premises Jabber deployment and Webex App users. This is different to the interoperability between cloud-based Jabber deployments and Webex App users (see https://help.webex.com/article/nzx9su0 for more on that deployment). |
|---|---|

| Feature | Description |
|---|---|
| Webex for Government environment | Hybrid Message service is available in the Webex for Government environment. |
| Instant Messaging Compliance | Hybrid Message can work with IM and Presence Service that is configured for compliance. Webex App does not support compliance and Webex App to Webex App messaging is possible for blocked Jabber users. |
| Message encryption | Supported (mandated) between your premises and Webex . Messages from IM and Presence Service to Webex App are encrypted by the message connector . Messages from Webex App to IM and Presence Service are decrypted by the message connector . message connector makes TCP connections to IM and Presence Service nodes. TLS is not supported on these connections. |
| Multiple on-premises domains | message connector works with multiple XMPP domains. |
| Coresidency with other Hybrid Services | The Message Connector supports coresidency with other Expressway-based Hybrid Services ( Hybrid Calling and Hybrid Calendar ). Coresidency reduces the number of Hybrid Message users carried by the connector host. See https://help.webex.com/article/nv5p67g for details of coresidency and capacity. |
| Data Security / Key Management System | The Hybrid Message is compatible with Hybrid Data Security . We normally use the Webex Key Management System (KMS) for securing Hybrid Message , but you have the option to use an on-premises instance of KMS with Hybrid Message . See https://www.cisco.com/go/hybrid-data-security for details of Hybrid Data Security deployment. |
| Coresidency with Mobile and Remote Access (MRA) | We do not recommend installing Message Connector on an Expressway cluster that is used for MRA. However, if you do choose
                                          to do this, we will only support up to 100 Message Service users per node, to a maximum of 500 per cluster. |
| Deployment scale | We currently support up to 195,000 users per organization enabled for Hybrid Message , across multiple Expressway clusters. This limit applies to the subset of users in your organization that use Hybrid Message . It does not affect the number of users that you enable for Webex App ; you should import all your Jabber users to Webex . See https://help.webex.com/article/nv5p67g for details of Hybrid Message scale and coresidency. You can deploy up to 5 IM and Presence Service clusters with one Expressway connector cluster. We do not recommend using multiple connector clusters with one IM and Presence Service cluster. |
| XMPP or SIP messaging federation between the Jabber deployment and another domain | Hybrid Message service works when you have interdomain federation between the IM and Presence Service and a third-party messaging provider. This means that when a contact in a federated organization sends a message to a Hybrid Message user, the message appears to that user in both Jabber and the Webex App . Note XMPP or SIP federation with Hybrid Message service is not supported in the Webex for Government environment. | Note | XMPP or SIP federation with Hybrid Message service is not supported in the Webex for Government environment. |
| Note | XMPP or SIP federation with Hybrid Message service is not supported in the Webex for Government environment. |
| High availability and failover of IM and Presence Service nodes | The Message Connector is aware of the high availability setting on Presence Redundancy Groups. It responds automatically to failover / fallback
                                          events. |
| Webex for Government: Hybrid Message to enable interoperability between Webex App and Jabber | Hybrid Message is a service that enables interoperability between Jabber users and Webex App users. This service provides
                                          an option for migrating users from Jabber, connected to IM & Presence on your premises, to Webex App. Users who are enabled for this service can use the Webex App to read and respond to messages from Jabber users. |

| Note | XMPP or SIP federation with Hybrid Message service is not supported in the Webex for Government environment. |
|---|---|

| Note | Existing contacts will not be transitioned across from Jabber to Webex. |
|---|---|

| Note | There is a known issue with offline messaging. When a Message Service user comes back online in Webex, stored messages are
                                       replayed in Webex but they may be out of sequence. The same messages are replayed in sequence in the user's Jabber client. |
|---|---|

| Note | This limitation has a consequence on the Do Not Disturb behavior: when a user manually resets their Jabber presence from "Do
                                          Not Disturb" back to "Available", the corresponding Webex App status does not change. This is confusing because typically this action would reset the presence on all of the user's logged
                                          in clients/devices. |
|---|---|

| Presence of a user, as seen by another Jabber user | How that presence was established by IM and Presence Service |
|---|---|
| Available The contact's presence indicator is green. | The contact is only using Jabber, and Jabber has determined that the user is Available . The contact is using Jabber and Webex App , and Jabber has determined that the user is Available . IM and Presence Service received that presence update more recently than presence from the same user's Webex App app. Jabber users do not see this presence for a user who is only using Webex App . |
| Available @ Webex The contact's presence indicator is green, and displays text "@ Webex". | The contact is only using Webex App , and was Active on Webex App within the last 10 minutes. The contact is using Jabber and Webex App , and was Active on Webex App within the last 10 minutes. IM and Presence Service received that presence update more recently than device presence from
                                                the same user's Jabber client. Jabber users do not see this presence for a user who is only using Jabber. |
| Available with custom message | The contact is only using Jabber, and has manually changed their presence status. The contact is using Jabber and Webex App , and has manually changed their presence status in Jabber. IM and Presence Service prefers the manually edited presence from
                                                Jabber over the device presence update from the same user's Webex App app. Jabber users do not see this presence for a user who is only using Webex App . |
| Away The contact's presence indicator is amber. | The contact is only using Jabber, and Jabber has determined that the user is Away . The contact is using Jabber and Webex App , and Jabber has determined that the user is Away . IM and Presence Service received that presence update more recently than presence from the same user's Webex App app. Jabber users do not see this presence for a user who is only using Webex App . |
| Away @ Webex The contact's presence indicator is amber, and displays text "@ Webex". | The contact is only using Webex App , and was Active more than 10 minutes ago, but within the last 72 hours. In Webex App this displays as, for example, " Active 2 hours ago " or " Active yesterday ". The contact is using Jabber and Webex App , and was Active on Webex App more recently than they were Available in Jabber. IM and Presence Service received the Webex App device presence more than 10 minutes ago but within the last 72 hours. Also, it received that presence update more recently
                                                than it received device presence from the same user's Jabber client. Jabber users generally do not see this presence for other users who are only using Jabber. Note that users who are enabled
                                                for Hybrid Message Service, but are not actually using Webex App , still have their presence composed as if they were using Webex App . In most cases their Jabber presence takes precedence, but it is possible that they can show as Away "@ Webex"; for example,
                                                if they are out of office and their calendars are integrated with Cisco Webex. Away @ Webex can also mean that the user is Out of Office in Webex App . Webex App shows an Airplane overlay on that user's profile picture. Out of Office status in Webex App is provided by integration with user calendars. If the user's Webex App app is not integrated with their calendar, there is no Out of Office status in Webex App . If a Webex App user is using Webex App while their calendar reports Out of Office, their Webex App status could change back to Active. This would correctly be translated to Available in that user's Jabber presence. Webex App user is not sharing status (the Show statuses box is unchecked in Webex App settings). Webex App users can choose to hide their status, which also prevents them from seeing status of other Webex App users. A Jabber user always sees these buddies as Away. The Message Connector will never destroy the user's XMPP session while the user is in an Away state. If the user is not showing
                                                their status, their session will persist even if they have not used Webex App within the previous 72 hours. |
| Away with custom message | The contact is only using Jabber, and has manually changed their presence status. The contact is using Jabber and Webex App , and has manually changed their presence status in Jabber. IM and Presence Service prefers the manually edited presence from
                                                Jabber over the device presence update from the same user's Webex App app. Jabber users do not see this presence for a user who is only using Webex App . |
| Do Not Disturb The contact's presence indicator is red. | This is a user level setting, which means that all the user's logged in clients/devices - including phones where applicable
                                          - have the "Do Not Disturb" status. The contact is using Jabber and has manually changed status to Do Not Disturb . If the user is also using Webex App , their Webex App presence is unaffected because Message Connector does not translate presence from Jabber to Webex App . Also, IM and Presence Service always prefers the manual DND from Jabber over the device presence from Webex App . The contact is using Webex App and has manually changed status to Do not disturb: for a period between 30 minutes and 24 hours . If a Webex App user has turned on "Do not disturb", then Webex App shows other Webex App users a crescent Moon overlay on that user's profile picture. The contact is using both clients and has manually changed status to Do not disturb: for a period between 30 minutes and 24 hours . This status persists in both clients until the period expires in Webex App , or until the user changes it in Webex App . A user who is using both clients cannot reset their Do Not Disturb status by changing their presence in Jabber (they can use Webex App , or wait for the DND to expire in Webex App ). This is because the Message Connector does not translate presence from Jabber to Webex App . |
| Offline The contact's presence indicator is gray. | The other user has not used Webex App or Jabber within the last 72 hours. The message connector destroys the XMPP session it was holding for the offline user's Webex App . You can see the count of inactive Hybrid Message users, on a particular message connector host, at Applications > Hybrid Services > Message Service > Message Service Status . |

| Note | There is a known issue with offline messaging. When a Message Service user comes back online in Webex, stored messages are
                                       replayed in Webex but they may be out of sequence. The same messages are replayed in sequence in the user's Jabber client. |
|---|---|

| Purpose | Src. IP | Src. Ports | Protocol | Dst. IP | Dst. Ports |
|---|---|---|---|---|---|
| Basic messaging | Webex App clients | Ephemeral | TCP | Webex hosts | 443 |
| Persistent HTTPS registration | Connector host Expressway | 30000-35999 | TLS | Webex hosts | 443 |
| XMPP (IM and Presence) | Connector host Expressway | 30000-35999 | TCP | Unified CM IM and Presence publisher | 7400 |
| AXL queries (Administrative XML Layer) | Connector host Expressway | 30000-35999 | TCP | Unified CM IM and Presence publisher | 8443 |
| Messaging and Presence | Cisco Jabber clients | Ephemeral | TCP | Unified CM IM and Presence publisher | 5222 |