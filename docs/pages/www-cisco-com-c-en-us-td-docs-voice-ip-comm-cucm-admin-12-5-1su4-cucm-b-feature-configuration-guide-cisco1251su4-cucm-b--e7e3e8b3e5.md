---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-feature-configuration-guide-cisco1251su4-cucm-b--e7e3e8b3e5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_feature-configuration-guide-cisco1251su4/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0101101.html
retrieved_at: 2026-08-16T17:00:45.208195+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: July 31, 2025

Chapter: Branding Customizations

## Chapter: Branding Customizations

# Branding Customizations

## Branding Overview

The Branding feature lets you upload customized branding for Cisco Unified Communications Manager. Branding gets applied to
                              the Cisco Unified CM Administration login and configuration windows. Among the items that you can modify include:

Company logos

Background colors

Border colors

Font colors

### Append Logo in Self Care Portal

The Branding feature allows you to append your company logo to the Unified Communications Self Care Portal login page and
                              to the user interface header. You must include the branding_logo.png file in your branding.zip file and upload the zip file into Cisco Unified Communications Manager. The logo displays in the Self Care Portal after you
                              enable branding in Cisco Unified Communications Manager.

There is no option to customize background colors or fonts for the Self-Care portal.

## Branding Prerequisites

You must create your branding.zip file that contains the specified folder structure and files. For details, see Branding File Requirements .

## Branding Task
                        	 Flow

### Before you begin

Review Branding Prerequisites

Step 1

Configure your
                                       			 branding settings using one of these procedures:

- Enable Branding

- Disable Branding

Apply branding
                                          				across the Cisco Unified Communications Manager cluster.

Step 2

Restart the Tomcat Service

You must
                                          				restart the Cisco Tomcat service for the new branding setting to get picked up
                                          				by the Unified Communications Self-Care Portal.

### Enable Branding

Use this procedure to enable branding customization for Unified Communications Manager . Branding updates appear even if the system is enabled for SAML Single Sign-On.

#### Before you begin

Prepare your branding.zip file and save it in a location that Unified Communications Manager can access.

Step 1

Log in to Cisco Unified OS Administration.

Step 2

Choose Software Upgrades > Branding .

Step 3

Browse to your remote server and select the branding.zip file.

Step 4

Click Upload File .

Step 5

Click Enable Branding .

You can also enable branding by running the utils branding enable CLI command.

Step 6

Refresh your browser.

Step 7

Repeat this procedure on all Cisco Unified Communications Manager cluster nodes.

If you want to append your company logo to the Self-Care Portal user interface, see Restart the Tomcat Service .

### Disable Branding

Use this procedure to disable branding in your Cisco Unified Communications Manager cluster. You also need to disable branding
                                 if you want to remove your company logo from the Self-Care Portal.

Step 1

Log in to Cisco Unified OS Administration.

Step 2

Choose Software Upgrades > Branding .

Step 3

Click Disable Branding .

You can also disable branding by running the utils branding disable CLI command.

Step 4

Refresh your browser.

Step 5

Repeat this procedure on all Cisco Unified Communications Manager cluster nodes.

If you want to remove your company logo from the Self-Care Portal user interface, see Restart the Tomcat Service

### Restart the Tomcat Service

#### Before you begin

To append your logo to the Self-Care Portal, you must first enable branding in Cisco Unified Communications Manager. The branding.zip upload file must include a 44x25 pixel branding_logo.png file with your company logo. For details, Enable Branding .

To remove your  logo from the Self-Care Portal, you must disable branding in Cisco Unified Communications Manager. For details, Disable Branding .

Step 1

Log in to the Command Line Interface.

Step 2

Run the utils service restart Cisco Tomcat CLI command.

Step 3

Repeat this procedure on all Cisco Unified Communications Manager cluster nodes.

#### What to do next

## Branding File Requirements

Before you apply customized branding to your system, create your branding.zip file according to the prescribed specifications. On a remote server, create a Branding folder and fill the folder with the specified contents. Once you have added all the image files and subfolders, zip the entire
                              folder and save the file as branding.zip .

There are two options for the folder structure, depending on whether you want to use a single image for the header or a combination
                              of six images in order to create a graded effect for the header.

Branding Option

Folder Structure

Single Header Option

If you want a single image for the header background (callout item 3), your branding folder must contain the following subfolders
                                          and image files:

```
Branding (folder)
   ccmadmin (folder)
      BrandingProperties.properties (properties file)
      brandingHeader.gif (2048*1 pixel image)
      ciscoLogo12pxMargin.gif (44*44 pixel image)
   branding_logo.png (44*25 pixel image)
```

