---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-maintenance-guide-pcce-b-featur-818c5ad106
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/maintenance/guide/pcce_b_features-guide-1262/ucce_m_virtual_agent_voice-nuancemix-1262.html
retrieved_at: 2026-08-21T12:29:22.144062+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: November 15, 2024

Chapter: Virtual Agent-Voice (VAV) for Nuance-based Connector

## Chapter: Virtual Agent-Voice (VAV) for Nuance-based Connector

# Virtual Agent-Voice (VAV) for Nuance-based Connector

## Overview

Virtual Agent–Voice (VAV) feature, earlier referred to as Customer Virtual Assistant (CVA) in 12.5(1) release, enables the
                           IVR platform to integrate with cloud-based speech services. This feature supports human-like interactions that enable customers
                           to resolve issues quickly and more efficiently within the IVR, thereby reducing the calls directed toward agents.

VAV-based IVR enables a new mechanism to leverage cloud-based-AI-enabled speech services. VAV provides the following speech
                           services:

Text-to-Speech : Integration with cloud-based TTS services in your application for Speech Synthesis operations.

Speech-to-Text : Integration with cloud-based ASR services in your application for Speech Recognition operations.

Speech-to-Intent : VAV provides capability of identifying the intent of customer utterances by processing the text that is received from Speech-to-Text
                                 operations. VAV offers this service by using cloud-based Natural Language Understanding (NLU) services.

## Onboarding Experience

From 12.6(2) onwards, you can enable your customer applications with AI capabilities offered by Nuance cloud-based connector.
                           The conversational IVR experience is implemented as Nuance Mix DLGaaS (Dialog As A Service).

Automatic Speech Recognition (ASR) and Text-to-Speech (TTS) are not supported.

The following table lists the support for the Nuance cloud-based connector for OEM and non-OEM customers:

VAV using Nuance Mix (OEM)

VAV using Nuance Mix (Non-OEM)

## Important Considerations

Consider the following before configuring VAV using the Nuance cloud-based connector:

The Nuance cloud-based connector feature is available with Cisco subscription services only.

Voice input : You can enable or disable the prompt bargein attribute.

DTMF input : You can enable or disable the prompt bargein. The DTMF input is collected on the client side based on the recognition configuration
                                 settings and then pushed to Nuance Mix, so you must ensure that DTMF recognition setting fields such as inter_digit_timeout and term_char are configured in the Nuance Mix application when the term char is pressed or the timer is hit. For information about enabling
                                 DTMF input, see https://docs.nuance.com/mix/apis/dialog-grpc/v1/nuance-dlg-service/#nuance.dlg.v1.common.RecognitionSettings.DtmfSettings .

Input modes : Nuance doesn't support setting input modes in Nuance Mix Dialog as a service. So, ensure that you always use Voice + DTMF
                                 as the input mode for all the dialogs.

Start of call : At the beginning of the call, the start node of the Nuance application is the only entry point to the Nuance Mix application.

Custom event : Reentry using a custom event name to a different node via Dialog event is supported in Nuance Mix. For more information,
                                 see https://docs.nuance.com/mix/tools/mix-dialog/manage-resources/manage-events/ .

Custom data : You can pass data from the client application to Nuance Mix using variables. For more information, see https://docs.nuance.com/mix/integration/ndep/exchange-data/#specify-custom-engagement-data-to-pass-to-the-dialog-service-at-the-start-of-a-session .

SIP Header : You can pass all the configured SIP headers to Nuance Mix. But, since Nuance Mix doesn't allow the use of special characters
                                 for variable names other than "_", we only support the use of " Simple SIP Headers " in the Nuance Mix application.

To use these SIP headers, create Variables in Nuance Mix with the name sipHeader_<Header Name>. For example, if you want to access the "From" header, your variable name should be "sipHeader_From".

Agent transfer : VAV doesn't support Nuance Mix agent routing. When the agent transfer response is received from Nuance Mix, the control
                                 is transferred to the Cisco platform for internal agent routing. To close the Session properly with Nuance Mix after Agent
                                 Transfer, we recommend that you add an External Action Node with the action type set as " End " in both success and failure scenarios. This ensures that the session is closed successfully after every agent transfer.

## Prerequisites

To configure VAV using the Nuance-based cloud connector, check the following:

You've installed Cisco Virtualized Voice Browser 12.6(2) ES04 or above.

You’ve installed the latest ES version of Cisco Unified Customer Voice Portal VXML Server and Call Studio.

Ensure that port 443 isn't blocked by the firewall.

The allowed list in your customer's network include the following URLs:

*.api.nuance.com

*.api.nuance.ca

*.api.nuance.eu

*.api.nuance.net.au

*.cisco.com.

*.wbx2.com

*.ciscoccservice.com

*.rtmsprod.net

You have built and deployed the Nuance Mix application at the customer's end and have selected the "IVR Channel" option to
                                 create the application.

## Configuration Task Flow

Here's the task flow for configuring the Nuance cloud-based connector.

Step 1

Create a Nuance Mix application, and get the client ID and client secret. For sample application, see the Nuance Mix documentation.

Step 2

