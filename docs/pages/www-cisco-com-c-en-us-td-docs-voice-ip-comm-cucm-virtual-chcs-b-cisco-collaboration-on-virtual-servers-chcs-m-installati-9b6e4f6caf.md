---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-virtual-chcs-b-cisco-collaboration-on-virtual-servers-chcs-m-installati-9b6e4f6caf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/virtual/chcs_b_cisco-collaboration-on-virtual-servers/chcs_m_installation-and-configuration.html
retrieved_at: 2026-08-17T00:09:29.533207+00:00
---

Cisco Collaboration on Virtual Servers

# Cisco Collaboration on Virtual Servers

Updated: November 18, 2020

Chapter: Installation and Configuration

## Chapter: Installation and Configuration

# Installation and Configuration

The Extra-Small TRC (UCS E160D M2 TRC1), Small TRCs (UCS C220 M3S TRC2, UCS C240 M4S TRC1) and the Small Plus TRCs (UCS C220
                                    M3S TRC3, UCS C220 M4S TRC2) are preloaded with software if purchased as a Cisco Business Edition 6000 appliance.

Certain Medium TRCs (UCS C240 M3S TRC2, UCS C240 M4S2 TRC1) and Large TRCs (UCS C240 M4SX TRC1) are preloaded with software
                                    if purchased as a Cisco Business Edition 7000 appliance.

HyperFlex TRCs (HX240cM4SX TRC1) (HX220c M5SX TRC1) are preloaded with virtualization and HyperFlex software.

## Install Cisco UCS B-Series Tested Reference Configurations

Ensure that your UCS Mini or Fabric Interconnect Switches, Blade Server Chassis, and Fabric Extenders are installed in the
                                       rack.

Ensure that the network connections of your UCS Mini or Fabric Interconnect Switches are connected to their designated, trunked,
                                       switch ports.

Ensure that your Fabric Interconnect Switches are properly connected to your Fabric Extenders.

Ensure that you are able to access the blade remotely using UCS Manager software.

For the remaining server installation, see Cisco documentation at http://www.cisco.com/go/ucs .

## Install Cisco UCS C-Series and E-Series Tested Reference Configurations

Perform the following tasks to install and configure a virtual machine on a Cisco UCS server.

### Before you begin

Review the “Preparation” chapter in this guide for the installation requirements for your server.

Install Cisco UCS C-Series or E-Series Server

Install the Cisco UCS Server.

Configure Cisco Integrated Management Controller

Power on the server and configure Cisco Integrated Management Controller (CIMC) for remote management.

Configure RAID using one of the following procedures:

Configure the RAID settings on your server using either the Preboot CLI or GUI indicated above.

Configure BIOS

Configure the BIOS boot order.

Install and Configure VMware ESXi 7.0

Install and configure the VMware ESXi and the vSphere client.

Download Virtual Machine Templates (OVA Templates)

Download an OVA for collaboration application software, such as Cisco Unified Communications Manager, onto your virtual machine.

Use vSphere to create the VM on the server:

Use vSphere to Create the VM for Servers with Optical Drives

- Use vSphere to Create the VM for Servers Without Optical Drives

Use vSphere to create the VM on the server. Map the OVA to the VM.

Install Cisco Collaboration Applications on VMs

Install Collaboration applications such as Cisco Unified Communications Manager on the virtual machine.

### Install Cisco UCS C-Series or E-Series Server

If UCS C-Series, install the server in the rack. If UCS E-Series, install the Cisco ISR in the rack and installe the UCS E-Series
                                          blade server into the ISR.

Attach the Cisco Integrated Management Controller (Cisco IMC) of the Cisco UCS C-Series or E-Series management port to the
                                          designated switch port.

Attach the UCS C-Series LAN on Motherboard (LOM) or NIC ports (or the UCS E-Series external ethernet ports if used instead
                                          of internal ethernet ports) to their designated, trunked switch ports.

Attach a VGA console, or a KVM to the VGA and keyboard ports. This step is necessary until Cisco IMC is configured.

Attach UCS C server or Cisco ISR for UCS E server to power supply.

#### What to do next

### Configure Cisco Integrated Management Controller

Configuring the Cisco IMC allows you to perform all subsequent configuration and installation using the Cisco IMC console.
                                 In addition, the Cisco IMC provides a measure of hardware monitoring.

#### Before you begin

Power on server.

During boot, press indicated function key (e.g. F8 for a UCS C-Series) to enter Cisco IMC configuration.

In the Cisco IMC configuration screen, under IPV4 (Basic):

Uncheck the DHCP enabled check box using the spacebar.

Enter values for the Cisco IMC IP, Subnet mask, and Gateway.

Leave VLAN (Advanced) unchecked.

Under Default User (Basic), enter the default Cisco IMC user, admin , and a password.

Press indicated function key (e.g. F10 for a UCS C-Series) to save your settings.

After it is configured, the Cisco IMC is accessible using http. Point a browser to the IP address configured above and log
                                          in as admin, using the password configured above.

### RAID Configuration

To be supported as a Tested Reference Configuration instead of UCS Specs-based, the RAID must be set up exactly as indicated
                                             below. Do not change the RAID configuration on a server ordered as Cisco Business Edition 6000 or Cisco Business Edition 7000.

While creating data store, you must exactly follow the RAID configuration as shown in the following table or it could degrade
                                             your disk read or write performance, impacting installation, upgrade, and database synchronization.

Refer to the following table for the RAID specifications for the type of virtual machine that you want to configure.

TRC

Information

UCS C220 M5SX TRC1 (Small TRC / BE6000M M5)

One virtual drive with a RAID-5 array

Six 300-GB hard drives

UCS C220 M5SX TRC2 (Small Plus TRC / BE6000H M5)

One virtual drive with RAID-5

Eight 300-GB hard drives

UCS C240 M5SX TRC1 (Medium TRC / BE7000M M5)

Two virtual drives (VDs) with RAID-5

Each VD has seven 300-GB hard drives

UCS C240 M5SX TRC2 (Large TRC / BE7000H M5)

Four virtual drives (VD) with RAID-5

Each VD has six 300-GB hard drives.

UCS C220 M4S TRC1 (Small TRC / BE6000M M4)

One virtual drive with a RAID-5 array

Six 300-GB hard drives

UCS C220 M4S TRC2 (Small Plus TRC / BE6000H M4)

One virtual drive with RAID-5

Eight 300-GB hard drives

UCS C240 M4S2 TRC1 (Medium TRC / BE7000M M4)

Two virtual drives (VDs) with RAID-5

Each VD has six 300-GB hard drives

UCS C240 M4SX TRC1 (Large TRC / BE7000H M4)

Four virtual drives (VD) with RAID-5

Each VD has five 300-GB hard drives.

(End of Sale) UCS C240 M3S TRC1 (Large TRC)

Two virtual drives (VD) with RAID-5 arrays

Eight 300 GB hard drives for each VD

(End of Sale) UCS C240 M3S TRC2 (Medium TRC / BE7000M M3)

Two virtual drives (VD) with RAID-5 arrays

Six 300-GB hard drives for each VD

(End of Sale) UCS C220 M3S (Medium TRC)

One virtual drive with a RAID-5 array

Eight 300-GB hard drives

(End of Sale) UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3)

One virtual drive with a RAID-5 array

Eight 300-GB hard drives

(End of Sale) UCS C220 M3S TRC2 (Small TRC / BE6000M M3)

One virtual drive with a RAID-10 array

Four 500-GB hard drives

UCS E160S M3 TRC1 (Extra-Small TRC)

One virtual drive with a RAID-1 array- Two 900-GB hard drives

(End of Sale) UCS E160D M2 TRC1 (Extra-Small TRC / BE6000S M2)

One virtual drive with a RAID-5 array

Three 600-GB hard drives

(End of Sale) UCS C260 M2 TRC1 (Extra-Large TRC)

Two virtual drives (VD) with RAID-5 arrays

Eight 300 GB hard drives for each VD

(End of Sale) UCS C210 M2/M1 TRCs (Medium TRC)

