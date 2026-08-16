---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-78c483156d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct_b_1501_cce-solutions-rns/rcct_m_1501_cisco-unified-customer-voice-portal.html
retrieved_at: 2026-08-16T19:36:41.913450+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

# Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

Updated: April 30, 2025

Chapter: Cisco Unified Customer Voice Portal

## Chapter: Cisco Unified Customer Voice Portal

# Cisco Unified Customer Voice Portal

## New Features

### Media Forking using Media Gateway for Contact Center AI Services

Cisco Contact Center Enterprise (CCE) has enhanced the Cisco Virtualized Voice Browser (VVB) to function as a Media Gateway.
                              This enhancement enables the management of media forking for the agent and caller leg of the call flow. The media forking
                              process is initiated by Cisco Unified Border Element (CUBE) or any third-party Session Border Controllers (SBCs) to efficiently
                              handle and route the forked media streams to the Contact Center AI (CCAI) Orchestrator services. This architecture supports
                              the real-time delivery of media streams to AI services for transcription, natural language understanding, and agent assistance
                              features such as Agent Answers and Call Transcription, thereby enhancing customer experience and operational efficiency.

CVP (along with CVP ES 202508 with CVP15.0(2)_ET4_7_build_0.exe) supports media forking with Media Gateway.

This enhancement aligns with Cisco's transition from WebSocket-based media forking to a more robust and standardized SIPREC-based
                              media forking mechanism, improving scalability, security, and compatibility with multiple AI providers, enabling flexible
                              AI enhancements for contact center agent interactions.

For detailed design considerations, refer to the Solution Design Guide for Cisco Contact Center Enterprise .

### Log Collection for VVB Cisco Speech Server Service

The Cisco Real-Time Monitoring Tool (RTMT) has expanded its capabilities to include the collection of Cisco Speech Server
                              logs (in addition to the previously supported Cisco VVB logs and Platform Services logs) from multiple Cisco VVBs. This enhancement
                              enables a streamlined and centralized log collection process.

For more information, see the Cisco Virtualized Voice Browser Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-and-configuration-guides-list.html .

### Ability to Host Custom Code Applications

CVP  supports hosting and running custom code applications. You can easily migrate existing CVP applications, whether hosted
                              locally or on remote servers, to other remote servers without disrupting ongoing calls using VXML and Call servers. This allows
                              you to separate your custom code from the core VXML application, allowing easier identification and isolation of unexpected
                              issues. Overall, it boosts the computing power and scalability for the components involved.

For more information on how to install and configure custom code using remote server, refer to the following documents:

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal

Configuration Guide for Cisco Unified Customer Voice Portal

## Updated Features

### Enhanced Scalability

Cisco VVB has undergone a significant scalability enhancement, greatly increasing its capacity to handle concurrent calls
                              and delivering enhanced value to our customers.

With the latest improvements in release 15.0(1), the Medium OVA profile now supports up to 1,000 concurrent calls using the
                              Traditional Call Flow , which includes Audio Playback and DTMF handling, over secure or non-secure signaling and up to 750
                              concurrent calls for ASR-TTS-based flows, with secure or non-secure signaling and media.

This capability also extends to 750 concurrent calls involving Virtual Agent Voice (VAV), as well as a combination of VAV,
                              Traditional, and ASR-TTS call flows, all supporting secure or non-secure signaling and media.

Similarly, the Small OVA profile now supports up to 800 concurrent calls using the Traditional Call Flow, and up to 600 ASR-TTS-based
                              calls, both over secure or non-secure signaling and media, with up to 600 concurrent VAV calls and combinations of VAV, Traditional,
                              and ASR-TTS flows also supported.

These enhancements are designed to optimize resource utilization and streamline call flow management, enabling more efficient
                              operations while minimizing the need for additional hardware.

By optimizing these profiles, Cisco VVB ensures improved system performance and scalability, allowing seamless handling of
                              peak loads with reduced hardware investments, providing our customers with increased efficiency and cost savings.

For more information, see the Cisco Virtualized Voice Browser Sizing section in the Sizing and Operating Conditions for Reference
                              Designs chapter of the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

