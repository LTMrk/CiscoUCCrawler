---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-15-english-administration-guide-cer0-b-cisco-emergency-responder-adminis-0d1470f249
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/15/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-15/cer0_m_cisco-emergency-responder-administration-installation.html
retrieved_at: 2026-08-21T06:36:18.647524+00:00
---

Cisco Emergency Responder Administration Guide, Release 15 and SUs

# Cisco Emergency Responder Administration Guide, Release 15 and SUs

Updated: March 17, 2026

Chapter: Cisco Emergency Responder Installation and Upgrade

## Chapter: Cisco Emergency Responder Installation and Upgrade

# Cisco Emergency Responder Installation and Upgrade

## Cisco Emergency Responder Installation

Cisco Emergency Responder (Emergency Responder) is distributed on an installation DVD that contains everything that is required
                           to install Emergency Responder, including the Cisco Unified Communications Operating System software.

From Release 15SU4, Emergency Responder also supports operations on the following two hypervisors: Cisco NFVIS for UC and
                           Cisco Compute Hyperconverged with Nutanix (CCHN), apart from the existing support on the VMware vSphere ESXi hypervisor.

For detailed information on the hypervisors, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications .

## Planning the Installation

### Installation Methods

This guide covers the installation methods for Emergency Responder.

These installation methods can be used for Fresh Install (first-time setup of a brand-new node or cluster, no existing deployment,
                                 and no existing customer data).

Installation Method

Description

Attended Install

This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC.

A baseline-typical installation of one node of Emergency Responder .

To install an Emergency Responder cluster using this method, follow the Installation on a New System steps in this sequence:

Emergency Responder publisher node

Emergency Responder subscriber node

You can use this method with any of the following software media options:

Physical install DVD.

Bootable installer image for base release in ISO format (obtained from either Cisco Commerce Workspace, Cisco License Central,
                                                   or a Cisco Business Edition appliance factory preload). This file applies for all the 3 hypervisors.

(Applicable only to VMware vSphere ESXi and Cisco NFVIS for UC) Base OVA containing all supported virtual machine configurations.

(Applicable only to Nutanix AHV) A set of base OVAs, each containing a supported virtual machine configuration.

(Applicable only to VMware vSphere ESXi) Partial skip-installed OVA. This OVA format file contains a partially installed application
                                                   up to the "skip" Install Wizard point where the application is ready to accept an Answer File and complete installation. OVA
                                                   format file is obtained either from Cisco License Central or from a Cisco Business Edition appliance factory preload.

Touchless Install of a Single Node or a Cluster

This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC.

A partially automated installation of one node or installation of an Emergency Responder cluster.

Use this method to get basic automation for one node, where you can fill out all the information initially, start the Install
                                             Wizard with that information, and complete the rest of the installation automatically using the Answer File.

For clusterwide installations, use this method to generate pre-created Answer Files, that occurs in one seamless process with
                                             minimal intervention.

To install a single node or a cluster using this method, follow the Touchless Installation steps for the hypervisor selected:

Create an Answer File for each node in the cluster using the Unified Communications Answer File Generator.

Place all those Answer Files in well-known locations. See Generate Answer Files for Touchless Install .

Power on the node or all the cluster nodes simultaneously.

In this method, no interaction with the native Install Wizard is required. The nodes will communicate with each other and
                                             each node will read its Answer File for instructions.

You can use this method with any of the software media options available for Attended Install. Use this method to:

Get more automation—Unattended Install of the entire cluster + zero interaction with the native Install Wizard.

Faster installation—Cluster nodes undergo installation in parallel. This is especially useful if you have a large cluster
                                                   with many nodes to install.

Fresh Install with Data Import

This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC.

To directly migrate a cluster, follow the Install with Data Import tasks:

On each cluster node, export your old version's data.

For each cluster node, provision a new virtual machine for your new version and follow either Attended Install or Touchless
                                                   Install for a single node or the cluster node(s) of interest. Using the Data Import options available in Install Wizard and/or
                                                   the Unified Communications Answer File Generator.

You can use this method with any of the software media options available for Attended Install.

Use this method for "native" direct migrations. You can have more granular control over individual nodes migration timing
                                             and sequencing. You may also use this method to avoid the use of application readdress and temporary extra hardware footprint
                                             for direct migration.

### Requirements and Limitations

The following sections provide information about the requirements that your system must meet, and limitations that apply when
                                 you install or upgrade Emergency Responder:

#### Virtualization Requirements

Emergency Responder is supported on VMware vSphere ESXi, Cisco NFVIS-for-UC, and Nutanix AHV versions.

Cisco NFVIS-for-UC is a special edition of NFVIS that introduces a new commercial offer with a separate product ID, distinct
                                    pricing, new licensing, and a slightly different administrative GUI.

Cisco NFVIS-for-UC supports only select on-premises calling applications.

Cisco NFVIS-for-UC supports only select Cisco Calling Appliances.

For general virtualization software/hardware requirements, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications .

##### Application/Hypervisor Compatibility

See the following table for compatibility of Emergency Responder with hypervisor releases.

Only the listed major/minor releases are supported, with a minimum required maintenance or patch release.

Unlisted major/minor release trains are not supported.

For support of subsequent maintenance or patch releases, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications .

Compatible Hypervisor Major/Minor Releases with Minimum Maintenance/Patch Release

Emergency Responder

VMware vSphere ESXi

Cisco NFVIS-for-UC

Nutanix AHV

Release 15SU4

8.0 U1

7.0 U3

4.18.2a

AHV 10.0 + AOS 7.0/PC 2024.3

Releases 15 FCS through 15SU3

8.0 U1

7.0 U3

Not supported

Not supported

##### Virtual Machine Configurations and CPU Minimum Base Frequencies

Applications are supported only with specific virtual machine (VM) configurations.

You must deploy these VMs using the latest Cisco-provided OVA file (see the Readme file for important notes.)

For Emergency Responder, the files are available here: https://software.cisco.com/download/home/286331954/type/282074227/release/15SU4

One base OVA is used for both VMware vSphere ESXi and Cisco NFVIS for UC, while a set of base OVAs is used for Nutanix AHV.

See the following table for the required and supported virtual machine configurations.

Each VM represents a particular application capacity point and has a minimum required CPU base frequency.

For more information on how these are used, see the Cisco Virtualization Guide for Cisco On-premises Calling Applications .

Component and Capacity Point

vCPU

Physical CPU Required Minimum Base Frequency

vRAM

vDisk

vNIC

20,000 users

2

2.00 GHz for <12K users

2.50 GHz for <20K users

6 GB

1 x 80 GB

1

30,000 users

2

2.50 GHz

6 GB

1 x 110 GB

1

40,000 users

4

2.50 GHz

6 GB

1 x 110 GB

1

#### Hardware and
                              	 Software Prerequisites

Cisco
                                 		Emergency Responder requires specific hardware and software to run properly.
                                 		Review the following sections before you proceed with an installation or
                                 		upgrade:

See the latest version of the Release Notes for Cisco Emergency Responder to verify that you have all the hardware and software,
                                       and in the supported versions, that you must install for Emergency Responder and to check that your Cisco Unified Communications
                                       Manager Appliance platform provides the Emergency Responder capabilities to meet your configuration needs. (You can also use
                                       equivalent Cisco-certified servers.)

See the 'License Requirements' section to make sure that you have all the required license keys available before you begin
                                       the installation process.

#### System Preparations

The Emergency
                                 		Responder installation process installs both the platform software and the
                                 		Emergency Responder software. During the installation, you are prompted to
                                 		enter information needed by the system to complete the installation.

We recommend that you perform the installation or upgrade during off-peak hours. The installation or upgrade procedure completely
                                             reformats the hard disk, so Emergency Responder is unavailable duration the installation or upgrade.

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
                                             ensure that you change the security password in the lower version to be the same as the higher version. Follow these steps
                                             to change the security password:

Switch the publisher node to a lower version.

Change the security password of the publisher node to the new password which is the same as the higher

version.

Switch the subscriber to a lower version.

Change the security password of the subscriber node to the new password which is the same as the higher version.

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

Perform the Emergency Responder installation tasks in the order shown in this table.

Installation Task

For
                                             				More Information

Install Cisco Unified Communications Manager

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

Install Emergency Responder as a new installation

Installation on a New System

#### Required Installation Information

When you install either Emergency Responder on a server, the installation process requires you to provide specific information.
                                    You can provide this information manually during the installation process or you can provide it using an answer file. For
                                    each server that you install in a cluster, you must gather this information before you begin the installation process.

The following table lists the information that you must gather before you begin the installation.

Because some of the fields are optional, they may not apply to your configuration. For example, if you decide not to set up
                                                an SMTP host during installation, the parameter still displays, but you do not need to enter a value.

You cannot change some of the fields after the installation without reinstalling the software, so be sure to enter the values
                                    that you want. The last column in the table shows whether you can change a parameter after installation, and if you can, it
                                    provides the appropriate menu path or Command Line Interface (CLI) command.

Configuration Data

Description

Editable after Installation

Administrator Credentials

Administrator Login

Specifies the name that you want to assign to the Administrator account.

No

After installation, you can create additional administrator accounts, but you cannot change the original administrator account
                                                user ID.

Administrator Password

Specifies the password for the Administrator account.

Yes

CLI: set password user admin

Application User Credentials

Application User Username

Specifies the user ID for applications installed on the system.

Yes

CLI: utils reset_application_ui_administrator_name

Application User Password

Specifies the password for applications on the system.

Yes

CLI: utils reset_application_ui_administrator_password

Security Password

Security password for Emergency Responder

Servers in the cluster use the security password to communicate with one another. Set this password on the Emergency Responder
                                                publisher node, and enter it when you install each additional node in the cluster.

Yes. You can change the security password on all nodes in the cluster using the following command:

CLI: set password user security

Certificate Information

Organization

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality] [state] [country]

Unit

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality] [state] [country]

Location

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality] [state] [country]

State

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality] [state] [country]

Country

Used to create the Certificate Signing Request.

Yes

CLI: set web-security [orgunit] [orgname] [locality] [state] [country]

(Optional) SMTP

SMTP Location

Specifies the name of the SMTP host that is used for outbound email.

You must fill in this field if you plan to use electronic notification. If not, you can leave it blank.

Yes

In Cisco Unified Operating System Administration Web Interface, select Settings > SMTP and enter the IP address or Hostname in the IP Address/Host Name field.

CLI: set smtp [host]

CER Emergency Number

Emergency Number

Specifies the primary emergency number that is dial-able and is handled by Emergency Responder.

All characters must either be numeric, a '*' or a '#'.

Yes

CER End User Language

End User Language

Specifies the language the user wants to use for Emergency Responder.

Yes

CER CCM Version

CCM Version

Yes

Network Information

DHCP

(Dynamic Host Configuration Protocol)

Check the check box if you want to use DHCP to automatically configure the network settings on your server. Also, enter the
                                                hostname.

If you uncheck the option, you must enter a hostname, IP Address, IP Mask, and Gateway Address.

Yes.

In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet .

CLI: set network dhcp eth0 [enable]

CLI: set network dhcp eth0 disable [node_ip] [net_mask] [gateway_ip]

Hostname

If DHCP is enabled, you must enter a hostname for this machine.

Yes; for Emergency Responder nodes, choose one of the following:

In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet .

CLI: set network hostname

You will be prompted to enter the parameters.

IP Address

If DHCP is disabled, you must enter the IP address of this machine.

Yes; for Emergency Responder nodes, choose one of the following:

In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet .

CLI: set network IP eth0 [ip-address] [ip-mask]

IP Mask

If DHCP is disabled, you must enter the IP subnet mask of this machine. The subnet mask together with the IP address defines
                                                the network address and the host address.

The subnet mask must use the following format: 255.255.255.0

Yes

In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet .

CLI: set network IP eth0 [ip-address] [ip-mask]

Gateway Address

If DHCP is disabled, you must enter the gateway address.

Yes

In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet .

CLI: set network gateway [addr]

(Optional) DNS

Primary DNS

If you have a Domain Name Server (DNS), Emergency Responder contacts this DNS server first when attempting to resolve hostnames.

Yes

CLI: set network dns primary [address]

Secondary DNS (optional)

When a primary DNS server fails, Emergency Responder will attempt to connect to the secondary DNS server.

Yes

CLI: set network dns secondary [address]

Domain

Represents the name of the domain in which this machine is located

Yes

CLI: set network domain [name]

Time Zone

Region

Allows you to select a region for your time zone.

Yes

Time Zone

Reflects the local time zone and offset from Greenwich Mean Time (GMT). Select the time zone that most closely matches the
                                                location of your machine.

Yes

CLI: set timezone [zone]

Network Time Protocol

NTP Server IP Address

During installation of the Emergency Responder publisher node, you must specify the IP address of an external Network Time
                                                Protocol (NTP) server. We recommend that you use the Emergency Responder publisher node as the NTP server.

Yes

In Cisco Unified Operating System Administration Web Interface, select Settings > NTP Servers .

(Optional) List of Secondary Nodes

This list identifies the secondary nodes (subscribers) in the cluster by host name.

Yes

## Preinstallation Tasks

### Preinstall Tasks for Emergency Responder on VMware vSphere ESXi

Step 1

Planning the Installation

Make sure to review the following:

Decide on your installation method.

Decide on your cluster topology.

Step 2

Required Installation Information

Review the installation requirements and record the configurations settings for each server that you plan to install.

Step 3

Create virtual machines.

Get base OVA. An example OVA file name is: cer_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova .

Run Collab Sizing Tool to get the required virtual machine count and specs of each virtual machine. If you don't want to run
                                                   Collab Sizing Tool, follow the guidance in the OVA readme and the OVA wizard to select a predefined starting point, which
                                                   can be changed later if needed.

Step 4

Mount the installation ISO file.

Place the installation ISO file in a location where the virtual machine can access it and edit the virtual machine's DVD drive
                                             to map to the file. Select the option to mount the DVD drive when you power on the virtual machine.

When you power on the virtual machine, it mounts the ISO file and start the installation process. Do not begin the installation
                                             process until you have completed all the steps in this procedure.

Step 5

Verify the NTP status on the publisher node.

If the publisher node fails to synchronize with an NTP server, subscriber node installation can fail. On the Emergency Responder
                                             publisher node, run the utils ntp status CLI command.

Step 6

Complete the following firewall updates:

- If a firewall is in the routing path between nodes, disable the firewall.

- Increase the firewall timeout settings until after you complete the installation.

Temporarily allowing network traffic in and out of the nodes (for example, setting the firewall rule for these nodes to IP
                                             any/any) does not always suffice. The firewall might still close necessary network sessions between nodes due to timeouts.

Step 7

If you use DNS, verify that all servers on which you plan to install Emergency Responder are properly registered in DNS.

Step 8

Cisco Smart Software Licensing

Make sure that your system has adequate licensing.

### Preinstall Tasks for Emergency Responder on Cisco NFVIS-for-UC

Step 1

Plan the installation

Pick an installation method supported by Hypervisor.

Step 2

Required Installation Information

Review the installation requirements and record the configuration settings for each server that you plan to install.

Step 3

Upload the OVA and ISO image.

Upload the OVA as a profile and the ISO as an image together. This process creates a separate profile for each VM configuration
                                             and a single image for the bootable ISO. For more information, refer to the 'Image Registration for CUCM Applications' section
                                             in the Cisco Enterprise Network Function Virtualization Infrastructure Software Configuration Guide . An example OVA file name is: cer_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova .

Step 4

Deploy a VM.

Ensure that an OVA and ISO image is already uploaded.

Navigate to Configuration > Deploy .

Select OTHER as the option when creating virtual machines for your application type.

Connect to the virtual network and assign the Image/Profile (depending on the deployment size that you prefer), and click Deploy .

Open the VM console via Configuration > Virtual Machine > Manage .

Use the console to complete the ISO installation process.

