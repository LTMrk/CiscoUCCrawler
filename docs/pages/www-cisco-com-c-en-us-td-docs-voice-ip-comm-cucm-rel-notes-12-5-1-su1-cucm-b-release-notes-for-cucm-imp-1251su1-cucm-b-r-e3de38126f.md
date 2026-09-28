---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-12-5-1-su1-cucm-b-release-notes-for-cucm-imp-1251su1-cucm-b-r-e3de38126f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/12_5_1/SU1/cucm_b_release-notes-for-cucm-imp-1251su1/cucm_b_release-notes-for-cucm-imp-1251su1_chapter_0100.html
retrieved_at: 2026-08-21T01:30:05.091953+00:00
---

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU1

# Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU1

Updated: June 19, 2019

Chapter: Cisco Endpoints

## Chapter: Cisco Endpoints

# Cisco Endpoints

## Cisco IP Phones and Gateways

### Phone and Gateway Firmware Versions

The following table lists the latest Cisco IP Phone firmware versions supported for Cisco Unified Communications Manager 12.5(1).

Cisco Unified SIP Phone 3905

9.4(1)SR3

Cisco Unified IP Phones 6901 and 6911

9.3(1)SR2

Cisco Unified IP Phones 6921, 6941, 6945, and 6961

9.4(1)SR3

Cisco IP Phone 7800 Series

12.5(1)

Cisco IP Conference Phone 7832

12.5(1)

Cisco Unified IP Phone 7900 Series

9.4(2)SR3

Cisco Unified Wireless IP Phones 7925G, 7925G-EX, and 7926G

1.4(8)SR1

Cisco IP Phone 8800 Series

12.5(1)

Cisco Wireless IP Phone 8821

11.0(4)SR1

11.0(5)

Cisco Unified IP Conference Phone 8831

10.3(1)SR4b

Cisco IP Conference Phone 8832

12.5(1)

Cisco Unified IP Phones 8941 and 8945

9.4(2)SR3

Cisco Unified IP Phones 8961, 9951, and 9971

9.4(2)SR4

The following table lists the latest gateway firmware versions supported for Cisco Unified Communications Manager 12.5.

Phone Family

Firmware Release Number

Cisco ATA 190 Analog Telephone Adapter

1.2.2

Cisco ATA 191 Analog Telephone Adapter

12.0(1)SR1

#### Phone Firmware Releases on Cisco Unified Communication Manager

Each Cisco Unified Communications Manager release contains a version of the phone firmware. But, this version may not be the
                                    latest version of the phone firmware.

The latest version of the phone firmware is available on the Software Download site.

#### Phone Documents in Cisco Unified Communications Manager Self Care Portal

The Cisco Unified Communications Manager Self Care Portal provide  links to the IP Phone user guides in PDF format. These
                                    user guides are stored in the portal and  match the phone firmware version that comes with the Cisco Unified Communications
                                    Manager release.

After a Cisco Unified Communications Manager release, subsequent updates to the user guides appear only on the Cisco website.
                                    The phone firmware release notes contain the applicable documentation URLs. In the web pages, updated documents display "Updated" beside the document link.

The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer
                                                do not update the English user guides on the Cisco Unified Communications Manager.

Administrators and users should check the Cisco website for updated user guides and download the PDF files. Administrators
                                    can also make the files available to the users on their company website.

Administrators may want to bookmark the web pages for the phone models that are deployed in their company and send these URLs
                                                to their users.

### Deprecated Phone Models for Cisco Unified Communications Manager

As of Cisco Unified Communications Manager Firmware Release 12.0 and later, the following phones are not supported:

Cisco Unified IP Phone 7970G

Cisco Unified IP Phone 7971G-GE

Cisco Unified Wireless IP Phone 7921G

As of Cisco Unified Communications Manager Firmware Release 11.5 and later, the following phones are not supported:

Cisco IP Phone 12 SP+ and related models

Cisco IP Phone 30 VIP and related models

Cisco Unified IP Phone 7902

Cisco Unified IP Phone 7905

Cisco Unified IP Phone 7910

Cisco Unified IP Phone 7910SW

Cisco Unified IP Phone 7912

Cisco Unified Wireless IP Phone 7920

Cisco Unified IP Conference Station 7935

### IPv6-Only Impact on Cisco IP Phones with SCCP Firmware

In Cisco Unified Communications Manager Release 12.0, you can use IPv6 to communicate with the phones that run Session Initiation
                                 Protocol (SIP) firmware.

Some of the Cisco IP Phones can run with Skinny Client Control Protocol (SCCP) firmware. The SCCP firmware does not support
                                 IPv6. The following desk phones can run with either SIP or SCCP firmware:

