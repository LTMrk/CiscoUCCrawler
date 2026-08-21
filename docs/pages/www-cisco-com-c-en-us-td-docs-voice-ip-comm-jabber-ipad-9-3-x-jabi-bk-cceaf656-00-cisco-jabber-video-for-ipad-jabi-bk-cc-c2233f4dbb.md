---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-ipad-9-3-x-jabi-bk-cceaf656-00-cisco-jabber-video-for-ipad-jabi-bk-cc-c2233f4dbb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/iPad/9_3_x/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad_chapter_00.html
retrieved_at: 2026-08-21T19:41:22.484250+00:00
---

Cisco Jabber Video for iPad 9.3.4 Administration Guide

# Cisco Jabber Video for iPad 9.3.4 Administration Guide

Updated: November 22, 2013

Chapter: Before you begin

## Chapter: Before you begin

# Before you begin

Review these topics before starting the configuration of Cisco Jabber Video for iPad .

## What is Cisco Jabber Video for iPad ?

Cisco Jabber Video for iPad is a Unified Communications application that provides instant messaging (IM), video and voice calling, corporate directory search, availability, and voicemail. The underlying technologies include:

- Cisco WebEx Messenger

- Cisco Unified Presence

- Cisco Unified Communications Manager

- Cisco TelePresence Video Communication Server

- Cisco Jabber Video for TelePresence (formerly known as the free Jabber Video service)

- Cisco WebEx TelePresence (formerly known as the paid Jabber Video service)

The video and voice quality of calls varies depending on the Wi-Fi or mobile data network connection. Cisco does not troubleshoot connectivity issues when users of the client are on 3G or 4G mobile data networks or non-corporate Wi-Fi networks over a VPN connection using applications such as Cisco AnyConnect Secure Mobility Client.

Use the Jabber Video for TelePresence login for both the Cisco Jabber Video for TelePresence and Cisco WebEx TelePresence services.

## How to Use this Document

This document is designed to help you set up the organization-specific technologies so they function properly on the user devices. Review this table to quickly navigate to the content that pertains to your needs.

Domain Name Server Server Record (DNS SRV) setup should be the first step in the configuration of any Cisco Jabber Video for iPad deployment.

Cisco Jabber Video for TelePresence and Cisco WebEx TelePresence do not require any administrative setup. If your users have questions about it, direct them to the following support sites:.

## Download and Installation of Cisco Jabber Video for iPad

Cisco Jabber Video for iPad is an application that you can download and install from the App Store within iTunes or on your iPad device.

## Connect on Demand VPN

Cisco Jabber Video for iPad contains the Connect on Demand VPN feature. The Connect on Demand VPN feature enables the application to automatically establish VPN connections when needed without additional actions by end users. The Connect on Demand VPN feature requires a user to download and install the Cisco AnyConnect Secure Mobility Client from the App Store.

Cisco AnyConnect Secure Mobility Client must be configured with certificate authentication to provide the Connect on Demand VPN feature to Cisco Jabber Video for iPad . See the Cisco AnyConnect Secure Mobility Client Administrator Guide for information and procedures for this configuration. The latest version of the Cisco AnyConnect Secure Mobility Client Administrator Guide is available at the following location: http:/​/​www.cisco.com/​en/​US/​products/​ps10884/​products_​installation_​and_​configuration_​guides_​list.html .

Additional Cisco Unified Communications Manager configuration may be required in certain network deployments. See Setting Up Connect on Demand VPN for additional information.

There is no configuration in Cisco Jabber Video for iPad other than turning the Connect on Demand VPN feature on or off. This feature is turned on by default after the application is installed.

## Cross Launching Cisco Jabber Video for iPad

Cisco Jabber Video for iPad can be launched from Safari or other browsers to perform one of the following tasks:

- Call a phone number

- Start a chat session

- Place a video call

The following table lists the cross launch URLs third party applications can use to make use of Cisco Jabber Video for iPad functionality.

- Cisco WebEx Messenger account

- Cisco Unified Presence account

- movi://<phone_number>

- movi://<URI>

- sip://<phone_number>

- sip://<URI>

- Cisco TelePresence Video Communication Server account for movi: URLs

- Cisco Unified Communications Manager or Cisco TelePresence Video Communication Server account for sip: URLs

ciscojabber://goim?screenname=<contact_id>&

message=<message_tx>

- Cisco WebEx Messenger account

- Cisco Unified Presence account

ciscojabber://call?address=<user_address>&

type=<call_type>

Call types:

- 0 - Point to Point

- 1 - Cisco Unified Communications Manager

- 2 - Cisco TelePresence Video Communication Server

- 3 - Cisco Jabber Video for TelePresence / Cisco WebEx TelePresence

- 4 - Determine the active account type and use that to place a call.

If a URL uses a value of 1, 2, or 3 and that account type is not present, the URL will be ignored.

- Cisco Unified Communications Manager account

- Cisco TelePresence Video Communication Server account

- Cisco Jabber Video for TelePresence / Cisco WebEx TelePresence account

ciscojabber://addbuddy?screenname=

<user_name>

ciscojabber://goprofile?screenname=

<user_name>

ciscojabber://login?type=<account_type>&username=

<user_name>&token=<login_token>&primaryserver=

<primary_login_server>&secondaryserver=

<secondary_login_server>&sipdomain=<sip_domain>

&devicename=<ucm_device>

Account types:

- 1 - Cisco WebEx Messenger

- 2 - Cisco WebEx Messenger Single Sign-On

- 3 - Cisco Unified Presence

- 4 - Cisco Unified Communications Manager

