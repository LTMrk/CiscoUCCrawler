---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-install-14-su2-cucm-b-install-guide-cucm-imp-14su2-cucm-b-install-guide-4decceccc1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/install/14_SU2/cucm_b_install-guide-cucm-imp-14su2/cucm_b_install-guide-cucm-imp-14_chapter_011.html
retrieved_at: 2026-08-17T00:06:14.649486+00:00
---

Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 14SU2

# Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 14SU2

Updated: June 30, 2025

Chapter: Postinstallation Tasks

## Chapter: Postinstallation Tasks

# Postinstallation Tasks

## Postinstall Tasks for Cisco Unified Communications Manager

Step 1

Read the Release Notes and any Readme files that come with your release.

You can download Release Notes from the below URL.  Make sure that you understand the features for your release and any COP
                                          file requirements.

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html

Step 2

Configure Software Location on cluster nodes that will be used for future upgrades and COP Installs.

Before you attempt to upgrade any cluster nodes or install any COP files on the cluster nodes, all cluster nodes need to have
                                          their Software Location fields configured. For more information on configuring software location details, see the 'Configure
                                          Cluster Software Location' section in the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service from Releases 12.5(1)SU6 and 14SU2 onwards.

Step 3

Reset Application User Passwords

We recommend that you reset your application user passwords post installation.

Step 4

Install the Real-Time Monitoring Tool

You can use the Cisco Unified Real-Time Monitoring Tool (RTMT) to monitor Unified Communications Manager and the IM and Presence
                                          Service in real time.

Step 5

Enable the Kerneldump Utility

If you have a kernel crash, the kerneldump utility provides a mechanism for collecting and dumping the crash.

Step 6

Install Licenses

Verify that you have the required licenses for your system and devices.

Step 7

Configure the Backup

We recommend performing regular backups. You can set up automatic backups or invoke a backup at any time.

Step 8

Install New Locales

Optional. The default locale is US - English. If you want to use a different locale, download and install it.

Step 9

COP File Installation Guidelines

You may need to install a COP file after the installation to fix a known defect, or to enable support for a custom device
                                          type that you want to use that does not ship with Unified Communications Manager.

Step 10

Install a dial plan by completing these tasks:

- Install a COP File

- Install a Prebuilt Dial Plan

- Restart the Cisco CallManager Service

If you want to use a dial plan other than the North American Numbering Plan (the default), you must download and install
                                          it.

Step 11

Activate Security

Optional. If you want to enable security on your system, install
                                          the Cisco CTL Client and enable mixed mode.

Step 12

Configure the Simple Network Management Protocol

Optional.  If you are using a Network Management System such as Cisco Prime Collaboration Assurance, enable the Simple Network
                                          Management Protocol.

Step 13

Change Virtual Machine Configuration Specifications

To change to the Guest OS version in the Cisco Unified Communications Manager virtual machine (VM) settings.

Step 14

Ensure that you configure the Trusted List of Hosts in HTTP Referer/Host Header and add the public IP address or DNS alias in the Cisco Unified CM Administration Enterprise Parameters page.

This configuration is necessary if your network topology has public IP address configured for external interfaces along with
                                          private IP address for the individual nodes in the cluster. Unified CM will now validate the IP address or hostname present
                                          in the Host header with the servers configured in the Unified CM cluster first before allowing access to Unified CM. You must
                                          also configure the DNS alias used to access the Unified CM under the Trusted List of Hosts configuration. For example, if
                                          your server is cm1.example.local, and you use phone.example.local to access the server, you must add phone.example.local to
                                          the Trusted List of Hosts configuration.

From the private network using a private IP address, navigate to the Cisco Unified CM Administration user interface and select System > Enterprise Parameters to configure the external IP addresses or DNS alias used.

You must restart the Cisco Tomcat service after performing this activity for all the web pages to load correctly.

### Reset Application User Passwords

The install process sets all Application User passwords to the same default Application User password that you entered during
                                 installation. We recommend that you reset all these passwords post installation.

Step 1

From Cisco Unified CM Administration, choose User Management > Application User .

Step 2

Click Find .

Step 3

Click an application user.

Step 4

Enter the new password in both the Password and Confirm Password fields.

Step 5

Click Save .

Step 6

Repeat this procedure for each application user.

### Install the Real-Time Monitoring Tool

Use this procedure to install the Cisco Unified Real-Time Monitoring Tool (RTMT). You can use RTMT to monitor Unified Communications
                                 Manager and the IM and Presence Service in real time.

#### Before you begin

Unified RTMT
                                       				requires at least 128 MB in memory to run on a Windows OS platform; the tool
                                       				requires at least 300 MB of disk space to run on a Windows/Linux OS platform.

The Linux
                                                   				  Unified RTMT plugin CcmServRtmtPlugin.bin can be installed on RHEL 5, RHEL 6,
                                                   				  or higher Linux machines. If you want to install it on a RHEL 4 machine, ensure
                                                   				  that the glibc (OS library) version is 2.4.x or higher. If the glibc version is
                                                   				  2.3.x or earlier, the underlying JRE install fails.

- The current Unified RTMT download supports earlier releases of Unified Communications Manager or Cisco Unity Connection. Some
                                    releases of Unified Communications Manager may require different versions of Unified RTMT to be installed on your computer
                                    (one version per Unified Communications Manager release). Verify that the Unified RTMT version that you install is compatible
                                    with the product that you are monitoring. If the Unified RTMT version that you are using is not compatible with the server
                                    that you want to monitor, the system prompts you to download the compatible version.

