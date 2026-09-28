---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-ucce-b-1501-a707510cfe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/ucce_b_1501_features-guide/rcct_m_1501_virtual-agent-voice.html
retrieved_at: 2026-08-20T19:10:56.690516+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Virtual Agent–Voice for Google-based Connectors

## Chapter: Virtual Agent–Voice for Google-based Connectors

# Virtual Agent–Voice for Google-based Connectors

## Feature Overview

Virtual Agent–Voice (VAV) feature, which was referred to as Customer Virtual Assistant (CVA) in 12.5(1) release, enables the
                           IVR platform to integrate with cloud-based speech services. This feature supports human-like interactions that enable customers
                           to resolve issues quickly and more efficiently within the IVR, thereby reducing the calls directed toward agents.

VAV-based IVR enables a new mechanism to leverage cloud-based-AI-enabled speech services. VAV provides the following speech
                           services:

Text-to-Speech : Integration with cloud-based TTS services in your application for Speech Synthesis operations. VAV currently supports Google Text to Speech service.

Speech-to-Text : Integration with cloud-based ASR services in your application for Speech Recognition operations. VAV currently supports Google Speech to Text service.

Speech-to-Intent : VAV provides capability of identifying the intent of customer utterances by processing the text that is received from Speech-to-Text
                                 operations. VAV offers this service by using cloud-based Natural Language Understanding (NLU) services. VAV currently supports Google Dialogflow service.

For accessing VAV functionality, Cisco Virtualized Voice Browser (VVB) uses one of the following connectors to leverage AI
                           services:

Cloud-based connector : VVB uses a cloud-based connector to connect to the Cisco CCAI service. This service is enabled through the Virtual Agent Voice element of Cisco Unified Call Studio. VAV currently supports Google's Dialogflow CX service via cloud-based connector.

Premise-based connector : VVB uses a native connector to connect to the Google Dialogflow service. This service is enabled through the Dialogflow or DialogflowCX elements of Cisco Unified Call Studio. VAV currently supports Google's Dialogflow ES and CX services via premise-based connector.

Ensure that the Unified CCE OAMP, VVB, and Cloud Connect Components have access to Webex services to use the Virtual Agent-Voice via cloud-based connector
                                       and premise-based connector.

## Onboarding Experience

From 12.6(1) release, the VAV feature provides different onboarding experience for OEM users (who use Cisco's contract, billing,
                              and support for Google's speech services) via Webex Control Hub. For details, see the Create a Contact Center AI configuration article. Non-OEM users use NOAMP in the Unified CCE solution and CCE Administration Portal in the Packaged CCE solution for
                              onboarding.

The following table lists the onboarding channel and Google APIs used for OEM and non-OEM customers:

Release

Services Billing

Onboarding

Google APIs

The following table lists the support for VAV Dialogflow CX and VAV Dialogflow ES via cloud-based or premise-based connectors
                              for OEM and non-OEM customers:

VAV Dialogflow CX (OEM)

VAV Dialogflow ES (OEM)

VAV Dialogflow CX (Non-OEM)

VAV Dialogflow ES (Non-OEM)

### VAV over Cloud-Based Connector

## Overview

Virtual Agent–Voice via cloud-based connector  leverages Cisco's cloud-based Artificial Intelligence (AI) and Natural Language
                           Understanding (NLU) services for designing virtual voice agents and creating complex IVR call flows.

The Webex Contact Center AI (Webex CCAI) services platform enables integration with speech-based services from different vendors.
                           On the premise side, VVB interfaces with the Orchestrator service and connects to the CCAI service via cloud-based connector.
                           This service is enabled through the VirtualAgentVoice element of Cisco Unified Call Studio.

Webex Contact Center Enterprise leverages Webex Contact Center AI (WCCAI) Cloud Orchestration Platform (Universal Harnes)
                                       for AI services.

For details of the VirtualAgentVoice element, refer to the Element Specifications for Cisco Unified CVP VXML Server and Call Studio guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

The partial response feature is supported via cloud-based connector. It notifies the caller that their request is being processed.
                           By default, the partial prompt will stop playing when the final response is received from the webhook. For more information,
                           see the Configure Partial Response in Dialogflow CX article.

## Important Considerations

Consider the following before configuring VAV via a cloud-based connector:

Supported codec is u-law.

This feature is available with Cisco-Billed and Vendor-Billed (Non-OEM) subscription services.

Google performs the voice activity detection.

If the call gets transferred to a real agent, then the transcript of the voice conversation between the customer and the virtual
                                 voice agent is displayed in the Transcript widget in the Agent Desktop (provided that the Transcript widget is configured on the Agent Desktop).

- Non barge-in prompt is supported only until the control gets transferred to the cloud.

You can use different conversational profiles for VAV and Agent Answers features in a single call or multiple conversation
                                 profiles within VAV calls.

## Prerequisites

To configure VAV via cloud-based connector, you should have completed the following:

The allowed list of your customer's network must include the following group of URLs:

accounts.google.com/o/oauth2

*.cisco.com

*.ciscoservice.com

*.ciscoccservice.com

*.ciscospark.com

*.cloud.google.com/dialogflow

*.google.com

*.googleapis.com

*.gcr.io

*.rtmsprod.net

*.webex.com

*.wbx2.com

The customer's CX Agent ID and GCP Project ID are created. For more information, refer to Google documentation at https://dialogflow.cloud.google.com/cx/projects .

Assessment to Quality (A2Q) process for Contact Center AI (CCAI) is completed and Cisco subscription Flex SKU for CX is procured.

Customer's GCP project ID is mapped with Cisco's GCP partner projects.

Control Hub credentials (For more information, see https://www.webex.com/us/en/solutions/cross-platform/control-hub.html ) and Hybrid Org (For more information, see https://www.webex.com/us/en/solutions/hybrid-work.html ) are generated.

Access the associated location settings for regions at Google at https://cloud.google.com/dialogflow/cx/docs/concept/region

Add non-proxy hosts using VVB CLI commands. For more information, refer to the Command Line Interface > Set Commands section in the Operations Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html .

CCE (on premise):

Cisco VVB is upgraded to 12.6(2) using a generic COP.

Cisco Unified CVP and Cisco VVB are configured:

Date and time in CVP, VVB, and proxy are synchronized with a common NTP server.

Access to DNS server is configured in CVP and VVB.

For more information on NTP and DNS server configurations in CVP, refer to the Microsoft Windows platform documentation.

For more information on NTP and DNS server configurations in VVB, refer to the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Port 443 and HTTP/2 are enabled in the proxy and firewall.

Average bandwidth consumption per call is 106 kbps.

The new Cisco Unified Call Studio application with the VirtualAgentVoice element is deployed. You can download and install the latest patch from https://software.cisco.com/download/specialrelease/c359e375005563ceec2081c9151b482e .

For details of the VirtualAgentVoice element, refer to the Element Specifications for Cisco Unified CVP VXML Server and Call Studio guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

Ensure that the Unified CCE OAMP , Cloud Connect, and VVB components have access to Webex services to use the Virtual Agent–Voice via cloud-based connector.

CCAI (in Cisco Webex Control Hub):

Service provider-specific Integration Connector is configured. For more details, see the article https://help.webex.com/en-us/article/9zvadfb/Configure-Google-CCAI-connector-for-Webex-Contact-Center .

Design Google Dialogflow CX Agents. For more information, refer to Google documentation at https://cloud.google.com/dialogflow/cx/docs/ .

CX conversational profile ID is created using credentials provided by Cisco via email. For detailed steps, see the section Create a Conversation Profile using Google Cloud SDK .

This conversation profile URL must be used to create the CCAI configuration.

CCAI configuration is created at https://admin.webex.com/ . For detailed steps, refer to the Create a Contact Center AI configuration article.

For further assistance, contact Cisco Support .

### What to do next

Configure Google Dialogflow CX Agent with Cisco Unified CCE solution.

## Configuration Task Flow

Task flow for configuring Google Dialogflow CX Agent with Cisco Unified CCE solution.

Step 1

Ensure that the Cloud Connect publisher and subscriber nodes are installed.

For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Step 2

Register and add Cloud Connect in Control Hub. For more details, see https://help.webex.com/en-us/article/n24wo0fb/Register-Cloud-Connect .

Step 3

Configure Cloud Connect with VVBs in the Operations Console (NOAMP for Cisco Unified CCE, and CCE Admin for Packaged CCE).

After an VVB upgrade, Cloud Connect has to be reconfigured with VVB devices.

Step 4

Import the Cloud Connect certificate to the CVP server.

For details, see the Unified CVP Security > Import Cloud Connect Certificate to Unified CVP Keystore section in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 5

View the default CCAI configuration (created as part of CCAI prerequisites). If required, synchronize the configuration (using Sync option), in the CVP Operations Console (NOAMP for Cisco Unified CCE and CCE Admin for Packaged CCE).

For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Cisco-Billed AI Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 6

Design Google Dialogflow CX application.

For more information, refer to Google documentation at https://dialogflow.cloud.google.com/cx/projects .

For further assistance, contact Cisco Support .

## Hybrid IVR with VAV via Cloud-based Connector

Dialogflow CX enables contact centers to use cloud-based AI features via Cisco Cloud. With Cisco's Hybrid IVR functionality,
                           customers who have on-premises applications can leverage their traditional ASR/TTS/CRM integrations, along with cloud-based
                           Dilaogflow CX AI capabilities. They can select a few nodes or sections of their application to be processed in the cloud and
                           few nodes to be processed on-premises. For example, in an application, OTP generation can be performed on-premises, while
                           other tasks can be processed in the cloud.

Hybrid IVR with Dialogflow CX provides the flexibility to switch from the cloud services to the on-premises application, to
                           use the on-premises subroutine calls, and perform the required operations. After these operations are done, the flow can go
                           back to the cloud services and resume from where it left.

The switching between the cloud services and the on-premises application is achieved by defining a custom payload with an
                           event and associated parameters. This custom payload is passed to the on-premises application. When the flow resumes in the
                           cloud, Dialogflow CX uses the event and parameters that are received from the on-premises application.

The VirtualAgentVoice element of Cisco Unified Call Studio is used to engage the Google Dialogflow CX services with Hybrid IVR functionality via
                           Cisco Cloud.

To configure the Hybrid IVR functionality with Dialogflow CX, see Configure Hybrid IVR .

Hybrid IVR functionality is available only with Dialogflow CX.

VirtualAgentVoice element supports both Cisco DTMF and Nuance adapters.

### Configure Hybrid IVR

Step 1

In the Google Dialogflow CX console, select the project and the agent.

Step 2

In the Google Dialogflow CX agent screen, under the Build tab, select the required flow and the required page ( Start / End Flow / End Session ) in this flow, in which a fulfillment is needed from the on-premises application. The details of the selected page appears.

Step 3

Under Routes section, define a route and conditions that satisfy the custom exit criteria, for triggering the transition.

Step 4

In this route, under Fulfillment section, click Add dialogue option and select Custom payload .

Only Custom payload has to be defined here. Do not add any other dialogue options.

Step 5

Add the custom payload of type Execute_Request that defines the action and elements to be filled in the Unified Call Studio VirtualAgentVoice element.

The format for defining the custom payload is as follows:

```
{"Execute_Request":{        
                   "Event_Name": "<Name of the event>",
                   "Data" : {        
                            "Params":{
                                     "<param1 name>": "<param1 value>",
                                     "<param2 name>": "<param2 value>"
                                     }        
                            }
                  }
}
```

Ensure that you map this event name with the same event name in Unified Call Studio VirtualAgentVoice element for decision mapping.

Step 6

Select Page under the Transition section, to set the transition to the same page when the flow resumes.

Step 7

For re-entry from the on-premises application to cloud, create an event handler. This event name is to be provided to the VirtualAgentVoice element during re-entry. For more information, refer to https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler .

The Dialogflow CX developer must create this event handler. Otherwise, the application fails.

## VAV over Premise-Based Connector

Virtual Agent–Voice via premise-based connector leverages Google's cloud-based Artificial Intelligence (AI) and Natural Language
                              Understanding (NLU) services for designing virtual voice agents and creating complex IVR call flows.

VAV currently supports two flavors of Google Dialogflow services via premise-based connector:

VAV for Dialogflow CX

VAV for Dialogflow ES

Ensure that the Unified CCE OAMP and Cloud Connect components have access to Webex services and VVB has access to Google services
                                          to use the Virtual Agent–Voice via premise-based connector.

Attention

Virtual Agent - Voice (VAV) over Premise based Connector, which utilizes Google's Dialogflow CX service leveraging DialogflowCX element in the Unified Call Studio is deprecated.

The Dialogflow ES integration, which is supported through the OAMP UI and powered by a service account, is now deprecated.

For more information, see the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html .

### VAV for Dialogflow CX

Overview

Prerequisites

Configuration Task Flow

#### Overview

Virtual Agent–Voice for Dialogflow CX leverages Google's Dialogflow CX service that allows designing virtual voice agents
                                 and creating and connecting complex IVR call flows.

Using Google Dialogflow CX, multiple agents can be created under the same Project ID. These agents can be accessed and managed
                                 for different lines of business with a single Google account. For more information, refer to the Google Dialogflow CX documentation
                                 at https://cloud.google.com/dialogflow/cx/docs .

VVB uses a premise-based connector to connect to the Google Dialogflow service. This service is enabled through the DialogflowCX element of Cisco Unified Call Studio.

For details of the DialogflowCX element, refer to the Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1) guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

Only u-law codec is supported.

This feature is available with Cisco subscription services only.

A-Law is supported for Dialogflow CX and Text-to-Speech with the VVB-based connector only.

#### Prerequisites

For supported minimum versions, refer to the Cisco Unified Customer Voice Portal > New Features > Virtual Agent–Voice for Dialogflow CX section in the Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1) . To configure Google Dialogflow CX, you should have completed the following procedures:

