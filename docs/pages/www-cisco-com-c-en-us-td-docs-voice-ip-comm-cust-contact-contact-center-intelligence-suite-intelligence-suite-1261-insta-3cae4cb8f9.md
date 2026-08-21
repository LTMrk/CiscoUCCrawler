---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1261-insta-3cae4cb8f9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1261/install/guide/cuic_b_install-and-upgrade-guide-1261/cuic_m_upgrades-1261.html
retrieved_at: 2026-08-21T16:15:23.881589+00:00
---

Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(1)

# Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(1)

Updated: May 14, 2021

Chapter: Upgrades

## Chapter: Upgrades

# Upgrades

## Before You Upgrade

For important notes, caveats, and other considerations, see the Cisco Unified Intelligence Center chapter in the Release Notes for Cisco Unified Contact Center Enterprise Solution available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html .

If you’re upgrading the Cisco Unified Intelligence Center (coresident) deployment, Live Data is also upgraded. As Live Data
                                                must be of the same version as Central Controller Components, Central Controller Components must be upgraded in the same window.

Unsupported Widgets

The Cisco Unified Intelligence Center 12.6 interface for Dashboards doesn’t support the following widgets:

Schedule Report widgets

URL widgets containing Dashboard permalinks (Nested Dashboards)

Migration Limitations

To address injection vulnerabilities, the Custom Widget feature in Dashboards is disabled by default. If any custom widgets were added to the Dashboards in versions earlier to Cisco Unified Intelligence Center 12.6 , those widgets are visible in the read-only mode post upgrade to the 12.6 version. You can opt to retain or delete them.

To enable the Custom Widget feature, use the CLI and set cuic properties dashboard-customwidget-enabled set the parameter value to "on".

For more information, see the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

To perform an upgrade of Cisco Unified Intelligence Center to 12.6(1), you must first perform an upgrade to 12.0(1) from the previous versions (11.0(x)) and then upgrade to 12.6(1).

Cisco Unified Intelligence Center 12.5(1) users can directly upgrade to 12.6(1).

Upgrade Prerequisites

Before starting the software upgrade,

Perform the Unified CCE User Integration to import supervisors and their teams from Unified CCE into the Cisco Unified Intelligence
                                    Center.

Back up your system data using the Disaster Recovery system application. To access the DRS application, direct your browser to https:// IP address of Intelligence Center :8443/drf. For more information, see the online help provided with the DRS application.

Ensure that the certificates aren’t expired. If the certificates are expired, regenerate the certificates.

Upgrade and restart the Controller node first. Then upgrade and restart the members. All nodes must be on the same version
                              of the Cisco Unified Intelligence Center.

After upgrading Cisco Unified Intelligence Center to release 12.6 , ensure to perform the following:

Disable the Unified CCE User Integration. (Uncheck the Enable UCCE User Integration check box in OAMP > Cluster Configuration > UCCE User Integration.)

Install the latest Cisco Options Package (COP) file for the Cisco Unified Intelligence Center 12.6 release.

Enable the Unified CCE User Integration manually to import the Supervisors with the required roles. This setting is required
                                          to view gadgets in the Cisco Finesse Desktop for Supervisors. For more information on User Integration, see the Unified CCE User Integration Configuration section in the Administration Console User Guide for Cisco Unified Intelligence Center at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

Configure CORS and reset the cluster configuration. For more information on enabling the CORS CLI and to reset the cluster
                                          configuration, see Post-Install Configuration .

When you upgrade Cisco Unified Intelligence Center from release 12.5(1) to release 12.6(1), permissions of all the STOCK value
                                          lists for the ALLUSERS group is set to NONE. Therefore, you must reset the permissions manually in 12.6(1) if you want users
                                          to use the entire value list.

Your configuration information moves automatically to the upgraded version in the active partition.

After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. You can add
                                          them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki .

For information about adding a certificate, see Insert a new tomcat-trust certificate at

https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/210541-CUCM-Certificate-Management-and-Change-N.html .

