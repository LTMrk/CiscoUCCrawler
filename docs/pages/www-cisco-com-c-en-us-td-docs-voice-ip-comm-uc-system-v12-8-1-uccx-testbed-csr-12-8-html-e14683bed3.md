---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-v12-8-1-uccx-testbed-csr-12-8-html-e14683bed3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/V12_8_1/uccx_testbed_csr_12_8.html
retrieved_at: 2026-08-16T18:27:21.030351+00:00
---

Unified CCX Test Bed Description for CSR 12.8

# Unified CCX Test Bed Description for CSR 12.8

- 12.8

- 12.5(1)

### Download Options

Updated: August 24, 2020

Cisco Unified Contact Center Express Test Bed for Collaboration Systems Release 12.8

First Published : August 21, 2020

NOTE: Works with document’s Advanced Properties “First Published” property. Click File | Properties | Advanced Properties | Custom .

## Overview

This document describes the Cisco Unified Contact Center Express (Unified CCX) test bed that was used to complete Cisco Collaboration Systems Release 12.8 testing. The test bed is designed to simulate a medium-sized inbound and outbound contact center with local and remote agents. It uses Unified CCX for call treatment and queuing and Cisco Unified Communications Manager (Unified Communications Manager) for call control.

This test bed is designed to implement and test some of the design considerations and guidelines of the Cisco Collaboration Systems Release 12.x Solution Reference Network Designs (SRND) , and Cisco Unified Contact Center Express SRND .

For information about how to install and configure these and other Contact Center components, see Components Installation and Configuration Guides at: Cisco Collaboration Systems for Contact Center Release 12.8 .

More configuration information for contact center components is available at: Configuration Examples and TechNotes .

## Unified CCX Test Bed and Deployment Architecture

This Unified CCX test bed is designed to replicate a 400 agent inbound and outbound contact center in multiple sites with agents located locally. The test bed design has two data centers separated across a WAN.

The entire deployment uses two data centers connected through a high-speed WAN for redundancy. All solution components are designed for high availability (HA) wherever possible. The figure provides an overview of the Unified CCX Test Bed and Deployment Architecture.

Figure 1: Collaboration Systems Release 12.8: Unified CCX Test Architecture

## General Deployment Options

Cisco Unified Contact Center Express (Unified CCX) provides a secure, highly available, and easy to deploy customer interaction management solution for up to 400 agents. This integrated solution is intended for both formal and informal contact centers.

Unified CCX provides options to address multiple functional areas such as:

■ Inbound voice

■ Outbound campaign

■ Agent email

■ Mobile and Remote Access

Other components included are:

■ Web-based reports

■ Cisco SocialMiner user licenses for social forum activity monitoring and follow-up

■ Web-based Cisco Finesse desktops

You can deploy these options on Cisco Unified Communications on Cisco Unified Computing System (Cisco Unified Communications on Cisco UCS) or any other equivalent specification-based third-party virtual servers with the supported deployment models.

As a part of testing, we completed sanity call flow testing for the following features:

### Cisco Headset and Finesse Integration

Cisco Finesse is the next generation browser-based agent and supervisor desktop for Unified CCX. Cisco Finesse is an alternative to Cisco Agent Desktop, Cisco Supervisor Desktop, and Cisco Desktop Administrator. Cisco Finesse is available with enhanced and premium license packages and provides typical inbound voice functionality. It supports Unified Communications Manager-based silent monitoring and workflow-based recording as well as Work Force Optimization (WFO).

Cisco Headset and Finesse Integration improves productivity of contact center agents by enabling them to change the Ready/Not Ready status from their Cisco headset. This feature is targeted to Contact Center customers whom also integrate with Cisco Unified Communications Manager.

### Cisco Unified Communications Mobile and Remote Access

Cisco Unified Communications Mobile and Remote Access (MRA) is a core part of the Cisco Collaboration Edge Architecture. It allows endpoints such as the Cisco IP Phone 7800 and 8800 Series and the Cisco DX Series to have their registration, call control, provisioning, messaging, and presence services provided by Unified Communications Manager when the endpoint is not within the enterprise network. Cisco Expressway provides secure firewall traversal and line-side support for Unified Communications Manager registrations.

For more deployment information about Mobile and Remote Access through Cisco Expressway, see https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html .

### 44XX Gateway Support

The Cisco 4451x Router runs on IOS-XE Software. The Cisco IOS-XE Software is designed to provide modular packaging, feature velocity, and powerful resiliency.

### Cisco Finesse

Cisco Finesse is the next generation browser-based agent and supervisor desktop for Unified CCX. Cisco Finesse is an alternative to Cisco Agent Desktop, Cisco Supervisor Desktop, and Cisco Desktop Administrator. Cisco Finesse is available with enhanced and premium license packages and provides typical inbound voice functionality. It supports Unified Communications Manager-based silent monitoring and workflow-based recording as well asF Work Force Optimization (WFO).

### Unified CCX Predictive and Progressive Agent Outbound

The outbound feature provides outbound dialing functionality in addition to existing Unified CCX inbound capabilities. This feature allows agents who are not busy with inbound calls to handle outbound calls.

With the Outbound feature, Unified CCX places customer calls using the Unified Communications Manager.

Agent Predictive and Progressive Dialer leverages the call control and Call Progress Analysis (CPA) from SIP gateway. The SIP gateway performs call progressive analysis of the call and informs the outcome of the call to Unified CCX. All the dialed contacts, which are live voice, are connected to an agent and the remaining calls are disconnected.

THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS” WITH ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING, WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

All printed copies and duplicate soft copies are considered un-Controlled copies and the original on-line version should be referred to for latest version.

Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at www.cisco.com/go/offices .

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

© 2020 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Collaboration Systems Release 12.5