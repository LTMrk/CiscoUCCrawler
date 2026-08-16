---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-readme-b-15su3cucrn-html-94834fc074
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/readme/b_15su3cucrn.html
retrieved_at: 2026-08-16T18:49:02.055442+00:00
---

Release Notes for Cisco Unity Connection Release 15 Service Update 3

# Release Notes for Cisco Unity Connection Release 15 Service Update 3

### Download Options

Updated: October 4, 2025

First Published: October 4, 2025

# Release Notes for Cisco Unity Connection Release 15 Service Update 3

This release notes contains installation and support information for Cisco Unity Connection Release 15 Service Update 3.

## Contents

## Requirements

- System Requirements

- Compatibility Information

- Determining the Software Version

### System
                  	 Requirements

System Requirements for Cisco Unity Connection Release 15SU3 is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

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

Cisco Unity Connection 15SU3 is a cumulative update that incorporates all of the fixes and changes to Cisco Unity Connection
                  version 15 — including the operating system and components shared by Cisco Unity Connection and Cisco Unified CM. It also
                  incorporates additional changes that are specific to this service update.

To determine the
                  		full version number of the Cisco Unified Communications Operating System that
                  		is currently installed on the active partition, run the CLI show version
                     		  active command.

Full version numbers include the build number (for example, 15.0.1.13900-61), the software versions listed on the download
                  pages on Cisco.com are abbreviated version numbers (for example, 15SU3).

Do not refer to version numbers in any of the administration user interfaces because those versions apply to the interfaces
                  themselves, not to the version installed on the active partition.

## New and Changed
               	 Support or Functionality

This section contains all new and changed support or functionality for release 15SU3 and later.

- Smart Receiver Transport

- FIPS Compliance

The following changes also have been introduced in 15SU3:

Certificate Management Changes

IPSec DH Group Changes

Updates to Cipher Management Page

For more information, refer Release Notes for Cisco Unified Communications Manager and the IM and Presence Service Release 15SU3 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/15/SU3/cucm_b_release-notes-for-cucm-imp-15su3.html

The new locales for Unity Connection 15SU3 have been released and available on Download Software site at https://software.cisco.com/download/home/282421576/type .

### Smart Receiver Transport

Smart Transport has been introduced as an enhanced transport mechanism for Smart Licensing, in addition to the existing Call
                     Home transport mode. All new Cisco Unity Connection installations will only support Smart Transport for Smart Licensing functionality.

In case of an upgrade or migration, Cisco Unity Connection automatically switches to Smart Transport if the connection to
                     the endpoint "smartreceiver.cisco.com" is successful. If the connection fails, Cisco Unity Connection falls back to the Call
                     Home mode temporarily.

For more information, see the “ Managing Licenses “ chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

### FIPS Compliance

From Release 15SU3 onwards:

The Cisco Unity Connection available is FIPS 140-3 compliant.

CiscoSSL has been upgraded to Cisco SSL 7.3, which is FIPS 140-3 compliant.

## Related
               	 Documentation

### Documentation for
                  	 Cisco Unity Connection

For descriptions and URLs of Cisco Unity Connection documentation on Cisco.com, see the Documentation Guide for Cisco Unity Connection Release 15 . The document is shipped with Unity Connection and is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

### Documentation for
                  	 Cisco Unified Communications Manager Business Edition

For descriptions and URLs of Cisco Unified Communications Manager Business Edition documentation on Cisco.com, see the applicable
                     version of Cisco Business Edition at https://www.cisco.com/c/en/us/support/unified-communications/index.html .

## Installation
               	 Information

For instructions on downloading the service update, see the " Downloading Cisco Unity Connection Release 15SU3 Software " section.

For instructions on installing the service update on Cisco Unity Connection, see the “ Upgrading Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg/b_15cuciumg_chapter_010.html .