Cisco Unified IP Phone 6901, 6911, 6921, 6941, 6945, and 6961

Cisco Unified IP Phone 7906G, 7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE, 7965G, 7962G, 7970G, 7971G-GE,
                                       and 7975G

Cisco Unified IP Phone 8941 and 8945

If you set up your Cisco Unified Communications Manager to communicate in IPv6 only, any of above phones that have SCCP firmware
                                 installed must be upgraded to SIP firmware. The SCCP firmware cannot communicate with the Cisco Unified Communications Manager
                                 with IPv6.

The Cisco Wireless IP Phones 7925G, 7925G-EX, and 7926G are also SCCP phones. They do not have SIP firmware and only support
                                 IPv4.

For details on how to configure IPv6 in Cisco Unified Communications Manager, see the "Configure IPv6" chapter of the System Configuration Guide for Cisco Unified Communications Manager .

### Cisco Unified SIP Phone 3905 Features

No new features were introduced for the Cisco Unified SIP Phone 3905 in Firmware Release 9.4(1)SR3.

### Cisco Unified IP Phone 6900 Series Features

No new features were introduced for the Cisco Unified IP Phones 6900 Series.

### Cisco IP Phone 7800 Series Features

The following table lists the features added to the Cisco IP Phone 7800 Series for Firmware Releases 12.0(1), 12.1(1), 12.1(1)SR1,
                                 and 12.5(1). For more information, see the Release Notes at the following location: http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/products-release-notes-list.html .

Feature Name

Firmware Release

IPv6 Feature Support

12.0(1)

Mobile and Remote Access Through Expressway and Domain Name Handling

12.0(1)

Cisco Headset 531 and Cisco Headset 532

12.1(1)

G722.2 ANR-WB Support

12.1(1)

Transport Layer Security Enhancements

12.1(1)

Enbloc Dialing

12.1(1)SR1

Activation Code Onboarding

12.5(1)

Cisco Headset 561 and 562

12.5(1)

Disable the Handset for Headset Users

12.5(1)

Disable Transport Layer Support Ciphers

12.5(1)

Elliptic Curve Support

12.5(1)

Interactive Connectivity Establishment and media Paths

12.5(1)

Remote Configuration of Headset Parameters

12.5(1)

Whisper Paging and Cisco Unified Communications Manager Express

12.5(1)

### Cisco IP Conference Phone 7832 Features

The following table lists the features added to the Cisco IP Conference Phone 7832 for Firmware Releases 12.0(1),12.1(1),
                                 and 12.5(1). For more information, see the Release Notes at the following location: http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/products-release-notes-list.html .

Feature Name

Firmware Release

Client Matter Code and Forced Authorization Code

12.1(1)

Mobile and Remote Access Through Expressway

12.1(1)

Transport Layer Security Enhancements

12.1(1)

Disable Transport Layer Support Ciphers

12.5(1)

Elliptic Curve Support

12.5(1)

Whisper Paging and Cisco Unified Communications manager Express

12.5(1)

### Cisco Unified IP Phone 7900 Series Features

No new features were introduced for the Cisco Unified IP Phones 7900 Series.

### Cisco Unified Wireless IP Phone 7920 Series Features

No new features were introduced for the Cisco Unified Wireless IP Phones 792x Series.

### Cisco IP Phone 8800 Series Features

The following table lists the features added to the Cisco IP Phone 8800 Series for Firmware Releases 12.0(1), 12.0(1)SR1,
                                 12.1(1), 12.1(1)SR1, and 12.5(1). For more information, see the Release Notes at the following location: http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-release-notes-list.html .

Feature Name

Firmware Release

New Feature Support for Enhanced Line Mode

12.0(1)

IPv6 Feature Support

12.0(1)

Mobile and Remote Access Through Expressway and Domain Name Handling

12.0(1)

Key Expansion Modules for Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR

12.0(1)

Cisco Headset 531 and Cisco Headset 532

12.1(1)

Voice Feedback

12.1(1)

Call History Enhancements

12.1(1)

Incoming Calls and Enhanced Line Mode

12.1(1)

Speed Dial and Navigation Enhancements

12.1(1)

G722.2 ANR-WB Support

12.1(1)

Transport Layer Security Enhancements

12.1(1)

Enhanced Line Mode and Simplified Line Display for Incoming Calls

12.1(1)SR1

Wallpaper and Key Expansion Modules

12.1(1)SR1

Enbloc Dialing

12.1(1)SR1

Activation Code Onboarding

12.5(1)

Chinese Language Support

12.5(1)

Cisco Headset 561 and 562

12.5(1)

Disable the Handset for Headset Users

12.5(1)

Disable Transport Layer Support Ciphers

12.5(1)

Elliptic Curve Support

12.5(1)

