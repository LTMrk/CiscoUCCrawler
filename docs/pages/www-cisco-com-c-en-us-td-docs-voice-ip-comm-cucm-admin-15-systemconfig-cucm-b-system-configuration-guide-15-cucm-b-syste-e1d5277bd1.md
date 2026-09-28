---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-15-systemconfig-cucm-b-system-configuration-guide-15-cucm-b-syste-e1d5277bd1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15/cucm_b_system-configuration-guide-14_chapter_01111.html
retrieved_at: 2026-08-16T16:09:07.730285+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# System Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: August 7, 2026

Chapter: Configure Push Notifications

## Chapter: Configure Push Notifications

- Configure Push Notifications

- Push Notifications Overview

- Push Notifications Configuration

# Configure Push Notifications

## Push Notifications Overview

When your cluster is enabled for Push Notifications, Unified Communications Manager and the IM and Presence Service use Google and Apple’s cloud-based Push Notification service to push notifications for voice
                              and video calls, instant message notification to Cisco Jabber or Cisco Webex on Android and iOS clients that are running in
                              suspended mode (also known as background mode). Push Notifications allows your system to maintain a persistent communication
                              with Cisco Jabber or Cisco Webex. Push Notifications is required both for Cisco Jabber and Cisco Webex on Android and iOS
                              clients that connect from within the enterprise network, and for clients that register to an on-premise deployment through
                              Expressway's Mobile and Remote Access feature.

### How Push Notifications Work

At startup, clients that are installed on Android and iOS platform devices register to Unified Communications Manager , the IM and Presence Service, and to the Google and Apple cloud. With Mobile and Remote Access deployments, the clients registers
                              to the on-premises servers through Expressway. So as long as the Cisco Jabber and Cisco Webex client remains in foreground
                              mode, Unified Communications Manager , and the IM and Presence Service can send calls and instant messages to the clients directly.

However, once the Cisco Jabber or Cisco Webex clients moves to suspended mode (for example, to maintain battery life), the
                              standard communication channel is unavailable, preventing Unified Communications Manager and IM and Presence Service from communicating directly with the clients. Push Notifications provides another channel to
                              reach the clients through the partner clouds.

Cisco Jabber and Cisco Webex are considered to be running in suspended mode if any of the following conditions are true:

The Cisco Jabber or Cisco Webex application is running off-screen (in the background).

The Android or iOS device is locked.

The Android or iOS device screen is turned off.

The above diagram displays what happens when Cisco Jabber or Cisco Webex for Android and iOS clients run in the background
                              or are stopped. The figure illustrates: (1) a Mobile and Remote Access deployment where the client that connects with an on-premises Cisco Unified Communications Manager and IM and Presence Service deployment through Expressway, and (2) a Cisco Jabber or Cisco Webex for Android and iOS clients
                              that connects directly to the on-premises deployment from within the enterprise network.

As of iOS13 for Apple clients and supported Android clients, voice calls and messages use separate Push Notifications channels
                                          ('VoIP' and 'Message') to reach a client that is running in background mode. However, the general flow is the same for both
                                          channels. With iOS 12, voice calls and messages are delivered using the same channel.

### Push Notifications Behavior for Cisco Jabber and Cisco Webex

The following table describes the behavior under iOS 12 and iOS 13 for Cisco Jabber or Cisco Webex iOS clients that are registered
                              to Unified Communications Manager and the IM and Presence Service.

Cisco Jabber or Cisco Webex client is running in...

Cisco Jabber is running on an iOS12 Device

Cisco Jabber is running on an iOS13 Device or Android Device

Foreground Mode

Voice and Video Calls

Unified Communications Manager sends voice and video calls to Cisco Jabber or Cisco Webex clients directly using the standard SIP communications channel.

For calls, Unified Communications Manager also sends Push Notifications to Cisco Jabber or Cisco Webex clients that are in foreground mode. However, the standard SIP
                                          channel gets used to establish the call, rather than the Push Notifications channel.

Messages

