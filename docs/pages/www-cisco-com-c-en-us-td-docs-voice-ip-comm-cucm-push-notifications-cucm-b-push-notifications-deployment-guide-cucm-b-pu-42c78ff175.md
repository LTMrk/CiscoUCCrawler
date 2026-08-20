---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-push-notifications-cucm-b-push-notifications-deployment-guide-cucm-b-pu-42c78ff175
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/push_notifications/cucm_b_push-notifications-deployment-guide/cucm_b_push-notifications-deployment-guide_chapter_010.html
retrieved_at: 2026-08-20T15:56:43.330687+00:00
---

Push Notifications Deployment Guide

# Push Notifications Deployment Guide

Updated: August 20, 2024

Chapter: Push Notifications (Cloud Deployment)

## Chapter: Push Notifications (Cloud Deployment)

- Push Notifications (Cloud Deployment)

- Cloud Deployments with Webex Messenger

# Push Notifications (Cloud Deployment)

## Cloud Deployments with Webex Messenger

At startup, Cisco Jabber or Cisco Webex for Android and iOS clients register both to Cisco WebEx Messenger and to the Apple
                              cloud. If a Cisco Jabber or Cisco Webex for Android and iOS clients moves into the background, the standard communication
                              channel from Webex Messenger to Cisco Jabber or Cisco Webex becomes unavailable. Push Notifications provides an alternative
                              channel to reach the Jabber client.

For instant messages, an IM notification gets sent to the Cisco Jabber or Cisco Webex clients client via the Apple cloud.
                              When the user clicks the IM notification, the Cisco Jabber or Cisco Webex clients moves back into the foreground, resumes
                              the session with Webex Messenger, and downloads the instant message.

For voice and video calls, the call gets sent to the Cisco Jabber or Cisco Webex clients through the Apple cloud. When the
                              Cisco Cisco Jabber or Cisco Webex clients receives the push notification, the client moves back to the foreground and the
                              client rings.

### Push Notifications Configuration

For IM-only cloud deployments, no configuration is required to enable Push Notifications–Webex Messenger supports Push Notifications
                              for Cisco Jabber or Cisco Webex for Android and iOS clients by default.

To add voice and video call support, you must onboard an on-premise Unified Communications Manager for Push Notifications. For details, refer to the prerequisites and configuration tasks in the chapter Push Notifications (On-Premises Deployments) .

For general Cisco Webex Messenger setup, see the Cisco Webex Messenger Administration Guide .

### Terminated Push Notifications for Cloud Deployments

If Webex Messenger shuts down gracefully, a terminated push notification gets sent to the Cisco Jabber or Cisco Webex for
                              Android and iOS clients. The terminated push notification notifies the user of the server shutdown and notifies the user that
                              all queud instant messages, Presence updates, and other XMPP stanzas (for example, chat room invites) are lost. The user must
                              move Cisco Jabber or Cisco Webex back to the foreground to start a new session with Push Notifications enabled for the new
                              session.

If the Webex Messenger server fails, no terminated push notification is sent. All queued instant messages, Presence updates,
                              and XMPP stanzas that are queued on the server and waiting to be delivered to the client, are lost. The user must move Cisco
                              Jabber or Cisco Webex back to the foreground to begin a new session with Push Notifications enabled in the new session.

### Customers Also Viewed

- Push Notifications Deployment Guide --- Push Notifications (On-Premises Deployments)