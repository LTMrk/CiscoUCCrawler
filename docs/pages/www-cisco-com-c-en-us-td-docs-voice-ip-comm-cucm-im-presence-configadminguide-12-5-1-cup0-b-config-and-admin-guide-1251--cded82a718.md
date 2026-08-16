---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-cup0-b-config-and-admin-guide-1251--cded82a718
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1/cup0_b_config-and-admin-guide-1251/cup0_b_config-and-admin-guide-1251_chapter_010101.html
retrieved_at: 2026-08-16T16:43:30.789427+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)

Updated: November 27, 2024

Chapter: Configure Advanced Features

## Chapter: Configure Advanced Features

# Configure Advanced Features

## Stream Management

The IM and Presence Service supports Stream Management for instant messaging. Stream Management is implemented using the XEP-0198
                              specification, which defines an Extensible Messaging and Presence Protocol (XMPP) extension for active management of an XML
                              stream between two XMPP entities, including features for stanza acknowledgements and stream resumption. For more information
                              about XEP-0198, see the specification at http://xmpp.org/extensions/xep-0198.html

If there is a temporary loss of communication between IM and Presence Service and Cisco Jabber, Stream Management ensures
                              that any instant messages that are sent during the communications outage are not lost. A configurable timeout period determines
                              how such messages are handled:

If Cisco Jabber reestablishes communication with IM and Presence Service within the timeout period, the messages are resent.

If Cisco Jabber does not reestablish communication with IM and Presence Service within the timeout period, the messages are
                                    returned to the sender.

Messages that are sent after the timeout period lapses are stored offline and delivered when Cisco Jabber resumes communication
                                    with IM and Presence Service.

Stream Management is enabled by default on a cluster-wide basis. However, you can use the Stream Management service parameters
                              to configure the feature.

### Configure Stream Management

Use this procedure to cofigure Stream Management (XEP-0198) on the IM and Presence Service.

Step 1

From Cisco Unified CM IM and Presence Administration, choose System > Service Parameters .

Step 2

From the Server drop-down, choose an IM and Presence node.

Step 3

From the Service drop-down, choose Cisco XCP Router .

Step 4

Set the Enable Stream Management service parameter to Enabled .

Step 5

Under Stream Management Parameters (Clusterwide) , configure any of the Stream Management  parameters:

Service Parameter

Description

Enable Stream Management

Enables or disables Stream Management cluster-wide. The default setting is Enabled.

Stream Management Timeout

The timeout controls how long a session (whose connection has been severed) will allow for a resume (in seconds) before giving
                                                         up. If the client attempts to negotiate a longer timeout (or does not specify a desired timeout) this maximum will apply.

Any messages that are sent after this timeout ends and before Cisco Jabber logs in again with IM and Presence Service are
                                                         stored offline and resent after relogin.

The range is 30 seconds—90 seconds. The default value is 60 seconds.

Stream Management Buffer

Defines the maximum number of packets (packet history) that will be kept in buffer for a stream management-enabled session.
                                                         A stream resume will fail if the client needs more history than what is available in the buffer.

The range is 5—150 packets with a default value of 100 packets.

Acknowledgement Request Rate

Defines the number of stanzas that the server sends before asking the client to provide the count of the last stanza received.
                                                         A smaller number makes for more network traffic, but helps the server prune the stanza history buffer and reduces memory used.

The range is 1—64 stanzas with a default value of 5.

Step 6

Click Save .

## Calendar Integration with Microsoft Outlook

This feature allows users to incorporate their
                              calendar and meeting status from Microsoft Outlook into their
                              Presence status on the IM and Presence Service server. If a
                              user is in a meeting, that status will display as a part of the
                              user's Presence status. This feature can be configured by
                              connecting the IM and Presence Service to an on-premises
                              Microsoft Exchange server or to a hosted Office 365 server.

For details on how to configure calender integration with
                              Microsoft Outlook, refer to the document Calendar Integration with
                                 Microsoft Outlook for the IM and Presence Service at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-and-configuration-guides-list.html .

## Federation

On IM and Presence Service, you can create federated networks from within any domain that IM and Presence Service manages.
                              There are two main types of Federation deployments:

Interdomain Federation—This integration enables users from within any domain that 
                                    
                                    IM and Presence Service manages to exchange availability information and Instant Messaging
                                    (IM) with users in external domains. The external domain may be managed by a Microsoft, Google, IBM, or AOL server. IM and
                                    Presence Service can use a variety of protocols to communicate with the server in the external domain.

Partitioned Intradomain Federation—With this integration, IM and Presence Service and the Microsoft server (for example, Microsoft
                                    Lync) host a common domain or set of domains. The integration allows IM and Presence Service client users and Microsoft Lync
                                    users within a single enterprise to exchange instant messaging and availability.

For configuration information, see the Interdomain Federation for IM and Presence Service on Cisco Unified Communications Manager or the Partitioned Intradomain Federation for IM and Presence Service on Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-and-configuration-guides-list.html .

## Message Archiver

Many industries require that instant messages adhere to the same regulatory compliance guidelines as for all other business
                              records. To comply with these regulations, your system must log and archive all business records, and the archived records
                              must be retrievable.

The IM and Presence Service supports instant messaging (IM) compliance by collecting data for the following IM activities
                              in single cluster, intercluster, or federated network configurations:

Point-to-point messages.

Group chat - This includes ad-hoc, or temporary chat messages, and permanent chat messages.

IM Compliance Components

Sample Topologies and Message Flow for IM Compliance

For more information on configuring IM Compliance, see Instant Messaging Compliance for IM and Presence Service on Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-and-configuration-guides-list.html .

