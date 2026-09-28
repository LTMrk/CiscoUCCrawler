---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-enterprise-14-collbcvd-preface-html-dcfc4ffc6e
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/enterprise/14/collbcvd/preface.html
retrieved_at: 2026-08-16T18:22:56.233321+00:00
---

Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployments, CVD

# Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployments, CVD

Updated: May 21, 2021

Chapter: Preface

## Chapter: Preface

# Preface

Revised: May 21, 2021

Cisco Validated Designs (CVDs) explain important design and deployment decisions based on common use cases and current system releases. They incorporate a broad set of technologies, features, and applications to address customer needs. Cisco engineers have comprehensively tested and documented the guidelines within the CVDs in order to provide faster, more reliable, and fully predictable deployment. CVDs provide a tested starting point for Cisco partners and customers to begin designing and deploying systems using their own setup and configuration.

## Documentation for Enterprise Collaboration

Cisco Preferred Architecture (PA) Design Overview guides help customers and sales teams select the appropriate architecture based on an organization's business requirements; understand the products that are used within the architecture; and obtain general design best practices. These guides support sales processes.

Cisco Validated Design (CVD) guides provide detailed steps for deploying the Cisco Preferred Architectures. These guides support planning, design, and implementation of the Preferred Architectures.

Alternative Design Guides — Are post-sales documents that describe optional designs that can be deployed as alternatives to the Preferred Architectures described in the PA overview guides and CVDs. The alternative design may start with the main PA as a foundation and build upon it; therefore, each alternative design guide may be used in conjunction with its corresponding PA overview guide and CVD. In some cases the Alternative Design Guides can be used as standalone guides.

Cisco Collaboration System Solution Reference Network Design (SRND) guide provides detailed design options for Cisco Collaboration. The SRND should be referenced when design requirements are outside the scope of Cisco Preferred Architectures.

## About This Guide

This Cisco Validated Design guide for the Cisco Enterprise Collaboration Preferred Architecture is for:

- Sales teams that sell, design, and deploy collaboration solutions

- Customers and sales teams who want detailed design best practices and ordered steps for deploying Cisco Collaboration

Readers of this guide should have a general knowledge of Cisco voice, video, and collaboration products and a basic understanding of how to deploy these products. We recommend that readers review the Preferred Architecture for Cisco Collaboration System Release14 On-Premises Deployments, Design Overview before reading this CVD document.

The design decisions within this CVD are in line with the framework outlined in the latest version of the Cisco Collaboration SRND . While the SRND offers many design and deployment options, in this document a single deployment recommendation is selected based on fundamental assumptions for the Preferred Architecture design. Different assumptions can certainly lead to different design decisions, which then should be validated against the SRND. For large deployments with unique needs and advanced customization, it is recommended to work with your Cisco Account Manager for guidance beyond that contained in this CVD or the SRND.

This guide simplifies the design and sales process by:

- Building upon the product and design recommendations of the Preferred Architecture for Cisco Collaboration System Release14 On-Premises Deployments, Design Overview

- Detailing a collaboration architecture, identifying best practices, and explaining the reasoning behind those recommendations

This CVD guide is organized into the following discrete modules that integrate together to form the overall Collaboration solution:

- Call Control — Explains fundamental concepts of dial plan design, Computer Telephony Integration (CTI), Survivable Remote Site Telephony (SRST), IM and Presence, LDAP directory integration, SIP trunks, and other aspects of call control. This chapter also lists the best practices for deploying call control in the Enterprise Collaboration Preferred Architecture.

- Conferencing — Describes the types of conferences available in the Enterprise Collaboration Preferred Architecture and explains how to deploy conferencing capability.

- Collaboration Edge — Explains how to deploy Cisco Collaboration Edge components to provide remote registration services, external communications, and interoperability.

- Voice Messaging — Lists the various applications and deployment tools available in the Enterprise Collaboration Preferred Architecture, and focuses on two core applications for unified messaging and conference scheduling.

