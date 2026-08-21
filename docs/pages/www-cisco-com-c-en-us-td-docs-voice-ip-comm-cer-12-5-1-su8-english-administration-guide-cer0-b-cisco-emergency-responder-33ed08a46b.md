---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1-su8-english-administration-guide-cer0-b-cisco-emergency-responder-33ed08a46b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1_su8/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251su8/cer0_b_cisco-emergency-responder-administration-guide-1251su3_chapter_010.html
retrieved_at: 2026-08-21T15:29:26.803604+00:00
---

Cisco Emergency Responder Administration Guide, Release 12.5(1)SU8b-SU9

# Cisco Emergency Responder Administration Guide, Release 12.5(1)SU8b-SU9

Updated: July 23, 2024

Chapter: Cisco Emergency Responder Installation

## Chapter: Cisco Emergency Responder Installation

# Cisco Emergency Responder Installation

## Cisco Emergency
                        	 Responder Installation Overview

Cisco Emergency Responder (Emergency Responder) is distributed on an installation DVD that contains everything that is required
                           to install Emergency Responder, including the Cisco Unified Communications Operating System software.

## Hardware and
                        	 Software Prerequisites

Cisco
                           		Emergency Responder requires specific hardware and software to run properly.
                           		Review the following sections before you proceed with an installation or
                           		upgrade:

See the latest
                                 			 version of the Release Notes for Cisco Emergency Responder to verify that you
                                 			 have all the hardware and software, and in the supported versions, that you
                                 			 must install for Emergency Responder and to check that your
                                 			 CiscoUnifiedCommunicationsManager Appliance platform provides the Emergency
                                 			 Responder capabilities to meet your configuration needs. (You can also use
                                 			 equivalent Cisco-certified servers.)

See the License
                                 			 Requirements section to make sure that you have all the required license keys
                                 			 available before you begin the installation process.

## System Preparations

The Emergency
                           		Responder installation process installs both the platform software and the
                           		Emergency Responder software. During the installation, you are prompted to
                           		enter information needed by the system to complete the installation.

We recommend that
                                       		  you perform the installation or upgrade during off-peak hours. The installation
                                       		  or upgrade procedure completely reformats the hard disk, so Emergency Responder
                                       		  is unavailable for the duration of the installation or upgrade.

Review the
                           		following information before you install Cisco Emergency Responder or upgrade
                           		your system to the latest version:

Upgrading
                                 			 Emergency Responder

Before you upgrade to the latest version of Emergency Responder, you must ensure that it is compatible with your existing
                                       version of Unified CM.

You must
                                       				  upgrade Emergency Responder before you upgrade Unified CM. Only after you have
                                       				  installed the new version of Emergency Responder can you then upgrade Unified
                                       				  CM.

After you have
                                       				  upgraded both Emergency Responder and Unified CM, you must then update the
                                       				  Unified CM Version on Emergency Responder.

See Table 1 for the correct upgrade order and additional information about this subject.

If you have different security passwords in the active and inactive versions, and when you switch back to a lower version,
                                       ensure that you change the security password in the lower version to be same as the higher version. Follow these steps to
                                       change the security password:

Switch the publisher node to a lower version.

Change the security password of the publisher node to the new password which is same as the higher

version.

Switch the subscriber to a lower version.

Change the security password of the subscriber node to the new password which is same as the higher version.

Emergency
                                 			 Responder Versions

Different
                                       				  versions of Emergency Responder cannot be deployed in the same Emergency
                                       				  Responder group. The primary and the standby Emergency Responder servers must
                                       				  be running the same version of Emergency Responder. If you are upgrading to the
                                       				  most recent version of Emergency Responder, also make sure to upgrade both
                                       				  Emergency Responder servers.

Determine and list
                                 			 your Emergency Responder hostname and passwords.

Decide on a
                                       				  permanent hostname, user interface administrator name, and password for the
                                       				  Emergency Responder server before you install Emergency Responder. Changing the
                                       				  hostname of an Emergency Responder server after installation may cause
                                       				  problems.

The hostname
                                       				  for the Emergency Responder Publisher and Subscriber must not contain the
                                       				  underscore character (_). If you have an existing Emergency Responder server
                                       				  with an underscore in its hostname, change the hostname of the server before
                                       				  installing Emergency Responder.

The hostname
                                       				  for the Emergency Responder Publisher and Subscriber can begin with a numeric
                                       				  value.

Decide on a
                                       				  password for the Cisco Emergency Responder administrative user.

The
                                                   					 Emergency Responder administrative users password must be at least six
                                                   					 characters long and can contain alphanumeric characters, hyphens, and
                                                   					 underscores. It must start with an alphanumeric character.

Ethernet NIC speed
                                 			 and duplex mode:

Decide if you
                                       				  want to enable auto-negotiation of Ethernet NIC speed and duplex.

If yes, you do
                                       				  not need any additional information.

If no,
                                       				  determine what Ethernet NIC speed and duplex mode you will use.

DHCP Configuration

Decide if you want to use the Dynamic Host Configuration Protocol (DHCP) to allocate IP addresses.

If yes, you do
                                       				  not need any additional information.

If no, you
                                       				  need the hostname, IP address, IP mask, and gateway address to enter for the
                                       				  Static Network Configuration.

NTP Client
                                 			 information

The system prompts you to set up external Network Time Protocol (NTP) servers. We recommend that you use external NTP servers
                                       to ensure that the system time is accurate.

If you decide
                                       				  to use external NTP servers, you must enter the IP address or hostname of the
                                       				  servers.

If you do not
                                       				  choose to use external NTP servers, you must enter the system date and time
                                       				  clock information manually.

Use of NTP server is
                                       		  mandatory when installing Emergency Responder on UCS servers.

To avoid upgrade failures due to time sync issues with VM, disable the VM's NTP sync with the ESXi host using the workaround
                                       mentioned in the following link: https://knowledge.broadcom.com/external/article?legacyId=1189 .

Database Access
                                 			 Security password

The system
                                       				  requires a database access security password to allow the nodes in a server
                                       				  group to communicate. The password is shared with all nodes in the server
                                       				  group.

The password
                                       				  must be at least six characters long and can contain alphanumeric characters,
                                       				  hyphens, and underscores. It must start with an alphanumeric character.

SMTP host
                                 			 configuration (optional)

Decide if you
                                       				  want to use an SMTP host.

If yes,
                                       				  determine the hostname or IP address of the SMTP host.

Caveats

Review the latest Release Notes for Emergency Responder before installation.

Perform the
                           		installation tasks in the order shown in this table.

Installation Task

For
                                       				More Information

