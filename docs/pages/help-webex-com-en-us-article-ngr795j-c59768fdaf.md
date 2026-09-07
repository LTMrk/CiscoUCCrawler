---
doc_id: help-webex-com-en-us-article-ngr795j-c59768fdaf
source_url: https://help.webex.com/en-us/article/ngr795j
retrieved_at: 2026-09-07T13:04:10.188704+00:00
---

## Key Expansion Module overview

Each Cisco Desk Phone 9800 Key Expansion Module (KEM) The Cisco Desk Phone 9800 Key Expansion Module (KEM) supports 40 lines, with two
        pages of 20 buttons each.

You can use more than one expansion module per phone on the 9861 and 9871 models. But each
        module must be the same type. The following table lists the phones and the number of key
        expansion modules that each model supports.

Phone model

Supported total number of KEMs and lines

Cisco Desk Phone 9851

Supports 1 KEM and 46 lines (6 lines on phone)

Cisco Desk Phone 9861

Supports up to 3 KEMs and 130 lines (10 lines on phone)

Cisco Desk Phone 9871

Supports up to 3 KEMs and 124-128 lines, depending on configuration (4 or 8 lines
                  on phone screen)

When your 9861 and 9871 phones are powered over Ethernet (PoE), you can only connect one KEM to each phone. To connect two or three KEMs, use an adapter to power your phone from an electrical outlet.

The calling system that your phone is registered with restricts the maximum number of
              SIP lines available on the phone. The supported lines in the table above include both
              SIP lines and feature line keys (PLK).

## Key Expansion Module buttons and hardware

The following table describes the features of the key expansion module.

Each button corresponds to one line. The light of each button indicates the state
                  of the corresponding line as follows:

The light of button indicates the state of the corresponding line as
                  follows:

Light off—Line is idle or not configured.

Green steady—Line is in use.

Red steady—Shared line or monitored line is in use
                  remotely.

Red flashing—Line has calls on hold.

Amber blinking—Line has an incoming call.

The LEDs also reflect the status of the extended features assigned to the
                  buttons.

LCD screen—Displays the phone number, speed-dial number (or name or other text label), phone service, or phone feature assigned to each button.

Icons that indicate line status resemble (in both appearance and function) the icons on the phone to which the KEM is attached.

Shift buttons—2 buttons. The button for page 1 is labeled as 1 and the button for page 2 is labeled as 2. The lights in each button indicate the state of the page as follows:

Green steady LED—Page is in view.

Light off—Page is not in view.

Amber steady LED—Page is not in view with one or more alerting calls on the page.

## Install Key Expansion Module

Connect the Key Expansion Module (KEM) to the phone. Depending on the calling system that your phone is registered with, you may need to contact your administrator to enable the KEM before you can use it.

Remove the accessory connector cover.

Firmly press the USB connector attached to the module to the phone.

Fasten the screw into the phone.

After you firmly attach the module to the phone, the front screen of the phone and KEM appears as following.

An automatic upgrade will initiate if the firmware version on the KEM is lower than that on the phone. Wait until the update is complete.

## Configure speed dials on KEM

The line keys on the Key Expansion Module (KEM) function similarly to the line keys on the phone itself. Depending on your phone settings, you can configure idle line keys with speed dials.

For more information about how to configure and use speed dials on line keys, see Use speed dials on your phone .

## Change KEM screen settings

The wallpaper, color theme, and brightness settings on phone also apply to the KEM screen.

For information about how to adjust screen brightness and change the screen appearance, see Customize the phone screen settings .

## Administration for KEM

- On Control Hub

- On Unified CM

- On phone web page

If your Cisco Desk Phone 9800 Series is registered to Webex Calling, follow the information in this section to set up the line keys on the attached Key Expansion Modules.

Move additional lines to KEM (9871 only)

Cisco Desk Phone 9871 natively supports up to 32 virtual line keys on the touchscreen. When a KEM is attached, you can specify whether to retain 4 lines or
        8 lines on the phone, and move the additional lines to the KEM.

Before you begin

Connect your KEM to the the phone.

From the customer view in Control Hub , go to Devices , and then select your phone.

Select All configurations .

In the Att Console section, choose 4 or 8 for Maximum Lines On Phone With KEM .

By default, the field is set to 4 . The additional extension lines and feature lines are moved to the attached KEMs.

Select Next .

Review your changes and select Apply .

Select Close to close the page.

Configure KEM line keys

The KEM line keys can be configured as primary or shared lines, as well as feature keys.

Use the custom layout to individually customize the KEM line keys.

To help you customize your phone layout, the portal alerts you if the quantities on the device’s shared line list or your monitoring list don't match your active layout. The alerts are called advisories and appear just above the layout area. Advisories are informational messages only and don't prevent you from saving the layout that you create. You can clear advisories by either adding more PLK positions of the required type to your layout or by reducing the entries in the device’s shared line list or the user’s monitoring list.

Before you begin

Connect your KEM to the phone.

From the customer view in Control Hub , go to Devices , and then select your phone.

Under Device Management , select Configure Layout and then select Custom Layout .

Do one of the following action based on your phone model:

At the bottom of the page, select Configure KEM Keys .

Go to Step 4.

Choose one of the following options for each line key you'd like to modify:

Open —No value specified.

Primary line —Setting a primary line clears all extended line key functions like monitoring or speed dial values that may exist in a PLK from a previous configuration.

Shared / Virtual line —Shared Line Appearance (SLA) positions populate from the values set in configure lines. SLAs populate PLK positions to the layout from top-left to bottom-right. A warning displays if the number of SLA in the configure lines list exceeds the available shared line positions in the layout.

Monitored line —Monitoring (BLF) positions populate from the values set in the monitoring list. Monitoring entries populate the defined monitoring PLKs first followed by open PLKs. A warning displays if the number of monitoring entries in your monitoring list exceeds the available monitoring positions in the layout.

Speed dial —Speed dial entries require a name and destination extension, telephone number or SIP URI ( example@webex.com ). SIP URI destinations aren’t routable. Speed dials defined here aren’t customizable on the device.

- Closed —The key is disabled.

Select Save .

Configure line key labels

In Control Hub, you can choose a predefined number or name format to display as the line label for configured lines.

The configurations are also applicable for Key Expansion Module (KEM).

The following example shows the positions of the configurable line key labels:

It also supports the multiple appearances for a same line (suffixed with a -1, -2, and so on).

From the customer view in Control Hub , go to Devices , and then select your phone.

Ensure that the value of Line Label is set to default or empty.

Select Configure Lines in the Device Management section to access the Configured Lines page.

Clear the value of Line Label for the configured lines.

The parameter Line Label takes precedence over Line Key Label . If Line Label is
                configured, the phone will show the configured line label instead.

Click Save .

On the device details page, select All Configurations in the Configurations section.

In the Phone section, configure the parameters Display Name , Line Key Label , and Line Key Secondary Label .

For more information about the parameters, see Parameters for configurable line key labels on Control Hub .

Click Next , review your changes, and then click Apply .

#### Parameters for configurable line key labels on Control Hub

For
                        9841/9851: User Phone Number / Location Number / User Extension

For
                        9861/9871/8875: User Name (First Name Last Name)

Options:

- User Phone Number / Location Number / User Extension

- User Name (First Name Last Name)

