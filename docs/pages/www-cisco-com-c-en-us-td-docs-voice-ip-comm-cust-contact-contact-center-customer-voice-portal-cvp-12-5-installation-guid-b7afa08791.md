---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-installation-guid-b7afa08791
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/installation/guide/ccvp_b_install_and_upgrade_12-5/ccvp_b_install_and_upgrade_12-5_chapter_0111.html
retrieved_at: 2026-08-21T03:07:40.084610+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: January 31, 2020

Chapter: Unified CVP
	 Migration

## Chapter: Unified CVP
	 Migration

# Unified CVP
                     	 Migration

If there is a change in platform of a later release of Unified CVP, migration from the existing release to the later release
                           is required. For example, moving from Unified CVP 12.0(1) on Windows Server 2012 to Unified CVP 12.5(1) is considered a migration
                           because it involves a change in operating system (Windows Server 2012 to Windows Server 2016), platform, or architecture of
                           the later release.

Migration can also involve moving to a new hardware or a software and moving from one database to another database. Migration
                           of database requires converting the data into a common format that can be used as output from the old database and saved into
                           the new database.

If you have enabled secure communication, see the Unified CVP Security chapter in Configuration Guide for Cisco Unified Customer Voice Portal for instructions on uploading certificate for the secure communication.

## Premigration
                        	 Tasks

### Before you begin

Back up the
                                    				Unified CVP installation files and data onto a different computer for
                                    				redundancy.

Important

Uninstall Cisco Security Agent.

(Optional)
                                    				Deploy additional servers if you choose to deploy Reporting Server.

(Optional)
                                    				Standalone distributed diagnostics and service network (SDDSN) is no longer
                                    				required. If you have SDDSN servers, decommission these servers or use them for
                                    				another purpose.

Deploy Operations Console. For deployment of Operations Console, see Configuration Guide for
                                             				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

(Optional) Gatekeepers are not required in SIP implementations. Decommission gatekeepers or in some cases convert them to
                                    use as ingress or VXML gateways (or both) if you choose to use SIP for the implementation.

(Optional) SIP Proxy servers and DNS servers for SIP message routing are optional components for SIP implementation. Add these
                                    components to the network if you intend to use them.

Ensure that
                                    				the version of Cisco IOS supports the required hardware.

Migrate the operating system. For more information, see the Compatibility Matrix available at https://cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

## Migrate Operations
                        	 Console

To migrate Operations Console, back up and restore the CVP Operations Console configuration. To know whether a change in platform
                              is required, see the Upgrade Path section.

### Back Up Operations
                           	 Console Configuration

Step 1

Log in to
                                          			 Operations Console.

Step 2

On the
                                          			 Operations Console page, click System > Export System
                                                				  Configuration > Export .

Step 3

Manually copy
                                          			 the sip.properties file.

For more information on Unified CVP Console Configuration, see Administration Guide for
                                                      				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

Step 4

Save the CVP-OpsConsole-Backup.zip file.

This file is password protected and can be opened only by the target OAMP server if the administrator password (at least 12
                                                         characters long) matches that of the server from where it is exported.

#### What to do next

Save the exported configuration and custom files on network storage media or a portable storage media.

Ensure that you are able to access the shared storage media from the Windows Server Machine.

### Restore Operations
                           	 Console Configuration

#### Before you begin

For latest operating system, see the Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

Export the Operations Console configuration from the older version to migrate it to the new version.

Step 1

Stop Cisco CVP WebServicesManager service.

Click Start > All Programs > Administrative Tools > Services .

In the list of services names, select Cisco CVP WebServicesManager and click Stop .

Step 2

Import the saved Operations Console configuration.

Ensure that the administrator's password (at least 12 characters long) for the new OAMP server matches the password of the
                                                         source OAMP server.

On the Operations Console page, click System > Import System Configuration .

Click Browse and select the filename from the location where you saved the Operations Console configuration files of the previous version.

Click Import .

Copy the custom files and sip.properties files from the location where you saved the Operations Console configuration to their
                                                corresponding Unified CVP directories to complete the restore operation.

If you have not restored the backup containing the user-related information from the earlier version of Unified CVP, then
                                                               skip to Step 5.

Step 3

In the
                                          			 Operations Console page, click Device
                                                				  management > Reporting Server > Database
                                                				  Administration .

Step 4

Delete the
                                          			 Reporting Users that are created in the earlier version of Unified CVP.

