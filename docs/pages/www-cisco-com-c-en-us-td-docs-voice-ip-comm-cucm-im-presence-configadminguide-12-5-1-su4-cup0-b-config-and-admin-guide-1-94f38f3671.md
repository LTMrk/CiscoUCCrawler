---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-su4-cup0-b-config-and-admin-guide-1-94f38f3671
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1_su4/cup0_b_config-and-admin-guide-1251su4/cup0_b_config-and-admin-guide-1251su3_chapter_010100.html
retrieved_at: 2026-08-16T16:46:01.235219+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU4 to 12.5(1)SU7

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU4 to 12.5(1)SU7

Updated: November 27, 2024

Chapter: Branding Customizations

## Chapter: Branding Customizations

# Branding Customizations

## Branding Overview

The Branding feature lets you apply customized branding for the IM and Presence Service. The branding customizations display
                              in the Cisco Unified CM IM and Presence Administration login and configuration windows. Among the items that you can add or
                              modify include:

Company logos

Background colors

Border colors

Font colors

## Branding Prerequisites

You must create a branding zip file with the prescribed folder structure and files. For details, see Branding File Requirements .

## Enable Branding

Use this procedure to enable branding customizations for the IM and Presence Service cluster. Branding updates display even
                              if you have SAML SSO enabled.

To enable branding, you must use the primary administrator account with privilege level 4 access. This is the main administrator
                                          account that is created during installation.

Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                          using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly.

### Before you begin

Save the branding.zip file with your IM and Presence customizations in a location that the IM and Presence Service can access.

Step 1

Log in to Cisco Unified IM and Presence OS Administration.

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

Refresh your browser to see the changes.

Step 7

Repeat this procedure on all IM and Presence Service cluster nodes.

## Disable Branding

To disable branding, you must use the master administrator account with privilege level 4 access. This is the main administrator
                                          account that is created during installation.

Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                          using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly.

Step 1

Log in to Cisco Unified IM and Presence OS Administration.

Step 2

Choose Software Upgrades > Branding .

Step 3

Click Disable Branding .

You can also disable branding by running the utils branding disable CLI command.

Step 4

Refresh your browser to see the changes.

Step 5

Repeat this procedure on all IM and Presence Service cluster nodes.

## Branding File Requirements

Before you apply customized branding to your system, create your branding.zip file according to the specifications. On a remote server, create a Branding folder and fill the folder with the specified contents. Once you have added all the image files and subfolders, zip the entire
                              folder and save the file as branding.zip .

There are two options for the folder structure, depending on whether you want to use a single image for the header, or a combination
                              of six images in order to create a graded effect for the header.

Branding Option

Folder Structure

Single Header Option

If you want a single image for the header background (callout item 3), your branding folder must contain the following subfolders
                                          and image files:

```
Branding (folder)
   cup (folder)
      BrandingProperties.properties (properties file)
      brandingHeader.gif (652*1 pixel)
      ciscoLogo12pxMargin.gif (44*44 pixel)
```

Graded Header Option

If you want to create a graded image for the header background (callout item 3, 4, 5), you need six separate image files to
                                          create the graded effect. Your branding folder must contain these subfolders and files

```
Branding(folder)
   cup (folder)
      BrandingProperties.properties (file)
      brandingHeaderBegLTR.gif (652*1 pixel image)
      brandingHeaderBegRTR.gif (652*1 pixel image)
      brandingHeaderEndLTR.gif (652*1 pixel image)
      brandingHeaderEndRTR.gif (652*1 pixel image)
      brandingHeaderMidLTR.gif (652*1 pixel image)
      brandingHeaderMidRTR.gif (652*1 pixel image)
      ciscoLogo12pxMargin.gif (44*44 pixel image)
```

### User Interface Branding Options

The following images display the branding options for the Cisco Unified CM IM and Presence Administration user interface.

The following table describes how the callout items in the above screen captures can be customized.

Item

Description

Branding Edits

Login Screen Image

1

Company Logo

To add your logo to the IM and Presence Service interface, save your company logo as a 44x44 pixel image with the following
                                          filename:

ciscoLogo12pxMargin.gif (44*44 pixels)

2

Unified CM IM and Presence Administration text in header

header.heading.color

3

Header Background (Graded option - left)

If you want to have a graded effect for the header image, use the following images for the left side.

brandingHeaderBegLTR.gif (652 x 1 pixel)

brandingHeaderBegLTR.gif (652 x 1 pixel)

4

Header Background

If you want to use a single image for the header:

brandingHeader.gif (652 x 1 pixel)

Otherwise, if you are creating a header with a graded effect, use the following images:

brandingHeaderMidLTR.gif (652 x 1 pixel)

brandingHeaderMidRTR.gif (652 x 1 pixel)

5

Header Background (Graded option - right)

If you want to use a graded effect for the header, use this image for the right header:

brandingHeaderEndLTR (652 x 1 pixel)

brandingHeaderEndRTR (652 x 1 pixel)

6

Navigation text

header.navigation.color

7

Go button

header.go.font.color

header.go.background.color

8

Username and Password text

splash.loginfield.color

9

Login and Reset buttons

splash.button.text.color

splash.button.color

10

Bottom background color – right

splash.hex.code.3

11

Bottom background color – left

splash.hex.code.2

12

Banner

splash.hex.code.1

Post Login Image

13

Logged in user text (for example, the 'admin' user)

header.text.bold.color

14

Search, About, Logout links

header.link.color

15

Link divider

