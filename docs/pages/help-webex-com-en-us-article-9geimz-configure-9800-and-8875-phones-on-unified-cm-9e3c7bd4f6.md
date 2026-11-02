---
doc_id: help-webex-com-en-us-article-9geimz-configure-9800-and-8875-phones-on-unified-cm-9e3c7bd4f6
source_url: https://help.webex.com/en-us/article/9geimz/Configure-9800-and-8875-phones-on-Unified-CM
retrieved_at: 2026-11-02T13:05:39.469835+00:00
---

## Phone feature configuration

You can set up phones to have a variety of features, based on the needs of your users. You
      can apply features to all phones, a group of phones, or to individual phones.

When you set up features, the Cisco Unified Communications Manager Administration window
      displays information that is applicable to all phones and information that is applicable to
      the phone model. The information that is specific to the phone model is in the Product
      Specific Configuration Layout area of the window.

For information on the fields applicable to all phone models, see the Cisco Unified
      Communications Manager documentation.

When you set a field, the window that you set the field in is important because there is a
      precedence to the windows. The precedence order is:

- Individual phones (highest precedence)

- Group of phones

- All phones (lowest precedence)

For example, if you don't want a specific set of users to access the phone web pages, but the
      rest of your users can access the pages, you can do the following:

- Enable access to the phone web pages for all users.

- Disable access to the phone web pages for each individual user, or set up a user group and
        disable access to the phone web pages for the group of users.

- If a specific user in the user group needs access to the phone web pages, you can enable
        it for that particular user.

Set up phone features for all phones

Sign into Cisco Unified Communications Manager Administration as an administrator.

Select System > Enterprise Phone Configuration .

Set the fields you want to change.

Check the Enable Enterprise Settings check box for any changed
          fields.

Click Save .

Click Apply Config .

Restart the phones.

This will impact all phones in your organization.

Set up phone features for a group of phones

Sign into Cisco Unified Communications Manager Administration as an administrator.

Select Device > Device Settings > Common Phone Profile .

Locate the profile that you want to set up.

Navigate to the Product Specific Configuration Layout pane and
          set the fields.

Check the Override Enterprise Settings check box for any changed
          fields.

Click Save .

Click Apply Config .

Restart the phones.

Set up phone features for a single phone

Sign into Cisco Unified Communications Manager Administration as an administrator.

Select Device > Phone .

Locate the phone associated with the user.

Navigate to the Product Specific Configuration Layout pane and
          set the fields.

Check the Override Enterprise/Common Phone Profile Settings check box for any changed fields.

Click Save .

Click Apply Config .

Restart the phone.

## Apply the custom wallpaper and logo

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

## Action button on 9800 Series

The Action button is the red button located at the top-right of the phone.
      It allows users to quickly access designated services, such as emergency or custom services.
      You can custom the button to initiate events that suit your specific use cases.

### Customize the Action button

The custom options for the Action button on Cisco Desk Phone 9800 Series require specific PhoneOS firmware support. See the following table for details:

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Customize the Action button settings with the following parameters based on your use
          cases.

There are three groups of parameters for the Action button, each corresponding to a
              service with a unique trigger. If a service trigger is specified in multiple groups,
              the settings in Group 1 take priority over those in Group 2 and 3, while Group 2 takes
              priority over Group 3.

Configure the following parameters:

Action Button Function : Select Emergency
                  Call .

Action Button Service Destination : Enter the phone number or
                the URI of the emergency service.

Action Button Service Name (Optional): Specify a name for
                the service associated with the action trigger. This name will be displayed in the
                on-screen message when the user presses the button, indicating which event will be
                initiated. If no name is specified, Emergency call will be used as the
                display name.

Dial Out Delay : Set the timeout period (in seconds) for the
                phone to initiate an emergency call after the trigger is detected. The default value
                is 5 seconds. If set to 0, the call is placed immediately upon detecting the
                trigger.

Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times .

Silent Emergency Call (Optional): By default, the emergency
                call functions as a two-way call, similar to other outgoing calls. When silent
                emergency call is enabled, the audio is silent on the caller side to avoid drawing
                attention during the onging call. Only the call recipient can end the silent
                emergency call.

During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                functions are inaccessible. The phone restores normal operation after the recipient
                ends the call.

Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key.

Configure the following parameters:

Action Button Function : Select Custom .

Action Button Service Destination :
                Enter the URL of the custom service. The URL must start with http:// or https:// , for example, https://10.11.20.159/path/service.xml .

Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name.

Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters.

For POST script examples and the syntax, see HTTP Post request for the Action button .

Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection.

Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times .

Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination .

Set the parameters in each group respectively. See the
              Emergency calls and Custom services sections above.

Configure the following parameters
              to assign multiple events to a trigger:

Action Button Function : Select Custom .

Action Button Service Destination : Enter the phone number
                  to call and the XML service URL in this format:

tel:<phonenumber or SIP URI> +
                  <serviceURL>

The URL must start with http:// or https:// .

Example: tel:1234 + https://10.11.20.159/path/service.xml

Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name.

Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters.

For POST script examples and the syntax, see HTTP Post request for the Action button .

Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection.

Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times .

Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination .

Silent Emergency Call (Optional): If you have included a
                  phone number or dialing URI in the service destination, enabling this feature will
                  silent emergency calls.

By default, the emergency call functions as a two-way call, similar to other
                  outgoing calls. When set to enabled, the audio is silent on the caller side to
                  avoid drawing attention during the onging call. Only the call recipient can end
                  the call.

During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                  while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                  functions are inaccessible. The phone restores normal operation after the
                  recipient ends the call.

Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key.

For more information about these parameters, see Parameters for the Action
            button .

Select Save .

Select Apply Config .

### References

#### Parameters for the Action button

The parameters are available in Enterprise Phone Configuration, Common Phone Profile, and
        individual phone configuration.

Default: Off

Options: Off, Emergency Call, Custom

You can configure the button with a specific service.

- Off : When set to Off, the Action button for single
                      service on the phone will not function.

- Emergency Call : Users can use the Action button to
                      place an emergency call, if configured.

- Custom : Users can use the Action button to access the
                      custom service, if configured.

When you set the field to Emergency Call or Custom , make sure that you enter the service
                    destination in the Action Button Service Destination field. Or, the phone will display a configuration error.

Default: Empty

Optionally specify a name for the service associated with the Action button.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered.

If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field.

Default: Empty

Provide the service destination in one of the following formats based on the
                    service assigned to the Action button:

For emergency call services, enter a telephone number or the URI of
                        emergency service.

When configure the button for a custom service, enter the service URL. The
                        URL must start with http:// or https:// . For example, https://10.11.20.159/path/service.xml .

To configure the button to initiate multiple events with a single trigger,
                        enter tel:<phonenumber or SIP URL> + <Service
                          RUL> . Example : tel:1234 +
                          https://10.11.20.159/path/service.xml .

Calling SIP URIs is also supported. Enter the URI in the format of tel: sip 4567@co.webex.com

If you enable the Action button without setting a valid service destination,
                    the user on the phone will see a message prompting for configuration. After the
                    user closes this notification, the warning icon will persist in the header of
                    the phone screen until the button is properly configured or disabled.

Phone numbers cannot be used as destinations for custom services. If you
                      configure the Action Button as Custom and enter a phone
                      number as the service destination, an alert message will display on the phone
                      indicating that the button is unconfigured. Instead, you can add a phone
                      number in this format tel:<phone number> , for
                      example, tel:1234 .

If you are not allowed to input a URL including ampersand (&), use %26 as a
                    replacement. For example, enter http://1.2.3.4/phone?a=1%26b=2%26c=3 instead of http://1.2.3.4/phone?a=1&b=2&c=3 .

Default: Empty

This setting works only when the Action Button
                        Function is set to Custom .

Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed.

If the service requires
                  authentication to access, make sure to enter the authentication secret in the Service Secret field. In the HTTP data, use the macro $SS as a reference to Service Secret.

For examples and the syntax, see HTTP Post request for the Action
                    button .

Default: Empty

A service secret can be an authentication secret, token or password. The
                    entered secret is displayed as a masked string and can be referenced using the
                    macro $SS in Custom Content Field and Action Button Service Destination .

Default: Single Press

Options: Single Press, Long Press, Press 3 times

Choose how users can place an emergency call or initiate a custom service using
                    the phone's Action button.

Single Press : Press the Action button to trigger the
                    associated call or service.

Long Press : Press the Action button down for at least 2
                    seconds to trigger the associated call or service.

Press 3 times : Press the Action button three times with
                    intervals of less than 2 seconds between each press to trigger the associated
                    call or service.

Don't repeat a trigger across multiple services, as the parameters with lower
                    priority will not function. The priority order, from highest to lowest, is as
                    follows: Group 1, Group 2, Group 3.

Default: 5

Options: 0 - 30

Set the timeout period, in seconds, for the phone to initiate an emergency call
                    or a custom action after the Action button is pressed.

Set it to 0 if you prefer the phone to place the call or initiate an event
                    immediately upon detecting the trigger, as specified by a single press, long
                    press, or triple presses on the button.

Default: Disabled

Options: Enabled, Disabled

Silent emergency call is designed for discreet assistance in dangerous
                    situations. It enables users to seek help without making any noise.

When enabled, users are able to place one-way calls with the Action button.

After the silent emergency call is placed, only the other party can end the
                        call. To avoid drawing attention during the ongoing call, the screen on
                        phone 9811 and 9841 will freeze, while
                        the screen on phone 9851, 9861, and 9871 will be turned off. The phone locks all
                          functions during a silent emergency call, by default. To allow users to
                          restore normal phone operation while maintaining the silent emergency
                          call, enable the Allow Silent Emergency Call
                            Retrieval feature.

When disabled, the emergency call functions as a two-way call, similar to
                        other outgoing calls.

Default: No

Options: Yes, No

Controls whether users can retrieve phone functionality during a silent
                    emergency call. By default, once a silent emergency call is initiated, the phone
                    locks all functions until the call recipient ends the call.

When this parameter is set to Yes , users can press any
                    key to restore normal phone operation while maintaining the emergency call. The
                    call audio remains silent unless the user increases the volume using the Volume
                    key.

#### HTTP Post request for the Action button

The Action button on Cisco Desk Phone 9800 Series can be configured to trigger XML applications through HTTP Post requests.

In Custom Content Field , enter your customized request script. You
        can specify either XML or JSON content type and include macros in the request. For example, $SS can be added to the script to retrieve the authentication secret,
        token, or password provided in the Service Secret field.

The following examples are in XML and JSON:

```
Sample #1: XML
--method POST
--header 'Content-Type: application/xml'
--header 'Authorization: Bearer username:$SS'
--body '<MetaData><Trigger>True</Trigger><Description>This is for HTTP POST XML</Description></MetaData>' 

Sample #2: JSON
--method POST
--header 'Content-Type: application/json'
--header 'Authorization: $SS'
--body '{"events":[{"evtid":"12345", "parameters": {"trigger":true}, "Description":"This is for HTTP POST JSON"}]}'
```

Cisco Unified Communications Manager (UCM) requires percent encoding for the reserved
          characters in accordance with RFC 3986.

The following script is an example using percent-encoded strings.

```
--method POST
--header %27Content-Type: application/xml%27
--body %27%3cMetaData%3e%3cTrigger%3eTrue%3c/Trigger%3e%3cDescription%3eThis is for HTTP POST XML%3c/Description%3e%3c/MetaData%3e%27
```

## Configure help desk for 9800 phones

You can enable the help desk feature and configure quick numbers for the phone users.

In the Cisco Unified Communications Manager Administration,  select one of the following windows:

- Select Device > Phone .

- Select Device > Device Settings > Common Phone Profile .

- Select System > Enterprise Phone Configuration .

Navigate to the Product Specific Configuration Layout area and set the following fields:

- Help Desk : Enable or disable the help desk feature. By default, the feature is disabled. When enabled, the user can press the Favorite button to access help desk screen where lists the quick numbers configured by you.

- Help Desk Customize Name : Customize the display name of the feature on the phone screen. If it's empty, the default name "Help Desk" is used.

- Name <n> : Determine the display name of the related quick number, where <n> represents the sequence number of the quick number. If it's empty, it will display the related quick number on the phone.

- Quick Number <n> : Specify a phone number or URI for the quick number, where <n> represents the sequence number of the quick number.

Click Save .

ThousandEyes Agent integration for phones supports the following models:

Supported features

On ThousandEyes portal, you can view the following information related to phones:

- Scheduled tests

- Dynamic tests for meetings on Webex, Microsoft Teams,  and Zoom via Office 365 calendar

- Dynamic tests for SIP calls

- Local networks

The Webex, Microsoft Teams, or Zoom meetings that you join through the phone are using Session Initiation Protocol (SIP). When setting up tests for your phones on the ThousandEyes application, make sure that you use the Webex template, instead of other meeting app templates.

Limitations

- Phone Wi-Fi statistics aren't available on the ThousandEyes portal.

- The Run Once option for instant tests isn't supported in PhoneOS.

- Real user tests are not supported for phones.

Before you begin

Get ThousandEyes Endpoint Agent licenses (either
            essential or advantage). You need one endpoint license per device.

Get the connection string from the ThousandEyes application.

Install the device package for your Unified Communications Manager version to make the ThousandEyes related parameters available. Download the device package at the CallManager Support page .

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To enable ThousandEyes Agent for all deployed phones, go to System > Enterprise Phone Configuration .

- To enable ThousandEyes Agent for phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To enable ThousandEyes Agent for an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

Set ThousandEyes Enable to True .

Copy the connection string from the ThousandEyes application and paste it into the Connection String field.

Select Save .

Select Apply Config .

## Office Hours

The Office Hours feature lets phones automatically power on, power off, or turn off the
        display based on a set schedule, helping organizations save energy, reduce costs, and
        optimize device performance. The information on this page applies to Cisco Desk Phone 9800 Series and Cisco Video Phone 8875 registered with Cisco Unified Communications Manager.

Two power-saving options are available on the phone to reduce power consumption during
          periods of inactivity.

Display Off Mode

When the Office Hours feature is enabled, the phone turns off its display according to
          the configured schedule. Users can light up the display by pressing any key on the phone.

Deep Sleep Mode

In Deep Sleep Mode, the phone automatically powers down during the designated periods.
          You can choose to enable Deep Sleep Mode exclusively for non-workdays, or for both
          non-workdays and non-working hours on workdays.

To wake up the phone, perform the appropriate action for your phone model:

- Press the Select button on the Navigation Cluster.

- Tap the Home button.

- Press the Power button.

While in Deep Sleep Mode, no calls, including emergency calls, can be made on the
              phone; and the Action button on the top-right of the device isn't accessible.

Display Off

Deep Sleep

(Controlled by phone)

Cisco Smart Power

(Deep Sleep controlled by switch)

### Enable your phone to manage its own power modes

