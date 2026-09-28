---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-release-notes-b-release-notes-1501-html-9b625822f5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/release/notes/b_release_notes_1501.html
retrieved_at: 2026-08-16T18:49:14.627882+00:00
---

Release Notes for Cisco Unity Connection Release 15

# Release Notes for Cisco Unity Connection Release 15

### Download Options

Updated: December 18, 2023

# Release Notes for Cisco Unity Connection Release 15

These release notes contain information on Cisco Unity Connection 15 new and changed functionality, upgrade information, limitations,
               and restrictions.

## Contents

## System
               	 Requirements

System Requirements for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

## Upgrade
               	 Information

You can upgrade from Unity Connection 14, 12.x, 11.x to Unity Connection 15. For more information on upgrade process and supported
                  upgrade paths, see the " Upgrading Cisco Unity Connection " chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

## Determining the
               	 Software Version

This section contains procedures
                  		for determining the version in use for the following software:

Cisco Unity Connection Application

- Cisco Personal Communications Assistant Application

- Cisco Unified Communications Operating System

### Cisco Unity
                  	 Connection Application

This section contains two
                     		procedures. Use the applicable procedure, depending on whether you want to use
                     		Unity Connection Administration or a command-line interface (CLI) session to
                     		determine the version.

#### Using Cisco Unity
                     	 Connection Administration

In Cisco Unity Connection
                                    			 Administration, in the upper-right corner below the Navigation list, select About .

#### Using the
                     	 Command-Line Interface

Before you begin

##### Before you begin

Step 1

Start a command-line
                                    			 interface (CLI) session. (For more information, see the Cisco Unified
                                    			 Communications Operating System Administration Help.)

Step 2

Run the show cuc version command to view the Unity Connection version.

### Cisco Personal
                  	 Communications Assistant Application

This section contains the
                        		  procedure to determine the version using Cisco PCA application.

Using Cisco PCA Application

Step 1

Sign in to Cisco PCA.

Step 2

On the Cisco PCA Home page, select the About link in the upper-right corner. (The link is available on every Cisco PCA page.)

Step 3

The Unity Connection version
                                 			 is displayed, which is same as the version of Cisco PCA.

### Cisco Unified
                  	 Communications Operating System

This section contains two
                     		procedures. Use the applicable procedure, depending on whether you want to use
                     		Cisco Unified Operating System Administration or a command-line interface
                     		session to determine the version.

#### Using Cisco
                     	 Unified Operating System Administration

In Cisco Unified Operating System Administration, the System Version is displayed below "Cisco Unified Operating System Administration"
                                    in the blue banner on the page that appears after you sign in.

#### Using the
                     	 Command-Line Interface

Before you begin

##### Before you begin

Step 1

Start a command-line
                                    			 interface session. (For more information, see Cisco Unified Operating System
                                    			 Administration Help.)

Step 2

Run the show version active command to view the Cisco Unified
                                    			 Operating System Administration version.

## Related
               	 Documentation

For virtualization requirements, see the "Requirements for Installing Unity Connection 15 on a Virtual Machine" section and
                        for the default license file, see the "Licensing Requirements" section of the System Requirements for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

- For instructions on migrating from an existing Unity Connection physical server to a new virtual machine, see the " Migrating a Physical Server to a Virtual Machine " section of "Maintaining Cisco Unity Connection Server" chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

- For more information on Unity Connection complete documentation see the Documentation Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/roadmap/b_15cucdg.html .

## New and Changed Features

This section contains information about features in the 15 release time frame only.

### Alma Linux and 64-bit Support

Cisco Unity Connection Release 15 brings an enhanced experience for users and administrators with major platform upgrades
                     to align with the industry standards. Enhancements include Application-layer changes and core Linux transition for long-term
                     support. The enhancements also includestransition to the 64-bit application architecture for removal of memory bottlenecks
                     and mitigating end-of-life for 32-bit dependencies. This release provides enhanced protection, security, innovation, and flexibility.

Some of the important considerations when installing or migrating to Release 15 are:

Minimum supported ESXi versions are 7.0 U3 or 8.0 U1 with a minimum VM Hardware version of 17. The other required VM specifications
                           like guest OS type may be found in the Readme of the base OVA at https://software.cisco.com/download/home/283062758/type . For more information, see Virtualization for Cisco Unity Connection (CUC) .

