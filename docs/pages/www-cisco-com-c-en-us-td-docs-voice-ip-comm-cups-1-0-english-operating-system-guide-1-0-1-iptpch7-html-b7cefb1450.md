---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-operating-system-guide-1-0-1-iptpch7-html-b7cefb1450
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/operating_system/guide/1_0_1/iptpch7.html
retrieved_at: 2026-08-21T02:47:19.739761+00:00
---

Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

# Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Software Upgrades

## Chapter: Software Upgrades

## Software Upgrades

You can use the Software Upgrades options to perform the following types of installations and upgrades:

• Install/Upgrade—Use this option to upgrade the application software.

• Upload TFTP Server Files—Use this option to upload various device files for use by the phones to the TFTP server. The TFTP server files that you can upload include custom phone rings, callback tones, and phone backgrounds.

## Software Upgrade and Installation

The Software Upgrade windows enable you to upgrade the Cisco Unified Communications Operating System software from either a local or a remote source.

The software upgrade process also enables you to back out of an upgrade if problems occur. You install the software for the upgrade on the system inactive partition and perform a restart to switch the system to the newer version of the software. During this process, the upgraded software becomes the active partition, and your current software becomes the inactive partition. Your configuration information migrates automatically to the upgraded version in the active partition.

If for any reason you decide to back out of the upgrade, you can restart the system to the inactive partition that contains the older version of the software. However, any configuration changes that you made since upgrading the software will be lost.

Starting with Cisco Unified CallManager version 5.0(4), CAPF uses the Certificate Manager Infrastructure to manage its certificates and keys. Because of this, when you upgrade to version 5.0(4), CAPF keys and certificates are automatically regenerated. You must then rerunning the CTL Client application to upgrade the CTL file. For information on using CAPF with Cisco Unified CallManager 5.0(4), refer to the Cisco Unified CallManager Security Guide .

### From Local Source

You can install software from a CD or DVD that is located in the local disc drive and then start the upgrade process.

Note Be sure to back up your system data before starting the software upgrade process. For more information, see the Disaster Recovery System Administration Guide .

To install or upgrade software from a CD or DVD, follow this procedure:

Step 1 Download the appropriate upgrade file from Cisco.com.

Note Do not unzip or untar the file. If you do, the system may not be able to read the upgrade files.

Step 2 Copy the upgrade file to a writeble CD or DVD.

Step 3 Insert the new CD or DVD into the disc drive on the local server that is to be upgraded.

Note Because of their size, some upgrade files may not fit on a CD and will require a DVD.

Step 4 Choose Software Upgrades>Install/Upgrade .

Step 5 For the software location source, choose DVD/CD .

Step 6 If you burned the patch file to a subdirectory on the CD or DVD, enter the path in the Directory field.

Step 7 To continue the upgrade process, click Next .

Step 8 Choose the upgrade version that you want to install and click Next .

Step 9 In the next window, monitor the progress of the download, which includes the filename and the number of megabytes that are getting transferred.

When the download completes, the Checksum window displays.

Step 10 Verify the checksum value against the checksum for the file you that downloaded that is shown on Cisco.com.

Step 11 After determining that the cheksums match, click Next to proceed with the software upgrade.

A Warning window displays the current and upgrade software versions.

Step 12 To continue with the software upgrade, click Next .

The Post Installation Options window displays.

Step 13 Choose whether you want the system to automatically reboot to the upgraded partition after installing the upgrade software:

– To install the upgrade and automatically reboot to the upgraded partition, choose Reboot to upgraded partition .

– To install the upgrade and then manually reboot to the upgraded partition at a later time, choose Do not reboot after upgrade .

Step 14 Click Upgrade .

The Upgrade Status windows displays and displays the Upgrade log.

Step 15 When the installation completes, click Finish .

Step 16 To restart the system and activate the upgrade, choose Restart>Switch Versions .

The Switch Software Version window displays.

Step 17 To switch software versions and restart the system, click Switch Versions .

The system restarts running the upgraded software.

### From Remote Source

To install software from a network drive or remote server, use the following procedure.

Note Be sure to back up your system data before starting the software upgrade process. For more information, see the Disaster Recovery System Administration Guide .

Step 1 Navigate to Software Upgrades>Install .

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

Step 14 To restart the system and activate the upgrade, choose Restart>Switch Versions .

The system restarts running the upgraded software.

## Dial Plan Installation

You can install dial plan files from either a local or a remote source by using the same process that is described earlier in this chapter for installing software upgrades. See Software Upgrade and Installation for more information about this process.

After the dial plan files are installed on the system, log in to Cisco Unified CallManager Administration and then navigate to Call Routing>Dial Plan Installer to complete installing the dial plans.

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

These errors could occur when the system fails to create a checksum file, caused by an absent Java executable, /usr/local/thirdparty/java/j2sdk/jre/bin/java, an absent or damaged Java archive file, /usr/local/cm/jar/cmutil.jar, or absent or damaged Java class, com.cisco.ccm.util.Zipper. Even if these errors occur, the locale will continue to work correctly, with the exception of Unified CM Assistant, which cannot detect a change in localized Unified CM Assistant files.

