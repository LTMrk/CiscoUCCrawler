---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su3-install-guide-uccx-b-1251-9afcd985ee
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su3/install/guide/uccx_b_1251su3_install-and-upgrade-guide/uccx_m_1251su2_unified-ccx-installation.html
retrieved_at: 2026-08-16T21:11:52.362104+00:00
---

Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1) SU3

# Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1) SU3

Updated: May 8, 2023

Chapter: Unified CCX Installation

## Chapter: Unified CCX Installation

# Unified CCX Installation

## Install Unified
                        	 CCX from Installation DVD

To
                              		  install Unified CCX from an installation DVD, perform the following steps:

Step 1

Boot from the installation DVD.

Step 2

The installer checks the integrity of the DVD before beginning installation. Click Yes to perform a media check.

If the media check fails, create another DVD.

If the media check passes, click OK to proceed with installation.

Step 3

Follow the instructions on the screen. When the Apply Patch window appears, select No to begin the basic installation.

If you want to perform a service upgrade by applying patch, see Service Update During Installation .

Step 4

Follow the instructions on the screen to complete the installation. Use the information from Server Configuration Information for Installation to enter the basic configuration information.

### What to do next

Configure the first node.

If you are installing on the second node, configure the first node and then add the second node.

Starting from Release 12.0(1), DVD support is not available. You can download the ISO files from https://software.cisco.com/download/home/270569179 .

## Add Second
                        	 Node

Configure the IP
                              		  address of the second node on the first node.

If you are using Smart Licensing and have already registered the first node with Cisco SSM , ensure that you have purchased HA license. Else, the product instance will be moved to out-of-compliance state.

Step 1

Log in to the
                                       			 Cisco Unified CCX Administration web interface of the first node.

Step 2

Choose System > Server .

Step 3

Click Add
                                          				New .

Step 4

Enter the IP
                                       			 address or the host name of the second node in the Host
                                          				Name/IP Address field.

When a new Unified CCX node is added , the Customer Collaboration Platform Configurations must be saved again in the Subsystems menu of Cisco Unified Contact Center Express Administration . This enables the change to take effect to re-create all the notifications for email and chat in Customer Collaboration Platform . For more details on this, see the guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

Step 5

Enter the IPv6 Address in IPv6 Address (for dual IPv4/IPv6) field.

Step 6

Enter the MAC
                                       			 address details in the MAC
                                          				Address field.

Step 7

Click ADD .

### What to do next

Install Unified CCX on Second Node

## Install Unified CCX on Second Node

Perform the following steps to install Unified CCX on the second node in the cluster:

Perform this installation during off-peak hours to avoid possible dropped calls during the
                                          				  formation of a cluster.

Step 1

Verify that the first node  is synchronized with an
                                       			 NTP server.

From the CLI on the first node, enter utils ntp
                                                			 status . The output indicates the synchronization state.

If the first node is not synchronized with an NTP server,
                                                            				  installation of the second node fails.

Step 2

Install Unified CCX on the second node using the procedure Install Unified CCX from Installation DVD .  The system checks that the second node connects to the first node during the installation.

If you have configured an SMTP server for the first node, you must configure it for the second node also.

During the installation procedure, when you are prompted to enter the administrator user name and password, enter the administrator
                                                            user name and password that you set up in the first node of Unified CCX. Otherwise, the installation fails.

Caution

After installing Unified CCX on the second node, configure it immediately. Until the second node is configured, do not change
                                                      the security password or enable FIPS 140-2 mode on the first node.

### What to do next

Configure the second node.

## Unattended
                        	 Installation

Unified Communications Answer File Generator generates answer files for unattended installations of Unified CCX 11.6(1) or later. Go to https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html (Cisco Unified Communications Answer File Generator web page) for details on the Answer File Generator.

The
                              		  Answer File Generator supports the following features:

Allows
                                    				simultaneous generation and saving of answer files for unattended installation
                                    				on the publisher node and the subscriber node.

Provides
                                    				syntactical validation of data entries.

Provides
                                    				online help and documentation.

Unattended
                                                				  installation supports only basic installations and not the upgrades.

Use a USB
                                                				  disk that is preformatted to be compatible with Linux 2.6 for the
                                                				  configuration file. This key has a FAT32 format.

### Perform Unattended Installation Using Answer File Generator

Step 1

Go to https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html (Cisco Unified Communications Answer File Generator web page).

Step 2

Save the platformConfig.xml file to a Linux-compatible USB drive.

Step 3

Plug in the USB drive to the server on which you will install Unified CCX.

Step 4

Follow the instructions in Install Unified CCX from Installation DVD .

## Service Update During Installation

Unified CCX Release 12.5(1) SU2 does not support the Service Update (SU) upgrade from the installation disc. To upgrade to
                           Release 12.5(1) SU2, see Preupgrade Tasks .

| Step 1 | Boot from the installation DVD. |
|---|---|
| Step 2 | The installer checks the integrity of the DVD before beginning installation. Click Yes to perform a media check. If the media check fails, create another DVD. If the media check passes, click OK to proceed with installation. |
| Step 3 | Follow the instructions on the screen. When the Apply Patch window appears, select No to begin the basic installation. Note If you want to perform a service upgrade by applying patch, see Service Update During Installation . | Note | If you want to perform a service upgrade by applying patch, see Service Update During Installation . |
| Note | If you want to perform a service upgrade by applying patch, see Service Update During Installation . |
| Step 4 | Follow the instructions on the screen to complete the installation. Use the information from Server Configuration Information for Installation to enter the basic configuration information. |

