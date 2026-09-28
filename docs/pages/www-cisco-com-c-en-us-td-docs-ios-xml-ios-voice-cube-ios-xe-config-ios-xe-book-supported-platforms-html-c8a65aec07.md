---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-supported-platforms-html-c8a65aec07
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/supported-platforms.html
retrieved_at: 2026-09-01T22:13:00.513869+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Supported Platforms

## Chapter: Supported Platforms

# Supported Platforms

## Supported
                        	 Platforms

Cisco Cloud Services Router 1000V Series (CSR 1000V) is no longer supported from Cisco IOS XE Bengaluru 17.4.1a onwards. If you are using CSR 1000V, you have to upgrade to Cisco Catalyst 8000V Edge Software (Catalyst 8000V). For End-of-Life
                                       information on CSR 1000V, see End-of-Sale and End-of-Life Announcement for the Select Cisco CSR 1000v Licenses .

Cisco Unified Border Element (CUBE) supports various platforms running on Cisco IOS XE Software Releases.

For information on migrating from existing Cisco IOS XE 3S releases to the Cisco IOS XE Denali 16.3 release, see Cisco IOS XE Denali 16.3 Migration Guide for Access and Edge Routers.

The following table provides information on Cisco router platform support for CUBE :

Cisco Router Platforms

Cisco Router Models

Cisco IOS Software Releases

Cisco 8300 Series Secure Routers Platform

C8375-E-G2

Cisco IOS XE 17.18.2

Cisco C8200L Catalyst Edge Series Platform

C8200L-1N-4T

Cisco IOS XE Bengaluru 17.5.1a

Cisco 8200 Catalyst Edge Series Platform

C8200-1N-4T

Cisco Cloud Services Routers (CSR)

Cisco Catalyst 8000V Edge Software (Catalyst 8000V)

Cisco 8300 Catalyst Edge Series Platforms

C8300-1N1S-6T

C8300-1N1S-4T2X

C8300-2N2S-6T

C8300-2N2S-4T2X

Cisco IOS XE Amsterdam 17.3.2

Cisco 4000 Series-Integrated Services Routers (ISR G3)

Cisco 4461 Integrated Services Routers

Cisco IOS XE Amsterdam 17.2.1r onwards

Cisco 1000 Series-Integrated Services Routers (ISR)

Cisco 1100 Integrated Services Router series models ISR1100 4G/6G support CUBE features when running on IOS XE

Cisco IOS XE Gibraltar 16.12.1a onwards

Cisco Aggregated Services Routers (ASR)

Cisco ASR1006-X Aggregated Services Routers with RP2 and ESP40

Cisco IOS XE Fuji 16.6.1 onwards

Cisco Aggregated Services Routers (ASR)

Cisco ASR1006-X Aggregated Services Routers with RP3 and ESP40/ESP100

Cisco IOS XE Everest 16.6.1 onwards

Cisco Cloud Services Routers (CSR)

Cisco Cloud Services Router 1000V series

Cisco IOS XE Denali 16.3.1 onwards

Cisco 4000 Series-Integrated Services Routers (ISR G3)

Cisco 4321 Integrated Services Routers

Cisco 4331 Integrated Services Routers

Cisco 4351 Integrated Services Routers

Cisco 4431 Integrated Services Routers

Cisco 4451 Integrated Services Routers

Cisco IOS XE Denali 16.3.1 onwards

Cisco Aggregated Services Routers (ASR)

Cisco ASR1001-X Aggregated Services Routers

Cisco ASR1002-X Aggregated Services Routers

Cisco ASR1004 Aggregated Services Routers with RP2

Cisco ASR1006 Aggregated Services Routers with RP2 and ESP40

Cisco IOS XE Denali 16.3.1 onwards

## Feature Comparison for Supported Platforms

The following table provides high level details of Cisco Unified Border Element (CUBE) features supported on different platforms.

Features

Cisco ASR 1000 Series Routers

Cisco ISR 4000 Series Routers

Cisco ISR 1000 Series Routers

C8375-E-G2 Routers

High Availability Implementation

Redundancy Group Infrastructure

Redundancy Group Infrastructure

No

Yes

Media Forking

Yes (Cisco IOS XE Release 3.8S onwards)

Yes (Cisco IOS XE Release 3.10S onwards)

No

Yes

DSP Card Type

