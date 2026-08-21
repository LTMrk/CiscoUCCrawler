---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-english-ag-p881-b-8800-mpp-ag-new-p881-b-8800-mpp-ag-new-cha-2067e2b2dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/english/AG/p881_b_8800-mpp-ag_new/p881_b_8800-mpp-ag_new_chapter_010100.html
retrieved_at: 2026-08-21T09:57:00.992907+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phone Administration Guide for Release 11.3(1) and Later

# Cisco IP Phone 8800 Series Multiplatform Phone Administration Guide for Release 11.3(1) and Later

Updated: November 21, 2019

Chapter: Phone Information and Display Configuration

## Chapter: Phone Information and Display Configuration

# Phone Information and Display Configuration

## Phone Information and Display Settings

The phone web user interface allows you to customize settings such as the phone name, background picture, logo, and screen
                              saver.

## Configure the Phone Name

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Phone .

Under the General section, enter the phone name in the Station Display Name or Station Name field.

When you configure both names on the phone, the phone only displays the Station Display Name .

If you enable XMPP and set Display XMPP User ID With Top Priority to Yes , the XMPP user ID overrides the configured name.

The priority sequence of displaying on the phone screen is as follows:

XMPP user ID > Station Display Name > Station Name.

```
<Station_Display_Name ua="na">Recetion Desk</Station_Display_Name
```

```
<Station_Name ua="na">Recetion Desk</Station_Name>
```

Click Submit All Changes .

## Customize the Startup Screen

You can create a text or an image logo to display when the Cisco IP Phone boots up. A logo displays during the boot sequence
                              for a short period after the Cisco logo displays.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Click Voice > User .

In the Screen section, select any option from the Boot Display field.

Default : Displays a blank screen or existing screen as the startup screen.

Download Picture : Displays a picture as the startup screen. Enter the path in the Picture Download URL field.

Logo : Displays a logo as the startup screen. Enter the path in the Logo URL field.

Text : Displays a text as the startup screen. Enter text in the Text Display field.

```
<Boot_Display ua="na">Logo</Boot_Display>
```

The allowed values are Default|Download Picture|Logo|Text. The default option is Default.

To display a picture or a logo, enter the path in the Picture Download URL or Logo URL field.

For example:

```
http://10.64.84.147/pictures/image04.png
```

When you enter an incorrect URL to download the image, the phone fails to upgrade to the new image and displays the existing
                                          image. If the phone does not have any image downloaded earlier, it displays a gray screen.

The logo must be a .jpg or a .png file. The phone has a fixed display area. So, if the original logo size doesn't fit into
                                          the display area, you need to scale it to fit the screen. For the Cisco IP Phone 8800 Series, the logo display area is at
                                          the mid-center of the phone screen. The display area size of the Cisco IP Phone 8800 Series is 128x128.

```
<Picture_Download_URL ua="na">http://10.64.84.147/pictures/bootimage1.jpg</Picture_Download_URL>
```

```
<Logo_URL ua="na">http://10.64.84.147/pictures/logo_image.jpg</Logo_URL>
```

To display text at bootup, enter the text to display in the Text Display field following the requirements:

Enter up to two lines of text with less than 32 characters for each line.

Insert a new line character (\n) and escape code (%0a) between the two lines.

```
Super\n%0aTelecom
```

```
Super
Telecom
```

Use the + character to add spaces for formatting. You can add multiple + characters before and after the text to center it.

```
<Text_Display ua="na">Super\n%0aTelecom</Text_Display>
```

Click Submit All Changes.

The phone reboots, retrieves the image file, and displays the picture, logo, or text when it boots next time.

## Customize Wallpaper for the Phone Display

You can set the phone to display a custom logo or picture as the background on the phone screen.

On the phone web interface, select Voice > User .

User can also change the wallpaper in the phone web interface.

In the Screen section, choose one of the options for the Phone Background field:

Default —Keeps the system default background.

Download Picture —Displays a picture downloaded from a TFTP, FTP, or HTTPS server. When select this option, enter the URL for the picture in
                                                the Picture Download URL field.

Logo —Displays a logo downloaded from a TFTP, FTP, or HTTPS server. When select this option, enter the URL for the logo image in
                                                the Logo URL field.

```
<Phone_Background ua="na">Logo</Phone_Background>
```

Upload the custom wallpaper to a TFTP, HTTP, or HTTPS server.

The image is a .jpg or .png file. Preferred dimension is 800x480 pixels. If the image is not the preferred size, user still
                                          can upload it but it will resize to fit the screen.

