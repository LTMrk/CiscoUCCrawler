---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-ccp-b-125install--8c519a5e09
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/ccp_b_125install-and-upgrade/ccp_b_125install-and-upgrade_chapter_011.html
retrieved_at: 2026-08-16T21:14:06.015382+00:00
---

Cisco Customer Collaboration Platform Installation and Upgrade Guide Release 12.5(1)

# Cisco Customer Collaboration Platform Installation and Upgrade Guide Release 12.5(1)

Updated: February 7, 2020

Chapter: Important Considerations for Upgrade

## Chapter: Important Considerations for Upgrade

# Important Considerations for Upgrade

Perform a DRS backup before you upgrade.

Upgrade Customer Collaboration Platform during off-peak hours or during a maintenance window to avoid service interruptions.

You can trigger the switch to new version immediately after you complete the upgrade.

You might experience a delay of approximately 10-15 minutes before the services start during the first boot of the Customer Collaboration Platform system after the switch version. This is due to the migration of data during the first boot. This delay will not occur in
                                 subsequent restarts.

You can choose to switch back to the older version at time if the newer version seems unstable or has performance issues.
                                 No data is migrated when you switch to the older version.

## Upgrade Overview

You can upgrade from SocialMiner Release 11.6(2) and 12.0(1) to CCP Release 12.5(1).

Before you begin upgrade, you must install the upgrade Cisco Options Package (COP) file and then upgrade Customer Collaboration Platform using the Software Upgrades menu option in Unified OS Administration or by using the CLI.

The upgrade runs unattended and may take over two hours.

During the upgrade, multiple reboots occur. After the upgrade is complete, the system boots from the lower version. You can
                              defer the switch to new version to a maintenance window or you can perform it immediately. To switch to the higher version,
                              you need to trigger Switch Version either from the Unified OS Administration or from the CLI.

### COP File for Upgrade

The following table lists the Customer Collaboration Platform version and the corresponding COP file that you have to download and install before you begin the upgrade.

Version

COP File

11.6.2.10000-21

12.0.1.10000-14

File Name: ciscosm.refreshupgrade.pre12.5.cop.sgn

MD5 Checksum: 1187e5fc2937ce2bb4253c982f5d1d18

## Upgrade Tasks

The following table lists the required tasks to upgrade Customer Collaboration Platform :

Upgrade Path

Tasks

11.6(2) to 12.5(1)

12.0(1) to 12.5(1)

### Update Virtual
                           	 Machine Settings

Before you perform a upgrade, you must modify Customer Collaboration Platform Virtual Machine's operating system version, total video memory.

Power off the
                                          			 virtual machine.

Change the operating system version to CentOS . Perform the following steps to change the operating system of the virtual machine:

Right click on the virtual machine and then choose Edit Settings .

The Virtual Machine Properties window appears.

In the Options tab, select General Options and choose CentOS from the Version drop-down list.

Click OK .

Increase the
                                          			 total video memory to 8 MB. Perform the following steps to increase the total
                                          			 video memory:

Right
                                                				  click on the virtual machine and then choose Edit
                                                      						Settings .

The Virtual Machine Properties window appears.

In the Hardware tab, select Video card .

In the Specify custom settings , set Total video memory to 8 MB and then click OK .

Power on the virtual machine and continue with upgrade.

### Install COP
                           	 File

The Cisco Options
                                 		  Package (COP) file provides a generic method to deploy Cisco software outside
                                 		  the normal upgrade process. For example, you use a COP file to install new
                                 		  language packs or to patch fixes and virtualization tools. You must first
                                 		  download and save the COP file before applying it.

Unlike
                                             			 upgrades, COP files cannot be removed or rolled back. Contact Cisco TAC if you
                                             			 want to roll back the COP file.

If the ReadMe
                                             			 file for a specific COP file contradicts the following general guidelines,
                                             			 follow the instructions in the ReadMe file.

Go to https://software.cisco.com/download/navigator.html .

Click Log
                                             				In and login by entering username and password.