- Your computer stores the
                                    			 user preferences, such as the IP address and Unified RTMT frame size, based on
                                    			 the last instance of Unified RTMT that you run.

Only the
                                             			 administrators with Standard Audit Users and Standard CCM Super Users
                                             			 privileges have access to Unified RTMT features. If an application user without
                                             			 these privileges logs into Unified RTMT, some of the features such as Call
                                             			 Control Discovery (CCD) and Service Advertisement Framework (SAF) will not work
                                             			 as expected.

On a Linux
                                             			 workstation, run RTMT with root access. Otherwise, when you initially install
                                             			 RTMT, the application will not start.

The current Unified RTMT requires JRE to run. Verify that the
                                       				system has JRE installed (Java 1.8).

Step 1

Go to the Plug-ins window of the administration interface for
                                          			 your configuration:

Interface

How
                                                         							 to access

Unified Communications Manager

From Unified Communications Manager Administration, choose Application > Plugins .

Unified Communications Manager IM and Presence Service

From Unified Communications Manager IM and Presence Administration, choose Application > Plugins .

Cisco Unity Connection

From Cisco Unity Connection Administration, choose System Settings > Plugins .

Step 2

Click Find .

Step 3

To install
                                          			 Unified RTMT on a client that is running the Microsoft Windows operating
                                          			 system, click the Download link for the Real-Time Monitoring Tool -
                                          			 Windows.

To install
                                             				Unified RTMT on a client that is running the Linux operating system, click the Download link for the Real-Time Monitoring Tool -
                                             				Linux.

Tip

When you
                                                         				  install Unified RTMT on Windows 7 or later, ensure that you perform the
                                                         				  installation as an administrator.

Step 4

Download the
                                          			 executable to the preferred location on your client.

Step 5

To install the
                                          			 Windows version, double-click the Unified RTMT icon that appears on the desktop
                                          			 or locate the directory where you downloaded the file and run the Unified RTMT
                                          			 installation file.

The extraction
                                             				process begins.

Step 6

To install the Linux version, ensure that the file has execute privileges; for example, enter the following command, which
                                          is case sensitive: chmod +x CcmServRtmtPlugin.bin .

Step 7

After the
                                          			 Unified RTMT welcome window appears, click Next .

Step 8

To accept the
                                          			 license agreement, click I
                                             				accept the terms of the license agreement ; then, click Next .

Step 9

Choose the absolute path of Java Virtual Machine executable from
                                          			 your system (java.exe from the JRE installed directory, that is latest version
                                          			 1.8) as prompted in the installation screen of Unified RTMT.

Step 10

Choose the
                                          			 location where you want to install Unified RTMT. If you do not want to use the
                                          			 default location, click Browse and navigate to a different location. Click Next .

Step 11

To begin the
                                          			 installation, click Next .

The Setup
                                                				  Status window appears.

Step 12

To complete
                                          			 the installation, click Finish .

For more details on how to use the Real-Time Monitoring Tool, refer to the Cisco Unified Real-Time Monitoring Tool Administration Guide .

### Enable the Kerneldump Utility

Use this procedure to enable the kerneldump utility. In the event of a kernel crash, the utility provides a mechanism for
                                 collecting and dumping the crash. You can configure the utility to dump the core to either the local server, or to an external
                                 server.

Step 1

Log in to the Command Line Interface.

Step 2

Complete either of the following:

- To dump kernel crashes on the local server, run the utils os kerneldump enable CLI command.

- To dump kernel crashes to an external server, run the utils os kerneldump ssh enable <ip_address> CLI command with the IP address of the external server.

Step 3

Reboot the server.

### Install Licenses

Make sure that you acquire the necessary licenses.

#### Unified Communications Manager Requirements

Use Cisco Smart Software Manager or Cisco Smart Software Manager satellite to manage licenses for Unified Communications Manager.
                                 For details on how to acquire licenses, see the "Smart Software Licensing" chapter of the System Configuration Guide for Cisco Unified Communications Manager .

#### IM and Presence Service Requirements

The IM and Presence Service does not require a server license or software version license.

### Configure the Backup

We recommend performing regular backups. You can use the Disaster Recovery System (DRS) to do a full data backup for all servers
                                 in a cluster. You can set up automatic backups or invoke a backup at any time.

You can initiate a manual backup or configure a backup schedule. For more details, see the "Backup the System" chapter of
                                 the Administration Guide for Cisco Unified Communications Manager .

### Locale Installation

You can configure Unified Communications Manager and IM and Presence Service to support multiple languages. There is no limit
                                 to the number of supported languages you can install.

Cisco provides locale-specific versions of the Unified Communications Manager Locale Installer and the IM and Presence Service
                                 Locale Installer on www.cisco.com. Installed by the system administrator, the locale installer allows the user to view/receive
                                 the chosen translated text or tones, if applicable, when a user works with supported interfaces.

For upgrades of Unified Communications Manager or the IM & Presence Service, you must install locales after you have completed
                                 all your upgrades and migrations. For upgrades, you must reinstall any locales that you are using, except for US-English,
                                 which is installed by default. Install the latest version of the locales that match the major.minor version number of your
                                 Unified Communications Manager node or IM and Presence Service node.

Install locales after you have installed Unified Communications Manager on every node in the cluster and have set up the database.
                                 If you want to install specific locales on IM and Presence Service nodes, you must first install the Unified Communications
                                 Manager locale file for the same country on the Unified Communications Manager cluster.