- User Name (Last Name First Name)

For the option User Phone Number / Location Number / User Extension , the display priority is:

User Phone Number > Location Number > User Extension.

If  User Phone Number is empty, then the phone will display Location Number.
                  Meanwhile, if the Location Number is also empty, then the phone will display User
                  Extension.

If the actual values of "Display Name" and "Line Key Label" are identical, the secondary line label on the primary line doesn't display.

Options:

- User Extension / First Name

- User Name (First Name Last Name)

- User Name (Last Name First Name)

For the option User Extension / First Name , the display priority is:

User Extension > First Name

If  User Extension is empty, then the phone will display First Name.

If a line is configured with multiple appearances, the suffix (-1, -2, and so on) is appended to the Line Key Label.

Options:

- User Extension / First Name

- User Name (First Name Last Name)

- User Name (Last Name First Name)

- User Phone Number / Location Number / User Extension

- None

If the actual values of "Line Key Label" and "Line Key Secondary Label" are identical, the secondary label on the line key will only display the string "Line".

If  your Cisco Desk Phone 9800 Series is registered to Cisco Unified Communications Manager (Unified CM), follow the information in this section to set up the attached Key Expansion Modules.

Enable a KEM for the phone

Enable the KEMs that are attached to the phone on Cisco Unified CM Administration before your users can use them.

Before you begin

- Connect your KEM to your phone.

- Make sure the side USB port is enabled.

On Cisco Unified CM Administration, choose Device > Phone .

Click Find and use the filters to search for your phone.

Click the device name of your phone to open the Phone Configuration page.

In the Expansion Module Information section, choose your KEM in the module drop-down list.

By default, the fields are set to None . The module appears in the list only when it's connected to the phone.

Click Save .

Click Apply Config .

Move additional lines to KEM (9871 only)

Cisco Desk Phone 9871 natively supports up to 32 virtual line keys on the touchscreen. With three KEMs connected, it can support up to 124 or 128 lines depending on the Unified CM configurations. When a KEM is attached, you can specify whether to retain 4 lines or 8 lines on the phone, and move the additional lines to the KEM.

On Cisco Unified CM Administration, choose Device > Phone .

Click Find and use the filters to search for your phone.

Click the device name of your phone to open the Phone Configuration page.

In the Maximum lines on phone with KEM field, choose 4 or 8 .

By default, the field is set to 4 . The additional extension lines and feature lines are moved to the attached KEMs.

Click Save .

Click Apply Config .

Assign an extension number to a line key on KEM

The Key Expansion Module (KEM) line keys function similarly to the line keys on the phone itself. You can configure the KEM line keys following the same steps. When the number of lines exceeds the phone's maximum capacity, they extend to the attached KEMs.

You can use the phone button template to arrange the sequence of the extension lines and feature lines.

Cisco Unified Communications Manager (Unified CM) supports up to 126 SIP lines on a phone. If you have three KEMs attached to Cisco Desk Phone 9861 and 9871, keep the following limitation in mind:

- 9861 : Don't assign extension numbers to the last four line keys on the third KEM. Instead, you can add features on them.

- 9871 : Don't assign extension numbers to the last two line keys on the third KEM. Instead, you can add features on them.

On Cisco Unified CM Administration, choose Device > Phone .

Use the filters to find your phone to configure.

Click the device name of your phone to open the Phone Configuration page.

Click Line [n] - Add a new DN in the Association pane on the left.

In the Directory Number Configuration window, enter a dialable phone number in the Directory Number field.

(Optional) Select a partition in the Rout Partition field.

(Optional) Select a calling search space in the Calling Search Space field in the Directory Number Settings area.

Click Save .

Add features to KEM line keys

You can add the features listed in the following table to line keys on Cisco Desk Phone 9800 Series and their attached KEMs.

We recommend using a phone button template to configure KEM line keys. These templates work for both phones and KEMs, allowing additional lines beyond the phone's maximum to flow to the KEM line keys.

#### Configure feature line keys with a phone button template

You can use the Phone Button Template on Cisco Unified Communications Manager Administration to configure the feature line keys for different features. Each feature line key takes up
        a line position. You can change the order of the feature.

On Cisco Unified Communications Manager Administration, choose Device > Device Settings > Phone Button Template .

Click Find to display list of supported phone templates.

Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step.

Select a default template for the model of phone and click Copy .

In the Phone Button Template Information field, enter a new name for the template.

Click Save .

Perform the following steps if you want to add phone buttons to an existing template.

Click Find and enter the search criteria.

Choose an existing template.

From the Line drop-down list, choose feature that you want to add to the template.

Click Save .

Perform one of the following tasks:

- Click Apply
              Config if you modified a template that is already associated with devices
            to restart the devices.

- If you created a new button template, associate the template with the devices and then restart them.

#### Apply a button template to a phone

On Cisco Unified Communications Manager Administration, choose Device > Phone .

Click Find to display the list of configured phones.

Choose the phone to which you want to add the phone button template.

In the Phone Button Template drop-down list, choose the phone
          button template that contains the new feature button.

Click Save .

A message prompts for clicking Reset to update the phone
          settings.

Click Reset .

Apply the custom wallpaper and logo

The wallpaper and color theme on the phone screen also applies to the attached Key Expansion Modules (KEM). The logo displays only on the phone screen and does not appear on the KEM screen.

To deploy your custom wallpaper and logo to your phones, follow this workflow:

- Prepare your wallpaper and logo images

- Upload the images files to the TFTP server

- Create a general management file List.xml

- Upload the List.xml to the TFTP server

- Restart the TFTP server

- Configure the wallpaper settings on Cisco Unified Communications Manager Administration

See the following for procedures:

Prepare your wallpaper and logo images

To get the best experience, keep the following tips in mind when choosing or designing your images:

- Avoid using clustered images that can make it hard for you to identify phone lines on the home screen. Simplicity is key when selecting wallpapers.

- Ensure that your chosen wallpapers match your phone's color scheme. Opt for wallpapers that complement either the dark or light color palettes. Dark images are best suited for dark mode, while light images work well for light mode.

- Avoid using high contrast images as wallpapers. The extreme contrast can make it challenging to see the logo and other screen elements against the background.

- Avoid using dynamic images as wallpapers.

- The logo displays on the phone screen only, and it doesn't display on the KEM screen. When multiple lines are configured on Cisco Desk Phone 9841, 9851, and 9861, the logo and the logo setting in the Settings menu are unavailable.

- To use custom wallpaper on phones with Key Expansion Modules (KEM) attached, prepare both phone wallpaper and KEM wallpaper.

Cisco Desk Phone 9851: 190x125

Cisco Desk Phone 9861: 380x250

Cisco Desk Phone 9871: 494x325 / 418x275

Cisco Video Phone 8875: 380x250

You don't need to create a separate thumbnail image for the
                  logo. The system automatically scales the logo image to fit the dimensions of the
                  thumbnail.

Cisco Desk Phone 9851: 480x240

Cisco Desk Phone 9861: 800x480

Cisco Desk Phone 9871: 1280x720

Cisco Desk Phone 9800 Key Expansion Module: 480x800

Cisco Video Phone 8875: 1024x600

Cisco Desk Phone 9851: 100x56

Cisco Desk Phone 9861: 150x90