In the Picture Download URL field, enter the path where the wallpaper image has been uploaded.

The URL must include the TFTP, HTTP, or HTTPS server name (or IP address), directory, and file name. Don't exceed 255 characters
                                          for the URL.

```
http:// 10.64.84.147/pictures/image04.jpg
```

When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the new wallpaper and displays
                                          the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen.

```
<Picture_Download_URL ua="na">http://10.64.84.147/pictures/image04.jpg</Picture_Download_URL>
```

Upload the logo image to a TFTP, HTTP, or HTTPS server.

The logo must be a .jpg or a .png file. The phone has a fixed display area. So, if the original logo size doesn't fit into
                                          the display area, you need to scale it to fit the screen. For the Cisco IP Phone 8800 Series, the logo display area is at
                                          the mid-center of the phone screen. The display area size of the Cisco IP Phone 8800 Series is 128x128.

In the Logo URL field, enter the path where the logo image has been uploaded.

The URL must include the TFTP, HTTP, or HTTPS server name (or IP address), directory, and file name. Don't exceed 255 characters
                                          for the URL.

```
http://10.64.84.147/pictures/logo_image.jpg
```

When you enter an incorrect URL to download a new logo, the phone fails to upgrade to the newer logo and displays the existing
                                          downloaded logo. If the phone does not have any logo downloaded earlier, it displays a gray screen.

```
<Logo_URL ua="na">http://10.64.84.147/pictures/logo_image.jpg</Logo_URL>
```

Click Submit All Changes .

The phone reboots after you change the background image URL.

## Configure the Screen Saver with the Phone Web Interface

You can configure a screen saver for the phone. When the phone is idle for a specified time, it enters screen saver mode.

Any button press returns the phone to normal mode.

You can also configure the parameters in the phone configuration file with XML (cfg.xml) code. To configure each parameter,
                              see the syntax of the string in Parameters for Screen Saver .

### Before you begin

Access the phone administration web interface. See Access the Phone Web Interface .

On the phone web page, select Voice > User .

The user can select User Login > Voice > User to add screen saver to the phone.

In the Screen section, set up the fields as described in Parameters for Screen Saver .

Click Submit All Changes .

### Parameters for Screen Saver

The following table defines the function and usage of the screen saver parameters in the Screen section under the Voice > User tab in the phone web interface. It also definesthe syntax of the stringthat is added in thephone configuration file (cfg.xml)
                                 with XML code to configure a parameter.

Parameter

Description

Screen Saver Enable

Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode.

Perform one of the following:

```
<Screen_Saver_Enable ua="rw">Yes</Screen_Saver_Enable>
```

In the phone web interface, set this field to Yes to enable screen saver.

Allowed values: Yes|No

Default: No

Screen Saver Type

Types of screen saver. Options you can choose:

Clock —Displays a digital clock on a plain background.

Download Picture —Displays a picture pushed from the phone webpage. Enter the image path in the Picture Download URL field.

Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field.

Perform one of the following:

```
<Screen_Saver_Type ua="rw">Clock</Screen_Saver_Type>
```

In the phone web interface, select a screen saver.

Allowed values: Clock|Download Picture|Logo

Default: Clock

Screen Saver Wait

Amount of idle time before screen saver displays.

Enter the number of seconds of idle time to elapse before the screen saver starts.

Perform one of the following:

```
<Screen_Saver_Wait ua="rw">300</Screen_Saver_Wait>
```

In the phone web interface, set the time in seconds.

Allowed values: An integer from 30 through 65000

Default: 300

Picture Download URL

URL locating the (.png) file to display on the phone screen background. The image can display as the screen background, the screensaver, or at bootup depending on the settings of the Phone Background , Screen Saver Type , or Boot Display field.

When you enter an incorrect URL to download a new image, the phone fails to update to the new image and displays the existing
                                             downloaded image. If the phone does not have any image downloaded earlier, it displays a gray screen.

Perform one of the following:

```
<Picture_Download_URL ua="rw">http://10.74.3.52/images/screensaver1.png</Picture_Download_URL>
```

In the phone web interface, specify the URL where the picture is located.

Allowed values: A valid URL not exceeding 255 characters

Default: Empty

Logo URL

Enter a URL or path for the location where the logo image is saved. The logo image can display as the screen background, the
                                             screensaver, or at bootup depending on the settings of the Screen Saver Type , Boot Display , or Phone Background field.

Perform one of the following:

```
<Logo_URL ua="rw">http://10.74.3.52/images/Logo1.png</Logo_URL>
```

In the phone web interface, specify the URL where the logo image is located.

