---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-installation-guid-e4addf0a16
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/installation/guide/ccvp_b_install_and_upgrade_12-5/ccvp_b_install_and_upgrade_12-5_chapter_0101.html
retrieved_at: 2026-08-21T03:07:32.121806+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: January 31, 2020

Chapter: Upgrade Unified CVP

## Chapter: Upgrade Unified CVP

# Upgrade Unified CVP

If the existing software is to be replaced with a newer version with a change in platform, architecture, or applications,
                        the process is called migration. For example, replacing Unified CVP 11.5(1) with Unified CVP 12.5(1) is a migration because the newer version works on a different platform than the older version. To learn whether replacing
                        the existing version with a new version is an upgrade or a migration, see the Upgrade Path section.

Upgrade of Cisco voice solution components is a multistage process; solution components are grouped in several stages for
                        upgrading. Users must follow the solution level upgrade order mentioned in the Upgrade section of the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html for smooth transitioning to higher grade versions.

Important

A new 12.5(1b) base installer is available for customers, which has OpenJDK JRE as the supporting Java runtime for the Unified CVP application.
                                    It is the same as the preceding 12.5(1) installer, except that in the 12.5(1b) base installer, the Java runtime environment
                                    is installed on the Unified CVP virtual machines (VMs).

You can continue to use Oracle JRE if you installed CVP 12.5(1) before the release of 12.5(1b). Further, you can download
                                    and install the Java security updates from the Oracle website.

For JRE update post installation of 12.5(1b), refer to the OpenLogic OpenJDK site to download the JREs.

Customers who are not installing 12.5(1b) and staying on 12.5(1) release can install the CVP ES to migrate from Oracle JRE
                                    to OpenJDK JRE. All subsequent ESs would be supported on top of this ES.

Upon installation of ES 33, the JRE in the CVP is updated with OpenLogic JRE. Any specific changes in configuration files
                                    of the JRE folder should be backed up and reconfigured after the JRE update.

Important

In the new 12.5(1b) release, CVP Reporting Server has support for IBM Informix version 14.10 FC8.

For migrating the Reporting Server from 12.5(1) to 12.5(1b), see Migrate Unified CVP Reporting Server .

Important

In the new 15.0(1) release, CVP Reporting Server has support for IBM Informix version 14.10 FC10W2.

For migrating the Reporting Server from 12.x to 15.0(1), see Migrate Unified CVP Reporting Server .

Push the TCL and VXML files to their respective ingress and VXML gateways after the CVP Operations Console is upgraded, but before any other CVP components are upgraded.

After the successful upgrade, the Certificate Authorities (CAs) that are unapproved by Cisco are removed from the platform
                                    trust store. However, you can add them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle here .

For information about adding a certificate, see here .

By default, Windows Defender is enabled on Windows Server 2016 . Windows Server 2016 upgrade will prompt to uninstall the antivirus due to compatibility issue with Windows Defender. To proceed with the upgrade,
                                    uninstall the antivirus. For more information on Windows Defender antivirus compatibility, see https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/ windows-defender-antivirus-compatibility .

## Upgrade Path

The following table lists the upgrade paths to replace an existing Unified CVP version with a new one.

Unified CVP

12.0(1) to 12.5(1b)

No

Direct upgrade to Unified CVP 12.5(1b).

For more information, see .

For more information, see Upgrade Windows Server .

Unified CVP

12.5(1) to 12.5(1b)

No

Fresh installation of Unified CVP 12.5(1b) ISO with data migration.

For more information, see Migrate Unified CVP Reporting Server .

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

- ESXi 6.5 with VMFS 5

- ESXi 6.5 U2 and later updates with VMFS 6

- ESXi 6.7 with VMFS 6

Step 7

Click OK to save the settings.

Step 8

Power on the virtual machine.

#### What to do next

Expand the Virtual
                                 		  Machines Disk Space

### Expand Disk Space of Virtual Machines