[LOCALE] Could not find /usr/local/cm/application_locale/cmservices/ipma/LocaleMasterVersion.txt in order to update Unified CM Assistant locale information.

This error occurs when the file has not been found in the correct location, which is most likely due to an error in the build process.

[LOCALE] Addition of <RPM-file-name> to the Cisco Unified CallManager database has failed!

This error occurs because of the collective result of any failure that occurs when a locale is being installed; it indicates a terminal condition.

### Supported Cisco Unified Communications Products

For a list of products that Cisco Unified CallManager Locale Installers support, see the Cisco IP Telephony Locale Installer for Cisco CallManager 5.0 , which is available at this URL:

http://www.cisco.com/cgi-bin/tablebuild.pl/callmgr-locale-50

### Caveats

See the following caveats and refer to the latest version of the Cisco Unified CallManager release notes for caveats that are specific to the Cisco Unified CallManager Locale Installer.

English_United_States phrases and voice prompts display after the installation completes.

This situation causes no problems in your cluster. You may not have the latest locale installer that is available on the web. Furthermore, Cisco may choose to update the Cisco Unified CallManager database and not immediately update the Cisco Unified CallManager Locale Installer.

Attempt to install the locale installer on all servers again. If English_United_States phrases or voice prompts display, wait until an updated version of the locale installer displays on the web. Download and install the updated version of the locale installer.

Note Unified CM Auto-Register Phone Tool voice prompts and Cisco Non-IOS gateway network tones do not fall back to English_United_States.

Cisco Unified CallManager only supports the English character set in the User area of Cisco Unified CallManager Administration.

After you download the locale installer, you can display field names in the User area of Cisco Unified CallManager Administration in your chosen language. However, Cisco Unified CallManager only supports the English character set, also known as ISO-Latin1 or ISO-8859-1, in the fields and in all user accounts and passwords that are needed to access these windows. If a user enters data that is not in the English character set, a dialog box displays and states that the user must enter data from the English character set.

You can choose different phone and gateway tones for the system.

If you choose to use different network locales, make sure that you choose a network locale in the parameters or the device pool that is supported by all gateway and phone device types that use the locale installer.

You cannot uninstall a locale or the Cisco Unified CallManager Locale Installer.

No option exists to modify, repair, or remove the locale or the locale installer. Running the locale installer multiple times results in a reinstallation of the locale, as if it is not already installed on the server.

You must reinstall the locale installer after you perform restoration procedures.

The Cisco Unified Communications Applications Server Restore Utility does not restore the locale installer.

Cisco does not support the localization of speed dials or the Personal Address Book on the Cisco Unified IP Phone.

Speed Dial and Personal Address Book text displays in English only.

### Obtaining the Release Notes for the Cisco Unified CallManager Locale Installer

To obtain the release notes for the Cisco Unified CallManager Locale Installer, click the following URL: http://www.cisco.com/univercd/cc/td/doc/product/voice/c_callmg/locinst/index.htm

## Uploading TFTP Server Files

You can use the Upload TFTP Server File option to upload various files for use by the phones to the server. Files that you can upload include custom phone rings, callback tones, and backgrounds. This option uploads files only to the specific server to which you connected, and other nodes in the cluster do not get upgraded.

Files upload into the tftp directory by default. You can also upload files to a subdirectory of the tftp directory.

To upload TFTP server files, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Software Upgrades>Upload TFTP Server File .

The Upload TFTP Server File window displays and shows a listing of the current uploaded files.

Step 2 To upload a file, click Browse and then choose the file that you want to upload.

Step 3 To upload the file to a subdirectory of the tftp directory, enter the subdirectory in the Subdirectory of the tftp directory where file will be uploaded field.

Step 4 To start the upload, click Upload File .

The Status area indicates when the file uploads successfully.

Note If you want to modify a file that is already in the TFTP directory, you can use the CLI command file list tftp to see the files in the TFTP directory and file get tftp to get a copy of a file in the TFTP directory. For more information, see "Command Line Interface."

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
| [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/com/cisco/ipma/client/locales/maDialogs_<ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/com/cisco/ipma/client/locales/maMessages_<ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/com/cisco/ipma/client/locales/maGlobalUI_<ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/LocaleMasterVersion.txt.Checksum. | These errors could occur when the system fails to create a checksum file, caused by an absent Java executable, /usr/local/thirdparty/java/j2sdk/jre/bin/java, an absent or damaged Java archive file, /usr/local/cm/jar/cmutil.jar, or absent or damaged Java class, com.cisco.ccm.util.Zipper. Even if these errors occur, the locale will continue to work correctly, with the exception of Unified CM Assistant, which cannot detect a change in localized Unified CM Assistant files. |
| [LOCALE] Could not find /usr/local/cm/application_locale/cmservices/ipma/LocaleMasterVersion.txt in order to update Unified CM Assistant locale information. | This error occurs when the file has not been found in the correct location, which is most likely due to an error in the build process. |
| [LOCALE] Addition of <RPM-file-name> to the Cisco Unified CallManager database has failed! | This error occurs because of the collective result of any failure that occurs when a locale is being installed; it indicates a terminal condition. |