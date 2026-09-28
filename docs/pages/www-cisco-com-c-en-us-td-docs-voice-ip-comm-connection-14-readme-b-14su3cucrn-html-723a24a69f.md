---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-readme-b-14su3cucrn-html-723a24a69f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/readme/b_14su3cucrn.html
retrieved_at: 2026-08-16T18:49:27.683746+00:00
---

Readme for Cisco Unity Connection Release 14 Service Update 3

# Readme for Cisco Unity Connection Release 14 Service Update 3

### Download Options

Updated: May 7, 2023

First Published: May 18, 2023

# Readme for Cisco Unity Connection Release 14 Service Update 3

This readme file contains installation and support information for Cisco Unity Connection Release 14 SU3.

## Contents

## Requirements

- System Requirements

- Compatibility Information

- Determining the Software Version

### System
                  	 Requirements

System Requirements for Cisco Unity Connection Release 14 is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/requirements/b_14cucsysreqs.html

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

Cisco Unity Connection 14 SU3 is a cumulative update that incorporates all of the fixes and changes to Cisco Unity Connection
                  version 14 —including the operating system and components shared by Cisco Unity Connection and Cisco Unified CM. It also incorporates
                  additional changes that are specific to this service update.

To determine the
                  		full version number of the Cisco Unified Communications Operating System that
                  		is currently installed on the active partition, run the CLI show version
                     		  active command.

Full version numbers include the build number (for example, 14.0.1.13900-70), the software versions listed on the download
                  pages on Cisco.com are abbreviated version numbers (for example, 14 ).

Do not refer to version numbers in any of the administration user interfaces because those versions apply to the interfaces
                  themselves, not to the version installed on the active partition.

## New and Changed
               	 Support or Functionality

This section contains all new and changed support or functionality for release 14SU3 and later.

The new locales for Unity Connection 14SU3 have been released and available on Download Software site at https://software.cisco.com/download/home/282421576/type .

### OAuth 2.0: ROPC to Client Credential Grant Flow

Cisco Unity Connection supports the OAuth 2.0 Resource Owner Password Credentials (ROPC) grant, which allows an application to sign in the user by directly handling their password for configuring Unified Messaging
                     Service with Microsoft Office 365. With Release 14SU3 and later, Unity Connection supports the OAuth 2.0 Client Credentials (CC) grant flow. It provides more security and permits a web service to use its own credentials, for authentication when calling
                     another web service.

If you are performing upgrade to Unity Connection 14SU3 from any of the older release, make sure to reconfigure permissions
                                 on Azure Portal after successful upgrade. For information on how to reconfigure permissions, see Step 4g of the section "Task List for Configuring Unified Messaging with Office 365" of the chapter "Configuring Unified Messaging"
                                 of the Unified Messaging Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html

### Directory Size Scaling of HTTPS Networking

Cisco Unity Connection 14SU3 and later, supports HTTPS networking with a directory size limit of 160k users.

For more information, see section HTTPS Networking of the chapter "Networking" of the Design Guide for Cisco Unity Connection 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/design/guide/b_14cucdg.html .

In addition to the features listed in the ReadMe, the following change is also introduced in 14SU3:

Log4j upgrade to 2.19.0

## Important Notes

Warning for Upgrades from 10.5(2)

Direct upgrades from any 10.5.2 release to 14SU2 release are not supported. Fresh Install with Data Import is the only supported
                  upgrade options from 10.5.2. Starting with Unity Connection 14SU2 release, upgrades from release 10.5.2 are blocked so a direct
                  upgrade attempt will fail as an usupported upgrade.

Warning for Upgrades with FIPS Enabled

If you are upgrading with FIPS enabled, see the CiscoSSL7 COP File Readme for information on the COP file ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop.sha512 . This document details the pre-requisites required for direct upgrade or direct migration to the 14SU2 destination versions
                  when FIPS is enabled.

## Related
               	 Documentation

### Documentation for
                  	 Cisco Unity Connection

For descriptions and URLs of Cisco Unity Connection documentation on Cisco.com, see the Documentation Guide for Cisco Unity Connection Release 14 . The document is shipped with Unity Connection and is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/roadmap/b_14cucdg.html .

### Documentation for
                  	 Cisco Unified Communications Manager Business Edition

For descriptions and URLs of Cisco Unified Communications Manager Business Edition documentation on Cisco.com, see the applicable
                     version of Cisco Business Edition at https://www.cisco.com/c/en/us/support/unified-communications/index.html .

## Installation
               	 Information

For instructions on downloading the service update, see the " Downloading Cisco Unity Connection Release 14 SU3 Software " section.

For instructions on installing the service update on Cisco Unity Connection, see the “ Upgrading Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/install_upgrade/guide/b_14cuciumg/b_14cuciumg_chapter_010.html .

