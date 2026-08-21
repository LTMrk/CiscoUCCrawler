---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-150-instal-7afae889bf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_150/install/guide/cuic_b_install_upgrade_guide_15_0/cuic_m_1501_upgrades.html
retrieved_at: 2026-08-21T04:41:25.386132+00:00
---

Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 15.0(1)

# Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 15.0(1)

Updated: April 30, 2025

Chapter: Upgrades

## Chapter: Upgrades

# Upgrades

## Before You Upgrade

For important notes, caveats, and other considerations, see the Cisco Unified Intelligence Center chapter in the Release Notes for Cisco Unified Contact Center Enterprise Solution available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html .

If you’re upgrading the Cisco Unified Intelligence Center (coresident) deployment, Live Data is also upgraded. As Live Data
                                                must be of the same version as Central Controller Components, Central Controller Components must be upgraded in the same window.

Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                                using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                                and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                                the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                                node is upgraded and in the IN_SERVICE status.

Unsupported Widgets

The Cisco Unified Intelligence Center interface for Dashboards doesn’t support the following widgets:

Schedule Report widgets

URL widgets containing Dashboard permalinks (Nested Dashboards)

Migration Limitations

To address injection vulnerabilities, the Custom Widget feature in Dashboards is disabled by default. If any custom widgets were added to the Dashboards in versions earlier to Cisco Unified Intelligence Center 12.6 , those widgets are visible in the read-only mode post upgrade to the 12.6 version. You can opt to retain or delete them.

To enable the Custom Widget feature, use the CLI and set cuic properties dashboard-customwidget-enabled set the parameter value to "on".

For more information, see the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

For base version before 12.5(1) SU, you must first upgrade to 12.5(1) SU and then upgrade to Cisco Unified Intelligence Center 15.0(1).

Cisco Unified Intelligence Center 12.5(1) SU, 12.6(1), and 12.6(2) users can directly upgrade to 15.0(1).

Upgrade Prerequisites

Before starting the software upgrade,

Perform the Unified CCE User Integration to import supervisors and their teams from Unified CCE into the Cisco Unified Intelligence
                                    Center.

Back up your system data using the Disaster Recovery system application. To access the DRS application, direct your browser to https:// IP address of Intelligence Center :8443/drf. For more information, see the online help provided with the DRS application.

Ensure that the certificates aren’t expired. If the certificates are expired, regenerate the certificates.

Upgrade and restart the Controller node first. Then upgrade and restart the members. All nodes must be on the same version
                              of the Cisco Unified Intelligence Center.

After upgrading Cisco Unified Intelligence Center to release 15.0(1) , ensure to perform the following:

Disable the Unified CCE User Integration. (Uncheck the Enable UCCE User Integration check box in OAMP > Cluster Configuration > UCCE User Integration.)

Install the latest Cisco Options Package (COP) file for the Cisco Unified Intelligence Center 15.0(1) release.

Enable the Unified CCE User Integration manually to import the Supervisors with the required roles. This setting is required
                                    to view gadgets in the Cisco Finesse Desktop for Supervisors. For more information on User Integration, see the Unified CCE User Integration Configuration section in the Administration Console User Guide for Cisco Unified Intelligence Center at

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

Configure CORS and reset the cluster configuration. For more information on enabling the CORS CLI and to reset the cluster
                                    configuration, see Post-Install Configuration .

When you upgrade Cisco Unified Intelligence Center from 12.5(1) SU to release 15.0(1) , permissions of all the STOCK value lists for the ALLUSERS group is set to NONE. Therefore, you must reset the permissions
                                    manually in 15.0(1) if you want users to use the entire value list.

Your configuration information moves automatically to the upgraded version in the active partition.

After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. You can add
                                          them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki .

For information about adding a certificate, see Insert a new tomcat-trust certificate at

https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/210541-CUCM-Certificate-Management-and-Change-N.html .

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

## Upgrade VMware vSphere ESXi for Upgrade

If you use VMware vCenter Server in your deployment, upgrade VMware vCenter Server before upgrading VMware vSphere ESXi.

Upgrade VMWare vSphere ESXi on Side A and Side B servers to the latest version supported with this release of Packaged CCE.
                           Packaged CCE uses standard upgrade procedures, which you can find using VMware documentation ( https://www.vmware.com/support/pubs/ ).

## Upgrade Unified Intelligence Center

If you are upgrading from 12.5(1) SU or 12.6(1) to 15.0(1), the Hazelcast library is upgraded. In TCP mode, Hazelcast can’t
                                          start with nodes having different versions. In TCP mode, the nodes that are upgraded to 15.0(1) have the Intelligence Center Reporting Service in starting state until all the remaining nodes in the cluster are upgraded to 15.0(1).

As mentioned earlier in this chapter, all the nodes in a cluster must be on the same version. However, if you have upgraded
                                          only some nodes and want Intelligence Center Reporting Service available on the upgraded nodes, do one of the following:

Stop the Intelligence Center Reporting Service on all the nodes that aren’t upgraded and then restart the upgraded nodes.

Before the upgrade, change the cluster mode to UDP on all the nodes using the utils cuic cluster mode CLI command. After upgrading all the nodes, set the cluster mode to TCP. For more information, see the Cluster Configuration for JVM Using Hazelcast section in the Administration Console User Guide for Cisco Unified Intelligence Center .

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

After successfully switching the version, verify if the node is upgraded.

If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2).

If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2).

If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2).

If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1).

Step 8

If the transfer protocol is selected as SFTP, the system displays the list of ISO files available in the SFTP location.

Step 9

Select the number corresponding to the ISO file that you want to install, and press Enter .

Step 10

In cluster setup, first complete the upgrade on the publisher node and perform the upgrade on the subscriber node. If you
                                       chose to manually switch version, after successful upgrades, switch the version using the command utils system switch-version first on the publisher node and later on the subscriber nodes.