By default, the Office Hours feature is enabled on your phone. The
        default office hours are set to 7:00 to 19:00 from Monday to Friday. The phone turns off the
        screen outside of the designated hours. You can customize working hours, workdays, and the
        power-saving modes — Display Off and Deep Sleep.

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Customize working hours and workdays to reflect the business hours of your users.

Enable Office Hours : By default, the Office Hours feature is
                enabled. If disabled, your phone won't enter power saving mode.

Workdays : The default workdays are Monday through Friday.
                Change the workdays as needed.

Working Hours Start and Working Hours
                  End : The default working hours are set to 7:00 to 19:00. Change the
                setting as needed.

See more information about these parameters , see Parameters for Office
            Hours .

Configure the settings for Display Off Mode for both working hours and non-working
          hours.

Cisco Desk Phone 9811 doesn't support Display Off Mode.

Display Off During Office Hours : By default, the phone
                display remains on during working hours. To enable the phone to enter Display Off
                Mode when inactive, select timeout period from the list.

Display Off Idle Timeout Outside Office Hours : Set the
                timeout period in minutes for the phone to automatically turn off the screen after
                being awakened during Display Off Mode.

LED Indicator In Display Off Mode : This setting determines
                whether to turn off the Front Arc LED when the phone enters Display Off Mode, both
                during or outside office hours. By default, the Front Arc LED remains illuminated
                after the phone enters Display Off Mode. When set to disabled, the Front Arc LED is
                off in Display Off Mode.

Line Key and Top 360 LED in Display Off Mode (Cisco Desk Phone 9841, 9851, 9861, and 9871): Controls whether the LEDs light up to notify users of phone statuses in Display Off mode. When disabled, both the Line Key LEDs on phone and Key Expansion Module (KEM) and Top 360 LEDs are off. When the corresponding LED is enabled, its indication behavior is the same as when the display is on. This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled.

Handset LED in Display Off Mode (Video Phone 8875): Controls whether the handset LED lights up to notify users of phone statuses in Display Off mode. When disabled, the handset LED is off. When enabled, its indication behavior is the same as when the display is on. This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled.

See more information about these parameters , see Parameters for Office
            Hours .

Configure the settings for Deep Sleep Mode for the 9800 Series phones.

Deep Sleep Mode on Cisco Video Phone 8875 and Cisco Desk Phone 9811 can only be enabled by Cisco switches through the smart power feature. To configure
              the smart power settings, follow the steps in Allow Cisco switch to manage power modes for your phone (smart power) .

Deep Sleep : Enable this feature to allow the phone to power
                off outside office hours.

Enter Deep Sleep After Working Hour End : Set the timeout
                period for the phone to automatically power off after the time specified in the Working Hours End field. The default setting is 60
                minutes.

Wakeup From Deep Sleep Before Working Hour Start : Set the
                timeout period for the phone to wake up from Deep Sleep Mode before the time
                specified in the Working Hours Start field. The default
                setting is 60 minutes.

Deep Sleep Idle Timeout : Sets timeout period for the phone
                to enter Deep Sleep Mode.

Enable Deep Sleep Audible Alert (Optional): If set to True,
                the phone plays audio tone to alert the user before it enters Deep Sleep Mode.

See more information about these parameters , see Parameters for Office
            Hours .

Select Save .

Select Apply Config .

### Allow Cisco switch to manage power modes for your phone (smart power)

The smart power feature allows Cisco Smart Switches to manage the phone's power modes via
          Power over Ethernet (PoE).

You can choose to let the switch manage the phone's power modes based on the schedules
          configured on the switch. The following table shows how the smart power settings interact
          with the phone's own Deep Sleep and Display Off settings configured in the phone's calling
          system.

Smart power is disabled. The phone follows the power saving configuration set on
                  its calling system.

Smart power is enabled only on non-work days.

On non-work days, the phone follows the display off and deep sleep schedules
                  configured on its calling system.

The switch wakes the phone from deep sleep following the phone's schedule.

Smart power is always enabled.

Smart power is always enabled.

The phone follows the display off and deep sleep schedules set on its calling
                  system.

The switch wakes the phone from deep sleep following the phone's schedule.

Smart power is always enabled.

Before you begin

Your phone uses Power over Ethernet (PoE) as the power source. If a power cube is
            connected, the smart power feature is automatically disabled.

Your phone is connected to a Cisco Smart Switch C9350 with IOS XE 17.18.2 or later.

- To use the Smart Power feature, you must first enable the office
            hours feature on your phone .

- Your Unified CM (UCM) cluster must be running version 14 or a
            later version and with the appropriate device package
          installed.

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Configure the following parameters:

Smart Power : Enable the smart power feature. The available
                options are:

- Disabled (Default): Disables the smart power
                  feature.

- Enabled for Non-work Day Only : Enables smart power only
                  on non-working days.

- Enabled for All Days : Enables smart power always, on both
                  work days and non-work days.

- Smart Power Override : Specify whether the
              switch can manage power modes based on the schedules configured on the switch,
              overriding the phone's settings configured in the phone's calling system.

- Smart Power Domain : Enter the smart power domain that the
              phone belongs to.

- Smart Power Endpoint Security Secret : Enter the password
              (shared secret) used for communication between the phone and the switch.

Select Save .

Select Apply Config .

### Parameters for Office Hours

Default: Enabled

Options: Enabled, Disabled

8875

9841

9851

9861

9871

Check this option to enable the Office Hours feature for Cisco Desk Phone 9800
                  Series. The Office Hours feature is designed to minimize power usage during
                  inactivity periods on the phone.

You can configure the phone to automatically turn off the screen (Display Off
                  Mode) or power off (Deep Sleep Mode) outside of the designated working periods.

Default: Monday through Friday

8875

9811

9841

9851

9861

9871

Customize the workdays by holding down the Ctrl key and selecting the desired
                  days.

During non-workdays, the phone will automatically turn off the screen. By
                  default, workdays are set from Monday to Friday.

This setting also applies to Deep Sleep Mode, if enabled. If you choose to enable
                  Deep Sleep Mode exclusively for non-workdays, the phone will power off during
                  those days. If you enable Deep Sleep Mode for all days, the phone will power off
                  during both non-workdays and non-working hours on workdays.

Set working hours for workdays using the Working Hour
                    Start and Working Hour End fields.

Default: 07:00

8875

9811

9841

9851

9861

9871

Set the start time for working hours using the 24-hour format. Outside of the
                  specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep is set to Enabled for All Days .

Examples: 09:00 for 09:00 am; 17:30 for 05:30 pm

Default: 19:00

8875

9811

9841

9851

9861

9871

Set the end time for working hours using the 24-hour format. Outside of the
                  specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep is set to Enabled for All Days .

Examples: 09:00 for 09:00 am; 17:30 for 05:30 pm

Ensure that the interval between the start and end time longer than 60
                    minutes.

Default: Disabled

Options: Disabled, In 1 minute, In 5 minutes, In 30 minutes

8875

9841

9851

9861

9871

Enable or disable Display Off Mode during office
                  hours. This feature is disabled by default, keeping the phone screen always on
                  during office hours. To enable this feature, select a timeout duration from the
                  available options. For example, if set to "In 5 minutes", the phone screen will
                  automatically turn off after 5 minutes of inactivity.

The LED indicator follows the setting of LED Indicator In Display Off
                    Mode .

Default: 5

Options: 1-60

8875

9841

9851

9861

9871

Default: Enabled

Options: Enabled, Disabled

8875

9841

9851

9861

9871

This setting determines whether to turn off the Front Arc LED on 9800 Series or
                  the Home button LED on 8875 when the phone enters Display Off Mode, both during or
                  outside office hours. By default (Enabled), the LED remains illuminated after the
                  phone enters Display Off Mode. When set to disabled, the LED is off in Display Off
                  Mode.

Default: Disabled

Options: Disabled, Enable Line Key LED, Enable Top 360 LED, Enable both Line Key and Top 360 LED

9841

9851

9861

9871

Controls whether the LEDs light up to notify users of phone statuses in Display Off mode. When disabled, both the Line Key LEDs on phone and Key Expansion Module (KEM) and Top 360 LEDs are off. When the corresponding LED is enabled, its indication behavior is the same as when the display is on.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled.

Default: Disabled

Options: Enabled, Disabled

8875

Controls whether the handset LED lights up to notify users of phone statuses in Display Off mode. When disabled, the handset LED is off. When enabled, its indication behavior is the same as when the display is on.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled.

When smart power isn't applied, the Deep Sleep settings work with the office
                    hours settings to determine the deep sleep schedule on 9841, 9851, 9861, and
                    9871.

When smart power is applied and Smart Power Override is disabled, the switch
                    also uses these settings to control the deep sleep mode on all applicable
                    phones.

Default: Disabled

Options: Disabled, Enabled for Non-Workdays Only, Enabled for All Days

9841

9851

9861

9871

Enable or disable Deep Sleep Mode on the phone.

This feature automatically powers off the phone during specified time periods.

This option works only when the Enabled Office Hour option
                  is checked. When disabled, the phone will not enter Deep Sleep Mode. If set to Enabled for Non-Workdays Only , the phone will power off
                  exclusively on non-workdays. For the specified workdays, the phone will turn off
                  the screen outside of the specified working hours. If set to Enabled
                    for All Days , the phone will power off during both non-workdays and
                  non-working hours on workdays.

Set working hours for workdays using the Working Hours
                    Start and Working Hours End fields.

Default: 60

Options: 0 - 360

8875

9811

9841

9851

9861

9871

The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled.

Default: 60

Options: 0 - 360

8875

9811

9841

9851

9861

9871

The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled.

Default: 5

Options: 0 - 60

8875

9811

9841

9851

9861

9871

This setting applies to the following two scenarios:

Ten minutes
                      before the scheduled deep sleep, a message pops up to notify the user that the
                      phone will power off in ten minutes, and a countdown starts. When it times
                      out, the phone powers off.

During the countdown period, if there is a
                      system activity such as an incoming call, firmware upgrade, or provisioning
                      resync, the countdown will restart. For example, if you have set this field to
                      20, the countdown will restart in 20 minutes after the activity completes. If
                      the phone restarts or its configuration is changed during the countdown, the
                      power-off notification appears again after the restart, and the countdown
                      continues.

After the specified idle timeout period, the phone displays a
                      power-off notification. The countdown shown in the notification is based on
                      the configured idle timeout value.

Examples

If you set the idle timeout to more than 10 minutes (for example, 20
                            minutes), a message appears after the phone has been idle for 20
                            minutes, notifying the user that the phone will power off in 10
                            minutes.

If you set the idle timeout to less than 10 minutes (for example, 6
                            minutes), a message appears after the phone has been idle for 6 minutes,
                            notifying the user that the phone will power off in 6 minutes.

During the countdown period, if there is a system activity such as
                      an incoming call, firmware upgrade, or provisioning resync, the countdown will
                      restart. For example, if you have set this field to 20, the countdown will
                      restart in 20 minutes after the activity completes.

The following notes apply to both scenarios described above.

If a user interacts with the phone during the countdown period, such as
                          answering or declining calls or pressing keys, the phone will not enter
                          Deep Sleep Mode for the rest of the day.

The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled.

Default: Unchecked

8875

9811

9841

9851

9861

9871

Enable or disable the phone to play audio tone to alert the user before it enters
                  Deep Sleep Mode.

Supported only on phones powered by Power over
                  Ethernet (PoE).

Default: Disabled

Options: Disabled, Enabled for Non-work Day Only, Enabled for All Days

8875

9811

9841

9851

9861

9871

Enable or disable the smart power feature. By default, smart power is disabled.
                    Set it to Non-work Day Only or All Days as needed to enable this feature.

The setting is effective only when a valid domain and security secret are
                    provided.

Default: No

Options: Yes, No

8875

9811

9841

9851

9861

9871

This setting determines whether the switch can override the phone's
                    power-saving configuration set by the calling system.

- No : The phone follows the power-saving configuration
                      set by its calling system.

- Yes : The switch fully controls the phone’s power
                      modes, overriding the configuration set by the phone's calling system.

8875

9811

9841

9851

9861

9871

The smart power domain that the phone belongs to. Max 128 characters.

8875

9811

9841

9851

9861

9871

The password (shared secret) used for communication between the phone and the
                    switch. Max 128 characters.

## Configure your phones for emergency calls (E911)

You can configure the E911 location service on Cisco phones to have an active location URI
        for emergency calls. The location of the phone can contain the street address, building
        number, floor number, room number, and other office location information. When you dial an
        emergency number, the emergency responder receives the phone location and a call-back
        number. If an emergency call disconnects, the emergency service uses the call-back number to
        reconnect to the caller.

Before you begin

Obtain an E911 location URL and a company ID for the phone from your emergency calling service provider (for example, Redsky admin).

Sign into Cisco Communication Manager Administration as an administrator.

Enable E911 service for the phone:

Perform one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Set HELD Support for Third-Party E911 to Enabled .

The default setting is Disabled .

Click Save .

Click Apply Config .

Configure a service profile:

Select User Management > User Settings > Service Profile .

Create a new service profile with a unique name. For example, "Emergency Calling Profile".

Configure the fields in the Emergency Calling Profile section.

For Emergency Numbers , enter the emergency service numbers, separated by commas. For example, 911,933 .

Click Save .

Associate an end user with the service profile (configured in Step 2):

Select User Management > End User .

Create a new user or modify an existing user.

In the Service Settings section, select the service profile that you created from the UC Service Profile drop-down list.

Click Save .

Create or modify an SIP dial rule for the emergency number:

Select Call Routing > Dial Rules > SIP Dial Rules .

Create a new SIP dial rule or modify an existing one.

If you choose to create a new SIP dial rule, select 7940_7960_OTHER from the Dial Pattern drop-down list.

Enter a name and relevant descriptions for the SIP dial rule.

In the Pattern Information section, add patterns of the emergency number (such as, "911" and "933").

Click Save .

Associate a phone with the user (configured in Step 3) and the SIP dial rule (Configured in Step 4):

Select Device > Phone to find an existing phone.

In the Device Information section, select User for the Owner field, and then select the user from the Owner User ID drop-down list.

In the Protocol Specific Information section, select the SIP dial rule from the SIP Dial Rules drop-down list.

Click Save .

Add the SIP Trunk to a RedSky server:

Select Device > Trunk .

Click Add New .

Select SIP Trunk from the Trunk Type drop-down list.

Select SIP from the Protocol Type drop-down list, and click Next .

In the SIP Information section, enter an IPv4 address of the RedSky server, fully qualified domain name, or DNS SRV record for the server or endpoint that you want to connect to the SIP trunk in the Destination Address field.

Assign a security profile from the SIP Trunk Security Profile drop-down list.

If you don't configure this field, a nonsecure profile will be assigned.

Select a Ping option enabled RedSky SIP profile from the SIP Profile drop-down list.

Click Save .

Configure route pattern to route E911 calls:

Select Call Routing > Route/Hunt > Route pattern .

Click Add New to create a new route pattern for the E911 calls.

