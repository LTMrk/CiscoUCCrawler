---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125install-ddb9fc7224
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125install-and-upgrade-guide/uccx_b_125install-and-upgrade-guide_chapter_00.html
retrieved_at: 2026-08-16T21:14:14.475302+00:00
---

Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Installation Preparation

## Chapter: Installation Preparation

# Installation Preparation

## Installation
                        	 Scenarios

Unified CCX installation has the following installation options:

Standard installation - This option allows you to install Unified CCX software from the installation disc.

Unattended installation - This option allows you to use the installation disc and a preconfigured USB disk to install Unified
                                    CCX software unattended.

Virtualization - Unified CCX supports installation on a virtual machine.

Installation Scenario

Tasks

Standalone (Single Node) Setup

Standard Installation:

Install Unified CCX from Installation DVD

Configure the first node

Unattended Installation:

Perform Unattended Installation Using Answer File Generator

Configure the first node

High Availability (Two Node) Setup

Standard Installation:

Install Unified CCX from Installation DVD

Configure the First Node

Add Second Node

Install Unified CCX on Second Node

Configure the second node

Unattended Installation:

Perform Unattended Installation Using Answer File Generator

Configure the first node

Add Second Node

Perform Unattended Installation Using Answer File Generator

Configure the second node

You can use the Cisco Prime Collaboration Deployment application also to install your
                                          					cluster. For more information, see Cisco Prime Collaboration Deployment
                                             						Administration Guide .

## System
                        	 Requirements

For information about system requirements, see the Unified CCX Compatibility related information located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html

For more information about VMware ESXi's that are supported, refer to the Virtualization for Cisco Unified Contact Center Express .

## Important Considerations Before
                        	 Installation

Read the following information carefully before you proceed
                              		  with the installation:

For 100 agent profile, if you want to deploy Cloud Connect on the BE6000, you must configure 14GB of vRAM. For 400 agent profile,
                                    you must use the new OVA for which, you must configure 20GB of vRAM.

Ensure that the reservation of CPU and memory adhere to the specifications mentioned in the Virtualization Wiki.

Unified CCX can only be installed on virtual machines and not on
                                    				bare metal servers.

DNS configuration and domain fields are mandatory for Unified CCX
                                    				installation. Both forward and reverse lookups are required. DNS is required
                                    				for the 
                                    				Unified CCX Chat feature to function and for integration with
                                    				ICM by hostname in Unified IP IVR.

When you Install Unified CCX on an existing server formats the
                                    				hard drive, it overwrites all existing data on the drive. It also upgrades the
                                    				system BIOS, firmware, and Redundant Array of Inexpensive Disks (RAID)
                                    				configuration if they are outdated.

Ensure that you connect each Unified CCX node to an uninterrupted power supply (UPS). This protects the Unified CCX server
                                    from unexpected power failure that damages the physical media.

All servers in a cluster must run the same release of Unified CCX.
                                    				The only exception is while upgrading cluster software, during which a
                                    				temporary mismatch is allowed.

Configure the server by using a static IP address so that the
                                    				server IP address remains unchanged.

Do not attempt to perform any configuration tasks during the
                                    				installation.

The field values (namely hostname and passwords) that you enter while you are running the installation program are case-sensitive.
                                    Hostname must be in lower case and the character limit is 24 characters.

Ensure that the administrator username is not the same as that of any end user in CUCM.

When you insert or remove a USB drive, you might see error
                                    				messages on the console similar to "sdb: assuming drive cache: write through." You can safely
                                    				ignore these messages.

Ensure that the third-party web services support TLS version 1.2
                                    				before you integrate any third-party web services.

After the installation of Unified CCX, you have to select appropriate Smart License Type. For Smart Licensing details, see Cisco Unified Contact Center Express Features Guide .

When creating the OS Administrator ID, ensure that it does not start with “uccx” or “UCCX” because such IDs conflict with
                                    system account names that are used internally within the Unified CCX server. Ensure that the OS Administration password is
                                    at least six characters long; it can contain alphanumeric characters, hyphens, and underscores.

Ensure that the Application User password is at least six characters long; it can contain alphanumeric characters, hyphens,
                                    and underscores.

## Preinstallation
                        	 Tasks

Step 1

