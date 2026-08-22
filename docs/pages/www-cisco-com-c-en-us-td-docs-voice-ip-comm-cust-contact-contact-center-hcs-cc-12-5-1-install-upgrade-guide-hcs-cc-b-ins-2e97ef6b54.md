---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-install-upgrade-guide-hcs-cc-b-ins-2e97ef6b54
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Install_Upgrade_Guide/hcs-cc_b_installing-and-upgrading-guide_12_5/hcs-cc_b_installing-and-upgrading-guide-for_chapter_011.html
retrieved_at: 2026-08-22T00:12:20.610018+00:00
---

Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

# Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

Updated: July 26, 2022

Chapter: Core Component Installation

## Chapter: Core Component Installation

# Core Component Installation

## Core Components
                        	 Installation Approach

You can use golden
                           		templates to clone and deploy contact center core components as virtual
                           		machines (VM) on servers.

If you chose to create virtual machines directly on destination servers, do not convert the virtual machine to a template.
                                       For VOS based machines, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

### Core Component
                           	 Voice Gateway Installation

For instructions on deploying the Cisco CSR 1000v OVA using vSphere, see the Cisco CSR 1000v Series Cloud Services Router
                              Software Configuration Guide at: https://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/configuration/b_CSR1000v_Configuration_Guide/b_CSR1000v_Configuration_Guide_chapter_011.html#d41950e959a1635

For information on Integrated Services Routers, see https://www.cisco.com/c/en/us/td/docs/routers/access/4400/release/xe-16-rn/isr4k-rel-notes-xe-16_3.html

If the SBC supports CUBE Enterprise with Multi-VRF, you can send calls directly from the SBC to the CVP without a dedicated
                                          CUBE Enterprise for the HCS for  Contact Center instances. However, using the aggregation SBC without a dedicated CUBE Enterprise
                                          affects performance and scalability.

The following figure shows the CUBE Enterprise topology for HCS
                              		deployment.

#### Configure Service
                              	 Interface for Carrier Network

To create the
                                 		service interface for carrier network, perform the following instructions.

```
interface GigabitEthernet1
ip address 192.168.10.2 255.255.255.0
negotiation auto
```

#### Configure Codec
                              	 List

To configure codec
                                 		list, perform the following instructions.

```
voice class codec 1
 codec preference 1 g711ulaw
 codec preference 2 g729r8
 codec preference 3 g729br8
 codec preference 5 g711alaw
```

For Small Contact
                                             		  Center deployments, you may configure the carrier interface as a VRF.

## Golden Template
                        	 Requirements

Contact center core components vary for each deployment model. The following table provides information about the golden templates
                              for required core components.

Golden Templates

2000 Agents

4000 Agents

12000 Agents

24000 Agents

Small Contact Center

Unified CCE Rogger

Yes

Yes

—

—

Yes

Unified CCE Router

—

—

Yes

Yes

—

Unified CCE Logger

—

—

Yes

Yes

—

Unified CCE AW-HDS-DDS

Yes

Yes

—

—

Yes

Unified CCE AW-HDS

—

—

Yes

Yes

—

Unified CCE HDS-DDS

—

—

Yes

Yes

—

Unified CCE Agent PG

—

—

—

—

Yes

Unified CCE VRU PG

—

—

—

—

Yes

Unified CCE PG

Yes

Yes

Yes

Yes

—

Unified CVP Server

Yes

Yes

Yes

Yes

Yes

Unified CVP OAMP Server

Yes

Yes

Yes

Yes

Yes

Unified CVP Reporting Server

Yes

Yes

Yes

Yes

Yes

Cisco Finesse

Yes

Yes

Yes

Yes

Yes

Cisco Unified Intelligence Center Coresident Deployment

Yes

—

—

—

—

Cisco Unified Intelligence Center

—

Yes

Yes

Yes

Yes

Live Data Reporting System

—

Yes

Yes

Yes

Yes

Cisco Identity Service

—

Yes

Yes

Yes

Yes

Cisco Unified Communications Manager

Yes

Yes

Yes

Yes

Yes

### Create Golden
                           	 Template for Unified CCE Rogger

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

After you deploy OVA for 500 agents deployment (HCS for CC 2000 reference only), edit the settings and change the MHz reservation
                                             to 2500.

Step 1

Create a
                                          			 virtual machine for Unified CCE Rogger using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install
                                          			 Microsoft SQL server.

Step 5

Install Unified Contact Center Enterprise.

Step 6

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Unified CCE Router

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

Step 1

Create a
                                          			 virtual machine for Unified CCE Router using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install Unified Contact Center Enterprise.

Step 5

Convert the
                                          			 virtual machine to a template.

### Create Golden
                           	 Template for Unified CCE Logger

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

Step 1

Create a
                                          			 virtual machine for Unified CCE Logger using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install
                                          			 Microsoft SQL server.

Step 5

Install Unified Contact Center Enterprise.

Step 6

Convert the
                                          			 virtual machine to a template.

### Create Golden
                           	 Template for Unified CCE AW-HDS-DDS

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

After you deploy OVA for 500 agents deployment (HCS for Contact Center 2000 reference only), edit the settings and change
                                             the Memory to 8GB and MHz Reservation to 3200.

Step 1

Create a
                                          			 virtual machine for Unified CCE AW-HDS-DDS using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install
                                          			 Microsoft SQL server.

Step 5

Install Unified Contact Center Enterprise.

Step 6

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Unified CCE AW-HDS

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

Step 1

Create a
                                          			 virtual machine for Unified CCE AW-HDS using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install
                                          			 Microsoft SQL server.

Step 5

Install Unified Contact Center Enterprise.

Step 6

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 template for Unified CCE HDS-DDS

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

Step 1

Create a
                                          			 virtual machine for Unified CCE HDS-DDS using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install
                                          			 Microsoft SQL server.

Step 5

Install Unified Contact Center Enterprise.

Step 6

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Unified CCE PG

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

For 500 agents deployment of the HCS for Contact Center 2000 agent reference, select the Small PG OVA.

Step 1

Create a
                                          			 virtual machine for Unified CCE PG using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install Unified Contact Center Enterprise.

Step 5

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Unified CVP Server

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

Step 1

Create a
                                          			 virtual machine for Unified CVP Server using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install the
                                          			 Unified CVP Server.

Step 5

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Unified CVP OAMP Server

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

Step 1

Create a
                                          			 virtual machine for Unified CVP OAMP Server using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install the
                                          			 Unified CVP OAMP server.

Step 5

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Unified CVP Reporting Server

#### Before you begin

Download the OVA files. Use UCCE_12.5_Windows_vmv13_v1.0 to
                                 				create the golden template.

Step 1

Create a
                                          			 virtual machine for Unified CVP Reporting server using the OVA.

Step 2

Install
                                          			 Microsoft Windows server.

Step 3

Install an
                                          			 anti-virus software.

Step 4

Install the
                                          			 Unified CVP Reporting server.

Step 5

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Cisco Finesse

#### Before you begin

Download the OVA files. Use Finesse_12.5.1_VOS12.5.1_vmv13_v1.3 to create the golden template.

For Small Contact Center 100 agents dedicated sub-customer deployment and 500 agents deployment (HCS for Contact Center 2000
                                             reference and Small Contact Center 500 agent deployment), select the Finesse 500 agents OVA.

After you deploy OVA for 500 agents deployment (HCS for Contact Center 2000 reference and Small Contact Center 500 agent deployment)
                                             change the vCPU value to 4.

Step 1

Create a
                                          			 virtual machine for Cisco Finesse.

Step 2

Install Cisco
                                             				Finesse .

Step 3

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Cisco Unified Intelligence Center Coresident Deployment

#### Before you begin

Cisco Unified
                                 		  Intelligence Center coresident deployment includes Cisco Unified Intelligence
                                 		  Center, Live Data, and Identity Service components.

Download the OVA files. Use CUIC_12.5.1_vmv13_v2.15 to create the golden template.

After you deploy OVA for 500 agents deployment (HCS for Contact Center 2000 reference only), edit the settings and change
                                             the memory to 12 GB.

Step 1