Cisco Desk Phone 9871: 228x128

Cisco Video Phone 8875: 180x100

Choose your desired logo and wallpaper images.

Format the images to meet the required specifications as described in the table above.

Rename the wallpaper image files in this format:

- For phone wallpaper and KEM wallpaper images, use wallpaper-xxx.png .
              Replace xxx with your desired name. For example, wallpaper-blue.png , wallpaper-darkgreen.png .

- For phone wallpaper thumbnail images, use thumbnail-xxx.png . Replace xxx with your desired name. For example, thumbnail-blue.png , thumbnail-darkgreen.png .

- The system cannot utilize wallpaper files that are named using different patterns. However, for the logo file, you have the flexibility to name it as per your requirements.

- Make sure that the phone wallpaper and KEM wallpaper have the same filename. Otherwise, the system will fail to load the KEM wallpaper and use the system default wallpaper for KEM.

- For the xxx in the filename, do not use special characters. Only use letters and numbers.

- Thumbnail images for logo and KEM wallpapers are not required.

Create a general management file

The system uses the List.xml file to manage the wallpaper and logo files. In the file, you can specify the wallpapers and the logo available in the phone custom wallpaper settings. The List.xml file must be uploaded to the repository where you store the image files for a particular phone model.

Here is an example of the definitions in a general management file:

```
<CiscoIPPhoneImageList version="1.0">
<!-- Please Add Images to the end of the list-->

<ImageItem Name="Blue"
Image="TFTP:Desktops/DP-9871/wallpaper-blue.png"
Thumbnail="TFTP:Desktops/DP-9871/thumbnail-blue.png"
Theme = "dark"/>

<ImageItem Name="Purple"
Image="TFTP:Desktops/DP-9871/wallpaper-purple.png"
Thumbnail="TFTP:Desktops/DP-9871/thumbnail-purple.png"
Theme = "dark"/>

<ImageItem Name="logo"
Image="TFTP:Desktops/DP-9871/logo.png"/>

</CiscoIPPhoneImageList>
```

Make sure you include the root element CiscoIPPhoneImageList in your XML file.

If you upload a new XML file or update the existing one, make sure to do the following actions:

- Increment the version number. For example, 1.1, 1.2, and so on.

- Restart the TFTP server.

```
<CiscoIPPhoneImageList version="1.0">
</CiscoIPPhoneImageLis>
```

You can add multiple ImageItem elements. Each element contains the information for a particular wallpaper file and has the following four parameters:

Name= : The display name of the wallpaper in the custom wallpaper settings.

Image= : Specifies the TFTP path of the image file as TFTP:Desktops/DP-9871/wallpaper-xxx.png , where replace wallpaper-xxx.png with your wallpaper filename.

Thumbnail= : Specifies the file path of the wallpaper thumbnail file as TFTP:Desktops/DP-9871/thumbnail-xxx.png , where replace thumbnail-xxx.png with your actual thumbnail filename.

Theme= : Specifies the default color theme when the phone uses the default custom wallpaper that the administrator specifies. If the color mode isn't specified, it defaults to the light theme. This parameter doesn't apply when access to the custom wallpaper settings is enabled.

Options: dark, light

```
<ImageItem Name="Blue"
Image="TFTP:Desktops/DP-9871/wallpaper-blue.png"
Thumbnail="TFTP:Desktops/DP-9871/thumbnail-blue.png"
Theme = "dark"/>
```

Name="logo" : Include Name="logo" as is in your XML file. Don't change the value. The system uses it to identify the logo file.

Image= : Specifies the TFTP path of the logo file as TFTP:Desktops/model-name/xxx.png .

Replace the model-name with the name of your phoen model, such as DP-9871, DP-9851, DP-9861NR, etc.  And,  replace xxx.png with your actual logo filename.

```
<ImageItem Name="logo"
Image="TFTP:Desktops/DP-9871/logo.png"/>
```

The following figure shows the Logo and Custom wallpaper setting screens:

When multiple lines are configured on Cisco Desk Phone 9841, 9851, and 9861, the logo and the logo setting in the menu are unavailable.

Before you begin

Obtain the file path on the TFTP server that you've uploaded the wallpaper and logo images to.

Create a new file with your text editor or XML editor.

Add the elements with the information of your image files included.

The file path and file names are case-sensitive. Make sure you enter them correctly.

Save the file as List.xml .

Upload files to the TFTP server

Upload the List.xml file and all your wallpaper and logo image files to the TFTP server. After you apply the custom wallpaper settings on Cisco Unified Communications Manager, your phones download the images from the server.

Upload your phone wallpaper images, logo image, and the List.xml file to the model-specific folder. Make sure the folder name matches your phone model. You can find the model name on the back of your phone. For example, DP-9851, DP-9861, DP-9861NR, DP-9871, DP-9871NR.

Upload your KEM wallpaper images to this folder.

On Cisco Unified Communications Manager Administration, select Cisco Unified OS Administration in the Navigation field and click Go .

Select Software Updates > TFTP File Management > Upload File .

Click Choose File and select the file to upload in your local drive.

Specify the upload directory for the wallpaper image.

Click Upload File .

Repeat Step 3 through Step 5 to upload more files.

What to do next

Restart the TFTP server.

Restart the TFTP server

To apply the changes that you've made, restart the TFTP server.

On Cisco Unified Communications Manager Administration, select Cisco Unified Serviceability in the Navigation field and click Go .

Navigate to Tools > Control Center - Feature Services .

Select your server and click Go .

Select Cisco TFTP in the CM Services section.

Click Restart .

Configure the wallpaper settings on Cisco Unified Communications Manager Administration

As an administrator, you can designate the wallpaper image that will be applied to the deployed phones. If you grant users access to the appearance settings on their phones, they can choose whether to display the logo and select their preferred wallpaper from the provided options. However, if you do not grant them access, the appearance settings will be hidden on the phones.

Before you begin

Before you start configuring the wallpaper settings on Cisco Unified Communications Manager Administration, finish the following actions first:

- Prepare your wallpaper and logo images

- Create a general management file ( List.xml )

- Upload the List.xml file and the image files to the TFTP server

Log in to Cisco Unified Communications Manager Administration.

Navigate to Device > Device Settings > Common Phone Profile .

Locate and click the profile that your phones are using.

In the Common Phone Profile Information section, check the check box of Enable End User Access to Phone Background Image Setting if you want to allow users to change the phone screen background image. Otherwise, leave the check box unchecked.

Go to the Product Specific Configuration Layout section and enter the filename of the wallpaper image file in the Background Image field.

It's important to enter the exact filename that you specified in the List.xml file. If you enter a wrong filename, the system will fail to load the wallpaper.

Click Save and then Apply Config .

Restart the phones.

Customize wallpaper by sending XML to the phone

In addition to uploading a prepared XML file to a TFTP server, you can also directly send an XML request to the phone to customize the wallpaper of the phone and KEM screens.

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

Set Phone Personalization to Enabled .

Associate the phone to the user.

Select User Management > User .

Find and locate the user that you want to configure.

In the Device Information section, click Device Associate .

Find and select the device, and then click Save Selected/Changes .

Prepare an HTML file that contains the XML information specified for customized wallpaper.

Here's an example of the HTML file:

```
<HTML>
<HEAD>
</HEAD>
<BODY>

<FORM action=" <Phone_IP_Address> " Method="POST">
<TEXTAREA NAME="XML" Rows="8" Cols="100">
<setBackground>
<background name=" <Name> " theme=" <light/dark> ">
<image> <File_Path> </image>
<thumbnail> <File_Path> </thumbnail>
<kem> <File_Path> </kem>
</background>
</setBackground>
</TEXTAREA>
<BR>
<input type="submit" value="POST to bumblebee"/> <P>
</FORM>

</BODY>
</HTML>
```

```
<FORM action="http://10.74.23.246/CGI/Execute" Method="POST">
```

```
<setBackground>
</setBackground>
```

"theme" defines the default theme of the wallpaper.

```
<background name="Sunset" theme="light">
```

The PNG format is only supported.

```
<image>http://10.79.63.28/wallpaper-sunset.png</image>
```

```
<thumbnail>http://10.79.63.28/thumbnail-sunset.png</thumbnail>
```

```
<kem>http://10.79.63.28/lajiang/wallpaper-sunset.png</kem>
```

Save and file to your local disk, and open it with a web browser, and then click the button.

The wallpaper will be pushed to the phone. When the configuration is complete, the users can view and set the wallpaper as usual on the phone screen.

(Optional) To remove the custom wallpaper from the phone, do the following:

Make sure that the <image> element is empty, other elements can remain the same. For example:

```
<image></image>
```

Save the file, open it with a browser, and then click the button.

The previously downloaded wallpaper will be removed from the phone. The default wallpaper setting will be applied to the phone.

If your Cisco Desk Phone 9800 Series is registered to Cisco BroadWorks, follow the information in this section to set up the attached Key Expansion Modules.

Enable or disable a KEM for the phone

The 9851 phone supports one Key Expansion Module (KEM); the 9861 and 9871 phones support up to three KEMs. You can specify the number of KEMs that can be used on the 9861 and 9871 phones. You can also disable the attached KEMs.

Before you begin

- Access the phone web interface.

- Make sure the side USB port on the phone is enabled.

Select Voice > Att Console .

In the General section, select an option from the drop-down list of Number of Units .

Setting the value to 0 disables all the connected KEMs. Setting the value to 2 for a phone with three KEMs disables the third KEM.

Default: 1 (for 9851); 3 (for 9861 and 9871)

Options for 9851: 0, 1

Options for 9861 and 9871: 0, 1, 2, 3

You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format:

<Number_of_Units ua="na">3</Number_of_Units>

Click Submit All Changes .

Move additional lines to KEM (9871 only)

Cisco Desk Phone 9871 natively supports up to 32 virtual line keys on the touchscreen. With three KEMs connected, it can support up to 124 or 128 lines depending on the Unified CM configurations. When a KEM is attached, you can specify whether to retain 4 lines or 8 lines on the phone, and move the additional lines to the KEM.

Before you begin

Access the phone administration web page.

Select Voice > Att Console .

In the Number of Phone Lines field, choose 4 or 8 .

By default, the field is set to 4 . The additional extension lines and feature lines are moved to the attached KEMs.

You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format:

<Number_of_Phone_Lines ua="na">4</Number_of_Phone_Lines>

Click Submit All Changes .

Assign an extension number to a line key on KEM

You can assign an extension number to a key expansion module line key so that the line key can be used as a SIP line.

Cisco BroadWorks supports up to 16 SIP lines on a phone. You can configure a line key as the primary line or as a shared line that shares a SIP number with other line keys.

Before you begin

Access the phone administration web page.

Access the KEM settings in the way that's applicable to your phone model.

Select Voice > Att Console .

Select Voice > Phone .

Go to the section of the KEM line key that you want to configure.

Select a number from 1 to 16 in the Extension drop-down list.

You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format:

<Unit_n_Extension_m_ ua="na">3</Unit_n_Extension_m_>

where, replace the n and m with the corresponding unit number and line key number.

<Extension_n_ ua="na">8</Extension_n_>

where, n is the line key number.

Click Submit All Changes .

Add an extended feature to a KEM line key

You can add a feature to a line key of the attached KEM. Then, the user can press the line key to access the feature. For the supported features, see Programmable features on line keys .

Before you begin

Access the phone administration web page.

Access the KEM settings in the way that's applicable to your phone model.

Select Voice > Att Console .

Select Voice > Phone .

Go to the section of the KEM line key that you want to configure.

Enter a string in the Extended Function field in this format:

```
fnc=blf+sd+cp;sub=<BLF_URI>;ext=$USER@$PROXY;
```

For the supported features on line keys and the valid string syntax, see Programmable features on line keys .

You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format:

<Unit_n_Key_m_ ua="na">fnc=blf+sd+cp;sub=<BLF_URI>;ext=$USER@$PROXY;</Unit_n_Key_m_>

where, replace the n and m with the corresponding unit number and line key number.

<Extended_Function_n_ ua="na">fnc=blf+sd+cp;sub=<BLF_URI>;ext=$USER@$PROXY;</Extended_Funcction_n_>

where, replace n with the KEM line key number.

Click Submit All Changes .

Enable users to configure features on KEM

You can enable the user to configure features on the line keys of the key expansion module. The user can access the list of available features by pressing the line key and configure it with their desired feature.

Before you begin

Access the phone administration web page.

Select Voice > Att Console .

In the General section, configure the Customizable PLK Options parameter with the codes of your desired features.

You can configure multiple features for line keys and separate each feature code with a semicolon. The user can add a feature to an empty line key, as well as edit or remove the existing feature.

- Create or edit Speed dial

- Create or edit BLF + Speed dial

- Replace the existing feature with another

- Remove the existing feature

- Create or edit BLF + Call pickup

- Remove the existing feature

- Create or edit Speed dial

- Create or edit BLF + Speed dial

- Create or edit BLF + Speed dial + Call pickup

- Replace the existing feature with another

- Remove the existing feature

- Create Call forward

- Remove the existing feature

If assigned with the call forward feature, pressing the line key opens the call forward settings window. The user can configure forward settings for each extension line on both the phone and KEM.

- Create Do not disturb

- Remove the existing feature

If assigned with the DND feature, pressing the line key toggles DND on or off.

- Create Redial

- Remove the existing feature

If assigned with the redial feature, pressing the line key redials the last called number.

- Create or edit Speed dial

- Remove the existing feature

You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format:

<Customizable_PLK_Options ua="na">blf;sd;dnd</Customizable_PLK_Options>

Click Submit All Changes .

Shut down a line key on KEM

You can shut down a line key on a KEM by setting it to Inert mode through the phone's web page. When a KEM line key is in Inert mode, it is completely disabled. For example, the LED on the line key is turned off, no icons or text are displayed next to the line key, and the line button is unresponsive. In short, it is completely unavailable.

Before you begin

Access the phone administration web interface.

Access the KEM settings in the way that's applicable to your phone model.

Select Voice > Att Console .

Select Voice > Phone .

Go to the section of the KEM line key that you want to shut down.

Enter fnc=inert in the Extended Function field.

fnc=inert means function=inert.

You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format:

<Unit_n_Key_m_ ua="na">fnc=inert</Unit_n_Key_m_>

where, replace the n and m with the corresponding unit number and line key number.