Creating the
                                                         				  new users that are the same as the existing users does not work.

Step 5

Set the same
                                          			 password for the existing user that you imported from the earlier versions of
                                          			 CVP Operations Console.

Click Server Manager > Configuration > Local Users and Groups > Users .

Right-click the existing username and click Set Password .

On the Set Password screen, click Proceed .

Type the
                                                				  old password and confirm the new password.

Click OK .

Step 6

Restart Cisco Unified CVP Operations Console and Cisco CVP WebServicesManager .

Click Start > All Programs > Administrative Tools > Services .

Select Cisco CVP Operations Console Server.

Click Restart .

The CVP Operations Console Server service starts in the Services window.

Select Cisco CVP WebServicesManager .

Click Restart .

The Cisco CVP WebServicesManager starts in the Services window.

All the existing
                                 		  CVP Operations Console data including the CVP Operations Console login
                                 		  credentials get overwritten by the new data that is imported from the saved CVP
                                 		  Operations Console configuration.

### Secure
                           	 Communication with Operations Console

To secure
                                          			 communication between Operations Console and CVP components, on the Operations
                                          			 Console page, click Enable
                                             				Secured Communication with the Operations Console .

For configuring the security certificate exchange between Operations Console and CVP components, see the Configuration Guide for
                                                      				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

## Migrate Unified CVP Call Server

### Before you begin

Back up existing Unified CVP installation onto a different
                                    				computer for redundancy.

If you are migrating from Windows Server 2012 R2 Standard Edition to Windows Server 2016, assign the IP address and hostname
                                    of the previous Unified CVP to the later release.

Install the latest Unified CVP server component.

Step 1

Log in to Operations Console and select Device Management > Unified CVP Call Server .

Step 2

Select the Unified CVP Call server with the chosen IP address and
                                       			 the hostname.

Step 3

Click Edit .

Step 4

Click Save and Deploy to deploy the configuration to
                                       			 Unified CVP Call Server.

Step 5

Click System > SIP Server Groups .

On the SIP Server Groups screen, verify that the data is populated from the previous OAMP configuration importing step.

Step 6

Click Save and Deploy and confirm that the operation
                                       			 has completed successfully.

Step 7

Select System > Dialed Number Pattern .

In the Dialed Number Pattern screen, verify that the data is populated from the previous OAMP configuration importing step.

Step 8

Click Deploy .

Step 9

Select Device Management > Media Server .

Step 10

From the Default Media Server drop-down list, choose
                                       			 the appropriate media server.

Step 11

Click Set .

Step 12

Click Deploy .

Step 13

From the Media Server that is installed on the computer, select Internet Information
                                             				  Services > Sites .

- To add a new
                                          				group to the list, click Add and select Everyone .

- To give full
                                          				control to group Everyone , check the Full Control check box.

Step 14

From the FTP site, click Restart to restart the FTP server.

If you want to configure Unified CVP Call Server as Media Server and use the agent greeting recording, then you must enable
                                                      FTP on the Media Server. If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic
                                                      and start the service.

## Migrate Unified CVP VXML Server

### Before you begin

Ensure that the Unified CVP VXML Server and Unified Call Studio are of the same version so that Unified Call Studio can work
                                    with the Unified CVP VXML Server.

Ensure that you have licenses for all Unified CVP components.

If you do not apply licenses to the migrated components, the software runs in evaluation mode.

Back up any custom audio files from %CATALINA_HOME%/webapps/CVP/audio .

Back up
                                    				third-party libraries, such as .class or .jar files, at:

```
%CVP_HOME%\VXMLServer\common\classes
%CVP_HOME%\VXMLServer\common\lib
%CVP_HOME%\VXMLServer\applications\APP_NAME\java\application\classes
%CVP_HOME%\VXMLServer\applications\APP_NAME\java\application\lib
%CVP_HOME%\VXMLServer\applications\APP_NAME\java\util
```

where APP_NAME
                                    				is the name of deployed voice application.

Install Unified CVP Server. See Install Unified CVP Server .

Step 1

Log in to Operations Console and select Device Management > Unified CVP VXML Server .

Step 2

Select the
                                       			 Unified CVP VXML Server with the chosen IP address and the hostname.

Step 3

Click Edit and select the Unified CVP VXML Server configuration for editing.

Step 4

Click Save and Deploy to deploy the configuration to the new Unified CVP VXML Server.