SPA-DSP

PVDM4

SM-X-PVDM

No

Virtual DSP (vDSP)

Transcoder registered to CUCM

No

Yes (Exists via SCCP - Cisco IOS XE Release 3.11S onwards)

No

Yes

Transcoder—LTI

Yes

Yes

No

Yes

Cisco UC Gateway Services API

Yes (Cisco IOS XE Release 3.8S onwards)

Yes

Yes

Yes

Noise Reduction and ASP

Yes

Yes

No

Yes

Call Progress Analysis

Yes

(Cisco IOS XE Release 3.9S onwards ; Recommended - Cisco IOS XE Release 3.15S)

Yes

Recommended - Cisco IOS XE Release 3.15S

No

Yes

SRTP-RTP Interworking

Yes - No DSP resources required

(Cisco IOS XE Release 3.7S onwards)

Cisco IOS XE Release 3.12S onwards

Yes - No DSP resources required

Yes

CUBE for SP Managed and Hosted Services

Yes

Yes

Yes

Unified SRST colocation with CUBE

Not supported

Yes (Cisco IOS XE Fuji 16.7.1 Release onwards)

Yes. From Cisco IOS XE Bengaluru 17.5.1a

Yes

IPv6

Yes

Yes

Yes

Yes

Features

Cisco CSR 1000V Series Routers

Cisco 8000V Catalyst Series Edge Platforms

Cisco 8300 Catalyst Edge Series Platforms

Cisco 8200 Catalyst Edge Series Platforms

HA Implementation

RG Infrastructure

RG Infrastructure

RG Infrastructure

RG Infrastructure

Media Forking

Yes

Yes

Yes

Yes

DSP Card Type

No

No

NIM-PVDM

SM-X-PVDM

NIM-PVDM

Transcoder registered to CUCM

No

No

Yes (via SCCP)

Yes (via SCCP)

Transcoder—LTI

No

No

Yes

Yes

Cisco UC Gateway Services API

Yes

Yes

Yes

Yes

Noise Reduction & ASP

No

No

Yes

Yes

Call Progress Analysis

No

No

Yes

Yes

SRTP-RTP interworking

Yes - No DSP resources required

Yes - No DSP resources required

Yes - No DSP resources required

Yes - No DSP resources required

CUBE for SP Managed and Hosted Services

Yes

Yes

Yes

Yes

Unified SRST colocation with CUBE

Not supported

No

Yes

Yes

IPv6

Yes

Yes

Yes

Yes

For more information on Unified SRST and CUBE Colocation, see Unified SRST and Unified Border Element Co-location .

Colocation of CUBE —High Availability (HA) with Unified SRST is not supported.

Starting from Cisco IOS XE 17.18.2 release, CUBE is supported on C8375-E-G2 secure routers with vDSP (Virtual DSP) enabled. These secure routers offer software-based
                                       DSP capabilities, effectively replacing traditional Packet Voice Digital Signal Processor Modules (PVDMs). The vDSP feature
                                       provides DSP resources in software, allowing voice processing functions like transcoding, conferencing, and hardware media
                                       termination point services to be handled by the router’s CPU instead of requiring dedicated DSP hardware. For details on vDSP
                                       installation, upgrade, downgrade configurations, see Virtual DSP for Secure Routers .

### Virtual Cube

## vCUBE

Virtual CUBE ( vCUBE ) is virtual deployment of Cisco Unified Border Element (CUBE) feature set.

From Cisco IOS XE Bengaluru 17.4.1a , vCUBE is available for use with Cisco® Catalyst® 8000V Edge Software (Catalyst 8000V) series.

H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

vCUBE qualification for Catalyst 8000V on Nutanix AHV

Cisco IOS XE 26.1.1

vCUBE is qualified on Cisco Catalyst 8000V running on Nutanix AHV.

vCUBE in Microsoft Azure

Cisco IOS XE Bengaluru 17.6.3a

vCUBE offer is introduced in Microsoft Azure for Cisco Catalyst 8000V Edge Software (Catalyst 8000V).

vCUBE Catalyst 8000V Edge Software (Catalyst 8000V)

vCUBE introduced for Cisco Catalyst 8000V Edge Software (Catalyst 8000V) in VMware ESXi environments and AWS environment.

vCUBE in Amazon Web Services (AWS)

## Prerequisites

### Hardware