### Preinstall Tasks for Emergency Responder on Nutanix AHV

Step 1

Plan the installation

Pick an installation method supported by Hypervisor.

Step 2

Required Installation Information

Review the installation requirements and record the configuration settings for each server that you plan to install.

Step 3

Create virtual machines in Nutanix AHV and select an OVA per each VM configuration from the Base OVA and deploy using the
                                          OVA.

Download the CER.ova files based on the required configuration from the Software Download page. An example OVA file name for
                                                   a small size deployment is: cer_15_20kusers_ahv_v1.0.sha512.ova .

Upload the CER.ova files (downloaded) onto the Nutanix cluster using Prism Central.

Download the desired Emergency Responder bootable .iso image version from the Software Download page and upload the image
                                                   to the Nutanix cluster.

Creating Emergency Responder Publisher and Subscriber VMs using the .ova files.

Update Emergency Responder VMs to mount CD-ROM with the Emergency Responder image.

#### Uploading OVA Files in Nutanix Prism Central

Step 1

Download the appropriate .ova files from the Software Download page according to the required Emergency Responder configuration.

You can choose Small, Medium, or Large depending up on your preference. For example, cer_15_small_ahv_v1.0.sha512.ova, cer_15_medium_ahv_v1.0.sha512.ova,
                                                cer_15_large_ahv_v1.0.sha512.ova.

Step 2

Log in to Nutanix Prism Central with your credentials.

Step 3

Select Infrastructure from the drop-down menu.

Step 4

Under Compute, Navigate to OVAs from the left pane, and click Upload OVA .

Step 5

Specify a name for the OVA file, and choose the downloaded OVS file by clicking Select File .

Step 6

Click Upload to start the file upload automatically.

Step 7

Verify that the .ova file uploads successfully, indicated by a green progress bar and a Done status.

Step 8

Verify the file upload success from the OVAs page in Prism Central.

#### Upload the Bootable Image to the Nutanix cluster

Step 1

Download the desired version of the CER bootable .iso image from the Software Download page to your local machine.

Step 2

Log in to Nutanix Prism Central or Prism Element with your credentials.

Step 3

In the top-right corner of the Nutanix Prism Central page, click the three-line menu icon.

Step 4

Click Images in the left pane, then select Add Image .

Step 5

On the Add Images page, you can either choose the Image File and click + Add File to select the locally downloaded file to upload to the Nutanix cluster, or select the URL radio button to upload the bootable .iso image from a remote server by providing the NFS path in the Image URL field.

Step 6

Click + Add URL and provide the authentication credentials to connect to the remote server.

Step 7

Click Next and save the changes.

Step 8

Check the status of the image upload on the Tasks page to confirm the successful upload of the .iso image to the Nutanix cluster. For example, a URL is the following: nfs://<Host IP>/<path>/Bootable_UCSInstall_CER_15.0.1.xxxxx-xx.sha512.iso .

## Installation Methods

### Installation Methods Task Flows for VMware vSphere ESXi

Choose one of the following installation methods task flows:

Task Flow

Description

Installation on a New System

Use this method for basic install of Emergency Responder.

Touchless Installation Task Flow for ESXi

Use this task flow to install an Emergency Responder cluster dynamically without the need for manual intervention.

Install with Data Import

Complete this task to install an Emergency Responder cluster using the Install with Data Import .

### Installation Methods Task Flows for Cisco NFVIS-for-UC

Choose one of the following installation methods task flows:

Task Flow

Description

Installation on a New System

Use this method for basic install of Emergency Responder.

Touchless Installation Task Flow for Cisco NFVIS-for-UC

Use this task flow to install an Emergency Responder cluster dynamically without the need for manual intervention.

Install with Data Import

Complete this task to install an Emergency Responder cluster using the Install with Data Import .

### Installation Methods Task Flows For Nutanix AHV

Choose one of the following installation methods task flows:

Task Flow

Description

Installation on a New System

Use this method for basic install of Emergency Responder.

Touchless Installation Task Flow for Nutanix AHV

Use this task flow to install an Emergency Responder cluster dynamically without the need for manual intervention.

Install with Data Import

Complete this task to install an Emergency Responder cluster using the Install with Data Import .

### Installation on a New System

This procedure describes how to install Emergency Responder  as a new installation.

You enter Emergency Responder group configuration through the Emergency Responder Administration web interface based on Publisher
                              (primary) and Subscriber (secondary) server pairs as described in the following sections.

From Release 15SU2 onwards, if you need to perform manual or scheduled DRS backups or if you want to change the server hostname,
                                          it is not required to manually exchange any tomcat certificate between the publisher and subscriber nodes. The publisher certificate
                                          gets synched to the subscriber node automatically.

#### Install Emergency
                              	 Responder Publisher

To install Emergency Responder, you install the Publisher (primary) first, then you install the Subscriber (backup) on a separate
                                    server. You must install Emergency Responder on separate servers from Cisco Unified Communications Manager or any Cisco Unified
                                    Communications applications.

Allow
                                    		  approximately 1 hour to perform a new installation.

Step 1

Insert the Emergency Responder Installation DVD.

If the system finds the DVD, you are asked if you want to perform a media check before installation to determine if there
                                                are problems with the DVD. The system displays the checksum of the DVD and instructs you to verify this checksum on the Emergency
                                                Responder website.

At the bottom of the screen you will see instructions for moving between elements and for selecting elements, as follows:

- Use the Tab key to advance to the next element.

- Use the Alt-Tab key combination to return to the previous element.

- Use the Space bar to select a highlighted element.

If you choose to perform the media check, the system performs the media check and displays the results.

If the result of the media check is PASS , click OK . The system install begins the installation. Skip to Step 2.

If the result of the media check is FAIL , obtain a new installation DVD from Cisco Systems.

Step 2

The Cisco Emergency Responder system installer starts. The Product Deployment Selection screen displays a message saying the
                                             Cisco Emergency Responder product suite is installing. Click OK to continue.

Step 3

The Proceed with Install page displays the current software version on the hard drive and the software version on the installation
                                             DVD.

If you are performing a fresh installation, there will be no software on the hard drive and the system asks if you want to
                                                proceed with the installation. Click Yes to proceed.

If you are performing an upgrade, the system displays the current software version and asks it you want to overwrite the hard
                                                drive. Click Yes to proceed.

If you click Yes , the system continues with the installation and the Platform Configuration Wizard appears.

If you click No , the installation is terminated.

Step 4

On the Platform Configuration Wizard page, click Proceed to continue with the platform installation.

To continue with Install with Data Import , choose Import . Use this installation method for direct migrations (Fresh Install with Data Import) from the older versions of Emergency
                                                      Responder.

If you click Skip , the system installs both the platform and Emergency Responder software without prompting you to provide information during
                                                      the installation. After the installation is completed and the system reboots, you are prompted to enter the required configuration
                                                      details.

Step 5

Click Continue to proceed. The Timezone Configuration page appears.

Step 6

Choose the correct time zone to use from the list provided.

Use the following keys to move between elements on the Timezone Configuration page:

- Arrow Up or Arrow Down to select a time zone from the list

- After selecting the correct time zone, click OK . The Auto Negotiation Configuration page appears.

Step 7

Click Yes to enable autonegotiation of the Ethernet NIC speed and duplex mode. The DHCP Configuration page appears. If you click Yes , skip to Step 10.

If you click No , the NIC Speed and Duplex Configuration page appears.

Step 8

On the NIC Speed and Duplex Configuration page, do the following:

Select the NIC Speed. The available options are 10 Megabit, 100 Megabit, or 1000 Megabit.

Select the NIC Duplex setting. The available options are Full or Half.

Click OK . The DHCP Configuration page appears.

Step 9

On the MTU Configuration page, you can set the maximum transmission unit (MTU) that can be sent in a network as follows:

Click Yes if you want to configure a a MTU value of less than 1500 bytes.

Click No to use the default MTU value of 1500 bytes.

Step 10

If you chose not to use DHCP, enter the following information about the Static Network Configuration page:

- Host Name

- IP Address

- IP Mask

- Gateway (GW) Address

Click OK . The DNS Client Configuration page appears.

Step 11

On the DNS Client Configuration page, you are asked if you want to configure the Domain Name System (DNS) client.

Click the Help button for details about configuring DNS.

If you select Yes , a second DNS Client Configuration page appears.

If you select No , the Administration Login Configuration page appears. Skip to Step 14.

Step 12

On the second DNS Client Configuration page, you are prompted to enter the following information:

- Primary

- Secondary DNS (optional)

- Domain

Click OK . The Administration Login Configuration page appears.

Step 13

On the Administration Login Configuration page, enter an ID and password for the Administrator account. This password is used
                                             to access the CLI and the CiscoUnifiedOS Administration and Disaster Recovery System (DRS) websites. Click Help to display guidelines for creating this password.

When you have finished, click OK . The Certificate Information page appears.

Step 14

Enter the following information about the Certificate Information page:

- Organization

- Unit

- Location

- State

- Country (select from the scroll-down menu).

Click OK . The Publisher Configuration page appears.

Step 15

Based on the type of installation you are performing, do one of the following:

- If the server you are configuring is the Publisher in the server group, click Yes . The Network Time Protocol Client Configuration page appears. Proceed to Step 17.

- If the server you are installing is not the Publisher in the server group, you must first configure this server on the Publisher
                                                before you can proceed. This server must also have network access to the Publisher, which must be in service for the installation
                                                to complete successfully. Click No only if you are configuring the Subscriber. See Install Emergency Responder Subscriber for information about installing the Subscriber.

Step 16

On the Network Time Protocol Client Configuration page, you are asked if you want to set up external Network Time Protocol
                                             (NTP) servers.

We strongly recommend that you use external NTP servers to ensure that the system time is kept accurate.

Caution

For Emergency Responder install on UCS servers, it is mandatory to configure NTP server.

If you click Yes , the system displays a second Network Time Protocol Client Configuration page. In the fields provided, enter the IP address
                                                or hostname of the external NTP servers, then click OK . The Database Access Security Configuration page appears. Skip to Step 18.

If you click No , the Hardware Clock Configuration page appears. Enter the following information:

- Year [yyyy]

- Month [mm]

- Day [dd]

- Hour [hh]

- Minute [mm]

- Second [ss]

When you finish entering this information, click OK . The Database Access Security Configuration page appears.

Step 17

On the Database Access Security Configuration page, enter the security password and then confirm the password in the fields
                                             provided.

The security password must be at least six characters long and can contain alphanumeric characters, hyphens, and underscores.
                                                            It must start with an alphanumeric character. The security password is used for secure communications between Emergency Responder
                                                            server groups when performing the installation or upgrade, DRS backup or restore, and "Point to a new Publisher" operations.

Click Help to display guidelines. When you finish, click OK . The SMTP Host Configuration page appears.

Step 18

You are asked if you want to configure a Simple Mail Transport Protocol (SMTP) host. This step is optional.

- If you click Yes , a second SMTP Host Configuration page appears. Click Help for guidelines, then enter the SMTP hostname or IP address in the field provided. When you are finished, click OK . The Platform Configuration Confirmation page appears.

- If you click No , the Platform Configuration Confirmation page appears.

Step 19

On the Platform Configuration Confirmation page, do one of the following:

After you select OK , you cannot modify the platform configuration information.

- Select Back if you want to return to the previous page to make modifications. Continue to select Back to scroll through each platform configuration page.

- Select Cancel to cancel the installation.

Step 20

On the Security End User Language Selection page, choose a language for the Cisco Emergency Responder web pages. The system
                                             defaults to the English language.

The Application User Password Configuration page appears.

Step 21

On the Application User Configuration page, enter the username and password. This username and password is associated with
                                             the default administrative account and is used to log in to the Emergency Responder Administration web page. Click Help for guidelines.

When you are finished, click OK . The Cisco Emergency Responder Configuration Confirmation page appears.

Step 22

On the Cisco Emergency Responder Configuration Confirmation page, do one of the following:

Caution

After you select OK , you cannot modify the Cisco Emergency Responder configuration information.

- Select Back if you want to return to the previous page to make modifications. Continue to select Back to scroll through each Emergency Responder Application User Configuration page.

- Select Cancel to cancel the installation.

Step 23

After the system reboots, it checks the status of various system components. If the system finds any problems, you are prompted
                                             to correct the problem.

If the system does not find any problems, the installation process continues. The system ejects the installation DVD, reboot,
                                                and then finishes the installation. When the installation is complete, a CLI prompt appears.

During this process, the system displays the MAC address of the Publisher. Write down the MAC address when it displays; you
                                                            use the MAC address later to acquire Emergency Responder licenses. If you are not able to capture the MAC address during installation,
                                                            you can look it up later. See the 'Server Licenses' section for information about looking up the server MAC address.

Step 24

To bring up the Emergency Responder websites, go to any Windows system on the network, start a supported web browser, and
                                             enter the following URL:

http://your Emergency Responder hostname/

or

http://your Emergency Responder IP address/

Make sure that the Emergency Responder is configured with DNS so that hostname is resolved to the IP address.

#### Install Emergency
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

Log in the Publisher Emergency Responder Administration user interface.

Select System > Add Subscriber .

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

The Platform Configuration Complete page appears. Select one of the following options:

- If the Publisher information is correct, click OK .

- If the information is not correct, click the Back button and make the needed corrections on the Publisher Access Configuration page, then click OK .

The installation of the Emergency Responder Subscriber begins and takes an additional 20-30 minutes to complete.

Step 9

When the
                                             			 installation completes, go to the Emergency Responder Administration website on
                                             			 the Subscriber to verify that the Subscriber was installed successfully. If the
                                             			 installation succeeded, a message saying "Primary Cisco
                                                				Emergency Responder is active" appears. This message indicates that the
                                             			 Subscriber was installed successfully.

If the
                                                            				  Subscriber installation cannot validate the Publisher, See Cannot Validate Publisher in the Troubleshooting chapter.

### Touchless Installation

Previous releases of Cisco Emergency Responder (Emergency Responder) cluster environment required you to install the publisher
                                 node first before you proceed to install the subscriber nodes. You had to install the subscriber node after adding this node
                                 details to the Cisco ER Administration > Add Subscriber page of the publisher node first before you proceed to install the subscriber nodes.

Touchless installation makes the installation process seamless and promotes simplified installation of Emergency Responder.
                                 With the CER server Group touchless installation, the subscriber node is configured dynamically along with the publisher node
                                 during their installation. The touchless installation proceeds without the requirement to provide any subscriber details in
                                 the installation wizard as the subscriber is not dependent on the installation of the publisher.

This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC.

This feature has the following benefits:

No manual intervention and scheduling during the deployment of a new cluster.

No manual entry of the subscriber node to an existing cluster.

No requirement to wait until the publisher node is active.

#### Answer File Generator