Step 5

(Optional) If you need a secure connection between the Operations Console and Unified CVP VXML Server, configure SSL certificates.

Step 6

Restore the audio files to the %CATALINA_HOME%\webapps\CVP\audio folder .

Step 7

Restart Cisco CVP VXML Server and VXMLServer service.

### What to do next

To configure the Unified CVP VXML Server using Operations Console, see Configuration Guide for
                                       				  Cisco Unified Customer Voice Portal .

## Migrate Unified Call Studio

### Before you begin

Audio files are deployed to %CATALINA_HOME%\webapps\CVP\audio are deleted. %CATALINA_HOME% implies the Tomcat installation directory.

Launch the Call Studio application.

If you do not apply licenses to migrated components, then the software runs in the evaluation mode.

Export Unified Call Studio projects to offline media, if they are not stored in version-control systems. You can export multiple
                                                   projects simultaneously by unchecking them from the list that Export wizard displays.

Step 1

Select the Existing Cisco Unified CVP Project into Workspace option to import the projects.

The import process upgrades the projects to the format of the new release, if necessary.

If you check out applications from a source repository rather than importing from the file system, you can still import the
                                                      applications to Call Studio project to start the conversion process. In addition, for the first check-in after importing,
                                                      all files in each project are considered modified and you need to update them in the repository.

Step 2

Recompile any custom components that were compiled in the earlier versions of Java.

Review the list of Java changes that may affect backward compatibility and make any required updates. You can locate the compatibility
                                          page at http://www.oracle.com/technetwork/java/javase/downloads/index.html .

Step 3

Deploy all projects, including the newly recompiled components from the previous step, to the appropriate Cisco Unified CVP
                                       VXML Servers.

Use Operations Console for bulk transfer of the project to multiple Unified CVP VXML Servers in one step.

## Migrate Unified CVP Reporting Server

### Before you begin

Retain the call data during migration by unloading the existing
                              		  databases of Unified CVP.

Step 1

Unload data from Reporting Server Database.

Step 2

Uninstall Reporting Server.

Step 3

Upgrade Microsoft Windows Server.

Step 4

Install Reporting Server.

Step 5

Load data to Reporting Server Database.

Step 6

Configure Unified CVP Reporting Server in Operations Console.

### Prepare Unified CVP Reporting Server

Step 1

Install Unified CVP Reporting Server on Windows Server.

Ensure that the Unified CVP Reporting database is active.

Start the Informix IDS - CVP service in Windows Service Manager.

Step 2

From the
                                          			 command prompt, run dbaccess , and then select a database.

Step 3

Select the
                                          			 following databases and press Return .

callback

ciscoadmin

cvp_data

### Unload Data from Reporting Server Database

Step 1

Log in as cvp_dbadmin user to Unified CVP.

Step 2

Stop Cisco CVP Call Server service from Windows Service Manager.

Ensure that enough disk space is available to unload data. To check the disk space (in MB), run the query:

select sum(tabsize(tabname)) from systables where tabid>99

-OR- go to OAMP > Unified CVP Reporting Server > Database Administration > Database details.

Step 3

Access the Unified CVP installation file.

Step 4

From the command prompt, change the directory to the migration folder.

You can also copy the migration folder to the local disk and run the unload script directly.

Step 5

Locate the migrate_unload.bat file.

Step 6

By default, the data is exported to c:\migration . Ensure that this path exists. If you want to change the default path, then update the path in unl.sql :

create procedure unld(path char(128) default " c:\migration\ ") RETURNING char(128)

Step 7

Run the following command to unload the Reporting Server database:

After running the script, a set of .unl files is created under the path provided. The .unl files are exported to c:\migration . This folder must have full access permission for cvp_dbadmin user.

Step 8

Copy the exported migration folder to the Unified CVP database Reporting Server.

Reduce the retention period for data and execute a purge to reduce the data to migrate.

Step 9

Start Cisco CVP Call Server service from Windows Service Manager.

### Load Data to Reporting Server Database

#### Before you begin

Stop all Purge Procedures from the Task Scheduler before loading the database. If this is not followed, there is a risk of
                                 loosing important data rows.

Step 1

Open the Unified CVP installation file.

Step 2

Stop Cisco CVP Call Server service from Windows Service Manager.

Step 3

Go to CVP > Migration .

Step 4

Copy the migration folder to the local disk and run the load script directly. From the command prompt, change the directory
                                          to the migration folder.

