---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1261-insta-269347a096
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1261/install/guide/cuic_b_install-and-upgrade-guide-1261/cuic_m_before-you-install-1261.html
retrieved_at: 2026-08-21T16:14:54.599839+00:00
---

Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(1)

# Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(1)

Updated: May 14, 2021

Chapter: Before You Install

## Chapter: Before You Install

# Before You Install

## About Cisco
                        	 Unified Intelligence Center

Unified
                              		  Intelligence Center can be installed as a standalone server or as a cluster of
                              		  a maximum of eight server nodes. There is one mandatory publisher node (called
                              		  the Controller ) and a maximum of seven subscriber nodes
                              		  (called Members ). The Controller node includes a Member; thus
                              		  a deployment can consist of a Controller only.

All nodes must
                              		  meet latency requirements as described in the Cisco Unified
                                 			 Intelligence Center Solution Reference Network Design (SRND) Guide .

The primary node
                              		  (the Controller ) includes both the Administration
                              		  (Operations, Administration, Maintenance, and Provisioning or OAMP) and the
                              		  Unified Intelligence Center Reporting web applications. A Controller is
                              		  required in all deployments. A deployment can consist of a Controller only.

The Member nodes
                              		  have the Unified Intelligence Center Reporting web application only.

Unified
                              		  Intelligence Center is installed on Cisco Unified Voice Operating System (VOS).
                              		  This is an appliance model or "closed box" and does not support navigation
                              		  into, or manipulation of, the file system.

Unified
                              		  Intelligence Center must be installed on a Virtual Machine running over UCS
                              		  B-Series and C-Series Servers or equivalent hardware.

The disk capacity
                              		  and hardware type of Member nodes should be equal to or greater than those of
                              		  the Controller node.

For Cisco Unified Intelligence Center Hardware and Software Specification, refer Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html and Compatibility Matrix for Unified CCX at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

See the Cisco Unified Intelligence Center Solution Reference Network Design (SRND) Guide , available in the Design Guides category at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/tsd-products-support-series-home.html .

## Prerequisites and
                        	 Important Considerations

Before you proceed
                              		  with the installation and upgrade, note these important requirements:

You must have
                                    				access to a Network Time Protocol (NTP) server.

You must have
                                    				a preconfigured default router.

You must have a preconfigured Domain Name Server (DNS).

You must
                                    				install the primary node (the Controller).

All configured
                                    				nodes in a cluster must be installed and started before you install a new node.
                                    				For example, if the Controller and one Member have been installed and you are
                                    				about to add a second Member, the Controller and first Member must be started
                                    				and available so that the second Member is able to access them.

Installation
                                    				on an existing (repurposed) server formats the hard drive and erases all data.
                                    				It might also change the system Basic Input Output System (BIOS), firmware, and
                                    				Redundant Array of Inexpensive Disks (RAID) configuration.

On the
                                    				installation configuration screens:

Values—such as host names, User IDs, and passwords—are
                                          					 case-sensitive.

You must
                                          					 enter the same security password on all nodes in the cluster. Keep a record of
                                          					 this password; you will need to use it if you replace or add a server in the
                                          					 future or if you want to replace the old security password with a new one.

Use the
                                          					 default Maximum Transmission Unit (MTU) setting, for all nodes in the cluster.

## Configuration
                        	 Worksheet

Use this worksheet
                              		  to record network and password information that the basic installation
                              		  configuration wizard prompts you to enter. Store this worksheet information for
                              		  future reference.

Configuration Data

Your Entry

Host Name

Controller

Member 1

Member 2

IP Address

Controller

Member

Gateway
                                          					 (GW) Address

Primary
                                          					 DNS IP Address

Controller

Member

Secondary
                                          					 DNS IP Address

Controller

Member

Domain

Username

System
                                          					 Administrator Password

Timezone

Use the same Timezone for all nodes.

Certificate Information

Organization

Unit

Location

State

Country

NTP Server
                                          					 Host Name or IP Address

NTP Server
                                          					 1

NTP Server
                                          					 2

NTP Server
                                          					 3

NTP Server
                                          					 4

NTP Server
                                          					 5

Database
                                          					 Access Security Password

Security
                                          					 Password

