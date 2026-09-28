---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-enterprise-14-collbcvd-intro-html-d02a12bcec
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/enterprise/14/collbcvd/intro.html
retrieved_at: 2026-08-16T18:23:00.570081+00:00
---

Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployments, CVD

# Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployments, CVD

Updated: May 21, 2021

Chapter: Introduction

## Chapter: Introduction

## Introduction

Revised: May 21, 2021

In recent years, many new collaborative tools have been introduced to the market, enabling businesses to enhance communications and extend collaboration outside the walls of their businesses. Organizations realize the added value that collaboration applications bring to their businesses through increased employee productivity and enhanced customer relationships. Significant advances have been made in the collaboration space to simplify deployment, improve interoperability, and enhance the overall user experience.

Today's collaboration solutions offer organizations the ability to integrate video, audio, and web participants into a single, unified meeting experience. The guidelines within this Cisco Validated Design (CVD) guide are written with the overall collaboration architecture in mind. Subsystems are used for better organization of the content, and the recommendations within them are tested to ensure they align with recommendations in related subsystems.

## What’s New in This Chapter

Table 1-1 lists the topics that are new in this chapter or that have changed significantly from previous releases of this document.

Table 1-1 New or Changed Information Since the Previous Release of This Document

Minor updates related to collaboration applications running on virtualized platform with ESXi 6.7 and 7.0

Virtualization

May 21, 2021

Added Cisco Webex Desk Pro and removed end of sale DX, MX, and SX series endpoints

Table 1-3

May 21, 2021

Added Cisco Webex Cloud-Connected Unified Communications (CCUC) component

Table 1-2

May 21, 2021

## Architectural Overview

This CVD for the Enterprise Collaboration Preferred Architecture incorporates a subset of products from the total Cisco Collaboration portfolio that is best suited for the enterprise market segment. This Preferred Architecture deployment model is prescriptive, out-of-the-box, and built to scale with an organization as its business needs change. This prescriptive approach simplifies the integration of multiple system-level components while also enabling an organization to select the features, services, and capacities that best address its business needs.

This CVD for the Enterprise Collaboration Preferred Architecture provides end-to-end collaboration targeted for deployments larger than 1,000 users. For smaller deployments, consult the Preferred Architecture Design Overview and CVDs for Midmarket Collaboration .

This CVD for the Enterprise Collaboration Preferred Architecture provides high availability for critical applications. The architecture supports an advanced set of collaboration services that extend to mobile workers, partners, and customers through the following key services:

- Voice communications

- Instant messaging and presence

- High-definition video and content sharing

- Rich media conferencing

- Enablement of mobile and remote workers

- Business-to-business voice and video communications

- Unified voice messaging

Because of the adaptable nature of Cisco endpoints and their support for IP networks, this architecture enables an organization to use its current data network to support both voice and video calls. The preferred architecture employs a holistic approach to bandwidth management that incorporates an end-to-end QoS architecture, call admission control, and video rate adaptation and resiliency mechanisms to provide the best possible user experience for deploying pervasive video over managed and unmanaged networks.

The Cisco Preferred Architecture for Enterprise Collaboration, shown in Figure 1-1 , provides highly available and secure centralized services. These services extend easily to remote offices and mobile workers, providing availability of critical services even if communication with headquarters is lost. This should be viewed as a fundamental architecture from which to design a new deployment or to evolve an existing one. As the Preferred Architecture progresses, this architecture will be expanded upon with additional products and solutions.

Figure 1-1 Cisco Preferred Architecture for Enterprise Collaboration

Table 1-2 lists the products in this architecture. For simplicity, products are grouped into modules to help categorize and define their roles. The content of this CVD is organized into the same modules.

Table 1-2 Components of the Cisco Preferred Architecture for Enterprise Collaboration

Call Control

Cisco Unified Communications Manager (Unified CM)

Cisco Unified Communications Manager IM and Presence Service

Cisco Integrated Services Router (ISR)

Call control provides registration, call processing, resource management and instant messaging and presence for users and endpoints. It also encompasses remote site survivability for remote offices.

Conferencing

Cisco Meeting Server

Cisco Meeting Management

Cisco TelePresence Management Suite (TMS)

Conferencing allows three or more parties to communicate via voice, video, and content sharing in real time.

Collaboration Edge

Cisco Expressway-C

Cisco Expressway-E

