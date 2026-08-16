---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-release-notes-b-release-notes-1201-html-082df93b13
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/release/notes/b_Release_Notes_1201.html
retrieved_at: 2026-08-16T18:49:53.302036+00:00
---

Release Notes for Cisco Unity Connection Release 12.0(1)

# Release Notes for Cisco Unity Connection Release 12.0(1)

- 12.5(1)

- 12.0(1)

### Download Options

Updated: August 31, 2017

# Release Notes for
	 Cisco Unity Connection Release 12.0(1)

These release notes
		contain information on Cisco Unity Connection 12.0(1) new and changed
		functionality, upgrade information, limitations, and restrictions.

Contents

## Contents

## System
	 Requirements

System Requirements
		for Cisco Unity Connection Release 12.x at http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​requirements/​b_​12xcucsysreqs.html .

## Upgrade
	 Information

You can upgrade from
		Unity Connection 11.x, 10.x, 9.x, and 8.x to Unity Connection 12.0(1).For more
		information on upgrade process and supported upgrade paths, see the " Upgrading Cisco Unity
		  Connection " chapter of the Install, Upgrade,
		  and Maintenance Guide for Cisco Unity Connection Release 12.x at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​install_upgrade/​guide/​b_​12xcuciumg.html .

## Determining the
	 Software Version

This section contains procedures
		for determining the version in use for the following software:

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

### Cisco Personal
	 Communications Assistant Application

This section contains the
		  procedure to determine the version using Cisco PCA application.

Using Cisco PCA Application

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

## Related
	 Documentation

For
			 virtualization requirements, see the "Requirements for Installing Unity
			 Connection 12.x on a Virtual Machine" section and for the default license file,
			 see the "Licensing Requirements" section of the System
				Requirements for Cisco Unity Connection Release 12.x at http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​requirements/​b_​12xcucsysreqs.html .

- For instructions on
		  migrating from an existing Unity Connection physical server to a new virtual
		  machine, see the "Migrating a Physical Server to a Virtual Machine" section of
		  "Maintaining Unity Connection Server" chapter of the Install,
			 Upgrade, and Maintenance Guide for Cisco Unity Connection 12.x at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​install_upgrade/​guide/​b_​12xcuciumg.html .

- For more information on
		  Unity Connection complete documentation see the Documentation
			 Guide for Cisco Unity Connection Release 12.x at http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​roadmap/​b_​12xcucdg.html .

## New and Changed
	 Functionality-Release 12.0(1)

This section
		contains information about new and changed functionality in the 12.0(1) release
		time frame only.

### Support for Cisco
	 Unity Connection ISO

In earlier releases, a common installer was used for Cisco Unity
		Connection and Cisco Unified CM. With release 12.0(1) and later, Unity
		Connection provides a specific installer that has been separated from Cisco
		Unified CM. The new installer for Cisco Unity Connection is available at
		Software Download site with UCSInstall_CUC ISO name. However, Unity Connection will still
		provide all the latest VOS changes. To see the active and inactive VOS version
		integrated with Unity Connection, a new CLI command "show vos version" is
		introduced.

For more information on the CLI command, see Command Line Interface Reference Guide for Cisco Unified
		  Communications Solutions available at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-maintenance-guides-list.html

The installation process for Cisco Unity Connection remains same for the
		specific ISO but for upgrading Cisco Unity Connection from any earlier releases
		to 12.0(1) or later, you must install a " ciscocm.cuc_upgrade_12_0.cop.sgn" COP
		file on the server. For more information to install the COP file, see Install, Upgrade, and Maintenance Guide for Cisco Unity Connection
		  Release 12.x available at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​install_upgrade/​guide/​b_​12xcuciumg.html .

### Cisco Smart
	 Software Licensing

With Unity
		Connection 12.0(1) and later, Prime License Manager is replaced by Cisco Smart
		Software Manager (CSSM) and Cisco Smart Software Licensing is introduced to use
		the various licensed feature of Cisco Unity Connection.

