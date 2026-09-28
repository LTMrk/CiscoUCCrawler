---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-installationguide-10-51-cucm-bk-bc403831-00-be6k-install-guide-1-fca5bb2fe1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/InstallationGuide/10_51/CUCM_BK_BC403831_00_be6k-install-guide-1051/CUCM_BK_BC403831_00_be6k-install-guide-1051_chapter_010.html
retrieved_at: 2026-08-21T21:40:04.879259+00:00
---

Cisco Business Edition 6000 Installation Guide, Release 10.5(1)

# Cisco Business Edition 6000 Installation Guide, Release 10.5(1)

Updated: June 6, 2014

Chapter: Installation

## Chapter: Installation

# Installation

## Power On and Initial Setup

Ensure that the BE6000 server has been rack mounted, connected to a power supply, connected to the data network, and a monitor and keyboard is connected to the server, as described in the Quick Start Guide .

The Cisco Integrated Management Controller (CIMC) is the management interface for the C-Series Servers. CIMC runs within the server, allowing remote administration, configuration, and monitoring of the server via web or SSH command line access.

## Customize ESXi Host for Remote Access

Follow this procedure to customize the ESXi host (the VMware hypervisor) to enable remote access  from your PC using the  vSphere client.

## Access and
	 Configure ESXi Host

Some Business Edition applications require the services of a valid NTP server. Follow these steps to
		  access the ESXi host, configure NTP, configure fault tolerance for network
		  interface cards (NICs) using the NIC teaming feature, view preinstalled applications,  and browse the datastore
		  to verify the preloaded collaboration application software.

- Locate the
				  envelope marked "Cisco
					 VMware vSphere Hypervisor" in the shipping box.

- Locate the
				  card titled "Right to
					 Use Notification" in the envelope.

- Note the
				  Master serial number, which is the license activation key.

- Navigate
				  to Configuration > Software > Licensed
						Features , and click Edit.

- Select Assign a new license key to this host .

- Click Enter Key... .

- Type in
				  the Master serial number.

- Click OK to close configuration dialogs and apply the
				  license.

- Navigate
				  to Configuration > Software > Time
						Configuration .

- Click Properties to launch the Time Configuration screen.

- Update the
				  Time Click Options... .

- Select NTP
				  Settings.

- Click Add and type the IP address of NTP server.

- Click OK , and select General, select Start and stop with
				  host, and click Start button, followed by click OK to close the configuration
				  screens.

- Navigate
				  to Configuration > Hardware > Networking .

- Click Properties for "Standard
					 Switch: vSwitch0," as shown in the figure below.

- In the
				  configuration screen vSwitch0 Properties, select the tab Network Adapters .

- Click Add… to add the NIC that is connected to data
				  network.

- Follow the
				  interactive configuration dialogs and close the configuration screens until you
				  see two or more NICs are added to vSwitch0, as shown in the figure below.

By default,
				  only one NIC is enabled in ESXi and identified as vmnic0.

The ESXi host
				is now ready for deploying virtual machines, which will host individual
				collaboration applications. Software for these applications are preloaded on
				the datastore of the Business Edition server.

- Navigate
				  to Configuration > Hardware > Storage .

- Click Datastore to list the datastores in the Business Edition
				  server.

- Select a
				  datastore, then right-click and select Browse Datastore as shown in the figure below.

Install virtual
		  machines.

### Preloaded Files on
	 Datastore

Cisco Business Edition servers are
		  shipped with selected Collaboration software, license files that are preloaded on the datastore.
		  Consider the following points for a basic understanding of the preloaded file types:

An ISO file
				  is a DVD image containing application install files.

Open
				  Virtualization Archive (OVA) is used to package and distribute the virtual machine.

Some OVA
				  files may include a prepared disk that includes preinstalled software (for example, cpc-provisioning-9.5.0-245-small.ova ).

