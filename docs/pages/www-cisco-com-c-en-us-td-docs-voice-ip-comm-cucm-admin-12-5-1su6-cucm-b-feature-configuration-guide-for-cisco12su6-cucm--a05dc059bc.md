---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--a05dc059bc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0101111.html
retrieved_at: 2026-08-16T16:38:23.222708+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: Custom Phone Rings and Backgrounds

## Chapter: Custom Phone Rings and Backgrounds

# Custom Phone Rings and Backgrounds

## Custom Phone Rings
                        	 Overview

Custom Phone Rings
                              		  allows you to create customized phone rings and upload the customized files to
                              		  the Cisco Unified Communications Manager TFTP server where they can be accessed
                              		  by Cisco Unified IP Phones.

Cisco Unified IP Phones ship with default ring types that are implemented in hardware: Chirp1 and Chirp2. In addition, Cisco
                              Unified Communications Manager provides the capability of uploading the following files to phones:

Cisco Unified Communications Manager provides a default set of phone ring sounds that are implemented in software as pulse
                                    code modulation (PCM) audio files. Each PCM file specifies a single  ring type.

The Ringlist.xml file describes the list of ring options that are available for phones.

You can upload customized PCM audio files, such as custom ring tones and call back tones, as well as the modified Ringlist.xml
                              file to the TFTP directory in Cisco Unified Communications Manager.

## Custom Phone Rings Prerequisites

The following prerequisites apply to Custom Phone Rings:

In order to upload your custom phone rings, the Cisco TFTP service must be running.

Any PCM files that you want to upload must meet a set of file requirements in order to be compatible with Cisco Unified IP
                                    Phones. For details, review the topic PCM File Format Requirements .

The Ringlist.xml file must meet  a set of formatting guidelines. For details, review the topic Ringlist.xml File Format Requirements .

## Custom Phone
                        	 Rings Configuration Task Flow

### Before you begin

Review Custom Phone Rings Prerequisites

Step 1

Prepare Custom Phone Rings for Upload

Create your
                                          				customized PCM and Ringlist.xml files.

Step 2

Upload Custom Phone Rings to TFTP Server

Upload
                                          				customized files to the Cisco Unified Communications Manager TFTP server.

Step 3

Restart TFTP Service

After the
                                          				upload completes, restart the Cisco TFTP service.

### Prepare Custom Phone Rings for Upload

Step 1

Use the file get tftp <tftp path> CLI command to download the existing  Ringlist.xml file, in addition to any PCM files that you want to modify.

Step 2

Create a  PCM file for each ring type that you want to upload. For guidelines on PCM file compatibility with Cisco Unified
                                          Communications Manager, see PCM File Format Requirements .

Step 3

Use an ASCII editor to update the Ringlist.xml file with your new phone rings. For details on Ringlist.xml file formatting
                                          requirements, see Ringlist.xml File Format Requirements .

### Upload Custom Phone Rings to
                           	 TFTP Server

#### Before you begin

Prepare Custom Phone Rings for Upload

Step 1

From Cisco Unified OS Administration, choose Software Upgrades > TFTP > File Management .

Step 2

Click Upload
                                             				File .

Step 3

Click Browse and select the Ringlist.xml file, as well as any PCM files that you want to upload.

Step 4

Click Upload
                                             				File .

### Restart TFTP
                           	 Service

#### Before you begin

Upload Custom Phone Rings to TFTP Server

Step 1

Log in to
                                          			 Cisco Unified Serviceability and choose Tools > Control Center - Feature
                                                				  Services .

Step 2

From the Server drop-down list, choose the server on which the Cisco TFTP service is running.

Step 3

Click the
                                          			 radio button that corresponds to the Cisco
                                             				TFTP service.

Step 4

Click Restart .

### PCM File Format
                           	 Requirements

PCM files for phone
                                 		  rings must meet a set of requirements for proper playback on Cisco Unified
                                 		  IP Phones. When creating or modifying your PCM files, you can use any standard audio editing packages that support the
                                 following file format requirements:

- Raw PCM

- 8000 samples per second

- 8 bits per sample

- mu-law compression

- Maximum ring size: 16080
                                    			 samples

- Number of samples in the
                                    			 ring must be evenly divisible by 240

- Ring starts and ends at the
                                    			 zero crossing

### Ringlist.xml File
                           	 Format Requirements

The Ringlist.xml file defines an XML object that contains a list of phone ring types. Each ring type contains a pointer to
                                 the PCM file that is used for that ring type and the text that will display on the Ring Type menu on a Cisco Unified IP Phone for that ring.

The CiscoIPPhoneRinglist XML object uses the following simple tag set to describe the information:

```
<CiscoIPPhoneRinglist>   <Ring>
      <DisplayName/>
      <FileName/>
   </Ring>
</CiscoIPPhoneRinglist>
```

The following characteristics apply to the definition names:

DisplayName defines the name of the custom ring for the associated PCM file that will display on the Ring Type menu of the Cisco Unified IP Phone .

FileName specifies the name of the PCM file for the custom ring to associate with DisplayName.

Tip

The DisplayName and FileName fields must not exceed 25 characters.

The following example shows a Ringlist.xml file that defines two phone ring types:

```
<CiscoIPPhoneRinglist>   <Ring>
      <DisplayName>Analog Synth 1</DisplayName>
      <FileName>Analog1.raw</FileName>
   </Ring>
   <Ring>
      <DisplayName>Analog Synth 2</DisplayName>
      <FileName>Analog2.raw</FileName>
   </Ring>
</CiscoIPPhoneRinglist>
```

Tip

You must include the required DisplayName and FileName for each phone ring type. The Ringlist.xml file can include up to 50
                                             ring types.

## Custom Backgrounds

You can also use the TFTP server to upload new custom background
                              images to the phones in your network. Phone users can select the images that you upload as their phone backgrounds. You can
                              configure your system
                              so that phone users can select from an assortment of images or you can assign a specific background image for all phone.

If you want your phone users to be able to customize their phone backgrounds, then you must prepare and upload the
                              following files to the TFTP server whenever you upload new images:

Full-size background image—Refer to your phone documentation for image specifications, including the image size (in pixels)
                                    and color-type, for your phone model.

A thumbnail image—This is only required if you want your phone users to be able to choose their own background image. Refer
                                    to your phone documentation for the thumbnail image specifications

An edited List.xml file—This file contains a listing of the background images from which phone users can select. You must add your new images
                                    to this file.

If you want to assign a specific image for all phones then you need to upload the main background image only. In addition,
                              you also must update the Common Phone Profile to direct the phones to use the image that you assign.

## Custom Backgrounds Configuration Task Flow

Complete these tasks to configure and upload customized background images for the phones in your deployment.  You can configure
                              the system so that phone users can select from an assortment of images, or you can assign a specific background image that
                              displays on all phones.

Step 1

Create Phone Background Images

Create your full-size background image and corresponding thumbnail image (if required). Refer to your phone documentation
                                          for image specifications, including file type, image size (in pixels) and color-type.

The  thumbnail is not required if you are assigning a specific background image.

Step 2

Edit the List.xml file

Update the List.xml file from the appropriate TFTP directory with your new images. This is required so that phone users see the new images in
                                          their list of phone background options.

This procedure is required only if you are giving your users the option to choose their own background. If you are assigning
                                                      a specific background image then there is no need to edit this file.

Step 3

Upload Backgrounds to TFTP Server

Upload your files to the TFTP server.

Step 4

Restart the TFTP Server

Restart the Cisco TFTP service in order to push the images to your phones.

Step 5

Assign Phone Background for Phone Users

Optional. By default, Cisco Unified Communications Manager gives phone users the option to select their own phone background
                                          image. However, you can use the Common Phone Profile to assign a specific background image for all phones that use this Common
                                          Phone Profile.

### Create Phone Background Images