Create a
                                          			 virtual machine for Cisco Unified Intelligence Center coresident deployment
                                          			 using the OVA.

Step 2

To install Cisco
                                             				Unified Intelligence Center with Live Data and Ids , follow the
                                          			 installation procedure in the Install Voice
                                             				OS based Application and select Cisco
                                             				Unified Intelligence Center with Live Data and Ids in the Product
                                             				Deployment Selection page .

Step 3

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Cisco Unified Intelligence Center

#### Before you begin

Download the OVA files. Use CUIC_12.5.1_vmv13_v2.15 to create the golden template.

Step 1

Create a
                                          			 virtual machine for Cisco Unified Intelligence Center using the OVA.

Step 2

To install Cisco
                                             				Unified Intelligence Center , follow the installation procedure in
                                          			 the Install Voice
                                             				OS based Application and select Cisco
                                             				Unified Intelligence Center in the Product
                                             				Deployment Selection page.

Step 3

Convert the
                                          			 virtual machine to a golden template.

### Create Golden Template for Live Data Reporting System

#### Before you begin

Download the OVA files. Use UCCELD_12.5_VOS_vmv13_v1.0 to create the golden template.

See related links to run the steps.

Step 1

Create a
                                          			 virtual machine for Live Data Reporting System using the OVA.

Step 2

Select Live
                                             				Data in the Product
                                             				Deployment Selection page .

Step 3

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Cisco Identity Service

#### Before you begin

Download the OVA files. Use IDS_12.5.1_VOS_vmv13_v1.0 to create the golden template.

Step 1

Create a
                                          			 virtual machine for Cisco Identity Service using the OVA.

Step 2

To install Cisco
                                             				Identity Service (Ids) , follow the installation procedure in the Install Voice
                                             				OS based Application and select Cisco
                                             				Identity Service (Ids) in the Product
                                             				Deployment Selection page.

Step 3

Convert the
                                          			 virtual machine to a golden template.

### Create Golden
                           	 Template for Cisco Unified Communications Manager

#### Before you begin

Download the OVA files. Use cucm_11.5_vmv8_v1.1 or cucm_12.5_vmv13_v1.0 to create the golden template.

Select the 2500 agents OVA for SCC 100 agents dedicated sub-customer deployment and 500 agents deployment (HCS for Contact Center 2000 reference
                                             and Small Contact Center 500 agent deployment).  After you deploy the OVA edit the settings and change the vCPU value to 2.

Step 1

Create a
                                          			 virtual machine for Cisco Unified Communications Manager using the OVA.

Step 2

To install Cisco
                                             				Unified Communications Manager , follow the installation procedure
                                          			 in the Install Voice
                                             				OS based Application and select Cisco
                                             				Unified Communications Manager in the Product
                                             				Deployment Selection page.

Step 3

Convert the
                                          			 virtual machine to a golden template.

## Common Procedures
                        	 for Golden Templates

### Download OVA
                           	 Files

Open Virtualization Format files (OVAs) are required for golden
                                 		  templates. Cisco HCS for Contact
                                       						Center uses the OVAs that define the basic structure of the corresponding VMs that are
                                 		  created. The structure definition Includes the CPU, RAM, disk space,
                                 		  reservation for CPU, and reservation for memory.

The VMs and software components are optimized for Cisco HCS for Contact
                                                   						Center .
                                             			 You must use the OVAs for Cisco HCS for Contact
                                                   						Center .

#### Before you begin

You must have a valid service contract associated with your Cisco.com
                                 		  profile

Step 1

Go to the Hosted Collaboration Solution for Contact Center Download Software page on Cisco.com.

Step 2

Select the required software type.

Step 3

Click Download and save the OVA file to your local
                                          			 drive. When you create VMs, select the OVA required for the application.

### Create Virtual
                           	 Machines

Step 1

Launch the
                                          			 VMware vSphere client and select File > Deploy OVF
                                                				  Template .

Step 2

Browse to the
                                          			 location on your local drive, where you have stored the OVA. Click Open to select the OVA file, click Next .

Step 3

On the OVF
                                             				Template Details page, click Next .

Step 4

On the Name
                                             				and Location page, in the Name field, enter the name of virtual machine, then
                                          			 click Next .

Enter a
                                                         				  maximum of 32 characters; spaces and special characters are not allowed.

Step 5

On the Deployment Configuration page, select the appropriate
                                          			 configuration from the drop-down list, click Next .

Step 6

On the Resource Pool page, select the required resource
                                          			 pool, then click Next .

Skip this
                                                         				  step if you do not have a resource pool allocated in the host server.

Step 7

On the Storage page, select a data store you want to deploy
                                          			 in the new virtual machine, then click Next .

Step 8

On the Disk
                                             				Format page, select Thick
                                             				provisioned Lazy Zeroed , then click Next .

Step 9

On the Network
                                             				Mapping page, select the appropriate network from the Destination Network drop-down list, then click Next .

Public
                                                               						to Visible Network

Private
                                                               						to Private Network

Step 10

Click Finish .

### Mount  ISO Files

Upload ISO image to data store:

Select the host in the vSphere client and click Configuration . Then click Storage in the left panel.

Select the datastore that will hold the ISO file.

Right click and select Browse datastore .

Click the Upload icon and select Upload file .

Browse to the location on your local drive where you saved the ISO file, and upload the ISO to the datastore.

Mount the ISO image:

Right-click the VM in the vSphere client and select Edit virtual machine settings .

Click Hardware and select CD|DVD Drive 1 .

Check Connect at power on (Device status panel upper right).

Click the Datastore ISO File radio button and then click Browse .

Navigate to the data store where you uploaded the file.

Select the ISO file and click OK .

### Unmount ISO
                           	 File

Step 1

Right-click
                                          			 the virtual machine in the vSphere client and select Edit
                                             				virtual machine settings .

Step 2

Click Hardware and select CD/DVD
                                             				Drive 1 .

Step 3

Select Client Device and click OK .

### Install Microsoft Windows Server

Complete the following procedure to install Microsoft Windows Server on the virtual machines deployed.

Deploying VM with Guest Operating System ‘Microsoft Windows Server 2019’ on ESXi 7.0 using CCE OVA template displays a warning
                                             message “The configured guest OS (Microsoft Windows Server 2016 or later (64-bit)) for this virtual machine does not match
                                             the guest that is currently running (Microsoft Windows Server 2019 (64-bit)). You should specify the correct guest OS to allow
                                             for guest-specific optimization”. This warning message is informational only and has no detrimental effect on the system.
                                             This warning message is displayed only once and can be dismissed.

Before installing 12.5(1) ICM on SQL Server 2019 , make sure to install ODBC Driver 13 for SQL Server® manually.

Step 1

Mount the Microsoft Windows Server ISO image to the virtual machine.

Check the Connect at power on check box when mounting the ISO.

Step 2

Power on the VM.

Step 3

Enter the Language, Time and Currency Format, and Keyboard settings. Click Next .

Step 4

Click Install Now .

Step 5

If prompted, enter the product key for Windows Server and click Next .

Step 6

Select the Desktop Experience option for the Windows Server and click Next .

Step 7

Accept the license terms and click Next .

Step 8

Select Custom: Install Windows only (advanced) , select Drive 0 to install Microsoft Windows Server, and then click Next .

The installation begins. After the installation is complete, the system restarts without prompting.

Step 9

Enter and confirm the password for the administrator account, and then click Finish .

Step 10

Enable Remote Desktop connections as follows:

Navigate to Control Panel > System and Security > System .

Click Remote Settings .

Click the Remote tab.

Select the Allow remote connections to this computer radio button. The Remote Desktop Connection dialog displays a notification that the Remote Desktop Firewall exception is
                                                enabled. Click OK .

Step 11

Open the Network and Sharing Center , and in the View
                                          					your basic network info and set up connections section, click Ethernet .

Step 12

In the Ethernet Status window, click Properties .

Step 13

In the Ethernet Properties dialog box, configure the network settings and the Domain Name System (DNS) data:

Uncheck Internet Protocol Version 6 (TCP/IPv6) .