Some OVA
				  files do not have application software preinstalled. In this case, you must
				  install the software using the ISO file that is provided on datastore (for
				  example, cucm_9.1_vmv8_v1.7.ova and associated ISO file Bootable_UCSInstall_UCOS_9.1.2.10000-28.sgn.iso ) .

For preloaded
			 files in the Export Restricted or Export Unrestricted software, see the
			 relevant Release Note.

## Deploy Virtual
	 Machines

Follow this
		  procedure to deploy virtual machines for applications that are listed in the
		  preloaded files. For preloaded files in the Export Restricted or Export
		  Unrestricted software, see the relevant Release Note here: http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​business-edition-6000/​products-release-notes-list.html .

The OVA template file defines the virtual machine for specific
		  applications.

- OVAs
				are deployed in seconds, and a preinstalled OVA may take 10-15 minutes to
				deploy.

- The figure below shows the view of vSphere client after deployment of various collaboration
				applications virtual machines. You can also see the time that is taken to
				deploy the last two virtual machines.

The
					 example in the figure below is for the High Density (HD) server model, which can host four collaboration applications plus Prime Collaboration Provisioning. The Medium
					 Density (MD) server model of a Business Edition server can also host four collaboration applications plus Prime Collaboration Provisioning.

The Deploy OVF
				Template screen is launched.

- For Cisco Unified
				Communications Manager, Cisco Unity Connection and IM and Presence Service,
				select 1000 Users.

- For Cisco Unified Contact
				Center Express, select 100 Agents.

- For Cisco Emergency
				Responder, select 12000 user node – C200 only from the drop-down menu.

After deploying
		  all required virtual machines, install individual collaboration applications.

## Install
	 Applications on Virtual Machines

Follow this
		  procedure to install and set up the applications on their designated virtual
		  machines.

The approximate
		  time that is required for each application is as follows:

- Cisco Unified
				Communications Manager: 60 minutes

- Cisco Unity
				Connection: 60 minutes

- Cisco Unified
				Communications Manager IM and Presence Service: 45 minutes

- Cisco Prime
				Collaboration: 30 minutes

- Cisco Unified
				Contact Center Express: 60 minutes

- Cisco
				Emergency Responder: 45 minutes

- Video
				Communication Server: 60 minutes

- Cisco Paging
				Server: 15 minutes

- Do not
				  install Unified Communications Manager and Cisco Unity Connection
				  simultaneously, because they use the same ISO image.

- You can
				  install multiple applications concurrently to save time.

- In Release 10.5(1) and later, the time it takes to install preinstalled applications is approximately 20 minutes less.

- In the
				  Device Type section, select the Datastore ISO File radio button.

- Browse to
				  the datastore and select the ISO file for the application.

- Make sure
				  to check the box Connect at Power On as shown in the figure below.

- Go to the following URL and generate the platformconfig.xml file: http:/​/​www.cisco.com/​web/​cuc_afg/​index.html .

- Using any freeware virtual floppy application, convert the platformconfig.xml file to *.flp image and copy this *.flp image to the  Answer File Generator directory in the datastore.

- Make sure that the floppy drive settings are changed accordingly to pick up the *.flp file from the datastore. Figure 14. Edit Virtual Machine Settings to Connect Floppy Drive to Read Configuration Settings from FLP File

- Power on
				  the virtual machine and open the console using the right-click menu shown in Figure
				  12.

- Follow the
				  interactive installation procedure on console.

- Accept the
				  defaults and provide the information that you collected in Step 1. Installation
				  is complete and successful when you are able to do a successful login on
				  console.

- For Prime Collaboration,
				Installation starts after typing setup for the "localhost
				  login:" . After that, the installation script asks for network information
				and various credentials (passwords for admin, root, globaladmin) information.
				Installation continues for 30 minutes.

- For a VCS server,
				installation starts after using first-time username password as admin and
				TANDBERG. Type y when asked "Run install
				  wizard [n]:" and continue with interactive installation.

If you
				  require detailed installation guidance, see the Installation Guide of the
				  applications on the Cisco Business Edition 6000 Support Documents website,
				  listed in "For More
					 Information" .

