---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-install-12-5-1su5-cucm-b-install-guide-cucm-imp-1251su5-cucm-b-install--8bd223ef68
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/install/12_5_1SU5/cucm_b_install-guide-cucm-imp-1251su5/cucm_b_install-guide-cucm-imp-14_chapter_010.html
retrieved_at: 2026-08-17T00:07:54.347899+00:00
---

Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU5

# Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU5

Updated: January 17, 2025

Chapter: Installation Tasks

## Chapter: Installation Tasks

# Installation Tasks

## Installation Task Flows

Choose one of the following installation task flows:

Task Flow

Description

Cluster Installs

Basic Installation Task Flow

Use this method for basic installs of any of the following deployments:

Cisco Unified Communications Manager telephony cluster installs

Standard Deployments (Decentralized) for IM and Presence

Install IM and Presence Central Cluster (Basic Installation)

For Centralized Deployments of IM and Presence, use this task flow for basic installs of the IM and Presence central cluster.

Touchless Installation Task Flow

Use this task flow to install a Unified Communications Manager or IM and Presence Service cluster dynamically without the
                                          need for manual intervention. Applies to either Centralized or Standard (Decentralized) IM and Presence deployments.

Install with Data Import

Complete this tasks to install a Unified Communications Manager or IM and Presence Service cluster using the Install with Data Import .

Node Installs

Add a New Node to an Existing Cluster

Complete these tasks if you want to add a node to an existing Unified Communications Manager or IM and Presence Service cluster.

You can also use Cisco Prime Collaboration Deployment to install your cluster. For motr information, see Cisco Prime Collaboration Deployment Administration Guide .

## Installation Task Flows

Choose one of the following installation task flows:

Task Flow

Description

Cluster Installs

Basic Installation Task Flow

Use this method for basic installs of any of the following deployments:

Cisco Unified Communications Manager telephony cluster installs

Standard Deployments (Decentralized) for IM and Presence

Install IM and Presence Central Cluster (Basic Installation)

For Centralized Deployments of IM and Presence, use this task flow for basic installs of the IM and Presence central cluster.

Touchless Installation Task Flow

Use this task flow to install a Unified Communications Manager or IM and Presence Service cluster dynamically without the
                                          need for manual intervention. Applies to either Centralized or Standard (Decentralized) IM and Presence deployments.

Install with Data Import

Complete this tasks to install a Unified Communications Manager or IM and Presence Service cluster using the Install with Data Import .

Node Installs

Add a New Node to an Existing Cluster

Complete these tasks if you want to add a node to an existing Unified Communications Manager or IM and Presence Service cluster.

You can also use Cisco Prime Collaboration Deployment to install your cluster. For motr information, see Cisco Prime Collaboration Deployment Administration Guide .

### Before You Begin

Before you begin
                                 		  the installation, review the following information:

Make sure that
                                       				the subscriber nodes that you are installing can connect to the publisher node
                                       				server during the installation.

Make sure that all Unified Communications Manager servers in a cluster have the same software version. Make sure that all IM and Presence servers in a cluster have the same version of the released software. The only exception is during a cluster software upgrade,
                                       during which a temporary mismatch is allowed. If you are installing IM and Presence nodes, Unified Communications Manager and IM and Presence Service software versions must have the same major and minor release number.

If you are installing on an existing cluster, do not attempt
                                       				to perform any configuration tasks during the installation.

Be aware that
                                       				directory names and filenames that you enter while you are running the
                                       				installation program are case-sensitive.

For IM and Presence Service installations, make sure that you know whether you are installing IM and Presence Service in a
                                       Centralized Deployment or in a Standard Deployment (Decentralized). For details, see Cluster Topology for IM and Presence .

### Installation
                           	 Wizard

The following table provides instructions on how to navigate within the installation wizard.

To Do This

Press This

Move to the
                                             					 next field

Tab

Move to the
                                             					 previous field

Alt-Tab

Choose an
                                             					 option

Space bar or
                                             					 Enter

Scroll up or
                                             					 down in a list

Up or down
                                             					 arrow

Go to the
                                             					 previous window

Space bar or
                                             					 Enter to choose Back (when available)

Get help
                                             					 information on a window

Space bar or
                                             					 Enter to choose Help (when available)

The installation wizard supports the following characters:

alphanumeric: A-Z, a-z, and 0-9- spaces

spaces and # (except as the first character)

only the following special characters: \.,-_:;{}()[]

## Basic Installation Task Flow

Complete the following tasks to install Unified Communications Manager and IM and Presence Service cluster using the basic
                              installation process:

Installs of a Cisco Unified Communications Manager telephony cluster

Installs of the IM and Presence Service in a Standard Deployment (Decentralized).

Depending on your installation scenario, you may not need to perform all of the tasks. For example, if you are installing
                                          the IM and Presence Service on an existing Unified Communications Manager cluster that is already in use, you only need to
                                          complete the tasks for installing the IM and Presence Service.

### Before You Begin

Preinstall Tasks for Unified Communications Manager

Preinstall Tasks for the IM and Presence Service

Cisco Unified Communications Manager

IM and Presence Service

Description

Step 1

Basic Installation

—

Begin the install process for Unified Communications Manager.

Step 2

Enter Configuration Information for Preinstalled Servers

—

Pre-installed servers only (e.g., Cisco Business Edition). Add pre-configured information to the installation.  Otherwise,
                                          skip this task.

Step 3

Optional. Complete either of the following tasks:

Upgrade Install Image from Local Source

Upgrade Install Image from Remote Server

—

Upgrade your install image to a newer version. This optional task is available for Unified Communications Manager installs
                                          only.

Step 4

Configure Basic Installation

—

Continue with the Basic Installation process by configuring your installation.

Step 5

Configure the Unified Communications Manager Publisher

—

Configure and install software on the publisher node.

Step 6

Add Subscriber Nodes

—

Add subscriber nodes to the publisher node.

Step 7

Install Subscriber Nodes

—

Install software on your Cisco Unified Communications Manager subscriber nodes.

Step 8

—

Basic Installation

Begin the install process for the IM and Presence Service.

Step 9

—

Enter Configuration Information for Preinstalled Servers

Pre-installed servers only (e.g., Cisco Business Edition). Add pre-configured information to the installation.  Otherwise,
                                          skip this task.

Step 10

—

Configure Basic Installation

Continue Basic Install process for IM and Presence by configuring the installation.

Step 11

—

Configure the IM and Presence Publisher

Configure and complete the installation for the IM and Presence database publisher node.

Step 12

Add Subscriber Nodes

—

On the Cisco Unified Communications Manager publisher node, add IM and Presence subscribers.

Step 13

—

Install Subscriber Nodes

Install software on your IM and Presence Service subscriber nodes.

## Install IM and Presence Central Cluster (Basic Installation)

Complete these tasks to install an IM and Presence Service Centralized Deployment using Basic Installation.

Unified CM Publisher (non-telephony)—The IM and Presence central cluster requires a local Unified Communications Manager publisher
                                    node within the central cluster for database and user provisioning. This node does not handle telephony. There is no need
                                    to install subscriber nodes.

IM and Presence Central Cluster

Unified CM Publisher (non-telephony)

IM and Presence Central Cluster

Description

Step 1

Basic Installation

Begin the install process for the Unified CM publisher node.

Step 2

Configure Basic Installation

Configure the Basic Installation.

Step 3

Configure the Unified Communications Manager Publisher

Configure the Unified CM publisher node.

Step 4

Basic Installation

Begin the install process for the IM and Presence central cluster.

Step 5

Configure Basic Installation

Continue with the Basic Install process for IM and Presence by continuing the installation.

Step 6

Configure the IM and Presence Publisher

Configure the IM and Presence database publisher node.

Step 7

Add Subscriber Nodes

On the Unified CM publisher, add IM and Presence subsciber nodes.

Step 8

Install Subscriber Nodes

Complete the installation on the IM and Presence subsicribers.

### Basic Installation

Use this procedure for Unified Communications Manager and IM and Presence Service installations to begin the basic installation
                                 process. You can use this procedure if you are installing a cluster or adding a node to an existing cluster.

Step 1

If you are using a configuration file created by the Answer File Generator, ensure that the virtual floppy image is in a location
                                          where the virtual machine can access it.

Step 2

Perform one of the following:

- If you are installing from a DVD drive located on a VMware ESXi server host, insert the installation DVD into the tray and
                                             restart the virtual machine, so that it boots from the DVD.

- If you are installing from a data store ISO file located on the local ESXi host or on a storage area network (SAN), edit the
                                             CD or DVD drive on the virtual machine to select the data store ISO file. Select the option to connect at power on, and restart
                                             the virtual machine. If you have configured the virtual machine to use the ISO at the same time that you created the virtual
                                             machine using the OVA file, skip this step and complete the rest of the procedure.

Step 3

Click Yes to perform the media check. Or click No to skip the media check.

The media check verifies the integrity of the DVD. If the DVD has passed the media check previously, choose to skip the media
                                             check.

Step 4

If you click Yes to perform the media check, the Media Check Result window displays.

If the Media Check Result displays Pass , click OK to continue the installation.

If the media check fails, either download another copy from cisco.com or obtain another DVD directly from Cisco.

Step 5

In the Product
                                             				Deployment Selection window, specify which product you want to install:

- Unified Communications Manager —Choose the product and click OK .

- IM and
                                                				  Presence Service —Select OK .

- Cisco Unity Connection —Select the product and click OK .

The window displays the products that are supported and not supported by your hardware. If only one product is supported,
                                                         you do not choose which product to install.

Step 6

If the software is currently installed on the server, the Overwrite Hard Drive window opens and displays the current software version on your hard drive, DVD or ISO file. Click Yes to continue with the installation or No to cancel.

Caution

If you choose to continue with the installation, all existing data on your hard drive gets overwritten and destroyed.

The Platform Installation Wizard window displays.

Step 7

In the Platform Installation Wizard window, choose one of
                                          			 the following options:

- To continue with the basic installation process, choose Proceed and continue. Allows you to configure the basic installation process. Use this installation method first-time setup or during
                                             restore from backup.

- To continue with Install with Data Import , choose Import . Use this installation method for direct migrations (Fresh Install with Data Import) from the older versions of Unified Communications
                                             Manager or IM and Presence Service.

- If you have a preinstalled server (for example, a Cisco Business Edition server), configure the pre-installed software. Click Skip and go to Enter Configuration Information for Preinstalled Servers .

- If you want to install the software first and then configure it later, click Skip . The installation process installs the software and then prompts you to configure it after the installation is complete.
                                             This method may increase the total time for the installation.

Step 8

In the Apply Additional Release window, if you have a newer Unified Communications Manager version than your install image, you can elect to upgrade the installation to the newer release. This option is not available
                                          for the IM and Presence Service.

Upgrade Install Image from Local Source

Upgrade Install Image from Remote Server

- No —Choose this option if you are installing the IM and Presence Service or if you are installing Unified Communications Manager and you do not want to upgrade the installed image.

Step 9

In the Basic Install window, click Continue to install the software or configure the pre-installed software.

#### What to do next

For pre-installed servers, Enter Configuration Information for Preinstalled Servers .

To upgrade the Unified Communications Manager install image to a later release, perform any of the following procedures:

Upgrade Install Image from Local Source

Upgrade Install Image from Remote Server

To continue the basic install process, Configure Basic Installation

### Enter Configuration Information for Preinstalled Servers

Use this procedure if you have a server with the product pre-installed (for example, a Cisco Business Edition appliance).
                                 You can use a USB key or AFG file to enter your server's pre-configured information.

#### Before you begin

Basic Installation

Step 1

