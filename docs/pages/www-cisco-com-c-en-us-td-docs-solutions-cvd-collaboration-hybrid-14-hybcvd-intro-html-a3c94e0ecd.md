---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-hybrid-14-hybcvd-intro-html-a3c94e0ecd
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/hybrid/14/hybcvd/intro.html
retrieved_at: 2026-08-16T18:23:45.847631+00:00
---

Preferred Architecture for Cisco Webex Hybrid Services, CVD

# Preferred Architecture for Cisco Webex Hybrid Services, CVD

Updated: April 27, 2020

Chapter: Introduction

## Chapter: Introduction

- Architectural Overview

- Collaboration Endpoints

- Webex Core Services

## Introduction

Revised: October 22, 2021

The Preferred Architecture (PA) for Webex Hybrid Services is a Cisco Validated Design (CVD) built upon the foundation of the PA for Cisco Collaboration Enterprise on-premises deployments. It requires many of the same products and infrastructure components as well as the architecture and planning incorporated in the PA for on-premises deployments. Therefore we expect you to follow and implement the latest version of the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments , available at https://www.cisco.com/go/pa , prior to deploying the PA for Webex Hybrid Services.

As part of implementing the PA for Webex Hybrid Services, there are a number of products and integrations covered in the latest version of the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments that overlap with, and thus are not part of, the PA for Webex Hybrid Services. The areas of overlap include Cisco Meeting Server, Cisco Unified Communications Manager IM and Presence Service, and Cisco Jabber. This does not mean that these products and services cannot be deployed in an environment with Webex Hybrid Services, but that this PA for Webex Hybrid Services will not discuss or treat any design considerations around these on-premises products and services when they overlap with those included in the Webex Hybrid Services solution.

## Architectural Overview

The PA for Webex Hybrid Services provides end-to-end collaboration targeted for deployments where a collaboration solution based on Cisco Unified Communications Manager (Unified CM) has been deployed. This architecture incorporates high availability for critical applications. The consistent user experience provided by the overall architecture facilitates quick user adoption. Additionally, the architecture supports an advanced set of collaboration services that extend to mobile workers, partners, and customers through the following key services:

- Voice and video communications

- Messaging

- Meetings that incorporate high-definition video, web conferencing, and content sharing capabilities

- Services for mobile and remote workers

The PA for Webex Hybrid Services, shown in Figure 1-1 , provides highly available and centralized on-premises and cloud services. These services extend easily to remote offices and mobile workers, providing availability of critical services even if communication to headquarters is lost. Centralized on-premises and cloud-based services also simplify management and administration of an organization's collaboration deployment.

Figure 1-1 Preferred Architecture for Webex Hybrid Services

Table 1-1 lists the components in this architecture. For simplicity, the components are grouped into modules to help categorize and define their roles. The content in this guide is organized in the same modules.

Table 1-1 Components of the Preferred Architecture for Webex Hybrid Services

Collaboration Endpoints

Cisco IP Phones, Webex Desk and Room Devices, and Webex App

Enable real-time message, meeting, and voice/video communications for users

Webex Core Services

Webex Control Hub

Web portal that enables provisioning and management of enterprise Webex App users and services; registration of endpoints, clients, and Expressway-C Connector Host to Webex; and Expressway Connector upgrades

Webex Messaging

Provides persistent messaging and content sharing in 1:1 and group-based spaces

Webex Meetings

Provides audio/video meetings, with content sharing and web conferencing capabilities for meetings

Cisco Expressway-C Connector Host Management Connector

Enables connectors hosted on Expressway-C to be managed by the Webex Control Hub

Webex Hybrid Directory Service

Cisco Directory Connector

Provides directory synchronization between Microsoft Active Directory and Webex

Microsoft Active Directory

Provides the full list of corporate resources and users and their attributes

Webex Hybrid Calendar Service

Cisco Expressway-C Connector Host Calendar Connector

Provides integration between the enterprise calendaring application and Webex

Microsoft Exchange

Provides corporate calendaring services

Webex Hybrid Call Service

Cisco Unified Communications Manager (Unified CM)

Provides endpoint registration, call processing, and media resource management