<Extended_Function_n_ ua="na">fnc=inert</Extended_Function_n_>

where, replace n with the KEM line key number.

Click Submit All Changes .

| Phone model | Supported total number of KEMs and lines |
|---|---|
| Cisco Desk Phone 9851 | Supports 1 KEM and 46 lines (6 lines on phone) |
| Cisco Desk Phone 9861 | Supports up to 3 KEMs and 130 lines (10 lines on phone) |
| Cisco Desk Phone 9871 | Supports up to 3 KEMs and 124-128 lines, depending on configuration (4 or 8 lines
                  on phone screen) |

| Hardware | Description |
|---|---|
| 1. Line keys | Each button corresponds to one line. The light of each button indicates the state
                  of the corresponding line as follows: The light of button indicates the state of the corresponding line as
                  follows: Light off—Line is idle or not configured. Green steady—Line is in use. Red steady—Shared line or monitored line is in use
                  remotely. Red flashing—Line has calls on hold. Amber blinking—Line has an incoming call. The LEDs also reflect the status of the extended features assigned to the
                  buttons. |
| 2. LCD screen | LCD screen—Displays the phone number, speed-dial number (or name or other text label), phone service, or phone feature assigned to each button. Icons that indicate line status resemble (in both appearance and function) the icons on the phone to which the KEM is attached. |
| 3. Shift buttons | Shift buttons—2 buttons. The button for page 1 is labeled as 1 and the button for page 2 is labeled as 2. The lights in each button indicate the state of the page as follows: Green steady LED—Page is in view. Light off—Page is not in view. Amber steady LED—Page is not in view with one or more alerting calls on the page. |

| 1 | Remove the accessory connector cover. |
|---|---|
| 2 | Firmly press the USB connector attached to the module to the phone. |
| 3 | Fasten the screw into the phone. After you firmly attach the module to the phone, the front screen of the phone and KEM appears as following. An automatic upgrade will initiate if the firmware version on the KEM is lower than that on the phone. Wait until the update is complete. |

| 1 | From the customer view in Control Hub , go to Devices , and then select your phone. |
|---|---|
| 2 | Select All configurations . |
| 3 | In the Att Console section, choose 4 or 8 for Maximum Lines On Phone With KEM . By default, the field is set to 4 . The additional extension lines and feature lines are moved to the attached KEMs. |
| 4 | Select Next . |
| 5 | Review your changes and select Apply . |
| 6 | Select Close to close the page. |

| 1 | From the customer view in Control Hub , go to Devices , and then select your phone. |
|---|---|
| 2 | Under Device Management , select Configure Layout and then select Custom Layout . |
| 3 | Do one of the following action based on your phone model: At the bottom of the page, select Configure KEM Keys . Go to Step 4. |
| 4 | Choose one of the following options for each line key you'd like to modify: Open —No value specified. Primary line —Setting a primary line clears all extended line key functions like monitoring or speed dial values that may exist in a PLK from a previous configuration. Shared / Virtual line —Shared Line Appearance (SLA) positions populate from the values set in configure lines. SLAs populate PLK positions to the layout from top-left to bottom-right. A warning displays if the number of SLA in the configure lines list exceeds the available shared line positions in the layout. Monitored line —Monitoring (BLF) positions populate from the values set in the monitoring list. Monitoring entries populate the defined monitoring PLKs first followed by open PLKs. A warning displays if the number of monitoring entries in your monitoring list exceeds the available monitoring positions in the layout. Speed dial —Speed dial entries require a name and destination extension, telephone number or SIP URI ( example@webex.com ). SIP URI destinations aren’t routable. Speed dials defined here aren’t customizable on the device. Closed —The key is disabled. |
| 5 | Select Save . |

| Index | Label Name | Description |
|---|---|---|
| 1 | Display Name | For the primary line only. It shows on the top left of the phone screen. |
| 2 | Line Key Label | For any other lines (except for the primary line) on the phone with multiple lines. It's the first line when the secondary label is enabled. It also supports the multiple appearances for a same line (suffixed with a -1, -2, and so on). |
| 3 | Line Key Secondary Label | For all lines. It shows as the second line label for the primary line and line keys. |

| 1 | From the customer view in Control Hub , go to Devices , and then select your phone. |
|---|---|
| 2 | Ensure that the value of Line Label is set to default or empty. Select Configure Lines in the Device Management section to access the Configured Lines page. Clear the value of Line Label for the configured lines. The parameter Line Label takes precedence over Line Key Label . If Line Label is
                configured, the phone will show the configured line label instead. Click Save . |
| 3 | On the device details page, select All Configurations in the Configurations section. |
| 4 | In the Phone section, configure the parameters Display Name , Line Key Label , and Line Key Secondary Label . For more information about the parameters, see Parameters for configurable line key labels on Control Hub . |
| 5 | Click Next , review your changes, and then click Apply . |

| Parameter | Default and options | Description |
|---|---|---|
| Display Name | Default: For
                        9841/9851: User Phone Number / Location Number / User Extension For
                        9861/9871/8875: User Name (First Name Last Name) Options: User Phone Number / Location Number / User Extension User Name (First Name Last Name) User Name (Last Name First Name) | For the option User Phone Number / Location Number / User Extension , the display priority is: User Phone Number > Location Number > User Extension. If  User Phone Number is empty, then the phone will display Location Number.
                  Meanwhile, if the Location Number is also empty, then the phone will display User
                  Extension. If the actual values of "Display Name" and "Line Key Label" are identical, the secondary line label on the primary line doesn't display. |
| Line Key Label | Default: User Name (First Name Last Name) Options: User Extension / First Name User Name (First Name Last Name) User Name (Last Name First Name) | For the option User Extension / First Name , the display priority is: User Extension > First Name If  User Extension is empty, then the phone will display First Name. If a line is configured with multiple appearances, the suffix (-1, -2, and so on) is appended to the Line Key Label. |
| Line Key Secondary Label | Default: User Phone Number / Location Number / User Extension Options: User Extension / First Name User Name (First Name Last Name) User Name (Last Name First Name) User Phone Number / Location Number / User Extension None | If set to None, the phone doesn't display the secondary label on the line key. In this case, only one line label displays on the phone (including the primary line on the upper left corner of the phone screen). If the actual values of "Line Key Label" and "Line Key Secondary Label" are identical, the secondary label on the line key will only display the string "Line". |

| 1 | On Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| 2 | Click Find and use the filters to search for your phone. |
| 3 | Click the device name of your phone to open the Phone Configuration page. |
| 4 | In the Expansion Module Information section, choose your KEM in the module drop-down list. By default, the fields are set to None . The module appears in the list only when it's connected to the phone. |
| 5 | Click Save . |
| 6 | Click Apply Config . |

| 1 | On Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| 2 | Click Find and use the filters to search for your phone. |
| 3 | Click the device name of your phone to open the Phone Configuration page. |
| 4 | In the Maximum lines on phone with KEM field, choose 4 or 8 . By default, the field is set to 4 . The additional extension lines and feature lines are moved to the attached KEMs. |
| 5 | Click Save . |
| 6 | Click Apply Config . |

