---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be7000-installationguide-12-5-be7k-b-installation-guide-m5-1251-be7k-b--74030c4c03
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE7000/installationguide/12_5/be7k_b_installation-guide-M5-1251/be7k_b_installation-guide-1251_chapter_01.html
retrieved_at: 2026-08-17T01:47:13.376069+00:00
---

Installation Guide for Cisco Business Edition 7000H/M (M5), Release 12.5

# Installation Guide for Cisco Business Edition 7000H/M (M5), Release 12.5

Updated: February 19, 2021

Chapter: Installation of Cisco Business Edition 7000H/M

## Chapter: Installation of Cisco Business Edition 7000H/M

# Installation of Cisco Business Edition 7000H/M

## Design Your Deployment

Review the following topics to design your deployment.

### Plan Your UC Applications

Before You Begin:

Ensure that your Cisco Business Edition 7000 server is rack-mounted and connected to power and data networks. For instructions, refer to the Quick Start Guide for Cisco Business Edition that was packaged with your server. You can also download a copy at:

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/products-installation-guides-list.html

Before you begin any installation, plan which UC applications you are going to install.

For information on the UC applications that are available for installation, and on how to design your Business Edition collaboration
                                 deployment refer to the following sites:

Cisco Business Edition 6000 and Cisco Business Edition 7000 Co-residency Policy Requirements —This document contains information on the Cisco virtualized applications that are available for installation on a Cisco Business
                                       Edition 7000 system and the conditions that you must meet to run those applications and any third-party applications on a
                                       Business Edition server.

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/products-implementation-design-guides-list.html

Unified Communications in a Virtualized Environment —This website contains information on Cisco Collaboration Virtualization applications and how to design your deployment.

http://www.cisco.com/go/virtualized-collaboration

Preferred Architecture Guides for Enterprise —Preferred Architecture documents and CVD guides offer prescriptive, end-to-end system solutions for Collaboration and Voice
                                       deployment. The design overviews provide a basic understanding of the products and their roles in the Preferred Architectures,
                                       including high-level best practices. The CVD guides provide more detailed design and deployment recommendations that help
                                       streamline the implementation of Preferred Architectures.

http://www.cisco.com/go/pa

Enterprise Collaboration CVD Guides — Enterprise CVDs provide detailed design and step-by-step deployment information for collaboration solutions that are built on the Cisco
                                       Business Edition 7000 . These CVDs are based on the core recommendations of the Preferred Architectures, and in some cases, they offer more solution
                                       designs as extensions or alternatives to the Preferred Architectures.

http://www.cisco.com/go/pa

Business Edition 7000 Software Load Summary —Preload Summary documents provide information on ISO and OVA files that are pre-loaded in your server's datastore.

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000/products-release-notes-list.html

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/products-release-notes-list.html

### Collect Required Network Information

Before you begin the installation, collect the following network information for your solution.

Collect the following network settings for your installation:

Subnet mask

Gateway IP Address

VMware vSphere ESXi management IP address

Cisco Integrated Management Controller (CIMC) IP address

UC application IP addresses

DNS server IP address

UC application hostnames

(Optional) Domain name

NTP server IP address

Time zone

(Optional) SMTP server

For general information on the Cisco UCS C240 M5 server used in Cisco Business Edition 7000, see the Cisco UCS C240 M5 Server Installation and Service Guide .

Decide how you will interconnect the appliance to your network. Specifics on network interconnection options are beyond the
                                 scope of this guide, but below are some important callouts.

For the full range of possible configuration settings options, consult Cisco UCS C240 M5 Rack Server (Small Form Factor Disk Drive Model) Spec Sheet , Cisco UCS C Server Installation and Service Guide and docs.vmware.com.

Available physical ethernet ports depend on the appliance model:

All M5 appliance models include modular LAN on motherboard ports as described in the Cisco UCS C240 M5 Rack Server (Small Form Factor Disk Drive Model) Spec Sheet .

BE7000M and BE7000H models include additional ports via a network interface card.

It is not supported on any appliance model to add network interface cards, add virtual interface cards, or change included
                                       network interface card.

Available VMware vSphere ESXi configuration settings options depend on what license is being used. If your appliance is using
                                             an embedded virtualization license,VMware vSphere ESXi distributed virtual switch features are not enabled.

## Set Up Your Appliance

Review the following topics before you begin your installation.

### Hardware Setup

#### Unpack Hardware

This section describes the tasks that you must perform to unpack and install the Cisco Business Edition 7000 hardware.

Unpack the BE7000 appliance and verify that all of the following items are present. If any item is missing or appears to be
                                 damaged, contact your supplier immediately.

Business Edition 7000 appliance (derived from Cisco UCS C240 M5SX)

Rack-mounting kit

Power cords

Ethernet cable

Console cable

License document for embedded virtualization, if purchased (For example, Cisco UC Virtualization Foundation or Cisco Collaboration
                                       Virtualization Standard).

If you purchased an embedded license, record and store the embedded virtualization license key in a safe place. This key will
                                                   be required if the software needs to be reinstalled in the future.

For your safety, before you work on any equipment, be aware of the hazards that are involved with electrical circuitry and
                                 be familiar with standard practices for preventing accidents.

#### Install BE7000 Hardware

##### Before you begin

Ensure that you have the following before you begin hardware installation:

Enough space in a standard 19-inch equipment rack (2 RU for each appliance)

110 / 220 VAC power feeds

Ethernet network port(s) configured for the appliance's network connection(s)

If you have purchased a keyboard-video-monitor dongle, VGA monitor and USB keyboard (not supplied) – for initial installation
                                          only.

See the figure and table below for components of front and rear panels of the BE7000 appliance (derived from UCS C240 M5SX).

Front Panel

1

UCSC-C240-M5SX: Drive bays 1—24 support SAS/SATA drives

2

UCSC-220-M5SX: Drive bays 1 and 2 support NVMe PCIe SSDs

3

Power button/power status LED

4

Unit identification button/LED

5

System status LED

6

Fan status LED

7

Temperature status LED

8

Power supply status LED

9

Network link activity LED

10

Pull-out asset tag

