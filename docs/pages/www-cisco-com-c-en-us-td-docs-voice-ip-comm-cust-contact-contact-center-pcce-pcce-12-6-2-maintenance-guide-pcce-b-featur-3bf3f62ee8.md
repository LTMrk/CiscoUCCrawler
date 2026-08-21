---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-maintenance-guide-pcce-b-featur-3bf3f62ee8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/maintenance/guide/pcce_b_features-guide-1262/pcce_b_features-guide-1261_appendix_010010.html
retrieved_at: 2026-08-21T12:29:46.857184+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: November 15, 2024

Chapter: Avaya Support

## Chapter: Avaya Support

- Avaya Support

- Avaya Support

# Avaya Support

## Avaya Support

### Prerequisite

Make sure you have Avaya Automatic Call Distribution (ACD) versions that are compatible with Packaged CCE deployments. For
                              more information, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Avaya Support Overview

Support for Avaya ACD int has been provided in Packaged CCE 4000 and 12000 Agent deployments. You can maintain an Avaya Peripheral
                              Gateway (PG) in a Packaged CCE environment and use its intelligent contact center routing capability to route calls to geographically
                              distributed contact center sites.

For detailed information about the required Avaya configurations, see chapter Unified ICM Software Configuration in the Cisco Unified ICM ACD Supplement for Avaya Communication Manager Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Note that Avaya PG must be deployed on a separate VM. Also Avaya agents cannot be associated with a department.

### Tools that Support Avaya Configurations

Configuration Manager Tools and nodes in the Script Editor have been enabled to facilitate the support for Avaya ACD in Packaged
                              CCE 4000 and 12000 agent deployments. For the complete list of nodes and tools, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

The following restrictions apply to the tools that support Avaya PG configurations.

Configuration Manager Tool

Restriction

Agent Explorer

Only supports Avaya PG configurations

Does not support selecting persons who are already associated with the CUCM Peripheral agents

Person List

Does not list persons who are already associated with the CUCM peripheral agents

Dialed Number/Script Selector List

Supports addition of Dialed Numbers for Avaya Agents and NIC Routing Clients

Skill Group Explorer

Only supports Avaya PG configurations

Bulk Configuration Tools

The following bulk tools only support Avaya PG configurations.

Agent Bulk Insert

Dialed Number Bulk Insert

Skill Group Bulk Insert

Agent Bulk Edit

Dialed Number Bulk Edit

Skill Group Bulk Edit

Person Bulk Insert

Person Bulk Edit

For design details, scalability constraints and sizing factors, see the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html .

You can also view historical and real-time stock reports for Avaya ACD. For more information, see the Cisco Packaged Contact Center Enterprise Reporting User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

| Note | Note that Avaya PG must be deployed on a separate VM. Also Avaya agents cannot be associated with a department. |
|---|---|

| Configuration Manager Tool | Restriction |
|---|---|
| Agent Explorer | Only supports Avaya PG configurations Does not support selecting persons who are already associated with the CUCM Peripheral agents |
| Person List | Does not list persons who are already associated with the CUCM peripheral agents |
| Dialed Number/Script Selector List | Supports addition of Dialed Numbers for Avaya Agents and NIC Routing Clients |
| Skill Group Explorer | Only supports Avaya PG configurations |
| Bulk Configuration Tools | The following bulk tools only support Avaya PG configurations. Agent Bulk Insert Dialed Number Bulk Insert Skill Group Bulk Insert Agent Bulk Edit Dialed Number Bulk Edit Skill Group Bulk Edit Person Bulk Insert Person Bulk Edit |