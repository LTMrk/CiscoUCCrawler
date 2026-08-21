---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-monitoring-guide-9-0-1-cucm-bk-m2f290d8-00-monitoring-cucm--5fc20db77b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/monitoring_guide/9_0_1/CUCM_BK_M2F290D8_00_monitoring-cucm-presence-guide-90/CUCM_BK_M2F290D8_00_monitoring-cucm-presence-guide-90_chapter_011.html
retrieved_at: 2026-08-21T01:27:11.826058+00:00
---

Monitoring Cisco Unified Communications Manager IM and Presence, Release 9.0(1)

# Monitoring Cisco Unified Communications Manager IM and Presence, Release 9.0(1)

Updated: February 19, 2013

Chapter: Performance counters

## Chapter: Performance counters

# Performance counters

## Monitor performance counters using Unified Operations Manager

Unified Operations Manager 9.0 allows the monitoring of the following counters in the following categories.

### Client connections

Counter Name

Number of connected XMPP clients

ConnectedSockets

None

Number of connected CAXL clients

WebCMConnectedSockets

None

### Database

Counter Value

Counter Name

Folder Location

Default Alert Threshold

Database Space Used

CcmDbSpace_​Used

DB Local_DSN

Yes ( > 90%)

Replication Status

Replicate_​state

Number of Replicates Created and State of Replication

None

Replication Queue Depth

ReplicationQueueDepth

Enterprise Replication Perfmon Counters

None

### Instant messaging

Counter Attribute

Counter Name

Folder Location

Default Alert Threshold

Number of Instant Message Sessions

Cisco XCP JSM

None

Total Instant Message Packets

Cisco XCP JSM

None

Instant Message Packets in the last 60 seconds

Cisco XCP JSM

None

MessagePackets Received per Session

Cisco XCP JSM Session Counters

None

Messages Sent per Session

Cisco XCP JSM Session Counters

None

Per User/Per Session counters existing for the duration of an IM session or user login.

Cisco XCP JSM Session Counters

None

### Presence

Counter Attribute

Counter Name

Folder Location

Default Alert Threshold

Number of Active JSM Sessions

Cisco Presence Engine

None

Number of Active Calendar Subscriptions

Cisco Presence Engine

None

### Process CPU usage

Counter Attribute

Counter Name

Folder Location

Default Alert Threshold

A Cisco DB CPU Usage

cmoninit

% CPU Time

Yes (CPU > 90%)

Cisco SIP Proxy CPU Usage

sipd

% CPU Time

Yes (CPU > 90%)

Cisco Tomcat CPU Usage

tomcat

% CPU Time

Yes (CPU > 90%)

Cisco Presence Engine CPU Usage

pe

% CPU Time

Yes (CPU > 90%)

Cisco XCP Router CPU Usage

jabberd

% CPU Time

Yes (CPU > 90%)

Cisco XCP Connection Manager CPU usage

cm

% CPU Time

Yes (CPU > 90%)

Cisco XCP SIP Federation Connection Manager CPU usage

cm#2

% CPU Time

Yes (CPU > 90%)

Cisco XCP XMPP Federation Connection Manager CPU usage

cm#3

% CPU Time

Yes (CPU > 90%)

Cisco XCP Web Connection Manager CPU usage

cm#1

% CPU Time

Yes (CPU > 90%)

### Process Memory usage

Counter Attribute

Counter Name

Folder Location

Default Alert Threshold

Database Memory Usage

cmoninit

VmSize

None

### SIP federation

Counter Attribute

Counter Name

Folder Location

Default Alert Threshold

Number of Active SIP Subscriptions

Cisco XCP SIP S2S

Cisco XCP SIP S2S

Yes ( > 260,000)

Number of Idle SIP Proxy Worker Processes

Cisco SIP Proxy

Yes (< 5 for 60 minutes)

### Text conferencing

Counter Attribute

Counter Name

Folder Location

Default Alert Threshold