If you upgrade Cisco Unified Intelligence Center to version 12.6(1) and your Live Data (standalone) server remains on an earlier
                                          version (11.6(1), 12.0(1), or 12.5(1)), ensure that you update the Live Data server with the latest ES for that release. This
                                          is required for the Live Data gadgets to work in the Finesse desktop.

## Download Unified
                        	 Intelligence Center Upgrade File

Step 1

Point your browser to the Download Software page for Cisco Unified Intelligence Center : https://software.cisco.com/download/type.html?mdfid=282163829&i=rm , and click the Unified Intelligence Center Software link.

Step 2

Navigate to the
                                       			 folder and subfolder for the release you want.

Step 3

Select the
                                       			 Unified Intelligence Center installer .iso file and click Download .

Step 4

Click Log
                                          				in .

## Refresh Upgrade

You can perform an upgrade from 12.0(1) to 12.6(1) on the publisher and subscriber nodes of Unified Intelligence Center . Before you begin upgrade, perform a backup. For more information, see Before You Upgrade .

### Upgrade VMware vSphere ESXi for Upgrade

If you use VMware vCenter Server in your deployment, upgrade VMware vCenter Server before upgrading VMware vSphere ESXi.

Upgrade VMWare vSphere ESXi on Side A and Side B servers to the latest version supported with this release of Packaged CCE.
                              Packaged CCE uses standard upgrade procedures, which you can find using VMware documentation ( https://www.vmware.com/support/pubs/ ).

### Upgrade Unified
                           	 Intelligence Center

Follow the steps to install the ISO file using the Unified Intelligence Center CLI.

You can also install the ISO using the upgrade procedure in the Cisco Unified Operating System Administration web interface.
                                 For more information, see Access Unified OS Administration .

#### Before you begin

Before you begin the upgrade from 12.0(1) or 12.5(1) to 12.6(1), you must install the COP ucos.keymanagement.cop.sgn on the base version.

Download the ISO file from https://software.cisco.com/download/home/282163829/type/282377062/release to the SFTP server that can be accessed from the Cisco Unified Intelligence Center system.

Step 1

Log in to Unified Intelligence Center CLI and specify the System Administration username and password.

Step 2

Enter the command utils system upgrade initiate to initiate the ISO installation.

Step 3

Select Remote File System from the source list page.

Step 4

Enter the remote path to the directory on the SFTP server where
                                          			 you have downloaded the ISO file.

If the ISO file is located on a Linux or UNIX server, you must
                                                         				  enter a forward slash (/) at the beginning of the directory path. For example,
                                                         				  if the COP file is in the patches directory, enter / patches . If the
                                                         				  ISO file is located on a Windows server, check with your system administrator
                                                         				  for the correct directory path.

Step 5

Enter the SFTP server name or IP address and then enter the credentials.

Step 6

Select the transfer protocol as SFTP. The system displays the list
                                          			 of ISO files available in the SFTP location.

Step 7

Select the number corresponding to the ISO file that you want to install, and press Enter .

Step 8

Enter the relevant option when you’re prompted Switch to new version if the upgrade is successful (yes/no) .

Enter yes to automatically switch the version .

Enter no if you  need to manually switch the version after all the nodes are upgraded (refer step 10 for more details).

After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                         Center 12.0(1) to 12.6(1).

If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1) and the active version is 12.6(1).

Step 9

Enter yes when you’re prompted Start Refresh Upgrade (yes/no) .

Step 10

In cluster setup, first complete the upgrade on the publisher node and perform the upgrade on the subscriber node. After successful
                                          upgrades, switch the version using the command utils system switch-version first on the publisher node and later on the subscriber nodes.

After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                         can upgrade from Cisco Unified Intelligence Center 12.0(1) to 12.6 (1).

If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1), and the active version is 12.6(1).

#### L2 Upgrade for Unified Intelligence Center

Follow the steps to install the ISO file using the Unified Intelligence Center CLI.

You can also install the ISO using the upgrade procedure in the Cisco Unified Operating System Administration web interface.
                                    For more information, see Access Unified OS Administration .

##### Before you begin