| 1 | On Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| 2 | Use the filters to find your phone to configure. |
| 3 | Click the device name of your phone to open the Phone Configuration page. |
| 4 | Click Line [n] - Add a new DN in the Association pane on the left. |
| 5 | In the Directory Number Configuration window, enter a dialable phone number in the Directory Number field. |
| 6 | (Optional) Select a partition in the Rout Partition field. |
| 7 | (Optional) Select a calling search space in the Calling Search Space field in the Directory Number Settings area. |
| 8 | Click Save . |

| Feature name | Description |
|---|---|
| BLF with Call Park | Use the Call Park BLF feature in the phone button template to control this shortcut. |
| BLF with Call Pickup | Use the Speed Dial BLF feature in the phone button template and enable the checkbox Call Pickup in the Busy Lamp Field Speed Dial Configuration window to control this shortcut. |
| BLF with Speed Dial | Use the Speed Dial BLF feature in the phone button template to control this shortcut. |
| Call Park | Use the Call Park feature in the phone button template
                to control this shortcut. |
| Call Pickup | Use the Call Pickup feature in the phone button template
                to control this shortcut. |
| DND | Use the Do Not Disturb feature in the phone button template to control this shortcut. |
| Group Pickup | Use the Group Call Pickup feature in the phone button
                template to control this shortcut. |
| Hunt Group | Use the Hunt Group Logout feature in the phone button template to control this shortcut. |
| Intercom | Use the Intercom feature in the phone button template to control this shortcut. |
| Malicious Call Identification | Use the Malicious Call Identification feature in the
                phone button template to control this shortcut. |
| Meet Me | Use the Meet Me Conference feature in the phone button template to control this shortcut. |
| Other Pickup | Use the Other Pickup feature in the phone button
                template to control this shortcut. |
| Privacy | Use the Privacy feature in the phone button template to control this shortcut. |
| Queue Status | Use the Queue Status feature in the phone button template to control this shortcut. |
| Redial | Use the Redial feature in the phone button template to control this shortcut. |
| Speed Dial | Use the Speed Dial feature in the phone button template to control this shortcut. |
| XSI Service | Use the Service URL feature in the phone button template to control this shortcut. |

| 1 | On Cisco Unified Communications Manager Administration, choose Device > Device Settings > Phone Button Template . |
|---|---|
| 2 | Click Find to display list of supported phone templates. |
| 3 | Perform the following steps if you want to create a new phone button template; otherwise, proceed to the next step. Select a default template for the model of phone and click Copy . In the Phone Button Template Information field, enter a new name for the template. Click Save . |
| 4 | Perform the following steps if you want to add phone buttons to an existing template. Click Find and enter the search criteria. Choose an existing template. |
| 5 | From the Line drop-down list, choose feature that you want to add to the template. |
| 6 | Click Save . |
| 7 | Perform one of the following tasks: Click Apply
              Config if you modified a template that is already associated with devices
            to restart the devices. If you created a new button template, associate the template with the devices and then restart them. |

| 1 | On Cisco Unified Communications Manager Administration, choose Device > Phone . |
|---|---|
| 2 | Click Find to display the list of configured phones. |
| 3 | Choose the phone to which you want to add the phone button template. |
| 4 | In the Phone Button Template drop-down list, choose the phone
          button template that contains the new feature button. |
| 5 | Click Save . A message prompts for clicking Reset to update the phone
          settings. |
| 6 | Click Reset . |

| Image | Supported format (Unified CM) | Recommended dimensions (pixels) | Description |
|---|---|---|---|
| Logo | PNG | Cisco Desk Phone 9851: 190x125 Cisco Desk Phone 9861: 380x250 Cisco Desk Phone 9871: 494x325 / 418x275 Cisco Video Phone 8875: 380x250 | Images that don't match the recommended dimensions will be scaled
                  proportionally. You don't need to create a separate thumbnail image for the
                  logo. The system automatically scales the logo image to fit the dimensions of the
                  thumbnail. |
| Wallpaper | Cisco Desk Phone 9851: 480x240 Cisco Desk Phone 9861: 800x480 Cisco Desk Phone 9871: 1280x720 Cisco Desk Phone 9800 Key Expansion Module: 480x800 Cisco Video Phone 8875: 1024x600 | Images that don't match the recommended dimensions may be scaled to fit the
                phone screen, which may cause the image to become distorted. |
| Wallpaper thumbnail | Cisco Desk Phone 9851: 100x56 Cisco Desk Phone 9861: 150x90 Cisco Desk Phone 9871: 228x128 Cisco Video Phone 8875: 180x100 | Images that don't match the recommended dimensions may cause certain issues on
                the phone. |

| Phone Model | Maximum size per image | Maximum number of images | Limit size |
|---|---|---|---|
| Cisco Desk Phone 9851 | 250KB | 10 | 250KB x 10 |
| Cisco Desk Phone 9861 | 1MB | 20 | 1MB x 20 |
| Cisco Desk Phone 9871 | 1MB | 20 | 1MB x 20 |
| Cisco Video Phone 8875 | 1MB | 20 | 1MB x 20 |

| 1 | Choose your desired logo and wallpaper images. |
|---|---|
| 2 | Format the images to meet the required specifications as described in the table above. |
| 3 | Rename the wallpaper image files in this format: For phone wallpaper and KEM wallpaper images, use wallpaper-xxx.png .
              Replace xxx with your desired name. For example, wallpaper-blue.png , wallpaper-darkgreen.png . For phone wallpaper thumbnail images, use thumbnail-xxx.png . Replace xxx with your desired name. For example, thumbnail-blue.png , thumbnail-darkgreen.png . The system cannot utilize wallpaper files that are named using different patterns. However, for the logo file, you have the flexibility to name it as per your requirements. Make sure that the phone wallpaper and KEM wallpaper have the same filename. Otherwise, the system will fail to load the KEM wallpaper and use the system default wallpaper for KEM. For the xxx in the filename, do not use special characters. Only use letters and numbers. Thumbnail images for logo and KEM wallpapers are not required. |

| Element | Description | Example |
|---|---|---|
| Root element | Make sure you include the root element CiscoIPPhoneImageList in your XML file. If you upload a new XML file or update the existing one, make sure to do the following actions: Increment the version number. For example, 1.1, 1.2, and so on. Restart the TFTP server. Otherwise, the phone won't download the latest version of the XML file. | <CiscoIPPhoneImageList version="1.0">
</CiscoIPPhoneImageLis> |
| Wallpaper item element | You can add multiple ImageItem elements. Each element contains the information for a particular wallpaper file and has the following four parameters: Name= : The display name of the wallpaper in the custom wallpaper settings. Image= : Specifies the TFTP path of the image file as TFTP:Desktops/DP-9871/wallpaper-xxx.png , where replace wallpaper-xxx.png with your wallpaper filename. Thumbnail= : Specifies the file path of the wallpaper thumbnail file as TFTP:Desktops/DP-9871/thumbnail-xxx.png , where replace thumbnail-xxx.png with your actual thumbnail filename. Theme= : Specifies the default color theme when the phone uses the default custom wallpaper that the administrator specifies. If the color mode isn't specified, it defaults to the light theme. This parameter doesn't apply when access to the custom wallpaper settings is enabled. Options: dark, light | <ImageItem Name="Blue"
Image="TFTP:Desktops/DP-9871/wallpaper-blue.png"
Thumbnail="TFTP:Desktops/DP-9871/thumbnail-blue.png"
Theme = "dark"/> |
| Logo item element | Your phone supports only one logo to be added. The logo item element also uses the ImageItem element but has the following two parameters. Name="logo" : Include Name="logo" as is in your XML file. Don't change the value. The system uses it to identify the logo file. Image= : Specifies the TFTP path of the logo file as TFTP:Desktops/model-name/xxx.png . Replace the model-name with the name of your phoen model, such as DP-9871, DP-9851, DP-9861NR, etc.  And,  replace xxx.png with your actual logo filename. | <ImageItem Name="logo"
Image="TFTP:Desktops/DP-9871/logo.png"/> |

