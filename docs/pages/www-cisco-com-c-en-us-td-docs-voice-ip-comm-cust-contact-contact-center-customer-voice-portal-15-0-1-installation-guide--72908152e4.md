---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-installation-guide--72908152e4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/installation/guide/ccvp_b_1501_installation-upgrade-guide-cisco-unified-customer-voice-portal/ccvp_b_install_and_upgrade_12-5_chapter_0101.html
retrieved_at: 2026-08-21T03:01:15.710505+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: April 30, 2025

Chapter: Upgrade Unified CVP

## Chapter: Upgrade Unified CVP

# Upgrade Unified CVP

You can upgrade to a new version of Unified CVP if the platform of the new and existing version is the same. For example,
                        replacing Unified CVP 11.6(1) with Unified CVP 12.0(1) is an upgrade because both the versions work on the same platform.

If the existing software is to be replaced with a newer version with a change in platform, architecture, or applications,
                        the process is called migration. For example, replacing Unified CVP 12.x with Unified CVP 15.0(1) is a migration because the newer version works on a different platform than the older version. To learn whether replacing
                        the existing version with a new version is an upgrade or a migration, see the Upgrade Path section.

Upgrade of Cisco voice solution components is a multistage process; solution components are grouped in several stages for
                        upgrading. Users must follow the solution level upgrade order mentioned in the Upgrade section of the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html for smooth transitioning to higher grade versions.

Important

A new Unified CVP 15.0(1) base installer is now available for customers, featuring OpenJDK JRE (v17.0.18) as the supporting
                                    Java runtime for the Unified CVP application. This is an upgrade from the previous 12.5(1) installer, where OpenJDK JRE (1.8.x)
                                    was installed as the Java runtime environment on the Unified CVP components.

Push the TCL and VXML files to their respective ingress and VXML gateways after the CVP Operations Console is upgraded, but before any other CVP components are upgraded.

After the successful upgrade, the Certificate Authorities (CAs) that are unapproved by Cisco are removed from the platform
                                    trust store. However, you can add them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle here .

For information about adding a certificate, see here .

## Upgrade Path

The following table lists the upgrade paths to upgrade an existing Unified CVP version from Windows Server 2016 or Windows
                           Server 2019 to Windows Server 2019 or Windows Server 2022.

Upgrade Path from Older Release to New Release

Platform Change

Conversion Process

Description

Unified CVP

12.5(1) to 15.0(1)

Yes

Perform an in-place upgrade from Windows Server 2016 to Windows Server 2019 or Windows Server 2022.

Upgrade to Unified CVP 15.0(1)

Change in platform from 15.0(1) release.

Unified CVP

12.6(1) to 15.0(1)

Yes

Perform an in-place upgrade from Windows Server 2016 or Windows Server 2019 to Windows Server 2019 or Windows Server 2022.

Upgrade to Unified CVP 15.0(1)

Change in platform from 15.0(1) release.

Unified CVP

12.6(2) to 15.0(1)

Yes

Perform an in-place upgrade from Windows Server 2016 or Windows Server 2019 to Windows Server 2019 or Windows Server 2022.

Upgrade to Unified CVP 15.0(1)

Change in platform from 15.0(1) release.

## Unified CVP Upgrade Strategies

You can upgrade Unified CVP in a maintenance window. However, when there are a large number of Unified CVP servers to upgrade,
                           it may not be possible to upgrade all of them in one maintenance window. Using the upgrade strategies, you can help large
                           Unified CVP deployments distribute the upgrade process. In addition, you can divide the server upgrades into multiple steps
                           that can be completed over several maintenance windows.

Unified CVP upgrade strategies are described in the following sections.

### Unified CVP Units

A Unified CVP unit is a single virtual machine and may comprise VXML Servers and Call Servers. For Unified CVP deployments
                                 that have multiple Unified CVP units, ensure that you upgrade one unit at a time. For example, you can upgrade a Unified CVP
                                 unit of related servers in a maintenance window. This deployment may be useful for call centers. There may be a need to migrate
                                 to Session Initiation Protocol (SIP) to continue call processing and minimize the risks.

### Multiphased
                           	 Approach

Multiphased approach is a strategy to upgrade a subset of Unified CVP Servers and resume call processing. Using the multiphased
                                 upgrade approach, you can divide the upgrades in phases over time. If a Unified CVP deployment has multiple Unified CVP units,
                                 you can upgrade each unit using the multiphased approach.

Depending on the
                                 		  deployment, choose one of the following multiphased approaches:

Upgrade all
                                       				servers of a certain type in a maintenance window.

Upgrade a
                                       				subset of a server type in a maintenance window.

Upgrade a subset of a server type from a Unified CVP unit in a maintenance window.

Use multiphased
                                 		  approach to upgrade the components in the following sequence:

Operations
                                       				Console

Unified CVP Reporting Server

Unified CVP Server

It is not necessary to upgrade all servers in a category in a single maintenance window; however, you must upgrade all Unified
                                             CVP components of one type before moving to the next set of components in the Unified CVP deployment or the Unified CVP unit.

## Important
                        	 Considerations for Upgrade

Upgrade
                                    				Unified CVP during off-peak hours or during a maintenance window to avoid
                                    				service interruptions.

Do not make
                                    				any configuration changes during the upgrade, because the changes are lost
                                    				after the upgrade.

Ensure that a Unified CVP unit remains offline until you upgrade all the components in that unit.

Upgrade
                                    				Unified CVP components in a sequence for a successful deployment. A change in
                                    				upgrade sequence results in loss of call data and error or inability to
                                    				configure properties that are introduced in the new version.

Push the TCL and VXML files (from the location C:\Cisco\CVP\GWDownloads\ ) to their respective ingress and VXML gateways after the Unified CVP Operations Console is upgraded, but before any other Unified CVP components are upgraded.

## Pre- Upgrade Tasks

Close all programs.

Stop any third-party services and applications that are running on the server.

Back up C:\Cisco\CVP for all Unified CVP components except Operations Console.

Unified CVP Server log files are saved in <CVP_HOME>\logs ; VXML Server log files are saved in <CVP_HOME>\VXMLServer\logs and <CVP_HOME>\VXMLServer\applications\<app_name>\logs .

Ensure that the servers are listed as supported hardware and sized appropriately. For information on platform hardware specifications
                                 and compatible third party software version requirements, see https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-technical-reference-list.html .

Back up the existing Unified CVP installation files onto a different computer for redundancy in case the automatic backup
                                 fails.

Back up the property files of Unified CVP Server, OAMP, and Reporting Server that need modification. Restore them after upgrade
                                 is complete.