Step 1

The customer's CX Agent ID and GCP Project ID are created. For more information, see the Google documentation at https://dialogflow.cloud.google.com/cx/projects .

Step 2

Assessment to Quality (A2Q) process for Contact Center AI (CCAI) is completed and Cisco subscription Flex SKU for CX is procured.

Customer's GCP project ID is mapped with Cisco's GCP partner projects.

Control Hub credentials and Hybrid Org are generated.

For assistance, you can contact the Cisco TAC team.

Step 3

CX conversational profile ID is created using credentials provided by Cisco via email. For details, see Create a Conversation Profile using Google Cloud SDK . This conversation profile URL is to be used for creating the CCAI configuration.

Step 4

Cisco Unified CVP and Cisco VVB are configured:

Date and time in CVP, VVB, and proxy are synchronized with a common NTP server.

Access to DNS server is configured in CVP and VVB.

For more information on NTP and DNS server configurations in CVP, see the Microsoft Windows platform documentation.

For more information on NTP and DNS server configurations in VVB, see the Command Line Interface Reference Guide for Cisco Unified Communications Solutions .

Step 5

Port 443 and HTTP/2 are enabled in the proxy and firewall.

Step 6

The new Cisco Unified Call Studio application with the DialogflowCX element and Virtual Agent Voice element is deployed. You can download and install the latest patch from https://software.cisco.com/download/specialrelease/c359e375005563ceec2081c9151b482e .

Step 7

For details of the DialogflowCX element and Virtual Agent Voice element, see the Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1) guide.

##### What to do next

Configure Google Dialogflow CX Agent with Cisco Unified CCE solution.

#### Configuration Task Flow

Task flow for configuring the Google Dialogflow CX Agent with Cisco Unified CCE, or Packaged CCE solution.

Step 1

Ensure that the Cloud Connect publisher and subscriber nodes are installed.

For more information, see the Install Cloud Connect section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

Step 2

Register and add Cloud Connect in Control Hub.

For more details, see https://help.webex.com/en-us/article/n24wo0fb/ .

Step 3

Configure Cloud Connect with VVBs in the Operations Console (NOAMP for Cisco Unified CCE and CCE Admin for Packaged CCE).

Step 4

Import the Cloud Connect certificate to the CVP server.

For details, see the Unified CVP Security > Import Cloud Connect Certificate to Unified CVP Keystore section in the Configuration Guide for Cisco Unified Customer Voice Portal .

Step 5

View the default CCAI configuration. If required, synchronize the configuration (using Sync option) in the CVP Operations Console (NOAMP for Cisco Unified CCE and CCE Admin for Packaged CCE).

For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Cisco-Billed AI Services section in the Administration Guide for Cisco Unified Customer Voice Portal .

Step 6

Design Google Dialogflow CX application.

For more information, refer to Google documentation at https://dialogflow.cloud.google.com/cx/projects .

For further assistance, contact Cisco Support .

Step 7

To use the regionalised media support, see the Regional Media Data Center Region Mapping .

##### Create a Conversation Profile using Google Cloud SDK

The steps in the following procedure are for reference only. For more details, refer to Google Documentation.

Step 1

Get the agent ID:

Open https://dialogflow.cloud.google.com/cx/projects .

Select the appropriate project. The list of configured agents is displayed.

Note the agent ID to be configured. If no new agents are created, you can select a preconfigured agent.

Step 2

Create a user via Google IAM (Identity and Access Management) and add the following roles: Dialogflow API admin, Service Account
                                                Token Creator, and Service Account user .

For more information, see https://cloud.google.com/iam/docs/creating-managing-service-accounts .

Step 3

Install and configure the Google SDK on your system.

For more information, see https://cloud.google.com/sdk/docs/quickstart .

Step 4

When you are asked to log in during the installation of Google SDK, log in using the ID of the agent for whom you want to
                                                create the conversation profile.

Step 5

Run the following command: gcloud auth print-access-token --impersonate-service-account=Service Account ID

For more information, see https://cloud.google.com/iam/docs/impersonating-service-accounts .

Step 6

Create the conversation profile using REST API for Dialogflow by using Postman:

In the Postman workspace, select the method as POST .

In the URL field, add the address in the following format after replacing the regionId and projectId appropriately: https://<regionId>-dialogflow.googleapis.com/v2beta1/projects/<projectId>/locations/<regionId>/conversationProfiles

Under the Headers section, add the following key values for Authorization and Content-type:

Authorization: Bearer <token generated with the Google command>

Content-type: application/json

Under the Body section, select raw . From the last dropdown, select JSON .

In the code space, enter the following code (after replacing the regionId , projectId , and agentId in the agent tag with actual values):

```
{
"name": "TACCXTest",
"automatedAgentConfig": {
    "agent": "projects/<projectId>/locations/<regionId>/agents/<agentId>”
    },
"displayName": "TACCXTest",
"humanAgentAssistantConfig": {
    "messageAnalysisConfig": {    
        "enableEntityExtraction": true,
        "enableSentimentAnalysis": true
        }
    }
}
```

Click Send to run the command.

Example response:

```
{
"name": "projects/projectrtp2020/locations/us-central1/conversationProfiles/QlO36mwSUa3cjg",
"displayName": "TACCXTest",
"automatedAgentConfig": {
"agent": "projects/projectrtp2020/locations/us-central1/agents/40d0-aa2a-1bf453d9bf5c/environments/draft"
    },
"humanAgentAssistantConfig": {
"notificationConfig": {},
"messageAnalysisConfig": {
"enableEntityExtraction": true,
"enableSentimentAnalysis": true
        }
    },
"languageCode": "en-US"
}
```

In the above example response, the following conversation profile is obtained: projects/projectrtp2020/locations/us-central1/conversationProfiles/dQlO36mwSUa3cjg.

You can use this profile while creating the Control Hub configuration.

For more information, see https://cloud.google.com/sdk/gcloud/reference .

Step 7

Create the conversation profile using REST API for Dialogflow by using Postman:

Add headers: Content-type Application/json.

Authorization: Bearer - add the token generated with the Google command.

Add the method as POST.

In the URL section, add the address after replacing the regionId and the projectId appropriately. The address is in the following
                                                      format: https://<regionId>-dialogflow.googleapis.com/v2beta1/projects/<projectId>/locations/<regionId>/conversationProfiles

In the body section, choose RAW and JSON.

In the Agent tag, use the appropriate regionId, projectId, and agentId.

```
{
"name": "TACCXTest",
"automatedAgentConfig": {
"agent": "projects/<projectId>/locations/<regionId>/agents/<agentId>”
},
"displayName": "TACCXTest",
"humanAgentAssistantConfig": {
"messageAnalysisConfig": {
"enableEntityExtraction": true,
"enableSentimentAnalysis": true
}
}
}
```

Example response:

```
{
"name": "projects/tacprojectrtp2020/locations/us-central1/conversationProfiles/dCv4lC1uQlO36mwSUa3cjg",
"displayName": "TACCXTest",
"automatedAgentConfig": {
"agent": "projects/tacprojectrtp2020/locations/us-central1/agents/5cca975a-bbb3-40d0-aa2a-1bf453d9bf5c/environments/draft"
    },
"humanAgentAssistantConfig": {
"notificationConfig": {},
"messageAnalysisConfig": {
"enableEntityExtraction": true,
"enableSentimentAnalysis": true
        }
    },
"languageCode": "en-US"
}
```

This is the conversation profile that you obtain in the example. projects/tacprojectrtp2020/locations/us-central1/conversationProfiles/dCv4lC1uQlO36mwSUa3cjg. You can use this profile while creating the Control Hub configuration.