Total Text Conferencing Rooms

Cisco XCP TC

None

Total AdHoc Group  Chat rooms

Cisco XCP TC

None

Total Persistent Chat Rooms

Cisco XCP TC

None

Room Message Packets Received

Cisco XCP TC Room Counters

None

Room Number of Occupants

Cisco XCP TC Room Counters

None

## Monitor performance counters using Unified RTMT

All IM and Presence Service counters are monitored in Unified RTMT through the Performance menu item, under the System tools:

Using Unified RTMT it is possible to create custom alerts based on the values of any Performance Counter. The following procedure is an example of creating a custom alert for Cisco SIP Proxy – NumIdleSipdWorkers.

The Alert Properties: General window opens.

The Alert Properties: Threshold & Duration window opens.

Cisco recommends that on IM and Presence Service this counter should not remain below a value of 5 for a period of 60 minutes (or 3600 seconds). For more details about this counter, see the List of Recommended Performance Counters .

The Alert Properties: Frequency & Schedule window opens.

"Trigger alert on every poll."

"Trigger Alert when it occurs (Non-Stop Monitoring)."

The Alert Properties: Email Notification window opens.

If you do not wish to receive email notifications, uncheck the Enable Email check box and proceed to Step 20 .

## Archive performance counters in Unified RTMT

- Select task Server Time Zone

- Schedule Start Date/Time

- Schedule End Date/Time

- Scheduler Frequency

- Collect Files generated in the last

When choosing an SFTP/FTP server, you must choose Test Connection to ensure your setup is correct.

You can find the CSV files by navigating down the directory structure to cm/log/ris/csv .  This unusual directory structure is necessary as it is possible to use Unified RTMT to archive many different logs in one query. It is possible to use Trace and Log collection to archive every log the server generates. Each log will have its own specific path for the sake of organization.

## List of recommended performance counters

### Client connections

- WebCMConnectedSockets

- ConnectedSockets

#### WebCMConnectedSockets

The WebCMConnectedSockets performance counter in the Cisco XCP WebCM folder contains the current number of CAXL web clients that are connected to the Cisco XCP Web Connection Manager on an individual IM and Presence Service server. This number rises and falls based on the usage patterns of your deployment. Further investigation may be required if this number is higher than expected for your user base.

#### ConnectedSockets

The ConnectedSockets performance counter in the Cisco XCP CM folder contains the current number of XMPP clients that are connected to the Cisco XCP Connection Manager on an individual IM and Presence Service server. This number rises and falls based on the usage patterns of your deployment. Further investigation may be required if this number is higher than expected for your user base.

### Database

- CcmDbSpace_Used

- ReplicationQueueDepth

- Replicate_state

#### CcmDbSpace_Used

The Database Space Used performance counter contains the percentage of ccm dbspace used. Monitor this counter for an indication of when you will run out of database space.

#### ReplicationQueueDepth

The Replication Queue Depth performance counter contains the replication queue depth. A high value is an indication of replication issues.

#### Replicate_state

### Instant messaging

#### JsmMsgsInLastSlice

The total number of IM packets handled by the IM and Presence Service node across all users in the past 60 seconds. This counter is reset to zero every 60 seconds. The same rules for counting IM packets apply as for TotalMessagePackets. Monitoring of this counter helps identify the busy IM hours in your organization.

#### JsmSessionMessagesOut

The IM Packets received per session performance counter contains the total number of IMs that are sent by the user from the user's IM client or session. Note that the term SessionMessagesIn is defined from the perspective of IM and Presence Service: the IM packet that was sent by the client is an inbound IM packet to IM and Presence Service . On large deployments of IM and Presence Service there can be many instances of this counter, and viewing individual counters in Unified RTMT can be time consuming. To get a long list of the value of this counter for every user on IM and Presence Service , use the CLI command:

show perf query counter "Cisco XCP JSM Session Counters" JsmSessionMessagesOut