First 2 drives are RAID-1 (mirrored) drives with the ESXi installation.

Remaining drives are RAID-5 with UC application VMs.

(End of Sale) UCS C200 M2 TRC1 (Small TRC / BE6000M M2)

One virtual drive with a RAID-10 array

Four 1 TB hard drives

If required, use the following settings for the Read and Write policies:

If UCS C-Series, do these settings:

Set Read Policy to read ahead = always .

Set Write Policy to one of the following:

write back with bbu – if you are using a RAID card with SuperCap (for example, RAID-9266CV).

This write policy is not available on the C240 M3 rack-mount server TRC2.

always write back – if you are using a RAID card with legacy Battery Backup (BBU) instead of SuperCap (for example, RAID-9266). This option
                                                         helps prevent a UC application performance impact if the BBU goes into learning mode or the battery dies. Whenever possible,
                                                         use the new RAID cards with SuperCap and make sure the UCS is attached to an Uninterruptible Power Supply (UPS).

If UCS E-Series M3, do these settings:

Strip Size = 64KB

Drives per Span = 2 (due to E160S M3 TRC1 shipping with two physical disks)

Span Depth = 1 (due to E160S M3 TRC1 using single LV, 2-disk RAID1)

Access Policy = Read-Write

Cache Policy = Direct

Read Ahead Policy = None

Requested Write Cache Policy = Write Through

Current Write Cache Policy = Write Through

Disk Cache Policy = Unchanged

Allow Background Init = true

Auto Snapshot = false

Auto Delete Oldest = true

#### Configure RAID with Preboot CLI (UCS C-Series M2 or M3 Servers)

Follow this procedure to configure a RAID array using the preboot CLI for M2 or M3 servers.

##### Before you begin

Check your current RAID configuration:

To use the Preboot CLI to configure RAID, enter Ctrl-Y .

Type the following commands:

TRC

Command

End of Sale UCS C260 M2 TRC1 (Extra-Large TRC)

-ldinfo -l0 -a0

-ldinfo -l1 -a0

End of Sale UCS C240 M3S TRC1 (Large TRC)

-ldinfo -l0 -a0

-ldinfo -l1 -a0

End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3)

End of Sale UCS C220 M3S TRC1 (Medium TRC)

-ldinfo -l0 -a0

End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3)

End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3)

End of Sale UCS C210 M2/M1 TRCs (Medium TRC)

End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2)

This command displays the number of drives, RAID level, and so forth for the specified logical drive.

Use the following sequence of commands to set the recommended RAID configuration:

Enter CTRL-Y to enter the Preboot CLI when prompted during boot

Enter the following Preboot CLI command to clear configuration:

TRC

Command

End of Sale UCS C260 M2 TRC1 (Extra-Large TRC)

-cfgclr -l0

End of Sale UCS C240 M3S TRC1 (Large TRC)

-cfgclr -a0

End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3)

End of Sale UCS C220 M3S TRC1 (Medium TRC)

End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3)

End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3)

End of Sale UCS C210 M2/M1 TRCs (Medium TRC)

End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2)

To determine the enclosure ID and drive numbering, which is required before you can configure RAID, run the following commands:

TRC

Command

End of Sale UCS C260 M2 TRC1 (Extra-Large TRC)

End of Sale UCS C240 M3S TRC1 (Large TRC)

-encinfo -a0 -page 20

End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3)

End of Sale UCS C220 M3S TRC1 (Medium TRC)

End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3)

End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3)

End of Sale UCS C210 M2/M1 TRCs (Medium TRC)

End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2)

The Cisco UCS Rack-Mount Server enclosure ID is not predictable, so you need to substitute the Device ID acquired above for
                                             <encl> in the commands below. When all drives are in a single enclosure, the slot numbering starts at zero. This may not be
                                             true in all cases, so verify the slot numbering with the following command:

-pdinfo -physdrv [<encl>:0] -a0

If this command generates meaningful output, the drives start at zero. If it generates an error, the drives start at one.

Use the following command to set up RAID on the existing drives on each RAID controller:

TRC

Command

End of Sale UCS C260 M2 TRC1 (Extra-Large TRC)

-cfgldadd -r5 [<encl>:1 <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7, <encl>:8 -a0

-cfgldadd -r5 [<encl>:9 <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16 -a0

End of Sale UCS C240 M3S TRC1 (Large TRC)

-cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0

–cfgldadd –r5 [<encl>:9, <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16] –a0

End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3)

End of Sale UCS C220 M3S TRC1 (Medium TRC)

-cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0

End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3)

End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3)

End of Sale UCS C210 M2/M1 TRCs (Medium TRC)

If your drives start at slot zero, run this command:

-cfgldadd -r1 [deviceID:0, deviceID:1] -a0

If your drives start at slot one, run this command:

-cfgldadd -r1 [deviceID:1, deviceID:2] -a0

If your server contains 6 total disk drives, enter the following command to configure the second RAID array:

-cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5] -a0

If your server contains 10 total disk drives, configure the second RAID array by entering one of the following commands, depending
                                                                  on the starting slot number:

If your drives start at slot zero, run this command:

-cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9] -a0

If your drives start at slot one, run this command:

-cfgldadd -r5 [ deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9, deviceID:10] -a0

End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2)

-CfgSpanAdd -r10 -Array0[enclosureID:0,enclosureID:1] -Array1[enclosureID:2,enclosureID:3] -a0

Set the Strip Size to 128 KB with the following command-line option on -cfgldadd command lines in step 5 above : -strpsz 128 . Also set required Read Policy and Write Policy described above via appropriate command line options. E.g. -cfgldadd -r5 [26:1, 26:2, 26:3, 26:4, 26:5, 26:6, 26:7, 26:8] WB RA Cached NoCachedBadBBU -strpsz 128 -a0.

The following commands are not necessary for new drives that have not been used.

- Use the -ldinit -start -l0 -a0 and –ldinit –start –l1 –a0 commands to perform a fast initialize.

We have noticed that a slow initialize can take up to 95 minutes or more to fully complete for array sizes of 1 TB+ that are used in a UCS C240 M3 Rack-Mount
                                                               Server TRC1 deployment.

After you configure the logical volume, exit the Preboot CLI by entering q .

##### What to do next

#### Configure RAID with GUI (UCS C-Series M3 Servers)

Use this procedure to configure a RAID array for a virtual drive on M3 servers. For servers with more than one virtual drive,
                                    perform these steps for each virtual drive.

##### Before you begin

During the boot process, ensure that Quiet Boot is disabled, and press Ctrl-H at the LSI screen when prompted. The MegaRaid BIOS Configuration utility opens and displays the LSI MegaRAID SAS adapters.
                                             Select Adapter 0 to begin and click Start.

Select New Configuration and click Next .

Select Manual Configuration .

On the next screen, you need to add drives to a Drive Group. Select one drive and then select all others by holding down Shift and the Down Arrow key. Click Add to Array .

Click Accept DG .

Add the drive group to a span. Select DG0 and click Add to Span .

After the drive group is part of a span, you can configure RAID on it.

Select RAID 5 or RAID 10 from the list of available options.

Cisco recommends that you select 128KB from the Strip Size drop-down list.

Set Read Policy to read ahead = always .

Set Write Policy to one of the following:

- write back with bbu –if you are using a RAID card with SuperCap (RAID-9266CV), for example.

- always write back –if you are using a RAID card with legacy Battery Backup (BBU) instead of SuperCap (for example, RAID-9266). This option helps
                                                      prevent a UC application performance impact if the BBU goes into learning mode or the battery dies.

When possible, use the new RAID cards with SuperCap and make sure the UCS is attached to an Uninterruptible Power Supply (UPS).

Click Update Size to finalize the RAID 5 volume and to determine the size of the resulting volume. A warning relating to BBU appears. Click Yes to accept a possible performance degradation if the BBU is over-tasked.

Click Next on the next screen to accept the Virtual Drive you just created (VD 0).

Click Next . At the next screen, you are presented with the option to initialize the array. Click:

Fast Initialize

Go

Set Boot Drive

Go