This ISO encrypts the keystore password, which is required for exchanging certificates. For detailed steps, refer to the Unified CVP Security section in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Exclude the following folders from on-access scanning configuration of the AV program from all Anti Virus scans:

c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA , and D:\IFMXDATA .

Caution

The 15.0(1) release replaces the JRE and Tomcat versions. If you have updated any files in Tomcat (from the %CVP_HOME%\VXMLServer\Tomcat\webapps\CVP folder) or JRE configurations (from the %CVP_HOME%\JRE folder), ensure that you take a backup of the files before you proceed with the installation. You can restore the backup
                                       after the installation is complete.

System Requirements

By default, Windows Defender is enabled on Windows Server. For more information on Windows Defender antivirus compatibility,
                           see https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/windows-defender-antivirus-compatibility .

Unified CVP installation can also take longer than expected due to scanning of files by Windows Defender or any other anti-virus
                           software. Based on your IT policy, do one of the following:

Disable Windows Defender. For more information, see Disable Microsoft Defender Antivirus procedure in Microsoft documentation.

Add the following path c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA , and D:\IFMXDATA to the exclusion list of Windows Defender. For more information, see https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/configure-extension-file-exclusions-windows-defender-antivirus .

To allow required access to installation program files or folders, add the following paths c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA , and D:\IFMXDATA to the exclusion list of your anti-virus software. For more information, refer to the documentation of the respective anti-virus
                                 software.

## Upgrade Existing Unified CVP Virtual Machine

You must not use VMware vSphere Client (Thick Client) to upgrade the
                                          			 virtual machine hardware.

### Configure Virtual
                           	 CPU Settings

Complete the following procedure to change the virtual hardware resource setting for CPU on Unified CVP virtual machines.

Step 1

Power off the
                                          			 virtual machine.

Step 2

Right-click
                                          			 the virtual machine, choose Edit
                                             				Settings .

Step 3

Click the Virtual Hardware tab.

Step 4

Click CPU .

Step 5

From the Cores per Socket drop-down list, select 1 .

Step 6

In the Reservation field, enter the CPU reservation speed (defined in MHz) for Unified CVP virtual machines.

For more information about virtual hardware resource setting for CPU and memory, see Unified CVP Virtualization Wiki available at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html .

Step 7

Click OK to save the settings.

#### What to do next

Upgrade Virtual Memory

### Upgrade Virtual Memory

Complete the following procedure to upgrade the system memory on Unified CVP virtual machines.

Step 1

Ensure that
                                          			 the virtual machine is switched off.

Step 2

Right-click the Virtual Machine and select Edit Settings .

Step 3

Click the Virtual Hardware tab.

Step 4

Click Memory .

Step 5

In the RAM field, change the RAM value (in MB) of Unified CVP virtual machines as defined in the Virtualization for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html .

Step 6

In the Reservation field, enter the RAM value (in MB) corresponding to Unified CVP VMs, as defined in the Virtualization for Cisco Unified Customer Voice Portal .

Step 7

Click OK to save the settings.

#### What to do next

Upgrade the Virtual Machine Hardware Version.

### Upgrade Virtual
                           	 Machine Hardware Version

Complete the following procedure to upgrade the virtual machine hardware version on Unified CVP virtual machines.

Step 1

Ensure that
                                          			 the virtual machine is switched off.

Step 2

Right-click the virtual machine and select Edit Settings .

Step 3

Click the Virtual Hardware tab.

Step 4

Click Upgrade .

Step 5

Check the Schedule VM Compatibility Upgrade check box.

Step 6

From the Compatible with (*) drop-down list, choose one of
                                          			 the following options:

- ESXi 7.1 U1 and later updates

Step 7

Click OK to save the settings.

Step 8

Power on the virtual machine.

#### What to do next

Expand the Virtual
                                 		  Machines Disk Space

### Expand Disk Space of Virtual Machines

Complete the following procedure to expand the virtual machines disk space on Unified CVP virtual machines:

### Enable Resource
                           	 Reservation on Upgraded Virtual Machine

After the virtual machine hardware version is upgraded based on the information provided in the Virtualization for Cisco Unified Customer Voice Portal , perform the following steps to enable resource reservation on the respective Unified CVP virtual machines.

For more information on supported virtual machine hardware versions, see available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html .

Step 1

Login to vSphere Client and select the Unified CVP virtual machine.

Step 2

Right-click the virtual machine and select the option Edit Settings from the popup menu.

Step 3

Select the Resources tab.

Step 4

Enable resource reservation for Unified CVP virtual machines.

Step 5

After the virtual hardware resource setting for CPU and memory for CVP virtual machines are set, click OK to close the VM Properties dialog box.

## Upgrade Windows Server

Microsoft supports an in-place upgrade of operating system.

By default, Windows Defender is enabled on Windows Server 2019 or Windows Server 2022. Windows Server 2019 or Windows Server
                                          2022 upgrade will prompt to uninstall the antivirus due to compatibility issue with Windows Defender. To proceed with the
                                          upgrade, uninstall the antivirus. For more information on Windows Defender antivirus compatibility, see https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/ windows-defender-antivirus-compatibility .

Complete the following procedure to upgrade your operating system on all virtual machines for server-based applications.

### Before you begin

Unified CVP 15.0(1) version has a dual support for Windows Server 2019 or Windows Server 2022. If you still have Windows Server
                              2016, upgrade the system.

As a precautionary measure, follow the steps listed under the Preupgrade Tasks section to preserve the existing version of CVP.

Upgrading to Windows Server may delete static network configuration (for private and public interfaces) for all Windows virtual
                                    machines. Record your static network configurations, including TCP/IP IPv4 information before upgrading. Reconfigure these
                                    settings after the upgrade completes.

Ensure that latest version of VMware Tools software is installed.

Ensure that the VMware version of the VM is 18.

Ensure that VMware ESXi version of the host is ESXi 7.0 U1 or later updates.

For operating system requirement, see the Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

Change the guest operating system to Microsoft Windows Server 2019 or 2022 . To do so, right-click the virtual machine, and select Edit settings > Options > General Options . Select the guest operating system as Microsoft Windows Server 2022 or Windows Server 2019 .

During Windows Server 2022 upgrade, you might be prompted to uninstall anti virus owing to a change in behavior of Windows
                                    Server. Re-install the anti-virus after the upgrade.

Step 1

Mount Windows Server ISO image to the virtual machine. Open the file explorer and double-click on the Drive to run the Windows Server setup.

Step 2

Select Download & install updates to let the installation go on smoothly. Click Next .

