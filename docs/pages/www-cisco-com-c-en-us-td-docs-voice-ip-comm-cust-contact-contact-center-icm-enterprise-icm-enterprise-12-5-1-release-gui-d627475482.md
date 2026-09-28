---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-release-gui-d627475482
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/release/guide/ucce_b_1251-ucce-release-notes/ucce_b_1251-ucce-release-notes_chapter_01.html
retrieved_at: 2026-08-16T19:40:19.699658+00:00
---

Release Notes for Unified Contact Center Enterprise, Release 12.5(1)

# Release Notes for Unified Contact Center Enterprise, Release 12.5(1)

Updated: January 21, 2020

Chapter: Cisco Unified Customer Voice Portal

## Chapter: Cisco Unified Customer Voice Portal

# Cisco Unified Customer Voice Portal

## New Features

The following features are available in this release:

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge). For information about supported versions, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Customer Virtual Assistant

Customer Virtual Assistant (CVA) enables the IVR Platform to integrate with cloud-based speech services. CVA provides the
                              following speech services:

Text to Speech : Integration with cloud-based TTS services in your application for Speech Synthesis operations. CVA currently supports Google
                                    Text to Speech service.

Speech to Text : Integration with cloud-based ASR services in your application for Speech Recognition operations. CVA currently supports
                                    Google Speech to Text service.

Speech to Intent : CVA provides capability of identifying the intent of customer utterances by processing the text received from Speech to
                                    Text operations. CVA offers this service by using cloud-based Natural Language Understanding (NLU) services CVA currently
                                    supports Google Dialogflow service.

For more information, see Customer Virtual Assistant chapter in Feature Guide for Cisco Unified Contact Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html .

### Smart Licensing

This release introduces Smart Licensing that delivers visibility into your license ownership and consumption. Smart Licensing
                              helps you to procure, deploy, and manage licenses easily and report license consumption. It pools license entitlements in
                              a single account and allows you to move licenses freely through the virtual accounts.

Smart Licensing registers the product instance, reports license usage, and obtains the necessary authorization from Cisco
                              Smart Software Manager or Cisco Smart Software Manager On-Prem.

For more information, see Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

For more information, see Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

### Send DTMF

This feature supports playing a Dual Tone Multi Frequency (DTMF) tone as a prompt in VVB.

For more information, see Developer Guide for Cisco Virtualized Voice Browser at https://developer.cisco.com/site/customer-voice-portal/documents/virtual-voice-browser/ .

### DTMF Tone Overlay

DTMF tone overlay provides the capability to enable injection of DTMF tones (overlay) on the caller stream at random intervals
                                 during the recognition of sensitive data. For more information, see Digits chapter in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

### Voice Activity Detection (VAD)

VAD enables VVB to handle events like start of speech, end of speech, total recording duration to reduce the initial silence
                                 duration based on configuration from Call Studio. It also enables configuring Cisco VVB to various levels of silence sensitivity.

For more information, see Record chapter in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

### Waveform URI

Record utterance uses Waveform URI to enable application developers to collect URI for the recordings done in the ASR systems.
                                 A new parameter recordutterance is introduced in the Form element in Call Studio. When the value of this parameter is set to true , the recordings are done in the ASR systems and the URI of the recording is sent back to VXML server for further use.

For more information, see Form chapter in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

### VVB Media Streaming

VVB now supports continuous streaming of media through HTTP(S) from a streaming URL.

For more information, see Audio chapter in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

## Updated Features

None.

## Important Notes

### Informix Upgrade

The 12.5(1b) base installer is now available for customers, which has support for IBM Informix 14.10 FC8 version for the Unified
                              CVP application. This release is supported on Windows Server 2016 and Windows Server 2019.

For more information, refer to the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

### OpenJDK Java Runtime Environment Update

The 12.5(1b) base installer has OpenJDK JRE as the supporting Java runtime for the Unified CVP application. It is the same as the preceding 12.5(1) installer, except
                              that in the 12.5(1b) base installer, the Java runtime environment is installed on the Unified CVP virtual machines (VMs).

For JRE update post installation of 12.5(1b) , refer to the OpenLogic OpenJDK site ( https://www.openlogic.com/openjdk-downloads ) to download the JREs.

For more information, refer to the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

For more information on JRE minor update, refer to the Java Runtime Environment Minor Update section in the Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

### Certificates Removed on Upgrade

After the successful upgrade to VVB 12.5(1) and CVP 12.5(1), the CAs that are unapproved by Cisco are removed from the platform
                                 trust store. However, you can add them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki .

For information about adding a certificate, see Insert a New Tomcat-trust Certificate section in the CUCM Certificate Management and Change Notification at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-tech-notes-list.html .

### TLS Version Support

This releaae supports only TLS 1.2. For more information, see Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html .

### Cisco VVB 12.5(1) SU

A new Service Update (SU) release is available for Cisco Virtualized Voice Browser 12.5(1). You can perform a fresh installation
                              or upgrade from 12.5(1) version to Cisco VVB 12.5(1) SU on supported virtual machines. For more information, see the ReadMe .

## Deprecated Features

Deprecated features are fully supported. However, there is no additional development for deprecated features. These features
                           may be scheduled to be removed in a future release. Plan to transition to the designated replacement feature. If you are implementing
                           a new deployment, use the replacement technology rather than the deprecated feature.

Deprecated Feature

Announced in Release

Replacement

Notes

Internet Explorer 11

Not applicable 1

Edge Chromium (Microsoft Edge v79 and later)

None.

## Removed and Unsupported Features

TLS 1.0 and TLS 1.1 are not supported in this release. However, these versions have not yet been removed completely in order
                           to prevent backward compatibility breakage.

## Third Party Software Impacts

None.

| Note | For JRE update post installation of 12.5(1b) , refer to the OpenLogic OpenJDK site ( https://www.openlogic.com/openjdk-downloads ) to download the JREs. |
|---|---|

| Deprecated Feature | Announced in Release | Replacement | Notes |
|---|---|---|---|
| Internet Explorer 11 | Not applicable 1 | Edge Chromium (Microsoft Edge v79 and later) | None. |