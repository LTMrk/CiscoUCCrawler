---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-maintenance-guide-pcce-b-featur-a3b820739c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/maintenance/guide/pcce_b_features_guide_12_5/pcce_b_pcce_features_guide_12_5_chapter_010100.html
retrieved_at: 2026-08-21T04:47:43.084057+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.5(1)

Updated: July 29, 2021

Chapter: Customer Virtual Assistant

## Chapter: Customer Virtual Assistant

# Customer Virtual Assistant

## Feature Overview

Customer Virtual Assistant (CVA) feature enables the IVR platform to integrate with cloud-based speech services. This feature
                           supports human-like interactions that enable customers to resolve issues quickly and more efficiently within the IVR, thereby,
                           reducing the calls directed towards agents.

In a traditional IVR, customers can interact with the IVR in the following ways:

VVB Media Services-Based Interaction : Prompts are played locally by VVB by downloading
                                 					WAV files. User inputs are captured using DTMF grammar.

ASR-Based and TTS-Based Interactions : Prompts are played by the external media server over MRCP Synthesis command for Text-to-Speech (TTS) functionality. The
                                 responses are recognized by external media server based on predefined grammar provided by Asynchronous Speech Recognition
                                 (ASR).

CVA -based IVR enables a new mechanism to leverage cloud-based-AI-enabled speech services. CVA provides the following speech services:

Text-to-Speech : Integration with cloud-based TTS services in your application for Speech Synthesis operations. CVA currently supports Google Text to Speech service.

Speech-to-Text : Integration with cloud-based ASR services in your application for Speech Recognition operations. CVA currently supports Google Speech to Text service.

Speech-to-Intent : CVA provides capability of identifying the intent of customer utterances by processing the text received from Speech-to-Text
                                 operations. CVA offers this service by using cloud-based Natural Language Understanding (NLU) services. CVA currently supports Google Dialogflow service.

You can configure the Customer Virtual Assistant (CVA) feature of VVB 12.5(1) keeping the Unified CCE Controller in 12.0 version (as in multi-stage upgrade). However, in this case,
                                             the configuration user interface for CVA service account will not be available in the Unified CCE Administration. So, System Administrators can use the Command Execution Pane for such configurations.

For more information, see the Command Execution Pane section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

## Getting Started

This section explains the prerequisites and the documentation resources for CVA .

### Prerequisites

Ensure that the VVB components have access to Google services to use the Virtual Agent-Voice for Dialogflow ES via VVB (non
                                          OEM users).

CVP 12.5(1) and VVB 12.5(1).

CVP/VVB configuration:

The allowed list of your customer's network must include the following group of URLs:

accounts.google.com/o/oauth2

*.cloud.google.com/dialogflow

*.google.com

*.googleapis.com

*.gcr.io

Enable access to cloud-based services from CVP and VVB directly or via proxy. For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                             for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Synchronize the date/time in CVP, VVB, and proxy with a common NTP server.

Configure access to DNS server in CVP/VVB.

For more information on NTP and DNS server configurations in CVP, refer to the Microsoft Windows platform documentation.

For more information on NTP and DNS server configurations in VVB, refer to the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Non-OEM users must enable speech services and generate JSON key. To know more about enabling speech services, see Enable Speech Services (For Non-OEM Users) . To know more about generating JSON key, see Generate JSON Key (for Non-OEM Users) .

OEM users must provision Google Contact Center AI (CCAI) for Cisco Contact Center Enterprise. To know more about provisioning
                                    Google CCAI, see Provision Google CCAI with Unified Contact Center Enterprise (for OEM Users) .

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

### Provision Google CCAI with Unified Contact Center Enterprise (for OEM Users)

To provision Google CCAI with Cisco Unified Contact Center Enterprise, follow these
                                 steps:

Step 1

Log in to the Cisco Commerce Workspace (CCW) portal https://apps.cisco.com/Commerce/ using your Cisco ID and place the order for Google CCAI.

Step 2

Complete the CCAI provisioning form and submit to get a CCAI account with Cisco.

When the CCAI provisioning request is approved, an email ( CCAI Onboarding Provision Status Update ) is triggered to the user. This email includes the account details and the CCAI Provisioning Document which explains the steps to configure the CCAI account and services.

Step 3

Configure the CCAI account and integrate the CCAI services with the Contact Center application by following the CCAI Provisioning Document . For any further assistance, contact the Cisco CCAI onboarding team or send an email to: cisco-ccai-onboarding@cisco.com .

The service account provided
                                 by Cisco allows the CCAI customers to leverage the following APIs to integrate with the
                                 Contact Center applications:

Dialogflow API

Text-to-Speech API

Speech-to-Text API

### Documentation Resources

The following table lists the reference documents for CVA .

