---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-febeecffd0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/ucce_b_features-guide-1261/ucce_m_dialogflow_cx-1261.html
retrieved_at: 2026-08-16T20:12:59.075984+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Virtual Agent–Voice for Dialogflow CX

## Chapter: Virtual Agent–Voice for Dialogflow CX

# Virtual Agent–Voice for Dialogflow CX

## Overview

Virtual Agent–Voice for Dialogflow CX leverages Google's Dialogflow CX service that allows designing virtual voice agents
                           and creating and connecting complex IVR call flows.

Using Google Dialogflow CX, multiple agents can be created under the same Project ID and can be accessed and managed for different
                           lines of business with a single Google account. For more information, refer to the Google Dialogflow CX documentation at https://cloud.google.com/dialogflow/cx/docs .

The DialogflowCX element of Cisco Unified Call Studio is used to engage Google's Dialogflow CX services.

Only U Law codec is supported.

This feature is available with Cisco subscription services only.

The DialogflowCX element works both with Cisco DTMF and Nuance ASR adaptors.

## Prerequisites

For supported minimum versions, refer to the Cisco Unified Customer Voice Portal > New Features > Virtual Agent–Voice for Dialogflow CX section in the Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1) .

To configure Google Dialogflow CX, you should have completed the following procedures:

The customer's CX Agent ID and GCP Project ID is created. For more information, refer to Google documentation at https://dialogflow.cloud.google.com/cx/projects .

Assessment to Quality (A2Q) process for Contact Center AI (CCAI) is completed and Cisco subscription Flex SKU for CX is procured.

Customer's GCP project ID and Cisco's GCP partner projects are mapped.

Control Hub credentials and Hybrid Org are generated.

For assistance, you can contact the Cisco TAC team.

CX conversational profile ID is created using credentials provided by Cisco via email. For details, see Create a Conversation Profile using Google Cloud SDK .

This conversation profile URL is to be used for creating the CCAI configuration.

Cisco Unified CVP and Cisco VVB are configured:

Date and time in CVP, VVB, and proxy are synchronized with a common NTP server.

Access to DNS server is configured in CVP and VVB.

For more information on NTP and DNS server configurations in CVP, refer to the Microsoft Windows platform documentation.

For more information on NTP and DNS server configurations in VVB, refer to the Command Line Interface Reference Guide for Cisco Unified Communications Solutions at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Port 443 and HTTP/2 are enabled in the proxy and firewall.

The new Cisco Unified Call Studio application with the DialogflowCX element is deployed. You can download and install the latest patch from https://software.cisco.com/download/specialrelease/c359e375005563ceec2081c9151b482e .

For details of the DialogflowCX element , refer to the Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1) guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

### What to do next

Configure Google Dialogflow CX Agent with Cisco Unified CCE solution.

## Configuration Task Flow

Task flow for configuring Google Dialogflow CX Agent with Cisco Unified CCE solution.

Step 1

Ensure that the Cloud Connect publisher and subscriber nodes are installed.

For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Step 2

Configure Cloud Connect with VVBs in the Operations Console (NOAMP for Cisco Unified CCE and CCE Admin for Packaged CCE).

Step 3

Create Contact Center AI (CCAI) configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services.

For detailed steps to set up Integration Connectors, see the Set Up Integration Connectors for Contact Center solutions article.

For detailed steps to create CCAI configuration, see the Create a Contact Center AI configuration article. This default config can be used for accessing multiple AI services on multiple devices.

Step 4

View the default CCAI configuration (created in step 1). Sync, if required, in the CVP Operations Console (NOAMP for Cisco
                                       Unified CCE and CCE Admin for Packaged CCE).

For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Cisco-Billed AI Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 5

Design Google Dialogflow CX Agents. For more information, refer to Google documentation at https://dialogflow.cloud.google.com/cx/projects .

Step 6

Configure a welcome event for all Google Dialogflow CX Agents. For details, see Create a Welcome Event .

To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured at the CX Agent to start the flow.

For further assistance, contact the Cisco TAC team.

### Create a Conversation Profile using Google Cloud SDK

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

Under the Headers section, add the following key values for Authorization  and Content-type:

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

In a new browser tab, open https://agentassist.cloud.google.com/ and select the appropriate project. The list of profiles is displayed.

Step 8

Click the copy icon next to the profile ID to be used. Copy the profile URL in the following format: projects/<project_ID>/locations/<location>/conversationProfiles/<profile ID>.

You can use this profile URL while creating the Control Hub configuration.

### Create a Welcome Event

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

| Note | Only U Law codec is supported. This feature is available with Cisco subscription services only. The DialogflowCX element works both with Cisco DTMF and Nuance ASR adaptors. |
|---|---|

| Step 1 | Ensure that the Cloud Connect publisher and subscriber nodes are installed. For more information, see the Install Cloud Connect section in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
|---|---|
| Step 2 | Configure Cloud Connect with VVBs in the Operations Console (NOAMP for Cisco Unified CCE and CCE Admin for Packaged CCE). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Integration > Cloud Connect > Configure CVP or VVB Devices
                                          for Cloud Connect section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 3 | Create Contact Center AI (CCAI) configuration in Cisco Webex Control Hub at https://admin.webex.com . A CCAI configuration leverages CCAI Connectors to invoke the CCAI services. For detailed steps to set up Integration Connectors, see the Set Up Integration Connectors for Contact Center solutions article. For detailed steps to create CCAI configuration, see the Create a Contact Center AI configuration article. This default config can be used for accessing multiple AI services on multiple devices. |
| Step 4 | View the default CCAI configuration (created in step 1). Sync, if required, in the CVP Operations Console (NOAMP for Cisco
                                       Unified CCE and CCE Admin for Packaged CCE). For details, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Contact Center AI > Configuration for Cisco-Billed AI Services section in the Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 5 | Design Google Dialogflow CX Agents. For more information, refer to Google documentation at https://dialogflow.cloud.google.com/cx/projects . |
| Step 6 | Configure a welcome event for all Google Dialogflow CX Agents. For details, see Create a Welcome Event . Note To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured at the CX Agent to start the flow. For further assistance, contact the Cisco TAC team. | Note | To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured at the CX Agent to start the flow. For further assistance, contact the Cisco TAC team. |
| Note | To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured at the CX Agent to start the flow. For further assistance, contact the Cisco TAC team. |

| Note | To override the default welcome event, provide the element data event_name in the DialogflowCX element. The same name must be configured at the CX Agent to start the flow. For further assistance, contact the Cisco TAC team. |
|---|---|

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
| Step 6 | Create the conversation profile using REST API for Dialogflow by using Postman: In the Postman workspace, select the method as POST . In the URL field, add the address in the following format after replacing the regionId and projectId appropriately: https://<regionId>-dialogflow.googleapis.com/v2beta1/projects/<projectId>/locations/<regionId>/conversationProfiles Under the Headers section, add the following key values for Authorization  and Content-type: Authorization: Bearer <token generated with the Google command> Content-type: application/json Under the Body section, select raw . From the last dropdown, select JSON . In the code space, enter the following code (after replacing the regionId , projectId , and agentId in the agent tag with actual values): {
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
| Step 7 | In a new browser tab, open https://agentassist.cloud.google.com/ and select the appropriate project. The list of profiles is displayed. |
| Step 8 | Click the copy icon next to the profile ID to be used. Copy the profile URL in the following format: projects/<project_ID>/locations/<location>/conversationProfiles/<profile ID>. You can use this profile URL while creating the Control Hub configuration. |

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
| Step 9 | Save the changes. |