Allowed values: A valid URL not exceeding 255 characters

Default: Empty

## Adjust Backlight Timer from the Phone Web Interface

You
                              		  can save energy by disabling the backlight on each phone at a preset time.

Select Voice > User .

In the Screen section, select a duration for the Back Light Timer parameter.

```
<Back_Light_Timer ua="rw">30s</Back_Light_Timer>
```

The allowed values are 1m|5m|30m|Always On. The default value is 5m (5 minutes).

In the Display Brightness field, enter an integer ranging from 4 to 15 for the desired brightness.

```
<Display_Brightness ua="rw">15</Display_Brightness>
```

The allowed value is an integer ranging from 4 through 15. The bigger the value, the brighter the screen display. The default
                                          value is 15.

Click Submit All Changes .

## Customize the Product Configuration Version

Edit the phone configuration file (cfg.xml) in a text or XML editor.

Add a value for the element <Device_Config_Version> in the cfg.xml file.

For example:

```
<Device_Config_Version ua="na">2021-01-05-v1</Device_Config_Version>
```

Default: Empty

Value range: 0 to 64 characters

If the tag doesn't exist in the cfg.xml file or the parameter value is empty, then the Configuration version menu item doesn't display on the phone screen Product information .

If the length of the assigned characters exceeds the width of the phone screen, the exceeded characters are truncated and
                                                      represented as an ellipsis (...) on the phone screen.

Save the changes to the cfg.xml file.

## Keep Focus on the Active Call

By default, the focus on the phone screen automatically moves from the active call to the incoming call. However, you can
                              configure the phone to ensure that the active call always remains in focus, even when the user has an incoming call.

The focus still moves to an incoming call in the following situations:

The user places an active call on hold and then receives one or more incoming calls, the focus automatically moves to the
                                    first incoming call.

The user is on an active call and receives one or more incoming calls, if the user places the active call on hold, then the
                                    focus automatically moves to the first incoming call.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > User .

In the Supplementary Services section, set the parameter Keep Focus On Active Call to Yes .

You can also configure this parameter in the configuration file:

```
<Keep_Focus_On_Active_Call ua="na">Yes</Keep_Focus_On_Active_Call>
```

Allowed values: Yes and No

Default: No

Click Submit All Changes .

## Report Headset Inventory

You can configure a phone to report the connected or disconnected peripheral information to the server. The peripherals that
                              the Cisco IP Phone Multiplatform Phones support are Key Expansion Module (KEM) and Cisco headset.

The supported Cisco headsets are Cisco Headset 500 Series and Cisco Headset 700 Series.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > SIP .

