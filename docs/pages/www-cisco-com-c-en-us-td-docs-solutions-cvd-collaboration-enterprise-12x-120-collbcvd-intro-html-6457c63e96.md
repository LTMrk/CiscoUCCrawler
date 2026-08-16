---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-enterprise-12x-120-collbcvd-intro-html-6457c63e96
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/enterprise/12x/120/collbcvd/intro.html
retrieved_at: 2026-08-16T18:24:11.802328+00:00
---

Preferred Architecture for Cisco Collaboration 12.x Enterprise On-Premises Deployments, CVD

# Preferred Architecture for Cisco Collaboration 12.x Enterprise On-Premises Deployments, CVD

Updated: August 28, 2017

Chapter: Introduction

## Chapter: Introduction

## Introduction

Revised: February 19, 2019

In recent years, many new collaborative tools have been introduced to the market, enabling businesses to enhance communications and extend collaboration outside the walls of their businesses. Organizations realize the added value that collaboration applications bring to their businesses through increased employee productivity and enhanced customer relationships. Significant advances have been made in the collaboration space to simplify deployment, improve interoperability, and enhance the overall user experience.

Today's collaboration solutions offer organizations the ability to integrate video, audio, and web participants into a single, unified meeting experience. The guidelines within this Cisco Validated Design (CVD) guide are written with the overall collaboration architecture in mind. Subsystems are used for better organization of the content, and the recommendations within them are tested to ensure they align with recommendations in related subsystems.

## What’s New in This Chapter

Table 1-1 lists the topics that are new in this chapter or that have changed significantly from previous releases of this document.

Table 1-1 New or Changed Information Since the Previous Release of This Document

Replace Cisco Prime License Manager with Cisco Smart Software Manager

Table 1-2

August 30, 2017

Added Cisco Webex Room Series endpoints

Table 1-3

August 30, 2017

## Architectural Overview

This CVD for the Enterprise Collaboration Preferred Architecture incorporates a subset of products from the total Cisco Collaboration portfolio that is best suited for the enterprise market segment. This Preferred Architecture deployment model is prescriptive, out-of-the-box, and built to scale with an organization as its business needs change. This prescriptive approach simplifies the integration of multiple system-level components while also enabling an organization to select the features, services, and capacities that best address its business needs.

This CVD for the Enterprise Collaboration Preferred Architecture provides end-to-end collaboration targeted for deployments larger than 1,000 users. For smaller deployments, consult the Preferred Architecture Design Overview and CVDs for Midmarket Collaboration .

This CVD for the Enterprise Collaboration Preferred Architecture provides high availability for critical applications. The architecture supports an advanced set of collaboration services that extend to mobile workers, partners, and customers through the following key services:

- Voice communications

- Instant messaging and presence

- High definition video and content sharing

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

Cisco TelePresence Management Suite (TMS)

Cisco WebEx Software as a Service (Cloud)

Conferencing allows three or more parties to communicate via voice, video, and content sharing in real time. Resources can be either on-premises or hosted in the cloud.

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

Internet-based web portal that provides simplified, enterprise-wide management of licensing. Cisco Smart Software Manager provides administrators with a single management point for the Cisco Unified CM and Cisco Unity Connection licenses within a deployment.

Cisco Prime Collaboration Provisioning

Cisco Prime Collaboration Provisioning enables rapid configuration of collaboration systems by providing a centralized template-based console for system configuration, user and device provisioning, and simplified moves, adds, and changes.

Security

All components

Security incorporates a compilation of security features ranging from those enabled by default to those recommended for deployment. Some example features include unauthorized access protection, toll-fraud protection, certificate generation and management, and provisioning and enabling encryption for all the components in this solution.

Bandwidth Management

Network infrastructure and products from all chapters of this document

Bandwidth management incorporates an end-to-end QoS architecture, call admission control, and video rate adaptation and resiliency mechanisms to provide the best possible user experience for deploying pervasive video over managed and unmanaged networks.

Sizing

Products from all chapters of this document

Virtual Machine Placement Tool (VMPT)

Sizing for all modules that are covered in this document, as well as a virtual machine placement example.

Network Services

The Preferred Architecture for Enterprise Collaboration requires a well-structured, highly available, and resilient network infrastructure as well as an integrated set of network services, including Domain Name System (DNS), Dynamic Host Configuration Protocol (DHCP), Trivial File Transfer Protocol (TFTP), and Network Time Protocol (NTP). A detailed description of how these basic network services are utilized by Cisco applications and endpoints can be found in the Network Services section of the Cisco Collaboration SRND .

## Virtualization

Virtualizing multiple applications and consolidating them on physical servers lowers cost, minimizes rack space, lowers power requirements, and simplifies deployment and management. Virtualization also accommodates redeploying hardware and scaling software applications as organizational needs change.

### Cisco Unified Communications on the Cisco Unified Computing System (UCS)

Cisco UCS servers are thoroughly tested with unified communications (UC) core applications to provide reliable and consistent performance in a virtualized environment. There are two options for deploying UC applications on UCS servers:

- UC on UCS Tested Reference Configurations (TRCs)

UCS TRCs are specific hardware configurations of UCS server components. These components include CPU, memory, hard disks (in the case of local storage), RAID controllers, and power supplies. Specific TRCs are documented at the Collaboration Virtualization Hardware website.