Step 3

Select Windows Server Desktop Experience . Click Next .

Step 4

Read the notes and license terms and then click Accept .

Step 5

To retain existing Unified CVP configurations, files, services, and all associated settings intact after the inplace upgrade
                                       to Windows Sever 2019 or Windows Server 2022, select Keep personal files and apps . Then click Next .

If you select Nothing , everything (including Unified CVP) in the existing Windows Server VM will be erased, and the system will be set up as a
                                                      new Windows Server 2019 or Windows Server 2022 VM.

Step 6

In case a Window is displayed with the title What needs your attention , click Confirm to proceed because existing Unified CVP on Windows Server has been successfully validated to be working on Windows Server
                                       2019 or Windows Server 2022 when such an upgrade process is followed.

Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed.

Step 7

Use your existing credentials to log in to the system and ensure that Unified CVP-related services are up and running after
                                       the completion of Windows Server 2016 or Windows Server 2019 platform upgrade to Windows Server 2019 or Windows Server 2022.

## Upgrade Unified CVP Components

Unified CVP Server

Operations Console

Remote Operations

Unified CVP Reporting Server

Follow the given steps to install the Unified CVP 15.0(1) on each of the above components:

Step 1

Run (double click) CVP15.0.1.exe . A welcome screen is displayed.

Step 2

Click Next to proceed.

Step 3

Review and accept the Software License Agreement , and click Next .

A warning message is displayed to backup all custom audio files. Click OK to proceed.

Step 4

Click Install to start the MR installation.

Step 5

Click Finish to complete the installation. Reboot the machine after the installation.

## Upgrade Operations
                        	 Console

The installed default media files are overwritten with the media format you choose for the Unified CVP upgrade; however, the
                              customized media files are not overwritten during the upgrade. Customized media files, such as custom applications and Whisper
                              Agent-Agent Greeting (WAAG), are retained in the format as they were prior to upgrade.

Following sections describe the various scenarios of Operations Console upgrade.

### Upgrade Operations Console 12.5(1), 12.6(1) and 12.6(2) in U-law to Operations Console 15.0(1) in U-law

Step 1

Mount the Unified CVP ISO image.

Step 2

Navigate to C:\CVP\installer_windows and run setup.exe.

The installer automatically detects the previous installation and guides you through the upgrade process.

Step 3

Restart the server.

Step 4

Navigate to the C:\Cisco\CVP\conf location and manually configure the Unified CVP properties file. For more information, see the Manual Configuration of Unified
                                          CVP Properties section.

Step 5

Restart the server.

### Upgrade Operations Console 12.5(1), 12.6(1) and 12.6(2) in U-law to Operations Console 15.0(1) in A-law

Step 1

Navigate to the C:\Cisco\CVP\conf location.

Step 2

Convert the custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG), and applications that
                                          are in u-law to A-law.

Step 3

In the cvp_pkgs.properties file, add the cvp-pkgs.PromptEncodeFormatALaw = 1 property at line 7 to enable the A-law flag.

Ensure that you leave a space before and after the " = " sign.

Step 4

Mount the Unified CVP ISO image, and run setup.exe.

Step 5

Follow the instructions on the screen.

Step 6

Restart the server.

All the standard packaged media files and applications are installed in A-law format.

Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade.

Step 7

Navigate to the C:\Cisco\CVP\conf location and manually configure the Unified CVP properties file. For more information, see the Manual Configuration of Unified
                                          CVP Properties section.

Step 8

Restart the server.

### Upgrade Operations Console 12.5(1), 12.6(1) and 12.6(2) in A-law to Operations Console 15.0(1) in A-law

Step 1

Navigate to the C:\Cisco\CVP\conf location.

Step 2

In the cvp_pkgs.properties file, add the cvp-pkgs.PromptEncodeFormatALaw = 1 property at line 7 to enable the A-law flag.

Ensure that you leave a space before and after the " = " sign.

Step 3

Mount the Unified CVP ISO image and run setup.exe.

The installer automatically detects the previous installation, and guides you through the upgrade process.

Step 4

Follow the instructions on the screen.

Step 5

Restart the server.

- All the standard packaged media files and applications are installed in the A-law format.

- Custom media files, such as custom applications and WAAG, are retained in the format as they were prior to upgrade.

Step 6

Navigate to the C:\Cisco\CVP\conf location and manually configure the Unified CVP properties file. For more information, see the Manual Configuration of Unified
                                          CVP Properties section.

Step 7

Restart the server.

#### What to do next

Load the IOS scripts into the Cisco IOS memory.

### Upgrade Operations Console 12.5(1), 12.6(1) and 12.6(2) in A-law or U-law to Operations Console 15.0(1) in G729

Step 1

Navigate to the C:\Cisco\CVP\conf location.

Step 2

In the cvp_pkgs.properties file, add the cvp-pkgs.PromptEncodeFormatG729 = 1 property at line 7 to enable the G729 flag.

Ensure that you leave a space before and after the " = " sign.

Step 3

Mount the Unified CVP ISO image and run setup.exe.

Step 4

Follow the instructions on the screen.

Step 5

Restart the server.

All the standard packaged media files and applications are installed in G729 format.

Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade.

Step 6

Navigate to the C:\Cisco\CVP\conf location and manually configure the Unified CVP properties file. For more information, see the Manual Configuration of Unified
                                          CVP Properties section.

Step 7

Restart the server.

## Upgrade Unified CVP Reporting Server

You cannot upgrade CVP Reporting Server from 12.5(1), 12.6(1) and 12.6(2) to 15.0(1) because the version of IBM Informix database
                              server has changed. You need to uninstall CVP Reporting Server 12.5(1), 12.6(1) and 12.6(2) and install CVP Reporting Server
                              15.0(1).

For more information, see Migrate Unified CVP Reporting Server .

### Upgrade Informix on CVP Reporting Server

This section describes the procedure to upgrade the Informix patch (14.10.FC12W5 or later) on the CVP Reporting Server.

Before installing the Informix patch, consider the following:

Informix does not support the rollback of an installation to a previous version.

The standalone uninstallation of Informix is not a supported procedure.

Given that the target upgrade version is Informix 14.10.FC12W5, standard backup and restore methods are incompatible due to
                                                   version discrepancies.

It is recommended to take a snapshot of the Reporting Server before upgrading so you can restore it if any issues occur.

Verify that the rootdbs is not full and has sufficient free space. The rootdbs must have at least 20-30% free space available to accommodate temporary objects, logs, and metadata updates during the upgrade
                                                   process.

#### Before you begin

Ensure the following:

Install CVP Reporting Server version 15.0(1).

Check your Informix version to confirm the upgrade path.

The JAVA_HOME path is set in the Environment Variables. If it is not set, follow the below steps to configure it:

Press Windows + R.

Enter sysdm.cpl , and then click OK .

In the System Properties window, click the Advanced tab, and then click Environment Variables .

Under System variables, click New .

In the Variable name field, enter JAVA_HOME .

In the Variable value field, enter your Java installation path, for example, C:\Cisco\CVP\jre .

Under System variables, select the Path variable, and then click Edit .

Add %JAVA_HOME%\bin to the list of paths.

Click OK to save the changes, and then click OK to close all open windows.

Step 1

Open the Windows Command Prompt as an administrator and run the following command: onstat - .

Verify that the output displays version 14.10.FC10W2 .

Step 2

Download and extract the downloaded Informix 14.10.FC12W5 package to a temporary local directory on the server.

Step 3

Run the installer and execute the file ids_install.exe from the unzipped folder by following the steps below:

Right-click on ids_install.exe and select Run as administrator .

On the Installation page, click Next .

On the License Agreement page, select I accept the terms in the license agreement and click Next .

Specify the Informix installation location.

Select Continue to proceed with the installation.

Click Next to proceed through the configuration summary.

Click Install to begin the upgrade process.

Step 4

After the installation, start Informix Service by following the below steps:

Open the Windows Services management console.

Locate the Informix IDS service.

Right-click on the service and select Start .

Step 5

Verify the successful upgrade of the database engine by following the steps below:

Open the Windows Command Prompt as an administrator.

Run the following command: onstat -

Confirm that the version output displays the required Informix version.

Verify that all CCE-dependent services have successfully reconnected to the database.

## Upgrade Unified CVP Server

### Before you begin

After successful upgrade of Unified CVP server, the CVP Call Server Service Startup Type is set to Automatic by default.

### Upgrade CVP Server 12.5(1), 12.6(1) and 12.6(2) in U-law to CVP Server 15.0(1) in U-law

Perform Steps 1 to 4 of the Upgrade Operations Console 12.5(1), 12.6(1) and 12.6(2) in U-law to Operations Console 15.0(1) in U-law procedure.

Log into Operations Console of the current version of Unified CVP and click Bulk Administration > File Transfer > Scripts and Media .

Load the gateway download transferred files into the Cisco IOS memory for each CVP service using the Cisco IOS call application voice load <service_name> CLI command.

Restore any backed-up third-party libraries.

### Upgrade CVP Server 12.5(1), 12.6(1) and 12.6(2) in U-law to CVP Server 15.0(1) in A-law

Perform Steps 1 to 8 of the Upgrade Operations Console 12.5(1), 12.6(1) and 12.6(2) in U-law to Operations Console 15.0(1) in A-law.

### Upgrade CVP Server 12.5(1), 12.6(1) and 12.6(2) in A-law to CVP Server 15.0(1) in A-law

Perform Steps 1 to 7 of the Upgrade Operations Console 12.5(1), 12.6(1) and 12.6(2) in A-law to Operations Console 15.0(1) in A-law procedure.

### Upgrade CVP Server 12.5(1), 12.6(1) and 12.6(2) in A-law or U-law to CVP Server 15.0(1) in G729

Perform Steps 1 to 7 of the Upgrade Operations Console 12.5(1), 12.6(1) and 12.6(2) in A-law or U-law to Operations Console 15.0(1) in G729 procedure.

## Upgrade Remote
                        	 Operations

Step 1

Mount the
                                       			 Unified CVP ISO image, and run setup.exe.

The installer
                                          				automatically detects the installation and upgrade of Remote Operations and
                                          				guides you through the upgrade process.

Step 2

Follow the
                                       			 instructions on the Upgrade screens and click Upgrade .

Step 3

Restart the
                                       			 Server.

## Upgrade Unified Call Studio

Step 1

Open Call Studio, right-click any existing project in the Navigator view, choose Export .

The Export wizard opens.

Step 2

Navigate to General > File System , and click Next .

Step 3

Browse to the directory where the projects will be exported and click OK and then click Finish .

Step 4

Uninstall the Call Studio software.

For more information, see the Unified CVP/Call Studio Uninstallation section.

Step 5

Install the Call Studio software.

For more information, see the Install Unified Call Studio section.

The SolarWinds TFTP software and AnyConnect (while a VPN connection is enabled) are the known causes for the Call Studio debugger
                                          errors. To resolve the Call Studio debugger errors:

If you are using SolarWinds, stop the SolarWinds TFTP software and run the debugger.

If you are using AnyConnect, disconnect the VPN connection and run the debugger.

## Postupgrade
                        	 Tasks

After you upgrade the Unified CVP components, synchronize the metadata files using the Sync-up tool.

Initiate metadata synchronization only if you are using the CVP Rest API. For more information, see Initiate Metadata Synchronization for Unified CVP Rest API .

Important

After upgrade, restart the WebServicesManager service to use the system CLI.

If you are using a VRU connection port other than the default port (5000), then click Save and Deploy of Unified CVP Call Server from OAMP.

Perform the following steps for Smart Licensing to work after upgrading to Unified CVP 15.0(1) :

Redeploy all Call Servers and VXML Servers from OAMP.

Restart the services.

VMWare Tools do not get updated automatically after upgrading to Unified , CVP 15.0(1) on Windows Server 2019/2022 and rebooting the machine.

Workaround : Perform the following steps to update the VMWare Tools manually:

Right-click on the VM.

Go to Guest OS and select Upgrade VMWare Tools .

After you upgrade to Unified CVP 15.0(1) , the WebServiceCredentials schema gets updated with the encryption method.

To encrypt the wsm password in OAMP, do the following:

Stop Cisco CVP OPSConsoleServer and Cisco CVP WebServicesManager services.

Navigate to C:\Cisco\CVP\bin\ .

Execute the mgr-init.bat -wsm <wsmadmin password> command from the command prompt.

Restart the Cisco Unified CVP Operations Console and Cisco CVP WebServicesManager.

The encryption key, which is a part of OAMP, is absent from the WebServicesCredentials.xml files on the CVP Call Server, VXML Server, and Reporting Servers.

Workaround: To synchronize the WebServicesCredentials.xml with the encryption method, it is necessary to redeploy all the Call Servers, VXML Servers, and Reporting Servers.

### Synchronize Unified CVP Property for Courtesy Callback