For more information, see https://cloud.google.com/sdk/gcloud/reference .

Step 8

In a new browser tab, open https://agentassist.cloud.google.com/ and select the appropriate project. The list of profiles is displayed.

Step 9

Click the copy icon next to the profile ID to be used. Copy the profile URL in the following format: projects/<project_ID>/locations/<location>/conversationProfiles/<profile ID>.

You can use this profile URL while creating the Control Hub configuration.

##### Create a Welcome Event

Create a welcome event to be played to the caller when a call is initiated.

Step 1

Open https://dialogflow.cloud.google.com/cx/projects .

Step 2

Select the project and agent for which the welcome event is to be configured.

Step 3

In the Google Dialogflow CX Agent screen, click Default Start Flow in the left panel.

Step 4

Click Start > Event handlers .

Step 5

In the right panel, click Add event handler .

Step 6

Check the Use custom event checkbox.

Step 7

In the Custom Event textbox, type welcome_event .

Step 8

In the Agent says textbox, type the welcome message to be played.

Step 9

Save the changes.

To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured in the CX Agent to start the flow.

### VAV for Dialogflow ES

Dialogflow ES over VVB for OEM Users

Dialogflow ES over VVB for Non-OEM Users

#### Dialogflow ES over VVB for OEM Users

##### Overview

Virtual Agent–Voice (VAV) feature provides an enhanced onboarding experience to OEM customers using Webex Control Hub. All
                                       contract, billing, and support are managed through Cisco for OEM customers and they can use Cisco services coupled with Google’s
                                       cloud-based-AI-enabled speech services.

A single config ID generated via Control Hub can be leveraged across all CVP/VVB instances as compared to the earlier experience
                                       where each instance was required to be configured individually.

##### Prerequisites

The prerequisites for configuring Virtual Agent–Voice for OEM users are:

OEM users must provision Google Contact Center AI (CCAI) for Cisco Contact Center Enterprise. For details, see the Create a Contact Center AI configuration article at https://help.webex.com/en-us/article/npbt02j/Create-a-Contact-Center-AI-configuration .

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

12.5 and higher

12.5 and higher

NA

11.6/12.0 with A2Q approval

11.6/12.0 with A2Q approval

##### VAV Onboarding for OEM Users Task Flow

Follow this procedure to provision Google CCAI with Cisco Unified Contact Center Enterprise. A single configuration created
                                       via Control Hub can be used for accessing multiple AI services, such as VAV and Agent Answers on multiple devices.

Step 1

Create a CCAI configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services.