11

KVM connector (used with KVM cable that provides one DB-15 VGA, one DB-9 serial, and two USB connectors)

Rear Panel

1

PCIe riser 1 (PCIe slot 1, 2, 3)

2

PCIe riser 2 (PCIe slots 4, 5, 6)

3

Rear 2.5-inch drive bays

4

Power supplies (two, redundant as 1+1)

5

Threaded holes for dual-hole grounding lug

6

Modular LAN-on-motherboard (mLOM) card slot (x16)

7

USB 3.0 ports (two)

8

Dual 1-Gb/10-Gb Ethernet ports (LAN1 and LAN2)

9

VGA video port (DB-15 connector)

10

1-Gb Ethernet dedicated management port

11

Serial port (RJ-45 connector)

12

Rear unit identification button/LED

See the following figures for details on rack-mounting hardware:

Step 1

Remove the slide rails from the top of the appliance's box and unpack them.

Step 2

At the end of one of the rails marked FRONT, slide the green tab in the direction of the arrow (A1) until the securing plate
                                             is latched in the open position (A2).

Step 3

At the desired height, engage the FRONT mounting pegs in to the front post of the equipment rack with the rail extending toward
                                             the rear (B1). Press the green release button (B2) to allow the plate to slide forward to secure the front mount (B3).

Step 4

Hold the rear securing latch open (C1) and extend the rail until the rear mounting pegs engage in the rear rack post at the
                                             same height as the front (C2). Release the rear latch, so that the latch wraps securely around the rear post (C3).

Step 5

Repeat Steps 2 to 4 for the second rail on the other side of the rack. Ensure that you install the rails at the same height.

Step 6

Pull the inner slide rails from the front of each assembly until they lock in place.

Step 7

Remove the appliance from its box and remove all packaging.

Step 8

Point the rear of the appliance toward the front of the rack and align the pre-fitted rails with the extended slide rails.

Step 9

Push the appliance in to the rack rails until the appliance meets the internal stops.

Step 10

Press the plastic release clips marked PUSH on each rail and push the appliance in to the rack until the appliance latches
                                             to the front rack-mount clips.

Step 11

Connect Ethernet Port 1 (and other Ethernet Ports, if required) to the data network.

Step 12

Connect the dedicated management Ethernet interface to the management network, if required for Lights-Out Management.

Step 13

Connect a monitor and keyboard using the rear VGA and USb connectors (or to the front KVM adapter if you purchased one).

Step 14

Connect the power supplies to the electrical outlets. Do not power on the server at this time.

### Installation of Virtualization and Application Software

This section describes the tasks that you must perform to install virtualization and application software on your Business
                                 Edition 7000 , using the factory preload.

### Installation Task Flow of Cisco Business Edition 7000H/M

Perform the following tasks to install software on your Cisco Business Edition 7000 server.

Step 1

Configure Cisco Integrated Management Controller

Configure CIMC for your Business Edition 7000 server.

Step 2

Customer Virtualization Software Remote Access

Configure the pre-installed VMware vSphere ESXi software on the appliance.

Step 3

Delete Unused or Unwanted Preloaded files

Delete any pre-deployed VMs that you do not require.

#### Configure Cisco Integrated Management Controller

Cisco Integrated Management Controller (CIMC) is the management interface for the Cisco UCS appliance . CIMC runs within the appliance , allowing remote administration, configuration, and monitoring of the appliance through web or SSH command-line access.

Complete the following tasks to configure CIMC on a Business Edition 7000 appliance for customized and preconfigured deployments.

Complete the following tasks to Configure Cisco Integrated Management Controller:

Step 1

Power On and Initial CIMC Setup

Step 2

Complete the CIMC Configuration

##### Power on and Initial CIMC Setup

Use this procedure to power on the appliance and begin the basic Cisco Integrated Management controller (CIMC) configuration.

###### Before you begin

Ensure that the Business Edition 7000 appliance has been rack-mounted, connected to a power supply, connected to the data network, and that a monitor and keyboard are connected
                                       to the appliance , as described in the Quick Start Guide .

Step 1

Verify that power is connected and that the power button LED is orange.

Step 2

Push the appliance power button and verify that it changes to green.

Step 3

Watch the boot process on the monitor.

Step 4

When the blue Cisco logo appears, press F8 to enter the CIMC configuration dialog.

Step 5

When prompted, enter the username admin and create a new password.

Step 6

On the CIMC configuration screen, complete the following details:

- CIMC IP address

- Subnet mask

- Gateway IP address

Step 7

When complete, press F10 to save your changes and boot the system.

##### Complete the CIMC Configuration

Use this procedure to configure DNS and NTP settings in the CIMC interface.

###### Before you begin

Step 1

In a web browser, enter the CIMC IP address and log in with the username admin and the password that you created in the previous task.

Step 2

From the left hand menu, select the Admin tab, and click Network .

Step 3

In the main screen, select the Network Settings tab.

Step 4

From Common Properties , change the Hostname setting to the CIMC hostname.

Step 5

From IPv4 Properties , change Preferred DNS Server to the IP address that you have specified for the DNS server.

Step 6

In the main screen, select the NTP Settings tab.

Step 7

Check the Enable NTP check box.

Step 8

In the Server 1 field, enter the NTP server IP address.

Step 9

Select Save Changes from the bottom right hand corner of the page.

###### What to do next

Customize Virtualization Hyoervisor for Remote Access

#### Configure VMware vSphere Hypervisor

Complete the following tasks to set up the VMware vSphere hypervisor :

Step 1

Customize VMware vSphere hypervisor Remote Access.

Step 2

Access and Configure the VMware vSphere hypervisor .

##### Customize Virtualization Software Remote Access

Follow this procedure to customize the VMware vSphere ESXi to enable remote access from your PC using the VMware Embedded
                                       Host Client.

If you use ESXi 6.5, then you must select VMFS5 file type to create the datastore.

Step 1

When the hypervisor boots, the ESXi Direct Console User Interface displays on the monitor as shown in the following figure.

Step 2

Press F2 to enter the System Customization menu as shown in the following figure.

Step 3

Choose Configure Password to change the password.