If you are performing an upgrade from a FIPS enabled Cisco Unity Connection release to Cisco Unity Connection 14 SU3, make
                              sure to follow the steps for regenerating certificates before using any pre-existing telephony integrations. To learn how
                              to regenerate certificates, see the Regenerating Certificates for FIPS section of the "FIPS Compliance in Cisco Unity Connection" chapter of the Security Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/security/guide/b_14cucsecx.html

### Downloading Cisco Unity Connection Release 14 SU3 Software

The service update files can be used to upgrade Cisco Unity Connection. The files can be downloaded from the Unity Connection
                                 downloads page.

Caution

With restricted and unrestricted versions of Cisco Unity Connection software now available, download software carefully. Upgrading
                                 a restricted version to an unrestricted version is supported, but future upgrades are then limited to unrestricted versions.
                                 Upgrading an unrestricted version to a restricted version is not supported. For more information on restricted and unrestricted
                                 versions of Unity Connection software, see the Downloading a VMware OVA Template for a Unity Connection 14 Virtual Machine
                                 of the Release Notes for Cisco Unity Connection Release 14 at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html .

#### Downloading Cisco Unity Connection Release 14 SU3 Software

Step 1

Sign in to a
                                    			 computer with a high-speed Internet Unity Connection, and go to the Voice and
                                    			 Unified Communications Downloads page at http://www.cisco.com/cisco/software/navigator.html?mdfid=280082558 .

To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user.

Step 2

In the tree control on the Downloads page, expand Products > Unified Communications > Unified Communications Applications > Messaging > Unity Connection , and select Unity Connection Version 14 .

Step 3

On the Select a Software Type page, select Unified Communications Manager /Cisco Unity Connection Updates .

Step 4

On the Select a Release page, select 14 SU3 , and the download buttons appear on the right side of the page.

Step 5

Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download descriptions include file sizes.)

Step 6

Select the
                                    			 applicable download, then follow the on-screen prompts to complete the
                                    			 download, making note of the MD5 value.

The VOS version for above mentioned ISO is 14.0.1.13900-155.

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

See the “ Rollback of Unity Connection ” section of the “Upgrading Cisco Unity Connection” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/install_upgrade/guide/b_14cuciumg/b_14cuciumg_chapter_010.html .

If a Unity
                  		Connection cluster is configured, revert to the previous version on the
                  		publisher server first, then on the subscriber server.

## Caveat
               	 Information

You can find the latest caveat information for Unity Connection version 14 by using Bug Toolkit, an Online tool available
                  for customers to query defects according to their own needs.

Bug Toolkit is available at https://bst.cloudapps.cisco.com/bugsearch/ . Fill in your query parameters by using the custom settings in the Advanced Settings option.

To access Bug
                              		  Toolkit, you must be logged on to Cisco.com as a registered user.

This section
                  		contains the following caveat information:

- Open Caveats—Unity Connection Release 14 SU3

- Resolved Caveats—Unity Connection Release 14 SU3

- Related Caveats—Cisco Unified Communications Manager 14SU3 Components that are Used by Unity Connection 14SU3

### Open Caveats—Unity Connection Release 14 SU3

Click a link in the Caveat Number column to view the latest information on the caveat in Bug Toolkit. (Caveats are listed
                        in order by severity, then by component, then by caveat number.)

CSCwf30759

serviceability

3

Performance Counter Logging through Rtmt Not working for Publisher Node

### Resolved Caveats—Unity Connection Release 14 SU3

Click a link in
                        		  the Caveat Number column to view the latest information on the caveat in Bug
                        		  Toolkit. (Caveats are listed in order by severity, then by component, then by
                        		  caveat number.)

CSCvy29659

admin

3

Unity Connection Apache Axis2 Directory Traversal Vulnerability

CSCwa33209

api

3

Upgrade Jetty Running on Port 7080

CSCwe66473

messaging

3

UC - Connection leak leading to pool exhausted causing SysAgent tasks to fail

CSCwe72423

build

3

The TLS cipher upgrade (TLS 1.2) on the ncs-artifactory require JAVA 8 to download the artifacts

CSCwc08253

https-networking

3

UC - User-Defined Alternate Extensions Don't Get Recognized on Remote Locations

CSCwd19222

messaging

3

Syncing of the VoiceMessages & UMA test button fails with Google Workspace Service

CSCwc77632

pca

3

Unity Connection PCA - User Defined Alternate Devices visual errors

### Related Caveats—Cisco Unified Communications Manager 14 SU3 Components that are Used by Unity Connection 14 SU3

Table
                           			 3 below describes the Cisco Unified Communications Manager components
                        		  that are used by Cisco Unity Connection.

Caveat information
                        		  for the Cisco Unified CM components is available in the following documents:

- ReadMe for Cisco Unified Communications Manager Release 14 SU3 on the download page for 14 SU3(start at https://software.cisco.com/download/home/280082558 ).

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

### This Document Applies to These Products

- Unity Connection Version 14

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

| Note | The new locales for Unity Connection 14SU3 have been released and available on Download Software site at https://software.cisco.com/download/home/282421576/type . |
|---|---|

| Note | If you are performing upgrade to Unity Connection 14SU3 from any of the older release, make sure to reconfigure permissions
                                 on Azure Portal after successful upgrade. For information on how to reconfigure permissions, see Step 4g of the section "Task List for Configuring Unified Messaging with Office 365" of the chapter "Configuring Unified Messaging"
                                 of the Unified Messaging Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx.html |
|---|---|

| Note | In addition to the features listed in the ReadMe, the following change is also introduced in 14SU3: Log4j upgrade to 2.19.0 |
|---|---|

| Note | If you are performing an upgrade from a FIPS enabled Cisco Unity Connection release to Cisco Unity Connection 14 SU3, make
                              sure to follow the steps for regenerating certificates before using any pre-existing telephony integrations. To learn how
                              to regenerate certificates, see the Regenerating Certificates for FIPS section of the "FIPS Compliance in Cisco Unity Connection" chapter of the Security Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/security/guide/b_14cucsecx.html |
|---|---|

| Note | The service update files can be used to upgrade Cisco Unity Connection. The files can be downloaded from the Unity Connection
                                 downloads page. |
|---|---|

| Caution | With restricted and unrestricted versions of Cisco Unity Connection software now available, download software carefully. Upgrading
                                 a restricted version to an unrestricted version is supported, but future upgrades are then limited to unrestricted versions.
                                 Upgrading an unrestricted version to a restricted version is not supported. For more information on restricted and unrestricted
                                 versions of Unity Connection software, see the Downloading a VMware OVA Template for a Unity Connection 14 Virtual Machine
                                 of the Release Notes for Cisco Unity Connection Release 14 at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html . |
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
| Step 2 | In the tree control on the Downloads page, expand Products > Unified Communications > Unified Communications Applications > Messaging > Unity Connection , and select Unity Connection Version 14 . |
| Step 3 | On the Select a Software Type page, select Unified Communications Manager /Cisco Unity Connection Updates . |
| Step 4 | On the Select a Release page, select 14 SU3 , and the download buttons appear on the right side of the page. |
| Step 5 | Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download descriptions include file sizes.) |
| Step 6 | Select the
                                    			 applicable download, then follow the on-screen prompts to complete the
                                    			 download, making note of the MD5 value. Restricted version UCSInstall_CUC_14.0.1.13900-70.sgn.iso Unrestricted version UCSInstall_CUC_UNRST_14.0.1.13900-70.sgn.iso Note The VOS version for above mentioned ISO is 14.0.1.13900-155. | Restricted version | UCSInstall_CUC_14.0.1.13900-70.sgn.iso | Unrestricted version | UCSInstall_CUC_UNRST_14.0.1.13900-70.sgn.iso | Note | The VOS version for above mentioned ISO is 14.0.1.13900-155. |
| Restricted version | UCSInstall_CUC_14.0.1.13900-70.sgn.iso |
| Unrestricted version | UCSInstall_CUC_UNRST_14.0.1.13900-70.sgn.iso |
| Note | The VOS version for above mentioned ISO is 14.0.1.13900-155. |
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

| Restricted version | UCSInstall_CUC_14.0.1.13900-70.sgn.iso |
|---|---|
| Unrestricted version | UCSInstall_CUC_UNRST_14.0.1.13900-70.sgn.iso |

| Note | The VOS version for above mentioned ISO is 14.0.1.13900-155. |
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
| CSCwf30759 | serviceability | 3 | Performance Counter Logging through Rtmt Not working for Publisher Node |

| Caveat Number | Component | Severity | Description |
|---|---|---|---|
| CSCvy29659 | admin | 3 | Unity Connection Apache Axis2 Directory Traversal Vulnerability |
| CSCwa33209 | api | 3 | Upgrade Jetty Running on Port 7080 |
| CSCwe66473 | messaging | 3 | UC - Connection leak leading to pool exhausted causing SysAgent tasks to fail |
| CSCwe72423 | build | 3 | The TLS cipher upgrade (TLS 1.2) on the ncs-artifactory require JAVA 8 to download the artifacts |
| CSCwc08253 | https-networking | 3 | UC - User-Defined Alternate Extensions Don't Get Recognized on Remote Locations |
| CSCwd19222 | messaging | 3 | Syncing of the VoiceMessages & UMA test button fails with Google Workspace Service |
| CSCwc77632 | pca | 3 | Unity Connection PCA - User Defined Alternate Devices visual errors |

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