---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-unified-communications-system-compatibility-tls-tls1-2-compatibili-fd045b7db2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/TLS/TLS1-2-Compatibility-Matrix.html
retrieved_at: 2026-08-16T18:26:31.063743+00:00
---

TLS 1.2 Compatibility Matrix for Cisco Collaboration Products

# TLS 1.2 Compatibility Matrix for Cisco Collaboration Products

### Download Options

Updated: February 2, 2024

TLS 1.2 Compatibility Matrix for Cisco Collaboration Products

First Published : September 6, 2017

Last Updated: June 06, 2019

## Introduction

The following products have been tested to support Transport Layer Security (TLS) 1.2. Products that are not listed here may not support TLS 1.2. For further information, refer to the respective product documentation.

This matrix identifies Cisco Collaboration products’:

· Minimum recommended versions that support TLS 1.2.

Note: Earlier releases may have some TLS 1.2 support, but they are not recommended in a deployment where TLS 1.0/1.1 is disabled.

· Minimum versions that can disable TLS version 1.0 and 1.1 on server interfaces.

For on overview on configuring TLS 1.2, see the TLS 1.2 Configuration Overview Guide .

Note: For complete compatibility information between products, including backwards compatibility, see product documentation .

Note: To see Cisco Collaboration Systems Release (CSR) product versions, see the Cisco Collaboration Systems Release Compatibility Matrix .

Table 1. Collaboration Products Compatible with TLS 1.2

Product

Minimum recommended version that supports TLS 1.2 1

Minimum version that can disable TLS version 1.0 and 1.1

Link to product support documentation

Call Control

Cisco Unified Communications Manager and IM and Presence Service

11.5(1)SU3

CTL client does not support TLS 1.2.

11.5(1)SU3

Support

Cisco Unified Survivable Remote Site Telephony

12.1 (IOS 16.7.1)

12.1 (IOS 16.7.1)

Support

Conferencing

Cisco Meeting Server

2.0

2.3

Support

Cisco Meeting App

1.9

Not applicable for clients.

Support

Cisco Meeting Management

1.0

1.0

Support

Cisco TelePresence Management Suite (Cisco TMS)

15.3

15.3

Windows registry edit required for Windows Server lockout of pre TLS 1.2.

Support

Cisco TelePresence Management Suite Extension for Microsoft Exchange (Cisco TMSXE)

5.3

Windows registry edit required.

5.6

Windows registry edit required for Windows Server lockout of pre TLS 1.2.

Support

Cisco TelePresence Management Suite Provisioning Extension (Cisco TMSPE)

HTTPS server interface: 1.12.0

Client interface: None (TLS 1.2 not supported)

HTTPS server interface: 1.12.0

Client interface: Not applicable

Support

Cisco TelePresence Server

2.3

4.4(1.20)

Support

Cisco TelePresence Conductor (TelePresence Conductor)

XC4.3.2

XC4.3.2

Support

Cisco Webex Meetings Server

2.7

2.7

TLS 1.0 is disabled.

TLS 1.1 and 1.2 allowed.

Support

Release Notes

Enterprise Edge

Cisco Expressway Series

X8.10.1

X8.10.1

Support

Cisco Unified Border Element (CUBE) for ISR G3 and vCUBE

IOS XE 3.17S

IOS 15.6.1S

IOS XE 16.6

Support

CUBE for ISR G2

15.6(1)T

SIP only.

15.6(1)T

SIP only.

Support

SIP PSTN Gateways G3

16.6.1

16.6.1

Support

SIP PSTN Gateways G2

15.6(3)M3

15.6(3)M3

Support

Server Applications

Cisco Emergency Responder

11.5(2)

11.5(2)

Support

Cisco Paging Server

12.0.1

12.5(1)

Support

Cisco Unified Attendant Console Standard

12.0(5)

12.0(5)

Support

Cisco Unified Attendant Console Advanced

12.0(4)

12.0(4)

Support

Voicemail and Messaging

Cisco Unity Connection

11.5(1)SU3

11.5(1)SU3

Support

Endpoints

Cisco IP Phone 7800 Series

12.0

12.1(1)

Support

Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, 8865NR, Cisco IP Conference Phone 8832

12.0

12.5 to include wireless authentication.

12.1(1)

Support

Cisco Wireless IP Phone 8821, 8821-EX

11.0(2)

Except for wireless authentication, which is implemented in 11.0(5).

11.0(5) for 8821

11.0(5)SR1 for 8821-EX

Support

Cisco TelePresence IX5000

8.2.1