JsmTotalMessagePackets , JsmMsgsInLastSlice , JsmSessionMessagesIn and JsmSessionMessagesOut each represent instant message packets being sent to IM and Presence Service and are not exact figures of Instant Messages on the system. The amount of IM packets that are sent to IM and Presence Service per IM can vary depending on the client in use.

##### Example

- A composed packet to indicate Alice is typing a new message.

- The instant message packet containing the message body.

- A paused packet to indicate the end of the communication.

In this scenario JSM counters will increment by three.

#### JsmSessionMessagesIn

The IM Packets sent per session performance counter counts the total number of IM packets that are sent to the user on the user's IM client or session. Note that the term SessionMessagesOut is defined from the perspective of IM and Presence Service: the IM packet is sent to the client and is an outbound IM packet from IM and Presence Service . On large deployments of IM and Presence Service there can be many instances of this counter, and viewing individual counters in Unified RTMT can be time consuming. To get a long list of the value of this counter for every user on IM and Presence Service use the CLI command:

#### JsmIMSessions

The Number of IM Sessions performance counter contains the total number of IM sessions on the IM and Presence Service node across all users. The Cisco Presence Engine, which provides presence composition services and rich, always-on network presence, creates an IM session on behalf of all users at Presence Engine (PE) startup time. This is necessary so that network presence events such as Cisco Unified Communications Manager Telephony Presence and Exchange Calendar notifications are reflected in a user’s presence even if that user is not logged in on any of their IM clients. Every licensed user that is assigned to an IM and Presence Service node will have one IM Session for PE rich presence composition in addition to one IM Session for any logged-in clients.

##### Example

If:

- 100 licensed users are assigned to the IM and Presence Service node.

- 50 users are not logged in.

- 40 users are logged in on one IM client.

- 10 users are logged in on two IM clients.

- 100 x 1 for rich Presence Engine sessions, plus

- 40 x 1 for users logged in on a single client, plus

- 10 x 2 for users logged in on two clients

#### Cisco XCP JSM Session Counters

The Per User/Per Session counters exist only for the duration of an IM session or user login. One set of these counters exists per Presence Engine network presence session, and one set of these counters exists per client login session. In the example given above for IM Sessions, 160 different sets of Cisco XCP JSM Session Counters would exist. When a user logs out, or when the Cisco Presence Engine is stopped, the associated Cisco XCP JSM Session Counters instance is deleted.

Administrators can use these counters to get a snapshot of all users that are currently logged in. These can be accessed by entering the following command on the CLI:

Every user that is assigned to an IM and Presence Service node that is logged in to the system will have a set of JSM session counters for their current logged-in client session and also their Presence Engine network session. On an IM and Presence Service node with 5000 users logged in, this would result in a minimum of 10,000 sets of JSM Session counters. Updating these counters with new values as they change would place the system under stress. To combat this problem, JSM Session counter values are cached locally by the system and are only updated to Unified RTMT every 30 minutes.

#### JsmTotalMessagePackets

The Total IM Packets performance counter gives the total number of IM packets that are handled by the IM and Presence Service node across all users.

##### Example

If user Alice sends an IM packet to user Bob, and both users are assigned to the same IM and Presence Service node, then this IM packet will be counted twice. This is because The Cisco XCP Router and Jabber Session Manager treat the two users separately. For example, Alice’s privacy rules will be applied to the IM packet before it is delivered to Bob, and then Bob’s privacy rules will be applied to the IM packet before it is delivered to Bob’s client. Whenever IM and Presence Service handles an IM packet, it is counted once for the originator and once for the terminator.

If Alice and Bob are assigned to different IM and Presence Service nodes and Alice sends an IM packet to Bob, then the IM packet will be counted once on Alice’s node and once on Bob’s node.

### Presence

- ActiveCalendarSubscriptions

- ActiveJsmSessions

#### ActiveCalendarSubscriptions