Select E911 from the Route Pattern drop-down list.

Select the SIP Trunk (created in Step 6) from the Gateway/Route List drop-down list.

Click Save .

Upload RedSky certificates to CUCM:

Download the certificate file (.pem) from the Location Url (configured in Step 2).

You can enter a Browser to access the address.

Sign into Cisco Unified OS Administration.

Select Security > Certificate Management .

Click Upload Certificate .

Select Phone Trust from the Certificate
                Purpose drop-down list.

Click Browse to choose the file that you want to upload.

Click Upload File .

## Set up Do Not Disturb

When Do Not Disturb (DND) is turned on, either no audible rings occur during the ringing-in state of a call, or no audible or visual notifications of any type occur.

One exception is the Multilevel Precedence and Preemption (MLPP) call. The user still receives the priority calls on the phone even though the DND is turned on.

You can configure the phone with a softkey template with DND as one of the selected
        features.

For more information, see the " Configure Software-Based Endpoints " chapter in System Configuration Guide for Cisco Unified
            Communications Manager , Release 11.5(1) or later .

Sign into Cisco Unified Communications Manager Administration as an
          administrator.

Select Device > Phone .

Locate the phone that you will set up.

Navigate to the Do Not Disturb pane, set the following
          parameters:

- Do Not Disturb : This check box allows you to enable or
              disable DND on the phone.

Do not choose Call Reject if you want priority (MLPP) calls to ring this phone
                  when DND is turned on.

- DND Incoming Call Alert : Choose the type of alert (Disable,
              Flash Only or Beep Only) to play on a phone for incoming calls when DND is
              active.

For the parameters DND Option and DND Incoming Call Alert , both can be found in the Common Phone Profile window ( Device > Device Settings > Common Phone Profile ) and the Phone Configuration window ( Device > Phone ). The setting in the Phone Configuration window takes precedence.

Click Save .

## Set up forward all

You can set up the phone to redirect incoming calls to another phone number or to your
        voicemail by using the Cisco Unified Administration Manager.

Sign into Cisco Unified Communications Manager Administration.

Select Device > Phone .

Locate the phone that you will set up.

Select the target line from the Association pane.

Navigate to the Call Forward and Call Pickup Settings pane,
          enter a forwarded-to destination number in the field Forward
          All .

Click Save .

## Enable E911 services on your phones

Historically, Cisco Emergency Responder (CER) and RedSky have worked together to provide
        compliant E911 services. As an alternative, we now offer another method for connecting to
        RedSky using HELD. Beginning with PhoneOS release 4.0.1, this new method of using HELD with
        E911 services are disabled on phones by default and must be manually enabled in CUCM before
        users can access them. Before enabling E911 with this new HELD method, it is important to
        carefully assess all dependencies and perform a comprehensive end-to-end evaluation of your
        infrastructure.

The Webex App using HELD+ and PhoneOS devices using HELD can't coexist within the
                same architecture.

The E911 setting described on this page don't work with Cisco Emergency Responder
                (CER) and requires appropriate licensing and provisioning from the third-party E911
                service provider.

Before you begin

Before enabling E911 services on your phones, make sure that E911 has been properly
        provisioned in CUCM by following the procedures in Feature Configuration Guide for Cisco Unified
            Communications Manager .

Log in to Cisco Unified Communications Manager Administration.

Perform one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Set HELD Support for Third-Party E911 to Enabled .

The default setting is Disabled .

Click Save .

Click Apply Config .

## Set up join and direct transfer

You can set up the Join and Direct Transfer feature on a phone. If you enable the feature, the users can quickly add a person into a conference call or transfer a call through the Calls tab displayed in the new call session. You can also change the scope of the calls listed in the tab.

Do one of the following actions from Cisco Unified CM Administration:

Choose Device > Phone and locate the phone that you want to set up.

Choose Device > Device Settings > Common Phone Profile and locate the profile that you want to set up.

Choose System > Enterprise Phone Configuration .

Set up the field Join And Direct Transfer Policy :

The Calls tab displays in the new call session. It shows all active calls from all lines on the phone.

The Calls tab displays in the new call session. It only shows the active calls from a selected line.

The Calls tab in the new call session doesn't display.

Click Save .

## Add speed-dial numbers

Phones registered with Cisco Unified Communications Manager support the following two types of speed-dial numbers:

Speed dials : These are assigned to line keys and also appear in the Speed Dials list. Users can call the associated number by pressing the configured line key or by selecting it from the list. The number of supported speed dials depends on the number of physical and virtual line keys available on the phone.

Abbreviated dials : These allow users to dial the assigned short index to place a call to the associated number using the Abbr Dial softkey. The phone doesn't display an abbreviated dials list. The maximum number of supported abbreviated dials is up to 199.

In Cisco Unified Communications Manager Administration, select Device > Phone .

Locate the phone that you will set up.

In the Phone Configuration window, select Add a new
            SD .

- To configure a speed dial entry, enter the information in the Speed Dial (Button) Settings section.

- To configure an abbreviated dial entry, enter the information in the Speed Dial (Abbreviated Dial) Settings section.

Enter valid speed-dial numbers in the Number fields and a label in the Label fields.

Click Save .

What to do next

Ensure that you add Abbreviated Dial (AbbrDial) to the softkey template for Off Hook and Digits After First states in the Cisco Unified CM Administration.

## Configure Application Dial Rules

Cisco Unified Communications Manager supports application dial rules that allow you to add and sort the priority of dialing rules for applications. Application dial rules automatically strip numbers from or add numbers to telephone numbers that the user dials. For example, the dial rules automatically add the digit 9 in front of a 7-digit telephone number to provide access to an outside line.

In Cisco Unified Communications Manager Administration, go to Call Routing > Dial Rules > Application Dial Rules .

Click Add New to create a new application dial rule, or choose an existing application dial rule to edit it.

Fill in the following fields:

- Name This field comprises a unique name for the dial rule that can contain up to 20 alphanumeric characters and any combination of spaces, periods (.), hyphens (-), and underscore characters (_).

- Description This field comprises a brief description that you enter for the dial rule.

- Number Begins With This field comprises the initial digits of the directory numbers to which you want to apply this application dial rule.

- Number of Digits This required field comprises the initial digits of the directory numbers to which you want to apply this application dial rule.

- Total Digits to be Removed This required field comprises the number of digits that you want Cisco Unified Communications Manager to remove from directory numbers that apply to this dial rule.

- Prefix With Pattern This required field comprises the pattern to prepend to directory numbers that apply to this application dial rule.

- Application Dial Rule Priority This field displays when you enter the Prefix With Pattern information. The field allows you to set the priority order of the application dial rules.

Click Save .

## Configure park monitoring

Park monitoring is supported only when a phone parks a call. Park monitoring then monitors
        the status of a parked call. The park monitoring call alert does not clear until the parked
        call gets retrieved or is abandoned by the parked call. This parked call can be retrieved by
        using the same call alert on the phone that parked the call.

For more information about how to configure park monitoring in Cisco Unified Communications
        Manager, see Feature Configuration Guide for Cisco Unified
            Communications Manager, Release 12.5(1) or later .

Set up park monitoring timers

Cisco Unified Communications Manager Administration provides three cluster-wide service
        timer parameters for park monitoring: Park Monitoring Reversion Timer , Park Monitoring Periodic Reversion Timer , and Park Monitoring
          Forward No Retrieve Timer . Each service parameter includes a default and requires
        no special configuration. These timer parameters are for park monitoring only; the Call Park Display Timer and Call Park Reversion Timer are not used for park monitoring. See the following table for descriptions of these
        parameters.

Configure the timers in the Cisco Unified Communications Manager Service Parameters page.

In Cisco Unified Communications Manager Administration,
      choose System > Service
        Parameters .

Select a server for the phone and the service Cisco CallManager
            (Active) .

In the Clusterwide Parameters (Feature - General) section, set
          the fields as described in the following table.

This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks an active call on the
                      phone, and a reminder is issued when the timer expires.

Default is 60 seconds.

You can override the value that this service parameter specifies on a
                      per-line basis in the Park Monitoring section of the Directory Number Configuration window (in Cisco
                      Unified Communications Manager Administration, choose Call Routing > Directory Number ). Specify a value of 0 to immediately utilize the periodic
                      reversion interval that the Park Monitoring Periodic Reversion
                        Timer service parameter specifies. (See the description that
                      follows.) For example, if this parameter is set to zero and the Park Monitoring Periodic Reversion Timer is set to
                      15, the user is immediately prompted about the parked call and every 15
                      seconds thereafter until the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) expires.

This parameter determines the interval (in seconds) that Cisco Unified
                      Communications Manager waits before prompting the user again that a call is
                      parked. To connect to the parked call, the user can simply go off-hook during
                      one of these prompts. Cisco Unified Communications Manager continues to prompt
                      the user about the parked call as long as the call remains parked and until
                      the time that the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) specifies expires.
                      Specify a value of 0 to disable periodic prompts about the parked call.

Default is 30 seconds.

This parameter determines the number of seconds that park reminder
                      notifications occur before the parked call forwards to the Park
                        Monitoring Forward No Retrieve destination that is specified in
                      the parker's Directory Number Configuration window. (If
                      no forward destination is provided in Cisco Unified Communications Manager
                      Administration, the call returns to the line that parked the call.) This timer
                      starts when the time that the call is parked. When Park Monitoring
                        Reversion Timer and Park Monitoring Forward No
                        Retrieve Timer expire, the call is removed from park and
                      forwards to the specified destination or returns to the parker line.

Default is 300 seconds.

Set up park monitoring for directory numbers

The Directory Number Configuration window contains a Park
          Monitoring area where you can configure the three parameters.

In Cisco
      Unified Communications Manager Administration, choose Call
        Routing > Directory Number .

Click Find and select the directory number on which you want to
          configure the park monitoring.

In the Park Monitoring section, set the fields as described in
          the following table.

Park Monitoring Forward No Retrieve Destination External

When the parkee is an external party, the call forwards to the specified
                      destination in the parker's Park Monitoring Forward No Retrieve
                        Destination External parameter. If the field is empty, the
                      parkee is redirected to the parker line.

Park Monitoring Forward No Retrieve Destination Internal

When the parkee is an internal party, the call forwards to the specified
                      destination in the parker’s Park Monitoring Forward No Retrieve
                        Destination Internal parameter. If the field is empty, the
                      parkee is redirected to the parker line.

Park Monitoring Reversion Timer

This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks a call on the phone,
                      and a reminder is issued when the timer expires.

Default: 60 seconds

If you configure a nonzero value, this value overrides the value of this
                      parameter set in the Service Parameters window.
                      However, if you configure a value of 0 here, then the value in the Service Parameters window is used.

Set up park monitoring for hunt lists

When a call that was routed via the hunt list is parked, the Park Monitoring
          Forward No Retrieve Destination parameter value is used (unless it is empty) when
        the Park Monitoring Forward No Retrieve Timer expires.

In Cisco
      Unified Communications Manager Administration, choose Call
        Routing > Route/Hunt > Hunt
          Pilot .

Click Find and select the hunt pilot on which you want to
          configure the park monitoring.

Set the Park Monitoring Forward No Retrieve Destination parameter.

If the field is empty, the call forwards to the destination that is configured in the Directory Number Configuration window when the Park
              Monitoring Forward No Retrieve Timer expires.

## Set up hold reversion

When the user places an active call on hold and the configured time limit expires, the Cisco Unified Communications Manager generates an alert on the phone, such as ring or beep, to remind the user to handle the call. The held call becomes a reverted call when the hold duration exceeds the configured time limit. For more information about the Hold Reversion feature, see Features and Services Guide for Cisco Unified Communications Manager .

## Set up music on hold

When the user places an active call on hold, the held call plays a music streamed from the Music on Hold server. For more information about the Music On Hold feature, see Features and Services Guide for Cisco Unified Communications Manager .

## Set up call recording

You can enable the call recording feature on a phone so that the users can record an active call or call conference.

Only the user who triggers the call recording might receive an audible alert to indicate
        that the call is being recording. The other connected parties don't receive any audible
        alert for the recording.

You can set whether the alert sound will be audible to both the user who triggers the
        recording and to other connected parties.

When an active call is being recorded, the user can receive or place intercom calls. However, if the user places an intercom call, the active call is put on hold. This action causes the recording session to terminate.

For more information, see the Monitoring and Recording section in Feature Configuration Guide for Cisco Unified
            Communications Manager, Release 15 and SUs .

In Cisco Unified Communications Manager Administration, add the softkey Record (Record) .

For more information, see Configure feature soft buttons with a softkey template .

Apply the new or updated softkey template to a phone.

For more information, see Apply a softkey template to a phone .

Enable Built in Bridge field for the phone.

Choose Device > Phone .

Click Find to locate the phone that you want to configure.

From the Built in Bridge drop-down list, choose On to enable it

Click Save .

Configure a phone line for recording.

Choose Device > Phone .

Click Find to locate the phone that you configured.

In the left Association pane, click a phone line for the recording setup.

From the Recording Option drop-down list, choose Selective Call Recording Enabled .

From the Recording Profile drop-down list, choose a recording profile that is configured for the line.

For more information about how to create a new recording profile, see the Create a Recording Profile section in Feature Configuration Guide for Cisco Unified
                  Communications Manager, Release 15 and SUs .

Click Save .

## Set up password protection for the settings menu

You can secure the phone settings menu with the password protection. Once enabled, the users are required to provide the correct password to access the settings menu.

Sign into Cisco Unified Communications Manager Administration as an administrator.

Select Device > Device Settings > Common Phone Profile

Locate the profile that you want to set up.

Navigate to the Common Phone Profile Information pane and set up a password in the Local Phone Unlock Password field.

Click Save .

Click Apply Config .

Restart the phones.

## Record call log from shared line

You can determine whether to record a shared line call in the call history. When enabled, users can recognize the shared call in the call history by the keyword "remote".

In Cisco Unified Communications Manager Administration, select Device > Phone .

Locate the phone that you will set up.

In the Product Specific Configuration Layout section, configure the field Record Call Log from Shared Line to enable or disable the feature.

Default value: Disabled

Click Save .

## Set up barge

You can set up the phone to allow a user to join a remotely active (conference) call on a shared line.

For more information about how to set up barge in Cisco Unified Communications Manager, see Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1) or later .

## Set up privacy on shared lines

You can set up the privacy on shared lines to determine whether the users to view the call status and to barge into a call or conference.

For more information about how to set up the privacy feature in Cisco Unified Communications Manager, see Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1) or later .

## Set up Malicious Call Identification (MCID)

You can configure the Malicious Call Identification (MCID) feature to track troublesome or
        threatening calls. Users can report these calls by requesting that Cisco Unified Communications Manager (Unified CM) identify and register the source of the incoming call in the network.

For more information about how to set up MCID in Cisco Unified CM, see Feature Configuration Guide for Cisco Unified
          Communications Manager, Release 14 and SUs .

