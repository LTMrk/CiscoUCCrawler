---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-unified-communications-system-compatibility-tls-tls1-3-compatibili-8429e58e4c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/TLS/TLS1-3-Compatibility-Matrix.html
retrieved_at: 2026-08-16T18:26:26.685372+00:00
---

TLS 1.3 Compatibility Matrix for Cisco Collaboration Products

# TLS 1.3 Compatibility Matrix for Cisco Collaboration Products

### Download Options

Updated: October 17, 2024

TLS 1.3 Compatibility Matrix for Cisco Collaboration Products

First Published : October 2024

## Introduction

The following products have been tested to support Transport Layer Security (TLS) 1.3. Products that are not listed here may not support TLS 1.3. For further information, refer to the respective product documentation.

This matrix identifies Cisco Collaboration products:

· Minimum recommended versions that support TLS 1.3.

Note: Earlier releases may have some TLS 1.2 support but are not recommended in a deployment where TLS 1.0/1.1 is disabled.

· Minimum versions that can disable TLS version 1.0 and 1.1 on server interfaces.

For an overview of configuring TLS 1.3, see the TLS 1.3 Configuration Overview Guide .

Note:

· See the product documentation for complete product compatibility information, including backward compatibility .

· See the Cisco Collaboration Systems Release Compatibility Matrix for the Cisco Collaboration Systems Release (CSR) product versions.

Table 1. Collaboration Products Compatible with TLS 1.3

Product

The minimum recommended version that supports TLS 1.3 1

The minimum recommended version that can set the TLS minimum version

Link to product support documentation

Call Control

Cisco Unified Communications Manager and IM and Presence Service

15 SU2

11.5(1)SU3

Support

Cisco Unified Survivable Remote Site Telephony

IOS XE 17.15.1a

IOS XE 16.7.1

Support

Conferencing

Cisco Meeting Server

3.10

Not Defined Yet

Support

Cisco Meeting Management

--

--

Not Supported

Enterprise Edge

Cisco Expressway Series

X15.2

X8.10.1

Support

Cisco Unified Border Element (CUBE) for  Voice Gateway (VG3) and vCUBE

IOS XE 17.15.1a

IOS XE 16.9.1

Support

SIP PSTN Gateways G3

17.16

17.16

Support

SIP PSTN Gateways G2

17.16

17.16

Support

Server Applications

Cisco Emergency Responder

15 SU2

11.5(2)

Support

Cisco Paging Server

Not Supported

Cisco Unified Attendant Console Standard

14.0(3) – Planned for December 2024 release

12.0(5)

Support

Cisco Unified Attendant Console Advanced

14.0(3) – Planned for December 2024 release

12.0(4)

Support

Voicemail and Messaging

Cisco Unity Connection

15 SU2

11.5(1)SU3

Support

Endpoints

Cisco IP Phone 7800 Series

Not Supported

Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, 8865NR, Cisco IP Conference Phone 8832

Not Supported

Cisco Wireless IP Phone 8821, 8821-EX

Not Supported

Cisco Video Phone 8875

PhoneOS 3.2

PhoneOS 3.2

Cisco Desk Phone 9800 Series

PhoneOS 3.1

PhoneOS 3.1

Support

For more information, see Release Notes for Cisco Desk Phone 9800 Series

Cisco RoomOS

11.9

Support

Cisco Webex App

Webex 44.5 and later releases

Cisco Jabber

15

Not applicable for clients.

Support

Service Management

Cisco Prime Collaboration (Deployment)

15 SU2

11.6(2)

Support

Cisco Prime License Manager

Not Supported – With the advent of Smart Licensing Manager (SLM), it is built with Unified CM

Other

MTP/CFB (ISR G3)

17.16

17.16

Cisco 4000 Series Integrated Services Routers (ISR4k)

17.16

17.16

Cisco Catalyst 8200/8300

17.16

17.16

Contact Center

Cisco Unified Contact Center Enterprise

--

11.6(1)

Not Supported

Cisco Unified Contact Center Express

--

11.6(1)

Not Supported

Third-Party Applications

Operating System

VMware ESXi 6.0U3