The Number of Active Calendar Subscriptions performance counter contains the number of calendar subscriptions that are currently active on the box.

#### ActiveJsmSessions

The Number of Active JSM Sessions performance counter contains the number of client emulation sessions between the Cisco Presence Engine and Cisco XCP Router. The value of this counter should always equal the number of licensed users on the box.

### SIP federation

#### SIPS2SSubscriptionsIn

The Number of Active Inbound SIP Subscriptions performance counter contains the current number of active inbound SIP Subscriptions that are maintained by the Cisco XCP SIP Federation Connection Manager service on the IM and Presence Service server. Monitor this counter if the IM and Presence Service server is configured for SIP Interdomain Federation or SIP Intradomain Federation.

The total combined count of SubscriptionsOut and SubscriptionsIn must not rise above 260,000 on any single IM and Presence Service server.

#### SIPS2SSubscriptionsOut

The Number of Active Outbound SIP Subscriptions performance counter contains the current number of active outgoing SIP Subscriptions being maintained by the Cisco XCP SIP Federation Connection Manager service on the IM and Presence Service server. Monitor this counter if IM and Presence Service server is configured for SIP Interdomain Federation or SIP Intradomain Federation.

The sum of the values of the SubscriptionsOut and SubscriptionsIn performance counters must not rise above 260,000 on any single IM and Presence Service server.

#### NumIdleSipdWorkers

The Number of Idle SIP Proxy Worker Processes performance counter contains the current number of idle/free SIP worker processes on the IM and Presence Service SIP Proxy. This counter gives a good indication of the load being applied to the Cisco SIP Proxy on each IM and Presence Service server. Monitor this counter if IM and Presence Service server is configured for SIP Interdomain Federation or SIP Intradomain Federation.

The number of idle processes can drop to zero on occasion and is not a cause for concern. However, if the number of idle processes is consistently below five processes, then it is an indication that the IM and Presence Service Server is being heavily loaded and requires further investigation.

#### SIPInviteRequestIn

- On a Routing IM and Presence Service server this count captures outbound INVITE requests to federated SIP contacts from IM and Presence Service users.

- All inbound INVITEs from federated SIP contacts to users that are provisioned on the IM and Presence Service server.

- All outbound INVITEs to federated SIP contacts from users that are provisioned on the IM and Presence Service server.

- All outbound INVITEs to local SIP clients from users that are provisioned on the IM and Presence Service server.

#### SIPMessageRequestIn

The Number of MESSAGE Requests Received performance counter is a cumulative count of the number of SIP MESSAGE requests arriving into the Cisco SIP Proxy since the service was last started. This is useful on the Routing IM and Presence Service server in terms of understanding the rate of IMs that are associated with SIP and federated SIP conversations. Depending on the role of the IM and Presence Service server, these SIP MESSAGE requests can come from multiple sources.

- On a Routing IM and Presence Service server this count captures outbound MESSAGE requests to federated SIP contacts from IM and Presence Service users.

- All inbound MESSAGE requests from federated SIP contacts to users that are provisioned on the IM and Presence Service server.

- All outbound MESSAGE requests to federated SIP contacts from users that are provisioned on the IM and Presence Service server.

- All outbound MESSAGE requests to local SIP clients from users that are provisioned on the IM and Presence Service server.

#### SIPNotifyRequestIn

- On a Routing IM and Presence Service server this count captures Outbound NOTIFY to federated SIP contacts from IM and Presence Service users.

- All inbound NOTIFY requests from federated SIP contacts to users that are provisioned on the IM and Presence Service server.

- All outbound NOTIFY requests to federated SIP contacts from users that are provisioned on the IM and Presence Service server.

- All outbound NOTIFY requests to local SIP clients from users that are provisioned on the IM and Presence Service server.

#### SIPS2SInviteIn