| Note | If you want to perform a service upgrade by applying patch, see Service Update During Installation . |
|---|---|

| Note | If you are installing on the second node, configure the first node and then add the second node. |
|---|---|

| Note | Starting from Release 12.0(1), DVD support is not available. You can download the ISO files from https://software.cisco.com/download/home/270569179 . |
|---|---|

| Note | If you are using Smart Licensing and have already registered the first node with Cisco SSM , ensure that you have purchased HA license. Else, the product instance will be moved to out-of-compliance state. |
|---|---|

| Step 1 | Log in to the
                                       			 Cisco Unified CCX Administration web interface of the first node. |
|---|---|
| Step 2 | Choose System > Server . |
| Step 3 | Click Add
                                          				New . |
| Step 4 | Enter the IP
                                       			 address or the host name of the second node in the Host
                                          				Name/IP Address field. Note When a new Unified CCX node is added , the Customer Collaboration Platform Configurations must be saved again in the Subsystems menu of Cisco Unified Contact Center Express Administration . This enables the change to take effect to re-create all the notifications for email and chat in Customer Collaboration Platform . For more details on this, see the guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . | Note | When a new Unified CCX node is added , the Customer Collaboration Platform Configurations must be saved again in the Subsystems menu of Cisco Unified Contact Center Express Administration . This enables the change to take effect to re-create all the notifications for email and chat in Customer Collaboration Platform . For more details on this, see the guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . |
| Note | When a new Unified CCX node is added , the Customer Collaboration Platform Configurations must be saved again in the Subsystems menu of Cisco Unified Contact Center Express Administration . This enables the change to take effect to re-create all the notifications for email and chat in Customer Collaboration Platform . For more details on this, see the guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . |
| Step 5 | Enter the IPv6 Address in IPv6 Address (for dual IPv4/IPv6) field. |
| Step 6 | Enter the MAC
                                       			 address details in the MAC
                                          				Address field. |
| Step 7 | Click ADD . |

| Note | When a new Unified CCX node is added , the Customer Collaboration Platform Configurations must be saved again in the Subsystems menu of Cisco Unified Contact Center Express Administration . This enables the change to take effect to re-create all the notifications for email and chat in Customer Collaboration Platform . For more details on this, see the guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . |
|---|---|

| Note | Perform this installation during off-peak hours to avoid possible dropped calls during the
                                          				  formation of a cluster. |
|---|---|

| Step 1 | Verify that the first node  is synchronized with an
                                       			 NTP server. From the CLI on the first node, enter utils ntp
                                                			 status . The output indicates the synchronization state. Note If the first node is not synchronized with an NTP server,
                                                            				  installation of the second node fails. | Note | If the first node is not synchronized with an NTP server,
                                                            				  installation of the second node fails. |
|---|---|---|---|
| Note | If the first node is not synchronized with an NTP server,
                                                            				  installation of the second node fails. |
| Step 2 | Install Unified CCX on the second node using the procedure Install Unified CCX from Installation DVD .  The system checks that the second node connects to the first node during the installation. Note If you have configured an SMTP server for the first node, you must configure it for the second node also. During the installation procedure, when you are prompted to enter the administrator user name and password, enter the administrator
                                                            user name and password that you set up in the first node of Unified CCX. Otherwise, the installation fails. Caution After installing Unified CCX on the second node, configure it immediately. Until the second node is configured, do not change
                                                      the security password or enable FIPS 140-2 mode on the first node. | Note | If you have configured an SMTP server for the first node, you must configure it for the second node also. During the installation procedure, when you are prompted to enter the administrator user name and password, enter the administrator
                                                            user name and password that you set up in the first node of Unified CCX. Otherwise, the installation fails. | Caution | After installing Unified CCX on the second node, configure it immediately. Until the second node is configured, do not change
                                                      the security password or enable FIPS 140-2 mode on the first node. |
| Note | If you have configured an SMTP server for the first node, you must configure it for the second node also. During the installation procedure, when you are prompted to enter the administrator user name and password, enter the administrator
                                                            user name and password that you set up in the first node of Unified CCX. Otherwise, the installation fails. |
| Caution | After installing Unified CCX on the second node, configure it immediately. Until the second node is configured, do not change
                                                      the security password or enable FIPS 140-2 mode on the first node. |

| Note | If the first node is not synchronized with an NTP server,
                                                            				  installation of the second node fails. |
|---|---|

| Note | If you have configured an SMTP server for the first node, you must configure it for the second node also. During the installation procedure, when you are prompted to enter the administrator user name and password, enter the administrator
                                                            user name and password that you set up in the first node of Unified CCX. Otherwise, the installation fails. |
|---|---|

| Caution | After installing Unified CCX on the second node, configure it immediately. Until the second node is configured, do not change
                                                      the security password or enable FIPS 140-2 mode on the first node. |
|---|---|

| Note | Unattended
                                                				  installation supports only basic installations and not the upgrades. Use a USB
                                                				  disk that is preformatted to be compatible with Linux 2.6 for the
                                                				  configuration file. This key has a FAT32 format. |
|---|---|

| Step 1 | Go to https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html (Cisco Unified Communications Answer File Generator web page). |
|---|---|
| Step 2 | Save the platformConfig.xml file to a Linux-compatible USB drive. |
| Step 3 | Plug in the USB drive to the server on which you will install Unified CCX. |
| Step 4 | Follow the instructions in Install Unified CCX from Installation DVD . |