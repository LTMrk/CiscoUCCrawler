---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-tls-tls-1-2-configuration-overview-guide-html-941b8d1eef
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/TLS/TLS-1-2-Configuration-Overview-Guide.html
retrieved_at: 2026-08-16T18:28:07.663668+00:00
---

TLS 1.2 Configuration Overview Guide

# TLS 1.2 Configuration Overview Guide

### Download Options

Updated: April 20, 2018

TLS 1.2 Configuration Overview Guide

First Published : April 20, 2018

Last Updated: June 4, 2018

## Overview

For security or compliance reasons, administrators can choose to lock down the TLS version of many Cisco Collaboration products to 1.2, and therefore disable TLS 1.0 and TLS 1.1. For an overview, considerations, and implications of enabling TLS 1.2 and disabling TLS 1.0 or 1.1, see the TLS 1.2 for On-Premises Cisco Collaboration Deployments available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/products-configuration-examples-list.html .

This document provides an overview on how to enable TLS 1.2 and disable TLS 1.0 and 1.1 for Cisco Collaboration products. It also provides references to the relevant product documentation.

## Configuration

The following table outlines how to configure your Cisco Collaboration products for TLS 1.2.

Prerequisite: Before configuring your products for TLS 1.2, verify that your product versions can enable TLS 1.2 and disable TLS 1.0 and 1.1. For a list of product versions with this capability, see the TLS 1.2 Compatibility Matrix for Cisco Collaboration Products : https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/TLS/TLS1-2-Compatibility-Matrix.html .

Note: You can configure TLS 1.2 and disable TLS 1.0 and 1.1 for the following products in any order.

Table 1. Configure Collaboration Products for TLS 1.2

Product

How to Configure TLS 1.2

References to Product Documentation

Call Control

Cisco Unified Communications Manager and IM and Presence Service

Use CLI Command:

set tls min-version <1.0 | 1.1 | 1.2>

TLS Setup chapter in the Security Guide for Cisco Unified Communications Manager, Release 11.5(1)SU3 or later, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Cisco Unified Survivable Remote Site Telephony

Use CLI Command:

sip-ua transport tcp tls [v1.0 | v1.1 | v1.2]

Cisco Unified SCCP and SIP SRST System Administrator Guide , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-survivable-remote-site-telephony/products-installation-and-configuration-guides-list.html .

Conferencing

Cisco Meeting Server

Use CLI Command:

tls <sip | ldap | webadmin> min-tls-version <1.0 | 1.1 | 1.2>

Cisco Meeting Server MMP Command Line Reference, Release 2.3 or later, available at https://www.cisco.com/c/en/us/support/conferencing/meeting-server/products-programming-reference-guides-list.html .

Cisco Meeting Management

No command necessary. TLS 1.1 and 1.0 are disabled.

Cisco Meeting Management 1.0.1 Release Notes : https://www.cisco.com/c/dam/en/us/td/docs/conferencing/Cisco-Meeting-Management/Release-Notes/Cisco-Meeting-Management-Release-Notes-1-0-1.pdf .

Cisco TelePresence Management Suite

Edit Windows Registry.

Refer to Microsoft documentation. For example, https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn786418(v=ws.11) .

Cisco TelePresence Management Suite Extension for Microsoft Exchange

Edit Windows Registry.

Refer to Microsoft documentation. For example, https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn786418(v=ws.11) .

Cisco TelePresence Conductor

TLS 1.0/1.1 is disabled by default with XC4.3.2.

Cisco TelePresence Conductor XC4.3.2, Release Notes , available at https://www.cisco.com/c/dam/en/us/td/docs/telepresence/infrastructure/conductor/release_note/TelePresence-Conductor-Release-Notes-XC4-3-2.pdf .

Cisco TelePresence Conductor Administrator Guide , XC4.3.2 or later, available at https://www.cisco.com/c/en/us/support/conferencing/telepresence-conductor/products-maintenance-guides-list.html .

Enterprise Edge

Cisco Expressway Series

You can configure the cipher suite and minimum supported TLS version for each service on the Maintenance > Security > Ciphers page of the product’s web UI.

Cisco Expressway Administrator Guide (X8.10) or later, available at https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-maintenance-guides-list.html .

Cisco Unified Border Element (CUBE)

Use CLI Command:

sip-ua transport tcp tls [v1.0 | v1.1 | v1.2]