The Number of SIP INVITE Messages Received performance counter is a cumulative total of the number of SIP INVITE messages that were received by the Cisco XCP SIP Federation Connection Manager service since the service was last started. A SIP INVITE message arrives from each IM conversation that is initiated by a federated SIP user. So this count equates to the number of inbound IM conversations that were established since the Cisco XCP SIP Federation Connection Manager was last started.

#### SIPS2SInviteOut

The Number of SIP INVITE Messages Sent performance counter contains the total number of SIP INVITE messages that were sent out by the Cisco XCP SIP Federation Connection Manager since the service was last started. A SIP INVITE message is sent out for each IM conversation that is initiated by a Cisco Unified Personal Communicator user to a federated SIP user. So this count equates to the number of outbound IM conversations that were established since the Cisco XCP SIP Federation Connection Manager was last started.

#### Number of SIP MESSAGES Received (Cisco XCP SIP S2S - SIPS2SMessagesIn)

The Number of SIP MESSAGES Received performance counter contains the total number of SIP MESSAGE packets that were received by the Cisco XCP SIP Federation Connection Manager service since the service was last started. Each Instant Message is sent in a SIP MESSAGE packet. So this count equates to the number of inbound IMs since the Cisco XCP SIP Federation Connection Manager was last started.

#### SIPS2SMessagesOut

The Number of SIP MESSAGES Sent performance counter contains the total number of SIP MESSAGE packets that were sent out by the Cisco XCP SIP Federation Connection Manager since the service was last started. Each Instant Message is sent in a SIP MESSAGE packet. So this count equates to the number of inbound IMs since the Cisco XCP SIP Federation Connection Manager was last started.

#### SIPS2SNotifyIn

The Number of SIP NOTIFY Messages Received performance counter contains the total number of SIP NOTIFY messages that were received by the Cisco XCP SIP Federation Connection Manager service since the service was last started.

#### SIPS2SNotifyOut

The Number of SIP NOTIFY Messages Sent performance counter contains the total number of SIP NOTIFY messages that were sent out from the Cisco XCP SIP Federation Connection Manager service since the service was last started.

#### SIPSubscribeRequestIn

The Number of SUBSCRIBE Requests Received performance counter contains the total number of SIP SUBSCRIBE requests arriving at the Cisco SIP Proxy service since the service was last started. This counter captures all SUBSCRIBE requests, including refresh SUBSCRIBE requests (sent every 2 hours to keep a SIP Subscription alive) and unSUBSCRIBE requests (to terminate the subscription). Depending on the role of the IM and Presence Service server, these SIP SUBSCRIBE requests can come from multiple sources.

- On a Routing IM and Presence server, this count captures outbound SUBSCRIBE requests to federated SIP contacts from IM and Presence users.

- All inbound SUBSCRIBE requests from federated SIP contacts to users that are provisioned on the IM and Presence server.

- All outbound SUBSCRIBE requests to federated SIP contacts from users that are provisioned on the IM and Presence server.

- All outbound SUBSCRIBE requests to local SIP clients from users that are provisioned on the IM and Presence server.

#### Sip_Tcp_Requests

The Number of TCP Requests Received performance counter contains a time-sliced count of the number of generic SIP packets arriving per second at the Cisco SIP Proxy over TCP connections, regardless of type. This includes any SIP requests (SUBSCRIBE/INVITE/MESSAGE/NOTIFY/INFO, etc.) and any SIP responses (100: Trying, 200: OK, 404: Not Found, etc.). You can use it to check for spikes in activity on the IM and Presence Service SIP Proxy.

### Text conferencing

#### TCRoomMsgPacketsRecv

The IMs received per room performance counter contains the number of IMs that are received by the room. On large deployments of IM and Presence Service there can be many instances of this counter, and viewing individual counters in Unified RTMT can be time consuming. To get a long list of the value of this counter for every user on IM and Presence Service , use the CLI command:

#### TCRoomNumOccupants