## Enable LED indication for missed calls

By default, the Top 360 LED is disabled for missed calls. You can enable the LED indication if you want to receive the missed call alerting more explicitly. Typically, you can find the missed call on the phone screen.

This topic is only available for Cisco Desk Phone 9800 Series.

Before you begin

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

Set Missed Call Led Alert to Enabled .

Default: Disabled.

Select Save .

Select Apply Config .

## Enable voicemail LED indicators for other lines

By default, the Top 360 LED lights up only on the primary line when the phone has new voicemails. You can also enable the LED indicator for other lines (non-primary lines) on the phone.

In Unified Communications Manager Administration, select Device > Phone .

Locate the phone that you will set up.

In the left Association area, click Add a New DN to create a new directory number or click an existing directory number to modify it.

The Directory Number Configuration window displays.

In the Line <n> on Device section, set the Visual Message Waiting Indicator Policy to Light and Prompt .

Configure the remaining fields in the Directory Number Configuration window.

Click Save .

The setting takes effect on the configured line.

(Optional) If you want to apply the settings on the corporate level, do the following:

Select System > Service Parameters .

Select a node from the Server drop-down list.

Select Cisco CallManager from the Service drop-down list.

In the Clusterwide Parameters (Feature - General) section, set Message Waiting Lamp Policy to Light and Prompt .

Click Save .

## Configure Cisco IPMA

The Unified Communications Manager Assistant feature is a plug-in that an assistant can use
        to handle calls on behalf of a manager, intercept manager calls, and route them
        appropriately.

Manager Assistant supports up to 3500 managers and 3500 assistants. To accommodate this
        number of users, you can configure up to three Manager Assistant applications in one Unified
        Communications Manager cluster and assign managers and assistants to each instance of the
        application.

Manager Assistant supports shared line support and proxy line support.

For information about administration configuration for IPMA, see Manager Assistant in Feature Configuration Guide for
            Cisco Unified Communications Manager

## Control the settings menu access

As an example, the Settings menu on Cisco Desk Phone 9811, 9841, 9851, and 9861 includes the following configuration menus.

- Recents: Shows the recent calls list where the user can view, edit, or delete the call
          history.

- EM: Signs in to a different phone in your network and have it act the same as your phone
          if extension mobility is configured.

- About this device: Shows basic information about the phone device.

- Issues and diagnostics: Displays whether the phone has any issue. Provides the
          statistics information of the phone. Provides the menu for the users to submit problem
          reports.

- Audio: Specifies a different ringtone to a specific line, adjusts audio volume, and
              configures the noise removal feature.

- Bluetooth: Enables or disables the Bluetooth connectivity.

- Screen: Adjusts the phone's default brightness. Customize the appearance, including
              logo, wall paper, and color theme if available.

- Network settings: Provides options for viewing and configuring network settings such
              as Wi-Fi and Ethernet.

- Network status: Provides an overview of the network connectivity.

- Security setup: Provides options for viewing and configuring security settings such
              as security mode and Locally Significant Certificate (LSC) update.

- Restart: Restarts the phone.

- Reset security certificate: Resets security certificate to factory defaults.

- Factory reset: Restores the phone to factory settings. All data will be erased and
              the user must reactivate the phone after the factory reset.

You can control whether a phone has full or partial access to the Settings menu by using Cisco Unified Communications Manager
        Administration.

In Cisco Unified Communications Manager Administration, select Device > Phone .

Locate the phone that you will set up.

Navigate to the Product Specific Configuration area and set the Settings Access field.

Enabled:

Allows full access to the Settings menu.

Disabled:

Allows access only to the following menus.

- EM (or EMCC if extension mobility
                  is configured)

- Network and service (if any other custom service or VPN
                  is configured)

This option prevents access to other options in the Settings menu.

Restricted:

Allows access only to the following menus.

- Recents

- EM (or EMCC if extension mobility
                  is configured)

- User preferences

- Network and service (if any other custom service or VPN
                  is configured)

- Accessibility

Allows access only to the following menus.

- EM (or EMCC if extension mobility
                  is configured)

- Audio

- Screen

- Network and service (if any other custom service or VPN
                  is configured)

- Accessibility

This option prevents access to other options in the Settings menu.

Select Save .

Select Apply Config .

Restart the phone.

## Set up date and time group

You can select a predefined date and time group for a device pool in Cisco Unified Communications Manager Administration. If your desired group is not in the list, you can create a new group or modify an
        existing one.

In Cisco Unified Communications Manager Administration, select System > Device Pool .

Locate the device pool that you need to set up.

Navigate to the Roaming Sensitive Settings area and select a
          group from the Date/Time Group field.

Select Save .

(Optional) If you want to create or modify a Date/Time group, do the following:

Select System > Date/Time Group .

Navigate to the Date/Time Group Information area, set the
              following parameters:

- Group Name : Enter a unique for the Date/Time group.

- Time Zone : Select a proper time zone for the Date/Time
                  group.

- Time Format : Select a time format that the phone
                  displays.

The settings to the parameters Separator and Date Format don't take effect.

Select Save .

## Set up wideband codec

By default, the G.722 codec is enabled for your phone. If Cisco Unified Communications Manager (Unified CM) is configured to use G.722 and the far endpoint supports G.722, the call connects using the G.722 codec in place of G.711.

This situation occurs regardless of whether the user has enabled a wideband headset or wideband handset. If either the headset or handset is enabled, the user may notice greater audio sensitivity during the call. Greater sensitivity means improved audio clarity but also means that the far endpoint can hear more background noise, such as rustling papers or nearby conversations. Even without a wideband headset or handset, some users may find the additional sensitivity of G.722 distracting.

The Advertise G.722 and iSAC Codec service parameter affects whether wideband support exists for all devices that register with this Cisco Unified CM server or for a specific phone.

To configure
			 wideband support for all devices:

On Cisco Unified Communications Manager Administration, click System > Enterprise Parameters

Set the Advertise G.722 and iSAC Codec field.

The default value of this enterprise parameter is True , which means that all Cisco IP Phone Models that register to this Cisco Unified CM advertise G.722. If each endpoint in an attempted call supports G.722 in the capabilities set, Cisco Unified CM uses that codec for the call whenever possible.

To configure
			 wideband support for a specific device:

On Cisco Unified Communications Manager Administration, choose Device > Phone .

Set the Advertise G.722 and iSAC Codec parameter in the Product Specific Configuration area.

The default value of this product-specific parameter is to use the value that the enterprise parameter specifies. If you want to override this on a per-phone basis, choose Enabled or Disabled

## Set up the audio and video port range for 8875 phones

Audio and video traffic can be sent to different RTP port ranges in order to improve Quality of Service (QoS).

The following fields control the port ranges in Cisco Unified Communications Manager Administration:

Audio ports

Start Media Port (default: 16384)

Stop Media Port (default: 32766)

Video ports

Start Video (This is to set the video start port).

Minimum: 2048

Maximum: 65535

Stop Video (This is to set the video stop port)

Minimum: 2048

Maximum: 65535

The following rules apply when configuring the video port fields:

After the Start Video RTP Port and Stop Video RTP Port are configured, the phone uses ports within the video port range for video traffic. The audio traffic uses the media ports.

If the audio and video port ranges overlap, the overlapped ports carry both audio and video traffic. If the video port range isn’t configured correctly, the phone uses the configured audio ports for both audio and video traffic.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

In Cisco Unified Communications Manager Administration, select Device > Device Settings > SIP Profile

Set the Start Media Port and Stop Media Port fields for the audio port range.

Select Save .

Navigate to one of the following windows:

System > Enterprise Phone Configuration

Device > Device Settings > Common Phone Profile

Device > Phone > Phone Configuration

Set the Start Video RTP Port and Stop Video RTP Port fields for the range of ports required.

The value for Stop Video RTP Port must be at least 16 larger
              than the value for Start Video RTP Port .

Select Save .

## Video transmit resolution supported on 8875 phones

Cisco Video Phone 8875 supports the following video formats:

1080p (1920x1080)

720p (1280x720)

600p (1024x600)–Default

WVGA (800x480)

VGA (640x480)

360p (640x360)

CIF (352x288)

240p (432x240)

SIF (352x240)

QCIF (176x144)

The phone negotiate the best bandwidth and resolution based on the phone configuration and phone screen limitations.

The following table shows the resolutions, frames per second, and video bit rate range for each of the supported video types.

Video type

Video resolution

Frames per second (fps)

Video bit rate range

720p

1280 x 720

30

2040–3750 kbps

720p

1280 x 720

15

1185–3750 kbps

WVGA

800 x 480

30

990–1500 kbps

WVGA

800 x 480

15

525–1500 kbps

VGA

640 x 480

30

520–1500 kbps

VGA

640 x 480

15

280–1500 kbps

360p

640 x 360

30

600–1350 kbps

360p

640 x 360

15

315–1350 kbps

240p

432 x 240

30

270–525 kbps

240p

432 x 240

15

96–525 kbps

CIF

352 x 288

30

200–350 kbps

CIF

352 x 288

15

120–350 kbps

SIF

352 x 240

30

200–350 kbps

SIF

352 x 240

15

120–350 kbps

QCIF

176 x 144

30

94–350 kbps

QCIF

176 x 144

15

64–350 kbps

QCIF

## Enable web access for a phone

You can enable web access for a Cisco Unified IP Phone.

For more information about how to enable web access for a phone in Cisco Unified
        Communications Manager, see Feature Configuration Guide for Cisco Unified
          Communications Manager, Release 12.5(1) or later .

## Use problem report tool

Users can submit problem reports to you with the Problem Report Tool.

The Problem Report Tool logs are required by Cisco TAC when troubleshooting problems. The
        logs are cleared if you restart the phone. Collect the logs before you restart the
        phones.

To issue a problem report, users access the Problem Report Tool and provide the date and time
      that the problem occurred, and a description of the problem.

If the PRT upload fails, you can access the PRT file for the phone from the URL http:// <phone-ip-address> /FS/ <prt-file-name> . This
      URL is displayed on the phone in the following cases:

- If the phone is in the factory default state. The URL is active for 1 hour. After 1 hour,
        the user should try to submit the phone logs again.

- If the phone has downloaded a configuration file and the call control system allows web
        access to the phone.

You must add a server address to the Customer Support Upload URL field on Cisco Unified
            Communications Manager.

- The phone isn't assigned with an IP address.

If you are deploying devices with Mobile and Remote Access (MRA) through Expressway, you must
      also add the PRT server address to the HTTP Server Allow list on the Expressway server.

Configure a customer support upload URL

You must use a server with an upload script to receive PRT files. The PRT uses an HTTP POST
        mechanism, with the following parameters included in the upload (utilizing multipart MIME
        encoding):

- devicename (example: “SEP001122334455”)

- serialno (example: “FCH12345ABC”)

- username (the username configured in Cisco Unified Communications Manager, the device
          owner)

- prt_file (example: “probrep-20141021-162840.tar.gz”)

A sample script is shown below. This script is provided for reference only. Cisco does not
        provide support for the upload script installed on a customer's server.

<?php

// NOTE: you may need to edit your php.ini file to allow larger

// size file uploads to work.

// Modify the setting for upload_max_filesize

// I used: upload_max_filesize = 20M

// Retrieve the name of the uploaded file

$filename = basename($_FILES['prt_file']['name']);

// Get rid of quotes around the device name, serial number and username if they
          exist

$devicename = $_POST['devicename'];

$devicename = trim($devicename, "'\"");

$serialno = $_POST['serialno'];

$serialno = trim($serialno, "'\"");

$username = $_POST['username'];

$username = trim($username, "'\"");

// where to put the file

$fullfilename = "/var/prtuploads/".$filename;

// If the file upload is unsuccessful, return a 500 error and

// inform the user to try again

if(!move_uploaded_file($_FILES['prt_file']['tmp_name'], $fullfilename))
        {

header("HTTP/1.0 500 Internal Server Error");

die("Error: You must select a file to upload.");

}

?>

The phones only support HTTP URLs.

Set up a server that can run your PRT upload script.

Write a script that can handle the parameters listed above, or edit the provided sample
          script to suit your needs.

Upload your script to your server.

In Cisco Unified Communications Manager, go to the Product Specific
            Configuration Layout area of the individual device configuration window,
          Common Phone Profile window, or Enterprise Phone Configuration window.

Check Customer support upload URL and enter your upload server
          URL.

http://example.com/prtscript.php

Save your changes.

## IPv6 ready logo setup

Define the IPv6 interface identifier for the device. The interface identifier you choose,
        either MAC or Opaque, will determine the method that is used for generating part of the IPv6
        address. This is applicable to both link-local IPv6 addresses and Stateless Address Auto
        Configuration (SLAAC) addresses. The address contains a 64-bit prefix and a 64-bit interface
        identifier generated by the device. With MAC, an EUI-64 based interface identifier is
        generated, as described in RFC-2373. With Opaque, a random 64-bit interface identifier is
        generated as described in RFC-7217 on the first boot of the device, and this is used
        forever, or until factory reset.

## Set the phone to always display the multi-line interface

The Always Use Multi-line Mode parameter is only available on Cisco
        Desk Phone 9841, 9851, and 9861. It ensures a consistent user experience by forcing the
        phone to always display the multi-line layout.

By default, the phone displays the multi-line interface only when multiple lines or other
        line key features are configured. When Always Use Multi-line Mode is enabled, the phone uses
        the multi-line layout even if only a single line is configured.

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Set the Always Use Multi-line Mode field to Enabled .

Select Save .

Select Apply Config .

## Enable xAPI on your phones

xAPI is a set of APIs used to monitor, manage, and control PhoneOS-based devices. In this
          release, we are introducing xAPI as a new option for customers and partners to manage
          phones and build custom solutions. Customers and partners can access xAPI through HTTP or
          HTTPS.

Cisco Desk Phone 9811 doesn't support this feature on PhoneOS
          4.0.1 or earlier.

The following features are now supported on phones registered to Webex Calling, Cisco
          Unified CM, or Cisco BroadWorks:

Retrieve basic device information and status, and subscribe to phone events

Perform device reboot and factory reset

Simulate hard key presses and screen touch operations

Capture device screens

Initiate calls

For information about the supported xAPIs and the related documentation, see https://phoneos.cisco.com .

Before you begin

- Your phone is running PhoneOS 3.5 or a later version.

- Your Unified CM (UCM) cluster must be running version 14 or a
            later version and with the appropriate device package
          installed.

- Prepare an HTTP client and HTTP server for feedback collection.

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Configure the following parameters:

Web Access : Set the Web Access field to Enabled .

HTTPs Server : Choose HTTP and HTTPS
                  Enabled to allow both protocols, or HTTPS Only to allow secure connections only, based on your server’s configuration.

xAPI Admin User Name : Enter the administrator username used
                to authenticate xAPI requests to the phone.

xAPI Admin Password : Enter the password associated with the
                xAPI administrator username to authorize remote access and management.