Use the information in the following sections to install locales on Unified Communications Manager nodes and on IM and Presence
                                 Service nodes after you complete the software upgrade.

#### User Locales

User locale files contain language information for a specific language and country. They provide translated text and voice
                                 prompts, if available, for phone displays, user applications, and user web pages in the locale that the user chooses. These
                                 files use the following naming convention:

cm-locale-language-country-version.cop (Unified Communications Manager)

ps- locale-language_country-version.cop (IM and Presence Service)

#### Network Locales

Network locale files provide country-specific files for various network items, including phone tones, annunciators, and gateway
                                 tones. The combined network locale file uses the following naming convention:

cm-locale-combinednetworklocale-version.cop (Unified Communications Manager)

Cisco may combine multiple network locales in a single locale
                                 installer.

You can install locale files from either a local or a remote source by using the same process for installing software upgrades.
                                 You can install more than one locale file on each node in the cluster. Changes do not take effect until you reboot every node
                                 in the cluster. We strongly recommend that you do not reboot the nodes until you have installed all locales on all nodes in
                                 the cluster. Minimize call-processing interruptions by rebooting the nodes after regular business hours.

#### Install New Locales

Use this procedure to install a new locale on Unified Communications Manager or IM and Presence Service. If you are installing
                                    a locale for both products, install the locale on all cluster nodes in the following order:

Unified Communications Manager publisher node

Unified Communications Manager subscriber nodes

IM and Presence database publisher node

IM and Presence subscriber nodes

##### Before you begin

Make sure that you have completed your installation or upgrade of Unified Communications Manager or IM and Presence Service
                                    on all cluster nodes before you attempt to install a new locale.

Step 1

Find the locale installer for your release on cisco.com:

- For Unified Communications Manager, go to https://software.cisco.com/download/navigator.html?mdfid=268439621&i=rm

- For IM and Presence Service, go to https://software.cisco.com/download/navigator.html?mdfid=280448682&i=rm

Step 2

Download your release's locale installer to a server that supports SFTP.

Step 3

Log in to Cisco Unified OS Administration using the administrator account.

Step 4

Choose Software Upgrades > Install/Upgrade .

Step 5

Complete the following fields in the Software Installation/Upgrade window:

- For the Source , choose Remote file System .

- From the Directory , enter the path to the directory where you saved the locale installer.

- From the Server field, enter the server name for the remote file system.

- Enter the credentials for the remote file system.

- From the Transfer Protocol drop-down list, choose SFTP . You must use SFTP for the transfer protocol.

Step 6

Click Next .

Step 7

Download and install the locale on the server.

Step 8

Restart the server. The updates take effect after the server restarts.

Step 9

Repeat this procedure on all Unified Communications Manager and IM and Presence Service cluster nodes in the prescribed order.

##### What to do next

After the locale installation is complete for all cluster nodes, your end users can begin using the new user locale.

#### Error
                              	 Messages

See the
                                    		  following table for a description of the messages that can occur during Locale
                                    		  Installer activation. If an error occurs, you can view the messages in the
                                    		  installation log.

Message

Description

[LOCALE] File not found:
                                                					 <language>_<country>_user_locale.csv, the user locale has not been
                                                					 added to the database.

This error occurs when the system cannot locate the CSV file,
                                                					 which contains user locale information to add to the database. This indicates
                                                					 an error with the build process.

[LOCALE] File not found: <country>_network_locale.csv, the
                                                					 network locale has not been added to the database.

This error occurs when the system cannot locate the CSV file, which contains network locale information to add to the database.
                                                This indicates an error with the build process.

[LOCALE] Communications Manager CSV file installer installdb is not present or not executable.

This error occurs because a Unified Communications Manager application called installdb must be present; it reads information that is contained in a CSV file and applies it correctly
                                                to the Unified Communications Manager database. If this application is not found, it either was not installed with Unified Communications Manager (very unlikely), has been deleted (more likely), or the node does not have Unified Communications Manager installed (most likely). Installation of the locale terminates because locales do not work without the correct records that
                                                are held in the database.

[LOCALE] Could not create /usr/local/cm/application_locale /cmservices/ipma/com/cisco/ipma /client/locales/maDialogs_<ll>_<CC>.properties.Checksum.

[LOCALE] Could not create
                                                					 /usr/local/cm/application_locale/cmservices/ipma/com/cisco/
                                                					 ipma/client/locales/maMessages_<ll>_<CC>.properties.Checksum.

[LOCALE] Could not create /usr/local/cm/
                                                					 application_locale/cmservices/ipma/com/cisco/
                                                					 ipma/client/locales/maGlobalUI_<ll>_<CC>.properties.Checksum.

[LOCALE] Could not create /usr/local/cm/
                                                					 application_locale/cmservices/ipma/ LocaleMasterVersion.txt.Checksum.

These errors could occur when the system fails to create a checksum file; causes can include an absent Java executable, /usr/local/thirdparty/java/j2sdk/ jre/bin/java , an absent or damaged Java archive file, /usr/local/cm/jar/cmutil.jar , or an absent or damaged Java class, com.cisco.ccm.util.Zipper. Even if these errors occur, the locale will continue to work
                                                correctly, with the exception of Unified Communications Manager Assistant , which cannot detect a change in localized Unified Communications Manager Assistant files.

[LOCALE] Could not find
                                                					 /usr/local/cm/application_locale/cmservices/ipma/LocaleMaster Version.txt in
                                                					 order to update UnifiedCMAssistant locale information.