Select Internet Protocol Version 4 (TCP/IPv4) and click Properties .

Select Use the following IP Address .

Enter the IP address, subnet mask, and default gateway.

Select Use the following DNS Server Address .

Enter the preferred DNS server address, and click OK .

Step 14

Navigate to Control Panel > System and Security > System . Follow the instructions:

Click Change Settings .

In Computer name tab, click Change .

Change the name of the computer from the name randomly generated during Microsoft Windows Server installation. The name does
                                                not contain underscores or spaces.

Select Domain radio button to change the member from Workgroup to Domain.

Enter qualified domain name and click OK .

In the Windows security dialog, validate the domain credentials and click OK .

On successful authentication, click OK .

Reboot the server and sign in with domain credentials.

If you want to install Unified CCE on
                                             					a multilingual version of Windows Server, refer to Microsoft documentation for
                                             					details in installing Microsoft Windows Server Multilingual language packs.

If Unified CCE language pack is applied on Chinese Windows OS machine, set the
                                             					screen resolution to 1600 x 1200.

### Install VMware Tools for Windows

Step 1

From the vSphere Client, right-click the virtual machine, select Power , and click Power On .

Step 2

Click the Summary tab.

installed and current

installed and not current

not installed

Step 3

Click the Console tab to make sure that the guest operating system starts successfully. Log in if prompted.

Step 4

Right-click the virtual machine, select Guest OS , and
                                          					then click Install/Upgrade VMware Tools . The Install/Upgrade VMware Tools window appears with the
                                          					option - Interactive Tools Upgrade and Automatic Tools Upgrade.

To install/upgrade the VMware tools manually, select the Interactive Tools Upgrade option, and click OK . Follow the on-screen instructions to
                                                							install/upgrade the VMware tools, and restart the virtual machine when
                                                							prompted.

To install/upgrade the VMware tools automatically, select the Automatic Tools Upgrade option, and click OK . This process takes a few minutes to
                                                							complete, and restart the virtual machine when prompted.

### Install Antivirus
                           	 Software

Perform this procedure for both golden-template and for direct-install options.

Install any of the antivirus software products supported by HCS for CC for Contact Center.

For more information on the anitvirus software and versions supported by HCS for CC for Contact Center, see Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/products-device-support-tables-list.html .

Install any of the antivirus software products supported by Enterprise Chat and Email. For more information on the anitvirus
                                 software and versions supported by Enterprise Chat and Email, see the System Requirements for Enterprise Chat and Email at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-implementation-design-guides-list.htm .

Important

Update antivirus software, manually - do not enable automatic updates.

Tip

To allow required access to installation program files or folders, perform file-blocking exclusions in the antivirus product
                                             file-and-folder protection rules. To do this in McAfee VirusScan:

Launch the VirusScan console.

Right-click Access Protection , then select Properties .

In the Anti-virus Standard Protection category, make sure that the Prevent IRC communication check box is unchecked in the Block column.

Important

HCS for CC for Contact Center supports Symantec Endpoint Protection.

Be aware that in the firewall component of Symantec Endpoint Protection 12.1, the Network Threat Protection feature, must
                                             be disabled. If it remains enabled, which is the default, both sides of the duplexed router shows up in simplex mode, thus
                                             blocking communications between each side of the router. This blocking impacts all deployment types.

If you retain the default (enabled) start services on side A and B of the router, a Symantec message pops up in the system
                                             tray indicating: The client will block traffic from IP address [side A router address] for the next 600 seconds(s). This message
                                             also appears in the client management security log. The Symantec Network Threat Protection traffic log indicates that a default
                                             firewall rule called “Block_all” was dynamically enabled. The result in both sides of the router come up in simplex mode.

To avoid the issue, you must disable the Symantec firewall and restart both sides of the router. To do this, double click the Symantec icon in the system tray and select Change Settings . Then configure settings for Network Threat Protection and uncheck the Enable Firewall check box at the top of the Firewall tab.

#### Disable Port
                              	 Blocking

Exclude the following folders from on-access scanning configuration of the AV program for all Antivirus scans:

c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA

It is the customer's responsibility to deploy the VXML applications after the Antivirus scans. This also applies to the custom java/jar/class files deployed in the shared path.

For more information on the Virus Scan guidelines, refer to the following sections of the UCCE documentation:

The Virus Protection section of UCCE Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

The General Antivirus Guidelines section of the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

### Install Microsoft SQL Server

Install Microsoft SQL Server and store the SQL Server log and
                                 				temporary files on the same vDisk as the operating system when using default (two) vDisk design. If you choose to use more
                                 				than two virtual disks, then the tempDB cannot be on the same vDisk as the solution
                                 				database.

For further information
                                 				about the database placement and performance tuning the SQL installation, see the
                                 				Microsoft documentation.

#### Before you begin

Microsoft SQL Server
                                             					does not contain SQL Server Management Studio in the default toolkit. To rerun
                                             					the SQL Server setup to install Management Studio, navigate to: SQL Selection Center > Installation > Install SQL Server Management Tools . If your computer has no internet connection, download and
                                             					install SQL Server Management Studio manually.

VC++ 2017 build#
                                                						14.12.25810 is not compatible with the Cisco Contact Center
                                             					Enterprise, ensure that it is not installed.

Step 1

Mount the Microsoft SQL Server ISO image to the virtual machine. For more
                                             						information, see Mount ISO Files .

Step 2

Select Installation in the left pane and then click New SQL Server stand-alone installation or add
                                             						features to an existing installation . Click OK .

Step 3

On the Product Key page, enter the product key and then
                                          					click Next .

Step 4

Accept the License Terms and then click Next .

Step 5

Optional: On the Microsoft Update page, check the Use Microsoft Update to check for updates check box,
                                          					and then click Next .

If you do not check the Use Microsoft Update to check for
                                                            								updates option, click Next on the Product Updates page.

Step 6

On the Install Rules page, click Next .

In this step, the installation program checks to see that your system meets
                                             						the hardware and software requirements. If there are any issues, warnings or
                                             						errors appear in the Status column. Click the links
                                             						for more information about the issues.

Step 7

On the Feature Selection page, select only the following,
                                          					and click Next :

Database Engine Services

Client Tools Connectivity

Client Tools Backwards Compatibility

Client Tools SDK

SQL Client Connectivity SDK

Step 8

On the Instance Configuration page, select Default Instance and click Next.

Step 9

On the Server Configuration page, click the Services Account tab.

Associate the SQL services with the virtual account.

For the SQL Server Database Engine, in the Account Name
                                                         										field, select NT
                                                            										Service\MSSQLSERVER .

While you can use the Network or Local Services account instead
                                                               									of the Virtual account, using the Virtual account provides
                                                               									security.

For the remaining services, accept the default values.

In the Start Up Type column, for the SQL Server Agent service account,
                                                							select Automatic from the list.

Enable Grant Perform Volume Maintenance Task privilege to
                                                   								SQL Server Database Engine Service .

Unified ICM Installer automatically enables the Grant Perform Volume Maintenance Task for the NT service account.If it is not enabled automatically then you must enable Grant Perform Volume Maintenance Task privilege to SQL Server Database Engine Service manually on the SQL server.

Step 10

On the Server Configuration page, click the Collation tab.

In the Database Engine section, click Customize .

Select the Windows Collation designator and sort
                                                   								order radio button.

Select the appropriate collation. Typically, you choose the SQL
                                                							Server collation that supports the Windows system locale most
                                                							commonly used by your organization; for example, "Latin1_General" for
                                                							English.

The database entry is related to the collation that you select. For
                                                   								example, if you set the collation for Latin1_General, but you select
                                                   								Chinese language at sign-in. When you enter field values in Chinese,
                                                   								the application displays the unsupported
                                                      									character error, because the database does not
                                                   								support the characters.

Important

It is critical to select the correct collation setting for the
                                                               									language display on your system. If you do not select the
                                                               									correct collation during installation, you must uninstall and
                                                               									reinstall Microsoft SQL Server.

Check the Binary check box.

Click OK , and then click Next .

Step 11

On the Database Engine Configuration page:

On the Server Configuration tab, click the Mixed
                                                   								Mode radio button.

Enter the password for the SQL Server system administrator
                                                							account, and confirm by reentering it.

Click Add Current User to add the user who is
                                                							installing the SQL Server as an administrator.

On the TempDB tab, set the Initial
                                                   								size and Autogrowth for Rogger,
                                                							Logger, AW-HDS-DDS, AW-HDS, and HDS-DDS. For information about values
                                                							for respective components Increase Database and Log File Size for TempDB .

For more information about the SQL Server TempDB Database and its
                                                   								use, see the Microsoft SQL Server documentation.

On the MaxDOP tab, choose the value of MaxDOP as half the value of logical CPU cores detected on the computer which is displayed just above the MaxDOP configuration. For
                                                example, if the logical CPU cores are detected as 4, then MaxDOP should be configured as 2.

SQL Server installation automatically recommends the MaxDOP server configuration based on the number of processors available.
                                                               This feature is introduced in SQL Server 2019 and later. In SQL Server 2017, you can configure MaxDOP post installation. To
                                                               configure MaxDOP, do the following:

In Object Explorer , right-click the database instance and select Properties .

Select Advanced .

In the Max Degree of Parallelism box, configure the number of processors as recommended above.

Click Next .

Step 12

On the Ready to Install page, click Install .

Step 13

On the Complete page, click Close .

Step 14

Enable Named Pipes and set the sort order as follows:

Open the SQL Server Configuration Manager.

In the left pane, navigate to SQL Native Client 11.0
                                                   								Configuration (32bit) > Client
                                                   								Protocols .

In the right pane, confirm that Named Pipes is Enabled .

Right-click Client Protocols and select Properties .

In the Enabled Protocols section of the Client Protocols Properties window, use the
                                                							arrow buttons to arrange the protocols in the following order:

Named Pipes

TCP/IP

Check the Enable Shared Memory Protocol and then
                                                							click OK .

In the left pane, navigate to SQL Server Network
                                                   								Configuration > Protocols for
                                                   								MSSQLSERVER .

In the right pane, right-click Named Pipes and
                                                							select Enable .

By default, Microsoft SQL Server dynamically resizes its memory. The SQL
                                                         							Server reserves the memory based on process demand. The SQL Server frees
                                                         							its memory when other processes request it, and it raises alerts about
                                                         							the memory monitoring tool.

Cisco supports the Microsoft validation to dynamically manage the SQL
                                                         							Server memory. If your solution raises too many memory alerts, you can
                                                         							manually limit SQL Server’s memory usage. Set the maximum and minimum
                                                         							limit of the SQL memory using the maximum memory
                                                            								usage settings in the SQL Server
                                                            								Properties menu.

For more information about the SQL Server memory settings and its use,
                                                         							see the Microsoft SQL Server documentation.

Step 15

Set the SQL Server's default language to English as follows:

Launch SQL Server Management Studio.

In the left pane, right-click the server and select Properties .

Click Advanced .

In the Miscellaneous section, set the Default Language to English .

Click OK .

Important

Set the SQL Server default language to English because Cisco
                                                         							Unified Contact Center Enterprise requires a US date format (MDY). Many
                                                         							European languages use the European date format (DMY) instead. This
                                                         							mismatch causes queries such as select * from table where date =
                                                            								'2012-04-08 00:00:00' to return data for the wrong date.
                                                         							Handle localization in the client application, such as Cisco Unified
                                                         							Intelligence Center.

Step 16

Restart the SQL Server service as follows:

Navigate to the Windows Services tool.

Right-click SQL Server (MSSQLSERVER) and click Stop .

Right-click SQL Server (MSSQLSERVER) and click Start .

Step 17

Ensure that the SQL Server Browser is started, as follows:

Navigate to the Windows Services tool.

Navigate to the SQL Server Browser.

Right-click to open the Properties window.

Enable the service, change the startup type to Automatic , and click Apply .

To start the service, click Start , and then
                                                							click OK .

#### What to do next

Before installing 12.5(1) ICM on SQL Server
                                             					2019, make sure to install ODBC Driver 13 for SQL Server® manually.

Caution

#### Increase Database and Log File Size for TempDB

To get the benefits of TempDB multiple data files support in CCE components, configure the following values as suggested for
                                 respective components.

### Convert the Virtual
                           	 Machine to a Golden Template

VMware uses the term Template .
                                             			 HCS for Contact Center uses the term Golden
                                                				Template for templates consisting of application and operating systems that
                                             			 are used for HCS for Contact Center.

#### Before you begin

Ensure that the Windows-based template virtual machine is in the WORKGROUP.

Step 1

If the VM is not
                                          			 already powered off, from the VM menu, select Power > Shut down the
                                                				  guest .

Step 2

From the VMware
                                          			 vCenter Inventory menu, right-click the virtual machine and
                                          			 choose Template > Convert to
                                                				  Template .

### Verification of the Downloaded ISO

Perform the following procedure to validate the downloaded ISO  signed by
                                 Cisco, to ensure that it is authorized.

Step 1

Install OpenSSL on Microsoft Windows.

Step 2

Add the OpenSSL installation path to System variables in the Environment Variables of the system.

Step 3

Add the downloaded ISO Image , ISO Image signature file  and the Public key.der file in the same folder for the specific
                                          product component.

Step 4

Launch Command Prompt on the system.

Step 5

Run the following CLI (Command Line Interface) command to verify the files:

openssl dgst -sha512 -keyform der -verify <PUBLIC key.der>
                                                -signature <ISO Image.iso.signature <ISO Image

If the verification fails do not proceed with the installation, contact
                                                         Cisco Support for a valid ISO .

| Note | If you chose to create virtual machines directly on destination servers, do not convert the virtual machine to a template.
                                       For VOS based machines, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
|---|---|

| Note | If the SBC supports CUBE Enterprise with Multi-VRF, you can send calls directly from the SBC to the CVP without a dedicated
                                          CUBE Enterprise for the HCS for  Contact Center instances. However, using the aggregation SBC without a dedicated CUBE Enterprise
                                          affects performance and scalability. |
|---|---|

| Note | For Small Contact
                                             		  Center deployments, you may configure the carrier interface as a VRF. |
|---|---|

| Golden Templates | 2000 Agents | 4000 Agents | 12000 Agents | 24000 Agents | Small Contact Center |
|---|---|---|---|---|---|
| Unified CCE Rogger | Yes | Yes | — | — | Yes |
| Unified CCE Router | — | — | Yes | Yes | — |
| Unified CCE Logger | — | — | Yes | Yes | — |
| Unified CCE AW-HDS-DDS | Yes | Yes | — | — | Yes |
| Unified CCE AW-HDS | — | — | Yes | Yes | — |
| Unified CCE HDS-DDS | — | — | Yes | Yes | — |
| Unified CCE Agent PG | — | — | — | — | Yes |
| Unified CCE VRU PG | — | — | — | — | Yes |
| Unified CCE PG | Yes | Yes | Yes | Yes | — |
| Unified CVP Server | Yes | Yes | Yes | Yes | Yes |
| Unified CVP OAMP Server | Yes | Yes | Yes | Yes | Yes |
| Unified CVP Reporting Server | Yes | Yes | Yes | Yes | Yes |
| Cisco Finesse | Yes | Yes | Yes | Yes | Yes |
| Cisco Unified Intelligence Center Coresident Deployment | Yes | — | — | — | — |
| Cisco Unified Intelligence Center | — | Yes | Yes | Yes | Yes |
| Live Data Reporting System | — | Yes | Yes | Yes | Yes |
| Cisco Identity Service | — | Yes | Yes | Yes | Yes |
| Cisco Unified Communications Manager | Yes | Yes | Yes | Yes | Yes |

| Note | After you deploy OVA for 500 agents deployment (HCS for CC 2000 reference only), edit the settings and change the MHz reservation
                                             to 2500. |
|---|---|

| Step 1 | Create a
                                          			 virtual machine for Unified CCE Rogger using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install
                                          			 Microsoft SQL server. |
| Step 5 | Install Unified Contact Center Enterprise. |
| Step 6 | Convert the
                                          			 virtual machine to a golden template. |