Use the Answer File Generator (AFG) tool ( http://www.cisco.com/web/cuc_afg/index.html ) to generate the answer files or ISO images for configuration. These files include clusterConfig.xml and platformConfig.xml
                                 files.

Start the virtual machine on which you mounted the ISO image to start the Emergency Responder installation. No manual intervention
                                 is required during installation of a standalone node. In a cluster environment, you can install both the publisher node and
                                 the subscriber node simultaneously. Sometimes, the installation of the subscriber node can stop during the installation of
                                 the publisher node. In this case, after the publisher node installation is complete, it generates a signal for the subscriber
                                 node to continue the installation.

#### Predefined Cluster Configurations (AFG Process)

With the implementation of this feature, the Answer File Generator (AFG) tool generates the clusterConfig.xml file along with
                                 the existing the platformConfig.xml file. If you provide the details of the subscriber node to the AFG tool, the clusterConfig.xml
                                 file includes those details. After the Emergency Responder publisher is installed, it reads the clusterConfig.xml file and
                                 if the publisher finds any subscriber node, it adds them to its cerserver tables. Adding the subscriber to cerserver tables
                                 eliminates the need to wait for the Emergency Responder publisher to finish its installation, and then manually add the subscriber
                                 on the server page. The entire installation process occurs automatically.

#### Touchless Installation Task Flow for ESXi

Complete these tasks to install your Emergency Responder clusters in a single process using the touchless installation method.

##### Before you begin

Preinstall Tasks for Emergency Responder on VMware vSphere ESXi

Step 1

Generate Answer Files for Touchless Install

Use this procedure to generate the configuration files (clusterconfig.xml and platformconfig.xml) with your network settings.
                                                The touchless install process uses these files to install and configure the various cluster nodes.

Step 2

Generate ISO Images

Use this procedure to create ISO images from the answer files. You will use the ISO image in your touchless installation.

Step 3

Upload ISO Image to Datastore

Use this procedure to upload the ISO image to the datastore.

Step 4

Mount ISO Image to VM

Use this procedure to mount the UC application ISO image on their corresponding VM.

Step 5

Run Touchless Install

Begin the cluster installation. You can kick off all node installations simultaneously.

##### Generate Answer Files for Touchless Install

Use this procedure to generate answer files for your touchless installation of your cluster. The answer files (clusterconfig.xml
                                       and platformconfig.xml) contain the configuration information that the install process installs and configures on each cluster
                                       node.

###### Before you begin

You must have already planned your network topology, including addresses for your Emergency Responder cluster nodes.

Step 1

Log in to the Cisco Emergency Responder Answer File Generator application at https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html .

Step 2

In the Hardware section, choose Virtual Machine .

Step 3

From the Product section, select the product and version that you want to install.

Step 4

In the Software Location of Data to Import section, check the Configure Software Location of Data to Import check box to configure Remote SFTP server details only if you choose to install using the Fresh Install with Data Import.
                                                Else ignore this step and proceed to step 5. For more details, see Install with Data Import .

By checking the Configure Software Location of Data to Import check box it disables, Administrator Credentials, Security Password, Application User Credentials fields. These details are
                                                   imported from source node data during installation. Enter the following fields:

Remote Server Name or IP —The Secure FTP (SFTP) server that stores the source cluster's exported data.

Export Data Directory —Directory path of the server containing export data.

Remote Server Login ID —Allows data retrieval of the remote SFTP server.

Remote Server Password —Can contain alphanumeric characters, hyphens, and underscores.

Step 5

Complete the remaining fields under Clusterwide Configuration with your cluster configuration details.

Step 6

Complete the fields in the Primary Node Configuration with configuration details for the publisher node.

Step 7

Under Secondary Node Configuration , enter the node details for your subscriber node and click Add Secondary Node .

Step 8

Add your subscriber node.

Step 9

Click Generate Answer Files .

Step 10

Download the answer files to your computer.

##### Generate ISO Images

Use this example procedure to create ISO images from the answer files. You will use the ISO images in your touchless installation.

This procedure describes how to use Winimage to create ISO images.

Step 1

From Winimage, choose File > New .

Step 2

From the Standard format, choose 1.44 MB and click OK .

Step 3

Navigate to the Menu Image, choose Inject and select the platformConfig.xml file.

Step 4

When prompted to inject the file into Winimage, click Yes .

Step 5

Choose File > Save As .

Step 6

Save the file as an ISO image (.iso file) using the following naming convention: Emergency Responder—cer.iso .

Step 7

Repeat these steps for the other Emergency Responder server groups in the cluster.

##### Upload ISO Image to Datastore

Use this procedure to upload the ISO images to the datastore.

Step 1

Start the vSphere client.

Step 2

Select the Configuration tab.

Step 3

Select Storage .

Step 4

Right-click on a datastore and Browse the datastore.

Step 5

Navigate to the destination directory and click the Upload files to this datastore icon.

Step 6

Upload the ISO images to your local folder.

Step 7

At the Upload/Download warning, click Yes .

Step 8

Close the Datastore Browser window.

##### Mount ISO Image to VM

Use this procedure to mount the UC application ISO images on their corresponding virtual machine (VM).

Step 1

In the vSphere client, choose the virtual machine.

Step 2

Open VMware Remote Console (VMRC), and click the CD/DVD Drive 2 .

Step 3

Browse to the datastore and locate the ISO image.

Step 4

Select the file and click OK .

Step 5

Under Device Status , enable the Connected and Connect at power on option.

Step 6

Click the Options tab. Under Boot Options , check Force entry to BIOS and click OK .

Step 7

Repeat this procedure for each VM on which you want to install a node.

##### Run Touchless Install

After you have mounted your ISO image to your application VMs, run the touchless installation process. You can install all
                                       nodes simultaneously.

Step 1

In vSphere client, right-click the VM and select Open Console . A console window opens.

Step 2

Click the Power On icon in the console toolbar to power on the virtual machine.

Step 3

When the BIOS screen appears, configure the following boot order:

CD-ROM

Hard Drive

Removable Devices

Network

Step 4

Save the settings and exit from the console. The installation commences immediately.

Step 5

Repeat these steps for each cluster node. All cluster nodes may install in parallel; you do not have to install them serially.

Step 6

After to emphasize the completion of an activity, remove the ISO configurations from the virtual machines.

#### Touchless Installation Task Flow for Cisco NFVIS-for-UC

Complete these tasks to install your Emergency Responder in a single process using the touchless installation method.

##### Before you begin

Preinstall Tasks for Emergency Responder on Cisco NFVIS-for-UC

Step 1

Generate Answer Files for Touchless Install

Use this procedure to generate the configuration files (clusterconfig.xml and platformconfig.xml) with your network settings.
                                                The touchless install process uses these files to install and configure the various cluster nodes.

Step 2

Generate ISO Images

Use this procedure to create ISO images from the answer files. You use this ISO image in your touchless installation.

Step 3

Upload ISO Image to Datastore

Use this procedure to upload the ISO image to the datastore.

Step 4

Deploy VM via NFVIS Portal

Use this procedure to deploy the VM. After deployment, the installation starts automatically.

##### Generate Answer Files for Touchless Install

Use this procedure to generate answer files for your touchless installation of your cluster. The answer files (clusterconfig.xml
                                       and platformconfig.xml) contain the configuration information that the install process installs and configures on each cluster
                                       node.

###### Before you begin

You must have already planned your network topology, including addresses for your Emergency Responder cluster nodes.

Step 1

Log in to the Cisco Emergency Responder Answer File Generator application at https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html .

Step 2

In the Hardware section, choose Virtual Machine .

Step 3

From the Product section, select the product and version that you want to install.

Step 4

In the Software Location of Data to Import section, check the Configure Software Location of Data to Import check box to configure Remote SFTP server details only if you choose to install using the Fresh Install with Data Import.
                                                Else ignore this step and proceed to step 5. For more details, see Install with Data Import .

By checking the Configure Software Location of Data to Import check box it disables, Administrator Credentials, Security Password, Application User Credentials fields. These details are
                                                   imported from source node data during installation. Enter the following fields:

Remote Server Name or IP —The Secure FTP (SFTP) server that stores the source cluster's exported data.

Export Data Directory —Directory path of the server containing export data.

Remote Server Login ID —Allows data retrieval of the remote SFTP server.

Remote Server Password —Can contain alphanumeric characters, hyphens, and underscores.

Step 5

Complete the remaining fields under Clusterwide Configuration with your cluster configuration details.

Step 6

Complete the fields in the Primary Node Configuration with configuration details for the publisher node.

Step 7

Under Secondary Node Configuration , enter the node details for your subscriber node and click Add Secondary Node .

Step 8

Add your subscriber node.

Step 9

Click Generate Answer Files .

Step 10

Download the answer files to your computer.

##### Generate ISO Images

Use this procedure to create ISO images. You will use the ISO images in your touchless installation.

This procedure describes how to use AnyBurn Tool to create ISO images. You can download any free version from https://www.anyburn.com/download.php .

NFVIS does not support ISO images created with the WinImage tool because WinImage does not generate ISO files in the true
                                                   ISO 9660 format required by NFVIS.

Step 1

Open any AnyBurn tool.

Step 2

From the options, select Create image file from files/folders .

Step 3

Click Add and include all the files that you want to include in the ISO.

Step 4

To create a destination and image name, select the path where you want to save the new ISO file and enter the required file
                                                name.

Step 5

Click Create Now to generate the ISO file.

##### Upload ISO Image to Datastore

Collaboration applications require registration of both the ISO image (installation media) and the OVA file (metadata). You
                                       must upload both the files at the same time. NFVIS supports two registration methods:

Local Registration : Upload files directly from your computer.

Remote Registration : Download files from a remote server using HTTP, HTTPS, FTP, or SCP.

Use this procedure to upload the ISO image to the datastore.

Step 1

Use this method when the ISO and OVA files are available on your local computer. To upload an image using the local registration
                                                method, perform the following:

Navigate to Configuration > Virtual Machine > Images > Image Repository .

To upload the ISO image, click Upload and select the ISO file from your local file system. For example: Bootable_UCSInstall_CER_15.0.1.xxxxx-xx.sha512.iso .

To configure the Image Properties, enter a pre-populated name in the Image Name to a descriptive name. For example, cer-15.0.1 . Also, select a VM Type from the drop-down list. If your application type is not listed, select OTHER .

To upload an OVA Metadata, select the Metadata checkbox, click Upload OVA , and select the OVA file. For example, cer_15_30kusers_ahv_v1.0.sha512.ova .

To configure additional options, select the Dedicated Cores check box (recommended for production environments). This allocates dedicated CPU cores to the VM for improved performance.

To submit the registration, click the Upload File button.

NFVIS performs the following:

Upload the ISO image

Upload and parse the OVA file

Register the image

Automatically create profiles/flavors from OVA metadata

To verify registration, wait for the process to complete. The image should appear in the Image Repository with the status Active . Verify that flavors are populated from the OVA file.

Step 2

Use this method when files are hosted on a remote server (HTTP, HTTPS, FTP, or SCP). To upload an image using the remote registration
                                                method, perform the following:

Navigate to Configuration > Virtual Machine > Images > Image Repository .

To select the Remote Registration, click Register Image and select Remote Image Registration option.

To configure the Image Details, enter a descriptive name in the Image Name field. For example, cer-15.0.1 .

To configure the Remote Server Connection Protocol, enter the following details:

Protocol : Select from the drop-down list (HTTP/HTTPS/FTP/SCP).

IP Address : Enter the server hostname or IP address.

Image File Path : Enter the directory path to the ISO file with the image name. For example: Bootable_UCSInstall_CER_15.0.1.xxxxx-xx.sha512.iso

Enter the Configure Authentication details for FTP/SCP (only).

Username : Enter the username for the remote server.

Password : Enter the password.

To upload an OVA Metadata, select the Metadata checkbox, and enter the OVA File Path name. For example, cer_15_30kusers_ahv_v1.0.sha512.ova .

The OVA file must be on the same server as the ISO file. Different remote servers for the ISO and OVA files are not supported.

To configure additional options, select the Dedicated Cores check box if necessary.

To submit the registration, click the Submit button.

NFVIS performs the following:

Download the ISO image from the remote server

Upload and parse the OVA file

Register the image

Automatically create profiles/flavors from OVA metadata

To verify registration, wait for the process to complete. The image should appear in the Image Repository with the status Active . Verify that flavors are populated from the OVA file.

Downloading large files may take several minutes.

##### Deploy VM via NFVIS Portal

Use this procedure to deploy the VM instance.

Step 1

Navigate to Configuration > Deploy to deploy a new virtual machine.

Step 2

Select an option from the VM. If your application type is not listed, select OTHER . If necessary, you can change the name of the VM Type created.

Step 3

Choose the required image from the drop-down list. Images are populated based on the VM type selected. For example, cer-15.0.1 .

Step 4

Select the appropriate flavor (with the image name) based on your sizing requirements.

Flavors are populated based on the selected image and are automatically created from the OVA file during image registration.

Step 5

(Optional) Enter the Group Name, VNC Password, Deployment Disk, and Low Latency (TRUE).

Step 6

To configure Network Connections, perform the following in the Network Design section:

Locate the VM icon on the canvas.

Drag a line from the VM to the desired network.

Connect to the appropriate network(s) for your deployment. Enter the directory path to the ISO file.

Add additional networks as required.

Step 7

To attach the bootstrap ISO, select the Bootstrap ISO check box, click Upload , and select your Day 0 configuration ISO.

Step 8

To deploy the VM, click the Deploy button.

The system will validate the configuration. If validation errors occur, they will be displayed for correction.

Step 9

Navigate to Configuration > Virtual Machine > Manage to monitor the deployment.

Step 10

To access the VM console, once the VM is in ACTIVE state, click the Terminal button in the VM row.

Monitor the installation progress via the console.

Follow the application-specific installation prompts.

#### Touchless Installation Task Flow for Nutanix AHV

Complete these tasks to install your Emergency Responder in a single process via the touchless installation method.

##### Before you begin

Preinstall Tasks for Emergency Responder on Nutanix AHV

Step 1

Generate Answer Files for Touchless Install

Use this procedure to generate the configuration files (clusterconfig.xml and platformconfig.xml) with your network settings.
                                                The touchless install process uses these files to install and configure a single node or the various cluster nodes.

Step 2

Generate ISO Images

Use this procedure to create ISO images from the answer files. You use this ISO image in your touchless installation.

Step 3

Upload ISO Image to Datastore

Use this procedure to upload the ISO images to the datastore.

Step 4

Power On the Virtual Machine

You can kick off all node installations simultaneously.

##### Generate Answer Files for Touchless Install

Use this procedure to generate answer files for your touchless installation of your cluster. The answer files (clusterconfig.xml
                                       and platformconfig.xml) contain the configuration information that the install process installs and configures on each cluster
                                       node.

###### Before you begin

You must have already planned your network topology, including addresses for your Emergency Responder cluster nodes.

Step 1

Log in to the Cisco Emergency Responder Answer File Generator application at https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html .

Step 2

In the Hardware section, choose Virtual Machine .

Step 3

From the Product section, select the product and version that you want to install.

Step 4

In the Software Location of Data to Import section, check the Configure Software Location of Data to Import check box to configure Remote SFTP server details only if you choose to install using the Fresh Install with Data Import.
                                                Else ignore this step and proceed to step 5. For more details, see Install with Data Import .

By checking the Configure Software Location of Data to Import check box it disables, Administrator Credentials, Security Password, Application User Credentials fields. These details are
                                                   imported from source node data during installation. Enter the following fields:

Remote Server Name or IP —The Secure FTP (SFTP) server that stores the source cluster's exported data.

Export Data Directory —Directory path of the server containing export data.

Remote Server Login ID —Allows data retrieval of the remote SFTP server.

Remote Server Password —Can contain alphanumeric characters, hyphens, and underscores.

Step 5

Complete the remaining fields under Clusterwide Configuration with your cluster configuration details.

Step 6

Complete the fields in the Primary Node Configuration with configuration details for the publisher node.

Step 7

Under Secondary Node Configuration , enter the node details for your subscriber node and click Add Secondary Node .

Step 8

Add your subscriber node.

Step 9

Click Generate Answer Files .

Step 10

Download the answer files to your computer.

##### Generate ISO Images

Use this procedure to create ISO images from the answer files. You will use the ISO images in your touchless installation.

This procedure describes how to use WinImage to create ISO images. You can download WinImage from https://www.winimage.com/download.htm .

Step 1

From WinImage, choose File > New .

Step 2

From the Standard format, choose 1.44 MB and click OK .

Step 3

Navigate to the Menu Image, choose Inject , and select the platformConfig.xml and the clusterConfig.xml file for the Emergency Responder Publisher node. For Emergency Responder Subscriber, choose Inject , and select the platformConfig.xml file only.

Step 4

When prompted to inject the file into WinImage, click Yes .

Step 5

Choose File > Save As .

Step 6

Choose All files from the drop-down for the Save as type and specify the file name as an ISO image (with .iso file extension, for example imagename.iso ) using the following naming convention: Emergency Responder— cer.iso .

Step 7

Repeat these steps for the other Emergency Responder server groups in the cluster.

##### Upload ISO Image to Datastore

Create ISO images for the Emergency Responder publisher and subscriber node based on the generated answer file, and upload
                                       the <cer_answer_file>.iso for the publisher and subscriber to the Nutanix clusters. In case of manual installation of Emergency
                                       Responder, the second CD-ROM does not need to be mounted with the <cer_answer_file>.iso file.

Step 1

Download the desired version of the Emergency Responder bootable .iso image from the Software Download page to your local
                                                machine.

Step 2

Log in to Nutanix Prism Central or Prism Element with your credentials.

Step 3

In the top-right corner of the Nutanix Prism Central page, click the three-line menu icon.

Step 4

Click Images in the left pane, then select Add Image .

Step 5

On the Add Images page, you can either choose the Image File and click + Add File to select the locally downloaded file to upload to the Nutanix cluster, or select the URL radio button to upload the bootable .iso image from a remote server by providing the NFS path in the Image URL field.

Step 6

Click + Add URL and provide the authentication credentials to connect to the remote server.

Step 7

Click Next and save the changes.

Step 8

Check the status of the image upload on the Tasks page to confirm the successful upload of the .iso image to the Nutanix cluster. For example, a URL is the following: nfs://<Host IP>/<path>/Bootable_UCSInstall_CER_15.0.1.xxxxx-xx.sha512.iso .

##### Power On the Virtual Machine

After you have mounted your ISO image to your application VMs, run the touchless installation process. You can install all
                                       nodes simultaneously.

### Install with Data Import

This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC.

#### Pre-Migration Tasks

Perform the tasks in this list for the mentioned migration methods.

Step 1

IPsec Requirements

Applicable for both Simple and Network Migrations

Before starting the migration, disable the IPsec policy on both the Publisher and Subscriber nodes.

Step 2

Configure SAML SSO

Applicable for both Simple and Network Migrations

Ensure that FIPS mode is enabled before configuring SSO and starting the migration.

Step 3

CTI Route Points and Ports Re-Registration

Applicable only for Simple Migration

After registering the source Emergency Responder with Unified Communications Manager in mixed mode, ensure the following before
                                                starting the migration:

Use only one application user, or a unique application user that is not assigned to any other Emergency Responder.

Use only one set of Certificate Authority Proxy Function (CAPF) profiles. These profiles must not be associated with any other
                                                      server or application user.

When migrating from Release 12.5(1)SU9 Emergency Responder with Emergency Responder operating in FIPS mode and Unified Communications
                                                            Manager in mixed mode, ensure that you update the CAPF profiles on Unified CM and the CAPF passwords in Emergency Responder
                                                            after the migration.

##### Configure SAML SSO

Enable FIPS before configuring SSO and perform the following steps.

Step 1

Verify the signing algorithm by running the CLI command: utils sso show signing-algorithm .

Step 2

If the signing algorithm is SHA-1, change it to SHA-256 using the CLI command: utils sso set signing algo sha256 .

Step 3

Enable SSO and proceed with the migration steps.

#### Install with Data Import

When creating a migration cluster using the Install with Data Import method, specify whether all destination cluster nodes
                                    will retain the same hostname or IP address, or a different network address. Based on this, there are two types of data migration:

Simple Migration : All destination target nodes use the source node settings.

Network Migration : One or more destination target nodes use new network settings.

Use the following procedure to configure Cisco Emergency Responder (Emergency Responder) installation with data import from
                                    an older version of Emergency Responder.

Important

Fresh Install with Data Import does not support domain name changes. If DNS is enabled on the publisher node of the target
                                                      destination, the domain name must match the source destination. If the domain name must change, install the target destination
                                                      on the publisher without the DNS enabled and then enable DNS via the CLI after the installation is complete. The subscriber
                                                      node can be installed with the DNS enabled, but ensure that the System > Add Subscriber entries on the publisher node are correct before installing the subscriber.

If you plan to change the hostname and/or IP address during the migration, the System > Add Subscriber entries must be updated on the publisher node of the target destination prior to installing the subscriber.

Fresh Install with Data Import does not support installation with DHCP configuration. If DHCP is enabled on the source destination,
                                                      install the target destination with Static configuration data and then configure the DHCP later post migration.

Ensure that the publisher/subscriber nodes are exported to the SFTP server before proceeding with Fresh Install with Data
                                                Import.

##### Before you begin

Step 1

Export data from the source destination publisher node.

Run the utils system upgrade dataexport initiate CLI command on each node of the desired source system to export the data which can be imported using this procedure.

Enter the SFTP server information to export the data.

Enter the node Hostname and IP Address (it is possible to change them at this stage.)

Run the utils system upgrade dataexport status to track the export status.

Step 2

Export data from the source destination subscriber node.

Run the utils system upgrade dataexport initiate CLI command on each node of the desired source system to export the data which can be imported using this procedure.

Enter the SFTP server information to export data.

Enter the node Hostname and IP Address (it is possible to change them at this stage).

Run the utils system upgrade dataexport status to track the export status.

Step 3

Then proceed with one of the following methods to complete installation/import.

During the configuration of an IP address, if the source and target destinations are using DHCP, ensure that you configure
                                                            a static IP address for the target destination. For example, the current IP address of the source destination.

Installation Method

See

Attended Install

Install a new publisher and import the data. To configure Emergency Responder with Install with Data Import follow the instructions as described in Install Emergency Responder Publisher from step 1 through 4.

In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Emergency Responder installation.

In the import wizard, provide details for the following information:

Hostname, IP Address, Subnet mask, and Gateway. This must be the same information provided in the destination node for which
                                                                        you exported the data.

SFTP—In the export data directory, enter the exported data folder name or cluster information: <Publisher IP Address>.

Confirm whether this is the First Node.

Enter one or more NTP servers.

If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node.

Install a new Subscriber and import the data. Repeat step 4 except for the First Node question. Respond to this query with
                                                                  a 'No' and provide the new publisher IP Address and hostname information.

If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node.

Touchless Install of a Single Node or a Cluster

Follow the instructions as described in Touchless Installation Task Flow for ESXi from step 1 through 5.

If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command.

##### What to do next

Post-Migration Tasks

#### Post-Migration Tasks

Perform the tasks in this list for the mentioned migration methods.

Step 1

Licensing

Applicable for both Simple and Network Migrations

You must reregister the license after migrating to the new Cisco Emergency Responder server. For more information on configuration,
                                                see License Manager .

Step 2

CTI Route Points and Ports Re-Registration

Applicable only for Network Migration

We recommend that you reregister the CTI Route Points and ports for the destination Emergency Responder Publisher and Subscriber
                                                nodes after network migration.

Step 3

(Optional) CTI Route Points and Ports Re-registration in Mixed Mode

Applicable for both Simple and Network Migrations

Post migration, you must perform this procedure to reregister the CTI Route Points and ports in mixed mode.

Step 4

Clustering

Applicable only for Network Migration

Consider the following for clustering points post migration:

Old Hostnames Retained in Cisco ER Groups After Network Migration —After a network migration, identify and update all outdated hostname entries (Publisher and Subscriber) with the new hostnames
                                                      and corresponding passwords in the Cisco ER Groups on both clusters. Restart both the clusters and verify that the hostname
                                                      changes are correctly reflected across all nodes.

Tomcat Certificate Exchange Required in CER Clustering Setup Post Migration in Secure Mode —After a network migration, redo the Tomcat exchange in the cluster.

Step 5

Upload a New National E911 Certificate After Network Migration

Applicable for both Simple and Network Migrations

Ensure that you upload a new National E911 Certificate if you are migrating from Release 12.5(1)SU9.

Step 6

Configure Off-premises Settings

Applicable only for Network Migration

You must re-configure the Off-premises settings in the Cisco Unified Communications Manager Administration user interface.

Step 7

SAML SSO

Applicable only for Network Migration

After you complete the network migration, ensure that you re-enable SSO on the destination nodes. This step is required because
                                                SAML SSO was previously enabled on the source Emergency Responder nodes metadata.

Step 8

Update Unified CM Node on Emergency Responder After Unified CM Network Migration

Perform this procedure only after a Network Migration of your Unified Communications Manager server.

Delete the Unified CM server and SNMPv2 settings from the Emergency Responder configuration and reconfigure it after network
                                                migration.

##### CTI Route Points and Ports Re-Registration

Step 1

To delete the Unified Communications Manager entry from the source node, perform the following steps after successful migration:

Log in to the Cisco Emergency Responder Administration Servlet on the source node.

Navigate to Phone Tracking > Cisco Unified Communications Manager .

Delete the connected Unified Communications Manager entry.

Step 2

To reregister CTI Route Points and CTI Ports on the destination Emergency Responder Publisher and Subscriber nodes, restart
                                                the Cisco Emergency Responder service by entering the following command: utils service restart Cisco Emergency Responder .

In case the CTI Ports does not reregister, perform the following steps:

Log in to the Cisco Unified CM Administration user interface.

Navigate to Device > CTI Route Points .

Select the Emergency Call Route Points (for example, 911, 912, and 913) and select Reset > Refresh .

##### (Optional) CTI Route Points and Ports Re-registration in Mixed Mode

For CTI Route Points Registration, perform these additional steps after successful migration.

For Simple Migration , after registering the source Emergency Responder with Unified Communications Manager in mixed mode, and before starting
                                                      the migration, ensure that:

You migrate using only one application user, or use a unique application user that is not currently assigned to any other
                                                               Emergency Responder.

You use only one set of Certificate Authority Proxy Function (CAPF) profiles, and these profiles are not attached to any other
                                                               server or application user.

After you complete the Network Migration , perform the following steps:

On the Emergency Responder source nodes, delete the Unified CM entry from Phone Tracking > Cisco Unified Communications Manager .

Restart the Cisco Emergency Responder service on the source Emergency Responder publisher node.

In the Cisco Unified CM Administration user interface, navigate to the User Management > User Settings > Application User CAPF Profile menu, and delete the existing CAPF profiles and readd them, OR create new CAPF profiles and provide the details in the destination
                                                               Emergency Responder ( Phone Tracking > Cisco Unified Communications Manager ).

In the Cisco Unified CM Administration user interface, navigate to Device > CTI Route Points . The CTI Route Points should register automatically. If they do not register, restart the CTI Route Points.

##### Upload a New National E911 Certificate After Network Migration

When you migrate your Emergency Responder from Release 12.5(1)SU9 to Release 15SU4 or higher, the old .psf certificate is
                                                   no longer valid or supported.

After the migration, complete the following steps:

Step 1

From Emergency Responder, choose System > National E911 Service Provider VUI Settings .

Step 2

Click Upload Certificate .

Step 3

Use the Browse button to locate the new .bcfks certificate file, highlight the file, and click the Upload button, and complete any additional configurations required for the National E911 Service Provider.

##### Configure Off-premises Settings

To configure Off-premises settings, perform the following steps on the Cisco Unified Communications Manager Administration
                                       user interface.

Step 1

In Cisco Unified Communications Manager Administration, use the System > Enterprise Parameters Configuration.

Step 2

If the Hostname (FQDN) Verification Policy is set to Always verify Hostname (FQDN) or Verify Hostname (FQDN) if possible , then perform the following steps:

Delete the Emergency Responder source node Tomcat certificate.

Add the Emergency Responder destination node Tomcat certificate as Tomcat-trust on Unified CM.

Update the IP Address and End User URL in the Application Server Configuration ( System > Application Server ) with the destination node details.

Restart the Cisco E911 service and Cisco Tomcat service on Unified CM.

Step 3

If the Hostname (FQDN) Verification Policy is set to Do not verify Hostname (FQDN) , then perform the following steps:

Update the IP Address and End User URL in the Application Server Configuration ( System > Application Server ) with the destination node details.

Restart the Cisco E911 service and Cisco Tomcat service on Unified CM.

##### Update Unified CM Node on Emergency Responder After Unified CM Network Migration

After completing the network migration, perform the following steps to update the Unified Communications Manager and SNMPv2
                                       Settings configuration on Emergency Responder:

Step 1

Select Phone Tracking > Cisco Unified Communications Manager details.

Step 2

Select the Unified CM server and click the Delete icon to delete the server.

Step 3

Click Add New to add the new IP address of the Unified CM server to the Emergency Responder after a Network Migration.

Step 4

Navigate to Phone Tracking > SNMPv2 Settings .

Step 5

Click Delete to delete the existing SNMPv2 configuration for the source Unified Communications Manager node from Emergency Responder.

Step 6

Click Add New to add the new SNMPv2 configuration for the destination Unified Communications Manager node to Emergency Responder.

Step 7

Verify that the CTI Route Points and CTI Ports register to the destination Unified Communications Manager node after the new
                                                Unified CM and SNMPv2 Settings are added.

## Postinstallation Tasks

### Postinstall Tasks for VMware vSphere ESXi, Cisco NFVIS-for-UC, and Nutanix AHV

Step 1

Read the Release Notes and any Readme files that come with your release.

You can download the Release Notes from the below URL. Make sure that you understand the features for your release and any
                                             COP file requirements.

https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/products-release-notes-list.html

Step 2

Configure Software Location on cluster nodes that will be used for future upgrades and COP Installs.

Before you attempt to upgrade any cluster nodes or install any COP files on the cluster nodes, all cluster nodes need to have
                                             their Software Location fields configured.

Step 3

Install Licenses

Verify that you have the required licenses for your system and devices.

Step 4

Configure the Backup

We recommend performing regular backups. You can set up automatic backups or invoke a backup at any time.

Step 5

Change Virtual Machine Configuration Specifications

To change to the Guest OS version in the Emergency Responder virtual machine (VM) settings.

This step is not applicable for Cisco NFVIS-for-UC and Nutanix AHV.

#### Install Licenses

Make sure that you acquire the necessary licenses.

See the Cisco Smart Software Licensing for more information.

#### Configure the Backup

We recommend performing regular backups. You can use the Disaster Recovery System (DRS) to do a full data backup for all servers
                                    in a cluster. You can set up automatic backups or invoke a backup at any time.

You can initiate a manual backup or configure a backup schedule. For more details, see the 'Backup and Restore Procedures'
                                    section in the "Configure Cisco Emergency Responder Disaster Recovery System" chapter.

#### Change Virtual Machine Configuration Specifications

Use the following procedure to change to the Guest OS version in the Emergency Responder virtual machine (VM) settings.

Step 1

Shut down the virtual machine.

Step 2

Change the configuration of the virtual machine as needed through vSphere. You can update the Guest OS and VM Hardware Compatibility

Update VM Hardware Compatibility—Left click Virtual Machine. Check for Updates . Click Update

If you are not aware of the host, click Check status and click Upgrade to match host.

Update Guest OS—Right click the Virtual Machine > Edit Settings > Virtual Machine Option > General Option > Guest OS Version .

Step 3

Power on the Virtual Machine.

The following warning message appears in ESXi when you open the virtual machine settings while the machine is running and
                                                there is a mismatch.

Warning

The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                            running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations.

## Cisco Emergency Responder Upgrade

To upgrade Cisco Emergency Responder to the most recent version, use the Cisco Unified OS Administration web interface or
                           Command Line Interface (CLI). See Software Upgrades section for information about performing upgrades.

Perform the Emergency Responder upgrade tasks in the order shown in this table.

Installation Task

For More Information

Upgrade Emergency Responder

Software Upgrades

Upgrade Unified CM

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

Change Cisco Unified Communications Manager Version

Update Unified CM Version

Update Cisco Unified Communications Manager Version

See "Performing Software Upgrades" section of the respective Cisco Emergency Responder Administration Guide for Emergency Responder for information about performing upgrades to Emergency Responder.

| Installation Method | Description |
|---|---|
| Attended Install | Note This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. A baseline-typical installation of one node of Emergency Responder . To install an Emergency Responder cluster using this method, follow the Installation on a New System steps in this sequence: Emergency Responder publisher node Emergency Responder subscriber node You can use this method with any of the following software media options: Physical install DVD. Bootable installer image for base release in ISO format (obtained from either Cisco Commerce Workspace, Cisco License Central,
                                                   or a Cisco Business Edition appliance factory preload). This file applies for all the 3 hypervisors. (Applicable only to VMware vSphere ESXi and Cisco NFVIS for UC) Base OVA containing all supported virtual machine configurations. (Applicable only to Nutanix AHV) A set of base OVAs, each containing a supported virtual machine configuration. (Applicable only to VMware vSphere ESXi) Partial skip-installed OVA. This OVA format file contains a partially installed application
                                                   up to the "skip" Install Wizard point where the application is ready to accept an Answer File and complete installation. OVA
                                                   format file is obtained either from Cisco License Central or from a Cisco Business Edition appliance factory preload. Note Use this method when manual installation without automation is acceptable, such as labs or small deployments. | Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. | Note | Use this method when manual installation without automation is acceptable, such as labs or small deployments. |
| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Note | Use this method when manual installation without automation is acceptable, such as labs or small deployments. |
| Touchless Install of a Single Node or a Cluster | Note This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. A partially automated installation of one node or installation of an Emergency Responder cluster. Use this method to get basic automation for one node, where you can fill out all the information initially, start the Install
                                             Wizard with that information, and complete the rest of the installation automatically using the Answer File. For clusterwide installations, use this method to generate pre-created Answer Files, that occurs in one seamless process with
                                             minimal intervention. To install a single node or a cluster using this method, follow the Touchless Installation steps for the hypervisor selected: Create an Answer File for each node in the cluster using the Unified Communications Answer File Generator. Place all those Answer Files in well-known locations. See Generate Answer Files for Touchless Install . Power on the node or all the cluster nodes simultaneously. In this method, no interaction with the native Install Wizard is required. The nodes will communicate with each other and
                                             each node will read its Answer File for instructions. You can use this method with any of the software media options available for Attended Install. Use this method to: Get more automation—Unattended Install of the entire cluster + zero interaction with the native Install Wizard. Faster installation—Cluster nodes undergo installation in parallel. This is especially useful if you have a large cluster
                                                   with many nodes to install. | Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Fresh Install with Data Import | Note This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. To directly migrate a cluster, follow the Install with Data Import tasks: On each cluster node, export your old version's data. For each cluster node, provision a new virtual machine for your new version and follow either Attended Install or Touchless
                                                   Install for a single node or the cluster node(s) of interest. Using the Data Import options available in Install Wizard and/or
                                                   the Unified Communications Answer File Generator. You can use this method with any of the software media options available for Attended Install. Use this method for "native" direct migrations. You can have more granular control over individual nodes migration timing
                                             and sequencing. You may also use this method to avoid the use of application readdress and temporary extra hardware footprint
                                             for direct migration. | Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |

| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
|---|---|

| Note | Use this method when manual installation without automation is acceptable, such as labs or small deployments. |
|---|---|

| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
|---|---|

| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
|---|---|

|  | Compatible Hypervisor Major/Minor Releases with Minimum Maintenance/Patch Release |
|---|---|
| Emergency Responder | VMware vSphere ESXi | Cisco NFVIS-for-UC | Nutanix AHV |
| Release 15SU4 | 8.0 U1 7.0 U3 | 4.18.2a | AHV 10.0 + AOS 7.0/PC 2024.3 |
| Releases 15 FCS through 15SU3 | 8.0 U1 7.0 U3 | Not supported | Not supported |

| Component and Capacity Point | vCPU | Physical CPU Required Minimum Base Frequency | vRAM | vDisk | vNIC |
|---|---|---|---|---|---|
| 20,000 users | 2 | 2.00 GHz for <12K users 2.50 GHz for <20K users | 6 GB | 1 x 80 GB | 1 |
| 30,000 users | 2 | 2.50 GHz | 6 GB | 1 x 110 GB | 1 |
| 40,000 users | 4 | 2.50 GHz | 6 GB | 1 x 110 GB | 1 |

| Note | We recommend that you perform the installation or upgrade during off-peak hours. The installation or upgrade procedure completely
                                             reformats the hard disk, so Emergency Responder is unavailable duration the installation or upgrade. |
|---|---|

| Note | Emergency Responder supports interoperability between two server groups in a cluster running different versions of Emergency
                                                      Responder. |
|---|---|

| Note | The
                                                         					 Emergency Responder administrative users password must be at least six
                                                         					 characters long and can contain alphanumeric characters, hyphens, and
                                                         					 underscores. It must start with an alphanumeric character. |
|---|---|

| Note | To avoid upgrade failures due to time sync issues with VM, disable the VM's NTP sync with the ESXi host using the workaround
                                             mentioned in the following link: https://knowledge.broadcom.com/external/article?legacyId=1189 . |
|---|---|

| Installation Task | For
                                             				More Information |
|---|---|
| Install Cisco Unified Communications Manager | https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html |
| Install Emergency Responder as a new installation | Installation on a New System |

| Note | Because some of the fields are optional, they may not apply to your configuration. For example, if you decide not to set up
                                                an SMTP host during installation, the parameter still displays, but you do not need to enter a value. |
|---|---|

| Configuration Data | Description | Editable after Installation |
|---|---|---|
| Administrator Credentials |
| Administrator Login | Specifies the name that you want to assign to the Administrator account. | No After installation, you can create additional administrator accounts, but you cannot change the original administrator account
                                                user ID. |
| Administrator Password | Specifies the password for the Administrator account. | Yes CLI: set password user admin |
| Application User Credentials |
| Application User Username | Specifies the user ID for applications installed on the system. | Yes CLI: utils reset_application_ui_administrator_name |
| Application User Password | Specifies the password for applications on the system. | Yes CLI: utils reset_application_ui_administrator_password |
| Security Password |
| Security password for Emergency Responder | Servers in the cluster use the security password to communicate with one another. Set this password on the Emergency Responder
                                                publisher node, and enter it when you install each additional node in the cluster. | Yes. You can change the security password on all nodes in the cluster using the following command: CLI: set password user security |
| Certificate Information |
| Organization | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality] [state] [country] |
| Unit | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality] [state] [country] |
| Location | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality] [state] [country] |
| State | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality] [state] [country] |
| Country | Used to create the Certificate Signing Request. | Yes CLI: set web-security [orgunit] [orgname] [locality] [state] [country] |
| (Optional) SMTP |
| SMTP Location | Specifies the name of the SMTP host that is used for outbound email. You must fill in this field if you plan to use electronic notification. If not, you can leave it blank. | Yes In Cisco Unified Operating System Administration Web Interface, select Settings > SMTP and enter the IP address or Hostname in the IP Address/Host Name field. CLI: set smtp [host] |
| CER Emergency Number |
| Emergency Number | Specifies the primary emergency number that is dial-able and is handled by Emergency Responder. All characters must either be numeric, a '*' or a '#'. | Yes |
| CER End User Language |
| End User Language | Specifies the language the user wants to use for Emergency Responder. | Yes |
| CER CCM Version |
| CCM Version | Indicates the version of Emergency Responder CCM. | Yes |
| Network Information |
| DHCP (Dynamic Host Configuration Protocol) | Check the check box if you want to use DHCP to automatically configure the network settings on your server. Also, enter the
                                                hostname. If you uncheck the option, you must enter a hostname, IP Address, IP Mask, and Gateway Address. | Yes. In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet . CLI: set network dhcp eth0 [enable] CLI: set network dhcp eth0 disable [node_ip] [net_mask] [gateway_ip] |