This error occurs when the file does not get found in the
                                                					 correct location, which is most likely due to an error in the build process.

[LOCALE] Addition of <RPM-file-name> to the Unified Communications Manager database has failed!

This error occurs because of the collective result of any
                                                					 failure that occurs when a locale is being installed; it indicates a terminal
                                                					 condition.

### COP File Installation Guidelines

Depending on your installation, you may need to install a COP file after the installation to fix a known defect, or to enable
                                 support for a custom device type that you want to use that does not ship with Unified Communications Manager.

If you need to install a COP file, follow these guidelines:

Install the appropriate COP file on every node in a cluster. Perform this task before you install new software on each node
                                       in the cluster and after set up the database.

After you install a COP file, you must restart the node.

Restart Unified Communications Manager and/or the IM and Presence Service to ensure that configuration changes that are made
                                       during the COP file installation get written into the database.

### Install a COP File

If you want to use a prebuilt Dial Plan other than the North American Numbering Plan (the system default), you must install
                                 a COP file with your dial plan.

Step 1

Begin this procedure on the Unified Communications Manager publisher node. From Cisco Unified Communications OS Administration, choose Software Upgrades > Install .

Step 2

In the Source field, choose Remote File System .

Step 3

Configure the fields on the Software Installation/Upgrade window. See the Related Topics for more information about the fields and their configuration options.

Step 4

Click Next .

Step 5

From the Options/Upgrades drop-down list, choose the DP COP file and click Next .

Step 6

When the Checksum window appears, verify the checksum value against the checksum for the file that you downloaded.

Step 7

Click Next to proceed with the software upgrade.

Step 8

Click Install .

Step 9

Click Finish .

Step 10

Repeat this procedure on the Unified Communications Manager subscriber nodes. You must install the COP file on all the nodes in the cluster.

#### What to do next

To apply the dial plan to the system, Install a Prebuilt Dial Plan .

### Install a Prebuilt Dial Plan

Install the national numbering plan on each Unified Communications Manager node in the cluster beginning. Begin with the Unified
                                 Communications Manager publisher node.

Complete this procedure only if you are installing a national numbering plan for countries outside of North America (the system
                                             default).

#### Before you begin

Install a COP file with your prebuilt dial plan. For details, see Install a COP File .

Step 1

From Cisco
                                          			 Unified Communications Manager Administration, choose Call Routing > Dial Plan
                                                				  Installer .

Step 2

Enter search criteria and click Find .

Step 3

Choose the
                                          			 dial plan version that you want to install from the Available Version drop-down
                                          			 list.

Step 4

Click Install .

Step 5

Repeat this
                                          			 procedure for every subscriber node in the cluster.

#### What to do next

Restart the Cisco CallManager Service

### Restart the Cisco CallManager Service

If you have installed a new dial plan, you must restart the Cisco CallManager service.

Step 1

From the Cisco Unified Serviceability interface, choose Tools > Control Center - Feature Services .

Step 2

Choose the Unified Communications Manager server from the Servers drop-down list.

Step 3

Click the radio button that corresponds to the Cisco CallManager service.

Step 4

Click Restart .

### Activate Security

If you want to enable security on your system, you must install
                                 the Cisco CTL Client and enable mixed mode. You can download the CTL installation file in Cisco Unified CM Administration
                                 from the Applications > Plugins window.

When mixed mode is enabled, the system uses the Certificate
                                 Trust List (CTL) file for authentication. The CTL file  contains a server certificate,
                                 public key, serial number, signature, issuer name, subject name,
                                 server function, DNS name, and IP address for each
                                 server.

For details on how to install the CTL client and enable mixed mode on your system, see the Security Guide for Cisco Unified Communications Manager .

### Configure the Simple Network Management Protocol

If you are using a Network Management System, such as Cisco Prime Collaboration Assurance, enable the Simple Network Management
                                 Protocol.

#### Before you begin

Your system does not allow more than ten concurrent polling queries. We recommend a maximum of eight trap destinations; anything
                                 higher will affect CPU performance. This requirement applies to all installations regardless of the OVA template that you
                                 use.

Step 1

Install and configure the SNMP NMS.

Step 2

In the Control Center - Network Services window,
                                          			 verify that the system started the SNMP services.

Step 3

Unified Communications Manager: In the Service Activation window, activate the Cisco
                                          			 CallManager SNMP service. Cisco Unity Connection only: The Connection SNMP Agent service
                                          			 automatically activates.

Step 4

If you are using SNMP V1/V2c, configure the community string.

Step 5

If you are using SNMP V3, configure the SNMP user.

Step 6

Configure the notification destination for traps or informs.

Step 7

Configure the system contact and location for the MIB2 system
                                          			 group.

Step 8

Configure trap settings for CISCO-SYSLOG-MIB.

Step 9

Unified Communications Manager only: Configure trap settings for
                                          			 CISCO-CCM-MIB.

Step 10

Restart the Primary Agent service.

Step 11

On the NMS, configure the Unified Communications Manager trap parameters.

### Change Virtual Machine Configuration Specifications

Use the following procedure to change to the Guest OS version in the Unified Communications Manager virtual machine (VM) settings.

Step 1

Shut down the virtual machine.

Step 2

Change the configuration of the virtual machine as needed through vSphere. You can update the Guest OS and VM Hardware Compatibly.

Update VM Hardware Compatibly—Left click Virtual Machine. Check for Updates . Click Update

