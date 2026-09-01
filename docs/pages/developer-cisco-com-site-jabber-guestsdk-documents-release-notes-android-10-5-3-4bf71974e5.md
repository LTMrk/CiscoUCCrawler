---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-android-10-5-3-4bf71974e5
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/android/10_5_3/
retrieved_at: 2026-09-01T17:47:19.256629+00:00
---

# Jabber Guest for Android SDK Release - 10.5.3

Introduction

Cisco Jabber Guest is a consumer-to-business (C2B) solution that extends the reach of Cisco's enterprise telephony to people outside of a corporate firewall who do not have phones registered with Cisco Unified Communications Manager. Cisco Jabber Guest lets you connect with visitors through your web site or mobile application to talk with one or more of your employees through instant-on, real-time voice and video.

New Functionality

This is the first release of the Jabber Guest SDK for Android and contains the following content.

- Feature alignment with Jabber Guest SDK for iOS 10.5 (with the exception of HD transmit support)

- Support for Android versions 4.0.3 – 5.0.1 (API 15 – API 21).

- SDK documentation and sample apps

Open Defects/Limitations:

SDK: MPEG-LA dialog runs off edge of screen on lower density devices (hdpi/mdpi) SDK: KeypadView can only be displayed if CallBarView is at the bottom of the screen and the KeypadView has room above it to be visible SDK: Can’t set the rear facing camera as the active camera on intial start-up. SDK: Local camera views may become unresponsive and stop showing video. Sample App: Keypad view overlaps the call bar on some devices. Browser Issues: Firefox and Opera mobile browsers do not redirect user to the Play Store to download Jabber Guest if it is not installed. If the Jabber Guest app is already installed on your mobile device, Opera will redirect correctly to the app, but Firefox will not. Newer versions of the Android Chrome Browser (v40+) won't cross launch non-Google apps when a url is manually typed into the browser. A link must be clicked on devices that have Chrome running as the default browser to launch Jabber Guest.