| Hostname | If DHCP is enabled, you must enter a hostname for this machine. | Yes; for Emergency Responder nodes, choose one of the following: In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet . CLI: set network hostname You will be prompted to enter the parameters. |
| IP Address | If DHCP is disabled, you must enter the IP address of this machine. | Yes; for Emergency Responder nodes, choose one of the following: In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet . CLI: set network IP eth0 [ip-address] [ip-mask] |
| IP Mask | If DHCP is disabled, you must enter the IP subnet mask of this machine. The subnet mask together with the IP address defines
                                                the network address and the host address. The subnet mask must use the following format: 255.255.255.0 | Yes In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet . CLI: set network IP eth0 [ip-address] [ip-mask] |
| Gateway Address | If DHCP is disabled, you must enter the gateway address. | Yes In Cisco Unified Operating System Administration Web Interface, select Settings > IP > Ethernet . CLI: set network gateway [addr] |
| (Optional) DNS |
| Primary DNS | If you have a Domain Name Server (DNS), Emergency Responder contacts this DNS server first when attempting to resolve hostnames. | Yes CLI: set network dns primary [address] |
| Secondary DNS (optional) | When a primary DNS server fails, Emergency Responder will attempt to connect to the secondary DNS server. | Yes CLI: set network dns secondary [address] |
| Domain | Represents the name of the domain in which this machine is located | Yes CLI: set network domain [name] |
| Time Zone |
| Region | Allows you to select a region for your time zone. | Yes |
| Time Zone | Reflects the local time zone and offset from Greenwich Mean Time (GMT). Select the time zone that most closely matches the
                                                location of your machine. | Yes CLI: set timezone [zone] |
