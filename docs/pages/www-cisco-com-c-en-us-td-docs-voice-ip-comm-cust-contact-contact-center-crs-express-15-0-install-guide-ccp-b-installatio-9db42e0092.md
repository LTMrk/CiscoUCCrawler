---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-install-guide-ccp-b-installatio-9db42e0092
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/install/guide/ccp_b_installation-and-upgrade-guide-release-150/important_considerations_for_upgrade.html
retrieved_at: 2026-08-16T21:08:51.911006+00:00
---

Cisco Customer Collaboration Platform Installation and Upgrade Guide, Release 15.0

# Cisco Customer Collaboration Platform Installation and Upgrade Guide, Release 15.0

Updated: April 30, 2025

Chapter: Important Considerations for Upgrade

## Chapter: Important Considerations for Upgrade

# Important Considerations for Upgrade

## Upgrade Overview

You can upgrade from CCP Release 12.5(1), 12.5(1) SU1, 12.5(1) SU2, and 12.5(1) SU3 to Release 15.0.

Before you begin upgrade, you must install the upgrade Cisco Options Package (COP) file and then upgrade Customer Collaboration Platform using the Software Upgrades menu option in Unified OS Administration or by using the CLI.

The upgrade runs unattended and may take over two hours.

During the upgrade, multiple reboots occur. After the upgrade is complete, the system boots from the lower version. You can
                              defer the switch to new version to a maintenance window or you can perform it immediately. To switch to the higher version,
                              you need to trigger Switch Version either from the Unified OS Administration or from the CLI.

### COP File for Upgrade

The following table lists the Customer Collaboration Platform version and the corresponding COP file that you have to download and install before you begin the upgrade. The COP files
                              for a specific release version can be downloaded from the location, Download Software by browsing to the specific version of Unified Contact Center Express.

Version

COP File

From Customer Collaboration Platform Release 12.5(1) SU3

ciscoccp.1501.PREUPGRADE-ApacheSolandraMigration.170.cop.sgn

From Customer Collaboration Platform Release 12.5(1) SU2

ciscoccp.keymanagement.v02.cop.sgn

ciscoccp.1501.PREUPGRADE-ApacheSolandraMigration.170.cop.sgn

From Customer Collaboration Platform Release 12.5(1) SU1

ciscoccp.keymanagement.v02.cop.sgn

ciscoccp.1501.PREUPGRADE-ApacheSolandraMigration.170.cop.sgn

From Customer Collaboration Platform Release 12.5(1)

ciscoccp.keymanagement.v01.cop.sgn

ciscoccp.1501.PREUPGRADE-ApacheSolandraMigration.170.cop.sgn

## Upgrade Tasks

The following table lists the required tasks to upgrade Customer Collaboration Platform :

Upgrade Path

Tasks

12.5(1), 12.5(1) SU1, 12.5(1) SU2 and 12.5(1) SU3 to 15.0

### Update Virtual
                           	 Machine Settings

Before you perform a upgrade, you must modify Customer Collaboration Platform Virtual Machine's operating system version, total video memory.

Step 1

Power off the
                                          			 virtual machine.

Step 2

Change the operating system version to Other Linux (64-bit) . Perform the following steps to change the operating system of the virtual machine:

Right click on the virtual machine and then choose Edit Settings .

The Virtual Machine Properties window appears.

In the VM Options tab, select General Options and choose Other Linux (64-bit) from the Version drop-down list.

Click OK .

Step 3

Increase the
                                          			 total video memory to 8 MB. Perform the following steps to increase the total
                                          			 video memory:

Right
                                                				  click on the virtual machine and then choose Edit
                                                      						Settings .

The Virtual Machine Properties window appears.

In the Virtual Hardware tab, select Video card .

In the Specify custom settings , set Total video memory to 8 MB and then click OK .

Step 4

Set the RAM memory for large and small deployment. Perform the following steps to set the RAM memory of the virtual machine:

Right click on the virtual machine and then choose Edit Settings .

The Virtual Machine Properties window appears.

In the Virtual Hardware tab, select Memory and enter 10 GB for small deployments and 14 GB for large deployments and then click OK .

Step 5

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

Step 1

Go to Download Software .

Step 2

Choose the required current version of the file from the list and download the COP file to a local source or an SFTP server
                                          that can be accessed by the Cisco Customer Collaboration Platform server.

Step 3

Apply the
                                          			 file using the procedure Upgrade Customer Collaboration Platform Using the CLI .

Step 4

Enter the
                                          			 command utils
                                             				system restart to restart the server.

### Upgrade Customer Collaboration Platform Using Cisco Unified OS Administration

You can upgrade Customer Collaboration Platform either from a local DVD or from a FTP/SFTP server.