Refer to your phone documentation for background image specifications and thumbnail image specifications. This includes the
                                 image sizes (in pixels), file type, and the appropriate destination TFTP directory for that phone model (the TFTP directory
                                 is based on the image specifications).

If you want phone users to have the option to use, or not use, the image that you upload, you must prepare both a full-size
                                       image and a thumbnail image according to the specifications for that particular phone model.

If you want to assign the image to specific phones, you need the full-size image only.

#### What to do next

If you want phone users to be able to choose their own background image, Edit the List.xml file .

If you want to assign  a specific background image, you don't need to update the List.xml file. Proceed to Upload Backgrounds to TFTP Server

### Edit the List.xml file

If you want phone users to be able to choose their background images, use this procedure to add any new background images
                                 that you upload to the existing List.xml file. Each TFTP image directory contains a List.xml file that gets used by the phones that use that TFTP directory. This  file points to the specific background and
                                 thumbnail image for each background option and can include up to 50 background images. The images are listed using the
                                 order in which they appear on the phone. For each image, the file contains an <ImageItem> element that includes these two
                                 attributes:

Image: Uniform resource identifier (URI) that specifies where the phone obtains the thumbnail image that will appear on the
                                       Background Images menu of a phone.

URL: URI that specifies where the phone obtains the full size image.

Example:

The following example (for a Cisco Unified IP Phone 7971G-GE and 7970G) shows a List.xml file that defines two images. The required Image and URL attributes must be included for each image. The TFTP URI that displays
                                 in the example is the only supported method for linking to full size and thumbnail images as HTTP URL support is not provided.

```
<CiscoIPPhoneImageList>
   <ImageItem Image=”TFTP:Desktops/320x212x12/TN-Fountain.png” URL=”TFTP:Desktops/320x212x12/Fountain.png”/>  
   <ImageItem Image=”TFTP:Desktops/320x212x12/TN-FullMoon.png” URL=”TFTP:Desktops/320x212x12/FullMoon.png”/>
</CiscoIPPhoneImageList
```

Step 1

Log in to the Command Line Interface

Step 2

Run the file get tftp <filename> CLI command where <filename> represents the file and filepath of the List.xml file for the appropriate TFTP directory.

Make sure that you download the List.xml file from the appropriate TFTP directory as each image directory has its own file. Refer to your phone documentation for
                                                         information on the appropriate TFTP directory for that phone model as the directory is based on the image specifications.

Step 3

Edit the xml file with a new <ImageItem> element for each new background option that you want to add.

### Upload Backgrounds to TFTP Server

Use this procedure to upload new phone background files to the TFTP server.

If you want your phone users to be able to choose their own background image, then you must upload your full-size background
                                       image, a thumbnail image, and the updated List.xml file.

If you are assigning a specific background image, you need to upload the full-size background image only.

Step 1

From Cisco Unified OS Administration, choose Software Upgrades > TFTP File Management

Step 2

Click Upload File and do the following:

Click Choose File and select the background file that you want to upload.

In  the Directory field, enter the appropriate TFTP directory for that phone model. The TFTP directory corresponds to the image size and color
                                                type. Refer to your phone documentation for images specification.

Click Upload File

Repeat these steps to upload both the thumbnail image and list.xml files as well. These files should be loaded to the same TFTP directory as the main background image.

Step 3

Click Close .

### Restart the TFTP Server

After you have uploaded your custom files to the TFTP directory, restart the Cisco TFTP server to push the files to the phones.

Step 1

Log in to
                                          			 Cisco Unified Serviceability and choose Tools > Control Center - Feature
                                                				  Services .

Step 2

From the Server drop-down list, choose the server on which the Cisco TFTP service is running.

Step 3

Click the
                                          			 radio button that corresponds to the Cisco
                                             				TFTP service.

Step 4

Click Restart .

### Assign Phone Background for Phone Users