Complete the following procedure to expand the virtual machines disk space on Unified CVP virtual machines.

Step 1

Ensure that
                                          			 the virtual machine is switched off.

Step 2

Right-click
                                          			 the virtual machine and choose Edit
                                             				Settings .

Step 3

Click the Virtual Hardware tab.

Step 4

In the Hard disk 1 field, change the disk size value (in GB) of the Unified CVP virtual machines, as defined in the Virtualization for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html .

Step 5

Click OK .

Step 6

Power on the
                                          			 virtual machine.

Step 7

Log into your operating system.

Step 8

Right-click My PC and select Manage .

Step 9

Select File and Storage Services > Disks .

Step 10

In the Volumes area, right-click C drive and select Extend Volume… .

Step 11

Change the disk size value (in GB) of the Unified CVP virtual machines as defined in the Unified CVP Virtualization Wiki .

Step 12

Click OK .

Step 13

Restart the
                                          			 server.

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

Step 1

Mount Windows Server ISO image to the virtual machine. Open the file explorer and double-click on the DVD Drive to run the Windows Server setup.

Step 2

Select Download & install updates to let the installation go on smoothly. Click Next .

Step 3

Select Windows Server Desktop Experience . Click Next .

Step 4

Read the notes and license terms and then click Accept .

Step 5

To retain existing Unified CVP configurations, files, services, and all associated settings intact after the inplace upgrade
                                       to Windows Sever 2016, select Keep personal files and apps . Then click Next .

If you select Nothing , everything (including Unified CVP) in the existing Windows Server 2012 VM will be erased, and the system will be set up
                                                      as a new Windows Server 2016 VM.

Step 6

In case a Window is displayed with the title What needs your attention , click Confirm to proceed because existing Unified CVP on Windows Server 2012 has been successfully validated to be working on Windows Server
                                       2016 when such an upgrade process is followed.

Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed.

Step 7

Use your existing credentials to log in to the system and ensure that Unified CVP-related services are up and running after
                                       the completion of Windows Server 2012 platform upgrade to Windows Server 2016.

## Upgrade Operations
                        	 Console

The installed default media files are overwritten with the media format you choose for the Unified CVP upgrade; however, the
                              customized media files are not overwritten during the upgrade. Customized media files, such as custom applications and Whisper
                              Agent-Agent Greeting (WAAG), are retained in the format as they were prior to upgrade.

Following sections describe the various scenarios of Operations Console upgrade.

### Upgrade Operations Console 12.0(1) in U-law to Operations Console 12.5(1) in U-law

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

### Upgrade Operations Console 12.0(1) in U-law to Operations Console 12.5(1) in A-law

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

### Upgrade Operations Console 12.0(1) in A-law to Operations Console 12.5(1) in A-law

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

### Upgrade Operations Console 12.0(1) in A-law or U-law to Operations Console 12.5(1) in G729

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

You cannot upgrade CVP Reporting Server from 12.0 to 12.5 because the version of IBM Informix database server has changed.
                              You need to uninstall CVP Reporting Server 12.0 and install CVP Reporting Server 12.5.

For more information, see Migrate Unified CVP Reporting Server .

## Upgrade Unified CVP Server

### Before you begin

After successful upgrade of Unified CVP server, the CVP Call Server Service Startup Type is set to Automatic by default.

### Upgrade CVP Server 12.0(1) in U-law to CVP Server 12.5(1) in U-law

Perform Steps 1 to 4 of the Upgrade Operations Console 12.0(1) in U-law to Operations Console 12.5(1) in U-law procedure.

Log into Operations Console of the current version of Unified CVP and click Bulk Administration > File Transfer > Scripts and Media .

Load the gateway download transferred files into the Cisco IOS memory for each CVP service using the Cisco IOS call application voice load <service_name> CLI command.

Restore any backed-up third-party libraries.

### Upgrade CVP Server 12.0(1) in U-law to CVP Server 12.5(1) in A-law

