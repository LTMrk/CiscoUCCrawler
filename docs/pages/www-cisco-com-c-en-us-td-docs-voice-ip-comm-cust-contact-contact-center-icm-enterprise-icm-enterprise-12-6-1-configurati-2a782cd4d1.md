---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-2a782cd4d1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/ucce_b_features-guide-1261/ucce_m_customer_virtual_assistant-1261.html
retrieved_at: 2026-08-16T20:12:54.922897+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Virtual Agent–Voice

## Chapter: Virtual Agent–Voice

# Virtual Agent–Voice

## Feature Overview

Virtual Agent–Voice (VAV) feature, which was referred to as Customer Virtual Assistant (CVA) in 12.5(1) release, enables the
                           IVR platform to integrate with cloud-based speech services. This feature supports human-like interactions that enable customers
                           to resolve issues quickly and more efficiently within the IVR, thereby, reducing the calls directed towards agents.

In a traditional IVR, customers can interact with the IVR in the following ways:

VVB Media Services-Based Interaction : Prompts are played locally by VVB by downloading
                                 					WAV files. User inputs are captured using DTMF grammar.

ASR-Based and TTS-Based Interactions : Prompts are played by the external media server over MRCP Synthesis command for Text-to-Speech (TTS) functionality. The
                                 responses are recognized by external media server based on predefined grammar provided by Asynchronous Speech Recognition
                                 (ASR).

VAV -based IVR enables a new mechanism to leverage cloud-based-AI-enabled speech services. VAV provides the following speech services:

Text-to-Speech : Integration with cloud-based TTS services in your application for Speech Synthesis operations. VAV currently supports Google Text to Speech service.

Speech-to-Text : Integration with cloud-based ASR services in your application for Speech Recognition operations. VAV currently supports Google Speech to Text service.

Speech-to-Intent : VAV provides capability of identifying the intent of customer utterances by processing the text received from Speech-to-Text
                                 operations. VAV offers this service by using cloud-based Natural Language Understanding (NLU) services. VAV currently supports Google Dialogflow service.

## Onboarding Experience