By default, Cisco Unified Communications Manager allows phone users to customize their own phone background image. However,
                                 you can use the Common Phone Profile setting to assign a specific background image for all phones that use this Common Phone
                                 Profile.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Common Phone Profile .

Step 2

Do one of the following:

- Click Find and select the Common Phone Profile that your phones use.

- Click Add New to create a new Common Phone Profile.

Step 3

If  you want users to be able to choose their background image, make sure that the Enable End User Access to Phone Background Image Setting check box is checked (this is the default setting).

Step 4

If you want to assign a specific background image for phones that use this profile:

- Uncheck the Enable End User Access to Phone Background Image Setting check box.

- In  the Background Image text box, enter the filename of the image file that you want to assign. Also,  check the Override Enterprise Settings check box that corresponds to this text box.

Step 5

Complete any remaining fields in the Common Phone Profile window. For help with the fields and their settings, refer to the online help.

Step 6

Click Save .

#### What to do next

If you have created a new Common Phone Profile, reconfigure your phones so that they use this profile. For details on how
                                 to configure
                                 phones in Cisco Unified Communications Manager, see the "Configure Endpoint Devices" section of the System Configuration Guide for Cisco Unified Communications Manager .

Tip

After you complete your configuration, reset your phones.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Prepare Custom Phone Rings for Upload | Create your
                                          				customized PCM and Ringlist.xml files. |
| Step 2 | Upload Custom Phone Rings to TFTP Server | Upload
                                          				customized files to the Cisco Unified Communications Manager TFTP server. |
| Step 3 | Restart TFTP Service | After the
                                          				upload completes, restart the Cisco TFTP service. |

| Step 1 | Use the file get tftp <tftp path> CLI command to download the existing  Ringlist.xml file, in addition to any PCM files that you want to modify. |
|---|---|
| Step 2 | Create a  PCM file for each ring type that you want to upload. For guidelines on PCM file compatibility with Cisco Unified
                                          Communications Manager, see PCM File Format Requirements . |
| Step 3 | Use an ASCII editor to update the Ringlist.xml file with your new phone rings. For details on Ringlist.xml file formatting
                                          requirements, see Ringlist.xml File Format Requirements . |

| Step 1 | From Cisco Unified OS Administration, choose Software Upgrades > TFTP > File Management . |
|---|---|
| Step 2 | Click Upload
                                             				File . |
| Step 3 | Click Browse and select the Ringlist.xml file, as well as any PCM files that you want to upload. |
| Step 4 | Click Upload
                                             				File . |

| Step 1 | Log in to
                                          			 Cisco Unified Serviceability and choose Tools > Control Center - Feature
                                                				  Services . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which the Cisco TFTP service is running. |
| Step 3 | Click the
                                          			 radio button that corresponds to the Cisco
                                             				TFTP service. |
| Step 4 | Click Restart . |

| Tip | The DisplayName and FileName fields must not exceed 25 characters. |
|---|---|

| Tip | You must include the required DisplayName and FileName for each phone ring type. The Ringlist.xml file can include up to 50
                                             ring types. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create Phone Background Images | Create your full-size background image and corresponding thumbnail image (if required). Refer to your phone documentation
                                          for image specifications, including file type, image size (in pixels) and color-type. Note The  thumbnail is not required if you are assigning a specific background image. | Note | The  thumbnail is not required if you are assigning a specific background image. |
| Note | The  thumbnail is not required if you are assigning a specific background image. |
| Step 2 | Edit the List.xml file | Update the List.xml file from the appropriate TFTP directory with your new images. This is required so that phone users see the new images in
                                          their list of phone background options. Note This procedure is required only if you are giving your users the option to choose their own background. If you are assigning
                                                      a specific background image then there is no need to edit this file. | Note | This procedure is required only if you are giving your users the option to choose their own background. If you are assigning
                                                      a specific background image then there is no need to edit this file. |
| Note | This procedure is required only if you are giving your users the option to choose their own background. If you are assigning
                                                      a specific background image then there is no need to edit this file. |