Perform Steps 1 to 8 of the Upgrade Operations Console 12.0(1) in U-law to Operations Console 12.5(1) in A-law.

### Upgrade CVP Server 12.0(1) in A-law to CVP Server 12.5(1) in A-law

Perform Steps 1 to 7 of the Upgrade Operations Console 12.0(1) in A-law to Operations Console 12.5(1) in A-law procedure.

### Upgrade CVP Server 12.0(1) in A-law or U-law to CVP Server 12.5(1) in G729

Perform Steps 1 to 7 of the Upgrade Operations Console 12.0(1) in A-law or U-law to Operations Console 12.5(1) in G729 procedure.

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

## Postupgrade
                        	 Tasks

After you upgrade the Unified CVP components, synchronize the metadata files using the Sync-up tool. For more information,
                           see Initiate Metadata Synchronization for Unified CVP Rest API .

After upgrade, restart the WebServicesManager service to use system CLI.

If you are using a VRU connection port other than the default port (5000), then click Save and Deploy of Unified CVP Call Server from OAMP.

If you have added the certificates in .ormkeystore, then add them again in .keystore.

Execute  the following command to retrieve the password for keytool.

more %CVP_HOME%\conf\security.properties .

The  output of the command is Security.keystorePW = <Returns the keystore password> .

Execute the following steps for Smart Licensing to work after upgrading to CVP 12.5(1).

Redeploy all Call Servers and VXML Servers from OAMP.

Restart the services.

VMWare Tools do not get updated automatically after upgrading to CVP 12.5 on Windows Server 2016 and rebooting the machine.

Workaround : Execute the following steps to update the VMWare Tools manually.

Right-click on the VM.

Go to Guest OS and select Upgrade VMWare Tools .

### Manual Configuration of Unified CVP Properties

The following table lists the procedure to manually configure the Unified CVP properties files based on the upgrade path.

Component

Upgrade Path

CVP Server

12.0(1) to 12.5(1)

```
VXML.usagefactor = 1.0
```

```
SIP.CloudConnect.RequestTimeout = 6000
SIP.CloudConnect.publisherAddress =
SIP.CloudConnect.subscriberAddress =
SIP.CloudConnect.CreateMeetingApi = /evapoint/meeting/create
SIP.CloudConnect.username =
SIP.CloudConnect.DeleteMeetingApi = /evapoint/meeting/end
SIP.CloudConnect.password =
SIP.CloudConnect.StatusApi = /evapoint/status
#Cloud connect Survey Endpoint API
SIP.CloudConnect.SurveyEndPointApi = /cherrypoint/surveyendpoint
```

```
SIP.CloudConnect.AuthTokenApi = /cherrypoint/authtoken
```

```
#CLoudCherry Customer ID
SIP.CloudCherry.CustomerID = icm
#CloudCherry Email ID
SIP.CloudCherry.CustomerEmailID = abc@cc.demo.com
```

```
SIP.CloudCherry.SurveyValidityTime = 300000
```

Open the ivr.properties file and add the following entry:

```
IVR.AuthTokenRefreshTimeOut = 1800 
IVR.SurveyTokenRefreshTimeOut = 43200
IVR.SurveyQuestionRefreshTimeOut = 43200 
IVR.WxmSurveyTokenApiUrl = https://api.getcloudcherry.com/api/SurveyToken
IVR.WxmSurveyQuestionsApiUrl = https://api.getcloudcherry.com/api/Questions/Questionnaire
IVR.WxmSurveyAnswersSubmitApiUrl = https://api.getcloudcherry.com/api/SurveyByToken/
IVR.WxmSurveySettingsApiUrl = https://api.getcloudcherry.com/api/Settings/
IVR.WxmAudioUrl=https://api.getcloudcherry.com/api/StreamUserAsset/
IVR.WxmSurveyQuestionnaireUrl = https://api.getcloudcherry.com/api/surveyquestionnaire/
```