Servers in
                                          					 the cluster use the security password to communicate with one another. The
                                          					 security password is also used by the Disaster Recovery System (DRS) for
                                          					 encryption of the backup file.

Simple
                                          					 Mail Transfer Protocol (SMTP) Location Host Name

SMTP
                                          					 Host Name or IP Address

Credentials

Application User ID

Application User Password

The
                                          					 Application User defined during the Controller installation is the only
                                          					 credential recognized by Unified Intelligence Center.

## Installation
                        	 Sequence and Time

A Unified Intelligence Center can include one or multiple nodes. The
                              		  installation for each node can take about an hour. For most of that time, it
                              		  can run unattended.

You must perform the installation on the primary
                                 			 node/Controller first.

Some configuration and installation processes differ slightly for the
                              		  first node (Controller) and for the Members. This is noted in these
                              		  instructions.

## Installation
                        	 Wizard Navigation

Much of the installation requires no action on the part of the person
                              		  who runs it. When user input is required, use the following keyboard navigation and selection actions.

The installation wizard screens do not recognize a mouse or a
                              		  touchpad.

To Do This

Press This Key

Move to the next field

Tab

Move to the previous field

Alt-Tab

Choose an option

Spacebar

Scroll up or down a list

Up or Down arrow keys

Go to the previous screen

Tab to Back and press the Spacebar

Get information on a screen

Tab to Help and press the Spacebar

Scroll up and down a list

Up or Down arrow keys

| Configuration Data | Your Entry |
|---|---|
| Host Name | Controller |
| Member 1 |
| Member 2 |
| IP Address | Controller |
| Member |
| Gateway
                                          					 (GW) Address | — |
| Primary
                                          					 DNS IP Address | Controller |
| Member |
| Secondary
                                          					 DNS IP Address | Controller |
| Member |
| Domain | — |
| Username | — |
| Note Ensure
                                                   					 that you use the same System Administrator credentials for all nodes. | Note | Ensure
                                                   					 that you use the same System Administrator credentials for all nodes. |
| Note | Ensure
                                                   					 that you use the same System Administrator credentials for all nodes. |
| System
                                          					 Administrator Password | — |
| Timezone Use the same Timezone for all nodes. | — |
| Certificate Information | Organization |
| Unit |
| Location |
| State |
| Country |
| NTP Server
                                          					 Host Name or IP Address | NTP Server
                                          					 1 |
| NTP Server
                                          					 2 |
| NTP Server
                                          					 3 |
| NTP Server
                                          					 4 |
| NTP Server
                                          					 5 |
| Database
                                          					 Access Security Password | Security
                                          					 Password |
| Servers in
                                          					 the cluster use the security password to communicate with one another. The
                                          					 security password is also used by the Disaster Recovery System (DRS) for
                                          					 encryption of the backup file. Note You
                                                   					 must enter the same security password for all servers in the cluster. | Note | You
                                                   					 must enter the same security password for all servers in the cluster. |
| Note | You
                                                   					 must enter the same security password for all servers in the cluster. |
| Simple
                                          					 Mail Transfer Protocol (SMTP) Location Host Name | SMTP
                                          					 Host Name or IP Address |
| Credentials | Application User ID |
| Application User Password |
| The
                                          					 Application User defined during the Controller installation is the only
                                          					 credential recognized by Unified Intelligence Center. Note Ensure that you use the same System Application credentials for
                                                   					 all nodes. | Note | Ensure that you use the same System Application credentials for
                                                   					 all nodes. |
| Note | Ensure that you use the same System Application credentials for
                                                   					 all nodes. |

| Note | Ensure
                                                   					 that you use the same System Administrator credentials for all nodes. |
|---|---|

| Note | You
                                                   					 must enter the same security password for all servers in the cluster. |
|---|---|

| Note | Ensure that you use the same System Application credentials for
                                                   					 all nodes. |
|---|---|

| To Do This | Press This Key |
|---|---|
| Move to the next field | Tab |
| Move to the previous field | Alt-Tab |
| Choose an option | Spacebar |
| Scroll up or down a list | Up or Down arrow keys |
| Go to the previous screen | Tab to Back and press the Spacebar |
| Get information on a screen | Tab to Help and press the Spacebar |
| Scroll up and down a list | Up or Down arrow keys |