Virtual Floppy Drive is replaced with virtual CDROM for touchless installation.

IPSec policy with 3DES Algorithm is not supported in FIPS mode for Release 15 in case you are planning to upgrade to Release
                           15. You must delete and recreate the IPSec policy with the Encryption and ESP Algorithms other than 3DES in both the nodes
                           between which the IPSec tunnel is to be established, and then plan an upgrade. For more information, see chapter FIPS Compliance in Cisco Unity Connection of the " Security Guide for Cisco Unity Connection Release 15 " available at https://www.cisco.com/content/en/us/td/docs/voice_ip_comm/connection/15/security/b_15cucsecx.html ..

Direct upgrade paths from release 10.5 or earlier will not be allowed due to swap realignement in release 15. Any setup with
                                          /dev/sda5 swap space of 2 GB must be rebuilt for successful upgrade and install pre-upgrade COP file should be checked for
                                          system requirement. For more information on upgrade paths, see section " Upgrade Types " of the chapter "Upgrading Cisco Unity Connection"of the Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/content/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/b_15cuciumg.html

### Enhancements for Cisco Unified Real-Time Monitoring Tool

From this release onwards, you can install Cisco Unified Real-Time Monitoring Tool (Unified RTMT) on workstations running
                     on both Windows or Linux operating systems using a single 'CiscoRTMTPlugin.zip' plug-in. This feature enhancement takes away
                     the need for a separate plug-in (.exe installer for 32 and 64 bit) for Windows and Linux platforms.

Unified RTMT installation is now supported on computers running on the Windows 11 operating system.

Unified RTMT certificate-based authentication support

In this release, Unified RTMT supports Certificate-based authentication that provides enhanced security considerations. Using
                     this authentication method, it reducesthe threat of compromised passwords, and provides protection of sensitive or classified
                     components in your network infrastructure.

### Log4j Upgrade

Cisco Unity Connection Release 15 supports Log4j version 2.19.0. .

### Migration to Strongswan

Cisco Unity Connection release 15 supports migration from Libreswan to Strongswan for IPSec DoDIN APL certification. For more
                     information, see chapter FIPS Compliance in Cisco Unity Connection of the " Security Guide for Cisco Unity Connection Release 15 " available at https://www.cisco.com/content/en/us/td/docs/voice_ip_comm/connection/15/security/b_15cucsecx.html .

## Installation and
               	 Upgrade Information

### Installing Cisco
                  	 Unity Connection for the First Time on a Virtual Machine

You must download and deploy a VMware OVA template, which automatically configures the virtual machine for Unity Connection.
                     To download the template, see the next section, “ Downloading a VMware OVA Template for a Unity Connection 15 Virtual Machine .” The installation and migration documentation tell you when to deploy the template.

For information on upgrading ESXi version, see the ReadMe of applicable OVAs availale at https://software.cisco.com/download/home/283062758/type .

#### Downloading a VMware OVA Template for a Unity Connection 15 Virtual Machine

It is recommended
                           		  to use VMware OVA template to configure VMware for Unity Connection, which
                           		  simplifies the process of configuring the virtual machine. If you want to
                           		  deploy the VMware OVA template for Unity Connection, do the following procedure
                           		  to download the OVA file.

Procedure to
                           		  download a VMware OVA template:

Step 1

Sign in to a
                                    			 computer with a high-speed Internet connection, and go to the Voice and Unified
                                    			 Communications Downloads page at http://www.cisco.com/cisco/software/navigator.html?mdfid=280082558 .

To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user.

Step 2

In the tree
                                    			 control on the Downloads page, expand Products >
                                       				Unified Communications >Unified Communications Applications > Messaging
                                       				> Unity Connection, and select Cisco Unity
                                       				Connection Virtualization .

Step 3

On the Download Software page, select OVA-15 , and the download links appear on the right side of the page.

Step 4

Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download file sizes appear below the download links.)

Step 5

Select the
                                    			 applicable link to download.

Restricted version

UCSInstall_CUC_15.0.1.10000-24.sgn.iso

Unrestricted version

UCSInstall_CUC_UNRST_15.0.1.10000-24.sgn.iso

The following
                                       				configurations are available with the OVA file, and you can select the required
                                       				configurations for deploying the OVA template:

Configures two virtual CPU, 10 GB RAM, and one 160-GB virtual disk with the file system aligned at 64KB blocks.

Configures two virtual CPUs, 12 GB RAM, and one 200-GB virtual disk with the file system aligned at 64KB blocks.

Configures four virtual CPUs, 12 GB RAM, and two 146-GB virtual disks with the file system aligned at 64 KB blocks.

Comes
                                                   						  in 3 variations: 146 GB, 300 GB, and 500 GB. In 300 GB and 500 GB variations,
                                                   						  the datastore where the Unity Connection virtual machine will reside must be
                                                   						  formatted with a VMware VMFS block size of 2 MB or more. A block size of 1 MB
                                                   						  limits the maximum virtual hard disk size to 256 GB. A block size of 2 MB
                                                   						  allows 512 GB virtual disks.

Configures seven virtual CPUs, 16 GB RAM, and either two 300-GB virtual disks or two 500-GB virtual disks with the file system
                                                   aligned at 64KB blocks.

### Installation and
                  	 Upgrade Notes

#### Installing
                     	 Additional Unity Connection Languages

All the locales for Unity Connection 15 are released and available on Download Software site at https://software.cisco.com/download/home/286328409/type .

For instructions on
                        		installing additional Unity Connection languages on the following server types,
                        		see the referenced documentation:

- On a Unity Connection server, see the “ Adding and Removing Unity Connection Languages ” section of “Maintaining Cisco Unity Connection Server” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

If you are
                              			 installing Japanese because you want Cisco Unity Connection Administration to
                              			 be localized, you must also install the Cisco Unified Communications Manager
                              			 Japanese locale. See the “Locale Installation” section in the “Software
                              			 Upgrades” chapter of the applicable Cisco Unified
                                 				Communications Operating System Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

If you are
                              			 installing other languages because you want the Cisco Personal Communications
                              			 Assistant to be localized, you must also install the corresponding Cisco
                              			 Unified Communications Manager locales. See the “Locale Installation” section
                              			 in the “Software Upgrades” chapter of the Cisco Unified
                                 				Communications Operating System Administration Guide at http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

#### Reverting a Server
                     	 to the Unity Connection Version on the Inactive Partition

If you revert from Unity Connection 15  to an earlier version of Unity Connection, some of the data for new Unity Connection
                        15 features is lost and cannot be retrieved when you upgrade again to Unity Connection 15.

## Limitations and
               	 Restrictions

### Secure Messaging
                  	 Limitations Regarding ViewMail

Adding non-audio attachments to secure messages composed in Cisco ViewMail for Microsoft Outlook version 11.0 and later is
                     not supported with Unity Connection 15.

### Using Internet
                  	 Explorer for Playing Voice Messages May Raise Issues

Due to some security issues in
                     		QuickTime player, Unity Connection does not recommend to use QuickTime player
                     		with Internet Explorer for playing the voice messages.

## Caveats

This section contains the following
                  		caveat information:

### Resolved
                  	 Caveats

You can find the latest caveat information for Cisco Unity Connection version 15 by using the Bug Search tool, an online tool
                     available for customers to query defects according to their own need at https://bst.cloudapps.cisco.com/bugsearch?kw=*&pf=prdNm&rls=15.0&sb=fr&svr=3nH&bt=custV.&prdNam=Cisco%20Unity%20Connection .

Bug Search tool is available at https:/​/​tools.cisco.com/​bugsearch . To access Bug Search tool, you must be logged on to Cisco.com as a registered user.

### Open Caveats—Unity Connection Release 15

Click a link in the Caveat Number column to view the latest information on the caveat in Bug Toolkit. (Caveats are listed
                     in order by severity, then by component, then by caveat number.)

### Related Caveats—Cisco Unified Communications Manager 15 Components Used by Unity Connection 15

Table 2 describes the Cisco Unified CM components used by Unity Connection. Caveat information for the Cisco Unified CM components
                        is available in Release Notes for Cisco Unified Communications Manager Release 15 at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html .

Cisco
                                    					 Unified CM Component

Description

backup-restore

Backup and
                                    					 restore utilities

ccm-serviceability

Cisco
                                    					 Unified Serviceability web interface

cdp

Cisco
                                    					 Discovery Protocol Drivers

cli