While creating a CCAI configuration (explained in the article https://help.webex.com/en-us/article/npbt02j/Create-a-Contact-Center-AI-configuration ):

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

###### What to do next

To change or override the default config (created in step 1), configure the CCAI.configId property of the Dialogflow element in Call Studio.

For details, see the Dialogflow Element > Custom VoiceXML Properties section in the Element Specifications for Cisco Unified CVP VXML Server and Call Studio at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

##### Migration for OEM Users

OEM users migrating from 12.5(1) or 12.5(1a) to 12.6(1) and later must onboard via Webex Control Hub for better experience
                                       and enhanced security. They can continue to use the old method of key generation by retaining their old configurations until
                                       their onboarding via Webex Control Hub is complete.

##### Important Considerations

Consider the following before configuring VAV via cloud-based connector:

Supported codec is u-law.

Voice activity detection is done by Google.

Allowed list in the customer's network must include the following URLs:

Allowed list in the customer's network must also include the following group of URLs:

Nonproxy hosts to be added using VVB CLI commands. For more information, refer to the Command Line Interface > Set Commands section in the Operations Guide for Cisco Virtualized Voice Browser, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html .

The counters available for Speech Server can be accessed via NOAMP ( NOAMP > Statistics ), AppD, or REST API.

Non barge-in prompt is supported only until the control gets transferred to the cloud.

Average bandwidth consumption per call is 106 kbps.

#### Dialogflow ES over VVB for Non-OEM Users

##### Overview

From 12.5(1) release, non-OEM users use NOAMP in Unified CCE solution, and CCE Administration Portal in Packaged CCE solution
                                       for VAV onboarding.

The following table lists the onboarding channel and Google APIs used for non-OEM customers:

Release

Services Billing

Onboarding

Google APIs

##### Prerequisites

CVP/VVB configuration:

Enable access to cloud-based services from CVP and VVB directly or via proxy.

For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                                      for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Synchronize the date/time in CVP, VVB, and proxy with a common NTP server.

Configure access to DNS server in CVP/VVB.

For more information on NTP and DNS server configurations in CVP, refer to the Microsoft Windows platform documentation.

For more information on NTP and DNS server configurations in VVB, refer to the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Access key for Google Text-to-Speech. For more information, see https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries .

Access key for Google Speech-to-Text. For more information, see https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries .

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

11.6/12.0 with A2Q approval

11.6/12.0 with A2Q approval

##### VAV Onboarding for Non-OEM Users Task Flow

Step 1

Enable Speech Services for Non-OEM Users .

Step 2

Generate the JSON Key for Non-OEM Users .

Step 3

Configure VVB devices for speech services.

For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Vendor-Billed AI
                                                      Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

##### Enable Speech Services for Non-OEM Users

Step 1

Log in to your Dialogflow account at https://dialogflow.cloud.google.com/ .

Step 2

Scroll down on the homepage and click Project ID of your Dialogflow agent.

This takes you to the Google Cloud Platform (GCP) homepage.

Step 3

Select APIs & Services from the left pane (through the hamburger menu).

Step 4

Select the API services (such as Cloud Text-to-Speech, Cloud Speech-to-Text, and Dialogflow) to be enabled.

Step 5

Click Enable to enable the selected API for the given Project ID.

##### Generate the JSON Key for Non-OEM Users

For best results:

Migrate your Dialogflow Agent to Enterprise Essential ( Console Left Bar > Migrate from Standard to Enterprise Essential ).

Enable the enhanced Speech Model in Dialogflow console ( Settings > Speech > Enable Enhanced Speech Model and Data Logging ).

If this option is enabled, speech recognition data is shared with Google. For more information see https://cloud.google.com/speech-to-text/docs/enhanced-models .

Step 1

In the GCP homepage, select IAM & Admin from the left pane (use the hamburger menu).

Step 2

Select Service accounts which shows the list of your enabled services.

Step 3

Select the service account for which the JSON key is to be generated.

Step 4

Click the ellipsis menu on the right and click +Create Key .

Step 5

Select JSON as Key type and then click Create .

## Documentation Resources

The following table lists the reference documents for VAV.

Information

Resource

Sample VAV Application

See https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant .

Design Considerations

Design Considerations for Integrated Features > Virtual Agent–Voice Considerations section in the Solution Design Guide .

VAV configuration in Packaged CCE Deployment

Virtual Agent–Voice section in the Packaged CCE Administration and Configuration Guide .

VAV configuration in Unified CCE Deployment

Operations Console (NOAMP) section in the CVP Administration Guide .

TTS Prompt Cache Management and proxy setting for Speech Server

VVB Operations Guide .

Proxy settings for VXML Server

See the VXML Server Configuration > Proxy Settings in VXML Server for Virtual Agent–Voice section in the CVP Configuration Guide .

Configuration of Call Studio elements for VAV

The following chapters are in the CVP Element Specification Guide :

Dialogflow Element

DialogflowIntent Element

DialogflowParam Element

Transcribe Element

VAV Speech Configuration APIs

See VAV Speech Configuration section in the VVB Developer Guide .

## Regional Media Data Center Region Mapping

Contact Center Enterprise (CCE) now extends support for regional media across all supported data centre locations. This feature
                              allows both customer and agent media (including audio and SIP signalling) to remain local to a specific geographic region,
                              irrespective of the location of the CCAI cloud services data center tenant or home location.

To utilize regional media from a country or location that differs from your customer’s organization, it is necessary to configure
                              the appropriate variables in the SIP profile. This configuration should be done within the Session Border Controller (SBC)
                              for both Virtual Agent-Voice and Agent Answers.

To enable regional media, follow these steps:

Step 1

Access the SBC console and modify the existing SIP profile configuration, which was used during the setup of both Virtual
                                       Agent-Voice and Agent Answers. For more information, see the Create a SIP Profile at the Dial-Peer Level in CUBE section in this Guide.

Step 2

Run the following command to add the X-Cisco-Clusterid variable. This variable is added using a custom SIP header in the outgoing INVITE request as shown below:

```
request INVITE sip-header Call-Info add "X-Cisco-Clusterid : rtmsClusterId = <Regional Media Variable> ; wxccClusterId = <Cisco CCAI Services Variable>"
```

The x-Cisco-Clusterid variable requires the following key values:

rtmsClusterId : The value of the variable used for Regional Media data center.

wxccClusterId : The value of the variable used for CCAI cloud services data center.

```
request INVITE sip-header Call-Info add "X-Cisco-Clusterid : rtmsClusterId = US1 ; wxccClusterId = US1"
```

The following tables list the variables associated with regional media data centers located in different countries. If your
                                          region is not listed below, ensure that you select the nearest data center location applicable to your region.

Important

Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment.

S. No

Country of Operation

Regional Media Data Center

Regional Media Variable

Cisco CCAI Services Variable

Default Regional Media Variable

Default Cisco CCAI Services Variable

1

Australia

Australia

AS1

ANZ1

AS1

ANZ1

2

Indonesia

Singapore

SN1

ANZ1

AS1

ANZ1

3

Jordan

United Kingdom

UK1

EU1

UK1

EU1

4

Malaysia

Singapore

SN1

ANZ1

AS1

ANZ1

5

New Zealand

Australia

ANZ1

ANZ1

AS1

ANZ1

6

Philippines

Singapore

SN1

ANZ1

AS1

ANZ1

7

Singapore

Singapore

SN1

ANZ1

AS1

ANZ1

8

South Korea

Japan

JA1

JP1

AS1

ANZ1

9

Thailand

Singapore

SN1

ANZ1

AS1

ANZ1

10

Vietnam

Singapore

SN1

ANZ1

AS1

ANZ1

11

Japan

Japan

JA1

JP1

JA1

JP1

12

India

India

IN1

IN1

IN1

IN1

S. No

Country of Operation

Regional Media Data Center

Regional Media Variable

Cisco CCAI Services Variable

Default Regional Media Variable

Cisco CCAI Services Variable

1

Austria

Germany

GM1

EU2

GM1

EU2

2

Belgium

Germany

GM1

EU2

GM1

EU2

3

Bulgaria

Germany

GM1

EU2

GM1

EU2

4

Croatia

Germany

GM1

EU2

GM1

EU2

5

Cyprus

Germany

GM1

EU2

GM1

EU2

6

Czech Republic

Germany

GM1

EU2

GM1

EU2

7

Denmark

Germany

GM1

EU2

GM1

EU2

8

Estonia

Germany

GM1

EU2

GM1

EU2

9

Finland

Germany

GM1

EU2

GM1

EU2

10

France

Germany

GM1

EU2

GM1

EU2

11

Georgia

Germany

GM1

EU2

GM1

EU2

12

Germany

Germany

GM1

EU2

GM1

EU2

13

Greece

Germany

GM1

EU2

GM1

EU2

14

Hungary

Germany

GM1

EU2

GM1

EU2

15

Ireland

Germany

GM1

EU2

GM1

EU2

16

Italy

Germany

GM1

EU2

GM1

EU2

17

Latvia

Germany

GM1

EU2

GM1

EU2

18

Lithuania

Germany

GM1

EU2

GM1

EU2

19

Luxembourg

Germany

GM1

EU2

GM1

EU2

20

Malta

Germany

GM1

EU2

GM1

EU2

21

Netherlands

Germany

GM1

EU2

GM1

EU2

22

Norway

Germany

GM1

EU2

GM1

EU2

23

Poland

Germany

GM1

EU2

GM1

EU2

24

Portugal

Germany

GM1

EU2

GM1

EU2

25

Romania

Germany

GM1

EU2

GM1

EU2

26

Slovakia

Germany

GM1

EU2

GM1

EU2

27

Slovenia

Germany

GM1

EU2

GM1

EU2

28

Spain

Germany

GM1

EU2

GM1

EU2

29

Sweden

Germany

GM1

EU2

GM1

EU2

30

Switzerland

Germany

GM1

EU2

GM1

EU2

31

Ukraine

Germany

GM1

EU2

GM1

EU2

32

United Arab Emirates

Germany

GM1

EU2

GM1

EU2

Saudi Arabia

United Kingdom

UK1

EU1

UK1

EU1

34

South Africa

United Kingdom

UK1

EU1

UK1

EU1

35

South Sudan

United Kingdom

UK1

EU1

UK1

EU1

36

United Kingdom

United Kingdom

UK1

EU1

UK1

EU1

S. No

Country of Operation

Regional Media Data Center

Regional Media Variable

Cisco CCAI Services Variable

Default Regional Media Variable

Default Cisco CCAI Services Variable

1

Argentina

United States

US1

US1

US1

US1

2

Aruba

United States

US1

US1

US1

US1

3

Bahamas

United States

US1

US1

US1

US1

4

Belize

United States

US1

US1

US1

US1

5

Bermuda

United States

US1

US1

US1

US1

6

Brazil

United States

US1

US1

US1

US1

7

Caymen Islands

United States

US1

US1

US1

US1

8

Chile

United States

US1

US1

US1

US1

9

Colombia

United States

US1

US1

US1

US1

10

Costa Rica

United States

US1

US1

US1

US1

11

Curacao

United States

US1

US1

US1

US1

12

Dominican Republic

United States

US1

US1

US1

US1

13

Ecuador

United States

US1

US1

US1

US1

14

El Salvador

United States

US1

US1

US1

US1

15

Guatemala

United States

US1

US1

US1

US1

16

Honduras

United States

US1

US1

US1

US1

18

Jamaica

United States

US1

US1

US1

US1

19

Mexico

United States

US1

US1

US1

US1

20

Nicaragua

United States

US1

US1

US1

US1

21

Panama

United States

US1

US1

US1

US1

22

Peru

United States

US1

US1

US1

US1

23

Puerto Rico

United States

US1

US1

US1

US1

24

Trinidad and Tobago

United States

US1

US1

US1

US1

25

United States

United States

US1

US1

US1

US1

26

Canada

Canada

CA1

CA1

CA1

CA1

Step 3

To ensure connection with the Cisco Finesse gadget, you must enable the POD.ID Extended Call Context (ECC) variable in Unified CCE Configuration Manager > List Tools > Expanded Call Variables List .

After you enable the POD.ID, you must restart the VRU PG during non-production time or a scheduled maintenance window for
                                                      the changes to take full effect.

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| Note | Ensure that the Unified CCE OAMP, VVB, and Cloud Connect Components have access to Webex services to use the Virtual Agent-Voice via cloud-based connector
                                       and premise-based connector. |
|---|---|

| Release | Services Billing | Onboarding | Google APIs |
|---|---|---|---|
| 12.6(1) and above | Cisco-billed (OEM) and Vendor-billed (non-OEM) | Webex Control Hub | AnalyzeContent (V2) |
| 12.6(1) and above | Vendor-billed (non-OEM) | NOAMP/CCEAdmin | DetectIntent (V2) |

|  | VAV Dialogflow CX (OEM) | VAV Dialogflow ES (OEM) | VAV Dialogflow CX (Non-OEM) | VAV Dialogflow ES (Non-OEM) |
|---|---|---|---|---|
| Via cloud-based connector | Yes (12.6(2) and above) | No | Yes (12.6(2) and above) | No |
| Via premise-based connector | Yes (12.6(1) and above) | Yes (12.6(1) and above) | Yes (12.6(2) and above) | Yes (12.6(1) and above) |

| Note | Webex Contact Center Enterprise leverages Webex Contact Center AI (WCCAI) Cloud Orchestration Platform (Universal Harnes)
                                       for AI services. |
|---|---|

| The allowed list of your customer's network must include the following group of URLs: accounts.google.com/o/oauth2 *.cisco.com *.ciscoservice.com *.ciscoccservice.com *.ciscospark.com *.cloud.google.com/dialogflow *.google.com *.googleapis.com *.gcr.io *.rtmsprod.net *.webex.com *.wbx2.com The customer's CX Agent ID and GCP Project ID are created. For more information, refer to Google documentation at https://dialogflow.cloud.google.com/cx/projects . Assessment to Quality (A2Q) process for Contact Center AI (CCAI) is completed and Cisco subscription Flex SKU for CX is procured. Customer's GCP project ID is mapped with Cisco's GCP partner projects. Control Hub credentials (For more information, see https://www.webex.com/us/en/solutions/cross-platform/control-hub.html ) and Hybrid Org (For more information, see https://www.webex.com/us/en/solutions/hybrid-work.html ) are generated. Access the associated location settings for regions at Google at https://cloud.google.com/dialogflow/cx/docs/concept/region Add non-proxy hosts using VVB CLI commands. For more information, refer to the Command Line Interface > Set Commands section in the Operations Guide for Cisco Virtualized Voice Browser at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-maintenance-guides-list.html . CCE (on premise): Cisco VVB is upgraded to 12.6(2) using a generic COP. Cisco Unified CVP and Cisco VVB are configured: Date and time in CVP, VVB, and proxy are synchronized with a common NTP server. Access to DNS server is configured in CVP and VVB. For more information on NTP and DNS server configurations in CVP, refer to the Microsoft Windows platform documentation. For more information on NTP and DNS server configurations in VVB, refer to the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . Port 443 and HTTP/2 are enabled in the proxy and firewall. Average bandwidth consumption per call is 106 kbps. The new Cisco Unified Call Studio application with the VirtualAgentVoice element is deployed. You can download and install the latest patch from https://software.cisco.com/download/specialrelease/c359e375005563ceec2081c9151b482e . For details of the VirtualAgentVoice element, refer to the Element Specifications for Cisco Unified CVP VXML Server and Call Studio guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html . Ensure that the Unified CCE OAMP , Cloud Connect, and VVB components have access to Webex services to use the Virtual Agent–Voice via cloud-based connector. CCAI (in Cisco Webex Control Hub): Service provider-specific Integration Connector is configured. For more details, see the article https://help.webex.com/en-us/article/9zvadfb/Configure-Google-CCAI-connector-for-Webex-Contact-Center . Design Google Dialogflow CX Agents. For more information, refer to Google documentation at https://cloud.google.com/dialogflow/cx/docs/ . CX conversational profile ID is created using credentials provided by Cisco via email. For detailed steps, see the section Create a Conversation Profile using Google Cloud SDK . Note En-US global customers can create the conversational profile ID through the UI at https://agentassist.cloud.google.com/projects . While creating the profile, enable the option Enable virtual agent under Choose to use Dialogflow . This profile ID can be used both for the Agent Answers and VAV features. This conversation profile URL must be used to create the CCAI configuration. CCAI configuration is created at https://admin.webex.com/ . For detailed steps, refer to the Create a Contact Center AI configuration article. For further assistance, contact Cisco Support . | Note | En-US global customers can create the conversational profile ID through the UI at https://agentassist.cloud.google.com/projects . While creating the profile, enable the option Enable virtual agent under Choose to use Dialogflow . This profile ID can be used both for the Agent Answers and VAV features. |
|---|---|---|
| Note | En-US global customers can create the conversational profile ID through the UI at https://agentassist.cloud.google.com/projects . While creating the profile, enable the option Enable virtual agent under Choose to use Dialogflow . This profile ID can be used both for the Agent Answers and VAV features. |

| Note | En-US global customers can create the conversational profile ID through the UI at https://agentassist.cloud.google.com/projects . While creating the profile, enable the option Enable virtual agent under Choose to use Dialogflow . This profile ID can be used both for the Agent Answers and VAV features. |
|---|---|

| Step 1 | Ensure that the Cloud Connect publisher and subscriber nodes are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
|---|---|
| Step 2 | Register and add Cloud Connect in Control Hub. For more details, see https://help.webex.com/en-us/article/n24wo0fb/Register-Cloud-Connect . |
| Step 3 | Configure Cloud Connect with VVBs in the Operations Console (NOAMP for Cisco Unified CCE, and CCE Admin for Packaged CCE). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                          for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . Note After an VVB upgrade, Cloud Connect has to be reconfigured with VVB devices. | Note | After an VVB upgrade, Cloud Connect has to be reconfigured with VVB devices. |
| Note | After an VVB upgrade, Cloud Connect has to be reconfigured with VVB devices. |
| Step 4 | Import the Cloud Connect certificate to the CVP server. For details, see the Unified CVP Security > Import Cloud Connect Certificate to Unified CVP Keystore section in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 5 | View the default CCAI configuration (created as part of CCAI prerequisites). If required, synchronize the configuration (using Sync option), in the CVP Operations Console (NOAMP for Cisco Unified CCE and CCE Admin for Packaged CCE). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Cisco-Billed AI Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 6 | Design Google Dialogflow CX application. For more information, refer to Google documentation at https://dialogflow.cloud.google.com/cx/projects . For further assistance, contact Cisco Support . |

| Note | After an VVB upgrade, Cloud Connect has to be reconfigured with VVB devices. |
|---|---|

| Note | Hybrid IVR functionality is available only with Dialogflow CX. VirtualAgentVoice element supports both Cisco DTMF and Nuance adapters. |
|---|---|

| Step 1 | In the Google Dialogflow CX console, select the project and the agent. |
|---|---|
| Step 2 | In the Google Dialogflow CX agent screen, under the Build tab, select the required flow and the required page ( Start / End Flow / End Session ) in this flow, in which a fulfillment is needed from the on-premises application. The details of the selected page appears. |
| Step 3 | Under Routes section, define a route and conditions that satisfy the custom exit criteria, for triggering the transition. |
| Step 4 | In this route, under Fulfillment section, click Add dialogue option and select Custom payload . Note Only Custom payload has to be defined here. Do not add any other dialogue options. | Note | Only Custom payload has to be defined here. Do not add any other dialogue options. |
| Note | Only Custom payload has to be defined here. Do not add any other dialogue options. |
| Step 5 | Add the custom payload of type Execute_Request that defines the action and elements to be filled in the Unified Call Studio VirtualAgentVoice element. The format for defining the custom payload is as follows: {"Execute_Request":{        
                   "Event_Name": "<Name of the event>",
                   "Data" : {        
                            "Params":{
                                     "<param1 name>": "<param1 value>",
                                     "<param2 name>": "<param2 value>"
                                     }        
                            }
                  }
} Note Ensure that you map this event name with the same event name in Unified Call Studio VirtualAgentVoice element for decision mapping. | Note | Ensure that you map this event name with the same event name in Unified Call Studio VirtualAgentVoice element for decision mapping. |
| Note | Ensure that you map this event name with the same event name in Unified Call Studio VirtualAgentVoice element for decision mapping. |
| Step 6 | Select Page under the Transition section, to set the transition to the same page when the flow resumes. |
| Step 7 | For re-entry from the on-premises application to cloud, create an event handler. This event name is to be provided to the VirtualAgentVoice element during re-entry. For more information, refer to https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler . The Dialogflow CX developer must create this event handler. Otherwise, the application fails. |

| Note | Only Custom payload has to be defined here. Do not add any other dialogue options. |
|---|---|

| Note | Ensure that you map this event name with the same event name in Unified Call Studio VirtualAgentVoice element for decision mapping. |
|---|---|

| Note | Ensure that the Unified CCE OAMP and Cloud Connect components have access to Webex services and VVB has access to Google services
                                          to use the Virtual Agent–Voice via premise-based connector. |
|---|---|

| Attention | Virtual Agent - Voice (VAV) over Premise based Connector, which utilizes Google's Dialogflow CX service leveraging DialogflowCX element in the Unified Call Studio is deprecated. The Dialogflow ES integration, which is supported through the OAMP UI and powered by a service account, is now deprecated. For more information, see the Release Notes for Cisco Contact Center Enterprise Solutions at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html . |
|---|---|

| Note | Only u-law codec is supported. This feature is available with Cisco subscription services only. |
|---|---|

| Note | A-Law is supported for Dialogflow CX and Text-to-Speech with the VVB-based connector only. |
|---|---|

| Step 1 | The customer's CX Agent ID and GCP Project ID are created. For more information, see the Google documentation at https://dialogflow.cloud.google.com/cx/projects . |
|---|---|
| Step 2 | Assessment to Quality (A2Q) process for Contact Center AI (CCAI) is completed and Cisco subscription Flex SKU for CX is procured. Customer's GCP project ID is mapped with Cisco's GCP partner projects. Control Hub credentials and Hybrid Org are generated. For assistance, you can contact the Cisco TAC team. |
| Step 3 | CX conversational profile ID is created using credentials provided by Cisco via email. For details, see Create a Conversation Profile using Google Cloud SDK . This conversation profile URL is to be used for creating the CCAI configuration. |
| Step 4 | Cisco Unified CVP and Cisco VVB are configured: Date and time in CVP, VVB, and proxy are synchronized with a common NTP server. Access to DNS server is configured in CVP and VVB. For more information on NTP and DNS server configurations in CVP, see the Microsoft Windows platform documentation. For more information on NTP and DNS server configurations in VVB, see the Command Line Interface Reference Guide for Cisco Unified Communications Solutions . |
| Step 5 | Port 443 and HTTP/2 are enabled in the proxy and firewall. |
| Step 6 | The new Cisco Unified Call Studio application with the DialogflowCX element and Virtual Agent Voice element is deployed. You can download and install the latest patch from https://software.cisco.com/download/specialrelease/c359e375005563ceec2081c9151b482e . |
| Step 7 | For details of the DialogflowCX element and Virtual Agent Voice element, see the Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1) guide. |