Graded Header Option

If you want to create a graded image for the header background, you need six separate image files to create the graded effect.
                                          Your branding folder must contain these subfolders and files

```
Branding(folder)
   ccmadmin (folder)
      BrandingProperties.properties (file)
      brandingHeaderBegLTR.gif (652*1 pixel image)
      brandingHeaderBegRTR.gif (652*1 pixel image)
      brandingHeaderEndLTR.gif (652*1 pixel image)
      brandingHeaderEndRTR.gif (652*1 pixel image)
      brandingHeaderMidLTR.gif (652*1 pixel image)
      brandingHeaderMidRTR.gif (652*1 pixel image)
      ciscoLogo12pxMargin.gif (44*44 pixel image)
   branding_logo.png (44*25 pixel image)
```

### User Interface Branding Options

The following images display the customization options for the Cisco Unified CM Administration user interface:

The following table describes the callout options.

Item

Description

Branding edits

1

Company Logo

To add your logo to Cisco Unified Communications Manager, save your company logo as a 44x44 pixel image with the following
                                          filename:

ciscoLogo12pxMargin.gif (44*44 pixels)

If you also want to append your logo to the header and login screen of the Self-Care Portal, you should also save your logo
                                                      as the 44x25 pixel branding_logo.png file.

2

Unified CM Administration header font color

heading.heading.color

3

Header Background

You can use a single image or a combination of six images to create a grading effect.

Single Image option —Save your header background as a single image:

brandingHeader.gif (2048*1 pixel)

Graded background option: —Save your header background as six images for a graded effect:

brandingHeaderBegLTR.gif (652*1 pixel)

brandingHeaderBegRTR.gif (652*1 pixel)

brandingHeaderEndLTR.gif (652*1 pixel)

brandingHeaderEndRTR.gif (652*1 pixel)

brandingHeaderMidLTR.gif (652*1 pixel)

brandingHeaderMidRTR.gif (652*1 pixel)

4

Navigation text

header.navigation.color

5

Go button

header.go.font.color

header.go.background.color

header.go.border.color

6

Username text

splash.username.color

7

Password text

splash.password.color

8

Login button

splash.login.text.color

splash.login.back.ground.color

9

Reset button

splash.reset.text.color

splash.reset.back.ground.color

10

Bottom background color – right

splash.hex.code.3

11

Bottom background color – left

splash.hex.code.2

12

Banner

splash.hex.code.1

Item

Description

Branding edits

13

User text (for example, 'admin')

header.admin.color

14

Search, About and Login text

header.hover.link.color

15

Unified CM Administration text heading

splash.header.color

16

System Version, VMware Installation text

splash.reset.text.color

splash.version.color

### Branding Properties Editing Example

