---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-srsv-guide-b-12xcucsrsvx-b-12xcucsrsvx-chapter-0100-html-96091978bd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/srsv/guide/b_12xcucsrsvx/b_12xcucsrsvx_chapter_0100.html
retrieved_at: 2026-08-21T07:56:04.950625+00:00
---

Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

# Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

Updated: August 17, 2017

Chapter: Upgrading Cisco Unity Connection SRSV

## Chapter: Upgrading Cisco Unity Connection SRSV

# Upgrading Cisco Unity Connection SRSV

## Introduction

You need to upgrade from the current version of Cisco Unity Connection SRSV to a higher version to use the new features. When
                           you upgrade a server, the new version of Unity Connection SRSV is installed in a separate disk partition known as inactive
                           partition. To activate the new version, you need to perform switch version. Following are the two ways to switch to the new
                           version:

Automatic Switching: Allows you to automatically switch to the new version of Unity Connection SRSV as part of the upgrade
                                 process.

Manual Switching: Allows you to manually switch to the new version of Unity Connection SRSV after the successful completion
                                 of upgrade.

During the switch version of the Unity Connection SRSV, it is recommended to stop the automatic provisioning/vmupload feature
                                             at the central Unity Connection. To stop the automatic provisioning/vmupload feature, uncheck the Enabled check box on the
                                             Branch Listing page in Cisco Unity Connection Administration.

## Upgrade
                        	 Types

The Unity Connection SRSV upgrade files are available as ISO
                           		image files. You can use either of the following interfaces to upgrade Unity
                           		Connection SRSV:

Command Line Interface (CLI). For more information, see Upgrade Unity Connection SRSV Using CLI section.

Cisco Unified OS Administration web interface. For more
                                 			 information, see Upgrade Unity Connection SRSV From a Local DVD or a Network Location section.

You must save the COP files on a network location FTP/SFTP
                           		server accessible during the upgrade. ISO image can be saved on a local DVD or
                           		on a network location. The performance of the upgrades can be monitored through
                           		CLI or Cisco Unified Operating System Administration interfaces.

## Status of Unity Connection Features During Unity Connection SRSV Upgrade

During the switch version of the Unity Connection SRSV, the telephone user interface (touchtone conversation) features and
                           web features of Unity Connection are completely disabled for approximately 1 hour.

## Duration of Upgrade

Under ideal network conditions, an upgrade process takes approximately four hours to upgrade to the Unity Connection SRSV
                           server. Depending on the data size of the server, the switch version process may take two more hours to successfully upgrade
                           to a new version.

If you are upgrading in a slow network condition, the upgrade process may take longer time than expected. It is always recommended
                           to upgrade during off-peak hours or during a maintenance window to avoid service interruptions.

## Task List for
                        	 Upgrading Unity Connection SRSV

Review the list of features that are disabled or that have limited functionality during the upgrade. See the Status of Unity Connection Features During Unity Connection SRSV Upgrade .

Run the CLI command run cuc preupgrade test to verify the prerequisites before starting the upgrade.

Upgrade the Unity Connection SRSV software. For more information, see the Upgrade Process section.

Switch to the upgraded software on the Unity Connection SRSV server. For more information, see the Switch Version section.

Make sure that the central Unity Connection server and Unity Connection SRSV have same release version.

After switch version, perform manual synchronization through central Unity Connection server and restart the Connection Conversation
                                 Manager service on Unity Connection SRSV branch.

For information on manual synchronization between central and branch sever, see Configuring Unity Connection SRSV Settings section.

Verify that the value entered in X.509 Subject Name field on SIP Trunk Security Profile Configuration page of Cisco Unified Communication Manager is the FQDN of the Unity Connection
                                                server

## Upgrade Process

### Upgrade Unity
                           	 Connection SRSV Using CLI

To upgrade Unity Connection SRSV using CLI, follow the upgrade
                              		process through the CLI interface. For more information, see the " Utils System Upgrade " section in the
                              		Command Line Interface Reference Guide for Cisco Unified Communications
                              		Solutions at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/8_6_1/cli_ref_861.html

You can check the status of the upgraded software by running the
                                          		  CLI command show cuc version. The upgrade is complete when the inactive
                                          		  partition has the upgraded software and the active partition has the old
                                          		  software.