| 1 | Create a new file with your text editor or XML editor. |
|---|---|
| 2 | Add the elements with the information of your image files included. The file path and file names are case-sensitive. Make sure you enter them correctly. |
| 3 | Save the file as List.xml . |

| 1 | On Cisco Unified Communications Manager Administration, select Cisco Unified OS Administration in the Navigation field and click Go . |
|---|---|
| 2 | Select Software Updates > TFTP File Management > Upload File . |
| 3 | Click Choose File and select the file to upload in your local drive. |
| 4 | Specify the upload directory for the wallpaper image. |
| 5 | Click Upload File . |
| 6 | Repeat Step 3 through Step 5 to upload more files. |

| 1 | On Cisco Unified Communications Manager Administration, select Cisco Unified Serviceability in the Navigation field and click Go . |
|---|---|
| 2 | Navigate to Tools > Control Center - Feature Services . |
| 3 | Select your server and click Go . |
| 4 | Select Cisco TFTP in the CM Services section. |
| 5 | Click Restart . |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Navigate to Device > Device Settings > Common Phone Profile . |
| 3 | Locate and click the profile that your phones are using. |
| 4 | In the Common Phone Profile Information section, check the check box of Enable End User Access to Phone Background Image Setting if you want to allow users to change the phone screen background image. Otherwise, leave the check box unchecked. |
| 5 | Go to the Product Specific Configuration Layout section and enter the filename of the wallpaper image file in the Background Image field. It's important to enter the exact filename that you specified in the List.xml file. If you enter a wrong filename, the system will fail to load the wallpaper. |
| 6 | Click Save and then Apply Config . |
| 7 | Restart the phones. |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. |
| 3 | Set Phone Personalization to Enabled . |
| 4 | Associate the phone to the user. Select User Management > User . Find and locate the user that you want to configure. In the Device Information section, click Device Associate . Find and select the device, and then click Save Selected/Changes . |
| 5 | Prepare an HTML file that contains the XML information specified for customized wallpaper. Here's an example of the HTML file: <HTML>
<HEAD>
</HEAD>
<BODY>

<FORM action=" <Phone_IP_Address> " Method="POST">
<TEXTAREA NAME="XML" Rows="8" Cols="100">
<setBackground>
<background name=" <Name> " theme=" <light/dark> ">
<image> <File_Path> </image>
<thumbnail> <File_Path> </thumbnail>
<kem> <File_Path> </kem>
</background>
</setBackground>
</TEXTAREA>
<BR>
<input type="submit" value="POST to bumblebee"/> <P>
</FORM>

</BODY>
</HTML> Element Description Example FORM IP address of the phone <FORM action="http://10.74.23.246/CGI/Execute" Method="POST"> setBackground Make sure you include the root element in the HTML file. <setBackground>
</setBackground> background The value of the attribute "name" will be displayed on the phone. "theme" defines the default theme of the wallpaper. <background name="Sunset" theme="light"> image File path of the wallpaper image. The PNG format is only supported. <image>http://10.79.63.28/wallpaper-sunset.png</image> thumbnail File path of the wallpaper thumbnail image. <thumbnail>http://10.79.63.28/thumbnail-sunset.png</thumbnail> kem File path of the wallpaper image for the phone Key Expansion Module (KEM). It's an optional element. <kem>http://10.79.63.28/lajiang/wallpaper-sunset.png</kem> | Element | Description | Example | FORM | IP address of the phone | <FORM action="http://10.74.23.246/CGI/Execute" Method="POST"> | setBackground | Make sure you include the root element in the HTML file. | <setBackground>
</setBackground> | background | The value of the attribute "name" will be displayed on the phone. "theme" defines the default theme of the wallpaper. | <background name="Sunset" theme="light"> | image | File path of the wallpaper image. The PNG format is only supported. | <image>http://10.79.63.28/wallpaper-sunset.png</image> | thumbnail | File path of the wallpaper thumbnail image. | <thumbnail>http://10.79.63.28/thumbnail-sunset.png</thumbnail> | kem | File path of the wallpaper image for the phone Key Expansion Module (KEM). It's an optional element. | <kem>http://10.79.63.28/lajiang/wallpaper-sunset.png</kem> |
| Element | Description | Example |
| FORM | IP address of the phone | <FORM action="http://10.74.23.246/CGI/Execute" Method="POST"> |
| setBackground | Make sure you include the root element in the HTML file. | <setBackground>
</setBackground> |
| background | The value of the attribute "name" will be displayed on the phone. "theme" defines the default theme of the wallpaper. | <background name="Sunset" theme="light"> |
| image | File path of the wallpaper image. The PNG format is only supported. | <image>http://10.79.63.28/wallpaper-sunset.png</image> |
| thumbnail | File path of the wallpaper thumbnail image. | <thumbnail>http://10.79.63.28/thumbnail-sunset.png</thumbnail> |
| kem | File path of the wallpaper image for the phone Key Expansion Module (KEM). It's an optional element. | <kem>http://10.79.63.28/lajiang/wallpaper-sunset.png</kem> |
| 6 | Save and file to your local disk, and open it with a web browser, and then click the button. The wallpaper will be pushed to the phone. When the configuration is complete, the users can view and set the wallpaper as usual on the phone screen. |
| 7 | (Optional) To remove the custom wallpaper from the phone, do the following: Make sure that the <image> element is empty, other elements can remain the same. For example: <image></image> Save the file, open it with a browser, and then click the button. The previously downloaded wallpaper will be removed from the phone. The default wallpaper setting will be applied to the phone. |

| Element | Description | Example |
|---|---|---|
| FORM | IP address of the phone | <FORM action="http://10.74.23.246/CGI/Execute" Method="POST"> |
| setBackground | Make sure you include the root element in the HTML file. | <setBackground>
</setBackground> |
| background | The value of the attribute "name" will be displayed on the phone. "theme" defines the default theme of the wallpaper. | <background name="Sunset" theme="light"> |
| image | File path of the wallpaper image. The PNG format is only supported. | <image>http://10.79.63.28/wallpaper-sunset.png</image> |
| thumbnail | File path of the wallpaper thumbnail image. | <thumbnail>http://10.79.63.28/thumbnail-sunset.png</thumbnail> |
| kem | File path of the wallpaper image for the phone Key Expansion Module (KEM). It's an optional element. | <kem>http://10.79.63.28/lajiang/wallpaper-sunset.png</kem> |

| 1 | Select Voice > Att Console . |
|---|---|
| 2 | In the General section, select an option from the drop-down list of Number of Units . Setting the value to 0 disables all the connected KEMs. Setting the value to 2 for a phone with three KEMs disables the third KEM. Default: 1 (for 9851); 3 (for 9861 and 9871) Options for 9851: 0, 1 Options for 9861 and 9871: 0, 1, 2, 3 You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format: <Number_of_Units ua="na">3</Number_of_Units> |
| 3 | Click Submit All Changes . |