If your applications are predeployed, skip to 5 .

Step 4

To assign a static IP address, select the Configure Management Network menu, and follow the instructions on the screen to change "IP Configuration" .

Step 5

Connect your PC to the data network, and browse to the new hypervisor IP address.

###### What to do next

Access and Configure Virtualization Software

##### Access and Configure Virtualization Software

Some Business Edition applications require the host to have a valid time reference. Follow these steps to access the ESXi
                                       host to configure NTP and configure fault tolerance for network interface cards (NICs) using the NIC teaming feature, view
                                       preinstalled applications, and browse the datastore to verify the preloaded collaboration application software.

Step 1

Browse to the "https://[ESXI-HOST-IP-Address]/ui/" to access VMware Embedded Host Client.

Step 2

Use the login credentials that you previously configured.

Step 3

If selected at time of quoting, BE 7000 appliances are factory loaded with a Collaboration embedded OEM license for Cisco UC Virtualization . If you want to use
                                                this license, it is ready for use. If you want to re upload or version-upgrade this license, follow these steps:

Locate your license document that has license serial number for the Cisco UC Virtualization . For installations, license serial
                                                      number ships from the factory along with the appliance. For version-upgrades, license serial number ships from the Cisco Product
                                                      Upgrade Tool.

Navigate to Manage > License > Assign License .

Type in or copy or paste the license serial number from the license document.

Click Check License to validate the license key.

License for the Cisco UC Virtualization Hypervisor Plus , Cisco UC Virtualization Foundation or Cisco Collaboration Virtualization Standard is a special Cisco Collaboration embedded OEM license. It is hardcoded to 2-CPU, pre combined, and cannot split or expand
                                                               through myvmware.com. It is neither a VMware Partner Activation Code (PAC) nor a Cisco Product Authorization Key (PAK). It is pre activated, no registration or activation on myvmware.com or cisco.com required. It does not support installation
                                                               through vCenter, license pooling in vCenter, or any vCenter features.

For more details, see the http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html#license_comparison .

Step 4

Configure NTP settings:

Navigate to Manage > System > Time & date .

Click Edit settings to launch the Edit time configuration screen.

Check Manually configure the date and time on this host check box.

Update the Time.

Check the Use Network Time Protocol (enable NTP client) check box.

Select Start and stop with host from NTP service startup policy drop-down.

Type the IP address of NTP server in NTP servers . If you want to add multiple NTP servers, type the IP address of NTP servers that are separated by commas.

Click Save .

Step 5

(Optional) Configure fault tolerance by using the NIC teaming feature in VMware:

Navigate to the Networking > Management Network .

Click Edit settings to launch Edit port group- Management Network .

In the Edit port group- Management Network screen, enter the name, VLANID, Virtual switch.

Expand NIC teaming, enter the required details.

Click Save to add the NIC that is connected to the data network.

By default, only one NIC is enabled for the hypervisor and identified as vmnic0.

Step 6

Browse the datastore:

Navigate to Storage > Datastore to list the datastores in the Business Edition appliance.

Select datastore1.

Click the Datastore browser . You can view the Preloaded Collaboration Virtual Machines and preloaded software.

You must select the VMFS5 file type while creating the datastore.

Step 7

(Optional) Cisco recommends that you archive the OVA-ISO directory locally. If a appliance fails, the replacement product does not include preloaded content.

###### What to do next

Delete Unused or Unwanted Virtual Machines

#### Delete Unused or Unwanted Virtual Machines

You can optionally delete unused or unwanted preloaded files to free up disk space or make room for subsequent installations
                                    in the following scenarios:

If you want to deploy a new application version or patch level than the existing factory-preloaded application.

If you do not want to run a particular preloaded application and its files.

Step 1

Log in to VMware Embedded Host Client .

Step 2

Expand Virtual Machines and locate the virtual machine that you want to delete.

Step 3

If the VM has
                                             			 a green triangle, right-click the icon and select Power > Power
                                                   				  Off .

Step 4

Right-click the VM and select Delete .

Step 5

Repeat this
                                             			 procedure for each virtual machine that you wish to remove.

## Set Up Your Applications

Perform the following tasks to set up your applications on Cisco Business Edition 7000 appliance .

Step 1

Deploy Virtual Machine OVAs

Deploy virtual machine OVAs for each UC application that you want to install.

Step 2

Customize Virtual Machines for Cisco Unity Connection

If your Business Edition 7000 deployment includes Cisco Unity Connection, customize the Unity Connection VM.

Step 3

Associate Application ISO Files to Virtual Machines

For UC application installations that require an ISO file, mount the ISO file on the application VM.

Step 4

Install UC Applications Using Touchless Installation

Optional. Use touchless installation to install any of the following core UC applications:

Cisco Unified Communications Manager

IM and Presence Service

Cisco Unity Connection

Cisco Unified Contact Center Express

Step 5

Install UC Applications Manually

Use the manual interactive process to install any remaining UC applications.

### Deploy Virtual Machine OVAs

For each application that you want to run, requires one of the preloaded virtual machine OVA files. If a new version is preferred,
                                 then it is recommended to delete the existing version.

Depending on the preloaded application, the OVA contains any of the following applications:

Fully installed ready to run application

Partially installed application

VM configuration alone for an empty virtual machine

For more details, see the Preload File Summaries in Release Notes at the http://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/products-release-notes-list.html .

The OVA template files that contain empty virtual machines are deployed in seconds, while larger OVA files that contain partially
                                             or fully installed applications can take longer to deploy.

Caution

Step 1

On the VMware Embedded Host Client, navigate to the Virtual Machines .

Step 2

Right-click the Virtual machines and select the Create/Register VM .

Step 3

Select Deploy a virtual machine from an OVF or OVA file as select creation type.

Step 4

Specify a meaningful name for the virtual machine.

Step 5

Browse and select the source OVA template file on your PC. For application and filename mapping, see the Build Summary PDF
                                          in the datastore OVA-ISO directory, or download from here: https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/products-release-notes-list.html .

Step 6

Select the datastore in which to store the configuration and disk files.

Step 7

Select the deployment options.