After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded.

If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2).

If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2).

If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2).

If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1).

## Upgrade VMware
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

If you have upgraded from 12.5(1) SU to 15.0(1), you cannot revert to versions earlier than 12.5(1) SU.

If you have upgraded from 12.6(1) to 15.0(1), you cannot revert to versions earlier than 12.6(1).

If you have upgraded from 12.6(2) to 15.0(1), you cannot revert to versions earlier than 12.6(2).

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
                                                must be of the same version as Central Controller Components, Central Controller Components must be upgraded in the same window. Upgrading Cisco IdS to 15.0(1) via maintenance mode is supported only on the primary node. Upgrade the secondary node to 15.0(1)
                                                using the standard system upgrade procedure. If a failover occurs during the initial login process (with IdP authentication
                                                and SAML assertions) after the primary node is upgraded, login failures may occur. In such cases, a browser refresh will restart
                                                the login process. Therefore, it is strongly recommended to upgrade the secondary node to 15.0(1) immediately after the primary
                                                node is upgraded and in the IN_SERVICE status. |
|---|---|

| Note | For base version before 12.5(1) SU, you must first upgrade to 12.5(1) SU and then upgrade to Cisco Unified Intelligence Center 15.0(1). Cisco Unified Intelligence Center 12.5(1) SU, 12.6(1), and 12.6(2) users can directly upgrade to 15.0(1). |
|---|---|

| Note | After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. You can add
                                          them back, if necessary. For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki . For information about adding a certificate, see Insert a new tomcat-trust certificate at https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/210541-CUCM-Certificate-Management-and-Change-N.html . |
|---|---|

| Step 1 | Point your browser to the Download Software page for Cisco Unified Intelligence Center : https://software.cisco.com/download/type.html?mdfid=282163829&i=rm , and click the Unified Intelligence Center Software link. |
|---|---|
| Step 2 | Navigate to the
                                       			 folder and subfolder for the release you want. |
| Step 3 | Select the
                                       			 Unified Intelligence Center installer .iso file and click Download . |
| Step 4 | Click Log
                                          				in . |

| Note | If you are upgrading from 12.5(1) SU or 12.6(1) to 15.0(1), the Hazelcast library is upgraded. In TCP mode, Hazelcast can’t
                                          start with nodes having different versions. In TCP mode, the nodes that are upgraded to 15.0(1) have the Intelligence Center Reporting Service in starting state until all the remaining nodes in the cluster are upgraded to 15.0(1). As mentioned earlier in this chapter, all the nodes in a cluster must be on the same version. However, if you have upgraded
                                          only some nodes and want Intelligence Center Reporting Service available on the upgraded nodes, do one of the following: Stop the Intelligence Center Reporting Service on all the nodes that aren’t upgraded and then restart the upgraded nodes. Before the upgrade, change the cluster mode to UDP on all the nodes using the utils cuic cluster mode CLI command. After upgrading all the nodes, set the cluster mode to TCP. For more information, see the Cluster Configuration for JVM Using Hazelcast section in the Administration Console User Guide for Cisco Unified Intelligence Center . |
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
| Step 7 | Enter the relevant option when you are prompted Switch-version server after upgrade [valid only for ISO] (yes/no) . Enter yes to automatically switch the version after upgrade. Enter no if you need to manually switch the version after all the nodes are upgraded (refer step 11 for more details). Note After successfully switching the version, verify if the node is upgraded. If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2). If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2). If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2). If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1). | Note | After successfully switching the version, verify if the node is upgraded. If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2). If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2). If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2). If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1). |
| Note | After successfully switching the version, verify if the node is upgraded. If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2). If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2). If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2). If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1). |
| Step 8 | If the transfer protocol is selected as SFTP, the system displays the list of ISO files available in the SFTP location. |
| Step 9 | Select the number corresponding to the ISO file that you want to install, and press Enter . When the download is complete, the nodes are automatically upgraded. |
| Step 10 | In cluster setup, first complete the upgrade on the publisher node and perform the upgrade on the subscriber node. If you
                                       chose to manually switch version, after successful upgrades, switch the version using the command utils system switch-version first on the publisher node and later on the subscriber nodes. Note After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2). If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2). If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2). If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1). | Note | After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2). If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2). If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2). If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1). |
| Note | After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2). If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2). If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2). If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1). |

| Note | If the ISO file is located on a Linux or UNIX server, you must enter a forward slash (/) at the beginning of the directory
                                                      path. For example, if the COP file is in the patches directory, enter / patches . If the ISO file is located on a Windows server, check with your system administrator for the correct directory path. |
|---|---|

| Note | After successfully switching the version, verify if the node is upgraded. If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2). If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2). If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2). If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1). |
|---|---|

| Note | After successfully switching the version of the publisher node and subscriber node, verify if the nodes are upgraded. If you upgrade from 12.5(1) to 12.6(2), the inactive version is 12.5(1) and the active version is 12.6(2). If you upgrade from 12.5(1) SU to 12.6(2), the inactive version is 12.5(1) SU and the active version is 12.6(2). If you upgrade from 12.6(1) to 12.6(2), the inactive version is 12.6(1) and the active version is 12.6(2). If you upgrade from 12.6(2) to 15.0(1), the inactive version is 12.6(2) and the active version is 15.0(1). |
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

| Note | If you have upgraded from 12.5(1) SU to 15.0(1), you cannot revert to versions earlier than 12.5(1) SU. If you have upgraded from 12.6(1) to 15.0(1), you cannot revert to versions earlier than 12.6(1). If you have upgraded from 12.6(2) to 15.0(1), you cannot revert to versions earlier than 12.6(2). |
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