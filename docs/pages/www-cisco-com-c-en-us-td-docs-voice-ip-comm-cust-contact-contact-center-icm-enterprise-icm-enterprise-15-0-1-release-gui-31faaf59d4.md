---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-31faaf59d4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct-b-cce-release-notes-1501_es202603/rcct-m-introduction-1501-es202603.html
retrieved_at: 2026-08-16T19:35:54.904049+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions Engineering Specials, 15.0(1) SU1/ES202603

# Release notes for Cisco Contact Center Enterprise Solutions Engineering Specials, 15.0(1) SU1/ES202603

Find Matches in This Book

## Results

Updated: March 31, 2026

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About This Guide

This Release Notes outlines the new features, updated features, beta features, and defect fixes with Engineering Special (ES)
                           15.0(1) SU1/ES202603 for the following Contact Center solutions and their components:

Cisco Unified Contact Center Enterprise, Release 15.0(1)

Cisco Packaged Contact Center Enterprise, Release 15.0(1)

The Features chapter provides a comprehensive list of features from the current 15.0(1) SU1/ES202603 release. The Caveats
                           and Limitations chapter includes Bug Search Tool (BST) queries that identify all defects fixed in this release.

All features, caveats, and limitations listed in this Release Notes also apply to Packaged CCE, unless explicitly stated otherwise.

This document is intended for system administrators and support personnel responsible for deploying, maintaining, and upgrading
                           Cisco Contact Center Enterprise solutions.

## Key Considerations for Installation

Considerations for 15.0(1) SU1/ES202603 :

ES releases are cumulative. If you are installing ES202603 without having previously installed an earlier ES release of 15.0(1),
                                 review the Key Considerations for Installation sections of preceeding ES release notes at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html for any actions that may apply to your deployment .

Starting from the 15.0(1) SU1/ES202603 release,  CCE supports upgrade from 12.6(2) to 15.0(1) SU1/ES202603 and from 15.0(1)
                                 to 15.0(1) SU1/ES202603.

It is recommended to follow the Multistage Upgrade Workflow when upgrading from 12.6(2) to 15.0(1) SU1/ES202603.

If you are upgrading from version 12.6(2) to 15.0 SU1/ES202603, follow the compatibility tables for 12.6(x) to 15.0(1) in
                                 the Compatibility Matrix at Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1) . However, if you are upgrading from 15.0(1) to 15.0 SU1/ES202603, there is no need to refer to a specific Compatibility Matrix.

The 15.0(1) SU1/ES202603 release includes patches for Windows-based components and full ISO image upgrades for VOS-based components.
                                 The following VOS-based components are released as 15.0(1) SU1 full ISO images and therefore require an upgrade rather than
                                 a patch installation:

Cisco Finesse

Cisco Virtualized Voice Browser (Cisco VVB)

Cisco Unified Intelligence Center

Cisco Cloud Connect

Cisco Identity Service (Cisco IdS)

Cisco Live Data

The 15.0(1) SU1/ES202603 upgrade of any of the above components must be performed on both the publisher and subscriber in
                                 the same maintenance window. For example, both the Cloud Connect publisher and subscriber must be upgraded to 15.0(1) SU1/ES202603
                                 in the same maintenance window.

If you have Digital Channels enabled in your deployment, upgrading Cloud Connect to 15.0(1) SU1 requires downtime. Before
                                             upgrading, all queued or in‑progress tasks must be completed or dropped on the active side. The upgraded Publisher side will
                                             remain inactive until the Subscriber is also upgraded to 15.0(1) SU1 and the version switch is completed. Until then, the
                                             Subscriber side will continue to handle all tasks.

15.0(1) OVA is supported for 15.0(1) and all subsequent 15.0(1) SU updates.

The deployed version displayed on the VOS-based component CLI does not explicitly display "SU1." Verify the installation by
                                 checking the version string for the 10100 suffix, which identifies the 15.0 SU1 release (for example, 15.0.1.10100-168).

