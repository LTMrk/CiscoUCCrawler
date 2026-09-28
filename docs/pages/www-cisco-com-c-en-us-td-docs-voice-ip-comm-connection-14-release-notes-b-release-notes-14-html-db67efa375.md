---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-release-notes-b-release-notes-14-html-db67efa375
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/release/notes/b_Release_Notes_14.html
retrieved_at: 2026-08-16T18:49:35.537350+00:00
---

Release Notes for Cisco Unity Connection Release 14

# Release Notes for Cisco Unity Connection Release 14

- 14

- 14

### Download Options

Updated: March 31, 2021

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

## New Functionality-Release 15

This section contains information about new functionality in the 15 release time frame only.

### Simplifying Release Number Scheme

Cisco Unity Connection Release 14 and later, has adopted single number release plan. There will be no (dot)releases like (dot)5
                     in past version releases. Service Upgrade release will be published on top of the main release through its Software Maintenance
                     cycle.

### Unified Messaging with Google Workspace

Cisco Unity Connection 15 and later, provides user a new way to access the work emails and voice messages on the Gmail account.
                     It allows administrator to integrate unified messaging with Google Workspace. Using Google Workspace, you can configure Unity
                     Connection to synchronize voice messages between Unity Connection and Gmail Server. All Unity Connection voice messages that
                     are sent to user, are first stored in Unity Connection and then synchronized to the user's Gmail account.

For more information on configuring unified messaging with Google Workspace, see " Configuring Unified Messaging " chapter of Unified Messaging Guide for Cisco Unity Connection 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html

### Resource Control through Docker Containerization

Cisco Unity Connection Release 15 and later, supports resource control through Docker containerization. The main aim of this
                     feature is to prevent the running Tomcat web application from locking out system administrator access of the application.

This feature provides following advantages:

Ensures that individual services running inside containers do not consume resources significantly above designed limits.

Restart the individual container without impacting other web applications on other containers.

For architecture details, see Resource Control through Docker Containerization section of "Cisco Unity Connection Overview" chapter in Design Guide for Cisco Unity Connection 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg.html .

For details about new CLI commands introduced to support this feature, see "Utils Commands" chapter in Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 15 , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

### Secure Access to Databases

In earlier releases, Cisco Unity Connection supports Connection Database Proxy service for accessing database through Open Database Connectivity (ODBC). By enabling this service off-box clients can access
                     the database through ODBC.

Cisco Unity Connection Release 15 and later, supports secure ODBC access to database. New secure port is introduced for listening
                     incoming requests to handle secure connections.

For information on ports, see IP Communications Required by Cisco Unity Connection chapter in Security Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15ucsecx.html .

### Digitally Sign Software and Control Keys

Cisco Unity Connection now improves the encryption for upgrading files. All COPand ISO upgrade files are now signed with the
                     SHA1SUM hash-based signing tool. SHA-1 is now deprecated and has been superseded by SHA-2 (for example SHA-512).

With Cisco Unity Connection Release 15 and later, all new COP and ISO files are signed with the SHA512SUM hash-based signing
                     tool. The COPs and ISOs have a ‘.sha512’ extension in their names instead of the ‘.sgn’ extension. For example: ciscocm.free_common_space_v1.5.cop.sha512.

For more information, see " Upgrading Cisco Unity Connection " chapter of Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

### Version Independent Licensing

Cisco Unity Connection supports Version Independent User Licenses. The Licenses are annuity-style and issued for the subscription
                     term. You can order these V14 licenses through Flex EA (Enterprise Agreement) or Flex NU (Named User—Professional, Enhanced,
                     Access). For more information, see Cisco Unity Connection Ordering Guide available at https://www.cisco.com/c/en/us/partners/tools/collaboration-ordering-guides.html .

Cisco Unity Connection 12.x continues to use the version 12.X License.

The licenses are managed on CSSM (Cisco Smart Software Manager). For more information, see the "Managing Licenses" chapter
                     of Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

### Notification Event for Transcriptions

Cisco Unity Connection Release 15 and later, supports transcription event for any new voicemails. New event is introduced
                     to notify voicemail client applications when the transcription becomes available.Client applications can now implement voicemail
                     transcriptions for end users

For more information on subscription event, see chapter Cisco Unity Connection Notification Interface (CUNI) API -- Subscribing to and Processing Notification Events of Cisco Unity Connection Notification Interface (CUNI) API Guide, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUNI_API/b_CUC_CUNI_API.html .

### SpeechView with Non MS Exchange Server

Cisco Unity Connection supports integration with mailbox other than On Premise MS Exchange Server to enable SpeechView voicemail
                     transcription. Administrator can now use Microsoft Office 365 mailbox to receive the incoming email containing the transcription
                     from the SpeechView server. It eases the deployment by removing the dependency on Microsoft Exchange Server.

## New and Changed Features

This section contains information about features in the 15 release time frame only.

### Enhanced scale for Unified Messaging with Microsoft Office 365

Cisco Unity Connection Release 15 and later, provides increase in number of maximum users for unified messaging with Microsoft
                     Office 365.

For information on number of supported users, see Cisco Unity Connection 15 Supported Platforms List available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html .

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

Bug Search tool is available at https://bst.cloudapps.cisco.com/bugsearch/ . To access Bug Search tool, you must be logged on to Cisco.com as a registered user.

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

### This Document Applies to These Products

- Unity Connection Version 14

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