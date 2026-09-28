---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-android-10-6-7-e5e765f5db
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/android/10_6_7/
retrieved_at: 2026-09-01T17:47:14.880482+00:00
---

# Jabber Guest for Android SDK Release - 10.6.7.331

Introduction

Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco Expressway to connect with remote visitors (guests) through their website or mobile application using instant-on, real-time voice and video. Guests simply click a URL, website link, or mobile application to start the interaction. Build these capabilities into your website or mobile application with the included SDKs, or use the Jabber Guest client experiences.

New and Changed Functionality

BFCP Receive support during an active call G.722 support Support for Android 5.1 (API 22) CallBarView - Will now programmatically determine where to draw KeypadView (above / below) based on available space CallFragment - New MenuItem for display of active call statistics available.  During an active call, this can be activated to show more detailed information about the audio and video statistics of the current call.

API Changes (refer to API Guide documentation for more details)

JabberGuestCallActivity - setEnableConfirmEndCallDialog(boolean) When a user ends an active call and they are currently viewing a remote screen share, should a dialog be shown to confirm they want to end the call (by default this is disabled and must be explicitly enabled before starting any call to be active).

BaseFragment - setEnableConfirmEndCallDialog(boolean) When a user ends an active call and they are currently viewing a remote screen share, should a dialog be shown to confirm they want to end the call (by default this is disabled and must be explicitly enabled before starting any call to be active).

CallBarView - setEnableConfirmEndCallDialog(boolean) When a user ends an active call and they are currently viewing a remote screen share, should a dialog be shown to confirm they want to end the call (by default this is disabled and must be explicitly enabled before starting any call to be active).

CallBarView - Buttons to include can be configured via XML layout (jgsdk:buttons attribute) now as well as programmatically

DataView - New class that will display remote screen shares during an active call.  Included by default with CallFragment.

JabberGuestCall - Two new CallControlEvent enum values:  remoteScreenShareStarted and remoteScreenShareEnded

JabberGuestCall - setRemoteScreenShareTextureView(TextureView) Provides the JabberGuestCall object with a TextureView to display remote screen share frames when a share is started.

JabberGuestCall - setRemoteScreenShareTextureView(TextureView, RenderCallbacks) Provides the JabberGuestCall object with a TextureView to display remote screen share frames when a share is started, and an implementation of the RenderCallbacks interface to communicate state changes with respect to that remote screen share media.

JabberGuestCall - isRemoteScreenShareActive() Can be used to determine whether or not the current active call is viewing a remote screen share.

PreviewFragment - resetUI() Will reset the PreviewFragment to its initial state (Remove any active spinners and re-enable the call button)

Samples

Remote Share Sample - A custom application showing how to use the DataView for the Remote Screen share feature.

South Beach Bank Sample - A sample online banking application with integrated call buttons to show how to integrate calling functionality into an app. Please follow the ReadMe.txt to enable the calling functionality.

Open Defects

Pressed state of OK button on Jabber Guest End Call dialog does not have rounded corners

Resolved Defects

Bypassing SHOW_PREVIEW results in a failed call because MPEG-LA dialog is not displayed for activation. Sample apps do not release camera lock when app put in background SDK: Keypad not displayed if Call Control Bar is not at bottom of screen. SDK: Can't start Jabber Guest app with rear facing camera SDK: Call bar view cannot be customized with xml SDK: PreviewFragment - If user override onCallClick() and handle the click themself, the progress bar still visible and call button still disabled. Preview/PreviewFragment - Won't show selfview video in the case where both the invalid certificate dialog box and video license dialog box need to show at the same time. MPEG-LA dialog box not fully displayed on Samsung Galaxy S2