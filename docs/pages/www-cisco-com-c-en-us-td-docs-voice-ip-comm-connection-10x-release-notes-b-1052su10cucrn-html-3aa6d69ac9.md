---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-10x-release-notes-b-1052su10cucrn-html-3aa6d69ac9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/10x/release/notes/b_1052su10cucrn.html
retrieved_at: 2026-09-01T21:06:06.231968+00:00
---

Readme for Cisco Unity Connection Release 12.5(1) Service Update 7

# Readme for Cisco Unity Connection Release 12.5(1) Service Update 7

### Download Options

Updated: June 1, 2021

# Readme for Cisco Unity Connection Release 12.5(1) Service Update 7

This readme file contains installation and support information for Cisco Unity Connection Release 12.5(1) SU7.

## Contents

## Requirements

- System Requirements

- Compatibility Information

- Determining the Software Version

### System
                  	 Requirements

System Requirements for Cisco Unity Connection Release 12.x is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

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

Start a command-line
                                       			 interface (CLI) session. (For more information, see Cisco Unified Operating
                                       			 System Administration Help.)

Run the show cuc version command.

#### Determine Version
                     	 of Cisco Personal Communications Assistant Application

##### Using Cisco
                        	 Personal Communications Assistant Application

Sign in to the Cisco PCA.

On the Cisco PCA Home page,
                                       			 select About in the upper right corner to display Cisco Unity
                                       			 Connection version.

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

Start a command-line
                                       			 interface (CLI) session. (For more information, see Cisco Unified Operating
                                       			 System Administration Help.)

Run the show version active command.

## Version and
               	 Description

Cisco Unity Connection 12.5(1) SU7 is a cumulative update that incorporates all of the fixes and changes to Cisco Unity Connection
                  version 12.5(1)—including the operating system and components shared by Cisco Unity Connection and Cisco Unified CM. It also
                  incorporates additional changes that are specific to this service update.

To determine the
                  		full version number of the Cisco Unified Communications Operating System that
                  		is currently installed on the active partition, run the CLI show version
                     		  active command.

Full version numbers include the build number (for example, 12.5.1.17900-31), the software versions listed on the download
                  pages on Cisco.com are abbreviated version numbers (for example, 12.5(1) ).

Do not refer to
                  		version numbers in any of the administration user interfaces because those
                  		versions apply to the interfaces themselves, not to the version installed on
                  		the active partition.

## New and Changed
               	 Support or Functionality

This section contains all new and changed support or functionality for release 12.5(1) SU7 and later.

The new locales for Unity Connection 12.5(1) SU7 have been released and available on Download Software site at https://software.cisco.com/download/home/282421576/type .

## Related
               	 Documentation

### Documentation for
                  	 Cisco Unity Connection

For descriptions and URLs of Cisco Unity Connection documentation on Cisco.com, see the Documentation Guide for Cisco Unity Connection Release 12.x . The document is shipped with Unity Connection and is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/roadmap/b_12xcucdg.html .

### Documentation for
                  	 Cisco Unified Communications Manager Business Edition

For descriptions and URLs of Cisco Unified Communications Manager Business Edition documentation on Cisco.com, see the applicable
                     version of Cisco Business Edition at https://www.cisco.com/c/en/us/support/unified-communications/index.html .

## Installation
               	 Information

For instructions on downloading the service update, see the " Downloading Cisco Unity Connection Release 12.5(1) SU7 Software " section.

For instructions on installing the service update on Cisco Unity Connection, see the “ Upgrading Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

If you are performing an upgrade from a FIPS enabled Cisco Unity Connection release to Cisco Unity Connection 12.5(1) SU7,
                              make sure to follow the steps for regenerating certificates before using any pre-existing telephony integrations. To learn
                              how to regenerate certificates, see the Regenerating Certificates for FIPS section of the "FIPS Compliance in Cisco Unity Connection" chapter of the Security Guide for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/guide/b_12xcucsecx.html .

### Downloading Cisco Unity Connection Release 12.5(1) SU7 Software

The service update files can be used to upgrade Cisco Unity Connection. The files can be downloaded from the Unity Connection
                                 downloads page.

With restricted and unrestricted versions of Cisco Unity Connection software now available, download software carefully. Upgrading
                                 a restricted version to an unrestricted version is supported, but future upgrades are then limited to unrestricted versions.
                                 Upgrading an unrestricted version to a restricted version is not supported. For more information on restricted and unrestricted
                                 versions of Unity Connection software, see the Downloading a VMware OVA Template for a Unity Connection 12.5(1) Virtual Machine
                                 of the Release Notes for Cisco Unity Connection Release 12.5(1) at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html .

#### Downloading Cisco Unity Connection Release 12.5(1) SU7 Software

Sign in to a
                                    			 computer with a high-speed Internet Unity Connection, and go to the Voice and
                                    			 Unified Communications Downloads page at http://www.cisco.com/cisco/software/navigator.html?mdfid=280082558 .

To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user.

In the tree control on the Downloads page, expand Products > Unified Communications > Unified Communications Applications > Messaging > Unity Connection , and select Unity Connection Version 12.x .

On the Select a Software Type page, select Unified Communications Manager /Cisco Unity Connection Updates .

On the Select a Release page, select 12.5(1) SU7 , and the download buttons appear on the right side of the page.

Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download descriptions include file sizes.)

Select the
                                    			 applicable download, then follow the on-screen prompts to complete the
                                    			 download, making note of the MD5 value.

The VOS version for above mentioned ISO is 12.5.1.17900-64.

Use a checksum
                                    			 generator to confirm that the MD5 checksum matches the checksum that is listed
                                    			 on Cisco.com. If the values do not match, the downloaded files are damaged.

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