After installing
		  all required applications, access applications using a web browser and perform
		  initial setup of some applications.

### Examples of Application Installation

The following are steps  to install Cisco Unified Communications Manager (a blank OVA) and Cisco Video Communications Server (a preinstalled OVA).

- Install Cisco Unified Communications Manager

- Install Cisco Video Communications Server

#### Install Cisco Unified Communications Manager

- In the Platform Installation Wizard window, select Proceed .

- In the Apply Patch window, select No .

- In the Basic Install window, select Continue .

- Select Timezone in the  next window followed by Auto Negotiation for Ethernet connection, and the default size for MTU.

The Static Network Configuration window appears.

#### Install Cisco Video Communications Server

| Step 1 | Verify that the monitor and keyboard are connected to the console port as shown in the figure below. |
|---|---|
| Step 2 | Verify that power is connected and the LED status is as shown in the figure below. Figure 1.  Power On, Console Port, and LED Status . The power button LED (2) is orange, and the five LEDs between the console port (1) and power button are green. If not, check the electrical and network connections. |
| Step 3 | Power on the monitor. |
| Step 4 | Push the power button (Figure 1) and verify that the power button LED the disk LED disk drive change to green. |
| Step 5 | Watch the boot process on the monitor. |
| Step 6 | (Optional) Press F8 to enter the CIMC configuration dialog to configure the management interface IP address and then exit. The Cisco Integrated Management Controller (CIMC) is the management interface for the C-Series Servers. CIMC runs within the server, allowing remote administration, configuration, and monitoring of the server via web or SSH command line access. |
| Step 7 | (Optional) If using CIMC for console access, browse to the IP address that you configured, and use the default username admin and password password . The CIMC screen is shown in Figure 2. Navigate the CIMC for various tasks, such as Locater LED, and KVM Console as marked in Figure 3. Figure 2.  Cisco Integrated Management Controller |
| Step 8 | Wait until the ESXi loads and displays the configuration screen on the console. |

| Step 1 | When the hypervisor has booted, the ESXi Direct Console User Interface displays on the monitor as shown in the following figure. Figure 3.  Console Screen After ESXi Loads . Note For release 10.5(1) and later, you are notified about preinstalled applications. | Note | For release 10.5(1) and later, you are notified about preinstalled applications. |
|---|---|---|---|
| Note | For release 10.5(1) and later, you are notified about preinstalled applications. |
| Step 2 | Press F2 to enter the System Customization menu as shown in the following figure. Figure 4.  ESXi System Customization Menu . The default username is root and password is password . |
| Step 3 | Choose Configure Password to change the password. |
| Step 4 | Assign a static IP address to ESXi. Enter the Configure Management Network menu, and follow the instructions on screen to change "IP Configuration" as shown in the figure below. Figure 5.  Assign Static IP Address to ESXi Host |
| Step 5 | Connect your PC to the data network, and verify that you can browse to the ESXi IP address that you configured in the previous step. Verify the web page as shown in the figure below. Figure 6.  ESXi Host |
| Step 6 | If not already installed on your PC, download and install the vSphere client. Internet access is required to download the vSphere client. |

| Note | For release 10.5(1) and later, you are notified about preinstalled applications. |
|---|---|

| Step 1 | Launch the
			 vSphere client application and type the IP address of the ESXi host. Figure 7.  Access
				  ESXi Host Using vSphere Client |
|---|---|
| Step 2 | Use the login
			 credentials that you previously configured during ESXi system customization. |
| Step 3 | (optional) The VMware license is not preinstalled, and you
			 may be presented with a 60 day evaluation license warning. You may also receive this warning if you performed a factory reset to the UCS server. In these cases,
			 follow these steps to apply the license. You may also verify the license status
			 using these steps: Locate the
				  envelope marked "Cisco
					 VMware vSphere Hypervisor" in the shipping box. Locate the
				  card titled "Right to
					 Use Notification" in the envelope. Note the
				  Master serial number, which is the license activation key. Navigate
				  to Configuration > Software > Licensed
						Features , and click Edit. Select Assign a new license key to this host . Click Enter Key... . Type in
				  the Master serial number. Click OK to close configuration dialogs and apply the
				  license. Figure 8. 
				  Configuring and Managing ESXi Host and Virtual Machine Note Notice the preinstalled applications listed in the left pane of the following figure. | Note | Notice the preinstalled applications listed in the left pane of the following figure. |