| Step 1 | Create a
                                          			 virtual machine for Unified CCE Router using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install Unified Contact Center Enterprise. |
| Step 5 | Convert the
                                          			 virtual machine to a template. |

| Step 1 | Create a
                                          			 virtual machine for Unified CCE Logger using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install
                                          			 Microsoft SQL server. |
| Step 5 | Install Unified Contact Center Enterprise. |
| Step 6 | Convert the
                                          			 virtual machine to a template. |

| Note | After you deploy OVA for 500 agents deployment (HCS for Contact Center 2000 reference only), edit the settings and change
                                             the Memory to 8GB and MHz Reservation to 3200. |
|---|---|

| Step 1 | Create a
                                          			 virtual machine for Unified CCE AW-HDS-DDS using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install
                                          			 Microsoft SQL server. |
| Step 5 | Install Unified Contact Center Enterprise. |
| Step 6 | Convert the
                                          			 virtual machine to a golden template. |

| Step 1 | Create a
                                          			 virtual machine for Unified CCE AW-HDS using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install
                                          			 Microsoft SQL server. |
| Step 5 | Install Unified Contact Center Enterprise. |
| Step 6 | Convert the
                                          			 virtual machine to a golden template. |

| Step 1 | Create a
                                          			 virtual machine for Unified CCE HDS-DDS using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install
                                          			 Microsoft SQL server. |
| Step 5 | Install Unified Contact Center Enterprise. |
| Step 6 | Convert the
                                          			 virtual machine to a golden template. |

| Note | For 500 agents deployment of the HCS for Contact Center 2000 agent reference, select the Small PG OVA. |
|---|---|

| Step 1 | Create a
                                          			 virtual machine for Unified CCE PG using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install Unified Contact Center Enterprise. |
| Step 5 | Convert the
                                          			 virtual machine to a golden template. |

| Step 1 | Create a
                                          			 virtual machine for Unified CVP Server using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install the
                                          			 Unified CVP Server. |
| Step 5 | Convert the
                                          			 virtual machine to a golden template. |

| Step 1 | Create a
                                          			 virtual machine for Unified CVP OAMP Server using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install the
                                          			 Unified CVP OAMP server. |
| Step 5 | Convert the
                                          			 virtual machine to a golden template. |

| Step 1 | Create a
                                          			 virtual machine for Unified CVP Reporting server using the OVA. |
|---|---|
| Step 2 | Install
                                          			 Microsoft Windows server. |
| Step 3 | Install an
                                          			 anti-virus software. |
| Step 4 | Install the
                                          			 Unified CVP Reporting server. |
| Step 5 | Convert the
                                          			 virtual machine to a golden template. |

| Note | For Small Contact Center 100 agents dedicated sub-customer deployment and 500 agents deployment (HCS for Contact Center 2000
                                             reference and Small Contact Center 500 agent deployment), select the Finesse 500 agents OVA. After you deploy OVA for 500 agents deployment (HCS for Contact Center 2000 reference and Small Contact Center 500 agent deployment)
                                             change the vCPU value to 4. |
|---|---|

| Step 1 | Create a
                                          			 virtual machine for Cisco Finesse. |
|---|---|
| Step 2 | Install Cisco
                                             				Finesse . |
| Step 3 | Convert the
                                          			 virtual machine to a golden template. |

| Note | After you deploy OVA for 500 agents deployment (HCS for Contact Center 2000 reference only), edit the settings and change
                                             the memory to 12 GB. |
|---|---|

| Step 1 | Create a
                                          			 virtual machine for Cisco Unified Intelligence Center coresident deployment
                                          			 using the OVA. |
|---|---|
| Step 2 | To install Cisco
                                             				Unified Intelligence Center with Live Data and Ids , follow the
                                          			 installation procedure in the Install Voice
                                             				OS based Application and select Cisco
                                             				Unified Intelligence Center with Live Data and Ids in the Product
                                             				Deployment Selection page . |
| Step 3 | Convert the
                                          			 virtual machine to a golden template. |

| Step 1 | Create a
                                          			 virtual machine for Cisco Unified Intelligence Center using the OVA. |
|---|---|
| Step 2 | To install Cisco
                                             				Unified Intelligence Center , follow the installation procedure in
                                          			 the Install Voice
                                             				OS based Application and select Cisco
                                             				Unified Intelligence Center in the Product
                                             				Deployment Selection page. |
| Step 3 | Convert the
                                          			 virtual machine to a golden template. |

| Note | See related links to run the steps. |
|---|---|

| Step 1 | Create a
                                          			 virtual machine for Live Data Reporting System using the OVA. |
|---|---|
| Step 2 | Select Live
                                             				Data in the Product
                                             				Deployment Selection page . |
| Step 3 | Convert the
                                          			 virtual machine to a golden template. |

| Step 1 | Create a
                                          			 virtual machine for Cisco Identity Service using the OVA. |
|---|---|
| Step 2 | To install Cisco
                                             				Identity Service (Ids) , follow the installation procedure in the Install Voice
                                             				OS based Application and select Cisco
                                             				Identity Service (Ids) in the Product
                                             				Deployment Selection page. |
| Step 3 | Convert the
                                          			 virtual machine to a golden template. |

| Note | Select the 2500 agents OVA for SCC 100 agents dedicated sub-customer deployment and 500 agents deployment (HCS for Contact Center 2000 reference
                                             and Small Contact Center 500 agent deployment).  After you deploy the OVA edit the settings and change the vCPU value to 2. |
|---|---|

| Step 1 | Create a
                                          			 virtual machine for Cisco Unified Communications Manager using the OVA. |
|---|---|
| Step 2 | To install Cisco
                                             				Unified Communications Manager , follow the installation procedure
                                          			 in the Install Voice
                                             				OS based Application and select Cisco
                                             				Unified Communications Manager in the Product
                                             				Deployment Selection page. |
| Step 3 | Convert the
                                          			 virtual machine to a golden template. |

| Note | The VMs and software components are optimized for Cisco HCS for Contact
                                                   						Center .
                                             			 You must use the OVAs for Cisco HCS for Contact
                                                   						Center . |
|---|---|

| Step 1 | Go to the Hosted Collaboration Solution for Contact Center Download Software page on Cisco.com. |
|---|---|
| Step 2 | Select the required software type. |
| Step 3 | Click Download and save the OVA file to your local
                                          			 drive. When you create VMs, select the OVA required for the application. |

| Step 1 | Launch the
                                          			 VMware vSphere client and select File > Deploy OVF
                                                				  Template . |
|---|---|
| Step 2 | Browse to the
                                          			 location on your local drive, where you have stored the OVA. Click Open to select the OVA file, click Next . |
| Step 3 | On the OVF
                                             				Template Details page, click Next . |
| Step 4 | On the Name
                                             				and Location page, in the Name field, enter the name of virtual machine, then
                                          			 click Next . Note Enter a
                                                         				  maximum of 32 characters; spaces and special characters are not allowed. | Note | Enter a
                                                         				  maximum of 32 characters; spaces and special characters are not allowed. |
| Note | Enter a
                                                         				  maximum of 32 characters; spaces and special characters are not allowed. |
| Step 5 | On the Deployment Configuration page, select the appropriate
                                          			 configuration from the drop-down list, click Next . |
| Step 6 | On the Resource Pool page, select the required resource
                                          			 pool, then click Next . Note Skip this
                                                         				  step if you do not have a resource pool allocated in the host server. | Note | Skip this
                                                         				  step if you do not have a resource pool allocated in the host server. |
| Note | Skip this
                                                         				  step if you do not have a resource pool allocated in the host server. |
| Step 7 | On the Storage page, select a data store you want to deploy
                                          			 in the new virtual machine, then click Next . |
| Step 8 | On the Disk
                                             				Format page, select Thick
                                             				provisioned Lazy Zeroed , then click Next . Note Thin
                                                         				  provision format is used for the template creation process, it is not supported
                                                         				  for production use. | Note | Thin
                                                         				  provision format is used for the template creation process, it is not supported
                                                         				  for production use. |