| Step 1 | Ensure that the Cloud Connect publisher and subscriber nodes are installed. For more information, see the Install Cloud Connect section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide . |
|---|---|
| Step 2 | Register and add Cloud Connect in Control Hub. For more details, see https://help.webex.com/en-us/article/n24wo0fb/ . |
| Step 3 | Configure Cloud Connect with VVBs in the Operations Console (NOAMP for Cisco Unified CCE and CCE Admin for Packaged CCE). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                                for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal . |
| Step 4 | Import the Cloud Connect certificate to the CVP server. For details, see the Unified CVP Security > Import Cloud Connect Certificate to Unified CVP Keystore section in the Configuration Guide for Cisco Unified Customer Voice Portal . |
| Step 5 | View the default CCAI configuration. If required, synchronize the configuration (using Sync option) in the CVP Operations Console (NOAMP for Cisco Unified CCE and CCE Admin for Packaged CCE). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Cisco-Billed AI Services section in the Administration Guide for Cisco Unified Customer Voice Portal . |
| Step 6 | Design Google Dialogflow CX application. For more information, refer to Google documentation at https://dialogflow.cloud.google.com/cx/projects . For further assistance, contact Cisco Support . |
| Step 7 | To use the regionalised media support, see the Regional Media Data Center Region Mapping . |

| Note | The steps in the following procedure are for reference only. For more details, refer to Google Documentation. |
|---|---|

| Step 1 | Get the agent ID: Open https://dialogflow.cloud.google.com/cx/projects . Select the appropriate project. The list of configured agents is displayed. Note the agent ID to be configured. If no new agents are created, you can select a preconfigured agent. |
|---|---|
| Step 2 | Create a user via Google IAM (Identity and Access Management) and add the following roles: Dialogflow API admin, Service Account
                                                Token Creator, and Service Account user . For more information, see https://cloud.google.com/iam/docs/creating-managing-service-accounts . |
| Step 3 | Install and configure the Google SDK on your system. For more information, see https://cloud.google.com/sdk/docs/quickstart . |
| Step 4 | When you are asked to log in during the installation of Google SDK, log in using the ID of the agent for whom you want to
                                                create the conversation profile. Note You can also log in using the same ID to the GCP CLI with the command gcloud auth login after installing the Google SDK. | Note | You can also log in using the same ID to the GCP CLI with the command gcloud auth login after installing the Google SDK. |
| Note | You can also log in using the same ID to the GCP CLI with the command gcloud auth login after installing the Google SDK. |
| Step 5 | Run the following command: gcloud auth print-access-token --impersonate-service-account=Service Account ID For more information, see https://cloud.google.com/iam/docs/impersonating-service-accounts . |
| Step 6 | Create the conversation profile using REST API for Dialogflow by using Postman: In the Postman workspace, select the method as POST . In the URL field, add the address in the following format after replacing the regionId and projectId appropriately: https://<regionId>-dialogflow.googleapis.com/v2beta1/projects/<projectId>/locations/<regionId>/conversationProfiles Under the Headers section, add the following key values for Authorization and Content-type: Authorization: Bearer <token generated with the Google command> Content-type: application/json Under the Body section, select raw . From the last dropdown, select JSON . In the code space, enter the following code (after replacing the regionId , projectId , and agentId in the agent tag with actual values): {
"name": "TACCXTest",
"automatedAgentConfig": {
    "agent": "projects/<projectId>/locations/<regionId>/agents/<agentId>”
    },
"displayName": "TACCXTest",
"humanAgentAssistantConfig": {
    "messageAnalysisConfig": {    
        "enableEntityExtraction": true,
        "enableSentimentAnalysis": true
        }
    }
} Click Send to run the command. Example response: {
"name": "projects/projectrtp2020/locations/us-central1/conversationProfiles/QlO36mwSUa3cjg",
"displayName": "TACCXTest",
"automatedAgentConfig": {
"agent": "projects/projectrtp2020/locations/us-central1/agents/40d0-aa2a-1bf453d9bf5c/environments/draft"
    },
"humanAgentAssistantConfig": {
"notificationConfig": {},
"messageAnalysisConfig": {
"enableEntityExtraction": true,
"enableSentimentAnalysis": true
        }
    },
"languageCode": "en-US"
} In the above example response, the following conversation profile is obtained: projects/projectrtp2020/locations/us-central1/conversationProfiles/dQlO36mwSUa3cjg. You can use this profile while creating the Control Hub configuration. For more information, see https://cloud.google.com/sdk/gcloud/reference . |
| Step 7 | Create the conversation profile using REST API for Dialogflow by using Postman: Add headers: Content-type Application/json. Authorization: Bearer - add the token generated with the Google command. Add the method as POST. In the URL section, add the address after replacing the regionId and the projectId appropriately. The address is in the following
                                                      format: https://<regionId>-dialogflow.googleapis.com/v2beta1/projects/<projectId>/locations/<regionId>/conversationProfiles In the body section, choose RAW and JSON. In the Agent tag, use the appropriate regionId, projectId, and agentId. {
"name": "TACCXTest",
"automatedAgentConfig": {
"agent": "projects/<projectId>/locations/<regionId>/agents/<agentId>”
},
"displayName": "TACCXTest",
"humanAgentAssistantConfig": {
"messageAnalysisConfig": {
"enableEntityExtraction": true,
"enableSentimentAnalysis": true
}
}
} Example response: {
"name": "projects/tacprojectrtp2020/locations/us-central1/conversationProfiles/dCv4lC1uQlO36mwSUa3cjg",
"displayName": "TACCXTest",
"automatedAgentConfig": {
"agent": "projects/tacprojectrtp2020/locations/us-central1/agents/5cca975a-bbb3-40d0-aa2a-1bf453d9bf5c/environments/draft"
    },
"humanAgentAssistantConfig": {
"notificationConfig": {},
"messageAnalysisConfig": {
"enableEntityExtraction": true,
"enableSentimentAnalysis": true
        }
    },
"languageCode": "en-US"
} This is the conversation profile that you obtain in the example. projects/tacprojectrtp2020/locations/us-central1/conversationProfiles/dCv4lC1uQlO36mwSUa3cjg. You can use this profile while creating the Control Hub configuration. For more information, see https://cloud.google.com/sdk/gcloud/reference . |
| Step 8 | In a new browser tab, open https://agentassist.cloud.google.com/ and select the appropriate project. The list of profiles is displayed. |
| Step 9 | Click the copy icon next to the profile ID to be used. Copy the profile URL in the following format: projects/<project_ID>/locations/<location>/conversationProfiles/<profile ID>. You can use this profile URL while creating the Control Hub configuration. |