In 12.6(1) release, the VAV feature provides different onboarding experience for OEM users (who use Cisco's contract, billing,
                              and support for Google's speech services) via Webex Control Hub. For details, see the Create a Contact Center AI configuration article. Non-OEM users use NOAMP in Unified CCE solution and CCE Administration Portal in Packaged CCE solution for onboarding.

The following table lists the onboarding channel and Google APIs used for OEM and non-OEM customers:

Release

Services Billing

Onboarding

Google APIs

## VAV Onboarding for OEM Users

Virtual Agent–Voice (VAV) feature provides an enhanced onboarding experience to OEM customers via Webex Control Hub. All contract,
                           billing, and support are managed through Cisco for OEM customers and they can use Cisco services coupled with Google’s cloud-based-AI-enabled
                           speech services.

A single config ID generated via Control Hub can be leveraged across all CVP/VVB instances as compared to the earlier experience
                           where each instance was required to be configured individually.

### Prerequisites

The prerequisites for configuring Virtual Agent–Voice for OEM users are:

OEM users must provision Google Contact Center AI (CCAI) for Cisco Contact Center Enterprise. For details, see the Create a Contact Center AI configuration article.

CVP/VVB configuration:

Enable access to cloud-based services from CVP and VVB directly or via proxy.

For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                             for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Synchronize the date/time in CVP, VVB, and proxy with a common NTP server.

Configure access to DNS server in CVP/VVB.

For more information on NTP and DNS server configurations in CVP, refer to the Microsoft Windows platform documentation.

For more information on NTP and DNS server configurations in VVB, refer to the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

The following table lists the required versions for Cisco Unified CVP, Cisco VVB, Cloud Connect, CCE components (Router, Logger,
                                    AW, and PG), and ICM.

CVP

VVB

Cloud Connect

CCE Components

ICM

12.6

12.6

12.6

12.0 and higher

12.0 and higher

### VAV Onboarding for OEM Users Task Flow

Follow this procedure to provision Google CCAI with Cisco Unified Contact Center Enterprise. A single configuration created
                                 via Control Hub can be used for accessing multiple AI services, such as VAV and Agent Answers on multiple devices.

Step 1

Create a CCAI configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services.

While creating a CCAI configuration (explained in the article Create a Contact Center AI configuration ):

Skip the creation of conversation profile.

Select the Apply as default for Virtual Agent configuration, because it is mandatory for ASR and TTS.

Step 2

Ensure that the Cloud Connect publisher and subscriber are installed.

For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Step 3

Import the Cloud Connect certificate to the CVP server.

For details, see the Unified CVP Security > Import Cloud Connect Certificate to Unified CVP Keystore section in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 4

Configure Cloud Connect with CVP in the Operations Console (NOAMP).

Step 5

Configure Cloud Connect with VVBs in the Operations Console (NOAMP).

Step 6

View the default CCAI configuration (created in step 1). If required, synchronize the configuration (using Sync option) in the CVP Operations Console (NOAMP).

For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Cisco-Billed AI Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

To change or override the default config (created in step 1), configure the CCAI.configId property of the Dialogflow element in Call Studio.

For details, see the Dialogflow Element > Custom VoiceXML Properties section in the Element Specifications for Cisco Unified CVP VXML Server and Call Studio at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

### Migration for OEM Users

OEM users migrating from 12.5(1) or 12.5(1a) to 12.6(1) must onboard via Webex Control Hub for better experience and enhanced
                              security. They can continue to use the old method of key generation by retaining their old configurations until their onboarding
                              via Webex Control Hub is complete.

### Important Considerations

VVB periodically refreshes the CCAI configurations. Whenever these configurations are changed in the Control Hub, it may take
                              upto 10 minutes for the changes to reflect in VVB. For applying the changes instantly, you need to restart the VVB speech
                              server service.

## VAV Onboarding for Non-OEM Users

### Prerequisites

Ensure that the VVB components have access to Google services to use the Virtual Agent-Voice for Dialogflow ES via VVB (non
                                          OEM users).

Enable access to cloud-based services from CVP and VVB directly or via proxy. For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                             for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Synchronize the date/time in CVP, VVB, and proxy with a common NTP server.

Configure access to DNS server in CVP/VVB.

For more information on NTP and DNS server configurations in CVP, refer to the Microsoft Windows platform documentation.

For more information on NTP and DNS server configurations in VVB, refer to the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Non-OEM users must enable speech services and generate JSON key. To know more about enabling speech services, see Enable Speech Services (For Non-OEM Users) . To know more about generating JSON key, see Generate JSON Key (for Non-OEM Users) .

The following table lists the required versions for Cisco Unified CVP, Cisco VVB, Cloud Connect, CCE components (Router, Logger,
                                    AW, and PG), and ICM.

CVP

VVB

Cloud Connect

CCE Components

ICM

12.5 and higher

12.5 and higher

NA

12.5 and higher with A2Q approval

12.5 and higher with A2Q approval

### VAV Onboarding for Non-OEM Users Task Flow

Step 1

Enable speech services for your account.

Step 2

Generate JSON key for your account.

Step 3

Configure VVB devices for speech services.

For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Vendor-Billed AI
                                                Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

### Enable Speech Services (For Non-OEM Users)

To enable speech services, follow these steps:

Log in to your Dialogflow account at https://dialogflow.cloud.google.com/ .

Scroll down on the homepage and click Project ID of your Dialogflow agent.

This takes you to the Google Cloud Platform (GCP) homepage.

Select APIs & Services from the left pane (through the hamburger menu).

Select the API services (such as Cloud Text-to-Speech, Cloud Speech-to-Text, and
                                       Dialogflow) to be enabled.

Click Enable to enable the selected API for the given Project ID.

### Generate JSON Key (for Non-OEM Users)

To generate the JSON key, follow these steps:

In the GCP homepage, select IAM & Admin from the
                                       left pane (through the hamburger menu).

Select Service accounts which shows the list of your
                                       enabled services.

Select the service for which the JSON key is to be generated.

Click the ellipsis menu on the right and click +Create
                                          Key .

Select JSON as Key type and then click Create .

The key is downloaded.

For best results:

Migrate your Dialogflow Agent to Enterprise Essential ( Console Left Bar > Migrate from Standard to Enterprise Essential ).

Enable the enhanced Speech Model in Dialogflow console ( Settings > Speech > Enable Enhanced Speech Model and Data Logging ).

If this option is enabled, speech recognition data is shared with Google. For more
                                 information see https://cloud.google.com/speech-to-text/docs/enhanced-models .

## Documentation Resources

The following table lists the reference documents for VAV .

Information

Resource

Sample VAV Application

See https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant .

Design Considerations

Design Considerations for Integrated Features > Virtual Agent–Voice Considerations section in Solution Design Guide

VAV configuration in Unified CCE Deployment

Operations Console (NOAMP) section in CVP Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

TTS Prompt Cache Management and proxy setting for Speech Server

VVB Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html .

Proxy settings for VXML Server

See the VXML Server Configuration > Proxy Settings in VXML Server for Virtual Agent–Voice section in CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configuration of Call Studio elements for VAV

The following chapters in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html :

Dialogflow Element

DialogflowIntent Element

DialogflowParam Element

Transcribe Element

VAV Speech Configuration APIs

See VAV Speech Configuration section in VVB Developer Guide at https://developer.cisco.com/site/customer-voice-portal/documents/virtual-voice-browser/ .

| Note | The Dialogflow ES GCP project trial version should not be used in a production environment. |
|---|---|

| Release | Services Billing | Onboarding | Google APIs |
|---|---|---|---|
| 12.6(1) | Cisco billed (OEM) | Webex Control Hub | AnalyzeContent (V2) |
| 12.6(1) | Vendor billed (non-OEM) | NOAMP/CCEAdmin | DetectIntent (V2) |

| CVP | VVB | Cloud Connect | CCE Components | ICM |
|---|---|---|---|---|
| 12.6 | 12.6 | 12.6 | 12.0 and higher | 12.0 and higher |

| Step 1 | Create a CCAI configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services. For details, see the Create a Contact Center AI configuration article. This default config can be used for accessing multiple AI services on multiple devices. Note While creating a CCAI configuration (explained in the article Create a Contact Center AI configuration ): Skip the creation of conversation profile. Select the Apply as default for Virtual Agent configuration, because it is mandatory for ASR and TTS. | Note | While creating a CCAI configuration (explained in the article Create a Contact Center AI configuration ): Skip the creation of conversation profile. Select the Apply as default for Virtual Agent configuration, because it is mandatory for ASR and TTS. |
|---|---|---|---|
| Note | While creating a CCAI configuration (explained in the article Create a Contact Center AI configuration ): Skip the creation of conversation profile. Select the Apply as default for Virtual Agent configuration, because it is mandatory for ASR and TTS. |
| Step 2 | Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Step 3 | Import the Cloud Connect certificate to the CVP server. For details, see the Unified CVP Security > Import Cloud Connect Certificate to Unified CVP Keystore section in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 4 | Configure Cloud Connect with CVP in the Operations Console (NOAMP). |
| Step 5 | Configure Cloud Connect with VVBs in the Operations Console (NOAMP). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                             for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 6 | View the default CCAI configuration (created in step 1). If required, synchronize the configuration (using Sync option) in the CVP Operations Console (NOAMP). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Cisco-Billed AI Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |

| Note | While creating a CCAI configuration (explained in the article Create a Contact Center AI configuration ): Skip the creation of conversation profile. Select the Apply as default for Virtual Agent configuration, because it is mandatory for ASR and TTS. |
|---|---|

| Note | To change or override the default config (created in step 1), configure the CCAI.configId property of the Dialogflow element in Call Studio. For details, see the Dialogflow Element > Custom VoiceXML Properties section in the Element Specifications for Cisco Unified CVP VXML Server and Call Studio at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html . |
|---|---|

| Note | Ensure that the VVB components have access to Google services to use the Virtual Agent-Voice for Dialogflow ES via VVB (non
                                          OEM users). |
|---|---|

| CVP | VVB | Cloud Connect | CCE Components | ICM |
|---|---|---|---|---|
| 12.5 and higher | 12.5 and higher | NA | 12.5 and higher with A2Q approval | 12.5 and higher with A2Q approval |

| Note | Trial version of Dialogflow ES GCP project should not be used in production environment. |
|---|---|

| Step 1 | Enable speech services for your account. To know more about enabling speech services, see Enable Speech Services (For Non-OEM Users) . |
|---|---|
| Step 2 | Generate JSON key for your account. To know more about generating JSON key, see Generate JSON Key (for Non-OEM Users) . |
| Step 3 | Configure VVB devices for speech services. For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Vendor-Billed AI
                                                Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |

| Information | Resource |
|---|---|
| Sample VAV Application | See https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant . |
| Design Considerations | Design Considerations for Integrated Features > Virtual Agent–Voice Considerations section in Solution Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . |
| VAV configuration in Unified CCE Deployment | Operations Console (NOAMP) section in CVP Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| TTS Prompt Cache Management and proxy setting for Speech Server | VVB Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html . |
| Proxy settings for VXML Server | See the VXML Server Configuration > Proxy Settings in VXML Server for Virtual Agent–Voice section in CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Configuration of Call Studio elements for VAV | The following chapters in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html : Dialogflow Element DialogflowIntent Element DialogflowParam Element Transcribe Element |
| VAV Speech Configuration APIs | See VAV Speech Configuration section in VVB Developer Guide at https://developer.cisco.com/site/customer-voice-portal/documents/virtual-voice-browser/ . |