### Enhanced Blind Transfer

Previously, when transferring calls, Cisco VVB did not wait for a response from the remote server nor communicate that response
                              to the VXML, leading to predefined application flows. However, with the recent upgrade to the Blind Transfer feature, Cisco
                              VVB now waits for a response from the agent phone before submitting the blind transfer status to the VXML server. Once the
                              response reaches the VXML server, it can be processed, allowing for appropriate actions by the VXML application. This enhancement
                              guarantees smooth IVR call transitions under agent phone or unavailable scenarios, greatly improving the overall customer
                              experience.

For more information, see Command Line Interface chapter in Operations Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html .

### CallServer Heartbeat Enhancement

The CVP CallServer Heartbeat enhancement ensures SIP server entries remain in the UnreachableDestinationTable until a successful
                              heartbeat response is received, improving reliability and performance during peak traffic periods.

For more information, see the Administration Guide and Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

## Important Notes

### Cisco VVB Services Port Update

The web application ports for VVB Administration, VVB Uccxservice, VVB Speech Server configuration, and VVB Admin API have
                              been updated from TCP port 8443 to TCP port 8445. Ensure to update all related configurations, such as firewall rules, application
                              URLs, and network policies, to ensure uninterrupted access to these services. Additionally, configure port 443 to redirect
                              users to the new port 8445 as needed.

For more information, see the Port Utilization in Cisco VVB chapter of the Port Utilization Guide for Cisco Unified Contact Center Solutions .

### SRTP Compatibility and Encryption

Cisco VVB now supports SRTP negotiation using either the AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80 cryptographic
                              suites, ensuring seamless compatibility and secure encryption of media streams. When both options are present in a request,
                              the SRTP negotiation configured in the system takes precedence.

For more information, see the Cisco Virtualized Voice Browser Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-and-configuration-guides-list.html .

## Deprecated Features

Deprecated features are fully supported. However, there is no additional development for deprecated features. These features
                              may be scheduled to be removed in a future release. Plan to transition to the designated replacement feature. If you are implementing
                              a new deployment, use the replacement technology rather than the deprecated feature.

Deprecated Feature

Announced

Replacement

Notes

Virtual Agent - Voice (VAV) over Premise-based Connector (Dialogflow CX)

15.0(1)

VAV over Cloud-based Connector

VAV over Premise based Connector, which utilizes Google's Dialogflow CX service leveraging DialogflowCX element in the Unified Call Studio is now deprecated.

VAV over Premise-based Connector (Dialogflow ES)

15.0(1)

VAV over Cloud-based Connector

The Dialogflow ES integration, which is supported through the Cisco OAMP UI and powered by a service account, is now deprecated.

Custom code hosting on the VXML server application folder will soon be deprecated.

15.0(1)

You must switch to remote server hosting.

For more information, see the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1) .

## Removed and Unsupported Features

The features listed in the following table are no longer available.

VMXL Gateway

Cisco VVB

App Monitoring for VVB-Admin JVM App Agent

12.6(2)

None

## Third Party Software Impacts

For the list of third-party software, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.

| Deprecated Feature | Announced | Replacement | Notes |
|---|---|---|---|
| Virtual Agent - Voice (VAV) over Premise-based Connector (Dialogflow CX) | 15.0(1) | VAV over Cloud-based Connector | VAV over Premise based Connector, which utilizes Google's Dialogflow CX service leveraging DialogflowCX element in the Unified Call Studio is now deprecated. |
| VAV over Premise-based Connector (Dialogflow ES) | 15.0(1) | VAV over Cloud-based Connector | The Dialogflow ES integration, which is supported through the Cisco OAMP UI and powered by a service account, is now deprecated. |
| Custom code hosting on the VXML server application folder will soon be deprecated. | 15.0(1) | You must switch to remote server hosting. | For more information, see the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1) . |

| Feature | Effective from Release | Replacement |
|---|---|---|
| VMXL Gateway | 15.0(1) | Cisco VVB |
| App Monitoring for VVB-Admin JVM App Agent | 12.6(2) | None |