| Step 3 | Upload Backgrounds to TFTP Server | Upload your files to the TFTP server. |
| Step 4 | Restart the TFTP Server | Restart the Cisco TFTP service in order to push the images to your phones. |
| Step 5 | Assign Phone Background for Phone Users | Optional. By default, Cisco Unified Communications Manager gives phone users the option to select their own phone background
                                          image. However, you can use the Common Phone Profile to assign a specific background image for all phones that use this Common
                                          Phone Profile. |

| Note | The  thumbnail is not required if you are assigning a specific background image. |
|---|---|

| Note | This procedure is required only if you are giving your users the option to choose their own background. If you are assigning
                                                      a specific background image then there is no need to edit this file. |
|---|---|

| Step 1 | Log in to the Command Line Interface |
|---|---|
| Step 2 | Run the file get tftp <filename> CLI command where <filename> represents the file and filepath of the List.xml file for the appropriate TFTP directory. Note Make sure that you download the List.xml file from the appropriate TFTP directory as each image directory has its own file. Refer to your phone documentation for
                                                         information on the appropriate TFTP directory for that phone model as the directory is based on the image specifications. | Note | Make sure that you download the List.xml file from the appropriate TFTP directory as each image directory has its own file. Refer to your phone documentation for
                                                         information on the appropriate TFTP directory for that phone model as the directory is based on the image specifications. |
| Note | Make sure that you download the List.xml file from the appropriate TFTP directory as each image directory has its own file. Refer to your phone documentation for
                                                         information on the appropriate TFTP directory for that phone model as the directory is based on the image specifications. |
| Step 3 | Edit the xml file with a new <ImageItem> element for each new background option that you want to add. |

| Note | Make sure that you download the List.xml file from the appropriate TFTP directory as each image directory has its own file. Refer to your phone documentation for
                                                         information on the appropriate TFTP directory for that phone model as the directory is based on the image specifications. |
|---|---|

| Step 1 | From Cisco Unified OS Administration, choose Software Upgrades > TFTP File Management |
|---|---|
| Step 2 | Click Upload File and do the following: Click Choose File and select the background file that you want to upload. In  the Directory field, enter the appropriate TFTP directory for that phone model. The TFTP directory corresponds to the image size and color
                                                type. Refer to your phone documentation for images specification. Click Upload File Repeat these steps to upload both the thumbnail image and list.xml files as well. These files should be loaded to the same TFTP directory as the main background image. |
| Step 3 | Click Close . |

| Step 1 | Log in to
                                          			 Cisco Unified Serviceability and choose Tools > Control Center - Feature
                                                				  Services . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which the Cisco TFTP service is running. |
| Step 3 | Click the
                                          			 radio button that corresponds to the Cisco
                                             				TFTP service. |
| Step 4 | Click Restart . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Common Phone Profile . |
|---|---|
| Step 2 | Do one of the following: Click Find and select the Common Phone Profile that your phones use. Click Add New to create a new Common Phone Profile. |
| Step 3 | If  you want users to be able to choose their background image, make sure that the Enable End User Access to Phone Background Image Setting check box is checked (this is the default setting). |
| Step 4 | If you want to assign a specific background image for phones that use this profile: Uncheck the Enable End User Access to Phone Background Image Setting check box. In  the Background Image text box, enter the filename of the image file that you want to assign. Also,  check the Override Enterprise Settings check box that corresponds to this text box. |
| Step 5 | Complete any remaining fields in the Common Phone Profile window. For help with the fields and their settings, refer to the online help. |
| Step 6 | Click Save . If you have assigned a specific background image, all phones that use this Common Phone Profile will use the image that you
                                          specify. |

| Tip | If you have a large number of phones to assign, use the Bulk
                                          Administration Tool to assign a Common Phone Profile to a large number of phones in a
                                          single operation. For details, see the Bulk Administration Guide
                                             for Cisco Unified Communications Manager . |
|---|---|

| Note | After you complete your configuration, reset your phones. |
|---|---|