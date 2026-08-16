---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-5-exwy-b-mra-expressway-deployment-guide-exwy-b--56f3b50d97
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-5/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_01011.html
retrieved_at: 2026-08-16T15:36:24.596743+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

Updated: May 1, 2019

Chapter: APNS Support (Optional)

## Chapter: APNS Support (Optional)

# APNS Support (Optional)

## Apple Push Notifications (APNS) Prerequisites and Recommendations

Apple Push Notifications apply for users with compatible Cisco Jabber iOS devices who sign in remotely. Expressway deployments that are configured for MRA can support Apple's cloud-based Push
                           Notification Service (APNS). From X8.9.1, we support Push Notifications for IM and Presence Service instant messages. From X8.10, we support voice and video calls too.

Push Notifications are only used for Jabber for iPhone and iPad (and Cisco Jabber for Android clients from X12.6). Windows, and Mac users are unaffected.

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

## Configure Apple Push Notifications in Expressway

Although the built-in forward proxy is in the Expressway interface, it is not currently supported and it should not be used.

Configure OAuth token validation on the Expressway (see Configure MRA Access Control ).

Configure Unified CM to use a forward proxy server (depending on your requirements for external requests from iOS devices) and make HTTPS connections
                                       with Cisco's cloud services.

| Note | If Unified CM detects a remote or mobile Jabber for iPhone and iPad connection, it always sends a Push Notification as well as a SIP Invite. |
|---|---|

| Caution | Although the built-in forward proxy is in the Expressway interface, it is not currently supported and it should not be used. |
|---|---|

| Step 1 | Configure OAuth token validation on the Expressway (see Configure MRA Access Control ). |
|---|---|
| Step 2 | Configure Unified CM to use a forward proxy server (depending on your requirements for external requests from iOS devices) and make HTTPS connections
                                       with Cisco's cloud services. |