After the system
                                          			 restarts, the Preexisting Installation Configuration window
                                          			 displays.

Step 2

If you have preexisting configuration information that the Answer File Generator created, that is stored on a USB key. Insert
                                          the USB key and choose Continue . The installation wizard reads the configuration information during the installation process.

If a popup window states that the system detected new hardware, press any key and then choose Install from the next window.

Step 3

In
                                          			 the Platform
                                             				Installation Wizard window, choose Proceed .

Step 4

In the Apply Additional Release window, you can choose the option to upgrade Unified Communications Manager install file to a newer release. This option
                                          is not available for the IM and Presence Service.

- > Upgrade Install Image from Local Source

- > Upgrade Install Image from Remote Server

- No —Choose this option if you are installing the IM and Presence Service or installing Unified Communications Manager and you do not want to upgrade the install image.

Step 5

In the Basic
                                             				Install window, choose Continue .

#### What to do next

To upgrade the Unified Communications Manager install image to a newer release, perform any of the following procedures:

Upgrade Install Image from Local Source

Upgrade Install Image from Remote Server

Otherwise, to continue the basic install process, Configure Basic Installation

### Upgrade Install Image from Local Source

Use this optional procedure for Unified Communications Manager installations if you have a newer version than your installation
                                 image and you want to upgrade your installation file to a newer version. This option is available for Unified Communications
                                 Manager installs only.

If you have placed your upgrade file on an FTP or SFTP server, refer to Upgrade Install Image from Remote Server .

#### Before you begin

Make sure to do the following:

To complete this procedure, you must have completed the Start Basic Installation procedure and have chosen to apply a patch
                                             via a LOCAL source.

Start a basic installation. Choose the option to apply apatch via a LOCAL source. For details, see

Download the appropriate patch file from Cisco.com. You must create an ISO image from the upgrade file and then either place
                                       it on a DVD or in the DVD drive of a virtual machine.

Step 1

When the Local
                                             				Patch Configuration window displays, enter the patch directory and
                                          			 patch name, if required, and choose OK.

The Install Upgrade Patch Selection Validation window displays.

Step 2

The window displays the patch file. To update the system with this patch, click Continue .

Step 3

Choose the
                                          			 upgrade patch to install. The system installs the patch, then restarts the
                                          			 system with the upgraded software version running.

After the system
                                             				restarts, the Preexisting Configuration Information window
                                             				displays.

Step 4

To continue the installation, choose Proceed .

The Platform Installation Wizard window displays.

Step 5

To continue the installation, click Proceed or click Cancel to stop the installation.

If you click Proceed , the Apply Patch window displays. Continue with the next step.

If you click Cancel , the system halts, and you can safely power down the server.

Step 6

When the Apply
                                             				Patch window displays, choose No.

Step 7

The Upgrade window displays.

Step 8

Click No and perform the procedure to configure the basic installation.

#### What to do next

Configure Basic Installation

### Upgrade Install Image from Remote Server

Use this optional procedure for Unified Communications Manager installations if you have a newer version than your installation
                                 image on an FTP or SFTP server and you want to upgrade your installation file to a newer version. This option is available
                                 for Unified Communications Manager installs only.

If you have placed your upgrade file on an FTP or SFTP server, refer to Upgrade Install Image from Local Source .

Step 1

Configure the
                                          			 auto negotiation setting.

- To disable automatic
                                             				negotiation, choose No . The NIC Speed and Duplex Configuration window
                                             				displays. Continue with the next step.

Step 2

If you chose to
                                          			 disable automatic negotiation, manually choose the appropriate NIC speed and
                                          			 duplex settings now and choose OK to continue.

The MTU
                                                				  Configuration window displays.

Step 3

In the MTU
                                             				Configuration window, you can change the MTU size from the operating
                                          			 system default.

The maximum transmission unit (MTU) represents the largest packet, in bytes, that this host transmits on the network. If you
                                             are unsure of the MTU setting for your network, use the default value.

Caution

If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected.

To accept the default value (1500 bytes), choose No .

To change the MTU size from the operating system default, choose Yes , enter the new MTU size, and choose OK .

The DHCP
                                                				  Configuration window displays.

Step 4

For network
                                          			 configuration, you can choose to either set up static network IP addresses for
                                          			 the node and gateway or to use Dynamic Host Configuration Protocol (DHCP).
                                          			 Static IP addresses are recommended. If you use DHCP, use static DHCP.

If you have
                                                   					 a DHCP server that is configured in your network and want to use DHCP, choose Yes . The installation process attempts to verify
                                                   					 network connectivity.

If you want
                                                   					 to configure static IP addresses for the node, choose No . The Static Network Configuration window
                                                   					 displays.

Step 5

If you chose not
                                          			 to use DHCP, enter your static network configuration values and choose OK .

The DNS
                                                				  Client Configuration window displays.

Step 6

To enable DNS,
                                          			 choose Yes , enter your DNS client information, and choose OK .

After the system
                                             				configures the network and checks for connectivity, the Remote Patch
                                             				Configuration window displays.

Step 7

Enter the
                                          			 location and login information for the remote file server. The system connects
                                          			 to the remote server and retrieves a list of available upgrade patches.

If the upgrade file is located on a Linux or Unix server, you must enter a forward slash at the beginning of the directory
                                             path. For example, if the upgrade file is in the patches directory, you must enter /patches .

If the upgrade
                                             				file is located on a Windows server, remember that you are connecting to an FTP
                                             				or SFTP server, so use the appropriate syntax, including:

Begin the path with a forward slash (/) and use forward slashes throughout the path.

The path
                                                   					 must start from the FTP or SFTP root directory on the server, so you cannot
                                                   					 enter a Windows absolute path, which starts with a drive letter (for example,
                                                   					 C:).

The Install Upgrade Patch Selection window displays.

Step 8

Choose the
                                          			 upgrade patch to install. The system downloads, unpacks, and installs the patch
                                          			 and then restarts the system with the upgraded software version running.

After the system
                                             				restarts, the Preexisting Configuration Information window
                                             				displays.

Step 9

To continue the
                                          			 installation, choose Proceed.

The Platform Installation Wizard window displays.

Step 10

Choose Proceed or choose Cancel to stop the installation.

If you choose Proceed , the Apply Patch window displays. Continue with the next step.

If you choose Cancel , the system halts, and you can safely power down the server.

Step 11

In the Apply Patch window displays, choose No .

The Windows Upgrade window displays.

Step 12

Choose No and perform the Configure Attended Installation procedure to configure the basic installation.

#### What to do next

Configure Basic Installation

### Configure Basic Installation

Use this procedure to configure Unified Communications Manager and IM and Presence Service basic installation.

#### Before you begin

Basic Installation

Step 1

In the Timezone Configuration window, choose the appropriate
                                          			 time zone for the server and then choose OK .

The Auto Negotiation Configuration window is displayed.

Step 2

The installation
                                          			 process allows you to automatically set the speed and duplex settings of the
                                          			 Ethernet network interface card (NIC) by using automatic negotiation. You can
                                          			 change this setting after installation.

To enable
                                                   					 automatic negotiation, choose Yes .

The MTU Configuration window is displayed.

To use
                                                               						this option, your hub or Ethernet switch must support automatic negotiation.

To disable
                                                   					 automatic negotiation, choose No and continue with the next step.

The NIC Speed and Duplex Configuration window is displayed.

Step 3

If you chose to
                                          			 disable automatic negotiation, manually choose the appropriate NIC speed and
                                          			 duplex settings now and choose OK to continue.

The MTU
                                                				  Configuration window displays.

Step 4

In the MTU
                                             				Configuration window, you can change the MTU size from the operating
                                          			 system default.

The maximum
                                             				transmission unit (MTU) represents the largest packet, in bytes, that this host
                                             				will transmit on the network. If you are unsure of the MTU setting for your
                                             				network, use the default value, which is 1500 bytes.

Caution

If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected.

To accept
                                                   					 the default value (1500 bytes), choose No.

To change
                                                   					 the MTU size from the operating system default, choose Yes, enter the new MTU
                                                   					 size, and choose OK.

The DHCP
                                                				  Configuration window displays.

Step 5

For network
                                          			 configuration, you can choose to either set up a static network IP address for
                                          			 the node or to use Dynamic Host Configuration Protocol (DHCP). Static IP
                                          			 addresses are recommended. If you use DHCP, use static DHCP.

If you have a DHCP server that is configured in your network and want to use DHCP, choose Yes . The network restarts, and the Administrator Login Configuration window is displayed.

If you want
                                                   					 to configure a static IP address for the node, choose No . The Static Network Configuration window
                                                   					 displays.

Step 6

If you chose not
                                          			 to use DHCP, enter your static network configuration values and choose OK .

The DNS Client Configuration window is displayed.

Step 7

In the DNS Client Configuration window, click Yes to enable DNS and enter the DNS client information.

Step 8

Click OK and choose one of the following in the Basic Installation procedure:

Click Proceed to restart the network using the new configuration. The Administrator Login Configuration window is displayed.

Enter Administrator login User Name and Password

Make sure that the User Name contians alphanumeric characters. Use the same login cerdentials to Cisco Unified Communications Operating System Administration,
                                                            the Command Line Interface, and the Disaster Recovery System.

Enter Remote Server Name or IP, Export Data Directory, Remote Login ID, Remote Password, and Confirm Password. Click OK to restart the network using the new configuration.

Step 9

The Certificate Information window is displayed.

Step 10

In Certificate Information window, enter your certificate signing request information and click OK.

Step 11

In the First Node Configuration window, choose how you want to assign this node:

- Yes —Choose this option to assign this node as the Cisco Unified Communications Manager publisher node.

- No —Choose this option to assign this node as a Cisco Unified Communications Manager subscriber node, or as an IM and Presence
                                             Service node.

#### What to do next

If you are installing the first node in the cluster, go to one of the following procedures, depending on whether you are installing
                                 Unified Communications Manager or the IM and Presence Service.:

Configure the Unified Communications Manager Publisher

Configure the IM and Presence Publisher

Otherwise, for subscriber node installs Add Subscriber Nodes .

### Configure the Unified Communications Manager Publisher

Follow this procedure to configure the first server where you install Unified Communications Manager software as the publisher node for the cluster. Perform this procedure after you have completed the attended installation
                                 and configured the attended installation.

You can configure Smart Call Home on the publisher node only.

Step 1

The Network
                                             				Time Protocol Client Configuration window appears.

We recommend that you use an external NTP server to ensure accurate system time on the publisher node. Subscriber nodes in
                                             the cluster will get their time from the first node.

Step 2

Choose whether
                                          			 you want to configure an external NTP server or manually configure the system
                                          			 time.

To set up an external NTP server, choose Yes and enter the IP address, NTP server name, or NTP server pool name for at least one NTP server. You can configure up to five
                                                   NTP servers, and we recommend that you use at least three. Choose Proceed to continue with the installation.

The system
                                                   					 contacts an NTP server and automatically sets the time on the hardware clock.

If the Test button appears, you can choose Test to check whether the NTP servers are accessible.

To manually
                                                   					 configure the system time, choose No and enter the appropriate date and time to set
                                                   					 the hardware clock. Choose OK to continue with the installation.

The Database Access Security Configuration window
                                             				appears.

Step 3

Enter the
                                          			 Security password from Required Installation Information.

The Security
                                                         				  password must start with an alphanumeric character, be at least six characters
                                                         				  long, and can contain alphanumeric characters, hyphens, and underscores. The
                                                         				  system uses this password to authorize communications between nodes, and you
                                                         				  must ensure this password is identical on all nodes in the cluster.

The SMTP
                                                				  Host Configuration window appears.