Cisco Smart Software
		Licensing is a new and enhanced way of licensing. It adds flexibility to your
		licensing and simplifies it across the enterprise. Cisco Smart Software
		Licensing provides visibility into your license ownership and consumption.

Cisco Smart Software
		Licensing reduces the complexity of the earlier model of licenses and it also
		removes the requirement of Product Activation Key (PAK). Using Cisco Smart
		Software Licensing, you can maintain your licenses by using a single interface
		of Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

For more information
		of Cisco Smart Software Licensing, see "Managing Licenses" chapter of the Install, Upgrade,
		  and Maintenance Guide for Cisco Unity Connection Release 12.x available at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​install_upgrade/​guide/​b_​12xcuciumg.html

### Support for Opus
	 Codec

With Unity
		Connection 12.0(1) and later, administrator can configure a wideband audio
		codec, Opus Codec to
		enhance the voice quality of playback and recording media. Opus codec is used
		as a line codec or advertising codec that is negotiated between the calling
		device and Unity Connection. The Opus codec requires more computation to
		transcode, and therefore places a significant additional load on the Unity
		Connection server.

For more information
		on Opus Codec, see "Audio Codec" section of the "Sizing and Scaling Cisco Unity
		Connection Servers" chapter of Design Guide for
		  Cisco Unity Connection 12.x available at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​design/​guide/​b_​12xcucdg.html

### Support for
	 Authorization Code Grant Flow

Unity Connection 12.0(1) and later provides an enhancement to the SSO
		and non SSO login experience for Jabber users by providing the support of OAuth 2.0 Authorization Code Grant Flow . For faster login,
		Authorization Code Grant Flow uses an Authorization Server (Authz Server) to
		provide access and refresh tokens to the Jabber client. After configuring an
		Authz server, Unity Connection uses authorization keys provided by Authz server
		to validate the token of a Jabber client.

For more information on the Authz server and its configuration, see
		"Authz Server" section of the "System Settings" chapter of the System Administration Guide for Cisco Unity Connection Release
		  12.x available at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​administration/​guide/​b_​12xcucsag.html

### Support for
	 Minimum TLS Version

With Unity
		Connection 12.0(1) and later, administrator can configure minimum Transport
		Layer Security (TLS) protocol version to comply with the organization security
		policies. Unity Connection supports TLS 1.0, TLS 1.1 and TLS 1.2 for secure
		communication across various interfaces of Cisco Unity Connection.

To configure the
		minimum TLS version on Unity Connection, a new CLI command set tls min-version <tls minVersion> is introduced. By
		default, TLS 1.0 is configured.

For more information on the CLI command, see Command Line Interface Reference Guide for Cisco Unified
		  Communications Solutions available at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-maintenance-guides-list.html .

For more information
		on Minimum TLS Version, see "Securing Transport Layer" section of "IP
		Communications Required by Cisco Unity Connection" chapter of Security Guide for
		  Cisco Unity Connection Release 12.x available at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​security/​b_​12xcucsecx.html .

### SAML SSO Support
	 for Platform Interfaces

With Unity Connection 12.0(1) and
		later, the Cisco Unified OS Administration and Disaster Recovery System are now
		the Security Assertion Markup Language (SAML) SSO-supported applications. If
		SAML SSO is enabled, you can launch these applications or other supported
		applications, such as Cisco Unity Connection and Cisco Unified CM after a
		single sign-in with an Identity Provider (IdP). You no longer need to sign in
		to these applications separately.

For more information on accessing platform applications using SAML SSO,
		see Quick Start Guide for SAML SSO Access available at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​quick_start/​guide/​b_​12xcucqssamlsso.html

### Enhancement in
	 Number of Secure Jabber Endpoints

Unity Connection
		12.0(1) and later supports increased number of secure Jabber endpoints. To
		deploy the secure Jabber endpoints in Unity Connection, a 7vCPU OVA is required
		with additional RAM of 2GB.