| 1 | Select Voice > Att Console . |
|---|---|
| 2 | In the Number of Phone Lines field, choose 4 or 8 . By default, the field is set to 4 . The additional extension lines and feature lines are moved to the attached KEMs. You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format: <Number_of_Phone_Lines ua="na">4</Number_of_Phone_Lines> |
| 3 | Click Submit All Changes . |

| 1 | Access the KEM settings in the way that's applicable to your phone model. Select Voice > Att Console . Select Voice > Phone . |
|---|---|
| 2 | Go to the section of the KEM line key that you want to configure. |
| 3 | Select a number from 1 to 16 in the Extension drop-down list. You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format: <Unit_n_Extension_m_ ua="na">3</Unit_n_Extension_m_> where, replace the n and m with the corresponding unit number and line key number. <Extension_n_ ua="na">8</Extension_n_> where, n is the line key number. |
| 4 | Click Submit All Changes . |

| 1 | Access the KEM settings in the way that's applicable to your phone model. Select Voice > Att Console . Select Voice > Phone . |
|---|---|
| 2 | Go to the section of the KEM line key that you want to configure. |
| 3 | Enter a string in the Extended Function field in this format: fnc=blf+sd+cp;sub=<BLF_URI>;ext=$USER@$PROXY; For the supported features on line keys and the valid string syntax, see Programmable features on line keys . You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format: <Unit_n_Key_m_ ua="na">fnc=blf+sd+cp;sub=<BLF_URI>;ext=$USER@$PROXY;</Unit_n_Key_m_> where, replace the n and m with the corresponding unit number and line key number. <Extended_Function_n_ ua="na">fnc=blf+sd+cp;sub=<BLF_URI>;ext=$USER@$PROXY;</Extended_Funcction_n_> where, replace n with the KEM line key number. |
| 4 | Click Submit All Changes . |

| 1 | Select Voice > Att Console . |
|---|---|
| 2 | In the General section, configure the Customizable PLK Options parameter with the codes of your desired features. You can configure multiple features for line keys and separate each feature code with a semicolon. The user can add a feature to an empty line key, as well as edit or remove the existing feature. Table 8. User-configurable features on KEM line keys Feature Code User options on line key BLF with Speed dial blf;sd Create or edit Speed dial Create or edit BLF + Speed dial Replace the existing feature with another Remove the existing feature BLF with Call pickup blf;cp Create or edit BLF + Call pickup Remove the existing feature BLF with Speed dial and Call pickup blf;sd;cp Create or edit Speed dial Create or edit BLF + Speed dial Create or edit BLF + Speed dial + Call pickup Replace the existing feature with another Remove the existing feature Call forward cfwd Create Call forward Remove the existing feature If assigned with the call forward feature, pressing the line key opens the call forward settings window. The user can configure forward settings for each extension line on both the phone and KEM. Do not disturb dnd Create Do not disturb Remove the existing feature If assigned with the DND feature, pressing the line key toggles DND on or off. Redial redial Create Redial Remove the existing feature If assigned with the redial feature, pressing the line key redials the last called number. Speed dial sd Create or edit Speed dial Remove the existing feature You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format: <Customizable_PLK_Options ua="na">blf;sd;dnd</Customizable_PLK_Options> | Feature | Code | User options on line key | BLF with Speed dial | blf;sd | Create or edit Speed dial Create or edit BLF + Speed dial Replace the existing feature with another Remove the existing feature | BLF with Call pickup | blf;cp | Create or edit BLF + Call pickup Remove the existing feature | BLF with Speed dial and Call pickup | blf;sd;cp | Create or edit Speed dial Create or edit BLF + Speed dial Create or edit BLF + Speed dial + Call pickup Replace the existing feature with another Remove the existing feature | Call forward | cfwd | Create Call forward Remove the existing feature If assigned with the call forward feature, pressing the line key opens the call forward settings window. The user can configure forward settings for each extension line on both the phone and KEM. | Do not disturb | dnd | Create Do not disturb Remove the existing feature If assigned with the DND feature, pressing the line key toggles DND on or off. | Redial | redial | Create Redial Remove the existing feature If assigned with the redial feature, pressing the line key redials the last called number. | Speed dial | sd | Create or edit Speed dial Remove the existing feature |
| Feature | Code | User options on line key |
| BLF with Speed dial | blf;sd | Create or edit Speed dial Create or edit BLF + Speed dial Replace the existing feature with another Remove the existing feature |
| BLF with Call pickup | blf;cp | Create or edit BLF + Call pickup Remove the existing feature |
| BLF with Speed dial and Call pickup | blf;sd;cp | Create or edit Speed dial Create or edit BLF + Speed dial Create or edit BLF + Speed dial + Call pickup Replace the existing feature with another Remove the existing feature |
| Call forward | cfwd | Create Call forward Remove the existing feature If assigned with the call forward feature, pressing the line key opens the call forward settings window. The user can configure forward settings for each extension line on both the phone and KEM. |
| Do not disturb | dnd | Create Do not disturb Remove the existing feature If assigned with the DND feature, pressing the line key toggles DND on or off. |
| Redial | redial | Create Redial Remove the existing feature If assigned with the redial feature, pressing the line key redials the last called number. |
| Speed dial | sd | Create or edit Speed dial Remove the existing feature |
| 3 | Click Submit All Changes . |

| Feature | Code | User options on line key |
|---|---|---|
| BLF with Speed dial | blf;sd | Create or edit Speed dial Create or edit BLF + Speed dial Replace the existing feature with another Remove the existing feature |
| BLF with Call pickup | blf;cp | Create or edit BLF + Call pickup Remove the existing feature |
| BLF with Speed dial and Call pickup | blf;sd;cp | Create or edit Speed dial Create or edit BLF + Speed dial Create or edit BLF + Speed dial + Call pickup Replace the existing feature with another Remove the existing feature |
| Call forward | cfwd | Create Call forward Remove the existing feature If assigned with the call forward feature, pressing the line key opens the call forward settings window. The user can configure forward settings for each extension line on both the phone and KEM. |
| Do not disturb | dnd | Create Do not disturb Remove the existing feature If assigned with the DND feature, pressing the line key toggles DND on or off. |
| Redial | redial | Create Redial Remove the existing feature If assigned with the redial feature, pressing the line key redials the last called number. |
| Speed dial | sd | Create or edit Speed dial Remove the existing feature |

| 1 | Access the KEM settings in the way that's applicable to your phone model. Select Voice > Att Console . Select Voice > Phone . |
|---|---|
| 2 | Go to the section of the KEM line key that you want to shut down. |
| 3 | Enter fnc=inert in the Extended Function field. fnc=inert means function=inert. You can also configure this parameter in the phone configuration file (cfg.xml). Enter a string in this format: <Unit_n_Key_m_ ua="na">fnc=inert</Unit_n_Key_m_> where, replace the n and m with the corresponding unit number and line key number. <Extended_Function_n_ ua="na">fnc=inert</Extended_Function_n_> where, replace n with the KEM line key number. |
| 4 | Click Submit All Changes . |