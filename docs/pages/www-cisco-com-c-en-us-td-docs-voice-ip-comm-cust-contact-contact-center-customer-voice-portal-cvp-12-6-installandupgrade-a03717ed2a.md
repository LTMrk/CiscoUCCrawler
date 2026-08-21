---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-installandupgrade-a03717ed2a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/installandupgrade/guide/ccvp_b_1261-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal_chapter_010.html
retrieved_at: 2026-08-21T17:03:58.630261+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: May 14, 2021

Chapter: Unified CVP Minor Release Upgrade

## Chapter: Unified CVP Minor Release Upgrade

# Unified CVP Minor Release Upgrade

Unified CVP 12.6(1) MR is an executable file which can be downloaded from CCO. The same executable file can be used to upgrade all Unified CVP
                        components.

Important

Before you install Unified CVP MR:

Refer to the licensing information in the Unified CVP Licensing chapter.

Ensure that the server chosen for Reporting Server is part of a workgroup.

Backup all custom audio files present in <CVP_HOME>/VXMLServer/tomcat/webapps/audio for Unified CVP upgrade.

Take a backup of the OAMP config using Export System Configuration from the system menu before OAMP upgrade.

After the successful upgrade, the Certificate Authorities (CAs) that are unapproved by Cisco are removed from the platform
                                    trust store. However, you can add them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle here .

For information about adding a certificate, see here .

## Upgrade Path

The following table lists the upgrade paths to replace the existing Unified CVP version with the MR on Windows Server 2016.

Unified CVP

12.5(1) to 12.6(1)

No

Direct upgrade to Unified CVP 12.6(1) through MR.

Unified CVP

12.5(1) + ES-33 and above to 12.6(1) + ES-18 or above

No

Direct upgrade to Unified CVP 12.6(1) through MR.

If the MR is installed on top of any 12.5(1) ES, the installer gives a warning to uninstall all ESs. However, this warning
                                          can be ignored.

ES-33 supports log4j.

After upgrading to 12.6(1), it is mandatory to install ES-18

Unified CVP

12.6(1) to 12.6(1) with latest Informix

No

Fresh installation of Unified CVP 12.5(1b) ISO with data migration.

For more information, see the Migrate Unified CVP Reporting Server section in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

This upgrade path can be followed for IBM Informix version 14.10 FC8 support on 12.6(1) release.

Migration is required only for the Reporting Server, where the customer needs to follow the migration procedure to upgrade
                                          to latest Informix.

On upgrading Reporting Server to CVP 12.5(1b), CallServer and OAMP can stay on 12.5(1)/12.5(1a).

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

## Upgrade Unified CVP Components

Unified CVP Server

Operations Console

Remote Operations

Unified CVP Reporting Server

Follow the given steps to install the Unified CVP 12.6(1) on each of the above components:

Step 1

Run (double click) CVP12.6.1.exe . A welcome screen is displayed.

Step 2

Click Next to proceed.

Step 3

Review and accept the Software License Agreement , and click Next .

A warning message is displayed to backup all custom audio files. Click OK to proceed.

Step 4

Click Install to start the MR installation.

As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed:

```
Following engineering special(s) installed in the system, are not merged into CVP 12.6(1) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(1) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade?
```

Click Yes to proceed only if the installed 12.5 ES is lesser than ES-21.

If any of the 12.5 ES installed is greater than ES-21, functionality may be lost after the 12.6(1) MR installation. Therefore,
                                                      it is recommended to install the latest available 12.6(1) ES after the MR installation.

Step 5

Click Finish to complete the MR installation. Reboot the machine after the installation.

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

If you have added the certificates in .ormkeystore , then add them again in .keystore .

Run the following command to retrieve the password for the keytool.

more %CVP_HOME%\conf\security.properties .

The output of the command is Security.keystorePW = <Returns the keystore password> .

Perform the following steps for Smart Licensing to work after upgrading to Unified CVP 12.6(1) :

Redeploy all Call Servers and VXML Servers from OAMP.

Restart the services.

VMWare Tools do not get updated automatically after upgrading to Unified CVP 12.6(1) ,  on Windows Server 2016/2019 and rebooting the machine.

Workaround : Perform the following steps to update the VMWare Tools manually:

Right-click on the VM.

Go to Guest OS and select Upgrade VMWare Tools .

After you upgrade to Unified , the WebServiceCredentials schema gets updated with the encryption method.

To encrypt the wsm password in OAMP, do the following:

Stop Cisco CVP OPSConsoleServer and Cisco CVP WebServicesManager services.

Navigate to C:\Cisco\CVP\bin\ .

Execute the mgr-init.bat -wsm <wsmadmin password> command from the command prompt.

Restart the Cisco Unified CVP Operations Console and Cisco CVP WebServicesManager.

The encryption key, which is a part of OAMP, is absent from the WebServicesCredentials.xml files on the CVP Call Server, VXML Server, and Reporting Servers.

Workaround: To synchronize the WebServicesCredentials.xml with the encryption method, it is necessary to redeploy all the Call Servers, VXML Servers, and Reporting Servers.

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

| Important | Before you install Unified CVP MR: Refer to the licensing information in the Unified CVP Licensing chapter. Ensure that the server chosen for Reporting Server is part of a workgroup. Backup all custom audio files present in <CVP_HOME>/VXMLServer/tomcat/webapps/audio for Unified CVP upgrade. Take a backup of the OAMP config using Export System Configuration from the system menu before OAMP upgrade. |
|---|---|

