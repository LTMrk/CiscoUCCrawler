---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-installation-guide-pcce-b-1262--36a2cec3a5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/installation/guide/pcce_b_1262_cisco_pcce_installationandupgrade_guide/pcce_b_cisco_pcce_installationandupgrade_guide_12_5_2_chapter_01.html
retrieved_at: 2026-08-21T04:50:23.461505+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

Updated: March 9, 2026

Chapter: System Requirements

## Chapter: System Requirements

# System Requirements

## Set up Active Directory

Ensure that you have a completed plan for your domain structure and Active Directory
                           implementation before you set up your network.

Warning

The Unified CCE servers should be in the same domain, and multiple domains are not supported.

For more information, see the Staging Guide for Cisco Unified ICM/Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

## Transport Layer
                        	 Security Version 1.2 Required

Contact center enterprise solutions require the use of TLS 1.2 only
                           		connections in this release. Our services accept incoming TLS connections only
                           		over TLS 1.2. All outgoing TLS connection use only TLS 1.2.

All clients that connect to either our web interfaces or databases must
                           		support TLS 1.2.

The older versions of the TLS/SSL are disabled by installer.

For more information see, Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

## Installation
                        	 Tools

During
                              		  installation, use one or all of the following tools, as required:

ICM-CCE-Installer—The main Unified CCE Installer copies all files into relevant folders, creates the base registries, and
                                       installs needed third-party software such as JRE and Apache Tomcat. It uses the Microsoft .NET Framework which is an integral
                                       software of Windows Server.

Optionally, you can update the JRE installed by the Unified CCE Installer with a later version of the JRE. See Java Upgrades .

If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                in the java certificate store, and removes all the unapproved certificates.

Do not run the installer remotely. Download the installer to a local machine for installation.

ICM12.6.2.exe—The Unified CCE patch installer. It copies all files into relevant folders, updates the registries, and installs
                                    needed third-party software such as JRE, Apache Tomcat, and Microsoft .NET Framework.

Cisco Unified
                                    				Intelligent Contact Management Database Administration (ICMDBA) Tool—Used to
                                    				create new databases, modify or delete existing databases, and perform limited
                                    				SQL Server configuration tasks.

Domain
                                    				Manager—Used to provision Active Directory.

Web Setup—Used to set up the Call Routers, Loggers, Network Gateways, Network Interface Controllers, and Administration &
                                    Data Servers.

Peripheral Gateway (PG) Setup—Used to set up MR PIMs and CG.

## VMware Hosting and
                        	 Hardware Support

See the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html for the supported specification based hardware, Cisco UCS C-Series servers for Packaged CCE fresh installs and upgrades,
                              and supported VMware vSphere ESXi versions.

## Software
                        	 Compatibility

See the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html

Endpoints for
                                    				agents and callers

Cisco gateway
                                    				hardware and software

Third-party
                                    				software

## Software
                        	 Licenses

The following table lists the Cisco components that comprise a Packaged CCE solution:

One server license for each of the voice applications.

One agent license for each concurrent user with different feature tiers.

You must register CVP instance with Cisco Smart
                                          									Licensing Server which includes CVP Call Server and VXML Server
                                          									in order to use the appropriate licenses.

For more information, see Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

Cisco Finesse

Cisco Finesse: User licenses included with selected tiers of Cisco Unified Contact Center Enterprise user licenses. One license
                                          for each server pair. One license for each Media Kit.

Packaged Contact Center Enterprise is enabled with Smart Licensing. For information on Smart Licensing, see the Packaged Contact
                                          Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Before you begin an installation or upgrade of any part of your contact center, confirm the following:

That you have all the required software products.

That all the software versions are compatible with each other.

That all software versions are also compatible with all hardware and VMware.

## Java Requirements

CCE has transitioned from Oracle to OpenJDK for the Java runtime environment (JRE). All CCE components require OpenJDK JRE
                           version 1.8 (32-bit), update 352 or later. The 12.6(2) installer will install the required OpenJDK 1.8 version. If the existing Oracle JRE is not needed, you may uninstall it from
                           the system manually.

| Warning | The Unified CCE servers should be in the same domain, and multiple domains are not supported. |
|---|---|

| Note | The older versions of the TLS/SSL are disabled by installer. |
|---|---|

| Note | Optionally, you can update the JRE installed by the Unified CCE Installer with a later version of the JRE. See Java Upgrades . If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                in the java certificate store, and removes all the unapproved certificates. |
|---|---|

| Components | License requirements |
|---|---|
| Cisco Packaged Contact Center Enterprise | One server license for each of the voice applications. One agent license for each concurrent user with different feature tiers. |
| Cisco Unified Communications Manager | One license for each Cisco Unified Communications Manager node, plus device licenses for connected devices. |
| Cisco Unified Customer Voice Portal (CVP) | You must register CVP instance with Cisco Smart
                                          									Licensing Server which includes CVP Call Server and VXML Server
                                          									in order to use the appropriate licenses. For more information, see Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html . |
| Cisco Finesse | Cisco Finesse: User licenses included with selected tiers of Cisco Unified Contact Center Enterprise user licenses. One license
                                          for each server pair. One license for each Media Kit. |
| Cisco Customer Collaboration Platform | User license included with Packaged CCE Agent License. One server license for each Customer Collaboration Platform server. |

| Note | Packaged Contact Center Enterprise is enabled with Smart Licensing. For information on Smart Licensing, see the Packaged Contact
                                          Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|