The Number of occupants per room performance counter contains the current number of occupants of the chat room. For Persistent Chat rooms, monitoring the Number of occupants per room performance counter will give an indication of the room's usage trend. On large deployments of IM and Presence there can be many instances of this counter and viewing individual counters in Unified RTMT can be time consuming. To get a long list of the value of this counter for every user on IM and Presence use the CLI command:

show perf query counter "Cisco XCP TC Room Counters" TCRoomNumOccupants

It is possible to have a maximum of 16,500 Text Conferencing rooms on a IM and Presence Service node. Each of these rooms will have its own set of Per Chat Room counters. In a similar fashion to JSM Session counters, updating these with new values as they change would place the system under stress. To reduce the stress, Per Chat Room counter values are cached locally by the system and only updated to Unified RTMT every 30 minutes.

#### Cisco XCP TC Room Counters

Per Chat Room performance counters only exist for the lifetime of a chat room. For ad hoc chat rooms, these counter instances will be destroyed when the ad hoc chat room is destroyed. For persistent chat rooms, the counter instances will also be destroyed when the persistent chat room is destroyed; however, persistent chat rooms are long lived, so they should rarely be destroyed.

Per Chat Room counters can be used to monitor the usage and participants in persistent (and ad hoc) chat rooms over their lifetime and can help identify persistent chat rooms that are no longer being used frequently.

Administrators can use Per Chat Room counters to get a snapshot of all rooms that are currently hosted on the node. These can be accessed by using the following CLI command:

#### TcAdHocRooms

The Total ad hoc Group Chat Rooms performance counter contains the total number of ad hoc chat rooms that are currently hosted on the node. Note that ad hoc chat rooms are automatically destroyed when all users leave the room, so this counter should rise and fall in value regularly.

#### TcPersistentRooms

The Total Persistent Chat Rooms performance counter contains the total number of persistent chat rooms hosted on the node. Persistent chat rooms must be explicitly destroyed by the room owner. This counter can be monitored to identify if the total number of persistent chat rooms is very large and also to help identify if some persistent chat rooms are not being used regularly anymore.

#### TcTotalRooms

The Total Text Conferencing Rooms performance counter contains the total number of Text Conferencing rooms that are hosted on the node. This includes both ad hoc rooms and persistent chat rooms.

| Counter Value | Counter Name | Folder Location | Default Alert Threshold |
|---|---|---|---|
| Number of connected XMPP clients | ConnectedSockets | Cisco XCP CM | None |
| Number of connected CAXL clients | WebCMConnectedSockets | Cisco XCP WebCM | None |

| Counter Value | Counter Name | Folder Location | Default Alert Threshold |
|---|---|---|---|
| Database Space Used | CcmDbSpace_​Used | DB Local_DSN | Yes ( > 90%) |
| Replication Status | Replicate_​state | Number of Replicates Created and State of Replication | None |
| Replication Queue Depth | ReplicationQueueDepth | Enterprise Replication Perfmon Counters | None |

| Counter Attribute | Counter Name | Folder Location | Default Alert Threshold |
|---|---|---|---|
| Number of Instant Message Sessions | JsmIMSessions | Cisco XCP JSM | None |
| Total Instant Message Packets | JsmTotalMessagePackets | Cisco XCP JSM | None |
| Instant Message Packets in the last 60 seconds | JsmMsgsInLastSlice | Cisco XCP JSM | None |
| MessagePackets Received per Session | JsmSessionMessagesIn | Cisco XCP JSM Session Counters | None |
| Messages Sent per Session | JsmSessionMessagesOut | Cisco XCP JSM Session Counters | None |
| Per User/Per Session counters existing for the duration of an IM session or user login. | Cisco XCP JSM Session Counters | Cisco XCP JSM Session Counters | None |

| Counter Attribute | Counter Name | Folder Location | Default Alert Threshold |
|---|---|---|---|
| Number of Active JSM Sessions | ActiveJsmSessions | Cisco Presence Engine | None |
| Number of Active Calendar Subscriptions | ActiveCalendarSubscriptions | Cisco Presence Engine | None |