If you are not aware of the host click Check statuts and click Upgrade to match host.

Update Guest OS—Right click the Virtual Machine > Edit Settings > Virtual Machine Option > General Option > Guest OS Version .

Step 3

Power on the Virtual Machine.

Following warning messages appears in ESXi while opening the Virtual Machine settings while running when there is a mismatch.

Warning

The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                         running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations.

## Postinstall tasks for the IM and Presence Service

If you have installed a new cluster or new node
                              for the IM and Presence Service, complete these tasks after your
                              installation.

Many of these tasks are documented in more detail in the Configuration and Administration of the IM and Presence Service Guide . Where indicated, see that guide for detail on how to complete these tasks.

Step 1

Read the Release Notes and any Readme files that come with your release.

You can download Release Notes from the below URL.  Make sure that you understand the features for your release and any COP
                                          file requirements.

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html

Step 2

Check for software and firmware updates for IM and Presence Service on Cisco.com.

You can download software from https://software.cisco.com/download/navigator.html?mdfid=280448682&i=rm

Step 3

Configure Presence Redundancy Groups.

For details, see the Configuration and Administration of the IM and Presence Service Guide .

Step 4

Change the default domain.

For details, see the Configuration and Administration of the IM and Presence Service Guide .

Step 5

Change the IM and Presence Service IM address scheme.

For details, see the Configuration and Administration of the IM and Presence Service Guide .

Step 6

Change the IM and Presence Service node name.

For details, see the Configuration and Administration of the IM and Presence Service Guide .

Step 7

Configure Unified Communications Manager as a Presence Gateway.

For details, see the Configuration and Administration of the IM and Presence Service Guide .

Step 8

Configure a SIP Publish trunk on Unified Communications Manager.

For details, see the Configuration and Administration of the IM and Presence Service Guide .

Step 9

Assign users to servers.

For details, see the Configuration and Administration of the IM and Presence Service Guide .

Step 10

Activate services

Turn on essential IM and Presence Service services.

### Activate services

You must activate the following services:

- Cisco SIP Proxy

- Cisco Presence Engine

- Cisco XCP Connection
                                    			 Manager

- Cisco XCP
                                    			 Authentication Service

To activate the services, select Tools > Service Activation in Cisco Unified Serviceability.

You must complete this task on each server that you install in an IM and Presence cluster.

## Where to Go Next

System Configuration Guide for Cisco Unified Communications Manager

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Read the Release Notes and any Readme files that come with your release. | You can download Release Notes from the below URL.  Make sure that you understand the features for your release and any COP
                                          file requirements. https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html |
| Step 2 | Configure Software Location on cluster nodes that will be used for future upgrades and COP Installs. | Before you attempt to upgrade any cluster nodes or install any COP files on the cluster nodes, all cluster nodes need to have
                                          their Software Location fields configured. For more information on configuring software location details, see the 'Configure
                                          Cluster Software Location' section in the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service from Releases 12.5(1)SU6 and 14SU2 onwards. |
| Step 3 | Reset Application User Passwords | We recommend that you reset your application user passwords post installation. |
| Step 4 | Install the Real-Time Monitoring Tool | You can use the Cisco Unified Real-Time Monitoring Tool (RTMT) to monitor Unified Communications Manager and the IM and Presence
                                          Service in real time. |
| Step 5 | Enable the Kerneldump Utility | If you have a kernel crash, the kerneldump utility provides a mechanism for collecting and dumping the crash. |
| Step 6 | Install Licenses | Verify that you have the required licenses for your system and devices. |
| Step 7 | Configure the Backup | We recommend performing regular backups. You can set up automatic backups or invoke a backup at any time. |
| Step 8 | Install New Locales | Optional. The default locale is US - English. If you want to use a different locale, download and install it. |
| Step 9 | COP File Installation Guidelines | You may need to install a COP file after the installation to fix a known defect, or to enable support for a custom device
                                          type that you want to use that does not ship with Unified Communications Manager. |
| Step 10 | Install a dial plan by completing these tasks: Install a COP File Install a Prebuilt Dial Plan Restart the Cisco CallManager Service | If you want to use a dial plan other than the North American Numbering Plan (the default), you must download and install
                                          it. |
| Step 11 | Activate Security | Optional. If you want to enable security on your system, install
                                          the Cisco CTL Client and enable mixed mode. |
| Step 12 | Configure the Simple Network Management Protocol | Optional.  If you are using a Network Management System such as Cisco Prime Collaboration Assurance, enable the Simple Network
                                          Management Protocol. |
| Step 13 | Change Virtual Machine Configuration Specifications | To change to the Guest OS version in the Cisco Unified Communications Manager virtual machine (VM) settings. |
| Step 14 | Ensure that you configure the Trusted List of Hosts in HTTP Referer/Host Header and add the public IP address or DNS alias in the Cisco Unified CM Administration Enterprise Parameters page. | This configuration is necessary if your network topology has public IP address configured for external interfaces along with
                                          private IP address for the individual nodes in the cluster. Unified CM will now validate the IP address or hostname present
                                          in the Host header with the servers configured in the Unified CM cluster first before allowing access to Unified CM. You must
                                          also configure the DNS alias used to access the Unified CM under the Trusted List of Hosts configuration. For example, if
                                          your server is cm1.example.local, and you use phone.example.local to access the server, you must add phone.example.local to
                                          the Trusted List of Hosts configuration. From the private network using a private IP address, navigate to the Cisco Unified CM Administration user interface and select System > Enterprise Parameters to configure the external IP addresses or DNS alias used. You must restart the Cisco Tomcat service after performing this activity for all the web pages to load correctly. |