Branding properties can be edited by adding the hex code in the properties file ( BrandingProperties.properties ). The properties file uses HTML-based hex code. For example, if you want to change the color of the Navigation text item
                              (callout item #4) to red, add the following code to your properties file:

```
header.navigation.color="#FF0000"
```

In this code, header.navigation.color is the branding property that you want to edit, and "#FF0000" is the new setting (red).

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure your
                                       			 branding settings using one of these procedures: Enable Branding Disable Branding | Apply branding
                                          				across the Cisco Unified Communications Manager cluster. |
| Step 2 | Restart the Tomcat Service | You must
                                          				restart the Cisco Tomcat service for the new branding setting to get picked up
                                          				by the Unified Communications Self-Care Portal. |

| Note | To enable branding, you must use the primary administrator account with privilege level 4 access. This is the main administrator
                                          account that is created during installation. |
|---|---|

| Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                          using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |
|---|---|

| Step 1 | Log in to Cisco Unified OS Administration. |
|---|---|
| Step 2 | Choose Software Upgrades > Branding . |
| Step 3 | Browse to your remote server and select the branding.zip file. |
| Step 4 | Click Upload File . |
| Step 5 | Click Enable Branding . Note You can also enable branding by running the utils branding enable CLI command. | Note | You can also enable branding by running the utils branding enable CLI command. |
| Note | You can also enable branding by running the utils branding enable CLI command. |
| Step 6 | Refresh your browser. |
| Step 7 | Repeat this procedure on all Cisco Unified Communications Manager cluster nodes. If you want to append your company logo to the Self-Care Portal user interface, see Restart the Tomcat Service . |

| Note | You can also enable branding by running the utils branding enable CLI command. |
|---|---|

| Note | To disable branding, you must use the primary administrator account with privilege level 4 access. This is the main administrator
                                          account that is created during installation. |
|---|---|

| Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                          using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |
|---|---|

| Step 1 | Log in to Cisco Unified OS Administration. |
|---|---|
| Step 2 | Choose Software Upgrades > Branding . |
| Step 3 | Click Disable Branding . Note You can also disable branding by running the utils branding disable CLI command. | Note | You can also disable branding by running the utils branding disable CLI command. |
| Note | You can also disable branding by running the utils branding disable CLI command. |
| Step 4 | Refresh your browser. |
| Step 5 | Repeat this procedure on all Cisco Unified Communications Manager cluster nodes. If you want to remove your company logo from the Self-Care Portal user interface, see Restart the Tomcat Service |

| Note | You can also disable branding by running the utils branding disable CLI command. |
|---|---|

| Step 1 | Log in to the Command Line Interface. |
|---|---|
| Step 2 | Run the utils service restart Cisco Tomcat CLI command. |
| Step 3 | Repeat this procedure on all Cisco Unified Communications Manager cluster nodes. |

| Branding Option | Folder Structure |
|---|---|
| Single Header Option | If you want a single image for the header background (callout item 3), your branding folder must contain the following subfolders
                                          and image files: Branding (folder)
   ccmadmin (folder)
      BrandingProperties.properties (properties file)
      brandingHeader.gif (2048*1 pixel image)
      ciscoLogo12pxMargin.gif (44*44 pixel image)
   branding_logo.png (44*25 pixel image) |
| Graded Header Option | If you want to create a graded image for the header background, you need six separate image files to create the graded effect.
                                          Your branding folder must contain these subfolders and files Branding(folder)
   ccmadmin (folder)
      BrandingProperties.properties (file)
      brandingHeaderBegLTR.gif (652*1 pixel image)
      brandingHeaderBegRTR.gif (652*1 pixel image)
      brandingHeaderEndLTR.gif (652*1 pixel image)
      brandingHeaderEndRTR.gif (652*1 pixel image)
      brandingHeaderMidLTR.gif (652*1 pixel image)
      brandingHeaderMidRTR.gif (652*1 pixel image)
      ciscoLogo12pxMargin.gif (44*44 pixel image)
   branding_logo.png (44*25 pixel image) |

| Item | Description | Branding edits |
|---|---|---|
| 1 | Company Logo | To add your logo to Cisco Unified Communications Manager, save your company logo as a 44x44 pixel image with the following
                                          filename: ciscoLogo12pxMargin.gif (44*44 pixels) Note If you also want to append your logo to the header and login screen of the Self-Care Portal, you should also save your logo
                                                      as the 44x25 pixel branding_logo.png file. | Note | If you also want to append your logo to the header and login screen of the Self-Care Portal, you should also save your logo
                                                      as the 44x25 pixel branding_logo.png file. |
| Note | If you also want to append your logo to the header and login screen of the Self-Care Portal, you should also save your logo
                                                      as the 44x25 pixel branding_logo.png file. |
| 2 | Unified CM Administration header font color | heading.heading.color |
| 3 | Header Background | You can use a single image or a combination of six images to create a grading effect. Single Image option —Save your header background as a single image: brandingHeader.gif (2048*1 pixel) Graded background option: —Save your header background as six images for a graded effect: brandingHeaderBegLTR.gif (652*1 pixel) brandingHeaderBegRTR.gif (652*1 pixel) brandingHeaderEndLTR.gif (652*1 pixel) brandingHeaderEndRTR.gif (652*1 pixel) brandingHeaderMidLTR.gif (652*1 pixel) brandingHeaderMidRTR.gif (652*1 pixel) |
| 4 | Navigation text | header.navigation.color |
| 5 | Go button | header.go.font.color header.go.background.color header.go.border.color |
| 6 | Username text | splash.username.color |
| 7 | Password text | splash.password.color |
| 8 | Login button | splash.login.text.color splash.login.back.ground.color |
| 9 | Reset button | splash.reset.text.color splash.reset.back.ground.color |
| 10 | Bottom background color – right | splash.hex.code.3 |
| 11 | Bottom background color – left | splash.hex.code.2 |
| 12 | Banner | splash.hex.code.1 |

| Note | If you also want to append your logo to the header and login screen of the Self-Care Portal, you should also save your logo
                                                      as the 44x25 pixel branding_logo.png file. |
|---|---|

| Item | Description | Branding edits |
|---|---|---|
| 13 | User text (for example, 'admin') | header.admin.color |
| 14 | Search, About and Login text | header.hover.link.color |
| 15 | Unified CM Administration text heading | splash.header.color |
| 16 | System Version, VMware Installation text | splash.reset.text.color splash.version.color |