The vCUBE features are supported as part of the Cisco Catalyst 8000V router platform in both Nutanix AHV and VMware ESXi virtualized
                                    environments. For supported hardware and hypervisors, see Install Cisco Catalyst 8000V in Nutanix AHV Hypervisor , Install the Cisco CSR 1000V in VMware ESXi Environments , and Cisco Catalyst 8000V Edge Software .

For information on the best practices for setting ESXi host BIOS parameters for performance, see BIOS Settings .

vCUBE is supported in both AWS and Microsoft Azure. Use the AWS Marketplace or Azure Marketplace product listing for the virtual
                                    CUBE, as applicable. For more information, see the Cisco CSR 1000V Series Cloud Services Router Deployment Guide for Amazon Web Services , Cisco C8000V Router Deployment Guide for Amazon Web Services , and Deploying Cisco Catalyst 8000V Edge Software on Microsoft Azure .

The Cisco Catalyst 8000V router platform may be used in several different public and private cloud environments. However,
                                                vCUBE is only supported when deployed on VMware ESXi, AWS, and Microsoft Azure platforms currently.

When you use a consolidated (.bin) image to upgrade a CSR 1000V medium configuration (2 vCPU, 4 GB RAM) to Catalyst 8000V,
                                                you must change the virtual machine vRAM allocation to at least 5 GB to ensure advertised performance. When deploying in AWS
                                                environments, boot the router using individual packages rather than a consolidated image without the need for extra memory.
                                                Refer to Installing Subpackages from a Consolidated Package for details.

### Software

Obtain the relevant license for the router platform. See vCUBE Licensing Requirements for more information.

In AWS platform, only Bring Your Own License (BYOL) is supported for vCUBE . Pay as You Go (Subscription) versions of the CSR 1000V and C8000V are not supported. Make sure you choose the vCUBE AWS Marketplace product listing. Refer to Cisco Virtual CUBE-BYOL for details.

In Microsoft Azure platform, only Bring Your Own License (BYOL) is supported for vCUBE . Pay as You Go (Subscription) versions of the C8000V are not supported. Make sure you choose the vCUBE Azure Marketplace product listing. Refer to Cisco Virtual CUBE-BYOL for details.

For more information about Cisco virtual routers, see CSR 1000V Data Sheet and Catalyst 8000V Data Sheet.

## Supported instance types for Amazon Web Services and Microsoft Azure

vCUBE on Cisco Catalyst 8000V running on Amazon Web Services (AWS) or Microsoft Azure supports VM with 4 vCPU 8 GB RAM, and
                              8 vCPU 16 GB RAM instance types.

The c5.xlarge (AWS), and Standard D4lds v5 (Azure) instance types are validated.

## Features Supported

vCUBE supports most of the CUBE features available in IOS XE releases.

From Cisco IOS XE Cupertino
                                             17.8.1a onwards, Catalyst 8000V supports software MTP for Cisco Unified Communications Manager.

vCUBE does not support the following:

DSP-based features

Codec
                                       				  Transcoding, Transrating

Raw in-band to RTP-NTE DTMF Interworking

Call
                                       				  Progress Analysis (CPA)

Noise
                                       				  Reduction (NR), Acoustic Shock Protection (ASP), and Audio Gain

IOS-based Hardware MTP

CUBE high availability is not supported on vCUBE when deployed in AWS and Microsoft Azure platforms.

## Virtual CUBE Support on Cisco CSR 1000V or C8000V Series Routers

vCUBE media performance depends on the underlying host platform consistently providing packet switching latency of less than
                           5 milliseconds. The recommended hardware and virtual machine configurations ensure this performance when followed closely.
                           For more information on how to monitor media performance, see Voice Quality Monitoring .

### vCUBE Licensing Requirements

#### vCUBE with CSR1000V

vCUBE is enabled for the CSR1000V with the APPX and AX platform licenses. vCUBE processes and CLI commands are enabled when either of these licenses are enabled. Secure call features require the AX license.
                                 In common with all CUBE instances, CUBE smart licenses are required for each active session.

The following table details the license requirements for vCUBE on the CSR1000V.

Virtual CUBE Session License

Platform License

Features

Throughput License

CUBE Smart Licenses

APPX

No TLS / SRTP support

Session count * (signaling + bidirectional media bandwidth)

AX

All vCUBE features