Step 5

On the local disk, locate the .unl files that you want to load into the Unified CVP database and copy them into the migration
                                          folder.

Step 6

Run the following command as an administrator to load the Unified CVP database: migrate_load.bat

If the .unl files are located in c:\migration , you must run the script load as migrate_load.bat .

This script loads all the three Unified CVP Reporting databases with the previous call data to the Unified CVP Reporting database.

The load runs at a rate of about 1GB/10 minutes approximately.

Step 7

Start Cisco CVP Call Server service from Windows Service Manager.

### Configure
                           	 Reporting Server in Operations Console

Step 1

Import the Operations Console configuration and redeploy the Unified CVP Reporting Server to retain the same IP address as
                                          that of Unified CVP.

Step 2

If the IP address of the server is changed, then delete the previous instance of the server and add the new Unified CVP Reporting
                                          Server to Operations Console, and then deploy the server.

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

## Unified CVP Redeployment

### Redeploy Operations Console

See Migrate Operations Console .

### Redeploy Unified CVP Server

See Migrate Unified CVP Call Server and Migrate Unified CVP VXML Server .

### Redeploy Unified CVP Reporting Server

Step 1

Reinstall the Unified CVP Reporting Server.

Step 2

Save and deploy the Unified CVP Reporting Server in Operations Console.

Step 3

Restart the Unified CVP Reporting Server.

Step 4

Redeploy courtesy callback system-level configuration, if applicable.

Step 5

Redeploy SNMP configuration, if applicable.

### Redeploy Unified Call Studio

See the Migrate Unified Call Studio section.

| Note | If you have enabled secure communication, see the Unified CVP Security chapter in Configuration Guide for Cisco Unified Customer Voice Portal for instructions on uploading certificate for the secure communication. |
|---|---|

| Important | You cannot roll back to an earlier version of Unified CVP after you initiate migration. Back up the installation files and
                                             data before you begin the migration process. |
|---|---|

| Note | SIP Proxy servers and DNS servers cannot co-reside with other Unified CVP product components. |
|---|---|

| Note | If you are
                                             				using an older gateway or gatekeeper hardware, the version of Cisco IOS that is
                                             				required in this release may no longer support the required hardware. Hence,
                                             				you need to purchase new hardware. |
|---|---|

| Step 1 | Log in to
                                          			 Operations Console. |
|---|---|
| Step 2 | On the
                                          			 Operations Console page, click System > Export System
                                                				  Configuration > Export . |
| Step 3 | Manually copy
                                          			 the sip.properties file. CVP
                                          			 Operations Console cannot export the sip.properties file. For more information on Unified CVP Console Configuration, see Administration Guide for
                                                      				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html . |
| Step 4 | Save the CVP-OpsConsole-Backup.zip file. Note This file is password protected and can be opened only by the target OAMP server if the administrator password (at least 12
                                                         characters long) matches that of the server from where it is exported. | Note | This file is password protected and can be opened only by the target OAMP server if the administrator password (at least 12
                                                         characters long) matches that of the server from where it is exported. |
| Note | This file is password protected and can be opened only by the target OAMP server if the administrator password (at least 12
                                                         characters long) matches that of the server from where it is exported. |

| Note | This file is password protected and can be opened only by the target OAMP server if the administrator password (at least 12
                                                         characters long) matches that of the server from where it is exported. |
|---|---|

| Step 1 | Stop Cisco CVP WebServicesManager service. Click Start > All Programs > Administrative Tools > Services . In the list of services names, select Cisco CVP WebServicesManager and click Stop . |
|---|---|
| Step 2 | Import the saved Operations Console configuration. Note Ensure that the administrator's password (at least 12 characters long) for the new OAMP server matches the password of the
                                                         source OAMP server. On the Operations Console page, click System > Import System Configuration . Click Browse and select the filename from the location where you saved the Operations Console configuration files of the previous version. Click Import . Copy the custom files and sip.properties files from the location where you saved the Operations Console configuration to their
                                                corresponding Unified CVP directories to complete the restore operation. Note If you have not restored the backup containing the user-related information from the earlier version of Unified CVP, then
                                                               skip to Step 5. | Note | Ensure that the administrator's password (at least 12 characters long) for the new OAMP server matches the password of the
                                                         source OAMP server. | Note | If you have not restored the backup containing the user-related information from the earlier version of Unified CVP, then
                                                               skip to Step 5. |