Before you begin the upgrade from 12.6(1) to 12.6(2), you must install the COP ucos.keymanagement.v02.cop.sgn on the base version.

For 12.5(1) SU to 12.6(2) upgrade no COP is required to be applied.

Download the ISO file from https://software.cisco.com/download/home/282163829/type/282377062/release to the SFTP server that can be accessed from the Cisco Unified Intelligence Center system.

Step 1

Log in to Unified Intelligence Center CLI and specify the System Administration username and password.

Step 2

Enter the command utils system upgrade initiate to initiate the ISO installation.

Step 3

Select Remote File System from source list page.

Step 4

Enter the remote path to the directory on the SFTP server where you have downloaded the ISO file.

If the ISO file is located on a Linux or UNIX server, you must enter a forward slash (/) at the beginning of the directory
                                                            path. For example, if the COP file is in the patches directory, enter / patches . If the ISO file is located on a Windows server, check with your system administrator for the correct directory path.

Step 5

Enter the SFTP server name or IP address and then enter the credentials.

Step 6

Enter the relevant option when you are prompted Continue with upgrade after download (yes/no) .

Enter yes to continue with upgrade after the download is complete.

Enter no if you want to cancel the upgrade.

Step 7

Enter the relevant option when you are prompted Switch-version server after upgrade [valid only for ISO] (yes/no) .

Enter yes to automatically switch the version after upgrade.

Enter no if you need to manually switch the version after all the nodes are upgraded (refer step 11 for more details).

After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                            Center 12.5(1) to 12.6(1).

If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1).

Step 8

If the transfer protocol is selected as SFTP, the system displays the list of ISO files available in the SFTP location.

Step 9

Select the number corresponding to the ISO file that you want to install, and press Enter .

Step 10

In cluster setup, first complete the upgrade on the publisher node and perform the upgrade on the subscriber node. If you
                                             chose to manually switch version, after successful upgrades, switch the version using the command utils system switch-version first on the publisher node and later on the subscriber nodes.

After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                            can upgrade from Cisco Unified Intelligence Center 12.5(1) to 12.6 (1).

If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1).

### Upgrade VMware
                           	 Tools

Use this procedure to upgrade VMware tools from the VMware vSphere Client followed by the CLI command.

To upgrade VMware tools for Cisco Unified Intelligence Center:

Step 1

Power on the virtual machine.

Step 2

Right-click the VM and select Guest > Install/Upgrade VMware Tools .

Step 3

Select the Interactive Tools Upgrade option and click OK .

Step 4

Open the administrator console and log in to command prompt.

Step 5

Run the command utils vmtools refresh and confirm.

Step 6

After reboot, from the vSphere client, select the VM and click the Summary tab.

Step 7

Check for the VMware Tools status is “Running (Current)”.

## Access Unified OS
                        	 Administration

Step 1

Enter http s ://x.x.x.x/cmplatform , where x.x.x.x is the IP address of the node.

Step 2

Sign in using
                                       			 the username and password of the system administrator account.

Step 3

Select Software
                                             				  Upgrades > Install/Upgrade to display the
                                       			 Software Installation/Upgrade page.

Step 4

Select source: DVD/CD or Remote
                                          				Filesystem .

Use Unified OS Administration to perform an upgrade using ISO. To install a COP, use the CLI option only. For more information
                                                      on how to use the CLI, refer to the readme file of the ES.

## Upgrade From
                        	 DVD/CD

Follow these steps if a DVD/CD is the source for your install or upgrade.

Step 1

Prepare a
                                       			 writeable DVD and insert it into the disc drive on the server that is to be
                                       			 upgraded.

Step 2

Select DVD/CD
                                       			 from the Source list on the Software
                                             				  Upgrades > Install/Upgrade page .

Step 3

In the Directory
                                       			 field, enter the path to the upgrade file.

If the file is
                                          				in the root directory, enter a slash (/) in the Directory field.

Step 4

To continue the
                                       			 upgrade process, click Next .

Step 5

Choose the
                                       			 upgrade version that you want to install and click Next .

Step 6

In the next
                                       			 window, monitor the progress of the download.