The RAID configuration is now complete for the first RAID controller. Go back to the controller selection by clicking on Controller selection . This time, select Adapter 1 .

Repeat all the steps that you performed for Adapter 0 with this new Adapter to set up the second RAID 5 array.

##### What to do next

#### Configure RAID with GUI (UCS C-Series M4 Servers)

Use this procedure if you have an M4 server and want to configure a RAID 5 Array on a virtual drive. For servers with more
                                    than one virtual drive, perform these steps for each virtual drive.

##### Before you begin

At the LSI screen, press CTRL-R .

Under Virtual Drive Management screen, highlight the controller, and press F2 for Operations.

If the drives are unconfigured (and the Create Virtual Drive option is not selectable), perform the following from the F2 menu:

Select Clear Configuration , then press Yes to clear the configuration.

Select Make JBOD (Just a Bunch Of Drives).

Select Make Unconfigured Good .

Select Create Virtual Drive and press Enter .

For the RAID Level option, select RAID 5 .

Tab to the Drives area. For each hard drive that you want to add to this virtual drive, select the hard drive by pressing
                                             the space bar.

Enter any name for the RAID.

Select Advanced .

Set Read Policy to read ahead = always .

For the Write Policy , select Write Back with BBU -if you are using a RAID card with SuperCap (RAID-9266CV), for example..

We recommend that you select 128-KB from the Strip Size drop-down list.

For the I/O Policy , select Cached .

For the Disk Cache Policy , select Enable .

Tab to the Initialize option and select the option by pressing the space bar.

Select OK . Press Enter .

Select OK and press Enter .

Press Ctrl-N twice to go to Ctrl Mgmt tab.

Press TAB, until the Boot Device field is selected, then press Enter .

Select the drive that you want to use to boot the virtual drive.

Press TAB multiple times to highlight Apply , then press Enter .

Press Ctrl-N until the VD Mgmt screen is displayed.

If your server has more than one virtual drive, repeat this process for each virtual drive.

##### What to do next

#### Configure RAID with CIMC RAID Configuration Utility (UCS C-Series M5)

Use this procedure if you have an M5 server and want to configure a RAID 5 Array on a virtual drive.

##### Before you begin

Login to Cisco Integrated Management Controller.

From the navigation bar, choose Cisco 12G Modular RAID controller .

Select Physical Drive Info from the menu.

Select all drives and mark them as unconfigured good.

Select the Controller Info menu.

Perform the following for each virtual drive in BE6M/H and BE7M/H.

BE6M and BE6H have only one virtual drive, whereas BE7M and BE7H has 2 and 4 virtual drives respectively.

Select the Create Virtual Drive from Unused Physical Drives link.

Select the RAID level as RAID 5 .

(Optional) Update the RAID name.

Select the number of drives from the available physical drives.

BE6M M5- all 6

BE6H M5- all 8

BE7M M5- for each of the 2 virtual drives, 7 disks

BE7H M5- for each of the 4 virtual drives, 6 disks

Set Access policy as Read Write .

Set Read policy as Always Read ahead .

Set Cache policy as Cached IO .

Set Disk Cache policy as Enabled .

Set Write policy as Write Back Good BBU .

Select OK .

Select the Virtual Drive Info menu.

Choose the created virtual drive and select Initialize button.

Choose the first virtual drive and select Set as Boot Drive button.

##### What to do next

#### Configure RAID with GUI (UCS E-Series M2 Servers)

Use this procedure if you have an M2 server and want to configure a RAID 5 Array on a virtual drive.

Configure the UCS E160D M2 for RAID5. At the time of this writing, follow the instructions in the GUI Configuration Guide
                                    for Cisco UCS E-Series Servers and the Cisco UCS E-Series Network Compute Engine Integrated Management Controller located
                                    at http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/e/3-1-1/sw/gui/config/guide/b_3_1_1_GUI_Config_Guide/b_3_x_GUI_Config_Guide_chapter_0100.html#task_2F69DDBC07194A419240DD1B09A8689B

##### Before you begin

In the Integrated Management Controller Navigation pane, click the Server tab.

2. On the Server tab, click RAID .

3. In the tabbed menu of the Storage Cards area, click the Virtual Drive Info tab.

4. In the Actions area of the Virtual Drive Info tab, click Create .

5. Complete the following fields:

Click and drag all 3 disk drives from Available Drives table to Selected Drives table. If you don’t have three disk drives,
                                                   your hardware configuration does not match the Tested Reference Configuration.

In RAID Level drop-down list, select RAID 5.

Set Strip Size to 64 KB.

Set Drive Cache to Disable.

Set Access Policy to Read-Write.

Check/enable Set this Virtual Drive Bootable.

Uncheck/disable Use the Remaining Drive as Hot Spare.

### Configure BIOS

You cannot select the hard drive in the BIOS Boot Order menu until the first logical volume has been defined. After RAID is
                                 configured, you need to make the second boot device the hard drive, as described in the following procedure:

Press indicated function key (e.g. F2 for a UCS C-Series) during boot to enter BIOS setup.

Move the cursor to Boot Options .

Verify that the CD ROM, or Cisco Virtual CD/DVD (Virtual CD/DVD drive), is selected for Boot Option #1.

Verify that the hard drive (the RAID 5 Array) is selected for Boot Option #2.

Verify that virtual threading is enabled in advanced CPU options.

Verify that VT I/O Redirection is disabled in the CPU options.

The server will now try to boot the CD ROM drive first and the hard drive second.

#### What to do next

## Install Cisco HyperFlex HX-Series Tested Reference Configurations

An example deployment including physical node placement, cabling, VLAN/subnet/IP address planning, and VM placement is available
                              at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-collaboration-storage-design-requirements.html#hyperflex .

This TRC setup process assumes HX Release 2.6 and VMware vSphere ESXi 7.0.

### Before you begin

For installation requirements, review System Requirements and Requirements for Cisco Tested Reference Configuration Installation . Also refer to the Preinstallation Checklist for Cisco HX Data Platform and Cisco HyperFlex Systems Installation Guide for
                              VMware ESXi Release 2.6, available at, https://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-data-platform-software/products-installation-guides-list.html

Perform the following tasks to install and configure a virtual machine on a Cisco HyperFlex TRC node.

Verify installation readiness, set up your 6200 Fabric Interconnect Switches, and prepare for HyperFlex node installation.

Follow instructions in the Cisco HyperFlex Systems Getting Started Guide, Release 2.6 at https://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-data-platform-software/products-installation-guides-list.html

Set up each HyperFlex node. Follow instructions in the Cisco HX240c M5 HyperFlex Node Installation Guide, Release 2.6 at http://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-series/products-installation-guides-list.html .

Complete procedure Download Virtual Machine Templates (OVA Templates) .

Download an OVA for collaboration application software, such as Cisco Unified CM onto your virtual machine.

Use vSphere to create the VM on the server:

Use vSphere to Create the VM for Servers Without Optical Drives .

Install Cisco Collaboration Applications on VMs .

Install Collaboration applications such as Cisco Unified CM on the virtual machine.

## Install and Configure VMware ESXi 7.0

The following sections provide a sequence of steps for bringing ESXi 7.0 into service at the customer site.

### Preparation for ESXi 7.0 Installation

Before you install ESXi 7.0, make sure these tasks are completed:

The BIOS boot order is configured to boot the CD-ROM or virtual CD/DVD first..

Each virtual drives on your servers has been configured with a RAID array. For RAID configuration details for your, see RAID Configuration

For additional information about ESXi storage configurations, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html .

For servers ordered as Cisco Business Edition 6000 or Cisco Business Edition 7000, these steps have been performed by the
                              factory prior to shipping.

### Install ESXi 7.0

To determine which ESXi version is required for the application you are intending to deploy, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html

Install ESXi 7.0 on one of the RAID arrays. If there are multiple RAID arrays, any is acceptable but we recommend that you
                                    install ESXi on the first.

ESXi Installation takes less than 5 minutes. After installation is complete, remove the install CD or the virtual DVD and
                                    reboot the machine.