Step 4

If you want to
                                          			 configure an SMTP server, choose Yes and enter the SMTP server name. If you do not
                                          			 want to configure the SMTP server, choose No , which redirects to Smart Call Home page. To go
                                          			 to previous page, choose Back and to see the information about the SMTP
                                          			 configuration, choose Help .

You must
                                                         				  configure an SMTP server to use certain platform features; however, you can
                                                         				  also configure an SMTP server later by using the platform GUI or the command
                                                         				  line interface.

Step 5

Choose OK .

Step 6

In the SMART Call Home Enable window, choose one of the following and click OK :

- Enable Smart Call Home on System Start

- Enable Anonymous Call Home on System Start

- Remind me Later to configure Smart Call Home —Select this option to configure the Smart Call Home feature service after installation using the Cisco Unified Serviceability
                                             interface.

- Disable All Call Home on System Start —Select this option to deactivate the Smart Call Home feature service. Please note that you can reactivate it after installation
                                             using the Cisco Unified Serviceability interface.

Step 7

If you have selected Smart Call Home on System Start , do the following:

Select the method for sending data to the Cisco Technical Assistance Center.

Secure Web (HTTPS)

Secure Web (HTTPS) through Proxy—If you select this option, enter the Hostname or IP address of the proxy server where the
                                                         Call Home info gets sent as well as the port number on which the server is enabled.

Email—If you select this option, you must have configured SMTP for any emails to be sent successfully.

To send a copy of the Call Home messages to multiple email recipients, enter the email addresses separated with a comma. You
                                                can enter up to a maximum of 1024 characters.

In the Customer Contact Details field, enter the customer's email address.

Click Continue to proceed, or select Back to return to the previous menu.

If you click Continue , a message appears as Cisco Call Home includes reporting capabilities that allow Cisco to receive diagnostic and system information from your Unified Communications Manager cluster. Cisco may use this information for proactive debugging, product development or marketing purposes. To learn more
                                                      about this feature, please visit: http://www.cisco.com/en/US/products/ps7334/serv_home.html.

If you have selected Secure Web (HTTPS) through Proxy and click Continue , the Smart Call Home Proxy Configuration window appears.

Click Confirm to proceed with normal installation or select Back to return to the Smart Call Home Enable Page.

Step 8

If you have selected Enable Anonymous Call Home on System Start , do the following:

Select the method for sending data to the Cisco Technical Assistance Center.

Secure Web (HTTPS)

Secure Web (HTTPS) through Proxy—If you select this option, enter the Hostname or IP address of the proxy server where the
                                                         Call Home info gets sent as well as the port number on which the server is enabled.

Email—If you select this option, you must have configured SMTP for any emails to be sent successfully.

To send a copy of the Call Home messages to multiple email recipients, enter the email addresses separated with a comma. You
                                                can enter up to a maximum of 1024 characters.

Click Continue to proceed, or click Back to return to the previous menu.

When you click Continue , the following message appears.

To help improve the Unified Communications Manager experience, click Confirm to allow Cisco Systems to securely receive usage
                                                      statistics from the server. This information will be used by Cisco to help understand how customers are using our product
                                                      and ultimately drive product direction. If you prefer not to participate, you may choose to opt-out.

If you have selected Secure Web (HTTPS) through Proxy and clicked Continue , the Anonymous Call Home Proxy Configuration window appears.

Click Confirm to proceed with normal installation or click Back to return to the Smart Call Home Enable Page.

If you choose Install with Data Import during basic installation the Application User Configuration window does not appear. Proceed to step 11 to complete the installation.

Step 9

Click OK . The Application User Configuration window appears.

Step 10

Enter the
                                          			 Application User name and password from and confirm the password by entering it
                                          			 again.

Step 11

Choose OK .

Step 12

Choose OK to continue with the installation or choose Back to modify the platform configuration.

The system installs and configures the software. The server reboots.

When the installation process completes, you are prompted to log in by using the Administrator account and password.

#### What to do next

If you want to install subscriber nodes, Add Subscriber Nodes .

### Configure the IM and Presence Publisher

Follow this procedure to configure the first server where you install IM and Presence Service software as the database publisher
                                 node for the IM and Presence cluster.

Step 1

Install and configure the IM and Presence database publisher node.

Step 2

Verify that the following services are running:

- Cisco SIP Proxy

- Cisco Presence Engine

- Cisco XCP Connection Manager

- Cisco XCP Authentication Service

If you need to activate services, you can do it in Cisco Unified Serviceability at Tools > Service Activation .

#### What to do next

Add Subscriber Nodes

### Add Subscriber Nodes

Before you install software on your subscriber nodes, you must add the subscriber nodes to the Unified Communications Manager
                                 publisher node. You must complete this task before installing subscriber nodes for either Unified Communications Manager or
                                 the IM and Presence Service.

Step 1

Log in to the Unified Communications Manager publisher node.

Step 2

From Cisco Unified CM Administration choose System > Server .

Step 3

Add your subscriber nodes:

Click Add New .

From the Server Type drop-down list, choose the node type that corresponds to the install that you are completing: Unified Communications Manager
                                                Voice/Video node, or IM and Presence Service node.

Enter the Fully Qualified Domain Name/IP Address field with a FQDN or IPv4 Address.

Optional. If you are deploying IPv6, enter an IPv6 Address .

Click Save .

Repeat these steps for each subscriber node that you want to add.

Step 4

(IM and Presence Service only) Add your
                                          Presence Redundancy Groups in order to define your subclusters.

From Cisco Unified CM Administration, choose System > Presence
                                                      Redundancy Groups .

Click Add New .

Enter a Name and Description for the group.

From the Server drop-down list, choose the IM and Presence Service nodes that you want to add to this group.

Click Save .

Repeat this procedure until you've created your groups. You can have up to three Presence Redundancy Groups in a cluster,
                                                with each group consisting of two IM and Presence Service nodes.

#### What to do next

Install Subscriber Nodes

### Install Subscriber Nodes

Use this procedure if you want to install subscriber nodes for Unified Communications Manager or the IM and Presence Service.

#### Before you begin

Before you install software for either Unified Communications Manager or IM and Presence Service subscriber nodes, you must
                                 add the node to the Cisco Unified Communications Manager publisher node. For details, Add Subscriber Nodes .

Step 1

If you have configured Network Time Protocol on the publisher node, ensure that it is synchronized with an NTP server before
                                          you install a subscriber node. From the Command Line Interface on the publisher node, enter utils ntp status . Ensure that the output indicates that the node is synchronized with an NTP server.

If the publisher node is not synchronized with an NTP server, installation of the subscriber node will fail.

Step 2

On the First Node Configuration window, read the Warning and make sure that you have correctly configured the first node as
                                          the publisher node. To continue with the installation of the subscriber node, click OK.

The Network Connectivity Test Configuration window displays.

Step 3

During
                                          			 installation of a subscriber node, the system checks to ensure that the
                                          			 subscriber node can connect to the publisher node.

To pause the
                                                   					 installation after the system successfully verifies network connectivity,
                                                   					 choose Yes.

To continue
                                                   					 the installation with a pause, choose No.

The First Node
                                             				Access Configuration window displays.

Step 4

Enter the
                                          			 publisher node connectivity information and choose OK.

The system
                                             				checks for network connectivity.

If you chose to
                                             				pause the system after the system successfully verifies network connectivity,
                                             				the Successful Connection to First Node window displays. Choose Continue.

If the network
                                                         				  connectivity test fails, the system always stops and allows you to go back and
                                                         				  reenter the parameter information.

The SMTP
                                                				  Host Configuration window displays.

Step 5

If you want to
                                          			 configure an SMTP server, choose Yes and enter the SMTP server name.

To use certain
                                                         				  operating system features, you must configure an SMTP server; however, you can
                                                         				  also configure an SMTP server later by using the operating system GUI or the
                                                         				  command line interface.

The Platform
                                             				Configuration Confirmation window displays.

Step 6

Choose OK to start installing the software or choose Back to change the configuration.

Step 7

When the
                                          			 installation process completes, you get prompted to log in by using the
                                          			 Administrator account and password.

#### What to do next

If you have just installed a Unified Communications Manager cluster and you want to install the IM and Presence Service on
                                 the same cluster in a standard IM and Presence deployment (as opposed to a central IM and Presence cluster deployment), return
                                 to Attended Installation in order to install the IM and Presence Service cluster.

Otherwise, proceed to the postinstallation tasks:

Postinstall Tasks for Cisco Unified Communications Manager

Postinstall tasks for the IM and Presence Service

## Touchless Installation Task Flow

Complete these tasks to install your Unified Communications Manager and IM and Presence Service node or clusters in a single
                              process via the touchless installation method.

### Before you begin

Preinstall Tasks for Unified Communications Manager

Preinstall Tasks for the IM and Presence Service

Step 1

Generate Answer Files for Touchless Install

Use this procedure to generate the configuration files (clusterconfig.xml and platformconfig.xml) with your network settings.
                                          The touchless install process uses these files to install and configure a single node or the various cluster nodes.

Step 2

Generate Virtual Floppy Images

Use this procedure to create virtual floppy images from the answer files. You use the virtual floppy images in your touchless
                                          installation.

Step 3

Upload Virtual Floppy Image to Datastore

Use this procedure to upload the virtual floppy images to the datastore.

Step 4

Mount Floppy Image to VM

Use this procedure to mount the UC application virtual floppy images on their corresponding VM.

Step 5

Run Touchless Install

Begin the single node or cluster installation. You can kick off all node installations simultaneously.

### Generate Answer Files for Touchless Install

Use this procedure to generate answer files for your touchless installation of your cluster. The answer files (clusterconfig.xml
                                 and platformconfig.xml) contain the configuration information that the install process installs and configures on each cluster
                                 node.

#### Before you begin

You must have already planned your network topology, including addresses for your Unified Communications Manager and IM and
                                 Presence Service cluster nodes.

Step 1

Log in to the Cisco Unified Communications Answer File Generator application at https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html .

Step 2

In the Hardware section, choose Virtual Machine .

Step 3

From the Product section, select the product and version that you want to install.

Step 4

In the Software Location of Data to Import section, check the Configure Software Location of Data to Import check box to configure Remote SFTP server details only if you choose to install using the Fresh Install with Data Import.
                                          Else ignore this step and proceed to step 5. For more details, see Install with Data Import installation method.

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

Check the Dynamic Cluster Config Enable check box and enter a value, in hours, for the Dynamic cluster Config Timer.

Step 8

Under Secondary Node Configuration , enter the node details for your first subscriber node and click Add Secondary Node .

Step 9

Add all your subscriber nodes.

Step 10

Add all your cluster nodes and click Generate Answer files .

Step 11

Download the answer files to your computer.

Step 12

Repeat this procedure to generate answer files for the IM and Presence Service cluster.

#### What to do next

Generate Virtual Floppy Images

### Generate Virtual Floppy Images

Use this procedure to create virtual floppy images from the answer files. You will use the virtual floppy images in your
                                 touchless installation.

This procedure describes how to use Winimage to create virtual floppy images. You can download Winimage from http:/​/​www.winimage.com/​download.htm . You can also use other tools, such as BFI, to create virtual floppy images.

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

Save the file as a virtual floppy image (.flp file) using the following naming conventions:

- Unified Communications Manager— ucm.flp

- IM and Presence Service— imp.flp

Step 7

Repeat these steps for both the Unified Communications Manager cluster and the IM and Presence Service cluster.

#### What to do next

Upload Virtual Floppy Image to Datastore

### Upload Virtual Floppy Image to Datastore

Use this procedure to upload the virtual floppy images to the datastore.

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

