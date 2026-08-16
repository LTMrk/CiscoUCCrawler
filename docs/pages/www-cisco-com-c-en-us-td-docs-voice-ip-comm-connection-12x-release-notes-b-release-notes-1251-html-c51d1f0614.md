---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-release-notes-b-release-notes-1251-html-c51d1f0614
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/release/notes/b_Release_Notes_1251.html
retrieved_at: 2026-08-16T18:49:49.015277+00:00
---

Release Notes for Cisco Unity Connection Release 12.5(1)

# Release Notes for Cisco Unity Connection Release 12.5(1)

- 12.5(1)

- 12.0(1)

### Download Options

Updated: January 24, 2019

# Release Notes for
            	 Cisco Unity Connection Release 12.5(1)

These release notes
               		contain information on Cisco Unity Connection 12.5(1) new and changed
               		functionality, upgrade information, limitations, and restrictions.

## Contents

## System
               	 Requirements

System Requirements
                  		for Cisco Unity Connection Release 12.x at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

## Upgrade
               	 Information

You can upgrade from Unity Connection 12.0(1), 11.x, 10.x, 9.x and 8.x to Unity Connection 12.5(1). For more information on
                  upgrade process and supported upgrade paths, see the " Upgrading Cisco Unity Connection " chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

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

Start a command-line
                                    			 interface (CLI) session. (For more information, see the Cisco Unified
                                    			 Communications Operating System Administration Help.)

Run the show cuc version command to view the Unity Connection.

### Cisco Personal
                  	 Communications Assistant Application

This section contains the
                        		  procedure to determine the version using Cisco PCA application.

Using Cisco PCA Application

Sign in to Cisco PCA.

On the Cisco PCA Home page,
                                 			 select the About link in the upper-right corner. (The link is available
                                 			 onevery Cisco PCA page.)

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

In Cisco Unified Operating
                                    			 System Administration, the System Version is displayed below "CiscoUnified
                                    			 Operating System Administration" in the blue banner on the page that appears
                                    			 after you sign in.

#### Using the
                     	 Command-Line Interface

Before you begin

##### Before you begin

Start a command-line
                                    			 interface session. (For more information, see Cisco Unified Operating System
                                    			 Administration Help.)

Run the show version active command to view the Cisco Unified
                                    			 Operating System Administration version.

## Related
               	 Documentation

For
                        			 virtualization requirements, see the "Requirements for Installing Unity
                        			 Connection 12.x on a Virtual Machine" section and for the default license file,
                        			 see the "Licensing Requirements" section of the System
                           				Requirements for Cisco Unity Connection Release 12.x at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

- For instructions on
                     		  migrating from an existing Unity Connection physical server to a new virtual
                     		  machine, see the "Migrating a Physical Server to a Virtual Machine" section of
                     		  "Maintaining Unity Connection Server" chapter of the Install,
                        			 Upgrade, and Maintenance Guide for Cisco Unity Connection 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

- For more information on
                     		  Unity Connection complete documentation see the Documentation
                        			 Guide for Cisco Unity Connection Release 12.x at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/roadmap/b_12xcucdg.html .

## New Functionality-Release 12.5(1)

This section contains information about new functionality in the 12.5(1) release time frame only.

### Cipher
                  	 Management

With Unity Connection 12.5(1) and later, a new feature Cipher Management is introduced to enhance the security by controlling the set of ciphers for different secure interfaces of Cisco Unity Connection.
                     To meet the security requirement of an organization, Cipher Management allows administrator to configure ciphers for different
                     secure interfaces such as TLS and SSH.

For more information on Cipher Management, see the " Security " chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 12.x available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/os_administration/b_12xcucosagx.html .

### Support of "Read Only Administrator" System Role

With Unity Connection 12.5(1) and later, a new System Role "Read Only Administrator" is introduced having access to view all
                     Unity Connection administrative functions.

This System Role provides read only access for the  following pages:

All Cisco Unity Connection Administration pages

Cisco Unified CM driven pages

RTMT Client

Cisco Unity Connection Serviceability pages

For more information on System Roles, see " User attributes " chapter of System Administration Guide for Cisco Unity Connection Release 12.x available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

### Specific License
                  	 Reservation

Unity Connection 12.5(1) and later provides Specific License Reservation feature that allows you to reserve the licenses or entitlements from your virtual account and associate them with the product
                     instance. The product instance can use the reserved licenses without communicating usage information to CSSM.

For more information on Specific License Reservation, see " Managing Licenses " chapter of Install, Upgrade, and Maintenance Guide for Cisco Unity Connection available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

### Branding
                  	 Customization

Unity Connection 12.5(1) and later introduces a feature Branding Customization by which the appearance of Unity Connection
                     web applications can be modified based on the organizational requirements.This feature allows an Operating System Administrator
                     to customize company logo, background colors, border colors and font colors of Unity Connection web applications. Branding
                     can be applied on the following web applications of Unity Connection:

Cisco Unity Connection Administration

Cisco Personal Communications Assistant

Web Inbox

For more information on Branding customization in Unity Connection, see the " Software Upgrades " chapter of the Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 12.x available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/os_administration/b_12xcucosagx.html

### Session Termination of Web Interfaces

With Unity Connection 12.5(1) and later, a Platform Administrator can terminate the active sessions that a user or administrator
                     have on the various web interfaces of Cisco Unity Connection through Session Management page of Cisco Unified OS Administration.

Session Termination is applicable for the following web interfaces:

Cisco Unity Connection Administration

Cisco Unity Connection Serviceability

Cisco Unified Serviceability

Cisco Personal Communications Assistant

Cisco Unity Connection Web Inbox

Cisco Unity Connection SRSV

For more inforation on the session termination, see Security chapter of the Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 12.x guide available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/os_administration/b_12xcucosagx.html .

## Changed
               	 Functionality - Release 12.5(1)

This section
                  		contains information about changed functionality in the 12.5(1) release time
                  		frame only.

### Concurrent Web-Session Limit

In Unity Connection 11.5(1) and later, a System Administrator was allowed to configure the maximum number of concurrent sessions
                     for a user on telephony, Visual Voicemail and IMAP interfaces.

With Unity Connection 12.5(1) and later, using set webapp session maxlimit <sessionlimit> CLI command, a Platform Administrator can configure the maximum number of concurrent sessions that a user or administrator
                     can have on the various web interfaces of Cisco Unity Connection. If the user or administrator attempts a new session beyond
                     the configured maximum limit, the login gets failed.

Concurrent web-session limit includes the session on the following interfaces:

Cisco Unity Connection Administration

Cisco Unity Connection Serviceability

Cisco Unified Serviceability

Cisco Personal Communications Assistant

Cisco Unity Connection Web Inbox

Cisco Unity Connection SRSV

The feature is not applicable for RTMT, Jabber and ViewMail for Outlook.

For more information of concurrent web session limit, see "Restricting the Concurrent Web Sessions" section of Passwords, PINs, and Authentication Rule Management chapter in Security Guide for Cisco Unity Connection Release 12.x guide available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/b_12xcucsecx.html

### Custom Roles

Unity Connection 12.5(1) and later provides the enhanced way of handling the Custom Roles . With this release, administrator has an option to inherit the privileges of a system role while creating or modifying the
                     custom roles.

Following are the system roles that can be inherited:

Audio Text Administrator

Greeting Administrator

Help Desk Administrator

Technician

User Administrator

Tenant Administrator

With this release, administrator can also create, modify or delete a custom role using REST API.

Each new custom role has read only access privilege by default.

For more information on Custom Roles functionality, see " User Attributes " chapter of System Administration Guide for Cisco Unity Connection Release 12.x available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

For information on Custom Roles API, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/APIs_Pages/b_Cisco_Unity_Connection_APIs.html .

### Rest API Support
                  	 for Cisco Smart Software Licensing

Unity Connection 12.5(1) and later provides the REST API support to perform various operations of Cisco Smart Software Licensing.

For more information on the APIs for Cisco Smart Software Licensing, see Documentation for Cisco Unity Connection API available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/APIs_Pages/b_Cisco_Unity_Connection_APIs.html .

### Video Message Playback Support over Web Inbox

With Unity Connection 12.5(1) and later, the end user gets an additional functionality to play all the Video Messages using
                     Web Inbox through telephone record and playback (TRAP). Using this functionality the user can play all the new video messages
                     that are received on Unity Connection 12.5(1) and later. The video messages that are received before upgrading to Unity connection
                     12.5(1) will be played as audio only.

For more information on Web Inbox , see Quick Start Guide for the Cisco Unity Connection Web Inbox Release 12.x available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/quick_start/guide/b_12xcucqsginbox.html .

For more information on Video Messaging, see the " Video Messaging " chapter of Design Guide for Cisco Unity Connection 12.x available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg.html .

## Installation and
               	 Upgrade Information

### Installing Cisco
                  	 Unity Connection for the First Time on a Virtual Machine

You must download
                     		and deploy a VMware OVA template, which automatically configures the virtual
                     		machine for Unity Connection. To download the template, see the next section,
                     		“ Downloading
                        		  a VMware OVA Template for a Unity Connection 12.5(1) Virtual Machine .”
                     		The installation and migration documentation tells you when to deploy the
                     		template.

Before installing Cisco Unity Connection 12.5(1) and later, make sure that the virtual machine has ESXi version 6.5 U2 and
                                 VM version 13.

For information on upgrading ESXi version, see the ReadMe of applicable OVAs availale at https://software.cisco.com/download/home/283062758/type .