Upgrade Emergency Responder

Software Upgrades

Upgrade Unified CM

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

Change Cisco Unified Communications Manager Version

Update Unified CM Version

Update Cisco Unified Communications Manager Version

Install the components
                           	 for Emergency Responder in the order shown in this table.

Installation Task

For
                                       				More Information

Install Cisco Unified Communications Manager

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

Install Emergency Responder as a new installation

Installation on a New System

## Installation and Migration on the Cisco UCS Server

The
                           		information in the following sections describe the changes for installation,
                           		upgrade, and migration of the Cisco Emergency Responder on the Cisco UCS
                           		Server.

### System
                           	 Requirements

To run
                                 		  Cisco Emergency Responder on the Cisco UCS Server, your system must meet the
                                 		  requirements listed in the following table.

System Parameter

System Parameter options

Supported Virtual Machine Configuration

See
                                             					 the documentation at

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-emergency-responder.html

IOPS per virtual machine (VM)

See
                                             					 the documentation at

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-emergency-responder.html

VMware version

ESXi 4.0 Update 1

VMware—vMotion

No

VMware—Site Recovery Manager

Yes

VMware—High Availability

Yes

VMware—Data Recovery (VDR)

Yes

All other unlisted VMware features

Not supported

To operate
                                 		  Cisco Emergency Responder on the Cisco UCS Server successfully, you should have
                                 		  the experience and skills to manage a host server running VMware ESXi. If you
                                 		  do not have this experience and want to obtain the required information
                                 		  quickly, consider using VMware GO, a Web-based application that facilitates
                                 		  VMware.

### Installation on Cisco UCS Server

### Configuration
                           	 Checklist for Installing and Configuring the Server

The
                                 		  following procedure provides the major steps required to install and configure
                                 		  Cisco Emergency Responder on the Cisco UCS Server.

Step 1

Prepare to
                                          			 install the server.

Step 2

Physically
                                          			 install and connect the server.

Step 3

Power on the
                                          			 server and configure Cisco Integrated Management Controller (CIMC) for remote
                                          			 management.

Step 4

If you purchased
                                          			 the UCS server separately, configure the RAID settings to the following
                                          			 specification:

- The first two drives are
                                             				configured as a RAID 1 (mirrored) drive. This drive is for ESXi installation.

Number of
                                                            					 drives may be different in different versions of UCS servers.

Step 5

If you purchased
                                          			 the UCS server separately, configure the BIOS to the following specification:

- Disable Quiet Mode.

- Enable Enhanced SATA for
                                             				CDROM access.

SATA5:Optiarc DVD first

PCI Raid
                                                      						Adapter second

Step 6

Install and
                                          			 configure VMware EXSi on the smaller of the two available disks.

Step 7

Install vSphere
                                          			 Client.

Step 8

Align the
                                          			 datastores for the VMs.

Step 9

If you use
                                          			 802.1q trunking, set the MTU size to 1472.

Step 10

Install and
                                          			 configure a virtual machine (VM).

Step 11

Install Cisco
                                          			 Emergency Responder on the VM.

### Install
                           	 Preparations

This section
                              		describes how to prepare to install a Cisco Emergency Responder on the Cisco
                              		UCS server in a standalone configuration, which indicates that it is not in a
                              		data center.

Allocate the
                              		following resources before installation:

Space in a rack to
                                    			 receive a 2-RU UCS server

Ethernet ports on
                                    			 a switch close to the UCS server:

One port for
                                          				  the CIMC

Two ports for
                                          				  the LAN on motherboard (LOM) NICs

An IP address for
                                    			 the CIMC management port

An IP address for
                                    			 the virtual host. The UCS server's IP address and is used by ESXi.

A hostname, and
                                    			 optionally configured DNS for the virtual host's hostname

IP addresses for
                                    			 the VMs

### Set Up RAID

If you
                                 		  purchased the UCS server separately, configure the RAID settings to the
                                 		  following specifications:

- The first two drives are
                                    			 configured as a RAID 1 (mirrored) drive. This drive is for ESXi installation.

- The next four drives are
                                    			 configured as a RAID 5 drive. This drive is for VMs.

Number of drives
                                             			 may be different in different versions of UCS servers.

Step 1

During server
                                          			 bootup, press Ctrl+Y to
                                          			 enter the preboot CLI.

Step 2

Enter the
                                          			 following commands to determine the current RAID configuration:

-ldinfo -l0 -a0

-ldinfo -l1 -a0

The required
                                             				configuration is two drives in a RAID 1 array for logical drive 0, and four
                                             				drives in a RAID 5 array for Logical drive 1. If the RAID configuration is
                                             				wrong, continue with this procedure.

Do not
                                                         				  continue with this procedure if RAID is configured correctly.

Step 3

Enter the
                                          			 command -cfgclr -a0 to clear the RAID configuration.

Caution

Clearing the
                                                         				  RAID configuration deletes all data on the hard drives.

Step 4

Enter the
                                          			 following commands to configure RAID:

-cfgldadd -r1 [252:0, 252:1]
                                                				  -a0

-cfgldadd -r5 [252:2, 252:3,
                                                				  252:4, 252:5] -a0

If the hard
                                             				drives did not have a RAID configuration previously, you are done configuring
                                             				RAID. If the hard drives had a RAID configuration before, continue with this
                                             				procedure.

Step 5

Enter the
                                          			 following commands to initialize the logical volumes:

- ldinit -start -full -l0
                                                				  -a0 (l0 is the letter l and the number 0, not the number 10)

- ldinit -start -full -l1
                                                				  -a0 (l1 is the letter l and the number 1, not the number 11)

These commands
                                             				clear data on the drives and initialize the new array.

Step 6

Allow these
                                          			 commands to finish running before exiting the Preboot CLI. Enter the following
                                          			 commands

to display the
                                             				progress of the commands:

-ldinit -showprog -l0 -a0

-ldinit -showprog -l1 -a0

When both
                                             				commands report that no initialization is running, it is safe to quit the
                                             				Preboot CLI.

Step 7

After
                                          			 configuring the two logical volumes, you can exit the Preboot CLI by entering q .

### vSphere Client
                           	 Installation

When the
                              		virtual host is available on the network, you can browse to its IP address to
                              		bring up a web-based interface. The vSphere Client is Windows-based, so the
                              		download and install must be performed from a Windows PC.

After the
                              		vSphere Client is installed, you can run it and log into the virtual host using
                              		the virtual host's name or IP address, the root login ID, and the password you
                              		configured.

You can join
                              		the host to a vCenter if you want to manage it through vCenter.

### Aligning the Datastore Used for VMs