8.2.2

Support

Cisco DX70 and Cisco Webex DX80

Cisco TelePresence MX 200/300 G2, MX 700/800

Cisco TelePresence SX Series

CE 9.1.3

CE 9.1.3

DX Support

MX Support

SX Support

Cisco TelePresence System EX Series

Cisco TelePresence MX 200/300 G1

Cisco TelePresence Integrator C Series

Cisco TelePresence Profile Series

TC7.3.11

TC7.3.11

TLS 1.0 disabled on the HTTPS server interface.

TLS 1.1 or 1.2 allowed.

EX Support

MX Support

Integrator C Series Support

Profile Series Support

Cisco TelePresence TX9000 Series

6.1.13

None.

Support

Cisco TelePresence System 1000

Cisco TelePresence System 1100

Cisco TelePresence System 500

Cisco TelePresence System 3200 Series

1.10.16

None.

1000 Support

1100 Support

500 Support

3200 Support

Cisco Webex Room Kit & Plus

CE 9.1.3

CE 9.1.3

Support

Cisco Jabber

11.7

Not applicable for clients.

Support

Service Management

Cisco Prime Collaboration (Provisioning)

12.3

12.3

Support

Cisco Prime Collaboration (Assurance and Analytics)

12.1 Service Pack1

12.1 Service Pack1

Support

Cisco Prime Collaboration (Deployment)

11.6(2)

11.6(2)

Support

Cisco Prime License Manager

11.5SU2

11.5SU2

Support

Communication Gateways

Virtual Cisco Unified SIP Proxy Software

Future release.

None.

Support

Cisco VG Series Gateways (VG202XM, VG204XM, VG310, VG320, and VG350 Analog Voice Gateway)

15.7.3M1

15.7.3M1

Support for Cisco VG Series Gateways

Support for Cisco VG300 Series Gateways

Other

MTP/CFB (ISR G3)

16.7.1

16.7.1

MTP/CFB (ISR G2)

15.7.3M1

15.7.3M1

Contact Center

Cisco Unified Contact Center Enterprise

11.6(1)

11.6(1)

Support

Cisco Unified Contact Center Express

11.6(1)

11.6(1)

Support

Third Party Applications

Operating System

VMware ESXi 6.0U3

VMware ESXi 6.0U3

Documentation

1 Earlier releases may have some TLS 1.2 support, but they are not recommended in a deployment where TLS 1.0/1.1 is disabled.

## Related Documentation

For more details about TLS 1.2 and the implications of disabling TLS 1.0 and 1.1 for on-premises Cisco Collaboration deployments, see TLS 1.2 for On-Premises Cisco Collaboration Deployments .

For on overview on configuring TLS 1.2, see the TLS 1.2 Configuration Overview Guide .

## Documentation Changes

Table 2. Documentation Changes

Date

Change

May 10, 2019

Updated wireless authentication notice for Cisco Wireless IP Phone 8821, 8821-EX.

April 02, 2019

Updated TLS support for Cisco Unified Attendant Console Standard and Cisco Unified Attendant Console Advanced .

February 11, 2019

Updated Cisco Paging Server to specify release 12.5(1) as minimum release to disable TLS 1.0 and 1.1.

August 20, 2018

Updated Cisco IP Phone 8800 Series section to include a note and a separate row for the Cisco Wireless IP Phone 8821, 8821-EX .

August 9, 2018

Added version 12.1 Service Pack1 for Cisco Prime Collaboration (Assurance and Analytics) .

June 4, 2018

Updated versions for Cisco IP Phone 7800 and 8800 Series .

Updated product names from Cisco Spark to Cisco Webex .

April 20, 2018

Added note: Earlier releases may have some TLS 1.2 support, but they are not recommended in a deployment where TLS 1.0/1.1 is disabled.

Added link to TLS 1.2 Configuration Overview Guide .

Updated versions for Cisco TMSPE .

Updated minimum version that can disable TLS version 1.0 and 1.1 for Cisco Unified Attendant Console Standard .

Updated versions for Cisco Unified Attendant Console Advanced .

December 21, 2017

Added Unified SRST 12.1 with IOS 16.7.1.

Added version 2.3 for Cisco Meeting Server .

Added Cisco Meeting Management 1.0.

Added VG Series Gateways .

Added versions for MTP/CFB (ISR G3) and MTP/CFB (ISR G2) .

October 23, 2017

In Endpoints section, changed TC7.3.10 to TC7.3.11.

October 6, 2017

Added link to related document: TLS 1.2 for On-Premises Cisco Collaboration Deployments .