Step 8

If prompted to accept license agreements, continue to click Next .

Step 9

Select the deployment options.

Step 10

If prompted for the Disk Format , specify Thick Provision Lazy Zero .

Step 11

Review your settings selection before finishing the wizard.

Step 12

Click Next .

Step 13

Deploy VMs for all your UC applications before proceeding to the next task.

If your system includes Cisco Unity Connection, then Customize Virtual Machines for Cisco Unity Connection . Otherwise, Associate Application ISO Files to Virtual Machines .

### Customize Virtual Machines for Cisco Unity Connection

For Customized installations, use this procedure to configure your Cisco Unity Connection virtual machine settings to ensure
                                 optimum performance.

#### Before you begin

For Customized installations, use this procedure to configure your Cisco Unity Connection virtual machine settings to ensure
                                 optimum performance. Deploy Virtual Machine OVAs

Step 1

On VMware Embedded Host Client, navigate to the Virtual Machines .

Step 2

Right click the Unity Connection entry and select Edit Settings .

Step 3

If you want to use the Unity Connection, or Unified, or Integrated Messaging, do the following:

Select the Virtual Hardware tab.

Select the CPU menu and set the number of Cores per Sockets to 2 .

In the Reservation tab, increase the reservation to 5.06MHz .

For more information, see the https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

### Associate Application ISO Files to Virtual Machines

If you have deployed a skip-install OVA that contains any of the following partially installed applications, skip this step.

Cisco Unified Communications Manager

IM and Presence Service

Cisco Unity Connection

Cisco Unified Contact Center Express

Cisco Emergency Responder

If you have deployed an OVA that contains ready to run fully installed applications, skip this step.

For all other OVA files that contain only VM configurations of empty virtual machines, use this procedure to associate the
                                 ISO installation files that is used to complete the installation.

Step 1

In the VMware Embedded Host Client, select the UC application virtual machine.

Step 2

Click Edit .

Step 3

From Virtual Hardware tab, select CD/DVD Drive 1 .

Step 4

Select Datastore ISO File from CD/DVD Drive 1 drop-down list.

Step 5

Browse to the datastore and locate the application ISO file.

Step 6

Select the file and click Select .

Step 7

In CD/DVD Drive 1 , check the Connect at power on check box under the Status .

Step 8

Repeat this procedure for each application that you want to install that includes an ISO file.

### Install UC Applications Using Touchless Installation

Touchless installation allows you to install multiple UC applications and virtual machines of an application simultaneously, across the different hosts if necessary, without having to interact with the system while the install process runs. While you must prepare the
                                 system, touchless installation can save time, particularly if you want to install multiple applications. If you are installing
                                 only one or two applications, you may prefer to follow the manual procedure in the following section.

Use touchless installation to install the following applications:

Cisco Unified Communications Manager

IM and Presence Service

Cisco Unity Connection

Cisco Unified Contact Center Express

Cisco Prime Collaboration Deployment

Step 1

Generate Answer Files

Generate answer files (AFG files) for UC applications.

Step 2

Create Virtual Floppy Images

Use your AFG files to create virtual floppy images.

Step 3

Upload Virtual Floppy Images to Datastore

Upload your virtual floppy images to the datastore.

Step 4

Mount Virtual Floppy on Virtual Machines and Set Boot Option

Mount each virtual floppy on the corresponding UC application VM.

Step 5

Run Touchless Installation

Run the touchless installation of your UC applications. We recommend that you run your installations simultaneously.

#### Generate Answer Files

Use this procedure to generate answer files for the touchless installation of your UC applications.

Tip

Step 1

Go to the online answer file generator at: https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html .

Step 2

From the Product drop-down list, select the UC application for which you want to generate answer files.

Step 3

Select the Version that you want to install.

Step 4

Complete the remaining fields with the installation details that you want to configure on the appliance . For example, you can assign items such as passwords, IP addressing, and DNS settings.

Step 5

Click Generate Answer Files to generate the platformConfig.xml file for that UC application.

Step 6

Save the generated answer files as follows:

- For Cisco Unified Communications Manager, save both the platformConfig.xml and clusterConfig.xml files in the UCM folder.

- For other UC applications, save the platformConfig.xml file in the relevant application folder.

Step 7

Repeat these steps for each UC application for which you want to use touchless installation.

#### Create Virtual Floppy Images

Use this procedure to create virtual floppy images from the answer files. You will use the virtual floppy images in your touchless
                                    installation.

Tip

We recommend that you follow the recommended naming conventions for your .flp files.

##### Before you begin

You can use Winimage to create the virtual floppy images. You can download Winimage from http://www.winimage.com/download.htm . You can also use other tools, such as BFI, to create virtual floppy images.

Generate Answer Files

Step 1

In Winimage, select File > New .

Step 2

From the Standard format , select 1.44 MB and click OK .

Step 3

Drag the platformConfig.xml file for the UC application onto the Winimage window.

Step 4

When prompted to inject the file into Winimage, click Yes .

Step 5

Cisco Unified Communications Manager only. Drag the clusterConfig.xml file onto the Winimage window.

Step 6

Select File > Save As .

Step 7

Save the file as a virtual floppy image (.flp file) using the following naming conventions:

- Cisco Unified Communications Manager— ucm.flp

- IM and Presence Service— imp.flp

- Cisco Unity Connection— cuc.flp

- Cisco Unified Contact Center Express— ccx.flp

Step 8

Repeat this procedure for each UC application for which you want to use touchless installation.

#### Upload Virtual Floppy Images to Datastore

Use this procedure to upload the virtual floppy images to the datastore.

##### Before you begin

Step 1

Start the VMware Embedded Host Client.

Step 2

Select Storage .

Step 3

Right-click on a datastore and Browse the datastore.

Step 4

Navigate to the destination directory and click the Upload icon.

Step 5

Upload the vFloppy images to the AFG folder.

Step 6

At the Upload/Download warning, click Yes .

Step 7

Close the Datastore Browser window.

#### Mount Virtual Floppy on Virtual Machines and Set Boot Option

Use this procedure to mount the UC application virtual floppy images on their corresponding VM.