When you
                              		install VMware ESXi, the second logical volume is automatically imported
                              		unaligned. VMs have better disk performance when all partitions (physical,
                              		ESXi, and VM) start on the same boundary and you will have fewer incidents of
                              		disk blocks being fragmented across the different boundaries.

To ensure
                              		that the ESXi partition used for VMs are aligned, delete the unaligned
                              		datastore (the larger disk partition, which is 407 GB), then recreate the
                              		datastore using vSphere client.

### Create Virtual
                           	 Machines

Cisco
                                 		  provides a VM template for you to download and transfer to your virtual host.
                                 		  Use this template to create the VM for Cisco Emergency Responder on the Cisco
                                 		  UCS Server installation.

Before you
                                 		  deploy the template and create the VM, you should have a hostname and IP
                                 		  address allocated for the new VM.

To create
                                 		  a VM and prepare to install Cisco Emergency Responder on the Cisco UCS Server,
                                 		  follow these steps.

Step 1

Download the VM
                                          			 template for your application.

See Download Virtual Machine Templates (OVA Templates) for more information.

Step 2

Upload the
                                          			 template to a datastore on the UCS server.

We recommend
                                             				that you use the smaller datastore (with ESXi installed on it).

Step 3

Make this
                                          			 template available to the UCS server.

Step 4

Deploy the
                                          			 template file using vSphere Client. Enter the following information for the new
                                          			 VM:

hostname

datastore—Select a datastore that has enough resource.

Step 5

Complete
                                          			 creating the VM.

At this point a
                                             				new VM is created with the correct amount of RAM, number of CPUs, size and
                                             				number of disks for the intended application.

Step 6

Install Cisco
                                          			 Emergency Responder on the Cisco UCS Server on the VM.

See Install Emergency Responder on VM for more information.

### Download Virtual
                           	 Machine Templates (OVA Templates)

The
                                 		  configuration of a Cisco Emergency Responder virtual machine must match a
                                 		  supported virtual machine template.

To obtain
                                 		  the virtual machine template for Cisco Emergency Responder on the Cisco UCS
                                 		  Server, follow these steps:

Step 1

Select this URL
                                          			 in your browser:

http://www.cisco.com/cisco/software/navigator.html?mdfid=272877967

Step 2

If your browser
                                          			 prompts you to do so, type your Cisco.com User Name and Password in the text
                                          			 boxes, then click the Log In button.

Step 3

Select the
                                          			 desired version of Cisco Emergency Responder.

Step 4

Click the Emergency
                                             				Responder Virtual Machine Templates link.

Step 5

Move your mouse
                                          			 over the filename and click the Readme link
                                          			 to view the virtual machine template's release information.

Step 6

Click the Download Now button. Follow the prompts and provide the required information to download the
                                          			 software.

### Install Emergency
                           	 Responder on VM

Step 1

In vSphere
                                          			 Client, edit the VM to force entry into BIOS setup the next time the VM
                                          			 reboots.

Step 2

Make the
                                          			 Emergency Responder installation media available to the VM DVD-ROM drive.

Step 3

Power on the VM,
                                          			 then in BIOS setup, promote CD ROM to boot before the hard drive.

Step 4

Complete booting
                                          			 the VM.

The Cisco
                                             				Emergency Responder installation program starts. For information about
                                             				performing the installation, see the Installing Cisco Emergency Responder
                                             				document.

#### Virtual Machine
                              	 Configurations

With the virtual machine configuration for running Cisco Emergency Responder on the Cisco UCS Server, the VMware server must
                                 match the specifications described in the System Requirements to be supported by Cisco.

While Cisco
                                 		Emergency Responder can be installed and licensed in other virtual machine
                                 		configurations, Cisco does not support these configurations.

### Migrate to Emergency
                           	 Responder on Cisco UCS Server

Migrating
                                 		  from a Media Convergence Server (MCS server) to a Cisco Emergency Responder on
                                 		  the Cisco UCS Server follows a procedure that is very similar to replacing
                                 		  server hardware.

The
                                 		  following procedure outlines the migration process and references to other
                                 		  pertinent documentation.

Step 1

Upgrade the MCS
                                          			 server to the most recent version of Cisco Emergency Responder.

Step 2

If the Emergency
                                          			 Responder VM uses a different IP address from the MCS server, change the IP
                                          			 address of the MCS server to the value used by the Emergency Responder VM.

Step 3

Perform a DRS
                                          			 backup on the MCS server.

Step 4

Create the
                                          			 virtual machine (VM) on the Cisco UCS server used as the replacement for the
                                          			 MCS node.

Step 5

Install the new
                                          			 version of Cisco Emergency Responder on the Cisco UCS server.

Step 6

Perform a DRS
                                          			 restore to restore the data backed up from the MCS server to the Cisco UCS
                                          			 server.

Step 7

Upload the new
                                          			 licenses to the Cisco Emergency Responder on the Cisco UCS server.

### VMWare
                           	 Support

Consider
                              		the following, when using Cisco Emergency Responder on the Cisco UCS Server:

Install, upgrade, and recovery procedures now use "soft media" such as ISO or FLP (virtual floppy) if the server does not have a DVD drive.

USB tape backup
                                    			 is not supported.

NIC teaming is
                                    			 configured at the VMware virtual switch.

Hardware SNMP
                                    			 and syslog move to VMware and UCS Manager.

Install logs are
                                    			 written only to the virtual serial port.

Unattended installs use virtual floppy instead of USB.

Basic UPS
                                    			 Integration is not supported.

Boot order is
                                    			 controlled by the BIOS of the VMware VM.

Hardware BIOS, firmware, and drivers must be the required level and configured for compatibility with Cisco Emergency Responder
                                    supported VMware product and version.

For more
                              		information about the UCS C-series server, go to the following URL:

https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/gui/config/guide/4_3/b_cisco_ucs_c-series_gui_configuration_guide_for_s3260_servers_43.html

To view
                              		the list of product installation and configuration guides for Cisco UCS
                              		C-Series Integrated Management Controller, go to the following URL:

http://www.cisco.com/en/US/products/ps10739/products_installation_and_configuration_guides_list.html

To view
                              		the list of product installation and configuration guides for Cisco UCS
                              		Manager, go to following URL:

http://www.cisco.com/en/US/products/ps10281/products_installation_and_configuration_guides_list.html

### Emergency Responder
                           	 Daily Operations on Cisco UCS Server

Daily
                              		operations for Cisco Emergency Responder on the Cisco UCS Server software
                              		applications are identical to when the application is installed on an MCS
                              		server.

