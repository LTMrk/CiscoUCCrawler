---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-15-0-cup0-b-config-and-admin-guide-15-cup0-2b0c3303c9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/15_0/cup0_b_config-and-admin-guide-15/cup0_b_config-and-admin-guide-1401_chapter_011011.html
retrieved_at: 2026-08-16T15:59:05.925186+00:00
---

Configuration and Administration of the IM and Presence Service, Release 15 and SUs

# Configuration and Administration of the IM and Presence Service, Release 15 and SUs

Updated: January 7, 2026

Chapter: Manage Locales

## Chapter: Manage Locales

# Manage Locales

## Manage Locales Overview

You can configure Cisco Unified Communications Manager and IM and Presence Service to support multiple languages. There is
                           no limit to the number of supported languages you can install.

Cisco provides locale-specific versions of the Cisco Unified Communications Manager Locale Installer and the IM and Presence
                           Service Locale Installer on www.cisco.com. Installed by the system administrator, the locale installer allows the user to
                           view/receive the chosen translated text or tones, if applicable, when a user works with supported interfaces.

After you upgrade Cisco Unified Communications Manager or the IM & Presence Service, you must reinstall all the locales. Install
                           the latest version of the locales that match the major.minor version number of your Cisco Unified Communications Manager node
                           or IM and Presence Service node.

Install locales after you have installed Cisco Unified Communications Manager on every node in the cluster and have set up
                           the database. If you want to install specific locales on IM and Presence Service nodes, you must first install the Cisco Unified
                           Communications Manager locale file for the same country on the Cisco Unified Communications Manager cluster.

Use the information in the following sections to install locales on Cisco Unified Communications Manager nodes and on IM and
                           Presence Service nodes after you complete the software upgrade.

### User Locales

User locale files contain language information for a specific language and country. They provide translated text and voice
                              prompts, if available, for phone displays, user applications, and user web pages in the locale that the user chooses. These
                              files use the following naming convention:

cm-locale-language-country-version.cop (Cisco Unified Communications Manager)

ps-locale-language_country-version.cop (IM and Presence Service)

If your system requires user locales only, install them after you have installed the CUCM locale.

### Network Locales

Network locale files provide country-specific files for various network items, including phone tones, annunciators, and gateway
                              tones. The combined network locale file uses the following naming convention:

cm-locale-combinednetworklocale-version.cop (Cisco Unified Communications Manager)

Cisco may combine multiple network locales in a single locale installer.

Cisco Unified Communications Manager and IM and Presence Service on Cisco-approved, customer-provided servers can support
                                          multiple locales. Installing multiple locale installers ensures that the user can choose from a multitude of locales.

You can install locale files from either a local or a remote source by using the same process for installing software upgrades.
                                          You can install more than one locale file on each node in the cluster. Changes do not take effect until you reboot every node
                                          in the cluster. Cisco strongly recommends that you do not reboot the nodes until you have installed all locales on all nodes
                                          in the cluster. Minimize call-processing interruptions by rebooting the nodes after regular business hours.

## Manage Locales Prerequisites

### Locale Installation Considerations

Install all of the Cisco Unified Communications Manager and IM and Presence Service cluster nodes and set up the database
                                    before you install locales.

If you want to install specific locales on IM and Presence Service nodes, you must first install the Cisco Unified Communications
                                    Manager locale file for the same country on the Cisco Unified Communications Manager cluster.

You can install more than one locale file on each node in the cluster. To activate the new locale, you must restart each node
                                    in the cluster after installation.

You can install locale files from either a local or a remote source by using the same process for installing software upgrades.
                                    See the Upgrade Guide for Cisco Unified Communications Manager for more information about upgrading from a local or a remote source.

## Install Locale Installer on IM and Presence Service

Install the Locale Installer on Cisco Unified Communications Manager before you install locales for IM and Presence Service.
                                    If you want to use a locale other than English, you must install the appropriate language installers on both Cisco Unified
                                    Communications Manager and on IM and Presence Service.

If your IM and Presence Service cluster has more than one node, make sure that the locale installer is installed on every
                                    node in the cluster (install on the IM and Presence database publisher node before the subscriber nodes).

User locales should not be set until all appropriate locale installers are loaded on both systems. Users may experience problems
                                    if they inadvertently set their user locale after the locale installer is loaded on Cisco Unified Communications Manager but
                                    before the locale installer is loaded on IM and Presence Service. If issues are reported, we recommend that you notify each
                                    user to sign into the Cisco Unified Communications Self Care Portal and change their locale from the current setting to English
                                    and then back again to the appropriate language. You can also use the BAT tool to synchronize user locales to the appropriate
                                    language.