#### Downloading a
                     	 VMware OVA Template for a Unity Connection 12.5(1) Virtual Machine

It is recommended
                           		  to use VMware OVA template to configure VMware for Unity Connection, which
                           		  simplifies the process of configuring the virtual machine. If you want to
                           		  deploy the VMware OVA template for Unity Connection, do the following procedure
                           		  to download the OVA file.

Procedure to
                           		  download a VMware OVA template:

Sign in to a
                                    			 computer with a high-speed Internet connection, and go to the Voice and Unified
                                    			 Communications Downloads page at http://www.cisco.com/cisco/software/navigator.html?mdfid=280082558 .

To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user.

In the tree
                                    			 control on the Downloads page, expand Products >
                                       				Unified Communications >Unified Communications Applications > Messaging
                                       				> Unity Connection, and select Cisco Unity
                                       				Connection Virtualization .

On the Download
                                       				Software page, select OVA-12.5(1) , and the download links appear on the right side
                                    			 of the page.

Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download file sizes appear below the download links.)

Select the
                                    			 applicable link to download.

Restricted version

UCSInstall_CUC_12.5.1.10000-23.sgn.iso

Unrestricted version

UCSInstall_CUC_UNRST_12.5.1.10000-23.sgn.iso

The following
                                       				configurations are available with the OVA file, and you can select the required
                                       				configurations for deploying the OVA template:

Configures one virtual CPU, 4 GB RAM, and one 160-GB virtual
                                                   						  disk with the file system aligned at 64KB blocks.

Configures two virtual CPU, 4 GB RAM, and one 160-GB virtual
                                                   						  disk with the file system aligned at 64KB blocks.

Configures two virtual CPUs, 6 GB RAM, and one 200-GB virtual
                                                   						  disk with the file system aligned at 64KB blocks.

Configures four virtual CPUs, 6 GB RAM, and two 146-GB virtual
                                                   						  disks with the file system aligned at 64 KB blocks.

Comes
                                                   						  in 3 variations: 146 GB, 300 GB, and 500 GB. In 300 GB and 500 GB variations,
                                                   						  the datastore where the Unity Connection virtual machine will reside must be
                                                   						  formatted with a VMware VMFS block size of 2 MB or more. A block size of 1 MB
                                                   						  limits the maximum virtual hard disk size to 256 GB. A block size of 2 MB
                                                   						  allows 512 GB virtual disks.

Configures seven virtual CPUs, 8 GB RAM, and either two 300-GB
                                                   						  virtual disks or two 500-GB virtual disks with the file system aligned at 64KB
                                                   						  blocks.

Configures seven virtual CPUs, 10 GB RAM, and either two 300-GB
                                                   						  virtual disks or two 500-GB virtual disks with the file system aligned at 64KB
                                                   						  blocks.

### Installation and
                  	 Upgrade Notes

#### Installing
                     	 Additional Unity Connection Languages

All the locales
                                    		  for Unity Connection 12.5(1) are released.

For instructions on
                        		installing additional Unity Connection languages on the following server types,
                        		see the referenced documentation:

- On a Unity Connection
                           		  server, see the “ Adding and Removing Unity
                              			 Connection Languages ” section of “Maintaining Cisco Unity Connection
                           		  Server” chapter of the Install,
                              			 Upgrade, and Maintenance Guide for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

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

If you revert from
                        		Unity Connection 12.5(1) to an earlier version of Unity Connection, some of the
                        		data for new Unity Connection 12.5(1) features is lost and cannot be retrieved
                        		when you upgrade again to Unity Connection 12.5(1).

## Limitations and
               	 Restrictions

### Secure Messaging
                  	 Limitations Regarding ViewMail

Adding non-audio attachments to secure messages composed in Cisco ViewMail for Microsoft Outlook version 11.0 and later is
                     not supported with Unity Connection 12.5(1).

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

You can find the latest caveat information for Cisco Unity Connection version 12.5(1) by using the Bug Search tool, an online
                     tool available for customers to query defects according to their own needs at https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=280082558&rls=12.5&sb=fr&svr=3nH&bt=custV . Bug Search tool is available at https:/​/​tools.cisco.com/​bugsearch . To access Bug Search tool, you must be logged on to Cisco.com as a registered user.

### Open Caveats—Unity
                  	 Connection Release 12.5(1)

Caveat Number

Component

Severity

Description

CSCvn51470

licensing

3

Smart licensing register operation failed with incorrect proxy server

### Related
                  	 Caveats—Cisco Unified Communications Manager 12.5(1) Components Used by Unity
                  	 Connection 12.5(1)

Table
                           			 2 describes the Cisco Unified CM components used by Unity Connection.
                        		  Caveat information for the Cisco Unified CM components is available in Release Notes
                           			 for Cisco Unified Communications Manager Release 12.5(1) at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html .

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