There are
                              		some differences in hardware management and monitoring because Cisco Emergency
                              		Responder on the Cisco UCS Server operates in a virtual environment.

#### Hardware Monitoring
                              	 From the VM

Applications
                                 		running in a VM have no ability to monitor the physical hardware. Hardware
                                 		monitoring must be done from the CIMC, ESXi plugins, vCenter, or by physical
                                 		inspection (for example, for flashing LEDs.).

#### Hardware Monitoring
                              	 From CIMC

The CIMC
                                 		provides the following hardware monitoring:

An overview of
                                       			 CPU, memory, and power supply health

An overview of
                                       			 hardware inventory, including CPUs, memory, power supplies, and storage

Monitoring of
                                       			 sensors for power supplies, fans, temperature, and voltage

A system event log
                                       			 that contains BIOS and sensor entries

#### Hardware Monitoring
                              	 From VSphere Client and VCenter

The vSphere
                                 		Client provides the following monitoring features:

When you are
                                       			 logged in to vCenter, the vSphere Client displays hardware and system alarms
                                       			 defined on the Alarms tab.

VM resource usage
                                       			 is displayed on the Virtual Machines tab and on the Performance tab for each
                                       			 VM.

Host performance
                                       			 and resource usage is displayed on the Performance tab for the Host.

When ESXi is used
                                       			 standalone (without vCenter), hardware status and resource usage are available,
                                       			 but alarming is not possible.

### Related
                           	 Documentation

The UCS RAID Controller SMI-S Reference Guide , which describes
                              		Storage Management Initiative Specification (SMI-S) support in the Cisco UCS
                              		Servers, is available at the following URL:

https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/utilities/raid/reference/guide/ucs_raid_smis_reference/Supported_Profiles.html

## Installation on a New System

This procedure describes how to install Emergency Responder  as a new installation.

You enter Emergency Responder group configuration through the Emergency Responder Administration web interface based on Publisher
                           (primary) and Subscriber (secondary) server pairs as described in the following sections.

### Install Emergency
                           	 Responder Publisher

To
                                 		  install Emergency Responder, you install the Publisher (primary) first, then
                                 		  you install the Subscriber (backup) on a separate server. You must install
                                 		  Emergency Responder on separate servers from
                                 		  CiscoUnifiedCommunicationsManager or any Cisco Unified Communications
                                 		  applications.

Allow
                                 		  approximately 1 hour to perform a new installation.

Insert the
                                    			 Emergency Responder Installation DVD.

If the system
                                       				finds the DVD, you are asked if you want to perform a media check before
                                       				installation to determine if there are problems with the DVD. The system
                                       				displays the checksum of the DVD and instructs you to verify this checksum on
                                       				the Emergency Responder website.

At the bottom
                                       				of the screen you will see instructions for moving between elements and for
                                       				selecting elements, as follows:

- Use the Tab key
                                       				to advance to the next element.

- Use the Alt-Tab key combination to return to the previous element.

- Use the Space bar to select a highlighted element.

If you choose
                                       				to perform the media check, the system performs the media check and displays
                                       				the results.

If the result
                                       				of the media check is PASS ,
                                       				click OK . The
                                       				system install begins the installation. Skip to Step 2.

If the result
                                       				of the media check is FAIL ,
                                       				obtain a new installation DVD from Cisco Systems.

The Cisco
                                    			 Emergency Responder system installer starts. The Product Deployment Selection
                                    			 screen displays a message saying the Cisco Emergency Responder product suite is
                                    			 installing. Click OK to
                                    			 continue.

The Proceed
                                    			 with Install page displays the current software version on the hard drive and
                                    			 the software version on the installation DVD.

If you are
                                       				performing a fresh installation, there will be no software on the hard drive
                                       				and the system asks if you want to proceed with the installation. Click Yes to
                                       				proceed.

If you are
                                       				performing an upgrade, the system displays the current software version and
                                       				asks it you want to overwrite the hard drive. Click Yes to
                                       				proceed.

If you click Yes , the
                                       				system continues with the installation and the Platform Configuration Wizard
                                       				appears.

If you click No , the
                                       				installation is terminated.

On the
                                    			 Platform Configuration Wizard page, click Proceed to
                                    			 continue with the platform installation.

If you click Skip ,
                                       				the system installs both the platform and Emergency Responder software without
                                       				prompting you to provide information during the installation. After the
                                       				installation is completed and the system reboots, you are prompted to enter the
                                       				required configuration details.

Click Continue to proceed. The Timezone Configuration page appears.

Choose the
                                    			 correct time zone to use from the list provided.

Use the
                                       				following keys to move between elements on the Timezone Configuration page:

- Arrow Up or Arrow
                                          				  Down to select a time zone from the list

- After selecting the correct
                                       				time zone, click OK . The
                                       				Auto Negotiation Configuration page appears.

Click Yes to
                                    			 enable autonegotiation of the Ethernet NIC speed and duplex mode. The DHCP
                                    			 Configuration page appears. If you click Yes , skip
                                    			 to Step 10.

If you click No , the
                                       				NIC Speed and Duplex Configuration page appears.

On the NIC
                                    			 Speed and Duplex Configuration page, do the following:

Select the
                                          				  NIC Speed. The available options are 10 Megabit, 100 Megabit, or 1000 Megabit.

Select the
                                          				  NIC Duplex setting. The available options are Full or Half.

Click OK .
                                          				  The DHCP Configuration page appears.

On the MTU
                                    			 Configuration page, you can set the maximum transmission unit (MTU) that can be
                                    			 sent in a network as follows:

- Click Yes if you want to configure a a MTU value of less than 1500 bytes.

- Click No to use the default MTU value of 1500 bytes.

Click Yes if you
                                    			 want to use Dynamic Host Configuration Protocol (DHCP). The Administration
                                    			 Login Configuration page appears. Skip to Step 14.

If you click No , the
                                       				Static Network Configuration page appears.

If you chose
                                    			 not to use DHCP, enter the following information about the Static Network
                                    			 Configuration page:

- Host Name

- IP Address

- IP Mask

- Gateway (GW) Address

Click OK . The
                                       				DNS Client Configuration page appears.

On the DNS
                                    			 Client Configuration page, you are asked if you want to configure the Domain
                                    			 Name System (DNS) client.

Click the Help button for details about configuring DNS.

If you
                                       				select Yes , a
                                       				second DNS Client Configuration page appears.

If you
                                       				select No ,
                                       				the Administration Login Configuration page appears. Skip to Step 14.

On the
                                    			 second DNS Client Configuration page, you are prompted to enter the following
                                    			 information:

- Primary

