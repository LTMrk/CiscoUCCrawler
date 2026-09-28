---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-release-gui-c509984c0c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/release/guide/rcct_b_cce-solutions-rns-12-6-2/ccvp_m_1262-cisco-unified-customer-voice-portal.html
retrieved_at: 2026-08-16T19:37:24.939345+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

# Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

Updated: February 27, 2026

Chapter: Cisco Unified Customer Voice Portal

## Chapter: Cisco Unified Customer Voice Portal

# Cisco Unified Customer Voice Portal

## New Features

### Ability to Host Custom Code Applications

CVP (along with it 12.6(2) ES 18 ) supports hosting and running custom code applications. You can easily migrate existing CVP applications, whether hosted locally
                              or on remote servers, to other remote servers without disrupting ongoing calls using VXML and Call servers. This allows you
                              to separate your custom code from the core VXML application, allowing easier identification and isolation of unexpected issues.
                              Overall, it boosts the computing power and scalability for the components involved.

For more information on how to install and configure custom code using remote server, refer to the following documents:

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal

Configuration Guide for Cisco Unified Customer Voice Portal

### Regionalized Media Support

Contact Center Enterprise (CCE) now extends support for regionalized media to all supported data center locations. Regionalized
                              media allows customers and agent media (audio and SIP signaling) to remain local to a geographic region, regardless of the
                              location of the CCE tenant or home location resides. Keeping media local to a region reduces latency, improves audio quality,
                              meets in-country data residency security compliance requirements, and allows for unique regionalized configurations in multinational
                              deployments.

For example, if the location of the CCE tenant is based in the United States (US) region, calls within the US are localized
                              there, European calls are handled in Europe, and Asian calls are managed in Asia. Only control signals are transmitted from
                              the media endpoint to the US region.

Regional media is available at no additional cost for all WxCCE and on-prem deployment customers who opt for Cisco CCAI services.
                              Ensure that your assigned tenant has been enabled for enhanced media platform capability. For more information, refer to the Solution Design Guide for Cisco Contact Center Enterprise .

### Custom SIP header passing to VXML server

You can parse selected SIP headers (custom headers) when using standalone deployment model and SIP trunk termination on VVB.
                              This feature provides you with a great amount of flexibility when sending user-data or context from third-party Automatic
                              Call Distributor (ACD) or service provider to a VXML server for processing. You can send and receive SIP headers only on the
                              initial SIP Invite message and not on the reinvite messages.

For more information, see Custom SIP header passing to a VXML server in Solution Design Guide for Cisco Unified Contact Center Enterprise and Solution Design Guide for Cisco Packaged Contact Center Enterprise.

### Virtual Agent–Voice via Cloud-Based Connector

#### Hybrid IVR with VAV via Cloud-Based Connector

This feature is available to customers on request and only after necessary review and agreement. Please contact your Partner
                                             or Customer Success Manager or Cisco Support for details.

Virtual Agent–Voice (VAV) via cloud-based connector leverages Cisco's cloud-based Artificial Intelligence (AI) and Natural
                                 Language Understanding (NLU) services for designing virtual voice agents and creating complex IVR call flows.

The Webex CCAI services platform enables integration with speech-based services from different vendors. On the premises side,
                                 VVB interfaces with the Orchestrator service and connects to the CCAI service via cloud-based connector.

With Cisco's Hybrid IVR functionality, customers who have on-premises applications can leverage their traditional ASR/TTS/CRM
                                 integrations, along with cloud-based Dilaogflow CX AI capabilities. They can select a few nodes or sections of their application
                                 to be processed in the cloud and few nodes to be processed on-premises. For example, in an application, OTP generation can
                                 be performed on-premises, while other tasks can be processed in the cloud.

The above services are enabled through the VirtualAgentVoice element of Cisco Unified Call Studio. For more information, see the VirtualAgentVoice chapter in the Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2) guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

For details on how to configure VAV via cloud-based connector and Hybrid IVR, refer to the following documents:

Virtual Agent–Voice > VAV via Cloud-Based Connector section in the Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2) guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

Virtual Agent–Voice > VAV via Cloud-Based Connector section in the Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2) guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/series.html#%7Etab-documents .

### Specific License Reservation (SLR)

CVP devices registered with Smart Licenses share device information at regular intervals with Cisco Smart Software Manager
                                 (CSSM). However, the devices that are deployed in highly secure networks must not share this information outside the network.
                                 Cisco offers specific license reservation as an on-request configuration for these CVP devices.

For details on how to reserve specific licenses for a device, see the Cisco Unified Customer Voice Portal > Operations Console (NOAMP) > Smart Licensing > Specific License Reservation (SLR) section in the following guide:

Administration Guide for Cisco Unified Customer Voice Portal 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

### Partial Response in Virtual Agent—Voice (ES01 Update)

The partial response feature addresses a key aspect of the user experience by engaging a user during a call. It plays an interim
                              message while the Webhook response takes time to process in the background.

An API or Webhook request to an AI application (Dialogflow CX) that requires several parameters often takes longer to receive
                              the correct response. An end user is kept absolutely silent while an API request is being processed. There is a chance that
                              the end-user will hang up the phone. To avoid this, an intermediate response must be sent to the end user informing them that
                              their request is currently being processed.

This feature allows an AI bot developer to create a static response that may be conveyed to the end user while their inquiry
                              is still being processed. In the CX bot agent, static messages can be configured for up to 30 seconds. Once the final API
                              response is received, the flow can be continued.

For configurations instructions, see Configure Partial Response in Dialogflow CX .

To configure this feature, you must upgrade Cisco VVB to Release 12.6(2) ES01 or above. You can access the 12.6(2) ES01 Release
                              and Readme from Virtualized Voice Browser Engineering Specials for Release 12.6(2) .

## Updated Features

### TTS Server Status Update

In this release, you can retrieve the status of the TTS server (Reachable or Unreachable) by invoking the following REST API
                              call:

```
https://<IP address> /adminapi/ttsServer/
```

### DecryptKeystoreUtil.bat Utility Update

In this release, you can retrieve the keystore password by running the DecryptKeystoreUtil.bat file stored in the %CVP_HOME%\bin folder.

## Important Notes

The following device/feature are supported in this release:

Cisco Catalyst 8000 series

Private Network Access (PNA) Compatibility in Chrome browser

If the Packaged CCE is not in 12.6(2) release, then the following ES has to be applied in Packaged CCE, before upgrading CVP
                           to 12.6(2).

ES 24 in 12.5(2)

ES 144 in 12.5(1)

## Third Party Software Impacts

For the list of third-party softwares, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.

| Note | This feature is available to customers on request and only after necessary review and agreement. Please contact your Partner
                                             or Customer Success Manager or Cisco Support for details. |
|---|---|