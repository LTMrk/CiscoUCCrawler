---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-configuration-guide-pcce-b-admi-b141f0d5d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/configuration/guide/pcce_b_admin-and-config-guide_12_5/pcce_b_admin-and-config-guide_12_5_chapter_0100.html
retrieved_at: 2026-08-21T04:44:16.879819+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

Updated: June 11, 2024

Chapter: Configuration
	 Manager

## Chapter: Configuration
	 Manager

- Configuration                              	 Manager

- Permanent Deletion

- Packaged CCE 4000 and 12000 Agent Supported Tools

# Configuration
                     	 Manager

You perform most
                        		Packaged CCE configuration with the Unified CCE Administration gadgets. Limited
                        		configuration is performed in the legacy Configuration Manager toolset. This
                        		section describes the tools in Configuration Manager and explains how and why
                        		to access them for Packaged CCE.

## Permanent Deletion

Some objects are "marked for deletion" only in Unified CCE Administration. They remain in the system for reporting and record-keeping purposes. Follow this procedure
                              to  delete them permanently:

Step 1

Open Configuration Manager.

Step 2

Select Tools > Miscellaneous Tools > Deleted Objects .

Step 3

Click the table name for the object you want to delete. This action opens a panel showing all records for that table that
                                       have been marked for deletion.

Step 4

Select one, several, or all records.

Step 5

Click Delete Permanently .

## Packaged CCE 4000 and 12000 Agent Supported Tools

You can perform some of the configurations for Packaged CCE 4000 and 12000 Agent deployments using the Configuration Manager
                           tool. For information on how to use the tools, see the online help provided in each tool.

Only Packaged CCE configuration users who have been added to the UcceConfig group in all the local distributors can access the Configuration Manager. For details on how to add users to a local security
                                       group, see Add Users to Local Security Group

Following is the list of tools that are supported in the Configuration Manager.

To enable the following configuration tools, navigate to Unified CCE Administration > User setup > Roles page and then select the required permissions.

Tools

List

Explorer Tools

Agent Explorer

Announcement Explorer

Database Lookup Explorer

ICM Instance Explorer

Network VRU Explorer

Network Trunk Group Explorer

NIC Explorer

PG Explorer

Region Explorer

Service Explorer

Skill Group Explorer

Translation Route Explorer

List Tools

Agent Desk Settings List

Agent Targeting Rule

Application Gateway List

Agent Instance List

Application Path List

Dialed Number/Script Selector List

Enterprise Service List

Enterprise Skill Group List

Expanded Call Variable Payload List

Label List

Media Class List

Media Routing Domain List

Person List

User Variable List

Bulk Tools

Bulk Insert Tools

Agent Bulk Insert

Dialed Number Bulk Insert

Label Bulk Insert

Network Trunk Group Bulk Insert

Peripheral Bulk Insert

Person Bulk Insert

Route Bulk Insert

Trunk Bulk Insert

Trunk Group Bulk Insert

Service Bulk Insert

Skill Group Bulk Insert

Bulk Edit Tools

Agent Bulk Edit

Dialed Number Bulk Edit

Label Bulk Edit

Network Trunk Group Bulk Edit

Peripheral Bulk Edit

Person Bulk Edit

Route Bulk Edit

Trunk Bulk Edit

Trunk Group Bulk Edit

Service Bulk Edit

Skill Group Bulk Edit

### Reenable Association for Existing Custom Roles

If you are upgrading to 
                              , you must reenable the association for the existing custom roles post upgrade. This table explains how to reenable the association
                              in each tool.

Configuration Manager Tool

To reenable the association

Agent Explorer

Go to Unified CCE Administration > User Setup > Roles > Agent .

Unselect the Manage Agent checkbox and then click Save .

Select the Manage Agent checkbox and then click Save .

Person List

Go to Unified CCE Administration > User Setup > Roles > Agent .

Unselect the Manage Agent Attributes checkbox and then click Save .

Select the Manage Agent Attributes checkbox and then click Save .

Dialed Number/Script Selector List

Go to Unified CCE Administration > User Setup > Roles > Call Settings .

Unselect the Dialed Number checkbox and then click Save .

Select the Dialed Number checkbox and then click Save .

Skill Group Explorer

Go to Unified CCE Administration > User Setup > Roles > Organization .

Unselect the Skill Groups checkbox and then click Save .

Select the Skill Groups checkbox and then click Save .

Application Gateway List

Go to Unified CCE Administration > User Setup > Roles > Infrastructure .

Unselect the Application Gateway checkbox and then click Save .