In the Peripheral section, set the Peripheral Inventory Enable parameter to Yes .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Peripheral_Inventory_Enable ua="na">No</Peripheral_Inventory_Enable>
```

When one peripheral is connected or disconnected to the phone, next scheduled Register provides the peripheral information
                                          in the Peripheral-Data header. All subsequent Registers do not carry peripheral information. The Peripheral-Data header is
                                          included for each peripheral, for example, if there are two headsets present, the header appears twice.

Click Submit All Changes .

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under the General section, enter the phone name in the Station Display Name or Station Name field. Note When you configure both names on the phone, the phone only displays the Station Display Name . If you enable XMPP and set Display XMPP User ID With Top Priority to Yes , the XMPP user ID overrides the configured name. The priority sequence of displaying on the phone screen is as follows: XMPP user ID > Station Display Name > Station Name. This name displays on the phone screen. You can also configure this parameter in the configuration file (cfg.xml) by entering
                                          a string in this format: <Station_Display_Name ua="na">Recetion Desk</Station_Display_Name <Station_Name ua="na">Recetion Desk</Station_Name> | Note | When you configure both names on the phone, the phone only displays the Station Display Name . If you enable XMPP and set Display XMPP User ID With Top Priority to Yes , the XMPP user ID overrides the configured name. The priority sequence of displaying on the phone screen is as follows: XMPP user ID > Station Display Name > Station Name. |
| Note | When you configure both names on the phone, the phone only displays the Station Display Name . If you enable XMPP and set Display XMPP User ID With Top Priority to Yes , the XMPP user ID overrides the configured name. The priority sequence of displaying on the phone screen is as follows: XMPP user ID > Station Display Name > Station Name. |
| Step 3 | Click Submit All Changes . |

| Note | When you configure both names on the phone, the phone only displays the Station Display Name . If you enable XMPP and set Display XMPP User ID With Top Priority to Yes , the XMPP user ID overrides the configured name. The priority sequence of displaying on the phone screen is as follows: XMPP user ID > Station Display Name > Station Name. |
|---|---|

| Step 1 | Click Voice > User . |
|---|---|
| Step 2 | In the Screen section, select any option from the Boot Display field. Default : Displays a blank screen or existing screen as the startup screen. Download Picture : Displays a picture as the startup screen. Enter the path in the Picture Download URL field. Logo : Displays a logo as the startup screen. Enter the path in the Logo URL field. Text : Displays a text as the startup screen. Enter text in the Text Display field. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Boot_Display ua="na">Logo</Boot_Display> The allowed values are Default\|Download Picture\|Logo\|Text. The default option is Default. |
| Step 3 | To display a picture or a logo, enter the path in the Picture Download URL or Logo URL field. For example: http://10.64.84.147/pictures/image04.png When you enter an incorrect URL to download the image, the phone fails to upgrade to the new image and displays the existing
                                          image. If the phone does not have any image downloaded earlier, it displays a gray screen. The logo must be a .jpg or a .png file. The phone has a fixed display area. So, if the original logo size doesn't fit into
                                          the display area, you need to scale it to fit the screen. For the Cisco IP Phone 8800 Series, the logo display area is at
                                          the mid-center of the phone screen. The display area size of the Cisco IP Phone 8800 Series is 128x128. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Picture_Download_URL ua="na">http://10.64.84.147/pictures/bootimage1.jpg</Picture_Download_URL> <Logo_URL ua="na">http://10.64.84.147/pictures/logo_image.jpg</Logo_URL> |
| Step 4 | To display text at bootup, enter the text to display in the Text Display field following the requirements: Enter up to two lines of text with less than 32 characters for each line. Insert a new line character (\n) and escape code (%0a) between the two lines. For example, Super\n%0aTelecom displays: Super
Telecom Use the + character to add spaces for formatting. You can add multiple + characters before and after the text to center it. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Text_Display ua="na">Super\n%0aTelecom</Text_Display> |
| Step 5 | Click Submit All Changes. The phone reboots, retrieves the image file, and displays the picture, logo, or text when it boots next time. |

| Step 1 | On the phone web interface, select Voice > User . User can also change the wallpaper in the phone web interface. |
|---|---|
| Step 2 | In the Screen section, choose one of the options for the Phone Background field: Default —Keeps the system default background. Download Picture —Displays a picture downloaded from a TFTP, FTP, or HTTPS server. When select this option, enter the URL for the picture in
                                                the Picture Download URL field. Logo —Displays a logo downloaded from a TFTP, FTP, or HTTPS server. When select this option, enter the URL for the logo image in
                                                the Logo URL field. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Phone_Background ua="na">Logo</Phone_Background> |
| Step 3 | Upload the custom wallpaper to a TFTP, HTTP, or HTTPS server. The image is a .jpg or .png file. Preferred dimension is 800x480 pixels. If the image is not the preferred size, user still
                                          can upload it but it will resize to fit the screen. |
| Step 4 | In the Picture Download URL field, enter the path where the wallpaper image has been uploaded. The URL must include the TFTP, HTTP, or HTTPS server name (or IP address), directory, and file name. Don't exceed 255 characters
                                          for the URL. Example: http:// 10.64.84.147/pictures/image04.jpg When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the new wallpaper and displays
                                          the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Picture_Download_URL ua="na">http://10.64.84.147/pictures/image04.jpg</Picture_Download_URL> |
| Step 5 | Upload the logo image to a TFTP, HTTP, or HTTPS server. The logo must be a .jpg or a .png file. The phone has a fixed display area. So, if the original logo size doesn't fit into
                                          the display area, you need to scale it to fit the screen. For the Cisco IP Phone 8800 Series, the logo display area is at
                                          the mid-center of the phone screen. The display area size of the Cisco IP Phone 8800 Series is 128x128. |
| Step 6 | In the Logo URL field, enter the path where the logo image has been uploaded. The URL must include the TFTP, HTTP, or HTTPS server name (or IP address), directory, and file name. Don't exceed 255 characters
                                          for the URL. Example: http://10.64.84.147/pictures/logo_image.jpg When you enter an incorrect URL to download a new logo, the phone fails to upgrade to the newer logo and displays the existing
                                          downloaded logo. If the phone does not have any logo downloaded earlier, it displays a gray screen. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Logo_URL ua="na">http://10.64.84.147/pictures/logo_image.jpg</Logo_URL> |
| Step 7 | Click Submit All Changes . The phone reboots after you change the background image URL. |

| Step 1 | On the phone web page, select Voice > User . The user can select User Login > Voice > User to add screen saver to the phone. |
|---|---|
| Step 2 | In the Screen section, set up the fields as described in Parameters for Screen Saver . |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Screen Saver Enable | Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Screen_Saver_Enable ua="rw">Yes</Screen_Saver_Enable> In the phone web interface, set this field to Yes to enable screen saver. Allowed values: Yes\|No Default: No |
| Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Enter the image path in the Picture Download URL field. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Screen_Saver_Type ua="rw">Clock</Screen_Saver_Type> In the phone web interface, select a screen saver. Allowed values: Clock\|Download Picture\|Logo Default: Clock |
| Screen Saver Wait | Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Screen_Saver_Wait ua="rw">300</Screen_Saver_Wait> In the phone web interface, set the time in seconds. Allowed values: An integer from 30 through 65000 Default: 300 |
| Picture Download URL | URL locating the (.png) file to display on the phone screen background. The image can display as the screen background, the screensaver, or at bootup depending on the settings of the Phone Background , Screen Saver Type , or Boot Display field. When you enter an incorrect URL to download a new image, the phone fails to update to the new image and displays the existing
                                             downloaded image. If the phone does not have any image downloaded earlier, it displays a gray screen. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Picture_Download_URL ua="rw">http://10.74.3.52/images/screensaver1.png</Picture_Download_URL> In the phone web interface, specify the URL where the picture is located. Allowed values: A valid URL not exceeding 255 characters Default: Empty |
| Logo URL | Enter a URL or path for the location where the logo image is saved. The logo image can display as the screen background, the
                                             screensaver, or at bootup depending on the settings of the Screen Saver Type , Boot Display , or Phone Background field. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Logo_URL ua="rw">http://10.74.3.52/images/Logo1.png</Logo_URL> In the phone web interface, specify the URL where the logo image is located. Allowed values: A valid URL not exceeding 255 characters Default: Empty |

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Screen section, select a duration for the Back Light Timer parameter. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Back_Light_Timer ua="rw">30s</Back_Light_Timer> The allowed values are 1m\|5m\|30m\|Always On. The default value is 5m (5 minutes). |
| Step 3 | In the Display Brightness field, enter an integer ranging from 4 to 15 for the desired brightness. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Display_Brightness ua="rw">15</Display_Brightness> The allowed value is an integer ranging from 4 through 15. The bigger the value, the brighter the screen display. The default
                                          value is 15. |
| Step 4 | Click Submit All Changes . |

| Step 1 | Edit the phone configuration file (cfg.xml) in a text or XML editor. |
|---|---|
| Step 2 | Add a value for the element <Device_Config_Version> in the cfg.xml file. For example: <Device_Config_Version ua="na">2021-01-05-v1</Device_Config_Version> Default: Empty Value range: 0 to 64 characters If the tag doesn't exist in the cfg.xml file or the parameter value is empty, then the Configuration version menu item doesn't display on the phone screen Product information . Note If the length of the assigned characters exceeds the width of the phone screen, the exceeded characters are truncated and
                                                      represented as an ellipsis (...) on the phone screen. | Note | If the length of the assigned characters exceeds the width of the phone screen, the exceeded characters are truncated and
                                                      represented as an ellipsis (...) on the phone screen. |
| Note | If the length of the assigned characters exceeds the width of the phone screen, the exceeded characters are truncated and
                                                      represented as an ellipsis (...) on the phone screen. |
| Step 3 | Save the changes to the cfg.xml file. |

| Note | If the length of the assigned characters exceeds the width of the phone screen, the exceeded characters are truncated and
                                                      represented as an ellipsis (...) on the phone screen. |
|---|---|

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Supplementary Services section, set the parameter Keep Focus On Active Call to Yes . You can also configure this parameter in the configuration file: <Keep_Focus_On_Active_Call ua="na">Yes</Keep_Focus_On_Active_Call> Allowed values: Yes and No Default: No |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > SIP . |
|---|---|
| Step 2 | In the Peripheral section, set the Peripheral Inventory Enable parameter to Yes . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Peripheral_Inventory_Enable ua="na">No</Peripheral_Inventory_Enable> When the parameter is set to Yes , the peripheral inventory headers are included in the SIP Register message. When set to No , the headers are not included in the SIP message. Default value of the parameter is No . When one peripheral is connected or disconnected to the phone, next scheduled Register provides the peripheral information
                                          in the Peripheral-Data header. All subsequent Registers do not carry peripheral information. The Peripheral-Data header is
                                          included for each peripheral, for example, if there are two headsets present, the header appears twice. |
| Step 3 | Click Submit All Changes . |