Upload the vFloppy images to your local folder.

Step 7

At the Upload/Download warning, click Yes .

Step 8

Close the Datastore Browser window.

#### What to do next

Mount Floppy Image to VM

### Mount Floppy Image to VM

Use this procedure to mount the UC application virtual floppy images on their corresponding VM.

Step 1

In the vSphere client, choose the virtual machine.

Step 2

Open VMware Remote Console (VMRC), and click the Floppy drive .

Step 3

Select Use existing floppy image in datastore .

Step 4

Browse to the datastore and locate the virtual floppy image.

Step 5

Select the file and click OK .

Step 6

Under Device Status , enable the Connected and Connect at power on option.

Step 7

Click the Options tab. Under Boot Options , check Force entry to BIOS and click OK .

Step 8

Repeat this procedure for each VM on which you want to install a node.

#### What to do next

Run Touchless Install

### Run Touchless Install

After you have mounted your virtual floppy drives to your application VMs, run the touchless installation process. You can
                                 install all nodes simultaneously.

Step 1

In vSphere client, right-click the VM and select Open Console . A console window opens.

Step 2

Click the Power On icon in the console tool bar to power on the virtual machine.

Step 3

When the BIOS screen appears, configure the following boot order:

CD-Rom

Hard Drive

Removable Devices

Network

Step 4

Save the settings and exit from the console. The installation commences immediately.

Step 5

Repeat these steps for each cluster node. All cluster nodes may install in parallel; you do not have to install them serially.

Step 6

After to emphasise the completion of an activity, remove the vFloppy configurations from the virtual machines.

#### What to do next

Postinstall Tasks for Cisco Unified Communications Manager

Postinstall tasks for the IM and Presence Service

## Add a New Node to an Existing Cluster

To add a new Unified Communications Manager or IM and Presence Service subscriber node to an existing cluster, you can use
                              either the Basic Installation or Touchless Installation methods to add and install the node. Any new nodes that you add must
                              be configured as subscriber nodes.

### Basic Installation

For basic installations of additional Unified Communications Manager or IM and Presence Service cluster nodes, complete the
                              following tasks:

Description

Step 1

Run a full backup of the cluster.

For details, see the "Manage Backups" chapter of the Administration Guide for Cisco Unified Communications Manager .

Step 2

Basic Installation

Begin the install process.

Step 3

Configure Basic Installation

Continue with the Basic Installation process by configuring your installation.

Step 4

Add Subscriber Nodes

Add subscriber nodes to Unified Communications Manager publisher.

Step 5

Install Subscriber Nodes

Install software on your subscriber nodes.

### Touchless Installation

For Touchless installations of additional Unified Communications Manager or IM and Presence Service cluster nodes, complete
                              these tasks:

Description

Step 1

Run a full backup of the cluster.

For details, see the "Manage Backups" chapter of the Administration Guide for Cisco Unified Communications Manager .

Step 2

Generate Answer Files for Touchless Install

Generate answer files for your installation. The touchless install process uses answer files to install and configure the
                                          various cluster nodes.

Step 3

Generate Virtual Floppy Images

Create a virtual floppy image from the answer file.

Step 4

Upload Virtual Floppy Image to Datastore

Upload the virtual floppy to the datastore.

Step 5

Mount Floppy Image to VM

Mount the virtual floppy to the virtual machine.

Step 6

Run Touchless Install

Install the software.

### Notes for Basic and Touchless Installs

Important

You can collect the logs from RTMT of a new node added to the existing FQDN cluster, only when you restart the trace collection
                                                service. When you sign in to Unified RTMT without restarting the trace collection, the following error message is displayed:
                                                .

Could not connect to 'Server' <new node name>

If you install a new node to an existing cluster where the IM and Presence server is not upgraded to the supported version
                                                or if the IM and Presence server has been decommissioned, the following error message is displayed:

"Add failed. Upgrade and migration for Cisco Unified IM & Presence Servers that are associated with this cluster appears to
                                                   be pending (not complete). Please make sure upgrade and migration of all IM & Presence servers is completed successfully before
                                                   adding servers to this cluster. Please check for any unused IM & Presence Application Servers and delete them”.

A touchless install cannot be used to simultaneously install multiple Unified Communications Manager and multiple IM and Presence
                                          Service nodes. The following scenarios are supported:

Installing only multiple Unified Communications Manager nodes

Installing only one Unified Communications Manager node (publisher) and multiple and IM and Presence Service nodes

If you need to simultaneously install multiple Unified Communications Manager and IM and Presence Service nodes, you need
                                          to use one of the above scenarios and install additional nodes manually.

## Install with Data Import

Use one of these steps to configure Unified Communications Manager and IM and Presence Service installation with data import
                              from an older version of Unified CM.

Important

Fresh Install with Data Import does not support domain name changes. If DNS is enabled on the publisher node of the destination
                                                cluster, the domain name must match the source cluster. If the domain name needs to change, install the destination cluster
                                                on the publisher without the DNS enabled and then enable DNS via the CLI after the installation is complete. The subscribers
                                                can be installed with the DNS enabled, but ensure that the System > Server entries on the publisher node are correct before installing the subscribers.

If you plan to change the hostname and/or IP address during the migration, the System > Server entries must be updated on the publisher node of the destination cluster prior to installing the subscribers.

Fresh Install with Data Import does not support installation with DHCP configuration. If DHCP is enabled on the source cluster,
                                                install the destination cluster with Static configuration data and then configure the DHCP later post migration.

Ensure that all nodes in the cluster are exported to the SFTP server before proceeding with Fresh Install with Data Import.

See the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service to refer to the supported source releases for direct migration to the 14SU2 destination versions.

### Before you begin

Step 1

Export data from the source cluster publisher node.

Run the utils system upgrade dataexport initiate CLI command on each node of the desired source system to export the data which can be imported using this procedure.

Enter the SFTP server information to export the data.

Enter the node Hostname and IP Address (it is possible to change them at this stage.)

Run the utils system upgrade dataexport status to track the export status.

Step 2

Export data from the source cluster subscriber node.

Run the utils system upgrade dataexport initiate CLI command on each node of the desired source system to export the data which can be imported using this procedure.

Enter the SFTP server information to export data.

Enter the node Hostname and IP Address (it is possible to change them at this stage).

Run the utils system upgrade dataexport status to track the export status.

Step 3

Repeat Step 2 for the remaining subscriber nodes.

Step 4

Then proceed with one of the following methods to complete installation/import.

During the configuration of an IP address, if the source and destination clusters are using DHCP, ensure that you configure
                                                      a static IP address for the destination cluster. For example, the current IP address of the source cluster.

Installation Method

See

Attended Install

Install a new publisher and import the data. To configure Unified Communications Manager and IM and Presence Service with Install with Data Import follow the instructions as described in Basic Installation from step 1 through 6.

In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Unified Communications Manager
                                                            and IM and Presence Service installation.

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

If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node.

Touchless Install of a Single Node or a Cluster

Follow the instructions as described in Touchless Installation Task Flow from step 1 through 5.

If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command.

| Task Flow | Description |
|---|---|
| Cluster Installs |
| Basic Installation Task Flow | Use this method for basic installs of any of the following deployments: Cisco Unified Communications Manager telephony cluster installs Standard Deployments (Decentralized) for IM and Presence |
| Install IM and Presence Central Cluster (Basic Installation) | For Centralized Deployments of IM and Presence, use this task flow for basic installs of the IM and Presence central cluster. |
| Touchless Installation Task Flow | Use this task flow to install a Unified Communications Manager or IM and Presence Service cluster dynamically without the
                                          need for manual intervention. Applies to either Centralized or Standard (Decentralized) IM and Presence deployments. |
| Install with Data Import | Complete this tasks to install a Unified Communications Manager or IM and Presence Service cluster using the Install with Data Import . |
| Node Installs |
| Add a New Node to an Existing Cluster | Complete these tasks if you want to add a node to an existing Unified Communications Manager or IM and Presence Service cluster. |

| Note | You can also use Cisco Prime Collaboration Deployment to install your cluster. For motr information, see Cisco Prime Collaboration Deployment Administration Guide . |
|---|---|

| Task Flow | Description |
|---|---|
| Cluster Installs |
| Basic Installation Task Flow | Use this method for basic installs of any of the following deployments: Cisco Unified Communications Manager telephony cluster installs Standard Deployments (Decentralized) for IM and Presence |
| Install IM and Presence Central Cluster (Basic Installation) | For Centralized Deployments of IM and Presence, use this task flow for basic installs of the IM and Presence central cluster. |
| Touchless Installation Task Flow | Use this task flow to install a Unified Communications Manager or IM and Presence Service cluster dynamically without the
                                          need for manual intervention. Applies to either Centralized or Standard (Decentralized) IM and Presence deployments. |
| Install with Data Import | Complete this tasks to install a Unified Communications Manager or IM and Presence Service cluster using the Install with Data Import . |
| Node Installs |
| Add a New Node to an Existing Cluster | Complete these tasks if you want to add a node to an existing Unified Communications Manager or IM and Presence Service cluster. |

| Note | You can also use Cisco Prime Collaboration Deployment to install your cluster. For motr information, see Cisco Prime Collaboration Deployment Administration Guide . |
|---|---|

| To Do This | Press This |
|---|---|
| Move to the
                                             					 next field | Tab |
| Move to the
                                             					 previous field | Alt-Tab |
| Choose an
                                             					 option | Space bar or
                                             					 Enter |
| Scroll up or
                                             					 down in a list | Up or down
                                             					 arrow |
| Go to the
                                             					 previous window | Space bar or
                                             					 Enter to choose Back (when available) |
| Get help
                                             					 information on a window | Space bar or
                                             					 Enter to choose Help (when available) |

| Note | The installation wizard supports the following characters: alphanumeric: A-Z, a-z, and 0-9- spaces spaces and # (except as the first character) only the following special characters: \.,-_:;{}()[] all other characters are not supported. |
|---|---|

| Note | Depending on your installation scenario, you may not need to perform all of the tasks. For example, if you are installing
                                          the IM and Presence Service on an existing Unified Communications Manager cluster that is already in use, you only need to
                                          complete the tasks for installing the IM and Presence Service. |
|---|---|

|  | Cisco Unified Communications Manager | IM and Presence Service | Description |
|---|---|---|---|
| Step 1 | Basic Installation | — | Begin the install process for Unified Communications Manager. |
| Step 2 | Enter Configuration Information for Preinstalled Servers | — | Pre-installed servers only (e.g., Cisco Business Edition). Add pre-configured information to the installation.  Otherwise,
                                          skip this task. |
| Step 3 | Optional. Complete either of the following tasks: Upgrade Install Image from Local Source Upgrade Install Image from Remote Server | — | Upgrade your install image to a newer version. This optional task is available for Unified Communications Manager installs
                                          only. |
| Step 4 | Configure Basic Installation | — | Continue with the Basic Installation process by configuring your installation. |
| Step 5 | Configure the Unified Communications Manager Publisher | — | Configure and install software on the publisher node. |
| Step 6 | Add Subscriber Nodes | — | Add subscriber nodes to the publisher node. |
| Step 7 | Install Subscriber Nodes | — | Install software on your Cisco Unified Communications Manager subscriber nodes. |
| Step 8 | — | Basic Installation | Begin the install process for the IM and Presence Service. |
| Step 9 | — | Enter Configuration Information for Preinstalled Servers | Pre-installed servers only (e.g., Cisco Business Edition). Add pre-configured information to the installation.  Otherwise,
                                          skip this task. |