Select the Application Gateway checkbox and then click Save .

Expanded Call Variables Payload List

Go to Unified CCE Administration > User Setup > Roles > Call Settings .

Unselect the Expanded Call Variables checkbox and then click Save .

Select the Expanded Call Variables checkbox and then click Save .

Agent Desk Settings Tool

Go to Unified CCE Administration > User Setup > Roles > Desktop Settings .

Unselect the Desk Settings checkbox and then click Save .

Select the Desk Settings checkbox and then click Save .

Bulk Configuration Tools

Go to Unified CCE Administration > User Setup > Roles .

Unselect the Bulk Import checkbox and then click Save .

Select the Bulk Import checkbox and then click Save .

For information on restrictions that apply to Configuration Manager tools while configuring ICM-to-ICM Gateway, see the Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

| Step 1 | Open Configuration Manager. |
|---|---|
| Step 2 | Select Tools > Miscellaneous Tools > Deleted Objects . |
| Step 3 | Click the table name for the object you want to delete. This action opens a panel showing all records for that table that
                                       have been marked for deletion. |
| Step 4 | Select one, several, or all records. |
| Step 5 | Click Delete Permanently . |

| Note | Only Packaged CCE configuration users who have been added to the UcceConfig group in all the local distributors can access the Configuration Manager. For details on how to add users to a local security
                                       group, see Add Users to Local Security Group |
|---|---|

| Note | To enable the following configuration tools, navigate to Unified CCE Administration > User setup > Roles page and then select the required permissions. |
|---|---|

| Tools | List |
|---|---|
| Explorer Tools | Agent Explorer Announcement Explorer Database Lookup Explorer ICM Instance Explorer Network VRU Explorer Network Trunk Group Explorer NIC Explorer PG Explorer Region Explorer Service Explorer Skill Group Explorer Translation Route Explorer |
| List Tools | Agent Desk Settings List Agent Targeting Rule Application Gateway List Agent Instance List Application Path List Dialed Number/Script Selector List Enterprise Service List Enterprise Skill Group List Expanded Call Variable Payload List Label List Media Class List Media Routing Domain List Person List User Variable List |
| Bulk Tools | Bulk Insert Tools Agent Bulk Insert Dialed Number Bulk Insert Label Bulk Insert Network Trunk Group Bulk Insert Peripheral Bulk Insert Person Bulk Insert Route Bulk Insert Trunk Bulk Insert Trunk Group Bulk Insert Service Bulk Insert Skill Group Bulk Insert Bulk Edit Tools Agent Bulk Edit Dialed Number Bulk Edit Label Bulk Edit Network Trunk Group Bulk Edit Peripheral Bulk Edit Person Bulk Edit Route Bulk Edit Trunk Bulk Edit Trunk Group Bulk Edit Service Bulk Edit Skill Group Bulk Edit |

| Configuration Manager Tool | To reenable the association |
|---|---|
| Agent Explorer | Go to Unified CCE Administration > User Setup > Roles > Agent . Unselect the Manage Agent checkbox and then click Save . Select the Manage Agent checkbox and then click Save . |
| Person List | Go to Unified CCE Administration > User Setup > Roles > Agent . Unselect the Manage Agent Attributes checkbox and then click Save . Select the Manage Agent Attributes checkbox and then click Save . |
| Dialed Number/Script Selector List | Go to Unified CCE Administration > User Setup > Roles > Call Settings . Unselect the Dialed Number checkbox and then click Save . Select the Dialed Number checkbox and then click Save . |
| Skill Group Explorer | Go to Unified CCE Administration > User Setup > Roles > Organization . Unselect the Skill Groups checkbox and then click Save . Select the Skill Groups checkbox and then click Save . |
| Application Gateway List | Go to Unified CCE Administration > User Setup > Roles > Infrastructure . Unselect the Application Gateway checkbox and then click Save . Select the Application Gateway checkbox and then click Save . |
| Expanded Call Variables Payload List | Go to Unified CCE Administration > User Setup > Roles > Call Settings . Unselect the Expanded Call Variables checkbox and then click Save . Select the Expanded Call Variables checkbox and then click Save . |
| Agent Desk Settings Tool | Go to Unified CCE Administration > User Setup > Roles > Desktop Settings . Unselect the Desk Settings checkbox and then click Save . Select the Desk Settings checkbox and then click Save . |
| Bulk Configuration Tools | Go to Unified CCE Administration > User Setup > Roles . Unselect the Bulk Import checkbox and then click Save . Select the Bulk Import checkbox and then click Save . |