Information

Resource

Sample CVA Application

See https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant .

Design Considerations

Design Considerations for Integrated Features > Customer Virtual Assistant Considerations section in Solution Design Guide

CVA configuration in PCCE Deployment

Customer Virtual Assistant section in PCCE Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

TTS Prompt Cache Management and proxy setting for Speech Server

VVB Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html .

Proxy settings for VXML Server

See the VXML Server Configuration > Proxy Settings in VXML Server for Customer Virtual Assistant section in CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configuration of Call Studio elements for CVA

The following chapters in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html :

Dialogflow Element

DialogflowIntent Element

DialogflowParam Element

Transcribe Element

CVA Speech Configuration APIs

See CVA Speech Configuration section in VVB Developer Guide at https://developer.cisco.com/site/customer-voice-portal/documents/virtual-voice-browser/ .

## Feature Overview

Customer Virtual Assistant (CVA) feature enables the IVR platform to integrate with cloud-based speech services. This feature
                           supports human-like interactions that enable customers to resolve issues quickly and more efficiently within the IVR, thereby,
                           reducing the calls directed towards agents.

In a traditional IVR, customers can interact with the IVR in the following ways:

VVB Media Services-Based Interaction : Prompts are played locally by VVB by downloading
                                 					WAV files. User inputs are captured using DTMF grammar.

ASR-Based and TTS-Based Interactions : Prompts are played by the external media server over MRCP Synthesis command for Text-to-Speech (TTS) functionality. The
                                 responses are recognized by external media server based on predefined grammar provided by Asynchronous Speech Recognition
                                 (ASR).

CVA -based IVR enables a new mechanism to leverage cloud-based-AI-enabled speech services. CVA provides the following speech services:

Text-to-Speech : Integration with cloud-based TTS services in your application for Speech Synthesis operations. CVA currently supports Google Text to Speech service.

Speech-to-Text : Integration with cloud-based ASR services in your application for Speech Recognition operations. CVA currently supports Google Speech to Text service.

Speech-to-Intent : CVA provides capability of identifying the intent of customer utterances by processing the text received from Speech-to-Text
                                 operations. CVA offers this service by using cloud-based Natural Language Understanding (NLU) services. CVA currently supports Google Dialogflow service.

You can configure the Customer Virtual Assistant (CVA) feature of VVB 12.5(1) keeping the Unified CCE Controller in 12.0 version (as in multi-stage upgrade). However, in this case,
                                             the configuration user interface for CVA service account will not be available in the Unified CCE Administration. So, System Administrators can use the Command Execution Pane for such configurations.

For more information, see the Command Execution Pane section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

## Getting Started

This section explains the prerequisites and the documentation resources for CVA .

### Prerequisites

Ensure that the VVB components have access to Google services to use the Virtual Agent-Voice for Dialogflow ES via VVB (non
                                          OEM users).

CVP 12.5(1) and VVB 12.5(1).

CVP/VVB configuration:

The allowed list of your customer's network must include the following group of URLs:

accounts.google.com/o/oauth2

*.cloud.google.com/dialogflow

*.google.com

*.googleapis.com

*.gcr.io

Enable access to cloud-based services from CVP and VVB directly or via proxy. For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                             for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Synchronize the date/time in CVP, VVB, and proxy with a common NTP server.

Configure access to DNS server in CVP/VVB.

For more information on NTP and DNS server configurations in CVP, refer to the Microsoft Windows platform documentation.

For more information on NTP and DNS server configurations in VVB, refer to the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Non-OEM users must enable speech services and generate JSON key. To know more about enabling speech services, see Enable Speech Services (For Non-OEM Users) . To know more about generating JSON key, see Generate JSON Key (for Non-OEM Users) .

OEM users must provision Google Contact Center AI (CCAI) for Cisco Contact Center Enterprise. To know more about provisioning
                                    Google CCAI, see Provision Google CCAI with Unified Contact Center Enterprise (for OEM Users) .

### Documentation Resources

The following table lists the reference documents for CVA .

Information

Resource

Sample CVA Application

See https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant .

Design Considerations

Design Considerations for Integrated Features > Customer Virtual Assistant Considerations section in Solution Design Guide

CVA configuration in PCCE Deployment

Customer Virtual Assistant section in PCCE Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

TTS Prompt Cache Management and proxy setting for Speech Server

VVB Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html .

Proxy settings for VXML Server

See the VXML Server Configuration > Proxy Settings in VXML Server for Customer Virtual Assistant section in CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configuration of Call Studio elements for CVA

The following chapters in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html :

Dialogflow Element

DialogflowIntent Element

DialogflowParam Element

Transcribe Element

CVA Speech Configuration APIs