Choose from the list Products > Customer Collaboration > Options for Contact Center Solutions > CCP .

Click CCP .

Choose the required current version of the file from the list and download the COP file to a local source or an SFTP server
                                          that can be accessed by the Cisco Customer Collaboration Platform server.

Apply the
                                          			 file using the procedure Upgrade Customer Collaboration Platform Using the CLI .

Enter the
                                          			 command utils
                                             				system restart to restart the server.

### Upgrade Customer Collaboration Platform Using Cisco Unified OS Administration

You can upgrade Customer Collaboration Platform either from a local DVD or from a FTP/SFTP server.

By default, access to Customer Collaboration Platform administration user interface is restricted. Administrator can provide access by whitelisting clients IP addresses. For information
                                             about how to provide access, see Control Customer Collaboration Platform Application Access

Open Unified OS Administration from the Administration tab > Platform Administration or access the URL https://<servername>/cmplatform , where <servername> is the hostname or IP address of your Customer Collaboration Platform server.

Log in to Cisco
                                             				Unified OS Administration using administrator username and password.

Choose Software
                                                				  Upgrades > Install/Upgrade .

From the Source list, choose either DVD or Remote
                                             				Filesystem .

Enter the path
                                          			 of the upgrade file in the Directory field.

For DVD , enter "/" in the filepath.

For Remote Filesystem , enter the full path to the file
                                             				that is located on the remote server.

If you chose Remote
                                             				Filesystem , follow the instructions on the screen; otherwise, go to Step 7 .

Click Next to see the list of upgrades that are available.

Choose the
                                          			 appropriate upgrade file, and click Next .

(Optional) To
                                          			 use the Email Notification feature, enter relevant information in the Email
                                             				Destination and SMTP
                                             				server fields.

Click Next to initiate the upgrade process.

After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary.

For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki

For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf

### Upgrade Customer Collaboration Platform Using the CLI

Log in to
                                          			 platform application CLI using the administrator username and password.

Enter the
                                          			 command show
                                             				version active and check the current version.

Enter the
                                          			 command utils
                                             				system upgrade initiate to initiate the upgrade process.

From the Source list, choose either DVD or Remote Filesystem .

Enter the
                                          			 path of the upgrade file in the Directory field.

For DVD , enter "/" in the filepath.

For Remote Filesystem , enter the full path to the file
                                             				that is located on the remote server.

Follow the
                                          			 instructions on the screen.

Your entries
                                             				are validated and the available files list is displayed.

Select the
                                          			 ISO image file or the COP file that you want to apply from the available list,
                                          			 and confirm the installation when you are prompted.

After the
                                          			 installation is completed, enter the command show
                                             				version inactive and check the upgraded version.

After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary.

For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki

For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf

### Verify Version
                           	 after Switch Version

You can check and
                                 		  perform switch version by using either of the following procedures: Switch Version Using the Web Interface or Switch Version Using the CLI .

Perform
                                                   				  switch version in the same maintenance window to avoid additional downtime.

The time
                                                   				  required for switch version depends on the size of records in the database.

#### Switch Version
                              	 Using the Web Interface

To check and
                                    		  perform switch version using the web interface, follow this procedure:

Log in to Cisco
                                                				Unified OS Administration using the administrator username and
                                             			 password.

Choose Settings > Version to check the versions.

Click Switch
                                                				Versions , and click OK to initiate the switch version process.

Choose Settings > Version to check the active version.

#### Switch Version
                              	 Using the CLI

To check and
                                    		  perform switch version using the CLI, follow this procedure:

Log in to
                                             			 Cisco Unified Communications OS Platform CLI using the administrator username
                                             			 and password.

Enter the
                                             			 command show
                                                				version active to check the active version.

Enter the
                                             			 command show
                                                				version inactive to check the inactive version.

Enter the
                                             			 command utils
                                                				system switch-version to initiate the switch version process.

Enter the
                                             			 command show
                                                				version active to check the active version.

