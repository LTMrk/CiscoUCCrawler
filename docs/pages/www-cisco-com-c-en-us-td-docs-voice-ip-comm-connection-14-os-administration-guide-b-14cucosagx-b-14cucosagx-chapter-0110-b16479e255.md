---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-os-administration-guide-b-14cucosagx-b-14cucosagx-chapter-0110-b16479e255
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/os_administration/guide/b_14cucosagx/b_14cucosagx_chapter_0110.html
retrieved_at: 2026-08-17T03:42:50.098908+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 14

# Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 14

Updated: November 28, 2025

Chapter: Software
	 Upgrades

## Chapter: Software
	 Upgrades

# Software
                     	 Upgrades

For information on upgrading Cisco Unity Connection to the shipping version, see the " Upgrading Cisco Unity Connection " chapter in the Install, Upgrade and Maintain guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

For information on installing Cisco Unity Connection languages, see the " Maintaining Cisco Unity Connection Server " chapter in the Install, Upgrade and Maintain guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

## Software Installation and Upgrade

The software upgrade options enable you to upgrade the software version that is running on the operating system or to install
                              specific software options, including Cisco Unified Communications Operating System Locale Installers, dial plans, and TFTP
                              server files.

From the Install/Upgrade menu option, you can upgrade system software from either a local disk or a remote server . The upgraded software gets installed
                              on the inactive partition, and you can then restart the system and switch partitions, so the system starts running on the
                              newer software version.

To upgrade Cisco Unity Connection, do the following procedure:

Step 1

From the Cisco Unified Communications Operating System Administration window, navigate to Software Upgrades > Install/Upgrade .

The Software Installation/Upgrade page displays.

Step 2

Do the following settings on the page for upgrading Unity Connection:

Field

Description

Use download credentials from Publisher

(Applicable only for Subscriber server) Check this check box to use the source configuration provided for the publisher server.

If check box is not checked, you must provide the all configuration for upgrade process.

By default, check box is checked.

Source

Select the applicable option from the drop down menu:

DVD/CD : Select this option to upgrade from disk drive

Remote Filesystem : Select this option to upgrade from remoter server.

Local Filesystem :  Select this option to use the previously downloaded ISO or COP files for the upgrade.

Directory

(Applicable for Remote Filesystem) Enter the path of the folder that contains the upgrade file.

Server

(Applicable for Remote Filesystem) Enter the server name or IP address.

User Name

(Applicable for Remote Filesystem) Enter the alias that is used to sign in to the remote server.

User Password

(Applicable for Remote Filesystem) Enter the password that is used to sign in to the remote server.

Transfer Protocol

(Applicable for Remote Filesystem) Select the applicable transfer protocol either SFTP or FTP.

SMTP Server

Enter the IP address of the SMTP server.

Email Destination

Enter your email address along with the SMTP server.

Continue with Upgrade after Download 1

Check this check box to start the upgrade immediately when the file download completes and start the installation. No checksum
                                                      and SHA details are displayed.

By default, check box is checked.

Switch-Version Server after Upgrade 1

Check this check box to reboot the system automatically after the completion of successful upgrade.

By default, check box is not checked.

For more information on upgrading Cisco Unity Connection, see " Upgrading Cisco Unity Connection " chapter of Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg/b_15cuciumg_chapter_0100.html

## Device Load
                        	 Management

For information on Device Load Management, see the Install, Upgrade and Maintain guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

## Setting Up a
                        	 Customized Log-on Message

To upload a customized log-on message, follow this procedure:

Step 1

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Software Upgrades > Customized Logon
                                             				  Message .

The Customized Logon Message window displays.

Step 2

Click Browse to
                                       			 select the text file (.txt) that contains the log-on message, which you want to
                                       			 display.

Step 3

Click Upload File .

- Cisco Unity Connection
                                             				  Administration

- Cisco Unity Connection
                                             				  Serviceability

- Cisco Unified Operating
                                             				  System Administration

- Cisco Unified
                                             				  Serviceability

- Disaster Recovery System
                                             				  Administration

- Cisco Prime License Manager

- Cisco Personal
                                             				  Communication Assistant

- Real-Time Monitoring Tool

- Command Line Interface

Step 4