header.divider.color

16

Unified CM IM and Presence Administration text in banner (post-login)

splash.login.text.color

17

System version and VMware Installation text

splash.version.color

### Branding Properties Editing Example

Branding properties can be edited by adding the hex code in the properties file ( BrandingProperties.properties ). The properties file uses HTML-based hex code. For example, if you want to change the color of the Navigation text item
                              (callout item #6) to red, add the following code to your properties file:

header.navigation.color="#FF0000"

In this code, header.navigation.color is the branding property that you want to edit, and "#FF0000" is the new setting (red).

| Note | To enable branding, you must use the primary administrator account with privilege level 4 access. This is the main administrator
                                          account that is created during installation. |
|---|---|

| Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                          using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |
|---|---|

| Step 1 | Log in to Cisco Unified IM and Presence OS Administration. |
|---|---|
| Step 2 | Choose Software Upgrades > Branding . |
| Step 3 | Browse to your remote server and select the branding.zip file. |
| Step 4 | Click Upload File . |
| Step 5 | Click Enable Branding . Note You can also enable branding by running the utils branding enable CLI command. | Note | You can also enable branding by running the utils branding enable CLI command. |
| Note | You can also enable branding by running the utils branding enable CLI command. |
| Step 6 | Refresh your browser to see the changes. |
| Step 7 | Repeat this procedure on all IM and Presence Service cluster nodes. |

| Note | You can also enable branding by running the utils branding enable CLI command. |
|---|---|

| Note | To disable branding, you must use the master administrator account with privilege level 4 access. This is the main administrator
                                          account that is created during installation. |
|---|---|

| Note | Ensure that you use only one among GUI and CLI to enable branding as well as to disable it. For example, if you enable branding
                                          using the GUI interface, you must use the GUI interface itself to disable branding. Else, it will not function properly. |
|---|---|

| Step 1 | Log in to Cisco Unified IM and Presence OS Administration. |
|---|---|
| Step 2 | Choose Software Upgrades > Branding . |
| Step 3 | Click Disable Branding . Note You can also disable branding by running the utils branding disable CLI command. | Note | You can also disable branding by running the utils branding disable CLI command. |
| Note | You can also disable branding by running the utils branding disable CLI command. |
| Step 4 | Refresh your browser to see the changes. |
| Step 5 | Repeat this procedure on all IM and Presence Service cluster nodes. |

| Note | You can also disable branding by running the utils branding disable CLI command. |
|---|---|

| Branding Option | Folder Structure |
|---|---|
| Single Header Option | If you want a single image for the header background (callout item 3), your branding folder must contain the following subfolders
                                          and image files: Branding (folder)
   cup (folder)
      BrandingProperties.properties (properties file)
      brandingHeader.gif (652*1 pixel)
      ciscoLogo12pxMargin.gif (44*44 pixel) |
| Graded Header Option | If you want to create a graded image for the header background (callout item 3, 4, 5), you need six separate image files to
                                          create the graded effect. Your branding folder must contain these subfolders and files Branding(folder)
   cup (folder)
      BrandingProperties.properties (file)
      brandingHeaderBegLTR.gif (652*1 pixel image)
      brandingHeaderBegRTR.gif (652*1 pixel image)
      brandingHeaderEndLTR.gif (652*1 pixel image)
      brandingHeaderEndRTR.gif (652*1 pixel image)
      brandingHeaderMidLTR.gif (652*1 pixel image)
      brandingHeaderMidRTR.gif (652*1 pixel image)
      ciscoLogo12pxMargin.gif (44*44 pixel image) |

| Item | Description | Branding Edits |
|---|---|---|
| Login Screen Image |
| 1 | Company Logo | To add your logo to the IM and Presence Service interface, save your company logo as a 44x44 pixel image with the following
                                          filename: ciscoLogo12pxMargin.gif (44*44 pixels) |
| 2 | Unified CM IM and Presence Administration text in header | header.heading.color |
| 3 | Header Background (Graded option - left) | If you want to have a graded effect for the header image, use the following images for the left side. brandingHeaderBegLTR.gif (652 x 1 pixel) brandingHeaderBegLTR.gif (652 x 1 pixel) |
| 4 | Header Background | If you want to use a single image for the header: brandingHeader.gif (652 x 1 pixel) Otherwise, if you are creating a header with a graded effect, use the following images: brandingHeaderMidLTR.gif (652 x 1 pixel) brandingHeaderMidRTR.gif (652 x 1 pixel) |
| 5 | Header Background (Graded option - right) | If you want to use a graded effect for the header, use this image for the right header: brandingHeaderEndLTR (652 x 1 pixel) brandingHeaderEndRTR (652 x 1 pixel) |
| 6 | Navigation text | header.navigation.color |
| 7 | Go button | header.go.font.color header.go.background.color |
| 8 | Username and Password text | splash.loginfield.color |
| 9 | Login and Reset buttons | splash.button.text.color splash.button.color |
| 10 | Bottom background color – right | splash.hex.code.3 |
| 11 | Bottom background color – left | splash.hex.code.2 |
| 12 | Banner | splash.hex.code.1 |
| Post Login Image |
| 13 | Logged in user text (for example, the 'admin' user) | header.text.bold.color |
| 14 | Search, About, Logout links | header.link.color |
| 15 | Link divider | header.divider.color |
| 16 | Unified CM IM and Presence Administration text in banner (post-login) | splash.login.text.color |
| 17 | System version and VMware Installation text | splash.version.color |