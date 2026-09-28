---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-installandupgrade-0ebebd8b46
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/installandupgrade/guide/ccvp_b_1261-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal_chapter_0110.html
retrieved_at: 2026-08-21T17:04:06.409908+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: May 14, 2021

Chapter: Unified CVP MR/Call Studio Uninstallation

## Chapter: Unified CVP MR/Call Studio Uninstallation

- Unified CVP MR/Call Studio Uninstallation

- Uninstall Unified CVP MR/Call Studio From Windows Control Panel

- Uninstall Unified CVP MR/Call Studio Using Installation Media

# Unified CVP MR /Call Studio Uninstallation

## Uninstall Unified CVP MR /Call Studio From Windows Control Panel

### Before you begin

Shut down all
                                    				applications and close all open files.

Close the Unified CVP component and related files.

Step 1

Click Start > Control
                                             				  Panel > Programs and Features .

Step 2

Click Cisco CVP Minor Release CVP12.6(1) / Cisco Unified Call Studio , and then click Remove .

Step 3

Click Next .

After
                                          				uninstallation, the Uninstall Complete screen appears. Depending on the
                                          				components you uninstalled, you may need to reboot your computer.

The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. Media folders with same names are replaced during the Unified CVP installation process.
                                                      User-created media files and folders remain unchanged during Unified CVP upgrade. Create all the media folders in wwwroot and use the relative paths to simplify the migration process for the future releases of Unified CVP that support A-law, u-law,
                                                      and G729 files.

The Unified CallStudio uninstallation procedure does not clean up all the files and folders, such as configuration files,
                                                      workspace files and folders that are generated post-installation. If required, backup the call studio applications from %CallStudio_directory%\eclipse\workspace . After uninstalling, manually delete the eclipse folder and then reboot your system.

## Uninstall Unified CVP MR /Call Studio Using Installation Media

### Before you begin

Shut down all
                                    				applications and close all open files.

Close Unified CVP component and related files.

Step 1

Run the CVP12.6.1.exe file of the Unified CVP software.

Step 2

Select the Remove option, and click Next .

The Uninstall Complete screen appears. Depending on the
                                          				components you uninstalled, you may need to reboot your computer.

The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. The media folders with same names get replaced during the Unified CVP installation process.
                                                      The user created media files and folders remains unchanged during Unified CVP upgrade. It is required to create all the media
                                                      folders in the wwwroot and use the relative paths, as it simplifies the migration process for the future releases of Unified CVP that supports A-law,
                                                      u-law, and G729 files.

| Step 1 | Click Start > Control
                                             				  Panel > Programs and Features . |
|---|---|
| Step 2 | Click Cisco CVP Minor Release CVP12.6(1) / Cisco Unified Call Studio , and then click Remove . |
| Step 3 | Click Next . After
                                          				uninstallation, the Uninstall Complete screen appears. Depending on the
                                          				components you uninstalled, you may need to reboot your computer. Note The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. Media folders with same names are replaced during the Unified CVP installation process.
                                                      User-created media files and folders remain unchanged during Unified CVP upgrade. Create all the media folders in wwwroot and use the relative paths to simplify the migration process for the future releases of Unified CVP that support A-law, u-law,
                                                      and G729 files. Note The Unified CallStudio uninstallation procedure does not clean up all the files and folders, such as configuration files,
                                                      workspace files and folders that are generated post-installation. If required, backup the call studio applications from %CallStudio_directory%\eclipse\workspace . After uninstalling, manually delete the eclipse folder and then reboot your system. | Note | The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. Media folders with same names are replaced during the Unified CVP installation process.
                                                      User-created media files and folders remain unchanged during Unified CVP upgrade. Create all the media folders in wwwroot and use the relative paths to simplify the migration process for the future releases of Unified CVP that support A-law, u-law,
                                                      and G729 files. | Note | The Unified CallStudio uninstallation procedure does not clean up all the files and folders, such as configuration files,
                                                      workspace files and folders that are generated post-installation. If required, backup the call studio applications from %CallStudio_directory%\eclipse\workspace . After uninstalling, manually delete the eclipse folder and then reboot your system. |
| Note | The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. Media folders with same names are replaced during the Unified CVP installation process.
                                                      User-created media files and folders remain unchanged during Unified CVP upgrade. Create all the media folders in wwwroot and use the relative paths to simplify the migration process for the future releases of Unified CVP that support A-law, u-law,
                                                      and G729 files. |
| Note | The Unified CallStudio uninstallation procedure does not clean up all the files and folders, such as configuration files,
                                                      workspace files and folders that are generated post-installation. If required, backup the call studio applications from %CallStudio_directory%\eclipse\workspace . After uninstalling, manually delete the eclipse folder and then reboot your system. |

| Note | The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. Media folders with same names are replaced during the Unified CVP installation process.
                                                      User-created media files and folders remain unchanged during Unified CVP upgrade. Create all the media folders in wwwroot and use the relative paths to simplify the migration process for the future releases of Unified CVP that support A-law, u-law,
                                                      and G729 files. |
|---|---|

| Note | The Unified CallStudio uninstallation procedure does not clean up all the files and folders, such as configuration files,
                                                      workspace files and folders that are generated post-installation. If required, backup the call studio applications from %CallStudio_directory%\eclipse\workspace . After uninstalling, manually delete the eclipse folder and then reboot your system. |
|---|---|

| Step 1 | Run the CVP12.6.1.exe file of the Unified CVP software. |
|---|---|
| Step 2 | Select the Remove option, and click Next . The Uninstall Complete screen appears. Depending on the
                                          				components you uninstalled, you may need to reboot your computer. Note The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. The media folders with same names get replaced during the Unified CVP installation process.
                                                      The user created media files and folders remains unchanged during Unified CVP upgrade. It is required to create all the media
                                                      folders in the wwwroot and use the relative paths, as it simplifies the migration process for the future releases of Unified CVP that supports A-law,
                                                      u-law, and G729 files. | Note | The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. The media folders with same names get replaced during the Unified CVP installation process.
                                                      The user created media files and folders remains unchanged during Unified CVP upgrade. It is required to create all the media
                                                      folders in the wwwroot and use the relative paths, as it simplifies the migration process for the future releases of Unified CVP that supports A-law,
                                                      u-law, and G729 files. |
| Note | The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. The media folders with same names get replaced during the Unified CVP installation process.
                                                      The user created media files and folders remains unchanged during Unified CVP upgrade. It is required to create all the media
                                                      folders in the wwwroot and use the relative paths, as it simplifies the migration process for the future releases of Unified CVP that supports A-law,
                                                      u-law, and G729 files. |

| Note | The Unified CVP uninstallation procedure does not clean up all the files and folders, such as log files, media files and folders
                                                      that are generated postinstallation. The media folders with same names get replaced during the Unified CVP installation process.
                                                      The user created media files and folders remains unchanged during Unified CVP upgrade. It is required to create all the media
                                                      folders in the wwwroot and use the relative paths, as it simplifies the migration process for the future releases of Unified CVP that supports A-law,
                                                      u-law, and G729 files. |
|---|---|