---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-ios-10-5-4-bee2444726
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/ios/10_5_4/
retrieved_at: 2026-09-01T17:48:33.092739+00:00
---

# Jabber Guest iOS SDK Release - 10.5.4

Introduction Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco Expressway to connect with remote visitors (guests) through their website or mobile application using instant-on, real-time voice and video. Guests simply click a URL, website link, or mobile application to start the interaction. Build these capabilities into your website or mobile application with the included SDKs, or use the Jabber Guest client experiences.

New and Changed Functionality This Jabber Guest for iOS SDK is a maintenance release that offers support for iOS 64-bit builds. As of Feb 1, 2015, all new App Store submissions are required to be compiled using the iOS 8 SDK, and support 64-bit architectures.

The Jabber Guest for iOS SDK is now a universal binary, containing code for both 32 and 64 bit devices.

To upgrade the SDK framework Please delete the Jabber Guest SDK Framework and the bundle and do a clean before trying to build your iOS application.

API updates There are no API updates in this release

Samples Two new Swift-based Samples are included in the SDK folder.

CJGuestCallController Swift version of the objective-C sample app , CJGuestCallController.
            CustomerSupport – Uses custom call bar view to create a Swift based sample. This is very similar to the LiveSupport sample app which is in Objective-C

Open Defects MPVolumeView no longer controls the volume under iOS 7 and later

Resolved Defects None