Following a reboot, a gray and yellow ESXi console is displayed with two options:

F2 to customize the system

F12 to restart or halt the system

At this point, press F2 and configure the system in accordance with your network.

### Configuring LAN on Motherboard (LOM) NICs and Virtual Switches

The following options may be configured:

Simple vSwitch0 (default VMware virtual switch)

For larger data centers using vCenter, you can configure distributed virtual switches (for example, distributed vSwitch or
                                    the Nexus 1000V distributed virtual switch)

For all options, you must define a port group for each VLAN running on the virtual switch. These port groups are selected
                                    when configuring a Virtual Machine network adapter, to place the virtual machine on a given LAN.

### What to Do Next

Download Virtual Machine Templates (OVA Templates)

### Manage Impact of Cisco RAID Operations

Cisco Redundant Array of Independent Disks (RAID) Controller conducts background operations such as Consistency Check (CC),
                                 Background Initialization (BGI), Rebuild (RBLD), Volume Expansion & Reconstruction (RLM) and Patrol Real (PR).

## Download Virtual Machine Templates (OVA Templates)

The configuration of a Cisco Collaboration application virtual machine must match a supported virtual machine template.

There is a known issue with VMware Embedded Host Client for VMware vSphere ESXi 7.0 on BE6000 and BE7000 appliances. You require
                                          Embedded Host Client update v1.24.0, to select individual VM configurations from the Cisco-provided OVA. This file is currently
                                          available only from VMware at https://labs.vmware.com/flings as a Fling. To download the "esxui-signed-7119706.vib" Fling file, see the https://labs.vmware.com/flings/esxi-embedded-host-client and follow the VMware instructions to install the same.

### Before you begin

Install and Configure VMware ESXi 7.0

To download OVAs for Cisco Collaboration applications, go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

### What to do next

Create the VM for your server type:

Use vSphere to Create the VM for Servers with Optical Drives

Use vSphere to Create the VM for Servers Without Optical Drives

### ISO and VM Template Delivery

Depending on the servers and virtualization licenses that you purchase, virtualization software and Cisco application software
                                 can be delivered either physically or electronically.

### Use vSphere to Create the VM for Servers with Optical Drives

Cisco provides templates on a URL to download and transfer to a host. Use the following procedure to use vSphere create the
                                 VM for servers with optical drives.

#### Before you begin

Download Virtual Machine Templates (OVA Templates)

Deploy a blank virtual machine from the OVA template for your application using the Cisco.com URL as the source.

Make the CD-ROM drive available to the newly deployed VM.

Click on Options > Boot Options the next time the virtual machine boots, force entry into BIOS Setup Screen.

Insert the application installation DVD from the media kit in the system CD-ROM drive.

Power on the VM, select Boot and promote CD-ROM to boot before the hard drive.

Save the BIOS settings and boot.

#### What to do next

Install Cisco Collaboration Applications on VMs .

### Use vSphere to Create the VM for Servers Without Optical Drives

Cisco provides templates on a URL to download and transfer to a host. Use the following procedure to use vSphere create the
                                 VM for servers without optical drives.

#### Before you begin

Download Virtual Machine Templates (OVA Templates)

Deploy a blank virtual machine from the appropriate OVA template for your application using the cisco.com URL as the source.

Associate the bootable application installation ISO file with the newly deployed VM.

Set up the BIOS boot order. For instructions, see the release notes for the OVA that you are deploying.

Map the ISO-format application installer file from the media kit to the physical or virtual CD/DVD drive..

Save the BIOS settings and boot.

#### What to do next

Install Cisco Collaboration Applications on VMs

### Install Cisco Collaboration Applications on VMs

#### Installing Cisco Unified Communications Manager

For details on how to install Cisco Unified Communications Manager, refer to the Installation Guide for Cisco Unified Communications Manager at the following URL:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

#### Installing Cisco Business Edition 6000

For details on how to install Cisco Business Edition 6000, refer to the Installation Guide for Cisco Business Edition 6000 at the following URL:

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000/products-installation-guides-list.html

#### Installing Cisco Business Edition 7000

For details on how to install Cisco Business Edition 7000, refer to the Installation Guide for Cisco Business Edition 7000 at the following URL:

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/products-installation-guides-list.html

| Caution | The Extra-Small TRC (UCS E160D M2 TRC1), Small TRCs (UCS C220 M3S TRC2, UCS C240 M4S TRC1) and the Small Plus TRCs (UCS C220
                                    M3S TRC3, UCS C220 M4S TRC2) are preloaded with software if purchased as a Cisco Business Edition 6000 appliance. Certain Medium TRCs (UCS C240 M3S TRC2, UCS C240 M4S2 TRC1) and Large TRCs (UCS C240 M4SX TRC1) are preloaded with software
                                    if purchased as a Cisco Business Edition 7000 appliance. HyperFlex TRCs (HX240cM4SX TRC1) (HX220c M5SX TRC1) are preloaded with virtualization and HyperFlex software. |
|---|---|

| Step 1 | Ensure that your UCS Mini or Fabric Interconnect Switches, Blade Server Chassis, and Fabric Extenders are installed in the
                                       rack. |
|---|---|
| Step 2 | Ensure that the network connections of your UCS Mini or Fabric Interconnect Switches are connected to their designated, trunked,
                                       switch ports. |
| Step 3 | Ensure that your Fabric Interconnect Switches are properly connected to your Fabric Extenders. |
| Step 4 | Ensure that you are able to access the blade remotely using UCS Manager software. |
| Step 5 | For the remaining server installation, see Cisco documentation at http://www.cisco.com/go/ucs . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Install Cisco UCS C-Series or E-Series Server | Install the Cisco UCS Server. |
| Step 2 | Configure Cisco Integrated Management Controller | Power on the server and configure Cisco Integrated Management Controller (CIMC) for remote management. |
| Step 3 | Configure RAID using one of the following procedures: | Configure the RAID settings on your server using either the Preboot CLI or GUI indicated above. |
| Step 4 | Configure BIOS | Configure the BIOS boot order. |
| Step 5 | Install and Configure VMware ESXi 7.0 | Install and configure the VMware ESXi and the vSphere client. |
| Step 6 | Download Virtual Machine Templates (OVA Templates) | Download an OVA for collaboration application software, such as Cisco Unified Communications Manager, onto your virtual machine. |
| Step 7 | Use vSphere to create the VM on the server: Use vSphere to Create the VM for Servers with Optical Drives Use vSphere to Create the VM for Servers Without Optical Drives | Use vSphere to create the VM on the server. Map the OVA to the VM. |
| Step 8 | Install Cisco Collaboration Applications on VMs | Install Collaboration applications such as Cisco Unified Communications Manager on the virtual machine. |

| Step 1 | If UCS C-Series, install the server in the rack. If UCS E-Series, install the Cisco ISR in the rack and installe the UCS E-Series
                                          blade server into the ISR. |
|---|---|
| Step 2 | Attach the Cisco Integrated Management Controller (Cisco IMC) of the Cisco UCS C-Series or E-Series management port to the
                                          designated switch port. |
| Step 3 | Attach the UCS C-Series LAN on Motherboard (LOM) or NIC ports (or the UCS E-Series external ethernet ports if used instead
                                          of internal ethernet ports) to their designated, trunked switch ports. |
| Step 4 | Attach a VGA console, or a KVM to the VGA and keyboard ports. This step is necessary until Cisco IMC is configured. |
| Step 5 | Attach UCS C server or Cisco ISR for UCS E server to power supply. |

| Note | Virtualized Collaboration Applications does not prescribe any specific version of BIOS. The current version is assumed to
                                          be compatible with the latest release of ESXi. Business Edition appliances ship with BIOS version, configuration and settings
                                          that are compatible with the factory-preloaded release of ESXi at time of appliance build. Non-appliance servers, or appliances
                                          that have been in the field for extended period of time, may require modification of these settings. See the UCS Release,
                                          CIMC version or firmware package in UCS Interoperability Matrix as well as UCS OS drivers for ESXi. |
|---|---|

