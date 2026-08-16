---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-e3c7b8717a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct-b-cce-release-notes-1501_es202607/rcct-m-introduction-1501-es202607.html
retrieved_at: 2026-08-16T19:35:42.648199+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions Engineering Specials, 15.0(1) SU2/ES202607

# Release notes for Cisco Contact Center Enterprise Solutions Engineering Specials, 15.0(1) SU2/ES202607

Find Matches in This Book

## Results

Updated: July 31, 2026

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About This Guide

These release notes outline the new features, updated features, beta features, and defect fixes in the 15.0(1) SU2/ES202607
                           release for the following Contact Center solutions and their components:

Cisco Unified Contact Center Enterprise (Unified CCE), Release 15.0(1)

Cisco Packaged Contact Center Enterprise (Packaged CCE), Release 15.0(1)

The Features chapter provides a comprehensive list of features from the current 15.0(1) SU2/ES202607 release. The Caveats
                           and Limitations chapter includes Bug Search Tool (BST) queries that identify all defects fixed in this release.

All features, caveats, and limitations listed in these release notes also apply to Packaged CCE, unless explicitly stated
                                       otherwise.

This document is intended for system administrators and support personnel responsible for deploying, maintaining, and upgrading
                           Cisco Contact Center Enterprise solutions.

## Key Considerations for Installation for 15.0(1) SU2/ES202607

ES releases are cumulative. If you are installing ES202607 without having previously installed an earlier ES release of 15.0(1),
                                 review the Key Considerations for Installation sections of preceding ES release notes at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html for any actions that may apply to your deployment.

OVA Template Naming Convention

VMware and Nutanix use separate OVA files. Select the OVA that contains the appropriate hypervisor identifier in its filename:

vmware —VMware

nutanix —Nutanix AHV

A Nutanix OVA filename also identifies its release applicability and deployment profile. For example:

VVB_15.0.1-SU2+_nutanix_Small_v.3.0.ova

VVB —Cisco Virtualized Voice Browser

15.0.1-SU2+ —Release 15.0(1) SU2 and later SUs, unless superseded

nutanix —Nutanix AHV

Small —small deployment profile

v.3.0 —OVA template version

Some components provide multiple OVAs in a ZIP archive. A filename containing OVAPack identifies an OVA bundle. Extract the archive and select the OVA for the required component and deployment profile.

ES202607 and SU2 Compatibility

ES202607 is a cumulative Engineering Special for Windows-based components . It can be installed directly on the 15.0(1) base release or over an earlier 15.0(1) quarterly ES, such as ES202511 or ES202603.

15.0(1) SU2 is an ISO-based release for VOS-based components and supports these upgrade paths:

Supported upgrade paths for 15.0(1) SU2:

12.6(2) to 15.0(1) SU2

15.0(1) FCS release to 15.0(1) SU2

15.0(1) SU1 to 15.0(1) SU2

For CCE 15.0(1), install ES202607 on Windows-based components and use the SU2 ISO to upgrade the following VOS-based components:

Cisco Finesse (Finesse)

Cisco Virtualized Voice Browser (Cisco VVB)

Cisco Unified Intelligence Center (Unified Intelligence Center)

Cisco Cloud Connect (Cloud Connect)

Cisco Identity Service (Cisco IdS)

Cisco Live Data

If you are upgrading from 12.6(2) to 15.0(1) SU2/ES202607, follow the compatibility tables for 12.6(2) to 15.0(1) in the Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1) .

If you are upgrading from an existing 15.0(1) deployment to 15.0(1) SU2/ES202607, there are no additional compatibility restrictions
                                 beyond those documented in the Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1) .

The 15.0(1) SU2 upgrade of any of the above components must be performed on both the publisher and subscriber in the same
                                 maintenance window. For example, both the Cloud Connect publisher and subscriber must be upgraded to 15.0(1) SU2 in the same
                                 maintenance window.