Cisco Unified Border Element Configuration Guide , available at https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/configuration/cube-book/voi-cube-sip-tls.html .

SIP PSTN Gateway

Use CLI Command:

sip-ua transport tcp tls [v1.0 | v1.1 | v1.2]

Cisco Unified Border Element Configuration Guide , available at https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/configuration/cube-book/voi-cube-sip-tls.html .

Server Applications

Cisco Emergency Responder

For pre 12.0(1)SU1, install cop file.

For 12.0(1)SU1+, use CLI command:

set tls min-version <1.0 | 1.1 | 1.2>

Cisco Emergency Responder Version 12.0(1)SU(1) Release Notes or later, available at https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/products-release-notes-list.html .

Voicemail and Messaging

Cisco Unity Connection

Use CLI Command:

set tls min-version <1.0 | 1.1 | 1.2>

IP Communications Required by Cisco Unity Connection chapter in the Security Guide for Cisco Unity Connection Release 12.x or later, available at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-user-guide-list.html .

Endpoints

Cisco IP Phone 7800 and 8800 Series

From Cisco Unified CM, set “ Disable TLS 1.0 and TLS 1.1 for Web Access ” to enabled or disabled .

TLS Setup chapter of Security Guide for Cisco Unified Communications Manager, Release 11.5(1)SU3 or later, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Cisco IP Phone Administration chapter in Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager , available at https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/products-maintenance-guides-list.html .

Cisco IP Phone Administration chapter in Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager , available at https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-maintenance-guides-list.html .

Cisco TelePresence  SX/MX/DX Series running the CE software

TLS 1.0 is always disabled starting from CE8.1.0. To disable TLS 1.1, in the endpoint web interface, go to Setup > Configuration > NetworkServices > ServerMinimumTLSVersion .

Cisco TelePresence SX, MX, and DX Series, Collaboration Endpoint Software 8 Release Notes : https://www.conferenceroomav.com/pdf/ce-software-release-notes-ce8%20collaboration%20software.pdf .

Cisco Webex Room Kit & Plus

TLS 1.0 is always disabled. To disable TLS 1.1, in the endpoint web interface, go to Setup > Configuration > NetworkServices > ServerMinimumTLSVersion .

https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit/model.html

https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-plus/model.html

Cisco TelePresence C/SX/EX/MX/Profile Series running the TC software

TLS 1.0 is always disabled on the HTTPS web interface. TLS 1.1 and TLS 1.2 are always allowed.

Cisco TelePresence System C/SX/EX/MX/Profile Series Software release notes TC 7 : https://www.cisco.com/c/dam/en/us/td/docs/telepresence/endpoint/software/tc7/release_notes/tc-software-release-notes-tc7.pdf .

Cisco TelePresence IX5000

TLS 1.0 and 1.1 are disabled by default since IX 8.2.2.

Release Notes for Cisco TelePresence System Software Release IX 8 , available at https://www.cisco.com/c/en/us/td/docs/telepresence/ix_sw/8_x/release/notes/ix_release_notes.html .

Cisco Jabber

Not applicable. There is no TLS server interface.

https://www.cisco.com/c/en/us/products/unified-communications/jabber/index.html

Service Management

Cisco Prime Collaboration (Provisioning)

TLS 1.0 and 1.1 are disabled on the TLS server interface (HTTPS).

https://www.cisco.com/c/en/us/support/cloud-systems-management/prime-collaboration/tsd-products-support-series-home.html

Cisco Prime Collaboration (Deployment)

Use CLI Command:

set tls min-version <1.0 | 1.1 | 1.2>

Minimum TLS Version Control chapter in the Cisco Prime Collaboration Deployment Administration Guide, Release 12.0(1) or later, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Cisco Prime License Manager

Use CLI Command:

set tls min-version <1.0 | 1.1 | 1.2>

Cisco Prime License Manager User Guide, Release 11.5(1)SU2 , available at https://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html .

Communication Gateways

STC App and Cisco VG Series Gateways

Use CLI Command:

stcapp security tls-version v1.2

Configuring Voice Functionality chapter in Cisco 4000 Series ISRs Software Configuration Guide, Cisco IOS XE Fuji 16.7.x or later, available at https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/products-installation-and-configuration-guides-list.html .

Other

IOS MTP/CFB

Use CLI Command:

dspfarm profile <n> conference security tls-version <v1.0 | v1.1 | v1.2>

Cisco 4000 Series ISRs Software Configuration Guide , available at https://www.cisco.com/c/en/us/td/docs/routers/access/4400/software/configuration/xe-16-7/isr4400swcfg-xe-16-7-book/configuring_voice_functionality.html .

## Documentation Changes

Table 2. Documentation Changes

Date

Change

June 4, 2018

Added Cisco IP Phone 7800 and 8800 Series to table.

Updated product names from Cisco Spark to Cisco Webex.

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see What’s New in Cisco Product Documentation .

To receive new and revised Cisco technical content directly to your desktop, you can subscribe to the What’s New in Cisco Product Documentation RSS feed . The RSS feeds are a free service.

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS” WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies are considered un-Controlled copies and the original on-line version should be referred to for latest version.

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at www.cisco.com/go/offices .

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

© 2018 Cisco Systems, Inc. All rights reserved.

| Product | How to Configure TLS 1.2 | References to Product Documentation |
|---|---|---|
| Call Control |
| Cisco Unified Communications Manager and IM and Presence Service | Use CLI Command: set tls min-version <1.0 \| 1.1 \| 1.2> | TLS Setup chapter in the Security Guide for Cisco Unified Communications Manager, Release 11.5(1)SU3 or later, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Cisco Unified Survivable Remote Site Telephony | Use CLI Command: sip-ua transport tcp tls [v1.0 \| v1.1 \| v1.2] | Cisco Unified SCCP and SIP SRST System Administrator Guide , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-survivable-remote-site-telephony/products-installation-and-configuration-guides-list.html . |
| Conferencing |
| Cisco Meeting Server | Use CLI Command: tls <sip \| ldap \| webadmin> min-tls-version <1.0 \| 1.1 \| 1.2> | Cisco Meeting Server MMP Command Line Reference, Release 2.3 or later, available at https://www.cisco.com/c/en/us/support/conferencing/meeting-server/products-programming-reference-guides-list.html . |
| Cisco Meeting Management | No command necessary. TLS 1.1 and 1.0 are disabled. | Cisco Meeting Management 1.0.1 Release Notes : https://www.cisco.com/c/dam/en/us/td/docs/conferencing/Cisco-Meeting-Management/Release-Notes/Cisco-Meeting-Management-Release-Notes-1-0-1.pdf . |
| Cisco TelePresence Management Suite | Edit Windows Registry. | Refer to Microsoft documentation. For example, https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn786418(v=ws.11) . |
| Cisco TelePresence Management Suite Extension for Microsoft Exchange | Edit Windows Registry. | Refer to Microsoft documentation. For example, https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn786418(v=ws.11) . |
| Cisco TelePresence Conductor | TLS 1.0/1.1 is disabled by default with XC4.3.2. | Cisco TelePresence Conductor XC4.3.2, Release Notes , available at https://www.cisco.com/c/dam/en/us/td/docs/telepresence/infrastructure/conductor/release_note/TelePresence-Conductor-Release-Notes-XC4-3-2.pdf . Cisco TelePresence Conductor Administrator Guide , XC4.3.2 or later, available at https://www.cisco.com/c/en/us/support/conferencing/telepresence-conductor/products-maintenance-guides-list.html . |
| Enterprise Edge |
| Cisco Expressway Series | You can configure the cipher suite and minimum supported TLS version for each service on the Maintenance > Security > Ciphers page of the product’s web UI. | Cisco Expressway Administrator Guide (X8.10) or later, available at https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-maintenance-guides-list.html . |
| Cisco Unified Border Element (CUBE) | Use CLI Command: sip-ua transport tcp tls [v1.0 \| v1.1 \| v1.2] | Cisco Unified Border Element Configuration Guide , available at https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/configuration/cube-book/voi-cube-sip-tls.html . |
| SIP PSTN Gateway | Use CLI Command: sip-ua transport tcp tls [v1.0 \| v1.1 \| v1.2] | Cisco Unified Border Element Configuration Guide , available at https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/configuration/cube-book/voi-cube-sip-tls.html . |
| Server Applications |
| Cisco Emergency Responder | For pre 12.0(1)SU1, install cop file. For 12.0(1)SU1+, use CLI command: set tls min-version <1.0 \| 1.1 \| 1.2> | Cisco Emergency Responder Version 12.0(1)SU(1) Release Notes or later, available at https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/products-release-notes-list.html . |
| Voicemail and Messaging |
| Cisco Unity Connection | Use CLI Command: set tls min-version <1.0 \| 1.1 \| 1.2> | IP Communications Required by Cisco Unity Connection chapter in the Security Guide for Cisco Unity Connection Release 12.x or later, available at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-user-guide-list.html . |
| Endpoints |
| Cisco IP Phone 7800 and 8800 Series | From Cisco Unified CM, set “ Disable TLS 1.0 and TLS 1.1 for Web Access ” to enabled or disabled . | TLS Setup chapter of Security Guide for Cisco Unified Communications Manager, Release 11.5(1)SU3 or later, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . Cisco IP Phone Administration chapter in Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager , available at https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/products-maintenance-guides-list.html . Cisco IP Phone Administration chapter in Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager , available at https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-maintenance-guides-list.html . |
| Cisco TelePresence  SX/MX/DX Series running the CE software | TLS 1.0 is always disabled starting from CE8.1.0. To disable TLS 1.1, in the endpoint web interface, go to Setup > Configuration > NetworkServices > ServerMinimumTLSVersion . | Cisco TelePresence SX, MX, and DX Series, Collaboration Endpoint Software 8 Release Notes : https://www.conferenceroomav.com/pdf/ce-software-release-notes-ce8%20collaboration%20software.pdf . |
| Cisco Webex Room Kit & Plus | TLS 1.0 is always disabled. To disable TLS 1.1, in the endpoint web interface, go to Setup > Configuration > NetworkServices > ServerMinimumTLSVersion . | https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit/model.html https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-plus/model.html |
| Cisco TelePresence C/SX/EX/MX/Profile Series running the TC software | TLS 1.0 is always disabled on the HTTPS web interface. TLS 1.1 and TLS 1.2 are always allowed. | Cisco TelePresence System C/SX/EX/MX/Profile Series Software release notes TC 7 : https://www.cisco.com/c/dam/en/us/td/docs/telepresence/endpoint/software/tc7/release_notes/tc-software-release-notes-tc7.pdf . |
| Cisco TelePresence IX5000 | TLS 1.0 and 1.1 are disabled by default since IX 8.2.2. | Release Notes for Cisco TelePresence System Software Release IX 8 , available at https://www.cisco.com/c/en/us/td/docs/telepresence/ix_sw/8_x/release/notes/ix_release_notes.html . |
| Cisco Jabber | Not applicable. There is no TLS server interface. | https://www.cisco.com/c/en/us/products/unified-communications/jabber/index.html |
| Service Management |
| Cisco Prime Collaboration (Provisioning) | TLS 1.0 and 1.1 are disabled on the TLS server interface (HTTPS). | https://www.cisco.com/c/en/us/support/cloud-systems-management/prime-collaboration/tsd-products-support-series-home.html |
| Cisco Prime Collaboration (Deployment) | Use CLI Command: set tls min-version <1.0 \| 1.1 \| 1.2> | Minimum TLS Version Control chapter in the Cisco Prime Collaboration Deployment Administration Guide, Release 12.0(1) or later, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Cisco Prime License Manager | Use CLI Command: set tls min-version <1.0 \| 1.1 \| 1.2> | Cisco Prime License Manager User Guide, Release 11.5(1)SU2 , available at https://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html . |
| Communication Gateways |
| STC App and Cisco VG Series Gateways | Use CLI Command: stcapp security tls-version v1.2 | Configuring Voice Functionality chapter in Cisco 4000 Series ISRs Software Configuration Guide, Cisco IOS XE Fuji 16.7.x or later, available at https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/products-installation-and-configuration-guides-list.html . |
| Other |
| IOS MTP/CFB | Use CLI Command: dspfarm profile <n> conference security tls-version <v1.0 \| v1.1 \| v1.2> | Cisco 4000 Series ISRs Software Configuration Guide , available at https://www.cisco.com/c/en/us/td/docs/routers/access/4400/software/configuration/xe-16-7/isr4400swcfg-xe-16-7-book/configuring_voice_functionality.html . |

| Date | Change |
|---|---|
| June 4, 2018 | Added Cisco IP Phone 7800 and 8800 Series to table. Updated product names from Cisco Spark to Cisco Webex. |