| Step 1 | Power on server. |
|---|---|
| Step 2 | During boot, press indicated function key (e.g. F8 for a UCS C-Series) to enter Cisco IMC configuration. |
| Step 3 | In the Cisco IMC configuration screen, under IPV4 (Basic): Uncheck the DHCP enabled check box using the spacebar. Enter values for the Cisco IMC IP, Subnet mask, and Gateway. |
| Step 4 | Leave VLAN (Advanced) unchecked. |
| Step 5 | Under Default User (Basic), enter the default Cisco IMC user, admin , and a password. Note The Cisco IMC username is not configurable and the setting is "admin." | Note | The Cisco IMC username is not configurable and the setting is "admin." |
| Note | The Cisco IMC username is not configurable and the setting is "admin." |
| Step 6 | Press indicated function key (e.g. F10 for a UCS C-Series) to save your settings. |
| Step 7 | After it is configured, the Cisco IMC is accessible using http. Point a browser to the IP address configured above and log
                                          in as admin, using the password configured above. |

| Note | The Cisco IMC username is not configurable and the setting is "admin." |
|---|---|

| Caution | To be supported as a Tested Reference Configuration instead of UCS Specs-based, the RAID must be set up exactly as indicated
                                             below. Do not change the RAID configuration on a server ordered as Cisco Business Edition 6000 or Cisco Business Edition 7000. |
|---|---|

| Warning | While creating data store, you must exactly follow the RAID configuration as shown in the following table or it could degrade
                                             your disk read or write performance, impacting installation, upgrade, and database synchronization. |
|---|---|

| TRC | Information |
|---|---|
| UCS C220 M5SX TRC1 (Small TRC / BE6000M M5) | One virtual drive with a RAID-5 array Six 300-GB hard drives |
| UCS C220 M5SX TRC2 (Small Plus TRC / BE6000H M5) | One virtual drive with RAID-5 Eight 300-GB hard drives |
| UCS C240 M5SX TRC1 (Medium TRC / BE7000M M5) | Two virtual drives (VDs) with RAID-5 Each VD has seven 300-GB hard drives |
| UCS C240 M5SX TRC2 (Large TRC / BE7000H M5) | Four virtual drives (VD) with RAID-5 Each VD has six 300-GB hard drives. |
| UCS C220 M4S TRC1 (Small TRC / BE6000M M4) | One virtual drive with a RAID-5 array Six 300-GB hard drives |
| UCS C220 M4S TRC2 (Small Plus TRC / BE6000H M4) | One virtual drive with RAID-5 Eight 300-GB hard drives |
| UCS C240 M4S2 TRC1 (Medium TRC / BE7000M M4) | Two virtual drives (VDs) with RAID-5 Each VD has six 300-GB hard drives |
| UCS C240 M4SX TRC1 (Large TRC / BE7000H M4) | Four virtual drives (VD) with RAID-5 Each VD has five 300-GB hard drives. |
| (End of Sale) UCS C240 M3S TRC1 (Large TRC) | Two virtual drives (VD) with RAID-5 arrays Eight 300 GB hard drives for each VD |
| (End of Sale) UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) | Two virtual drives (VD) with RAID-5 arrays Six 300-GB hard drives for each VD |
| (End of Sale) UCS C220 M3S (Medium TRC) | One virtual drive with a RAID-5 array Eight 300-GB hard drives |
| (End of Sale) UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) | One virtual drive with a RAID-5 array Eight 300-GB hard drives |
| (End of Sale) UCS C220 M3S TRC2 (Small TRC / BE6000M M3) | One virtual drive with a RAID-10 array Four 500-GB hard drives |
| UCS E160S M3 TRC1 (Extra-Small TRC) | One virtual drive with a RAID-1 array- Two 900-GB hard drives |
| (End of Sale) UCS E160D M2 TRC1 (Extra-Small TRC / BE6000S M2) | One virtual drive with a RAID-5 array Three 600-GB hard drives |
| (End of Sale) UCS C260 M2 TRC1 (Extra-Large TRC) | Two virtual drives (VD) with RAID-5 arrays Eight 300 GB hard drives for each VD |
| (End of Sale) UCS C210 M2/M1 TRCs (Medium TRC) | First 2 drives are RAID-1 (mirrored) drives with the ESXi installation. Remaining drives are RAID-5 with UC application VMs. |
| (End of Sale) UCS C200 M2 TRC1 (Small TRC / BE6000M M2) | One virtual drive with a RAID-10 array Four 1 TB hard drives |

| Important | If required, use the following settings for the Read and Write policies: If UCS C-Series, do these settings: Set Read Policy to read ahead = always . Set Write Policy to one of the following: write back with bbu – if you are using a RAID card with SuperCap (for example, RAID-9266CV). Note This write policy is not available on the C240 M3 rack-mount server TRC2. always write back – if you are using a RAID card with legacy Battery Backup (BBU) instead of SuperCap (for example, RAID-9266). This option
                                                         helps prevent a UC application performance impact if the BBU goes into learning mode or the battery dies. Whenever possible,
                                                         use the new RAID cards with SuperCap and make sure the UCS is attached to an Uninterruptible Power Supply (UPS). | Note | This write policy is not available on the C240 M3 rack-mount server TRC2. |
|---|---|---|---|
| Note | This write policy is not available on the C240 M3 rack-mount server TRC2. |

| Note | This write policy is not available on the C240 M3 rack-mount server TRC2. |
|---|---|

| Step 1 | Check your current RAID configuration: To use the Preboot CLI to configure RAID, enter Ctrl-Y . Type the following commands: TRC Command End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) -ldinfo -l0 -a0 -ldinfo -l1 -a0 End of Sale UCS C240 M3S TRC1 (Large TRC) -ldinfo -l0 -a0 -ldinfo -l1 -a0 End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) End of Sale UCS C220 M3S TRC1 (Medium TRC) -ldinfo -l0 -a0 End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) End of Sale UCS C210 M2/M1 TRCs (Medium TRC) End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) This command displays the number of drives, RAID level, and so forth for the specified logical drive. | TRC | Command | End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -ldinfo -l0 -a0 -ldinfo -l1 -a0 | End of Sale UCS C240 M3S TRC1 (Large TRC) | -ldinfo -l0 -a0 -ldinfo -l1 -a0 | End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) | End of Sale UCS C220 M3S TRC1 (Medium TRC) | -ldinfo -l0 -a0 | End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) | End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) | End of Sale UCS C210 M2/M1 TRCs (Medium TRC) | End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TRC | Command |
| End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -ldinfo -l0 -a0 -ldinfo -l1 -a0 |
| End of Sale UCS C240 M3S TRC1 (Large TRC) | -ldinfo -l0 -a0 -ldinfo -l1 -a0 |
| End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) |
| End of Sale UCS C220 M3S TRC1 (Medium TRC) | -ldinfo -l0 -a0 |
| End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) |
| End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) |
| End of Sale UCS C210 M2/M1 TRCs (Medium TRC) |
| End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) |
| Step 2 | Use the following sequence of commands to set the recommended RAID configuration: Enter CTRL-Y to enter the Preboot CLI when prompted during boot Enter the following Preboot CLI command to clear configuration: TRC Command End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) -cfgclr -l0 End of Sale UCS C240 M3S TRC1 (Large TRC) -cfgclr -a0 End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) End of Sale UCS C220 M3S TRC1 (Medium TRC) End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) End of Sale UCS C210 M2/M1 TRCs (Medium TRC) End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) | TRC | Command | End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -cfgclr -l0 | End of Sale UCS C240 M3S TRC1 (Large TRC) | -cfgclr -a0 | End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) | End of Sale UCS C220 M3S TRC1 (Medium TRC) | End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) | End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) | End of Sale UCS C210 M2/M1 TRCs (Medium TRC) | End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) |
| TRC | Command |
| End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -cfgclr -l0 |
| End of Sale UCS C240 M3S TRC1 (Large TRC) | -cfgclr -a0 |
| End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) |
| End of Sale UCS C220 M3S TRC1 (Medium TRC) |
| End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) |
| End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) |
| End of Sale UCS C210 M2/M1 TRCs (Medium TRC) |
| End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) |
| Step 3 | To determine the enclosure ID and drive numbering, which is required before you can configure RAID, run the following commands: TRC Command End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) -encinfo -l0 -page 20 End of Sale UCS C240 M3S TRC1 (Large TRC) -encinfo -a0 -page 20 End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) End of Sale UCS C220 M3S TRC1 (Medium TRC) End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) End of Sale UCS C210 M2/M1 TRCs (Medium TRC) End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) Note This command can generate more than one page of output, so enter -page 20 to look at 20 lines at a time. Look for the Device ID of the enclosure that has a nonzero Number of Physical Drives. Use
                                                         this Device ID (also called Enclosure ID) in the following commands. | TRC | Command | End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -encinfo -l0 -page 20 | End of Sale UCS C240 M3S TRC1 (Large TRC) | -encinfo -a0 -page 20 | End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) | End of Sale UCS C220 M3S TRC1 (Medium TRC) | End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) | End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) | End of Sale UCS C210 M2/M1 TRCs (Medium TRC) | End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) | Note | This command can generate more than one page of output, so enter -page 20 to look at 20 lines at a time. Look for the Device ID of the enclosure that has a nonzero Number of Physical Drives. Use
                                                         this Device ID (also called Enclosure ID) in the following commands. |
