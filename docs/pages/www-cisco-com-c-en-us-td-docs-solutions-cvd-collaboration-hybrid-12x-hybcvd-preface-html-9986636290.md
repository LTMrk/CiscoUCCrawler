---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-hybrid-12x-hybcvd-preface-html-9986636290
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/hybrid/12x/hybcvd/preface.html
retrieved_at: 2026-08-16T18:25:12.807013+00:00
---

Preferred Architecture for Cisco Webex Hybrid Services, CVD

# Preferred Architecture for Cisco Webex Hybrid Services, CVD

Updated: December 21, 2017

Chapter: Preface

## Chapter: Preface

# Preface

Revised: May 31, 2019

Cisco Validated Designs (CVDs) explain important design and deployment decisions based on common use cases and current system releases. They incorporate a broad set of technologies, features, and applications to address customer needs. Cisco engineers have comprehensively tested and documented the guidelines within the CVDs in order to provide faster, more reliable, and fully predictable deployments. CVDs provide a tested starting point for Cisco partners and customers to begin designing and deploying systems using their own setup and configuration.

## Documentation for Collaboration Solutions

Cisco Preferred Architecture (PA) Design Overview guides help customers and sales teams select the appropriate architecture based on an organization's business requirements; understand the products that are used within the architecture; and obtain general design best practices. These guides support sales processes.

Cisco Validated Design (CVD) guides provide detailed steps for deploying the Cisco Preferred Architectures. These guides support planning, design, and implementation of the Preferred Architectures.

Cisco Collaboration System Solution Reference Network Design (SRND) guide provides detailed design options for Cisco Collaboration solutions. The SRND should be referenced when design requirements are outside the scope of Cisco Preferred Architectures.

## About This Guide

This Cisco Validated Design guide for the Webex Hybrid Services Preferred Architecture is for:

- Sales teams that sell, design, and deploy collaboration solutions

- Customers and sales teams who want detailed design best practices and ordered steps for deploying Webex Hybrid Services

Readers of this guide should have a general knowledge of Cisco voice, video, and collaboration products and a basic understanding of how to deploy those products. We recommend that readers review the Preferred Architecture for Cisco Webex Hybrid Services, Design Overview before reading this CVD document.

The design decisions within this CVD are in line with the framework outlined in the latest version of the Cisco Collaboration SRND . While the SRND offers many design and deployment options, in this document a single deployment recommendation is selected based on fundamental assumptions for the Preferred Architecture design. Different assumptions can certainly lead to different design decisions, which then should be validated against the SRND. For large deployments with unique needs and advanced customization, we recommend working with your Cisco Account Manager for guidance beyond that contained in this CVD or the SRND.

This guide simplifies the design and sales process by:

- Building upon the product and design recommendations of the Preferred Architecture for Cisco Webex Hybrid Services, Design Overview

- Detailing a collaboration architecture, identifying best practices, and explaining the reasoning behind those recommendations

This CVD guide is organized into the following discrete modules that integrate together to form the overall hybrid services solution:

- Cisco Webex Hybrid Directory Service — Simplifies user on-boarding by integrating directory services between the on-premises LDAP directory and the common identity service within the customer's Webex organization. This chapter describes, at a high level, how to deploy Webex Hybrid Directory Service within the Webex Hybrid Services solution.

- Cisco Webex Hybrid Calendar Service — Improves the end-user experience for managing meeting invitations, content, and communications with participants by synchronizing enterprise calendar services with the Webex Hybrid Calendar Service. This chapter describes, at a high level, how to deploy Webex Hybrid Calendar Service within the Webex Hybrid Services solution.

- Cisco Webex Video Mesh — Allows organizations to deploy an instance of Webex media processing on-premises so that Webex Teams endpoints and applications can terminate media on-premises instead of sending all media to the cloud. This chapter describes, at a high level, how to deploy Webex Video Mesh within the Webex Hybrid Services solution.

- Cisco Webex Hybrid Call Service — Provides integration of Cisco Unified Communications Manager call services with Webex. This chapter describes, at a high level, how to deploy Webex Hybrid Call Service within the Webex Hybrid Services solution.

- Bandwidth Management — Seeks to provide the best possible user experience end-to-end for all media capable endpoints, clients, and applications in the collaboration solution. This chapter describes, at a high level, how to deploy recommended bandwidth management techniques within the Webex Hybrid Services solution.

- Sizing Cisco Webex Hybrid Services — This chapter provides simplified examples to illustrate how to size the components of the Preferred Architecture for Webex Hybrid Services to fit the requirements of your deployment.

## Revision History

This CVD guide may be updated at any time without notice. You can obtain the latest version of this document online at:

https://www.cisco.com/go/pa

Visit the above website periodically and check for documentation updates by comparing the revision date of your copy with the revision date of the online document.

Table 1 lists the revision history for this document.

Table 1 Revision History for This CVD Guide

May 31, 2019

The architecture was updated to remove Call Service Aware. Other changes and corrections were made in various chapters.

February 11, 2019

Minor errors were corrected in several sections.

June 1, 2018

This document was updated with information for a new release of Cisco Webex Hybrid Services.

December 21, 2017

Initial release of this document.

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
| May 31, 2019 | The architecture was updated to remove Call Service Aware. Other changes and corrections were made in various chapters. |
| February 11, 2019 | Minor errors were corrected in several sections. |
| June 1, 2018 | This document was updated with information for a new release of Cisco Webex Hybrid Services. |
| December 21, 2017 | Initial release of this document. |

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