If the system
                                       			 time is from an Network Time Protocol (NTP) server (mandatory for VMware
                                       			 deployments), verify that the first node synchronizes with the NTP server
                                       			 before you install a second node.

If the first
                                                      				  node fails to synchronize with an NTP server, installation of a second node
                                                      				  also fails.

Step 2

If the
                                       			 firewall is in the routing path, disable the firewall between nodes. Increase
                                       			 the firewall timeout settings until you complete the installation.

Step 3

Record the
                                       			 network interface card (NIC) speed and duplex settings of the switch port to
                                       			 which you will connect the new server.

Step 4

Enable
                                       			 PortFast on all switch ports that are connected to Cisco servers.

Caution

Do not run
                                                      				  Network Address Translation (NAT) or Port Address Translation (PAT) between Unified CCX nodes.

Step 5

If you choose to apply a patch during installation, use a Secure File Transfer Protocol (SFTP) server that is certified by
                                       Cisco through the Cisco Technology Developer Partner program (CTDP). For more information about Supported SFTP Servers, see System Requirements section in Cisco Unified Contact Center Express Admin and Operations Guide .

| Note | For more information, see the Unified CCX Virtualization related information located at: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html . |
|---|---|

| Installation Scenario | Tasks |
|---|---|
| Standalone (Single Node) Setup | Standard Installation: Install Unified CCX from Installation DVD Configure the first node Unattended Installation: Perform Unattended Installation Using Answer File Generator Configure the first node |
| High Availability (Two Node) Setup | Standard Installation: Install Unified CCX from Installation DVD Configure the First Node Add Second Node Install Unified CCX on Second Node Configure the second node Unattended Installation: Perform Unattended Installation Using Answer File Generator Configure the first node Add Second Node Perform Unattended Installation Using Answer File Generator Configure the second node |

| Note | You can use the Cisco Prime Collaboration Deployment application also to install your
                                          					cluster. For more information, see Cisco Prime Collaboration Deployment
                                             						Administration Guide . |
|---|---|

| Note | For more information about VMware ESXi's that are supported, refer to the Virtualization for Cisco Unified Contact Center Express . |
|---|---|

| Note | Ensure that the reservation of CPU and memory adhere to the specifications mentioned in the Virtualization Wiki. |
|---|---|

| Step 1 | If the system
                                       			 time is from an Network Time Protocol (NTP) server (mandatory for VMware
                                       			 deployments), verify that the first node synchronizes with the NTP server
                                       			 before you install a second node. Note If the first
                                                      				  node fails to synchronize with an NTP server, installation of a second node
                                                      				  also fails. | Note | If the first
                                                      				  node fails to synchronize with an NTP server, installation of a second node
                                                      				  also fails. |
|---|---|---|---|
| Note | If the first
                                                      				  node fails to synchronize with an NTP server, installation of a second node
                                                      				  also fails. |
| Step 2 | If the
                                       			 firewall is in the routing path, disable the firewall between nodes. Increase
                                       			 the firewall timeout settings until you complete the installation. |
| Step 3 | Record the
                                       			 network interface card (NIC) speed and duplex settings of the switch port to
                                       			 which you will connect the new server. |
| Step 4 | Enable
                                       			 PortFast on all switch ports that are connected to Cisco servers. Caution Do not run
                                                      				  Network Address Translation (NAT) or Port Address Translation (PAT) between Unified CCX nodes. | Caution | Do not run
                                                      				  Network Address Translation (NAT) or Port Address Translation (PAT) between Unified CCX nodes. |
| Caution | Do not run
                                                      				  Network Address Translation (NAT) or Port Address Translation (PAT) between Unified CCX nodes. |
| Step 5 | If you choose to apply a patch during installation, use a Secure File Transfer Protocol (SFTP) server that is certified by
                                       Cisco through the Cisco Technology Developer Partner program (CTDP). For more information about Supported SFTP Servers, see System Requirements section in Cisco Unified Contact Center Express Admin and Operations Guide . |

| Note | If the first
                                                      				  node fails to synchronize with an NTP server, installation of a second node
                                                      				  also fails. |
|---|---|

| Caution | Do not run
                                                      				  Network Address Translation (NAT) or Port Address Translation (PAT) between Unified CCX nodes. |
|---|---|