## Remote Call Control

Microsoft Remote Call Control (RCC) allows enterprise users to control their Cisco Unified IP Phone or Cisco IP Communicator
                              Phone through Microsoft Lync, a third-party desktop instant-messaging (IM) application. When a user signs in to the Microsoft
                              Lync client, the Lync server sends instructions, through the IM and Presence Service node, to the Cisco Unified Communications
                              Manager to set up, tear down and maintain calling features based on a user's action at the Lync client.

For more information on configuring Remote Call Control, see Remote Call Control with Microsoft Lync Server for IM and Presence Service on Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-and-configuration-guides-list.html .

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down, choose an IM and Presence node. |
| Step 3 | From the Service drop-down, choose Cisco XCP Router . |
| Step 4 | Set the Enable Stream Management service parameter to Enabled . |
| Step 5 | Under Stream Management Parameters (Clusterwide) , configure any of the Stream Management  parameters: Table 1. Stream Management Service Parameters Service Parameter Description Enable Stream Management Enables or disables Stream Management cluster-wide. The default setting is Enabled. Stream Management Timeout The timeout controls how long a session (whose connection has been severed) will allow for a resume (in seconds) before giving
                                                         up. If the client attempts to negotiate a longer timeout (or does not specify a desired timeout) this maximum will apply. Any messages that are sent after this timeout ends and before Cisco Jabber logs in again with IM and Presence Service are
                                                         stored offline and resent after relogin. The range is 30 seconds—90 seconds. The default value is 60 seconds. Stream Management Buffer Defines the maximum number of packets (packet history) that will be kept in buffer for a stream management-enabled session.
                                                         A stream resume will fail if the client needs more history than what is available in the buffer. The range is 5—150 packets with a default value of 100 packets. Acknowledgement Request Rate Defines the number of stanzas that the server sends before asking the client to provide the count of the last stanza received.
                                                         A smaller number makes for more network traffic, but helps the server prune the stanza history buffer and reduces memory used. The range is 1—64 stanzas with a default value of 5. Note A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. | Service Parameter | Description | Enable Stream Management | Enables or disables Stream Management cluster-wide. The default setting is Enabled. | Stream Management Timeout | The timeout controls how long a session (whose connection has been severed) will allow for a resume (in seconds) before giving
                                                         up. If the client attempts to negotiate a longer timeout (or does not specify a desired timeout) this maximum will apply. Any messages that are sent after this timeout ends and before Cisco Jabber logs in again with IM and Presence Service are
                                                         stored offline and resent after relogin. The range is 30 seconds—90 seconds. The default value is 60 seconds. | Stream Management Buffer | Defines the maximum number of packets (packet history) that will be kept in buffer for a stream management-enabled session.
                                                         A stream resume will fail if the client needs more history than what is available in the buffer. The range is 5—150 packets with a default value of 100 packets. | Acknowledgement Request Rate | Defines the number of stanzas that the server sends before asking the client to provide the count of the last stanza received.
                                                         A smaller number makes for more network traffic, but helps the server prune the stanza history buffer and reduces memory used. The range is 1—64 stanzas with a default value of 5. Note A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. | Note | A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. |
| Service Parameter | Description |
| Enable Stream Management | Enables or disables Stream Management cluster-wide. The default setting is Enabled. |
| Stream Management Timeout | The timeout controls how long a session (whose connection has been severed) will allow for a resume (in seconds) before giving
                                                         up. If the client attempts to negotiate a longer timeout (or does not specify a desired timeout) this maximum will apply. Any messages that are sent after this timeout ends and before Cisco Jabber logs in again with IM and Presence Service are
                                                         stored offline and resent after relogin. The range is 30 seconds—90 seconds. The default value is 60 seconds. |
| Stream Management Buffer | Defines the maximum number of packets (packet history) that will be kept in buffer for a stream management-enabled session.
                                                         A stream resume will fail if the client needs more history than what is available in the buffer. The range is 5—150 packets with a default value of 100 packets. |
| Acknowledgement Request Rate | Defines the number of stanzas that the server sends before asking the client to provide the count of the last stanza received.
                                                         A smaller number makes for more network traffic, but helps the server prune the stanza history buffer and reduces memory used. The range is 1—64 stanzas with a default value of 5. Note A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. | Note | A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. |
| Note | A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. |
| Step 6 | Click Save . |

| Service Parameter | Description |
|---|---|
| Enable Stream Management | Enables or disables Stream Management cluster-wide. The default setting is Enabled. |
| Stream Management Timeout | The timeout controls how long a session (whose connection has been severed) will allow for a resume (in seconds) before giving
                                                         up. If the client attempts to negotiate a longer timeout (or does not specify a desired timeout) this maximum will apply. Any messages that are sent after this timeout ends and before Cisco Jabber logs in again with IM and Presence Service are
                                                         stored offline and resent after relogin. The range is 30 seconds—90 seconds. The default value is 60 seconds. |
| Stream Management Buffer | Defines the maximum number of packets (packet history) that will be kept in buffer for a stream management-enabled session.
                                                         A stream resume will fail if the client needs more history than what is available in the buffer. The range is 5—150 packets with a default value of 100 packets. |
| Acknowledgement Request Rate | Defines the number of stanzas that the server sends before asking the client to provide the count of the last stanza received.
                                                         A smaller number makes for more network traffic, but helps the server prune the stanza history buffer and reduces memory used. The range is 1—64 stanzas with a default value of 5. Note A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. | Note | A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. |
| Note | A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. |

| Note | A smaller Acknowledgement Request Rate leads to increased network traffic, but reduced memory use. |
|---|---|