| Note | You can also log in using the same ID to the GCP CLI with the command gcloud auth login after installing the Google SDK. |
|---|---|

| Step 1 | Open https://dialogflow.cloud.google.com/cx/projects . |
|---|---|
| Step 2 | Select the project and agent for which the welcome event is to be configured. |
| Step 3 | In the Google Dialogflow CX Agent screen, click Default Start Flow in the left panel. |
| Step 4 | Click Start > Event handlers . |
| Step 5 | In the right panel, click Add event handler . |
| Step 6 | Check the Use custom event checkbox. |
| Step 7 | In the Custom Event textbox, type welcome_event . |
| Step 8 | In the Agent says textbox, type the welcome message to be played. |
| Step 9 | Save the changes. Note To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured in the CX Agent to start the flow. | Note | To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured in the CX Agent to start the flow. |
| Note | To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured in the CX Agent to start the flow. |

| Note | To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured in the CX Agent to start the flow. |
|---|---|

| Note | The Dialogflow ES GCP project trial version should not be used in a production environment. |
|---|---|

| CVP | VVB | Cloud Connect | CCE Components | ICM |
|---|---|---|---|---|
| 12.5 and higher | 12.5 and higher | NA | 11.6/12.0 with A2Q approval | 11.6/12.0 with A2Q approval |

