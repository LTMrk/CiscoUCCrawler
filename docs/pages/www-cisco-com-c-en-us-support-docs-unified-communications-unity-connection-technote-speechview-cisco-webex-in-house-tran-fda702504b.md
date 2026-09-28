---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-technote-speechview-cisco-webex-in-house-tran-fda702504b
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/Technote-SpeechView-Cisco-Webex-in-house-transcription-service-for-Unity-Connection.html
retrieved_at: 2026-08-16T18:51:35.458838+00:00
---

SpeechView Cisco Webex in-house transcription service for Unity Connection

# SpeechView Cisco Webex in-house transcription service for Unity Connection

### Download Options

Updated: September 5, 2024

Document ID: 1725545925901123

SpeechView Cisco Webex in-house transcription service for Unity Connection

# Contents

Introduction

Abbreviations

Prerequisites

Requirements

Components Used

Background Information

SpeechView Operation

Data Flow Diagram

Configure

Unity Connection Configuration

Verify

Troubleshoot

# Introduction

This document walks through the configuration of Unity Connection Release 14 SU4 or later in order to enable SpeechView voicemail transcription in a Cisco Unity Connection. While the screenshots are sourced from specific versions of Unity Connection, the concepts should apply to any later version of the product.

# Abbreviations

· CUC – Cisco Unity Connection

· CCUC – Cloud Connected Unified Collaboration

· CSSM – Cisco Smart Software Manager

# Prerequisites

## Requirements

Cisco recommends that you have knowledge of these topics:

· Unity Connection.

· Webex Cloud-Connected UC. For details, refer Webex Cloud-Connected UC Overview.

## Components Used

The information in this document is based on these software versions:

• Unity Connection Release 14 SU4 or later.

The information in this document was created from the devices in a specific lab environment. All the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

# Background Information

The third-party service supporting the Cisco Unity Connection SpeechView transcription service will reach end of life on or after December 30, 2024. As a result, Cisco migrated Cisco Unity Connection SpeechView transcription service from the third-party vendor to Cisco Webex in-house transcription service.

Cisco Webex offers in-house transcription to power closed captions and transcription in English, French, German, Spanish, and Italian (September 2024). Cisco Webex in-house transcription is a Cisco-built machine learning model that leverages automatic speech recognition to provide closed captions and transcription features. In-house transcription takes speech audio input; performs feature extraction; decodes with the use of acoustic, language, and other models; and produces the text output. The model is trained with unique Cisco data sets that are curated for diverse demographics and further fine-tuned for specific feature use with Cisco Webex Meetings, Cisco Webex Contact Center, Cisco Webex Calling, Cisco devices, and Vidcast. Bringing transcription services in-house will enable Cisco to offer best-in-class technology, utilizing the latest models to transcribe voice messages across multiple languages and dialects .

# SpeechView Operation

This process outlines the general message flow for a SpeechView operation. The steps to this configuration are in these sections.

1. Unity Connection sends the voicemail message to Cisco Webex in-house transcription service for transcription.

2. Cisco Webex in-house transcription service processes the audio and converts it into text.

3. Once transcription is complete, the transcribed text is sent back to the Unity Connection through Cisco Webex Cloud-Connected UC.

4. When Unity Connection receives the response, it takes the transcription and sends it to whatever notification device(s) are defined for the user who received the voicemail.

## Data Flow Diagram

Data flow diagram for SpeechView is shown in figure 1 below.

Figure 1 . Data flow diagram

# Configure

## Unity Connection Configuration

1. Configure Disaster Recovery System (DRS) at Unity Connection Cluster. For more information, refer

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/install_upgrade/guide/b_14cuciumg/b_14cuciumg_chapter_01.html#concept_965CA33CF88F4142B98784BC55C42B0D .

2. Onboard Unity Connection Server/Cluster to Cisco Webex Cloud-Connected UC. For more information, refer Set up Webex Cloud-Connected UC for on-premises devices .

Network Requirements for Webex Cloud-Connected UC: https://help.webex.com/en-us/article/fg3qim/Network-Requirements-for-Webex-Cloud-Connected-UC .

Ensure that the status of Telemetry Module is Online .

3. Enable “ SpeechView Voicemail Transcript ” on the Service Management Page of Cisco Webex Cloud-Connected UC. For more information, refer Enable or Disable Webex Cloud-Connected UC Services in Control Hub .

4. Register Unity Connection with Cisco Smart Software Manager (CSSM) or Cisco Smart Software Manager satellite and ensure that you have acquired proper licenses, SpeechView from Cisco to use this feature. For more information, refer Managing Licenses .

5. Once the above steps are completed, navigate to SpeechView Transcription Services page on Unity Connection and verify that SpeechView Status is Enabled . If you are registering the license for the first time or if the Unity Connection SpeechView license needs to be updated, click on the Sync license status button to get the latest compliance state for SpeechView.

Transcription services can be accessed by Unity Connection server directly or through proxy location.

· If this server is going to access transcription services directly, do the given steps:

o Select Access Transcription Service Directly field.

o If you want this server to offer transcription proxy services to other Unity Connection locations in a digital network, check the Advertise Transcription Proxy Services to Other Unity Connection Locations check box.

· If this server accesses the transcription services through another digitally networked Unity Connection location, select the Access Transcription Services through Unity Connection Proxy Location field. Select the name of the Unity Connection location from the list.

Select Save and then Sync License Status .

6. Assign users to a class of service that provides SpeechView transcription of voice messages.

For more information on configuring SpeechView, refer SpeechView Cisco Webex in-house transcription service chapter of System Administration Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html

Verify

To verify the SpeechView Configuration, navigate to SpeechView Transcription Services page and click on “ Test” button.

The Test performs the following actions and shows the results with recommendation(s) for failure cases if any:

· Checks the status of Connection SpeechView Processor service.

· Checks if the SpeechView license is in compliance with the configuration.

· Checks if Cisco Unity Connection server is onboarded and SpeechView Voicemail Transcript is enabled on Cisco Webex Cloud-Connected UC.

· Checks if communication with Cisco Webex Cloud-Connected UC is persistent.

· Checks if Cisco Webex in-house transcription is healthy. This ensures that Webex in-house transcription service domain is in allowlist.

· Sends a test transcription request to Webex in-house transcription service and looks for a response. This ensures that the transcription request is routed correctly, the service is reachable and that a response is received.

# Troubleshoot

For information related to Troubleshooting SpeechView with Cisco Webex in-house transcription service, refer Troubleshooting SpeechView (Cisco Webex in-house transcription service) chapter of Troubleshooting Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg.html.

### Revision History

1.0

05-Sep-2024

Initial Release

### This Document Applies to These Products

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Sep-2024 | Initial Release |