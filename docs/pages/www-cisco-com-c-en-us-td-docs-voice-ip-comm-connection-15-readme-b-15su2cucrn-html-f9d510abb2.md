---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-readme-b-15su2cucrn-html-f9d510abb2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/readme/b_15su2cucrn.html
retrieved_at: 2026-08-16T18:49:06.013357+00:00
---

Readme for Cisco Unity Connection Release 15 Service Update 2

# Readme for Cisco Unity Connection Release 15 Service Update 2

- 15 Service Update 2

- 15 Service Update 1

### Download Options

Updated: September 4, 2025

First Published: October 1, 2024

Last Updated: September 4, 2025

# Release Note for Cisco Unity Connection Release 15 Service Update 2

This release note contains installation and support information for Cisco Unity Connection Release 15 Service Update 2.

## Contents

## Requirements

- System Requirements

- Compatibility Information

- Determining the Software Version

### System
                  	 Requirements

System Requirements for Cisco Unity Connection Release 15SU2 is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

### Compatibility
                  	 Information

The Compatibility Matrix for Cisco Unity Connection lists the most
                     		recent version combinations qualified to use for Cisco Unity Connection, and
                     		Unity Connection and with Cisco Business Edition (where applicable) at

http://www.cisco.com/en/US/products/ps6509/products_device_support_tables_list.html .

### Determining the
                  	 Software Version

This section
                     		contains procedures for determining the version in use for the following
                     		software:

- Determine
                           			 Version of Cisco Unity Connection Application

- Determine
                           			 Version of Cisco Personal Communications Assistant Application

- Determine
                           			 Version of Cisco Unified Communications Operating System

#### Determine Version
                     	 of Cisco Unity Connection Application

This section
                        		contains two procedures. Use the applicable procedure, depending on whether you
                        		want to use Unity Connection Administration or a command-line interface (CLI)
                        		session to determine the version.

##### Using Cisco Unity
                        	 Connection Administration

In Cisco Unity Connection
                                       			 Administration, in the upper-right corner below the Navigation list, select About .

The Unity Connection version is displayed below “Cisco Unity
                                       			 Connection Administration.”

##### Using the
                        	 Command-Line Interface

Step 1

Start a command-line
                                       			 interface (CLI) session. (For more information, see Cisco Unified Operating
                                       			 System Administration Help.)

Step 2

Run the show cuc version command.

#### Determine Version
                     	 of Cisco Personal Communications Assistant Application

##### Using Cisco
                        	 Personal Communications Assistant Application

Step 1

Sign in to the Cisco PCA.

Step 2

On the Cisco PCA Home page,
                                       			 select About in the upper right corner to display Cisco Unity
                                       			 Connection version.

Step 3

The Cisco PCA version is the
                                       			 same as the Unity Connection version.

#### Determine Version
                     	 of Cisco Unified Communications Operating System

Use the applicable procedure.

##### Using Cisco
                        	 Unified Operating System Administration

In Cisco Unified Operating
                                       			 System Administration, the System Version is displayed below “Cisco Unified
                                       			 Operating System Administration” in the blue banner on the page that appears
                                       			 after you sign in.

##### Using the
                        	 Command-Line Interface

Step 1

Start a command-line
                                       			 interface (CLI) session. (For more information, see Cisco Unified Operating
                                       			 System Administration Help.)

Step 2

Run the show version active command.

## Version and
               	 Description

Cisco Unity Connection 15SU2 is a cumulative update that incorporates all of the fixes and changes to Cisco Unity Connection
                  version 15 — including the operating system and components shared by Cisco Unity Connection and Cisco Unified CM. It also
                  incorporates additional changes that are specific to this service update.

To determine the
                  		full version number of the Cisco Unified Communications Operating System that
                  		is currently installed on the active partition, run the CLI show version
                     		  active command.

Full version numbers include the build number (for example, 15.0.1.12900-43), the software versions listed on the download
                  pages on Cisco.com are abbreviated version numbers (for example, 15SU2).

Do not refer to version numbers in any of the administration user interfaces because those versions apply to the interfaces
                  themselves, not to the version installed on the active partition.

## New and Changed
               	 Support or Functionality

This section contains all new and changed support or functionality for release 15SU2 and later.

The new locales for Unity Connection 15SU2 have been released and available on Download Software site at https://software.cisco.com/download/home/282421576/type .

## Speechview Transcription using Cisco Webex In House Transcription