If you have configured Courtesy Callback and upgrade Unified CVP from Release 12.x to 15.0, you may notice changes to the
                                 configuration that impact Courtesy Callback functionality in the CVP Reporting Server. Follow these steps to restore the required
                                 settings using the OAMP UI.

These steps are necessary only if the property is checked in the OAMP UI.

Step 1

Log in to the CVP OAMP portal.

Step 2

In the navigation pane, choose Courtesy Callback .

Step 3

Uncheck the Allow unmatched Dialed Numbers check box and click Save .

Step 4

Re-check the Allow unmatched Dialed Numbers check box and click Save .

Step 5

Restart the CVP Reporting Server to apply the configuration changes.

### Manual Configuration of Unified CVP Properties

The following table lists the procedure to manually configure the Unified CVP properties files based on the upgrade path.

Component

Upgrade Path

CVP Server

12.5(1) to 15.0(1)

12.6(1) to 15.0(1)

12.6(2) to 15.0(1)

No configuration required.

WebServices Manager

12.5(1) to 15.0(1)

12.6(1) to 15.0(1)

12.6(2) to 15.0(1)

No configuration required.

Operations Console

12.5(1) to 15.0(1)

12.6(1) to 15.0(1)

12.6(2) to 15.0(1)

No configuration required.

Reporting Server

12.5(1) to 15.0(1)

12.6(1) to 15.0(1)

12.6(2) to 15.0(1)

No configuration required.

### Initiate Metadata Synchronization for Unified CVP Rest API

In the CVP REST API architecture, customers use the REST API to create, update, and delete media files on the media server
                                 and VXML applications on the VXML server. When this process is used, media files on the media server and VXML applications
                                 on the VXML server are saved as metadata in the OpsConsole server’s Derby database. There may be situations where the metadata
                                 becomes out of sync with the files on the media servers and VXML servers. Typical examples include the addition or deletion
                                 of CVP servers, and the deployment of applications and media files using tools other than the REST API.

A command line tool “metasynch.cmd” is available in the C:\Cisco\CVP\wsm\CLI location on the OpsConsole server to enable synchronization of metadata with the files on VXML servers and media servers.
                                 The tool internally uses the Sync Up API to perform synchronization. It takes three arguments: WSM username, WSM user password,
                                 and server type (MEDIA, VXML, or VXML_STANDALONE). Based on the server type specified, all servers of the respective server
                                 type are synchronized with the OpsConsole server as metadata. If the server type argument is not provided, metadata is synchronized
                                 from all media servers and VXML servers configured in the OpsConsole server. In case of an upgrade from an earlier version,
                                 the media files and VXML applications are present on the media servers and VXML servers, but the corresponding metadata information
                                 is not present on the WSM server. The absence of metadata limits the user from using the REST API to access, update, or delete
                                 existing media files and VXML applications on the media server and VXML server.

In case of Upgrade from an earlier version, the media files and vxml applications are present in the media servers and vxml
                                 servers but corresponding metadata information is not present in the WSM server. The absence of metadata information limits
                                 the user from using the REST API to access, update, and delete existing media files and vxml applications on the media server
                                 and the vxml server.

Wsmadmin (CLI) users or any other serviceability/readonly role users cannot login or use OAMP/NOAMP/CLI until an Administrator
                                             or Super Administrator role user updates their password post an install/upgrade.

#### Synchronize
                              	 Metadata Files Using Sync-Up Tool

To invoke metasynch.cmd , complete the following steps.

Step 1

On the Unified CVP OAMP Server, navigate to the C:\Cisco\CVP\wsm\ CLI location.

Step 2

Run the metasynch.cmd file with following arguments:

- wsm
                                                   				  username

- wsm
                                                   				  password

##### Example:

```
metasynch.cmd wsmusername wsmpassword MEDIA
```

servertype : MEDIA/VXML /VXML_STANDALONE

options : -help -? print this help message

C:\Cisco\CVP\wsm\CLI\log\SyncTool.log

### Removing TLS Cipher Configuration from OAMP User Interface

After upgrading the CVP server to 15.0(1) version, it is recommended to remove the TLS_RSA cipher from the OAMP user interface.

To remove TLS_RSA cipher from the OAMP user interface, perform the following steps:

Step 1

Upgrade the CVP server, the OAMP server, and the Reporting server to 15.0 version.

Step 2

Log in to the Operations Console and click Device Management > Unified CVP Call Server .

Step 3

Edit the call server record.

Step 4

Go to SIP > Advanced Configurations > Security Properties .

The available supported ciphers are listed.

Step 5

Select the cipher starting with TLS_RSA.

Step 6

Click Remove .

Step 7

In the Supported Ciphers field, type TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 and click Add .

Step 8

Click Save & Deploy .

Step 9

Restart the CVP server.

| Important | A new Unified CVP 15.0(1) base installer is now available for customers, featuring OpenJDK JRE (v17.0.18) as the supporting
                                    Java runtime for the Unified CVP application. This is an upgrade from the previous 12.5(1) installer, where OpenJDK JRE (1.8.x)
                                    was installed as the Java runtime environment on the Unified CVP components. |
|---|---|

| Note | Push the TCL and VXML files to their respective ingress and VXML gateways after the CVP Operations Console is upgraded, but before any other CVP components are upgraded. |
|---|---|

| Note | After the successful upgrade, the Certificate Authorities (CAs) that are unapproved by Cisco are removed from the platform
                                    trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle here . For information about adding a certificate, see here . |
|---|---|

| Upgrade Path from Older Release to New Release | Platform Change | Conversion Process | Description |
|---|---|---|---|
| Unified CVP 12.5(1) to 15.0(1) | Yes | Perform an in-place upgrade from Windows Server 2016 to Windows Server 2019 or Windows Server 2022. Upgrade to Unified CVP 15.0(1) | Change in platform from 15.0(1) release. |
| Unified CVP 12.6(1) to 15.0(1) | Yes | Perform an in-place upgrade from Windows Server 2016 or Windows Server 2019 to Windows Server 2019 or Windows Server 2022. Upgrade to Unified CVP 15.0(1) | Change in platform from 15.0(1) release. |
| Unified CVP 12.6(2) to 15.0(1) | Yes | Perform an in-place upgrade from Windows Server 2016 or Windows Server 2019 to Windows Server 2019 or Windows Server 2022. Upgrade to Unified CVP 15.0(1) | Change in platform from 15.0(1) release. |

| Note | It is not necessary to upgrade all servers in a category in a single maintenance window; however, you must upgrade all Unified
                                             CVP components of one type before moving to the next set of components in the Unified CVP deployment or the Unified CVP unit. |
|---|---|