| Note | Notice the preinstalled applications listed in the left pane of the following figure. |
| Step 4 | Add the NTP
			 server: Navigate
				  to Configuration > Software > Time
						Configuration . Click Properties to launch the Time Configuration screen. Update the
				  Time Click Options... . Select NTP
				  Settings. Click Add and type the IP address of NTP server. Click OK , and select General, select Start and stop with
				  host, and click Start button, followed by click OK to close the configuration
				  screens. |
| Step 5 | Configure
			 fault tolerance by using the NIC teaming feature in VMware: Navigate
				  to Configuration > Hardware > Networking . Click Properties for "Standard
					 Switch: vSwitch0," as shown in the figure below. In the
				  configuration screen vSwitch0 Properties, select the tab Network Adapters . Click Add… to add the NIC that is connected to data
				  network. Follow the
				  interactive configuration dialogs and close the configuration screens until you
				  see two or more NICs are added to vSwitch0, as shown in the figure below. Note By default,
				  only one NIC is enabled in ESXi and identified as vmnic0. Note If connecting teamed NICs to a Cisco switch channel-group, ensure that the NIC teaming load balancing policy is set to Route based on IP hash . For more information about  this policy and other aspects of hypervisor networking for Cisco Collaboration applications, see Deploying Expressway with Business Edition at http:/​/​www.cisco.com/​c/​dam/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​BE6000/​InstallationGuide/​10_01/​Deploying_​Expressway_​with_​Business_​Edition.pdf Figure 9.  Fault
				  Tolerance for Business Edition Network Connectivity The ESXi host
				is now ready for deploying virtual machines, which will host individual
				collaboration applications. Software for these applications are preloaded on
				the datastore of the Business Edition server. | Note | By default,
				  only one NIC is enabled in ESXi and identified as vmnic0. | Note | If connecting teamed NICs to a Cisco switch channel-group, ensure that the NIC teaming load balancing policy is set to Route based on IP hash . For more information about  this policy and other aspects of hypervisor networking for Cisco Collaboration applications, see Deploying Expressway with Business Edition at http:/​/​www.cisco.com/​c/​dam/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​BE6000/​InstallationGuide/​10_01/​Deploying_​Expressway_​with_​Business_​Edition.pdf |
| Note | By default,
				  only one NIC is enabled in ESXi and identified as vmnic0. |
| Note | If connecting teamed NICs to a Cisco switch channel-group, ensure that the NIC teaming load balancing policy is set to Route based on IP hash . For more information about  this policy and other aspects of hypervisor networking for Cisco Collaboration applications, see Deploying Expressway with Business Edition at http:/​/​www.cisco.com/​c/​dam/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​BE6000/​InstallationGuide/​10_01/​Deploying_​Expressway_​with_​Business_​Edition.pdf |
| Step 6 | Browse the
			 datastore: Navigate
				  to Configuration > Hardware > Storage . Click Datastore to list the datastores in the Business Edition
				  server. Select a
				  datastore, then right-click and select Browse Datastore as shown in the figure below. Figure 10. 
				  Browse Datastore to View Preloaded Collaboration Software, License, and Open
				  Virtualization Archive Files |
| Step 7 | (Optional) Cisco recommends that you archive the OVA-ISO directory because, in the case of merchandise returned for troubleshooting, the new UCS server may have a blank datastore. |

| Note | Notice the preinstalled applications listed in the left pane of the following figure. |
|---|---|

| Note | By default,
				  only one NIC is enabled in ESXi and identified as vmnic0. |
|---|---|