| Step 1 | Create a CCAI configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services. For details, see the Create a Contact Center AI configuration article. This default config can be used for accessing multiple AI services on multiple devices. Note While creating a CCAI configuration (explained in the article https://help.webex.com/en-us/article/npbt02j/Create-a-Contact-Center-AI-configuration ): Skip the creation of conversation profile. Select the Apply as default for Virtual Agent configuration, because it is mandatory for ASR and TTS. | Note | While creating a CCAI configuration (explained in the article https://help.webex.com/en-us/article/npbt02j/Create-a-Contact-Center-AI-configuration ): Skip the creation of conversation profile. Select the Apply as default for Virtual Agent configuration, because it is mandatory for ASR and TTS. |
|---|---|---|---|
| Note | While creating a CCAI configuration (explained in the article https://help.webex.com/en-us/article/npbt02j/Create-a-Contact-Center-AI-configuration ): Skip the creation of conversation profile. Select the Apply as default for Virtual Agent configuration, because it is mandatory for ASR and TTS. |
| Step 2 | Ensure that the Cloud Connect publisher and subscriber are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Step 3 | Import the Cloud Connect certificate to the CVP server. For details, see the Unified CVP Security > Import Cloud Connect Certificate to Unified CVP Keystore section in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 4 | Configure Cloud Connect with CVP in the Operations Console (NOAMP). |
| Step 5 | Configure Cloud Connect with VVBs in the Operations Console (NOAMP). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                                   for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 6 | View the default CCAI configuration (created in step 1). If required, synchronize the configuration (using Sync option) in the CVP Operations Console (NOAMP). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Cisco-Billed AI Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |

| Note | While creating a CCAI configuration (explained in the article https://help.webex.com/en-us/article/npbt02j/Create-a-Contact-Center-AI-configuration ): Skip the creation of conversation profile. Select the Apply as default for Virtual Agent configuration, because it is mandatory for ASR and TTS. |
|---|---|

| Note | To change or override the default config (created in step 1), configure the CCAI.configId property of the Dialogflow element in Call Studio. For details, see the Dialogflow Element > Custom VoiceXML Properties section in the Element Specifications for Cisco Unified CVP VXML Server and Call Studio at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html . |
|---|---|

| Release | Services Billing | Onboarding | Google APIs |
|---|---|---|---|
| 12.5(1) and above | Vendor-billed (non-OEM) | NOAMP/CCEAdmin | DetectIntent (V2) |

| CVP | VVB | Cloud Connect | CCE Components | ICM |
|---|---|---|---|---|
| 12.5 and higher | 12.5 and higher | NA | 11.6/12.0 with A2Q approval | 11.6/12.0 with A2Q approval |

| Step 1 | Enable Speech Services for Non-OEM Users . |
|---|---|
| Step 2 | Generate the JSON Key for Non-OEM Users . |
| Step 3 | Configure VVB devices for speech services. For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Vendor-Billed AI
                                                      Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |

| Step 1 | Log in to your Dialogflow account at https://dialogflow.cloud.google.com/ . |
|---|---|
| Step 2 | Scroll down on the homepage and click Project ID of your Dialogflow agent. This takes you to the Google Cloud Platform (GCP) homepage. |
| Step 3 | Select APIs & Services from the left pane (through the hamburger menu). |
| Step 4 | Select the API services (such as Cloud Text-to-Speech, Cloud Speech-to-Text, and Dialogflow) to be enabled. |
| Step 5 | Click Enable to enable the selected API for the given Project ID. |

| Step 1 | In the GCP homepage, select IAM & Admin from the left pane (use the hamburger menu). |
|---|---|
| Step 2 | Select Service accounts which shows the list of your enabled services. |
| Step 3 | Select the service account for which the JSON key is to be generated. |
| Step 4 | Click the ellipsis menu on the right and click +Create Key . |
| Step 5 | Select JSON as Key type and then click Create . The key downloads. |

| Information | Resource |
|---|---|
| Sample VAV Application | See https://github.com/CiscoDevNet/cvp-sample-code/tree/master/CustomerVirtualAssistant . |
| Design Considerations | Design Considerations for Integrated Features > Virtual Agent–Voice Considerations section in the Solution Design Guide . |
| VAV configuration in Packaged CCE Deployment | Virtual Agent–Voice section in the Packaged CCE Administration and Configuration Guide . |
| VAV configuration in Unified CCE Deployment | Operations Console (NOAMP) section in the CVP Administration Guide . |
| TTS Prompt Cache Management and proxy setting for Speech Server | VVB Operations Guide . |
| Proxy settings for VXML Server | See the VXML Server Configuration > Proxy Settings in VXML Server for Virtual Agent–Voice section in the CVP Configuration Guide . |
| Configuration of Call Studio elements for VAV | The following chapters are in the CVP Element Specification Guide : Dialogflow Element DialogflowIntent Element DialogflowParam Element Transcribe Element |
| VAV Speech Configuration APIs | See VAV Speech Configuration section in the VVB Developer Guide . |

| Step 1 | Access the SBC console and modify the existing SIP profile configuration, which was used during the setup of both Virtual
                                       Agent-Voice and Agent Answers. For more information, see the Create a SIP Profile at the Dial-Peer Level in CUBE section in this Guide. |
|---|---|
| Step 2 | Run the following command to add the X-Cisco-Clusterid variable. This variable is added using a custom SIP header in the outgoing INVITE request as shown below: Syntax : request INVITE sip-header Call-Info add "X-Cisco-Clusterid : rtmsClusterId = <Regional Media Variable> ; wxccClusterId = <Cisco CCAI Services Variable>" The x-Cisco-Clusterid variable requires the following key values: rtmsClusterId : The value of the variable used for Regional Media data center. wxccClusterId : The value of the variable used for CCAI cloud services data center. Example : request INVITE sip-header Call-Info add "X-Cisco-Clusterid : rtmsClusterId = US1 ; wxccClusterId = US1" The following tables list the variables associated with regional media data centers located in different countries. If your
                                          region is not listed below, ensure that you select the nearest data center location applicable to your region. Important Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment. Table 1. Data Center Location - APAC S. No Country of Operation Regional Media Data Center Regional Media Variable Cisco CCAI Services Variable Default Regional Media Variable Default Cisco CCAI Services Variable 1 Australia Australia AS1 ANZ1 AS1 ANZ1 2 Indonesia Singapore SN1 ANZ1 AS1 ANZ1 3 Jordan United Kingdom UK1 EU1 UK1 EU1 4 Malaysia Singapore SN1 ANZ1 AS1 ANZ1 5 New Zealand Australia ANZ1 ANZ1 AS1 ANZ1 6 Philippines Singapore SN1 ANZ1 AS1 ANZ1 7 Singapore Singapore SN1 ANZ1 AS1 ANZ1 8 South Korea Japan JA1 JP1 AS1 ANZ1 9 Thailand Singapore SN1 ANZ1 AS1 ANZ1 10 Vietnam Singapore SN1 ANZ1 AS1 ANZ1 11 Japan Japan JA1 JP1 JA1 JP1 12 India India IN1 IN1 IN1 IN1 Table 2. Data Center Location - EMEA S. No Country of Operation Regional Media Data Center Regional Media Variable Cisco CCAI Services Variable Default Regional Media Variable Cisco CCAI Services Variable 1 Austria Germany GM1 EU2 GM1 EU2 2 Belgium Germany GM1 EU2 GM1 EU2 3 Bulgaria Germany GM1 EU2 GM1 EU2 4 Croatia Germany GM1 EU2 GM1 EU2 5 Cyprus Germany GM1 EU2 GM1 EU2 6 Czech Republic Germany GM1 EU2 GM1 EU2 7 Denmark Germany GM1 EU2 GM1 EU2 8 Estonia Germany GM1 EU2 GM1 EU2 9 Finland Germany GM1 EU2 GM1 EU2 10 France Germany GM1 EU2 GM1 EU2 11 Georgia Germany GM1 EU2 GM1 EU2 12 Germany Germany GM1 EU2 GM1 EU2 13 Greece Germany GM1 EU2 GM1 EU2 14 Hungary Germany GM1 EU2 GM1 EU2 15 Ireland Germany GM1 EU2 GM1 EU2 16 Italy Germany GM1 EU2 GM1 EU2 17 Latvia Germany GM1 EU2 GM1 EU2 18 Lithuania Germany GM1 EU2 GM1 EU2 19 Luxembourg Germany GM1 EU2 GM1 EU2 20 Malta Germany GM1 EU2 GM1 EU2 21 Netherlands Germany GM1 EU2 GM1 EU2 22 Norway Germany GM1 EU2 GM1 EU2 23 Poland Germany GM1 EU2 GM1 EU2 24 Portugal Germany GM1 EU2 GM1 EU2 25 Romania Germany GM1 EU2 GM1 EU2 26 Slovakia Germany GM1 EU2 GM1 EU2 27 Slovenia Germany GM1 EU2 GM1 EU2 28 Spain Germany GM1 EU2 GM1 EU2 29 Sweden Germany GM1 EU2 GM1 EU2 30 Switzerland Germany GM1 EU2 GM1 EU2 31 Ukraine Germany GM1 EU2 GM1 EU2 32 United Arab Emirates Germany GM1 EU2 GM1 EU2 33 Saudi Arabia United Kingdom UK1 EU1 UK1 EU1 34 South Africa United Kingdom UK1 EU1 UK1 EU1 35 South Sudan United Kingdom UK1 EU1 UK1 EU1 36 United Kingdom United Kingdom UK1 EU1 UK1 EU1 Table 3. Data Center Location - AMER S. No Country of Operation Regional Media Data Center Regional Media Variable Cisco CCAI Services Variable Default Regional Media Variable Default Cisco CCAI Services Variable 1 Argentina United States US1 US1 US1 US1 2 Aruba United States US1 US1 US1 US1 3 Bahamas United States US1 US1 US1 US1 4 Belize United States US1 US1 US1 US1 5 Bermuda United States US1 US1 US1 US1 6 Brazil United States US1 US1 US1 US1 7 Caymen Islands United States US1 US1 US1 US1 8 Chile United States US1 US1 US1 US1 9 Colombia United States US1 US1 US1 US1 10 Costa Rica United States US1 US1 US1 US1 11 Curacao United States US1 US1 US1 US1 12 Dominican Republic United States US1 US1 US1 US1 13 Ecuador United States US1 US1 US1 US1 14 El Salvador United States US1 US1 US1 US1 15 Guatemala United States US1 US1 US1 US1 16 Honduras United States US1 US1 US1 US1 18 Jamaica United States US1 US1 US1 US1 19 Mexico United States US1 US1 US1 US1 20 Nicaragua United States US1 US1 US1 US1 21 Panama United States US1 US1 US1 US1 22 Peru United States US1 US1 US1 US1 23 Puerto Rico United States US1 US1 US1 US1 24 Trinidad and Tobago United States US1 US1 US1 US1 25 United States United States US1 US1 US1 US1 26 Canada Canada CA1 CA1 CA1 CA1 | Important | Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment. | S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | Default Regional Media Variable | Default Cisco CCAI Services Variable | 1 | Australia | Australia | AS1 | ANZ1 | AS1 | ANZ1 | 2 | Indonesia | Singapore | SN1 | ANZ1 | AS1 | ANZ1 | 3 | Jordan | United Kingdom | UK1 | EU1 | UK1 | EU1 | 4 | Malaysia | Singapore | SN1 | ANZ1 | AS1 | ANZ1 | 5 | New Zealand | Australia | ANZ1 | ANZ1 | AS1 | ANZ1 | 6 | Philippines | Singapore | SN1 | ANZ1 | AS1 | ANZ1 | 7 | Singapore | Singapore | SN1 | ANZ1 | AS1 | ANZ1 | 8 | South Korea | Japan | JA1 | JP1 | AS1 | ANZ1 | 9 | Thailand | Singapore | SN1 | ANZ1 | AS1 | ANZ1 | 10 | Vietnam | Singapore | SN1 | ANZ1 | AS1 | ANZ1 | 11 | Japan | Japan | JA1 | JP1 | JA1 | JP1 | 12 | India | India | IN1 | IN1 | IN1 | IN1 | S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | Default Regional Media Variable | Cisco CCAI Services Variable | 1 | Austria | Germany | GM1 | EU2 | GM1 | EU2 | 2 | Belgium | Germany | GM1 | EU2 | GM1 | EU2 | 3 | Bulgaria | Germany | GM1 | EU2 | GM1 | EU2 | 4 | Croatia | Germany | GM1 | EU2 | GM1 | EU2 | 5 | Cyprus | Germany | GM1 | EU2 | GM1 | EU2 | 6 | Czech Republic | Germany | GM1 | EU2 | GM1 | EU2 | 7 | Denmark | Germany | GM1 | EU2 | GM1 | EU2 | 8 | Estonia | Germany | GM1 | EU2 | GM1 | EU2 | 9 | Finland | Germany | GM1 | EU2 | GM1 | EU2 | 10 | France | Germany | GM1 | EU2 | GM1 | EU2 | 11 | Georgia | Germany | GM1 | EU2 | GM1 | EU2 | 12 | Germany | Germany | GM1 | EU2 | GM1 | EU2 | 13 | Greece | Germany | GM1 | EU2 | GM1 | EU2 | 14 | Hungary | Germany | GM1 | EU2 | GM1 | EU2 | 15 | Ireland | Germany | GM1 | EU2 | GM1 | EU2 | 16 | Italy | Germany | GM1 | EU2 | GM1 | EU2 | 17 | Latvia | Germany | GM1 | EU2 | GM1 | EU2 | 18 | Lithuania | Germany | GM1 | EU2 | GM1 | EU2 | 19 | Luxembourg | Germany | GM1 | EU2 | GM1 | EU2 | 20 | Malta | Germany | GM1 | EU2 | GM1 | EU2 | 21 | Netherlands | Germany | GM1 | EU2 | GM1 | EU2 | 22 | Norway | Germany | GM1 | EU2 | GM1 | EU2 | 23 | Poland | Germany | GM1 | EU2 | GM1 | EU2 | 24 | Portugal | Germany | GM1 | EU2 | GM1 | EU2 | 25 | Romania | Germany | GM1 | EU2 | GM1 | EU2 | 26 | Slovakia | Germany | GM1 | EU2 | GM1 | EU2 | 27 | Slovenia | Germany | GM1 | EU2 | GM1 | EU2 | 28 | Spain | Germany | GM1 | EU2 | GM1 | EU2 | 29 | Sweden | Germany | GM1 | EU2 | GM1 | EU2 | 30 | Switzerland | Germany | GM1 | EU2 | GM1 | EU2 | 31 | Ukraine | Germany | GM1 | EU2 | GM1 | EU2 | 32 | United Arab Emirates | Germany | GM1 | EU2 | GM1 | EU2 | 33 | Saudi Arabia | United Kingdom | UK1 | EU1 | UK1 | EU1 | 34 | South Africa | United Kingdom | UK1 | EU1 | UK1 | EU1 | 35 | South Sudan | United Kingdom | UK1 | EU1 | UK1 | EU1 | 36 | United Kingdom | United Kingdom | UK1 | EU1 | UK1 | EU1 | S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | Default Regional Media Variable | Default Cisco CCAI Services Variable | 1 | Argentina | United States | US1 | US1 | US1 | US1 | 2 | Aruba | United States | US1 | US1 | US1 | US1 | 3 | Bahamas | United States | US1 | US1 | US1 | US1 | 4 | Belize | United States | US1 | US1 | US1 | US1 | 5 | Bermuda | United States | US1 | US1 | US1 | US1 | 6 | Brazil | United States | US1 | US1 | US1 | US1 | 7 | Caymen Islands | United States | US1 | US1 | US1 | US1 | 8 | Chile | United States | US1 | US1 | US1 | US1 | 9 | Colombia | United States | US1 | US1 | US1 | US1 | 10 | Costa Rica | United States | US1 | US1 | US1 | US1 | 11 | Curacao | United States | US1 | US1 | US1 | US1 | 12 | Dominican Republic | United States | US1 | US1 | US1 | US1 | 13 | Ecuador | United States | US1 | US1 | US1 | US1 | 14 | El Salvador | United States | US1 | US1 | US1 | US1 | 15 | Guatemala | United States | US1 | US1 | US1 | US1 | 16 | Honduras | United States | US1 | US1 | US1 | US1 | 18 | Jamaica | United States | US1 | US1 | US1 | US1 | 19 | Mexico | United States | US1 | US1 | US1 | US1 | 20 | Nicaragua | United States | US1 | US1 | US1 | US1 | 21 | Panama | United States | US1 | US1 | US1 | US1 | 22 | Peru | United States | US1 | US1 | US1 | US1 | 23 | Puerto Rico | United States | US1 | US1 | US1 | US1 | 24 | Trinidad and Tobago | United States | US1 | US1 | US1 | US1 | 25 | United States | United States | US1 | US1 | US1 | US1 | 26 | Canada | Canada | CA1 | CA1 | CA1 | CA1 |
| Important | Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment. |
| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | Default Regional Media Variable | Default Cisco CCAI Services Variable |
| 1 | Australia | Australia | AS1 | ANZ1 | AS1 | ANZ1 |
| 2 | Indonesia | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 3 | Jordan | United Kingdom | UK1 | EU1 | UK1 | EU1 |
| 4 | Malaysia | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 5 | New Zealand | Australia | ANZ1 | ANZ1 | AS1 | ANZ1 |
| 6 | Philippines | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 7 | Singapore | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 8 | South Korea | Japan | JA1 | JP1 | AS1 | ANZ1 |
| 9 | Thailand | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 10 | Vietnam | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 11 | Japan | Japan | JA1 | JP1 | JA1 | JP1 |
| 12 | India | India | IN1 | IN1 | IN1 | IN1 |
| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | Default Regional Media Variable | Cisco CCAI Services Variable |
| 1 | Austria | Germany | GM1 | EU2 | GM1 | EU2 |
| 2 | Belgium | Germany | GM1 | EU2 | GM1 | EU2 |
| 3 | Bulgaria | Germany | GM1 | EU2 | GM1 | EU2 |
| 4 | Croatia | Germany | GM1 | EU2 | GM1 | EU2 |
| 5 | Cyprus | Germany | GM1 | EU2 | GM1 | EU2 |
| 6 | Czech Republic | Germany | GM1 | EU2 | GM1 | EU2 |
| 7 | Denmark | Germany | GM1 | EU2 | GM1 | EU2 |
| 8 | Estonia | Germany | GM1 | EU2 | GM1 | EU2 |
| 9 | Finland | Germany | GM1 | EU2 | GM1 | EU2 |
| 10 | France | Germany | GM1 | EU2 | GM1 | EU2 |
| 11 | Georgia | Germany | GM1 | EU2 | GM1 | EU2 |
| 12 | Germany | Germany | GM1 | EU2 | GM1 | EU2 |
| 13 | Greece | Germany | GM1 | EU2 | GM1 | EU2 |
| 14 | Hungary | Germany | GM1 | EU2 | GM1 | EU2 |
| 15 | Ireland | Germany | GM1 | EU2 | GM1 | EU2 |
| 16 | Italy | Germany | GM1 | EU2 | GM1 | EU2 |
| 17 | Latvia | Germany | GM1 | EU2 | GM1 | EU2 |
| 18 | Lithuania | Germany | GM1 | EU2 | GM1 | EU2 |
| 19 | Luxembourg | Germany | GM1 | EU2 | GM1 | EU2 |
| 20 | Malta | Germany | GM1 | EU2 | GM1 | EU2 |
| 21 | Netherlands | Germany | GM1 | EU2 | GM1 | EU2 |
| 22 | Norway | Germany | GM1 | EU2 | GM1 | EU2 |
| 23 | Poland | Germany | GM1 | EU2 | GM1 | EU2 |
| 24 | Portugal | Germany | GM1 | EU2 | GM1 | EU2 |
| 25 | Romania | Germany | GM1 | EU2 | GM1 | EU2 |
| 26 | Slovakia | Germany | GM1 | EU2 | GM1 | EU2 |
| 27 | Slovenia | Germany | GM1 | EU2 | GM1 | EU2 |
| 28 | Spain | Germany | GM1 | EU2 | GM1 | EU2 |
| 29 | Sweden | Germany | GM1 | EU2 | GM1 | EU2 |
| 30 | Switzerland | Germany | GM1 | EU2 | GM1 | EU2 |
| 31 | Ukraine | Germany | GM1 | EU2 | GM1 | EU2 |
| 32 | United Arab Emirates | Germany | GM1 | EU2 | GM1 | EU2 |
| 33 | Saudi Arabia | United Kingdom | UK1 | EU1 | UK1 | EU1 |
| 34 | South Africa | United Kingdom | UK1 | EU1 | UK1 | EU1 |
| 35 | South Sudan | United Kingdom | UK1 | EU1 | UK1 | EU1 |
| 36 | United Kingdom | United Kingdom | UK1 | EU1 | UK1 | EU1 |
| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | Default Regional Media Variable | Default Cisco CCAI Services Variable |
| 1 | Argentina | United States | US1 | US1 | US1 | US1 |
| 2 | Aruba | United States | US1 | US1 | US1 | US1 |
| 3 | Bahamas | United States | US1 | US1 | US1 | US1 |
| 4 | Belize | United States | US1 | US1 | US1 | US1 |
| 5 | Bermuda | United States | US1 | US1 | US1 | US1 |
| 6 | Brazil | United States | US1 | US1 | US1 | US1 |
| 7 | Caymen Islands | United States | US1 | US1 | US1 | US1 |
| 8 | Chile | United States | US1 | US1 | US1 | US1 |
| 9 | Colombia | United States | US1 | US1 | US1 | US1 |
| 10 | Costa Rica | United States | US1 | US1 | US1 | US1 |
| 11 | Curacao | United States | US1 | US1 | US1 | US1 |
| 12 | Dominican Republic | United States | US1 | US1 | US1 | US1 |
| 13 | Ecuador | United States | US1 | US1 | US1 | US1 |
| 14 | El Salvador | United States | US1 | US1 | US1 | US1 |
| 15 | Guatemala | United States | US1 | US1 | US1 | US1 |
| 16 | Honduras | United States | US1 | US1 | US1 | US1 |
| 18 | Jamaica | United States | US1 | US1 | US1 | US1 |
| 19 | Mexico | United States | US1 | US1 | US1 | US1 |
| 20 | Nicaragua | United States | US1 | US1 | US1 | US1 |
| 21 | Panama | United States | US1 | US1 | US1 | US1 |
| 22 | Peru | United States | US1 | US1 | US1 | US1 |
| 23 | Puerto Rico | United States | US1 | US1 | US1 | US1 |
| 24 | Trinidad and Tobago | United States | US1 | US1 | US1 | US1 |
| 25 | United States | United States | US1 | US1 | US1 | US1 |
| 26 | Canada | Canada | CA1 | CA1 | CA1 | CA1 |
| Step 3 | To ensure connection with the Cisco Finesse gadget, you must enable the POD.ID Extended Call Context (ECC) variable in Unified CCE Configuration Manager > List Tools > Expanded Call Variables List . Note After you enable the POD.ID, you must restart the VRU PG during non-production time or a scheduled maintenance window for
                                                      the changes to take full effect. | Note | After you enable the POD.ID, you must restart the VRU PG during non-production time or a scheduled maintenance window for
                                                      the changes to take full effect. |
| Note | After you enable the POD.ID, you must restart the VRU PG during non-production time or a scheduled maintenance window for
                                                      the changes to take full effect. |

| Important | Ensure that you input the values of the variable exactly as they are specified in the tables below. These values are case
                                                      sensitive. Any discrepancies in the values could potentially lead to data loss or system downtime. Therefore, it is crucial
                                                      to verify these values before implementing them in a production environment. |
|---|---|

| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | Default Regional Media Variable | Default Cisco CCAI Services Variable |
|---|---|---|---|---|---|---|
| 1 | Australia | Australia | AS1 | ANZ1 | AS1 | ANZ1 |
| 2 | Indonesia | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 3 | Jordan | United Kingdom | UK1 | EU1 | UK1 | EU1 |
| 4 | Malaysia | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 5 | New Zealand | Australia | ANZ1 | ANZ1 | AS1 | ANZ1 |
| 6 | Philippines | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 7 | Singapore | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 8 | South Korea | Japan | JA1 | JP1 | AS1 | ANZ1 |
| 9 | Thailand | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 10 | Vietnam | Singapore | SN1 | ANZ1 | AS1 | ANZ1 |
| 11 | Japan | Japan | JA1 | JP1 | JA1 | JP1 |
| 12 | India | India | IN1 | IN1 | IN1 | IN1 |

| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | Default Regional Media Variable | Cisco CCAI Services Variable |
|---|---|---|---|---|---|---|
| 1 | Austria | Germany | GM1 | EU2 | GM1 | EU2 |
| 2 | Belgium | Germany | GM1 | EU2 | GM1 | EU2 |
| 3 | Bulgaria | Germany | GM1 | EU2 | GM1 | EU2 |
| 4 | Croatia | Germany | GM1 | EU2 | GM1 | EU2 |
| 5 | Cyprus | Germany | GM1 | EU2 | GM1 | EU2 |
| 6 | Czech Republic | Germany | GM1 | EU2 | GM1 | EU2 |
| 7 | Denmark | Germany | GM1 | EU2 | GM1 | EU2 |
| 8 | Estonia | Germany | GM1 | EU2 | GM1 | EU2 |
| 9 | Finland | Germany | GM1 | EU2 | GM1 | EU2 |
| 10 | France | Germany | GM1 | EU2 | GM1 | EU2 |
| 11 | Georgia | Germany | GM1 | EU2 | GM1 | EU2 |
| 12 | Germany | Germany | GM1 | EU2 | GM1 | EU2 |
| 13 | Greece | Germany | GM1 | EU2 | GM1 | EU2 |
| 14 | Hungary | Germany | GM1 | EU2 | GM1 | EU2 |
| 15 | Ireland | Germany | GM1 | EU2 | GM1 | EU2 |
| 16 | Italy | Germany | GM1 | EU2 | GM1 | EU2 |
| 17 | Latvia | Germany | GM1 | EU2 | GM1 | EU2 |
| 18 | Lithuania | Germany | GM1 | EU2 | GM1 | EU2 |
| 19 | Luxembourg | Germany | GM1 | EU2 | GM1 | EU2 |
| 20 | Malta | Germany | GM1 | EU2 | GM1 | EU2 |
| 21 | Netherlands | Germany | GM1 | EU2 | GM1 | EU2 |
| 22 | Norway | Germany | GM1 | EU2 | GM1 | EU2 |
| 23 | Poland | Germany | GM1 | EU2 | GM1 | EU2 |
| 24 | Portugal | Germany | GM1 | EU2 | GM1 | EU2 |
| 25 | Romania | Germany | GM1 | EU2 | GM1 | EU2 |
| 26 | Slovakia | Germany | GM1 | EU2 | GM1 | EU2 |
| 27 | Slovenia | Germany | GM1 | EU2 | GM1 | EU2 |
| 28 | Spain | Germany | GM1 | EU2 | GM1 | EU2 |
| 29 | Sweden | Germany | GM1 | EU2 | GM1 | EU2 |
| 30 | Switzerland | Germany | GM1 | EU2 | GM1 | EU2 |
| 31 | Ukraine | Germany | GM1 | EU2 | GM1 | EU2 |
| 32 | United Arab Emirates | Germany | GM1 | EU2 | GM1 | EU2 |
| 33 | Saudi Arabia | United Kingdom | UK1 | EU1 | UK1 | EU1 |
| 34 | South Africa | United Kingdom | UK1 | EU1 | UK1 | EU1 |
| 35 | South Sudan | United Kingdom | UK1 | EU1 | UK1 | EU1 |
| 36 | United Kingdom | United Kingdom | UK1 | EU1 | UK1 | EU1 |

| S. No | Country of Operation | Regional Media Data Center | Regional Media Variable | Cisco CCAI Services Variable | Default Regional Media Variable | Default Cisco CCAI Services Variable |
|---|---|---|---|---|---|---|
| 1 | Argentina | United States | US1 | US1 | US1 | US1 |
| 2 | Aruba | United States | US1 | US1 | US1 | US1 |
| 3 | Bahamas | United States | US1 | US1 | US1 | US1 |
| 4 | Belize | United States | US1 | US1 | US1 | US1 |
| 5 | Bermuda | United States | US1 | US1 | US1 | US1 |
| 6 | Brazil | United States | US1 | US1 | US1 | US1 |
| 7 | Caymen Islands | United States | US1 | US1 | US1 | US1 |
| 8 | Chile | United States | US1 | US1 | US1 | US1 |
| 9 | Colombia | United States | US1 | US1 | US1 | US1 |
| 10 | Costa Rica | United States | US1 | US1 | US1 | US1 |
| 11 | Curacao | United States | US1 | US1 | US1 | US1 |
| 12 | Dominican Republic | United States | US1 | US1 | US1 | US1 |
| 13 | Ecuador | United States | US1 | US1 | US1 | US1 |
| 14 | El Salvador | United States | US1 | US1 | US1 | US1 |
| 15 | Guatemala | United States | US1 | US1 | US1 | US1 |
| 16 | Honduras | United States | US1 | US1 | US1 | US1 |
| 18 | Jamaica | United States | US1 | US1 | US1 | US1 |
| 19 | Mexico | United States | US1 | US1 | US1 | US1 |
| 20 | Nicaragua | United States | US1 | US1 | US1 | US1 |
| 21 | Panama | United States | US1 | US1 | US1 | US1 |
| 22 | Peru | United States | US1 | US1 | US1 | US1 |
| 23 | Puerto Rico | United States | US1 | US1 | US1 | US1 |
| 24 | Trinidad and Tobago | United States | US1 | US1 | US1 | US1 |
| 25 | United States | United States | US1 | US1 | US1 | US1 |
| 26 | Canada | Canada | CA1 | CA1 | CA1 | CA1 |

| Note | After you enable the POD.ID, you must restart the VRU PG during non-production time or a scheduled maintenance window for
                                                      the changes to take full effect. |
|---|---|