Cisco Unity Connection supports the Speechview functionality with a third party transcription service, which converts the
                  voice message to text and the transcribed text is sent to the user along with the voice message. With Release 15SU2 and later,
                  Unity Connection uses the Cisco Webex in-house transcription service for transcription of voice messages.

Thirdparty transcription service will be EOL by Decemeber 30,2024. Hence customers are advised to upgrade to 15SU2 or later
                              releases. For more information see Field Notice: FN74144 - Cisco Unity Connection SpeechView Transcription Service Will Stop Working after December 30, 2024
                                 - Software Upgrade Recommended - Cisco

For more information, see chapter "SpeechView Cisco Webex in-house Transcription Service" of the System Administration Guide
                  guide available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html

## Securing Transport Layer (TLS 1.3)

Cisco Unity Connection uses Transport Layer Security(TLS) protocol for signaling and client server communication. With Release
                  of Cisco Unity Connection 15SU2, TLS version 1.3 is supported. TLS 1.3 version is faster and more secure than older version
                  of TLS. One  of the key improvements in TLS 1.3 is the reduction in handshake latency.  It significantly enhances the performance
                  of time-sensitive applications. Moreover, TS 1.3 also reduces round-trip times (RTT), by further optimizing the connection
                  establishment process. TLS 1.3 has dropped support for older and less secure cryptographic algorithms.

TLS 1.3 is not supported for below Interfaces:

- Cisco Unity Tools

- Cisco Smart Software Licensing (CSSM)

- Voice Mail for Outlook (VMO)

- Chrome Extension for Gmail

- Microsoft Exchange Server

- Microsoft Office 365

- Microsoft Outlook

For more information about the TLS 1.3 support, see the "TLS 1.3 (Applicable to Release 15 SU2 or later)" section in IP Communications Required by Cisco Unity Connection chapter of the Security Guide for Cisco Unity Connection Release 15 present at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/b_15cucsecx.html

## Related
               	 Documentation

### Documentation for
                  	 Cisco Unity Connection

For descriptions and URLs of Cisco Unity Connection documentation on Cisco.com, see the Documentation Guide for Cisco Unity Connection Release 15SU2 . The document is shipped with Unity Connection and is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

### Documentation for
                  	 Cisco Unified Communications Manager Business Edition

For descriptions and URLs of Cisco Unified Communications Manager Business Edition documentation on Cisco.com, see the applicable
                     version of Cisco Business Edition at https://www.cisco.com/c/en/us/support/unified-communications/index.html .

## Installation
               	 Information

For instructions on downloading the service update, see the " Downloading Cisco Unity Connection Release 15SU2 Software " section.

For instructions on installing the service update on Cisco Unity Connection, see the “ Upgrading Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg/b_15cuciumg_chapter_010.html .

- If you are performing an upgrade from a FIPS enabled Cisco Unity Connection release to Cisco Unity Connection 15SU2, make
                                    sure to follow the steps for regenerating certificates before using any pre-existing telephony integrations. To learn how
                                    to regenerate certificates, see the Regenerating Certificates for FIPS section of the "FIPS Compliance in Cisco Unity Connection" chapter of the Security Guide for Cisco Unity Connection Release 15SU2 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15cucsecx.html

- In FIPS mode, it is mandatory to upgrade all nodes in the Networking to Release 15 SU2 or later to ensure smooth operation
                                    and avoid replication issues.

### Downloading Cisco Unity Connection Release 15 Service Update 2 Software

The service update files can be used to upgrade Cisco Unity Connection. The files can be downloaded from the Unity Connection
                                 downloads page.

Caution

With restricted and unrestricted versions of Cisco Unity Connection software now available, download software carefully. Upgrading
                                 a restricted version to an unrestricted version is supported, but future upgrades are then limited to unrestricted versions.
                                 Upgrading an unrestricted version to a restricted version is not supported. For more information on restricted and unrestricted
                                 versions of Unity Connection software, see the Downloading a VMware OVA Template for a Unity Connection 15 Virtual Machine
                                 of the Release Notes for Cisco Unity Connection Release 15SU2 at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html .

#### Downloading Cisco Unity Connection Release 15 Service Update 2 Software

Step 1

Sign in to a
                                    			 computer with a high-speed Internet Unity Connection, and go to the Voice and
                                    			 Unified Communications Downloads page at http://www.cisco.com/cisco/software/navigator.html?mdfid=280082558 .