| Note | Unified CVP Server log files are saved in <CVP_HOME>\logs ; VXML Server log files are saved in <CVP_HOME>\VXMLServer\logs and <CVP_HOME>\VXMLServer\applications\<app_name>\logs . |
|---|---|

| Note | Exclude the following folders from on-access scanning configuration of the AV program from all Anti Virus scans: c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA , and D:\IFMXDATA . |
|---|---|

| Caution | The 15.0(1) release replaces the JRE and Tomcat versions. If you have updated any files in Tomcat (from the %CVP_HOME%\VXMLServer\Tomcat\webapps\CVP folder) or JRE configurations (from the %CVP_HOME%\JRE folder), ensure that you take a backup of the files before you proceed with the installation. You can restore the backup
                                       after the installation is complete. |
|---|---|

| Note | You must not use VMware vSphere Client (Thick Client) to upgrade the
                                          			 virtual machine hardware. |
|---|---|

| Step 1 | Power off the
                                          			 virtual machine. |
|---|---|
| Step 2 | Right-click
                                          			 the virtual machine, choose Edit
                                             				Settings . |
| Step 3 | Click the Virtual Hardware tab. |
| Step 4 | Click CPU . |
| Step 5 | From the Cores per Socket drop-down list, select 1 . |
| Step 6 | In the Reservation field, enter the CPU reservation speed (defined in MHz) for Unified CVP virtual machines. For more information about virtual hardware resource setting for CPU and memory, see Unified CVP Virtualization Wiki available at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html . |
| Step 7 | Click OK to save the settings. |

| Step 1 | Ensure that
                                          			 the virtual machine is switched off. |
|---|---|
| Step 2 | Right-click the Virtual Machine and select Edit Settings . |
| Step 3 | Click the Virtual Hardware tab. |
| Step 4 | Click Memory . |
| Step 5 | In the RAM field, change the RAM value (in MB) of Unified CVP virtual machines as defined in the Virtualization for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html . |
| Step 6 | In the Reservation field, enter the RAM value (in MB) corresponding to Unified CVP VMs, as defined in the Virtualization for Cisco Unified Customer Voice Portal . |
| Step 7 | Click OK to save the settings. |

| Step 1 | Ensure that
                                          			 the virtual machine is switched off. |
|---|---|
| Step 2 | Right-click the virtual machine and select Edit Settings . |
| Step 3 | Click the Virtual Hardware tab. |
| Step 4 | Click Upgrade . |
| Step 5 | Check the Schedule VM Compatibility Upgrade check box. |
| Step 6 | From the Compatible with (*) drop-down list, choose one of
                                          			 the following options: ESXi 7.1 U1 and later updates |
| Step 7 | Click OK to save the settings. |
| Step 8 | Power on the virtual machine. |

| Step 1 | Login to vSphere Client and select the Unified CVP virtual machine. |
|---|---|
| Step 2 | Right-click the virtual machine and select the option Edit Settings from the popup menu. The Virtual Machine Properties window pops up. |
| Step 3 | Select the Resources tab. The
                                          			 Virtual Hardware Resource Setting that can be customized is shown in the left
                                          			 dialog box. The Resource Allocation for respective virtual hardware is shown in
                                          			 the right. |
| Step 4 | Enable resource reservation for Unified CVP virtual machines. Note To enable the Virtual Hardware Resource reservation for Unified CVP virtual machines, the setting for CPU and memory must
                                                      be modified. For information about virtual hardware resource setting for CPU and memory, see Virtualization for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html . | Note | To enable the Virtual Hardware Resource reservation for Unified CVP virtual machines, the setting for CPU and memory must
                                                      be modified. For information about virtual hardware resource setting for CPU and memory, see Virtualization for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html . |
| Note | To enable the Virtual Hardware Resource reservation for Unified CVP virtual machines, the setting for CPU and memory must
                                                      be modified. For information about virtual hardware resource setting for CPU and memory, see Virtualization for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html . |
| Step 5 | After the virtual hardware resource setting for CPU and memory for CVP virtual machines are set, click OK to close the VM Properties dialog box. The CVP virtual machine is reconfigured and the Resource Reservation is enabled. |

| Note | To enable the Virtual Hardware Resource reservation for Unified CVP virtual machines, the setting for CPU and memory must
                                                      be modified. For information about virtual hardware resource setting for CPU and memory, see Virtualization for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html . |
|---|---|

| Note | By default, Windows Defender is enabled on Windows Server 2019 or Windows Server 2022. Windows Server 2019 or Windows Server
                                          2022 upgrade will prompt to uninstall the antivirus due to compatibility issue with Windows Defender. To proceed with the
                                          upgrade, uninstall the antivirus. For more information on Windows Defender antivirus compatibility, see https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/ windows-defender-antivirus-compatibility . |
|---|---|

| Step 1 | Mount Windows Server ISO image to the virtual machine. Open the file explorer and double-click on the Drive to run the Windows Server setup. |
|---|---|
| Step 2 | Select Download & install updates to let the installation go on smoothly. Click Next . |
| Step 3 | Select Windows Server Desktop Experience . Click Next . |
| Step 4 | Read the notes and license terms and then click Accept . |
| Step 5 | To retain existing Unified CVP configurations, files, services, and all associated settings intact after the inplace upgrade
                                       to Windows Sever 2019 or Windows Server 2022, select Keep personal files and apps . Then click Next . Note If you select Nothing , everything (including Unified CVP) in the existing Windows Server VM will be erased, and the system will be set up as a
                                                      new Windows Server 2019 or Windows Server 2022 VM. | Note | If you select Nothing , everything (including Unified CVP) in the existing Windows Server VM will be erased, and the system will be set up as a
                                                      new Windows Server 2019 or Windows Server 2022 VM. |
| Note | If you select Nothing , everything (including Unified CVP) in the existing Windows Server VM will be erased, and the system will be set up as a
                                                      new Windows Server 2019 or Windows Server 2022 VM. |
| Step 6 | In case a Window is displayed with the title What needs your attention , click Confirm to proceed because existing Unified CVP on Windows Server has been successfully validated to be working on Windows Server
                                       2019 or Windows Server 2022 when such an upgrade process is followed. Note Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed. | Note | Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed. |
| Note | Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed. |
| Step 7 | Use your existing credentials to log in to the system and ensure that Unified CVP-related services are up and running after
                                       the completion of Windows Server 2016 or Windows Server 2019 platform upgrade to Windows Server 2019 or Windows Server 2022. |

| Note | If you select Nothing , everything (including Unified CVP) in the existing Windows Server VM will be erased, and the system will be set up as a
                                                      new Windows Server 2019 or Windows Server 2022 VM. |