| Network Time Protocol |
| NTP Server IP Address | During installation of the Emergency Responder publisher node, you must specify the IP address of an external Network Time
                                                Protocol (NTP) server. We recommend that you use the Emergency Responder publisher node as the NTP server. | Yes In Cisco Unified Operating System Administration Web Interface, select Settings > NTP Servers . |
| (Optional) List of Secondary Nodes | This list identifies the secondary nodes (subscribers) in the cluster by host name. | Yes |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Planning the Installation | Make sure to review the following: Decide on your installation method. Decide on your cluster topology. |
| Step 2 | Required Installation Information | Review the installation requirements and record the configurations settings for each server that you plan to install. |
| Step 3 | Create virtual machines. | Get base OVA. An example OVA file name is: cer_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova . Run Collab Sizing Tool to get the required virtual machine count and specs of each virtual machine. If you don't want to run
                                                   Collab Sizing Tool, follow the guidance in the OVA readme and the OVA wizard to select a predefined starting point, which
                                                   can be changed later if needed. |
| Step 4 | Mount the installation ISO file. | Place the installation ISO file in a location where the virtual machine can access it and edit the virtual machine's DVD drive
                                             to map to the file. Select the option to mount the DVD drive when you power on the virtual machine. When you power on the virtual machine, it mounts the ISO file and start the installation process. Do not begin the installation
                                             process until you have completed all the steps in this procedure. |
| Step 5 | Verify the NTP status on the publisher node. | If the publisher node fails to synchronize with an NTP server, subscriber node installation can fail. On the Emergency Responder
                                             publisher node, run the utils ntp status CLI command. |
| Step 6 | Complete the following firewall updates: If a firewall is in the routing path between nodes, disable the firewall. Increase the firewall timeout settings until after you complete the installation. | Temporarily allowing network traffic in and out of the nodes (for example, setting the firewall rule for these nodes to IP
                                             any/any) does not always suffice. The firewall might still close necessary network sessions between nodes due to timeouts. |
| Step 7 | If you use DNS, verify that all servers on which you plan to install Emergency Responder are properly registered in DNS. |  |
| Step 8 | Cisco Smart Software Licensing | Make sure that your system has adequate licensing. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Plan the installation | Pick an installation method supported by Hypervisor. |
| Step 2 | Required Installation Information | Review the installation requirements and record the configuration settings for each server that you plan to install. |
| Step 3 | Upload the OVA and ISO image. | Upload the OVA as a profile and the ISO as an image together. This process creates a separate profile for each VM configuration
                                             and a single image for the bootable ISO. For more information, refer to the 'Image Registration for CUCM Applications' section
                                             in the Cisco Enterprise Network Function Virtualization Infrastructure Software Configuration Guide . An example OVA file name is: cer_15_all_esxi_vmv17_or_nfvis_v1.0.sha512.ova . |
| Step 4 | Deploy a VM. | Ensure that an OVA and ISO image is already uploaded. Navigate to Configuration > Deploy . Select OTHER as the option when creating virtual machines for your application type. Connect to the virtual network and assign the Image/Profile (depending on the deployment size that you prefer), and click Deploy . Open the VM console via Configuration > Virtual Machine > Manage . Use the console to complete the ISO installation process. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Plan the installation | Pick an installation method supported by Hypervisor. |
| Step 2 | Required Installation Information | Review the installation requirements and record the configuration settings for each server that you plan to install. |
| Step 3 | Create virtual machines in Nutanix AHV and select an OVA per each VM configuration from the Base OVA and deploy using the
                                          OVA. | Download the CER.ova files based on the required configuration from the Software Download page. An example OVA file name for
                                                   a small size deployment is: cer_15_20kusers_ahv_v1.0.sha512.ova . Upload the CER.ova files (downloaded) onto the Nutanix cluster using Prism Central. Download the desired Emergency Responder bootable .iso image version from the Software Download page and upload the image
                                                   to the Nutanix cluster. Creating Emergency Responder Publisher and Subscriber VMs using the .ova files. Update Emergency Responder VMs to mount CD-ROM with the Emergency Responder image. |

| Step 1 | Download the appropriate .ova files from the Software Download page according to the required Emergency Responder configuration. You can choose Small, Medium, or Large depending up on your preference. For example, cer_15_small_ahv_v1.0.sha512.ova, cer_15_medium_ahv_v1.0.sha512.ova,
                                                cer_15_large_ahv_v1.0.sha512.ova. |
|---|---|
| Step 2 | Log in to Nutanix Prism Central with your credentials. |
| Step 3 | Select Infrastructure from the drop-down menu. |
| Step 4 | Under Compute, Navigate to OVAs from the left pane, and click Upload OVA . |
| Step 5 | Specify a name for the OVA file, and choose the downloaded OVS file by clicking Select File . |
| Step 6 | Click Upload to start the file upload automatically. |
| Step 7 | Verify that the .ova file uploads successfully, indicated by a green progress bar and a Done status. |
| Step 8 | Verify the file upload success from the OVAs page in Prism Central. |

| Step 1 | Download the desired version of the CER bootable .iso image from the Software Download page to your local machine. |
|---|---|
| Step 2 | Log in to Nutanix Prism Central or Prism Element with your credentials. |
| Step 3 | In the top-right corner of the Nutanix Prism Central page, click the three-line menu icon. |
| Step 4 | Click Images in the left pane, then select Add Image . |
| Step 5 | On the Add Images page, you can either choose the Image File and click + Add File to select the locally downloaded file to upload to the Nutanix cluster, or select the URL radio button to upload the bootable .iso image from a remote server by providing the NFS path in the Image URL field. |
| Step 6 | Click + Add URL and provide the authentication credentials to connect to the remote server. |
| Step 7 | Click Next and save the changes. |
| Step 8 | Check the status of the image upload on the Tasks page to confirm the successful upload of the .iso image to the Nutanix cluster. For example, a URL is the following: nfs://<Host IP>/<path>/Bootable_UCSInstall_CER_15.0.1.xxxxx-xx.sha512.iso . |

| Task Flow | Description |
|---|---|
| Installation on a New System | Use this method for basic install of Emergency Responder. |
| Touchless Installation Task Flow for ESXi | Use this task flow to install an Emergency Responder cluster dynamically without the need for manual intervention. |
| Install with Data Import | Complete this task to install an Emergency Responder cluster using the Install with Data Import . |

| Task Flow | Description |
|---|---|
| Installation on a New System | Use this method for basic install of Emergency Responder. |
| Touchless Installation Task Flow for Cisco NFVIS-for-UC | Use this task flow to install an Emergency Responder cluster dynamically without the need for manual intervention. |
| Install with Data Import | Complete this task to install an Emergency Responder cluster using the Install with Data Import . |