| Note | Ensure that the administrator's password (at least 12 characters long) for the new OAMP server matches the password of the
                                                         source OAMP server. |
| Note | If you have not restored the backup containing the user-related information from the earlier version of Unified CVP, then
                                                               skip to Step 5. |
| Step 3 | In the
                                          			 Operations Console page, click Device
                                                				  management > Reporting Server > Database
                                                				  Administration . |
| Step 4 | Delete the
                                          			 Reporting Users that are created in the earlier version of Unified CVP. Note Creating the
                                                         				  new users that are the same as the existing users does not work. | Note | Creating the
                                                         				  new users that are the same as the existing users does not work. |
| Note | Creating the
                                                         				  new users that are the same as the existing users does not work. |
| Step 5 | Set the same
                                          			 password for the existing user that you imported from the earlier versions of
                                          			 CVP Operations Console. Click Server Manager > Configuration > Local Users and Groups > Users . Right-click the existing username and click Set Password . On the Set Password screen, click Proceed . Type the
                                                				  old password and confirm the new password. Click OK . |
| Step 6 | Restart Cisco Unified CVP Operations Console and Cisco CVP WebServicesManager . Click Start > All Programs > Administrative Tools > Services . Select Cisco CVP Operations Console Server. Click Restart . The CVP Operations Console Server service starts in the Services window. Select Cisco CVP WebServicesManager . Click Restart . The Cisco CVP WebServicesManager starts in the Services window. |

| Note | Ensure that the administrator's password (at least 12 characters long) for the new OAMP server matches the password of the
                                                         source OAMP server. |
|---|---|

| Note | If you have not restored the backup containing the user-related information from the earlier version of Unified CVP, then
                                                               skip to Step 5. |
|---|---|

| Note | Creating the
                                                         				  new users that are the same as the existing users does not work. |
|---|---|

| To secure
                                          			 communication between Operations Console and CVP components, on the Operations
                                          			 Console page, click Enable
                                             				Secured Communication with the Operations Console . For configuring the security certificate exchange between Operations Console and CVP components, see the Configuration Guide for
                                                      				  Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html . |
|---|

| Step 1 | Log in to Operations Console and select Device Management > Unified CVP Call Server . |
|---|---|
| Step 2 | Select the Unified CVP Call server with the chosen IP address and
                                       			 the hostname. |
| Step 3 | Click Edit . |
| Step 4 | Click Save and Deploy to deploy the configuration to
                                       			 Unified CVP Call Server. |
| Step 5 | Click System > SIP Server Groups . On the SIP Server Groups screen, verify that the data is populated from the previous OAMP configuration importing step. |
| Step 6 | Click Save and Deploy and confirm that the operation
                                       			 has completed successfully. |
| Step 7 | Select System > Dialed Number Pattern . In the Dialed Number Pattern screen, verify that the data is populated from the previous OAMP configuration importing step. |
| Step 8 | Click Deploy . |
| Step 9 | Select Device Management > Media Server . |
| Step 10 | From the Default Media Server drop-down list, choose
                                       			 the appropriate media server. |
| Step 11 | Click Set . |
| Step 12 | Click Deploy . |
| Step 13 | From the Media Server that is installed on the computer, select Internet Information
                                             				  Services > Sites . To add a new
                                          				group to the list, click Add and select Everyone . To give full
                                          				control to group Everyone , check the Full Control check box. |
| Step 14 | From the FTP site, click Restart to restart the FTP server. Note If you want to configure Unified CVP Call Server as Media Server and use the agent greeting recording, then you must enable
                                                      FTP on the Media Server. If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic
                                                      and start the service. | Note | If you want to configure Unified CVP Call Server as Media Server and use the agent greeting recording, then you must enable
                                                      FTP on the Media Server. If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic
                                                      and start the service. |
| Note | If you want to configure Unified CVP Call Server as Media Server and use the agent greeting recording, then you must enable
                                                      FTP on the Media Server. If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic
                                                      and start the service. |

| Note | If you want to configure Unified CVP Call Server as Media Server and use the agent greeting recording, then you must enable
                                                      FTP on the Media Server. If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic
                                                      and start the service. |
|---|---|

| Note | If you do not apply licenses to the migrated components, the software runs in evaluation mode. |
|---|---|