By default, access to Customer Collaboration Platform administration user interface is restricted. Administrator can provide access by including clients IP addresses in the allowed
                                             list. For information about how to provide access, see Control Customer Collaboration Platform Application Access

Step 1

Open Unified OS Administration from the Administration tab > Platform Administration or access the URL https://<servername>/cmplatform , where <servername> is the hostname or IP address of your Customer Collaboration Platform server.

Step 2

Log in to Cisco
                                             				Unified OS Administration using administrator username and password.

Step 3

Choose Software
                                                				  Upgrades > Install/Upgrade .

Step 4

From the Source list, choose either DVD or Remote
                                             				Filesystem .

Step 5

Enter the path
                                          			 of the upgrade file in the Directory field.

For DVD , enter "/" in the filepath.

For Remote Filesystem , enter the full path to the file
                                             				that is located on the remote server.

Step 6

If you chose Remote
                                             				Filesystem , follow the instructions on the screen; otherwise, go to Step 7 .

Step 7

Click Next to see the list of upgrades that are available.

Step 8

Choose the
                                          			 appropriate upgrade file, and click Next .

Step 9

(Optional) To
                                          			 use the Email Notification feature, enter relevant information in the Email
                                             				Destination and SMTP
                                             				server fields.

Step 10

Click Next to initiate the upgrade process.

After upgrading Customer Collaboration Platform , the CAs that are not approved by Cisco are removed from the platform trust store. However, you can add them back, if necessary.

For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle in https://www.cisco.com/security/pki

For information about adding a certificate, see the To Upload the Certificates and After You Upload the Certificates sections in Cisco Customer Collaboration Platform User Guide Release 11.6(2) located at: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/socialminer/socialminer_1162/user_guide/Guide/cusm_b_cisco-socialminer-user-guide-release_1162.pdf

### Upgrade Customer Collaboration Platform Using the CLI

Step 1

Log in to
                                          			 platform application CLI using the administrator username and password.

Step 2

Enter the
                                          			 command show
                                             				version active and check the current version.

Step 3

Enter the
                                          			 command utils
                                             				system upgrade initiate to initiate the upgrade process.

Step 4

From the Source list, choose either DVD or Remote Filesystem .

Step 5

Enter the
                                          			 path of the upgrade file in the Directory field.

For DVD , enter "/" in the filepath.

For Remote Filesystem , enter the full path to the file
                                             				that is located on the remote server.

Step 6

Follow the
                                          			 instructions on the screen.

Your entries
                                             				are validated and the available files list is displayed.

Step 7

Select the
                                          			 ISO image file or the COP file that you want to apply from the available list,
                                          			 and confirm the installation when you are prompted.

Step 8

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

Caution

Perform
                                                   				  switch version in the same maintenance window to avoid additional downtime.

The time
                                                   				  required for switch version depends on the size of records in the database.

If you switch back from CCP 15.0(1) to any of the previous versions, the chat related information in the Cassandra database,
                                                   that are updated for 15.0(1), will not be synced.

#### Switch Version
                              	 Using the Web Interface

To check and
                                    		  perform switch version using the web interface, follow this procedure:

Step 1

Log in to Cisco
                                                				Unified OS Administration using the administrator username and
                                             			 password.

Step 2

Choose Settings > Version to check the versions.

Step 3

Click Switch
                                                				Versions , and click OK to initiate the switch version process.

Step 4

Choose Settings > Version to check the active version.

#### Switch Version
                              	 Using the CLI

To check and
                                    		  perform switch version using the CLI, follow this procedure:

Step 1

Log in to
                                             			 Cisco Unified Communications OS Platform CLI using the administrator username
                                             			 and password.

Step 2

Enter the
                                             			 command show
                                                				version active to check the active version.

Step 3

Enter the
                                             			 command show
                                                				version inactive to check the inactive version.

Step 4

Enter the
                                             			 command utils
                                                				system switch-version to initiate the switch version process.

Step 5

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

Step 1

Log in to Cisco
                                                				Unified OS Administration using the administrator username and
                                             			 password.

Step 2

Choose Settings > Version to check the current active
                                             			 and inactive versions.

#### Verify Version
                              	 Using the CLI

Step 1

Log in to
                                             			 application platform CLI using the administrator username and password.

Step 2

Enter the
                                             			 command show
                                                				version active to check the active version.

Step 3

Enter the
                                             			 command show
                                                				version inactive to check the inactive version.

### Upgrade VMware Tools

#### Before you begin

Before upgrading CCP to 15.0, ensure that the VM type is open-vm-tools. Use the utils vmtools status command to know the type
                                 of vm-tools. Run the utils vmtools switch open command to change the VM type. This command updates the vm-tools and restarts
                                 the VM. After the restart, verify the VM type and then upgrade.

Step 1

Power on the
                                          			 virtual machine.

Step 2

Right
                                          				  click on the virtual machine and then choose Guest > Install / Upgrade VMware tools .