- 5 - Cisco TelePresence Video Communication Server

- 6 - Cisco Jabber Video for TelePresence / Cisco WebEx TelePresence

- Cisco WebEx Messenger account

- Cisco Unified Presence account

- Cisco Unified Communications Manager account

- Cisco TelePresence Video Communication Server account

- Cisco Jabber Video for TelePresence / Cisco WebEx TelePresence account

## Apple iOS Support Statement

Cisco supports Cisco Jabber releases only on the latest major iOS release. Apple maintains iOS, provides free iOS updates, and actively encourages users to upgrade to new iOS releases. To help enterprise customers transition to new major iOS updates, Cisco supports the last dot release of the previous major release for three months after a new release is introduced.

## Important Notice About Emergency Calls

Using your iPad as a phone may not provide the most timely or accurate location data for an emergency call such as 911, 999, and 112. Calls may be misdirected to the wrong emergency response center or the emergency response center may make errors when determining your location. Use your device as a phone only as a last resort during an emergency. Cisco is not liable for resulting errors or delays.

| Note | The video and voice quality of calls varies depending on the Wi-Fi or mobile data network connection. Cisco does not troubleshoot connectivity issues when users of the client are on 3G or 4G mobile data networks or non-corporate Wi-Fi networks over a VPN connection using applications such as Cisco AnyConnect Secure Mobility Client. |
|---|---|

| Note | Use the Jabber Video for TelePresence login for both the Cisco Jabber Video for TelePresence and Cisco WebEx TelePresence services. |
|---|---|

| If you want to set up… | Go to this chapter… |
|---|---|
| Domain Name Server Service Records | Set up Simple Sign-In using DNS SRV |
| Cisco WebEx Messenger only | Set up for Cisco WebEx Messenger |
| Cisco Unified Presence only | Set up for Cisco Unified Presence |
| Cisco Unified Communications Manager only | Set up for Cisco Unified Communications Manager 8.x |
| Cisco TelePresence Video Communication Server only | Set up for Cisco TelePresence Video Communication Server |
| Cisco WebEx Messenger and Cisco Unified Communications Manager | Setup for Cisco WebEx Messenger and Cisco Unified Communications Manager |
| Cisco WebEx Messenger and Cisco TelePresence Video Communication Server | Setup for Cisco WebEx Messenger and Cisco TelePresence Video Communication Server |
| Cisco Unified Presence and Cisco Unified Communications Manager | Setup for Cisco Unified Presence and Cisco Unified Communications Manager |

| Note | Domain Name Server Server Record (DNS SRV) setup should be the first step in the configuration of any Cisco Jabber Video for iPad deployment. |
|---|---|

| Note | Cisco Jabber Video for TelePresence and Cisco WebEx TelePresence do not require any administrative setup. If your users have questions about it, direct them to the following support sites:. |
|---|---|

| Note | There is no configuration in Cisco Jabber Video for iPad other than turning the Connect on Demand VPN feature on or off. This feature is turned on by default after the application is installed. |
|---|---|

| Function | Cross Launch URL | Precondition |
|---|---|---|
| Call a phone number | ciscotel://<phone_number> | Cisco Unified Communications Manager account |
| Start a chat session | xmpp://<instant_message_id> | Cisco WebEx Messenger account Cisco Unified Presence account |
| Place a video call | movi://<phone_number> movi://<URI> sip://<phone_number> sip://<URI> | Cisco TelePresence Video Communication Server account for movi: URLs Cisco Unified Communications Manager or Cisco TelePresence Video Communication Server account for sip: URLs |
| Send instant message | ciscojabber://goim?screenname=<contact_id>& message=<message_tx> | Cisco WebEx Messenger account Cisco Unified Presence account |
| Place a VoIP or video call | ciscojabber://call?address=<user_address>& type=<call_type> Call types: 0 - Point to Point 1 - Cisco Unified Communications Manager 2 - Cisco TelePresence Video Communication Server 3 - Cisco Jabber Video for TelePresence / Cisco WebEx TelePresence 4 - Determine the active account type and use that to place a call. Note If a URL uses a value of 1, 2, or 3 and that account type is not present, the URL will be ignored. | Note | If a URL uses a value of 1, 2, or 3 and that account type is not present, the URL will be ignored. | Cisco Unified Communications Manager account Cisco TelePresence Video Communication Server account Cisco Jabber Video for TelePresence / Cisco WebEx TelePresence account |
| Note | If a URL uses a value of 1, 2, or 3 and that account type is not present, the URL will be ignored. |
| Add a contact | ciscojabber://addbuddy?screenname= <user_name> |  |
| View profile | ciscojabber://goprofile?screenname= <user_name> |  |
| Sign in to Cisco Jabber Video for iPad | ciscojabber://login?type=<account_type>&username= <user_name>&token=<login_token>&primaryserver= <primary_login_server>&secondaryserver= <secondary_login_server>&sipdomain=<sip_domain> &devicename=<ucm_device> Account types: 1 - Cisco WebEx Messenger 2 - Cisco WebEx Messenger Single Sign-On 3 - Cisco Unified Presence 4 - Cisco Unified Communications Manager 5 - Cisco TelePresence Video Communication Server 6 - Cisco Jabber Video for TelePresence / Cisco WebEx TelePresence | Cisco WebEx Messenger account Cisco Unified Presence account Cisco Unified Communications Manager account Cisco TelePresence Video Communication Server account Cisco Jabber Video for TelePresence / Cisco WebEx TelePresence account |

| Note | If a URL uses a value of 1, 2, or 3 and that account type is not present, the URL will be ignored. |
|---|---|