- Collaboration Management Services — Lists the core management applications that are considered to be a basic requirement and foundational to any collaboration solution such as Cisco Prime Collaboration Deployment to assists with installation of applications, Cisco Smart Software Manager an Internet-based Cisco cloud service with web portal for managing collaboration user licenses and Cisco Webex Cloud-Connected UC (CCUC) providing centralized on-premises application analytics and operations from Webex Control Hub.

- Security — Provides simplified guidance on network access security, toll-fraud access protection, certificate management, and encryption for the Cisco Preferred Architecture (PA) for Enterprise Collaboration.

- Bandwidth Management — Provides a holistic approach to bandwidth management that incorporates an end-to-end Quality of Service (QoS) architecture, call admission control, and video rate adaptation and resiliency mechanisms to ensure the best possible user experience for deploying pervasive video over managed and unmanaged networks

- Sizing — Provides simplified sizing examples to size the components of the Enterprise Collaboration Preferred Architecture to fit the requirements of your deployment.

## Revision History

This CVD guide may be updated at any time without notice. You can obtain the latest version of this document online at:

https://www.cisco.com/go/pa

Visit the above website periodically and check for documentation updates by comparing the revision date of your copy with the revision date of the online document.

Table 1 lists the revision history for this document.

Table 1 Revision History for This CVD Guide

May 21, 2021

This document was created for Cisco Collaboration System Release (CSR) 14.

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering additional information, see What’s New in Cisco Product Documentation at: https://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html .

Subscribe to What’s New in Cisco Product Documentation , which lists all new and revised Cisco technical documentation, as an RSS feed and deliver content directly to your desktop using a reader application. The RSS feeds are a free service.

## Conventions

This document uses the following conventions:

bold font

Commands and keywords and user-entered text appear in bold font.

italic font

Document titles, new or emphasized terms, and arguments for which you supply values are in italic font.

[ ]

Elements in square brackets are optional.

{x | y | z }

Required alternative keywords are grouped in braces and separated by vertical bars.

[ x | y | z ]

Optional alternative keywords are grouped in brackets and separated by vertical bars.

string

A nonquoted set of characters. Do not use quotation marks around the string or the string will include the quotation marks.

courier font

Terminal sessions and information the system displays appear in courier font.

< >

Nonprinting characters such as passwords are in angle brackets.

[ ]

Default responses to system prompts are in square brackets.

!, #

An exclamation point (!) or a pound sign (#) at the beginning of a line of code indicates a comment line.

Note Means reader take note . Notes contain helpful suggestions or references to material not covered in the manual.

Tip Means the following information will help you solve a problem . The tips information might not be troubleshooting or even an action, but could be useful information, similar to a Timesaver.

Timesaver Means the described action saves time . You can save time by performing the action described in the paragraph.

Warning IMPORTANT SAFETY INSTRUCTIONS This warning symbol means danger. You are in a situation that could cause bodily injury. Before you work on any equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. Use the statement number provided at the end of each warning to locate its translation in the translated safety warnings that accompanied this device. SAVE THESE INSTRUCTIONS

Warning Statements using this symbol are provided for additional information and to comply with regulatory and customer requirements.

| Revision Date | Comments |
|---|---|
| May 21, 2021 | This document was created for Cisco Collaboration System Release (CSR) 14. |

| Convention | Indication |
|---|---|
| bold font | Commands and keywords and user-entered text appear in bold font. |
| italic font | Document titles, new or emphasized terms, and arguments for which you supply values are in italic font. |
| [ ] | Elements in square brackets are optional. |
| {x \| y \| z } | Required alternative keywords are grouped in braces and separated by vertical bars. |
| [ x \| y \| z ] | Optional alternative keywords are grouped in brackets and separated by vertical bars. |
| string | A nonquoted set of characters. Do not use quotation marks around the string or the string will include the quotation marks. |
| courier font | Terminal sessions and information the system displays appear in courier font. |
| < > | Nonprinting characters such as passwords are in angle brackets. |
| [ ] | Default responses to system prompts are in square brackets. |
| !, # | An exclamation point (!) or a pound sign (#) at the beginning of a line of code indicates a comment line. |