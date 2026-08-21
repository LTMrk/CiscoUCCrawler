---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1261-insta-23dfebf186
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1261/install/guide/cuic_b_install-and-upgrade-guide-1261/cuic_m_preparation-for-cuic-1261.html
retrieved_at: 2026-08-21T16:14:58.736675+00:00
---

Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(1)

# Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(1)

Updated: May 14, 2021

Chapter: Preparation for Unified Intelligence Center

## Chapter: Preparation for Unified Intelligence Center

# Preparation for Unified Intelligence Center

You can perform a fresh installation or upgrade of Unified Intelligence Center on supported virtual machines. Also, you can perform an upgrade from previous versions to 12.6(1), by first upgrading Unified Intelligence Center to 12.5(1) and then to 12.6(1) . For more information, see About Upgrades .

## Install VMware ESXi

Before you begin your Unified Intelligence Center installation, you must install VMware ESXi and configure the virtual server.

Step 1

Refer to Unified Communication Virtualization at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-intelligence-center.html to install, setup, and configure the UCS Hardware.

Step 2

Configure the UCS Network. See UCS Network Configuration at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html for more information.

Step 3

Use the instructions mentioned in the https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-intelligence-center.html to install VMWare ESXi 6.5 and 6.7 (with VMFSv6) on your UCS B-series and C-series server.

Step 4

After ESXi is installed successfully, reboot the server.

## Deploy Unified
                        	 Intelligence Center Open Virtualization Format/Open Virtual Appliance (OVF/OVA)
                        	 Template

Open Virtualization Format/Open Virtual Appliance (OVF/OVA) is an open
                              		  standard for packaging and distributing virtual appliances. Files in this
                              		  format have an extension of .ova. The naming convention for the OVF/OVA
                              		  template is PRODUCT_COMPONENT_USER COUNT_VERSION_VMVER.ova .

The OVF/OVA template defines the configuration of the virtual machine
                              		  hardware. The configuration of a Cisco Unified Communications application
                              		  virtual machine must match a supported virtual machine template. This section
                              		  describes the steps to deploy a Unified Intelligence Center OVF/OVA template on
                              		  the virtual machine.

Step 1

Log in to ESXi using VMWare Vsphere or any other compatible client.

Step 2

Highlight the host or cluster to which you want to deploy the
                                       			 Virtual Machine.

Step 3

Select File > Deploy OVF/OVA
                                             				  Template .

Step 4

Click Deploy from File/Template and specify the name
                                       			 and location of the OVF/OVA file (with a .ova extension)

Alternatively, you can click Deploy from URL and specify the URL of the
                                          				OVF/OVA file.

Step 5

Click Next .

Step 6

Verify the details of the template, and click Next .

Step 7

Specify a name for the Virtual Machine that you are about to create
                                       			 and choose an inventory location on your host.

Step 8

Click Next .

Step 9

Choose the Deployment Configuration Type from the drop-down.

Co-Resident : To deploy options with CUIC, LD and IdS.

Stand-Alone : To deploy option with CUIC only.

Step 10

Click Next .

Step 11

In Disk Format, click Next .

Step 12

Verify the deployment settings, and click Finish .

The virtual machine that you added is listed under the UCS server
                                          				tree in the vSphere Client home page.

## Specify Location
                        	 of Unified Intelligence Center Installable

Step 1

Select the newly added Virtual Machine.

Step 2

From the Inventory menu, select Virtual Machine > Edit
                                             				  Settings .

Step 3

In the Hardware tab, select CD/DVD Drive 1 .

Step 4

Select one of the following options to specify the location where
                                       			 you have the bootable Unified Intelligence Center installer file:

Client Device – If you want to use the
                                             				  CD/DVD drive on the client machine from where you are accessing the virtual
                                             				  machine remotely.

Host Device – If you want to use the
                                             				  CD/DVD drive on the ESXi host machine.

Datastore ISO file – If you want to use
                                             				  the datastore on the virtual machine. Before using this option, ensure that the
                                             				  Bootable iso image of Unified Intelligence Center is copied to the datastore of
                                             				  the ESXi host.

Step 5

Click OK to save and close the Virtual Machine Properties window.

Important: Make sure that you have copied or
                              		  inserted the CD/DVD with the Unified Intelligence Center installable in the
                              		  appropriate location before you proceed with the next step.

## Set Boot
                        	 Order

To set the boot order:

Step 1

From the Inventory menu, select Virtual Machine > Edit
                                             				  Settings .

The Virtual Machine Properties window appears.

Step 2

In the Options tab, select Boot Options .