October 4, 2017

For Cisco Prime Collaboration Provisioning , updated “Minimum recommended version that supports TLS 1.2” and “Minimum version that can disable TLS version 1.0 and 1.1” from Future release to 12.3 .

For Cisco TelePresence Server , updated “Minimum version that can disable TLS version 1.0 and 1.1” from Future release to 4.4(1.20) .

September 19, 2017

Added SIP PSTN Gateways G2 .

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see What’s New in Cisco Product Documentation .

To receive new and revised Cisco technical content directly to your desktop, you can subscribe to the What’s New in Cisco Product Documentation RSS feed . The RSS feeds are a free service.

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS” WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies are considered un-Controlled copies and the original on-line version should be referred to for latest version.

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at www.cisco.com/go/offices .

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

© 2018 Cisco Systems, Inc. All rights reserved.

| Product | Minimum recommended version that supports TLS 1.2 1 | Minimum version that can disable TLS version 1.0 and 1.1 | Link to product support documentation |
|---|---|---|---|
| Call Control |
| Cisco Unified Communications Manager and IM and Presence Service | 11.5(1)SU3 CTL client does not support TLS 1.2. | 11.5(1)SU3 | Support |
| Cisco Unified Survivable Remote Site Telephony | 12.1 (IOS 16.7.1) | 12.1 (IOS 16.7.1) | Support |
| Conferencing |
| Cisco Meeting Server | 2.0 | 2.3 | Support |
| Cisco Meeting App | 1.9 | Not applicable for clients. | Support |
| Cisco Meeting Management | 1.0 | 1.0 | Support |
| Cisco TelePresence Management Suite (Cisco TMS) | 15.3 | 15.3 Windows registry edit required for Windows Server lockout of pre TLS 1.2. | Support |
| Cisco TelePresence Management Suite Extension for Microsoft Exchange (Cisco TMSXE) | 5.3 Windows registry edit required. | 5.6 Windows registry edit required for Windows Server lockout of pre TLS 1.2. | Support |
| Cisco TelePresence Management Suite Provisioning Extension (Cisco TMSPE) | HTTPS server interface: 1.12.0 Client interface: None (TLS 1.2 not supported) | HTTPS server interface: 1.12.0 Client interface: Not applicable | Support |
| Cisco TelePresence Server | 2.3 | 4.4(1.20) | Support |
| Cisco TelePresence Conductor (TelePresence Conductor) | XC4.3.2 | XC4.3.2 | Support |
| Cisco Webex Meetings Server | 2.7 | 2.7 TLS 1.0 is disabled. TLS 1.1 and 1.2 allowed. | Support Release Notes |
| Enterprise Edge |
| Cisco Expressway Series | X8.10.1 | X8.10.1 | Support |
| Cisco Unified Border Element (CUBE) for ISR G3 and vCUBE | IOS XE 3.17S IOS 15.6.1S | IOS XE 16.6 | Support |
| CUBE for ISR G2 | 15.6(1)T SIP only. | 15.6(1)T SIP only. | Support |
| SIP PSTN Gateways G3 | 16.6.1 | 16.6.1 | Support |
| SIP PSTN Gateways G2 | 15.6(3)M3 | 15.6(3)M3 | Support |
| Server Applications |
| Cisco Emergency Responder | 11.5(2) | 11.5(2) | Support |
| Cisco Paging Server | 12.0.1 | 12.5(1) | Support |
| Cisco Unified Attendant Console Standard | 12.0(5) | 12.0(5) | Support |
| Cisco Unified Attendant Console Advanced | 12.0(4) | 12.0(4) | Support |
| Voicemail and Messaging |
| Cisco Unity Connection | 11.5(1)SU3 | 11.5(1)SU3 | Support |
| Endpoints |
| Cisco IP Phone 7800 Series | 12.0 | 12.1(1) | Support |
| Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, 8865NR, Cisco IP Conference Phone 8832 | 12.0 12.5 to include wireless authentication. | 12.1(1) | Support |
| Cisco Wireless IP Phone 8821, 8821-EX | 11.0(2) Except for wireless authentication, which is implemented in 11.0(5). | 11.0(5) for 8821 11.0(5)SR1 for 8821-EX | Support |
| Cisco TelePresence IX5000 | 8.2.1 | 8.2.2 | Support |
| Cisco DX70 and Cisco Webex DX80 Cisco TelePresence MX 200/300 G2, MX 700/800 Cisco TelePresence SX Series | CE 9.1.3 | CE 9.1.3 | DX Support MX Support SX Support |
| Cisco TelePresence System EX Series Cisco TelePresence MX 200/300 G1 Cisco TelePresence Integrator C Series Cisco TelePresence Profile Series | TC7.3.11 | TC7.3.11 TLS 1.0 disabled on the HTTPS server interface. TLS 1.1 or 1.2 allowed. | EX Support MX Support Integrator C Series Support Profile Series Support |
| Cisco TelePresence TX9000 Series | 6.1.13 | None. | Support |
| Cisco TelePresence System 1000 Cisco TelePresence System 1100 Cisco TelePresence System 500 Cisco TelePresence System 3200 Series | 1.10.16 | None. | 1000 Support 1100 Support 500 Support 3200 Support |
| Cisco Webex Room Kit & Plus | CE 9.1.3 | CE 9.1.3 | Support |
| Cisco Jabber | 11.7 | Not applicable for clients. | Support |
| Service Management |
| Cisco Prime Collaboration (Provisioning) | 12.3 | 12.3 | Support |
| Cisco Prime Collaboration (Assurance and Analytics) | 12.1 Service Pack1 | 12.1 Service Pack1 | Support |
| Cisco Prime Collaboration (Deployment) | 11.6(2) | 11.6(2) | Support |
| Cisco Prime License Manager | 11.5SU2 | 11.5SU2 | Support |
| Communication Gateways |
| Virtual Cisco Unified SIP Proxy Software | Future release. | None. | Support |
| Cisco VG Series Gateways (VG202XM, VG204XM, VG310, VG320, and VG350 Analog Voice Gateway) | 15.7.3M1 | 15.7.3M1 | Support for Cisco VG Series Gateways Support for Cisco VG300 Series Gateways |
| Other |
| MTP/CFB (ISR G3) | 16.7.1 | 16.7.1 |  |
| MTP/CFB (ISR G2) | 15.7.3M1 | 15.7.3M1 |  |
| Contact Center |
| Cisco Unified Contact Center Enterprise | 11.6(1) | 11.6(1) | Support |
| Cisco Unified Contact Center Express | 11.6(1) | 11.6(1) | Support |
| Third Party Applications |
| Operating System | VMware ESXi 6.0U3 | VMware ESXi 6.0U3 | Documentation |

