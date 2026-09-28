---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-maintenance-guide-pcce-b-featur-e66ab13133
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_features-guide-1261/pcce_b_features-guide-1261_appendix_010100.html
retrieved_at: 2026-08-21T16:42:23.629004+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: ICM to ICM Gateway Support

## Chapter: ICM to ICM Gateway Support

- ICM to ICM Gateway Support

- ICM to ICM Gateway Support

# ICM to ICM Gateway Support

## ICM to ICM Gateway Support

### Prerequisite

Make sure you have ICM-to-ICM Gateway versions that are compatible with Packaged CCE deployments. For more information, see
                              the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### ICM-to-ICM Gateway Overview

Support for ICM-to-ICM Gateway has been provided in Packaged CCE 4000 and 12000 Agent deployments, where Packaged CCE can
                              act as a client or a server. The call requests can be routed from Packaged CCE to remote Unified CCE/Unified ICM deployments
                              and vice versa.

ICM-to-ICM Gateway extends the ICM software capability by allowing agents to simultaneously pre-route/post-route calls, and
                              supply additional call-related information to a second agent on a different ICM. This enables the initial agent to pass on
                              gathered information without the customer’s needing to repeat it to the second agent.

Following are some business scenarios where ICM-to-ICM Gateway functionality can be useful.

A customer calls the institutional department of a financial corporation for customer service assistance with a company-sponsored
                                    401k. The customer then asks to be transferred to the retail department to obtain assistance with a personal account.

Two corporations (for example, a bank and an insurance company), each of which has a contact center that uses an ICM, merge.
                                    It may often be desirable to transfer a call between the two companies; for example, to sell insurance to a bank customer.

A customer calls a hotel to make a reservation. The hotel agent then asks the customer if he/she also needs to rent a car,
                                    and then transfers the customer to a car rental agent.

A company uses an outsourcer to handle part of its overflow traffic. For example, the company service department handles paid
                                    support calls in-house but transfers warranty service requests to the outsourcer.

A multi-national corporation encompasses several geographic regions; each geographic region has its own ICM.

In all these cases, ICM-to-ICM Gateway enables the call-related data to be transferred along with the call so the customer
                              does not need to supply this information again.

For more information about ICM-to-ICM Gateway call flows and configuration, see the ICM-to-ICM Gateway User Guide for Cisco Unified ICM Enterprise & Hosted Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

### Tools Supported for ICM-to-ICM Gateway

Configuration Manager Tools and nodes in the Script Editor have been enabled to facilitate the ICM-to-ICM Gateway capability
                              in Packaged CCE 4000 and 12000 Agent deployments. For the complete list of nodes and tools, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

For design details, scalability constraints and sizing factors, see the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html .

| Note | The Application Gateway List tool only supports remote ICM configuration. |
|---|---|