| Counter Attribute | Counter Name | Folder Location | Default Alert Threshold |
|---|---|---|---|
| A Cisco DB CPU Usage | cmoninit | % CPU Time | Yes (CPU > 90%) |
| Cisco SIP Proxy CPU Usage | sipd | % CPU Time | Yes (CPU > 90%) |
| Cisco Tomcat CPU Usage | tomcat | % CPU Time | Yes (CPU > 90%) |
| Cisco Presence Engine CPU Usage | pe | % CPU Time | Yes (CPU > 90%) |
| Cisco XCP Router CPU Usage | jabberd | % CPU Time | Yes (CPU > 90%) |
| Cisco XCP Connection Manager CPU usage | cm | % CPU Time | Yes (CPU > 90%) |
| Cisco XCP SIP Federation Connection Manager CPU usage | cm#2 | % CPU Time | Yes (CPU > 90%) |
| Cisco XCP XMPP Federation Connection Manager CPU usage | cm#3 | % CPU Time | Yes (CPU > 90%) |
| Cisco XCP Web Connection Manager CPU usage | cm#1 | % CPU Time | Yes (CPU > 90%) |

| Counter Attribute | Counter Name | Folder Location | Default Alert Threshold |
|---|---|---|---|
| Database Memory Usage | cmoninit | VmSize | None |

| Counter Attribute | Counter Name | Folder Location | Default Alert Threshold |
|---|---|---|---|
| Number of Active SIP Subscriptions | SIPS2SSubscriptionsOut SIPS2SSubscriptionsIn | Cisco XCP SIP S2S Cisco XCP SIP S2S | Yes ( > 260,000) |
| Number of Idle SIP Proxy Worker Processes | NumIdleSipdWorkers | Cisco SIP Proxy | Yes (< 5 for 60 minutes) |

| Counter Attribute | Counter Name | Folder Location | Default Alert Threshold |
|---|---|---|---|
| Total Text Conferencing Rooms | TcTotalRooms | Cisco XCP TC | None |
| Total AdHoc Group  Chat rooms | TcAdHocRooms | Cisco XCP TC | None |
| Total Persistent Chat Rooms | TcPersistentRooms | Cisco XCP TC | None |
| Room Message Packets Received | TCRoomMsgPacketsRecv | Cisco XCP TC Room Counters | None |
| Room Number of Occupants | TCRoomNumOccupants | Cisco XCP TC Room Counters | None |

| Step 1 | Select Performance from the Performance menu item in Unified RTMT. |
|---|---|
| Step 2 | Double-click the NumIdleSipdWorkers counter. |
| Step 3 | Select the counter graph in the main Unified RTMT pane. Figure 2. Counter graph |
| Step 4 | Right-click, select Set Alert/Properties The Alert Properties: General window opens. Figure 3. Alert Properties: General window |
| Step 5 | Ensure the Enable Alert check box is checked. |
| Step 6 | In the Description field, enter a brief description for the alert. |
| Step 7 | In the Recommended Action field, enter a brief action for the alert. |
| Step 8 | Choose a severity from the Severity drop-down menu. |
| Step 9 | Click Next . The Alert Properties: Threshold & Duration window opens. Figure 4. Alert Properties: Threshold & Duration window |
| Step 10 | In the Threshold field, specify the alerting threshold for the counter. |
| Step 11 | In the Value Calculated As field, specify how this threshold is calculated. |
| Step 12 | In the Duration field, specify duration of time that the counter value must be above or below the specified threshold before the alert is triggered. Note Cisco recommends that on IM and Presence Service this counter should not remain below a value of 5 for a period of 60 minutes (or 3600 seconds). For more details about this counter, see the List of Recommended Performance Counters . | Note | Cisco recommends that on IM and Presence Service this counter should not remain below a value of 5 for a period of 60 minutes (or 3600 seconds). For more details about this counter, see the List of Recommended Performance Counters . |
| Note | Cisco recommends that on IM and Presence Service this counter should not remain below a value of 5 for a period of 60 minutes (or 3600 seconds). For more details about this counter, see the List of Recommended Performance Counters . |
| Step 13 | Click Next . The Alert Properties: Frequency & Schedule window opens. Figure 5. Alert Properties: Frequency & Schedule window |
| Step 14 | In the Frequency field, specify the amount of times the custom alert is triggered. The default is: "Trigger alert on every poll." |
| Step 15 | In the Schedule field, specify when the alert is triggered. The default is: "Trigger Alert when it occurs (Non-Stop Monitoring)." |
| Step 16 | Click Next The Alert Properties: Email Notification window opens. Figure 6. Alert Properties: Email Notification window |
| Step 17 | To receive email notifications, ensure the Enable Email check box is checked. Note If you do not wish to receive email notifications, uncheck the Enable Email check box and proceed to Step 20 . | Note | If you do not wish to receive email notifications, uncheck the Enable Email check box and proceed to Step 20 . |
| Note | If you do not wish to receive email notifications, uncheck the Enable Email check box and proceed to Step 20 . |
| Step 18 | In the Trigger Alert Action field, use the drop-down menu to select the profile this alert will use. |
| Step 19 | In the User-defined email text field, enter a brief message for the alert. |
| Step 20 | Click Save . |