- Secondary DNS (optional)

- Domain

Click OK .
                                       				The Administration Login Configuration page appears.

On the
                                    			 Administration Login Configuration page, enter an ID and password for the
                                    			 Administrator account. This password is used to access the CLI and the
                                    			 CiscoUnifiedOS Administration and Disaster Recovery System (DRS) websites.
                                    			 Click Help to
                                    			 display guidelines for creating this password.

When you
                                       				have finished, click OK .
                                       				The Certificate Information page appears.

Enter the
                                    			 following information about the Certificate Information page:

- Organization

- Unit

- Location

- State

- Country (select from the
                                       				scroll-down menu).

Click OK .
                                       				The Publisher Configuration page appears.

Based on the
                                    			 type of installation you are performing, do one of the following:

- If the server you are
                                       				configuring is the Publisher in the server group, click Yes .
                                       				The Network Time Protocol Client Configuration page appears. Proceed to Step
                                       				17.

- If the server you are
                                       				installing is not the Publisher in the server group, you must first configure
                                       				this server on the Publisher before you can proceed. This server must also have
                                       				network access to the Publisher, which must be in service for the installation
                                       				to complete successfully. Click No only if you are configuring the Subscriber. See Install Emergency Responder Subscriber for information about installing the Subscriber.

On the
                                    			 Network Time Protocol Client Configuration page, you are asked if you want to
                                    			 set up external Network Time Protocol (NTP) servers.

We
                                                   				  strongly recommend that you use external NTP servers to ensure that the system
                                                   				  time is kept accurate.

Caution

For
                                                   				  Emergency Responder install on UCS servers, it is mandatory to configure NTP
                                                   				  server.

If you click Yes ,
                                       				the system displays a second Network Time Protocol Client Configuration page.
                                       				In the fields provided, enter the IP address or hostname of the external NTP
                                       				servers, then click OK .
                                       				The Database Access Security Configuration page appears. Skip to Step 18.

If you click No ,
                                       				the Hardware Clock Configuration page appears. Enter the following information:

- Year [yyyy]

- Month [mm]

- Day [dd]

- Hour [hh]

- Minute [mm]

- Second [ss]

When you
                                       				finish entering this information, click OK .
                                       				The Database Access Security Configuration page appears.

On the
                                    			 Database Access Security Configuration page, enter the security password and
                                    			 then confirm the password in the fields provided.

The
                                                   				  security password must be at least six characters long and can contain
                                                   				  alphanumeric characters, hyphens, and underscores. It must start with an
                                                   				  alphanumeric character. The security password is used for secure communications
                                                   				  between Emergency Responder server groups when performing the installation or
                                                   				  upgrade, DRS backup or restore, and "Point to
                                                      					 a new Publisher" operations.

Click Help to display guidelines. When you finish, click OK .
                                       				The SMTP Host Configuration page appears.

You are
                                    			 asked if you want to configure a Simple Mail Transport Protocol (SMTP) host.
                                    			 This step is optional.

- If you click Yes , a
                                       				second SMTP Host Configuration page appears. Click Help for guidelines, then enter the SMTP hostname or IP address in the field
                                       				provided. When you are finished, click OK .
                                       				The Platform Configuration Confirmation page appears.

- If you click No ,
                                       				the Platform Configuration Confirmation page appears.

On the
                                    			 Platform Configuration Confirmation page, do one of the following:

After
                                                      					 you select OK , you cannot modify the platform configuration
                                                      					 information.

- Select Back if you want to return to the previous page to make modifications. Continue to
                                       				select Back to scroll through each platform configuration page.

- Select Cancel to cancel the installation.

On the Cisco
                                    			 Emergency Responder Configuration page, do the following:

- Enter the emergency
                                       				number (for example, 911 ).

- Select the Cisco Unified
                                       				CommunicationsManager version. Use the Up or Down arrows to select the version number and then select OK .

On the
                                    			 Security End User Language Selection page, choose a language for the Cisco
                                    			 Emergency Responder web pages. The system defaults to the English language.

The
                                       				Application User Password Configuration page appears.

On the
                                    			 Application User Configuration page, enter the username and password. This
                                    			 username and password is associated with the default administrative account and
                                    			 is used to log in to the Emergency Responder Administration web page. Click Help for
                                    			 guidelines.

When you are
                                       				finished, click OK .
                                       				The Cisco Emergency Responder Configuration Confirmation page appears.

On the Cisco
                                    			 Emergency Responder Configuration Confirmation page, do one of the following:

Caution

After
                                                      					 you select OK , you can not modify the Cisco Emergency Responder
                                                      					 configuration information.

- Select Back if you want to return to the previous page to make modifications. Continue to
                                       				select Back to scroll through each Emergency Responder Application User Configuration page.

- Select Cancel to cancel the installation.

After the
                                    			 system reboots, it checks the status of various system components. If the
                                    			 system finds any problems, you are prompted to correct the problem.

If the
                                       				system does not find any problems, the installation process continues. The
                                       				system ejects the installation DVD, reboot, and then finishes the installation.
                                       				When the installation is complete, a CLI prompt appears.

During
                                                   				  this process, the system displays the MAC address of the Publisher. Write down
                                                   				  the MAC address when it displays; you use the MAC address later to acquire
                                                   				  Emergency Responder licenses. If you are not able to capture the MAC address
                                                   				  during installation, you can look it up later. See the Server Licenses section
                                                   				  for information about looking up the server MAC address.

To bring up
                                    			 the Emergency Responder websites, go to any Windows system on the network,
                                    			 start a supported web browser, and enter the following URL:

http://your Emergency
                                          				  Responder hostname/

or

http://your Emergency
                                          				  Responder IP address/

Make sure
                                                   				  that the Emergency Responder is configured with DNS so that hostname is
                                                   				  resolved to the IP address.

### Install Emergency
                           	 Responder Subscriber

You must
                                 		  install Subscriber only after you have installed the Publisher. You must
                                 		  install the Subscriber on a separate server from the Emergency Responder
                                 		  Publisher.

Caution

You must complete
                                             			 the installation of the Publisher, which includes a system reboot, before you
                                             			 start to install the Subscriber.

Step 1

On the Publisher
                                          			 server, add the details about the Subscriber server by doing the following:

Log in the
                                                				  Publisher Emergency Responder Administration website.

Select System >
                                                   					 Add Subscriber . The Add Server page appears.

Enter the
                                                				  hostname of the new Subscriber and click Insert .
                                                				  The Add Subscriber page appears again.

In the Configured
                                                   					 Servers list, check that the hostname and IP address of the new
                                                				  Subscriber is listed.