| Task Flow | Description |
|---|---|
| Installation on a New System | Use this method for basic install of Emergency Responder. |
| Touchless Installation Task Flow for Nutanix AHV | Use this task flow to install an Emergency Responder cluster dynamically without the need for manual intervention. |
| Install with Data Import | Complete this task to install an Emergency Responder cluster using the Install with Data Import . |

| Note | From Release 15SU2 onwards, if you need to perform manual or scheduled DRS backups or if you want to change the server hostname,
                                          it is not required to manually exchange any tomcat certificate between the publisher and subscriber nodes. The publisher certificate
                                          gets synched to the subscriber node automatically. |
|---|---|

| Step 1 | Insert the Emergency Responder Installation DVD. If the system finds the DVD, you are asked if you want to perform a media check before installation to determine if there
                                                are problems with the DVD. The system displays the checksum of the DVD and instructs you to verify this checksum on the Emergency
                                                Responder website. At the bottom of the screen you will see instructions for moving between elements and for selecting elements, as follows: Use the Tab key to advance to the next element. Use the Alt-Tab key combination to return to the previous element. Use the Space bar to select a highlighted element. If you choose to perform the media check, the system performs the media check and displays the results. If the result of the media check is PASS , click OK . The system install begins the installation. Skip to Step 2. If the result of the media check is FAIL , obtain a new installation DVD from Cisco Systems. |
|---|---|
| Step 2 | The Cisco Emergency Responder system installer starts. The Product Deployment Selection screen displays a message saying the
                                             Cisco Emergency Responder product suite is installing. Click OK to continue. |
| Step 3 | The Proceed with Install page displays the current software version on the hard drive and the software version on the installation
                                             DVD. If you are performing a fresh installation, there will be no software on the hard drive and the system asks if you want to
                                                proceed with the installation. Click Yes to proceed. If you are performing an upgrade, the system displays the current software version and asks it you want to overwrite the hard
                                                drive. Click Yes to proceed. If you click Yes , the system continues with the installation and the Platform Configuration Wizard appears. If you click No , the installation is terminated. |
| Step 4 | On the Platform Configuration Wizard page, click Proceed to continue with the platform installation. To continue with Install with Data Import , choose Import . Use this installation method for direct migrations (Fresh Install with Data Import) from the older versions of Emergency
                                                      Responder. If you click Skip , the system installs both the platform and Emergency Responder software without prompting you to provide information during
                                                      the installation. After the installation is completed and the system reboots, you are prompted to enter the required configuration
                                                      details. |
| Step 5 | Click Continue to proceed. The Timezone Configuration page appears. |
| Step 6 | Choose the correct time zone to use from the list provided. Use the following keys to move between elements on the Timezone Configuration page: Arrow Up or Arrow Down to select a time zone from the list After selecting the correct time zone, click OK . The Auto Negotiation Configuration page appears. |
| Step 7 | Click Yes to enable autonegotiation of the Ethernet NIC speed and duplex mode. The DHCP Configuration page appears. If you click Yes , skip to Step 10. If you click No , the NIC Speed and Duplex Configuration page appears. |
| Step 8 | On the NIC Speed and Duplex Configuration page, do the following: Select the NIC Speed. The available options are 10 Megabit, 100 Megabit, or 1000 Megabit. Select the NIC Duplex setting. The available options are Full or Half. Click OK . The DHCP Configuration page appears. |
| Step 9 | On the MTU Configuration page, you can set the maximum transmission unit (MTU) that can be sent in a network as follows: Click Yes if you want to configure a a MTU value of less than 1500 bytes. Click No to use the default MTU value of 1500 bytes. |
| Step 10 | If you chose not to use DHCP, enter the following information about the Static Network Configuration page: Host Name IP Address IP Mask Gateway (GW) Address Click OK . The DNS Client Configuration page appears. |
| Step 11 | On the DNS Client Configuration page, you are asked if you want to configure the Domain Name System (DNS) client. Note Click the Help button for details about configuring DNS. If you select Yes , a second DNS Client Configuration page appears. If you select No , the Administration Login Configuration page appears. Skip to Step 14. | Note | Click the Help button for details about configuring DNS. |
| Note | Click the Help button for details about configuring DNS. |
| Step 12 | On the second DNS Client Configuration page, you are prompted to enter the following information: Primary Secondary DNS (optional) Domain Click OK . The Administration Login Configuration page appears. |
| Step 13 | On the Administration Login Configuration page, enter an ID and password for the Administrator account. This password is used
                                             to access the CLI and the CiscoUnifiedOS Administration and Disaster Recovery System (DRS) websites. Click Help to display guidelines for creating this password. When you have finished, click OK . The Certificate Information page appears. |
| Step 14 | Enter the following information about the Certificate Information page: Organization Unit Location State Country (select from the scroll-down menu). Click OK . The Publisher Configuration page appears. |
| Step 15 | Based on the type of installation you are performing, do one of the following: If the server you are configuring is the Publisher in the server group, click Yes . The Network Time Protocol Client Configuration page appears. Proceed to Step 17. If the server you are installing is not the Publisher in the server group, you must first configure this server on the Publisher
                                                before you can proceed. This server must also have network access to the Publisher, which must be in service for the installation
                                                to complete successfully. Click No only if you are configuring the Subscriber. See Install Emergency Responder Subscriber for information about installing the Subscriber. |
| Step 16 | On the Network Time Protocol Client Configuration page, you are asked if you want to set up external Network Time Protocol
                                             (NTP) servers. Note We strongly recommend that you use external NTP servers to ensure that the system time is kept accurate. Caution For Emergency Responder install on UCS servers, it is mandatory to configure NTP server. If you click Yes , the system displays a second Network Time Protocol Client Configuration page. In the fields provided, enter the IP address
                                                or hostname of the external NTP servers, then click OK . The Database Access Security Configuration page appears. Skip to Step 18. If you click No , the Hardware Clock Configuration page appears. Enter the following information: Year [yyyy] Month [mm] Day [dd] Hour [hh] Minute [mm] Second [ss] When you finish entering this information, click OK . The Database Access Security Configuration page appears. | Note | We strongly recommend that you use external NTP servers to ensure that the system time is kept accurate. | Caution | For Emergency Responder install on UCS servers, it is mandatory to configure NTP server. |
| Note | We strongly recommend that you use external NTP servers to ensure that the system time is kept accurate. |
| Caution | For Emergency Responder install on UCS servers, it is mandatory to configure NTP server. |
| Step 17 | On the Database Access Security Configuration page, enter the security password and then confirm the password in the fields
                                             provided. Note The security password must be at least six characters long and can contain alphanumeric characters, hyphens, and underscores.
                                                            It must start with an alphanumeric character. The security password is used for secure communications between Emergency Responder
                                                            server groups when performing the installation or upgrade, DRS backup or restore, and "Point to a new Publisher" operations. Click Help to display guidelines. When you finish, click OK . The SMTP Host Configuration page appears. | Note | The security password must be at least six characters long and can contain alphanumeric characters, hyphens, and underscores.
                                                            It must start with an alphanumeric character. The security password is used for secure communications between Emergency Responder
                                                            server groups when performing the installation or upgrade, DRS backup or restore, and "Point to a new Publisher" operations. |
| Note | The security password must be at least six characters long and can contain alphanumeric characters, hyphens, and underscores.
                                                            It must start with an alphanumeric character. The security password is used for secure communications between Emergency Responder
                                                            server groups when performing the installation or upgrade, DRS backup or restore, and "Point to a new Publisher" operations. |
| Step 18 | You are asked if you want to configure a Simple Mail Transport Protocol (SMTP) host. This step is optional. If you click Yes , a second SMTP Host Configuration page appears. Click Help for guidelines, then enter the SMTP hostname or IP address in the field provided. When you are finished, click OK . The Platform Configuration Confirmation page appears. If you click No , the Platform Configuration Confirmation page appears. |
| Step 19 | On the Platform Configuration Confirmation page, do one of the following: Select OK to save the platform configuration information and continue with the installation. The Cisco Emergency Responder Configuration
                                                page appears. Note After you select OK , you cannot modify the platform configuration information. Select Back if you want to return to the previous page to make modifications. Continue to select Back to scroll through each platform configuration page. Select Cancel to cancel the installation. | Note | After you select OK , you cannot modify the platform configuration information. |
| Note | After you select OK , you cannot modify the platform configuration information. |
| Step 20 | On the Security End User Language Selection page, choose a language for the Cisco Emergency Responder web pages. The system
                                             defaults to the English language. The Application User Password Configuration page appears. |
| Step 21 | On the Application User Configuration page, enter the username and password. This username and password is associated with
                                             the default administrative account and is used to log in to the Emergency Responder Administration web page. Click Help for guidelines. When you are finished, click OK . The Cisco Emergency Responder Configuration Confirmation page appears. |
| Step 22 | On the Cisco Emergency Responder Configuration Confirmation page, do one of the following: Select OK to save the Cisco Emergency Responder configuration information and continue with the installation. The system continues
                                                the installation process and then reboots. Caution After you select OK , you cannot modify the Cisco Emergency Responder configuration information. Select Back if you want to return to the previous page to make modifications. Continue to select Back to scroll through each Emergency Responder Application User Configuration page. Select Cancel to cancel the installation. | Caution | After you select OK , you cannot modify the Cisco Emergency Responder configuration information. |
| Caution | After you select OK , you cannot modify the Cisco Emergency Responder configuration information. |
| Step 23 | After the system reboots, it checks the status of various system components. If the system finds any problems, you are prompted
                                             to correct the problem. If the system does not find any problems, the installation process continues. The system ejects the installation DVD, reboot,
                                                and then finishes the installation. When the installation is complete, a CLI prompt appears. Note During this process, the system displays the MAC address of the Publisher. Write down the MAC address when it displays; you
                                                            use the MAC address later to acquire Emergency Responder licenses. If you are not able to capture the MAC address during installation,
                                                            you can look it up later. See the 'Server Licenses' section for information about looking up the server MAC address. | Note | During this process, the system displays the MAC address of the Publisher. Write down the MAC address when it displays; you
                                                            use the MAC address later to acquire Emergency Responder licenses. If you are not able to capture the MAC address during installation,
                                                            you can look it up later. See the 'Server Licenses' section for information about looking up the server MAC address. |
| Note | During this process, the system displays the MAC address of the Publisher. Write down the MAC address when it displays; you
                                                            use the MAC address later to acquire Emergency Responder licenses. If you are not able to capture the MAC address during installation,
                                                            you can look it up later. See the 'Server Licenses' section for information about looking up the server MAC address. |
| Step 24 | To bring up the Emergency Responder websites, go to any Windows system on the network, start a supported web browser, and
                                             enter the following URL: http://your Emergency Responder hostname/ or http://your Emergency Responder IP address/ Note Make sure that the Emergency Responder is configured with DNS so that hostname is resolved to the IP address. | Note | Make sure that the Emergency Responder is configured with DNS so that hostname is resolved to the IP address. |
| Note | Make sure that the Emergency Responder is configured with DNS so that hostname is resolved to the IP address. |

| Note | Click the Help button for details about configuring DNS. |
|---|---|

| Note | We strongly recommend that you use external NTP servers to ensure that the system time is kept accurate. |
|---|---|

| Caution | For Emergency Responder install on UCS servers, it is mandatory to configure NTP server. |
|---|---|

| Note | The security password must be at least six characters long and can contain alphanumeric characters, hyphens, and underscores.
                                                            It must start with an alphanumeric character. The security password is used for secure communications between Emergency Responder
                                                            server groups when performing the installation or upgrade, DRS backup or restore, and "Point to a new Publisher" operations. |
|---|---|

| Note | After you select OK , you cannot modify the platform configuration information. |
|---|---|

| Caution | After you select OK , you cannot modify the Cisco Emergency Responder configuration information. |
|---|---|

| Note | During this process, the system displays the MAC address of the Publisher. Write down the MAC address when it displays; you
                                                            use the MAC address later to acquire Emergency Responder licenses. If you are not able to capture the MAC address during installation,
                                                            you can look it up later. See the 'Server Licenses' section for information about looking up the server MAC address. |
|---|---|

| Note | Make sure that the Emergency Responder is configured with DNS so that hostname is resolved to the IP address. |
|---|---|

| Caution | You must complete
                                                			 the installation of the Publisher, which includes a system reboot, before you
                                                			 start to install the Subscriber. |
|---|---|

| Step 1 | On the Publisher
                                             			 server, add the details about the Subscriber server by doing the following: Log in the Publisher Emergency Responder Administration user interface. Select System > Add Subscriber . Enter the
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
| Step 8 | The Platform Configuration Complete page appears. Select one of the following options: If the Publisher information is correct, click OK . If the information is not correct, click the Back button and make the needed corrections on the Publisher Access Configuration page, then click OK . The installation of the Emergency Responder Subscriber begins and takes an additional 20-30 minutes to complete. |
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

| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
|---|---|

| Note | After publisher installation is complete, and if the subscriber installation does not happen automatically, you must restart
                                          the Cisco Tomcat service using the CLI command utils service restart Cisco Tomcat from the publisher node. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate Answer Files for Touchless Install | Use this procedure to generate the configuration files (clusterconfig.xml and platformconfig.xml) with your network settings.
                                                The touchless install process uses these files to install and configure the various cluster nodes. |
| Step 2 | Generate ISO Images | Use this procedure to create ISO images from the answer files. You will use the ISO image in your touchless installation. |
| Step 3 | Upload ISO Image to Datastore | Use this procedure to upload the ISO image to the datastore. |
| Step 4 | Mount ISO Image to VM | Use this procedure to mount the UC application ISO image on their corresponding VM. |
| Step 5 | Run Touchless Install | Begin the cluster installation. You can kick off all node installations simultaneously. |

| Step 1 | Log in to the Cisco Emergency Responder Answer File Generator application at https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html . |
|---|---|
| Step 2 | In the Hardware section, choose Virtual Machine . |
| Step 3 | From the Product section, select the product and version that you want to install. |
| Step 4 | In the Software Location of Data to Import section, check the Configure Software Location of Data to Import check box to configure Remote SFTP server details only if you choose to install using the Fresh Install with Data Import.
                                                Else ignore this step and proceed to step 5. For more details, see Install with Data Import . By checking the Configure Software Location of Data to Import check box it disables, Administrator Credentials, Security Password, Application User Credentials fields. These details are
                                                   imported from source node data during installation. Enter the following fields: Remote Server Name or IP —The Secure FTP (SFTP) server that stores the source cluster's exported data. Export Data Directory —Directory path of the server containing export data. Remote Server Login ID —Allows data retrieval of the remote SFTP server. Remote Server Password —Can contain alphanumeric characters, hyphens, and underscores. |
| Step 5 | Complete the remaining fields under Clusterwide Configuration with your cluster configuration details. |
| Step 6 | Complete the fields in the Primary Node Configuration with configuration details for the publisher node. |
| Step 7 | Under Secondary Node Configuration , enter the node details for your subscriber node and click Add Secondary Node . |
| Step 8 | Add your subscriber node. |
| Step 9 | Click Generate Answer Files . |
| Step 10 | Download the answer files to your computer. |

| Note | This procedure describes how to use Winimage to create ISO images. |
|---|---|

| Step 1 | From Winimage, choose File > New . |
|---|---|
| Step 2 | From the Standard format, choose 1.44 MB and click OK . |
| Step 3 | Navigate to the Menu Image, choose Inject and select the platformConfig.xml file. |
| Step 4 | When prompted to inject the file into Winimage, click Yes . |
| Step 5 | Choose File > Save As . |
| Step 6 | Save the file as an ISO image (.iso file) using the following naming convention: Emergency Responder—cer.iso . |
| Step 7 | Repeat these steps for the other Emergency Responder server groups in the cluster. |

