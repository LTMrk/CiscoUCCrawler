---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-200651-uccx-version-11-5-prerel-27f86d22f1
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/200651-UCCX-Version-11-5-Prerelease-Field-Commu.html
retrieved_at: 2026-08-21T06:52:04.923798+00:00
---

UCCX Version 11.5 Prerelease Field Communication

# UCCX Version 11.5 Prerelease Field Communication

Updated: September 9, 2016

Document ID: 200651

Contents

## Contents

## Introduction

This document provides a sneak peek into the upgrade paths, design and the new features embedded into the Cisco Unified Contact Center Express (UCCX) version 11.5 release.

Further information is documented on the Release Notes (RN), Solution Reference Network Design (SRND) guide and the Administration guides.

## Background Information

UCCX version 11.5 is due to be released soon. With the introduction of this version, there are a lot of new features, bug fixes and serviceability improvements. UCCX has evolved from a product to a solution along with the integration of SocialMiner for Chat/Email, MediaSense for Recording, co-resident Finesse as the Agent Desktop Solution.

## Upgrade Paths and Getting to 11.5

UCCX supports these upgrade paths for 11.5 release:

- 9.0(2)SU3

- 10.0(1)SU1, 10.5(1)SU1, 10.6(1), 10.6(1)SU1, 10.6(1)SU2

- 11.0(1)

If you are not in any of the above versions, you first need to upgrade to the versions mentioned above and then stage an upgrade to 11.5 version. UCCX 11.5 is supported with Call managers 10.5(1), 10.5(2), 11.0(1), 11.0(1a) and 11.5(1). More details about the same is in the compatibility matrix which is updated real-time.

To start with 11.5, the compatibility matrix is updated to provide more granular information about the platform components as shown in the image:

﻿

Administrators can evaluate the platform for various security and administrative purposes using this feature.

If you deploy a new UCCX 11.5 or plan an upgrade to 11.5, to have the right hardware specifications for the virtual machine is very important. These are the Open Virtualiaton Alliance (OVA) configuration settings for the UCCX 11.5:

Refer to these documents for the latest information on Open Virtualization Format (OVF) and compatibility:

## New Supported Components

To start with 11.5, the UCCX solution supports a few additional components. The support for these components not only includes qualification efforts but enhancements to the UCCX itself to allow interoparability with these new components.

Some of the main components include:

Office365 support: UCCX 11.5 can now provide email functionality while working with a cloud email service in the form of Office365. The email flow remains the same as the previous release, and a new Socket Secure (SOCKS) proxy implementation within the UCCX enables a proxy connection from the SocialMiner to the Office365 account.

In addition to this, Finesse email also supports Microsoft Exchage Server 2010 E, 2013 E and 2016 E editions.

Google Chorme support: UCCX 11.5 supports Google Chrome versions 48 and higher. All the administrative and user pages are available to be used with Chrome with the exception of Context Service Registration User Interface and Real-Time Reporting.

Windows 10 support: UCCX 11.5 now supports Windows 10 as a supported operating system for agents, supervisors and administrators. Details are provided in the compatibility matrix.

## CUIC New UI

The new User Interface (UI) of Cisco Unified Intelligence Center (CUIC) available with version 11.5 is a completely improved, revamped User Interface aimed at greatly simplifying and enhancing the user experience. It is very important to note that this new UI is available for Reports and Dashboards only. The table shown, summrizes the features that are available on the new UI and the older ones:

The redirection to the legacy UI happens automatically and does not require any user intervention.

CUIC sync CLI commands:

Individual CUIC sync commands have been removed and now there is only one command to sync all the configuration to CUIC:

utils uccx synctocuic

utils uccx synctocuic team teamname

utils uccx synctocuic user username

utils uccx synctocuic permission all

## Certificate considerations

With 11.5, the platform has added another security certificate to allow support for FEDRamp. Because of this, the UCCX agent desktops are presented with an additional certificate when accessing Live Data or other gadgets, even if all the certificates were accepted in 11.0.

This is on the port 12015 and the agents have to be advised to accept the same:

﻿

When you use self-signed certificates, it is required to replace both the tomcat and the tomcat-ECDSA certificates with the CA signed ones to ensure Live Data gadgets connect to the SocketIO service in 11.5.

﻿

## Single Sign On (SSO)

With 11.5, UCCX is capable of Single Sign On functionality for these components:

- UCCX (Cisco Unified Contact Center Express)

- CUIC (Cisco Unified Intelligence Center)

- Finesse

This capability allows Agents/Supervisors to use Single Sign On (SSO) for Finesse to login on the Desktop and also to CUIC for viewing Agent/Supervisor based reports. It is also useful for UCCX Administrators, which perform a variety of administrative functions within the Contact Center.

Configuration and implementation of SSO involves three phases:

- Configuration of the Identity Provider (IdP)

- Integration between UCCX and Identity Provider

- Register, Test and Enable the SSO functionality from Appadmin page.

For more information on the configuration of the Identity Provider and establishing the trust between the IdP and UCCX, refer to the article Configure Identity Provider for SSO.

### Support and Limitations

### Register, Test and Enable SSO

SSO flow includes registeration of all the components, testing and then enabling SSO. Enabling SSO involves a warning message to ensure that this is done during maintenance window.

﻿ ﻿ ﻿

## Serviceability Enhancements

UCCX 11.5 has major improvements in this areas:

Finesse Failover Behavior - Enhanced to reduce the failover time period for the Finesse clients by reduction of redundant messages being sent to the node IN SERVICE. This also includes the enhancement of deferred failover approach so that requests do not overwhelm the server at once. Clients failover within a span of 10 - 45 seconds after the engine mastership changes to the active node.

AXL (Cisco Administrative XML - Extensible Markup Language) failover - More reliable failover to the secondary Administrative XML layer (AXL) providers during transient failover issues.

Reskilling Performance Improvements - Enhanced the indexing to improve the performance on the RMCM (Resource Manager Contact Manager) pages and reduce the Central Processing Unit (CPU) cycles on UCCX.

Purge Enhancements - Historical Database (DB) Purge enhancement on Manual and Scheduled Purge to show the status of the purge initiated.

CUIC Enhancements - Usage of the UCCX Historical Reporting User (HR User) for the UCCX Datasource.

### Revision History

1.0

09-Sep-2016

Initial Release

### Contributed by Cisco Engineers

Arundeep Nagaraj

Cisco TAC Engineer

Abhiram Kramadhati

Cisco Engineering

### This Document Applies to These Products

- Unified Contact Center Express

| Agent Capacity | vCPU | vRAM | vDisk |
|---|---|---|---|
| 100 agents | 2 | 10 GB | 1 x 146 GB |
| 300 agents | 2 | 10 GB | 2 x 146 GB |
| 400 agents | 4 | 15 GB | 2 x 146 GB |

| Report Type | Operation | 11.5 UI | Legacy UI |
|---|---|---|---|
| Grid | View - CRUD (Create, Retrieve, Update, Delete) | √ | × |
| Grouping - CRUD | √ | × |
| Threshold - CRUD | √ | × |
| Report Execution | √ | × |
| Report Import | × | √ |
| Report Export | × | √ |
| Gauge and Charts | View - CRUD | × | √ |
| Report Execution | √ | × |
| Report Import | × | √ |
| Report Export | × | √ |

| Feature | Support/Limitations |
|---|---|
| SSO for UCCX Admin, CUIC and Finesse | Yes |
| OS (Operating System) Administration and DRS (Disaster Recovery System) | No - Platform User Credentials will be used |
| Finesse Administration Page | No support for SSO yet |
| Identity Providers Supported | Active Directory Federation Service (ADFS) Version 2.0 and 3.0 |
| Signature Algorithm for SAML (Security Assertion Markup Language) | SHA-1 only |
| SSO enforcement | UCCX, CUIC and Finesse at the same time |
| Stock Gadget and MediaSense Gadget support within Finesse | SSO supported by default |
| Custom Gadgets on Finesse | No |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 09-Sep-2016 | Initial Release |