Configure the Nuance cloud-based connector via Control Hub. For details, see https://help.webex.com/en-us/article/preview/euwer2/Configure-Nuance-Connector .

Step 3

Configure the Nuance Mix feature in Control Hub and get the Config ID. For details, see https://help.webex.com/en-us/article/preview/npbt02j/Create-a-Contact-Center-AI-configuration .

Step 4

Use the Config ID in the VirtualAgentVoice element in CVP Call Studio. For details, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_m_1261-vav-element.html .

You can use the existing VirtualAgentVoice element in Call Studio for connecting to the Nuance cloud-based connector.

## Features

### Hybrid IVR

VAV supports the exit and reentry into the Nuance Mix application, also known as the client-side fetch in Nuance. To configure
                              client-side fetch in Nuance Mix, see https://docs.nuance.com/mix/tasks/data-access/data_access_client_app/ .

During reentry, the application developer must add the returnCode = 0 in the Event data of the VAV element. This is a mandatory
                              field in the requested data and as an application developer, you must ensure it is propagated. A return code 0 indicates success,
                              and any other value indicates failure.

We recommend that you don't use the event name that comes from the Nuance Mix application during hybrid exit. When no event
                                          name is provided, the reentry happens through the same node from which it exited the Nuance Mix application.

### Partial Response

The partial response feature is supported via cloud-based connector. It notifies the caller that their request is being processed.
                              By default, the partial prompt will stop playing when the final response is received from the webhook.

You can perform support partial response handling, referred to as "server-side fetch" in Nuance. After receiving the partial
                              response from Nuance, wait for 30 secs to receive the final response. If no response is received within 30 seconds, then the
                              connection with Nuance is closed and an exception error is thrown. For more information, see https://docs.nuance.com/mix/tasks/data-access/web/data_access_web_service/ .

The default session timeout in Nuance Mix is 15 mins. For more information, see https://docs.nuance.com/mix/apis/dialog-grpc/dlg-essentials/#session .

## Documentation Resources

The following table lists the reference documents for implementing VAV using the Nuance cloud-based connector.

Information

Resource

Sample VAV application

https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant .

Design Considerations

Design Considerations for Integrated Features > Virtual Agent–Voice Considerations section in Solution Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

VAV configuration in Packaged CCE Deployment

Virtual Agent–Voice section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Proxy settings for VXML Server

VXML Server Configuration > Proxy Settings in VXML Server for Virtual Agent–Voice section in CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configuration of Call Studio elements for VAV

VirtualAgentVoice chapter in the CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

| Note | Automatic Speech Recognition (ASR) and Text-to-Speech (TTS) are not supported. |
|---|---|

| Connector type | VAV using Nuance Mix (OEM) | VAV using Nuance Mix (Non-OEM) |
|---|---|---|
| Cloud-based connector | Yes (12.6(2) and above) | No |
| Premise-based connector | No | No |

| Note | Custom event names to start from a different point in the application at the beginning of the call isn't supported in Nuance
                                          Mix. For more information, see https://docs.nuance.com/mix/tools/mix-dialog/build-dialog-flows/nod-start-enter/ . |
|---|---|

| Step 1 | Create a Nuance Mix application, and get the client ID and client secret. For sample application, see the Nuance Mix documentation. |
|---|---|
| Step 2 | Configure the Nuance cloud-based connector via Control Hub. For details, see https://help.webex.com/en-us/article/preview/euwer2/Configure-Nuance-Connector . |
| Step 3 | Configure the Nuance Mix feature in Control Hub and get the Config ID. For details, see https://help.webex.com/en-us/article/preview/npbt02j/Create-a-Contact-Center-AI-configuration . |
| Step 4 | Use the Config ID in the VirtualAgentVoice element in CVP Call Studio. For details, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_m_1261-vav-element.html . Note You can use the existing VirtualAgentVoice element in Call Studio for connecting to the Nuance cloud-based connector. | Note | You can use the existing VirtualAgentVoice element in Call Studio for connecting to the Nuance cloud-based connector. |
| Note | You can use the existing VirtualAgentVoice element in Call Studio for connecting to the Nuance cloud-based connector. |

| Note | You can use the existing VirtualAgentVoice element in Call Studio for connecting to the Nuance cloud-based connector. |
|---|---|

| Note | We recommend that you don't use the event name that comes from the Nuance Mix application during hybrid exit. When no event
                                          name is provided, the reentry happens through the same node from which it exited the Nuance Mix application. |
|---|---|

| Note | The default session timeout in Nuance Mix is 15 mins. For more information, see https://docs.nuance.com/mix/apis/dialog-grpc/dlg-essentials/#session . |
|---|---|

| Information | Resource |
|---|---|
| Sample VAV application | https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant . |
| Design Considerations | Design Considerations for Integrated Features > Virtual Agent–Voice Considerations section in Solution Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . |
| VAV configuration in Packaged CCE Deployment | Virtual Agent–Voice section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
| Proxy settings for VXML Server | VXML Server Configuration > Proxy Settings in VXML Server for Virtual Agent–Voice section in CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Configuration of Call Studio elements for VAV | VirtualAgentVoice chapter in the CVP Element Specification Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html . |