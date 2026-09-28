---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-3-op-system-administration-guide-ups1030s-iptpch7-html-09b3855011
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_3/op_system/administration/guide/ups1030s/iptpch7.html
retrieved_at: 2026-08-21T02:48:32.235565+00:00
---

Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

# Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

Updated: February 21, 2007

Chapter: Software Upgrades

## Chapter: Software Upgrades

## Software Upgrades

You can use the Software Upgrades options to perform the following types of installations and upgrades:

• Install/Upgrade—Use this option to upgrade the application software, install Cisco Unified CallManager Locale Installers and dial plans, and upload and install device packs, phone firmware loads, and other COP files.

• Upload TFTP Server Files—Use this option to upload various device files for use by the phones to the TFTP server. The TFTP server files that you can upload include custom phone rings, callback tones, and phone backgrounds.

## Software Upgrade and Installation

The Software Upgrade windows enable you to upgrade the Cisco Unified Communications Operating System software from either a local or a remote source.

The software upgrade process also enables you to back out of an upgrade if problems occur. You install the software for the upgrade on the system inactive partition and perform a restart to switch the system to the newer version of the software. During this process, the upgraded software becomes the active partition, and your current software becomes the inactive partition. Your configuration information migrates automatically to the upgraded version in the active partition.

If for any reason you decide to back out of the upgrade, you can restart the system to the inactive partition that contains the older version of the software. However, any configuration changes that you made since upgrading the software will be lost.

Starting with Cisco Unified CallManager version 5.0(4), CAPF uses the Certificate Manager Infrastructure to manage its certificates and keys. Because of this, when you upgrade to version 5.0(4), CAPF keys and certificates automatically regenerate. You must then rerun the CTL Client application to upgrade the CTL file. For information on using CAPF with Cisco Unified CallManager, refer to the Cisco Unified CallManager Security Guide .

### From Local Source

You can install software from a CD or DVD that is located in the local disc drive and then start the upgrade process.

Note Be sure to back up your system data before starting the software upgrade process. For more information, see the Disaster Recovery System Administration Guide .

To install or upgrade software from a CD or DVD, follow this procedure:

Step 1 If you plan to download the upgrade file, create a CD or DVD by doing the following steps:

Note If you download an upgrade file from Cisco.com using Internet Explorer and have WinZip (or a similar zip utility) installed on your PC, the file extension gets changed from .gz.sgn to .gz.gz. To successfully install the upgrade, you must rename the file and change the extension back to .gz.sgn.

a. Download the appropriate upgrade file from Cisco.com.

Note Do not unzip or untar the file, or the system may not be able to read the upgrade files.

b. Copy the upgrade file to a writeble CD or DVD.

Step 2 Insert the CD or DVD into the disc drive on the local server that is to be upgraded.

Note Because of their size, some upgrade files may not fit on a CD and will require a DVD.

Step 3 Choose Software Upgrades > Install/Upgrade .

Step 4 For the software location source, choose DVD/CD .

Step 5 If you burned the patch file to a subdirectory on the CD or DVD, enter the path in the Directory field.

Step 6 To continue the upgrade process, click Next .

Step 7 Choose the upgrade version that you want to install and click Next .

Step 8 In the next window, monitor the progress of the download, which includes the filename and the number of megabytes that are getting transferred.

When the download completes, the Checksum window displays.

Step 9 Verify the checksum value against the checksum for the file that you downloaded that is shown on Cisco.com.

Step 10 After determining that the cheksums match, click Next to proceed with the software upgrade.

A Warning window displays the current and upgrade software versions.

Step 11 To continue with the software upgrade, click Next .

The Post Installation Options window displays.

Step 12 Choose whether you want the system to automatically reboot to the upgraded partition after installing the upgrade software:

– To install the upgrade and automatically reboot to the upgraded partition, choose Reboot to upgraded partition .

– To install the upgrade and then manually reboot to the upgraded partition at a later time, choose Do not reboot after upgrade .

Step 13 Click Upgrade .

The Upgrade Status windows displays and displays the Upgrade log.

Step 14 When the installation completes, click Finish .

Step 15 To restart the system and activate the upgrade, choose Restart > Switch Versions .

The Switch Software Version window displays.

Step 16 To switch software versions and restart the system, click Switch Versions .

The system restarts running the upgraded software.

### From Remote Source

To install software from a network drive or remote server, use the following procedure.

Note Be sure to back up your system data before starting the software upgrade process. For more information, see the Disaster Recovery System Administration Guide .

Step 1 Navigate to Software Upgrades > Install .

Step 2 For the Software Location Source, choose Remote File System .

Step 3 Enter the directory name for the software upgrade, if required.

If the upgrade file is located on a Linux or Unix server, you must enter a forward slash at the beginning of the directory path you want to specify. For example, if the upgrade file is in the patches directory, you must enter /patches . If the upgrade file is located on a Windows server, check with your system administrator for the correct directory path.