Enhanced Line Mode and Call History

12.5(1)

Interactive Connectivity Establishment and Media Paths

12.5(1)

Remote Configuration of Headset Parameters

12.5(1)

Transport Layer Security 1.2 and Wireless Authentication

12.5(1)

Whisper Paging and Cisco Unified Communications Manager Express

12.5(1)

### Cisco Wireless IP Phone 8821 Features

The following table lists the features added to the Cisco Wireless IP Phone 882x Series for Firmware Releases 11.0(3)SR4,
                                 11.0(3)SR5, 11.0(3)SR6, 11.0(4), 11.0(4)SR1, and 11.0(4)SR2. For more information, see the Release Notes at the following
                                 location: http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-release-notes-list.html .

Feature Name

Firmware Release

OPUS Codec Support

11.0(3)SR4

Bulk Deployment Utility

11.0(3)SR4

Configurable Home Screen

11.0(4)

Local Contacts

11.0(4)

Problem Report Tool

11.0(4)

Ringtone Enhancements

11.0(4)

User Interface Enhancements for Firmware Release 11.0(4)

11.0(4)

Resized Wallpapers

11.0(4)

### Cisco Unified IP Conference Phone 8831 Features

No new features were introduced for the Cisco Unified IP Conference Phone 8831.

### Cisco IP Conference Phone 8832 Features

The following table lists the features added to the Cisco Conference IP Phone 8832 for Firmware Releases 12.0(1)SR2, 12.0(1)SR3,
                                 12.1(1) and 12.5(1). For more information, see the Release Notes at the following location: http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-release-notes-list.html .

Feature Name

Firmware Release

Cisco IP Conference Phone 8832 PoE Injector

12.0(1)SR2

Audio Clock Frequency

12.0(1)SR3

Client Matter Code and Forced Authorization Code

12.1(1)

Daisy Chain Support

12.1(1)

G722.2 ANR-WB Support

12.1(1)

Wireless Microphone Support

12.1(1)

Mobile and Remote Access Through Expressway

12.1(1)

Transport Layer Security Enhancements

12.1(1)

Wi-Fi Support and Wireless LAN Profiles

12.1(1)

Disable Transport Layer Support Ciphers

Elliptic Curve Support

12.5(1)SR2

Transport Layer Security 1.2 and Wireless Authentication

12.5(1)SR2

Whisper Paging and Cisco Unified Communications Manager Express

12.5(1)SR2

### Cisco Unified IP Phone 8941 and 8845 Features

No new features were introduced for the Cisco Unified IP Phone 8941 and 8945.

### Cisco Unified IP Phone 8961, 9951, and 9971 Features

No new features were introduced for the Cisco Unified IP Phone 8961, 9951, and 9971.

### Cisco ATA 190 Series Features

The Cisco ATA 190 Analog Telephone Adapter had no new features added.

The Cisco ATA 191 Analog Telephone Adapter was released after Cisco Unified Communications Manager 12.1 was released. This
                                 device allows you to turn an analog phone or fax machine into an IP phone. No new features were introduced after the initial
                                 release.

| Phone Family | Firmware Release Number |
|---|---|
| Cisco Unified SIP Phone 3905 | 9.4(1)SR3 |
| Cisco Unified IP Phones 6901 and 6911 | 9.3(1)SR2 |
| Cisco Unified IP Phones 6921, 6941, 6945, and 6961 | 9.4(1)SR3 |
| Cisco IP Phone 7800 Series | 12.5(1) |
| Cisco IP Conference Phone 7832 | 12.5(1) |
| Cisco Unified IP Phone 7900 Series | 9.4(2)SR3 |
| Cisco Unified Wireless IP Phones 7925G, 7925G-EX, and 7926G | 1.4(8)SR1 |
| Cisco IP Phone 8800 Series | 12.5(1) |
| Cisco Wireless IP Phone 8821 | 11.0(4)SR1 11.0(5) |
| Cisco Unified IP Conference Phone 8831 | 10.3(1)SR4b |
| Cisco IP Conference Phone 8832 | 12.5(1) |
| Cisco Unified IP Phones 8941 and 8945 | 9.4(2)SR3 |
| Cisco Unified IP Phones 8961, 9951, and 9971 | 9.4(2)SR4 |

| Phone Family | Firmware Release Number |
|---|---|
| Cisco ATA 190 Analog Telephone Adapter | 1.2.2 |
| Cisco ATA 191 Analog Telephone Adapter | 12.0(1)SR1 |

| Note | The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer
                                                do not update the English user guides on the Cisco Unified Communications Manager. |
|---|---|

| Tip | Administrators may want to bookmark the web pages for the phone models that are deployed in their company and send these URLs
                                                to their users. |