| Step 1 | Start the vSphere client. |
|---|---|
| Step 2 | Select the Configuration tab. |
| Step 3 | Select Storage . |
| Step 4 | Right-click on a datastore and Browse the datastore. |
| Step 5 | Navigate to the destination directory and click the Upload files to this datastore icon. |
| Step 6 | Upload the ISO images to your local folder. |
| Step 7 | At the Upload/Download warning, click Yes . |
| Step 8 | Close the Datastore Browser window. |

| Step 1 | In the vSphere client, choose the virtual machine. |
|---|---|
| Step 2 | Open VMware Remote Console (VMRC), and click the CD/DVD Drive 2 . |
| Step 3 | Browse to the datastore and locate the ISO image. |
| Step 4 | Select the file and click OK . |
| Step 5 | Under Device Status , enable the Connected and Connect at power on option. |
| Step 6 | Click the Options tab. Under Boot Options , check Force entry to BIOS and click OK . |
| Step 7 | Repeat this procedure for each VM on which you want to install a node. |

| Step 1 | In vSphere client, right-click the VM and select Open Console . A console window opens. |
|---|---|
| Step 2 | Click the Power On icon in the console toolbar to power on the virtual machine. |
| Step 3 | When the BIOS screen appears, configure the following boot order: CD-ROM Hard Drive Removable Devices Network |
| Step 4 | Save the settings and exit from the console. The installation commences immediately. |
| Step 5 | Repeat these steps for each cluster node. All cluster nodes may install in parallel; you do not have to install them serially. |
| Step 6 | After to emphasize the completion of an activity, remove the ISO configurations from the virtual machines. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate Answer Files for Touchless Install | Use this procedure to generate the configuration files (clusterconfig.xml and platformconfig.xml) with your network settings.
                                                The touchless install process uses these files to install and configure the various cluster nodes. |
| Step 2 | Generate ISO Images | Use this procedure to create ISO images from the answer files. You use this ISO image in your touchless installation. |
| Step 3 | Upload ISO Image to Datastore | Use this procedure to upload the ISO image to the datastore. |
| Step 4 | Deploy VM via NFVIS Portal | Use this procedure to deploy the VM. After deployment, the installation starts automatically. |

| Step 1 | Log in to the Cisco Emergency Responder Answer File Generator application at https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html . |
|---|---|
| Step 2 | In the Hardware section, choose Virtual Machine . |
| Step 3 | From the Product section, select the product and version that you want to install. |
| Step 4 | In the Software Location of Data to Import section, check the Configure Software Location of Data to Import check box to configure Remote SFTP server details only if you choose to install using the Fresh Install with Data Import.
                                                Else ignore this step and proceed to step 5. For more details, see Install with Data Import . By checking the Configure Software Location of Data to Import check box it disables, Administrator Credentials, Security Password, Application User Credentials fields. These details are
                                                   imported from source node data during installation. Enter the following fields: Remote Server Name or IP —The Secure FTP (SFTP) server that stores the source cluster's exported data. Export Data Directory —Directory path of the server containing export data. Remote Server Login ID —Allows data retrieval of the remote SFTP server. Remote Server Password —Can contain alphanumeric characters, hyphens, and underscores. |
| Step 5 | Complete the remaining fields under Clusterwide Configuration with your cluster configuration details. |
| Step 6 | Complete the fields in the Primary Node Configuration with configuration details for the publisher node. |
| Step 7 | Under Secondary Node Configuration , enter the node details for your subscriber node and click Add Secondary Node . |
| Step 8 | Add your subscriber node. |
| Step 9 | Click Generate Answer Files . |
| Step 10 | Download the answer files to your computer. |

| Note | This procedure describes how to use AnyBurn Tool to create ISO images. You can download any free version from https://www.anyburn.com/download.php . |
|---|---|

| Note | NFVIS does not support ISO images created with the WinImage tool because WinImage does not generate ISO files in the true
                                                   ISO 9660 format required by NFVIS. |
|---|---|

| Step 1 | Open any AnyBurn tool. |
|---|---|
| Step 2 | From the options, select Create image file from files/folders . |
| Step 3 | Click Add and include all the files that you want to include in the ISO. |
| Step 4 | To create a destination and image name, select the path where you want to save the new ISO file and enter the required file
                                                name. |
| Step 5 | Click Create Now to generate the ISO file. |

| Step 1 | Use this method when the ISO and OVA files are available on your local computer. To upload an image using the local registration
                                                method, perform the following: Navigate to Configuration > Virtual Machine > Images > Image Repository . To upload the ISO image, click Upload and select the ISO file from your local file system. For example: Bootable_UCSInstall_CER_15.0.1.xxxxx-xx.sha512.iso . To configure the Image Properties, enter a pre-populated name in the Image Name to a descriptive name. For example, cer-15.0.1 . Also, select a VM Type from the drop-down list. If your application type is not listed, select OTHER . To upload an OVA Metadata, select the Metadata checkbox, click Upload OVA , and select the OVA file. For example, cer_15_30kusers_ahv_v1.0.sha512.ova . To configure additional options, select the Dedicated Cores check box (recommended for production environments). This allocates dedicated CPU cores to the VM for improved performance. To submit the registration, click the Upload File button. NFVIS performs the following: Upload the ISO image Upload and parse the OVA file Register the image Automatically create profiles/flavors from OVA metadata To verify registration, wait for the process to complete. The image should appear in the Image Repository with the status Active . Verify that flavors are populated from the OVA file. |
|---|---|
| Step 2 | Use this method when files are hosted on a remote server (HTTP, HTTPS, FTP, or SCP). To upload an image using the remote registration
                                                method, perform the following: Navigate to Configuration > Virtual Machine > Images > Image Repository . To select the Remote Registration, click Register Image and select Remote Image Registration option. To configure the Image Details, enter a descriptive name in the Image Name field. For example, cer-15.0.1 . To configure the Remote Server Connection Protocol, enter the following details: Protocol : Select from the drop-down list (HTTP/HTTPS/FTP/SCP). IP Address : Enter the server hostname or IP address. Image File Path : Enter the directory path to the ISO file with the image name. For example: Bootable_UCSInstall_CER_15.0.1.xxxxx-xx.sha512.iso Enter the Configure Authentication details for FTP/SCP (only). Username : Enter the username for the remote server. Password : Enter the password. To upload an OVA Metadata, select the Metadata checkbox, and enter the OVA File Path name. For example, cer_15_30kusers_ahv_v1.0.sha512.ova . Note The OVA file must be on the same server as the ISO file. Different remote servers for the ISO and OVA files are not supported. To configure additional options, select the Dedicated Cores check box if necessary. To submit the registration, click the Submit button. NFVIS performs the following: Download the ISO image from the remote server Upload and parse the OVA file Register the image Automatically create profiles/flavors from OVA metadata To verify registration, wait for the process to complete. The image should appear in the Image Repository with the status Active . Verify that flavors are populated from the OVA file. Note Downloading large files may take several minutes. | Note | The OVA file must be on the same server as the ISO file. Different remote servers for the ISO and OVA files are not supported. | Note | Downloading large files may take several minutes. |
| Note | The OVA file must be on the same server as the ISO file. Different remote servers for the ISO and OVA files are not supported. |
| Note | Downloading large files may take several minutes. |

| Note | The OVA file must be on the same server as the ISO file. Different remote servers for the ISO and OVA files are not supported. |
|---|---|

| Note | Downloading large files may take several minutes. |
|---|---|

| Step 1 | Navigate to Configuration > Deploy to deploy a new virtual machine. |
|---|---|
| Step 2 | Select an option from the VM. If your application type is not listed, select OTHER . If necessary, you can change the name of the VM Type created. |
| Step 3 | Choose the required image from the drop-down list. Images are populated based on the VM type selected. For example, cer-15.0.1 . |
| Step 4 | Select the appropriate flavor (with the image name) based on your sizing requirements. Flavors are populated based on the selected image and are automatically created from the OVA file during image registration. |
| Step 5 | (Optional) Enter the Group Name, VNC Password, Deployment Disk, and Low Latency (TRUE). |
| Step 6 | To configure Network Connections, perform the following in the Network Design section: Locate the VM icon on the canvas. Drag a line from the VM to the desired network. Connect to the appropriate network(s) for your deployment. Enter the directory path to the ISO file. Add additional networks as required. |
| Step 7 | To attach the bootstrap ISO, select the Bootstrap ISO check box, click Upload , and select your Day 0 configuration ISO. |
| Step 8 | To deploy the VM, click the Deploy button. The system will validate the configuration. If validation errors occur, they will be displayed for correction. |
| Step 9 | Navigate to Configuration > Virtual Machine > Manage to monitor the deployment. |
| Step 10 | To access the VM console, once the VM is in ACTIVE state, click the Terminal button in the VM row. Monitor the installation progress via the console. Follow the application-specific installation prompts. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate Answer Files for Touchless Install | Use this procedure to generate the configuration files (clusterconfig.xml and platformconfig.xml) with your network settings.
                                                The touchless install process uses these files to install and configure a single node or the various cluster nodes. |
| Step 2 | Generate ISO Images | Use this procedure to create ISO images from the answer files. You use this ISO image in your touchless installation. |
| Step 3 | Upload ISO Image to Datastore | Use this procedure to upload the ISO images to the datastore. |
| Step 4 | Power On the Virtual Machine | You can kick off all node installations simultaneously. |

| Step 1 | Log in to the Cisco Emergency Responder Answer File Generator application at https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html . |
|---|---|
| Step 2 | In the Hardware section, choose Virtual Machine . |
| Step 3 | From the Product section, select the product and version that you want to install. |
| Step 4 | In the Software Location of Data to Import section, check the Configure Software Location of Data to Import check box to configure Remote SFTP server details only if you choose to install using the Fresh Install with Data Import.
                                                Else ignore this step and proceed to step 5. For more details, see Install with Data Import . By checking the Configure Software Location of Data to Import check box it disables, Administrator Credentials, Security Password, Application User Credentials fields. These details are
                                                   imported from source node data during installation. Enter the following fields: Remote Server Name or IP —The Secure FTP (SFTP) server that stores the source cluster's exported data. Export Data Directory —Directory path of the server containing export data. Remote Server Login ID —Allows data retrieval of the remote SFTP server. Remote Server Password —Can contain alphanumeric characters, hyphens, and underscores. |
| Step 5 | Complete the remaining fields under Clusterwide Configuration with your cluster configuration details. |
| Step 6 | Complete the fields in the Primary Node Configuration with configuration details for the publisher node. |
| Step 7 | Under Secondary Node Configuration , enter the node details for your subscriber node and click Add Secondary Node . |
| Step 8 | Add your subscriber node. |
| Step 9 | Click Generate Answer Files . |
| Step 10 | Download the answer files to your computer. |

| Note | This procedure describes how to use WinImage to create ISO images. You can download WinImage from https://www.winimage.com/download.htm . |
|---|---|

| Step 1 | From WinImage, choose File > New . |
|---|---|
| Step 2 | From the Standard format, choose 1.44 MB and click OK . |
| Step 3 | Navigate to the Menu Image, choose Inject , and select the platformConfig.xml and the clusterConfig.xml file for the Emergency Responder Publisher node. For Emergency Responder Subscriber, choose Inject , and select the platformConfig.xml file only. |
| Step 4 | When prompted to inject the file into WinImage, click Yes . |
| Step 5 | Choose File > Save As . |
| Step 6 | Choose All files from the drop-down for the Save as type and specify the file name as an ISO image (with .iso file extension, for example imagename.iso ) using the following naming convention: Emergency Responder— cer.iso . |
| Step 7 | Repeat these steps for the other Emergency Responder server groups in the cluster. |

| Step 1 | Download the desired version of the Emergency Responder bootable .iso image from the Software Download page to your local
                                                machine. |
|---|---|
| Step 2 | Log in to Nutanix Prism Central or Prism Element with your credentials. |
| Step 3 | In the top-right corner of the Nutanix Prism Central page, click the three-line menu icon. |
| Step 4 | Click Images in the left pane, then select Add Image . |
| Step 5 | On the Add Images page, you can either choose the Image File and click + Add File to select the locally downloaded file to upload to the Nutanix cluster, or select the URL radio button to upload the bootable .iso image from a remote server by providing the NFS path in the Image URL field. |
| Step 6 | Click + Add URL and provide the authentication credentials to connect to the remote server. |
| Step 7 | Click Next and save the changes. |
| Step 8 | Check the status of the image upload on the Tasks page to confirm the successful upload of the .iso image to the Nutanix cluster. For example, a URL is the following: nfs://<Host IP>/<path>/Bootable_UCSInstall_CER_15.0.1.xxxxx-xx.sha512.iso . |

| Note | This installation method is applicable for VMware vSphere ESXi, Nutanix AHV, and Cisco NFVIS-for-UC. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | IPsec Requirements | Note Applicable for both Simple and Network Migrations Before starting the migration, disable the IPsec policy on both the Publisher and Subscriber nodes. | Note | Applicable for both Simple and Network Migrations |
| Note | Applicable for both Simple and Network Migrations |
| Step 2 | Configure SAML SSO | Note Applicable for both Simple and Network Migrations Ensure that FIPS mode is enabled before configuring SSO and starting the migration. | Note | Applicable for both Simple and Network Migrations |
| Note | Applicable for both Simple and Network Migrations |
| Step 3 | CTI Route Points and Ports Re-Registration | Note Applicable only for Simple Migration After registering the source Emergency Responder with Unified Communications Manager in mixed mode, ensure the following before
                                                starting the migration: Use only one application user, or a unique application user that is not assigned to any other Emergency Responder. Use only one set of Certificate Authority Proxy Function (CAPF) profiles. These profiles must not be associated with any other
                                                      server or application user. Note When migrating from Release 12.5(1)SU9 Emergency Responder with Emergency Responder operating in FIPS mode and Unified Communications
                                                            Manager in mixed mode, ensure that you update the CAPF profiles on Unified CM and the CAPF passwords in Emergency Responder
                                                            after the migration. | Note | Applicable only for Simple Migration | Note | When migrating from Release 12.5(1)SU9 Emergency Responder with Emergency Responder operating in FIPS mode and Unified Communications
                                                            Manager in mixed mode, ensure that you update the CAPF profiles on Unified CM and the CAPF passwords in Emergency Responder
                                                            after the migration. |
| Note | Applicable only for Simple Migration |
| Note | When migrating from Release 12.5(1)SU9 Emergency Responder with Emergency Responder operating in FIPS mode and Unified Communications
                                                            Manager in mixed mode, ensure that you update the CAPF profiles on Unified CM and the CAPF passwords in Emergency Responder
                                                            after the migration. |

| Note | Applicable for both Simple and Network Migrations |
|---|---|

| Note | Applicable for both Simple and Network Migrations |
|---|---|

| Note | Applicable only for Simple Migration |
|---|---|

| Note | When migrating from Release 12.5(1)SU9 Emergency Responder with Emergency Responder operating in FIPS mode and Unified Communications
                                                            Manager in mixed mode, ensure that you update the CAPF profiles on Unified CM and the CAPF passwords in Emergency Responder
                                                            after the migration. |
|---|---|

| Step 1 | Verify the signing algorithm by running the CLI command: utils sso show signing-algorithm . |
|---|---|
| Step 2 | If the signing algorithm is SHA-1, change it to SHA-256 using the CLI command: utils sso set signing algo sha256 . |
| Step 3 | Enable SSO and proceed with the migration steps. |

| Important | Fresh Install with Data Import does not support domain name changes. If DNS is enabled on the publisher node of the target
                                                      destination, the domain name must match the source destination. If the domain name must change, install the target destination
                                                      on the publisher without the DNS enabled and then enable DNS via the CLI after the installation is complete. The subscriber
                                                      node can be installed with the DNS enabled, but ensure that the System > Add Subscriber entries on the publisher node are correct before installing the subscriber. If you plan to change the hostname and/or IP address during the migration, the System > Add Subscriber entries must be updated on the publisher node of the target destination prior to installing the subscriber. Fresh Install with Data Import does not support installation with DHCP configuration. If DHCP is enabled on the source destination,
                                                      install the target destination with Static configuration data and then configure the DHCP later post migration. |