To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user.

Step 2

In the tree control on the Downloads page, expand Products > Unified Communications > Unified Communications Applications > Messaging > Unity Connection , and select Unity Connection Version 15SU2 .

Step 3

On the Select a Software Type page, select Cisco Unity Connection Updates .

Step 4

On the Select a Release page, select 15 SU2 , and the download buttons appear on the right side of the page.

Step 5

Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download descriptions include file sizes.)

Step 6

Select the
                                    			 applicable download, then follow the on-screen prompts to complete the
                                    			 download, making note of the MD5 value.

The VOS version for above mentioned ISO is 15.0.1.12900-234.

Step 7

Use a checksum
                                    			 generator to confirm that the MD5 checksum matches the checksum that is listed
                                    			 on Cisco.com. If the values do not match, the downloaded files are damaged.

Caution

Do not attempt to use a damaged file to install software, or the
                                                				results will be unpredictable. If the MD5 values do not match, download the
                                                				file again until the value for the downloaded file matches the value listed on
                                                				Cisco.com.

Free checksum
                                       				tools are available on the Internet, for example, the Microsoft File Checksum
                                       				Integrity Verifier utility. The utility is described in Microsoft Knowledge
                                       				Base article 841290, Availability
                                          				  and Description of the File Checksum Integrity Verifier Utility . The KB
                                       				article also includes a link for downloading the utility.

Step 8

If you are
                                    			 installing from a DVD, burn the DVD, noting the following considerations:

Choose the
                                          				  option to burn a disc image, not the option to copy files. Burning a disc image
                                          				  will extract the thousands of files from the .iso file and write them to a DVD,
                                          				  which is necessary for the files to be accessible for the installation.

- Use the Joliet file system,
                                       				which accommodates filenames up to 64 characters long.

- If the disc-burning
                                       				application that you are using includes an option to verify the contents of the
                                       				burned disc, choose that option. This causes the application to compare the
                                       				contents of the burned disc with the source files.

Step 9

Confirm that
                                    			 the DVD contains a large number of directories and files.

Step 10

Delete
                                    			 unnecessary files from the hard disk to free disk space, including the .iso
                                    			 file that you downloaded.

## Reverting to the
               	 Unity Connection Version on the Inactive Partition

See the “ Rollback of Unity Connection ” section of the “Upgrading Cisco Unity Connection” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15SU2 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

If a Unity
                  		Connection cluster is configured, revert to the previous version on the
                  		publisher server first, then on the subscriber server.

## Caveat
               	 Information

You can find the latest caveat information for Unity Connection version 15SU2 by using Bug Toolkit, an Online tool available
                  for customers to query defects according to their own needs.

Bug Toolkit is available at https://bst.cloudapps.cisco.com/bugsearch/ . Fill in your query parameters by using the custom settings in the Advanced Settings option.

To access Bug
                              		  Toolkit, you must be logged on to Cisco.com as a registered user.

This section
                  		contains the following caveat information:

- Open Caveats—Unity Connection Release 15SU2

- Resolved Caveats—Unity Connection Release 15SU2

Related Caveats—Cisco Unified Communications Manager 15SU2 Components that are Used by Unity Connection 15SU2

### Open Caveats—Unity Connection Release 15SU2

Click a link in the Caveat Number column to view the latest information on the caveat in Bug Toolkit. (Caveats are listed
                        in order by severity, then by component, then by caveat number.)

2

2

3

3

3

SMTP relay/um messaging is not working post 15SU2 Upgrade

### Resolved Caveats—Unity Connection Release 15SU2

Click a link in
                        		  the Caveat Number column to view the latest information on the caveat in Bug
                        		  Toolkit. (Caveats are listed in order by severity, then by component, then by
                        		  caveat number.)

### Related Caveats—Cisco Unified Communications Manager 15SU2 Components that are Used by Unity Connection 15SU2

Table
                           			 3 below describes the Cisco Unified Communications Manager components
                        		  that are used by Cisco Unity Connection.

Caveat information
                        		  for the Cisco Unified CM components is available in the following documents:

- ReadMe for Cisco Unified Communications Manager Release 15SU2 on the download page for 15SU2 (start at https://software.cisco.com/download/home/280082558 ).

## Obtaining
               	 Documentation and Submitting a Service Request

For information on obtaining documentation, submitting a service
                  		request, and gathering additional information, see the monthly What’s New in
                  		Cisco Product Documentation, which also lists all new and revised Cisco
                  		technical documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really
                  		Simple Syndication (RSS) feed and set content to be delivered directly to your
                  		desktop using a reader application. The RSS feeds are a free service and Cisco
                  		currently supports RSS Version 2.0.

## Cisco Product
               	 Security Overview

This product contains cryptographic features and is subject to United
                  		States and local country laws governing import, export, transfer and use.
                  		Delivery of Cisco cryptographic products does not imply third-party authority
                  		to import, export, distribute or use encryption. Importers, exporters,
                  		distributors and users are responsible for compliance with U.S. and local
                  		country laws. By using this product you agree to comply with applicable laws
                  		and regulations. If you are unable to comply with U.S. and local laws, return
                  		this product immediately.

Further information regarding U.S. export regulations may be found at

https://research.ucdavis.edu/wp-content/uploads/Export-Control-Overview-of-Regulations.pdf

| In Cisco Unity Connection
                                       			 Administration, in the upper-right corner below the Navigation list, select About . The Unity Connection version is displayed below “Cisco Unity
                                       			 Connection Administration.” |
|---|

| Step 1 | Start a command-line
                                       			 interface (CLI) session. (For more information, see Cisco Unified Operating
                                       			 System Administration Help.) |
|---|---|
| Step 2 | Run the show cuc version command. |

| Step 1 | Sign in to the Cisco PCA. |
|---|---|
| Step 2 | On the Cisco PCA Home page,
                                       			 select About in the upper right corner to display Cisco Unity
                                       			 Connection version. |
| Step 3 | The Cisco PCA version is the
                                       			 same as the Unity Connection version. |

| In Cisco Unified Operating
                                       			 System Administration, the System Version is displayed below “Cisco Unified
                                       			 Operating System Administration” in the blue banner on the page that appears
                                       			 after you sign in. |
|---|

| Step 1 | Start a command-line
                                       			 interface (CLI) session. (For more information, see Cisco Unified Operating
                                       			 System Administration Help.) |
|---|---|
| Step 2 | Run the show version active command. |

| Note | The new locales for Unity Connection 15SU2 have been released and available on Download Software site at https://software.cisco.com/download/home/282421576/type . |
|---|---|

| Note | Thirdparty transcription service will be EOL by Decemeber 30,2024. Hence customers are advised to upgrade to 15SU2 or later
                              releases. For more information see Field Notice: FN74144 - Cisco Unity Connection SpeechView Transcription Service Will Stop Working after December 30, 2024
                                 - Software Upgrade Recommended - Cisco |
|---|---|

| Note | TLS 1.3 is not supported for below Interfaces: Cisco Unity Tools Cisco Smart Software Licensing (CSSM) Voice Mail for Outlook (VMO) Chrome Extension for Gmail Microsoft Exchange Server Microsoft Office 365 Microsoft Outlook |
|---|---|

| Note | If you are performing an upgrade from a FIPS enabled Cisco Unity Connection release to Cisco Unity Connection 15SU2, make
                                    sure to follow the steps for regenerating certificates before using any pre-existing telephony integrations. To learn how
                                    to regenerate certificates, see the Regenerating Certificates for FIPS section of the "FIPS Compliance in Cisco Unity Connection" chapter of the Security Guide for Cisco Unity Connection Release 15SU2 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15cucsecx.html In FIPS mode, it is mandatory to upgrade all nodes in the Networking to Release 15 SU2 or later to ensure smooth operation
                                    and avoid replication issues. |
|---|---|

| Note | The service update files can be used to upgrade Cisco Unity Connection. The files can be downloaded from the Unity Connection
                                 downloads page. |
|---|---|

| Caution | With restricted and unrestricted versions of Cisco Unity Connection software now available, download software carefully. Upgrading
                                 a restricted version to an unrestricted version is supported, but future upgrades are then limited to unrestricted versions.
                                 Upgrading an unrestricted version to a restricted version is not supported. For more information on restricted and unrestricted
                                 versions of Unity Connection software, see the Downloading a VMware OVA Template for a Unity Connection 15 Virtual Machine
                                 of the Release Notes for Cisco Unity Connection Release 15SU2 at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html . |
|---|---|

| Step 1 | Sign in to a
                                    			 computer with a high-speed Internet Unity Connection, and go to the Voice and
                                    			 Unified Communications Downloads page at http://www.cisco.com/cisco/software/navigator.html?mdfid=280082558 . Note To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user. | Note | To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user. |
|---|---|---|---|
| Note | To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user. |
| Step 2 | In the tree control on the Downloads page, expand Products > Unified Communications > Unified Communications Applications > Messaging > Unity Connection , and select Unity Connection Version 15SU2 . |
| Step 3 | On the Select a Software Type page, select Cisco Unity Connection Updates . |
| Step 4 | On the Select a Release page, select 15 SU2 , and the download buttons appear on the right side of the page. |
| Step 5 | Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download descriptions include file sizes.) |
| Step 6 | Select the
                                    			 applicable download, then follow the on-screen prompts to complete the
                                    			 download, making note of the MD5 value. Restricted version UCSInstall_CUC_15.0.1.12900-43.sgn.iso Unrestricted version UCSInstall_CUC_UNRST_15.0.1.12900-43.sgn.iso Note The VOS version for above mentioned ISO is 15.0.1.12900-234. | Restricted version | UCSInstall_CUC_15.0.1.12900-43.sgn.iso | Unrestricted version | UCSInstall_CUC_UNRST_15.0.1.12900-43.sgn.iso | Note | The VOS version for above mentioned ISO is 15.0.1.12900-234. |