For more information
		on secure Jabber endpoints, see Cisco Unity
		  Connection 12.x Supported Platforms List available at http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​supported_platforms/​b_​12xcucspl.html .

### Cisco Unity
	 Connection- Restricted and Unrestricted Version

Cisco Unity
		Connection provides two versions of the Connection software-restricted and
		unrestricted-that address import requirements for some countries related to
		encryption of user data. Restricted version of the Cisco Unity Connection
		allows you to use the all security modules whereas with Unrestricted version,
		you cannot use the security modules of Cisco Unity Connection.

In earlier releases,
		by default encryption was enabled on Cisco Unity Connection. Unity Connection
		12.0(1) and later allows you to enable or disable the encryption on the product
		Restricted version. In Evaluation Mode (referred as Demo in PLM), the
		encryption on the product is disabled by default. It means you are not allowed
		to use the security modules of Cisco Unity Connection in Evaluation Mode. You
		can enable the encryption on Unity Connection only when the product is
		registered with Cisco Smart Software Manager (CSSM) or Cisco Smart Software
		Manager satellite using token that allows Export-Controlled Functionality.

For more information
		on the encryption behavior of Restricted and Unrestricted version of Unity
		Connection, see "Cisco Unity Connection - Restricted and Unrestricted Version"
		chapter of Security Guide for Cisco Unity Connection available at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​security/​b_​12xcucsecx.html

Following new CLI
		command is introduced to enable or disable the encryption on Cisco Unity
		Connection 12.0(1) and later:

utils cuc encryption
		  <enable/disable>

For more information
		on the CLI, see the Command Line Interface Reference Guide for Cisco Unified
		Solutions for the latest release, available at https:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-maintenance-guides-list.html

## Installation and
	 Upgrade Information

### Installing Cisco
	 Unity Connection for the First Time on a Virtual Machine

You must download
		and deploy a VMware OVA template, which automatically configures the virtual
		machine for Unity Connection. To download the template, see the next section,
		“ Downloading
		  a VMware OVA Template for a Unity Connection 12.0(1) Virtual Machine .”
		The installation and migration documentation tells you when to deploy the
		template.

#### Downloading a
	 VMware OVA Template for a Unity Connection 12.0(1) Virtual Machine

It is recommended
		  to use VMware OVA template to configure VMware for Unity Connection, which
		  simplifies the process of configuring the virtual machine. If you want to
		  deploy the VMware OVA template for Unity Connection, do the following procedure
		  to download the OVA file.

Procedure to
		  download a VMware OVA template:

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

For instructions on
		installing additional Unity Connection languages on the following server types,
		see the referenced documentation:

- On a Unity Connection
		  server, see the “ Adding and Removing Unity
			 Connection Languages ” section of “Maintaining Cisco Unity Connection
		  Server” chapter of the Install,
			 Upgrade, and Maintenance Guide for Cisco Unity Connection at https:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​connection/​12x/​install_upgrade/​guide/​b_​12xcuciumg.html .

If you are
			 installing Japanese because you want Cisco Unity Connection Administration to
			 be localized, you must also install the Cisco Unified Communications Manager
			 Japanese locale. See the “Locale Installation” section in the “Software
			 Upgrades” chapter of the applicable Cisco Unified
				Communications Operating System Administration Guide at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-maintenance-guides-list.html .

If you are
			 installing other languages because you want the Cisco Personal Communications
			 Assistant to be localized, you must also install the corresponding Cisco
			 Unified Communications Manager locales. See the “Locale Installation” section
			 in the “Software Upgrades” chapter of the Cisco Unified
				Communications Operating System Administration Guide at http:/​/​www.cisco.com/​en/​US/​products/​sw/​voicesw/​ps556/​prod_​maintenance_​guides_​list.html .

#### Reverting a Server
	 to the Unity Connection Version on the Inactive Partition

If you revert from
		Unity Connection 12.0(1) to an earlier version of Unity Connection, some of the
		data for new Unity Connection 12.0(1) features is lost and cannot be retrieved
		when you upgrade again to Unity Connection 12.0(1).