Step 7

When the
                                       			 download completes, Click Next .

Step 8

If you want to
                                       			 install the upgrade and automatically reboot to the upgraded partition, choose Reboot
                                          				to upgraded partition . The system restarts running the upgraded
                                       			 software.

Step 9

If you want to
                                       			 install the upgrade and then manually reboot to the upgraded partition at a
                                       			 later time, do the following:

Choose Do
                                                					 not reboot after upgrade .

Click Next . The Upgrade Status window displays the Upgrade
                                             				  log.

When the
                                             				  installation completes, click Finish .

To restart
                                             				  the system and activate the upgrade, choose Settings > Version , and then click Switch Version .

The system
                                          				restarts running the upgraded software.

Step 10

Run the utility to update the VMware settings. See Upgrade VMWare Settings Utility .

Step 11

Clear the browser cache and cookies manually before you start working on the new version of Unified Intelligence Center. For
                                       more information about clearing the cache and cookies, see your browser-specific documentation.

## Upgrade From Remote
                        	 Filesystem

Follow these steps if Remote Filesystem is the source for your install or upgrade.

Step 1

Choose Remote
                                          				Filesystem from the Source list on the Software
                                             				  Upgrades > Install/Upgrade page.

Step 2

Enter the path
                                       			 to the directory that contains the patch file on the remote system in the
                                       			 Directory field.

If the upgrade
                                          				file is on a Linux or Unix server, you must enter a forward slash at the
                                          				beginning of the directory path. For example, if the upgrade file is in the
                                          				patches directory, enter /patches . If the upgrade file is on a Windows
                                          				server, check with your system administrator for the correct directory path.

Step 3

In the Server field, enter the server name or IP address.

Step 4

In the User
                                          				Name field, enter your username on the remote server.

Step 5

In the User
                                          				Password field, enter your password on the remote server.

Step 6

Select the
                                       			 transfer protocol from the Transfer
                                          				Protocol field.

Step 7

To continue the
                                       			 upgrade process, click Next .

Step 8

In the next
                                       			 window, monitor the progress of the download.

Step 9

When the
                                       			 download completes, click Next .

Step 10

If you want to
                                       			 install the upgrade and automatically reboot to the upgraded partition, choose Reboot
                                          				to upgraded partition . The system restarts running the upgraded
                                       			 software.

Step 11

If you want to
                                       			 install the upgrade and then manually reboot to the upgraded partition at a
                                       			 later time, do the following:

Choose Do
                                                					 not reboot after upgrade .

Click Next . The Upgrade Status window displays the Upgrade
                                             				  log.

When the
                                             				  installation completes, click Finish .

To restart
                                             				  the system and activate the upgrade, choose Settings > Version , and then click Switch Version .

The system
                                          				restarts running the upgraded software.

Step 12

Run the utility to update the VMware settings. See Upgrade VMWare Settings Utility .

Step 13

Clear the browser cache before you start working on the new version of Unified Intelligence Center. For more information about
                                       clearing the cache and cookies, see your browser-specific documentation.

## Revert to Previous
                        	 Version

All nodes must be running the same version of Unified Intelligence
                                          			 Center. Reverting is an all-or-none operation when you operate a cluster of
                                          			 Unified Intelligence Center nodes.

### Procedure to Revert to Previous Version

If you have upgraded from 12.0(1) to 12.6(1), you cannot revert to versions earlier than 12.0(1).

If you have upgraded from 12.5(1) to 12.6(1), you cannot revert to versions earlier than 12.5(1).

Follow these steps to revert using Unified OS Administration:

Step 1

Open Unified OS Administration page entering the following URL: https://server-name/cmplatform , where server-name is the hostname or IP address of the node.

Step 2

Sign in using the system administrator credentials.

Step 3

Choose Settings > Version . This opens the Version Settings screen, which shows the software version on both the active and inactive partitions. To
                                          switch versions and restart, click Switch Versions . When the system restarts, it boots to the now-active (formerly inactive) partition with your migrated data in place.

It takes about half an hour to complete the Switch Version and the restart.