| Restricted version | UCSInstall_CUC_15.0.1.12900-43.sgn.iso |
| Unrestricted version | UCSInstall_CUC_UNRST_15.0.1.12900-43.sgn.iso |
| Note | The VOS version for above mentioned ISO is 15.0.1.12900-234. |
| Step 7 | Use a checksum
                                    			 generator to confirm that the MD5 checksum matches the checksum that is listed
                                    			 on Cisco.com. If the values do not match, the downloaded files are damaged. Caution Do not attempt to use a damaged file to install software, or the
                                                				results will be unpredictable. If the MD5 values do not match, download the
                                                				file again until the value for the downloaded file matches the value listed on
                                                				Cisco.com. Free checksum
                                       				tools are available on the Internet, for example, the Microsoft File Checksum
                                       				Integrity Verifier utility. The utility is described in Microsoft Knowledge
                                       				Base article 841290, Availability
                                          				  and Description of the File Checksum Integrity Verifier Utility . The KB
                                       				article also includes a link for downloading the utility. | Caution | Do not attempt to use a damaged file to install software, or the
                                                				results will be unpredictable. If the MD5 values do not match, download the
                                                				file again until the value for the downloaded file matches the value listed on
                                                				Cisco.com. |
| Caution | Do not attempt to use a damaged file to install software, or the
                                                				results will be unpredictable. If the MD5 values do not match, download the
                                                				file again until the value for the downloaded file matches the value listed on
                                                				Cisco.com. |
| Step 8 | If you are
                                    			 installing from a DVD, burn the DVD, noting the following considerations: Choose the
                                          				  option to burn a disc image, not the option to copy files. Burning a disc image
                                          				  will extract the thousands of files from the .iso file and write them to a DVD,
                                          				  which is necessary for the files to be accessible for the installation. Use the Joliet file system,
                                       				which accommodates filenames up to 64 characters long. If the disc-burning
                                       				application that you are using includes an option to verify the contents of the
                                       				burned disc, choose that option. This causes the application to compare the
                                       				contents of the burned disc with the source files. |
| Step 9 | Confirm that
                                    			 the DVD contains a large number of directories and files. |
| Step 10 | Delete
                                    			 unnecessary files from the hard disk to free disk space, including the .iso
                                    			 file that you downloaded. |

| Note | To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user. |
|---|---|

| Restricted version | UCSInstall_CUC_15.0.1.12900-43.sgn.iso |
|---|---|
| Unrestricted version | UCSInstall_CUC_UNRST_15.0.1.12900-43.sgn.iso |

| Note | The VOS version for above mentioned ISO is 15.0.1.12900-234. |
|---|---|

| Caution | Do not attempt to use a damaged file to install software, or the
                                                				results will be unpredictable. If the MD5 values do not match, download the
                                                				file again until the value for the downloaded file matches the value listed on
                                                				Cisco.com. |
|---|---|

| Note | To access Bug
                              		  Toolkit, you must be logged on to Cisco.com as a registered user. |
|---|---|