|---|---|

| Note | Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed. |
|---|---|

| Step 1 | Run (double click) CVP15.0.1.exe . A welcome screen is displayed. |
|---|---|
| Step 2 | Click Next to proceed. |
| Step 3 | Review and accept the Software License Agreement , and click Next . A warning message is displayed to backup all custom audio files. Click OK to proceed. |
| Step 4 | Click Install to start the MR installation. |
| Step 5 | Click Finish to complete the installation. Reboot the machine after the installation. |

| Note | For Unified CVP upgrade, u-law is the default media file format type. |
|---|---|

| Step 1 | Mount the Unified CVP ISO image. |
|---|---|
| Step 2 | Navigate to C:\CVP\installer_windows and run setup.exe. The installer automatically detects the previous installation and guides you through the upgrade process. |
| Step 3 | Restart the server. |
| Step 4 | Navigate to the C:\Cisco\CVP\conf location and manually configure the Unified CVP properties file. For more information, see the Manual Configuration of Unified
                                          CVP Properties section. |
| Step 5 | Restart the server. |

| Step 1 | Navigate to the C:\Cisco\CVP\conf location. |
|---|---|
| Step 2 | Convert the custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG), and applications that
                                          are in u-law to A-law. |
| Step 3 | In the cvp_pkgs.properties file, add the cvp-pkgs.PromptEncodeFormatALaw = 1 property at line 7 to enable the A-law flag. Note Ensure that you leave a space before and after the " = " sign. | Note | Ensure that you leave a space before and after the " = " sign. |
| Note | Ensure that you leave a space before and after the " = " sign. |
| Step 4 | Mount the Unified CVP ISO image, and run setup.exe. |
| Step 5 | Follow the instructions on the screen. |
| Step 6 | Restart the server. Note All the standard packaged media files and applications are installed in A-law format. Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade. | Note | All the standard packaged media files and applications are installed in A-law format. Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade. |
| Note | All the standard packaged media files and applications are installed in A-law format. Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade. |
| Step 7 | Navigate to the C:\Cisco\CVP\conf location and manually configure the Unified CVP properties file. For more information, see the Manual Configuration of Unified
                                          CVP Properties section. |
| Step 8 | Restart the server. |

| Note | Ensure that you leave a space before and after the " = " sign. |
|---|---|

| Note | All the standard packaged media files and applications are installed in A-law format. Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade. |
|---|---|

| Step 1 | Navigate to the C:\Cisco\CVP\conf location. |
|---|---|
| Step 2 | In the cvp_pkgs.properties file, add the cvp-pkgs.PromptEncodeFormatALaw = 1 property at line 7 to enable the A-law flag. Note Ensure that you leave a space before and after the " = " sign. | Note | Ensure that you leave a space before and after the " = " sign. |
| Note | Ensure that you leave a space before and after the " = " sign. |
| Step 3 | Mount the Unified CVP ISO image and run setup.exe. The installer automatically detects the previous installation, and guides you through the upgrade process. |
| Step 4 | Follow the instructions on the screen. |
| Step 5 | Restart the server. Note All the standard packaged media files and applications are installed in the A-law format. Custom media files, such as custom applications and WAAG, are retained in the format as they were prior to upgrade. | Note | All the standard packaged media files and applications are installed in the A-law format. Custom media files, such as custom applications and WAAG, are retained in the format as they were prior to upgrade. |
| Note | All the standard packaged media files and applications are installed in the A-law format. Custom media files, such as custom applications and WAAG, are retained in the format as they were prior to upgrade. |
| Step 6 | Navigate to the C:\Cisco\CVP\conf location and manually configure the Unified CVP properties file. For more information, see the Manual Configuration of Unified
                                          CVP Properties section. |
| Step 7 | Restart the server. |

| Note | Ensure that you leave a space before and after the " = " sign. |
|---|---|

| Note | All the standard packaged media files and applications are installed in the A-law format. Custom media files, such as custom applications and WAAG, are retained in the format as they were prior to upgrade. |
|---|---|

| Step 1 | Navigate to the C:\Cisco\CVP\conf location. |
|---|---|
| Step 2 | In the cvp_pkgs.properties file, add the cvp-pkgs.PromptEncodeFormatG729 = 1 property at line 7 to enable the G729 flag. Note Ensure that you leave a space before and after the " = " sign. | Note | Ensure that you leave a space before and after the " = " sign. |
| Note | Ensure that you leave a space before and after the " = " sign. |
| Step 3 | Mount the Unified CVP ISO image and run setup.exe. |
| Step 4 | Follow the instructions on the screen. |
| Step 5 | Restart the server. Note All the standard packaged media files and applications are installed in G729 format. Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade. | Note | All the standard packaged media files and applications are installed in G729 format. Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade. |
| Note | All the standard packaged media files and applications are installed in G729 format. Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade. |
| Step 6 | Navigate to the C:\Cisco\CVP\conf location and manually configure the Unified CVP properties file. For more information, see the Manual Configuration of Unified
                                          CVP Properties section. |
| Step 7 | Restart the server. |

| Note | Ensure that you leave a space before and after the " = " sign. |
|---|---|

| Note | All the standard packaged media files and applications are installed in G729 format. Custom media files, such as custom applications and Whisper Agent-Agent Greeting (WAAG) are retained in the format as they
                                                               were prior to upgrade. |
|---|---|

| Note | Before installing the Informix patch, consider the following: Informix does not support the rollback of an installation to a previous version. The standalone uninstallation of Informix is not a supported procedure. Given that the target upgrade version is Informix 14.10.FC12W5, standard backup and restore methods are incompatible due to
                                                   version discrepancies. It is recommended to take a snapshot of the Reporting Server before upgrading so you can restore it if any issues occur. Verify that the rootdbs is not full and has sufficient free space. The rootdbs must have at least 20-30% free space available to accommodate temporary objects, logs, and metadata updates during the upgrade
                                                   process. |
|---|---|

| Step 1 | Open the Windows Command Prompt as an administrator and run the following command: onstat - . Verify that the output displays version 14.10.FC10W2 . |
|---|---|
| Step 2 | Download and extract the downloaded Informix 14.10.FC12W5 package to a temporary local directory on the server. |
| Step 3 | Run the installer and execute the file ids_install.exe from the unzipped folder by following the steps below: Right-click on ids_install.exe and select Run as administrator . On the Installation page, click Next . On the License Agreement page, select I accept the terms in the license agreement and click Next . Specify the Informix installation location. Select Continue to proceed with the installation. Click Next to proceed through the configuration summary. Click Install to begin the upgrade process. |
| Step 4 | After the installation, start Informix Service by following the below steps: Open the Windows Services management console. Locate the Informix IDS service. Right-click on the service and select Start . |
| Step 5 | Verify the successful upgrade of the database engine by following the steps below: Open the Windows Command Prompt as an administrator. Run the following command: onstat - Confirm that the version output displays the required Informix version. Verify that all CCE-dependent services have successfully reconnected to the database. |