Step 2

Follow Steps 1
                                          			 through 15 in the Installation on a New System section. After you complete Step 15,
                                          			 the Publisher Configuration page appears.

Step 3

On the Publisher
                                          			 Configuration page, select No to
                                          			 indicate that you are installing a Subscriber, not a Publisher. The system
                                          			 displays a warning saying that if this is not the Publisher, you must first
                                          			 configure this server using the Publisher Administration web interface before
                                          			 you can proceed (see Step 1 of this procedure for more information). Also, this
                                          			 server being added must have network access to the Publisher, which must be in
                                          			 service for the installation to complete successfully.

Click OK to
                                             				close the warning.

Step 4

The Network
                                          			 Connectivity Test Configuration page appears. The system attempts to verify
                                          			 system connectivity. Click No to
                                          			 continue the installation.

Step 5

The Publisher
                                          			 Access Configuration page appears. Enter the following:

- Publisher hostname

- Publisher IP address

- Publisher Database/Security
                                             				password

Step 6

Verify that the
                                          			 Publisher information is correct and click OK .

Step 7

The SMTP Host
                                          			 Configuration page appears. Choose Yes if you
                                          			 want to configure the SMTP Host.

Step 8

The Platform
                                          			 Configuration Complete page appears. Select one of the following options:

- If the Publisher information
                                             				is correct, click OK .

- If the information is not
                                             				correct, click the Back button and make the needed corrections on the Publisher Access
                                             				Configuration page, then click OK .

The installation
                                             				of the Emergency Responder Subscriber begins and takes an additional 20 to 30
                                             				minutes to complete.

Step 9

When the
                                          			 installation completes, go to the Emergency Responder Administration website on
                                          			 the Subscriber to verify that the Subscriber was installed successfully. If the
                                          			 installation succeeded, a message saying "Primary Cisco
                                             				Emergency Responder is active" appears. This message indicates that the
                                          			 Subscriber was installed successfully.

If the
                                                         				  Subscriber installation cannot validate the Publisher, See Cannot Validate Publisher in the Troubleshooting chapter.

## Emergency Responder
                        	 Upgrade

To upgrade Cisco Emergency Responder to the most recent version, use the Cisco Unified OS Administration web interface or
                           Command Line Interface (CLI). See Software Upgrades section for information about performing upgrades.

See "Performing Software Upgrades" section of the respective Cisco Emergency Responder Administration Guide for Emergency Responder for information about performing upgrades to Emergency Responder.

| Note | We recommend that
                                       		  you perform the installation or upgrade during off-peak hours. The installation
                                       		  or upgrade procedure completely reformats the hard disk, so Emergency Responder
                                       		  is unavailable for the duration of the installation or upgrade. |
|---|---|

| Note | Emergency Responder supports interoperability between two server groups in a cluster running different versions of Emergency
                                                Responder. |
|---|---|

| Note | The
                                                   					 Emergency Responder administrative users password must be at least six
                                                   					 characters long and can contain alphanumeric characters, hyphens, and
                                                   					 underscores. It must start with an alphanumeric character. |
|---|---|

| Note | Use of NTP server is
                                       		  mandatory when installing Emergency Responder on UCS servers. |
|---|---|

| Note | To avoid upgrade failures due to time sync issues with VM, disable the VM's NTP sync with the ESXi host using the workaround
                                       mentioned in the following link: https://knowledge.broadcom.com/external/article?legacyId=1189 . |
|---|---|

| Installation Task | For
                                       				More Information |
|---|---|
| Upgrade Emergency Responder | Software Upgrades |
| Upgrade Unified CM | https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html Change Cisco Unified Communications Manager Version |
| Update Unified CM Version | Update Cisco Unified Communications Manager Version |

| Installation Task | For
                                       				More Information |
|---|---|
| Install Cisco Unified Communications Manager | https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
| Install Emergency Responder as a new installation | Installation on a New System |

| System Parameter | System Parameter options |
|---|---|
| Supported Virtual Machine Configuration | See
                                             					 the documentation at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-emergency-responder.html |
| IOPS per virtual machine (VM) | See
                                             					 the documentation at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-emergency-responder.html |
| VMware version | ESXi 4.0 Update 1 Note Ensure that you use ESXi, rather than ESX, to run Cisco Emergency Responder on the Cisco UCS Server. However, the server can
                                                      be part of a VMware vCenter that includes ESX hosts. | Note | Ensure that you use ESXi, rather than ESX, to run Cisco Emergency Responder on the Cisco UCS Server. However, the server can
                                                      be part of a VMware vCenter that includes ESX hosts. |
| Note | Ensure that you use ESXi, rather than ESX, to run Cisco Emergency Responder on the Cisco UCS Server. However, the server can
                                                      be part of a VMware vCenter that includes ESX hosts. |
| VMware—vMotion | No Note Cisco does not support vMotion on a VM that is running. However, Cisco does support powering-down a VM, then rebooting the
                                                      VM on a different rack server. This may be helpful if you want to put a rack server into maintenance mode. | Note | Cisco does not support vMotion on a VM that is running. However, Cisco does support powering-down a VM, then rebooting the
                                                      VM on a different rack server. This may be helpful if you want to put a rack server into maintenance mode. |
| Note | Cisco does not support vMotion on a VM that is running. However, Cisco does support powering-down a VM, then rebooting the
                                                      VM on a different rack server. This may be helpful if you want to put a rack server into maintenance mode. |
| VMware—Site Recovery Manager | Yes |
| VMware—High Availability | Yes |
| VMware—Data Recovery (VDR) | Yes |
| All other unlisted VMware features | Not supported |

| Note | Ensure that you use ESXi, rather than ESX, to run Cisco Emergency Responder on the Cisco UCS Server. However, the server can
                                                      be part of a VMware vCenter that includes ESX hosts. |
|---|---|

| Note | Cisco does not support vMotion on a VM that is running. However, Cisco does support powering-down a VM, then rebooting the
                                                      VM on a different rack server. This may be helpful if you want to put a rack server into maintenance mode. |
|---|---|

| Note | Even if you use VMware GO, you still must use the supported VMware configuration on Cisco Emergency Responder on the Cisco
                                          UCS Server, which are documented at both http://www.cisco.com/go/swonly and https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-emergency-responder.html . |
|---|---|

| Step 1 | Prepare to
                                          			 install the server. For more
                                          			 information, see Install Preparations . |
|---|---|
| Step 2 | Physically
                                          			 install and connect the server. |
| Step 3 | Power on the
                                          			 server and configure Cisco Integrated Management Controller (CIMC) for remote
                                          			 management. |