For detailed information about licensing, see Cisco CSR 1000V Series cloud services Router Configuration Guide and Smart Licensing .

#### vCUBE with C8000V

vCUBE is enabled for the C8000V with the DNA Network Essentials with an appropriate bandwidth tier license.

When upgrading to C8000V software from a CSR1000V release, an existing throughput configuration is reset to a maximum of 250
                                             Mbps. Install an HSEC authorization code, which you can obtain from your Smart License account, before reconfiguring your
                                             required throughput level.

Virtual CUBE Session License

DNA Subscription

Features

Bandwidth Tier License

CUBE Smart Licenses

Essentials or above

All vCUBE features

Session count * (signaling + media bandwidth)

For detailed information on licensing, see Licensing .

## Installation

You can install Virtual CUBE in two ways:

Install using an
                                 			 OVA file

Install using an
                                 			 ISO image

### Install vCUBE on ESXi

Use the CSR1000V or the C8000V OVA application file (available from software.cisco.com ) to deploy a new virtual instance directly in VMware ESXi.

For further details on how to perform the deployment, see Cisco CSR 1000V Series Cloud Services Router Software Configuration Guide or Cisco Catalyst 8000V Edge Software Installation And Configuration Guide .

## Enable vCUBE

Step 1

Power on the virtual machine.

Step 2

Enable platform and throughput licenses and register to a Cisco licensing server.

Step 3

Perform the steps Enable the CUBE Application on a Device to enable vCUBE .

## Troubleshoot vCUBE

To troubleshoot vCUBE , follow the same procedure as that of Cisco hardware routers. This includes crash file decoding, decoding traceback, and
                           so on. For more details, see Troubleshoot Cisco ASR 1000 Series Aggregation Services Routers Crashes .

To troubleshoot Virtual Machine (VM) issues, see Cisco CSR 1000V Series Cloud Services Router Software Configuration Guide and Cisco Catalyst 8000V Edge Software Configuration Guide .

| Note | Cisco Cloud Services Router 1000V Series (CSR 1000V) is no longer supported from Cisco IOS XE Bengaluru 17.4.1a onwards. If you are using CSR 1000V, you have to upgrade to Cisco Catalyst 8000V Edge Software (Catalyst 8000V). For End-of-Life
                                       information on CSR 1000V, see End-of-Sale and End-of-Life Announcement for the Select Cisco CSR 1000v Licenses . |
|---|---|

| Note | For information on migrating from existing Cisco IOS XE 3S releases to the Cisco IOS XE Denali 16.3 release, see Cisco IOS XE Denali 16.3 Migration Guide for Access and Edge Routers. |
|---|---|

| Cisco Router Platforms | Cisco Router Models | Cisco IOS Software Releases |
|---|---|---|
| Cisco 8300 Series Secure Routers Platform | C8375-E-G2 | Cisco IOS XE 17.18.2 |
| Cisco C8200L Catalyst Edge Series Platform | C8200L-1N-4T | Cisco IOS XE Bengaluru 17.5.1a |
| Cisco 8200 Catalyst Edge Series Platform | C8200-1N-4T | Cisco IOS XE Bengaluru 17.4.1a |
| Cisco Cloud Services Routers (CSR) | Cisco Catalyst 8000V Edge Software (Catalyst 8000V) | Cisco IOS XE Bengaluru 17.4.1a onwards |
| Cisco 8300 Catalyst Edge Series Platforms | C8300-1N1S-6T C8300-1N1S-4T2X C8300-2N2S-6T C8300-2N2S-4T2X | Cisco IOS XE Amsterdam 17.3.2 |
| Cisco 4000 Series-Integrated Services Routers (ISR G3) | Cisco 4461 Integrated Services Routers | Cisco IOS XE Amsterdam 17.2.1r onwards |
| Cisco 1000 Series-Integrated Services Routers (ISR) | Cisco 1100 Integrated Services Router series models ISR1100 4G/6G support CUBE features when running on IOS XE | Cisco IOS XE Gibraltar 16.12.1a onwards |
| Cisco Aggregated Services Routers (ASR) | Cisco ASR1006-X Aggregated Services Routers with RP2 and ESP40 | Cisco IOS XE Fuji 16.6.1 onwards |
| Cisco Aggregated Services Routers (ASR) | Cisco ASR1006-X Aggregated Services Routers with RP3 and ESP40/ESP100 | Cisco IOS XE Everest 16.6.1 onwards |
| Cisco Cloud Services Routers (CSR) | Cisco Cloud Services Router 1000V series | Cisco IOS XE Denali 16.3.1 onwards |
| Cisco 4000 Series-Integrated Services Routers (ISR G3) | Cisco 4321 Integrated Services Routers Cisco 4331 Integrated Services Routers Cisco 4351 Integrated Services Routers Cisco 4431 Integrated Services Routers Cisco 4451 Integrated Services Routers | Cisco IOS XE Denali 16.3.1 onwards |
| Cisco Aggregated Services Routers (ASR) | Cisco ASR1001-X Aggregated Services Routers Cisco ASR1002-X Aggregated Services Routers Cisco ASR1004 Aggregated Services Routers with RP2 Cisco ASR1006 Aggregated Services Routers with RP2 and ESP40 | Cisco IOS XE Denali 16.3.1 onwards |

