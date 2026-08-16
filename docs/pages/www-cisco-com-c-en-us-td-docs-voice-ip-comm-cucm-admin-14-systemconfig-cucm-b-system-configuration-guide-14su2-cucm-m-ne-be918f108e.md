---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14-systemconfig-cucm-b-system-configuration-guide-14su2-cucm-m-ne-be918f108e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14/systemConfig/cucm_b_system-configuration-guide-14su2/cucm_m_new-and-changed-information-sysconfig.html
retrieved_at: 2026-08-16T16:29:43.173090+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: August 7, 2026

Chapter: New and Changed Information

## Chapter: New and Changed Information

- New and Changed Information

- New and Changed Information

# New and Changed Information

## New and Changed Information

The following table provides an overview of the significant changes to the features in this guide up to this current release.
                              The table does not provide an exhaustive list of all changes made to the guide or of the new features up to this release.

Change History

Description

See

Date

Call Control Discovery via Service Advertisement Framework in Unified Communications Manager

Removed support for Call Control Discovery via Service Advertisement Framework in Unified Communications Manager

July 31, 2025

Smart Receiver Transport

Updates for Smart Licensing

Configure Connection to Smart Software Licensing (Applicable from Release 14SU4 and 15SU2 Onwards)

May 30, 2024

The System guide was re-published for Release 14SU3.

—

May 18, 2023

DTMF SRTP interworking

Currently, Unified Communications Manager inserts MTP for a DTMF mismatch in both secure and non-secure calls. But for secure
                                          calls, though MTP is inserted for a DTMF mismatch, it just passes through the media between the parties. Hence, the DTMF events
                                          are not sent between the parties. Before Unified CM Release 14SU3, DTMF translation worked only for non-secure calls when
                                          there was an MTP allocated for a DTMF mismatch.

With this release, Unified CM can invoke a hardware MTP (with SRTP DTMF interwork support) for a DTMF mismatch between secure
                                          endpoints.

SRTP DTMF Interworking

May 18, 2023

iOS Local Push Connectivity for Calls

Webex App is not notified of incoming VoIP call notifications when an iOS device operates in a Wi-Fi constrained network with
                                          no internet connection such as, hospitals, cruise ships, airplane, and so on. Due to lack of internet connectivity, the device
                                          does not have access to the Apple Push Notification Service (APNS). Users expect to receive calls without any delay. However,
                                          with APNS a call can be delayed for a few seconds when there is a network latency.

With this release, Local Push Notification Service (LPNS) for calls has been introduced on Apple devices. It helps to minimize
                                          any delay as the push message is sent to the client through a persistent connection.

Common Service Ports

Signaling, Media, and Other Communication Between Phones and Cisco Unified Communications Manager

May 18, 2023

Release 14SU2

The System guide was re-published for Release 14SU2. No technical features were introduced for this release.

—

June 16, 2022

Release 14SU1

The System guide was re-published for Release 14SU1.

—

October 27, 2021

Opus Codec Transcoder Support

Unified Communications Manager now includes Skinny Client Control Protocol (SCCP) controlled iOS-based registered media resource
                                          that supports transcoding Opus audio codec that is required for successful media negotiation.

Opus Codec Transcoder Support

October 27, 2021

TFTP Proxy Support for OAuth

Unified Communications Manager supports TFTP Proxy in SIP OAuth deployments.

Configure TFTP Server Dynamically

Configure TFTP Server Manually

October 27, 2021

Release 14

Initial publication of the System guide.

—

March 31, 2021

Enable SIP OAuth for 78xx and 88xx Phones

SIP OAuth provides end to end secure signaling and media encryption without CAPF on-premises as well as over MRA and by default,
                                          TFTP is secure for SIP phones when SIP OAuth is enabled.

Set Registration Method to use Activation Codes

Activation Code Use Cases

March 31, 2021

Version Independent Licensing

Unified Communications Manager supports Version Independent User Licenses. The Licenses are annuity-style and issued for the
                                          subscription term. You can order these V14 licenses through Flex EA (Enterprise Agreement) or Flex NU (Named User—Professional,
                                          Enhanced, Access).

Smart Software Licensing

March 31, 2021

| Change History | Description | See | Date |
|---|---|---|---|
| Call Control Discovery via Service Advertisement Framework in Unified Communications Manager | Removed support for Call Control Discovery via Service Advertisement Framework in Unified Communications Manager | Call Routing Restrictions | July 31, 2025 |
| Smart Receiver Transport | Updates for Smart Licensing | Configure Connection to Smart Software Licensing (Applicable from Release 14SU4 and 15SU2 Onwards) | May 30, 2024 |
| Update for Release 14SU3 | The System guide was re-published for Release 14SU3. | — | May 18, 2023 |
| DTMF SRTP interworking | Currently, Unified Communications Manager inserts MTP for a DTMF mismatch in both secure and non-secure calls. But for secure
                                          calls, though MTP is inserted for a DTMF mismatch, it just passes through the media between the parties. Hence, the DTMF events
                                          are not sent between the parties. Before Unified CM Release 14SU3, DTMF translation worked only for non-secure calls when
                                          there was an MTP allocated for a DTMF mismatch. With this release, Unified CM can invoke a hardware MTP (with SRTP DTMF interwork support) for a DTMF mismatch between secure
                                          endpoints. | SRTP DTMF Interworking | May 18, 2023 |
| iOS Local Push Connectivity for Calls | Webex App is not notified of incoming VoIP call notifications when an iOS device operates in a Wi-Fi constrained network with
                                          no internet connection such as, hospitals, cruise ships, airplane, and so on. Due to lack of internet connectivity, the device
                                          does not have access to the Apple Push Notification Service (APNS). Users expect to receive calls without any delay. However,
                                          with APNS a call can be delayed for a few seconds when there is a network latency. With this release, Local Push Notification Service (LPNS) for calls has been introduced on Apple devices. It helps to minimize
                                          any delay as the push message is sent to the client through a persistent connection. | Common Service Ports Signaling, Media, and Other Communication Between Phones and Cisco Unified Communications Manager | May 18, 2023 |
| Release 14SU2 | The System guide was re-published for Release 14SU2. No technical features were introduced for this release. | — | June 16, 2022 |
| Release 14SU1 | The System guide was re-published for Release 14SU1. | — | October 27, 2021 |
| Opus Codec Transcoder Support | Unified Communications Manager now includes Skinny Client Control Protocol (SCCP) controlled iOS-based registered media resource
                                          that supports transcoding Opus audio codec that is required for successful media negotiation. | Opus Codec Transcoder Support | October 27, 2021 |
| TFTP Proxy Support for OAuth | Unified Communications Manager supports TFTP Proxy in SIP OAuth deployments. | Configure TFTP Server Dynamically Configure TFTP Server Manually | October 27, 2021 |
| Release 14 | Initial publication of the System guide. | — | March 31, 2021 |
| Enable SIP OAuth for 78xx and 88xx Phones | SIP OAuth provides end to end secure signaling and media encryption without CAPF on-premises as well as over MRA and by default,
                                          TFTP is secure for SIP phones when SIP OAuth is enabled. | Set Registration Method to use Activation Codes Activation Code Use Cases | March 31, 2021 |
| Version Independent Licensing | Unified Communications Manager supports Version Independent User Licenses. The Licenses are annuity-style and issued for the
                                          subscription term. You can order these V14 licenses through Flex EA (Enterprise Agreement) or Flex NU (Named User—Professional,
                                          Enhanced, Access). | Smart Software Licensing | March 31, 2021 |