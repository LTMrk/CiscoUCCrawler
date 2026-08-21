---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-su2-cup0-b-config-and-admin-guide-1-571185c91d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1_su2/cup0_b_config-and-admin-guide-1251su2/cup0_b_config-and-admin-guide-1251su2_chapter_01110.html
retrieved_at: 2026-08-21T09:06:09.935778+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU2

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU2

Updated: November 27, 2024

Chapter: Configure Availability and Instant Messaging

## Chapter: Configure Availability and Instant Messaging

# Configure Availability and Instant Messaging

## Availability and Instant Messaging Overview

IM and Presence Service allows your users to share their availability status with their contacts.

Point-to-point
                           instant
                           messaging 
                           supports
                           real-time
                           conversations
                           between  two users at a time. IM and
                           Presence
                           Service
                           exchanges
                           messages
                           directly
                           between users, from the sender to the
                           recipient. Users must be online in their instant message
                           clients to
                           exchange
                           point-to-point instant messages.

Instant messaging capabilities include:

When a user sends an instant message to a
                                 contact who is signed into
                                 multiple instant message
                                 clients, IM and
                                 Presence
                                 Service
                                 delivers the instant message to each
                                 client. IM and
                                 Presence
                                 Service
                                 continues to fork instant messages to each
                                 client, until the
                                 contact
                                 replies. Once the
                                 contact
                                 replies, IM and
                                 Presence
                                 Service only
                                 delivers instant messages to the
                                 client on
                                 which the
                                 contact
                                 replied.

When a user sends an instant message to a
                                 contact who is not signed in (offline), IM and
                                 Presence
                                 Service stores the instant message and
                                 delivers it after the offline
                                 contact signs back in to their instant message
                                 client.

Allows a user to send an instant message to
                                 multiple
                                 contacts at the same time, for
                                 example, when a user wants to send a
                                 notification to a large group of
                                 contacts.

Please note that not all instant message
                                 clients
                                 support broadcasting.

Maximum Contact List Size

Configure the maximum contact list size for a user; this is the number of contacts the user can add to their contact list.
                           This setting applies to the contact list on Cisco Jabber client applications and on third-party client applications.

Users who reach the maximum number of contacts are unable to add new contacts to their contact list, nor can other users add
                           them as a contact. If a user is close to the maximum contact list size, and the user adds a group of contacts that pushes
                           the contact list over the maximum number, IM and Presence Service does not add the surplus contacts. For example, if the maximum
                           contact list size on IM and Presence Service is 200. A user has 195 contacts and attempts to add 6 new contacts to the list,
                           IM and Presence Service adds five contacts and does not add the sixth contact.

Tip

The System Troubleshooter in Cisco Unified CM IM and Presence
                                          Administration indicates if there are users who have reached the
                                       contact list limit.

## Availability and Instant Messaging Prerequisites

For SIP to SIP instant messaging, the following services must be running on IM and Presence Service:

Cisco SIP Proxy

Cisco Presence Engine

Cisco XCP Router

For SIP to XMPP instant messaging, the following services must be running on IM and Presence Service:

Cisco SIP Proxy

Cisco Presence Engine

Cisco XCP Router

Cisco XCP Text Conference Manager

## Availability and Instant Messaging Task Flow

Perform the following tasks to configure availability and instant messaging on IM and Presence Service.

Step 1

Configure Presence Sharing

Use this procedure to configure the cluster-wide setting for Presence and IM availability sharing.  Presence sharing allow
                                          your users to be able to view each other's IM availability status.

Step 2

Enable Instant Messaging

Configure the system to allow users to exchange instant messages.

### Configure Presence
                           Sharing

Use this procedure to configure the cluster-wide setting for Presence and IM availability sharing.  Presence sharing allow
                                 your users to be able to view each other's IM availability status.

When availability sharing is turned off:

Users can view their own availability status in the client application, but the status for other users is greyed out.

When users enter a chat room, their availability status displays as Unknown .

Step 1

In Cisco Unified CM IM and Presence Administration , choose Presence > Settings > Standard Configuration .

Step 2

To enable cluster-wide Presence sharing, check the Enable availability sharing check box.

Individual Cisco Jabber users can enable or disable this setting for their own Jabber client, by reconfiguring the policy
                                                         settings within their Cisco Jabber client.

Step 3

If you want users to be able to view the Presence of other users without requiring the other user's approval, check the Allow user to view the availability of other users without being prompted for approval check box. Otherwise, all Presence requests must be authorized by the other user.

Individual end users can override this setting by reconfiguring the policy settings within their Cisco Jabber client.

Step 4

Configure maximum values for the Maximum Contact List Size and Maximum Watchers (per user) settings. If you don't want to use maximums, check the No Limit check box for each.

Step 5

Optional.  If you want Cisco Jabber users to be able to temporarily subscribe the Presence status  of other users whom are
                                          not on their contact list, check the Enable ad-hoc presence subscriptions check box and configure the additional ad-hoc presence settings.

Step 6

Complete any additional settings in the Presence Settings window. Refer to the online help for help with the fields and their settings.

Step 7

Click Save .

Step 8

Restart the Cisco XCP Router and Cisco Presence Engine services:

Log in to Cisco Unified IM and Presence Serviceability and choose Tools > Control Center - Feature Services

Select the Cisco Presence Engine service and click Restart .

Choose Tools > Control Center - Network Services .

Select the Cisco XCP Router service and click Restart .

Depending on which fields you edited, you may not need to restart services. Refer to the online help for information on the
                                                         fields that you edited.