```
#Cloud Cherry batch properties (thresholds to trigger the SMS/Email Cloud Connect API)
IVR.CloudCherryBatchSize = 100 #Or optimized value
IVR.CloudCherryBatchTimeout = 60 #Or optimized value
```

Add the following entries in the respective files:

```
jmx_callserver.conf com.sun.management.jmxremote.rmi.port = 2097
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2 jmx_oamp.conf com.sun.management.jmxremote.rmi.port = 10000
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2 jmx_vxml.conf com.sun.management.jmxremote.rmi.port = 9697
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2 jmx_wsm.conf com.sun.management.jmxremote.rmi.port = 10003
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2 orm_jmx.properties com.sun.management.jmxremote.rmi.port=3000
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2
```

Restart the CVP and VXML services.

WebServices Manager

12.0(1) to 12.5(1)

No configuration required.

Operations Console

12.0(1) to 12.5(1)

No configuration required.

Reporting Server

12.0(1) to 12.5(1)

No configuration required.

| Important | A new 12.5(1b) base installer is available for customers, which has OpenJDK JRE as the supporting Java runtime for the Unified CVP application.
                                    It is the same as the preceding 12.5(1) installer, except that in the 12.5(1b) base installer, the Java runtime environment
                                    is installed on the Unified CVP virtual machines (VMs). You can continue to use Oracle JRE if you installed CVP 12.5(1) before the release of 12.5(1b). Further, you can download
                                    and install the Java security updates from the Oracle website. For JRE update post installation of 12.5(1b), refer to the OpenLogic OpenJDK site to download the JREs. Customers who are not installing 12.5(1b) and staying on 12.5(1) release can install the CVP ES to migrate from Oracle JRE
                                    to OpenJDK JRE. All subsequent ESs would be supported on top of this ES. |
|---|---|

| Note | Upon installation of ES 33, the JRE in the CVP is updated with OpenLogic JRE. Any specific changes in configuration files
                                    of the JRE folder should be backed up and reconfigured after the JRE update. |
|---|---|

| Important | In the new 12.5(1b) release, CVP Reporting Server has support for IBM Informix version 14.10 FC8. For migrating the Reporting Server from 12.5(1) to 12.5(1b), see Migrate Unified CVP Reporting Server . |
|---|---|

| Important | In the new 15.0(1) release, CVP Reporting Server has support for IBM Informix version 14.10 FC10W2. For migrating the Reporting Server from 12.x to 15.0(1), see Migrate Unified CVP Reporting Server . |
|---|---|

| Note | Push the TCL and VXML files to their respective ingress and VXML gateways after the CVP Operations Console is upgraded, but before any other CVP components are upgraded. |
|---|---|

| Note | After the successful upgrade, the Certificate Authorities (CAs) that are unapproved by Cisco are removed from the platform
                                    trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle here . For information about adding a certificate, see here . |
|---|---|

| Note | By default, Windows Defender is enabled on Windows Server 2016 . Windows Server 2016 upgrade will prompt to uninstall the antivirus due to compatibility issue with Windows Defender. To proceed with the upgrade,
                                    uninstall the antivirus. For more information on Windows Defender antivirus compatibility, see https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/ windows-defender-antivirus-compatibility . |
|---|---|

| Upgrade Path from Older Release to New Release | Platform Change | Conversion Process | Description |
|---|---|---|---|
| Unified CVP 12.0(1) to 12.5(1b) | No | Direct upgrade to Unified CVP 12.5(1b). For more information, see . | Platform change is not required because CVP 12.5(1b) is supported on Windows Server 2016 and Windows Server 2019. Note For more information, see Upgrade Windows Server . | Note | For more information, see Upgrade Windows Server . |
| Note | For more information, see Upgrade Windows Server . |
| Unified CVP 12.5(1) to 12.5(1b) | No | Fresh installation of Unified CVP 12.5(1b) ISO with data migration. For more information, see Migrate Unified CVP Reporting Server . | Platform change is not required. |

