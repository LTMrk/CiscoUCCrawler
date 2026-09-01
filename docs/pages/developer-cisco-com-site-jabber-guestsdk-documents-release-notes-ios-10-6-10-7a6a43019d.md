---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-ios-10-6-10-7a6a43019d
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/ios/10_6_10/
retrieved_at: 2026-09-01T17:48:15.590202+00:00
---

# Jabber Guest iOS SDK Release - 10.6.10

Introduction

Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco Expressway to connect with remote visitors (guests) through their website or mobile application using instant-on, real-time voice and video. Guests simply click a URL, website link, or mobile application to start the interaction. Build these capabilities into your website or mobile application with the included SDKs, or use the Jabber Guest client experiences.

New and Changed Functionality

- UI enhancement

- Cross-launch parameters improvement

- Fix crash issue on 32bit device

To upgrade the SDK framework

- Please delete the Jabber Guest SDK Framework and the bundle and do a clean before trying to build your iOS application.

- Add Video Toolbox framework.

- Disable bitcode in Enable Bitcode option.

API updates (Refer to API Guide documentation for more details)

CJGuestServerConfiguraionCallDelegate

-add new callback method:

–(void) allServerConfigurationDidRetrieve:

which is called when all configurations from server are retrieved.

-change callback behavior:

-(void) serverConfigurationDidRetriveWithScheduledCallInfo:(NSInteger)secs;

which was for all configurations ready but is for pre-fetched automatically call parameters.

Samples

No new samples.

Resolved Defects

- CSCuy11808: Jabber Guest client crashes on some iPhone models