| Date | Change |
|---|---|
| May 10, 2019 | Updated wireless authentication notice for Cisco Wireless IP Phone 8821, 8821-EX. |
| April 02, 2019 | Updated TLS support for Cisco Unified Attendant Console Standard and Cisco Unified Attendant Console Advanced . |
| February 11, 2019 | Updated Cisco Paging Server to specify release 12.5(1) as minimum release to disable TLS 1.0 and 1.1. |
| August 20, 2018 | Updated Cisco IP Phone 8800 Series section to include a note and a separate row for the Cisco Wireless IP Phone 8821, 8821-EX . |
| August 9, 2018 | Added version 12.1 Service Pack1 for Cisco Prime Collaboration (Assurance and Analytics) . |
| June 4, 2018 | Updated versions for Cisco IP Phone 7800 and 8800 Series . Updated product names from Cisco Spark to Cisco Webex . |
| April 20, 2018 | Added note: Earlier releases may have some TLS 1.2 support, but they are not recommended in a deployment where TLS 1.0/1.1 is disabled. Added link to TLS 1.2 Configuration Overview Guide . Updated versions for Cisco TMSPE . Updated minimum version that can disable TLS version 1.0 and 1.1 for Cisco Unified Attendant Console Standard . Updated versions for Cisco Unified Attendant Console Advanced . |
| December 21, 2017 | Added Unified SRST 12.1 with IOS 16.7.1. Added version 2.3 for Cisco Meeting Server . Added Cisco Meeting Management 1.0. Added VG Series Gateways . Added versions for MTP/CFB (ISR G3) and MTP/CFB (ISR G2) . |
| October 23, 2017 | In Endpoints section, changed TC7.3.10 to TC7.3.11. |
| October 6, 2017 | Added link to related document: TLS 1.2 for On-Premises Cisco Collaboration Deployments . |
| October 4, 2017 | For Cisco Prime Collaboration Provisioning , updated “Minimum recommended version that supports TLS 1.2” and “Minimum version that can disable TLS version 1.0 and 1.1” from Future release to 12.3 . For Cisco TelePresence Server , updated “Minimum version that can disable TLS version 1.0 and 1.1” from Future release to 4.4(1.20) . |
| September 19, 2017 | Added SIP PSTN Gateways G2 . |