| Step 1 | From Cisco Unified CM Administration, choose User Management > Application User . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Click an application user. The details of the application user appear in the Application User Configuration window. |
| Step 4 | Enter the new password in both the Password and Confirm Password fields. |
| Step 5 | Click Save . |
| Step 6 | Repeat this procedure for each application user. |

| Note | The Linux
                                                   				  Unified RTMT plugin CcmServRtmtPlugin.bin can be installed on RHEL 5, RHEL 6,
                                                   				  or higher Linux machines. If you want to install it on a RHEL 4 machine, ensure
                                                   				  that the glibc (OS library) version is 2.4.x or higher. If the glibc version is
                                                   				  2.3.x or earlier, the underlying JRE install fails. |
|---|---|

| Note | Only the
                                             			 administrators with Standard Audit Users and Standard CCM Super Users
                                             			 privileges have access to Unified RTMT features. If an application user without
                                             			 these privileges logs into Unified RTMT, some of the features such as Call
                                             			 Control Discovery (CCD) and Service Advertisement Framework (SAF) will not work
                                             			 as expected. |
|---|---|

| Note | On a Linux
                                             			 workstation, run RTMT with root access. Otherwise, when you initially install
                                             			 RTMT, the application will not start. |
|---|---|

| Step 1 | Go to the Plug-ins window of the administration interface for
                                          			 your configuration: Interface How
                                                         							 to access Unified Communications Manager From Unified Communications Manager Administration, choose Application > Plugins . Unified Communications Manager IM and Presence Service From Unified Communications Manager IM and Presence Administration, choose Application > Plugins . Cisco Unity Connection From Cisco Unity Connection Administration, choose System Settings > Plugins . | Interface | How
                                                         							 to access | Unified Communications Manager | From Unified Communications Manager Administration, choose Application > Plugins . | Unified Communications Manager IM and Presence Service | From Unified Communications Manager IM and Presence Administration, choose Application > Plugins . | Cisco Unity Connection | From Cisco Unity Connection Administration, choose System Settings > Plugins . |
|---|---|---|---|---|---|---|---|---|---|
| Interface | How
                                                         							 to access |
| Unified Communications Manager | From Unified Communications Manager Administration, choose Application > Plugins . |
| Unified Communications Manager IM and Presence Service | From Unified Communications Manager IM and Presence Administration, choose Application > Plugins . |
| Cisco Unity Connection | From Cisco Unity Connection Administration, choose System Settings > Plugins . |
| Step 2 | Click Find . |
| Step 3 | To install
                                          			 Unified RTMT on a client that is running the Microsoft Windows operating
                                          			 system, click the Download link for the Real-Time Monitoring Tool -
                                          			 Windows. To install
                                             				Unified RTMT on a client that is running the Linux operating system, click the Download link for the Real-Time Monitoring Tool -
                                             				Linux. Tip When you
                                                         				  install Unified RTMT on Windows 7 or later, ensure that you perform the
                                                         				  installation as an administrator. | Tip | When you
                                                         				  install Unified RTMT on Windows 7 or later, ensure that you perform the
                                                         				  installation as an administrator. |
| Tip | When you
                                                         				  install Unified RTMT on Windows 7 or later, ensure that you perform the
                                                         				  installation as an administrator. |
| Step 4 | Download the
                                          			 executable to the preferred location on your client. |
| Step 5 | To install the
                                          			 Windows version, double-click the Unified RTMT icon that appears on the desktop
                                          			 or locate the directory where you downloaded the file and run the Unified RTMT
                                          			 installation file. The extraction
                                             				process begins. |
| Step 6 | To install the Linux version, ensure that the file has execute privileges; for example, enter the following command, which
                                          is case sensitive: chmod +x CcmServRtmtPlugin.bin . |
| Step 7 | After the
                                          			 Unified RTMT welcome window appears, click Next . |
| Step 8 | To accept the
                                          			 license agreement, click I
                                             				accept the terms of the license agreement ; then, click Next . |
| Step 9 | Choose the absolute path of Java Virtual Machine executable from
                                          			 your system (java.exe from the JRE installed directory, that is latest version
                                          			 1.8) as prompted in the installation screen of Unified RTMT. |
| Step 10 | Choose the
                                          			 location where you want to install Unified RTMT. If you do not want to use the
                                          			 default location, click Browse and navigate to a different location. Click Next . |
| Step 11 | To begin the
                                          			 installation, click Next . The Setup
                                                				  Status window appears. |
| Step 12 | To complete
                                          			 the installation, click Finish . |

| Interface | How
                                                         							 to access |
|---|---|
| Unified Communications Manager | From Unified Communications Manager Administration, choose Application > Plugins . |
| Unified Communications Manager IM and Presence Service | From Unified Communications Manager IM and Presence Administration, choose Application > Plugins . |
| Cisco Unity Connection | From Cisco Unity Connection Administration, choose System Settings > Plugins . |

| Tip | When you
                                                         				  install Unified RTMT on Windows 7 or later, ensure that you perform the
                                                         				  installation as an administrator. |
|---|---|

| Note | For more details on how to use the Real-Time Monitoring Tool, refer to the Cisco Unified Real-Time Monitoring Tool Administration Guide . |
|---|---|