| TRC | Command |
| End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -encinfo -l0 -page 20 |
| End of Sale UCS C240 M3S TRC1 (Large TRC) | -encinfo -a0 -page 20 |
| End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) |
| End of Sale UCS C220 M3S TRC1 (Medium TRC) |
| End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) |
| End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) |
| End of Sale UCS C210 M2/M1 TRCs (Medium TRC) |
| End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) |
| Note | This command can generate more than one page of output, so enter -page 20 to look at 20 lines at a time. Look for the Device ID of the enclosure that has a nonzero Number of Physical Drives. Use
                                                         this Device ID (also called Enclosure ID) in the following commands. |
| Step 4 | The Cisco UCS Rack-Mount Server enclosure ID is not predictable, so you need to substitute the Device ID acquired above for
                                             <encl> in the commands below. When all drives are in a single enclosure, the slot numbering starts at zero. This may not be
                                             true in all cases, so verify the slot numbering with the following command: -pdinfo -physdrv [<encl>:0] -a0 If this command generates meaningful output, the drives start at zero. If it generates an error, the drives start at one. |
| Step 5 | Use the following command to set up RAID on the existing drives on each RAID controller: TRC Command End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) -cfgldadd -r5 [<encl>:1 <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7, <encl>:8 -a0 -cfgldadd -r5 [<encl>:9 <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16 -a0 End of Sale UCS C240 M3S TRC1 (Large TRC) -cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0 –cfgldadd –r5 [<encl>:9, <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16] –a0 End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) End of Sale UCS C220 M3S TRC1 (Medium TRC) -cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0 End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) End of Sale UCS C210 M2/M1 TRCs (Medium TRC) If your drives start at slot zero, run this command: -cfgldadd -r1 [deviceID:0, deviceID:1] -a0 If your drives start at slot one, run this command: -cfgldadd -r1 [deviceID:1, deviceID:2] -a0 If your server contains 6 total disk drives, enter the following command to configure the second RAID array: -cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5] -a0 If your server contains 10 total disk drives, configure the second RAID array by entering one of the following commands, depending
                                                                  on the starting slot number: If your drives start at slot zero, run this command: -cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9] -a0 If your drives start at slot one, run this command: -cfgldadd -r5 [ deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9, deviceID:10] -a0 End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) -CfgSpanAdd -r10 -Array0[enclosureID:0,enclosureID:1] -Array1[enclosureID:2,enclosureID:3] -a0 Note To clear data on previously used drives and initialize a new array, use the -ldinit -start -full -l0 command. Allow command to finish before exiting the Preboot CLI. | TRC | Command | End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -cfgldadd -r5 [<encl>:1 <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7, <encl>:8 -a0 -cfgldadd -r5 [<encl>:9 <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16 -a0 | End of Sale UCS C240 M3S TRC1 (Large TRC) | -cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0 –cfgldadd –r5 [<encl>:9, <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16] –a0 | End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) | End of Sale UCS C220 M3S TRC1 (Medium TRC) | -cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0 | End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) | End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) | End of Sale UCS C210 M2/M1 TRCs (Medium TRC) | If your drives start at slot zero, run this command: -cfgldadd -r1 [deviceID:0, deviceID:1] -a0 If your drives start at slot one, run this command: -cfgldadd -r1 [deviceID:1, deviceID:2] -a0 If your server contains 6 total disk drives, enter the following command to configure the second RAID array: -cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5] -a0 If your server contains 10 total disk drives, configure the second RAID array by entering one of the following commands, depending
                                                                  on the starting slot number: If your drives start at slot zero, run this command: -cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9] -a0 If your drives start at slot one, run this command: -cfgldadd -r5 [ deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9, deviceID:10] -a0 | End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) | -CfgSpanAdd -r10 -Array0[enclosureID:0,enclosureID:1] -Array1[enclosureID:2,enclosureID:3] -a0 | Note | To clear data on previously used drives and initialize a new array, use the -ldinit -start -full -l0 command. Allow command to finish before exiting the Preboot CLI. |
| TRC | Command |
| End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -cfgldadd -r5 [<encl>:1 <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7, <encl>:8 -a0 -cfgldadd -r5 [<encl>:9 <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16 -a0 |
| End of Sale UCS C240 M3S TRC1 (Large TRC) | -cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0 –cfgldadd –r5 [<encl>:9, <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16] –a0 |
| End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) |
| End of Sale UCS C220 M3S TRC1 (Medium TRC) | -cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0 |
| End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) |
| End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) |
| End of Sale UCS C210 M2/M1 TRCs (Medium TRC) | If your drives start at slot zero, run this command: -cfgldadd -r1 [deviceID:0, deviceID:1] -a0 If your drives start at slot one, run this command: -cfgldadd -r1 [deviceID:1, deviceID:2] -a0 If your server contains 6 total disk drives, enter the following command to configure the second RAID array: -cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5] -a0 If your server contains 10 total disk drives, configure the second RAID array by entering one of the following commands, depending
                                                                  on the starting slot number: If your drives start at slot zero, run this command: -cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9] -a0 If your drives start at slot one, run this command: -cfgldadd -r5 [ deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9, deviceID:10] -a0 |
| End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) | -CfgSpanAdd -r10 -Array0[enclosureID:0,enclosureID:1] -Array1[enclosureID:2,enclosureID:3] -a0 |
| Note | To clear data on previously used drives and initialize a new array, use the -ldinit -start -full -l0 command. Allow command to finish before exiting the Preboot CLI. |
| Step 6 | Set the Strip Size to 128 KB with the following command-line option on -cfgldadd command lines in step 5 above : -strpsz 128 . Also set required Read Policy and Write Policy described above via appropriate command line options. E.g. -cfgldadd -r5 [26:1, 26:2, 26:3, 26:4, 26:5, 26:6, 26:7, 26:8] WB RA Cached NoCachedBadBBU -strpsz 128 -a0. |
| Step 7 | The following commands are not necessary for new drives that have not been used. Use the -ldinit -start -l0 -a0 and –ldinit –start –l1 –a0 commands to perform a fast initialize. To clear data on previously used drives and to slow (or full ) initialize a new array, use the -ldinit -start -full -l0 -a0 and -ldinit -start -full -l1 -a0 commands. Allow the commands to finish before exiting the Preboot CLI. When both commands, –ldinit –showprog –l0 –a0 and –ldinit –showprog –l1 –a0 , show that initialization is not running, it is safe to exit the Preboot CLI. Note We have noticed that a slow initialize can take up to 95 minutes or more to fully complete for array sizes of 1 TB+ that are used in a UCS C240 M3 Rack-Mount
                                                               Server TRC1 deployment. | Note | We have noticed that a slow initialize can take up to 95 minutes or more to fully complete for array sizes of 1 TB+ that are used in a UCS C240 M3 Rack-Mount
                                                               Server TRC1 deployment. |