- If you are performing an upgrade from a FIPS enabled Cisco Unity Connection release to Cisco Unity Connection 15SU3, make
                                    sure to follow the steps for regenerating certificates before using any pre-existing telephony integrations. To learn how
                                    to regenerate certificates, see the Regenerating Certificates for FIPS section of the "FIPS Compliance in Cisco Unity Connection" chapter of the Security Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15cucsecx.html

- In FIPS mode, it is mandatory to upgrade all nodes in the Networking to Release 15 SU2 or later to ensure smooth operation
                                    and avoid replication issues.

### Downloading Cisco Unity Connection Release 15 Service Update 3 Software

The service update files can be used to upgrade Cisco Unity Connection. The files can be downloaded from the Unity Connection
                                 downloads page.

Caution

With restricted and unrestricted versions of Cisco Unity Connection software now available, download software carefully. Upgrading
                                 a restricted version to an unrestricted version is supported, but future upgrades are then limited to unrestricted versions.
                                 Upgrading an unrestricted version to a restricted version is not supported. For more information on restricted and unrestricted
                                 versions of Unity Connection software, see the Downloading a VMware OVA Template for a Unity Connection 15 Virtual Machine
                                 of the Release Notes for Cisco Unity Connection Release 15 at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html .

#### Downloading Cisco Unity Connection Release 15 Service Update 3 Software

Step 1

Sign in to a
                                    			 computer with a high-speed Internet Unity Connection, and go to the Voice and
                                    			 Unified Communications Downloads page at http://www.cisco.com/cisco/software/navigator.html?mdfid=280082558 .

To access
                                                				the software download page, you must be signed in to Cisco.com as a registered
                                                				user.

Step 2

In the tree control on the Downloads page, expand Products > Unified Communications > Unified Communications Applications > Messaging > Unity Connection , and select Unity Connection Version 15SU3 .

Step 3

On the Select a Software Type page, select Cisco Unity Connection Updates .

Step 4

On the Select a Release page, select 15 SU3 , and the download buttons appear on the right side of the page.

Step 5

Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download descriptions include file sizes.)

Step 6

Select the
                                    			 applicable download, then follow the on-screen prompts to complete the
                                    			 download, making note of the MD5 value.

The VOS version for above mentioned ISO is 15.0.1.13900-79.

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

See the “ Rollback of Unity Connection ” section of the “Upgrading Cisco Unity Connection” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

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

- Open Caveats—Unity Connection Release 15SU3

- Resolved Caveats—Unity Connection Release 15SU3

Related Caveats—Cisco Unified Communications Manager 15SU3 Components that are Used by Unity Connection 15SU3

### Open Caveats—Unity Connection Release 15SU3

Click a link in the Caveat Number column to view the latest information on the caveat in Bug Toolkit. (Caveats are listed
                        in order by severity, then by component, then by caveat number.)

2

3

3

3

3

### Resolved Caveats—Unity Connection Release 15SU3

Click a link in
                        		  the Caveat Number column to view the latest information on the caveat in Bug
                        		  Toolkit. (Caveats are listed in order by severity, then by component, then by
                        		  caveat number.)

### Related Caveats—Cisco Unified Communications Manager 15SU3 Components that are Used by Unity Connection 15SU3

Table
                           			 3 below describes the Cisco Unified Communications Manager components
                        		  that are used by Cisco Unity Connection.

Caveat information
                        		  for the Cisco Unified CM components is available in the following documents:

- ReadMe for Cisco Unified Communications Manager Release 15SU3 on the download page for 15SU3 (start at https://software.cisco.com/download/home/280082558 ).

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

| Note | The new locales for Unity Connection 15SU3 have been released and available on Download Software site at https://software.cisco.com/download/home/282421576/type . |
|---|---|

| Note | If you are performing an upgrade from a FIPS enabled Cisco Unity Connection release to Cisco Unity Connection 15SU3, make
                                    sure to follow the steps for regenerating certificates before using any pre-existing telephony integrations. To learn how
                                    to regenerate certificates, see the Regenerating Certificates for FIPS section of the "FIPS Compliance in Cisco Unity Connection" chapter of the Security Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15cucsecx.html In FIPS mode, it is mandatory to upgrade all nodes in the Networking to Release 15 SU2 or later to ensure smooth operation
                                    and avoid replication issues. |
|---|---|

| Note | The service update files can be used to upgrade Cisco Unity Connection. The files can be downloaded from the Unity Connection
                                 downloads page. |
|---|---|

| Caution | With restricted and unrestricted versions of Cisco Unity Connection software now available, download software carefully. Upgrading
                                 a restricted version to an unrestricted version is supported, but future upgrades are then limited to unrestricted versions.
                                 Upgrading an unrestricted version to a restricted version is not supported. For more information on restricted and unrestricted
                                 versions of Unity Connection software, see the Downloading a VMware OVA Template for a Unity Connection 15 Virtual Machine
                                 of the Release Notes for Cisco Unity Connection Release 15 at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html . |
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
| Step 2 | In the tree control on the Downloads page, expand Products > Unified Communications > Unified Communications Applications > Messaging > Unity Connection , and select Unity Connection Version 15SU3 . |
| Step 3 | On the Select a Software Type page, select Cisco Unity Connection Updates . |
| Step 4 | On the Select a Release page, select 15 SU3 , and the download buttons appear on the right side of the page. |
| Step 5 | Confirm that
                                    			 the computer you are using has sufficient hard-disk space for the downloaded
                                    			 files. (The download descriptions include file sizes.) |
| Step 6 | Select the
                                    			 applicable download, then follow the on-screen prompts to complete the
                                    			 download, making note of the MD5 value. Restricted version UCSInstall_CUC_15.0.1.13900-61.sgn.iso Unrestricted version UCSInstall_CUC_UNRST_15.0.1.13900-61.sgn.iso Note The VOS version for above mentioned ISO is 15.0.1.13900-79. | Restricted version | UCSInstall_CUC_15.0.1.13900-61.sgn.iso | Unrestricted version | UCSInstall_CUC_UNRST_15.0.1.13900-61.sgn.iso | Note | The VOS version for above mentioned ISO is 15.0.1.13900-79. |
| Restricted version | UCSInstall_CUC_15.0.1.13900-61.sgn.iso |
| Unrestricted version | UCSInstall_CUC_UNRST_15.0.1.13900-61.sgn.iso |
| Note | The VOS version for above mentioned ISO is 15.0.1.13900-79. |
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

| Restricted version | UCSInstall_CUC_15.0.1.13900-61.sgn.iso |
|---|---|
| Unrestricted version | UCSInstall_CUC_UNRST_15.0.1.13900-61.sgn.iso |

| Note | The VOS version for above mentioned ISO is 15.0.1.13900-79. |
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
| CSCwq85838 | core | 2 | Node is booting up to the upgraded image even switch-version has failed. |
| CSCwo60229 | messaging | 3 | Rest-Tomcat stuck while deploying the war files leading to 503/502 service unavailable/gateway timeout for VMrest |
| CSCwq27598 | setup | 3 | DRS restore or Upgrade fails at DB component with SQLCODE -242 non-exclusive access ISAM 106 |
| CSCwo60282 | conversations | 3 | UC15 CuMixer service experiencing delayed prompt playback during business hours call processing |
| CSCwq61805 | backup | 3 | Switch version fails intermittently on subscriber due to ontape restore still attempted on STDIO for CUC instance |

| Caveat Number | Component | Severity | Description |
|---|---|---|---|
| CSCwn63334 | trap | 2 | TRAP call is going to wrong Port in Unity 15 |
| CSCwn97864 | speechview | 2 | CUC SttService sends duplicate RequestId Under Heavy Voicemail Traffic |
| CSCwn42420 | messaging | 2 | Google Workspace Sync not working with direct connection after upgrading to 15su2 |
| CSCwo47190 | messaging | 3 | Push is not getting confirmed in database on unity intermittently after email is sent by MbxSync |
| CSCwn40925 | messaging | 3 | CuImapSvr core are getting created on the unity box |
| CSCwo22001 | setup | 3 | CUC Switch version fails if Informix does not come up online in one minute |
| CSCwo52765 | messaging | 3 | UC - Mbxsync repeatedly core dumps if empty/invalid token response received |
| CSCwo25742 | setup | 3 | CUC preupgrade COP leaves Orphan Java process leading to high CPU |
| CSCwp83385 | messaging | 3 | Connection Mailbox Sync cores with Exchange 2003 Unified Messaging service |
| CSCwo12114 | messaging | 3 | Smtp relay is not working post 15SU2 Upgrade with secure smtp config |
| CSCwo60587 | core | 3 | Connection Conversation Manager service is generating core dump durring qualys scan. |
| CSCwo25754 | core | 3 | RisSystemAccessMaxProcessesThreads is getting overwritten in upgrade . |
| CSCwo56062 | messaging | 3 | SpeechView Queue getting Stuck Processing If some Invalid entries in sttrequestQ |
| CSCwm77586 | core | 3 | Unity is generating cores while transcoding on v15 |
| CSCwo92025 | messaging | 3 | Change Password Option is not presented on CUADMIN app even though password has expired |
| CSCwp14881 | database | 3 | R15: CUC Subscriber Switch Version Fails while restoring ontape backup from Publisher |
| CSCwo71852 | core | 3 | UC15 CuCsMgr cores with SCCP Integration & 'Reconnect to a Higher-order CUCM When Available' Enabled |
| CSCwm77126 | core | 3 | Connection IMAP Service core dump generated during performance run and IMAP connectivity |
| CSCwo47197 | speechview | 3 | SttRequestQ grows enormously if there is a surge of failures from Cisco Webex Transcription Service |
| CSCwo77293 | licensing | 3 | CUC Smart License Reservation no longer works due to EOS/EOL notice for CUC-SL-EXRTKY-K9= |
| CSCwo02878 | speechview | 3 | AutoClean of the Dynamic DB SttQueue entries Left Out due to Corner Scenarios |
| CSCwn26351 | admin | 3 | AXL connection from cuc to cucm failing |
| CSCwn24391 | speechview | 3 | The voicemail transcription failed for messages sent to users in different mailbox stores. |
| CSCwn65588 | user-experience | 3 | DRS File Decryption Tool not working on Unity Connection 15 |
| CSCwn22220 | perfmon | 3 | CPU spike and higher RTT observed while fetching external services configured on unity |
| CSCwo11491 | licensing | 3 | Smart License Registration failing with SSM On-Prem |
| CSCwk75669 | messaging | 3 | "Connection Google Workspace Sync Service" (CuGSuiteSy+) is using high CPU than expected |
| CSCwn40867 | serviceability | 3 | User Synchronization is failing in Control Hub for Unity Connection for users with blank mailid |
| CSCwk55275 | messaging | 3 | UC "Delete Messages without Saving to Deleted Items Folder" feature does not work if User has 2 UMA |
| CSCwd33658 | licensing | 3 | SLM :Renew Auth Failure intermittently. RTMT alerts are displayed with time-out error. |
| CSCwo48977 | speechview | 3 | Onboarding status is not reflecting correctly on CUC cluster setup. |
| CSCwo42079 | speechview | 3 | Make Cleanup of stt queue Configurable in Unity Connection |
| CSCwo68587 | speechview | 3 | Existing Requests in SttRequestQ are not processed if heavy voicemail traffic is suddenly stopped |
| CSCwk89125 | admin | 3 | The "All Hours" and "Voice Recognition Update Schedule" pages are not opening. |
| CSCwn26139 | speechview | 3 | Attributes missing for speech view tables in Dir.xml. |
| CSCwn73992 | conversations | 3 | Evaluation of Unity for Vulnerabilities in tomcat - multiple versions CVE-2024-50379 |
| CSCwm88943 | speechview | 3 | Handle the processing of supported language codes when sending requests to Lexus. |
| CSCwm00058 | speechview | 3 | Clicking "Sync License Status" and then "Test" redirects to the GUI login screen. |

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