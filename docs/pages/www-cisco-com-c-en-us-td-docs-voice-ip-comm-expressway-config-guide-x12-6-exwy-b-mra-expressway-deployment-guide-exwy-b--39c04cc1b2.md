---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-6-exwy-b-mra-expressway-deployment-guide-exwy-b--39c04cc1b2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-6/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_01011.html
retrieved_at: 2026-08-16T15:35:21.536654+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

Updated: June 3, 2020

Chapter: Push Notifications Support (Optional)

## Chapter: Push Notifications Support (Optional)

# Push Notifications Support (Optional)

## Push Notifications (APNS) Prerequisites and Recommendations

Apple Push Notifications apply for users with compatible Cisco Jabber and Webex Teams iOS devices who sign in remotely. Expressway deployments that are configured for MRA can support Apple's
                           cloud-based Push Notification Service (APNS). From X8.9.1, we support Push Notifications for IM and Presence Service instant messages. From X8.10, we support voice and video calls too.

Apple Push Notifications are used for Jabber for iPhone and iPad clients as well as Webex Teams on iPhone and iPad clients. Windows, and Mac users are unaffected.

From X12.6, we support Android Push Notifications to Cisco Jabber for Android devices as well as Webex Teams on Android (subject
                           to compatible software versions on the devices and the IM and Presence Service). Depending on the software version this feature may be available in preview/demonstration mode only (the latest release notes detail its current status).

If Unified CM detects a remote or mobile Jabber for iPhone and iPad connection, it always sends a Push Notification as well as a SIP Invite.

No specific configuration is needed on the Expressway for Push Notifications, assuming Expressway-E is already providing Mobile
                           and Remote Access (MRA) for Jabber iOS devices. However, these prerequisites and recommendations apply:

Push Notifications in the Expressway require a network connection between Cisco Jabber and the Push Notification servers in
                                 the Apple cloud.

They cannot work in a private network, with no internet connection.

Expressway is already providing Mobile and Remote Access for Jabber for iPhone and iPad . MRA must be fully configured (domain, zone, server settings).

Depending on your Unified CM configuration, you may need a forward proxy to send Push Notifications to the Cisco Collaboration Cloud .

We recommend using self-describing token authorization.

Expressway-E restart required for Push Notifications with instant messages. After you enable Push Notifications on the IM and Presence Service you need to restart the Expressway-E. Until the restart, Expressway-E cannot recognize the push capability on IM and Presence Service , and does not send PUSH messages to the Jabber clients.

You need the following Push Notification-enabled software versions, or later:

Expressway X8.10.1

Cisco Jabber iOS 11.9

Cisco Unified Communications Manager 11.5(SU3)

Cisco Unified Communications Manager IM and Presence Service 11.5(SU3)

Cisco Unity Connection 11.5(SU3)

### Why Have We Implemented Support for Push Notifications?

Apple now deprecates the VoIP Background Mode that allows Jabber iOS to keep a SIP session open even when the app is running
                              in the background. Push Notifications allow Unified CM to tell Jabber about incoming calls and messages. Then Jabber can reconnect to Unified CM to retrieve the message or answer the call. Jabber uses the new self-describing token feature to help it to do this quickly.

## Push Notifications in Unified Communications Products

For information about Push Notifications in Unified CM and IM and Presence Service , see Deploying Push Notifications for Cisco Jabber on iPhone and iPad with Cisco Unified Communication Manager available from the Cisco Unified Communications Manager documentation pages on Cisco.com.

## Configure Push Notifications in Expressway

Configure OAuth token validation on the Expressway (see Configure MRA Access Control ).

Configure Unified CM to use a forward proxy server (depending on your requirements for external requests from iOS devices) and make HTTPS connections
                                       with Cisco's cloud services.

| Note | If Unified CM detects a remote or mobile Jabber for iPhone and iPad connection, it always sends a Push Notification as well as a SIP Invite. |
|---|---|

| Note | The above image illustrates the message flow for Apple Push Notifications. With Android Push Notifications, the ougoing notification
                                    goes to the Android Push Notification service, which exists in the Google cloud. |
|---|---|

| Note | The former built-in forward proxy in Expressway is removed from the product in X12.6.2 and later versions. For earlier Expressway
                                       versions, the built-in forward proxy is not supported and should not be used. |
|---|---|

| Step 1 | Configure OAuth token validation on the Expressway (see Configure MRA Access Control ). |
|---|---|
| Step 2 | Configure Unified CM to use a forward proxy server (depending on your requirements for external requests from iOS devices) and make HTTPS connections
                                       with Cisco's cloud services. |