| Step 1 | Log in to the Command Line Interface. |
|---|---|
| Step 2 | Complete either of the following: To dump kernel crashes on the local server, run the utils os kerneldump enable CLI command. To dump kernel crashes to an external server, run the utils os kerneldump ssh enable <ip_address> CLI command with the IP address of the external server. |
| Step 3 | Reboot the server. |

| Step 1 | Find the locale installer for your release on cisco.com: For Unified Communications Manager, go to https://software.cisco.com/download/navigator.html?mdfid=268439621&i=rm For IM and Presence Service, go to https://software.cisco.com/download/navigator.html?mdfid=280448682&i=rm |
|---|---|
| Step 2 | Download your release's locale installer to a server that supports SFTP. |
| Step 3 | Log in to Cisco Unified OS Administration using the administrator account. |
| Step 4 | Choose Software Upgrades > Install/Upgrade . |
| Step 5 | Complete the following fields in the Software Installation/Upgrade window: For the Source , choose Remote file System . From the Directory , enter the path to the directory where you saved the locale installer. From the Server field, enter the server name for the remote file system. Enter the credentials for the remote file system. From the Transfer Protocol drop-down list, choose SFTP . You must use SFTP for the transfer protocol. |
| Step 6 | Click Next . |
| Step 7 | Download and install the locale on the server. |
| Step 8 | Restart the server. The updates take effect after the server restarts. |
| Step 9 | Repeat this procedure on all Unified Communications Manager and IM and Presence Service cluster nodes in the prescribed order. |

| Note | Do not reset user locales for your end users until the new locale is installed on all cluster nodes. If you are installing
                                             the locale for both Unified Communications Manager and IM and Presence Service, you must install the locale for both products
                                             before you reset user locales. If you run into any issues, such as could occur if an end user resets a phone language before
                                             the locale installation is complete for IM and Presence Service, have your users reset their phone language in the Self-Care
                                             Portal to English. After the locale installation is complete, users can reset their phone language, or you use Bulk Administration
                                             to synchronize locales to the appropriate language by bulk. |
|---|---|

| Message | Description |
|---|---|
| [LOCALE] File not found:
                                                					 <language>_<country>_user_locale.csv, the user locale has not been
                                                					 added to the database. | This error occurs when the system cannot locate the CSV file,
                                                					 which contains user locale information to add to the database. This indicates
                                                					 an error with the build process. |
| [LOCALE] File not found: <country>_network_locale.csv, the
                                                					 network locale has not been added to the database. | This error occurs when the system cannot locate the CSV file, which contains network locale information to add to the database.
                                                This indicates an error with the build process. |
| [LOCALE] Communications Manager CSV file installer installdb is not present or not executable. | This error occurs because a Unified Communications Manager application called installdb must be present; it reads information that is contained in a CSV file and applies it correctly
                                                to the Unified Communications Manager database. If this application is not found, it either was not installed with Unified Communications Manager (very unlikely), has been deleted (more likely), or the node does not have Unified Communications Manager installed (most likely). Installation of the locale terminates because locales do not work without the correct records that
                                                are held in the database. |
| [LOCALE] Could not create /usr/local/cm/application_locale /cmservices/ipma/com/cisco/ipma /client/locales/maDialogs_<ll>_<CC>.properties.Checksum. [LOCALE] Could not create
                                                					 /usr/local/cm/application_locale/cmservices/ipma/com/cisco/
                                                					 ipma/client/locales/maMessages_<ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/
                                                					 application_locale/cmservices/ipma/com/cisco/
                                                					 ipma/client/locales/maGlobalUI_<ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/
                                                					 application_locale/cmservices/ipma/ LocaleMasterVersion.txt.Checksum. | These errors could occur when the system fails to create a checksum file; causes can include an absent Java executable, /usr/local/thirdparty/java/j2sdk/ jre/bin/java , an absent or damaged Java archive file, /usr/local/cm/jar/cmutil.jar , or an absent or damaged Java class, com.cisco.ccm.util.Zipper. Even if these errors occur, the locale will continue to work
                                                correctly, with the exception of Unified Communications Manager Assistant , which cannot detect a change in localized Unified Communications Manager Assistant files. |
| [LOCALE] Could not find
                                                					 /usr/local/cm/application_locale/cmservices/ipma/LocaleMaster Version.txt in
                                                					 order to update UnifiedCMAssistant locale information. | This error occurs when the file does not get found in the
                                                					 correct location, which is most likely due to an error in the build process. |
| [LOCALE] Addition of <RPM-file-name> to the Unified Communications Manager database has failed! | This error occurs because of the collective result of any
                                                					 failure that occurs when a locale is being installed; it indicates a terminal
                                                					 condition. |

| Step 1 | Begin this procedure on the Unified Communications Manager publisher node. From Cisco Unified Communications OS Administration, choose Software Upgrades > Install . The Software Installation/Upgrade window appears. |
|---|---|
| Step 2 | In the Source field, choose Remote File System . |
| Step 3 | Configure the fields on the Software Installation/Upgrade window. See the Related Topics for more information about the fields and their configuration options. |
| Step 4 | Click Next . The window refreshes with a list of available software options and upgrades. |
| Step 5 | From the Options/Upgrades drop-down list, choose the DP COP file and click Next . The Installation File window opens and downloads the file from the FTP server. The window displays the progress of the download. |
| Step 6 | When the Checksum window appears, verify the checksum value against the checksum for the file that you downloaded. |
| Step 7 | Click Next to proceed with the software upgrade. A warning message displays the DP COP file that you selected to install. |
| Step 8 | Click Install . The Install Status window appears. |
| Step 9 | Click Finish . |
| Step 10 | Repeat this procedure on the Unified Communications Manager subscriber nodes. You must install the COP file on all the nodes in the cluster. |