This step is not required for predeployed VMs as they are already configured.

##### Before you begin

Step 1

In the VMware Embedded Host Client, select the UC application virtual machine.

Step 2

Select Virtual Machine .

Step 3

Click Edit .

Step 4

From the Virtual Hardware tab, select Floppy drive .

Step 5

Select Use existing floppy image .

Step 6

Browse to the datastore and locate the virtual floppy image.

Step 7

Select the file and click OK .

Step 8

Under Status , enable the Connect at power on option.

Step 9

Click the VM Options tab. Under Boot Options , check the Force BIOS setup , and then click Save .

Step 10

Repeat this procedure for each UC application for which you want to perform touchless installation.

#### Run Touchless
                              	 Installation

If your VM is predeployed, you need to perform step 6 only.

Step 1

In the VMware Embedded Host Client, right-click the VM and select the Console > Open console in new window .

Step 2

Click the Power On icon in the console toolbar to power on the virtual machine.

Step 3

When the BIOS
                                             			 screen appears, configure the following boot order:

CD-ROM

Hard Drive

Removable
                                                   				  Devices

Network

Step 4

Save the
                                             			 settings and exit the console.

Step 5

Repeat these
                                             			 steps for each UC application that you want to install.

Step 6

Once the
                                             			 installations are complete, remove the vFloppy configurations from the virtual
                                             			 machines.

### Install UC
                           	 Applications Manually

Use this procedure to follow the interactive install process to install any UC applications that do not have a touchless install
                                 option such as Cisco Emergency Responder.

Step 1

In the VMware Embedded Host Client, power on the VM for the application that you want to install.

Step 2

Right-click the VM, and choose the Console > Open console in new window .

Step 3

Follow the
                                          			 screen prompts to install the application from the console.

Step 4

If you are
                                          			 using the manual method to install both Cisco Unified Communications Manager
                                          			 and IM and Presence Service, once the Cisco Unified Communications Manager
                                          			 publisher node installation completes, do the following:

From the VMware Embedded Host console, log in to the Cisco Unified Communications Manager CLI.

Run the set
                                                   					 network cluster subscriber dynamic-cluster-configuration 24 command.

Open a VMware Embedded Host console window for the IM and Presence or subscriber virtual machine.

Power On the
                                                				  virtual machine.

Enter the
                                                				  configuration information for the application to complete the installation.

Step 5

Repeat this
                                          			 procedure for each UC application that you want to install.

| Note | For general information on the Cisco UCS C240 M5 server used in Cisco Business Edition 7000, see the Cisco UCS C240 M5 Server Installation and Service Guide . |
|---|---|

| Note | Available VMware vSphere ESXi configuration settings options depend on what license is being used. If your appliance is using
                                             an embedded virtualization license,VMware vSphere ESXi distributed virtual switch features are not enabled. |
|---|---|

| Note | If you purchased an embedded license, record and store the embedded virtualization license key in a safe place. This key will
                                                   be required if the software needs to be reinstalled in the future. |
|---|---|

| Front Panel |
|---|
| 1 | UCSC-C240-M5SX: Drive bays 1—24 support SAS/SATA drives |
| 2 | UCSC-220-M5SX: Drive bays 1 and 2 support NVMe PCIe SSDs |
| 3 | Power button/power status LED |
| 4 | Unit identification button/LED |
| 5 | System status LED |
| 6 | Fan status LED |
| 7 | Temperature status LED |
| 8 | Power supply status LED |
| 9 | Network link activity LED |
| 10 | Pull-out asset tag |
| 11 | KVM connector (used with KVM cable that provides one DB-15 VGA, one DB-9 serial, and two USB connectors) |
| Rear Panel |
| 1 | PCIe riser 1 (PCIe slot 1, 2, 3) |
| 2 | PCIe riser 2 (PCIe slots 4, 5, 6) |
| 3 | Rear 2.5-inch drive bays |
| 4 | Power supplies (two, redundant as 1+1) |
| 5 | Threaded holes for dual-hole grounding lug |
| 6 | Modular LAN-on-motherboard (mLOM) card slot (x16) |
| 7 | USB 3.0 ports (two) |
| 8 | Dual 1-Gb/10-Gb Ethernet ports (LAN1 and LAN2) |
| 9 | VGA video port (DB-15 connector) |
| 10 | 1-Gb Ethernet dedicated management port |
| 11 | Serial port (RJ-45 connector) |
| 12 | Rear unit identification button/LED |

| Step 1 | Remove the slide rails from the top of the appliance's box and unpack them. |
|---|---|
| Step 2 | At the end of one of the rails marked FRONT, slide the green tab in the direction of the arrow (A1) until the securing plate
                                             is latched in the open position (A2). |
| Step 3 | At the desired height, engage the FRONT mounting pegs in to the front post of the equipment rack with the rail extending toward
                                             the rear (B1). Press the green release button (B2) to allow the plate to slide forward to secure the front mount (B3). |
| Step 4 | Hold the rear securing latch open (C1) and extend the rail until the rear mounting pegs engage in the rear rack post at the
                                             same height as the front (C2). Release the rear latch, so that the latch wraps securely around the rear post (C3). |
| Step 5 | Repeat Steps 2 to 4 for the second rail on the other side of the rack. Ensure that you install the rails at the same height. |
| Step 6 | Pull the inner slide rails from the front of each assembly until they lock in place. |
| Step 7 | Remove the appliance from its box and remove all packaging. |
| Step 8 | Point the rear of the appliance toward the front of the rack and align the pre-fitted rails with the extended slide rails. |
| Step 9 | Push the appliance in to the rack rails until the appliance meets the internal stops. |
| Step 10 | Press the plastic release clips marked PUSH on each rail and push the appliance in to the rack until the appliance latches
                                             to the front rack-mount clips. |