| Features | Cisco ASR 1000 Series Routers | Cisco ISR 4000 Series Routers | Cisco ISR 1000 Series Routers | C8375-E-G2 Routers |
|---|---|---|---|---|
| High Availability Implementation | Redundancy Group Infrastructure | Redundancy Group Infrastructure | No | Yes |
| Media Forking | Yes (Cisco IOS XE Release 3.8S onwards) | Yes (Cisco IOS XE Release 3.10S onwards) | No | Yes |
| DSP Card Type | SPA-DSP | PVDM4 SM-X-PVDM | No | Virtual DSP (vDSP) |
| Transcoder registered to CUCM | No | Yes (Exists via SCCP - Cisco IOS XE Release 3.11S onwards) | No | Yes |
| Transcoder—LTI | Yes | Yes | No | Yes |
| Cisco UC Gateway Services API | Yes (Cisco IOS XE Release 3.8S onwards) | Yes | Yes | Yes |
| Noise Reduction and ASP | Yes | Yes | No | Yes |
| Call Progress Analysis | Yes (Cisco IOS XE Release 3.9S onwards ; Recommended - Cisco IOS XE Release 3.15S) | Yes Recommended - Cisco IOS XE Release 3.15S | No | Yes |
| SRTP-RTP Interworking | Yes - No DSP resources required (Cisco IOS XE Release 3.7S onwards) | Yes - No DSP resources required Cisco IOS XE Release 3.12S onwards | Yes - No DSP resources required | Yes |
| CUBE for SP Managed and Hosted Services | Yes | Yes | Yes | Yes |
| Unified SRST colocation with CUBE | Not supported | Yes (Cisco IOS XE Fuji 16.7.1 Release onwards) | Yes. From Cisco IOS XE Bengaluru 17.5.1a | Yes |
| IPv6 | Yes | Yes | Yes | Yes |

| Features | Cisco CSR 1000V Series Routers | Cisco 8000V Catalyst Series Edge Platforms | Cisco 8300 Catalyst Edge Series Platforms | Cisco 8200 Catalyst Edge Series Platforms |
|---|---|---|---|---|
| HA Implementation | RG Infrastructure | RG Infrastructure | RG Infrastructure | RG Infrastructure |
| Media Forking | Yes | Yes | Yes | Yes |
| DSP Card Type | No | No | NIM-PVDM SM-X-PVDM | NIM-PVDM |
| Transcoder registered to CUCM | No | No | Yes (via SCCP) | Yes (via SCCP) |
| Transcoder—LTI | No | No | Yes | Yes |
| Cisco UC Gateway Services API | Yes | Yes | Yes | Yes |
| Noise Reduction & ASP | No | No | Yes | Yes |
| Call Progress Analysis | No | No | Yes | Yes |
| SRTP-RTP interworking | Yes - No DSP resources required | Yes - No DSP resources required | Yes - No DSP resources required | Yes - No DSP resources required |
| CUBE for SP Managed and Hosted Services | Yes | Yes | Yes | Yes |
| Unified SRST colocation with CUBE | Not supported | No | Yes | Yes |
| IPv6 | Yes | Yes | Yes | Yes |

| Note | For more information on Unified SRST and CUBE Colocation, see Unified SRST and Unified Border Element Co-location . Colocation of CUBE —High Availability (HA) with Unified SRST is not supported. |
|---|---|

