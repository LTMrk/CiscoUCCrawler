---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-ios-10-6-7-0e12a1453d
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/ios/10_6_7/
retrieved_at: 2026-09-01T17:48:28.687270+00:00
---

# Jabber Guest iOS SDK Release - 10.6.7.855

Introduction Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco Expressway to connect with remote visitors (guests) through their website or mobile application using instant-on, real-time voice and video. Guests simply click a URL, website link, or mobile application to start the interaction. Build these capabilities into your website or mobile application with the included SDKs, or use the Jabber Guest client experiences.

New and Changed Functionality

- added BFCP Screen Share Receive

- added G.722 support

To upgrade the SDK framework Please delete the Jabber Guest SDK Framework and the bundle and do a clean before trying to build your iOS application.

API updates CJGuestCallViewController object -- added property: BOOL confirmBeforeHangupDuringScreenShare; -- added methods: appWillResignActive: and appDidBecomeActive: to handle UIApplicationWillResignActiveNotification and UIApplicationDidBecomeActiveNotification internally

CJGuestCallBarView object -- added property: BOOL confirmBeforeHangupDuringScreenShare;

CJGuestCall object — added properties: UIImageView * remotePresoView; CGSize remotePresoSize; BOOL remotePresoActive; BOOL remotePresoStarted; — added notifications: CJGuestCallRemotePresoVideoResolutionNotification CJGuestCallRemotePresoVideoActiveNotification CJGuestCallRemotePresoVideoStartedNotification

Samples No new samples.

Open Defects MPVolumeView no longer controls the volume under iOS 7 and later

Resolved Defects None