If switch
                                                            				  version is unsuccessful, contact Cisco TAC.

### Verify
                           	 Version

#### Verify Version
                              	 Using the Web Interface

To verify the active and inactive versions of Customer Collaboration Platform using the web interface, follow this procedure:

Log in to Cisco
                                                				Unified OS Administration using the administrator username and
                                             			 password.

Choose Settings > Version to check the current active
                                             			 and inactive versions.

#### Verify Version
                              	 Using the CLI

Log in to
                                             			 application platform CLI using the administrator username and password.

Enter the
                                             			 command show
                                                				version active to check the active version.

Enter the
                                             			 command show
                                                				version inactive to check the inactive version.

### Upgrade VMware Tools

Power on the
                                          			 virtual machine.

Right
                                          				  click on the virtual machine and then choose Guest > Install / Upgrade VMware tools .

Choose Automatic Tools Upgrade or Interactive Tools Upgrade and click OK .

If you choose Automatic Tools Upgrade , the process is complete.

If you choose Interactive Tools Upgrade , then complete the following steps:

Log in to platform application CLI using the administrator username and password.

Enter the command utils vmtools refresh .

#### What to do next

Check the Summary tab of the virtual machine and verify that the version of the VMware tools is current.

If the version is not current, reboot the VM and check.

### Change NIC Adapter
                           	 Type

Power off the
                                          			 virtual machine.

Right click on
                                          			 the virtual machine and then choose Edit
                                                				  Settings .

In the Hardware tab, select Network adapter 1 , and then click Add .

The Add
                                                				  Hardware window appears.

Select Ethernet Adapter and then click Next .

The Network Type window appears.

Select the
                                          			 adapter type VMXNET3 , click Next , and click Finish .

To remove the
                                          			 previous network adapter complete the following steps:

Right
                                                				  click on the virtual machine and then choose Edit
                                                      						Settings .

The Virtual Machine Properties window appears.

In the Hardware tab, select Network adapter 1 , and click Remove .

Click OK .

Power on the
                                          			 virtual machine.

| Note | Ensure that Cisco Customer Collaboration Platform OVA template is deployed for a successful upgrade. The upgrade stops if no Cisco Customer Collaboration Platform OVA template is found in the deployment. |
|---|---|

| Note | Before you upgrade, you must perform a DRS backup to ensure that you can revert to the previous version if necessary. |
|---|---|

| Version | COP File |
|---|---|
| 11.6.2.10000-21 12.0.1.10000-14 | File Name: ciscosm.refreshupgrade.pre12.5.cop.sgn MD5 Checksum: 1187e5fc2937ce2bb4253c982f5d1d18 |

| Upgrade Path | Tasks |
|---|---|
| 11.6(2) to 12.5(1) 12.0(1) to 12.5(1) |  |

| Step 1 | Power off the
                                          			 virtual machine. |
|---|---|
| Step 2 | Change the operating system version to CentOS . Perform the following steps to change the operating system of the virtual machine: Right click on the virtual machine and then choose Edit Settings . The Virtual Machine Properties window appears. In the Options tab, select General Options and choose CentOS from the Version drop-down list. Click OK . |
| Step 3 | Increase the
                                          			 total video memory to 8 MB. Perform the following steps to increase the total
                                          			 video memory: Right
                                                				  click on the virtual machine and then choose Edit
                                                      						Settings . The Virtual Machine Properties window appears. In the Hardware tab, select Video card . In the Specify custom settings , set Total video memory to 8 MB and then click OK . |
| Step 4 | Power on the virtual machine and continue with upgrade. Note For a refresh upgrade (RU) of Cisco Customer Collaboration Platform you must initiate the upgrade from the VM console. A confirmation message related to Cisco CCP OVA deployment confirmation is displayed. The Administrator must press Yes to proceed for the refresh upgrade to continue. | Note | For a refresh upgrade (RU) of Cisco Customer Collaboration Platform you must initiate the upgrade from the VM console. A confirmation message related to Cisco CCP OVA deployment confirmation is displayed. The Administrator must press Yes to proceed for the refresh upgrade to continue. |
| Note | For a refresh upgrade (RU) of Cisco Customer Collaboration Platform you must initiate the upgrade from the VM console. A confirmation message related to Cisco CCP OVA deployment confirmation is displayed. The Administrator must press Yes to proceed for the refresh upgrade to continue. |