Select Save .

Select Apply Config .

## Enable 9800 Series to use the video capability on Webex

The Companion mode allows the phone to participate in video meetings or calls by using the
        Webex App for video. Users can send and receive video or share content through the Webex App
        while keeping audio on the phone.

By default, this feature is disabled on the phone.

Before you begin

- The phone is running PhoneOS 3.6 or a later version and registered in personal mode.
          This feature isn't supported on Workspace phones.

- Your Unified CM (UCM) cluster must be running version 14 or a
            later version and with the appropriate device package
          installed.

- The user is running Webex App 45.11 or later on Windows OS. This feature isn't supported
          on Webex App for macOS.

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Set Video Capability on Webex to Enabled .

Select Save .

Select Apply Config .

## Set minimum ringer volume

You can define a minimum ringer volume for phones to help ensure incoming calls are not
        missed. When configured, attempts to reduce the ringer volume below the minimum are
        blocked.

Log in to Cisco Unified Communications Manager Administration.

Go to Device > Phone .

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Choose a value from the Minimum Ring Volume drop-down
          list.

The default setting is 0-Silent , which allows users to mute the
          ringer. If a minimum volume is set, the phone will display a notification when users reach
          the minimum level.

Select Save .

Select Apply Config .

## Configure MARI and FEC for media quality

By default, Media Adaptation and Resilience Implementation (MARI) and Forward Error
        Correction (FEC) are enabled on your phones to dynamically maintain optimal media
        quality.

MARI monitors the network conditions in real time and dynamically executes corrective
        algorithms to maintain optimal quality of experience in lossy networks. MARI may apply Rate
        Adaptation or Forward Error Correction based on network conditions.

FEC is a resilience mechanism used to recover lost packets without the need for
        retransmission. FEC adds extra packets to the original media stream so that the media
        receiver can reconstruct the missing data with these packets to provide better audio or
        video quality in lossy networks.

Because FEC increases bandwidth usage, it may negatively impact media quality in
              congested or bandwidth-constrained networks. You can decide whether to disable it
              based on your network conditions.

CUCM by default doesn't support all SDP attributes, especially custom or
              vendor-specific ones like MARI attributes. For MARI to work, configure the SDP
                Transparency Profile that your devices use to allow passing all unknown
              attributes.

Log in to Cisco Unified Communications Manager Administration.

Go to Device > Phone .

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Enable or disable MARI and MARI FEC based
          on your network conditions.

Select Save .

Select Apply Config .

### Configure SDP Transparency Profile

SDP Transparency Profiles contain a set of rules for declarative SDP attributes that allow
        the system to pass through declarative attributes that are not natively supported by Unified
        Communications Manager from the ingress to the egress call leg. Without an SDP transparency
        profile, Unified Communications Manager drops non-supported SDP attributes.

You can configure SDP transparency profiles with the MARI rules and apply them to your
        phones via the SIP profile. In order for the SDP transparency profile to be applied, both
        call legs must be SIP.

For more information about SDP Transparency Profile, see Feature Configuration Guide for Cisco Unified
            Communications Manager .

Configure your SDP transparency profile or create a new one with MARI attributes.

From Cisco Unified CM Administration, choose Device > Device Settings > SDP Transparency Profile .

Open your SDP profile to configure it.

If you don't have any SDP transparency profile configured, click Add
                  New and enter a name and description.

In the Attribute Information pane, create rules with the
              following attributes:

Click Save .

Apply your SDP transparency profile to the SIP profile that your phones use.

Choose Device > Device Settings > SIP Profile .

Find and open your SIP profile.

In the SDP Information section, select your SDP transparency
              profile in the SDP Transparency Profile drop-down list.

Click Save .

## Enable Acoustic Shock Protection

The Acoustic Shock Protection parameter is only available on Cisco Desk Phone 9861 and 9871 and Cisco Video Phone 8875. It protects users from sudden loud sounds during calls.

By default, this parameter is disabled. When enabled, this setting is read-only in the Settings menu, and it overrides all the other incoming audio options on the phone.

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

Set the Acoustic Shock Protection field to Enabled .

Select Save .

Select Apply Config .

| 1 | Sign into Cisco Unified Communications Manager Administration as an administrator. |
|---|---|
| 2 | Select System > Enterprise Phone Configuration . |
| 3 | Set the fields you want to change. |
| 4 | Check the Enable Enterprise Settings check box for any changed
          fields. |
| 5 | Click Save . |
| 6 | Click Apply Config . |
| 7 | Restart the phones. This will impact all phones in your organization. |

| 1 | Sign into Cisco Unified Communications Manager Administration as an administrator. |
|---|---|
| 2 | Select Device > Device Settings > Common Phone Profile . |
| 3 | Locate the profile that you want to set up. |
| 4 | Navigate to the Product Specific Configuration Layout pane and
          set the fields. |
| 5 | Check the Override Enterprise Settings check box for any changed
          fields. |
| 6 | Click Save . |
| 7 | Click Apply Config . |
| 8 | Restart the phones. |

| 1 | Sign into Cisco Unified Communications Manager Administration as an administrator. |
|---|---|
| 2 | Select Device > Phone . |
| 3 | Locate the phone associated with the user. |
| 4 | Navigate to the Product Specific Configuration Layout pane and
          set the fields. |
| 5 | Check the Override Enterprise/Common Phone Profile Settings check box for any changed fields. |
| 6 | Click Save . |
| 7 | Click Apply Config . |
| 8 | Restart the phone. |

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

| Feature | Required firmware version |
|---|---|
| Emergency call | PhoneOS 3.0.1 and later |
| Custom service | PhoneOS 3.2.1 and later |
| Multiple triggers | PhoneOS 3.3.1 and later |
| HTTP Post | PhoneOS 3.3.1 and later |
| Multiple events on a single trigger | PhoneOS 3.4.1 and later |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 3 | Customize the Action button settings with the following parameters based on your use
          cases. There are three groups of parameters for the Action button, each corresponding to a
              service with a unique trigger. If a service trigger is specified in multiple groups,
              the settings in Group 1 take priority over those in Group 2 and 3, while Group 2 takes
              priority over Group 3. Emergency calls Configure the following parameters: Action Button Function : Select Emergency
                  Call . Action Button Service Destination : Enter the phone number or
                the URI of the emergency service. Action Button Service Name (Optional): Specify a name for
                the service associated with the action trigger. This name will be displayed in the
                on-screen message when the user presses the button, indicating which event will be
                initiated. If no name is specified, Emergency call will be used as the
                display name. Dial Out Delay : Set the timeout period (in seconds) for the
                phone to initiate an emergency call after the trigger is detected. The default value
                is 5 seconds. If set to 0, the call is placed immediately upon detecting the
                trigger. Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times . Silent Emergency Call (Optional): By default, the emergency
                call functions as a two-way call, similar to other outgoing calls. When silent
                emergency call is enabled, the audio is silent on the caller side to avoid drawing
                attention during the onging call. Only the call recipient can end the silent
                emergency call. During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                functions are inaccessible. The phone restores normal operation after the recipient
                ends the call. Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key. Custom services Configure the following parameters: Action Button Function : Select Custom . Action Button Service Destination :
                Enter the URL of the custom service. The URL must start with http:// or https:// , for example, https://10.11.20.159/path/service.xml . Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name. Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters. For POST script examples and the syntax, see HTTP Post request for the Action button . Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection. Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times . Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination . Multiple triggers Set the parameters in each group respectively. See the
              Emergency calls and Custom services sections above. A single trigger for multiple events Configure the following parameters
              to assign multiple events to a trigger: Action Button Function : Select Custom . Action Button Service Destination : Enter the phone number
                  to call and the XML service URL in this format: tel:<phonenumber or SIP URI> +
                  <serviceURL> The URL must start with http:// or https:// . Example: tel:1234 + https://10.11.20.159/path/service.xml Action Button Service Name (Optional): Specify a name for the service associated with the trigger. This name
                will be displayed in the on-screen message when the user presses the button,
                indicating which service will be triggered. When no name is specified, Custom
                  service will be used as the display name. Custom Content Field (Optional): If
                you want to enable the phone to send an HTTP Post request when the Action button is
                pressed, enter the HTTP data such as method, header, and post content, with a
                maximum length of 1024 characters. For POST script examples and the syntax, see HTTP Post request for the Action button . Dial Out Delay : Set the timeout
                period, in seconds, for the phone to initiate an event after detecting the trigger.
                The default value is 5 seconds. When set to 0, the event is initiated immediately
                upon trigger detection. Service Trigger Select a trigger
                from the list: Single Press , Long
                  Press , or Press 3 Times . Service Secret (Optional): Enter
                the authentication secret, token or password if your custom service requires
                authentication to access it. The entered secret is displayed as a masked string and
                can be referenced using the macro $SS in Custom Content
                  Field and Action Button Service
                Destination . Silent Emergency Call (Optional): If you have included a
                  phone number or dialing URI in the service destination, enabling this feature will
                  silent emergency calls. By default, the emergency call functions as a two-way call, similar to other
                  outgoing calls. When set to enabled, the audio is silent on the caller side to
                  avoid drawing attention during the onging call. Only the call recipient can end
                  the call. During a silent emergency call, the screen on phone 9811 and 9841 will freeze,
                  while the screen on phone 9851, 9861, and 9871 will be turned off. All other
                  functions are inaccessible. The phone restores normal operation after the
                  recipient ends the call. Allow Silent
                  Emergency Call Retrieval (Optional): Enable this feature if you allow
                users to press any key to restore normal phone operation while maintaining the
                emergency call. The call audio remains silent unless the user increases the speaker
                volume using the Volume key. For more information about these parameters, see Parameters for the Action
            button . |
| 4 | Select Save . |
| 5 | Select Apply Config . |

| Parameter | Default and options | Description |
|---|---|---|
| Action Button Function 1~3 | Default: Off Options: Off, Emergency Call, Custom | You can configure the button with a specific service. Off : When set to Off, the Action button for single
                      service on the phone will not function. Emergency Call : Users can use the Action button to
                      place an emergency call, if configured. Custom : Users can use the Action button to access the
                      custom service, if configured. When you set the field to Emergency Call or Custom , make sure that you enter the service
                    destination in the Action Button Service Destination field. Or, the phone will display a configuration error. |
| Action Button Service Name 1~3 | Default: Empty | Optionally specify a name for the service associated with the Action button.
                    This name will be displayed in the on-screen message when the user presses the
                    button, indicating which service will be triggered. If you don't specify a name, the default name will be Emergency call, Silent
                    emergency call, or Custom action based on your selection in the Action Button Function field. |
| Action Button Service Destination 1~3 | Default: Empty | Provide the service destination in one of the following formats based on the
                    service assigned to the Action button: For emergency call services, enter a telephone number or the URI of
                        emergency service. When configure the button for a custom service, enter the service URL. The
                        URL must start with http:// or https:// . For example, https://10.11.20.159/path/service.xml . To configure the button to initiate multiple events with a single trigger,
                        enter tel:<phonenumber or SIP URL> + <Service
                          RUL> . Example : tel:1234 +
                          https://10.11.20.159/path/service.xml . Calling SIP URIs is also supported. Enter the URI in the format of tel: sip 4567@co.webex.com If you enable the Action button without setting a valid service destination,
                    the user on the phone will see a message prompting for configuration. After the
                    user closes this notification, the warning icon will persist in the header of
                    the phone screen until the button is properly configured or disabled. Phone numbers cannot be used as destinations for custom services. If you
                      configure the Action Button as Custom and enter a phone
                      number as the service destination, an alert message will display on the phone
                      indicating that the button is unconfigured. Instead, you can add a phone
                      number in this format tel:<phone number> , for
                      example, tel:1234 . If you are not allowed to input a URL including ampersand (&), use %26 as a
                    replacement. For example, enter http://1.2.3.4/phone?a=1%26b=2%26c=3 instead of http://1.2.3.4/phone?a=1&b=2&c=3 . |
| Custom Content Field 1~3 | Default: Empty | This setting works only when the Action Button
                        Function is set to Custom . Enter the HTTP data such as method, header, and post content, with a maximum
                    length of 1024 characters. When configured, the phone sends an HTTP Post request
                    when the Action is pressed. If the service requires
                  authentication to access, make sure to enter the authentication secret in the Service Secret field. In the HTTP data, use the macro $SS as a reference to Service Secret. For examples and the syntax, see HTTP Post request for the Action
                    button . |
| Service Secret 1~3 | Default: Empty | A service secret can be an authentication secret, token or password. The
                    entered secret is displayed as a masked string and can be referenced using the
                    macro $SS in Custom Content Field and Action Button Service Destination . |
| Service Trigger 1~3 | Default: Single Press Options: Single Press, Long Press, Press 3 times | Choose how users can place an emergency call or initiate a custom service using
                    the phone's Action button. Single Press : Press the Action button to trigger the
                    associated call or service. Long Press : Press the Action button down for at least 2
                    seconds to trigger the associated call or service. Press 3 times : Press the Action button three times with
                    intervals of less than 2 seconds between each press to trigger the associated
                    call or service. Don't repeat a trigger across multiple services, as the parameters with lower
                    priority will not function. The priority order, from highest to lowest, is as
                    follows: Group 1, Group 2, Group 3. |
| Dial Out Delay 1~3 | Default: 5 Options: 0 - 30 | Set the timeout period, in seconds, for the phone to initiate an emergency call
                    or a custom action after the Action button is pressed. Set it to 0 if you prefer the phone to place the call or initiate an event
                    immediately upon detecting the trigger, as specified by a single press, long
                    press, or triple presses on the button. |
| Silent Emergency Call 1~3 | Default: Disabled Options: Enabled, Disabled | Silent emergency call is designed for discreet assistance in dangerous
                    situations. It enables users to seek help without making any noise. When enabled, users are able to place one-way calls with the Action button. After the silent emergency call is placed, only the other party can end the
                        call. To avoid drawing attention during the ongoing call, the screen on
                        phone 9811 and 9841 will freeze, while
                        the screen on phone 9851, 9861, and 9871 will be turned off. The phone locks all
                          functions during a silent emergency call, by default. To allow users to
                          restore normal phone operation while maintaining the silent emergency
                          call, enable the Allow Silent Emergency Call
                            Retrieval feature. When disabled, the emergency call functions as a two-way call, similar to
                        other outgoing calls. |
| Allow
                  Silent Emergency Call Retrieval | Default: No Options: Yes, No | Controls whether users can retrieve phone functionality during a silent
                    emergency call. By default, once a silent emergency call is initiated, the phone
                    locks all functions until the call recipient ends the call. When this parameter is set to Yes , users can press any
                    key to restore normal phone operation while maintaining the emergency call. The
                    call audio remains silent unless the user increases the volume using the Volume
                    key. |

| Character | Percent encoding |
|---|---|
| & | %26 |
| ' | %27 |
| " | %22 |
| < | %3c |
| > | %3e |

