---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb12-0-installation-guide-cvvp-b-migr-8c53a55695
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb12_0/installation/guide/cvvp_b_migration-guide-1201/cvvp_b_migration-guide-1201_chapter_011.html
retrieved_at: 2026-08-21T16:28:46.976643+00:00
---

Migration Guide for Cisco Virtualized Voice Browser, Release 12.0(1)

# Migration Guide for Cisco Virtualized Voice Browser, Release 12.0(1)

Updated: January 11, 2019

Chapter: Features Comparison

## Chapter: Features Comparison

- Features Comparison

- Feature Comparison

# Features Comparison

## Feature Comparison

The Feature Comparison table lists the features that are available on Cisco IOS and Cisco VVB.

Feature

Cisco IOS

Cisco VVB

Comprehensive Call Model

Supported

Supported

Standalone Call Model

Supported

Supported

VRU-only
                                       					 Call Model

Supported

Supported

WAAG

Supported

Supported

CCB

Supported

Supported

Sigdigit

Supported

Supported

Codec:
                                       					 G.711 a law / u law

Supported

Supported

Codec:
                                       					 G.729

Supported

Supported

HTTPS

Supported

Supported

Transfer

Blind
                                       					 and Consultative Transfer in Standalone Call Model

Blind (using REFER method) and Bridge Transfer Support in Standalone Call Model.

MRCPv1
                                       					 and v2

Supported

Supported

Local
                                       					 Prompts

Supported

Supported

Hostname
                                       					 Resolution

Supported

Supported

Rest API
                                       					 for Configuration

Not
                                       					 supported

Supported

CLIs

Vast

Platform, Call summary, Cache, HTTP client, MRCP statistics

Real
                                       					 Time Reporting

Not
                                       					 supported

Supported

RTMT
                                       					 Support

Not
                                       					 supported

Supported

Prime
                                       					 Support

Limited

Supported

TLS

1.0, 1.1

1.0, 1.1, 1.2 (default)

Cisco VXML Tags (CVP Call Studio)

Supported

Supported

Hardware
                                       					 Platforms

See https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html

Spec
                                       					 based hardware, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html

RTSP
                                       					 Streaming

Supported

Not
                                       					 supported

Video in
                                       					 Queue

Supported

Not
                                       					 supported

RSM

Supported

Not supported

Grammar Types

Supported

Supported types: application/srgs+xml , application/grammar+xml , and application/grammar+regex

Digit Element

Grammar accepts only digits from 0 – 9

Grammar accepts digits from 0 – 9 , "#", and "*". "#" is the default termination character. You can mark any digit or DTMF
                                       character as termination character by adding it in custom VXML property.

Custom SIP header passing to a VXML server

Supported

Supported

For more information, see Custom SIP header passing to a VXML server in Solution Design Guide for Cisco Unified Contact Center Enterprise and Solution Design Guide for Cisco Packaged Contact Center Enterprise.

To know whether any script changes are required while migrating from IOS VXML to VVB for Conformance 2.0 and Conformance 2.1 , refer to CSCvk32060 .

| Feature | Cisco IOS | Cisco VVB |
|---|---|---|
| Comprehensive Call Model | Supported | Supported |
| Standalone Call Model | Supported | Supported |
| VRU-only
                                       					 Call Model | Supported | Supported |
| WAAG | Supported | Supported |
| CCB | Supported | Supported |
| Sigdigit | Supported | Supported |
| Codec:
                                       					 G.711 a law / u law | Supported | Supported |
| Codec:
                                       					 G.729 | Supported | Supported |
| HTTPS | Supported | Supported |
| Transfer | Blind
                                       					 and Consultative Transfer in Standalone Call Model | Blind (using REFER method) and Bridge Transfer Support in Standalone Call Model. |
| MRCPv1
                                       					 and v2 | Supported | Supported |
| Local
                                       					 Prompts | Supported | Supported |
| Hostname
                                       					 Resolution | Supported | Supported |
| Rest API
                                       					 for Configuration | Not
                                       					 supported | Supported |
| CLIs | Vast | Platform, Call summary, Cache, HTTP client, MRCP statistics |
| Real
                                       					 Time Reporting | Not
                                       					 supported | Supported |
| RTMT
                                       					 Support | Not
                                       					 supported | Supported |
| Prime
                                       					 Support | Limited | Supported |
| TLS | 1.0, 1.1 | 1.0, 1.1, 1.2 (default) |
| Cisco VXML Tags (CVP Call Studio) | Supported | Supported |
| Hardware
                                       					 Platforms | See https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html | Spec
                                       					 based hardware, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html |
| RTSP
                                       					 Streaming | Supported | Not
                                       					 supported |
| Video in
                                       					 Queue | Supported | Not
                                       					 supported |
| RSM | Supported | Not supported |
| Grammar Types | Supported | Supported types: application/srgs+xml , application/grammar+xml , and application/grammar+regex |
| Digit Element | Grammar accepts only digits from 0 – 9 | Grammar accepts digits from 0 – 9 , "#", and "*". "#" is the default termination character. You can mark any digit or DTMF
                                       character as termination character by adding it in custom VXML property. |
| Custom SIP header passing to a VXML server | Supported | Supported For more information, see Custom SIP header passing to a VXML server in Solution Design Guide for Cisco Unified Contact Center Enterprise and Solution Design Guide for Cisco Packaged Contact Center Enterprise. |