| Note | For a refresh upgrade (RU) of Cisco Customer Collaboration Platform you must initiate the upgrade from the VM console. A confirmation message related to Cisco CCP OVA deployment confirmation is displayed. The Administrator must press Yes to proceed for the refresh upgrade to continue. |
|---|---|

| Note | Unlike
                                             			 upgrades, COP files cannot be removed or rolled back. Contact Cisco TAC if you
                                             			 want to roll back the COP file. |
|---|---|

| Note | If the ReadMe
                                             			 file for a specific COP file contradicts the following general guidelines,
                                             			 follow the instructions in the ReadMe file. |
|---|---|

| Step 1 | Go to https://software.cisco.com/download/navigator.html . |
|---|---|
| Step 2 | Click Log
                                             				In and login by entering username and password. |
| Step 3 | Choose from the list Products > Customer Collaboration > Options for Contact Center Solutions > CCP . |
| Step 4 | Click CCP . |
| Step 5 | Choose the required current version of the file from the list and download the COP file to a local source or an SFTP server
                                          that can be accessed by the Cisco Customer Collaboration Platform server. |
| Step 6 | Apply the
                                          			 file using the procedure Upgrade Customer Collaboration Platform Using the CLI . |
| Step 7 | Enter the
                                          			 command utils
                                             				system restart to restart the server. |

| Note | By default, access to Customer Collaboration Platform administration user interface is restricted. Administrator can provide access by whitelisting clients IP addresses. For information
                                             about how to provide access, see Control Customer Collaboration Platform Application Access |
|---|---|

| Step 1 | Open Unified OS Administration from the Administration tab > Platform Administration or access the URL https://<servername>/cmplatform , where <servername> is the hostname or IP address of your Customer Collaboration Platform server. |
|---|---|
| Step 2 | Log in to Cisco
                                             				Unified OS Administration using administrator username and password. |
| Step 3 | Choose Software
                                                				  Upgrades > Install/Upgrade . |
| Step 4 | From the Source list, choose either DVD or Remote
                                             				Filesystem . |
| Step 5 | Enter the path
                                          			 of the upgrade file in the Directory field. For DVD , enter "/" in the filepath. For Remote Filesystem , enter the full path to the file
                                             				that is located on the remote server. |
| Step 6 | If you chose Remote
                                             				Filesystem , follow the instructions on the screen; otherwise, go to Step 7 . |
| Step 7 | Click Next to see the list of upgrades that are available. |
| Step 8 | Choose the
                                          			 appropriate upgrade file, and click Next . |
| Step 9 | (Optional) To
                                          			 use the Email Notification feature, enter relevant information in the Email
                                             				Destination and SMTP
                                             				server fields. |
| Step 10 | Click Next to initiate the upgrade process. Note After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf | Note | After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf |
| Note | After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf |

| Note | After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf |
|---|---|

| Step 1 | Log in to
                                          			 platform application CLI using the administrator username and password. |
|---|---|
| Step 2 | Enter the
                                          			 command show
                                             				version active and check the current version. |
| Step 3 | Enter the
                                          			 command utils
                                             				system upgrade initiate to initiate the upgrade process. |
| Step 4 | From the Source list, choose either DVD or Remote Filesystem . |
| Step 5 | Enter the
                                          			 path of the upgrade file in the Directory field. For DVD , enter "/" in the filepath. For Remote Filesystem , enter the full path to the file
                                             				that is located on the remote server. |
| Step 6 | Follow the
                                          			 instructions on the screen. Your entries
                                             				are validated and the available files list is displayed. |