| Note | Thin
                                                         				  provision format is used for the template creation process, it is not supported
                                                         				  for production use. |
| Step 9 | On the Network
                                             				Mapping page, select the appropriate network from the Destination Network drop-down list, then click Next . Note For Unified Contact Center Enterprise machines, confirm that Network Mapping page is correct: Public
                                                               						to Visible Network Private
                                                               						to Private Network | Note | For Unified Contact Center Enterprise machines, confirm that Network Mapping page is correct: Public
                                                               						to Visible Network Private
                                                               						to Private Network |
| Note | For Unified Contact Center Enterprise machines, confirm that Network Mapping page is correct: Public
                                                               						to Visible Network Private
                                                               						to Private Network |
| Step 10 | Click Finish . |

| Note | Enter a
                                                         				  maximum of 32 characters; spaces and special characters are not allowed. |
|---|---|

| Note | Skip this
                                                         				  step if you do not have a resource pool allocated in the host server. |
|---|---|

| Note | Thin
                                                         				  provision format is used for the template creation process, it is not supported
                                                         				  for production use. |
|---|---|

| Note | For Unified Contact Center Enterprise machines, confirm that Network Mapping page is correct: Public
                                                               						to Visible Network Private
                                                               						to Private Network |
|---|---|

| Step 1 | Right-click
                                          			 the virtual machine in the vSphere client and select Edit
                                             				virtual machine settings . |
|---|---|
| Step 2 | Click Hardware and select CD/DVD
                                             				Drive 1 . |
| Step 3 | Select Client Device and click OK . |

| Note | Deploying VM with Guest Operating System ‘Microsoft Windows Server 2019’ on ESXi 7.0 using CCE OVA template displays a warning
                                             message “The configured guest OS (Microsoft Windows Server 2016 or later (64-bit)) for this virtual machine does not match
                                             the guest that is currently running (Microsoft Windows Server 2019 (64-bit)). You should specify the correct guest OS to allow
                                             for guest-specific optimization”. This warning message is informational only and has no detrimental effect on the system.
                                             This warning message is displayed only once and can be dismissed. |
|---|---|

| Note | Before installing 12.5(1) ICM on SQL Server 2019 , make sure to install ODBC Driver 13 for SQL Server® manually. |
|---|---|

| Step 1 | Mount the Microsoft Windows Server ISO image to the virtual machine. Check the Connect at power on check box when mounting the ISO. |
|---|---|
| Step 2 | Power on the VM. |
| Step 3 | Enter the Language, Time and Currency Format, and Keyboard settings. Click Next . |
| Step 4 | Click Install Now . |
| Step 5 | If prompted, enter the product key for Windows Server and click Next . |
| Step 6 | Select the Desktop Experience option for the Windows Server and click Next . |
| Step 7 | Accept the license terms and click Next . |
| Step 8 | Select Custom: Install Windows only (advanced) , select Drive 0 to install Microsoft Windows Server, and then click Next . The installation begins. After the installation is complete, the system restarts without prompting. |
| Step 9 | Enter and confirm the password for the administrator account, and then click Finish . |
| Step 10 | Enable Remote Desktop connections as follows: Navigate to Control Panel > System and Security > System . Click Remote Settings . Click the Remote tab. Select the Allow remote connections to this computer radio button. The Remote Desktop Connection dialog displays a notification that the Remote Desktop Firewall exception is
                                                enabled. Click OK . |
| Step 11 | Open the Network and Sharing Center , and in the View
                                          					your basic network info and set up connections section, click Ethernet . |
| Step 12 | In the Ethernet Status window, click Properties . |
| Step 13 | In the Ethernet Properties dialog box, configure the network settings and the Domain Name System (DNS) data: Uncheck Internet Protocol Version 6 (TCP/IPv6) . Select Internet Protocol Version 4 (TCP/IPv4) and click Properties . Select Use the following IP Address . Enter the IP address, subnet mask, and default gateway. Select Use the following DNS Server Address . Enter the preferred DNS server address, and click OK . |
| Step 14 | Navigate to Control Panel > System and Security > System . Follow the instructions: Click Change Settings . In Computer name tab, click Change . Change the name of the computer from the name randomly generated during Microsoft Windows Server installation. The name does
                                                not contain underscores or spaces. Select Domain radio button to change the member from Workgroup to Domain. Enter qualified domain name and click OK . In the Windows security dialog, validate the domain credentials and click OK . On successful authentication, click OK . Reboot the server and sign in with domain credentials. Restart your system for the change to take effect. |

| Note | If you want to install Unified CCE on
                                             					a multilingual version of Windows Server, refer to Microsoft documentation for
                                             					details in installing Microsoft Windows Server Multilingual language packs. If Unified CCE language pack is applied on Chinese Windows OS machine, set the
                                             					screen resolution to 1600 x 1200. |
|---|---|

| Step 1 | From the vSphere Client, right-click the virtual machine, select Power , and click Power On . |
|---|---|
| Step 2 | Click the Summary tab. In the General section, the VMware Tools field indicates whether VMware Tools are: installed and current installed and not current not installed |
| Step 3 | Click the Console tab to make sure that the guest operating system starts successfully. Log in if prompted. |
| Step 4 | Right-click the virtual machine, select Guest OS , and
                                          					then click Install/Upgrade VMware Tools . The Install/Upgrade VMware Tools window appears with the
                                          					option - Interactive Tools Upgrade and Automatic Tools Upgrade. To install/upgrade the VMware tools manually, select the Interactive Tools Upgrade option, and click OK . Follow the on-screen instructions to
                                                							install/upgrade the VMware tools, and restart the virtual machine when
                                                							prompted. To install/upgrade the VMware tools automatically, select the Automatic Tools Upgrade option, and click OK . This process takes a few minutes to
                                                							complete, and restart the virtual machine when prompted. |

| Important | Update antivirus software, manually - do not enable automatic updates. |
|---|---|

| Tip | To allow required access to installation program files or folders, perform file-blocking exclusions in the antivirus product
                                             file-and-folder protection rules. To do this in McAfee VirusScan: Launch the VirusScan console. Right-click Access Protection , then select Properties . In the Anti-virus Standard Protection category, make sure that the Prevent IRC communication check box is unchecked in the Block column. |
|---|---|

| Important | HCS for CC for Contact Center supports Symantec Endpoint Protection. Be aware that in the firewall component of Symantec Endpoint Protection 12.1, the Network Threat Protection feature, must
                                             be disabled. If it remains enabled, which is the default, both sides of the duplexed router shows up in simplex mode, thus
                                             blocking communications between each side of the router. This blocking impacts all deployment types. If you retain the default (enabled) start services on side A and B of the router, a Symantec message pops up in the system
                                             tray indicating: The client will block traffic from IP address [side A router address] for the next 600 seconds(s). This message
                                             also appears in the client management security log. The Symantec Network Threat Protection traffic log indicates that a default
                                             firewall rule called “Block_all” was dynamically enabled. The result in both sides of the router come up in simplex mode. To avoid the issue, you must disable the Symantec firewall and restart both sides of the router. To do this, double click the Symantec icon in the system tray and select Change Settings . Then configure settings for Network Threat Protection and uncheck the Enable Firewall check box at the top of the Firewall tab. |
|---|---|

| Note | Exclude the following folders from on-access scanning configuration of the AV program for all Antivirus scans: c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA It is the customer's responsibility to deploy the VXML applications after the Antivirus scans. This also applies to the custom java/jar/class files deployed in the shared path. For more information on the Virus Scan guidelines, refer to the following sections of the UCCE documentation: The Virus Protection section of UCCE Design Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . The General Antivirus Guidelines section of the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
|---|---|

| Note | Microsoft SQL Server
                                             					does not contain SQL Server Management Studio in the default toolkit. To rerun
                                             					the SQL Server setup to install Management Studio, navigate to: SQL Selection Center > Installation > Install SQL Server Management Tools . If your computer has no internet connection, download and
                                             					install SQL Server Management Studio manually. VC++ 2017 build#
                                                						14.12.25810 is not compatible with the Cisco Contact Center
                                             					Enterprise, ensure that it is not installed. |