Step 3

Select Force BIOS Setup .

Step 4

In the BIOS screen, select Boot Options > make the
                                             				  CD/DVD ROM as the first device for bootup .

Step 5

Click Save .

## Install Cisco
                        	 Unified Intelligence Center on Virtual Machine

Step 1

Select the
                                       			 virtual machine and click Power > Power
                                             				  On from the shortcut menu. Alternatively, from the Inventory menu, select Power > Power
                                             				  On .

Step 2

The virtual
                                       			 machine powers on and Unified Intelligence Center installation starts up
                                       			 automatically. Follow the steps mentioned in Installation — All Nodes to complete the Unified Intelligence Center installation.

The answer
                                                   					 file generated by the Answer File Generator (platformConfig.xml) is not
                                                   					 readable from a USB key. The Answer File Generator generates a floppy image
                                                   					 [FLP - virtual floppy] for performing an unattended installation.

USB tape
                                                   					 backup is not supported. Use SFTP instead.

Install
                                                   					 logs are written only to the virtual serial port.

Unattended
                                                   					 installs use virtual floppy instead of USB.

Boot order
                                                   					 is controlled by the BIOS of the VMware VM.

Hardware
                                                   					 BIOS, firmware, and drivers must be the required level and configured for
                                                   					 compatibility with Unified Intelligence Center-supported VMware product and
                                                   					 version.

| Step 1 | Refer to Unified Communication Virtualization at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-intelligence-center.html to install, setup, and configure the UCS Hardware. |
|---|---|
| Step 2 | Configure the UCS Network. See UCS Network Configuration at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html for more information. |
| Step 3 | Use the instructions mentioned in the https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-intelligence-center.html to install VMWare ESXi 6.5 and 6.7 (with VMFSv6) on your UCS B-series and C-series server. |
| Step 4 | After ESXi is installed successfully, reboot the server. |

| Step 1 | Log in to ESXi using VMWare Vsphere or any other compatible client. |
|---|---|
| Step 2 | Highlight the host or cluster to which you want to deploy the
                                       			 Virtual Machine. |
| Step 3 | Select File > Deploy OVF/OVA
                                             				  Template . |
| Step 4 | Click Deploy from File/Template and specify the name
                                       			 and location of the OVF/OVA file (with a .ova extension) Alternatively, you can click Deploy from URL and specify the URL of the
                                          				OVF/OVA file. |
| Step 5 | Click Next . |
| Step 6 | Verify the details of the template, and click Next . |
| Step 7 | Specify a name for the Virtual Machine that you are about to create
                                       			 and choose an inventory location on your host. |
| Step 8 | Click Next . |
| Step 9 | Choose the Deployment Configuration Type from the drop-down. Co-Resident : To deploy options with CUIC, LD and IdS. Stand-Alone : To deploy option with CUIC only. |
| Step 10 | Click Next . |
| Step 11 | In Disk Format, click Next . |
| Step 12 | Verify the deployment settings, and click Finish . The virtual machine that you added is listed under the UCS server
                                          				tree in the vSphere Client home page. |

| Step 1 | Select the newly added Virtual Machine. |
|---|---|
| Step 2 | From the Inventory menu, select Virtual Machine > Edit
                                             				  Settings . |
| Step 3 | In the Hardware tab, select CD/DVD Drive 1 . |
| Step 4 | Select one of the following options to specify the location where
                                       			 you have the bootable Unified Intelligence Center installer file: Client Device – If you want to use the
                                             				  CD/DVD drive on the client machine from where you are accessing the virtual
                                             				  machine remotely. Host Device – If you want to use the
                                             				  CD/DVD drive on the ESXi host machine. Datastore ISO file – If you want to use
                                             				  the datastore on the virtual machine. Before using this option, ensure that the
                                             				  Bootable iso image of Unified Intelligence Center is copied to the datastore of
                                             				  the ESXi host. Note Ensure that you set the boot order by making CD ROM the first device upon power up. For
                                                   				details, refer to Set Boot Order . | Note | Ensure that you set the boot order by making CD ROM the first device upon power up. For
                                                   				details, refer to Set Boot Order . |
| Note | Ensure that you set the boot order by making CD ROM the first device upon power up. For
                                                   				details, refer to Set Boot Order . |
| Step 5 | Click OK to save and close the Virtual Machine Properties window. |

| Note | Ensure that you set the boot order by making CD ROM the first device upon power up. For
                                                   				details, refer to Set Boot Order . |
|---|---|

| Step 1 | From the Inventory menu, select Virtual Machine > Edit
                                             				  Settings . The Virtual Machine Properties window appears. |