| Step 7 | Select the
                                          			 ISO image file or the COP file that you want to apply from the available list,
                                          			 and confirm the installation when you are prompted. |
| Step 8 | After the
                                          			 installation is completed, enter the command show
                                             				version inactive and check the upgraded version. Note After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf | Note | After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf |
| Note | After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf |

| Note | After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf |
|---|---|

| Caution | Never initiate switch
                                             			 version from the recovery CD. |
|---|---|

| Note | Perform
                                                   				  switch version in the same maintenance window to avoid additional downtime. The time
                                                   				  required for switch version depends on the size of records in the database. |
|---|---|

| Step 1 | Log in to Cisco
                                                				Unified OS Administration using the administrator username and
                                             			 password. |
|---|---|
| Step 2 | Choose Settings > Version to check the versions. |
| Step 3 | Click Switch
                                                				Versions , and click OK to initiate the switch version process. |
| Step 4 | Choose Settings > Version to check the active version. |

| Step 1 | Log in to
                                             			 Cisco Unified Communications OS Platform CLI using the administrator username
                                             			 and password. |
|---|---|
| Step 2 | Enter the
                                             			 command show
                                                				version active to check the active version. |
| Step 3 | Enter the
                                             			 command show
                                                				version inactive to check the inactive version. |
| Step 4 | Enter the
                                             			 command utils
                                                				system switch-version to initiate the switch version process. |
| Step 5 | Enter the
                                             			 command show
                                                				version active to check the active version. Note If switch
                                                            				  version is unsuccessful, contact Cisco TAC. | Note | If switch
                                                            				  version is unsuccessful, contact Cisco TAC. |
| Note | If switch
                                                            				  version is unsuccessful, contact Cisco TAC. |

| Note | If switch
                                                            				  version is unsuccessful, contact Cisco TAC. |
|---|---|

| Step 1 | Log in to Cisco
                                                				Unified OS Administration using the administrator username and
                                             			 password. |
|---|---|
| Step 2 | Choose Settings > Version to check the current active
                                             			 and inactive versions. |

| Step 1 | Log in to
                                             			 application platform CLI using the administrator username and password. |
|---|---|
| Step 2 | Enter the
                                             			 command show
                                                				version active to check the active version. |
| Step 3 | Enter the
                                             			 command show
                                                				version inactive to check the inactive version. |

| Step 1 | Power on the
                                          			 virtual machine. |
|---|---|
| Step 2 | Right
                                          				  click on the virtual machine and then choose Guest > Install / Upgrade VMware tools . The Install/Upgrade Tools window appears. |
| Step 3 | Choose Automatic Tools Upgrade or Interactive Tools Upgrade and click OK . If you choose Automatic Tools Upgrade , the process is complete. If you choose Interactive Tools Upgrade , then complete the following steps: Log in to platform application CLI using the administrator username and password. Enter the command utils vmtools refresh . The server reboots twice. The Summary tab of the virtual machine will display that the WMware tools that are running. |

| Step 1 | Power off the
                                          			 virtual machine. |
|---|---|
| Step 2 | Right click on
                                          			 the virtual machine and then choose Edit
                                                				  Settings . The Virtual Machine Properties window appears. |
| Step 3 | In the Hardware tab, select Network adapter 1 , and then click Add . The Add
                                                				  Hardware window appears. |
| Step 4 | Select Ethernet Adapter and then click Next . The Network Type window appears. |
| Step 5 | Select the
                                          			 adapter type VMXNET3 , click Next , and click Finish . |
| Step 6 | To remove the
                                          			 previous network adapter complete the following steps: Right
                                                				  click on the virtual machine and then choose Edit
                                                      						Settings . The Virtual Machine Properties window appears. In the Hardware tab, select Network adapter 1 , and click Remove . Click OK . |
| Step 7 | Power on the
                                          			 virtual machine. |

| Note | If you choose
                                          		  to perform a switch-back to previous versions after upgrade, you do not need to
                                          		  modify the virtual machine parameters. |
|---|---|