See CVA Speech Configuration section in VVB Developer Guide at https://developer.cisco.com/site/customer-voice-portal/documents/virtual-voice-browser/ .

| Note | The Dialogflow ES GCP project trial version should not be used in a production environment. |
|---|---|

| Note | You can configure the Customer Virtual Assistant (CVA) feature of VVB 12.5(1) keeping the Unified CCE Controller in 12.0 version (as in multi-stage upgrade). However, in this case,
                                             the configuration user interface for CVA service account will not be available in the Unified CCE Administration. So, System Administrators can use the Command Execution Pane for such configurations. For more information, see the Command Execution Pane section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|

| Note | Ensure that the VVB components have access to Google services to use the Virtual Agent-Voice for Dialogflow ES via VVB (non
                                          OEM users). |
|---|---|

| Note | Trial version of Dialogflow ES GCP project should not be used in production environment. |
|---|---|

| Step 1 | Log in to the Cisco Commerce Workspace (CCW) portal https://apps.cisco.com/Commerce/ using your Cisco ID and place the order for Google CCAI. |
|---|---|
| Step 2 | Complete the CCAI provisioning form and submit to get a CCAI account with Cisco. Note When the CCAI provisioning request is approved, an email ( CCAI Onboarding Provision Status Update ) is triggered to the user. This email includes the account details and the CCAI Provisioning Document which explains the steps to configure the CCAI account and services. | Note | When the CCAI provisioning request is approved, an email ( CCAI Onboarding Provision Status Update ) is triggered to the user. This email includes the account details and the CCAI Provisioning Document which explains the steps to configure the CCAI account and services. |
| Note | When the CCAI provisioning request is approved, an email ( CCAI Onboarding Provision Status Update ) is triggered to the user. This email includes the account details and the CCAI Provisioning Document which explains the steps to configure the CCAI account and services. |
| Step 3 | Configure the CCAI account and integrate the CCAI services with the Contact Center application by following the CCAI Provisioning Document . For any further assistance, contact the Cisco CCAI onboarding team or send an email to: cisco-ccai-onboarding@cisco.com . |

| Note | When the CCAI provisioning request is approved, an email ( CCAI Onboarding Provision Status Update ) is triggered to the user. This email includes the account details and the CCAI Provisioning Document which explains the steps to configure the CCAI account and services. |
|---|---|

| Information | Resource |
|---|---|
| Sample CVA Application | See https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant . |
| Design Considerations | Design Considerations for Integrated Features > Customer Virtual Assistant Considerations section in Solution Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . |
| CVA configuration in PCCE Deployment | Customer Virtual Assistant section in PCCE Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
| TTS Prompt Cache Management and proxy setting for Speech Server | VVB Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html . |
| Proxy settings for VXML Server | See the VXML Server Configuration > Proxy Settings in VXML Server for Customer Virtual Assistant section in CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Configuration of Call Studio elements for CVA | The following chapters in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html : Dialogflow Element DialogflowIntent Element DialogflowParam Element Transcribe Element |
| CVA Speech Configuration APIs | See CVA Speech Configuration section in VVB Developer Guide at https://developer.cisco.com/site/customer-voice-portal/documents/virtual-voice-browser/ . |

| Note | The Dialogflow ES GCP project trial version should not be used in a production environment. |
|---|---|

| Note | You can configure the Customer Virtual Assistant (CVA) feature of VVB 12.5(1) keeping the Unified CCE Controller in 12.0 version (as in multi-stage upgrade). However, in this case,
                                             the configuration user interface for CVA service account will not be available in the Unified CCE Administration. So, System Administrators can use the Command Execution Pane for such configurations. For more information, see the Command Execution Pane section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|

| Note | Ensure that the VVB components have access to Google services to use the Virtual Agent-Voice for Dialogflow ES via VVB (non
                                          OEM users). |
|---|---|

| Note | Trial version of Dialogflow ES GCP project should not be used in production environment. |
|---|---|

| Information | Resource |
|---|---|
| Sample CVA Application | See https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant . |
| Design Considerations | Design Considerations for Integrated Features > Customer Virtual Assistant Considerations section in Solution Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . |
| CVA configuration in PCCE Deployment | Customer Virtual Assistant section in PCCE Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
| TTS Prompt Cache Management and proxy setting for Speech Server | VVB Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html . |
| Proxy settings for VXML Server | See the VXML Server Configuration > Proxy Settings in VXML Server for Customer Virtual Assistant section in CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Configuration of Call Studio elements for CVA | The following chapters in CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html : Dialogflow Element DialogflowIntent Element DialogflowParam Element Transcribe Element |
| CVA Speech Configuration APIs | See CVA Speech Configuration section in VVB Developer Guide at https://developer.cisco.com/site/customer-voice-portal/documents/virtual-voice-browser/ . |