### This Document Applies to These Products

- Unity Connection Version 12.x

| In Cisco Unity Connection
                                    			 Administration, in the upper-right corner below the Navigation list, select About . |
|---|

| Step 1 | Start a command-line
                                    			 interface (CLI) session. (For more information, see the Cisco Unified
                                    			 Communications Operating System Administration Help.) |
|---|---|
| Step 2 | Run the show cuc version command to view the Unity Connection. |

| Step 1 | Sign in to Cisco PCA. |
|---|---|
| Step 2 | On the Cisco PCA Home page,
                                 			 select the About link in the upper-right corner. (The link is available
                                 			 onevery Cisco PCA page.) |
| Step 3 | The Unity Connection version
                                 			 is displayed, which is same as the version of Cisco PCA. |

| In Cisco Unified Operating
                                    			 System Administration, the System Version is displayed below "CiscoUnified
                                    			 Operating System Administration" in the blue banner on the page that appears
                                    			 after you sign in. |
|---|

| Step 1 | Start a command-line
                                    			 interface session. (For more information, see Cisco Unified Operating System
                                    			 Administration Help.) |
|---|---|
| Step 2 | Run the show version active command to view the Cisco Unified
                                    			 Operating System Administration version. |

| Note | The feature is not applicable for RTMT, Jabber and ViewMail for Outlook. |
|---|---|

| Note | Each new custom role has read only access privilege by default. |
|---|---|

| Note | Before installing Cisco Unity Connection 12.5(1) and later, make sure that the virtual machine has ESXi version 6.5 U2 and
                                 VM version 13. For information on upgrading ESXi version, see the ReadMe of applicable OVAs availale at https://software.cisco.com/download/home/283062758/type . |
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
| Step 3 | On the Download
                                       				Software page, select OVA-12.5(1) , and the download links appear on the right side
                                    			 of the page. |
| Step 4 | Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download file sizes appear below the download links.) |
| Step 5 | Select the
                                    			 applicable link to download. Restricted version UCSInstall_CUC_12.5.1.10000-23.sgn.iso Unrestricted version UCSInstall_CUC_UNRST_12.5.1.10000-23.sgn.iso The following
                                       				configurations are available with the OVA file, and you can select the required
                                       				configurations for deploying the OVA template: For up to 1,000 Unity
                                          				  Connection users. Configures one virtual CPU, 4 GB RAM, and one 160-GB virtual
                                                   						  disk with the file system aligned at 64KB blocks. Configures two virtual CPU, 4 GB RAM, and one 160-GB virtual
                                                   						  disk with the file system aligned at 64KB blocks. For up to 5,000 Unity
                                          				  Connection users. Configures two virtual CPUs, 6 GB RAM, and one 200-GB virtual
                                                   						  disk with the file system aligned at 64KB blocks. For up to 10,000 Unity
                                          				  Connection users. Configures four virtual CPUs, 6 GB RAM, and two 146-GB virtual
                                                   						  disks with the file system aligned at 64 KB blocks. Comes
                                                   						  in 3 variations: 146 GB, 300 GB, and 500 GB. In 300 GB and 500 GB variations,
                                                   						  the datastore where the Unity Connection virtual machine will reside must be
                                                   						  formatted with a VMware VMFS block size of 2 MB or more. A block size of 1 MB
                                                   						  limits the maximum virtual hard disk size to 256 GB. A block size of 2 MB
                                                   						  allows 512 GB virtual disks. For up to 20,000 Unity
                                          				  Connection users. Configures seven virtual CPUs, 8 GB RAM, and either two 300-GB
                                                   						  virtual disks or two 500-GB virtual disks with the file system aligned at 64KB
                                                   						  blocks. Configures seven virtual CPUs, 10 GB RAM, and either two 300-GB
                                                   						  virtual disks or two 500-GB virtual disks with the file system aligned at 64KB
                                                   						  blocks. | Restricted version | UCSInstall_CUC_12.5.1.10000-23.sgn.iso | Unrestricted version | UCSInstall_CUC_UNRST_12.5.1.10000-23.sgn.iso |
| Restricted version | UCSInstall_CUC_12.5.1.10000-23.sgn.iso |
| Unrestricted version | UCSInstall_CUC_UNRST_12.5.1.10000-23.sgn.iso |

| Note | To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user. |
|---|---|

| Restricted version | UCSInstall_CUC_12.5.1.10000-23.sgn.iso |
|---|---|
| Unrestricted version | UCSInstall_CUC_UNRST_12.5.1.10000-23.sgn.iso |

| Note | All the locales
                                    		  for Unity Connection 12.5(1) are released. |
|---|---|

| Caveat Number | Component | Severity | Description |
|---|---|---|---|
| CSCvn51470 | licensing | 3 | Smart licensing register operation failed with incorrect proxy server |

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