- UC on UCS Spec-Based

Specifications-based UCS hardware configurations are not explicitly validated with UC applications. Therefore, no prediction or assurance of UC application virtual machine performance is made when the applications are installed on UCS specs-based hardware. In those cases Cisco provides guidance only, and ownership of assuring that the pre-sales hardware design provides the performance required by UC applications is the responsibility of the customer.

Both options are fully supported by the Cisco Technical Assistance Center (TAC), provided all rules for Cisco Collaboration Virtualization are followed.

### Cisco Business Edition 7000 (BE7000)

The Cisco BE7000 is built on a virtualized UCS that ships ready-for-use with a pre-installed virtualization hypervisor and application installation files. The BE7000 is a UCS TRC in that UC applications have been explicitly tested on its specific UCS configuration. The Cisco BE7000 solution offers premium voice, video, messaging, instant messaging and presence, and contact center features on a single, integrated platform. For more information about the Cisco BE7000, see the Cisco Business Edition 7000 Solutions Data Sheet .

### Core Applications

In the Preferred Architecture for Enterprise Collaboration, the following virtualized applications are deployed on multiple Cisco UCS servers to provide hardware and software redundancy:

- Cisco Unified Communications Manager

- Cisco Unified Communications Manager IM and Presence Service

- Cisco Unity Connection

- Cisco Expressway, consisting of Expressway-C and Expressway-E

- Cisco Meeting Server

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

Cisco IP Phone 8832

IP conference phone

Cisco Webex DX 80

Personal TelePresence endpoint for the desktop

Cisco MX Series

TelePresence multipurpose room endpoint

Cisco SX Series

Integrator series TelePresence endpoint

Cisco Webex Room Series

Collaboration integrator and multipurpose room endpoint

| New or Revised Topic | Described in: | Revision Date |
|---|---|---|
| Replace Cisco Prime License Manager with Cisco Smart Software Manager | Table 1-2 | August 30, 2017 |
| Added Cisco Webex Room Series endpoints | Table 1-3 | August 30, 2017 |

| Module | Component(s) | Purpose |
|---|---|---|
| Call Control | Cisco Unified Communications Manager (Unified CM) Cisco Unified Communications Manager IM and Presence Service Cisco Integrated Services Router (ISR) | Call control provides registration, call processing, resource management and instant messaging and presence for users and endpoints. It also encompasses remote site survivability for remote offices. |
| Conferencing | Cisco Meeting Server Cisco TelePresence Management Suite (TMS) Cisco WebEx Software as a Service (Cloud) | Conferencing allows three or more parties to communicate via voice, video, and content sharing in real time. Resources can be either on-premises or hosted in the cloud. |
| Collaboration Edge | Cisco Expressway-C Cisco Expressway-E Cisco Integrated Services Router (ISR) Cisco Aggregation Services Routers (ASR) | Collaboration Edge provides remote registration services, external communications, and interoperability. |
| Voice Messaging | Cisco Unity Connection | Cisco Unity Connection provides unified messaging and voicemail services. |
| Collaboration Management Services | Cisco Prime Collaboration Deployment | Cisco Prime Collaboration Deployment assists in the management of Unified Communications applications. It allows the user to perform tasks such as migration of older software versions of clusters to new virtual machines, fresh installs, and upgrades on existing clusters. |
| Cisco Smart Software Manager | Internet-based web portal that provides simplified, enterprise-wide management of licensing. Cisco Smart Software Manager provides administrators with a single management point for the Cisco Unified CM and Cisco Unity Connection licenses within a deployment. |
| Cisco Prime Collaboration Provisioning | Cisco Prime Collaboration Provisioning enables rapid configuration of collaboration systems by providing a centralized template-based console for system configuration, user and device provisioning, and simplified moves, adds, and changes. |
| Security | All components | Security incorporates a compilation of security features ranging from those enabled by default to those recommended for deployment. Some example features include unauthorized access protection, toll-fraud protection, certificate generation and management, and provisioning and enabling encryption for all the components in this solution. |
| Bandwidth Management | Network infrastructure and products from all chapters of this document | Bandwidth management incorporates an end-to-end QoS architecture, call admission control, and video rate adaptation and resiliency mechanisms to provide the best possible user experience for deploying pervasive video over managed and unmanaged networks. |
| Sizing | Products from all chapters of this document Virtual Machine Placement Tool (VMPT) | Sizing for all modules that are covered in this document, as well as a virtual machine placement example. |

| Product | Description |
|---|---|
| Mobile: Jabber for Android Jabber for iPhone and iPad Desktop: Jabber for Mac Jabber for Windows | Soft client with integrated voice, video, voicemail, instant messaging, and presence functionality as well as secure edge traversal for mobile devices and personal computers |
| Cisco IP Phone 8800 Series | Public space, general office use, single-line and multi-line audio and video phones |
| Cisco IP Phone 8832 | IP conference phone |
| Cisco Webex DX 80 | Personal TelePresence endpoint for the desktop |
| Cisco MX Series | TelePresence multipurpose room endpoint |
| Cisco SX Series | Integrator series TelePresence endpoint |
| Cisco Webex Room Series | Collaboration integrator and multipurpose room endpoint |