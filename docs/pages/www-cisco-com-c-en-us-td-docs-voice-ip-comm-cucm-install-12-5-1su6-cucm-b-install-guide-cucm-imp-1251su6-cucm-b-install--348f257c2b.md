---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-install-12-5-1su6-cucm-b-install-guide-cucm-imp-1251su6-cucm-b-install--348f257c2b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/install/12_5_1SU6/cucm_b_install-guide-cucm-imp-1251su6/cucm_b_install-guide-cucm-imp-14_chapter_0100.html
retrieved_at: 2026-08-17T00:07:40.049417+00:00
---

Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU6

# Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU6

Updated: January 17, 2025

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Network Errors
                        	 During Installation

During the
                              		  installation process, the installation program verifies that the server can
                              		  successfully connect to the network by using the network configuration that you
                              		  enter. If it cannot connect, a message displays, and you get prompted to select
                              		  one of the following options:

—RETRY - The installation program tries to validate networking again. If validation fails again, the error dialog box displays
                                    again.

—REVIEW (Check Install) - This option allows you to review and modify the networking configuration. When detected, the installation
                                    program returns to the network configuration windows.

Networking gets validated after you complete each networking window, so the message might display multiple times.

—HALT - The installation halts. You should use the Recovery CD to recover the logs to access the diagnostic information. For
                                    more details, see Obtain and Run Recovery Software on the CUCM VM .

—IGNORE - The installation continues. The networking error gets logged. Sometimes, the installation program validates networking
                                    multiple times, so this error dialog box might display multiple times. If you choose to ignore network errors, the installation
                                    may fail.

### Steps to Recover Logs using Recovery CD

You should use the Recovery CD to recover the logs to access the diagnostic information. Follow the steps mentioned:

Insert the recovery CD.

Reboot the system.

Once the recovery CD menu comes up, press Alt + F2 to get to the command prompt.

Find the largest partition by performing a "df -h". (/mnt/part6).

Locate the install logs at: /mnt/part6/log/install/ directory.

Collect the logs.

## Failed Installations

If your installation fails, check the configuration and confirm the following:

Parse the passwords from the platformconfig.xml file to verify security password.

Complete a packet capture from Unified Communications Manager to confirm that the IM and Presence Service IP address is reaching
                                    Unified Communications Manager during the install.

Verify that NTP is synchronized on Unified Communications Manager.

If you get a message that install has failed and you want to recover the logs to access the diagnostic information, see Obtain and Run Recovery Software on the CUCM VM .

Confirm that the version of the IM and Presence Service and Unified Communications Manager are compatible.

If you are installing a subscriber, verify that the subscriber node is the same version as the publisher node. The subscriber
                                    OVA should be the same OVA that is used for the publisher.

## Unrecoverable IM
                        	 and Presence Service Node

If a node is in a
                              		  state that cannot be recovered you must reinstall the node.

### IM and
                              		  Presence Service Database Publisher Node

Complete the following high-level procedure to reinstall an IM and Presence Service database publisher node.

Power down all the IM and Presence Service subscriber nodes.

Delete the subscriber nodes as follows:

Unassign all users that are assigned to each of the IM and Presence Service subscriber nodes. (Select Cisco Unified CM Administration > User Management > Assign Presence Users ).

Remove the subscriber nodes from their presence redundancy groups. (Select Cisco Unified CM Administration > System > Presence Redundancy Groups ).

Delete the subscriber nodes from the Unified Communications Manager server list. (Select Cisco Unified CM Administration > System > Server ).

Power down the IM and Presence Service database publisher node.

Delete the IM and Presence Service database publisher node as follows:

Unassign the users that are assigned to the IM and Presence Service database publisher node. (Select Cisco Unified CM Administration > User Management > Assign Presence Users ).

Remove the node from the presence redundancy group. (Select Cisco Unified CM Administration > System > Presence Redundancy Groups ).

Delete the IM and Presence Service database publisher node from the Unified Communications Manager server list. (Select Cisco Unified CM Administration > System > Server ).

Readd the IM and Presence Service database publisher node to the Unified Communications Manager server list.

Perform a fresh install of the IM and Presence Service database publisher node.

Readd the IM and Presence Service subscriber nodes to the Unified Communications Manager server list.

Perform a fresh install of each subscriber node.

### IM and
                              		  Presence Service Subscriber Node

Complete the following high-level procedure to reinstall an IM and Presence Service subscriber node.

Power down the IM and Presence Service node.

Delete the subscriber node as follows:

Unassign the users that are assigned to the node. (Select Cisco Unified CM Administration > User Management > Assign Presence Users ).

Remove the node from the presence redundancy group. (Select Cisco Unified CM Administration > System > Presence Redundancy Groups ).

Delete the node from the Unified Communications Manager server list. (Select Cisco Unified CM Administration > System > Server )

Readd the IM and Presence Service node to the Unified Communications Manager server list.

Perform a fresh install of the node.

| Note | We no longer support the collection of logs by dumping them to serial port due to CentOS limitations. |
|---|---|

| Note | We no longer support the collection of logs by dumping them to serial port due to CentOS limitations. |
|---|---|

| Note | If you
                                       		  reinstall a node in an intercluster deployment, you must delete and re-add the
                                       		  intercluster peer connections between the reinstalled node and the other nodes
                                       		  in the cluster. |
|---|---|

| Note | If you do not complete all of these steps in the order shown, recovery of the IM and Presence Service database publisher node will fail. |
|---|---|

| Note | If you do not complete all of these steps in the order shown, recovery of the IM and Presence Service subscriber node will fail. |
|---|---|