---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-97a148fa6b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct-b-cce-release-notes-1501_es202511/rcct-m-introduction-1501-es202511.html
retrieved_at: 2026-08-16T19:36:07.463718+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202511

# Release notes for Cisco Contact Center Enterprise Solutions 15.0(1) Engineering Specials, ES202511

Find Matches in This Book

## Results

Updated: November 30, 2025

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About This Guide

This Release Notes outlines the new features, updated features, beta features, and defect fixes with Engineering Special (ES)
                           15.0(1) ES202511 for the following Contact Center solutions and their components:

Cisco Unified Contact Center Enterprise, Release 15.0(1)

Cisco Packaged Contact Center Enterprise, Release 15.0(1)

The Features chapter provides a comprehensive list of features from the current ES and all previous 15.0(1) ESs. The Caveats
                                       and Limitations chapter includes Bug Search Tool (BST) queries that identify all defects fixed in this ES.

This document is intended for system administrators and support personnel responsible for deploying, maintaining, and upgrading
                           Cisco Contact Center Enterprise solutions.

## Key Considerations for Installation

The Engineering Special (ES) is a cumulative update for the Contact Center Enterprise (CCE) components. It contains all new
                           features, updated features, trials features, security fixes, and resolved defects from the base release, customized for VOS,
                           CCE, and CVP components.

The CCE ES is applicable to all CCE nodes including PGs, Administation Clients, and all Central Controller Components (Logger,
                           Router, and Administration and Data Server).

For procedures on how to install (and uninstall) the ES patches, see the Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Considerations for 15.0(1) ES202511 :

The 15.0(1) ES202511 Cloud Connect patch must be upgraded on all Cloud Connect VMs in the same maintenance window.

If you intend to upgrade only Cloud Connect and not Cisco Finesse, ensure that after Cloud Connect is upgraded, you run the
                                 following command on all Finesse nodes to set the cloudconnectMaxTokenExpireBufferTime to 900 seconds:

A restart of the Cisco Finesse Tomcat Service is required for these changes to take effect. Running this command ensures Finesse
                                 functions effectively.

Alternatively, you can choose to upgrade all the Finesse nodes to the 15.0(1) ES202511 Finesse patch.

If you are using Google CCAI with the VAV element and plan to install 15.0(1) ES202511, you must install the ES on both the
                                 Unified CVP VXML Server and Cisco VVB. You must also redeploy all VXML Server applications that include the VAV element by
                                 using the latest Call Studio version.

For more information, see the Unified CVP Migration chapter in Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

To install the 15.0(1) ES202511 patch on Cisco VVB, use the CLI command utils system upgrade initiate . If the CLI command fails, use the Install/Upgrade option in the Cisco VVB Operations Console to complete the installation.

For more information, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

To collect Media Gateway–related logs effectively, after installing the 15.0(1) ES202511 VVB patch, make sure you download
                                 the latest version of the Real-Time Monitoring Tool (RTMT).

If AppDynamics is configured in Cisco VVB, when rolling back to version 15.0(1), you must reconfigure the AppDynamics agents
                                 by running these commands to ensure performance monitoring is properly reset and enabled:

First, disable performance monitoring on the selected nodes:

Then, re-enable performance monitoring and apply the necessary configuration changes after restarting the target nodes:

## Quarterly Patch Downloads for 15.0(1) ES202511

For CCE 15.0(1) ES202511, the following components have made an ES available which can be downloaded from the provided links:

Component

Download Links

https://software.cisco.com/download/home/268439622/type/286337858/release/15.0(1)ES202511

https://software.cisco.com/download/home/270563413/type/280840592/release/15.0(1)ES202511

https://software.cisco.com/download/home/286338554/type/286289787/release/15.0(1)ES202511

https://software.cisco.com/download/home/283613135/type/284259728/release/15.0(1)ES202511

https://software.cisco.com/download/home/268439622/type/286310764/release/15.0(1)ES202511

https://software.cisco.com/download/home/280810493/type/281558204/release/15.0(1)ES202511

https://software.cisco.com/download/home/282163829/type/282377062/release/15.0(1)ES202511

## Cisco Security
                        	 Advisories

The Cisco Product Security Incident Response Team (PSIRT) is a dedicated, global team that manages the receipt, investigation,
                              and public reporting of security vulnerability information that relates to Cisco products and networks.

For information on
                              		  existing security issues, see Cisco
                                 			 Security Advisories, Responses, and Alerts at https://tools.cisco.com/security/center/publicationListing.x .

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| Note | The Features chapter provides a comprehensive list of features from the current ES and all previous 15.0(1) ESs. The Caveats
                                       and Limitations chapter includes Bug Search Tool (BST) queries that identify all defects fixed in this ES. |
|---|---|

| Component | Download Links |
|---|---|
| Cisco Reverse Proxy | https://software.cisco.com/download/home/268439622/type/286337858/release/15.0(1)ES202511 |
| Cloud Connect | https://software.cisco.com/download/home/268439622/type/286325642/release/15.0(1)ES202511 |
| Cisco Unified Customer Voice Portal (Unified CVP) | https://software.cisco.com/download/home/270563413/type/280840592/release/15.0(1)ES202511 |
| Cisco Virtualized Voice Browser (Cisco VVB) | https://software.cisco.com/download/home/286338554/type/286289787/release/15.0(1)ES202511 |
| Cisco Finesse | https://software.cisco.com/download/home/283613135/type/284259728/release/15.0(1)ES202511 |
| Cisco Enterprise Chat and Email (ECE) | https://software.cisco.com/download/home/268439622/type/286310764/release/15.0(1)ES202511 |
| Cisco Unified Contact Center Management Portal (Unified CCMP) | https://software.cisco.com/download/home/280810493/type/281558204/release/15.0(1)ES202511 |
| Cisco Unified Intelligence Center (Unified Intelligence Center) | https://software.cisco.com/download/home/282163829/type/282377062/release/15.0(1)ES202511 |
| Identity Service (IdS)/Single Sign-On(SSO) |
| Live Data |
| Logger | https://software.cisco.com/download/home/268439622/type/280840583/release/15.0(1)ES202511 |
| Router |
| Administration & Data Server |
| PG |