Cisco Integrated Services Router (ISR)

Cisco Aggregation Services Routers (ASR)

Collaboration Edge provides remote registration services, external communications, and interoperability.

Voice Messaging

Cisco Unity Connection

Cisco Unity Connection provides unified messaging and voicemail services.

Collaboration Management Services

Cisco Prime Collaboration Deployment

Cisco Prime Collaboration Deployment assists in the management of Unified Communications applications. It allows the user to perform tasks such as migration of older software versions of clusters to new virtual machines, fresh installs, and upgrades on existing clusters.

Cisco Smart Software Manager

Internet-based web portal that provides simplified, enterprise-wide management of licensing. Cisco Smart Software Manager provides administrators with a single management point for the Cisco Unified CM, Cisco Unity Connection Cisco Meeting Server, and Expressway licenses within a deployment.

Cisco Webex Cloud-Connected Unified Communications

Cisco Webex Cloud-Connected Unified Communications (CCUC) is a suite of cloud services providing centralized administrative services within Webex Control Hub for on-premises collaboration applications. Services enabled with CUCC include system health checks and analytics.

Security

All components

Security incorporates a compilation of security features ranging from those enabled by default to those recommended for deployment. Some example features include unauthorized access protection, toll-fraud protection, certificate generation and management, and provisioning and enabling encryption for all the components in this solution.

Bandwidth Management

Network infrastructure and products from all chapters of this document

Bandwidth management incorporates an end-to-end QoS architecture, call admission control, and video rate adaptation and resiliency mechanisms to provide the best possible user experience for deploying pervasive video over managed and unmanaged networks.

Sizing

Products from all chapters of this document

Quote Collab Tool

Sizing for all modules that are covered in this document, as well as a virtual machine placement example using the Quote Collab Tool.

Network Services

The Preferred Architecture for Enterprise Collaboration requires a well-structured, highly available, and resilient network infrastructure as well as an integrated set of network services, including Domain Name System (DNS), Dynamic Host Configuration Protocol (DHCP), Trivial File Transfer Protocol (TFTP), and Network Time Protocol (NTP). A detailed description of how these basic network services are utilized by Cisco applications and endpoints can be found in the Network Infrastructure chapter of the Cisco Collaboration SRND .

## Virtualization

Virtualizing multiple applications and consolidating them on physical servers lowers cost, minimizes rack space, lowers power requirements, and simplifies deployment and management. Virtualization also accommodates redeploying hardware and scaling software applications as organizational needs change.

### Cisco Business Edition 7000 (BE7000)

The Cisco BE7000 is built on a modified virtualized UCS that ships ready-for-use with a pre-installed virtualization hypervisor and application installation files. The specifications of the BE7000 appliance accommodates deployments of 1000 phones or more (multiple appliances usually required). The Cisco BE7000 solution offers premium voice, video, messaging, instant messaging, and presence, and contact center features on a single, integrated platform. For more information about the Cisco BE7000, see the Cisco Business Edition 7000 Solutions Data Sheet .

### Cisco Unified Communications on the Cisco Unified Computing System (UCS)

Cisco Collaboration applications define requirements for compatibility, minimum hardware specifications and virtual machine (VM) placement, with example bills of materials provided for various deployment sizes. For more information, refer to the Cisco Collaboration Infrastructure Requirements collateral available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html

Note The Cisco Collaboration Infrastructure Requirements collateral applies not only to CSR 14 on ESXi 6.7/7.0, but also to CSR 12.7 on ESXi 7.0.

The Cisco Technical Assistance Center (TAC) supports Cisco applications on Cisco or 3rd-party virtualized hardware environments satisfying application rules. Cisco TAC also supports Cisco OEMs of VMware software and Cisco hardware.

### Core Applications

In the Preferred Architecture for Enterprise Collaboration, the following virtualized applications are deployed on multiple Cisco UCS servers to provide hardware and software redundancy:

- Cisco Unified Communications Manager

- Cisco Unified Communications Manager IM and Presence Service

- Cisco Unity Connection

- Cisco Expressway, consisting of Expressway-C and Expressway-E

- Cisco Meeting Server and Cisco Meeting Management

- Cisco TelePresence Management Suite

We recommend always deploying redundant configurations to provide the highest availability for critical business applications.

## Collaboration Endpoints

