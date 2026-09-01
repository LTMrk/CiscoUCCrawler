---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-android-10-6-10-5418bef9ce
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/android/10_6_10/
retrieved_at: 2026-09-01T17:47:06.080771+00:00
---

# Jabber Guest for Android SDK Release - 10.6.10

Introduction

Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco Expressway to connect with remote visitors (guests) through their website or mobile application using instant-on, real-time voice and video. Guests simply click a URL, website link, or mobile application to start the interaction. Build these capabilities into your website or mobile application with the included SDKs, or use the Jabber Guest client experiences.

New and Changed Functionality

- UI enhancement

- Cross-launch parameters improvement

API Changes (refer to API Guide documentation for more details)

JabberGuestCall - ACTION_SERVER_CONFIGURATION_PREPARED

Name of Intent sent to registered BroadcastReceivers when server configuration prepared.

JabberGuestCall - publishServerConfigurationPrepared

Trigger a callback to all registered listeners indicating that server configuration has already prepared.

JabberGuestCall - Two new CallControlEvent enum values: videoControlEnabled and videoControlDisabled

JabberGuestCall -  isServerConfigPrepared()

Can be used to determine whether or not the server configuration is prepared.

JabberGuestCall - isAutoCallPrepared()

Can be used to determine whether or not the auto call is prepared.

JabberGuestCall - getAutoCallDelayTime()

Can be used to retrieve delay time from Auto call prepare to Auto call execute.

Samples

No new samples.

Resolved Defects

- N/A