### Upgrade Unity
                           	 Connection SRSV From a Local DVD or a Network Location

Perform either of the following tasks:

Copy the ISO file to a folder on an FTP or SFTP server
                                                   					 accessible to Unity Connection.

Insert the DVD with the ISO file of the Unity Connection server
                                                   					 that you want install into the disk drive of the server

In Cisco
                                          			 Unified Operating System Administration, expand Software Upgrades and select
                                          			 Install/Upgrade.

On the
                                          			 Software Installation/Upgrade page, in the Source field, select any one of the
                                          			 following:

Remote Filesystem: Select this option to upgrade from remoter
                                                   					 server and follow the procedure from Step
                                                      						4 .

DVD/CD: Select this option to upgrade from disk drive and move
                                                   					 to Step
                                                      						5

Enter the
                                          			 values in the following fields:

Directory

Server

- User Name

- User Password

- Transfer Protocol

Select the
                                          			 upgrade version that you want to install and select Next. The upgrade file is
                                          			 copied to the hard disk of the Unity Connection server. When the file is
                                          			 copied, a screen displaying the checksum value appears.

Verify the
                                          			 checksum.

On the next
                                          			 page, monitor the progress of the upgrade.

Select Next.

To verify if
                                          			 the upgrade is successful, run the following CLI commands:

show cuc
                                                   					 version: Displays the version of Unity Connection server in both active and
                                                   					 inactive partitions. The upgraded Unity Connection version is in the inactive
                                                   					 partition.

utils
                                                   					 system upgrade status: Displays the status of the upgrade that you performed.
                                                   					 This command should display the message for successful upgrade along with the
                                                   					 upgraded version.

## Switch Version

After completing the upgrade process, you need to manually switch over to the upgraded version of the Unity Connection SRSV.
                           For a single Unity Connection SRSV server, you can select either manual switch version or automatic switch version.

You can perform the switch version by running the utils system switch-version CLI command. The system automatically reboots
                           after the switch version.

If you select not to automatically switch to the upgraded partition at the end of the upgrade, perform the following procedure
                           when you are ready to switch partitions.

## Switching to the Upgraded Version of Unity Connection SRSV

In Cisco Unified Operating System
                                       			 Administration, expand Settings and select Version.

On the Version Settings page, select Switch
                                       			 Versions to start the following activities:

Unity Connection SRSV services are
                                                					 stopped.

Data from the active partition is copied
                                                					 to the inactive partition. Note that the messages are stored in a common
                                                					 partition, therefore they are not copied.

The Unity Connection SRSV server
                                                					 restarts and switches to the newer version.

| Note | During the switch version of the Unity Connection SRSV, it is recommended to stop the automatic provisioning/vmupload feature
                                             at the central Unity Connection. To stop the automatic provisioning/vmupload feature, uncheck the Enabled check box on the
                                             Branch Listing page in Cisco Unity Connection Administration. |
|---|---|

| Note | Verify that the value entered in X.509 Subject Name field on SIP Trunk Security Profile Configuration page of Cisco Unified Communication Manager is the FQDN of the Unity Connection
                                                server |
|---|---|

| Note | You can check the status of the upgraded software by running the
                                          		  CLI command show cuc version. The upgrade is complete when the inactive
                                          		  partition has the upgraded software and the active partition has the old
                                          		  software. |
|---|---|

| Step 1 | Perform either of the following tasks: Copy the ISO file to a folder on an FTP or SFTP server
                                                   					 accessible to Unity Connection. Insert the DVD with the ISO file of the Unity Connection server
                                                   					 that you want install into the disk drive of the server |
|---|---|
| Step 2 | In Cisco
                                          			 Unified Operating System Administration, expand Software Upgrades and select
                                          			 Install/Upgrade. |
| Step 3 | On the
                                          			 Software Installation/Upgrade page, in the Source field, select any one of the
                                          			 following: Remote Filesystem: Select this option to upgrade from remoter
                                                   					 server and follow the procedure from Step
                                                      						4 . DVD/CD: Select this option to upgrade from disk drive and move
                                                   					 to Step
                                                      						5 |