If you have Digital Channels enabled in your deployment, upgrading Cloud Connect to 15.0(1) SU2 requires a maintenance window
                                             with Cloud Connect downtime. Before upgrading, all queued or in-progress tasks must be completed or dropped on the active
                                             side. Upgrade Cloud Connect to 15.0(1) SU2 on the inactive partition of both the publisher and subscriber. Switch the version
                                             on the publisher first, followed by the subscriber. After the version is switched on the publisher and until it is switched
                                             on the subscriber, the publisher remains inactive for Digital Channels and the subscriber continues to handle all Digital
                                             Channels tasks.

The 15.0(1) VMware OVA supports the 15.0(1) base release and subsequent 15.0(1) SUs. Nutanix deployments require the separate
                                 Nutanix OVA.

The version displayed on the VOS-based component CLI does not explicitly identify the release as FCS, SU1, or SU2. Use the
                                 release identifier in the version string to identify the installed release:

15.0(1) FCS — 15.0.1. 10000 -xx

15.0(1) SU1 — 15.0.1. 10100 -xx

15.0(1) SU2 — 15.0.1. 10200 -xx

For example, 15.0.1.10200-xx identifies a 15.0(1) SU2 installation. The value after the release identifier varies by component.

For procedures on how to upgrade to the corresponding 15.0(1) SU2 version, see the solution or component's Install and Upgrade
                                 guide.

For procedures on how to install (and uninstall) the ES patches, see the Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

For Cisco Unified Customer Voice Portal (Unified CVP), the SIP.EnableSIPREC property in SIP.Property is set to FALSE by default. To enable SIPREC, set this property to TRUE .

After upgrading to ES202607, SIPREC/Port API users must synchronize the routing configuration data to the CVP CallServers
                                 using OAMP/CCE admin.

## Software Downloads for 15.0(1) SU2/ES202607

The following table lists the ES download links for each component:

Component

Download Links

Download Link

Download Link

Download Link

Download Link

The following table lists the SU download links for each component:

Component

Download Links

Unified CCE Download Link

Packaged CCE Download Link

Download Link

Download Link

Download Link

Download Link

## Cisco Security
                        	 Advisories

The Cisco Product Security Incident Response Team (PSIRT) is a dedicated, global team that manages the receipt, investigation,
                              and public reporting of security vulnerability information that relates to Cisco products and networks.

For information on
                              		  existing security issues, see Cisco
                                 			 Security Advisories, Responses, and Alerts at https://tools.cisco.com/security/center/publicationListing.x .

| Note | All features, caveats, and limitations listed in these release notes also apply to Packaged CCE, unless explicitly stated
                                       otherwise. |
|---|---|

| Note | If you have Digital Channels enabled in your deployment, upgrading Cloud Connect to 15.0(1) SU2 requires a maintenance window
                                             with Cloud Connect downtime. Before upgrading, all queued or in-progress tasks must be completed or dropped on the active
                                             side. Upgrade Cloud Connect to 15.0(1) SU2 on the inactive partition of both the publisher and subscriber. Switch the version
                                             on the publisher first, followed by the subscriber. After the version is switched on the publisher and until it is switched
                                             on the subscriber, the publisher remains inactive for Digital Channels and the subscriber continues to handle all Digital
                                             Channels tasks. |
|---|---|

| Component | Download Links |
|---|---|
| Cisco Unified Customer Voice Portal (Unified CVP) | Download Link |
| Cisco Enterprise Chat and Email (ECE) | Download Link |
| Cisco Unified Contact Center Management Portal (Unified CCMP) | Download Link |
| Logger | Download Link |
| Router |
| Administration & Data Server |
| PG |

| Component | Download Links |
|---|---|
| Cisco Reverse Proxy | Unified CCE Download Link Packaged CCE Download Link |
| Cloud Connect | Download Link |
| Cisco VVB | Download Link |
| Finesse | Download Link |
| Unified Intelligence Center | Download Link |
| Cisco IdS |
| Live Data |