|---|---|

| Feature Name | Firmware Release |
|---|---|
| IPv6 Feature Support | 12.0(1) |
| Mobile and Remote Access Through Expressway and Domain Name Handling | 12.0(1) |
| Cisco Headset 531 and Cisco Headset 532 | 12.1(1) |
| G722.2 ANR-WB Support | 12.1(1) |
| Transport Layer Security Enhancements | 12.1(1) |
| Enbloc Dialing | 12.1(1)SR1 |
| Activation Code Onboarding | 12.5(1) |
| Cisco Headset 561 and 562 | 12.5(1) |
| Disable the Handset for Headset Users | 12.5(1) |
| Disable Transport Layer Support Ciphers | 12.5(1) |
| Elliptic Curve Support | 12.5(1) |
| Interactive Connectivity Establishment and media Paths | 12.5(1) |
| Remote Configuration of Headset Parameters | 12.5(1) |
| Whisper Paging and Cisco Unified Communications Manager Express | 12.5(1) |

| Feature Name | Firmware Release |
|---|---|
| Client Matter Code and Forced Authorization Code | 12.1(1) |
| Mobile and Remote Access Through Expressway | 12.1(1) |
| Transport Layer Security Enhancements | 12.1(1) |
| Disable Transport Layer Support Ciphers | 12.5(1) |
| Elliptic Curve Support | 12.5(1) |
| Whisper Paging and Cisco Unified Communications manager Express | 12.5(1) |

| Feature Name | Firmware Release |
|---|---|
| New Feature Support for Enhanced Line Mode | 12.0(1) |
| IPv6 Feature Support | 12.0(1) |
| Mobile and Remote Access Through Expressway and Domain Name Handling | 12.0(1) |
| Key Expansion Modules for Cisco IP Phone 8851, 8851NR, 8861, 8865, and 8865NR | 12.0(1) |
| Cisco Headset 531 and Cisco Headset 532 | 12.1(1) |
| Voice Feedback | 12.1(1) |
| Call History Enhancements | 12.1(1) |
| Incoming Calls and Enhanced Line Mode | 12.1(1) |
| Speed Dial and Navigation Enhancements | 12.1(1) |
| G722.2 ANR-WB Support | 12.1(1) |
| Transport Layer Security Enhancements | 12.1(1) |
| Enhanced Line Mode and Simplified Line Display for Incoming Calls | 12.1(1)SR1 |
| Wallpaper and Key Expansion Modules | 12.1(1)SR1 |
| Enbloc Dialing | 12.1(1)SR1 |
| Activation Code Onboarding | 12.5(1) |
| Chinese Language Support | 12.5(1) |
| Cisco Headset 561 and 562 | 12.5(1) |
| Disable the Handset for Headset Users | 12.5(1) |
| Disable Transport Layer Support Ciphers | 12.5(1) |
| Elliptic Curve Support | 12.5(1) |
| Enhanced Line Mode and Call History | 12.5(1) |
| Interactive Connectivity Establishment and Media Paths | 12.5(1) |
| Remote Configuration of Headset Parameters | 12.5(1) |
| Transport Layer Security 1.2 and Wireless Authentication | 12.5(1) |
| Whisper Paging and Cisco Unified Communications Manager Express | 12.5(1) |

| Feature Name | Firmware Release |
|---|---|
| OPUS Codec Support | 11.0(3)SR4 |
| Bulk Deployment Utility | 11.0(3)SR4 |
| Configurable Home Screen | 11.0(4) |
| Local Contacts | 11.0(4) |
| Problem Report Tool | 11.0(4) |
| Ringtone Enhancements | 11.0(4) |
| User Interface Enhancements for Firmware Release 11.0(4) | 11.0(4) |
| Resized Wallpapers | 11.0(4) |

| Feature Name | Firmware Release |
|---|---|
| Cisco IP Conference Phone 8832 PoE Injector | 12.0(1)SR2 |
| Audio Clock Frequency | 12.0(1)SR3 |
| Client Matter Code and Forced Authorization Code | 12.1(1) |
| Daisy Chain Support | 12.1(1) |
| G722.2 ANR-WB Support | 12.1(1) |
| Wireless Microphone Support | 12.1(1) |
| Mobile and Remote Access Through Expressway | 12.1(1) |
| Transport Layer Security Enhancements | 12.1(1) |
| Wi-Fi Support and Wireless LAN Profiles | 12.1(1) |
| Disable Transport Layer Support Ciphers |  |
| Elliptic Curve Support | 12.5(1)SR2 |
| Transport Layer Security 1.2 and Wireless Authentication | 12.5(1)SR2 |
| Whisper Paging and Cisco Unified Communications Manager Express | 12.5(1)SR2 |