Webex Device Connector

Provides integration between on-premises call processing services and room systems registered as Webex devices

Cisco Expressway-C and Expressway-E

Enables interoperability and firewall traversal with Webex

High Availability

The PA for Webex Hybrid Services provides high availability for all deployed on-premises applications by means of the underlying clustering mechanism present in all Cisco Unified Communications applications. Clustering replicates the administration and configuration of deployed applications to backup instances of those applications. Likewise, cloud services are natively redundant by virtue of elastic compute and highly available service distribution within the cloud platform.

If an instance of an application or services fails, Cisco on-premises and cloud-based services such as endpoint registration, call processing, messaging, and many others continue to operate on the remaining instance(s) of the application or service. This failover process is transparent to the users. In addition to clustering, the PA for Webex Hybrid Services provides high availability using redundant power, network connectivity, and elastic storage.

Sizing Considerations

Sizing a deployment can become complex for large enterprises with sophisticated requirements. This PA for Webex Hybrid Services presents some examples that simplify the sizing process. For details, see the chapter on Sizing Cisco Webex Hybrid Services .

Licensing

Details about the individual licenses for the endpoints and infrastructure components in the PA for Webex Hybrid Services are beyond the scope of this document. Information about Cisco Collaboration Flex Plan licensing is available at

https://www.cisco.com/c/en/us/products/unified-communications/collaboration-flex-plan/index.html

## Collaboration Endpoints

The recommendations within this Preferred Architecture assume a deployment of Cisco voice and video endpoints, including the Webex App. Some of the endpoint use SIP to register to Unified CM on-premises, while others use HTTPS to connect to the Webex Hybrid Services. Table 1-2 lists the preferred endpoints for optimal features, functionality, and user experience.

Table 1-2 Cisco Collaboration Endpoints

- Webex App for Android

- Webex App for iPhone and iPad

- Webex App for Mac

- Webex App for Windows

- Webex App web client

Application with cloud-based integrated voice/video meeting, calling, messaging, and content sharing for mobile devices, personal computers, and web browsers. The mobile and desktop clients are also capable of registering to Unified CM for voice/video calling.

Cisco IP Phone 8800 Series

General office use, multiple-line audio and video phones

Cisco IP Phone 8832

IP conference phone

Webex Desk Series

Personal TelePresence endpoint for the desktop

Webex Room Kit Series

TelePresence multipurpose and integrator room endpoints

Webex Room Series

TelePresence multipurpose and integrator room endpoints with built-in single or dual screens

Webex Board Series

All-in-one presentation, white board, and audio/video multipurpose room endpoint

## Webex Core Services

The PA for Webex Hybrid Services includes the following foundational components and services that underlie the entire Webex Hybrid Services solution. All of these services and components are relevant for the deployment of the PA for Webex Hybrid Services, and they are referenced as appropriate in the remainder of this document.

Webex Control Hub

The web-hosted online Webex Control Hub, available at https://admin.webex.com/ , is used to administer and manage an organization's Webex services.

After logging into the control hub, the administrator is presented with the overview screen, which provides a one-screen snapshot of the organization and the status and utilization of cloud services. Clickable tiles on the overview screen allow quick drill-down to more information and configuration for various features and services.

The left-hand navigation menu of the Webex Control Hub provides links to various management and provisioning areas within the web-based portal, including:

- Users — Area for managing users and provisioning them for cloud services.

- Places — Area for managing physical locations containing a device (for example, a meeting room).

- Services — Area for managing and configuring cloud services, including Webex Hybrid Services.

- Devices — Area for managing and provisioning cloud-registered room systems and Webex Boards.

- Reports — Area for viewing diagnostics and reports and reviewing and analyzing cloud and hybrid service metrics, including service and device utilization, call quality, and other statistics.

- Support — Area for finding documentation and other support resources.

- Settings — Area for managing base global organizational settings.

Webex Messaging

One of the key features of the Webex App and the Webex platform is one-to-one and group messaging with file sharing. This feature delivers persistent instant messaging with Webex spaces, where users can message and share files. Spaces are manually or dynamically created based on user workflows, and spaces can be grouped into teams to provide team-focused spaces across organizations.