| Step 10 | — | Configure Basic Installation | Continue Basic Install process for IM and Presence by configuring the installation. |
| Step 11 | — | Configure the IM and Presence Publisher | Configure and complete the installation for the IM and Presence database publisher node. |
| Step 12 | Add Subscriber Nodes | — | On the Cisco Unified Communications Manager publisher node, add IM and Presence subscribers. |
| Step 13 | — | Install Subscriber Nodes | Install software on your IM and Presence Service subscriber nodes. |

| Note | For basic installation of IM and Presence Service in a Decentralized (Standard) deployment, follow the Basic Installation Task Flow to install both the telephony and IM and Presence clusters. |
|---|---|

|  | Unified CM Publisher (non-telephony) | IM and Presence Central Cluster | Description |
|---|---|---|---|
| Step 1 | Basic Installation |  | Begin the install process for the Unified CM publisher node. |
| Step 2 | Configure Basic Installation |  | Configure the Basic Installation. |
| Step 3 | Configure the Unified Communications Manager Publisher |  | Configure the Unified CM publisher node. |
| Step 4 |  | Basic Installation | Begin the install process for the IM and Presence central cluster. |
| Step 5 |  | Configure Basic Installation | Continue with the Basic Install process for IM and Presence by continuing the installation. |
| Step 6 |  | Configure the IM and Presence Publisher | Configure the IM and Presence database publisher node. |
| Step 7 | Add Subscriber Nodes |  | On the Unified CM publisher, add IM and Presence subsciber nodes. |
| Step 8 |  | Install Subscriber Nodes | Complete the installation on the IM and Presence subsicribers. |

| Step 1 | If you are using a configuration file created by the Answer File Generator, ensure that the virtual floppy image is in a location
                                          where the virtual machine can access it. Note If you have a Cisco Business Edition 6000/7000 appliance with the software pre-installed, you do not need to install from
                                                      a DVD or ISO file, unless you want to re-image the server with a later product release. Go directly to the configure basic
                                                      installation procedure to enter the configuration information. For more information, see Installation Guide for Cisco Business Edition 6000 or Installation Guide for Cisco Business Edition 7000 . | Note | If you have a Cisco Business Edition 6000/7000 appliance with the software pre-installed, you do not need to install from
                                                      a DVD or ISO file, unless you want to re-image the server with a later product release. Go directly to the configure basic
                                                      installation procedure to enter the configuration information. For more information, see Installation Guide for Cisco Business Edition 6000 or Installation Guide for Cisco Business Edition 7000 . |
|---|---|---|---|
| Note | If you have a Cisco Business Edition 6000/7000 appliance with the software pre-installed, you do not need to install from
                                                      a DVD or ISO file, unless you want to re-image the server with a later product release. Go directly to the configure basic
                                                      installation procedure to enter the configuration information. For more information, see Installation Guide for Cisco Business Edition 6000 or Installation Guide for Cisco Business Edition 7000 . |
| Step 2 | Perform one of the following: If you are installing from a DVD drive located on a VMware ESXi server host, insert the installation DVD into the tray and
                                             restart the virtual machine, so that it boots from the DVD. If you are installing from a data store ISO file located on the local ESXi host or on a storage area network (SAN), edit the
                                             CD or DVD drive on the virtual machine to select the data store ISO file. Select the option to connect at power on, and restart
                                             the virtual machine. If you have configured the virtual machine to use the ISO at the same time that you created the virtual
                                             machine using the OVA file, skip this step and complete the rest of the procedure. After the server completes the boot sequence, the DVD Found window displays. |
| Step 3 | Click Yes to perform the media check. Or click No to skip the media check. The media check verifies the integrity of the DVD. If the DVD has passed the media check previously, choose to skip the media
                                             check. |
| Step 4 | If you click Yes to perform the media check, the Media Check Result window displays. If the Media Check Result displays Pass , click OK to continue the installation. If the media check fails, either download another copy from cisco.com or obtain another DVD directly from Cisco. |
| Step 5 | In the Product
                                             				Deployment Selection window, specify which product you want to install: Unified Communications Manager —Choose the product and click OK . IM and
                                                				  Presence Service —Select OK . Cisco Unity Connection —Select the product and click OK . Note The window displays the products that are supported and not supported by your hardware. If only one product is supported,
                                                         you do not choose which product to install. | Note | The window displays the products that are supported and not supported by your hardware. If only one product is supported,
                                                         you do not choose which product to install. |
| Note | The window displays the products that are supported and not supported by your hardware. If only one product is supported,
                                                         you do not choose which product to install. |
| Step 6 | If the software is currently installed on the server, the Overwrite Hard Drive window opens and displays the current software version on your hard drive, DVD or ISO file. Click Yes to continue with the installation or No to cancel. Caution If you choose to continue with the installation, all existing data on your hard drive gets overwritten and destroyed. The Platform Installation Wizard window displays. | Caution | If you choose to continue with the installation, all existing data on your hard drive gets overwritten and destroyed. |
| Caution | If you choose to continue with the installation, all existing data on your hard drive gets overwritten and destroyed. |
| Step 7 | In the Platform Installation Wizard window, choose one of
                                          			 the following options: To continue with the basic installation process, choose Proceed and continue. Allows you to configure the basic installation process. Use this installation method first-time setup or during
                                             restore from backup. To continue with Install with Data Import , choose Import . Use this installation method for direct migrations (Fresh Install with Data Import) from the older versions of Unified Communications
                                             Manager or IM and Presence Service. If you have a preinstalled server (for example, a Cisco Business Edition server), configure the pre-installed software. Click Skip and go to Enter Configuration Information for Preinstalled Servers . If you want to install the software first and then configure it later, click Skip . The installation process installs the software and then prompts you to configure it after the installation is complete.
                                             This method may increase the total time for the installation. |
| Step 8 | In the Apply Additional Release window, if you have a newer Unified Communications Manager version than your install image, you can elect to upgrade the installation to the newer release. This option is not available
                                          for the IM and Presence Service. Yes —Choose this option to upgrade the Unified Communications Manager install image to a newer Service Release. Go to one of the following procedures: Upgrade Install Image from Local Source Upgrade Install Image from Remote Server No —Choose this option if you are installing the IM and Presence Service or if you are installing Unified Communications Manager and you do not want to upgrade the installed image. |
| Step 9 | In the Basic Install window, click Continue to install the software or configure the pre-installed software. |

| Note | If you have a Cisco Business Edition 6000/7000 appliance with the software pre-installed, you do not need to install from
                                                      a DVD or ISO file, unless you want to re-image the server with a later product release. Go directly to the configure basic
                                                      installation procedure to enter the configuration information. For more information, see Installation Guide for Cisco Business Edition 6000 or Installation Guide for Cisco Business Edition 7000 . |
|---|---|

| Note | The window displays the products that are supported and not supported by your hardware. If only one product is supported,
                                                         you do not choose which product to install. |
|---|---|

| Caution | If you choose to continue with the installation, all existing data on your hard drive gets overwritten and destroyed. |
|---|---|

| Step 1 | After the system
                                          			 restarts, the Preexisting Installation Configuration window
                                          			 displays. |
|---|---|
| Step 2 | If you have preexisting configuration information that the Answer File Generator created, that is stored on a USB key. Insert
                                          the USB key and choose Continue . The installation wizard reads the configuration information during the installation process. Note If a popup window states that the system detected new hardware, press any key and then choose Install from the next window. | Note | If a popup window states that the system detected new hardware, press any key and then choose Install from the next window. |
| Note | If a popup window states that the system detected new hardware, press any key and then choose Install from the next window. |
| Step 3 | In
                                          			 the Platform
                                             				Installation Wizard window, choose Proceed . |
| Step 4 | In the Apply Additional Release window, you can choose the option to upgrade Unified Communications Manager install file to a newer release. This option
                                          is not available for the IM and Presence Service. Yes —Choose this option to upgrade the Unified Communications Manager install image to a newer Service Release. Go to one of the following procedures: > Upgrade Install Image from Local Source > Upgrade Install Image from Remote Server No —Choose this option if you are installing the IM and Presence Service or installing Unified Communications Manager and you do not want to upgrade the install image. |
| Step 5 | In the Basic
                                             				Install window, choose Continue . |

| Note | If a popup window states that the system detected new hardware, press any key and then choose Install from the next window. |
|---|---|

| Note | If you have placed your upgrade file on an FTP or SFTP server, refer to Upgrade Install Image from Remote Server . |
|---|---|

| Note | To complete this procedure, you must have completed the Start Basic Installation procedure and have chosen to apply a patch
                                             via a LOCAL source. |
|---|---|

| Step 1 | When the Local
                                             				Patch Configuration window displays, enter the patch directory and
                                          			 patch name, if required, and choose OK. The Install Upgrade Patch Selection Validation window displays. |
|---|---|
| Step 2 | The window displays the patch file. To update the system with this patch, click Continue . |
| Step 3 | Choose the
                                          			 upgrade patch to install. The system installs the patch, then restarts the
                                          			 system with the upgraded software version running. After the system
                                             				restarts, the Preexisting Configuration Information window
                                             				displays. |
| Step 4 | To continue the installation, choose Proceed . The Platform Installation Wizard window displays. |
| Step 5 | To continue the installation, click Proceed or click Cancel to stop the installation. If you click Proceed , the Apply Patch window displays. Continue with the next step. If you click Cancel , the system halts, and you can safely power down the server. |
| Step 6 | When the Apply
                                             				Patch window displays, choose No. |
| Step 7 | The Upgrade window displays. |
| Step 8 | Click No and perform the procedure to configure the basic installation. |

| Note | If you have placed your upgrade file on an FTP or SFTP server, refer to Upgrade Install Image from Local Source . |
|---|---|

| Step 1 | Configure the
                                          			 auto negotiation setting. To enable automatic negotiation, choose Yes . This option sets the speed and duplex settings of the Ethernet network interface card (NIC) by using automatic negotiation.
                                             The MTU Configuration window displays. Skip the next step and then continue. Note To use this option, your hub or the Ethernet switch must support automatic negotiation. To disable automatic
                                             				negotiation, choose No . The NIC Speed and Duplex Configuration window
                                             				displays. Continue with the next step. | Note | To use this option, your hub or the Ethernet switch must support automatic negotiation. |
|---|---|---|---|
| Note | To use this option, your hub or the Ethernet switch must support automatic negotiation. |
| Step 2 | If you chose to
                                          			 disable automatic negotiation, manually choose the appropriate NIC speed and
                                          			 duplex settings now and choose OK to continue. The MTU
                                                				  Configuration window displays. |
| Step 3 | In the MTU
                                             				Configuration window, you can change the MTU size from the operating
                                          			 system default. The maximum transmission unit (MTU) represents the largest packet, in bytes, that this host transmits on the network. If you
                                             are unsure of the MTU setting for your network, use the default value. Caution If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected. To accept the default value (1500 bytes), choose No . To change the MTU size from the operating system default, choose Yes , enter the new MTU size, and choose OK . The DHCP
                                                				  Configuration window displays. | Caution | If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected. |
| Caution | If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected. |
| Step 4 | For network
                                          			 configuration, you can choose to either set up static network IP addresses for
                                          			 the node and gateway or to use Dynamic Host Configuration Protocol (DHCP).
                                          			 Static IP addresses are recommended. If you use DHCP, use static DHCP. If you have
                                                   					 a DHCP server that is configured in your network and want to use DHCP, choose Yes . The installation process attempts to verify
                                                   					 network connectivity. If you want
                                                   					 to configure static IP addresses for the node, choose No . The Static Network Configuration window
                                                   					 displays. |
| Step 5 | If you chose not
                                          			 to use DHCP, enter your static network configuration values and choose OK . The DNS
                                                				  Client Configuration window displays. |