| Macro name | Macro expansion |
|---|---|
| #DEVICENAME# | The device name displayed in the calling system. For example,
                SEP845A3EC21288 |
| $SS | Service Secret which presents a masked string in the phone configuration page,
                such as authentication secret, token, or password. |

| 1 | In the Cisco Unified Communications Manager Administration,  select one of the following windows: Select Device > Phone . Select Device > Device Settings > Common Phone Profile . Select System > Enterprise Phone Configuration . |
|---|---|
| 2 | Navigate to the Product Specific Configuration Layout area and set the following fields: Help Desk : Enable or disable the help desk feature. By default, the feature is disabled. When enabled, the user can press the Favorite button to access help desk screen where lists the quick numbers configured by you. Help Desk Customize Name : Customize the display name of the feature on the phone screen. If it's empty, the default name "Help Desk" is used. Name <n> : Determine the display name of the related quick number, where <n> represents the sequence number of the quick number. If it's empty, it will display the related quick number on the phone. Quick Number <n> : Specify a phone number or URI for the quick number, where <n> represents the sequence number of the quick number. |
| 3 | Click Save . |

| Phone model | Firmware version |
|---|---|
| Cisco Video Phone 8875 | 5.0.1 and later |
| Cisco Desk Phone 9861 | 3.2.1 and later |
| Cisco Desk Phone 9871 | 3.2.1 and later |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To enable ThousandEyes Agent for all deployed phones, go to System > Enterprise Phone Configuration . To enable ThousandEyes Agent for phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To enable ThousandEyes Agent for an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. |
| 3 | Set ThousandEyes Enable to True . |
| 4 | Copy the connection string from the ThousandEyes application and paste it into the Connection String field. |
| 5 | Select Save . |
| 6 | Select Apply Config . |

| Feature | 8875 | 9811 | 9841 | 9851 | 9861 | 9871 |
|---|---|---|---|---|---|---|
| Display Off | Yes | No | Yes | Yes | Yes | Yes |
| Deep Sleep (Controlled by phone) | No | No | Yes | Yes | Yes | Yes |
| Cisco Smart Power (Deep Sleep controlled by switch) | Yes | Yes | Yes | Yes | Yes | Yes |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 3 | Customize working hours and workdays to reflect the business hours of your users. Enable Office Hours : By default, the Office Hours feature is
                enabled. If disabled, your phone won't enter power saving mode. Workdays : The default workdays are Monday through Friday.
                Change the workdays as needed. Working Hours Start and Working Hours
                  End : The default working hours are set to 7:00 to 19:00. Change the
                setting as needed. See more information about these parameters , see Parameters for Office
            Hours . |
| 4 | Configure the settings for Display Off Mode for both working hours and non-working
          hours. Cisco Desk Phone 9811 doesn't support Display Off Mode. Display Off During Office Hours : By default, the phone
                display remains on during working hours. To enable the phone to enter Display Off
                Mode when inactive, select timeout period from the list. Display Off Idle Timeout Outside Office Hours : Set the
                timeout period in minutes for the phone to automatically turn off the screen after
                being awakened during Display Off Mode. LED Indicator In Display Off Mode : This setting determines
                whether to turn off the Front Arc LED when the phone enters Display Off Mode, both
                during or outside office hours. By default, the Front Arc LED remains illuminated
                after the phone enters Display Off Mode. When set to disabled, the Front Arc LED is
                off in Display Off Mode. Line Key and Top 360 LED in Display Off Mode (Cisco Desk Phone 9841, 9851, 9861, and 9871): Controls whether the LEDs light up to notify users of phone statuses in Display Off mode. When disabled, both the Line Key LEDs on phone and Key Expansion Module (KEM) and Top 360 LEDs are off. When the corresponding LED is enabled, its indication behavior is the same as when the display is on. This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled. Handset LED in Display Off Mode (Video Phone 8875): Controls whether the handset LED lights up to notify users of phone statuses in Display Off mode. When disabled, the handset LED is off. When enabled, its indication behavior is the same as when the display is on. This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled. See more information about these parameters , see Parameters for Office
            Hours . |
| 5 | Configure the settings for Deep Sleep Mode for the 9800 Series phones. Deep Sleep Mode on Cisco Video Phone 8875 and Cisco Desk Phone 9811 can only be enabled by Cisco switches through the smart power feature. To configure
              the smart power settings, follow the steps in Allow Cisco switch to manage power modes for your phone (smart power) . Deep Sleep : Enable this feature to allow the phone to power
                off outside office hours. Enter Deep Sleep After Working Hour End : Set the timeout
                period for the phone to automatically power off after the time specified in the Working Hours End field. The default setting is 60
                minutes. Wakeup From Deep Sleep Before Working Hour Start : Set the
                timeout period for the phone to wake up from Deep Sleep Mode before the time
                specified in the Working Hours Start field. The default
                setting is 60 minutes. Deep Sleep Idle Timeout : Sets timeout period for the phone
                to enter Deep Sleep Mode. Enable Deep Sleep Audible Alert (Optional): If set to True,
                the phone plays audio tone to alert the user before it enters Deep Sleep Mode. See more information about these parameters , see Parameters for Office
            Hours . |
| 6 | Select Save . |
| 7 | Select Apply Config . |

| Smart Power | Smart Power Override | Description |
|---|---|---|
| Disabled | Yes / No | Smart power is disabled. The phone follows the power saving configuration set on
                  its calling system. |
| Enabled for non-work day only | No | Smart power is enabled only on non-work days. On non-work days, the phone follows the display off and deep sleep schedules
                  configured on its calling system. The switch wakes the phone from deep sleep following the phone's schedule. |
| Yes | Smart power is always enabled. Since Smart Power Override is set to Yes,
                the switch manages the phone's display off and deep sleep modes based on the
                schedules configured on the switch. The phone's own settings in its calling system
                are overridden. |
| Enabled for all days | No | Smart power is always enabled. The phone follows the display off and deep sleep schedules set on its calling
                  system. The switch wakes the phone from deep sleep following the phone's schedule. |
| Yes | Smart power is always enabled. Since Smart Power Override is set to Yes,
                the switch manages the phone's display off and deep sleep modes based on the
                schedules configured on the switch. The phone's own settings in its calling system
                are overridden. |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 3 | Configure the following parameters: Smart Power : Enable the smart power feature. The available
                options are: Disabled (Default): Disables the smart power
                  feature. Enabled for Non-work Day Only : Enables smart power only
                  on non-working days. Enabled for All Days : Enables smart power always, on both
                  work days and non-work days. Smart Power Override : Specify whether the
              switch can manage power modes based on the schedules configured on the switch,
              overriding the phone's settings configured in the phone's calling system. Smart Power Domain : Enter the smart power domain that the
              phone belongs to. Smart Power Endpoint Security Secret : Enter the password
              (shared secret) used for communication between the phone and the switch. For more information about these parameters, see Parameters for Office
          Hours . |
| 4 | Select Save . |
| 5 | Select Apply Config . |

| Parameter | Default and options | Supported model | Description |
|---|---|---|---|
| Office Hours parameters |
| Enable Office Hours | Default: Enabled Options: Enabled, Disabled | 8875 9841 9851 9861 9871 | Check this option to enable the Office Hours feature for Cisco Desk Phone 9800
                  Series. The Office Hours feature is designed to minimize power usage during
                  inactivity periods on the phone. You can configure the phone to automatically turn off the screen (Display Off
                  Mode) or power off (Deep Sleep Mode) outside of the designated working periods. |
| Work Days | Default: Monday through Friday | 8875 9811 9841 9851 9861 9871 | Customize the workdays by holding down the Ctrl key and selecting the desired
                  days. During non-workdays, the phone will automatically turn off the screen. By
                  default, workdays are set from Monday to Friday. This setting also applies to Deep Sleep Mode, if enabled. If you choose to enable
                  Deep Sleep Mode exclusively for non-workdays, the phone will power off during
                  those days. If you enable Deep Sleep Mode for all days, the phone will power off
                  during both non-workdays and non-working hours on workdays. Set working hours for workdays using the Working Hour
                    Start and Working Hour End fields. |
| Working Hours Start | Default: 07:00 | 8875 9811 9841 9851 9861 9871 | Set the start time for working hours using the 24-hour format. Outside of the
                  specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep is set to Enabled for All Days . Examples: 09:00 for 09:00 am; 17:30 for 05:30 pm |
| Working Hours End | Default: 19:00 | 8875 9811 9841 9851 9861 9871 | Set the end time for working hours using the 24-hour format. Outside of the
                  specified working hours, the phone will automatically turn off the screen, or
                  enter Deep Sleep Mode only when Deep Sleep is set to Enabled for All Days . Examples: 09:00 for 09:00 am; 17:30 for 05:30 pm Ensure that the interval between the start and end time longer than 60
                    minutes. |
| Display Off Parameters |
| Display Off During Office Hours | Default: Disabled Options: Disabled, In 1 minute, In 5 minutes, In 30 minutes | 8875 9841 9851 9861 9871 | Enable or disable Display Off Mode during office
                  hours. This feature is disabled by default, keeping the phone screen always on
                  during office hours. To enable this feature, select a timeout duration from the
                  available options. For example, if set to "In 5 minutes", the phone screen will
                  automatically turn off after 5 minutes of inactivity. The LED indicator follows the setting of LED Indicator In Display Off
                    Mode . |
| Display Off Idle Timeout Outside Office Hours | Default: 5 Options: 1-60 | 8875 9841 9851 9861 9871 | Set the timeout period in minutes for the phone to automatically turn off the
                screen after being awakened during Display Off Mode. |
| LED Indicator In Display Off Mode | Default: Enabled Options: Enabled, Disabled | 8875 9841 9851 9861 9871 | This setting determines whether to turn off the Front Arc LED on 9800 Series or
                  the Home button LED on 8875 when the phone enters Display Off Mode, both during or
                  outside office hours. By default (Enabled), the LED remains illuminated after the
                  phone enters Display Off Mode. When set to disabled, the LED is off in Display Off
                  Mode. |
| Line Key and Top 360 LED in Display Off Mode | Default: Disabled Options: Disabled, Enable Line Key LED, Enable Top 360 LED, Enable both Line Key and Top 360 LED | 9841 9851 9861 9871 | Controls whether the LEDs light up to notify users of phone statuses in Display Off mode. When disabled, both the Line Key LEDs on phone and Key Expansion Module (KEM) and Top 360 LEDs are off. When the corresponding LED is enabled, its indication behavior is the same as when the display is on. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Line_Key_and_Top_360_LED_In_Display_Off_Mode ua="na">Disabled</Line_Key_and_Top_360_LED_In_Display_Off_Mode> This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled. |
| Handset LED in Display Off Mode | Default: Disabled Options: Enabled, Disabled | 8875 | Controls whether the handset LED lights up to notify users of phone statuses in Display Off mode. When disabled, the handset LED is off. When enabled, its indication behavior is the same as when the display is on. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Handset_LED_In_Display_Off_Mode ua="na">Disabled</Handset_LED_In_Display_Off_Mode> This setting works only when the LED Indicator In Display Off Mode parameter is set to Enabled. |
| Deep Sleep Parameters When smart power isn't applied, the Deep Sleep settings work with the office
                    hours settings to determine the deep sleep schedule on 9841, 9851, 9861, and
                    9871. When smart power is applied and Smart Power Override is disabled, the switch
                    also uses these settings to control the deep sleep mode on all applicable
                    phones. |
| Deep Sleep | Default: Disabled Options: Disabled, Enabled for Non-Workdays Only, Enabled for All Days | 9841 9851 9861 9871 | Enable or disable Deep Sleep Mode on the phone. This feature automatically powers off the phone during specified time periods. This option works only when the Enabled Office Hour option
                  is checked. When disabled, the phone will not enter Deep Sleep Mode. If set to Enabled for Non-Workdays Only , the phone will power off
                  exclusively on non-workdays. For the specified workdays, the phone will turn off
                  the screen outside of the specified working hours. If set to Enabled
                    for All Days , the phone will power off during both non-workdays and
                  non-working hours on workdays. Set working hours for workdays using the Working Hours
                    Start and Working Hours End fields. |
| Enter Deep Sleep After Working Hour End | Default: 60 Options: 0 - 360 | 8875 9811 9841 9851 9861 9871 | Set the timeout period, in minutes, for the phone to automatically power off
                after the time specified in the Working Hours End field. If
                you want the phone to enter Deep Sleep Mode immediately after working hours, set it
                to 0. The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled. |
| Wakeup From Deep Sleep Before Working Hour Start | Default: 60 Options: 0 - 360 | 8875 9811 9841 9851 9861 9871 | Set the timeout period for the phone to wake up from Deep Sleep Mode before the
                time specified in the Working Hours Start field. If you want
                the phone to wake up until working hours start, set it to 0. The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled. |
| Deep Sleep Idle Timeout | Default: 5 Options: 0 - 60 | 8875 9811 9841 9851 9861 9871 | This setting applies to the following two scenarios: Before the phone enters a scheduled Deep Sleep Mode Ten minutes
                      before the scheduled deep sleep, a message pops up to notify the user that the
                      phone will power off in ten minutes, and a countdown starts. When it times
                      out, the phone powers off. During the countdown period, if there is a
                      system activity such as an incoming call, firmware upgrade, or provisioning
                      resync, the countdown will restart. For example, if you have set this field to
                      20, the countdown will restart in 20 minutes after the activity completes. If
                      the phone restarts or its configuration is changed during the countdown, the
                      power-off notification appears again after the restart, and the countdown
                      continues. After being awakened manually or by a configured restart during Deep Sleep
                      Mode After the specified idle timeout period, the phone displays a
                      power-off notification. The countdown shown in the notification is based on
                      the configured idle timeout value. Examples If you set the idle timeout to more than 10 minutes (for example, 20
                            minutes), a message appears after the phone has been idle for 20
                            minutes, notifying the user that the phone will power off in 10
                            minutes. If you set the idle timeout to less than 10 minutes (for example, 6
                            minutes), a message appears after the phone has been idle for 6 minutes,
                            notifying the user that the phone will power off in 6 minutes. During the countdown period, if there is a system activity such as
                      an incoming call, firmware upgrade, or provisioning resync, the countdown will
                      restart. For example, if you have set this field to 20, the countdown will
                      restart in 20 minutes after the activity completes. The following notes apply to both scenarios described above. If a user interacts with the phone during the countdown period, such as
                          answering or declining calls or pressing keys, the phone will not enter
                          Deep Sleep Mode for the rest of the day. The smart power feature uses this setting to control the
                    phone's power mode only when Smart Power Override is
                    disabled. |
| Enable Deep Sleep Audible Alert | Default: Unchecked | 8875 9811 9841 9851 9861 9871 | Enable or disable the phone to play audio tone to alert the user before it enters
                  Deep Sleep Mode. |
| Smart Power Parameters Supported only on phones powered by Power over
                  Ethernet (PoE). |