| Step 11 | Connect Ethernet Port 1 (and other Ethernet Ports, if required) to the data network. |
| Step 12 | Connect the dedicated management Ethernet interface to the management network, if required for Lights-Out Management. |
| Step 13 | Connect a monitor and keyboard using the rear VGA and USb connectors (or to the front KVM adapter if you purchased one). |
| Step 14 | Connect the power supplies to the electrical outlets. Do not power on the server at this time. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Cisco Integrated Management Controller | Configure CIMC for your Business Edition 7000 server. |
| Step 2 | Customer Virtualization Software Remote Access | Configure the pre-installed VMware vSphere ESXi software on the appliance. |
| Step 3 | Delete Unused or Unwanted Preloaded files | Delete any pre-deployed VMs that you do not require. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Power On and Initial CIMC Setup |  |
| Step 2 | Complete the CIMC Configuration |  |

| Step 1 | Verify that power is connected and that the power button LED is orange. |
|---|---|
| Step 2 | Push the appliance power button and verify that it changes to green. |
| Step 3 | Watch the boot process on the monitor. |
| Step 4 | When the blue Cisco logo appears, press F8 to enter the CIMC configuration dialog. Figure 7. Press F8 at the CIMC Boot Screen |
| Step 5 | When prompted, enter the username admin and create a new password. |
| Step 6 | On the CIMC configuration screen, complete the following details: CIMC IP address Subnet mask Gateway IP address Figure 8. Enter the CIMC IP Address Details |
| Step 7 | When complete, press F10 to save your changes and boot the system. |

| Step 1 | In a web browser, enter the CIMC IP address and log in with the username admin and the password that you created in the previous task. |
|---|---|
| Step 2 | From the left hand menu, select the Admin tab, and click Network . |
| Step 3 | In the main screen, select the Network Settings tab. |
| Step 4 | From Common Properties , change the Hostname setting to the CIMC hostname. |
| Step 5 | From IPv4 Properties , change Preferred DNS Server to the IP address that you have specified for the DNS server. |
| Step 6 | In the main screen, select the NTP Settings tab. |
| Step 7 | Check the Enable NTP check box. |
| Step 8 | In the Server 1 field, enter the NTP server IP address. |
| Step 9 | Select Save Changes from the bottom right hand corner of the page. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Customize VMware vSphere hypervisor Remote Access. |  |
| Step 2 | Access and Configure the VMware vSphere hypervisor . |  |

| Note | If you use ESXi 6.5, then you must select VMFS5 file type to create the datastore. |
|---|---|

| Step 1 | When the hypervisor boots, the ESXi Direct Console User Interface displays on the monitor as shown in the following figure. Figure 9. Console Screen After ESXi Loads |
|---|---|
| Step 2 | Press F2 to enter the System Customization menu as shown in the following figure. Figure 10. ESXi System Customization Menu. The default username is root and password is password . |
| Step 3 | Choose Configure Password to change the password. If your applications are predeployed, skip to 5 . |
| Step 4 | To assign a static IP address, select the Configure Management Network menu, and follow the instructions on the screen to change "IP Configuration" . Figure 11. Assign Static IP Address to ESXi Host |
| Step 5 | Connect your PC to the data network, and browse to the new hypervisor IP address. Figure 12. Hypervisor Welcome Page |

| Step 1 | Browse to the "https://[ESXI-HOST-IP-Address]/ui/" to access VMware Embedded Host Client. Figure 13. Access Virtualization Software Using VMware Embedded Host Client |
|---|---|
| Step 2 | Use the login credentials that you previously configured. |
| Step 3 | If selected at time of quoting, BE 7000 appliances are factory loaded with a Collaboration embedded OEM license for Cisco UC Virtualization . If you want to use
                                                this license, it is ready for use. If you want to re upload or version-upgrade this license, follow these steps: Locate your license document that has license serial number for the Cisco UC Virtualization . For installations, license serial
                                                      number ships from the factory along with the appliance. For version-upgrades, license serial number ships from the Cisco Product
                                                      Upgrade Tool. Navigate to Manage > License > Assign License . Type in or copy or paste the license serial number from the license document. Click Check License to validate the license key. Note License for the Cisco UC Virtualization Hypervisor Plus , Cisco UC Virtualization Foundation or Cisco Collaboration Virtualization Standard is a special Cisco Collaboration embedded OEM license. It is hardcoded to 2-CPU, pre combined, and cannot split or expand
                                                               through myvmware.com. It is neither a VMware Partner Activation Code (PAC) nor a Cisco Product Authorization Key (PAK). It is pre activated, no registration or activation on myvmware.com or cisco.com required. It does not support installation
                                                               through vCenter, license pooling in vCenter, or any vCenter features. For more details, see the http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html#license_comparison . | Note | License for the Cisco UC Virtualization Hypervisor Plus , Cisco UC Virtualization Foundation or Cisco Collaboration Virtualization Standard is a special Cisco Collaboration embedded OEM license. It is hardcoded to 2-CPU, pre combined, and cannot split or expand
                                                               through myvmware.com. It is neither a VMware Partner Activation Code (PAC) nor a Cisco Product Authorization Key (PAK). It is pre activated, no registration or activation on myvmware.com or cisco.com required. It does not support installation
                                                               through vCenter, license pooling in vCenter, or any vCenter features. For more details, see the http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html#license_comparison . |
| Note | License for the Cisco UC Virtualization Hypervisor Plus , Cisco UC Virtualization Foundation or Cisco Collaboration Virtualization Standard is a special Cisco Collaboration embedded OEM license. It is hardcoded to 2-CPU, pre combined, and cannot split or expand
                                                               through myvmware.com. It is neither a VMware Partner Activation Code (PAC) nor a Cisco Product Authorization Key (PAK). It is pre activated, no registration or activation on myvmware.com or cisco.com required. It does not support installation
                                                               through vCenter, license pooling in vCenter, or any vCenter features. For more details, see the http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html#license_comparison . |