| Note | For important notes, caveats, and other considerations, see the Cisco Unified Intelligence Center chapter in the Release Notes for Cisco Unified Contact Center Enterprise Solution available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html . If you’re upgrading the Cisco Unified Intelligence Center (coresident) deployment, Live Data is also upgraded. As Live Data
                                                must be of the same version as Central Controller Components, Central Controller Components must be upgraded in the same window. |
|---|---|

| Note | To perform an upgrade of Cisco Unified Intelligence Center to 12.6(1), you must first perform an upgrade to 12.0(1) from the previous versions (11.0(x)) and then upgrade to 12.6(1). Cisco Unified Intelligence Center 12.5(1) users can directly upgrade to 12.6(1). |
|---|---|

| Note | After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. You can add
                                          them back, if necessary. For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki . For information about adding a certificate, see Insert a new tomcat-trust certificate at https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/210541-CUCM-Certificate-Management-and-Change-N.html . |
|---|---|

| Note | If you upgrade Cisco Unified Intelligence Center to version 12.6(1) and your Live Data (standalone) server remains on an earlier
                                          version (11.6(1), 12.0(1), or 12.5(1)), ensure that you update the Live Data server with the latest ES for that release. This
                                          is required for the Live Data gadgets to work in the Finesse desktop. |
|---|---|

| Step 1 | Point your browser to the Download Software page for Cisco Unified Intelligence Center : https://software.cisco.com/download/type.html?mdfid=282163829&i=rm , and click the Unified Intelligence Center Software link. |
|---|---|
| Step 2 | Navigate to the
                                       			 folder and subfolder for the release you want. |
| Step 3 | Select the
                                       			 Unified Intelligence Center installer .iso file and click Download . |
| Step 4 | Click Log
                                          				in . |

| Step 1 | Log in to Unified Intelligence Center CLI and specify the System Administration username and password. |
|---|---|
| Step 2 | Enter the command utils system upgrade initiate to initiate the ISO installation. |
| Step 3 | Select Remote File System from the source list page. |
| Step 4 | Enter the remote path to the directory on the SFTP server where
                                          			 you have downloaded the ISO file. Note If the ISO file is located on a Linux or UNIX server, you must
                                                         				  enter a forward slash (/) at the beginning of the directory path. For example,
                                                         				  if the COP file is in the patches directory, enter / patches . If the
                                                         				  ISO file is located on a Windows server, check with your system administrator
                                                         				  for the correct directory path. | Note | If the ISO file is located on a Linux or UNIX server, you must
                                                         				  enter a forward slash (/) at the beginning of the directory path. For example,
                                                         				  if the COP file is in the patches directory, enter / patches . If the
                                                         				  ISO file is located on a Windows server, check with your system administrator
                                                         				  for the correct directory path. |
| Note | If the ISO file is located on a Linux or UNIX server, you must
                                                         				  enter a forward slash (/) at the beginning of the directory path. For example,
                                                         				  if the COP file is in the patches directory, enter / patches . If the
                                                         				  ISO file is located on a Windows server, check with your system administrator
                                                         				  for the correct directory path. |
| Step 5 | Enter the SFTP server name or IP address and then enter the credentials. It’s optional for you to enter the SMTP Host Server name. |
| Step 6 | Select the transfer protocol as SFTP. The system displays the list
                                          			 of ISO files available in the SFTP location. |
| Step 7 | Select the number corresponding to the ISO file that you want to install, and press Enter . |
| Step 8 | Enter the relevant option when you’re prompted Switch to new version if the upgrade is successful (yes/no) . Enter yes to automatically switch the version . Enter no if you  need to manually switch the version after all the nodes are upgraded (refer step 10 for more details). Note After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                         Center 12.0(1) to 12.6(1). If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1) and the active version is 12.6(1). | Note | After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                         Center 12.0(1) to 12.6(1). If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1) and the active version is 12.6(1). |
| Note | After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                         Center 12.0(1) to 12.6(1). If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1) and the active version is 12.6(1). |
| Step 9 | Enter yes when you’re prompted Start Refresh Upgrade (yes/no) . |
| Step 10 | In cluster setup, first complete the upgrade on the publisher node and perform the upgrade on the subscriber node. After successful
                                          upgrades, switch the version using the command utils system switch-version first on the publisher node and later on the subscriber nodes. Note After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                         can upgrade from Cisco Unified Intelligence Center 12.0(1) to 12.6 (1). If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1), and the active version is 12.6(1). | Note | After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                         can upgrade from Cisco Unified Intelligence Center 12.0(1) to 12.6 (1). If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1), and the active version is 12.6(1). |
