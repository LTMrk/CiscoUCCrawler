---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-ios-11-2-1-ad32e4990a
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/ios/11_2_1/
retrieved_at: 2026-09-01T17:47:36.458476+00:00
---

# Jabber Guest iOS SDK Release - 11.2.1

Introduction Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco Expressway to connect with remote visitors (guests) through their website or mobile application using instant-on, real-time voice and video. Guests simply click a URL, website link, or mobile application to start the interaction. Build these capabilities into your website or mobile application with the included SDKs, or use the Jabber Guest client experiences.

New and Changed Functionality

- Built with iOS 12.1 SDK

- Support 64-bit architectures

To upgrade the SDK framework Please delete the Jabber Guest SDK Framework and the bundle and do a clean before trying to build your iOS application.

API updates(Refer to API Guide documentation for more details) NA

Samples New sample code to demonstrate low level call API for ring back tone support

Resolved Defects

- CSCvr34973: Jabber guest client does not working anymore iOS version 13

- CSCvr45197: JabberGuest Client does not send video on iOS 13