VMware ESXi 6.0U3

Documentation

## Related Documentation

For more details about TLS 1.3 and the implications of disabling TLS 1.0 and 1.1 for on-premises Cisco Collaboration deployments, see TLS 1.3  for On-Premises Cisco Collaboration Deployments .

For an overview of configuring TLS 1.3, see the TLS 1.3 Configuration Overview Guide .

## Documentation Changes

Table 2. Documentation Changes

Date

Change

October 2024

Updated and Published the Compatibility Matrix for TLS 1.3.

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see What’s New in Cisco Product Documentation .

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS” WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies are considered un-Controlled copies and the original on-line version should be referred to for latest version.

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at www.cisco.com/go/offices .

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R).

© 2024 Cisco Systems, Inc. All rights reserved.

| Product | The minimum recommended version that supports TLS 1.3 1 | The minimum recommended version that can set the TLS minimum version | Link to product support documentation |
|---|---|---|---|
| Call Control |
| Cisco Unified Communications Manager and IM and Presence Service | 15 SU2 | 11.5(1)SU3 | Support |
| Cisco Unified Survivable Remote Site Telephony | IOS XE 17.15.1a | IOS XE 16.7.1 | Support |
| Conferencing |
| Cisco Meeting Server | 3.10 | Not Defined Yet | Support |
| Cisco Meeting Management | -- | -- | Not Supported |
| Enterprise Edge |
| Cisco Expressway Series | X15.2 | X8.10.1 | Support |
| Cisco Unified Border Element (CUBE) for  Voice Gateway (VG3) and vCUBE | IOS XE 17.15.1a | IOS XE 16.9.1 | Support |
| SIP PSTN Gateways G3 | 17.16 | 17.16 | Support |
| SIP PSTN Gateways G2 | 17.16 | 17.16 | Support |
| Server Applications |
| Cisco Emergency Responder | 15 SU2 | 11.5(2) | Support |
| Cisco Paging Server |  |  | Not Supported |
| Cisco Unified Attendant Console Standard | 14.0(3) – Planned for December 2024 release | 12.0(5) | Support |
| Cisco Unified Attendant Console Advanced | 14.0(3) – Planned for December 2024 release | 12.0(4) | Support |
| Voicemail and Messaging |
| Cisco Unity Connection | 15 SU2 | 11.5(1)SU3 | Support |
| Endpoints |
| Cisco IP Phone 7800 Series |  |  | Not Supported |
| Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, 8865NR, Cisco IP Conference Phone 8832 |  |  | Not Supported |
| Cisco Wireless IP Phone 8821, 8821-EX |  |  | Not Supported |
| Cisco Video Phone 8875 | PhoneOS 3.2 | PhoneOS 3.2 |  |
| Cisco Desk Phone 9800 Series | PhoneOS 3.1 | PhoneOS 3.1 | Support For more information, see Release Notes for Cisco Desk Phone 9800 Series |
| Cisco RoomOS | 11.9 |  | Support |
| Cisco Webex App | Webex 44.5 and later releases |  |  |
| Cisco Jabber | 15 | Not applicable for clients. | Support |
| Service Management |
| Cisco Prime Collaboration (Deployment) | 15 SU2 | 11.6(2) | Support |
| Cisco Prime License Manager |  |  | Not Supported – With the advent of Smart Licensing Manager (SLM), it is built with Unified CM |
| Other |
| MTP/CFB (ISR G3) | 17.16 | 17.16 |  |
| Cisco 4000 Series Integrated Services Routers (ISR4k) | 17.16 | 17.16 |  |
| Cisco Catalyst 8200/8300 | 17.16 | 17.16 |  |
| Contact Center |
| Cisco Unified Contact Center Enterprise | -- | 11.6(1) | Not Supported |
| Cisco Unified Contact Center Express | -- | 11.6(1) | Not Supported |
| Third-Party Applications |
| Operating System | VMware ESXi 6.0U3 | VMware ESXi 6.0U3 | Documentation |

| Date | Change |
|---|---|
| October 2024 | Updated and Published the Compatibility Matrix for TLS 1.3. |