The recommendations within this CVD guide assume a deployment of Cisco voice and video endpoints, including soft clients such as Cisco Jabber. These endpoints use SIP to register to Cisco Unified Communications Manager (Unified CM). Table 1-3 lists the preferred endpoints for optimal features, functionality, and user experience.

Table 1-3 Cisco Collaboration Endpoints

- Jabber for Android

- Jabber for iPhone and iPad

- Jabber for Mac

- Jabber for Windows

Soft client with integrated voice, video, voicemail, instant messaging, and presence functionality as well as secure edge traversal for mobile devices and personal computers

Cisco IP Phone 8800 Series

Public space, general office use, single-line and multi-line audio and video phones

Cisco IP Phone Conference 8832

IP conference phone

Cisco Webex Deskpro

Personal Collaboration endpoint for the desktop

Cisco Webex Room Series

Collaboration integrator and multipurpose room endpoint

| New or Revised Topic | Described in: | Revision Date |
|---|---|---|
| Minor updates related to collaboration applications running on virtualized platform with ESXi 6.7 and 7.0 | Virtualization | May 21, 2021 |
| Added Cisco Webex Desk Pro and removed end of sale DX, MX, and SX series endpoints | Table 1-3 | May 21, 2021 |
| Added Cisco Webex Cloud-Connected Unified Communications (CCUC) component | Table 1-2 | May 21, 2021 |

| Module | Component(s) | Purpose |
|---|---|---|
| Call Control | Cisco Unified Communications Manager (Unified CM) Cisco Unified Communications Manager IM and Presence Service Cisco Integrated Services Router (ISR) | Call control provides registration, call processing, resource management and instant messaging and presence for users and endpoints. It also encompasses remote site survivability for remote offices. |
| Conferencing | Cisco Meeting Server Cisco Meeting Management Cisco TelePresence Management Suite (TMS) | Conferencing allows three or more parties to communicate via voice, video, and content sharing in real time. |
| Collaboration Edge | Cisco Expressway-C Cisco Expressway-E Cisco Integrated Services Router (ISR) Cisco Aggregation Services Routers (ASR) | Collaboration Edge provides remote registration services, external communications, and interoperability. |
| Voice Messaging | Cisco Unity Connection | Cisco Unity Connection provides unified messaging and voicemail services. |
| Collaboration Management Services | Cisco Prime Collaboration Deployment | Cisco Prime Collaboration Deployment assists in the management of Unified Communications applications. It allows the user to perform tasks such as migration of older software versions of clusters to new virtual machines, fresh installs, and upgrades on existing clusters. |
| Cisco Smart Software Manager | Internet-based web portal that provides simplified, enterprise-wide management of licensing. Cisco Smart Software Manager provides administrators with a single management point for the Cisco Unified CM, Cisco Unity Connection Cisco Meeting Server, and Expressway licenses within a deployment. |
| Cisco Webex Cloud-Connected Unified Communications | Cisco Webex Cloud-Connected Unified Communications (CCUC) is a suite of cloud services providing centralized administrative services within Webex Control Hub for on-premises collaboration applications. Services enabled with CUCC include system health checks and analytics. |
| Security | All components | Security incorporates a compilation of security features ranging from those enabled by default to those recommended for deployment. Some example features include unauthorized access protection, toll-fraud protection, certificate generation and management, and provisioning and enabling encryption for all the components in this solution. |
| Bandwidth Management | Network infrastructure and products from all chapters of this document | Bandwidth management incorporates an end-to-end QoS architecture, call admission control, and video rate adaptation and resiliency mechanisms to provide the best possible user experience for deploying pervasive video over managed and unmanaged networks. |
| Sizing | Products from all chapters of this document Quote Collab Tool | Sizing for all modules that are covered in this document, as well as a virtual machine placement example using the Quote Collab Tool. |

| Product | Description |
|---|---|
| Mobile: Jabber for Android Jabber for iPhone and iPad Desktop: Jabber for Mac Jabber for Windows | Soft client with integrated voice, video, voicemail, instant messaging, and presence functionality as well as secure edge traversal for mobile devices and personal computers |
| Cisco IP Phone 8800 Series | Public space, general office use, single-line and multi-line audio and video phones |
| Cisco IP Phone Conference 8832 | IP conference phone |
| Cisco Webex Deskpro | Personal Collaboration endpoint for the desktop |
| Cisco Webex Room Series | Collaboration integrator and multipurpose room endpoint |