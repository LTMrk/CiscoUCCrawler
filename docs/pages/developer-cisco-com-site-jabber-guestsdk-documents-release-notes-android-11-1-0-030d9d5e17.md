---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-release-notes-android-11-1-0-030d9d5e17
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/release-notes/android/11_1_0/
retrieved_at: 2026-09-01T17:46:44.267849+00:00
---

# Jabber Guest for Android SDK Release - 11.1

Introduction

Cisco Jabber Guest enables organizations using Cisco Unified Communications Manager (UCM) and Cisco
                Expressway to connect
                with remote visitors (guests) through their website or mobile application using instant-on, real-time
                voice and video. Guests simply click a URL, website link, or mobile application to start the
                interaction.
                Build these capabilities into your website or mobile application with the included SDKs, or use the
                Jabber
                Guest client experiences.

New and Changed Functionality

- Customized Guest Caller Name

New fields Allow customized caller name in individual link setting and Allow customized caller name for ad hoc links are added at server side, enabling
                    these configurations
                    will give a guest user the ability to specify his/her own name instead of the default caller name.
                    Guest user could specify the customized caller name with additional URL query parameter callerName in the call link.

For example, Alice could call https://jg.example.com/call/agent?callerName=Alice ,
                    while Bob could contact the same destination
                    endpoint but with a different query parameter value Bob: https://jg.example.com/call/agent?callerName=Bob .
                    The destination endpoint will show different
                    caller names for Alice and Bob.

This new feature prevents any confusion when multiple guest users are dialing into the same call
                    link (For example, a link
                    for a video conference call), furthermore, it gives additional ability for Cisco Jabber Guest SDK
                    integration, in which case, the call link is created in advance but distributed to different users
                    along with an additional URL query parameter callerName associated with different values.

Customized caller name in multiple languages are supported, in order to preserve customized caller
                    name in SIP messages and
                    display correctly on destination endpoints, make sure that the following actions are applied to
                    Cisco
                    Unified Communications Manager and the destination endpoints:

- The selected language locale is supported and installed on Cisco Unified Communications Manager
                        and the destination endpoint(s).

- The destination endpoint User Locale matches locale setting of Common Device Configuration in SIP trunk setting.

- Transmit UTF-8 for Calling Party Name in SIP trunk setting is checked for
                        Unicode
                        support.

See Cisco
                        Unified Communications Manager Configuration Guide for more details.

API updates Refer to API Guide documentation for more details

Samples No new samples.

Resolved Defects

- CSCve99573: JG client failover is not supported when expressway primary node is down

- CSCvg51557: JG android: app crashed when showing call statistics