(Optional) Check the Require User
                                          				Acknowledgment check box to display the customized log-on message in pop-up
                                       			 window as well whenever a user accesses the above interfaces along with Web
                                       			 Inbox. To successfully log in to the interface, user must explicitly
                                       			 acknowledge the pop-up window by clicking OK .

Step 5

To revert to the default log-on message, click Delete .

Your customized log-on message gets deleted, and the system
                                          				displays the default log-on message.

## Branding
                        	 Customization in Unity Connection

Cisco Unity Connection supports feature Branding Customization by which the appearance of Unity Connection web applications can be modified based on the organizational requirements. This
                           feature allows an Operating System Administrator to customize company logo, background colors, border colors and font colors
                           of Unity Connection web applications. Branding can be applied on the following web applications of Unity Connection:

- Cisco Unity Connection Administration

- Cisco Personal Communications Assistant

- Web Inbox

### Prerequisite for Configuring Branding

To configure the branding in Unity Connection you must have a branding.zip file that includes specified folders, sub folders
                              and other image files. Unity Connection also provides branding.zip template which allows you to rebrand Unity Connection web
                              applications.

For more information on structure of branding.zip file, see Branding File Structure .

### Task List for Configuring Branding in Unity Connection

Do the following to configure the branding feature in Unity Connection:

(Optional) Execute file get install branding.zip CLI command to copy the branding.zip template file to your remote server. After copying the file to remote server, you can
                                    modify it as per your organizational requirement and save it as branding.zip. For information on branding customization options
                                    and the procedure to modify them, see User Interface Branding Options .

For more information on CLI command, see Command Line Interface Reference Guide for Cisco Unified Communications Solutions available at, https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Login to Cisco Unified Communications Operating System Administration page, navigate Software Upgrades > Branding . On the Branding page, select Choose File to browse branding.zip file from your remote server and select Upload File .

After successfully uploading the file, select Enable Branding .

To disable the customized branding, select Disable Branding on the Branding page.

To enable or disable the branding, you can also execute utils branding enable/disable CLI command.

Restart the Tomcat service to reflect the branding updates on Cisco Unity Connection web applications.

In case of a cluster, you must enable or disable the branding on each node of the cluster.

### User Interface
                           	 Branding Options

Below images describe the branding customization options for one of the web application of Unity Connection ( Example: Cisco
                                 Unity Connection Administration ).

```
ciscoLogo12pxMargin.gif
```

```
branding_logo.png
```

You can use a single image or a combination of six images to create a grading effect.

Single Image option— Save your header background as a single image:

- brandingHeader.gif (652*1 pixel)

Graded background option:— Save your header background as six images for a graded effect:

- brandingHeaderBegLTR.gif (652*1 pixel)

- brandingHeaderBegRTL.gif (652*1 pixel)

- brandingHeaderEndLTR.gif (652*1 pixel)

- brandingHeaderEndRTL.gif (652*1 pixel)

- brandingHeaderMidLTR.gif (652*1 pixel)

- brandingHeaderMidRTL.gif (652*1 pixel)

header.go.font.color

header.go.background.color

header.go.border.color

splash.reset.text.color

splash.reset.back.ground.color

splash.hexcode.3

splash.login.text.color

splash.login.back.ground.color

Unity Connection Administration text heading

System Version text

splash.version.color

#### Branding File
                              	 Structure

This section describes the structure of folder, subfolder and other files included in branding.zip template. There are two
                                    options for the folder structure, depending on whether you want to use a single image for the header or a combination of six
                                    images in order to create a graded effect for the header.

If you
                                                   						want a single image for the header background (callout item 3), your branding
                                                   						folder must contain the following subfolders and image files:

```
Branding (folder)
           ccmadmin (folder)
              BrandingProperties.properties (properties file)
              brandingHeader.gif (652*1 pixel image)
              ciscoLogo12pxMargin.gif (44*44 pixel image)
           branding_logo.png (44*25 pixel image)
```

If you
                                                   						want to create a graded image for the header background, you need six separate
                                                   						image files to create the graded effect. Your branding folder must contain
                                                   						these subfolders and files

```
Branding(folder)
           ccmadmin (folder)
               BrandingProperties.properties (file)
               brandingHeaderBegLTR.gif (652*1 pixel image)
               brandingHeaderBegRTL.gif (652*1 pixel image)
               brandingHeaderEndLTR.gif (652*1 pixel image)
               brandingHeaderEndRTL.gif (652*1 pixel image)
               brandingHeaderMidLTR.gif (652*1 pixel image)
               brandingHeaderMidRTL.gif (652*1 pixel image)
               ciscoLogo12pxMargin.gif (44*44 pixel image)
           branding_logo.png (44*25 pixel image)
```