| Caveat Number | Component | Severity | Description |
|---|---|---|---|
| CSCwn42420 | messaging | 2 | Google Workspace Sync not working with direct connection after upgrading to 15su2 |
| CSCwq85838 | core | 2 | Node is booting up to the upgraded image even switch-version has failed. |
| CSCwq61805 | backup | 3 | Switch version fails intermittently on subscriber due to ontape restore still attempted on STDIO for CUC instance |
| CSCwq27598 | setup | 3 | DRS restore or Upgrade fails at DB component with SQLCODE -242 non-exclusive access ISAM 106 |
| CSCwk75669 | messaging | 3 | "Connection Google Workspace Sync Service" (CuGSuiteSy+) is using high CPU than expected. |
| CSCwo12114 | messaging | 3 | SMTP relay/um messaging is not working post 15SU2 Upgrade |

| Caveat Number | Component | Severity | Description |
|---|---|---|---|
| CSCwk63494 | core | 3 | Evaluation of Cisco Unity Connection for OpenSSH regreSSHion |
| CSCwm46543 | setup | 3 | Unable to send voicemail message marked secure through TUI / Web Inbox in https networking |
| CSCwk31084 | config | 3 | CUC Incorrect Swap Error reported with "ciscocm.cuc_preUpgradeCheck-005.cop.sha512" cop file |
| CSCwm11004 | core | 3 | Tomcat core dump generated when Metaspace is full |
| CSCwj85245 | telephony | 3 | UDP socket not getting created leading to SIP Trunks being down after upgrading to v15 |
| CSCwj72969 | setup | 3 | Upgrade 14SU3 to 15 SU1 Subscriber node switch version failing |
| CSCwk76764 | utilities | 3 | Security flaw in Cisco Unity Redirector tool allowing negotiation on weak TLS protocol. |
| CSCwk63447 | setup | 3 | CUC Dataexport fails on Blue Screen stuck indefinitely when exporting data from 11.5 to 15 |
| CSCwk41352 | database | 3 | CUC DB table service entries created on subscriber removed after switch-version from 12.5.x to 15.x |
| CSCwj56788 | database | 3 | Tomcat REST actions do not get updated to tbl_messageactivity in UnityRptDB |
| CSCwj69324 | inbox | 3 | Unity Inbox doesn't have webapp specific configurable timeout leading session limit error |
| CSCwb82664 | utilities | 3 | UC : Use ExternalEwsUrl for SOAP AutoDiscovery with Client Credential Flow |
| CSCwm62687 | core | 3 | Debug Symbols installation failed with conflict error |
| CSCwm38487 | speechview | 3 | Speechview Test button throws Incorrect Error about Webex in-house transcription service not healthy |
| CSCwh78412 | core | 3 | Legacy secure call not working in "Authenticated" mode |
| CSCwk20670 | admin | 3 | Vulnerabilities in haproxy - multiple versions CVE-2023-40225 |
| CSCwk74953 | serviceability | 3 | In ESM mode, RU and M2 Migration fails involving 12.5 SU8 and 12.5 SU9 as destination version |

| Cisco Unified CM Component | Description |
|---|---|
| backup-restore | Backup and restore
                                    				  utilities |
| ccm-serviceability | ccm-serviceability Cisco
                                    				  Unified Serviceability web interface |
| cdp | Cisco Discovery Protocol
                                    				  Drivers |
| cli | Command-line interface
                                    				  (CLI) |
| cmui | Certain elements in the
                                    				  Unity Connection web interfaces (such as search tables and splash screens) |
| cpi-afg | Cisco Unified
                                    				  Communications Answer File Generator |
| cpi-appinstall | Installation and upgrades |
| cpi-cert-mgmt | Certificate management |
| cpi-diagnose | Automated diagnostics
                                    				  system |
| cpi-os | Cisco Unified
                                    				  Communications Operating System |
| cpi-platform-api | Abstraction layer between
                                    				  the Cisco Unified Communications Operating System and the applications hosted
                                    				  on the platform |
| cpi-security | Security for connections to
                                    				  the server |
| cpi-service-mgr | Service Manager (ServM) |
| cpi-vendor | External vendor issues |
| cuc-tomcat | Apache Tomcat and
                                    				  third-party software |
| database | Installation and access to
                                    				  the configuration database (IDS) |
| database-ids | IDS database patches |
| ims | Identity Management System
                                    				  (IMS) |
| rtmt | Real-Time Monitoring Tool
                                    				  (RTMT) |