Command-line interface (CLI)

cmui

Certain
                                    					 elements in the Unity Connection web interfaces (such as search tables and
                                    					 splash screens)

cpi-afg

Cisco
                                    					 Unified Communications Answer File Generator

cpi-appinstall

Installation and upgrades

cpi-cert-mgmt

Certificate management

cpi-diagnose

Automated
                                    					 diagnostics system

cpi-os

Cisco
                                    					 Unified Communications Operating System

cpi-platform-api

Abstraction layer between the Cisco Unified Communications
                                    					 Operating System and the applications hosted on the platform

cpi-security

Security
                                    					 for connections to the server

cpi-service-mgr

Service
                                    					 Manager (ServM)

cpi-vendor

External
                                    					 vendor issues

cuc-tomcat

Apache
                                    					 Tomcat and third-party software

database

Installation and access to the configuration database (IDS)

database-ids

IDS
                                    					 database patches

ims

Identity
                                    					 Management System (IMS)

rtmt

Real-Time Monitoring Tool (RTMT)

## Obtaining
               	 Documentation and Submitting a Service Request

For information on obtaining documentation, submitting a service
                  		request, and gathering additional information, see the monthly What’s New in
                  		Cisco Product Documentation, which also lists all new and revised Cisco
                  		technical documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple
                  		Syndication (RSS) feed and set content to be delivered directly to your desktop
                  		using a reader application. The RSS feeds is a free service and Cisco currently
                  		supports RSS version 2.0.

## Cisco Product
               	 Security Overview

This product contains cryptographic
                  		features and is subject to United States and local country laws governing
                  		import, export, transfer and use. Delivery of Cisco cryptographic products does
                  		not imply third-party authority to import, export, distribute, or use
                  		encryption. Importers, exporters, distributors and users are responsible for
                  		compliance with U.S. and local country laws. By using this product you agree to
                  		comply with applicable laws and regulations. If you are unable to comply with
                  		U.S. and local laws, return this product immediately.

Further information regarding U.S. export regulations may be found at http://www.access.gpo.gov/bis/ear/ear_data.html .

| In Cisco Unity Connection
                                    			 Administration, in the upper-right corner below the Navigation list, select About . |
|---|

| Step 1 | Start a command-line
                                    			 interface (CLI) session. (For more information, see the Cisco Unified
                                    			 Communications Operating System Administration Help.) |
|---|---|
| Step 2 | Run the show cuc version command to view the Unity Connection version. |

| Step 1 | Sign in to Cisco PCA. |
|---|---|
| Step 2 | On the Cisco PCA Home page, select the About link in the upper-right corner. (The link is available on every Cisco PCA page.) |
| Step 3 | The Unity Connection version
                                 			 is displayed, which is same as the version of Cisco PCA. |

| In Cisco Unified Operating System Administration, the System Version is displayed below "Cisco Unified Operating System Administration"
                                    in the blue banner on the page that appears after you sign in. |
|---|

| Step 1 | Start a command-line
                                    			 interface session. (For more information, see Cisco Unified Operating System
                                    			 Administration Help.) |
|---|---|
| Step 2 | Run the show version active command to view the Cisco Unified
                                    			 Operating System Administration version. |

| Note | Direct upgrade paths from release 10.5 or earlier will not be allowed due to swap realignement in release 15. Any setup with
                                          /dev/sda5 swap space of 2 GB must be rebuilt for successful upgrade and install pre-upgrade COP file should be checked for
                                          system requirement. For more information on upgrade paths, see section " Upgrade Types " of the chapter "Upgrading Cisco Unity Connection"of the Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/content/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/b_15cuciumg.html |
|---|---|

| Note | For information on upgrading ESXi version, see the ReadMe of applicable OVAs availale at https://software.cisco.com/download/home/283062758/type . |
|---|---|

| Step 1 | Sign in to a
                                    			 computer with a high-speed Internet connection, and go to the Voice and Unified
                                    			 Communications Downloads page at http://www.cisco.com/cisco/software/navigator.html?mdfid=280082558 . Note To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user. | Note | To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user. |
|---|---|---|---|
| Note | To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user. |
| Step 2 | In the tree
                                    			 control on the Downloads page, expand Products >
                                       				Unified Communications >Unified Communications Applications > Messaging
                                       				> Unity Connection, and select Cisco Unity
                                       				Connection Virtualization . |