| Note | After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                         can upgrade from Cisco Unified Intelligence Center 12.0(1) to 12.6 (1). If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1), and the active version is 12.6(1). |

| Note | If the ISO file is located on a Linux or UNIX server, you must
                                                         				  enter a forward slash (/) at the beginning of the directory path. For example,
                                                         				  if the COP file is in the patches directory, enter / patches . If the
                                                         				  ISO file is located on a Windows server, check with your system administrator
                                                         				  for the correct directory path. |
|---|---|

| Note | After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                         Center 12.0(1) to 12.6(1). If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1) and the active version is 12.6(1). |
|---|---|

| Note | After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                         can upgrade from Cisco Unified Intelligence Center 12.0(1) to 12.6 (1). If you upgrade from 12.0(1) to 12.6(1), the inactive version is 12.0(1), and the active version is 12.6(1). |
|---|---|

| Note | For 12.5(1) SU to 12.6(2) upgrade no COP is required to be applied. |
|---|---|

| Step 1 | Log in to Unified Intelligence Center CLI and specify the System Administration username and password. |
|---|---|
| Step 2 | Enter the command utils system upgrade initiate to initiate the ISO installation. |
| Step 3 | Select Remote File System from source list page. |
| Step 4 | Enter the remote path to the directory on the SFTP server where you have downloaded the ISO file. Note If the ISO file is located on a Linux or UNIX server, you must enter a forward slash (/) at the beginning of the directory
                                                            path. For example, if the COP file is in the patches directory, enter / patches . If the ISO file is located on a Windows server, check with your system administrator for the correct directory path. | Note | If the ISO file is located on a Linux or UNIX server, you must enter a forward slash (/) at the beginning of the directory
                                                            path. For example, if the COP file is in the patches directory, enter / patches . If the ISO file is located on a Windows server, check with your system administrator for the correct directory path. |
| Note | If the ISO file is located on a Linux or UNIX server, you must enter a forward slash (/) at the beginning of the directory
                                                            path. For example, if the COP file is in the patches directory, enter / patches . If the ISO file is located on a Windows server, check with your system administrator for the correct directory path. |
| Step 5 | Enter the SFTP server name or IP address and then enter the credentials. It is optional for you to enter the SMTP Host Server name. |
| Step 6 | Enter the relevant option when you are prompted Continue with upgrade after download (yes/no) . Enter yes to continue with upgrade after the download is complete. Enter no if you want to cancel the upgrade. |
| Step 7 | Enter the relevant option when you are prompted Switch-version server after upgrade [valid only for ISO] (yes/no) . Enter yes to automatically switch the version after upgrade. Enter no if you need to manually switch the version after all the nodes are upgraded (refer step 11 for more details). Note After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                            Center 12.5(1) to 12.6(1). If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1). | Note | After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                            Center 12.5(1) to 12.6(1). If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1). |
| Note | After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                            Center 12.5(1) to 12.6(1). If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1). |
| Step 8 | If the transfer protocol is selected as SFTP, the system displays the list of ISO files available in the SFTP location. |
| Step 9 | Select the number corresponding to the ISO file that you want to install, and press Enter . When the download is complete, the nodes are automatically upgraded. |
| Step 10 | In cluster setup, first complete the upgrade on the publisher node and perform the upgrade on the subscriber node. If you
                                             chose to manually switch version, after successful upgrades, switch the version using the command utils system switch-version first on the publisher node and later on the subscriber nodes. Note After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                            can upgrade from Cisco Unified Intelligence Center 12.5(1) to 12.6 (1). If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1). | Note | After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                            can upgrade from Cisco Unified Intelligence Center 12.5(1) to 12.6 (1). If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1). |