| Note | Cisco recommends that on IM and Presence Service this counter should not remain below a value of 5 for a period of 60 minutes (or 3600 seconds). For more details about this counter, see the List of Recommended Performance Counters . |
|---|---|

| Note | If you do not wish to receive email notifications, uncheck the Enable Email check box and proceed to Step 20 . |
|---|---|

| Step 1 | Open Trace and Log Collection . |
|---|---|
| Step 2 | Double-click Schedule Collection . The Schedule Collection window opens to the Select System Services/Applications table. Figure 7. Schedule Collection window |
| Step 3 | Choose the Cisco RIS Data CollectorPerfMon Log service. |
| Step 4 | To download the PerfMon logs: From... ... take this action: All nodes in the cluster Check All Servers . A single node Select the node name. | From... | ... take this action: | All nodes in the cluster | Check All Servers . | A single node | Select the node name. |
| From... | ... take this action: |
| All nodes in the cluster | Check All Servers . |
| A single node | Select the node name. |
| Step 5 | Choose Next . The Schedule Collection Options window opens. Figure 8. Schedule Collection Options window |
| Step 6 | In the Schedule Options field, configure the following drop-down menus, as desired: Select task Server Time Zone Schedule Start Date/Time Schedule End Date/Time Scheduler Frequency Collect Files generated in the last |
| Step 7 | In the Action Options field, check the Download Files check box. The Trace Download Configuration window opens. Figure 9. Trace Download Configuration window |
| Step 8 | Choose the archive location for the PerfMon logs. The default is Localhost . Note When choosing an SFTP/FTP server, you must choose Test Connection to ensure your setup is correct. | Note | When choosing an SFTP/FTP server, you must choose Test Connection to ensure your setup is correct. |
| Note | When choosing an SFTP/FTP server, you must choose Test Connection to ensure your setup is correct. |
| Step 9 | Click OK . The Trace Download Configuration window closes. |
| Step 10 | Click Finish . The Schedule Collection window closes. |

| From... | ... take this action: |
|---|---|
| All nodes in the cluster | Check All Servers . |
| A single node | Select the node name. |

| Note | When choosing an SFTP/FTP server, you must choose Test Connection to ensure your setup is correct. |
|---|---|

| Note | You can find the CSV files by navigating down the directory structure to cm/log/ris/csv .  This unusual directory structure is necessary as it is possible to use Unified RTMT to archive many different logs in one query. It is possible to use Trace and Log collection to archive every log the server generates. Each log will have its own specific path for the sake of organization. |
|---|---|