| Note | We have noticed that a slow initialize can take up to 95 minutes or more to fully complete for array sizes of 1 TB+ that are used in a UCS C240 M3 Rack-Mount
                                                               Server TRC1 deployment. |
| Step 8 | After you configure the logical volume, exit the Preboot CLI by entering q . Note The LSI adapter has factory default values for the drive rebuild rate, patrol read rate, and other settings. Cisco recommends
                                                         leaving the default values unchanged. | Note | The LSI adapter has factory default values for the drive rebuild rate, patrol read rate, and other settings. Cisco recommends
                                                         leaving the default values unchanged. |
| Note | The LSI adapter has factory default values for the drive rebuild rate, patrol read rate, and other settings. Cisco recommends
                                                         leaving the default values unchanged. |

| TRC | Command |
|---|---|
| End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -ldinfo -l0 -a0 -ldinfo -l1 -a0 |
| End of Sale UCS C240 M3S TRC1 (Large TRC) | -ldinfo -l0 -a0 -ldinfo -l1 -a0 |
| End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) |
| End of Sale UCS C220 M3S TRC1 (Medium TRC) | -ldinfo -l0 -a0 |
| End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) |
| End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) |
| End of Sale UCS C210 M2/M1 TRCs (Medium TRC) |
| End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) |

| TRC | Command |
|---|---|
| End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -cfgclr -l0 |
| End of Sale UCS C240 M3S TRC1 (Large TRC) | -cfgclr -a0 |
| End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) |
| End of Sale UCS C220 M3S TRC1 (Medium TRC) |
| End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) |
| End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) |
| End of Sale UCS C210 M2/M1 TRCs (Medium TRC) |
| End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) |

| TRC | Command |
|---|---|
| End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -encinfo -l0 -page 20 |
| End of Sale UCS C240 M3S TRC1 (Large TRC) | -encinfo -a0 -page 20 |
| End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) |
| End of Sale UCS C220 M3S TRC1 (Medium TRC) |
| End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) |
| End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) |
| End of Sale UCS C210 M2/M1 TRCs (Medium TRC) |
| End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) |

| Note | This command can generate more than one page of output, so enter -page 20 to look at 20 lines at a time. Look for the Device ID of the enclosure that has a nonzero Number of Physical Drives. Use
                                                         this Device ID (also called Enclosure ID) in the following commands. |
|---|---|

| TRC | Command |
|---|---|
| End of Sale UCS C260 M2 TRC1 (Extra-Large TRC) | -cfgldadd -r5 [<encl>:1 <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7, <encl>:8 -a0 -cfgldadd -r5 [<encl>:9 <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16 -a0 |
| End of Sale UCS C240 M3S TRC1 (Large TRC) | -cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0 –cfgldadd –r5 [<encl>:9, <encl>:10, <encl>:11, <encl>:12, <encl>:13, <encl>:14, <encl>:15, <encl>:16] –a0 |
| End of Sale UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) |
| End of Sale UCS C220 M3S TRC1 (Medium TRC) | -cfgldadd -r5 [<encl>:0, <encl>:1, <encl>:2, <encl>:3, <encl>:4, <encl>:5, <encl>:6, <encl>:7] -a0 |
| End of Sale UCS C220 M3S TRC3 (Small Plus TRC / BE6000H M3) |
| End of Sale UCS C220 M3S TRC2 (Small TRC / BE6000M M3) |
| End of Sale UCS C210 M2/M1 TRCs (Medium TRC) | If your drives start at slot zero, run this command: -cfgldadd -r1 [deviceID:0, deviceID:1] -a0 If your drives start at slot one, run this command: -cfgldadd -r1 [deviceID:1, deviceID:2] -a0 If your server contains 6 total disk drives, enter the following command to configure the second RAID array: -cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5] -a0 If your server contains 10 total disk drives, configure the second RAID array by entering one of the following commands, depending
                                                                  on the starting slot number: If your drives start at slot zero, run this command: -cfgldadd -r5 [deviceID:2, deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9] -a0 If your drives start at slot one, run this command: -cfgldadd -r5 [ deviceID:3, deviceID:4, deviceID:5, deviceID:6, deviceID:7, deviceID:8, deviceID:9, deviceID:10] -a0 |
| End of Sale UCS C200 M2 TRC1 (Small TRC / BE6000M M2) | -CfgSpanAdd -r10 -Array0[enclosureID:0,enclosureID:1] -Array1[enclosureID:2,enclosureID:3] -a0 |

| Note | To clear data on previously used drives and initialize a new array, use the -ldinit -start -full -l0 command. Allow command to finish before exiting the Preboot CLI. |
|---|---|

| Note | We have noticed that a slow initialize can take up to 95 minutes or more to fully complete for array sizes of 1 TB+ that are used in a UCS C240 M3 Rack-Mount
                                                               Server TRC1 deployment. |
|---|---|

| Note | The LSI adapter has factory default values for the drive rebuild rate, patrol read rate, and other settings. Cisco recommends
                                                         leaving the default values unchanged. |
|---|---|

| Step 1 | During the boot process, ensure that Quiet Boot is disabled, and press Ctrl-H at the LSI screen when prompted. The MegaRaid BIOS Configuration utility opens and displays the LSI MegaRAID SAS adapters.
                                             Select Adapter 0 to begin and click Start. |
|---|---|
| Step 2 | Select New Configuration and click Next . |
| Step 3 | Select Manual Configuration . |
| Step 4 | On the next screen, you need to add drives to a Drive Group. Select one drive and then select all others by holding down Shift and the Down Arrow key. Click Add to Array . |
| Step 5 | Click Accept DG . |
| Step 6 | Add the drive group to a span. Select DG0 and click Add to Span . |
| Step 7 | After the drive group is part of a span, you can configure RAID on it. Select RAID 5 or RAID 10 from the list of available options. Cisco recommends that you select 128KB from the Strip Size drop-down list. |
| Step 8 | Set Read Policy to read ahead = always . |
| Step 9 | Set Write Policy to one of the following: - write back with bbu –if you are using a RAID card with SuperCap (RAID-9266CV), for example. - always write back –if you are using a RAID card with legacy Battery Backup (BBU) instead of SuperCap (for example, RAID-9266). This option helps
                                                      prevent a UC application performance impact if the BBU goes into learning mode or the battery dies. Note When possible, use the new RAID cards with SuperCap and make sure the UCS is attached to an Uninterruptible Power Supply (UPS). | Note | When possible, use the new RAID cards with SuperCap and make sure the UCS is attached to an Uninterruptible Power Supply (UPS). |
| Note | When possible, use the new RAID cards with SuperCap and make sure the UCS is attached to an Uninterruptible Power Supply (UPS). |
| Step 10 | Click Update Size to finalize the RAID 5 volume and to determine the size of the resulting volume. A warning relating to BBU appears. Click Yes to accept a possible performance degradation if the BBU is over-tasked. |
| Step 11 | Click Next on the next screen to accept the Virtual Drive you just created (VD 0). |
| Step 12 | Click Next . At the next screen, you are presented with the option to initialize the array. Click: Fast Initialize Go Set Boot Drive Go |
| Step 13 | The RAID configuration is now complete for the first RAID controller. Go back to the controller selection by clicking on Controller selection . This time, select Adapter 1 . |
| Step 14 | Repeat all the steps that you performed for Adapter 0 with this new Adapter to set up the second RAID 5 array. |

| Note | When possible, use the new RAID cards with SuperCap and make sure the UCS is attached to an Uninterruptible Power Supply (UPS). |
|---|---|

