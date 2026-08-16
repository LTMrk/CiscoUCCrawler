---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-install-guide-uccx-b-1251-f41beff8b4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/install/guide/uccx_b_1251su1install-and-upgrade-guide/uccx_b_1252install-and-upgrade-guide_chapter_0101.html
retrieved_at: 2026-08-16T21:13:36.618931+00:00
---

Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1) SU1

# Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1) SU1

Updated: January 31, 2021

Chapter: Unified CCX Rollback

## Chapter: Unified CCX Rollback

# Unified CCX Rollback

## Important Considerations for Rollback

Caution

Configuration/reporting updates that are made after the upgrade are not be preserved when you roll back.

Do not make any configuration changes during the rollback, because the changes are lost after the rollback.

In an HA setup, do not switch
                                    			 versions on both the first and second nodes at the same time. Perform switch version on the second node only after you
                                    have switched versions on the first node.

## Roll Back Upgrade
                        	 for Single Node Setup

Step 1

Check and Perform Switch
                                          				Version

Step 2

Verify Version of Unified CCX

Step 3

Verify Status of
                                          				Services

Step 4

Roll Back Unified CCX Clients

## Roll Back Upgrade
                        	 for HA Setup

Step 1

Check and
                                          				Perform Switch Version . Perform switch version on the first node.

Step 2

Check and Perform Switch
                                          				Version . Perform switch version on the second node.

Step 3

Verify Version of Unified CCX

Step 4

Verify Status of
                                          				Services

Step 5

Roll Back Unified CCX Clients

Step 6

Reset Database Replication after Rollback

Step 7

Verify Unified CCX Database Replication

Step 8

Verify Cisco Database Replication

## Reset Database Replication after Rollback

If you roll back to an older version of Unified CCX, you must manually reset database replication within the
                              		  cluster for an HA setup.

Step 1

Log in to Cisco Unified OS Platform CLI using administrator username and password.

Step 2

Enter the command utils uccx dbreplication reset all to reset database replication.

## Roll Back Unified CCX
                        	 Clients

Step 1

Remove the Editor. For more information, refer to the "Removal of the Unified CCX Editor" section in Cisco Unified Contact Center Express Getting Started with Scripts Guide .

Step 2

Uninstall the Cisco Unified Real-Time Monitoring Tool.

Step 3

Remove the Cisco Unified Real-Time Reporting Tool.

Step 4

Log in to Cisco Unified CCX Administration using Unified
                                       			 CCX username and password.

Step 5

Choose Tools > Plug-ins .

Step 6

Click the Cisco Unified CCX Editor Web Launcher hyperlink to download and launch the Unified CCX Editor (.jnlp) file. No installation required.

Before launching the downloaded JNLP file, copy the file to a different location for future use. Ensure to clear the Java
                                          cache before launching the JNLP file.

Step 7

Click Cisco Unified Real-Time Monitoring Tool for
                                          				Windows or Cisco Unified Real-Time Monitoring Tool for
                                          				Linux as required to install Unified RTMT.

Step 8

Click Cisco Unified Real-Time Reporting Tool to launch Unified Real-Time Reporting Tool.

## Impact on Historical Reporting Users After Roll Back

Rolling back versions from a later version of Unified CCX to an earlier version does not retain the privileges  of Historical
                              Report Users that were created in later version. These users will not have access to Historical Reports. After reverting to
                              the earlier version, update the reporting capability for them.

To update the reporting capability:

Step 1

Log in to Cisco Unified CCX Administration using Unified CCX username and password.

Step 2

Choose Tools > User Management > Reporting Capability .

Step 3

Select the users that you want to update.

Step 4

Click Update .

| Caution | Configuration/reporting updates that are made after the upgrade are not be preserved when you roll back. |
|---|---|

| Step 1 | Check and Perform Switch
                                          				Version |
|---|---|
| Step 2 | Verify Version of Unified CCX |
| Step 3 | Verify Status of
                                          				Services |
| Step 4 | Roll Back Unified CCX Clients |

| Step 1 | Check and
                                          				Perform Switch Version . Perform switch version on the first node. |
|---|---|
| Step 2 | Check and Perform Switch
                                          				Version . Perform switch version on the second node. |
| Step 3 | Verify Version of Unified CCX |
| Step 4 | Verify Status of
                                          				Services |
| Step 5 | Roll Back Unified CCX Clients |
| Step 6 | Reset Database Replication after Rollback |
| Step 7 | Verify Unified CCX Database Replication |
| Step 8 | Verify Cisco Database Replication |

| Step 1 | Log in to Cisco Unified OS Platform CLI using administrator username and password. |
|---|---|
| Step 2 | Enter the command utils uccx dbreplication reset all to reset database replication. |

| Step 1 | Remove the Editor. For more information, refer to the "Removal of the Unified CCX Editor" section in Cisco Unified Contact Center Express Getting Started with Scripts Guide . |
|---|---|
| Step 2 | Uninstall the Cisco Unified Real-Time Monitoring Tool. |
| Step 3 | Remove the Cisco Unified Real-Time Reporting Tool. |
| Step 4 | Log in to Cisco Unified CCX Administration using Unified
                                       			 CCX username and password. |
| Step 5 | Choose Tools > Plug-ins . |
| Step 6 | Click the Cisco Unified CCX Editor Web Launcher hyperlink to download and launch the Unified CCX Editor (.jnlp) file. No installation required. Before launching the downloaded JNLP file, copy the file to a different location for future use. Ensure to clear the Java
                                          cache before launching the JNLP file. |
| Step 7 | Click Cisco Unified Real-Time Monitoring Tool for
                                          				Windows or Cisco Unified Real-Time Monitoring Tool for
                                          				Linux as required to install Unified RTMT. |
| Step 8 | Click Cisco Unified Real-Time Reporting Tool to launch Unified Real-Time Reporting Tool. |

| Step 1 | Log in to Cisco Unified CCX Administration using Unified CCX username and password. |
|---|---|
| Step 2 | Choose Tools > User Management > Reporting Capability . |
| Step 3 | Select the users that you want to update. |
| Step 4 | Click Update . |