| Note | After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                            can upgrade from Cisco Unified Intelligence Center 12.5(1) to 12.6 (1). If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1). |

| Note | If the ISO file is located on a Linux or UNIX server, you must enter a forward slash (/) at the beginning of the directory
                                                            path. For example, if the COP file is in the patches directory, enter / patches . If the ISO file is located on a Windows server, check with your system administrator for the correct directory path. |
|---|---|

| Note | After successfully switching the version, verify if the node is upgraded. You can upgrade from Cisco Unified Intelligence
                                                            Center 12.5(1) to 12.6(1). If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1). |
|---|---|

| Note | After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. You
                                                            can upgrade from Cisco Unified Intelligence Center 12.5(1) to 12.6 (1). If you upgrade from 12.5(1) to 12.6(1), the inactive version is 12.5(1), and the active version is 12.6(1). |
|---|---|

| Step 1 | Power on the virtual machine. |
|---|---|
| Step 2 | Right-click the VM and select Guest > Install/Upgrade VMware Tools . |
| Step 3 | Select the Interactive Tools Upgrade option and click OK . |
| Step 4 | Open the administrator console and log in to command prompt. |
| Step 5 | Run the command utils vmtools refresh and confirm. The server automatically reboots twice. This process takes a few minutes. |
| Step 6 | After reboot, from the vSphere client, select the VM and click the Summary tab. |
| Step 7 | Check for the VMware Tools status is “Running (Current)”. |

| Step 1 | Enter http s ://x.x.x.x/cmplatform , where x.x.x.x is the IP address of the node. |
|---|---|
| Step 2 | Sign in using
                                       			 the username and password of the system administrator account. |
| Step 3 | Select Software
                                             				  Upgrades > Install/Upgrade to display the
                                       			 Software Installation/Upgrade page. Figure 1. Software
                                             				  Upgrade Page |
| Step 4 | Select source: DVD/CD or Remote
                                          				Filesystem . Note Use Unified OS Administration to perform an upgrade using ISO. To install a COP, use the CLI option only. For more information
                                                      on how to use the CLI, refer to the readme file of the ES. | Note | Use Unified OS Administration to perform an upgrade using ISO. To install a COP, use the CLI option only. For more information
                                                      on how to use the CLI, refer to the readme file of the ES. |
| Note | Use Unified OS Administration to perform an upgrade using ISO. To install a COP, use the CLI option only. For more information
                                                      on how to use the CLI, refer to the readme file of the ES. |

| Note | Use Unified OS Administration to perform an upgrade using ISO. To install a COP, use the CLI option only. For more information
                                                      on how to use the CLI, refer to the readme file of the ES. |
|---|---|

| Step 1 | Prepare a
                                       			 writeable DVD and insert it into the disc drive on the server that is to be
                                       			 upgraded. |
|---|---|
| Step 2 | Select DVD/CD
                                       			 from the Source list on the Software
                                             				  Upgrades > Install/Upgrade page . |
| Step 3 | In the Directory
                                       			 field, enter the path to the upgrade file. If the file is
                                          				in the root directory, enter a slash (/) in the Directory field. |
| Step 4 | To continue the
                                       			 upgrade process, click Next . |
| Step 5 | Choose the
                                       			 upgrade version that you want to install and click Next . |
| Step 6 | In the next
                                       			 window, monitor the progress of the download. |
| Step 7 | When the
                                       			 download completes, Click Next . |
| Step 8 | If you want to
                                       			 install the upgrade and automatically reboot to the upgraded partition, choose Reboot
                                          				to upgraded partition . The system restarts running the upgraded
                                       			 software. |
