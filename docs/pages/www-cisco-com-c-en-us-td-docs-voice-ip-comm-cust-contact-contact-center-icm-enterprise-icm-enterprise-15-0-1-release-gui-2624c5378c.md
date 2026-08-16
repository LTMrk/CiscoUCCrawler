---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-2624c5378c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct-b-cce-release-notes-for-es/rcct-m-introduction-15-01-es.html
retrieved_at: 2026-08-16T19:36:20.408340+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202508

# Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202508

Find Matches in This Book

## Results

Updated: August 29, 2025

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About This Guide

This Release Notes outlines the new features, updated features, trials features, and defect fixes with Engineering Special
                           (ES) ES202508 for the following Contact Center solutions and their components:

Cisco Unified Contact Center Enterprise, Release 15.0(1)

Cisco Packaged Contact Center Enterprise, Release 15.0(1)

This document is intended for system administrators and support personnel responsible for deploying, maintaining, and upgrading
                           Cisco Contact Center Enterprise solutions.

## Key Considerations Before Installation

The Engineering Special (ES) is a cumulative update for the Contact Center Enterprise (CCE) components. It contains all new
                           features, updated features, trials features, security fixes, and resolved defects from the base release, customized for VOS
                           (Virtual Operating System), CCE, and Cisco Unified Customer Voice Portal (Unified CVP) components.

The CCE ES is applicable to all CCE nodes including PGs, Administation Clients, and all Central Controller Components (Logger,
                           Router, and Administration and Data Server).

For procedures on how install (and uninstall) the ES patches on VOS, CCE, and CVP components, see the Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Ensure the Unified CVP VXML Server and Unified Call Studio are on the same ES version, then re-deploy all VXML Server applications
                           containing the VAV element using the latest Call Studio by importing the application, selecting the appropriate Connector
                           Type (Webex CCAI, Integration, or Service App) and Agent Type (Scripted or Autonomous) in the VAV settings, saving and re-deploying
                           to the latest VXML Server, and finally restarting the VXML Server or running updateApp.bat to complete the update.

## Quarterly Patch Downloads – 15.0_ES202508

For CCE ES202508 , the following components have made an ES available which can be downloaded from the provided links:

Component

Download Links

https://software.cisco.com/download/home/268439622/type/286337858/release/15.0(1)ES202508

https://software.cisco.com/download/home/284360381/type/286337858/release/15.0(1)ES202508

https://software.cisco.com/download/home/286337798/type/286337858/release/15.0(1)ES202508

Cloud Connect

https://software.cisco.com/download/home/268439622/type/286325642/release/15.0(1)ES202508

https://software.cisco.com/download/home/270563413/type/280840592/release/15.0(1)ES202508

https://software.cisco.com/download/home/286338554/type/286289787/release/15.(1)ES202508

https://software.cisco.com/download/home/283613135/type/284259728/release/15.0(1)ES202508

Cisco Enterprise Chat and Email

https://software.cisco.com/download/home/286311237/type/286310764/release/15.0(1)ES202508

https://software.cisco.com/download/home/280810493/type/281558204/release/15.0(1)ES202508

https://software.cisco.com/download/home/282163829/type/282377062/release/15.0(1)ES202508

Identity Service (IdS)/Single Sign-On(SSO)

Live Data

https://software.cisco.com/download/home/268439622/type/280840583/release/15.0(1)ES202508

Router

Administration & Data Server

PG

## Cisco Security
                        	 Advisories

The Cisco Product Security Incident Response Team (PSIRT) is a dedicated, global team that manages the receipt, investigation,
                              and public reporting of security vulnerability information that relates to Cisco products and networks.

For information on
                              		  existing security issues, see Cisco
                                 			 Security Advisories, Responses, and Alerts at https://tools.cisco.com/security/center/publicationListing.x .

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| Component | Download Links |
|---|---|
| Cisco Reverse Proxy | https://software.cisco.com/download/home/268439622/type/286337858/release/15.0(1)ES202508 https://software.cisco.com/download/home/284360381/type/286337858/release/15.0(1)ES202508 https://software.cisco.com/download/home/286337798/type/286337858/release/15.0(1)ES202508 |
| Cloud Connect | https://software.cisco.com/download/home/268439622/type/286325642/release/15.0(1)ES202508 |
| Cisco Unified Customer Voice Portal. | https://software.cisco.com/download/home/270563413/type/280840592/release/15.0(1)ES202508 |
| Cisco Virtualized Voice Browser | https://software.cisco.com/download/home/286338554/type/286289787/release/15.(1)ES202508 |
| Finesse | https://software.cisco.com/download/home/283613135/type/284259728/release/15.0(1)ES202508 |
| Cisco Enterprise Chat and Email | https://software.cisco.com/download/home/286311237/type/286310764/release/15.0(1)ES202508 |
| Cisco Unified Contact Center Management Portal | https://software.cisco.com/download/home/280810493/type/281558204/release/15.0(1)ES202508 |
| Cisco Unified Intelligence Center server | https://software.cisco.com/download/home/282163829/type/282377062/release/15.0(1)ES202508 |
| Identity Service (IdS)/Single Sign-On(SSO) |
| Live Data |
| Logger | https://software.cisco.com/download/home/268439622/type/280840583/release/15.0(1)ES202508 |
| Router |
| Administration & Data Server |
| PG |