|---|---|

| Step 1 | Mount the Microsoft SQL Server ISO image to the virtual machine. For more
                                             						information, see Mount ISO Files . |
|---|---|
| Step 2 | Select Installation in the left pane and then click New SQL Server stand-alone installation or add
                                             						features to an existing installation . Click OK . |
| Step 3 | On the Product Key page, enter the product key and then
                                          					click Next . |
| Step 4 | Accept the License Terms and then click Next . |
| Step 5 | Optional: On the Microsoft Update page, check the Use Microsoft Update to check for updates check box,
                                          					and then click Next . Note If you do not check the Use Microsoft Update to check for
                                                            								updates option, click Next on the Product Updates page. | Note | If you do not check the Use Microsoft Update to check for
                                                            								updates option, click Next on the Product Updates page. |
| Note | If you do not check the Use Microsoft Update to check for
                                                            								updates option, click Next on the Product Updates page. |
| Step 6 | On the Install Rules page, click Next . In this step, the installation program checks to see that your system meets
                                             						the hardware and software requirements. If there are any issues, warnings or
                                             						errors appear in the Status column. Click the links
                                             						for more information about the issues. |
| Step 7 | On the Feature Selection page, select only the following,
                                          					and click Next : Database Engine Services Client Tools Connectivity Client Tools Backwards Compatibility Client Tools SDK SQL Client Connectivity SDK |
| Step 8 | On the Instance Configuration page, select Default Instance and click Next. |
| Step 9 | On the Server Configuration page, click the Services Account tab. Associate the SQL services with the virtual account. For the SQL Server Database Engine, in the Account Name
                                                         										field, select NT
                                                            										Service\MSSQLSERVER . Note While you can use the Network or Local Services account instead
                                                               									of the Virtual account, using the Virtual account provides
                                                               									security. For the remaining services, accept the default values. In the Start Up Type column, for the SQL Server Agent service account,
                                                							select Automatic from the list. Enable Grant Perform Volume Maintenance Task privilege to
                                                   								SQL Server Database Engine Service . Note Unified ICM Installer automatically enables the Grant Perform Volume Maintenance Task for the NT service account.If it is not enabled automatically then you must enable Grant Perform Volume Maintenance Task privilege to SQL Server Database Engine Service manually on the SQL server. | Note | While you can use the Network or Local Services account instead
                                                               									of the Virtual account, using the Virtual account provides
                                                               									security. | Note | Unified ICM Installer automatically enables the Grant Perform Volume Maintenance Task for the NT service account.If it is not enabled automatically then you must enable Grant Perform Volume Maintenance Task privilege to SQL Server Database Engine Service manually on the SQL server. |
| Note | While you can use the Network or Local Services account instead
                                                               									of the Virtual account, using the Virtual account provides
                                                               									security. |
| Note | Unified ICM Installer automatically enables the Grant Perform Volume Maintenance Task for the NT service account.If it is not enabled automatically then you must enable Grant Perform Volume Maintenance Task privilege to SQL Server Database Engine Service manually on the SQL server. |
| Step 10 | On the Server Configuration page, click the Collation tab. In the Database Engine section, click Customize . Select the Windows Collation designator and sort
                                                   								order radio button. Select the appropriate collation. Typically, you choose the SQL
                                                							Server collation that supports the Windows system locale most
                                                							commonly used by your organization; for example, "Latin1_General" for
                                                							English. The database entry is related to the collation that you select. For
                                                   								example, if you set the collation for Latin1_General, but you select
                                                   								Chinese language at sign-in. When you enter field values in Chinese,
                                                   								the application displays the unsupported
                                                      									character error, because the database does not
                                                   								support the characters. Important It is critical to select the correct collation setting for the
                                                               									language display on your system. If you do not select the
                                                               									correct collation during installation, you must uninstall and
                                                               									reinstall Microsoft SQL Server. Check the Binary check box. Click OK , and then click Next . | Important | It is critical to select the correct collation setting for the
                                                               									language display on your system. If you do not select the
                                                               									correct collation during installation, you must uninstall and
                                                               									reinstall Microsoft SQL Server. |
| Important | It is critical to select the correct collation setting for the
                                                               									language display on your system. If you do not select the
                                                               									correct collation during installation, you must uninstall and
                                                               									reinstall Microsoft SQL Server. |
| Step 11 | On the Database Engine Configuration page: On the Server Configuration tab, click the Mixed
                                                   								Mode radio button. Enter the password for the SQL Server system administrator
                                                							account, and confirm by reentering it. Click Add Current User to add the user who is
                                                							installing the SQL Server as an administrator. On the TempDB tab, set the Initial
                                                   								size and Autogrowth for Rogger,
                                                							Logger, AW-HDS-DDS, AW-HDS, and HDS-DDS. For information about values
                                                							for respective components Increase Database and Log File Size for TempDB . For more information about the SQL Server TempDB Database and its
                                                   								use, see the Microsoft SQL Server documentation. On the MaxDOP tab, choose the value of MaxDOP as half the value of logical CPU cores detected on the computer which is displayed just above the MaxDOP configuration. For
                                                example, if the logical CPU cores are detected as 4, then MaxDOP should be configured as 2. Note SQL Server installation automatically recommends the MaxDOP server configuration based on the number of processors available.
                                                               This feature is introduced in SQL Server 2019 and later. In SQL Server 2017, you can configure MaxDOP post installation. To
                                                               configure MaxDOP, do the following: In Object Explorer , right-click the database instance and select Properties . Select Advanced . In the Max Degree of Parallelism box, configure the number of processors as recommended above. Click Next . | Note | SQL Server installation automatically recommends the MaxDOP server configuration based on the number of processors available.
                                                               This feature is introduced in SQL Server 2019 and later. In SQL Server 2017, you can configure MaxDOP post installation. To
                                                               configure MaxDOP, do the following: In Object Explorer , right-click the database instance and select Properties . Select Advanced . In the Max Degree of Parallelism box, configure the number of processors as recommended above. |
| Note | SQL Server installation automatically recommends the MaxDOP server configuration based on the number of processors available.
                                                               This feature is introduced in SQL Server 2019 and later. In SQL Server 2017, you can configure MaxDOP post installation. To
                                                               configure MaxDOP, do the following: In Object Explorer , right-click the database instance and select Properties . Select Advanced . In the Max Degree of Parallelism box, configure the number of processors as recommended above. |
| Step 12 | On the Ready to Install page, click Install . |
| Step 13 | On the Complete page, click Close . |
| Step 14 | Enable Named Pipes and set the sort order as follows: Open the SQL Server Configuration Manager. In the left pane, navigate to SQL Native Client 11.0
                                                   								Configuration (32bit) > Client
                                                   								Protocols . In the right pane, confirm that Named Pipes is Enabled . Right-click Client Protocols and select Properties . In the Enabled Protocols section of the Client Protocols Properties window, use the
                                                							arrow buttons to arrange the protocols in the following order: Named Pipes TCP/IP Check the Enable Shared Memory Protocol and then
                                                							click OK . In the left pane, navigate to SQL Server Network
                                                   								Configuration > Protocols for
                                                   								MSSQLSERVER . In the right pane, right-click Named Pipes and
                                                							select Enable . Note By default, Microsoft SQL Server dynamically resizes its memory. The SQL
                                                         							Server reserves the memory based on process demand. The SQL Server frees
                                                         							its memory when other processes request it, and it raises alerts about
                                                         							the memory monitoring tool. Cisco supports the Microsoft validation to dynamically manage the SQL
                                                         							Server memory. If your solution raises too many memory alerts, you can
                                                         							manually limit SQL Server’s memory usage. Set the maximum and minimum
                                                         							limit of the SQL memory using the maximum memory
                                                            								usage settings in the SQL Server
                                                            								Properties menu. For more information about the SQL Server memory settings and its use,
                                                         							see the Microsoft SQL Server documentation. | Note | By default, Microsoft SQL Server dynamically resizes its memory. The SQL
                                                         							Server reserves the memory based on process demand. The SQL Server frees
                                                         							its memory when other processes request it, and it raises alerts about
                                                         							the memory monitoring tool. Cisco supports the Microsoft validation to dynamically manage the SQL
                                                         							Server memory. If your solution raises too many memory alerts, you can
                                                         							manually limit SQL Server’s memory usage. Set the maximum and minimum
                                                         							limit of the SQL memory using the maximum memory
                                                            								usage settings in the SQL Server
                                                            								Properties menu. For more information about the SQL Server memory settings and its use,
                                                         							see the Microsoft SQL Server documentation. |