| Step 6 | To enable DNS,
                                          			 choose Yes , enter your DNS client information, and choose OK . After the system
                                             				configures the network and checks for connectivity, the Remote Patch
                                             				Configuration window displays. |
| Step 7 | Enter the
                                          			 location and login information for the remote file server. The system connects
                                          			 to the remote server and retrieves a list of available upgrade patches. If the upgrade file is located on a Linux or Unix server, you must enter a forward slash at the beginning of the directory
                                             path. For example, if the upgrade file is in the patches directory, you must enter /patches . If the upgrade
                                             				file is located on a Windows server, remember that you are connecting to an FTP
                                             				or SFTP server, so use the appropriate syntax, including: Begin the path with a forward slash (/) and use forward slashes throughout the path. The path
                                                   					 must start from the FTP or SFTP root directory on the server, so you cannot
                                                   					 enter a Windows absolute path, which starts with a drive letter (for example,
                                                   					 C:). The Install Upgrade Patch Selection window displays. |
| Step 8 | Choose the
                                          			 upgrade patch to install. The system downloads, unpacks, and installs the patch
                                          			 and then restarts the system with the upgraded software version running. After the system
                                             				restarts, the Preexisting Configuration Information window
                                             				displays. |
| Step 9 | To continue the
                                          			 installation, choose Proceed. The Platform Installation Wizard window displays. |
| Step 10 | Choose Proceed or choose Cancel to stop the installation. If you choose Proceed , the Apply Patch window displays. Continue with the next step. If you choose Cancel , the system halts, and you can safely power down the server. |
| Step 11 | In the Apply Patch window displays, choose No . The Windows Upgrade window displays. |
| Step 12 | Choose No and perform the Configure Attended Installation procedure to configure the basic installation. |

| Note | To use this option, your hub or the Ethernet switch must support automatic negotiation. |
|---|---|

| Caution | If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected. |
|---|---|

| Step 1 | In the Timezone Configuration window, choose the appropriate
                                          			 time zone for the server and then choose OK . The Auto Negotiation Configuration window is displayed. |
|---|---|
| Step 2 | The installation
                                          			 process allows you to automatically set the speed and duplex settings of the
                                          			 Ethernet network interface card (NIC) by using automatic negotiation. You can
                                          			 change this setting after installation. To enable
                                                   					 automatic negotiation, choose Yes . The MTU Configuration window is displayed. Note To use
                                                               						this option, your hub or Ethernet switch must support automatic negotiation. To disable
                                                   					 automatic negotiation, choose No and continue with the next step. The NIC Speed and Duplex Configuration window is displayed. | Note | To use
                                                               						this option, your hub or Ethernet switch must support automatic negotiation. |
| Note | To use
                                                               						this option, your hub or Ethernet switch must support automatic negotiation. |
| Step 3 | If you chose to
                                          			 disable automatic negotiation, manually choose the appropriate NIC speed and
                                          			 duplex settings now and choose OK to continue. The MTU
                                                				  Configuration window displays. |
| Step 4 | In the MTU
                                             				Configuration window, you can change the MTU size from the operating
                                          			 system default. The maximum
                                             				transmission unit (MTU) represents the largest packet, in bytes, that this host
                                             				will transmit on the network. If you are unsure of the MTU setting for your
                                             				network, use the default value, which is 1500 bytes. Caution If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected. To accept
                                                   					 the default value (1500 bytes), choose No. To change
                                                   					 the MTU size from the operating system default, choose Yes, enter the new MTU
                                                   					 size, and choose OK. The DHCP
                                                				  Configuration window displays. | Caution | If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected. |
| Caution | If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected. |
| Step 5 | For network
                                          			 configuration, you can choose to either set up a static network IP address for
                                          			 the node or to use Dynamic Host Configuration Protocol (DHCP). Static IP
                                          			 addresses are recommended. If you use DHCP, use static DHCP. If you have a DHCP server that is configured in your network and want to use DHCP, choose Yes . The network restarts, and the Administrator Login Configuration window is displayed. If you want
                                                   					 to configure a static IP address for the node, choose No . The Static Network Configuration window
                                                   					 displays. |
| Step 6 | If you chose not
                                          			 to use DHCP, enter your static network configuration values and choose OK . The DNS Client Configuration window is displayed. |
| Step 7 | In the DNS Client Configuration window, click Yes to enable DNS and enter the DNS client information. |
| Step 8 | Click OK and choose one of the following in the Basic Installation procedure: Proceed: Click Proceed to restart the network using the new configuration. The Administrator Login Configuration window is displayed. Enter Administrator login User Name and Password Note Make sure that the User Name contians alphanumeric characters. Use the same login cerdentials to Cisco Unified Communications Operating System Administration,
                                                            the Command Line Interface, and the Disaster Recovery System. Software Location of Data to Import Enter Remote Server Name or IP, Export Data Directory, Remote Login ID, Remote Password, and Confirm Password. Click OK to restart the network using the new configuration. | Note | Make sure that the User Name contians alphanumeric characters. Use the same login cerdentials to Cisco Unified Communications Operating System Administration,
                                                            the Command Line Interface, and the Disaster Recovery System. |
| Note | Make sure that the User Name contians alphanumeric characters. Use the same login cerdentials to Cisco Unified Communications Operating System Administration,
                                                            the Command Line Interface, and the Disaster Recovery System. |
| Step 9 | The Certificate Information window is displayed. |
| Step 10 | In Certificate Information window, enter your certificate signing request information and click OK. |
| Step 11 | In the First Node Configuration window, choose how you want to assign this node: Yes —Choose this option to assign this node as the Cisco Unified Communications Manager publisher node. No —Choose this option to assign this node as a Cisco Unified Communications Manager subscriber node, or as an IM and Presence
                                             Service node. |

| Note | To use
                                                               						this option, your hub or Ethernet switch must support automatic negotiation. |
|---|---|

| Caution | If you
                                                         				  configure the MTU size incorrectly, your network performance can be affected. |
|---|---|

| Note | Make sure that the User Name contians alphanumeric characters. Use the same login cerdentials to Cisco Unified Communications Operating System Administration,
                                                            the Command Line Interface, and the Disaster Recovery System. |
|---|---|

| Note | You can configure Smart Call Home on the publisher node only. |
|---|---|

| Step 1 | The Network
                                             				Time Protocol Client Configuration window appears. We recommend that you use an external NTP server to ensure accurate system time on the publisher node. Subscriber nodes in
                                             the cluster will get their time from the first node. |
|---|---|
| Step 2 | Choose whether
                                          			 you want to configure an external NTP server or manually configure the system
                                          			 time. To set up an external NTP server, choose Yes and enter the IP address, NTP server name, or NTP server pool name for at least one NTP server. You can configure up to five
                                                   NTP servers, and we recommend that you use at least three. Choose Proceed to continue with the installation. The system
                                                   					 contacts an NTP server and automatically sets the time on the hardware clock. Note If the Test button appears, you can choose Test to check whether the NTP servers are accessible. To manually
                                                   					 configure the system time, choose No and enter the appropriate date and time to set
                                                   					 the hardware clock. Choose OK to continue with the installation. The Database Access Security Configuration window
                                             				appears. | Note | If the Test button appears, you can choose Test to check whether the NTP servers are accessible. |
| Note | If the Test button appears, you can choose Test to check whether the NTP servers are accessible. |
| Step 3 | Enter the
                                          			 Security password from Required Installation Information. Note The Security
                                                         				  password must start with an alphanumeric character, be at least six characters
                                                         				  long, and can contain alphanumeric characters, hyphens, and underscores. The
                                                         				  system uses this password to authorize communications between nodes, and you
                                                         				  must ensure this password is identical on all nodes in the cluster. The SMTP
                                                				  Host Configuration window appears. | Note | The Security
                                                         				  password must start with an alphanumeric character, be at least six characters
                                                         				  long, and can contain alphanumeric characters, hyphens, and underscores. The
                                                         				  system uses this password to authorize communications between nodes, and you
                                                         				  must ensure this password is identical on all nodes in the cluster. |
| Note | The Security
                                                         				  password must start with an alphanumeric character, be at least six characters
                                                         				  long, and can contain alphanumeric characters, hyphens, and underscores. The
                                                         				  system uses this password to authorize communications between nodes, and you
                                                         				  must ensure this password is identical on all nodes in the cluster. |
| Step 4 | If you want to
                                          			 configure an SMTP server, choose Yes and enter the SMTP server name. If you do not
                                          			 want to configure the SMTP server, choose No , which redirects to Smart Call Home page. To go
                                          			 to previous page, choose Back and to see the information about the SMTP
                                          			 configuration, choose Help . Note You must
                                                         				  configure an SMTP server to use certain platform features; however, you can
                                                         				  also configure an SMTP server later by using the platform GUI or the command
                                                         				  line interface. | Note | You must
                                                         				  configure an SMTP server to use certain platform features; however, you can
                                                         				  also configure an SMTP server later by using the platform GUI or the command
                                                         				  line interface. |
| Note | You must
                                                         				  configure an SMTP server to use certain platform features; however, you can
                                                         				  also configure an SMTP server later by using the platform GUI or the command
                                                         				  line interface. |
| Step 5 | Choose OK . |
| Step 6 | In the SMART Call Home Enable window, choose one of the following and click OK : Enable Smart Call Home on System Start Enable Anonymous Call Home on System Start Remind me Later to configure Smart Call Home —Select this option to configure the Smart Call Home feature service after installation using the Cisco Unified Serviceability
                                             interface. Disable All Call Home on System Start —Select this option to deactivate the Smart Call Home feature service. Please note that you can reactivate it after installation
                                             using the Cisco Unified Serviceability interface. |
| Step 7 | If you have selected Smart Call Home on System Start , do the following: Select the method for sending data to the Cisco Technical Assistance Center. Secure Web (HTTPS) Secure Web (HTTPS) through Proxy—If you select this option, enter the Hostname or IP address of the proxy server where the
                                                         Call Home info gets sent as well as the port number on which the server is enabled. Email—If you select this option, you must have configured SMTP for any emails to be sent successfully. To send a copy of the Call Home messages to multiple email recipients, enter the email addresses separated with a comma. You
                                                can enter up to a maximum of 1024 characters. In the Customer Contact Details field, enter the customer's email address. Click Continue to proceed, or select Back to return to the previous menu. If you click Continue , a message appears as Cisco Call Home includes reporting capabilities that allow Cisco to receive diagnostic and system information from your Unified Communications Manager cluster. Cisco may use this information for proactive debugging, product development or marketing purposes. To learn more
                                                      about this feature, please visit: http://www.cisco.com/en/US/products/ps7334/serv_home.html. Note If you have selected Secure Web (HTTPS) through Proxy and click Continue , the Smart Call Home Proxy Configuration window appears. Click Confirm to proceed with normal installation or select Back to return to the Smart Call Home Enable Page. | Note | If you have selected Secure Web (HTTPS) through Proxy and click Continue , the Smart Call Home Proxy Configuration window appears. |
