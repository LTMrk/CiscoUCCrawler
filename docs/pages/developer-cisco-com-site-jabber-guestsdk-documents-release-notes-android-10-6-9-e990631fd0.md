---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-android-10-6-9-e990631fd0
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/android/10_6_9/
retrieved_at: 2026-09-01T17:47:10.439069+00:00
---

# Jabber Guest for Android SDK Release - 10.6.9

Introduction

Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco Expressway to connect with remote visitors (guests) through their website or mobile application using instant-on, real-time voice and video. Guests simply click a URL, website link, or mobile application to start the interaction. Build these capabilities into your website or mobile application with the included SDKs, or use the Jabber Guest client experiences.

New and Changed Functionality

- Android Studio IDE support

- Android 6.0 support

- Automatically start call

- Start call without video

- Opus codec support

- Add screen shared statistics

- UI enhancements

API Changes (refer to API Guide documentation for more details)

JabberGuestCall - isVideoControlEnabled()

Determine if user has capability to control the local device’s video.  Return true indicating that video button is enabled (user has capability to mute/unmute local video); return false indicating that video button is disabled.

JabberGuestCall – enum AutoCallEvent

Represent the different events that take place once a auto call is either in the prepared or executed states.

JabberGuestCall – cancelAutoCall

Cancel auto call when received the event (ACTION_AUTO_CALL_EVENT), only work when delay seconds from event by ARG_AUTO_CALL_DELAY_SECS is positive & between AutoCallEvent#PREPARED and AutoCallEvent#EXECUTED.

JabberGuestCall – publishAutoCallEvent(final AutoCallEvent event)

publishAutoCallEvent(final AutoCallEvent event, String key, String value)

publishAutoCallEvent(final AutoCallEvent event, final Bundle bundle)

Trigger a callback to all registered listeners indicating that a auto call event has occurred.

Samples

No new sample

Resolved Defects

- CSCuu47954: "Launching Desktop Share" Notify is not coming when sharing presentation

- CSCut62094: Jabber Guest support to use 9443 / 9880 in URL on mobile clients

- CSCuw16229: 2nd call fails for JG Android upon relaunching it from recents history