Step 4 Enter the required upgrade information as described in the following table:

Remote Server

Host name or IP address of the remote server from which software will be downloaded.

Remote User

Name of a user who is configured on the remote server.

Remote Password

Password that is configured for this user on the remote server.

Download Protocol

Choose sftp or ftp.

Note You must choose Remote File System to enable the remote server configuration fields.

Step 5 Click Next .

The system checks for available upgrades.

Step 6 Choose the upgrade or option that you want to install and click Next .

Step 7 In the next window, monitor the progress of the download, which includes the filename and the number of megabytes that are getting transferred.

When the download completes, the Checksum window displays.

Step 8 Verify the checksum value against the checksum for the file that you downloaded that was shown on Cisco.com.

Step 9 After determining that the cheksums match, click Next to proceed with the software upgrade.

A Warning window displays the current and upgrade software versions.

Step 10 To continue with the software upgrade, click Next .

The Post Installation Options window displays.

Step 11 Choose whether you want the system to automatically reboot to the upgraded partition after installing the upgrade software:

– To install the upgrade and automatically reboot to the upgraded partition, choose Reboot to upgraded partition .

– To install the upgrade and then manually reboot to the upgraded partition at a later time, choose Do not reboot after upgrade .

Step 12 Click Upgrade .

The Upgrade Status window, which shows the Upgrade log, displays.

Step 13 When the installation completes, click Finish .

Step 14 To restart the system and activate the upgrade, choose Restart > Switch Versions .

The system restarts running the upgraded software.

Note After upgrading from Cisco Unified Presence Server Release 1.0(2) to Release 1.0(3), ensure that LDAP search works in Cisco Unified Personal Communicator. If LDAP search does not work, delete the Cisco Unified Personal Communicator LDAP Profile in Cisco Unified Presence Server Administration and then recreate it. For more information, see the LDAP Profile chapter in the Cisco Unified Presence Server Administration Guide .

## Locale Installation

Cisco provides locale-specific versions of the Cisco Unified CallManager Locale Installer on www.cisco.com. Installed by the system administrator, the locale installer allows the user to view/receive the chosen translated text or tones, if applicable, when a user works with supported interfaces.

User Locales

User locale files provide translated text and voice prompts, if available, for phone displays, user applications, and user web pages in the locale that the user chooses. User-only locale installers exist on the web.

Network Locales

Network locale files provide country-specific phone tones and gateway tones, if available. Network-only locale installers exist on the web.

Cisco may combine multiple network locales in a single locale installer.

Note The Cisco Media Convergence Server (MCS) or Cisco-approved, customer-provided server can support multiple locales. Installing multiple locale installers ensures that the user can choose from a multitude of locales. Changes do not take effect until you reboot every server in the cluster. Cisco strongly recommends that you do not reboot the servers until you have installed all locales on all servers in the cluster. Minimize call-processing interruptions by rebooting the servers after regular business hours.

### Installing Locales

You can install locale files from either a local or a remote source by using the same process that is described earlier in this chapter for installing software upgrades. See Software Upgrade and Installation for more information about this process.

Note To activate the newly installed locales, you must restart the server.

See Locale Files for information on the locale files that you must install. You can install more than one locale before you restart the server.

### Locale Files

When installing locales, you must install both the following files:

• User Locale files—Contain language information for a specific language and country and use the following convention:

cm-locale- language - country - version .cop

• Combined Network Locale file—Contains country-specific files for all countries for various network items, including phone tones, annunciators, and gateway tones. The combined network locale file uses the following naming convention:

cm-locale-combinednetworklocale- version .cop

### Error Messages

See Table 7-1 for a description of the error messages that can occur during Locale Installer activation. If an error occurs, you can view the error messages in the installation log.

Table 7-1 Locale Installer Error Messages and Descriptions

[LOCALE] File not found: <language>_<country>_user_locale.csv, the user locale has not been added to the database.

This error occurs when the system cannot locate the CSV file, which contains user locale information to add to the database. This indicates an error with the build process.

[LOCALE] File not found: <country>_network_locale.csv, the network locale has not been added to the database.

This error occurs when the system cannot locate the CSV file, which contains network locale information to add to the database This indicates an error with the build process.

[LOCALE] CallManager CSV file installer installdb is not present or not executable

A Cisco Unified CallManager application called installdb must be present; it reads information that is contained in a CSV file and applies it correctly to the Cisco Unified CallManager database. If this application is not found, it either was not installed with Cisco Unified CallManager (very unlikely), has been deleted (more likely), or the server does not have Cisco Unified CallManager installed (most likely). Installation of the locale will terminate because locales will not work without the correct records that are held in the database.

[LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/com/cisco/ipma/client/locales/maDialogs_<ll>_<CC>.properties.Checksum.

[LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/com/cisco/ipma/client/locales/maMessages_<ll>_<CC>.properties.Checksum.

[LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/com/cisco/ipma/client/locales/maGlobalUI_<ll>_<CC>.properties.Checksum.

[LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/LocaleMasterVersion.txt.Checksum.

These errors could occur when the system fails to create a checksum file, caused by an absent Java executable, /usr/local/thirdparty/java/j2sdk/jre/bin/java, an absent or damaged Java archive file, /usr/local/cm/jar/cmutil.jar, or absent or damaged Java class, com.cisco.ccm.util.Zipper. Even if these errors occur, the locale will continue to work correctly, with the exception of Cisco Unified CallManager Assistant, which cannot detect a change in localized Cisco Unified CallManager Assistant files.

[LOCALE] Could not find /usr/local/cm/application_locale/cmservices/ipma/LocaleMasterVersion.txt in order to update Unified CM Assistant locale information.

This error occurs when the file has not been found in the correct location, which is most likely due to an error in the build process.

[LOCALE] Addition of <RPM-file-name> to the Cisco Unified CallManager database has failed!

This error occurs because of the collective result of any failure that occurs when a locale is being installed; it indicates a terminal condition.

## Uploading TFTP Server Files

You can use the Upload TFTP Server File option to upload various files for use by the phones to the server. Files that you can upload include custom phone rings, callback tones, and backgrounds. This option uploads files only to the specific server to which you connected, and other nodes in the cluster do not get upgraded.

Files upload into the tftp directory by default. You can also upload files to a subdirectory of the tftp directory.

If you have two Cisco TFTP servers that are configured in the cluster, you must perform the following procedure on both servers. This process does not distribute files to all servers, nor to both of the Cisco TFTP servers in a cluster.

To upload TFTP server files, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Software Upgrades>Upload TFTP Server File .

The Upload TFTP Server File window displays and shows a listing of the current uploaded files.

Step 2 To upload a file, click Browse and then choose the file that you want to upload.

Step 3 To upload the file to a subdirectory of the tftp directory, enter the subdirectory in the Subdirectory of the tftp directory where file will be uploaded field.

Step 4 To start the upload, click Upload File .

The Status area indicates when the file uploads successfully.

Step 5 After the file uploads, restart the Cisco TFTP service.

Note If you plan to upload several files, restart the Cisco TFTP service only once, after you have uploaded all of the files.

For information about restarting services, refer to Cisco Unified CallManager Serviceability Administration Guide .

Note If you want to modify a file that is already in the TFTP directory, you can use the CLI command file list tftp to see the files in the TFTP directory and file get tftp to get a copy of a file in the TFTP directory. For more information, see Appendix A, "Command Line Interface."

| Field | Description |
|---|---|
| Remote Server | Host name or IP address of the remote server from which software will be downloaded. |
| Remote User | Name of a user who is configured on the remote server. |
| Remote Password | Password that is configured for this user on the remote server. |
| Download Protocol | Choose sftp or ftp. |

| Message | Description |
|---|---|
| [LOCALE] File not found: <language>_<country>_user_locale.csv, the user locale has not been added to the database. | This error occurs when the system cannot locate the CSV file, which contains user locale information to add to the database. This indicates an error with the build process. |
| [LOCALE] File not found: <country>_network_locale.csv, the network locale has not been added to the database. | This error occurs when the system cannot locate the CSV file, which contains network locale information to add to the database This indicates an error with the build process. |
| [LOCALE] CallManager CSV file installer installdb is not present or not executable | A Cisco Unified CallManager application called installdb must be present; it reads information that is contained in a CSV file and applies it correctly to the Cisco Unified CallManager database. If this application is not found, it either was not installed with Cisco Unified CallManager (very unlikely), has been deleted (more likely), or the server does not have Cisco Unified CallManager installed (most likely). Installation of the locale will terminate because locales will not work without the correct records that are held in the database. |
| [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/com/cisco/ipma/client/locales/maDialogs_<ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/com/cisco/ipma/client/locales/maMessages_<ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/com/cisco/ipma/client/locales/maGlobalUI_<ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/LocaleMasterVersion.txt.Checksum. | These errors could occur when the system fails to create a checksum file, caused by an absent Java executable, /usr/local/thirdparty/java/j2sdk/jre/bin/java, an absent or damaged Java archive file, /usr/local/cm/jar/cmutil.jar, or absent or damaged Java class, com.cisco.ccm.util.Zipper. Even if these errors occur, the locale will continue to work correctly, with the exception of Cisco Unified CallManager Assistant, which cannot detect a change in localized Cisco Unified CallManager Assistant files. |
| [LOCALE] Could not find /usr/local/cm/application_locale/cmservices/ipma/LocaleMasterVersion.txt in order to update Unified CM Assistant locale information. | This error occurs when the file has not been found in the correct location, which is most likely due to an error in the build process. |
| [LOCALE] Addition of <RPM-file-name> to the Cisco Unified CallManager database has failed! | This error occurs because of the collective result of any failure that occurs when a locale is being installed; it indicates a terminal condition. |