| Note | If you have selected Secure Web (HTTPS) through Proxy and click Continue , the Smart Call Home Proxy Configuration window appears. |
| Step 8 | If you have selected Enable Anonymous Call Home on System Start , do the following: Select the method for sending data to the Cisco Technical Assistance Center. Secure Web (HTTPS) Secure Web (HTTPS) through Proxy—If you select this option, enter the Hostname or IP address of the proxy server where the
                                                         Call Home info gets sent as well as the port number on which the server is enabled. Email—If you select this option, you must have configured SMTP for any emails to be sent successfully. To send a copy of the Call Home messages to multiple email recipients, enter the email addresses separated with a comma. You
                                                can enter up to a maximum of 1024 characters. Click Continue to proceed, or click Back to return to the previous menu. When you click Continue , the following message appears. To help improve the Unified Communications Manager experience, click Confirm to allow Cisco Systems to securely receive usage
                                                      statistics from the server. This information will be used by Cisco to help understand how customers are using our product
                                                      and ultimately drive product direction. If you prefer not to participate, you may choose to opt-out. Note If you have selected Secure Web (HTTPS) through Proxy and clicked Continue , the Anonymous Call Home Proxy Configuration window appears. Click Confirm to proceed with normal installation or click Back to return to the Smart Call Home Enable Page. Note If you choose Install with Data Import during basic installation the Application User Configuration window does not appear. Proceed to step 11 to complete the installation. | Note | If you have selected Secure Web (HTTPS) through Proxy and clicked Continue , the Anonymous Call Home Proxy Configuration window appears. | Note | If you choose Install with Data Import during basic installation the Application User Configuration window does not appear. Proceed to step 11 to complete the installation. |
| Note | If you have selected Secure Web (HTTPS) through Proxy and clicked Continue , the Anonymous Call Home Proxy Configuration window appears. |
| Note | If you choose Install with Data Import during basic installation the Application User Configuration window does not appear. Proceed to step 11 to complete the installation. |
| Step 9 | Click OK . The Application User Configuration window appears. |
| Step 10 | Enter the
                                          			 Application User name and password from and confirm the password by entering it
                                          			 again. |
| Step 11 | Choose OK . The Platform Configuration Confirmation window appears. |
| Step 12 | Choose OK to continue with the installation or choose Back to modify the platform configuration. The system installs and configures the software. The server reboots. When the installation process completes, you are prompted to log in by using the Administrator account and password. |

| Note | If the Test button appears, you can choose Test to check whether the NTP servers are accessible. |
|---|---|

| Note | The Security
                                                         				  password must start with an alphanumeric character, be at least six characters
                                                         				  long, and can contain alphanumeric characters, hyphens, and underscores. The
                                                         				  system uses this password to authorize communications between nodes, and you
                                                         				  must ensure this password is identical on all nodes in the cluster. |
|---|---|

| Note | You must
                                                         				  configure an SMTP server to use certain platform features; however, you can
                                                         				  also configure an SMTP server later by using the platform GUI or the command
                                                         				  line interface. |
|---|---|

| Note | If you have selected Secure Web (HTTPS) through Proxy and click Continue , the Smart Call Home Proxy Configuration window appears. |
|---|---|

| Note | If you have selected Secure Web (HTTPS) through Proxy and clicked Continue , the Anonymous Call Home Proxy Configuration window appears. |
|---|---|

| Note | If you choose Install with Data Import during basic installation the Application User Configuration window does not appear. Proceed to step 11 to complete the installation. |
|---|---|

| Step 1 | Install and configure the IM and Presence database publisher node. |
|---|---|
| Step 2 | Verify that the following services are running: Cisco SIP Proxy Cisco Presence Engine Cisco XCP Connection Manager Cisco XCP Authentication Service If you need to activate services, you can do it in Cisco Unified Serviceability at Tools > Service Activation . |

| Step 1 | Log in to the Unified Communications Manager publisher node. |
|---|---|
| Step 2 | From Cisco Unified CM Administration choose System > Server . |
| Step 3 | Add your subscriber nodes: Click Add New . From the Server Type drop-down list, choose the node type that corresponds to the install that you are completing: Unified Communications Manager
                                                Voice/Video node, or IM and Presence Service node. Enter the Fully Qualified Domain Name/IP Address field with a FQDN or IPv4 Address. Note Do not use single quotes (' ') in the Description field while adding the node details. Optional. If you are deploying IPv6, enter an IPv6 Address . Click Save . Repeat these steps for each subscriber node that you want to add. | Note | Do not use single quotes (' ') in the Description field while adding the node details. |
| Note | Do not use single quotes (' ') in the Description field while adding the node details. |
| Step 4 | (IM and Presence Service only) Add your
                                          Presence Redundancy Groups in order to define your subclusters. From Cisco Unified CM Administration, choose System > Presence
                                                      Redundancy Groups . Click Add New . Enter a Name and Description for the group. From the Server drop-down list, choose the IM and Presence Service nodes that you want to add to this group. Click Save . Repeat this procedure until you've created your groups. You can have up to three Presence Redundancy Groups in a cluster,
                                                with each group consisting of two IM and Presence Service nodes. |

| Note | Do not use single quotes (' ') in the Description field while adding the node details. |
|---|---|

| Step 1 | If you have configured Network Time Protocol on the publisher node, ensure that it is synchronized with an NTP server before
                                          you install a subscriber node. From the Command Line Interface on the publisher node, enter utils ntp status . Ensure that the output indicates that the node is synchronized with an NTP server. Note If the publisher node is not synchronized with an NTP server, installation of the subscriber node will fail. | Note | If the publisher node is not synchronized with an NTP server, installation of the subscriber node will fail. |
|---|---|---|---|
| Note | If the publisher node is not synchronized with an NTP server, installation of the subscriber node will fail. |
| Step 2 | On the First Node Configuration window, read the Warning and make sure that you have correctly configured the first node as
                                          the publisher node. To continue with the installation of the subscriber node, click OK. The Network Connectivity Test Configuration window displays. |
| Step 3 | During
                                          			 installation of a subscriber node, the system checks to ensure that the
                                          			 subscriber node can connect to the publisher node. To pause the
                                                   					 installation after the system successfully verifies network connectivity,
                                                   					 choose Yes. To continue
                                                   					 the installation with a pause, choose No. The First Node
                                             				Access Configuration window displays. |
| Step 4 | Enter the
                                          			 publisher node connectivity information and choose OK. The system
                                             				checks for network connectivity. If you chose to
                                             				pause the system after the system successfully verifies network connectivity,
                                             				the Successful Connection to First Node window displays. Choose Continue. Note If the network
                                                         				  connectivity test fails, the system always stops and allows you to go back and
                                                         				  reenter the parameter information. The SMTP
                                                				  Host Configuration window displays. | Note | If the network
                                                         				  connectivity test fails, the system always stops and allows you to go back and
                                                         				  reenter the parameter information. |
| Note | If the network
                                                         				  connectivity test fails, the system always stops and allows you to go back and
                                                         				  reenter the parameter information. |
| Step 5 | If you want to
                                          			 configure an SMTP server, choose Yes and enter the SMTP server name. Note To use certain
                                                         				  operating system features, you must configure an SMTP server; however, you can
                                                         				  also configure an SMTP server later by using the operating system GUI or the
                                                         				  command line interface. The Platform
                                             				Configuration Confirmation window displays. | Note | To use certain
                                                         				  operating system features, you must configure an SMTP server; however, you can
                                                         				  also configure an SMTP server later by using the operating system GUI or the
                                                         				  command line interface. |
| Note | To use certain
                                                         				  operating system features, you must configure an SMTP server; however, you can
                                                         				  also configure an SMTP server later by using the operating system GUI or the
                                                         				  command line interface. |
| Step 6 | Choose OK to start installing the software or choose Back to change the configuration. |
| Step 7 | When the
                                          			 installation process completes, you get prompted to log in by using the
                                          			 Administrator account and password. |

| Note | If the publisher node is not synchronized with an NTP server, installation of the subscriber node will fail. |
|---|---|

| Note | If the network
                                                         				  connectivity test fails, the system always stops and allows you to go back and
                                                         				  reenter the parameter information. |
|---|---|

| Note | To use certain
                                                         				  operating system features, you must configure an SMTP server; however, you can
                                                         				  also configure an SMTP server later by using the operating system GUI or the
                                                         				  command line interface. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate Answer Files for Touchless Install | Use this procedure to generate the configuration files (clusterconfig.xml and platformconfig.xml) with your network settings.
                                          The touchless install process uses these files to install and configure a single node or the various cluster nodes. |
| Step 2 | Generate Virtual Floppy Images | Use this procedure to create virtual floppy images from the answer files. You use the virtual floppy images in your touchless
                                          installation. |
| Step 3 | Upload Virtual Floppy Image to Datastore | Use this procedure to upload the virtual floppy images to the datastore. |
| Step 4 | Mount Floppy Image to VM | Use this procedure to mount the UC application virtual floppy images on their corresponding VM. |
| Step 5 | Run Touchless Install | Begin the single node or cluster installation. You can kick off all node installations simultaneously. |

| Step 1 | Log in to the Cisco Unified Communications Answer File Generator application at https://www.cisco.com/c/en/us/applicat/content/cuc-afg/index.html . |
|---|---|
| Step 2 | In the Hardware section, choose Virtual Machine . |
| Step 3 | From the Product section, select the product and version that you want to install. |
| Step 4 | In the Software Location of Data to Import section, check the Configure Software Location of Data to Import check box to configure Remote SFTP server details only if you choose to install using the Fresh Install with Data Import.
                                          Else ignore this step and proceed to step 5. For more details, see Install with Data Import installation method. By checking the Configure Software Location of Data to Import check box it disables, Administrator Credentials, Security Password, Application User Credentials fields. These details are
                                             imported from source node data during installation. Enter the following fields: Remote Server Name or IP —The Secure FTP (SFTP) server that stores the source cluster's exported data. Export Data Directory —Directory path of the server containing export data. Remote Server Login ID —Allows data retrieval of the remote SFTP server. Remote Server Password —Can contain alphanumeric characters, hyphens, and underscores. |
| Step 5 | Complete the remaining fields under Clusterwide Configuration with your cluster configuration details. |
| Step 6 | Complete the fields in the Primary Node Configuration with configuration details for the publisher node. |
| Step 7 | Check the Dynamic Cluster Config Enable check box and enter a value, in hours, for the Dynamic cluster Config Timer. Note This check box must be checked if you want to install your full cluster in a single process. Otherwise, you will need to either
                                                      configure this option later through the CLI, or add your subscriber nodes manually after the publisher node installs. | Note | This check box must be checked if you want to install your full cluster in a single process. Otherwise, you will need to either
                                                      configure this option later through the CLI, or add your subscriber nodes manually after the publisher node installs. |
| Note | This check box must be checked if you want to install your full cluster in a single process. Otherwise, you will need to either
                                                      configure this option later through the CLI, or add your subscriber nodes manually after the publisher node installs. |
| Step 8 | Under Secondary Node Configuration , enter the node details for your first subscriber node and click Add Secondary Node . |
| Step 9 | Add all your subscriber nodes. |
| Step 10 | Add all your cluster nodes and click Generate Answer files . |
| Step 11 | Download the answer files to your computer. |
| Step 12 | Repeat this procedure to generate answer files for the IM and Presence Service cluster. |

| Note | This check box must be checked if you want to install your full cluster in a single process. Otherwise, you will need to either
                                                      configure this option later through the CLI, or add your subscriber nodes manually after the publisher node installs. |
|---|---|

| Note | This procedure describes how to use Winimage to create virtual floppy images. You can download Winimage from http:/​/​www.winimage.com/​download.htm . You can also use other tools, such as BFI, to create virtual floppy images. |
|---|---|

| Step 1 | From Winimage, choose File > New . |
|---|---|
| Step 2 | From the Standard format, choose 1.44 MB and click OK . |
| Step 3 | Navigate to the Menu Image, choose Inject and select the platformConfig.xml file. |
| Step 4 | When prompted to inject the file into Winimage, click Yes . |
| Step 5 | Choose File > Save As . |
| Step 6 | Save the file as a virtual floppy image (.flp file) using the following naming conventions: Unified Communications Manager— ucm.flp IM and Presence Service— imp.flp |
| Step 7 | Repeat these steps for both the Unified Communications Manager cluster and the IM and Presence Service cluster. |