| Note | For more information, see Upgrade Windows Server . |
|---|---|

| Note | It is not necessary to upgrade all servers in a category in a single maintenance window; however, you must upgrade all Unified
                                             CVP components of one type before moving to the next set of components in the Unified CVP deployment or the Unified CVP unit. |
|---|---|

| Note | Unified CVP Server log files are saved in <CVP_HOME>\logs ; VXML Server log files are saved in <CVP_HOME>\VXMLServer\logs and <CVP_HOME>\VXMLServer\applications\<app_name>\logs . |
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
                                          			 the following options: ESXi 6.5 with VMFS 5 ESXi 6.5 U2 and later updates with VMFS 6 ESXi 6.7 with VMFS 6 |
| Step 7 | Click OK to save the settings. |
| Step 8 | Power on the virtual machine. |

| Step 1 | Ensure that
                                          			 the virtual machine is switched off. |
|---|---|
| Step 2 | Right-click
                                          			 the virtual machine and choose Edit
                                             				Settings . |
| Step 3 | Click the Virtual Hardware tab. |
| Step 4 | In the Hard disk 1 field, change the disk size value (in GB) of the Unified CVP virtual machines, as defined in the Virtualization for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-customer-voice-portal.html . |
| Step 5 | Click OK . |
| Step 6 | Power on the
                                          			 virtual machine. |
| Step 7 | Log into your operating system. |
| Step 8 | Right-click My PC and select Manage . |
| Step 9 | Select File and Storage Services > Disks . |
| Step 10 | In the Volumes area, right-click C drive and select Extend Volume… . |
| Step 11 | Change the disk size value (in GB) of the Unified CVP virtual machines as defined in the Unified CVP Virtualization Wiki . |
| Step 12 | Click OK . |
| Step 13 | Restart the
                                          			 server. |

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

| Step 1 | Mount Windows Server ISO image to the virtual machine. Open the file explorer and double-click on the DVD Drive to run the Windows Server setup. |
|---|---|
| Step 2 | Select Download & install updates to let the installation go on smoothly. Click Next . |
| Step 3 | Select Windows Server Desktop Experience . Click Next . |
| Step 4 | Read the notes and license terms and then click Accept . |
| Step 5 | To retain existing Unified CVP configurations, files, services, and all associated settings intact after the inplace upgrade
                                       to Windows Sever 2016, select Keep personal files and apps . Then click Next . Note If you select Nothing , everything (including Unified CVP) in the existing Windows Server 2012 VM will be erased, and the system will be set up
                                                      as a new Windows Server 2016 VM. | Note | If you select Nothing , everything (including Unified CVP) in the existing Windows Server 2012 VM will be erased, and the system will be set up
                                                      as a new Windows Server 2016 VM. |
| Note | If you select Nothing , everything (including Unified CVP) in the existing Windows Server 2012 VM will be erased, and the system will be set up
                                                      as a new Windows Server 2016 VM. |
| Step 6 | In case a Window is displayed with the title What needs your attention , click Confirm to proceed because existing Unified CVP on Windows Server 2012 has been successfully validated to be working on Windows Server
                                       2016 when such an upgrade process is followed. Note Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed. | Note | Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed. |
| Note | Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed. |
| Step 7 | Use your existing credentials to log in to the system and ensure that Unified CVP-related services are up and running after
                                       the completion of Windows Server 2012 platform upgrade to Windows Server 2016. |

| Note | If you select Nothing , everything (including Unified CVP) in the existing Windows Server 2012 VM will be erased, and the system will be set up
                                                      as a new Windows Server 2016 VM. |
|---|---|

| Note | Once the upgrade begins, the system will restart multiple times without prompting until the upgrade is completed. |
|---|---|

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

| Note | After upgrade, restart the WebServicesManager service to use system CLI. |
|---|---|

| Note | If you are using a VRU connection port other than the default port (5000), then click Save and Deploy of Unified CVP Call Server from OAMP. If you have added the certificates in .ormkeystore, then add them again in .keystore. |
|---|---|