| Note | After the successful upgrade, the Certificate Authorities (CAs) that are unapproved by Cisco are removed from the platform
                                    trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle here . For information about adding a certificate, see here . |
|---|---|

| Upgrade Path from Older Release to New Release | Platform Change | Conversion Process | Description |
|---|---|---|---|
| Unified CVP 12.5(1) to 12.6(1) | No | Direct upgrade to Unified CVP 12.6(1) through MR. | Platform change is not required. |
| Unified CVP 12.5(1) + ES-33 and above to 12.6(1) + ES-18 or above | No | Direct upgrade to Unified CVP 12.6(1) through MR. | If the MR is installed on top of any 12.5(1) ES, the installer gives a warning to uninstall all ESs. However, this warning
                                          can be ignored. ES-33 supports log4j. After upgrading to 12.6(1), it is mandatory to install ES-18 |
| Unified CVP 12.6(1) to 12.6(1) with latest Informix | No | Fresh installation of Unified CVP 12.5(1b) ISO with data migration. For more information, see the Migrate Unified CVP Reporting Server section in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . | This upgrade path can be followed for IBM Informix version 14.10 FC8 support on 12.6(1) release. Migration is required only for the Reporting Server, where the customer needs to follow the migration procedure to upgrade
                                          to latest Informix. |

| Note | On upgrading Reporting Server to CVP 12.5(1b), CallServer and OAMP can stay on 12.5(1)/12.5(1a). |
|---|---|

| Note | It is not necessary to upgrade all servers in a category in a single maintenance window; however, you must upgrade all Unified
                                             CVP components of one type before moving to the next set of components in the Unified CVP deployment or the Unified CVP unit. |
|---|---|

| Step 1 | Run (double click) CVP12.6.1.exe . A welcome screen is displayed. |
|---|---|
| Step 2 | Click Next to proceed. |
| Step 3 | Review and accept the Software License Agreement , and click Next . A warning message is displayed to backup all custom audio files. Click OK to proceed. |
| Step 4 | Click Install to start the MR installation. Note As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed: Following engineering special(s) installed in the system, are not merged into CVP 12.6(1) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(1) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade? Click Yes to proceed only if the installed 12.5 ES is lesser than ES-21. If any of the 12.5 ES installed is greater than ES-21, functionality may be lost after the 12.6(1) MR installation. Therefore,
                                                      it is recommended to install the latest available 12.6(1) ES after the MR installation. | Note | As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed: Following engineering special(s) installed in the system, are not merged into CVP 12.6(1) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(1) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade? Click Yes to proceed only if the installed 12.5 ES is lesser than ES-21. If any of the 12.5 ES installed is greater than ES-21, functionality may be lost after the 12.6(1) MR installation. Therefore,
                                                      it is recommended to install the latest available 12.6(1) ES after the MR installation. |
| Note | As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed: Following engineering special(s) installed in the system, are not merged into CVP 12.6(1) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(1) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade? Click Yes to proceed only if the installed 12.5 ES is lesser than ES-21. If any of the 12.5 ES installed is greater than ES-21, functionality may be lost after the 12.6(1) MR installation. Therefore,
                                                      it is recommended to install the latest available 12.6(1) ES after the MR installation. |
| Step 5 | Click Finish to complete the MR installation. Reboot the machine after the installation. |

| Note | As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed: Following engineering special(s) installed in the system, are not merged into CVP 12.6(1) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(1) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade? Click Yes to proceed only if the installed 12.5 ES is lesser than ES-21. If any of the 12.5 ES installed is greater than ES-21, functionality may be lost after the 12.6(1) MR installation. Therefore,
                                                      it is recommended to install the latest available 12.6(1) ES after the MR installation. |
|---|---|

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

| Important | After upgrade, restart the WebServicesManager service to use the system CLI. If you are using a VRU connection port other than the default port (5000), then click Save and Deploy of Unified CVP Call Server from OAMP. If you have added the certificates in .ormkeystore , then add them again in .keystore . Run the following command to retrieve the password for the keytool. more %CVP_HOME%\conf\security.properties . The output of the command is Security.keystorePW = <Returns the keystore password> . Perform the following steps for Smart Licensing to work after upgrading to Unified CVP 12.6(1) : Redeploy all Call Servers and VXML Servers from OAMP. Restart the services. VMWare Tools do not get updated automatically after upgrading to Unified CVP 12.6(1) ,  on Windows Server 2016/2019 and rebooting the machine. Workaround : Perform the following steps to update the VMWare Tools manually: Right-click on the VM. Go to Guest OS and select Upgrade VMWare Tools . After you upgrade to Unified , the WebServiceCredentials schema gets updated with the encryption method. To encrypt the wsm password in OAMP, do the following: Stop Cisco CVP OPSConsoleServer and Cisco CVP WebServicesManager services. Navigate to C:\Cisco\CVP\bin\ . Execute the mgr-init.bat -wsm <wsmadmin password> command from the command prompt. Restart the Cisco Unified CVP Operations Console and Cisco CVP WebServicesManager. The encryption key, which is a part of OAMP, is absent from the WebServicesCredentials.xml files on the CVP Call Server, VXML Server, and Reporting Servers. Workaround: To synchronize the WebServicesCredentials.xml with the encryption method, it is necessary to redeploy all the Call Servers, VXML Servers, and Reporting Servers. |
|---|---|

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