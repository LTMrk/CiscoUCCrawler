---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-administrat-36ba8b06c3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/administration/guide/ucce_b_administration-guide-for-cisco-unified12_5/ucce_b_administration-guide-for-cisco-unified12_5_chapter_011.html
retrieved_at: 2026-08-16T20:47:28.333477+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

# Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

Updated: February 7, 2019

Chapter: Routing Tasks Multichannel Options

## Chapter: Routing Tasks Multichannel Options

# Routing Tasks Multichannel Options

## Task Routing for Third-Party Multichannel Applications

Task
                                    					Routing APIs provide a standard way to request,
                              				queue, route, and handle third-party multichannel tasks in CCE.

Contact Center customers or partners can develop applications using Customer Collaboration Platform and Finesse APIs in order to use Task Routing . The Customer Collaboration Platform Task API enables applications to submit nonvoice task requests to CCE. The Finesse APIs enable agents to sign into different
                              types of media and handle the tasks. Agents sign into and manage their state in each media independently.

Cisco partners can use the sample code available on Cisco DevNet as a guide for building these applications ( https://developer.cisco.com/site/task-routing/ ).

For information about configuring Task Routing for third-party multichannel applications, see the Cisco Unified Contact Center Enterprise Features Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

## Routing Unified Interaction Manager Tasks

### Unified CCE Configuration for Multichannel Routing

To route contact requests submitted from the World Wide Web or email,
                                 		  you must configure:

Media Routing Peripheral Gateway

Media Routing Domains and Media Classes

Multichannel agents

Application instances

Administration connections

Multichannel skill groups

Multichannel routing scripts

For more information about configuring Unified CCE for multichannel routing with Unified Interaction Manager,
                                 		  see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

When implementing Task Routing for third-party multichannel applications, some of the configuration in the list above is provided by default or automated.
                                             See the Cisco Unified Contact Center Enterprise Features Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

### Multichannel Software Configuration

After you complete your Unified ICM/Unified CCE configuration, you must configure your Unified ICM multichannel software.

The multichannel software you must configure includes Enterprise Chat and
                                       						Email .

For more information about how to administer this component, see Enterprise Chat and
                                       						Email Installation Guides and Administration Guides at

https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html , and

| Note | When implementing Task Routing for third-party multichannel applications, some of the configuration in the list above is provided by default or automated.
                                             See the Cisco Unified Contact Center Enterprise Features Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html |
|---|---|