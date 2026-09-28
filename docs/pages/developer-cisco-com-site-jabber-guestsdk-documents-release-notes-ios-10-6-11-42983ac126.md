---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-ios-10-6-11-42983ac126
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/ios/10_6_11/
retrieved_at: 2026-09-01T17:48:11.155017+00:00
---

# Jabber Guest iOS SDK Release - 10.6.11

Introduction Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco Expressway to connect with remote visitors (guests) through their website or mobile application using instant-on, real-time voice and video. Guests simply click a URL, website link, or mobile application to start the interaction. Build these capabilities into your website or mobile application with the included SDKs, or use the Jabber Guest client experiences.

New and Changed Functionality

- Introduce a new API to disable call logs at run time

To upgrade the SDK framework Please delete the Jabber Guest SDK Framework and the bundle and do a clean before trying to build your iOS application.

API updates(Refer to API Guide documentation for more details) -- added methods: setGlobalLoggingEnabled: to enable or disable logging to console and disk file

Samples No new samples.

Resolved Defects

- CSCuz53600: [iOS SDK]JG framework cause app crash

- CSCuz53297: [iOS SDK]Jabber Guest showing 150% CPU usage and crashes