| Step 9 | If you want to
                                       			 install the upgrade and then manually reboot to the upgraded partition at a
                                       			 later time, do the following: Choose Do
                                                					 not reboot after upgrade . Click Next . The Upgrade Status window displays the Upgrade
                                             				  log. When the
                                             				  installation completes, click Finish . To restart
                                             				  the system and activate the upgrade, choose Settings > Version , and then click Switch Version . The system
                                          				restarts running the upgraded software. |
| Step 10 | Run the utility to update the VMware settings. See Upgrade VMWare Settings Utility . |
| Step 11 | Clear the browser cache and cookies manually before you start working on the new version of Unified Intelligence Center. For
                                       more information about clearing the cache and cookies, see your browser-specific documentation. |

| Step 1 | Choose Remote
                                          				Filesystem from the Source list on the Software
                                             				  Upgrades > Install/Upgrade page. |
|---|---|
| Step 2 | Enter the path
                                       			 to the directory that contains the patch file on the remote system in the
                                       			 Directory field. If the upgrade
                                          				file is on a Linux or Unix server, you must enter a forward slash at the
                                          				beginning of the directory path. For example, if the upgrade file is in the
                                          				patches directory, enter /patches . If the upgrade file is on a Windows
                                          				server, check with your system administrator for the correct directory path. |
| Step 3 | In the Server field, enter the server name or IP address. |
| Step 4 | In the User
                                          				Name field, enter your username on the remote server. |
| Step 5 | In the User
                                          				Password field, enter your password on the remote server. |
| Step 6 | Select the
                                       			 transfer protocol from the Transfer
                                          				Protocol field. |
| Step 7 | To continue the
                                       			 upgrade process, click Next . |
| Step 8 | In the next
                                       			 window, monitor the progress of the download. |
| Step 9 | When the
                                       			 download completes, click Next . |
| Step 10 | If you want to
                                       			 install the upgrade and automatically reboot to the upgraded partition, choose Reboot
                                          				to upgraded partition . The system restarts running the upgraded
                                       			 software. |
| Step 11 | If you want to
                                       			 install the upgrade and then manually reboot to the upgraded partition at a
                                       			 later time, do the following: Choose Do
                                                					 not reboot after upgrade . Click Next . The Upgrade Status window displays the Upgrade
                                             				  log. When the
                                             				  installation completes, click Finish . To restart
                                             				  the system and activate the upgrade, choose Settings > Version , and then click Switch Version . The system
                                          				restarts running the upgraded software. Note It takes
                                                   				about half an hour to complete the Switch Version and the restart. | Note | It takes
                                                   				about half an hour to complete the Switch Version and the restart. |
| Note | It takes
                                                   				about half an hour to complete the Switch Version and the restart. |
| Step 12 | Run the utility to update the VMware settings. See Upgrade VMWare Settings Utility . |
| Step 13 | Clear the browser cache before you start working on the new version of Unified Intelligence Center. For more information about
                                       clearing the cache and cookies, see your browser-specific documentation. |

| Note | It takes
                                                   				about half an hour to complete the Switch Version and the restart. |
|---|---|

| Note | All nodes must be running the same version of Unified Intelligence
                                          			 Center. Reverting is an all-or-none operation when you operate a cluster of
                                          			 Unified Intelligence Center nodes. |
|---|---|

| Note | If you have upgraded from 12.0(1) to 12.6(1), you cannot revert to versions earlier than 12.0(1). If you have upgraded from 12.5(1) to 12.6(1), you cannot revert to versions earlier than 12.5(1). |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Open Unified OS Administration page entering the following URL: https://server-name/cmplatform , where server-name is the hostname or IP address of the node. |  |
| Step 2 | Sign in using the system administrator credentials. |  |
| Step 3 | Choose Settings > Version . This opens the Version Settings screen, which shows the software version on both the active and inactive partitions. To
                                          switch versions and restart, click Switch Versions . When the system restarts, it boots to the now-active (formerly inactive) partition with your migrated data in place. | Note It takes about half an hour to complete the Switch Version and the restart. | Note | It takes about half an hour to complete the Switch Version and the restart. |
| Note | It takes about half an hour to complete the Switch Version and the restart. |

| Note | It takes about half an hour to complete the Switch Version and the restart. |
|---|---|