| Step 1 | Log in to Operations Console and select Device Management > Unified CVP VXML Server . |
|---|---|
| Step 2 | Select the
                                       			 Unified CVP VXML Server with the chosen IP address and the hostname. |
| Step 3 | Click Edit and select the Unified CVP VXML Server configuration for editing. |
| Step 4 | Click Save and Deploy to deploy the configuration to the new Unified CVP VXML Server. |
| Step 5 | (Optional) If you need a secure connection between the Operations Console and Unified CVP VXML Server, configure SSL certificates. |
| Step 6 | Restore the audio files to the %CATALINA_HOME%\webapps\CVP\audio folder . |
| Step 7 | Restart Cisco CVP VXML Server and VXMLServer service. |

| Note | Audio files are deployed to %CATALINA_HOME%\webapps\CVP\audio are deleted. %CATALINA_HOME% implies the Tomcat installation directory. |
|---|---|

| Note | If you do not apply licenses to migrated components, then the software runs in the evaluation mode. |
|---|---|

| Note | Export Unified Call Studio projects to offline media, if they are not stored in version-control systems. You can export multiple
                                                   projects simultaneously by unchecking them from the list that Export wizard displays. |
|---|---|

| Step 1 | Select the Existing Cisco Unified CVP Project into Workspace option to import the projects. The import process upgrades the projects to the format of the new release, if necessary. Note If you check out applications from a source repository rather than importing from the file system, you can still import the
                                                      applications to Call Studio project to start the conversion process. In addition, for the first check-in after importing,
                                                      all files in each project are considered modified and you need to update them in the repository. | Note | If you check out applications from a source repository rather than importing from the file system, you can still import the
                                                      applications to Call Studio project to start the conversion process. In addition, for the first check-in after importing,
                                                      all files in each project are considered modified and you need to update them in the repository. |
|---|---|---|---|
| Note | If you check out applications from a source repository rather than importing from the file system, you can still import the
                                                      applications to Call Studio project to start the conversion process. In addition, for the first check-in after importing,
                                                      all files in each project are considered modified and you need to update them in the repository. |
| Step 2 | Recompile any custom components that were compiled in the earlier versions of Java. Review the list of Java changes that may affect backward compatibility and make any required updates. You can locate the compatibility
                                          page at http://www.oracle.com/technetwork/java/javase/downloads/index.html . |
| Step 3 | Deploy all projects, including the newly recompiled components from the previous step, to the appropriate Cisco Unified CVP
                                       VXML Servers. Use Operations Console for bulk transfer of the project to multiple Unified CVP VXML Servers in one step. |

| Note | If you check out applications from a source repository rather than importing from the file system, you can still import the
                                                      applications to Call Studio project to start the conversion process. In addition, for the first check-in after importing,
                                                      all files in each project are considered modified and you need to update them in the repository. |
|---|---|

| Step 1 | Unload data from Reporting Server Database. |
|---|---|
| Step 2 | Uninstall Reporting Server. |
| Step 3 | Upgrade Microsoft Windows Server. |
| Step 4 | Install Reporting Server. |
| Step 5 | Load data to Reporting Server Database. |
| Step 6 | Configure Unified CVP Reporting Server in Operations Console. |

| Step 1 | Install Unified CVP Reporting Server on Windows Server. Note Ensure that the Unified CVP Reporting database is active. Start the Informix IDS - CVP service in Windows Service Manager. | Note | Ensure that the Unified CVP Reporting database is active. Start the Informix IDS - CVP service in Windows Service Manager. |
|---|---|---|---|
| Note | Ensure that the Unified CVP Reporting database is active. Start the Informix IDS - CVP service in Windows Service Manager. |
| Step 2 | From the
                                          			 command prompt, run dbaccess , and then select a database. |
| Step 3 | Select the
                                          			 following databases and press Return . callback ciscoadmin cvp_data |

| Note | Ensure that the Unified CVP Reporting database is active. Start the Informix IDS - CVP service in Windows Service Manager. |
|---|---|