| Note | By default, Microsoft SQL Server dynamically resizes its memory. The SQL
                                                         							Server reserves the memory based on process demand. The SQL Server frees
                                                         							its memory when other processes request it, and it raises alerts about
                                                         							the memory monitoring tool. Cisco supports the Microsoft validation to dynamically manage the SQL
                                                         							Server memory. If your solution raises too many memory alerts, you can
                                                         							manually limit SQL Server’s memory usage. Set the maximum and minimum
                                                         							limit of the SQL memory using the maximum memory
                                                            								usage settings in the SQL Server
                                                            								Properties menu. For more information about the SQL Server memory settings and its use,
                                                         							see the Microsoft SQL Server documentation. |
| Step 15 | Set the SQL Server's default language to English as follows: Launch SQL Server Management Studio. In the left pane, right-click the server and select Properties . Click Advanced . In the Miscellaneous section, set the Default Language to English . Click OK . Important Set the SQL Server default language to English because Cisco
                                                         							Unified Contact Center Enterprise requires a US date format (MDY). Many
                                                         							European languages use the European date format (DMY) instead. This
                                                         							mismatch causes queries such as select * from table where date =
                                                            								'2012-04-08 00:00:00' to return data for the wrong date.
                                                         							Handle localization in the client application, such as Cisco Unified
                                                         							Intelligence Center. | Important | Set the SQL Server default language to English because Cisco
                                                         							Unified Contact Center Enterprise requires a US date format (MDY). Many
                                                         							European languages use the European date format (DMY) instead. This
                                                         							mismatch causes queries such as select * from table where date =
                                                            								'2012-04-08 00:00:00' to return data for the wrong date.
                                                         							Handle localization in the client application, such as Cisco Unified
                                                         							Intelligence Center. |
| Important | Set the SQL Server default language to English because Cisco
                                                         							Unified Contact Center Enterprise requires a US date format (MDY). Many
                                                         							European languages use the European date format (DMY) instead. This
                                                         							mismatch causes queries such as select * from table where date =
                                                            								'2012-04-08 00:00:00' to return data for the wrong date.
                                                         							Handle localization in the client application, such as Cisco Unified
                                                         							Intelligence Center. |
| Step 16 | Restart the SQL Server service as follows: Navigate to the Windows Services tool. Right-click SQL Server (MSSQLSERVER) and click Stop . Right-click SQL Server (MSSQLSERVER) and click Start . |
| Step 17 | Ensure that the SQL Server Browser is started, as follows: Navigate to the Windows Services tool. Navigate to the SQL Server Browser. Right-click to open the Properties window. Enable the service, change the startup type to Automatic , and click Apply . To start the service, click Start , and then
                                                							click OK . |

| Note | If you do not check the Use Microsoft Update to check for
                                                            								updates option, click Next on the Product Updates page. |
|---|---|

| Note | While you can use the Network or Local Services account instead
                                                               									of the Virtual account, using the Virtual account provides
                                                               									security. |
|---|---|

| Note | Unified ICM Installer automatically enables the Grant Perform Volume Maintenance Task for the NT service account.If it is not enabled automatically then you must enable Grant Perform Volume Maintenance Task privilege to SQL Server Database Engine Service manually on the SQL server. |
|---|---|

| Important | It is critical to select the correct collation setting for the
                                                               									language display on your system. If you do not select the
                                                               									correct collation during installation, you must uninstall and
                                                               									reinstall Microsoft SQL Server. |
|---|---|

| Note | SQL Server installation automatically recommends the MaxDOP server configuration based on the number of processors available.
                                                               This feature is introduced in SQL Server 2019 and later. In SQL Server 2017, you can configure MaxDOP post installation. To
                                                               configure MaxDOP, do the following: In Object Explorer , right-click the database instance and select Properties . Select Advanced . In the Max Degree of Parallelism box, configure the number of processors as recommended above. |
|---|---|

| Note | By default, Microsoft SQL Server dynamically resizes its memory. The SQL
                                                         							Server reserves the memory based on process demand. The SQL Server frees
                                                         							its memory when other processes request it, and it raises alerts about
                                                         							the memory monitoring tool. Cisco supports the Microsoft validation to dynamically manage the SQL
                                                         							Server memory. If your solution raises too many memory alerts, you can
                                                         							manually limit SQL Server’s memory usage. Set the maximum and minimum
                                                         							limit of the SQL memory using the maximum memory
                                                            								usage settings in the SQL Server
                                                            								Properties menu. For more information about the SQL Server memory settings and its use,
                                                         							see the Microsoft SQL Server documentation. |
|---|---|

| Important | Set the SQL Server default language to English because Cisco
                                                         							Unified Contact Center Enterprise requires a US date format (MDY). Many
                                                         							European languages use the European date format (DMY) instead. This
                                                         							mismatch causes queries such as select * from table where date =
                                                            								'2012-04-08 00:00:00' to return data for the wrong date.
                                                         							Handle localization in the client application, such as Cisco Unified
                                                         							Intelligence Center. |
|---|---|

| Note | Before installing 12.5(1) ICM on SQL Server
                                             					2019, make sure to install ODBC Driver 13 for SQL Server® manually. |
|---|---|

| Caution | Do not change the SQL port number. Retain the default port numbers
                                          				as 1433 for TCP and 1434 for UDP connections. In case you change the port numbers,
                                          				the applications like CCEAdmin will not work. |
|---|---|

| CCE Component | vCPU | TempDB Data Files | TempDB Transaction Log File |
|---|---|---|---|
| Number of Files | Initial Size | Autogrowth | Initial Size | Autogrowth |
| Rogger | 4 | 4 | 800MB | 100MB | 600MB | 10MB |
| Logger | 4 | 4 | 800MB | 100MB | 600MB | 10MB |
| AW-HDS-DDS | 4 | 4 | 800MB | 100MB | 600MB | 10MB |
| AW-HDS | 8 | 8 | 400MB | 100MB | 600MB | 10MB |
| HDS-DDS | 8 | 8 | 400MB | 100MB | 600MB | 10MB |

| Note | VMware uses the term Template .
                                             			 HCS for Contact Center uses the term Golden
                                                				Template for templates consisting of application and operating systems that
                                             			 are used for HCS for Contact Center. |
|---|---|

| Step 1 | If the VM is not
                                          			 already powered off, from the VM menu, select Power > Shut down the
                                                				  guest . |
|---|---|
| Step 2 | From the VMware
                                          			 vCenter Inventory menu, right-click the virtual machine and
                                          			 choose Template > Convert to
                                                				  Template . |

| Step 1 | Install OpenSSL on Microsoft Windows. |
|---|---|
| Step 2 | Add the OpenSSL installation path to System variables in the Environment Variables of the system. |
| Step 3 | Add the downloaded ISO Image , ISO Image signature file  and the Public key.der file in the same folder for the specific
                                          product component. |
| Step 4 | Launch Command Prompt on the system. |
| Step 5 | Run the following CLI (Command Line Interface) command to verify the files: openssl dgst -sha512 -keyform der -verify <PUBLIC key.der>
                                                -signature <ISO Image.iso.signature <ISO Image The system displays Verified OK on successful verification and Verification failed on verification failure. Note If the verification fails do not proceed with the installation, contact
                                                         Cisco Support for a valid ISO . | Note | If the verification fails do not proceed with the installation, contact
                                                         Cisco Support for a valid ISO . |
| Note | If the verification fails do not proceed with the installation, contact
                                                         Cisco Support for a valid ISO . |

| Note | If the verification fails do not proceed with the installation, contact
                                                         Cisco Support for a valid ISO . |
|---|---|