| Note | Starting from Cisco IOS XE 17.18.2 release, CUBE is supported on C8375-E-G2 secure routers with vDSP (Virtual DSP) enabled. These secure routers offer software-based
                                       DSP capabilities, effectively replacing traditional Packet Voice Digital Signal Processor Modules (PVDMs). The vDSP feature
                                       provides DSP resources in software, allowing voice processing functions like transcoding, conferencing, and hardware media
                                       termination point services to be handled by the router’s CPU instead of requiring dedicated DSP hardware. For details on vDSP
                                       installation, upgrade, downgrade configurations, see Virtual DSP for Secure Routers . |
|---|---|

| Note | H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications. |
|---|---|

| Feature Name | Releases | Feature Information |
|---|---|---|
| vCUBE qualification for Catalyst 8000V on Nutanix AHV | Cisco IOS XE 26.1.1 | vCUBE is qualified on Cisco Catalyst 8000V running on Nutanix AHV. |
| vCUBE in Microsoft Azure | Cisco IOS XE Bengaluru 17.6.3a | vCUBE offer is introduced in Microsoft Azure for Cisco Catalyst 8000V Edge Software (Catalyst 8000V). |
| vCUBE Catalyst 8000V Edge Software (Catalyst 8000V) | Cisco IOS XE Bengaluru 17.4.1a | vCUBE introduced for Cisco Catalyst 8000V Edge Software (Catalyst 8000V) in VMware ESXi environments and AWS environment. |
| vCUBE in Amazon Web Services (AWS) | Cisco IOS XE Gibraltar 16.12.4a | vCUBE offer introduced in AWS for Cisco CSR 1000v Series Cloud Services Router |

| Note | The Cisco Catalyst 8000V router platform may be used in several different public and private cloud environments. However,
                                                vCUBE is only supported when deployed on VMware ESXi, AWS, and Microsoft Azure platforms currently. When you use a consolidated (.bin) image to upgrade a CSR 1000V medium configuration (2 vCPU, 4 GB RAM) to Catalyst 8000V,
                                                you must change the virtual machine vRAM allocation to at least 5 GB to ensure advertised performance. When deploying in AWS
                                                environments, boot the router using individual packages rather than a consolidated image without the need for extra memory.
                                                Refer to Installing Subpackages from a Consolidated Package for details. |
|---|---|

| Note | The c5.xlarge (AWS), and Standard D4lds v5 (Azure) instance types are validated. |
|---|---|

| Note | From Cisco IOS XE Cupertino
                                             17.8.1a onwards, Catalyst 8000V supports software MTP for Cisco Unified Communications Manager. |
|---|---|

| Note | CUBE high availability is not supported on vCUBE when deployed in AWS and Microsoft Azure platforms. |
|---|---|

| Virtual CUBE Session License | Platform License | Features | Throughput License |
|---|---|---|---|
| CUBE Smart Licenses | APPX | No TLS / SRTP support | Session count * (signaling + bidirectional media bandwidth) |
| AX | All vCUBE features |

| Note | When upgrading to C8000V software from a CSR1000V release, an existing throughput configuration is reset to a maximum of 250
                                             Mbps. Install an HSEC authorization code, which you can obtain from your Smart License account, before reconfiguring your
                                             required throughput level. |
|---|---|

| Virtual CUBE Session License | DNA Subscription | Features | Bandwidth Tier License |
|---|---|---|---|
| CUBE Smart Licenses | Essentials or above | All vCUBE features | Session count * (signaling + media bandwidth) |

| Command or Action | Purpose |
|---|---|
| Use the CSR1000V or the C8000V OVA application file (available from software.cisco.com ) to deploy a new virtual instance directly in VMware ESXi. | Note Select the required instance size during the OVA deployment. For further details on how to perform the deployment, see Cisco CSR 1000V Series Cloud Services Router Software Configuration Guide or Cisco Catalyst 8000V Edge Software Installation And Configuration Guide . | Note | Select the required instance size during the OVA deployment. |
| Note | Select the required instance size during the OVA deployment. |

| Note | Select the required instance size during the OVA deployment. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Power on the virtual machine. |  |
| Step 2 | Enable platform and throughput licenses and register to a Cisco licensing server. |  |
| Step 3 | Perform the steps Enable the CUBE Application on a Device to enable vCUBE . |  |