| Smart Power | Default: Disabled Options: Disabled, Enabled for Non-work Day Only, Enabled for All Days | 8875 9811 9841 9851 9861 9871 | Enable or disable the smart power feature. By default, smart power is disabled.
                    Set it to Non-work Day Only or All Days as needed to enable this feature. The setting is effective only when a valid domain and security secret are
                    provided. |
| Smart Power Override | Default: No Options: Yes, No | 8875 9811 9841 9851 9861 9871 | This setting determines whether the switch can override the phone's
                    power-saving configuration set by the calling system. No : The phone follows the power-saving configuration
                      set by its calling system. Yes : The switch fully controls the phone’s power
                      modes, overriding the configuration set by the phone's calling system. |
| Smart Power Domain | Default: Empty | 8875 9811 9841 9851 9861 9871 | The smart power domain that the phone belongs to. Max 128 characters. |
| Smart Power Endpoints Security Secret | Default: Empty | 8875 9811 9841 9851 9861 9871 | The password (shared secret) used for communication between the phone and the
                    switch. Max 128 characters. |

| 1 | Sign into Cisco Communication Manager Administration as an administrator. |
|---|---|
| 2 | Enable E911 service for the phone: Perform one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings Set HELD Support for Third-Party E911 to Enabled . The default setting is Disabled . Click Save . Click Apply Config . |
| 3 | Configure a service profile: Select User Management > User Settings > Service Profile . Create a new service profile with a unique name. For example, "Emergency Calling Profile". Configure the fields in the Emergency Calling Profile section. The Organization ID , Secret , and Location Url are provided by your emergency calling service provider. For Emergency Numbers , enter the emergency service numbers, separated by commas. For example, 911,933 . Click Save . |
| 4 | Associate an end user with the service profile (configured in Step 2): Select User Management > End User . Create a new user or modify an existing user. In the Service Settings section, select the service profile that you created from the UC Service Profile drop-down list. Click Save . |
| 5 | Create or modify an SIP dial rule for the emergency number: Select Call Routing > Dial Rules > SIP Dial Rules . Create a new SIP dial rule or modify an existing one. If you choose to create a new SIP dial rule, select 7940_7960_OTHER from the Dial Pattern drop-down list. Enter a name and relevant descriptions for the SIP dial rule. In the Pattern Information section, add patterns of the emergency number (such as, "911" and "933"). Click Save . |
| 6 | Associate a phone with the user (configured in Step 3) and the SIP dial rule (Configured in Step 4): Select Device > Phone to find an existing phone. In the Device Information section, select User for the Owner field, and then select the user from the Owner User ID drop-down list. In the Protocol Specific Information section, select the SIP dial rule from the SIP Dial Rules drop-down list. Click Save . |
| 7 | Add the SIP Trunk to a RedSky server: Select Device > Trunk . Click Add New . Select SIP Trunk from the Trunk Type drop-down list. Select SIP from the Protocol Type drop-down list, and click Next . In the SIP Information section, enter an IPv4 address of the RedSky server, fully qualified domain name, or DNS SRV record for the server or endpoint that you want to connect to the SIP trunk in the Destination Address field. Assign a security profile from the SIP Trunk Security Profile drop-down list. If you don't configure this field, a nonsecure profile will be assigned. Select a Ping option enabled RedSky SIP profile from the SIP Profile drop-down list. Click Save . |
| 8 | Configure route pattern to route E911 calls: Select Call Routing > Route/Hunt > Route pattern . Click Add New to create a new route pattern for the E911 calls. Select E911 from the Route Pattern drop-down list. Select the SIP Trunk (created in Step 6) from the Gateway/Route List drop-down list. Click Save . |
| 9 | Upload RedSky certificates to CUCM: Download the certificate file (.pem) from the Location Url (configured in Step 2). You can enter a Browser to access the address. Sign into Cisco Unified OS Administration. Select Security > Certificate Management . Click Upload Certificate . Select Phone Trust from the Certificate
                Purpose drop-down list. Click Browse to choose the file that you want to upload. Click Upload File . |

| 1 | Sign into Cisco Unified Communications Manager Administration as an
          administrator. |
|---|---|
| 2 | Select Device > Phone . |
| 3 | Locate the phone that you will set up. |
| 4 | Navigate to the Do Not Disturb pane, set the following
          parameters: Do Not Disturb : This check box allows you to enable or
              disable DND on the phone. DND Option : Ring Off, Call Reject, or Use Common Phone Profile
                Setting. Do not choose Call Reject if you want priority (MLPP) calls to ring this phone
                  when DND is turned on. DND Incoming Call Alert : Choose the type of alert (Disable,
              Flash Only or Beep Only) to play on a phone for incoming calls when DND is
              active. For the parameters DND Option and DND Incoming Call Alert , both can be found in the Common Phone Profile window ( Device > Device Settings > Common Phone Profile ) and the Phone Configuration window ( Device > Phone ). The setting in the Phone Configuration window takes precedence. |
| 5 | Click Save . |

| 1 | Sign into Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Select Device > Phone . |
| 3 | Locate the phone that you will set up. |
| 4 | Select the target line from the Association pane. |
| 5 | Navigate to the Call Forward and Call Pickup Settings pane,
          enter a forwarded-to destination number in the field Forward
          All . |
| 6 | Click Save . |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Perform one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 3 | Set HELD Support for Third-Party E911 to Enabled . The default setting is Disabled . |
| 4 | Click Save . |
| 5 | Click Apply Config . |

| 1 | Do one of the following actions from Cisco Unified CM Administration: To set up the feature for a specific phone: Choose Device > Phone and locate the phone that you want to set up. To set up the feature for a group of phones: Choose Device > Device Settings > Common Phone Profile and locate the profile that you want to set up. To set up the feature for all phones: Choose System > Enterprise Phone Configuration . |
|---|---|
| 2 | Set up the field Join And Direct Transfer Policy : Same line, across line enable : All active calls can be transferred or joined. The Calls tab displays in the new call session. It shows all active calls from all lines on the phone. Same line enable only : Only active calls in the same line can be transferred or joined. The Calls tab displays in the new call session. It only shows the active calls from a selected line. Same line, across line disable : No active calls can be transferred or joined. The Calls tab in the new call session doesn't display. |
| 3 | Click Save . |

| 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| 2 | Locate the phone that you will set up. |
| 3 | In the Phone Configuration window, select Add a new
            SD . A Speed Dial Configuration window appears, which contains settings for both speed dials and abbreviated dials. To configure a speed dial entry, enter the information in the Speed Dial (Button) Settings section. To configure an abbreviated dial entry, enter the information in the Speed Dial (Abbreviated Dial) Settings section. |
| 4 | Enter valid speed-dial numbers in the Number fields and a label in the Label fields. |
| 5 | Click Save . |

| 1 | In Cisco Unified Communications Manager Administration, go to Call Routing > Dial Rules > Application Dial Rules . |
|---|---|
| 2 | Click Add New to create a new application dial rule, or choose an existing application dial rule to edit it. |
| 3 | Fill in the following fields: Name This field comprises a unique name for the dial rule that can contain up to 20 alphanumeric characters and any combination of spaces, periods (.), hyphens (-), and underscore characters (_). Description This field comprises a brief description that you enter for the dial rule. Number Begins With This field comprises the initial digits of the directory numbers to which you want to apply this application dial rule. Number of Digits This required field comprises the initial digits of the directory numbers to which you want to apply this application dial rule. Total Digits to be Removed This required field comprises the number of digits that you want Cisco Unified Communications Manager to remove from directory numbers that apply to this dial rule. Prefix With Pattern This required field comprises the pattern to prepend to directory numbers that apply to this application dial rule. Application Dial Rule Priority This field displays when you enter the Prefix With Pattern information. The field allows you to set the priority order of the application dial rules. |
| 4 | Click Save . |

| 1 | In Cisco Unified Communications Manager Administration,
      choose System > Service
        Parameters . |
|---|---|
| 2 | Select a server for the phone and the service Cisco CallManager
            (Active) . |
| 3 | In the Clusterwide Parameters (Feature - General) section, set
          the fields as described in the following table. Table 10. Service parameters for park monitoring Field Description Park Monitoring Reversion Timer This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks an active call on the
                      phone, and a reminder is issued when the timer expires. Default is 60 seconds. You can override the value that this service parameter specifies on a
                      per-line basis in the Park Monitoring section of the Directory Number Configuration window (in Cisco
                      Unified Communications Manager Administration, choose Call Routing > Directory Number ). Specify a value of 0 to immediately utilize the periodic
                      reversion interval that the Park Monitoring Periodic Reversion
                        Timer service parameter specifies. (See the description that
                      follows.) For example, if this parameter is set to zero and the Park Monitoring Periodic Reversion Timer is set to
                      15, the user is immediately prompted about the parked call and every 15
                      seconds thereafter until the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) expires. Park Monitoring Periodic Reversion Timer This parameter determines the interval (in seconds) that Cisco Unified
                      Communications Manager waits before prompting the user again that a call is
                      parked. To connect to the parked call, the user can simply go off-hook during
                      one of these prompts. Cisco Unified Communications Manager continues to prompt
                      the user about the parked call as long as the call remains parked and until
                      the time that the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) specifies expires.
                      Specify a value of 0 to disable periodic prompts about the parked call. Default is 30 seconds. Park Monitoring Forward No Retrieve Timer This parameter determines the number of seconds that park reminder
                      notifications occur before the parked call forwards to the Park
                        Monitoring Forward No Retrieve destination that is specified in
                      the parker's Directory Number Configuration window. (If
                      no forward destination is provided in Cisco Unified Communications Manager
                      Administration, the call returns to the line that parked the call.) This timer
                      starts when the time that the call is parked. When Park Monitoring
                        Reversion Timer and Park Monitoring Forward No
                        Retrieve Timer expire, the call is removed from park and
                      forwards to the specified destination or returns to the parker line. Default is 300 seconds. | Field | Description | Park Monitoring Reversion Timer | This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks an active call on the
                      phone, and a reminder is issued when the timer expires. Default is 60 seconds. You can override the value that this service parameter specifies on a
                      per-line basis in the Park Monitoring section of the Directory Number Configuration window (in Cisco
                      Unified Communications Manager Administration, choose Call Routing > Directory Number ). Specify a value of 0 to immediately utilize the periodic
                      reversion interval that the Park Monitoring Periodic Reversion
                        Timer service parameter specifies. (See the description that
                      follows.) For example, if this parameter is set to zero and the Park Monitoring Periodic Reversion Timer is set to
                      15, the user is immediately prompted about the parked call and every 15
                      seconds thereafter until the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) expires. | Park Monitoring Periodic Reversion Timer | This parameter determines the interval (in seconds) that Cisco Unified
                      Communications Manager waits before prompting the user again that a call is
                      parked. To connect to the parked call, the user can simply go off-hook during
                      one of these prompts. Cisco Unified Communications Manager continues to prompt
                      the user about the parked call as long as the call remains parked and until
                      the time that the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) specifies expires.
                      Specify a value of 0 to disable periodic prompts about the parked call. Default is 30 seconds. | Park Monitoring Forward No Retrieve Timer | This parameter determines the number of seconds that park reminder
                      notifications occur before the parked call forwards to the Park
                        Monitoring Forward No Retrieve destination that is specified in
                      the parker's Directory Number Configuration window. (If
                      no forward destination is provided in Cisco Unified Communications Manager
                      Administration, the call returns to the line that parked the call.) This timer
                      starts when the time that the call is parked. When Park Monitoring
                        Reversion Timer and Park Monitoring Forward No
                        Retrieve Timer expire, the call is removed from park and
                      forwards to the specified destination or returns to the parker line. Default is 300 seconds. |
| Field | Description |
| Park Monitoring Reversion Timer | This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks an active call on the
                      phone, and a reminder is issued when the timer expires. Default is 60 seconds. You can override the value that this service parameter specifies on a
                      per-line basis in the Park Monitoring section of the Directory Number Configuration window (in Cisco
                      Unified Communications Manager Administration, choose Call Routing > Directory Number ). Specify a value of 0 to immediately utilize the periodic
                      reversion interval that the Park Monitoring Periodic Reversion
                        Timer service parameter specifies. (See the description that
                      follows.) For example, if this parameter is set to zero and the Park Monitoring Periodic Reversion Timer is set to
                      15, the user is immediately prompted about the parked call and every 15
                      seconds thereafter until the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) expires. |
| Park Monitoring Periodic Reversion Timer | This parameter determines the interval (in seconds) that Cisco Unified
                      Communications Manager waits before prompting the user again that a call is
                      parked. To connect to the parked call, the user can simply go off-hook during
                      one of these prompts. Cisco Unified Communications Manager continues to prompt
                      the user about the parked call as long as the call remains parked and until
                      the time that the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) specifies expires.
                      Specify a value of 0 to disable periodic prompts about the parked call. Default is 30 seconds. |
| Park Monitoring Forward No Retrieve Timer | This parameter determines the number of seconds that park reminder
                      notifications occur before the parked call forwards to the Park
                        Monitoring Forward No Retrieve destination that is specified in
                      the parker's Directory Number Configuration window. (If
                      no forward destination is provided in Cisco Unified Communications Manager
                      Administration, the call returns to the line that parked the call.) This timer
                      starts when the time that the call is parked. When Park Monitoring
                        Reversion Timer and Park Monitoring Forward No
                        Retrieve Timer expire, the call is removed from park and
                      forwards to the specified destination or returns to the parker line. Default is 300 seconds. |

| Field | Description |
|---|---|
| Park Monitoring Reversion Timer | This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks an active call on the
                      phone, and a reminder is issued when the timer expires. Default is 60 seconds. You can override the value that this service parameter specifies on a
                      per-line basis in the Park Monitoring section of the Directory Number Configuration window (in Cisco
                      Unified Communications Manager Administration, choose Call Routing > Directory Number ). Specify a value of 0 to immediately utilize the periodic
                      reversion interval that the Park Monitoring Periodic Reversion
                        Timer service parameter specifies. (See the description that
                      follows.) For example, if this parameter is set to zero and the Park Monitoring Periodic Reversion Timer is set to
                      15, the user is immediately prompted about the parked call and every 15
                      seconds thereafter until the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) expires. |
| Park Monitoring Periodic Reversion Timer | This parameter determines the interval (in seconds) that Cisco Unified
                      Communications Manager waits before prompting the user again that a call is
                      parked. To connect to the parked call, the user can simply go off-hook during
                      one of these prompts. Cisco Unified Communications Manager continues to prompt
                      the user about the parked call as long as the call remains parked and until
                      the time that the Park Monitoring Forward No Retrieve
                        Timer (see the description that follows) specifies expires.
                      Specify a value of 0 to disable periodic prompts about the parked call. Default is 30 seconds. |