The IM and Presence Service sends messages to the client directly using the standard SIP communication channel. For messages,
                                          Push Notifications are not sent to clients that are in foreground mode.

The behaviour is the same as with iOS12.

Background Mode

Presence

Auto-set to Away (Default) —The user presence is automatically set to Away for IM and/or Presence enabled deployments and changes to Offline for Voice
                                                Only Mode deployments.

Preserve Active Presence (Optional) —Users retain their preset manual or system presence (such as Available, Do Not Disturb, or In a Call) for IM and/or Presence
                                                enabled deployments and Voice Only Mode deployments.

Presence

Auto-set to Away (Default) —The user presence is automatically set to Away for IM and/or Presence enabled deployments and changes to Offline for Voice
                                                Only Mode deployments.

Preserve Active Presence (Optional) —Users retain their preset manual or system presence (such as Available, Do Not Disturb, or In a Call) for IM and/or Presence
                                                enabled deployments and Voice Only Mode deployments.

### Supported Clients for Push Notifications

Client

OS

Platform Cloud

Cloud Service

Cisco Jabber on iPhone and iPad

iOS

Apple

Apple Push Notification Service (APNS)

Cisco Jabber on Android

Android

Google

Android PNS Service

Webex on iOS

iOS

Apple

Apple Push Notification Service (APNS)

Webex on Android

Android

Google

Android PNS Service

## Push Notifications Configuration

For details on how to configure and deploy Push Notifications, refer to Deploying Push Notifications for Cisco Jabber on iPhone and iPad at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

| Note | Cisco Jabber and Cisco Webex are considered to be running in suspended mode if any of the following conditions are true: The Cisco Jabber or Cisco Webex application is running off-screen (in the background). The Android or iOS device is locked. The Android or iOS device screen is turned off. |
|---|---|

| Note | As of iOS13 for Apple clients and supported Android clients, voice calls and messages use separate Push Notifications channels
                                          ('VoIP' and 'Message') to reach a client that is running in background mode. However, the general flow is the same for both
                                          channels. With iOS 12, voice calls and messages are delivered using the same channel. |
|---|---|

| Cisco Jabber or Cisco Webex client is running in... | Cisco Jabber is running on an iOS12 Device | Cisco Jabber is running on an iOS13 Device or Android Device |
|---|---|---|
| Foreground Mode | Voice and Video Calls Unified Communications Manager sends voice and video calls to Cisco Jabber or Cisco Webex clients directly using the standard SIP communications channel. For calls, Unified Communications Manager also sends Push Notifications to Cisco Jabber or Cisco Webex clients that are in foreground mode. However, the standard SIP
                                          channel gets used to establish the call, rather than the Push Notifications channel. Messages The IM and Presence Service sends messages to the client directly using the standard SIP communication channel. For messages,
                                          Push Notifications are not sent to clients that are in foreground mode. | The behaviour is the same as with iOS12. |
| Background Mode | Presence Auto-set to Away (Default) —The user presence is automatically set to Away for IM and/or Presence enabled deployments and changes to Offline for Voice
                                                Only Mode deployments. Preserve Active Presence (Optional) —Users retain their preset manual or system presence (such as Available, Do Not Disturb, or In a Call) for IM and/or Presence
                                                enabled deployments and Voice Only Mode deployments. | Presence Auto-set to Away (Default) —The user presence is automatically set to Away for IM and/or Presence enabled deployments and changes to Offline for Voice
                                                Only Mode deployments. Preserve Active Presence (Optional) —Users retain their preset manual or system presence (such as Available, Do Not Disturb, or In a Call) for IM and/or Presence
                                                enabled deployments and Voice Only Mode deployments. |

| Client | OS | Platform Cloud | Cloud Service |
|---|---|---|---|
| Cisco Jabber on iPhone and iPad | iOS | Apple | Apple Push Notification Service (APNS) |
| Cisco Jabber on Android | Android | Google | Android PNS Service |
| Webex on iOS | iOS | Apple | Apple Push Notification Service (APNS) |
| Webex on Android | Android | Google | Android PNS Service |