| Note | After successful upgrade of Unified CVP server, the CVP Call Server Service Startup Type is set to Automatic by default. |
|---|---|

| Step 1 | Mount the
                                       			 Unified CVP ISO image, and run setup.exe. The installer
                                          				automatically detects the installation and upgrade of Remote Operations and
                                          				guides you through the upgrade process. |
|---|---|
| Step 2 | Follow the
                                       			 instructions on the Upgrade screens and click Upgrade . |
| Step 3 | Restart the
                                       			 Server. |

| Step 1 | Open Call Studio, right-click any existing project in the Navigator view, choose Export . The Export wizard opens. |
|---|---|
| Step 2 | Navigate to General > File System , and click Next . Note From the list displayed by the Export wizard, select multiple projects to export them simultaneously. | Note | From the list displayed by the Export wizard, select multiple projects to export them simultaneously. |
| Note | From the list displayed by the Export wizard, select multiple projects to export them simultaneously. |
| Step 3 | Browse to the directory where the projects will be exported and click OK and then click Finish . |
| Step 4 | Uninstall the Call Studio software. For more information, see the Unified CVP/Call Studio Uninstallation section. |
| Step 5 | Install the Call Studio software. For more information, see the Install Unified Call Studio section. |

| Note | From the list displayed by the Export wizard, select multiple projects to export them simultaneously. |
|---|---|

| Note | The SolarWinds TFTP software and AnyConnect (while a VPN connection is enabled) are the known causes for the Call Studio debugger
                                          errors. To resolve the Call Studio debugger errors: If you are using SolarWinds, stop the SolarWinds TFTP software and run the debugger. If you are using AnyConnect, disconnect the VPN connection and run the debugger. |
|---|---|

| Important | After upgrade, restart the WebServicesManager service to use the system CLI. If you are using a VRU connection port other than the default port (5000), then click Save and Deploy of Unified CVP Call Server from OAMP. Perform the following steps for Smart Licensing to work after upgrading to Unified CVP 15.0(1) : Redeploy all Call Servers and VXML Servers from OAMP. Restart the services. VMWare Tools do not get updated automatically after upgrading to Unified , CVP 15.0(1) on Windows Server 2019/2022 and rebooting the machine. Workaround : Perform the following steps to update the VMWare Tools manually: Right-click on the VM. Go to Guest OS and select Upgrade VMWare Tools . After you upgrade to Unified CVP 15.0(1) , the WebServiceCredentials schema gets updated with the encryption method. To encrypt the wsm password in OAMP, do the following: Stop Cisco CVP OPSConsoleServer and Cisco CVP WebServicesManager services. Navigate to C:\Cisco\CVP\bin\ . Execute the mgr-init.bat -wsm <wsmadmin password> command from the command prompt. Restart the Cisco Unified CVP Operations Console and Cisco CVP WebServicesManager. The encryption key, which is a part of OAMP, is absent from the WebServicesCredentials.xml files on the CVP Call Server, VXML Server, and Reporting Servers. Workaround: To synchronize the WebServicesCredentials.xml with the encryption method, it is necessary to redeploy all the Call Servers, VXML Servers, and Reporting Servers. |
|---|---|

| Note | These steps are necessary only if the property is checked in the OAMP UI. |
|---|---|

| Step 1 | Log in to the CVP OAMP portal. |
|---|---|
| Step 2 | In the navigation pane, choose Courtesy Callback . |
| Step 3 | Uncheck the Allow unmatched Dialed Numbers check box and click Save . |
| Step 4 | Re-check the Allow unmatched Dialed Numbers check box and click Save . |
| Step 5 | Restart the CVP Reporting Server to apply the configuration changes. |

| Component | Upgrade Path | Procedure |
|---|---|---|
| CVP Server | 12.5(1) to 15.0(1) 12.6(1) to 15.0(1) 12.6(2) to 15.0(1) | No configuration required. |
| WebServices Manager | 12.5(1) to 15.0(1) 12.6(1) to 15.0(1) 12.6(2) to 15.0(1) | No configuration required. |
| Operations Console | 12.5(1) to 15.0(1) 12.6(1) to 15.0(1) 12.6(2) to 15.0(1) | No configuration required. |
| Reporting Server | 12.5(1) to 15.0(1) 12.6(1) to 15.0(1) 12.6(2) to 15.0(1) | No configuration required. |

| Note | Wsmadmin (CLI) users or any other serviceability/readonly role users cannot login or use OAMP/NOAMP/CLI until an Administrator
                                             or Super Administrator role user updates their password post an install/upgrade. |
|---|---|

| Step 1 | On the Unified CVP OAMP Server, navigate to the C:\Cisco\CVP\wsm\ CLI location. |
|---|---|
| Step 2 | Run the metasynch.cmd file with following arguments: wsm
                                                   				  username wsm
                                                   				  password Example: metasynch.cmd wsmusername wsmpassword MEDIA Usage : metasynch [options] username password [servertype] servertype : MEDIA/VXML /VXML_STANDALONE options : -help -? print this help message Note The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                         and all media files on Media servers. Logs for synch command tool can be found at the following location: C:\Cisco\CVP\wsm\CLI\log\SyncTool.log | Note | The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                         and all media files on Media servers. Logs for synch command tool can be found at the following location: |
| Note | The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                         and all media files on Media servers. Logs for synch command tool can be found at the following location: |

| Note | The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                         and all media files on Media servers. Logs for synch command tool can be found at the following location: |
|---|---|

| Step 1 | Upgrade the CVP server, the OAMP server, and the Reporting server to 15.0 version. |
|---|---|
| Step 2 | Log in to the Operations Console and click Device Management > Unified CVP Call Server . |
| Step 3 | Edit the call server record. |
| Step 4 | Go to SIP > Advanced Configurations > Security Properties . The available supported ciphers are listed. |
| Step 5 | Select the cipher starting with TLS_RSA. |
| Step 6 | Click Remove . |
| Step 7 | In the Supported Ciphers field, type TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 and click Add . |
| Step 8 | Click Save & Deploy . |
| Step 9 | Restart the CVP server. |