| Step 4 | If you purchased
                                          			 the UCS server separately, configure the RAID settings to the following
                                          			 specification: The first two drives are
                                             				configured as a RAID 1 (mirrored) drive. This drive is for ESXi installation. The next four drives are
                                             				configured as a RAID 5 drive. This drive is for VMs. Note Number of
                                                            					 drives may be different in different versions of UCS servers. For more
                                          			 information, see Set Up RAID | Note | Number of
                                                            					 drives may be different in different versions of UCS servers. |
| Note | Number of
                                                            					 drives may be different in different versions of UCS servers. |
| Step 5 | If you purchased
                                          			 the UCS server separately, configure the BIOS to the following specification: Disable Quiet Mode. Enable Enhanced SATA for
                                             				CDROM access. Configure the following boot
                                             				order: SATA5:Optiarc DVD first PCI Raid
                                                      						Adapter second |
| Step 6 | Install and
                                          			 configure VMware EXSi on the smaller of the two available disks. For more
                                          			 information, see the VMware ESXi documentation. |
| Step 7 | Install vSphere
                                          			 Client. For more
                                          			 information, see vSphere Client Installation and the vSphere Client
                                          			 documentation. |
| Step 8 | Align the
                                          			 datastores for the VMs. For more
                                          			 information, see Aligning the Datastore Used for VMs . |
| Step 9 | If you use
                                          			 802.1q trunking, set the MTU size to 1472. |
| Step 10 | Install and
                                          			 configure a virtual machine (VM). For more
                                          			 information, see Create Virtual Machines and Download Virtual Machine Templates (OVA Templates) . |
| Step 11 | Install Cisco
                                          			 Emergency Responder on the VM. For more
                                          			 information, see Install Emergency Responder on VM . |

| Note | Number of
                                                            					 drives may be different in different versions of UCS servers. |
|---|---|

| Note | Number of drives
                                             			 may be different in different versions of UCS servers. |
|---|---|

| Step 1 | During server
                                          			 bootup, press Ctrl+Y to
                                          			 enter the preboot CLI. |
|---|---|
| Step 2 | Enter the
                                          			 following commands to determine the current RAID configuration: -ldinfo -l0 -a0 -ldinfo -l1 -a0 The required
                                             				configuration is two drives in a RAID 1 array for logical drive 0, and four
                                             				drives in a RAID 5 array for Logical drive 1. If the RAID configuration is
                                             				wrong, continue with this procedure. Note Do not
                                                         				  continue with this procedure if RAID is configured correctly. | Note | Do not
                                                         				  continue with this procedure if RAID is configured correctly. |
| Note | Do not
                                                         				  continue with this procedure if RAID is configured correctly. |
| Step 3 | Enter the
                                          			 command -cfgclr -a0 to clear the RAID configuration. Caution Clearing the
                                                         				  RAID configuration deletes all data on the hard drives. | Caution | Clearing the
                                                         				  RAID configuration deletes all data on the hard drives. |
| Caution | Clearing the
                                                         				  RAID configuration deletes all data on the hard drives. |
| Step 4 | Enter the
                                          			 following commands to configure RAID: -cfgldadd -r1 [252:0, 252:1]
                                                				  -a0 -cfgldadd -r5 [252:2, 252:3,
                                                				  252:4, 252:5] -a0 If the hard
                                             				drives did not have a RAID configuration previously, you are done configuring
                                             				RAID. If the hard drives had a RAID configuration before, continue with this
                                             				procedure. |
| Step 5 | Enter the
                                          			 following commands to initialize the logical volumes: - ldinit -start -full -l0
                                                				  -a0 (l0 is the letter l and the number 0, not the number 10) - ldinit -start -full -l1
                                                				  -a0 (l1 is the letter l and the number 1, not the number 11) These commands
                                             				clear data on the drives and initialize the new array. |
| Step 6 | Allow these
                                          			 commands to finish running before exiting the Preboot CLI. Enter the following
                                          			 commands to display the
                                             				progress of the commands: -ldinit -showprog -l0 -a0 -ldinit -showprog -l1 -a0 When both
                                             				commands report that no initialization is running, it is safe to quit the
                                             				Preboot CLI. |
| Step 7 | After
                                          			 configuring the two logical volumes, you can exit the Preboot CLI by entering q . |

| Note | Do not
                                                         				  continue with this procedure if RAID is configured correctly. |
|---|---|

| Caution | Clearing the
                                                         				  RAID configuration deletes all data on the hard drives. |
|---|---|

| Step 1 | Download the VM
                                          			 template for your application. See Download Virtual Machine Templates (OVA Templates) for more information. |
|---|---|
| Step 2 | Upload the
                                          			 template to a datastore on the UCS server. We recommend
                                             				that you use the smaller datastore (with ESXi installed on it). |
| Step 3 | Make this
                                          			 template available to the UCS server. |
| Step 4 | Deploy the
                                          			 template file using vSphere Client. Enter the following information for the new
                                          			 VM: hostname datastore—Select a datastore that has enough resource. |
| Step 5 | Complete
                                          			 creating the VM. At this point a
                                             				new VM is created with the correct amount of RAM, number of CPUs, size and
                                             				number of disks for the intended application. |
| Step 6 | Install Cisco
                                          			 Emergency Responder on the Cisco UCS Server on the VM. See Install Emergency Responder on VM for more information. |

| Step 1 | Select this URL
                                          			 in your browser: http://www.cisco.com/cisco/software/navigator.html?mdfid=272877967 |
|---|---|
| Step 2 | If your browser
                                          			 prompts you to do so, type your Cisco.com User Name and Password in the text
                                          			 boxes, then click the Log In button. |
| Step 3 | Select the
                                          			 desired version of Cisco Emergency Responder. |
| Step 4 | Click the Emergency
                                             				Responder Virtual Machine Templates link. |
| Step 5 | Move your mouse
                                          			 over the filename and click the Readme link
                                          			 to view the virtual machine template's release information. |
| Step 6 | Click the Download Now button. Follow the prompts and provide the required information to download the
                                          			 software. |

| Step 1 | In vSphere
                                          			 Client, edit the VM to force entry into BIOS setup the next time the VM
                                          			 reboots. |
|---|---|
| Step 2 | Make the
                                          			 Emergency Responder installation media available to the VM DVD-ROM drive. |
| Step 3 | Power on the VM,
                                          			 then in BIOS setup, promote CD ROM to boot before the hard drive. |
| Step 4 | Complete booting
                                          			 the VM. The Cisco
                                             				Emergency Responder installation program starts. For information about
                                             				performing the installation, see the Installing Cisco Emergency Responder
                                             				document. |