|---|---|
| Step 2 | In the Options tab, select Boot Options . |
| Step 3 | Select Force BIOS Setup . Note When you restart the Virtual Machine, you will see the BIOS
                                                   				screen in the VM console tab. | Note | When you restart the Virtual Machine, you will see the BIOS
                                                   				screen in the VM console tab. |
| Note | When you restart the Virtual Machine, you will see the BIOS
                                                   				screen in the VM console tab. |
| Step 4 | In the BIOS screen, select Boot Options > make the
                                             				  CD/DVD ROM as the first device for bootup . |
| Step 5 | Click Save . |

| Note | When you restart the Virtual Machine, you will see the BIOS
                                                   				screen in the VM console tab. |
|---|---|

| Step 1 | Select the
                                       			 virtual machine and click Power > Power
                                             				  On from the shortcut menu. Alternatively, from the Inventory menu, select Power > Power
                                             				  On . |
|---|---|
| Step 2 | The virtual
                                       			 machine powers on and Unified Intelligence Center installation starts up
                                       			 automatically. Follow the steps mentioned in Installation — All Nodes to complete the Unified Intelligence Center installation. When using
                                          				Unified Intelligence Center on the UCS Servers, note the following: The answer
                                                   					 file generated by the Answer File Generator (platformConfig.xml) is not
                                                   					 readable from a USB key. The Answer File Generator generates a floppy image
                                                   					 [FLP - virtual floppy] for performing an unattended installation. USB tape
                                                   					 backup is not supported. Use SFTP instead. Install
                                                   					 logs are written only to the virtual serial port. Unattended
                                                   					 installs use virtual floppy instead of USB. Boot order
                                                   					 is controlled by the BIOS of the VMware VM. Hardware
                                                   					 BIOS, firmware, and drivers must be the required level and configured for
                                                   					 compatibility with Unified Intelligence Center-supported VMware product and
                                                   					 version. Note vSphere
                                                   				provides you with a console that you can use to provide inputs during the
                                                   				installation. To open the console, select the virtual machine from the vSphere
                                                   				home page and click Open
                                                      				  Console from the shortcut menu. Alternatively, select the virtual
                                                   				machine and click the Console tab in the right pane of the vSphere home page. Pointing and clicking anywhere in
                                                   				the console window will allow you to enter data in the console. Once you start
                                                   				working on the console, the mouse is locked and you can no longer use it. Use Tab key to navigate and use the Enter button to commit the values you entered. To
                                                   				release the mouse from the console window, press Ctrl
                                                      				  + Alt . | Note | vSphere
                                                   				provides you with a console that you can use to provide inputs during the
                                                   				installation. To open the console, select the virtual machine from the vSphere
                                                   				home page and click Open
                                                      				  Console from the shortcut menu. Alternatively, select the virtual
                                                   				machine and click the Console tab in the right pane of the vSphere home page. Pointing and clicking anywhere in
                                                   				the console window will allow you to enter data in the console. Once you start
                                                   				working on the console, the mouse is locked and you can no longer use it. Use Tab key to navigate and use the Enter button to commit the values you entered. To
                                                   				release the mouse from the console window, press Ctrl
                                                      				  + Alt . |
| Note | vSphere
                                                   				provides you with a console that you can use to provide inputs during the
                                                   				installation. To open the console, select the virtual machine from the vSphere
                                                   				home page and click Open
                                                      				  Console from the shortcut menu. Alternatively, select the virtual
                                                   				machine and click the Console tab in the right pane of the vSphere home page. Pointing and clicking anywhere in
                                                   				the console window will allow you to enter data in the console. Once you start
                                                   				working on the console, the mouse is locked and you can no longer use it. Use Tab key to navigate and use the Enter button to commit the values you entered. To
                                                   				release the mouse from the console window, press Ctrl
                                                      				  + Alt . |

| Note | vSphere
                                                   				provides you with a console that you can use to provide inputs during the
                                                   				installation. To open the console, select the virtual machine from the vSphere
                                                   				home page and click Open
                                                      				  Console from the shortcut menu. Alternatively, select the virtual
                                                   				machine and click the Console tab in the right pane of the vSphere home page. Pointing and clicking anywhere in
                                                   				the console window will allow you to enter data in the console. Once you start
                                                   				working on the console, the mouse is locked and you can no longer use it. Use Tab key to navigate and use the Enter button to commit the values you entered. To
                                                   				release the mouse from the console window, press Ctrl
                                                      				  + Alt . |
|---|---|