| Note | Execute  the following command to retrieve the password for keytool. more %CVP_HOME%\conf\security.properties . The  output of the command is Security.keystorePW = <Returns the keystore password> . |
|---|---|

| Note | Execute the following steps for Smart Licensing to work after upgrading to CVP 12.5(1). Redeploy all Call Servers and VXML Servers from OAMP. Restart the services. |
|---|---|

| Note | VMWare Tools do not get updated automatically after upgrading to CVP 12.5 on Windows Server 2016 and rebooting the machine. Workaround : Execute the following steps to update the VMWare Tools manually. Right-click on the VM. Go to Guest OS and select Upgrade VMWare Tools . |
|---|---|

| Component | Upgrade Path | Procedure |
|---|---|---|
| CVP Server | 12.0(1) to 12.5(1) | Open the vxml.properties file and add the following entry: VXML.usagefactor = 1.0 Open the sip.properties file and add the following entry: SIP.CloudConnect.RequestTimeout = 6000
SIP.CloudConnect.publisherAddress =
SIP.CloudConnect.subscriberAddress =
SIP.CloudConnect.CreateMeetingApi = /evapoint/meeting/create
SIP.CloudConnect.username =
SIP.CloudConnect.DeleteMeetingApi = /evapoint/meeting/end
SIP.CloudConnect.password =
SIP.CloudConnect.StatusApi = /evapoint/status
#Cloud connect Survey Endpoint API
SIP.CloudConnect.SurveyEndPointApi = /cherrypoint/surveyendpoint SIP.CloudConnect.AuthTokenApi = /cherrypoint/authtoken #CLoudCherry Customer ID
SIP.CloudCherry.CustomerID = icm
#CloudCherry Email ID
SIP.CloudCherry.CustomerEmailID = abc@cc.demo.com SIP.CloudCherry.SurveyValidityTime = 300000 Open the ivr.properties file and add the following entry: IVR.AuthTokenRefreshTimeOut = 1800 
IVR.SurveyTokenRefreshTimeOut = 43200
IVR.SurveyQuestionRefreshTimeOut = 43200 
IVR.WxmSurveyTokenApiUrl = https://api.getcloudcherry.com/api/SurveyToken
IVR.WxmSurveyQuestionsApiUrl = https://api.getcloudcherry.com/api/Questions/Questionnaire
IVR.WxmSurveyAnswersSubmitApiUrl = https://api.getcloudcherry.com/api/SurveyByToken/
IVR.WxmSurveySettingsApiUrl = https://api.getcloudcherry.com/api/Settings/
IVR.WxmAudioUrl=https://api.getcloudcherry.com/api/StreamUserAsset/
IVR.WxmSurveyQuestionnaireUrl = https://api.getcloudcherry.com/api/surveyquestionnaire/ #Cloud Cherry batch properties (thresholds to trigger the SMS/Email Cloud Connect API)
IVR.CloudCherryBatchSize = 100 #Or optimized value
IVR.CloudCherryBatchTimeout = 60 #Or optimized value Add the following entries in the respective files: jmx_callserver.conf com.sun.management.jmxremote.rmi.port = 2097
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2 jmx_oamp.conf com.sun.management.jmxremote.rmi.port = 10000
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2 jmx_vxml.conf com.sun.management.jmxremote.rmi.port = 9697
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2 jmx_wsm.conf com.sun.management.jmxremote.rmi.port = 10003
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2 orm_jmx.properties com.sun.management.jmxremote.rmi.port=3000
com.sun.management.jmxremote.ssl.enabled.protocols=TLSv1.2 Restart the CVP and VXML services. |
| WebServices Manager | 12.0(1) to 12.5(1) | No configuration required. |
| Operations Console | 12.0(1) to 12.5(1) | No configuration required. |
| Reporting Server | 12.0(1) to 12.5(1) | No configuration required. |