| Step 4 | Enter the
                                          			 values in the following fields: Directory Server User Name User Password Transfer Protocol |
| Step 5 | Select the
                                          			 upgrade version that you want to install and select Next. The upgrade file is
                                          			 copied to the hard disk of the Unity Connection server. When the file is
                                          			 copied, a screen displaying the checksum value appears. |
| Step 6 | Verify the
                                          			 checksum. |
| Step 7 | On the next
                                          			 page, monitor the progress of the upgrade. Caution If you
                                                      				loose your connection with the remote server or close your browser during this
                                                      				step, you may see the following warning when you try to view the Software
                                                      				Installation/Upgrade page again: Warning Another
                                                      				session is installing software, click Assume Control to take over the
                                                      				installation. To continue monitoring the upgrade, select Assume Control. | Caution | If you
                                                      				loose your connection with the remote server or close your browser during this
                                                      				step, you may see the following warning when you try to view the Software
                                                      				Installation/Upgrade page again: | Warning | Another
                                                      				session is installing software, click Assume Control to take over the
                                                      				installation. To continue monitoring the upgrade, select Assume Control. |
| Caution | If you
                                                      				loose your connection with the remote server or close your browser during this
                                                      				step, you may see the following warning when you try to view the Software
                                                      				Installation/Upgrade page again: |
| Warning | Another
                                                      				session is installing software, click Assume Control to take over the
                                                      				installation. To continue monitoring the upgrade, select Assume Control. |
| Step 8 | Select Next. Note During the
                                                      				initial phase of upgrade, the Installation Log text box in Cisco Unified
                                                      				Operating System Administration is updated with the information on the progress
                                                      				of the upgrade. To confirm the completion of upgrade, open the console of the
                                                      				Unity Connection server and make sure that a message indicating the completion
                                                      				of upgrade appears on the screen along with the login prompt. | Note | During the
                                                      				initial phase of upgrade, the Installation Log text box in Cisco Unified
                                                      				Operating System Administration is updated with the information on the progress
                                                      				of the upgrade. To confirm the completion of upgrade, open the console of the
                                                      				Unity Connection server and make sure that a message indicating the completion
                                                      				of upgrade appears on the screen along with the login prompt. |
| Note | During the
                                                      				initial phase of upgrade, the Installation Log text box in Cisco Unified
                                                      				Operating System Administration is updated with the information on the progress
                                                      				of the upgrade. To confirm the completion of upgrade, open the console of the
                                                      				Unity Connection server and make sure that a message indicating the completion
                                                      				of upgrade appears on the screen along with the login prompt. |
| Step 9 | To verify if
                                          			 the upgrade is successful, run the following CLI commands: show cuc
                                                   					 version: Displays the version of Unity Connection server in both active and
                                                   					 inactive partitions. The upgraded Unity Connection version is in the inactive
                                                   					 partition. utils
                                                   					 system upgrade status: Displays the status of the upgrade that you performed.
                                                   					 This command should display the message for successful upgrade along with the
                                                   					 upgraded version. |

| Caution | If you
                                                      				loose your connection with the remote server or close your browser during this
                                                      				step, you may see the following warning when you try to view the Software
                                                      				Installation/Upgrade page again: |
|---|---|

| Warning | Another
                                                      				session is installing software, click Assume Control to take over the
                                                      				installation. To continue monitoring the upgrade, select Assume Control. |
|---|---|

| Note | During the
                                                      				initial phase of upgrade, the Installation Log text box in Cisco Unified
                                                      				Operating System Administration is updated with the information on the progress
                                                      				of the upgrade. To confirm the completion of upgrade, open the console of the
                                                      				Unity Connection server and make sure that a message indicating the completion
                                                      				of upgrade appears on the screen along with the login prompt. |
|---|---|

| Step 1 | In Cisco Unified Operating System
                                       			 Administration, expand Settings and select Version. |
|---|---|
| Step 2 | On the Version Settings page, select Switch
                                       			 Versions to start the following activities: Unity Connection SRSV services are
                                                					 stopped. Data from the active partition is copied
                                                					 to the inactive partition. Note that the messages are stored in a common
                                                					 partition, therefore they are not copied. The Unity Connection SRSV server
                                                					 restarts and switches to the newer version. |