| Note | If connecting teamed NICs to a Cisco switch channel-group, ensure that the NIC teaming load balancing policy is set to Route based on IP hash . For more information about  this policy and other aspects of hypervisor networking for Cisco Collaboration applications, see Deploying Expressway with Business Edition at http:/​/​www.cisco.com/​c/​dam/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​BE6000/​InstallationGuide/​10_01/​Deploying_​Expressway_​with_​Business_​Edition.pdf |
|---|---|

| Note | For preloaded
			 files in the Export Restricted or Export Unrestricted software, see the
			 relevant Release Note. |
|---|---|

| Note | In Release 10.5(1) and later, five applications are preinstalled. If you are deploying virtual machines using any of these five applications, you can skip the following procedure. |
|---|---|

| Step 1 | On the vSphere
			 Client, navigate to File > Deploy OVF
				  Template . The Deploy OVF
				Template screen is launched. |
|---|---|
| Step 2 | Browse and
			 select the source OVA template file on your PC. For application and filename
			 mapping, see the Release Note pertaining to Export Restricted software here: http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​business-edition-6000/​products-release-notes-list.html . |
| Step 3 | Continue to
			 click Next to accept license agreements and default
			 values. |
| Step 4 | Configure your
			 deployment: For Cisco Unified
				Communications Manager, Cisco Unity Connection and IM and Presence Service,
				select 1000 Users. For Cisco Unified Contact
				Center Express, select 100 Agents. For Cisco Emergency
				Responder, select 12000 user node – C200 only from the drop-down menu. |
| Step 5 | Specify a meaningful name for the VM. |

| Note | Do not
				  install Unified Communications Manager and Cisco Unity Connection
				  simultaneously, because they use the same ISO image. You can
				  install multiple applications concurrently to save time. In Release 10.5(1) and later, the time it takes to install preinstalled applications is approximately 20 minutes less. |
|---|---|

| Step 1 | Contact the
			 data network administrator and make sure that you collect the network
			 information that is described in "Preparation." |
|---|---|
| Step 2 | Plan the
			 sequence of installing the applications to minimize the time that is required. |
| Step 3 | Using vSphere
			 client, select an application’s virtual machine. The client changes the panel
			 name to application name, and adds one more tab named "Getting
				Started" . Right click to open the action
			 menu as shown in the figure below. Figure 12.  Select
				  an Application VM to Edit Settings, Associate the ISO with the VM, Power On, and Take Any Other Administrative
				  Action |
| Step 4 | For VMs that
			 are deployed using blank OVA templates, you need to edit the settings of
			 virtual machines to connect the ISO image of application software at power on.
			 Note that Unified Communications Manager and Cisco Unity Connection use same
			 ISO file (see the Preloaded files for Cisco Business Edition 6000 here: http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​business-edition-6000/​products-release-notes-list.html ). Figure 13.  Edit
				  Virtual Machine Settings to Connect ISO Image of Application
				  Software In the
				  Device Type section, select the Datastore ISO File radio button. Browse to
				  the datastore and select the ISO file for the application. Make sure
				  to check the box Connect at Power On as shown in the figure below. |
| Step 5 | Select Edit
				Settings from the right-click menu as shown in Figure 12. 
		  The Virtual
				Machines Properties editing screen appears, as shown in the Figure 13. Go to the following URL and generate the platformconfig.xml file: http:/​/​www.cisco.com/​web/​cuc_afg/​index.html . Using any freeware virtual floppy application, convert the platformconfig.xml file to *.flp image and copy this *.flp image to the  Answer File Generator directory in the datastore. Make sure that the floppy drive settings are changed accordingly to pick up the *.flp file from the datastore. Figure 14. Edit Virtual Machine Settings to Connect Floppy Drive to Read Configuration Settings from FLP File |