Step 1

Navigate to cisco.com and choose the locale installer for your version of IM and Presence Service. http://software.cisco.com/download/navigator.html?mdfid=285971059

Step 2

Click the version of the IM and Presence Locale Installer that is appropriate for your working environment.

Step 3

After downloading the file, save the file to the hard drive and note the location of the saved file.

Step 4

Copy this file to a server that supports SFTP.

Step 5

Sign into Cisco Unified IM and Presence Operating System Administration using the administrator account and password.

Step 6

Choose Software Upgrades > Install/Upgrade .

Step 7

Choose Remote File System as the software location source.

Step 8

Enter the file location, for example /tmp , in the Directory field.

Step 9

Enter the IM and Presence Service server name in the Server field.

Step 10

Enter your username and password credentials in the User Name and User Password fields.

Step 11

Choose SFTP for the Transfer Protocol.

Step 12

Click Next .

Step 13

Choose the IM and Presence Service locale installer from the list of search results.

Step 14

Click Next to load the installer file and validate it.

Step 15

After you complete the locale installation, restart each server in the cluster.

Step 16

The default setting for installed locales is "English, United States”. While your IM and Presence Service node is restarting,
                                       change the language of your browser, if necessary, to match the locale of the installer that you have downloaded.

Step 17

Verify that your users can choose the locales for supported products.

Tip

Make sure that you install the same components on every server in the cluster.

### Error Messages Locales Reference

See the following table for a description of the messages that can occur during Locale Installer activation. If an error occurs,
                                 you can view the messages in the installation log.

Message

Description

[LOCALE] File not found: <language>_<country>_user_locale.csv, the user locale has not been added to the database.

This error occurs when the system cannot locate the CSV file, which contains user locale information to add to the database,
                                             which indicates an error with the build process.

[LOCALE] File not found: <country>_network_locale.csv, the network locale has not been added to the database.

This error occurs when the system cannot locate the CSV file, which contains network locale information to add to the database
                                             This indicates an error with the build process.

[LOCALE] CSV file installer installdb is not present or not executable

You must ensure that an application called installdb is present. It reads information that a CSV file contains and applies
                                             it correctly to the target database. If this application is not found, it did not get installed with the Cisco Unified Communications
                                             application (very unlikely), has been deleted (more likely), or the node does not have a Cisco Unified Communications application,
                                             such as Cisco Unified Communications Manager or IM and Presence Service, installed (most likely). Installation of the locale
                                             will terminate because locales will not work without the correct records in the database.

[LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ ipma/com/cisco/ipma/client/locales/maDialogs_ <ll>_<CC>.properties.Checksum.

[LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ ipma/com/cisco/ipma/client/locales/maMessages_ <ll>_<CC>.properties.Checksum.

[LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ ipma/com/cisco/ipma/client/locales/maGlobalUI_ <ll>_<CC>.properties.Checksum.

[LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/ LocaleMasterVersion.txt.Checksum.

These errors could occur when the system fails to create a checksum file, which an absent Java executable, /usr/local/thirdparty/java/j2sdk/jre/bin/java , an absent or damaged Java archive file, /usr/local/cm/jar/cmutil.jar , or an absent or damaged Java class, com.cisco.ccm.util.Zipper , causes. Even if these errors occur, the locale will continue to work correctly, with the exception of Cisco Unified Communications
                                             Manager Assistant, which can not detect a change in localized Cisco Unified Communications Manager Assistant files.

[LOCALE] Could not find /usr/local/cm/application_locale/cmservices/ ipma/LocaleMasterVersion.txt in order to update Unified
                                             CM Assistant locale information.

This error occurs when the system does not find the file in the correct location, which is most likely due to an error in
                                             the build process.

[LOCALE] Addition of <locale-installer-file-name> to the database has failed!

This error occurs because the collective result of any failure that occurs when a locale is being installed causes it; it
                                             indicates a terminal condition.

[LOCALE] Could not locate <locale-installer-file-name>

The system will not migrate this locale during an upgrade.

The downloaded locale installer file no longer resides in the download location. The platform may have moved or deleted it.
                                             This is noncritical error indicates that after the Cisco Unified Communications application has been upgraded, you need to
                                             either reapply the locale installer or download and apply a new locale installer.

[LOCALE] Could not copy <locale-installer-file-name> to migratory path. This locale will not be migrated during an upgrade!

You cannot copy the downloaded locale installer file to the migration path. This noncritical error indicates that after the
                                             Cisco Unified Communications application has been upgraded, you need to either reapply the locale installer or download and
                                             apply a new locale installer.

[LOCALE] DRS unregistration failed

The locale installer could not deregister from the Disaster Recovery System. A backup or restore record will not include the
                                             locale installer. Record the installation log and contact Cisco TAC.

[LOCALE] Backup failed!

The Disaster Recovery System could not create a tarball from the downloaded locale installer files. Re-apply the local installer
                                             before attempting to back up.

Manually reinstalling locales after a system restore achieves the same goal.

[LOCALE] No COP files found in restored tarball!

Corruption of backup files may prevent successful extraction of locale installer files.

Manual reapplication of the locale installer will restore the locale fully.

[LOCALE] Failed to successfully reinstall COP files!

Corruption of backup files may damage locale installer files.

Manual reapplication of the locale installer will restore the locale fully.

[LOCALE] Failed to build script to reinstall COP files!

The platform could not dynamically create the script used to reinstall locales.

Manual reapplication of the locale installer will restore the locale fully. Record the installation log and contact TAC.

### Localized Applications

IM and Presence Service applications support a variety of different languages. See the following table for a list of localized
                                 applications and the available languages.

Interface

Supported Languages

Administrative Applications

Cisco Unified CM IM and Presence Administration

Chinese (China), English, Japanese (Japan), Korean (Korean Republic)

Cisco Unified IM and Presence Operating System

Chinese (China), English, Japanese (Japan), Korean (Korean Republic)

| Note | Cisco Unified Communications Manager and IM and Presence Service on Cisco-approved, customer-provided servers can support
                                          multiple locales. Installing multiple locale installers ensures that the user can choose from a multitude of locales. You can install locale files from either a local or a remote source by using the same process for installing software upgrades.
                                          You can install more than one locale file on each node in the cluster. Changes do not take effect until you reboot every node
                                          in the cluster. Cisco strongly recommends that you do not reboot the nodes until you have installed all locales on all nodes
                                          in the cluster. Minimize call-processing interruptions by rebooting the nodes after regular business hours. |
|---|---|

| Step 1 | Navigate to cisco.com and choose the locale installer for your version of IM and Presence Service. http://software.cisco.com/download/navigator.html?mdfid=285971059 |
|---|---|
| Step 2 | Click the version of the IM and Presence Locale Installer that is appropriate for your working environment. |
| Step 3 | After downloading the file, save the file to the hard drive and note the location of the saved file. |
| Step 4 | Copy this file to a server that supports SFTP. |
| Step 5 | Sign into Cisco Unified IM and Presence Operating System Administration using the administrator account and password. |
| Step 6 | Choose Software Upgrades > Install/Upgrade . |
| Step 7 | Choose Remote File System as the software location source. |
| Step 8 | Enter the file location, for example /tmp , in the Directory field. |
| Step 9 | Enter the IM and Presence Service server name in the Server field. |
| Step 10 | Enter your username and password credentials in the User Name and User Password fields. |
| Step 11 | Choose SFTP for the Transfer Protocol. |
| Step 12 | Click Next . |
| Step 13 | Choose the IM and Presence Service locale installer from the list of search results. |
| Step 14 | Click Next to load the installer file and validate it. |
| Step 15 | After you complete the locale installation, restart each server in the cluster. |
| Step 16 | The default setting for installed locales is "English, United States”. While your IM and Presence Service node is restarting,
                                       change the language of your browser, if necessary, to match the locale of the installer that you have downloaded. |
| Step 17 | Verify that your users can choose the locales for supported products. Tip Make sure that you install the same components on every server in the cluster. | Tip | Make sure that you install the same components on every server in the cluster. |
| Tip | Make sure that you install the same components on every server in the cluster. |

| Tip | Make sure that you install the same components on every server in the cluster. |
|---|---|

| Message | Description |
|---|---|
| [LOCALE] File not found: <language>_<country>_user_locale.csv, the user locale has not been added to the database. | This error occurs when the system cannot locate the CSV file, which contains user locale information to add to the database,
                                             which indicates an error with the build process. |
| [LOCALE] File not found: <country>_network_locale.csv, the network locale has not been added to the database. | This error occurs when the system cannot locate the CSV file, which contains network locale information to add to the database
                                             This indicates an error with the build process. |
| [LOCALE] CSV file installer installdb is not present or not executable | You must ensure that an application called installdb is present. It reads information that a CSV file contains and applies
                                             it correctly to the target database. If this application is not found, it did not get installed with the Cisco Unified Communications
                                             application (very unlikely), has been deleted (more likely), or the node does not have a Cisco Unified Communications application,
                                             such as Cisco Unified Communications Manager or IM and Presence Service, installed (most likely). Installation of the locale
                                             will terminate because locales will not work without the correct records in the database. |
| [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ ipma/com/cisco/ipma/client/locales/maDialogs_ <ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ ipma/com/cisco/ipma/client/locales/maMessages_ <ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ ipma/com/cisco/ipma/client/locales/maGlobalUI_ <ll>_<CC>.properties.Checksum. [LOCALE] Could not create /usr/local/cm/application_locale/cmservices/ipma/ LocaleMasterVersion.txt.Checksum. | These errors could occur when the system fails to create a checksum file, which an absent Java executable, /usr/local/thirdparty/java/j2sdk/jre/bin/java , an absent or damaged Java archive file, /usr/local/cm/jar/cmutil.jar , or an absent or damaged Java class, com.cisco.ccm.util.Zipper , causes. Even if these errors occur, the locale will continue to work correctly, with the exception of Cisco Unified Communications
                                             Manager Assistant, which can not detect a change in localized Cisco Unified Communications Manager Assistant files. |
| [LOCALE] Could not find /usr/local/cm/application_locale/cmservices/ ipma/LocaleMasterVersion.txt in order to update Unified
                                             CM Assistant locale information. | This error occurs when the system does not find the file in the correct location, which is most likely due to an error in
                                             the build process. |
| [LOCALE] Addition of <locale-installer-file-name> to the database has failed! | This error occurs because the collective result of any failure that occurs when a locale is being installed causes it; it
                                             indicates a terminal condition. |
| [LOCALE] Could not locate <locale-installer-file-name> | The system will not migrate this locale during an upgrade. The downloaded locale installer file no longer resides in the download location. The platform may have moved or deleted it.
                                             This is noncritical error indicates that after the Cisco Unified Communications application has been upgraded, you need to
                                             either reapply the locale installer or download and apply a new locale installer. |
| [LOCALE] Could not copy <locale-installer-file-name> to migratory path. This locale will not be migrated during an upgrade! | You cannot copy the downloaded locale installer file to the migration path. This noncritical error indicates that after the
                                             Cisco Unified Communications application has been upgraded, you need to either reapply the locale installer or download and
                                             apply a new locale installer. |
| [LOCALE] DRS unregistration failed | The locale installer could not deregister from the Disaster Recovery System. A backup or restore record will not include the
                                             locale installer. Record the installation log and contact Cisco TAC. |
| [LOCALE] Backup failed! | The Disaster Recovery System could not create a tarball from the downloaded locale installer files. Re-apply the local installer
                                             before attempting to back up. Note Manually reinstalling locales after a system restore achieves the same goal. | Note | Manually reinstalling locales after a system restore achieves the same goal. |
| Note | Manually reinstalling locales after a system restore achieves the same goal. |
| [LOCALE] No COP files found in restored tarball! | Corruption of backup files may prevent successful extraction of locale installer files. Note Manual reapplication of the locale installer will restore the locale fully. | Note | Manual reapplication of the locale installer will restore the locale fully. |
| Note | Manual reapplication of the locale installer will restore the locale fully. |
| [LOCALE] Failed to successfully reinstall COP files! | Corruption of backup files may damage locale installer files. Note Manual reapplication of the locale installer will restore the locale fully. | Note | Manual reapplication of the locale installer will restore the locale fully. |
| Note | Manual reapplication of the locale installer will restore the locale fully. |
| [LOCALE] Failed to build script to reinstall COP files! | The platform could not dynamically create the script used to reinstall locales. Note Manual reapplication of the locale installer will restore the locale fully. Record the installation log and contact TAC. | Note | Manual reapplication of the locale installer will restore the locale fully. Record the installation log and contact TAC. |
| Note | Manual reapplication of the locale installer will restore the locale fully. Record the installation log and contact TAC. |

| Note | Manually reinstalling locales after a system restore achieves the same goal. |
|---|---|

| Note | Manual reapplication of the locale installer will restore the locale fully. |
|---|---|

| Note | Manual reapplication of the locale installer will restore the locale fully. |
|---|---|

| Note | Manual reapplication of the locale installer will restore the locale fully. Record the installation log and contact TAC. |
|---|---|

| Interface | Supported Languages |
|---|---|
| Administrative Applications |
| Cisco Unified CM IM and Presence Administration | Chinese (China), English, Japanese (Japan), Korean (Korean Republic) |
| Cisco Unified IM and Presence Operating System | Chinese (China), English, Japanese (Japan), Korean (Korean Republic) |