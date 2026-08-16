---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-86c345c983
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_features-guide-1262/ucce_b_features-guide-1261_chapter_0100.html
retrieved_at: 2026-08-16T20:10:48.245338+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: April 30, 2025

Chapter: Call Transcript

## Chapter: Call Transcript

# Call Transcript

## Feature Overview

Call Transcript is an Enterprise Voice Assistant that provides advanced speech recognition and transcription to the Contact Center solution.
                           When Call Transcript is integrated with the Contact Center solution, agents can view the live transcript of the call on their desktop. This transcript
                           enables the agent to wrap-up the call quickly and ensures that the wrap-up notes are accurate and readily available for future
                           reference.

This also enhances agent experience, reduces agent workload, and reduces the cost of Contact Center operations. The reduced
                           wrap-up time increases agent productivity and makes tangible impact to the business.

## Capabilities

The following benefits are derived when Call Transcript is integrated with the Contact Center solution:

Availability of the call transcript with the agent on the desktop.

Faster turn-around time to wrap-up the call by the agent.

Agents can quickly prepare notes and summary for quick reference.

Option to configure Hot words for easy reference.

Search option on the transcript and notes to easily find relevant information.

Quicker issue resolution.

## Getting Started

This section explains the prerequisites, configuration task flow, and the documentation resources for Call Transcript. The
                           call flow and design considerations for the Call Transcript feature are described in the Unified CCE Solutions Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

### Prerequisities

CUBE or Ingress gateway is required for sending media and SIP signals to the public IP of the Call Transcript service. For
                              supported IOS versions for Call Transcript , see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Configuration Task Flow

Step

Component

Configuration

Link

Step 1

Call Transcript Service

Create a tenant for the customer.

Refer section Create Manual Tenant in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

Step 2

CUCM

Configure SIP trunk from CUCM to CVP (CVP is the recording server).

Refer section Configure the SIP Trunk from CUCM to Recording Server in Configuration Guide for Cisco Unified Customer Voice Portal .

Enable agent phones for NBR media forking (gateway-preferred forking).

Refer section Gateway Setup for Network-based Recording in Configuration Guide for Cisco Unified Customer Voice Portal ..

Step 3

CUBE

Configure CUBE to route the calls coming from CVP to the Call Transcript Service.

Refer section Configure CUBE to Route Calls from CVP to Call Transcript in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

Step 4

Cloud Connect

Onboard the tenant created in Step 1 into the current deployment.

Refer section Set CloudConnect evapoint config in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

Step 5

Unified CVP

Integrate Cloud Connect from Cisco CVP NOAMP.

Refer section Operations Console > Integration in Administration Guide for Cisco Unified Customer Voice Portal .

Import Cloud Connect certificate to CVP keystore.

Refer section Operations Console > Integration in Administration Guide for Cisco Unified Customer Voice Portal .

Step 6

Unified CCE

Configure ICM / CCE.

Refer section Configuration for Call Transcript Integration in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

Step 7

Cisco Finesse

Configure Cloud Connect.

Refer section Configure Cloud Connect Server Settings in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

Configure Highlights.

Refer section Highlight Custom Keywords in Call Transcript Gadget in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

Configure Gadgets.

Refer section Add Call Transcript Gadget in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

### Documentation Resources

The following table lists the reference documents for Call Transcript :

Information

Resource

Design Considerations and Call Flow

Unified CCE Solutions Design Guide , https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

Pre-Install Setup

Unified CCE Solutions Features Guide , Prerequisities

Cloud Connect Configurations

Unified CCE Configuration Guide , https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

CVP Integrations

Unified CVP Administration Guide , https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html

Desktop Application

Cisco Finesse User Guide , https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html

| Step | Component | Configuration | Link |
|---|---|---|---|
| Step 1 | Call Transcript Service | Create a tenant for the customer. | Refer section Create Manual Tenant in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise . |
| Step 2 | CUCM | Configure SIP trunk from CUCM to CVP (CVP is the recording server). | Refer section Configure the SIP Trunk from CUCM to Recording Server in Configuration Guide for Cisco Unified Customer Voice Portal . |
| Enable agent phones for NBR media forking (gateway-preferred forking). | Refer section Gateway Setup for Network-based Recording in Configuration Guide for Cisco Unified Customer Voice Portal .. |
| Step 3 | CUBE | Configure CUBE to route the calls coming from CVP to the Call Transcript Service. | Refer section Configure CUBE to Route Calls from CVP to Call Transcript in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise . |
| Step 4 | Cloud Connect | Onboard the tenant created in Step 1 into the current deployment. | Refer section Set CloudConnect evapoint config in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide . |
| Step 5 | Unified CVP | Integrate Cloud Connect from Cisco CVP NOAMP. | Refer section Operations Console > Integration in Administration Guide for Cisco Unified Customer Voice Portal . |
| Import Cloud Connect certificate to CVP keystore. | Refer section Operations Console > Integration in Administration Guide for Cisco Unified Customer Voice Portal . |
| Step 6 | Unified CCE | Configure ICM / CCE. | Refer section Configuration for Call Transcript Integration in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise . |
| Step 7 | Cisco Finesse | Configure Cloud Connect. | Refer section Configure Cloud Connect Server Settings in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise . |
| Configure Highlights. | Refer section Highlight Custom Keywords in Call Transcript Gadget in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise . |
| Configure Gadgets. | Refer section Add Call Transcript Gadget in Configuration Guide for Cisco Unified ICM/Contact Center Enterprise . |
|  |  |

| Information | Resource |
|---|---|
| Design Considerations and Call Flow | Unified CCE Solutions Design Guide , https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html |
| Pre-Install Setup | Unified CCE Solutions Features Guide , Prerequisities |
| Cloud Connect Configurations | Unified CCE Configuration Guide , https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
| CVP Integrations | Unified CVP Administration Guide , https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html |
| Desktop Application | Cisco Finesse User Guide , https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html |