| Park Monitoring Forward No Retrieve Timer | This parameter determines the number of seconds that park reminder
                      notifications occur before the parked call forwards to the Park
                        Monitoring Forward No Retrieve destination that is specified in
                      the parker's Directory Number Configuration window. (If
                      no forward destination is provided in Cisco Unified Communications Manager
                      Administration, the call returns to the line that parked the call.) This timer
                      starts when the time that the call is parked. When Park Monitoring
                        Reversion Timer and Park Monitoring Forward No
                        Retrieve Timer expire, the call is removed from park and
                      forwards to the specified destination or returns to the parker line. Default is 300 seconds. |

| 1 | In Cisco
      Unified Communications Manager Administration, choose Call
        Routing > Directory Number . |
|---|---|
| 2 | Click Find and select the directory number on which you want to
          configure the park monitoring. |
| 3 | In the Park Monitoring section, set the fields as described in
          the following table. Table 11. Park monitoring parameters Field Description Park Monitoring Forward No Retrieve Destination External When the parkee is an external party, the call forwards to the specified
                      destination in the parker's Park Monitoring Forward No Retrieve
                        Destination External parameter. If the field is empty, the
                      parkee is redirected to the parker line. Park Monitoring Forward No Retrieve Destination Internal When the parkee is an internal party, the call forwards to the specified
                      destination in the parker’s Park Monitoring Forward No Retrieve
                        Destination Internal parameter. If the field is empty, the
                      parkee is redirected to the parker line. Park Monitoring Reversion Timer This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks a call on the phone,
                      and a reminder is issued when the timer expires. Default: 60 seconds If you configure a nonzero value, this value overrides the value of this
                      parameter set in the Service Parameters window.
                      However, if you configure a value of 0 here, then the value in the Service Parameters window is used. | Field | Description | Park Monitoring Forward No Retrieve Destination External | When the parkee is an external party, the call forwards to the specified
                      destination in the parker's Park Monitoring Forward No Retrieve
                        Destination External parameter. If the field is empty, the
                      parkee is redirected to the parker line. | Park Monitoring Forward No Retrieve Destination Internal | When the parkee is an internal party, the call forwards to the specified
                      destination in the parker’s Park Monitoring Forward No Retrieve
                        Destination Internal parameter. If the field is empty, the
                      parkee is redirected to the parker line. | Park Monitoring Reversion Timer | This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks a call on the phone,
                      and a reminder is issued when the timer expires. Default: 60 seconds If you configure a nonzero value, this value overrides the value of this
                      parameter set in the Service Parameters window.
                      However, if you configure a value of 0 here, then the value in the Service Parameters window is used. |
| Field | Description |
| Park Monitoring Forward No Retrieve Destination External | When the parkee is an external party, the call forwards to the specified
                      destination in the parker's Park Monitoring Forward No Retrieve
                        Destination External parameter. If the field is empty, the
                      parkee is redirected to the parker line. |
| Park Monitoring Forward No Retrieve Destination Internal | When the parkee is an internal party, the call forwards to the specified
                      destination in the parker’s Park Monitoring Forward No Retrieve
                        Destination Internal parameter. If the field is empty, the
                      parkee is redirected to the parker line. |
| Park Monitoring Reversion Timer | This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks a call on the phone,
                      and a reminder is issued when the timer expires. Default: 60 seconds If you configure a nonzero value, this value overrides the value of this
                      parameter set in the Service Parameters window.
                      However, if you configure a value of 0 here, then the value in the Service Parameters window is used. |

| Field | Description |
|---|---|
| Park Monitoring Forward No Retrieve Destination External | When the parkee is an external party, the call forwards to the specified
                      destination in the parker's Park Monitoring Forward No Retrieve
                        Destination External parameter. If the field is empty, the
                      parkee is redirected to the parker line. |
| Park Monitoring Forward No Retrieve Destination Internal | When the parkee is an internal party, the call forwards to the specified
                      destination in the parker’s Park Monitoring Forward No Retrieve
                        Destination Internal parameter. If the field is empty, the
                      parkee is redirected to the parker line. |
| Park Monitoring Reversion Timer | This parameter determines the number of seconds that Cisco Unified
                      Communications Manager waits before prompting the user to retrieve a call that
                      the user parked. This timer starts when the user parks a call on the phone,
                      and a reminder is issued when the timer expires. Default: 60 seconds If you configure a nonzero value, this value overrides the value of this
                      parameter set in the Service Parameters window.
                      However, if you configure a value of 0 here, then the value in the Service Parameters window is used. |

| 1 | In Cisco
      Unified Communications Manager Administration, choose Call
        Routing > Route/Hunt > Hunt
          Pilot . |
|---|---|
| 2 | Click Find and select the hunt pilot on which you want to
          configure the park monitoring. |
| 3 | Set the Park Monitoring Forward No Retrieve Destination parameter. If the field is empty, the call forwards to the destination that is configured in the Directory Number Configuration window when the Park
              Monitoring Forward No Retrieve Timer expires. |

| 1 | In Cisco Unified Communications Manager Administration, add the softkey Record (Record) . For more information, see Configure feature soft buttons with a softkey template . |
|---|---|
| 2 | Apply the new or updated softkey template to a phone. For more information, see Apply a softkey template to a phone . |
| 3 | Enable Built in Bridge field for the phone. Choose Device > Phone . Click Find to locate the phone that you want to configure. From the Built in Bridge drop-down list, choose On to enable it Click Save . |
| 4 | Configure a phone line for recording. Choose Device > Phone . Click Find to locate the phone that you configured. In the left Association pane, click a phone line for the recording setup. From the Recording Option drop-down list, choose Selective Call Recording Enabled . From the Recording Profile drop-down list, choose a recording profile that is configured for the line. For more information about how to create a new recording profile, see the Create a Recording Profile section in Feature Configuration Guide for Cisco Unified
                  Communications Manager, Release 15 and SUs . Click Save . |

| 1 | Sign into Cisco Unified Communications Manager Administration as an administrator. |
|---|---|
| 2 | Select Device > Device Settings > Common Phone Profile |
| 3 | Locate the profile that you want to set up. |
| 4 | Navigate to the Common Phone Profile Information pane and set up a password in the Local Phone Unlock Password field. |
| 5 | Click Save . |
| 6 | Click Apply Config . |
| 7 | Restart the phones. |

| 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| 2 | Locate the phone that you will set up. |
| 3 | In the Product Specific Configuration Layout section, configure the field Record Call Log from Shared Line to enable or disable the feature. Default value: Disabled |
| 4 | Click Save . |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. |
| 3 | Set Missed Call Led Alert to Enabled . Default: Disabled. |
| 4 | Select Save . |
| 5 | Select Apply Config . |

| 1 | In Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| 2 | Locate the phone that you will set up. |
| 3 | In the left Association area, click Add a New DN to create a new directory number or click an existing directory number to modify it. The Directory Number Configuration window displays. |
| 4 | In the Line <n> on Device section, set the Visual Message Waiting Indicator Policy to Light and Prompt . |
| 5 | Configure the remaining fields in the Directory Number Configuration window. |
| 6 | Click Save . The setting takes effect on the configured line. |
| 7 | (Optional) If you want to apply the settings on the corporate level, do the following: Select System > Service Parameters . Select a node from the Server drop-down list. Select Cisco CallManager from the Service drop-down list. In the Clusterwide Parameters (Feature - General) section, set Message Waiting Lamp Policy to Light and Prompt . Click Save . |

| 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| 2 | Locate the phone that you will set up. |
| 3 | Navigate to the Product Specific Configuration area and set the Settings Access field. Enabled: Allows full access to the Settings menu. Disabled: Allows access only to the following menus. EM (or EMCC if extension mobility
                  is configured) Network and service (if any other custom service or VPN
                  is configured) This option prevents access to other options in the Settings menu. Restricted: Allows access only to the following menus. Recents EM (or EMCC if extension mobility
                  is configured) User preferences Network and service (if any other custom service or VPN
                  is configured) Accessibility Allows access only to the following menus. EM (or EMCC if extension mobility
                  is configured) Audio Screen Network and service (if any other custom service or VPN
                  is configured) Accessibility This option prevents access to other options in the Settings menu. |
| 4 | Select Save . |
| 5 | Select Apply Config . |
| 6 | Restart the phone. |

| 1 | In Cisco Unified Communications Manager Administration, select System > Device Pool . |
|---|---|
| 2 | Locate the device pool that you need to set up. |
| 3 | Navigate to the Roaming Sensitive Settings area and select a
          group from the Date/Time Group field. |
| 4 | Select Save . |
| 5 | (Optional) If you want to create or modify a Date/Time group, do the following: Select System > Date/Time Group . Navigate to the Date/Time Group Information area, set the
              following parameters: Group Name : Enter a unique for the Date/Time group. Time Zone : Select a proper time zone for the Date/Time
                  group. Time Format : Select a time format that the phone
                  displays. The settings to the parameters Separator and Date Format don't take effect. Select Save . |

| 1 | To configure
			 wideband support for all devices: On Cisco Unified Communications Manager Administration, click System > Enterprise Parameters Set the Advertise G.722 and iSAC Codec field. The default value of this enterprise parameter is True , which means that all Cisco IP Phone Models that register to this Cisco Unified CM advertise G.722. If each endpoint in an attempted call supports G.722 in the capabilities set, Cisco Unified CM uses that codec for the call whenever possible. |
|---|---|
| 2 | To configure
			 wideband support for a specific device: On Cisco Unified Communications Manager Administration, choose Device > Phone . Set the Advertise G.722 and iSAC Codec parameter in the Product Specific Configuration area. The default value of this product-specific parameter is to use the value that the enterprise parameter specifies. If you want to override this on a per-phone basis, choose Enabled or Disabled |

| 1 | In Cisco Unified Communications Manager Administration, select Device > Device Settings > SIP Profile |
|---|---|
| 2 | Set the Start Media Port and Stop Media Port fields for the audio port range. |
| 3 | Select Save . |
| 4 | Navigate to one of the following windows: System > Enterprise Phone Configuration Device > Device Settings > Common Phone Profile Device > Phone > Phone Configuration |
| 5 | Set the Start Video RTP Port and Stop Video RTP Port fields for the range of ports required. The value for Stop Video RTP Port must be at least 16 larger
              than the value for Start Video RTP Port . |
| 6 | Select Save . |

| Video type | Video resolution | Frames per second (fps) | Video bit rate range |
|---|---|---|---|
| 1080p | 1920 x 1080 | 30 | 3500–4000 kbps |
| 1080p | 1920 x 1080 | 15 | 2667–4000 kbps |
| 720p | 1280 x 720 | 30 | 2040–3750 kbps |
| 720p | 1280 x 720 | 15 | 1185–3750 kbps |
| 600p | 1024 x 600 | 30 | 1584–3000 kbps |
| 600p | 1024 x 600 | 15 | 840–3000 kbps |
| WVGA | 800 x 480 | 30 | 990–1500 kbps |
| WVGA | 800 x 480 | 15 | 525–1500 kbps |
| VGA | 640 x 480 | 30 | 520–1500 kbps |
| VGA | 640 x 480 | 15 | 280–1500 kbps |
| 360p | 640 x 360 | 30 | 600–1350 kbps |
| 360p | 640 x 360 | 15 | 315–1350 kbps |
| 240p | 432 x 240 | 30 | 270–525 kbps |
| 240p | 432 x 240 | 15 | 96–525 kbps |
| CIF | 352 x 288 | 30 | 200–350 kbps |
| CIF | 352 x 288 | 15 | 120–350 kbps |
| SIF | 352 x 240 | 30 | 200–350 kbps |
| SIF | 352 x 240 | 15 | 120–350 kbps |
| QCIF | 176 x 144 | 30 | 94–350 kbps |
| QCIF | 176 x 144 | 15 | 64–350 kbps |
| QCIF | 176 x 144 | 15 | 17–350 kbps |

| 1 | Set up a server that can run your PRT upload script. |
|---|---|
| 2 | Write a script that can handle the parameters listed above, or edit the provided sample
          script to suit your needs. |
| 3 | Upload your script to your server. |
| 4 | In Cisco Unified Communications Manager, go to the Product Specific
            Configuration Layout area of the individual device configuration window,
          Common Phone Profile window, or Enterprise Phone Configuration window. |
| 5 | Check Customer support upload URL and enter your upload server
          URL. Example : http://example.com/prtscript.php |
| 6 | Save your changes. |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 3 | Set the Always Use Multi-line Mode field to Enabled . |
| 4 | Select Save . |
| 5 | Select Apply Config . |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 3 | Configure the following parameters: Web Access : Set the Web Access field to Enabled . HTTPs Server : Choose HTTP and HTTPS
                  Enabled to allow both protocols, or HTTPS Only to allow secure connections only, based on your server’s configuration. xAPI Admin User Name : Enter the administrator username used
                to authenticate xAPI requests to the phone. xAPI Admin Password : Enter the password associated with the
                xAPI administrator username to authorize remote access and management. |
| 4 | Select Save . |
| 5 | Select Apply Config . |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 3 | Set Video Capability on Webex to Enabled . |
| 4 | Select Save . |
| 5 | Select Apply Config . |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Go to Device > Phone . |
| 3 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 4 | Choose a value from the Minimum Ring Volume drop-down
          list. The default setting is 0-Silent , which allows users to mute the
          ringer. If a minimum volume is set, the phone will display a notification when users reach
          the minimum level. |
| 5 | Select Save . |
| 6 | Select Apply Config . |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Go to Device > Phone . |
| 3 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 4 | Enable or disable MARI and MARI FEC based
          on your network conditions. |
| 5 | Select Save . |
| 6 | Select Apply Config . |

| 1 | Configure your SDP transparency profile or create a new one with MARI attributes. From Cisco Unified CM Administration, choose Device > Device Settings > SDP Transparency Profile . Open your SDP profile to configure it. If you don't have any SDP transparency profile configured, click Add
                  New and enter a name and description. In the Attribute Information pane, create rules with the
              following attributes: Attribute name Type cisco-mari Any Value cisco-mari-rate Property Click Save . | Attribute name | Type | cisco-mari | Any Value | cisco-mari-rate | Property |
|---|---|---|---|---|---|---|---|
| Attribute name | Type |
| cisco-mari | Any Value |
| cisco-mari-rate | Property |
| 2 | Apply your SDP transparency profile to the SIP profile that your phones use. Choose Device > Device Settings > SIP Profile . Find and open your SIP profile. In the SDP Information section, select your SDP transparency
              profile in the SDP Transparency Profile drop-down list. Click Save . |

| Attribute name | Type |
|---|---|
| cisco-mari | Any Value |
| cisco-mari-rate | Property |

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. |
| 3 | Set the Acoustic Shock Protection field to Enabled . |
| 4 | Select Save . |
| 5 | Select Apply Config . |

## Figuras

![the graphic for switching to Unified OS Administration](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/475001-476000/475747.png)

![For 9811, 9841,9851, and 9861](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489180.png)

![for 9871](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483152.png)

![For 8875](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489178.png)

![Icon for 9871 and 8875 for common topics](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/485001-486000/485950.png)