#### Branding
                              	 Properties Editing Example

Branding properties can be edited by adding the hex code in the properties file (BrandingProperties.properties). The properties file uses HTML-based hex code. For example, if you want to change the color of the Navigation text item (callout
                                 item #4) to red, add the following code to your properties file:

header.navigation.color="#FF0000" .

In this code, header.navigation.color is the branding property that
                                 		you want to edit, and #FF0000" is the new setting (red).

| Note | You must do all software installations and upgrades with the software upgrades features that are included in the Cisco Unified
                                       Communications Operating System GUI and command line interface. The system can upload and process only software that Cisco
                                       Systems approved. You cannot install or use third-party or Windows-based software applications that you may have been using
                                       with a previous version of Cisco Unified Communications Manager. |
|---|---|

| Step 1 | From the Cisco Unified Communications Operating System Administration window, navigate to Software Upgrades > Install/Upgrade . The Software Installation/Upgrade page displays. |
|---|---|
| Step 2 | Do the following settings on the page for upgrading Unity Connection: Field Description Use download credentials from Publisher (Applicable only for Subscriber server) Check this check box to use the source configuration provided for the publisher server. If check box is not checked, you must provide the all configuration for upgrade process. By default, check box is checked. Source Select the applicable option from the drop down menu: DVD/CD : Select this option to upgrade from disk drive Remote Filesystem : Select this option to upgrade from remoter server. Local Filesystem :  Select this option to use the previously downloaded ISO or COP files for the upgrade. Directory (Applicable for Remote Filesystem) Enter the path of the folder that contains the upgrade file. Server (Applicable for Remote Filesystem) Enter the server name or IP address. User Name (Applicable for Remote Filesystem) Enter the alias that is used to sign in to the remote server. User Password (Applicable for Remote Filesystem) Enter the password that is used to sign in to the remote server. Transfer Protocol (Applicable for Remote Filesystem) Select the applicable transfer protocol either SFTP or FTP. SMTP Server Enter the IP address of the SMTP server. Email Destination Enter your email address along with the SMTP server. Continue with Upgrade after Download 1 Check this check box to start the upgrade immediately when the file download completes and start the installation. No checksum
                                                      and SHA details are displayed. By default, check box is checked. Switch-Version Server after Upgrade 1 Check this check box to reboot the system automatically after the completion of successful upgrade. By default, check box is not checked. 1 The field is not applicable for Cisco Unity Connection. For more information on upgrading Cisco Unity Connection, see " Upgrading Cisco Unity Connection " chapter of Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg/b_15cuciumg_chapter_0100.html | Field | Description | Use download credentials from Publisher | (Applicable only for Subscriber server) Check this check box to use the source configuration provided for the publisher server. If check box is not checked, you must provide the all configuration for upgrade process. By default, check box is checked. | Source | Select the applicable option from the drop down menu: DVD/CD : Select this option to upgrade from disk drive Remote Filesystem : Select this option to upgrade from remoter server. Local Filesystem :  Select this option to use the previously downloaded ISO or COP files for the upgrade. | Directory | (Applicable for Remote Filesystem) Enter the path of the folder that contains the upgrade file. | Server | (Applicable for Remote Filesystem) Enter the server name or IP address. | User Name | (Applicable for Remote Filesystem) Enter the alias that is used to sign in to the remote server. | User Password | (Applicable for Remote Filesystem) Enter the password that is used to sign in to the remote server. | Transfer Protocol | (Applicable for Remote Filesystem) Select the applicable transfer protocol either SFTP or FTP. | SMTP Server | Enter the IP address of the SMTP server. | Email Destination | Enter your email address along with the SMTP server. | Continue with Upgrade after Download 1 | Check this check box to start the upgrade immediately when the file download completes and start the installation. No checksum
                                                      and SHA details are displayed. By default, check box is checked. | Switch-Version Server after Upgrade 1 | Check this check box to reboot the system automatically after the completion of successful upgrade. By default, check box is not checked. |
| Field | Description |
| Use download credentials from Publisher | (Applicable only for Subscriber server) Check this check box to use the source configuration provided for the publisher server. If check box is not checked, you must provide the all configuration for upgrade process. By default, check box is checked. |
| Source | Select the applicable option from the drop down menu: DVD/CD : Select this option to upgrade from disk drive Remote Filesystem : Select this option to upgrade from remoter server. Local Filesystem :  Select this option to use the previously downloaded ISO or COP files for the upgrade. |
| Directory | (Applicable for Remote Filesystem) Enter the path of the folder that contains the upgrade file. |
| Server | (Applicable for Remote Filesystem) Enter the server name or IP address. |
| User Name | (Applicable for Remote Filesystem) Enter the alias that is used to sign in to the remote server. |
| User Password | (Applicable for Remote Filesystem) Enter the password that is used to sign in to the remote server. |
| Transfer Protocol | (Applicable for Remote Filesystem) Select the applicable transfer protocol either SFTP or FTP. |
| SMTP Server | Enter the IP address of the SMTP server. |
| Email Destination | Enter your email address along with the SMTP server. |
| Continue with Upgrade after Download 1 | Check this check box to start the upgrade immediately when the file download completes and start the installation. No checksum
                                                      and SHA details are displayed. By default, check box is checked. |
| Switch-Version Server after Upgrade 1 | Check this check box to reboot the system automatically after the completion of successful upgrade. By default, check box is not checked. |

| Field | Description |
|---|---|
| Use download credentials from Publisher | (Applicable only for Subscriber server) Check this check box to use the source configuration provided for the publisher server. If check box is not checked, you must provide the all configuration for upgrade process. By default, check box is checked. |
| Source | Select the applicable option from the drop down menu: DVD/CD : Select this option to upgrade from disk drive Remote Filesystem : Select this option to upgrade from remoter server. Local Filesystem :  Select this option to use the previously downloaded ISO or COP files for the upgrade. |
| Directory | (Applicable for Remote Filesystem) Enter the path of the folder that contains the upgrade file. |
| Server | (Applicable for Remote Filesystem) Enter the server name or IP address. |
| User Name | (Applicable for Remote Filesystem) Enter the alias that is used to sign in to the remote server. |
| User Password | (Applicable for Remote Filesystem) Enter the password that is used to sign in to the remote server. |
| Transfer Protocol | (Applicable for Remote Filesystem) Select the applicable transfer protocol either SFTP or FTP. |
| SMTP Server | Enter the IP address of the SMTP server. |
| Email Destination | Enter your email address along with the SMTP server. |
| Continue with Upgrade after Download 1 | Check this check box to start the upgrade immediately when the file download completes and start the installation. No checksum
                                                      and SHA details are displayed. By default, check box is checked. |
| Switch-Version Server after Upgrade 1 | Check this check box to reboot the system automatically after the completion of successful upgrade. By default, check box is not checked. |

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Software Upgrades > Customized Logon
                                             				  Message . The Customized Logon Message window displays. |
|---|---|
| Step 2 | Click Browse to
                                       			 select the text file (.txt) that contains the log-on message, which you want to
                                       			 display. |
| Step 3 | Click Upload File . The
                                       			 customized log-on message will be displayed on the login screen as well as home
                                       			 screen of the following interfaces of Unity Connection: Cisco Unity Connection
                                             				  Administration Cisco Unity Connection
                                             				  Serviceability Cisco Unified Operating
                                             				  System Administration Cisco Unified
                                             				  Serviceability Disaster Recovery System
                                             				  Administration Cisco Prime License Manager Cisco Personal
                                             				  Communication Assistant Real-Time Monitoring Tool Command Line Interface Note You
                                                      				  cannot upload a file that is larger than 10kB. | Note | You
                                                      				  cannot upload a file that is larger than 10kB. |
| Note | You
                                                      				  cannot upload a file that is larger than 10kB. |
| Step 4 | (Optional) Check the Require User
                                          				Acknowledgment check box to display the customized log-on message in pop-up
                                       			 window as well whenever a user accesses the above interfaces along with Web
                                       			 Inbox. To successfully log in to the interface, user must explicitly
                                       			 acknowledge the pop-up window by clicking OK . Note In case
                                                      				  of Web Inbox, customized log-on message is displayed only in pop-up window | Note | In case
                                                      				  of Web Inbox, customized log-on message is displayed only in pop-up window |
| Note | In case
                                                      				  of Web Inbox, customized log-on message is displayed only in pop-up window |
| Step 5 | To revert to the default log-on message, click Delete . Your customized log-on message gets deleted, and the system
                                          				displays the default log-on message. |

| Note | You
                                                      				  cannot upload a file that is larger than 10kB. |
|---|---|

| Note | In case
                                                      				  of Web Inbox, customized log-on message is displayed only in pop-up window |
|---|---|

| Note | In Web Inbox, only company logo can be modified. |
|---|---|

| Note | To enable or disable the branding, you can also execute utils branding enable/disable CLI command. For more information on CLI, see Command Line Interface Guide for Cisco Unified Communications Solutions available at, https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| Note | In case of a cluster, you must enable or disable the branding on each node of the cluster. |
|---|---|

| Item | Description | Branding edits |
|---|---|---|
| 1 | Company Logo | To add your logo to Cisco Unity Connection, save your company logo as a 44*44 pixel image with the following filename: ciscoLogo12pxMargin.gif (44*44 pixels) Note To add your logo to Web Inbox and Mini Inbox, save your company logo as a 44*25 pixel image with the following filename: branding_logo.png | Note | To add your logo to Web Inbox and Mini Inbox, save your company logo as a 44*25 pixel image with the following filename: |
| Note | To add your logo to Web Inbox and Mini Inbox, save your company logo as a 44*25 pixel image with the following filename: |
| 2 | Cisco Unity Connection Administration header font color | heading.heading.color |
| 3 | Header Background | You can use a single image or a combination of six images to create a grading effect. Single Image option— Save your header background as a single image: brandingHeader.gif (652*1 pixel) Graded background option:— Save your header background as six images for a graded effect: brandingHeaderBegLTR.gif (652*1 pixel) brandingHeaderBegRTL.gif (652*1 pixel) brandingHeaderEndLTR.gif (652*1 pixel) brandingHeaderEndRTL.gif (652*1 pixel) brandingHeaderMidLTR.gif (652*1 pixel) brandingHeaderMidRTL.gif (652*1 pixel) |
| 4 | Navigation text | header.navigation.color |
| 5 | Go button | header.go.font.color header.go.background.color header.go.border.color |
| 6 | Username text | splash.username.color |
| 7 | Password text | splash.password.color |
| 8 | Reset button | splash.reset.text.color splash.reset.back.ground.color |
| 9 | Bottom background color – right | splash.hexcode.3 |
| 10 | Login Button | splash.login.text.color splash.login.back.ground.color |
| 11 | Bottom background color – left | splash.hex.code.2 |
| 12 | Banner | splash.hex.code.1 |
| 13 | User text (for example, 'admin') | header.admin.color |
| 14 | Search Documentation, About and Signout text | header.hover.link.color |
| 15 | Unity Connection Administration text heading | splash.header.color |
| 16 | System Version text | splash.version.color |

| Note | To add your logo to Web Inbox and Mini Inbox, save your company logo as a 44*25 pixel image with the following filename: |
|---|---|

| Branding Option | Folder Structure |
|---|---|
| Single Header Option | If you
                                                   						want a single image for the header background (callout item 3), your branding
                                                   						folder must contain the following subfolders and image files: Branding (folder)
           ccmadmin (folder)
              BrandingProperties.properties (properties file)
              brandingHeader.gif (652*1 pixel image)
              ciscoLogo12pxMargin.gif (44*44 pixel image)
           branding_logo.png (44*25 pixel image) |

| Branding Option | Folder Structure |
|---|---|
| Graded Header Option | If you
                                                   						want to create a graded image for the header background, you need six separate
                                                   						image files to create the graded effect. Your branding folder must contain
                                                   						these subfolders and files Branding(folder)
           ccmadmin (folder)
               BrandingProperties.properties (file)
               brandingHeaderBegLTR.gif (652*1 pixel image)
               brandingHeaderBegRTL.gif (652*1 pixel image)
               brandingHeaderEndLTR.gif (652*1 pixel image)
               brandingHeaderEndRTL.gif (652*1 pixel image)
               brandingHeaderMidLTR.gif (652*1 pixel image)
               brandingHeaderMidRTL.gif (652*1 pixel image)
               ciscoLogo12pxMargin.gif (44*44 pixel image)
           branding_logo.png (44*25 pixel image) |