| Step 4 | Configure NTP settings: Navigate to Manage > System > Time & date . Click Edit settings to launch the Edit time configuration screen. Check Manually configure the date and time on this host check box. Update the Time. Check the Use Network Time Protocol (enable NTP client) check box. Select Start and stop with host from NTP service startup policy drop-down. Type the IP address of NTP server in NTP servers . If you want to add multiple NTP servers, type the IP address of NTP servers that are separated by commas. Click Save . |
| Step 5 | (Optional) Configure fault tolerance by using the NIC teaming feature in VMware: Navigate to the Networking > Management Network . Click Edit settings to launch Edit port group- Management Network . In the Edit port group- Management Network screen, enter the name, VLANID, Virtual switch. Expand NIC teaming, enter the required details. Click Save to add the NIC that is connected to the data network. Note By default, only one NIC is enabled for the hypervisor and identified as vmnic0. | Note | By default, only one NIC is enabled for the hypervisor and identified as vmnic0. |
| Note | By default, only one NIC is enabled for the hypervisor and identified as vmnic0. |
| Step 6 | Browse the datastore: Navigate to Storage > Datastore to list the datastores in the Business Edition appliance. Select datastore1. Click the Datastore browser . You can view the Preloaded Collaboration Virtual Machines and preloaded software. Note You must select the VMFS5 file type while creating the datastore. Figure 14. Browse Datastore to View Preloaded Collaboration Virtual Machines and Preloaded Software | Note | You must select the VMFS5 file type while creating the datastore. |
| Note | You must select the VMFS5 file type while creating the datastore. |
| Step 7 | (Optional) Cisco recommends that you archive the OVA-ISO directory locally. If a appliance fails, the replacement product does not include preloaded content. |

| Note | License for the Cisco UC Virtualization Hypervisor Plus , Cisco UC Virtualization Foundation or Cisco Collaboration Virtualization Standard is a special Cisco Collaboration embedded OEM license. It is hardcoded to 2-CPU, pre combined, and cannot split or expand
                                                               through myvmware.com. It is neither a VMware Partner Activation Code (PAC) nor a Cisco Product Authorization Key (PAK). It is pre activated, no registration or activation on myvmware.com or cisco.com required. It does not support installation
                                                               through vCenter, license pooling in vCenter, or any vCenter features. For more details, see the http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html#license_comparison . |
|---|---|

| Note | By default, only one NIC is enabled for the hypervisor and identified as vmnic0. |
|---|---|

| Note | You must select the VMFS5 file type while creating the datastore. |
|---|---|

| Step 1 | Log in to VMware Embedded Host Client . Figure 15. Delete Any VMs That You Are Not Using |
|---|---|
| Step 2 | Expand Virtual Machines and locate the virtual machine that you want to delete. |
| Step 3 | If the VM has
                                             			 a green triangle, right-click the icon and select Power > Power
                                                   				  Off . The
                                             			 green arrow disappears as the VM powers off. |
| Step 4 | Right-click the VM and select Delete . |
| Step 5 | Repeat this
                                             			 procedure for each virtual machine that you wish to remove. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Deploy Virtual Machine OVAs | Deploy virtual machine OVAs for each UC application that you want to install. |
| Step 2 | Customize Virtual Machines for Cisco Unity Connection | If your Business Edition 7000 deployment includes Cisco Unity Connection, customize the Unity Connection VM. |
| Step 3 | Associate Application ISO Files to Virtual Machines | For UC application installations that require an ISO file, mount the ISO file on the application VM. Note For a list of applications that use ISO installation files, see the Preload Summary for your appliance . | Note | For a list of applications that use ISO installation files, see the Preload Summary for your appliance . |
| Note | For a list of applications that use ISO installation files, see the Preload Summary for your appliance . |
| Step 4 | Install UC Applications Using Touchless Installation | Optional. Use touchless installation to install any of the following core UC applications: Cisco Unified Communications Manager IM and Presence Service Cisco Unity Connection Cisco Unified Contact Center Express Note If you prefer, you can use manual installation for these applications. | Note | If you prefer, you can use manual installation for these applications. |
| Note | If you prefer, you can use manual installation for these applications. |
| Step 5 | Install UC Applications Manually | Use the manual interactive process to install any remaining UC applications. |

| Note | For a list of applications that use ISO installation files, see the Preload Summary for your appliance . |
|---|---|

| Note | If you prefer, you can use manual installation for these applications. |
|---|---|

| Note | The OVA template files that contain empty virtual machines are deployed in seconds, while larger OVA files that contain partially
                                             or fully installed applications can take longer to deploy. |
|---|---|

| Caution | To ensure proper operation of your appliance and any embedded virtualization licenses, ensure it is running ESXi 6.5 U2 or
                                             greater, with the Cisco UCS-specific image of ESXi. |
|---|---|

| Step 1 | On the VMware Embedded Host Client, navigate to the Virtual Machines . |
|---|---|
| Step 2 | Right-click the Virtual machines and select the Create/Register VM . |
| Step 3 | Select Deploy a virtual machine from an OVF or OVA file as select creation type. |
| Step 4 | Specify a meaningful name for the virtual machine. |
| Step 5 | Browse and select the source OVA template file on your PC. For application and filename mapping, see the Build Summary PDF
                                          in the datastore OVA-ISO directory, or download from here: https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/products-release-notes-list.html . |
| Step 6 | Select the datastore in which to store the configuration and disk files. |
| Step 7 | Select the deployment options. |
| Step 8 | If prompted to accept license agreements, continue to click Next . |
| Step 9 | Select the deployment options. |
| Step 10 | If prompted for the Disk Format , specify Thick Provision Lazy Zero . |
| Step 11 | Review your settings selection before finishing the wizard. |
| Step 12 | Click Next . |
| Step 13 | Deploy VMs for all your UC applications before proceeding to the next task. If your system includes Cisco Unity Connection, then Customize Virtual Machines for Cisco Unity Connection . Otherwise, Associate Application ISO Files to Virtual Machines . |

| Step 1 | On VMware Embedded Host Client, navigate to the Virtual Machines . |
|---|---|
| Step 2 | Right click the Unity Connection entry and select Edit Settings . |
| Step 3 | If you want to use the Unity Connection, or Unified, or Integrated Messaging, do the following: Select the Virtual Hardware tab. Select the CPU menu and set the number of Cores per Sockets to 2 . In the Reservation tab, increase the reservation to 5.06MHz . For more information, see the https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html . |

| Note | For an up to date list of installation files for your appliance, see the Preload Summary for your appliance in the datastore OVA-ISO directory or at: https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/products-release-notes-list.html . |
|---|---|

