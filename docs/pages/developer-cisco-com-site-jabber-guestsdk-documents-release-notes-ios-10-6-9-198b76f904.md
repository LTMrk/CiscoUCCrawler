---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-ios-10-6-9-198b76f904
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/ios/10_6_9/
retrieved_at: 2026-09-01T17:48:20.008609+00:00
---

# Jabber Guest iOS SDK Release - 10.6.9

Introduction

Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco Expressway to connect with remote visitors (guests) through their website or mobile application using instant-on, real-time voice and video. Guests simply click a URL, website link, or mobile application to start the interaction. Build these capabilities into your website or mobile application with the included SDKs, or use the Jabber Guest client experiences.

New and Changed Functionality

- iOS 9 SDK support

- IPv6 support (Meet Apple requirements)

- Automatically start call

- Start call without video

- Opus codec support

- Add screen shared statistics

- UI enhancements

To upgrade the SDK framework

- Please delete the Jabber Guest SDK Framework and the bundle and do a clean before trying to build your iOS application.

- Add VideoToolbox.framework to your Xcode project.

- Disable bitcode in your Xcode project: Build settings -> Enable Bitcode -> Select No

API updates (Refer to API Guide documentation for more details)

CJGuestCall object

-- added property:

id <CJGuestServerConfiguraionCallDelegate> autoStartCallDelegate

BOOL videoControlEnabled

-- added notification:

CJGuestCallSelfVideoActiveNotification

-- added protocol:

CJGuestServerConfiguraionCallDelegate protocol

-(void) serverConfiguraionDidRetriveWithScheduledCallInfo:(NSInteger)secs;

-(void) scheduledCallDidExecute;

Samples

No new samples.

Resolved Defects

- CSCut62094: Jabber Guest support to use 9443 / 9880 in URL on mobile clients