| Step 1 | At the LSI screen, press CTRL-R . The Virtual Drive Management screen displays the list of unconfigured hard drives for the virtual drive. |
|---|---|
| Step 2 | Under Virtual Drive Management screen, highlight the controller, and press F2 for Operations. |
| Step 3 | If the drives are unconfigured (and the Create Virtual Drive option is not selectable), perform the following from the F2 menu: Note You can skip this step if the Create Virtual Drive option is selectable. Select Clear Configuration , then press Yes to clear the configuration. Select Make JBOD (Just a Bunch Of Drives). Select Make Unconfigured Good . | Note | You can skip this step if the Create Virtual Drive option is selectable. |
| Note | You can skip this step if the Create Virtual Drive option is selectable. |
| Step 4 | Select Create Virtual Drive and press Enter . |
| Step 5 | For the RAID Level option, select RAID 5 . |
| Step 6 | Tab to the Drives area. For each hard drive that you want to add to this virtual drive, select the hard drive by pressing
                                             the space bar. When the drive is selected, an X appears in the ID box. |
| Step 7 | Enter any name for the RAID. |
| Step 8 | Select Advanced . |
| Step 9 | Set Read Policy to read ahead = always . |
| Step 10 | For the Write Policy , select Write Back with BBU -if you are using a RAID card with SuperCap (RAID-9266CV), for example.. We recommend that you select 128-KB from the Strip Size drop-down list. |
| Step 11 | For the I/O Policy , select Cached . |
| Step 12 | For the Disk Cache Policy , select Enable . |
| Step 13 | Tab to the Initialize option and select the option by pressing the space bar. An X displays in the Initialize box. |
| Step 14 | Select OK . Press Enter . When the Initialization is complete, a popup appears. |
| Step 15 | Select OK and press Enter . The Virtual Drive Management screen appears. |
| Step 16 | Press Ctrl-N twice to go to Ctrl Mgmt tab. |
| Step 17 | Press TAB, until the Boot Device field is selected, then press Enter . |
| Step 18 | Select the drive that you want to use to boot the virtual drive. |
| Step 19 | Press TAB multiple times to highlight Apply , then press Enter . The Back Initialization process begins. It may take several minutes to initialize the virtual drive. |
| Step 20 | Press Ctrl-N until the VD Mgmt screen is displayed. |
| Step 21 | If your server has more than one virtual drive, repeat this process for each virtual drive. |

| Note | You can skip this step if the Create Virtual Drive option is selectable. |
|---|---|

| Step 1 | Login to Cisco Integrated Management Controller. |
|---|---|
| Step 2 | From the navigation bar, choose Cisco 12G Modular RAID controller . |
| Step 3 | Select Physical Drive Info from the menu. |
| Step 4 | Select all drives and mark them as unconfigured good. |
| Step 5 | Select the Controller Info menu. |
| Step 6 | Perform the following for each virtual drive in BE6M/H and BE7M/H. Note BE6M and BE6H have only one virtual drive, whereas BE7M and BE7H has 2 and 4 virtual drives respectively. Select the Create Virtual Drive from Unused Physical Drives link. Select the RAID level as RAID 5 . (Optional) Update the RAID name. Select the number of drives from the available physical drives. BE6M M5- all 6 BE6H M5- all 8 BE7M M5- for each of the 2 virtual drives, 7 disks BE7H M5- for each of the 4 virtual drives, 6 disks Set Access policy as Read Write . Set Read policy as Always Read ahead . Set Cache policy as Cached IO . Set Disk Cache policy as Enabled . Set Write policy as Write Back Good BBU . Select OK . Select the Virtual Drive Info menu. Choose the created virtual drive and select Initialize button. Choose the first virtual drive and select Set as Boot Drive button. | Note | BE6M and BE6H have only one virtual drive, whereas BE7M and BE7H has 2 and 4 virtual drives respectively. |
| Note | BE6M and BE6H have only one virtual drive, whereas BE7M and BE7H has 2 and 4 virtual drives respectively. |

| Note | BE6M and BE6H have only one virtual drive, whereas BE7M and BE7H has 2 and 4 virtual drives respectively. |
|---|---|

| Step 1 | In the Integrated Management Controller Navigation pane, click the Server tab. |
|---|---|
| Step 2 | 2. On the Server tab, click RAID . |
| Step 3 | 3. In the tabbed menu of the Storage Cards area, click the Virtual Drive Info tab. |
| Step 4 | 4. In the Actions area of the Virtual Drive Info tab, click Create . |
| Step 5 | 5. Complete the following fields: Click and drag all 3 disk drives from Available Drives table to Selected Drives table. If you don’t have three disk drives,
                                                   your hardware configuration does not match the Tested Reference Configuration. In RAID Level drop-down list, select RAID 5. Set Strip Size to 64 KB. Set Drive Cache to Disable. Set Access Policy to Read-Write. Check/enable Set this Virtual Drive Bootable. Uncheck/disable Use the Remaining Drive as Hot Spare. |

| Step 1 | Press indicated function key (e.g. F2 for a UCS C-Series) during boot to enter BIOS setup. |
|---|---|
| Step 2 | Move the cursor to Boot Options . |
| Step 3 | Verify that the CD ROM, or Cisco Virtual CD/DVD (Virtual CD/DVD drive), is selected for Boot Option #1. |
| Step 4 | Verify that the hard drive (the RAID 5 Array) is selected for Boot Option #2. |
| Step 5 | Verify that virtual threading is enabled in advanced CPU options. |
| Step 6 | Verify that VT I/O Redirection is disabled in the CPU options. The server will now try to boot the CD ROM drive first and the hard drive second. |

| Note | This TRC setup process assumes HX Release 2.6 and VMware vSphere ESXi 7.0. |
|---|---|

| Step 1 | Verify installation readiness, set up your 6200 Fabric Interconnect Switches, and prepare for HyperFlex node installation. Follow instructions in the Cisco HyperFlex Systems Getting Started Guide, Release 2.6 at https://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-data-platform-software/products-installation-guides-list.html |
|---|---|
| Step 2 | Set up each HyperFlex node. Follow instructions in the Cisco HX240c M5 HyperFlex Node Installation Guide, Release 2.6 at http://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-series/products-installation-guides-list.html . |
| Step 3 | Complete procedure Download Virtual Machine Templates (OVA Templates) . |
| Step 4 | Download an OVA for collaboration application software, such as Cisco Unified CM onto your virtual machine. |
| Step 5 | Use vSphere to create the VM on the server: Use vSphere to Create the VM for Servers Without Optical Drives . |
| Step 6 | Install Cisco Collaboration Applications on VMs . |
| Step 7 | Install Collaboration applications such as Cisco Unified CM on the virtual machine. |

| Note | You can install ESXi on the first RAID array. It is not required that you install ESXi on both arrays. |
|---|---|

| Note | There is a known issue with VMware Embedded Host Client for VMware vSphere ESXi 7.0 on BE6000 and BE7000 appliances. You require
                                          Embedded Host Client update v1.24.0, to select individual VM configurations from the Cisco-provided OVA. This file is currently
                                          available only from VMware at https://labs.vmware.com/flings as a Fling. To download the "esxui-signed-7119706.vib" Fling file, see the https://labs.vmware.com/flings/esxi-embedded-host-client and follow the VMware instructions to install the same. |
|---|---|

| To download OVAs for Cisco Collaboration applications, go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . |
|---|

| Step 1 | Deploy a blank virtual machine from the OVA template for your application using the Cisco.com URL as the source. |
|---|---|
| Step 2 | Make the CD-ROM drive available to the newly deployed VM. |
| Step 3 | Click on Options > Boot Options the next time the virtual machine boots, force entry into BIOS Setup Screen. |
| Step 4 | Insert the application installation DVD from the media kit in the system CD-ROM drive. |
| Step 5 | Power on the VM, select Boot and promote CD-ROM to boot before the hard drive. |
| Step 6 | Save the BIOS settings and boot. The installation screens for your application appear at this point. |

| Step 1 | Deploy a blank virtual machine from the appropriate OVA template for your application using the cisco.com URL as the source. |
|---|---|
| Step 2 | Associate the bootable application installation ISO file with the newly deployed VM. |
| Step 3 | Set up the BIOS boot order. For instructions, see the release notes for the OVA that you are deploying. |
| Step 4 | Map the ISO-format application installer file from the media kit to the physical or virtual CD/DVD drive.. |
| Step 5 | Save the BIOS settings and boot. The normal installation screen for your application opens. |