| Step 1 | In the VMware Embedded Host Client, select the UC application virtual machine. |
|---|---|
| Step 2 | Click Edit . |
| Step 3 | From Virtual Hardware tab, select CD/DVD Drive 1 . |
| Step 4 | Select Datastore ISO File from CD/DVD Drive 1 drop-down list. |
| Step 5 | Browse to the datastore and locate the application ISO file. |
| Step 6 | Select the file and click Select . |
| Step 7 | In CD/DVD Drive 1 , check the Connect at power on check box under the Status . |
| Step 8 | Repeat this procedure for each application that you want to install that includes an ISO file. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate Answer Files | Generate answer files (AFG files) for UC applications. |
| Step 2 | Create Virtual Floppy Images | Use your AFG files to create virtual floppy images. |
| Step 3 | Upload Virtual Floppy Images to Datastore | Upload your virtual floppy images to the datastore. |
| Step 4 | Mount Virtual Floppy on Virtual Machines and Set Boot Option | Mount each virtual floppy on the corresponding UC application VM. |
| Step 5 | Run Touchless Installation | Run the touchless installation of your UC applications. We recommend that you run your installations simultaneously. |

| Tip | We recommend that you create application-specific folders (for example, UCM, IMP, CUC, CCX) in which to save the generated
                                             files so that you do not get the files mixed up. |
|---|---|

| Step 1 | Go to the online answer file generator at: https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html . |
|---|---|
| Step 2 | From the Product drop-down list, select the UC application for which you want to generate answer files. |
| Step 3 | Select the Version that you want to install. |
| Step 4 | Complete the remaining fields with the installation details that you want to configure on the appliance . For example, you can assign items such as passwords, IP addressing, and DNS settings. |
| Step 5 | Click Generate Answer Files to generate the platformConfig.xml file for that UC application. Each UC application generates a platformConfig.xml file. Cisco Unified Communications Manager also generates a clusterConfig.xml file. |
| Step 6 | Save the generated answer files as follows: For Cisco Unified Communications Manager, save both the platformConfig.xml and clusterConfig.xml files in the UCM folder. For other UC applications, save the platformConfig.xml file in the relevant application folder. |
| Step 7 | Repeat these steps for each UC application for which you want to use touchless installation. |

| Tip | We recommend that you follow the recommended naming conventions for your .flp files. |
|---|---|

| Step 1 | In Winimage, select File > New . |
|---|---|
| Step 2 | From the Standard format , select 1.44 MB and click OK . |
| Step 3 | Drag the platformConfig.xml file for the UC application onto the Winimage window. |
| Step 4 | When prompted to inject the file into Winimage, click Yes . |
| Step 5 | Cisco Unified Communications Manager only. Drag the clusterConfig.xml file onto the Winimage window. |
| Step 6 | Select File > Save As . |
| Step 7 | Save the file as a virtual floppy image (.flp file) using the following naming conventions: Cisco Unified Communications Manager— ucm.flp IM and Presence Service— imp.flp Cisco Unity Connection— cuc.flp Cisco Unified Contact Center Express— ccx.flp |
| Step 8 | Repeat this procedure for each UC application for which you want to use touchless installation. |

| Step 1 | Start the VMware Embedded Host Client. |
|---|---|
| Step 2 | Select Storage . |
| Step 3 | Right-click on a datastore and Browse the datastore. |
| Step 4 | Navigate to the destination directory and click the Upload icon. |
| Step 5 | Upload the vFloppy images to the AFG folder. |
| Step 6 | At the Upload/Download warning, click Yes . |
| Step 7 | Close the Datastore Browser window. |

| Note | This step is not required for predeployed VMs as they are already configured. |
|---|---|

| Step 1 | In the VMware Embedded Host Client, select the UC application virtual machine. |
|---|---|
| Step 2 | Select Virtual Machine . |
| Step 3 | Click Edit . |
| Step 4 | From the Virtual Hardware tab, select Floppy drive . |
| Step 5 | Select Use existing floppy image . |
| Step 6 | Browse to the datastore and locate the virtual floppy image. |
| Step 7 | Select the file and click OK . |
| Step 8 | Under Status , enable the Connect at power on option. |
| Step 9 | Click the VM Options tab. Under Boot Options , check the Force BIOS setup , and then click Save . |
| Step 10 | Repeat this procedure for each UC application for which you want to perform touchless installation. |

| Note | If your VM is predeployed, you need to perform step 6 only. |
|---|---|

| Step 1 | In the VMware Embedded Host Client, right-click the VM and select the Console > Open console in new window . A console window opens. |
|---|---|
| Step 2 | Click the Power On icon in the console toolbar to power on the virtual machine. |
| Step 3 | When the BIOS
                                             			 screen appears, configure the following boot order: CD-ROM Hard Drive Removable
                                                   				  Devices Network |
| Step 4 | Save the
                                             			 settings and exit the console. The UC
                                             			 application installation commences immediately. |
| Step 5 | Repeat these
                                             			 steps for each UC application that you want to install. |
| Step 6 | Once the
                                             			 installations are complete, remove the vFloppy configurations from the virtual
                                             			 machines. |

| Step 1 | In the VMware Embedded Host Client, power on the VM for the application that you want to install. |
|---|---|
| Step 2 | Right-click the VM, and choose the Console > Open console in new window . A console window appears. |
| Step 3 | Follow the
                                          			 screen prompts to install the application from the console. |
| Step 4 | If you are
                                          			 using the manual method to install both Cisco Unified Communications Manager
                                          			 and IM and Presence Service, once the Cisco Unified Communications Manager
                                          			 publisher node installation completes, do the following: From the VMware Embedded Host console, log in to the Cisco Unified Communications Manager CLI. Run the set
                                                   					 network cluster subscriber dynamic-cluster-configuration 24 command. Open a VMware Embedded Host console window for the IM and Presence or subscriber virtual machine. Power On the
                                                				  virtual machine. Enter the
                                                				  configuration information for the application to complete the installation. |
| Step 5 | Repeat this
                                          			 procedure for each UC application that you want to install. |