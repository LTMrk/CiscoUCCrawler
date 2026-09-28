---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-vg248-1-1-english-configuration-guide-sw-confg-vg248swa-html-9f62c44610
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/vg248/1_1/english/configuration/guide/sw_confg/vg248swa.html
retrieved_at: 2026-08-22T01:19:20.598014+00:00
---

Software Configuration Guide (Version 1.1)

# Software Configuration Guide (Version 1.1)

Updated: March 17, 2015

Chapter: About This Guide

## Chapter: About This Guide

# About this Guide

## Overview

The Cisco VG248 Analog Phone Gateway Software Configuration Guide provides the information you need to configure and manage the Cisco VG248 Analog Phone Gateway (VG248) on your network.

## Audience

Network engineers, system administrators, and telecom engineers should review this guide for information about configuring and using the VG248 in the network.

The tasks described in this guide are considered to be administration-level tasks. Because of the close interaction of the VG248 with Cisco CallManager and analog telephony systems, these tasks require that you are familiar with these systems as well.

## Objectives

This guide provides the required steps to configure and manage the VG248. You must use this guide in conjunction with the Cisco VG248 Analog Phone Gateway Hardware Installation Guide to get the VG248 up and running on your network.

Because of the complexity of an IP telephony network, this guide does not provide detailed information for required procedures performed on other Cisco or third-party devices. Refer to the documentation provided with these systems for installation and configuration instructions.

## Organization

Table 1 provides an overview of the organization of this guide.

Table 1 Cisco VG248 Analog Phone Gateway Software Configuration Guide Organization

Chapter 1, "Overview"

Provides an overview of software features and how they are implemented on the VG248.

Chapter 2, "Getting Started with the VG248"

Describes the basic network settings you need to configure on the VG248.

Chapter 3, "Configuring the Telephony Settings on the VG248"

Includes the procedures for configuring the telephony settings on the VG248.

"Configuring Analog Phones Using Cisco CallManager"

Describes necessary steps in Cisco CallManager for adding and configuring the VG248 ports.

Chapter 5, "Integrating Cisco CallManager with Voice Mail Systems Using SMDI"

Provides an overview of SMDI support, configuration options, instructions for configuring, and troubleshooting tips.

Chapter 6, "Troubleshooting the VG248"

Provides troubleshooting tips for the VG248.

## Related Documentation

For information about Cisco CallManager and additional information about the VG248, refer to these publications:

• Cisco VG248 Analog Phone Gateway Hardware Installation Guide

• Cisco VG248 Analog Phone Gateway Release Notes

• Cisco CallManager Administration Guide

## Obtaining Documentation

The following sections provide sources for obtaining documentation from Cisco Systems.

### World Wide Web

You can access the most current Cisco documentation on the World Wide Web at the following sites:

• http://www.cisco.com

• http://www-china.cisco.com

• http://www-europe.cisco.com

### Documentation CD-ROM

Cisco documentation and additional literature are available in a CD-ROM package, which ships with your product. The Documentation CD-ROM is updated monthly and may be more current than printed documentation. The CD-ROM package is available as a single unit or as an annual subscription.

### Ordering Documentation

Cisco documentation is available in the following ways:

• Registered Cisco Direct Customers can order Cisco Product documentation from the Networking Products MarketPlace:

http://www.cisco.com/cgi-bin/order/order_root.pl

• Registered Cisco.com users can order the Documentation CD-ROM through the online Subscription Store:

http://www.cisco.com/go/subscription

• Nonregistered Cisco.com users can order documentation through a local account representative by calling Cisco corporate headquarters (California, USA) at 408 526-7208 or, in North America, by calling 800 553-NETS(6387).

### Documentation Feedback

If you are reading Cisco product documentation on the World Wide Web, you can submit technical comments electronically. Click Feedback in the toolbar and select Documentation. After you complete the form, click Submit to send it to Cisco.

You can e-mail your comments to bug-doc@cisco.com.

To submit your comments by mail, use the response card behind the front cover of your document, or write to the following address:

Attn Document Resource Connection Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-9883

We appreciate your comments.

## Obtaining Technical Assistance

Cisco provides Cisco.com as a starting point for all technical assistance. Customers and partners can obtain documentation, troubleshooting tips, and sample configurations from online tools. For Cisco.com registered users, additional troubleshooting tools are available from the TAC website.

### Cisco.com

Cisco.com is the foundation of a suite of interactive, networked services that provides immediate, open access to Cisco information and resources at anytime, from anywhere in the world. This highly integrated Internet application is a powerful, easy-to-use tool for doing business with Cisco.

Cisco.com provides a broad range of features and services to help customers and partners streamline business processes and improve productivity. Through Cisco.com, you can find information about Cisco and our networking solutions, services, and programs. In addition, you can resolve technical issues with online technical support, download and test software packages, and order Cisco learning materials and merchandise. Valuable online skill assessment, training, and certification programs are also available.

Customers and partners can self-register on Cisco.com to obtain additional personalized information and services. Registered users can order products, check on the status of an order, access technical support, and view benefits specific to their relationships with Cisco.

To access Cisco.com, go to the following website:

http://www.cisco.com

### Technical Assistance Center

The Cisco TAC website is available to all customers who need technical assistance with a Cisco product or technology that is under warranty or covered by a maintenance contract.

### Contacting TAC by Using the Cisco TAC Website

If you have a priority level 3 (P3) or priority level 4 (P4) problem, contact TAC by going to the TAC website:

http://www.cisco.com/tac

P3 and P4 level problems are defined as follows:

• P3—Your network performance is degraded. Network functionality is noticeably impaired, but most business operations continue.

• P4—You need information or assistance on Cisco product capabilities, product installation, or basic product configuration.

In each of the above cases, use the Cisco TAC website to quickly find answers to your questions.

To register for Cisco.com, go to the following website:

http://www.cisco.com/register/

If you cannot resolve your technical issue by using the TAC online resources, Cisco.com registered users can open a case online by using the TAC Case Open tool at the following website:

http://www.cisco.com/tac/caseopen

### Contacting TAC by Telephone

If you have a priority level 1 (P1) or priority level 2 (P2) problem, contact TAC by telephone and immediately open a case. To obtain a directory of toll-free numbers for your country, go to the following website:

http://www.cisco.com/warp/public/687/Directory/DirTAC.shtml

P1 and P2 level problems are defined as follows:

• P1—Your production network is down, causing a critical impact to business operations if service is not restored quickly. No workaround is available.

• P2—Your production network is severely degraded, affecting significant aspects of your business operations. No workaround is available.

| Chapter | Description |
|---|---|
| Chapter 1, "Overview" | Provides an overview of software features and how they are implemented on the VG248. |
| Chapter 2, "Getting Started with the VG248" | Describes the basic network settings you need to configure on the VG248. |
| Chapter 3, "Configuring the Telephony Settings on the VG248" | Includes the procedures for configuring the telephony settings on the VG248. |
| "Configuring Analog Phones Using Cisco CallManager" | Describes necessary steps in Cisco CallManager for adding and configuring the VG248 ports. |
| Chapter 5, "Integrating Cisco CallManager with Voice Mail Systems Using SMDI" | Provides an overview of SMDI support, configuration options, instructions for configuring, and troubleshooting tips. |
| Chapter 6, "Troubleshooting the VG248" | Provides troubleshooting tips for the VG248. |