| Note | Complete this procedure only if you are installing a national numbering plan for countries outside of North America (the system
                                             default). |
|---|---|

| Step 1 | From Cisco
                                          			 Unified Communications Manager Administration, choose Call Routing > Dial Plan
                                                				  Installer . |
|---|---|
| Step 2 | Enter search criteria and click Find . |
| Step 3 | Choose the
                                          			 dial plan version that you want to install from the Available Version drop-down
                                          			 list. |
| Step 4 | Click Install . The
                                          			 Status displays that the dial plan has been installed. |
| Step 5 | Repeat this
                                          			 procedure for every subscriber node in the cluster. |

| Step 1 | From the Cisco Unified Serviceability interface, choose Tools > Control Center - Feature Services . |
|---|---|
| Step 2 | Choose the Unified Communications Manager server from the Servers drop-down list. In the CM Services area, Cisco CallManager displays in the Service Name column. |
| Step 3 | Click the radio button that corresponds to the Cisco CallManager service. |
| Step 4 | Click Restart . The service restarts and displays the message, Service Successfully Restarted . |

| Step 1 | Install and configure the SNMP NMS. |
|---|---|
| Step 2 | In the Control Center - Network Services window,
                                          			 verify that the system started the SNMP services. |
| Step 3 | Unified Communications Manager: In the Service Activation window, activate the Cisco
                                          			 CallManager SNMP service. Cisco Unity Connection only: The Connection SNMP Agent service
                                          			 automatically activates. |
| Step 4 | If you are using SNMP V1/V2c, configure the community string. |
| Step 5 | If you are using SNMP V3, configure the SNMP user. |
| Step 6 | Configure the notification destination for traps or informs. |
| Step 7 | Configure the system contact and location for the MIB2 system
                                          			 group. |
| Step 8 | Configure trap settings for CISCO-SYSLOG-MIB. |
| Step 9 | Unified Communications Manager only: Configure trap settings for
                                          			 CISCO-CCM-MIB. |
| Step 10 | Restart the Primary Agent service. |
| Step 11 | On the NMS, configure the Unified Communications Manager trap parameters. |

| Step 1 | Shut down the virtual machine. |
|---|---|
| Step 2 | Change the configuration of the virtual machine as needed through vSphere. You can update the Guest OS and VM Hardware Compatibly. Update VM Hardware Compatibly—Left click Virtual Machine. Check for Updates . Click Update Note If you are not aware of the host click Check statuts and click Upgrade to match host. Update Guest OS—Right click the Virtual Machine > Edit Settings > Virtual Machine Option > General Option > Guest OS Version . | Note | If you are not aware of the host click Check statuts and click Upgrade to match host. |
| Note | If you are not aware of the host click Check statuts and click Upgrade to match host. |
| Step 3 | Power on the Virtual Machine. Note Following warning messages appears in ESXi while opening the Virtual Machine settings while running when there is a mismatch. Warning The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                         running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations. | Note | Following warning messages appears in ESXi while opening the Virtual Machine settings while running when there is a mismatch. | Warning | The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                         running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations. |
| Note | Following warning messages appears in ESXi while opening the Virtual Machine settings while running when there is a mismatch. |
| Warning | The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                         running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations. |

| Note | If you are not aware of the host click Check statuts and click Upgrade to match host. |
|---|---|

| Note | Following warning messages appears in ESXi while opening the Virtual Machine settings while running when there is a mismatch. |
|---|---|

| Warning | The configured guest OS (CentOS 4/5 or later (64 bit)) for this virtual machine does not match the guest that is currently
                                                         running (CentOS 7 (64 bit)). You should specify the correct guest OS to allow for guest-specific optimizations. |
|---|---|

| Note | Many of these tasks are documented in more detail in the Configuration and Administration of the IM and Presence Service Guide . Where indicated, see that guide for detail on how to complete these tasks. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Read the Release Notes and any Readme files that come with your release. | You can download Release Notes from the below URL.  Make sure that you understand the features for your release and any COP
                                          file requirements. https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html |
| Step 2 | Check for software and firmware updates for IM and Presence Service on Cisco.com. | You can download software from https://software.cisco.com/download/navigator.html?mdfid=280448682&i=rm |
| Step 3 | Configure Presence Redundancy Groups. | For details, see the Configuration and Administration of the IM and Presence Service Guide . |
| Step 4 | Change the default domain. | For details, see the Configuration and Administration of the IM and Presence Service Guide . |
| Step 5 | Change the IM and Presence Service IM address scheme. | For details, see the Configuration and Administration of the IM and Presence Service Guide . |
| Step 6 | Change the IM and Presence Service node name. | For details, see the Configuration and Administration of the IM and Presence Service Guide . |
| Step 7 | Configure Unified Communications Manager as a Presence Gateway. | For details, see the Configuration and Administration of the IM and Presence Service Guide . |
| Step 8 | Configure a SIP Publish trunk on Unified Communications Manager. | For details, see the Configuration and Administration of the IM and Presence Service Guide . |
| Step 9 | Assign users to servers. | For details, see the Configuration and Administration of the IM and Presence Service Guide . |
| Step 10 | Activate services | Turn on essential IM and Presence Service services. |

| Note | You must complete this task on each server that you install in an IM and Presence cluster. |
|---|---|