| Step 1 | Upgrade the MCS
                                          			 server to the most recent version of Cisco Emergency Responder. |
|---|---|
| Step 2 | If the Emergency
                                          			 Responder VM uses a different IP address from the MCS server, change the IP
                                          			 address of the MCS server to the value used by the Emergency Responder VM. Note The
                                                         				  hostname on the Emergency Responder VM must remain the same as that on the MCS
                                                         				  Server. | Note | The
                                                         				  hostname on the Emergency Responder VM must remain the same as that on the MCS
                                                         				  Server. |
| Note | The
                                                         				  hostname on the Emergency Responder VM must remain the same as that on the MCS
                                                         				  Server. |
| Step 3 | Perform a DRS
                                          			 backup on the MCS server. |
| Step 4 | Create the
                                          			 virtual machine (VM) on the Cisco UCS server used as the replacement for the
                                          			 MCS node. For more
                                          			 information, see Installation on Cisco UCS Server . |
| Step 5 | Install the new
                                          			 version of Cisco Emergency Responder on the Cisco UCS server. For more
                                          			 information, see Installation on Cisco UCS Server . |
| Step 6 | Perform a DRS
                                          			 restore to restore the data backed up from the MCS server to the Cisco UCS
                                          			 server. |
| Step 7 | Upload the new
                                          			 licenses to the Cisco Emergency Responder on the Cisco UCS server. |

| Note | The
                                                         				  hostname on the Emergency Responder VM must remain the same as that on the MCS
                                                         				  Server. |
|---|---|

| Note | For
                                                				version 8.6 and earlier, the Cisco Emergency Responder Subscriber may fail to
                                                				install with unrecoverable internal error indicated in the logs. If this
                                                				happens, do a Skip install by skipping the configurations step initially,
                                                				proceed with the installation, and then key in the configuration details when
                                                				prompted at the end of the procedure. |
|---|---|

| Note | Click the Help button for details about configuring DNS. |
|---|---|

| Note | We
                                                   				  strongly recommend that you use external NTP servers to ensure that the system
                                                   				  time is kept accurate. |
|---|---|

| Caution | For
                                                   				  Emergency Responder install on UCS servers, it is mandatory to configure NTP
                                                   				  server. |
|---|---|

| Note | The
                                                   				  security password must be at least six characters long and can contain
                                                   				  alphanumeric characters, hyphens, and underscores. It must start with an
                                                   				  alphanumeric character. The security password is used for secure communications
                                                   				  between Emergency Responder server groups when performing the installation or
                                                   				  upgrade, DRS backup or restore, and "Point to
                                                      					 a new Publisher" operations. |
|---|---|

| Note | After
                                                      					 you select OK , you cannot modify the platform configuration
                                                      					 information. |
|---|---|

| Caution | After
                                                      					 you select OK , you can not modify the Cisco Emergency Responder
                                                      					 configuration information. |
|---|---|

| Note | During
                                                   				  this process, the system displays the MAC address of the Publisher. Write down
                                                   				  the MAC address when it displays; you use the MAC address later to acquire
                                                   				  Emergency Responder licenses. If you are not able to capture the MAC address
                                                   				  during installation, you can look it up later. See the Server Licenses section
                                                   				  for information about looking up the server MAC address. |
|---|---|

| Note | Make sure
                                                   				  that the Emergency Responder is configured with DNS so that hostname is
                                                   				  resolved to the IP address. |
|---|---|

| Caution | You must complete
                                             			 the installation of the Publisher, which includes a system reboot, before you
                                             			 start to install the Subscriber. |
|---|---|

| Step 1 | On the Publisher
                                          			 server, add the details about the Subscriber server by doing the following: Log in the
                                                				  Publisher Emergency Responder Administration website. Select System >
                                                   					 Add Subscriber . The Add Server page appears. Enter the
                                                				  hostname of the new Subscriber and click Insert .
                                                				  The Add Subscriber page appears again. In the Configured
                                                   					 Servers list, check that the hostname and IP address of the new
                                                				  Subscriber is listed. |
|---|---|
| Step 2 | Follow Steps 1
                                          			 through 15 in the Installation on a New System section. After you complete Step 15,
                                          			 the Publisher Configuration page appears. |
| Step 3 | On the Publisher
                                          			 Configuration page, select No to
                                          			 indicate that you are installing a Subscriber, not a Publisher. The system
                                          			 displays a warning saying that if this is not the Publisher, you must first
                                          			 configure this server using the Publisher Administration web interface before
                                          			 you can proceed (see Step 1 of this procedure for more information). Also, this
                                          			 server being added must have network access to the Publisher, which must be in
                                          			 service for the installation to complete successfully. Click OK to
                                             				close the warning. |
| Step 4 | The Network
                                          			 Connectivity Test Configuration page appears. The system attempts to verify
                                          			 system connectivity. Click No to
                                          			 continue the installation. |
| Step 5 | The Publisher
                                          			 Access Configuration page appears. Enter the following: Publisher hostname Publisher IP address Publisher Database/Security
                                             				password |
| Step 6 | Verify that the
                                          			 Publisher information is correct and click OK . |
| Step 7 | The SMTP Host
                                          			 Configuration page appears. Choose Yes if you
                                          			 want to configure the SMTP Host. |
| Step 8 | The Platform
                                          			 Configuration Complete page appears. Select one of the following options: If the Publisher information
                                             				is correct, click OK . If the information is not
                                             				correct, click the Back button and make the needed corrections on the Publisher Access
                                             				Configuration page, then click OK . The installation
                                             				of the Emergency Responder Subscriber begins and takes an additional 20 to 30
                                             				minutes to complete. |
| Step 9 | When the
                                          			 installation completes, go to the Emergency Responder Administration website on
                                          			 the Subscriber to verify that the Subscriber was installed successfully. If the
                                          			 installation succeeded, a message saying "Primary Cisco
                                             				Emergency Responder is active" appears. This message indicates that the
                                          			 Subscriber was installed successfully. Note If the
                                                         				  Subscriber installation cannot validate the Publisher, See Cannot Validate Publisher in the Troubleshooting chapter. | Note | If the
                                                         				  Subscriber installation cannot validate the Publisher, See Cannot Validate Publisher in the Troubleshooting chapter. |
| Note | If the
                                                         				  Subscriber installation cannot validate the Publisher, See Cannot Validate Publisher in the Troubleshooting chapter. |

| Note | If the
                                                         				  Subscriber installation cannot validate the Publisher, See Cannot Validate Publisher in the Troubleshooting chapter. |
|---|---|