Confirm that
                                    			 the DVD contains a large number of directories and files.

Delete
                                    			 unnecessary files from the hard disk to free disk space, including the .iso
                                    			 file that you downloaded.

## Reverting to the
               	 Unity Connection Version on the Inactive Partition

See the “ Rollback of Unity Connection ” section of the “Upgrading Cisco Unity Connection” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

If a Unity
                  		Connection cluster is configured, revert to the previous version on the
                  		publisher server first, then on the subscriber server.

## Caveat
               	 Information

You can find the latest caveat information for Unity Connection version 12.5 by using Bug Toolkit, an Online tool available
                  for customers to query defects according to their own needs.

Bug Toolkit is available at https://bst.cloudapps.cisco.com/bugsearch/ . Fill in your query parameters by using the custom settings in the Advanced Settings option.

To access Bug
                              		  Toolkit, you must be logged on to Cisco.com as a registered user.

This section
                  		contains the following caveat information:

- Open Caveats—Unity Connection Release 12.5(1) SU7

- Resolved Caveats—Unity Connection Release 12.5(1) SU7

- Related Caveats—Cisco Unified Communications Manager 12.5(1) Components that are Used by Unity Connection 12.5(1)

### Open Caveats—Unity Connection Release 12.5(1) SU7

There are no open caveats for this release.

### Resolved Caveats—Unity Connection Release 12.5(1) SU7

Click a link in
                        		  the Caveat Number column to view the latest information on the caveat in Bug
                        		  Toolkit. (Caveats are listed in order by severity, then by component, then by
                        		  caveat number.)

CSCwc37421

conversations

2

Unity 12.X streams 54 Bytes RTP packets while caller records the Voicemail, leading to call drop.

CSCwc08253

https-networking

3

UC - User-Defined Alternate Extensions Don't Get Recognized on Remote Locations.

### Related Caveats—Cisco Unified Communications Manager 12.5(1) Components that are Used by Unity Connection 12.5(1)

Table
                           			 3 below describes the Cisco Unified Communications Manager components
                        		  that are used by Cisco Unity Connection.

Caveat information
                        		  for the Cisco Unified CM components is available in the following documents:

- ReadMe for Cisco Unified Communications Manager Release 12.5(1) SU7 on the download page for 12.5(1) SU7 (start at https://software.cisco.com/download/home/280082558 ).

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

- Unity Connection Version 12.x

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

| Note | The new locales for Unity Connection 12.5(1) SU7 have been released and available on Download Software site at https://software.cisco.com/download/home/282421576/type . |
|---|---|

| Note | If you are performing an upgrade from a FIPS enabled Cisco Unity Connection release to Cisco Unity Connection 12.5(1) SU7,
                              make sure to follow the steps for regenerating certificates before using any pre-existing telephony integrations. To learn
                              how to regenerate certificates, see the Regenerating Certificates for FIPS section of the "FIPS Compliance in Cisco Unity Connection" chapter of the Security Guide for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/guide/b_12xcucsecx.html . |
|---|---|

| Note | The service update files can be used to upgrade Cisco Unity Connection. The files can be downloaded from the Unity Connection
                                 downloads page. |
|---|---|

| Caution | With restricted and unrestricted versions of Cisco Unity Connection software now available, download software carefully. Upgrading
                                 a restricted version to an unrestricted version is supported, but future upgrades are then limited to unrestricted versions.
                                 Upgrading an unrestricted version to a restricted version is not supported. For more information on restricted and unrestricted
                                 versions of Unity Connection software, see the Downloading a VMware OVA Template for a Unity Connection 12.5(1) Virtual Machine
                                 of the Release Notes for Cisco Unity Connection Release 12.5(1) at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html . |
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
| Step 2 | In the tree control on the Downloads page, expand Products > Unified Communications > Unified Communications Applications > Messaging > Unity Connection , and select Unity Connection Version 12.x . |
| Step 3 | On the Select a Software Type page, select Unified Communications Manager /Cisco Unity Connection Updates . |
| Step 4 | On the Select a Release page, select 12.5(1) SU7 , and the download buttons appear on the right side of the page. |
| Step 5 | Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download descriptions include file sizes.) |
| Step 6 | Select the
                                    			 applicable download, then follow the on-screen prompts to complete the
                                    			 download, making note of the MD5 value. Restricted version UCSInstall_CUC_12.5.1.17900-31.sgn.iso Unrestricted version UCSInstall_CUC_UNRST_12.5.1.17900-31.sgn.iso Note The VOS version for above mentioned ISO is 12.5.1.17900-64. | Restricted version | UCSInstall_CUC_12.5.1.17900-31.sgn.iso | Unrestricted version | UCSInstall_CUC_UNRST_12.5.1.17900-31.sgn.iso | Note | The VOS version for above mentioned ISO is 12.5.1.17900-64. |
| Restricted version | UCSInstall_CUC_12.5.1.17900-31.sgn.iso |
| Unrestricted version | UCSInstall_CUC_UNRST_12.5.1.17900-31.sgn.iso |
| Note | The VOS version for above mentioned ISO is 12.5.1.17900-64. |
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

| Restricted version | UCSInstall_CUC_12.5.1.17900-31.sgn.iso |
|---|---|
| Unrestricted version | UCSInstall_CUC_UNRST_12.5.1.17900-31.sgn.iso |

| Note | The VOS version for above mentioned ISO is 12.5.1.17900-64. |
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
| CSCwc37421 | conversations | 2 | Unity 12.X streams 54 Bytes RTP packets while caller records the Voicemail, leading to call drop. |
| CSCwc08253 | https-networking | 3 | UC - User-Defined Alternate Extensions Don't Get Recognized on Remote Locations. |

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