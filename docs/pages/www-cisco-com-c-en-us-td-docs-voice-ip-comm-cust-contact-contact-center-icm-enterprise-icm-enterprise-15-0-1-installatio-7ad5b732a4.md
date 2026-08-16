---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-7ad5b732a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_150_install_upgrade_guide/installation_overview.html
retrieved_at: 2026-08-16T19:56:16.175999+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Installation Overview

## Chapter: Installation Overview

- Installation Overview

- Installation                              	 Tools

# Installation Overview

## Installation
                        	 Tools

During
                              		  installation, use one or all of the following tools, as required:

ICM-CCE-Installer—The main Unified CCE Installer copies all files into relevant folders, creates the base registries, and
                                       installs needed third-party software such as JRE and Apache Tomcat. It uses the Microsoft .NET Framework which is an integral
                                       software of Windows Server.

Optionally, you can update the JRE installed by the Unified CCE Installer with a later version of the JRE. For more information, see Java Upgrades topic in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                in the java certificate store, and removes all the unapproved certificates.

Do not run the installer remotely. Download the installer to a local machine for installation.

Cisco Unified
                                    				Intelligent Contact Management Database Administration (ICMDBA) Tool—Used to
                                    				create new databases, modify or delete existing databases, and perform limited
                                    				SQL Server configuration tasks.

Domain
                                    				Manager—Used to provision Active Directory.

Web Setup—Used to set up the Call Routers, Loggers, Network Gateways, Network Interface Controllers, and Administration &
                                    Data Servers.

Peripheral Gateway (PG) Setup—Used to set up PGs, the CTI server,  and the Outbound Option dialer.

AdminClientInstaller—Installs the Administration Client on a system that is not running other Unified CCE components.

The AdminClientInstaller is delivered on the installation media with the ICM-CCE-Installer.

Administration Client Setup—Used to add, edit, or remove Administration Clients and Administration Client Instances.

| Note | Optionally, you can update the JRE installed by the Unified CCE Installer with a later version of the JRE. For more information, see Java Upgrades topic in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                in the java certificate store, and removes all the unapproved certificates. |
|---|---|