|---|---|

| Note | Ensure that the publisher/subscriber nodes are exported to the SFTP server before proceeding with Fresh Install with Data
                                                Import. |
|---|---|

| Step 1 | Export data from the source destination publisher node. Run the utils system upgrade dataexport initiate CLI command on each node of the desired source system to export the data which can be imported using this procedure. Enter the SFTP server information to export the data. Enter the node Hostname and IP Address (it is possible to change them at this stage.) Run the utils system upgrade dataexport status to track the export status. A new folder is created at the SFTP server with the cluster name: Publisher IP Address. |
|---|---|
| Step 2 | Export data from the source destination subscriber node. Run the utils system upgrade dataexport initiate CLI command on each node of the desired source system to export the data which can be imported using this procedure. Enter the SFTP server information to export data. Enter the node Hostname and IP Address (it is possible to change them at this stage). Run the utils system upgrade dataexport status to track the export status. The exported subscriber data is stored in the same cluster folder: Publisher IP Address. |
| Step 3 | Then proceed with one of the following methods to complete installation/import. Note During the configuration of an IP address, if the source and target destinations are using DHCP, ensure that you configure
                                                            a static IP address for the target destination. For example, the current IP address of the source destination. Installation Method See Attended Install Install a new publisher and import the data. To configure Emergency Responder with Install with Data Import follow the instructions as described in Install Emergency Responder Publisher from step 1 through 4. In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Emergency Responder installation. In the import wizard, provide details for the following information: Hostname, IP Address, Subnet mask, and Gateway. This must be the same information provided in the destination node for which
                                                                        you exported the data. SFTP—In the export data directory, enter the exported data folder name or cluster information: <Publisher IP Address>. Confirm whether this is the First Node. Enter one or more NTP servers. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. Install a new Subscriber and import the data. Repeat step 4 except for the First Node question. Respond to this query with
                                                                  a 'No' and provide the new publisher IP Address and hostname information. Note If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. Touchless Install of a Single Node or a Cluster Follow the instructions as described in Touchless Installation Task Flow for ESXi from step 1 through 5. Note If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command. | Note | During the configuration of an IP address, if the source and target destinations are using DHCP, ensure that you configure
                                                            a static IP address for the target destination. For example, the current IP address of the source destination. | Installation Method | See | Attended Install | Install a new publisher and import the data. To configure Emergency Responder with Install with Data Import follow the instructions as described in Install Emergency Responder Publisher from step 1 through 4. In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Emergency Responder installation. In the import wizard, provide details for the following information: Hostname, IP Address, Subnet mask, and Gateway. This must be the same information provided in the destination node for which
                                                                        you exported the data. SFTP—In the export data directory, enter the exported data folder name or cluster information: <Publisher IP Address>. Confirm whether this is the First Node. Enter one or more NTP servers. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. Install a new Subscriber and import the data. Repeat step 4 except for the First Node question. Respond to this query with
                                                                  a 'No' and provide the new publisher IP Address and hostname information. Note If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. | Touchless Install of a Single Node or a Cluster | Follow the instructions as described in Touchless Installation Task Flow for ESXi from step 1 through 5. | Note | If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command. |
| Note | During the configuration of an IP address, if the source and target destinations are using DHCP, ensure that you configure
                                                            a static IP address for the target destination. For example, the current IP address of the source destination. |
| Installation Method | See |
| Attended Install | Install a new publisher and import the data. To configure Emergency Responder with Install with Data Import follow the instructions as described in Install Emergency Responder Publisher from step 1 through 4. In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Emergency Responder installation. In the import wizard, provide details for the following information: Hostname, IP Address, Subnet mask, and Gateway. This must be the same information provided in the destination node for which
                                                                        you exported the data. SFTP—In the export data directory, enter the exported data folder name or cluster information: <Publisher IP Address>. Confirm whether this is the First Node. Enter one or more NTP servers. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. Install a new Subscriber and import the data. Repeat step 4 except for the First Node question. Respond to this query with
                                                                  a 'No' and provide the new publisher IP Address and hostname information. Note If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. |
| Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. |
| Note | If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. |
| Touchless Install of a Single Node or a Cluster | Follow the instructions as described in Touchless Installation Task Flow for ESXi from step 1 through 5. |
| Note | If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command. |

| Note | During the configuration of an IP address, if the source and target destinations are using DHCP, ensure that you configure
                                                            a static IP address for the target destination. For example, the current IP address of the source destination. |
|---|---|

| Installation Method | See |
|---|---|
| Attended Install | Install a new publisher and import the data. To configure Emergency Responder with Install with Data Import follow the instructions as described in Install Emergency Responder Publisher from step 1 through 4. In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Emergency Responder installation. In the import wizard, provide details for the following information: Hostname, IP Address, Subnet mask, and Gateway. This must be the same information provided in the destination node for which
                                                                        you exported the data. SFTP—In the export data directory, enter the exported data folder name or cluster information: <Publisher IP Address>. Confirm whether this is the First Node. Enter one or more NTP servers. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. Install a new Subscriber and import the data. Repeat step 4 except for the First Node question. Respond to this query with
                                                                  a 'No' and provide the new publisher IP Address and hostname information. Note If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. |
| Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. |
| Note | If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. |
| Touchless Install of a Single Node or a Cluster | Follow the instructions as described in Touchless Installation Task Flow for ESXi from step 1 through 5. |

| Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                              a new publisher node. |
|---|---|

| Note | If you are planning to use the same Hostname/IP Address, ensure that the older subscriber node is shut down before installing
                                                                              a new subscriber node. |
|---|---|

| Note | If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Licensing | Note Applicable for both Simple and Network Migrations You must reregister the license after migrating to the new Cisco Emergency Responder server. For more information on configuration,
                                                see License Manager . | Note | Applicable for both Simple and Network Migrations |
| Note | Applicable for both Simple and Network Migrations |
| Step 2 | CTI Route Points and Ports Re-Registration | Note Applicable only for Network Migration We recommend that you reregister the CTI Route Points and ports for the destination Emergency Responder Publisher and Subscriber
                                                nodes after network migration. | Note | Applicable only for Network Migration |
| Note | Applicable only for Network Migration |
| Step 3 | (Optional) CTI Route Points and Ports Re-registration in Mixed Mode | Note Applicable for both Simple and Network Migrations Post migration, you must perform this procedure to reregister the CTI Route Points and ports in mixed mode. | Note | Applicable for both Simple and Network Migrations |
| Note | Applicable for both Simple and Network Migrations |
| Step 4 | Clustering | Note Applicable only for Network Migration Consider the following for clustering points post migration: Old Hostnames Retained in Cisco ER Groups After Network Migration —After a network migration, identify and update all outdated hostname entries (Publisher and Subscriber) with the new hostnames
                                                      and corresponding passwords in the Cisco ER Groups on both clusters. Restart both the clusters and verify that the hostname
                                                      changes are correctly reflected across all nodes. Tomcat Certificate Exchange Required in CER Clustering Setup Post Migration in Secure Mode —After a network migration, redo the Tomcat exchange in the cluster. | Note | Applicable only for Network Migration |
| Note | Applicable only for Network Migration |
| Step 5 | Upload a New National E911 Certificate After Network Migration | Note Applicable for both Simple and Network Migrations Ensure that you upload a new National E911 Certificate if you are migrating from Release 12.5(1)SU9. | Note | Applicable for both Simple and Network Migrations |
| Note | Applicable for both Simple and Network Migrations |
| Step 6 | Configure Off-premises Settings | Note Applicable only for Network Migration You must re-configure the Off-premises settings in the Cisco Unified Communications Manager Administration user interface. | Note | Applicable only for Network Migration |
| Note | Applicable only for Network Migration |
| Step 7 | SAML SSO | Note Applicable only for Network Migration After you complete the network migration, ensure that you re-enable SSO on the destination nodes. This step is required because
                                                SAML SSO was previously enabled on the source Emergency Responder nodes metadata. | Note | Applicable only for Network Migration |
| Note | Applicable only for Network Migration |
| Step 8 | Update Unified CM Node on Emergency Responder After Unified CM Network Migration | Note Perform this procedure only after a Network Migration of your Unified Communications Manager server. Delete the Unified CM server and SNMPv2 settings from the Emergency Responder configuration and reconfigure it after network
                                                migration. | Note | Perform this procedure only after a Network Migration of your Unified Communications Manager server. |
| Note | Perform this procedure only after a Network Migration of your Unified Communications Manager server. |

| Note | Applicable for both Simple and Network Migrations |
|---|---|

| Note | Applicable only for Network Migration |
|---|---|

| Note | Applicable for both Simple and Network Migrations |
|---|---|

| Note | Applicable only for Network Migration |
|---|---|

| Note | Applicable for both Simple and Network Migrations |
|---|---|

| Note | Applicable only for Network Migration |
|---|---|

| Note | Applicable only for Network Migration |
|---|---|

| Note | Perform this procedure only after a Network Migration of your Unified Communications Manager server. |
|---|---|

| Step 1 | To delete the Unified Communications Manager entry from the source node, perform the following steps after successful migration: Log in to the Cisco Emergency Responder Administration Servlet on the source node. Navigate to Phone Tracking > Cisco Unified Communications Manager . Delete the connected Unified Communications Manager entry. |
|---|---|
| Step 2 | To reregister CTI Route Points and CTI Ports on the destination Emergency Responder Publisher and Subscriber nodes, restart
                                                the Cisco Emergency Responder service by entering the following command: utils service restart Cisco Emergency Responder . Note In case the CTI Ports does not reregister, perform the following steps: Log in to the Cisco Unified CM Administration user interface. Navigate to Device > CTI Route Points . Select the Emergency Call Route Points (for example, 911, 912, and 913) and select Reset > Refresh . | Note | In case the CTI Ports does not reregister, perform the following steps: |
| Note | In case the CTI Ports does not reregister, perform the following steps: |

| Note | In case the CTI Ports does not reregister, perform the following steps: |
|---|---|

| For CTI Route Points Registration, perform these additional steps after successful migration. For Simple Migration , after registering the source Emergency Responder with Unified Communications Manager in mixed mode, and before starting
                                                      the migration, ensure that: You migrate using only one application user, or use a unique application user that is not currently assigned to any other
                                                               Emergency Responder. You use only one set of Certificate Authority Proxy Function (CAPF) profiles, and these profiles are not attached to any other
                                                               server or application user. After you complete the Network Migration , perform the following steps: On the Emergency Responder source nodes, delete the Unified CM entry from Phone Tracking > Cisco Unified Communications Manager . Restart the Cisco Emergency Responder service on the source Emergency Responder publisher node. In the Cisco Unified CM Administration user interface, navigate to the User Management > User Settings > Application User CAPF Profile menu, and delete the existing CAPF profiles and readd them, OR create new CAPF profiles and provide the details in the destination
                                                               Emergency Responder ( Phone Tracking > Cisco Unified Communications Manager ). In the Cisco Unified CM Administration user interface, navigate to Device > CTI Route Points . The CTI Route Points should register automatically. If they do not register, restart the CTI Route Points. |
|---|

| Note | When you migrate your Emergency Responder from Release 12.5(1)SU9 to Release 15SU4 or higher, the old .psf certificate is
                                                   no longer valid or supported. |
|---|---|

| Step 1 | From Emergency Responder, choose System > National E911 Service Provider VUI Settings . |
|---|---|
| Step 2 | Click Upload Certificate . |
| Step 3 | Use the Browse button to locate the new .bcfks certificate file, highlight the file, and click the Upload button, and complete any additional configurations required for the National E911 Service Provider. |

| Step 1 | In Cisco Unified Communications Manager Administration, use the System > Enterprise Parameters Configuration. |
|---|---|
| Step 2 | If the Hostname (FQDN) Verification Policy is set to Always verify Hostname (FQDN) or Verify Hostname (FQDN) if possible , then perform the following steps: Delete the Emergency Responder source node Tomcat certificate. Add the Emergency Responder destination node Tomcat certificate as Tomcat-trust on Unified CM. Update the IP Address and End User URL in the Application Server Configuration ( System > Application Server ) with the destination node details. Restart the Cisco E911 service and Cisco Tomcat service on Unified CM. |
| Step 3 | If the Hostname (FQDN) Verification Policy is set to Do not verify Hostname (FQDN) , then perform the following steps: Update the IP Address and End User URL in the Application Server Configuration ( System > Application Server ) with the destination node details. Restart the Cisco E911 service and Cisco Tomcat service on Unified CM. |

| Step 1 | Select Phone Tracking > Cisco Unified Communications Manager details. |
|---|---|
| Step 2 | Select the Unified CM server and click the Delete icon to delete the server. |
| Step 3 | Click Add New to add the new IP address of the Unified CM server to the Emergency Responder after a Network Migration. |
| Step 4 | Navigate to Phone Tracking > SNMPv2 Settings . |
| Step 5 | Click Delete to delete the existing SNMPv2 configuration for the source Unified Communications Manager node from Emergency Responder. |
| Step 6 | Click Add New to add the new SNMPv2 configuration for the destination Unified Communications Manager node to Emergency Responder. |
| Step 7 | Verify that the CTI Route Points and CTI Ports register to the destination Unified Communications Manager node after the new
                                                Unified CM and SNMPv2 Settings are added. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Read the Release Notes and any Readme files that come with your release. | You can download the Release Notes from the below URL. Make sure that you understand the features for your release and any
                                             COP file requirements. https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/products-release-notes-list.html |
| Step 2 | Configure Software Location on cluster nodes that will be used for future upgrades and COP Installs. | Before you attempt to upgrade any cluster nodes or install any COP files on the cluster nodes, all cluster nodes need to have
                                             their Software Location fields configured. |
| Step 3 | Install Licenses | Verify that you have the required licenses for your system and devices. |
| Step 4 | Configure the Backup | We recommend performing regular backups. You can set up automatic backups or invoke a backup at any time. |
| Step 5 | Change Virtual Machine Configuration Specifications | To change to the Guest OS version in the Emergency Responder virtual machine (VM) settings. Note This step is not applicable for Cisco NFVIS-for-UC and Nutanix AHV. | Note | This step is not applicable for Cisco NFVIS-for-UC and Nutanix AHV. |
| Note | This step is not applicable for Cisco NFVIS-for-UC and Nutanix AHV. |

| Note | This step is not applicable for Cisco NFVIS-for-UC and Nutanix AHV. |
|---|---|

| Step 1 | Shut down the virtual machine. |
|---|---|
| Step 2 | Change the configuration of the virtual machine as needed through vSphere. You can update the Guest OS and VM Hardware Compatibility Update VM Hardware Compatibility—Left click Virtual Machine. Check for Updates . Click Update Note If you are not aware of the host, click Check status and click Upgrade to match host. Update Guest OS—Right click the Virtual Machine > Edit Settings > Virtual Machine Option > General Option > Guest OS Version . | Note | If you are not aware of the host, click Check status and click Upgrade to match host. |
| Note | If you are not aware of the host, click Check status and click Upgrade to match host. |
| Step 3 | Power on the Virtual Machine. The following warning message appears in ESXi when you open the virtual machine settings while the machine is running and
                                                there is a mismatch. Warning The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                            running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations. | Warning | The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                            running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations. |
| Warning | The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                            running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations. |

| Note | If you are not aware of the host, click Check status and click Upgrade to match host. |
|---|---|

| Warning | The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                            running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations. |
|---|---|

| Installation Task | For More Information |
|---|---|
| Upgrade Emergency Responder | Software Upgrades |
| Upgrade Unified CM | https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html Change Cisco Unified Communications Manager Version |
| Update Unified CM Version | Update Cisco Unified Communications Manager Version |