| Step 1 | Start the vSphere client. |
|---|---|
| Step 2 | Select the Configuration tab. |
| Step 3 | Select Storage . |
| Step 4 | Right-click on a datastore and Browse the datastore. |
| Step 5 | Navigate to the destination directory and click the Upload files to this datastore icon. |
| Step 6 | Upload the vFloppy images to your local folder. |
| Step 7 | At the Upload/Download warning, click Yes . |
| Step 8 | Close the Datastore Browser window. |

| Step 1 | In the vSphere client, choose the virtual machine. |
|---|---|
| Step 2 | Open VMware Remote Console (VMRC), and click the Floppy drive . |
| Step 3 | Select Use existing floppy image in datastore . |
| Step 4 | Browse to the datastore and locate the virtual floppy image. |
| Step 5 | Select the file and click OK . |
| Step 6 | Under Device Status , enable the Connected and Connect at power on option. |
| Step 7 | Click the Options tab. Under Boot Options , check Force entry to BIOS and click OK . |
| Step 8 | Repeat this procedure for each VM on which you want to install a node. |

| Step 1 | In vSphere client, right-click the VM and select Open Console . A console window opens. |
|---|---|
| Step 2 | Click the Power On icon in the console tool bar to power on the virtual machine. |
| Step 3 | When the BIOS screen appears, configure the following boot order: CD-Rom Hard Drive Removable Devices Network |
| Step 4 | Save the settings and exit from the console. The installation commences immediately. |
| Step 5 | Repeat these steps for each cluster node. All cluster nodes may install in parallel; you do not have to install them serially. |
| Step 6 | After to emphasise the completion of an activity, remove the vFloppy configurations from the virtual machines. |

|  | Procedure | Description |
|---|---|---|
| Step 1 | Run a full backup of the cluster. | For details, see the "Manage Backups" chapter of the Administration Guide for Cisco Unified Communications Manager . |
| Step 2 | Basic Installation | Begin the install process. |
| Step 3 | Configure Basic Installation | Continue with the Basic Installation process by configuring your installation. |
| Step 4 | Add Subscriber Nodes | Add subscriber nodes to Unified Communications Manager publisher. |
| Step 5 | Install Subscriber Nodes | Install software on your subscriber nodes. |

|  | Procedure | Description |
|---|---|---|
| Step 1 | Run a full backup of the cluster. | For details, see the "Manage Backups" chapter of the Administration Guide for Cisco Unified Communications Manager . |
| Step 2 | Generate Answer Files for Touchless Install | Generate answer files for your installation. The touchless install process uses answer files to install and configure the
                                          various cluster nodes. |
| Step 3 | Generate Virtual Floppy Images | Create a virtual floppy image from the answer file. |
| Step 4 | Upload Virtual Floppy Image to Datastore | Upload the virtual floppy to the datastore. |
| Step 5 | Mount Floppy Image to VM | Mount the virtual floppy to the virtual machine. |
| Step 6 | Run Touchless Install | Install the software. |

| Important | After you install a new node on an existing cluster, if you plan to utilize Cisco CallManager or Cisco TFTP services, we recommend
                                       that you restart all of the phones in your cluster to get the latest ITL file. If you are using a Certificate Trust List (CTL),
                                       you will also need to update this file manually by running the utils ctl update CTLFile CLI command (using Tokenless CTL) or by updating the file via the CTL Client (Legacy USB tokens). After you update the CTL
                                       file, you must restart phones so that they can download the latest CTL file. For additional details on the CTL File, see the
                                       “Cisco CTL Client Setup” chapter of the Security Guide for Cisco Unified Communications Manager . |
|---|---|

| Note | You can collect the logs from RTMT of a new node added to the existing FQDN cluster, only when you restart the trace collection
                                                service. When you sign in to Unified RTMT without restarting the trace collection, the following error message is displayed:
                                                . Could not connect to 'Server' <new node name> If you install a new node to an existing cluster where the IM and Presence server is not upgraded to the supported version
                                                or if the IM and Presence server has been decommissioned, the following error message is displayed: "Add failed. Upgrade and migration for Cisco Unified IM & Presence Servers that are associated with this cluster appears to
                                                   be pending (not complete). Please make sure upgrade and migration of all IM & Presence servers is completed successfully before
                                                   adding servers to this cluster. Please check for any unused IM & Presence Application Servers and delete them”. |
|---|---|

| Note | A touchless install cannot be used to simultaneously install multiple Unified Communications Manager and multiple IM and Presence
                                          Service nodes. The following scenarios are supported: Installing only multiple Unified Communications Manager nodes Installing only one Unified Communications Manager node (publisher) and multiple and IM and Presence Service nodes If you need to simultaneously install multiple Unified Communications Manager and IM and Presence Service nodes, you need
                                          to use one of the above scenarios and install additional nodes manually. |
|---|---|

| Important | Fresh Install with Data Import does not support domain name changes. If DNS is enabled on the publisher node of the destination
                                                cluster, the domain name must match the source cluster. If the domain name needs to change, install the destination cluster
                                                on the publisher without the DNS enabled and then enable DNS via the CLI after the installation is complete. The subscribers
                                                can be installed with the DNS enabled, but ensure that the System > Server entries on the publisher node are correct before installing the subscribers. If you plan to change the hostname and/or IP address during the migration, the System > Server entries must be updated on the publisher node of the destination cluster prior to installing the subscribers. Fresh Install with Data Import does not support installation with DHCP configuration. If DHCP is enabled on the source cluster,
                                                install the destination cluster with Static configuration data and then configure the DHCP later post migration. |
|---|---|

| Note | Ensure that all nodes in the cluster are exported to the SFTP server before proceeding with Fresh Install with Data Import. |
|---|---|

| Step 1 | Export data from the source cluster publisher node. Run the utils system upgrade dataexport initiate CLI command on each node of the desired source system to export the data which can be imported using this procedure. Enter the SFTP server information to export the data. Enter the node Hostname and IP Address (it is possible to change them at this stage.) Run the utils system upgrade dataexport status to track the export status. A new folder is created at the SFTP server with the cluster name: Publisher IP Address. |
|---|---|
| Step 2 | Export data from the source cluster subscriber node. Run the utils system upgrade dataexport initiate CLI command on each node of the desired source system to export the data which can be imported using this procedure. Enter the SFTP server information to export data. Enter the node Hostname and IP Address (it is possible to change them at this stage). Run the utils system upgrade dataexport status to track the export status. The exported subscriber data is stored in the same cluster folder: Publisher IP Address. |
| Step 3 | Repeat Step 2 for the remaining subscriber nodes. |
| Step 4 | Then proceed with one of the following methods to complete installation/import. Note During the configuration of an IP address, if the source and destination clusters are using DHCP, ensure that you configure
                                                      a static IP address for the destination cluster. For example, the current IP address of the source cluster. Installation Method See Attended Install Install a new publisher and import the data. To configure Unified Communications Manager and IM and Presence Service with Install with Data Import follow the instructions as described in Basic Installation from step 1 through 6. In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Unified Communications Manager
                                                            and IM and Presence Service installation. In the import wizard, provide details for the following information: Hostname, IP Address, Subnet mask, and Gateway. This must be the same information provided in the destination node for which
                                                                  you exported the data. SFTP—In the export data directory, enter the exported data folder name or cluster information: <Publisher IP Address>. Confirm whether this is the First Node. Enter one or more NTP servers. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. Install a new Subscriber and import the data. Repeat step 4 except for the First Node question. Respond to this query with
                                                            a 'No' and provide the new publisher IP Address and hostname information. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. Touchless Install of a Single Node or a Cluster Follow the instructions as described in Touchless Installation Task Flow from step 1 through 5. Note If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command. | Note | During the configuration of an IP address, if the source and destination clusters are using DHCP, ensure that you configure
                                                      a static IP address for the destination cluster. For example, the current IP address of the source cluster. | Installation Method | See | Attended Install | Install a new publisher and import the data. To configure Unified Communications Manager and IM and Presence Service with Install with Data Import follow the instructions as described in Basic Installation from step 1 through 6. In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Unified Communications Manager
                                                            and IM and Presence Service installation. In the import wizard, provide details for the following information: Hostname, IP Address, Subnet mask, and Gateway. This must be the same information provided in the destination node for which
                                                                  you exported the data. SFTP—In the export data directory, enter the exported data folder name or cluster information: <Publisher IP Address>. Confirm whether this is the First Node. Enter one or more NTP servers. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. Install a new Subscriber and import the data. Repeat step 4 except for the First Node question. Respond to this query with
                                                            a 'No' and provide the new publisher IP Address and hostname information. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. | Touchless Install of a Single Node or a Cluster | Follow the instructions as described in Touchless Installation Task Flow from step 1 through 5. | Note | If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command. |
| Note | During the configuration of an IP address, if the source and destination clusters are using DHCP, ensure that you configure
                                                      a static IP address for the destination cluster. For example, the current IP address of the source cluster. |
| Installation Method | See |
| Attended Install | Install a new publisher and import the data. To configure Unified Communications Manager and IM and Presence Service with Install with Data Import follow the instructions as described in Basic Installation from step 1 through 6. In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Unified Communications Manager
                                                            and IM and Presence Service installation. In the import wizard, provide details for the following information: Hostname, IP Address, Subnet mask, and Gateway. This must be the same information provided in the destination node for which
                                                                  you exported the data. SFTP—In the export data directory, enter the exported data folder name or cluster information: <Publisher IP Address>. Confirm whether this is the First Node. Enter one or more NTP servers. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. Install a new Subscriber and import the data. Repeat step 4 except for the First Node question. Respond to this query with
                                                            a 'No' and provide the new publisher IP Address and hostname information. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. |
| Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. |
| Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. |
| Touchless Install of a Single Node or a Cluster | Follow the instructions as described in Touchless Installation Task Flow from step 1 through 5. |
| Note | If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command. |

| Note | During the configuration of an IP address, if the source and destination clusters are using DHCP, ensure that you configure
                                                      a static IP address for the destination cluster. For example, the current IP address of the source cluster. |
|---|---|

| Installation Method | See |
|---|---|
| Attended Install | Install a new publisher and import the data. To configure Unified Communications Manager and IM and Presence Service with Install with Data Import follow the instructions as described in Basic Installation from step 1 through 6. In the Platform Installation Wizard window, choose Import from the various options that are provided to import data from the SFTP server during the Unified Communications Manager
                                                            and IM and Presence Service installation. In the import wizard, provide details for the following information: Hostname, IP Address, Subnet mask, and Gateway. This must be the same information provided in the destination node for which
                                                                  you exported the data. SFTP—In the export data directory, enter the exported data folder name or cluster information: <Publisher IP Address>. Confirm whether this is the First Node. Enter one or more NTP servers. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. Install a new Subscriber and import the data. Repeat step 4 except for the First Node question. Respond to this query with
                                                            a 'No' and provide the new publisher IP Address and hostname information. Note If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. | Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. |
| Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. |
| Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. |
| Touchless Install of a Single Node or a Cluster | Follow the instructions as described in Touchless Installation Task Flow from step 1 through 5. |

| Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. |
|---|---|

| Note | If you are planning to use the same Hostname/IP Address, ensure that the older publisher node is shut down before installing
                                                                        a new publisher node. |
|---|---|

| Note | If you are planning to use DHCP for the cluster node IP addresses, enable this configuration using the set network dhcp eth0 command. |
|---|---|