## Limitations and
	 Restrictions

### Secure Messaging
	 Limitations Regarding ViewMail

Adding non-audio
		attachments to secure messages composed in Cisco ViewMail for Microsoft Outlook
		version 8.5 and later is not supported with Unity Connection 12.0(1).

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

You can find the
		latest caveat information for Cisco Unity Connection version 12.0(1) by using
		the Bug Search tool, an online tool available for customers to query defects
		according to their own needs at https:/​/​bst.cloudapps.cisco.com/​bugsearch/​search?kw=*&pf=prdNm&pfVal=280082558&rls=12.0&sb=fr&svr=3nH&bt=custV .
		Bug Search tool is available at https:/​​/​​tools.cisco.com/​​bugsearch . To access Bug
		Search tool, you must be logged on to Cisco.com as a registered user.

### Open Caveats—Unity
	 Connection Release 12.0(1)

This section list
		  any Severity 1, 2, and 3 open caveats when Unity Connection version 12.0(1) was
		  released.

### Related
	 Caveats—Cisco Unified Communications Manager 12.0(1) Components Used by Unity
	 Connection 12.0(1)

Table
			 2 describes the Cisco Unified CM components used by Unity Connection.
		  Caveat information for the Cisco Unified CM components is available in Release Notes
			 for Cisco Unified Communications Manager Release 12.0(1) at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-release-notes-list.html .

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

http:/​/​www.cisco.com/​en/​US/​docs/​general/​whatsnew/​whatsnew.html

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

Further information regarding U.S. export regulations may be found at http:/​/​www.access.gpo.gov/​bis/​ear/​ear_​data.html .

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

| Note | If networking
		  (except VPIM) is configured on the system, you can use Opus codec as line codec
		  to get the highest audio quality only when all the nodes are on Opus codec
		  supported version or higher version. |
|---|---|

| Note | When SAML SSO support is enabled for a Cisco Unity Connection
		  administrator, it is applicable across the cluster. |
|---|---|

| Step 1 | Sign in to a
			 computer with a high-speed Internet connection, and go to the Voice and Unified
			 Communications Downloads page at http:/​/​www.cisco.com/​cisco/​software/​navigator.html?mdfid=280082558 . Note To access
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
				Software page, select OVA-12.0(1) , and the download links appear on the right side
			 of the page. |
| Step 4 | Confirm that
			 the computer you are using has sufficient hard-disk space for the downloaded
			 files. (The download file sizes appear below the download links.) |
| Step 5 | Select the
			 applicable link to download. Restricted version UCSInstall_CUC_12.0.1.10000-8.sgn.iso Unrestricted version UCSInstall_CUC_UNRST_12.0.1.10000-8.sgn.iso The following
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
						  blocks. | Restricted version | UCSInstall_CUC_12.0.1.10000-8.sgn.iso | Unrestricted version | UCSInstall_CUC_UNRST_12.0.1.10000-8.sgn.iso |
| Restricted version | UCSInstall_CUC_12.0.1.10000-8.sgn.iso |
| Unrestricted version | UCSInstall_CUC_UNRST_12.0.1.10000-8.sgn.iso |

| Note | To access
				the software download page, you must be signed in to Cisco.com as a registered
				user. |
|---|---|

| Restricted version | UCSInstall_CUC_12.0.1.10000-8.sgn.iso |
|---|---|
| Unrestricted version | UCSInstall_CUC_UNRST_12.0.1.10000-8.sgn.iso |

| Note | All the locales
		  for Unity Connection 12.0(1) are released. |
|---|---|

| Caveat Number | Component | Severity | Description |
|---|---|---|---|
| CSCvf61828 | Admin | 3 | Users prompted to change
				  PIN/Password when "Credentials Expires After" set as "Never" in Auth Rule |
| CSCvf73846 | Licensing | 3 | "Smart Licensing Registration Expired" RTMT
				  Alerts on CUC Subscriber server |

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