Step 3

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

Step 1

Power off the
                                          			 virtual machine.

Step 2

Right click on
                                          			 the virtual machine and then choose Edit
                                                				  Settings .

Step 3

In the Hardware tab, select Network adapter 1 , and then click Add .

The Add
                                                				  Hardware window appears.

Step 4

Select Ethernet Adapter and then click Next .

The Network Type window appears.

Step 5

Select the
                                          			 adapter type VMXNET3 , click Next , and click Finish .

Step 6

To remove the
                                          			 previous network adapter complete the following steps:

Right
                                                				  click on the virtual machine and then choose Edit
                                                      						Settings .

The Virtual Machine Properties window appears.

In the Hardware tab, select Network adapter 1 , and click Remove .

Click OK .

Step 7

Power on the
                                          			 virtual machine.

| Note | Ensure that Cisco Customer Collaboration Platform OVA template is deployed for a successful upgrade. The upgrade stops if no Cisco Customer Collaboration Platform OVA template is found in the deployment. |
|---|---|

| Note | Before you upgrade, you must perform a DRS backup to ensure that you can revert to the previous version if necessary. |
|---|---|

| Version | COP File |
|---|---|
| From Customer Collaboration Platform Release 12.5(1) SU3 | ciscoccp.1501.PREUPGRADE-ApacheSolandraMigration.170.cop.sgn |
| From Customer Collaboration Platform Release 12.5(1) SU2 | ciscoccp.keymanagement.v02.cop.sgn ciscoccp.1501.PREUPGRADE-ApacheSolandraMigration.170.cop.sgn |
| From Customer Collaboration Platform Release 12.5(1) SU1 | ciscoccp.keymanagement.v02.cop.sgn ciscoccp.1501.PREUPGRADE-ApacheSolandraMigration.170.cop.sgn |
| From Customer Collaboration Platform Release 12.5(1) | ciscoccp.keymanagement.v01.cop.sgn ciscoccp.1501.PREUPGRADE-ApacheSolandraMigration.170.cop.sgn |

| Upgrade Path | Tasks |
|---|---|
| 12.5(1), 12.5(1) SU1, 12.5(1) SU2 and 12.5(1) SU3 to 15.0 |  |

| Step 1 | Power off the
                                          			 virtual machine. |
|---|---|
| Step 2 | Change the operating system version to Other Linux (64-bit) . Perform the following steps to change the operating system of the virtual machine: Right click on the virtual machine and then choose Edit Settings . The Virtual Machine Properties window appears. In the VM Options tab, select General Options and choose Other Linux (64-bit) from the Version drop-down list. Click OK . |
| Step 3 | Increase the
                                          			 total video memory to 8 MB. Perform the following steps to increase the total
                                          			 video memory: Right
                                                				  click on the virtual machine and then choose Edit
                                                      						Settings . The Virtual Machine Properties window appears. In the Virtual Hardware tab, select Video card . In the Specify custom settings , set Total video memory to 8 MB and then click OK . |
| Step 4 | Set the RAM memory for large and small deployment. Perform the following steps to set the RAM memory of the virtual machine: Right click on the virtual machine and then choose Edit Settings . The Virtual Machine Properties window appears. In the Virtual Hardware tab, select Memory and enter 10 GB for small deployments and 14 GB for large deployments and then click OK . |
| Step 5 | Power on the virtual machine and continue with upgrade. Note For a refresh upgrade (RU) of Cisco Customer Collaboration Platform you must initiate the upgrade from the VM console. A confirmation message related to Cisco CCP OVA deployment confirmation is displayed. The Administrator must press Yes to proceed for the refresh upgrade to continue. | Note | For a refresh upgrade (RU) of Cisco Customer Collaboration Platform you must initiate the upgrade from the VM console. A confirmation message related to Cisco CCP OVA deployment confirmation is displayed. The Administrator must press Yes to proceed for the refresh upgrade to continue. |
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

| Step 1 | Go to Download Software . |
|---|---|
| Step 2 | Choose the required current version of the file from the list and download the COP file to a local source or an SFTP server
                                          that can be accessed by the Cisco Customer Collaboration Platform server. |
| Step 3 | Apply the
                                          			 file using the procedure Upgrade Customer Collaboration Platform Using the CLI . |
| Step 4 | Enter the
                                          			 command utils
                                             				system restart to restart the server. |

| Note | By default, access to Customer Collaboration Platform administration user interface is restricted. Administrator can provide access by including clients IP addresses in the allowed
                                             list. For information about how to provide access, see Control Customer Collaboration Platform Application Access |
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
                                                   				  required for switch version depends on the size of records in the database. If you switch back from CCP 15.0(1) to any of the previous versions, the chat related information in the Cassandra database,
                                                   that are updated for 15.0(1), will not be synced. |
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