For procedures on how to upgrade to the corresponding 15.0(1) SU1 version, see the solution or component's Install and Upgrade
                                 guide.

For procedures on how to install (and uninstall) the ES patches, see the Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

## Quarterly Patch Downloads for 15.0(1) SU1/ES202603

For CCE 15.0(1) SU1/ES202603, the following components have an ES available for download:

Component

Download Links

https://software.cisco.com/download/home/270563413/type/280840592/release/15.0(1)ES202603

https://software.cisco.com/download/home/268439622/type/286310764/release/15.0(1)ES202603

https://software.cisco.com/download/home/280810493/type/281558204/release/15.0(1)ES202603

https://software.cisco.com/download/home/268439622/type/280840583/release/15.0(1)ES202603

For CCE 15.0(1) SU1/ES202603, the following components have a SU available for download:

Component

Download Links

https://software.cisco.com/download/home/268439622/type/286337858/release/15.0(1)SU1

https://software.cisco.com/download/home/268439622/type/286325642/release/15.0(1)SU1

https://software.cisco.com/download/home/286338554/type/286289787/release/15.0(1)SU1

https://software.cisco.com/download/home/283613135/type/284259728/release/15.0(1)SU1

https://software.cisco.com/download/home/282163829/type/282377062/release/15.0(1)SU1

## Cisco Security
                        	 Advisories

The Cisco Product Security Incident Response Team (PSIRT) is a dedicated, global team that manages the receipt, investigation,
                              and public reporting of security vulnerability information that relates to Cisco products and networks.

For information on
                              		  existing security issues, see Cisco
                                 			 Security Advisories, Responses, and Alerts at https://tools.cisco.com/security/center/publicationListing.x .

| Note | All features, caveats, and limitations listed in this Release Notes also apply to Packaged CCE, unless explicitly stated otherwise. |
|---|---|

| Note | If you have Digital Channels enabled in your deployment, upgrading Cloud Connect to 15.0(1) SU1 requires downtime. Before
                                             upgrading, all queued or in‑progress tasks must be completed or dropped on the active side. The upgraded Publisher side will
                                             remain inactive until the Subscriber is also upgraded to 15.0(1) SU1 and the version switch is completed. Until then, the
                                             Subscriber side will continue to handle all tasks. |
|---|---|

| Component | Download Links |
|---|---|
| Cisco Unified Customer Voice Portal (Unified CVP) | https://software.cisco.com/download/home/270563413/type/280840592/release/15.0(1)ES202603 |
| Cisco Enterprise Chat and Email (ECE) | https://software.cisco.com/download/home/268439622/type/286310764/release/15.0(1)ES202603 |
| Cisco Unified Contact Center Management Portal (Unified CCMP) | https://software.cisco.com/download/home/280810493/type/281558204/release/15.0(1)ES202603 |
| Logger | https://software.cisco.com/download/home/268439622/type/280840583/release/15.0(1)ES202603 |
| Router |
| Administration & Data Server |
| PG |

| Component | Download Links |
|---|---|
| Cisco Reverse Proxy | https://software.cisco.com/download/home/268439622/type/286337858/release/15.0(1)SU1 |
| Cloud Connect | https://software.cisco.com/download/home/268439622/type/286325642/release/15.0(1)SU1 |
| Cisco Virtualized Voice Browser (Cisco VVB) | https://software.cisco.com/download/home/286338554/type/286289787/release/15.0(1)SU1 |
| Cisco Finesse | https://software.cisco.com/download/home/283613135/type/284259728/release/15.0(1)SU1 |
| Cisco Unified Intelligence Center (Unified Intelligence Center) | https://software.cisco.com/download/home/282163829/type/282377062/release/15.0(1)SU1 |
| Identity Service (IdS)/Single Sign-On(SSO) |
| Live Data |