Webex Meetings

Meetings are another key feature of the Webex platform utilized by Webex App and Webex endpoints. Webex Meetings provides voice and video conferencing along with screen sharing by leveraging the Webex conferencing service. Webex Meetings builds upon and leverages the messaging and file sharing capabilities of Webex Messaging. Webex Meetings also enables permanent Personal Meeting Rooms (PMR) to provide users with personalized permanent voice and video meeting spaces.

Cisco Expressway-C Connector Host Management Connector

The Cisco Expressway-C Connector Host is a standard Cisco Expressway-C server deployed within the customer's organization to provide an integration point between the on-premises and cloud collaboration services. The integration between the Cisco Expressway-C server and Webex is facilitated via micro-services installed and managed on the Expressway-C Connector Host by Webex. These micro-services enable integration of Webex Hybrid Services.

The Management Connector is included in the Expressway-C base software and is used by the administrator to register Expressway to Webex and to link the Expressway interface with the Webex management interfaces.

The Management Connector plays an important role as the coordinator of all connectors running on the Expressway server or cluster. It provides the administrator with a single point of control for connector activities. The Management Connector enables Webex-based management of the on-premises connectors, handles initial registration with Webex, manages the connector software life cycle, and provides status and alarms.

The Management Connector requires that certificates of the Certification Authorities (CA) that signed the certificates in use by Webex must be in the trusted list of the Expressway-C connector host, so that the HTTPS connection can be established. The administrator can decide to allow Webex to upload CA certificates to the Expressway-C trust store. Or, in cases where security policies prevent Webex from uploading trusted CA certificates on Expressway-C, the administrator may upload them manually.

| Module | Component | Description |
|---|---|---|
| Collaboration Endpoints | Cisco IP Phones, Webex Desk and Room Devices, and Webex App | Enable real-time message, meeting, and voice/video communications for users |
| Webex Core Services | Webex Control Hub | Web portal that enables provisioning and management of enterprise Webex App users and services; registration of endpoints, clients, and Expressway-C Connector Host to Webex; and Expressway Connector upgrades |
| Webex Messaging | Provides persistent messaging and content sharing in 1:1 and group-based spaces |
| Webex Meetings | Provides audio/video meetings, with content sharing and web conferencing capabilities for meetings |
| Cisco Expressway-C Connector Host Management Connector | Enables connectors hosted on Expressway-C to be managed by the Webex Control Hub |
| Webex Hybrid Directory Service | Cisco Directory Connector | Provides directory synchronization between Microsoft Active Directory and Webex |
| Microsoft Active Directory | Provides the full list of corporate resources and users and their attributes |
| Webex Hybrid Calendar Service | Cisco Expressway-C Connector Host Calendar Connector | Provides integration between the enterprise calendaring application and Webex |
| Microsoft Exchange | Provides corporate calendaring services |
| Webex Hybrid Call Service | Cisco Unified Communications Manager (Unified CM) | Provides endpoint registration, call processing, and media resource management |
| Webex Device Connector | Provides integration between on-premises call processing services and room systems registered as Webex devices |
| Cisco Expressway-C and Expressway-E | Enables interoperability and firewall traversal with Webex |

| Product | Description |
|---|---|
| Mobile: Webex App for Android Webex App for iPhone and iPad Desktop: Webex App for Mac Webex App for Windows Web browser: Webex App web client | Application with cloud-based integrated voice/video meeting, calling, messaging, and content sharing for mobile devices, personal computers, and web browsers. The mobile and desktop clients are also capable of registering to Unified CM for voice/video calling. |
| Cisco IP Phone 8800 Series | General office use, multiple-line audio and video phones |
| Cisco IP Phone 8832 | IP conference phone |
| Webex Desk Series | Personal TelePresence endpoint for the desktop |
| Webex Room Kit Series | TelePresence multipurpose and integrator room endpoints |
| Webex Room Series | TelePresence multipurpose and integrator room endpoints with built-in single or dual screens |
| Webex Board Series | All-in-one presentation, white board, and audio/video multipurpose room endpoint |