#### What to do next

Enable Instant Messaging

### Enable Instant Messaging

Configure the system to allow users to exchange instant messages.

#### Before you begin

Configure Presence Sharing

Step 1

In Cisco Unified CM IM and Presence Administration , choose Messaging > Settings .

Step 2

Check the Enable instant messaging check box.

Step 3

Check the check box options that meet your deployment needs. For field descriptions, refer to the online help:

- Suppress offline instant messaging

- Allow clients to log instant message history (on supported clients only)

- Allow cut & paste in instant messages

Step 4

Click Save .

## Availability and Instant Messaging Interactions and Restrictions

Feature

Restriction

Availability Sharing

If you turn off this setting, users can view only their own availability status. Availability information is not shared to
                                          other users in the cluster. In addition, availability information received from outside the cluster is not shared either.

Instant Messages

If Cisco XCP Router shuts down abruptly or if the user stops/restarts it, the instant messages that were sent at the beginning
                                          or during the outage period may not be delivered to the destination user. Warning messages may not be sent to the user who
                                          sent the messages.

For more details, the administrator can check for error log lines containing "Dropping packet after jsm db shutdown" at the
                                          Cisco XCP Router trace files rtr-jsm-1.

| Tip | The System Troubleshooter in Cisco Unified CM IM and Presence
                                          Administration indicates if there are users who have reached the
                                       contact list limit. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Presence Sharing | Use this procedure to configure the cluster-wide setting for Presence and IM availability sharing.  Presence sharing allow
                                          your users to be able to view each other's IM availability status. |
| Step 2 | Enable Instant Messaging | Configure the system to allow users to exchange instant messages. |

| Note | When availability sharing is turned off: Users can view their own availability status in the client application, but the status for other users is greyed out. When users enter a chat room, their availability status displays as Unknown . |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Presence > Settings > Standard Configuration . |
|---|---|
| Step 2 | To enable cluster-wide Presence sharing, check the Enable availability sharing check box. Note Individual Cisco Jabber users can enable or disable this setting for their own Jabber client, by reconfiguring the policy
                                                         settings within their Cisco Jabber client. | Note | Individual Cisco Jabber users can enable or disable this setting for their own Jabber client, by reconfiguring the policy
                                                         settings within their Cisco Jabber client. |
| Note | Individual Cisco Jabber users can enable or disable this setting for their own Jabber client, by reconfiguring the policy
                                                         settings within their Cisco Jabber client. |
| Step 3 | If you want users to be able to view the Presence of other users without requiring the other user's approval, check the Allow user to view the availability of other users without being prompted for approval check box. Otherwise, all Presence requests must be authorized by the other user. Note Individual end users can override this setting by reconfiguring the policy settings within their Cisco Jabber client. | Note | Individual end users can override this setting by reconfiguring the policy settings within their Cisco Jabber client. |
| Note | Individual end users can override this setting by reconfiguring the policy settings within their Cisco Jabber client. |
| Step 4 | Configure maximum values for the Maximum Contact List Size and Maximum Watchers (per user) settings. If you don't want to use maximums, check the No Limit check box for each. |
| Step 5 | Optional.  If you want Cisco Jabber users to be able to temporarily subscribe the Presence status  of other users whom are
                                          not on their contact list, check the Enable ad-hoc presence subscriptions check box and configure the additional ad-hoc presence settings. |
| Step 6 | Complete any additional settings in the Presence Settings window. Refer to the online help for help with the fields and their settings. |
| Step 7 | Click Save . |
| Step 8 | Restart the Cisco XCP Router and Cisco Presence Engine services: Log in to Cisco Unified IM and Presence Serviceability and choose Tools > Control Center - Feature Services Select the Cisco Presence Engine service and click Restart . Choose Tools > Control Center - Network Services . Select the Cisco XCP Router service and click Restart . Note Depending on which fields you edited, you may not need to restart services. Refer to the online help for information on the
                                                         fields that you edited. | Note | Depending on which fields you edited, you may not need to restart services. Refer to the online help for information on the
                                                         fields that you edited. |
| Note | Depending on which fields you edited, you may not need to restart services. Refer to the online help for information on the
                                                         fields that you edited. |

| Note | Individual Cisco Jabber users can enable or disable this setting for their own Jabber client, by reconfiguring the policy
                                                         settings within their Cisco Jabber client. |
|---|---|

| Note | Individual end users can override this setting by reconfiguring the policy settings within their Cisco Jabber client. |
|---|---|

| Note | Depending on which fields you edited, you may not need to restart services. Refer to the online help for information on the
                                                         fields that you edited. |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Messaging > Settings . |
|---|---|
| Step 2 | Check the Enable instant messaging check box. |
| Step 3 | Check the check box options that meet your deployment needs. For field descriptions, refer to the online help: Suppress offline instant messaging Allow clients to log instant message history (on supported clients only) Allow cut & paste in instant messages |
| Step 4 | Click Save . |

| Feature | Restriction |
|---|---|
| Availability Sharing | If you turn off this setting, users can view only their own availability status. Availability information is not shared to
                                          other users in the cluster. In addition, availability information received from outside the cluster is not shared either. |
| Instant Messages | If Cisco XCP Router shuts down abruptly or if the user stops/restarts it, the instant messages that were sent at the beginning
                                          or during the outage period may not be delivered to the destination user. Warning messages may not be sent to the user who
                                          sent the messages. For more details, the administrator can check for error log lines containing "Dropping packet after jsm db shutdown" at the
                                          Cisco XCP Router trace files rtr-jsm-1. |