| Step 6 | To begin
			 installation of each application, follow these steps: Installation will
			 continue automatically for the time listed in Step 2. Power on
				  the virtual machine and open the console using the right-click menu shown in Figure
				  12. Follow the
				  interactive installation procedure on console. Accept the
				  defaults and provide the information that you collected in Step 1. Installation
				  is complete and successful when you are able to do a successful login on
				  console. For Prime Collaboration,
				Installation starts after typing setup for the "localhost
				  login:" . After that, the installation script asks for network information
				and various credentials (passwords for admin, root, globaladmin) information.
				Installation continues for 30 minutes. For a VCS server,
				installation starts after using first-time username password as admin and
				TANDBERG. Type y when asked "Run install
				  wizard [n]:" and continue with interactive installation. Note If you
				  require detailed installation guidance, see the Installation Guide of the
				  applications on the Cisco Business Edition 6000 Support Documents website,
				  listed in "For More
					 Information" . | Note | If you
				  require detailed installation guidance, see the Installation Guide of the
				  applications on the Cisco Business Edition 6000 Support Documents website,
				  listed in "For More
					 Information" . |
| Note | If you
				  require detailed installation guidance, see the Installation Guide of the
				  applications on the Cisco Business Edition 6000 Support Documents website,
				  listed in "For More
					 Information" . |

| Note | If you
				  require detailed installation guidance, see the Installation Guide of the
				  applications on the Cisco Business Edition 6000 Support Documents website,
				  listed in "For More
					 Information" . |
|---|---|

| Note | If the application is preinstalled and the FLP file is copied in the Answer File Generator directory, as described in previous section, installation will happen automatically without installer intervention |
|---|---|

| Step 1 | Power on and open the console of the virtual machine, as illustrated in Figure 12. |
|---|---|
| Step 2 | On the DVD Found window, select No for media check. |
| Step 3 | In the Product Deployment Selection window, select Cisco Unified Communications Manager , then select OK . Finally, select Yes in the next Proceed with Install window. Note Enterprise License Manager is also deployed as part of this installation. | Note | Enterprise License Manager is also deployed as part of this installation. |
| Note | Enterprise License Manager is also deployed as part of this installation. |
| Step 4 | Perform the following steps: In the Platform Installation Wizard window, select Proceed . In the Apply Patch window, select No . In the Basic Install window, select Continue . Select Timezone in the  next window followed by Auto Negotiation for Ethernet connection, and the default size for MTU. |
| Step 5 | Select No for DHCP. The Static Network Configuration window appears. |
| Step 6 | Enter the hostname, (such as CUCM), IP address, IP mask, and gateway address; then select OK . Select Yes for DNS Client, followed by entering DNS server information in next window. |
| Step 7 | The next two windows prompt you to set up administrative login information and organization information, followed by confirming whether the server is the first node; in most cases, select Yes . |
| Step 8 | In the next windows, select No for network connectivity test, and again provide the hostname, IP address and security password. Finally, provide a valid reachable NTP server. |
| Step 9 | The next two windows prompt you to set a security password and SMTP server information. Finally, application user information is required, followed by the last window Platform Configuration Confirmation. Select OK to continue the installation, which will last for approximately 60 minutes without any user interaction on the console. After you see the login prompt on the console, access the Unified Communications Manager IP address in a web browser. |

| Note | Enterprise License Manager is also deployed as part of this installation. |
|---|---|

| Step 1 | Power on and open the console of the virtual machine, as illustrated in Figure 12. |
|---|---|
| Step 2 | At the login prompt, enter admin for username and TANDBERG for the password. |
| Step 3 | At the Run Install Wizard prompt, type Y and press Enter . |
| Step 4 | To change password, type Y and press Enter , and at the prompt type the new password and click Enter . |
| Step 5 | The next series of prompts are for network information. Select the IP Protocol (the default is IPv4), provide the IP address, subnet mask, and default gateway address. Finally, select the ethernet speed of the LAN (the default is auto). |
| Step 6 | For the Run SSH (Secure shell) daemon, type Y and press Enter . |
| Step 7 | At the Restart Now prompt, type Y and press Enter . |
| Step 8 | After the system reboots, access the Cisco Video Communication Server in a web browser. |