| Step 3 | On the Download Software page, select OVA-15 , and the download links appear on the right side of the page. |
| Step 4 | Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download file sizes appear below the download links.) |
| Step 5 | Select the
                                    			 applicable link to download. Restricted version UCSInstall_CUC_15.0.1.10000-24.sgn.iso Unrestricted version UCSInstall_CUC_UNRST_15.0.1.10000-24.sgn.iso The following
                                       				configurations are available with the OVA file, and you can select the required
                                       				configurations for deploying the OVA template: For up to 1,000 Unity
                                          				  Connection users. Configures two virtual CPU, 10 GB RAM, and one 160-GB virtual disk with the file system aligned at 64KB blocks. For up to 5,000 Unity
                                          				  Connection users. Configures two virtual CPUs, 12 GB RAM, and one 200-GB virtual disk with the file system aligned at 64KB blocks. For up to 10,000 Unity
                                          				  Connection users. Configures four virtual CPUs, 12 GB RAM, and two 146-GB virtual disks with the file system aligned at 64 KB blocks. Comes
                                                   						  in 3 variations: 146 GB, 300 GB, and 500 GB. In 300 GB and 500 GB variations,
                                                   						  the datastore where the Unity Connection virtual machine will reside must be
                                                   						  formatted with a VMware VMFS block size of 2 MB or more. A block size of 1 MB
                                                   						  limits the maximum virtual hard disk size to 256 GB. A block size of 2 MB
                                                   						  allows 512 GB virtual disks. For up to 20,000 Unity
                                          				  Connection users. Configures seven virtual CPUs, 16 GB RAM, and either two 300-GB virtual disks or two 500-GB virtual disks with the file system
                                                   aligned at 64KB blocks. | Restricted version | UCSInstall_CUC_15.0.1.10000-24.sgn.iso | Unrestricted version | UCSInstall_CUC_UNRST_15.0.1.10000-24.sgn.iso |
| Restricted version | UCSInstall_CUC_15.0.1.10000-24.sgn.iso |
| Unrestricted version | UCSInstall_CUC_UNRST_15.0.1.10000-24.sgn.iso |

| Note | To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user. |
|---|---|

| Restricted version | UCSInstall_CUC_15.0.1.10000-24.sgn.iso |
|---|---|
| Unrestricted version | UCSInstall_CUC_UNRST_15.0.1.10000-24.sgn.iso |

| Note | All the locales for Unity Connection 15 are released and available on Download Software site at https://software.cisco.com/download/home/286328409/type . |
|---|---|

| Caveat Number | Component | Severity | Description |
|---|---|---|---|
| CSCwh93696 | setup | 3 | Auto switch-version can't be enabled on standalone Unity |
| CSCwj49918 | telephony | 3 | CUC: Failsafe are observed with 160K users in https network in load testing |

| Cisco
                                    					 Unified CM Component | Description |
|---|---|
| backup-restore | Backup and
                                    					 restore utilities |
| ccm-serviceability | Cisco
                                    					 Unified Serviceability web interface |
| cdp | Cisco
                                    					 Discovery Protocol Drivers |
| cli | Command-line interface (CLI) |
| cmui | Certain
                                    					 elements in the Unity Connection web interfaces (such as search tables and
                                    					 splash screens) |
| cpi-afg | Cisco
                                    					 Unified Communications Answer File Generator |
| cpi-appinstall | Installation and upgrades |
| cpi-cert-mgmt | Certificate management |
| cpi-diagnose | Automated
                                    					 diagnostics system |
| cpi-os | Cisco
                                    					 Unified Communications Operating System |
| cpi-platform-api | Abstraction layer between the Cisco Unified Communications
                                    					 Operating System and the applications hosted on the platform |
| cpi-security | Security
                                    					 for connections to the server |
| cpi-service-mgr | Service
                                    					 Manager (ServM) |
| cpi-vendor | External
                                    					 vendor issues |
| cuc-tomcat | Apache
                                    					 Tomcat and third-party software |
| database | Installation and access to the configuration database (IDS) |
| database-ids | IDS
                                    					 database patches |
| ims | Identity
                                    					 Management System (IMS) |
| rtmt | Real-Time Monitoring Tool (RTMT) |