| Step 1 | Log in as cvp_dbadmin user to Unified CVP. |
|---|---|
| Step 2 | Stop Cisco CVP Call Server service from Windows Service Manager. Note Ensure that enough disk space is available to unload data. To check the disk space (in MB), run the query: select sum(tabsize(tabname)) from systables where tabid>99 -OR- go to OAMP > Unified CVP Reporting Server > Database Administration > Database details. | Note | Ensure that enough disk space is available to unload data. To check the disk space (in MB), run the query: select sum(tabsize(tabname)) from systables where tabid>99 -OR- go to OAMP > Unified CVP Reporting Server > Database Administration > Database details. |
| Note | Ensure that enough disk space is available to unload data. To check the disk space (in MB), run the query: select sum(tabsize(tabname)) from systables where tabid>99 -OR- go to OAMP > Unified CVP Reporting Server > Database Administration > Database details. |
| Step 3 | Access the Unified CVP installation file. |
| Step 4 | From the command prompt, change the directory to the migration folder. Note You can also copy the migration folder to the local disk and run the unload script directly. | Note | You can also copy the migration folder to the local disk and run the unload script directly. |
| Note | You can also copy the migration folder to the local disk and run the unload script directly. |
| Step 5 | Locate the migrate_unload.bat file. |
| Step 6 | By default, the data is exported to c:\migration . Ensure that this path exists. If you want to change the default path, then update the path in unl.sql : create procedure unld(path char(128) default " c:\migration\ ") RETURNING char(128) |
| Step 7 | Run the following command to unload the Reporting Server database: migrate_unload.bat After running the script, a set of .unl files is created under the path provided. The .unl files are exported to c:\migration . This folder must have full access permission for cvp_dbadmin user. |
| Step 8 | Copy the exported migration folder to the Unified CVP database Reporting Server. Note Reduce the retention period for data and execute a purge to reduce the data to migrate. | Note | Reduce the retention period for data and execute a purge to reduce the data to migrate. |
| Note | Reduce the retention period for data and execute a purge to reduce the data to migrate. |
| Step 9 | Start Cisco CVP Call Server service from Windows Service Manager. |

| Note | Ensure that enough disk space is available to unload data. To check the disk space (in MB), run the query: select sum(tabsize(tabname)) from systables where tabid>99 -OR- go to OAMP > Unified CVP Reporting Server > Database Administration > Database details. |
|---|---|

| Note | You can also copy the migration folder to the local disk and run the unload script directly. |
|---|---|

| Note | Reduce the retention period for data and execute a purge to reduce the data to migrate. |
|---|---|

| Step 1 | Open the Unified CVP installation file. |
|---|---|
| Step 2 | Stop Cisco CVP Call Server service from Windows Service Manager. |
| Step 3 | Go to CVP > Migration . |
| Step 4 | Copy the migration folder to the local disk and run the load script directly. From the command prompt, change the directory
                                          to the migration folder. |
| Step 5 | On the local disk, locate the .unl files that you want to load into the Unified CVP database and copy them into the migration
                                          folder. |
| Step 6 | Run the following command as an administrator to load the Unified CVP database: migrate_load.bat Note If the .unl files are located in c:\migration , you must run the script load as migrate_load.bat . This script loads all the three Unified CVP Reporting databases with the previous call data to the Unified CVP Reporting database. Note The load runs at a rate of about 1GB/10 minutes approximately. | Note | If the .unl files are located in c:\migration , you must run the script load as migrate_load.bat . | Note | The load runs at a rate of about 1GB/10 minutes approximately. |
| Note | If the .unl files are located in c:\migration , you must run the script load as migrate_load.bat . |
| Note | The load runs at a rate of about 1GB/10 minutes approximately. |
| Step 7 | Start Cisco CVP Call Server service from Windows Service Manager. |

| Note | If the .unl files are located in c:\migration , you must run the script load as migrate_load.bat . |
|---|---|

| Note | The load runs at a rate of about 1GB/10 minutes approximately. |
|---|---|

| Step 1 | Import the Operations Console configuration and redeploy the Unified CVP Reporting Server to retain the same IP address as
                                          that of Unified CVP. |
|---|---|
| Step 2 | If the IP address of the server is changed, then delete the previous instance of the server and add the new Unified CVP Reporting
                                          Server to Operations Console, and then deploy the server. |

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

| See Migrate Operations Console . |
|---|

| See Migrate Unified CVP Call Server and Migrate Unified CVP VXML Server . |
|---|

| Step 1 | Reinstall the Unified CVP Reporting Server. |
|---|---|
| Step 2 | Save and deploy the Unified CVP Reporting Server in Operations Console. |
| Step 3 | Restart the Unified CVP Reporting Server. |
| Step 4 | Redeploy courtesy callback system-level configuration, if applicable. |
| Step 5 | Redeploy SNMP configuration, if applicable. |