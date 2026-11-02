---
doc_id: help-webex-com-en-us-article-mdos1db-configure-calling-features-f90aa851f3
source_url: https://help.webex.com/en-us/article/mdos1db/Configure-calling-features
retrieved_at: 2026-11-02T13:13:11.942810+00:00
---

## Shared lines

A shared line is a directory number that appears on more than one phone. You can create a shared line by assigning the same phone number to various phones.

Incoming calls display on all phones that share a line, and anyone can answer the call. Only one call remains active at a time on a phone.

Call information displays on all phones that are sharing a line. If somebody turns on the privacy feature, you don't see the outbound calls made from the phone. However, you see inbound calls to the shared line.

All phones with a shared line ring when a call is made to the line. If you place the shared call on hold, anyone shared with the line can resume the call on their phones.

The following shared line features are supported:

Line Seizure

Public Hold

Private Hold

Silent Barge (only through enabled programmable softkey)

The following features are supported as for a private line

Transfer

Conference

Call Park / Call Retrieve

Call Pickup

Do Not Disturb

Call Forward

You can configure each phone independently. Account information is usually the same for all IP phones, but settings such as the dial plan or preferred codec information can vary.

### Configure a shared line

You can create a shared line by assigning the same directory number to more than one phone on the phone web page.

You can also configure the parameters in the phone configuration file with XML (cfg.xml) code. To configure each parameter, see the syntax of the string in the following table of Parameters for configuring a shared line .

Access the phone administration web page.

Select Voice > Ext(n) , where (n) is the number of an extension to share.

In the General section, set the Line Enable parameter as described in the following table of Parameters for shared lines .

In the Share Line Appearance section, set Share Ext , Shared User ID field and Subscription Expires parameters as described in the following table of Parameters for shared lines .

In the Proxy and Registration section, enter the IP address of the proxy server in the Proxy field.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Proxy_1_ ua="na">as1bsoft.sipurash.com</Proxy_1_>
```

Example for proxy server address: as1bsoft.sipurash.com

In the Subscriber Information section, enter the Display Name and User ID (extension number) for the shared extension.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Display_Name_1_ ua="na">name</Display_Name_1_>
<User_ID_1_ ua="na">4085273251</User_ID_1_>
```

In the Miscellaneous Line Key Settings section, set SCA Barge-In Enable parameter as described in the following table of Miscellaneous line key settings .

Click Submit All Changes.

### Parameters for configuring a shared line

The following table describes the parameters in the Voice > Ext(n) tab of the phone web page.

Parameter

Description

Line Enable

Enables a line for the service.

Perform one of the following:

In the phone web interface, select yes to enable. Otherwise, select No .

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Line_Enable_1_ ua="na">Yes</Line_Enable_1_>
```

Valid values: Yes|No

Default: Yes

Share Ext

Indicates whether other Cisco IP phones share this extension is, or the extension is private.

Perform one of the following:

In the phone web interface, select yes to enable. Otherwise, select No .

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Share_Ext_1_ ua="na">No</Share_Ext_1_>
```

If you set Share Ext to No , this extension is private and doesn't share calls, regardless of the Share Line Appearance setting. If you set this extension to Yes , calls follow the Share Line Appearance setting.

Valid values: Yes|No

Default: Yes

Shared User ID

The user identified assigned to the shared line appearance.

Perform one of the following:

In the phone web interface, enter the user ID.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Shared_User_ID_1_ ua="na">Shared UserID</Shared_User_ID_1>
```

Subscription Expires

Number of seconds before the SIP subscription expires. Before the subscription expiration, the phone gets NOTIFY messages from the SIP server on the status of the shared phone extension.

Perform one of the following:

In the phone web interface, enter the value in seconds.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<Subscription_Expires_1_ ua="na">3600</Subscription_Expires_1_>
```

Valid values: An integer from 10 through 65535

Default: 3600 seconds

The following table describes the parameters in the Voice > Phone tab of the phone web page.

Parameter

Description

SCA Barge-In Enable

Enables the SCA Barge-In.

Perform one of the following:

In the phone web interface, select Yes to enable. Otherwise, select No .

In the phone configuration file with XML(cfg.xml), enter a string in this format:

```
<SCA_Barge-In-Enable ua="na">No</SCA_Barge-In-Enable>
```

Valid values: Yes|No

Default: No

## Call Park

The user can retrieve a parked call using the call unpark code on any phone within the organization. If you have configured the call park shortcut on an extension, the user can retrieve the parked call with a single tap on the extension.

### Enable call park feature

When you enable the call park feature on the phone, the users can park a call or retrieve a parked call on the phone. When disabled, the Call park/unpark softkey doesn't show on the phone screen.

Access the phone administration web page.

Select Voice > Phone .

In the Supplementary Services section, set Call Park Serv to Yes to enable the feature on the phone.

```
<Call_Park_Serv ua="na">Yes</Call_Park_Serv>
```

Options: Yes and No

Default: Yes

Click Submit All Changes .

### Configure Call Park codes

You can configure
		  call park so that the user can put a call on hold and then retrieve the call
		  from either the user's phone or another phone.

When configuring call park, the Call Park Code and the Call Unpark Code must match the Feature Access Code configured on the server.

Access the phone administration web page.

Select Voice > Regional .

Enter *68 in the Call
				Park Code field.

You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format:

```
<Call_Park_Code ua="na">*68</Call_Park_Code>
```

Enter *88 in the Call
				Unpark Code field.

You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format:

```
<Call_Unpark_Code ua="na">*88</Call_Unpark_Code>
```

Click Submit
				All Changes .

### Add Call Park shortcut to an idle extension

You can add call park to an idle extension to enable the user to temporarily store and retrieve calls. Call Park is supported on private lines and shared lines. When configured, the user can park and unpark a call through the extension.

Access the phone administration web page.

Select Voice > Att Console > General .

Select No for the parameter BLF Callpark On Line Key Enable to disable the Busy Lamp Field (BLF) Call Park feature on the phone.

Select Voice > Phone .

Select a line key.

(Optional) Set the Extension parameter to Disabled .

If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step.

You can also configure the parameter in the configuration file (cfg.xml). The parameter is line-specific. Enter a string in the following format:

```
<Extension_2_ ua="na">Disabled</Extension_2_>
```

In the Extended Function parameter, enter a string in this format:

For a private line, enter

```
fnc=prk;sub=$USER@$PROXY;nme=callpark;vid=1;
```

For a shared line, enter

```
fnc=prk;sub=$USER@$PROXY;nme=callpark;orbit=<DN of shared line>;vid=1;
```

Where,

fnc=prk means function=call park

sub is the SIP URI of the monitored park slot.

nme is the name displayed on the phone for the call park line key.

orbit is the DN of the shared line.

vid is the extension ID. The values of $USER and $PROXY are retrieved from the specified extension. If vid is missing in the function string, the values of $USER and $PROXY are retrieved from extension 1.

You can also configure the line-specific parameter in the configuration file (cfg.xml). Enter a string in the following format:

```
<Extended_Function_2_ ua="na">fnc=prk;sub=$USER@$PROXY;nme=callpark;vid=1;</Extended_Function_2_>
```

Click Submit
				All Changes .

### Configure One-Button Call Park

With One-Button Call Park, there is no need to enter a combination of key strokes for parking and unparking a call.

You can also configure parking calls in a dedicated call park extension

Access the phone administration web page.

Go to Voice > Att Console .

In the BLF List URI field, enter uri_name@server .

The BLF List URI field must have the same value as that configured for the List URI:sip parameter on the BroadSoft server.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<BLF_List_URI ua="na">uri_name@server</BLF_List_URI>
```

From the BLF List Feature Options drop down list, select prk .

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<BLF_List_Feature_Options ua="na">prk</BLF_List_Feature_Options>
```

The allowed values are blf+sd+cp|prk. The default value is blf+sd+cp.

When the BLF List Feature Options field is set to blf+sd+cp , the auto-assigned keys can be used for blf+sd+cp function or a call park function. If type="park" is included in the resource element, then the auto-assigned keys are used for call park function, else it is used for blf+sd+cp function when the type is not included.

In the server, there are three resource elements in NOTIFY requests. Enter the strings in the resource elements in the format and add new attribute type="park" in the call park extension resource URI:

```
<resource uri="sip:test01@as1bsoft.sipurash.com"><name>test 01</name><instance id="cROdMctbQE" state="active" cid="BQQ7uR@broadworks"/></resource>
```

```
<resource uri="sip:2345@as1bsoft.sipurash.com" type="park"><name>Park Location1</name><instance id="cROdMctbQE" state="active" cid="BQQ8uR@broadworks"/></resource>
```

```
<resource uri="sip:test02@as1bsoft.sipurash.com"><name>test 02</name><instance id="cROdMctbQE" state="active" cid="BQQ9uR@broadworks"/></resource>
```

After successful configuration, the phone monitors test 01, Park Location1, and test 02. If call park extensions and users are subscribed successfully, linekeys will be assigned for callpark or blf function respectively, and get the monitored extension and user status.

When the BLF List Feature Options field is set to prk , the BLF List URI monitors call park extensions and users.

In the server, there are three resource elements in NOTIFY requests. Enter the strings in the resource elements in the format and add new attribute type="park" in the call park extension resource URI:

```
<resource uri="sip:test01@as1bsoft.sipurash.com"><name>test 01</name><instance id="cROdMctbQE" state="active" cid="BQQ7uR@broadworks"/></resource>
```

```
<resource uri="sip:2345@as1bsoft.sipurash.com" type="park"><name>Park Location1</name><instance id="cROdMctbQE" state="active" cid="BQQ8uR@broadworks"/></resource>
```

```
<resource uri="sip:test02@as1bsoft.sipurash.com"><name>test 02</name><instance id="cROdMctbQE" state="active" cid="BQQ9uR@broadworks"/></resource>
```

After successful configuration, the phone monitors test 01, Park Location1, and test 02. If call park extensions and users are subscribed successfully, linekeys will be assigned for call park function and get the monitored extension and user status.

Click Submit All Changes .

### Add BLF call park on a line key

You can add the call park feature on a specific line key to use only a single button to park or unpark a call for a monitored user.

This topic is for Cisco Desk Phone 9800 Series registered to BroadWorks.

Select Voice > Att Console > General .

Select Yes for the parameter BLF Callpark On Line Key Enable .

To disable the feature, select No .

You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<BLF_Callpark_On_Line_Key_Enable ua=”na“>Yes</BLF_Callpark_On_Line_Key_Enable>
```

Default: No .

Navigate to Voice > Phone and select a line key.

(Optional) Set the Extension parameter to Disabled .

If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step.

You can also configure the parameter in the configuration file (cfg.xml). The parameter is line-specific. Enter a string in the following format:

```
<Extension_2_ ua="na">Disabled</Extension_2_>
```

Enter the string in the following format in the Extended Function field:

```
fnc=prk;sub=BLF_URI;usr=$USER@$PROXY;
or
fnc=prk;sub=BLF_URI;ext=$USER@$PROXY;
```

- fnc=prk means feature is call park

- sub— the URI to which the SUBSCRIBE message is sent. This name must be identical to the name defined in the BLF List URI.

- usr— the call park extension that the BLF monitors.

Click Submit All Changes .

### Show the call parked status on the home screen

You can choose to show or hide the call parked status that displays on the phone home screen.

By default, the display of the call parked status is disabled on the phone home screen.

If enabled, the users can be notified with the call parked status, so they can retrieve the parked call from the line.

Access the phone administration web page.

Select Voice > Ext(n) , where (n) is the number of an extension to share.

In the Call Feature Settings section, set Call Park Monitor Enable to Yes or No to show or hide the call parked status from the phone home screen.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Call_Park_Monitor_Enable_1_ ua="na">Yes</Call_Park_Monitor_Enable_1_>
```

Options: Yes and No

Default: No

Click Submit All Changes .

## Emergency call

### Emergency Call Support Background

Emergency call service providers can register a phone's location for each IP-based phone in a company. The location information server (LIS) transfers the emergency response location (ERL) to the phone. The phone stores its location during registration, after the phone restarts, and when a person signs in to the phone. The location entry can specify the street address, building number, floor, room, and other office location information.

When you place an emergency call, the phone transfers the location to the call server. The call server forwards the call and the location to the emergency call service provider. The emergency call service provider forwards the call and a unique call-back number (ELIN) to the emergency services. The emergency service or public safety answering point (PSAP) receives the phone location. The PSAP also receives a number to call you back, if the call disconnects.

You insert the following parameters to obtain the phone's location for any phone extension number:

Company Identifier–A Unique number (UUID) assigned to your company by the NG9-1-1 service provider.

Primary Request URL–The HTTPS address of the primary server used to obtain the phone location.

Secondary Request URL–The HTTPS address of a secondary server (backup) used to obtain the phone location.

Emergency Number–A sequence of digits that identify an emergency call. You can specify multiple emergency numbers, by separating each emergency number with a comma.

Common emergency service numbers include:

North America–911

European countries–112

Hong Kong–999

The phone requests new location information for the following activities:

You register the phone with the call server.

A person restarts the phone and the phone was previously registered with the call server.

A guest signs in to the phone.

You change the IP address of the phone.

If all of the location servers do not send a location response, the phone re-sends the location request every two minutes.

### Emergency call support terminology

The following terms describe emergency call support for the phones.

Emergency Location ID Number (ELIN)–A number used to represent one or more phone extensions that locate the person who dialed emergency services.

Emergency Response Location (ERL)–A logical location that groups a set of phone extensions.

HTTP Enabled Location Delivery (HELD)–An encrypted protocol that obtains the PIDF-LO location for a phone from a location information server (LIS).

Location Information Server (LIS)–A server that responds to a SIP-based phone HELD request and provides the phone location using a HELD XML response.

Emergency Call Service Provider–The company that responds to a phone HELD request with the phone's location. When you make an emergency call (which carries the phone's location), a call server routes the call to this company The emergency call service provider adds an ELIN and routes the call to the emergency services (PSAP). If the call is disconnected, the PSAP uses the ELIN to reconnect with the phone used to make the emergency call.

Public Safety Answering Point (PSAP)–Any emergency service (for example, fire, police, or ambulance) joined to the Emergency Services IP Network.

Universally Unique Identifier (UUID)–A 128-bit number used to uniquely identify a company using emergency call support.

### Configure a phone to make emergency calls

Before you begin

Obtain the E911 Geolocation Configuration URLs and the company identifier for the phone from your emergency call service provider. You can use the same Geolocation URLs and company identifier for multiple phone extensions in the same office area.

Access the phone administration web page.

Select Voice > Ext n , where n is the phone extension number (1-10) of the phone web dialog.

In the Dial Plan section, set the Emergency Number parameter

In the E911 Geolocation Configuration section, set the following parameters as described in Parameters for emergency calls :

- E911 Enable

- Location Source

- Company UUID

- Primary Request URL

- Secondary Request URL

Click Submit All Changes .

#### Parameters for emergency calls

The following table defines the function and usage of emergency calls parameters in the Dial Plan and E911 Geolocation Configuration sections under the Voice > Ext(n) tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Section: Dial Plan

Emergency Number

Enter a comma-separated list of emergency numbers.

To specify multiple emergency numbers, separate each emergency number with a comma.

When one of these numbers is dialed, the unit disables processing of CONF, HOLD, and other similar softkeys or buttons to avoid accidentally putting the current call on hold. The phone also disables hook flash event handling.

Only the far end can terminate an emergency call. The phone is restored to normalcy after the call is terminated and the receiver is back on-hook.

Perform one of the following: to the digits that correspond to the customer emergency service numbers.

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, set Emergency Number parameter to the digits that correspond to the customer emergency service numbers.

Valid Values: Maximum number length is 63 characters

Default: Blank (no emergency number)

Section: E911 Geolocation Configuration

If set to Yes, the phone will insert geolocation information into the SIP INVITE when placing an emergency call.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format: <E911_Enable_1_ ua="na" um="y">Yes</E911_Enable_1_>

In the phone web page, select Yes to enable this feature or select No to disable it.

Options: Yes and No

Default: Yes

If the phone is registered to Webex Calling or BroadWorks, select this option.

If the phone is registered to the call controllers that support LLDP MED TLV Location Identification Support, select this option. Currently, the feature isn't supported on Webex Calling and BroadWorks.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Location_Source_1_ ua="na" um="y">LLDP-MED</Location_Source_1_>

Options: HELD and LLDP-MED

Default: HELD

Company UUID

The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider.

For example:

07072db6-2dd5-4aa1-b2ff-6d588822dd46

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter a valid identifier assigned by the call services provider.

Valid Values: Maximum identifier length is 128 characters.

Default: Blank

Primary Request URL

Encrypted HTTPS phone location request. The request uses the phone IP addresses, MAC address, Network Access Identifier (NAI), and chassis ID and port ID assigned by the network switch manufacturer. The request also includes the location server name and the customer identifier.

The server used by the emergency call services provider responds with an Emergency Response Location (ERL) that has a location Uniform Resource Identifier (URI) tied to the user phone IP address.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter encrypted HTTPS phone location request.

For example:

https://prod.blueearth.com/e911Locate/held/held_request.action

Default: Blank

Secondary Request URL

Encrypted HTTPS request sent to the emergency call services provider's backup server to obtain the user's phone location.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the encrypted for the backup server that can return location information.

For example:

https://prod2.blueearth.com/e911Locate/held/held_request.action

Default: Blank

## Enable LED indication for missed calls

By default, the Top 360 LED is disabled for missed calls. You can enable the LED indication if you want to receive the missed call alerting more explicitly. Typically, you can find the missed call on the phone screen.

This topic is only available for Cisco Desk Phone 9800 Series.

Access the phone web page.

Select Voice > User .

The user can select User Login > Voice User .

In the Supplementary Services section, set the Missed Call Led Alert parameter to Enabled .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Missed_Call_Led_Alert ua="rw">Enabled</Missed_Call_Led_Alert>
```

Options: Enabled and Disabled

Default: Disabled

Click Submit All Changes .

## Do Not Disturb

### Enable the Do Not Disturb (DND) feature

When you enable the DND feature on the phone, the users can turn DND on and off with the Do not disturb softkey on the phone screen. When disabled, the DND softkey doesn't show on the phone screen.

Access the phone administration web page.

Select Voice > Phone .

In the Supplementary Services area, set DND Serv to Yes to enable DND for the phone.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<DND_Serv ua="rw">Yes</DND_Serv>
```

Options: Yes and No

Default: No

Click Submit All Changes .

### Turn Do Not Disturb (DND) on and off for lines

On the phone administration web page, you can switch the Do not disturb (DND) feature on or off on the phone.

Your setting applies to only the lines with Feature Key Sync (FKS) and XSI service for DND disabled. If the user changes the DND status on the phone, the change syncs to the web page. For the lines with FKS or XSI enabled, the changes don't sync between the phone and the web page.

Before you begin

Ensure that the DND feature is enabled on the Voice > Phone tab.

Make sure that you disable FKS and XSI service for DND on the lines that you want to apply the DND setting to.

Access the phone administration web page.

Select Voice > User .

In the Supplementary Services area, set DND Setting to Yes or No to turn on or off DND.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<DND_Setting ua="rw">Yes</DND_Setting>
```

Options: Yes and No

Default: No

Click Submit All Changes .

## Call forward

On the phone administration web page, you can enable the Call Forward feature for a phone on the Voice > Phone tab and turn call forward on and off for all lines on the Voice > User tab.

When you enable the Call Forward feature, the users can turn the feature on and off and specify the destination numbers for each line.

### Enable the Call Forward feature

Enable the Call Forward feature on the phone to allow the users to forward the incoming calls on their lines to another extension. When disabled, the users don't see the call forward options on their lines. When enabled, you can also configure the Call Forward feature for your uses on the Voice > User tab.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure each parameter, see the syntax of the string in the following table of Parameters for enabling Call Forward for a phone .

Access the phone administration web page.

Select Voice > Phone .

Under Supplementary Services , configure the parameters as described in the following table of Parameters for enabling Call Forward .

Click Submit All Changes .

Parameters for enabling Call Forward

The following table defines the function and usage of  Call Forward parameters in the Supplementary Services section under the Voice > Phone tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Cfwd All Serv

Forwards all calls.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward all calls. Select No to disable it.

Options: Yes and No

Default: Yes

Cfwd Busy Serv

Forwards calls only if the line is busy.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward calls when the line is busy. Select No to disable it.

Options: Yes and No

Default: Yes

Cfwd No Ans Serv

Forwards calls only if the line is not answered.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward calls if the line is not answered. Select No to disable it.

Options: Yes and No

Default: Yes

### Switch on and off Call Forward for lines

Use the call forward settings on the User tab to specify call forward destination and turn call forward on or off for the lines. The settings apply to only the lines with Feature key synchronization (FKS) and XSI synchronization disabled.

Your setting applies to only the lines with Feature Key Sync (FKS) and XSI service for call forward disabled. If the user changes the DND status on the phone, the change syncs to the web page. For the lines with FKS or XSI enabled, the changes don't sync between the phone and the web page.

Before you begin

Ensure that the Call Forward feature is enabled on the Voice > Phone tab.

Make sure that you disable FKS and XSI service for call forward on the lines that you want to apply the call forward setting to.

Access the phone administration web page.

Select Voice > User .

In the Call Forward section, configure the parameters as described in the following table of Call Forward Parameters on User tab .

Click Submit All Changes .

Call Forward parameters on User tab

#### Call Forward parameters on the User tab

The following table defines the function and usage of the Call Forward parameters on the Voice > User tab in the phone web page. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml) code to configure a parameter.

The parameters in the following table take effect only when FKS and XSI are disabled.

Parameter

Description

Cfwd All

Forwards all calls. The setting of this parameter takes precedence over Cfwd Busy and Cfwd No Answer.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward all calls. Select No to disable it.

Options: Yes and No

Default: No

Cfwd All Dest

Specifies the destination to which all calls are forwarded. The destination can be an alphanumeric input, a phone number, or a SIP URI.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the destination number in the field.

When you select Yes for Cfwd All , make sure to configure the parameter.

Default: Empty

Cfwd Busy

Forwards calls only if the line is busy.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward calls when the line is busy. Select No to disable it.

Options: Yes and No

Default: No

Cfwd Busy Dest

Specifies the destination to which calls are forwarded if the line is busy. The destination can be an alphanumeric input, a phone number, or a SIP URI.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the destination number in the field.

When you select Yes for Cfwd Busy, make sure to configure the parameter.

Default: Empty

Cfwd No Answer

Forwards the incoming call only if the call isn’t answered.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to forward the incoming call if the call isn't answered. Select No to disable it.

Options: Yes and No

Default: No

Cfwd No Ans Dest

Specifies the phone number of destination to which the incoming call is forwarded if the call isn’t answered. The destination can be an alphanumeric input, a phone number, or a SIP URI.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the destination number in the field.

When you select Yes for Cfwd No Answer, make sure to configure the parameter.

Default: Empty

Cfwd No Ans Delay

Assigns a response delay time (in seconds) for the no answer scenario.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, enter the delay time in the field.

Default: 20

## Call transfer

### Enable call transfer

You can enable attended call transfer and blind call transfer services for your user.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure each parameter, see the syntax of the string in the following table of Parameters for enabling call transfer .

Access the phone administration web page.

Select Voice > Phone .

Under Supplementary Services , configure the parameters as defined  in the following table of Parameters for enabling call transfer .

Click Submit All Changes .

### Parameters for enabling call transfer

The following table defines the function and usage of Call Transfer parameters in the Supplementary Services section under the Voice > Phone tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file with XML(cfg.xml) code to configure a parameter.

Parameter

Description

Attn Transfer Serv

Attended call transfer service. The user answers the call before transferring it.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the transfer service. Select No to disable it.

Options: Yes and No

Default: Yes

Blind Transfer Serv

Blind call transfer service. The user transfers the call without speaking to the caller.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web page, select Yes to enable the transfer service. Select No to disable it.

Options: Yes and No

Default: Yes

## Webex contacts and call logs

### Configure call logs to display on the phone

You can enable a phone to display call logs from Webex, the XSI server, or the local phone
        storage. When configured, the Display recents from menu on the Recents screen includes the specified data source in the list. The
        user then can set the phone to display the desired call history.

Before you begin

The phone is registered to Webex cloud successfully. For more information on phone onboarding to Webex cloud, see Webex for Cisco BroadWorks Solution Guide .

Access the phone administration web page.

Select Voice > Phone .

In the Call Log section, choose the line in the CallLog Associated Line list and select the desired option in the Display Recents From field.

Options: Phone|XSI Server|Webex

Default value of Display Recents From : Phone

You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format:

```
<CallLog_Associated_Line ua="na">1</CallLog_Associated_Line>
```

```
<Display_Recents_From ua="na”>Webex</Display_Recents_From>
```

To display only XSI call logs on the associated line, enter a string in this
            format:

```
<Display_Recents_From ua="na”>XSI Server</Display_Recents_From>
```

The Recents screen on the phone displays only XSI call logs when
            the associated line is selected.

Click Submit All Changes .

### Show Webex contacts on the phone

When you onboard a phone to Webex cloud successfully, you can enable the phone to support Webex contacts. When you enable this feature on the phone, your user can see the Webex directory under the phone directory list.

Before you begin

The phone is registered to Cisco Webex cloud successfully. For more information on phone onboarding to Webex Cloud, see Webex for Cisco BroadWorks Solution Guide .

Access the phone administration web page.

Select Voice > Phone .

In the Webex section, set the Directory Enable to Yes .

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Webex_Directory_Enable ua="na”>Yes</Webex_Directory_Enable>
```

Default value: No

In the Directory Name field, enter a name for the Webex directory.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Webex_Directory_Name ua="na”>wcdir</Webex_Directory_Name>
```

Default value: Empty

The name you enter (for example, wcdir ), displays as the Webex directory name on the phone under the directory list. You can modify this name from the phone administration web page or from the configuration XML file string. When the Directory Name field is empty, by default, the Webex directory name on the phone appears as Webex directory .

Click Submit All Changes .

## Vertical service activation codes

### Assign vertical service activation codes

Your phone users recognize Vertical Service Activation Codes as Feature Access Codes (FACs) or star codes. When configured, the users can dial the codes on their lines to activate and deactivate the corresponding services.

Access the phone administration web page.

Select Voice > Regional .

In the Vertical Service Activation Codes section, assign the codes to services as described in the following table of Vertical service activation codes .

### Vertical service activation codes

Parameter

Description

Call Return Code

This code calls the last caller.

Defaults to *69.

Blind Transfer Code

Begins a blind transfer of the current call to the extension specified after the activation code.

Defaults to *95.

Cfwd All Act Code

Forwards all calls to the extension specified after the activation code.

Defaults to *72.

Cfwd All Deact Code

Cancels call forward of all calls.

Defaults to *73.

Cfwd Busy Act Code

Forwards busy calls to the extension specified after the activation code.

Defaults to *90.

Cfwd Busy Deact Code

Cancels call forward of busy calls.

Defaults to *91.

Cfwd No Ans Act Code

Forwards no-answer calls to the extension specified after the activation code.

Defaults to *92.

Cfwd No Ans Deact Code

Cancels call forward of no-answer calls.

Defaults to *93.

CW Act Code

Enables call waiting on all calls.

Defaults to *56.

CW Deact Code

Disables call waiting on all calls.

Defaults to *57.

CW Per Call Act Code

Enables call waiting for the next call.

Defaults to *71.

CW Per Call Deact Code

Disables call waiting for the next call.

Defaults to *70.

Block CID Act Code

Blocks caller ID on all outbound calls.

Defaults to *61.

Block CID Deact Code

Removes caller ID blocking on all outbound calls.

Defaults to *62.

Block CID Per Call Act Code

Removes caller ID blocking on the next inbound call.

Defaults to *81.

Block CID Per Call Deact Code

Removes caller ID blocking on the next inbound call.

Defaults to *82.

Block ANC Act Code

Blocks all anonymous calls.

Defaults to *77.

Block ANC Deact Code

Removes blocking of all anonymous calls.

Defaults to *87.

DND Act Code

Enables the do not disturb feature.

Defaults to *78.

DND Deact Code

Disables the do not disturb feature.

Defaults to *79.

Secure All Call Act Code

Makes all outbound calls secure.

Defaults to *16.

Secure No Call Act Code

Makes all outbound calls not secure.

Defaults to *17.

Secure One Call Act Code

Makes a secure call.

Default: *18.

Secure One Call Deact Code

Disables secure call feature.

Default: *19.

Call Park Code

The star code used for parking the current call.

Defaults to *68.

Call Pickup Code

The star code used for picking up a ringing call.

Defaults to *97.

Call Unpark Code

The star code used for picking up a call from the call park.

Defaults to *88.

Group Call Pickup Code

The star code used for picking up a group call.

Defaults to *98.

Referral Services Codes

These codes tell the IP phone what to do when the user places the current call on hold and is listening to the second dial tone.

One or more *code can be configured into this parameter, such as *98, or *97|*98|*123, and so on. Max total length is 79 chars. This parameter applies when the user places the current call on hold (by Hook Flash) and is listening to second dial tone. Each *code (and the following valid target number according to current dial plan) entered on the second dial-tone triggers the phone to perform a blind transfer to a target number that is prepended by the service *code.

For example, after the user dials *98, the IP phone plays a special dial tone called the Prompt Tone while waiting for the user the enter a target number (which is checked according to dial plan as in normal dialing). When a complete number is entered, the phone sends a blind REFER to the holding party with the Refer-To target equals to *98<target_number>. This feature allows the phone to hand off a call to an application server to perform further processing, such as call park.

The *codes should not conflict with any of the other vertical service codes internally processed by the IP phone. You can empty the corresponding *code that you do not want to the phone to process.

Feature Dial Services Codes

These codes tell the phone what to do when the user is listening to the first or second dial tone.

One or more *code can be configured into this parameter, such as *72, or *72|*74|*67|*82, and so forth. The maximum total length is 79 characters. This parameter applies when the user has a dial tone (first or second dial tone). Enter *code (and the following target number according to current dial plan) entered at the dial tone triggers the phone to call the target number prepended by the *code. For example, after user dials *72, the phone plays a prompt tone awaiting the user to enter a valid target number. When a complete number is entered, the phone sends a INVITE to *72<target_number> as in a normal call. This feature allows the proxy to process features like call forward (*72) or BLock Caller ID (*67).

The *codes should not conflict with any of the other vertical service codes internally processed by the phone. You can empty the corresponding *code that you do not want to the phone to process.

You can add a parameter to each *code in Features Dial Services Codes to indicate what tone to play after the *code is entered, such as *72‘c‘|*67‘p‘. Below are a list of allowed tone parameters (note the use of back quotes surrounding the parameter without spaces)

• c = Cfwd Dial Tone

• d = Dial Tone

• m = MWI Dial Tone

• o = Outside Dial Tone

• p = Prompt Dial Tone

• s = Second Dial Tone

• x = No tones are place, x is any digit not used above

If no tone parameter is specified, the phone plays Prompt tone by default.

If the *code is not to be followed by a phone number, such as *73 to cancel call forward, do not include it in this parameter. In that case, simple add that *code in the dial plan and the phone sends INVITE *73@..... as usual when user dials *73.

## Enable users to add multiple people to a call

You can enable your user to talk to several people in a single call. When you enable this feature, your user can dial several people and add them to the call.

Access the phone administration web page.

Select Voice > Phone .

Under Supplementary Services , choose Yes for the Conference Serv parameter.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

```
<Conference_Serv ua="na">Yes</Conference_Serv>
```

Options: Yes and No

Default: Yes

Click Submit All Changes .

## Configure help desk with phone web page

Enable the help desk feature for your phones so that users can quickly dial out the quick numbers by using the Favorite button.

Access the phone administration web page.

Select Voice > Phone .

In the Help Desk section, choose Yes for the Help Desk Enable parameter.

(Optional) Set the parameter Custom Menu Name to customize the help desk display name on the phone screen. If it's empty, the display name is "Help Desk".

Enter the quick number and relevant name in Quick Number <n> and Name <n> respectively, where <n> represents the sequence number of the number. The maximum number of the quick numbers is 10.

If the name is empty and only the quick number is configured, the phone will repeatedly display the quick number as the name.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code:

Click Submit All Changes .

## Configure the number of call appearances per line

Each line can support multiple calls. By default, the phone supports two active calls per line, and a maximum of ten active calls per line. Only one call can be connected at any time; other calls are automatically placed on hold.

Phones that support multiple call appearances on a line can be configured to specify the number of calls to allow on the line.

Before you begin

Access the phone administration web page.

Select Voice > Phone .

In the Miscellaneous Line Key Settings section, for the Call Appearances Per Line parameter, specify the number of calls per line to allow.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Call_Appearances_Per_Line ua="na">2</Call_Appearances_Per_Line>
```

The allowed values range from 2 to 10. The default value is 2.

Click Submit All Changes .

## Configure alphanumeric dialing

You can configure a phone so that the user of the phone can make a call by dialing
        alphanumeric characters instead of dialing only digits. In the phone web page, you can
        configure alphanumeric dialing with speed-dial, blf, and call pickup.

Access the phone administration web page.

Select Voice > Ext(n) , where n is an
          extension number.

You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format:

```
<Enable_URI_Dialing_1_ ua="na">Yes</Enable_URI_Dialing_1_>
```

Select Voice > Phone , you can add a
          string on a line key in this format to enable speed dial with alphanumeric dialing
          capability:

```
fnc=sd;ext=xxxx.yyyy@$PROXY;nme=yyyy,xxxx
```

For example:

```
fnc=sd;ext=first.last@$PROXY;nme=Last,First
```

The above example will enable the user to dial "first.last" to make a call.

The supported characters that you can use for alphanumeric dialing are a-z, A-Z, 0-9,
              -, _, ., and +.

Phone also supports plus dialing in which you dial E.164 numbers prefixed with a plus
              (+) sign. To dial the + sign, the user needs to press and hold the star (*) key for at
              least 1 second. This applies to dialing the first digit for an on-hook (including edit
              mode) or off-hook call.

## Dial plan

Dial plans determine how digits are interpreted and transmitted. They also determine
        whether the dialed number is accepted or rejected. You can use a dial plan to facilitate
        dialing or to block certain types of calls such as long distance or international.

Use the phone web user interface to configure dial plans on the IP phone.

This section includes information that you must understand about dial plans, and procedures
        to configure your own dial plans.

The Cisco IP Phone has various levels of dial plans and processes the digits sequence.

When a user presses the speaker button on the phone, the following sequence of events
        begins:

The phone begins to collect the dialed digits. The interdigit timer starts to track the
            time that elapses between digits.

- If the interdigit timer value is reached, or if another terminating event occurs, the
          phone compares the dialed digits with the IP phone dial plan. This dial plan is configured
          in the phone web user interface in Voice > Ext(n) under the Dial Plan section.

### Digit sequences

A dial plan contains a series of digit sequences, separated by the | character. The entire
        collection of sequences is enclosed within parentheses. Each digit sequence within the dial
        plan consists of a series of elements that are individually matched to the keys that the
        user presses.

White space is ignored, but can be used for readability.

Digit Sequence

Function

0 1 2 3 4 5 6 7 8 9 0 * #

Characters that represent a key that the user must press on the phone keypad.

x

Any character on the phone keypad.

[sequence]

Characters within square brackets create a list of accepted key presses. The user
                  can press any one of the keys in the list.

A numeric range, for example, [2-9] allows a user to press any
                  one digit from 2 through 9 .

A numeric range can include other characters. For example, [35-8*] allows a user to press 3, 5, 6, 7, 8, or *.

.  (period)

A period indicates element repetition. The dial plan accepts 0 or more entries of the digit. For example, 01 . allows users to
                  enter 0, 01, 011, 0111, and so forth.

<dialed:substituted>

When the user presses 8 followed by a seven-digit number, the system
                  automatically replaces the dialed 8 with the sequence 1650 . If the user dials 85550112 , the system transmits 16505550112 .

If the dialed parameter is empty and there is a value in the substituted field, no digits are replaced and the substituted value is
                  always prepended to the transmitted string. For example:

```
<:1>xxxxxxxxxx
```

When the user dials 9725550112 , the number 1 is added at the beginning of
                  the sequence; the system transmits 19725550112 .

,  (comma)

```
9, 1xxxxxxxxxx
```

An outside line dial tone plays after the user presses 9 . The
                  tone continues until the user presses 1 .

!  (exclamation point)

```
1900xxxxxxx!
```

Rejects any 11-digit sequence that begins with 1900.

*xx

Allows a user to enter a 2-digit star code.

S0 or L0

For Interdigit Timer Master Override, enter S0 to reduce
                  the short interdigit timer to 0 seconds, or enter L0 to
                  reduce the long interdigit timer to 0 seconds.

P

To pause, enter P , the number of seconds to pause, and a space.
                  This feature is typically used for implementation of a hotline and warm line, with
                  a 0 delay for the hot line, and a nonzero delay for a warm line. For example:

```
P5
```

A pause of 5 seconds is introduced.

Examples:

The following examples show digit sequences that you can enter in a dial plan. In a
        complete dial plan entry, sequences are separated by a pipe character (|), and the entire
        set of sequences is enclosed within parentheses.

```
[1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! |
9, 011xxxxxx. | 0 | [49]11 ) | [*#]xx[*#] | #xx+xxxxxxxxxxx*xxxxxxxxxx
```

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! |
9, 011xxxxxx. | 0 | [49]11 ) | [*#]xx[*#] | #xx+xxxxxxxxxxx*xxxxxxxxxx
```

- Extensions on your system:

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
```

```
[1-8]xx
```

```
[1-8]xxx
```

- Local dialing with seven-digit number:

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]111)
```

9, xxxxxxx After a user presses 9, an external dial tone sounds. The
        user can enter any seven-digit number, as in a local call.

- Local dialing with 3-digit area code and a 7-digit local number:

```
[1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
9, <:1>[2-9]xxxxxxxxx
```

This example is useful where a local area code is required. After a user presses 9, an
        external dial tone sounds. The user must enter a 10-digit number that begins with a digit 2
        through 9. The system automatically inserts the 1 prefix before it transmits the number to
        the carrier.

- Local dialing with an automatically inserted 3-digit area code:

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
8, <:1212>xxxxxxx
```

This example is useful where a local area code is required by the carrier but most calls go
        to one area code. After the user presses 8, an external dial tone sounds. The user can enter
        any seven-digit number. The system automatically inserts the 1 prefix and the 212 area code
        before it transmits the number to the carrier.

- U.S. long-distance dialing:

```
[1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
9, 1 [2-9] xxxxxxxxx
```

After the user presses 9, an external dial tone sounds. The user can enter any 11-digit
        number that starts with 1 and is followed by a digit 2 through 9.

- Blocked number:

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
9, 1 900 xxxxxxx !
```

This digit sequence is useful if you want to prevent users from dialing numbers that are
        associated with high tolls or inappropriate content, such as 1-900 numbers in the U.S. After
        the user presses 9, an external dial tone sounds. If the user enters an 11-digit number that
        starts with the digits 1900, the call is rejected.

- U.S. international dialing:

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
9, 011xxxxxx
```

After the user presses 9, an external dial tone sounds. The user can enter any number that
        starts with 011, as in an international call from the U.S.

- Informational numbers:

```
( [1-8]xx | 9, xxxxxxx | 9, <:1>[2-9]xxxxxxxxx | 8, <:1212>xxxxxxx | 9, 1 [2-9] xxxxxxxxx
| 9, 1 900 xxxxxxx ! | 9, 011xxxxxx. | 0 | [49]11 )
0 | [49]11
```

This example includes two-digit sequences, separated by the pipe character. The first
        sequence allows a user to dial 0 for an operator. The second sequence allows the user to
        enter 411 for local information or 911 for emergency services.

- Service activation codes:

```
[*#]xx[*#]
```

Allows the user to dial # codes and * codes to access functions.

- Service activation codes with additional parameters :

Allows the user to dial a # code, followed by two 10-digit numbers.

### Acceptance and Transmission of the Dialed Digits

When a user dials a series of digits, each sequence in the dial plan is tested as a
        possible match. The matching sequences form a set of candidate digit sequences. As the user
        enters more digits, the set of candidates diminishes until only one or none is valid. When a
        terminating event occurs, the IP PBX either accepts the user-dialed sequence and initiates a
        call, or else rejects the sequence as invalid. The user hears the reorder (fast busy) tone
        if the dialed sequence is invalid.

The following table explains how terminating events are processed.

Terminating Event

Processing

Dialed digits have not matched any sequence in the dial plan.

The number is rejected.

Dialed digits exactly match one sequence in the dial plan.

If the dial plan allows the sequence, the number is accepted and is transmitted
                  according to the dial plan.

If the dial plan blocks the sequence, the number is rejected.

A timeout occurs.

The number is rejected if the dialed
                  digits are not matched to a digit sequence in the dial plan within the time that
                  the applicable interdigit timer specifies.

The Interdigit Long Timer applies when
                  the dialed digits do not match any digit sequence in the dial plan.

Default: 10 seconds.

The Interdigit Short Timer applies
                  when the dialed digits match one or more candidate sequences in the dial plan.
                  Default: 3 seconds.

A user presses the # key or the dial softkey on the IP phone screen.

If the sequence is complete and is
                  allowed by the dial plan, the number is accepted and is transmitted according to
                  the dial plan.

If the sequence is incomplete or is
                  blocked by the dial plan, the number is rejected.

### Dial Plan Timer (Off-Hook Timer)

You can think of the Dial Plan Timer as the off-hook timer. This timer starts when the
        phone goes off hook. If no digits are dialed within the specified number of seconds, the
        timer expires and the null entry is evaluated. Unless you have a special dial plan string to
        allow a null entry, the call is rejected.

The timer before a number is dialed is whichever shorter of the dial plan default timer
          and the dial tone timer set in the Dial Tone field on the Regional tab.

#### Syntax for the Dial Plan Timer

```
(Ps<:n> | dial plan)
```

s: The number of seconds; The timer before a number is dialed is whichever shorter of
        the dial plan default timer and the dial tone timer set in the Dial Tone field. With
        the timer set to 0 seconds, the call transmits automatically to the specified extension when
        the phone goes off hook.

n: (optional): The number to transmit automatically when the timer expires; you can
        enter an extension number or a DID number. No wildcard characters are allowed because the
        number is transmitted as shown. If you omit the number substitution, <:n>, the user hears
        a reorder (fast busy) tone after the specified number of seconds.

#### Examples for the Dial Plan Timer

The actual timer before a number is dialed is whichever shorter of the dial plan default
          timer and the dial tone timer set in the Dial Tone field. In the following
          examples, the dial tone timer is assumed to be longer than the dial plan timer.

Allow more time for users to start dialing after taking a phone off
        hook:

```
(P9 | (9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)
```

P9 means that after taking a phone off hook, a
        user has 9 seconds to begin dialing. If no digits are pressed within 9 seconds, the user
        hears a reorder (fast busy) tone. By setting a longer timer, you allow more time for users
        to enter digits.

To create a hotline for
        all sequences on the System Dial Plan:

P9<:23> means
        that after taking the phone off hook, a user has 9 seconds to begin dialing. If no digits
        are pressed within 9 seconds, the call is transmitted automatically to extension 23.

To create a hotline on a line button for an
        extension:

```
(P0 <:1000>)
```

With the timer set to 0 seconds,
        the call is transmitted automatically to the specified extension when the phone goes off
        hook. Enter this sequence in the Phone Dial Plan for Ext 2 or higher on a client
      phone.

### Interdigit Long Timer (Incomplete Entry Timer)

You can think of this timer as the incomplete
        entry timer. This timer measures the interval between dialed digits. It applies as long as
        the dialed digits do not match any digit sequences in the dial plan. Unless the user enters
        another digit within the specified number of seconds, the entry is evaluated as incomplete,
        and the call is rejected. The default value is 10 seconds.

This section explains how to edit a timer as
        part of a dial plan. Alternatively, you can modify the Control Timer that controls the
        default interdigit timers for all calls.

#### Syntax for the Interdigit Long Timer

```
L:s, (dial plan)
```

s: The number of seconds; if no number is entered after L:, the default timer is 5
        seconds. With the timer set to 0 seconds, the call is transmitted automatically to the
        specified extension when the phone goes off hook.

Note that the timer sequence appears to the left
        of the initial parenthesis for the dial plan.

L:15 means that this dial
        plan allows the user to pause for up to 15 seconds between digits before the Interdigit Long
        Timer expires. This setting is especially helpful to users such as sales people, who are
        reading the numbers from business cards and other printed materials while
      dialing.

### Interdigit Short Timer (Complete Entry Timer)

You can think of this timer as the
        complete entry timer. This timer measures the interval between dialed digits. The timer
        applies when the dialed digits match at least one digit sequence in the dial plan. Unless
        the user enters another digit within the specified number of seconds, the entry is
        evaluated. If the entry is valid, the call proceeds. If the entry is invalid, the call is
        rejected.

Default: 3 seconds.

SYNTAX
          1:

```
S:s, (dial plan)
```

Use this
        syntax to apply the new setting to the entire dial plan within the parentheses.

SYNTAX 2: sequence Ss

Use this syntax to apply
        the new setting to a particular dialing sequence.

s: The number of seconds; if no number is
        entered after S, the default timer of 5 seconds applies.

S:6 means that while the user enters a number with the phone off
        hook, the user can pause for up to 15 seconds between digits before the Interdigit Short
        Timer expires. This setting is especially helpful to users such as sales people, who are
        reading the numbers from business cards and other printed materials while dialing.

Set
        an instant timer for a particular sequence within the dial plan:

## Edit the dial plan

Access the phone administration web page.

Select Voice > Ext(n) , where n is an
          extension number.

Scroll to the Dial Plan section.

Enter the digit sequences in the Dial Plan field.

The default (US-based) systemwide dial plan appears in the field by default.

Modify the digit sequences. You can delete digit sequences, add digit sequences, or
          replace the entire dial plan with a new dial plan.

Separate each digit sequence with a pipe character, and enclose the entire set of digit
            sequences within parentheses. Example:

```
(9,8<:1408>[2-9]xxxxxx | 9,8,1[2-9]xxxxxxxxx | 9,8,011xx. | 9,8,xx.|[1-8]xx)
```

Click Submit All Changes .

The phone reboots.

Verify that you can successfully complete a call with each digit sequence that you
          entered in the dial plan.

If you hear a reorder (fast busy) tone, review your entries
            and modify the dial plan appropriately.

## Add outbound proxy survivability support

You can configure a phone with the ability to register to the Site Survivability Gateway (SGW) nodes when WxC SSE nodes are unreachable.

Access the phone administration web page.

Select Voice > Ext (n) .

In the Proxy and Registration section, set up Survivability Proxy and Survivability Proxy Fallback Intvl fields as described in the following table:

The parameter can be configured with an extension that includes a statically-configured SRV record. This allows phone to perform a failover to a survivability gateway.

Perform one of the following:

<Survivability_Proxy_n_>hostname[:port][:A=ip-list] [| hostname2[:port][:A=ip-list]]</Survivability_Proxy_n_>

hostname[:port][:A=ip-list] [| hostname2[:port][:A=ip-list]]

Where: ip-list: ip-addr[,ip-addr[,ip-addr…]]

Default: port=0

Example: wxclsg.example.com:8933:A=192.169.10.1

where,

wxclsg.example.com=Provisioned SGW hostname. It is used for TLS certificate validation when connecting to SGW nodes.

8933=SGW port

192.169.10.1=Provisioned SGW address

Compared to SGW, SSE nodes will always have high priority. If there are multiple SGW nodes, try one after the other.

Allowed values: String

Default: Empty

<Survivability_Proxy_Fallback_Intvl_n_>30</Survivability_Proxy_Fallback_Intvl_n_>

- In the phone web interface, specify the time interval in seconds.

Default: 30 seconds

Select Voice > System .

In the System Configuration section, set up Survivability Test Mode field as described in the following table:

<Survivability_Test_Mode>No</Survivability_Test_Mode>

- In the phone web interface, select the test mode.

Options: Yes|No

Default: No

Click Submit All Changes .

## Disable speakerphone

You can disable the speakerphone functionality and prevent the user from re-enabling the
        speakerphone. However, disabling speakerphone functionality will not affect the handset or
        headset. Users can change the audio path to headset or handset to use lines, speed dials,
        and softkeys for calling features.

Access the phone web page.

Select Voice > System .

In the System Configuration section, set the Disable
            Speakerphone parameter to Yes .

You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format:

```
<Disable_Speakerphone ua="na" um="y">Yes</Disable_Speakerphone>
```

Options: Yes and No

Default: No

Click Submit All Changes .

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext(n) , where (n) is the number of an extension to share. |
| 3 | In the General section, set the Line Enable parameter as described in the following table of Parameters for shared lines . |
| 4 | In the Share Line Appearance section, set Share Ext , Shared User ID field and Subscription Expires parameters as described in the following table of Parameters for shared lines . |
| 5 | In the Proxy and Registration section, enter the IP address of the proxy server in the Proxy field. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Proxy_1_ ua="na">as1bsoft.sipurash.com</Proxy_1_> Example for proxy server address: as1bsoft.sipurash.com |
| 6 | In the Subscriber Information section, enter the Display Name and User ID (extension number) for the shared extension. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Display_Name_1_ ua="na">name</Display_Name_1_>
<User_ID_1_ ua="na">4085273251</User_ID_1_> |
| 7 | In the Miscellaneous Line Key Settings section, set SCA Barge-In Enable parameter as described in the following table of Miscellaneous line key settings . |
| 8 | Click Submit All Changes. |

| Parameter | Description |
|---|---|
| Line Enable | Enables a line for the service. Perform one of the following: In the phone web interface, select yes to enable. Otherwise, select No . In the phone configuration file with XML(cfg.xml), enter a string in this format: <Line_Enable_1_ ua="na">Yes</Line_Enable_1_> Valid values: Yes\|No Default: Yes |
| Share Ext | Indicates whether other Cisco IP phones share this extension is, or the extension is private. Perform one of the following: In the phone web interface, select yes to enable. Otherwise, select No . In the phone configuration file with XML(cfg.xml), enter a string in this format: <Share_Ext_1_ ua="na">No</Share_Ext_1_> If you set Share Ext to No , this extension is private and doesn't share calls, regardless of the Share Line Appearance setting. If you set this extension to Yes , calls follow the Share Line Appearance setting. Valid values: Yes\|No Default: Yes |
| Shared User ID | The user identified assigned to the shared line appearance. Perform one of the following: In the phone web interface, enter the user ID. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Shared_User_ID_1_ ua="na">Shared UserID</Shared_User_ID_1> |
| Subscription Expires | Number of seconds before the SIP subscription expires. Before the subscription expiration, the phone gets NOTIFY messages from the SIP server on the status of the shared phone extension. Perform one of the following: In the phone web interface, enter the value in seconds. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Subscription_Expires_1_ ua="na">3600</Subscription_Expires_1_> Valid values: An integer from 10 through 65535 Default: 3600 seconds |

| Parameter | Description |
|---|---|
| SCA Barge-In Enable | Enables the SCA Barge-In. Perform one of the following: In the phone web interface, select Yes to enable. Otherwise, select No . In the phone configuration file with XML(cfg.xml), enter a string in this format: <SCA_Barge-In-Enable ua="na">No</SCA_Barge-In-Enable> Valid values: Yes\|No Default: No |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Supplementary Services section, set Call Park Serv to Yes to enable the feature on the phone. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Call_Park_Serv ua="na">Yes</Call_Park_Serv> Options: Yes and No Default: Yes |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Regional . |
| 3 | Enter *68 in the Call
				Park Code field. You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format: <Call_Park_Code ua="na">*68</Call_Park_Code> |
| 4 | Enter *88 in the Call
				Unpark Code field. You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format: <Call_Unpark_Code ua="na">*88</Call_Unpark_Code> |
| 5 | Click Submit
				All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Att Console > General . |
| 3 | Select No for the parameter BLF Callpark On Line Key Enable to disable the Busy Lamp Field (BLF) Call Park feature on the phone. |
| 4 | Select Voice > Phone . |
| 5 | Select a line key. |
| 6 | (Optional) Set the Extension parameter to Disabled . If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step. You can also configure the parameter in the configuration file (cfg.xml). The parameter is line-specific. Enter a string in the following format: <Extension_2_ ua="na">Disabled</Extension_2_> |
| 7 | In the Extended Function parameter, enter a string in this format: For a private line, enter fnc=prk;sub=$USER@$PROXY;nme=callpark;vid=1; For a shared line, enter fnc=prk;sub=$USER@$PROXY;nme=callpark;orbit=<DN of shared line>;vid=1; Where, fnc=prk means function=call park sub is the SIP URI of the monitored park slot. nme is the name displayed on the phone for the call park line key. orbit is the DN of the shared line. vid is the extension ID. The values of $USER and $PROXY are retrieved from the specified extension. If vid is missing in the function string, the values of $USER and $PROXY are retrieved from extension 1. You can also configure the line-specific parameter in the configuration file (cfg.xml). Enter a string in the following format: <Extended_Function_2_ ua="na">fnc=prk;sub=$USER@$PROXY;nme=callpark;vid=1;</Extended_Function_2_> |
| 8 | Click Submit
				All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Go to Voice > Att Console . |
| 3 | In the BLF List URI field, enter uri_name@server . The BLF List URI field must have the same value as that configured for the List URI:sip parameter on the BroadSoft server. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <BLF_List_URI ua="na">uri_name@server</BLF_List_URI> |
| 4 | From the BLF List Feature Options drop down list, select prk . You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <BLF_List_Feature_Options ua="na">prk</BLF_List_Feature_Options> The allowed values are blf+sd+cp\|prk. The default value is blf+sd+cp. When the BLF List Feature Options field is set to blf+sd+cp , the auto-assigned keys can be used for blf+sd+cp function or a call park function. If type="park" is included in the resource element, then the auto-assigned keys are used for call park function, else it is used for blf+sd+cp function when the type is not included. In the server, there are three resource elements in NOTIFY requests. Enter the strings in the resource elements in the format and add new attribute type="park" in the call park extension resource URI: <resource uri="sip:test01@as1bsoft.sipurash.com"><name>test 01</name><instance id="cROdMctbQE" state="active" cid="BQQ7uR@broadworks"/></resource> <resource uri="sip:2345@as1bsoft.sipurash.com" type="park"><name>Park Location1</name><instance id="cROdMctbQE" state="active" cid="BQQ8uR@broadworks"/></resource> <resource uri="sip:test02@as1bsoft.sipurash.com"><name>test 02</name><instance id="cROdMctbQE" state="active" cid="BQQ9uR@broadworks"/></resource> After successful configuration, the phone monitors test 01, Park Location1, and test 02. If call park extensions and users are subscribed successfully, linekeys will be assigned for callpark or blf function respectively, and get the monitored extension and user status. When the BLF List Feature Options field is set to prk , the BLF List URI monitors call park extensions and users. In the server, there are three resource elements in NOTIFY requests. Enter the strings in the resource elements in the format and add new attribute type="park" in the call park extension resource URI: <resource uri="sip:test01@as1bsoft.sipurash.com"><name>test 01</name><instance id="cROdMctbQE" state="active" cid="BQQ7uR@broadworks"/></resource> <resource uri="sip:2345@as1bsoft.sipurash.com" type="park"><name>Park Location1</name><instance id="cROdMctbQE" state="active" cid="BQQ8uR@broadworks"/></resource> <resource uri="sip:test02@as1bsoft.sipurash.com"><name>test 02</name><instance id="cROdMctbQE" state="active" cid="BQQ9uR@broadworks"/></resource> After successful configuration, the phone monitors test 01, Park Location1, and test 02. If call park extensions and users are subscribed successfully, linekeys will be assigned for call park function and get the monitored extension and user status. |
| 5 | Click Submit All Changes . |

| 1 | Select Voice > Att Console > General . |
|---|---|
| 2 | Select Yes for the parameter BLF Callpark On Line Key Enable . To disable the feature, select No . You can also configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <BLF_Callpark_On_Line_Key_Enable ua=”na“>Yes</BLF_Callpark_On_Line_Key_Enable> Default: No . |
| 3 | Navigate to Voice > Phone and select a line key. |
| 4 | (Optional) Set the Extension parameter to Disabled . If the Direct PLK Configuration feature is enabled, you don't need to disable the extension manually, skip the step. You can also configure the parameter in the configuration file (cfg.xml). The parameter is line-specific. Enter a string in the following format: <Extension_2_ ua="na">Disabled</Extension_2_> |
| 5 | Enter the string in the following format in the Extended Function field: fnc=prk;sub=BLF_URI;usr=$USER@$PROXY;
or
fnc=prk;sub=BLF_URI;ext=$USER@$PROXY; Where, fnc=prk means feature is call park sub— the URI to which the SUBSCRIBE message is sent. This name must be identical to the name defined in the BLF List URI. usr— the call park extension that the BLF monitors. |
| 6 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext(n) , where (n) is the number of an extension to share. |
| 3 | In the Call Feature Settings section, set Call Park Monitor Enable to Yes or No to show or hide the call parked status from the phone home screen. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Call_Park_Monitor_Enable_1_ ua="na">Yes</Call_Park_Monitor_Enable_1_> Options: Yes and No Default: No |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext n , where n is the phone extension number (1-10) of the phone web dialog. |
| 3 | In the Dial Plan section, set the Emergency Number parameter |
| 4 | In the E911 Geolocation Configuration section, set the following parameters as described in Parameters for emergency calls : E911 Enable Location Source Company UUID Primary Request URL Secondary Request URL |
| 5 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Section: Dial Plan |
| Emergency Number | Enter a comma-separated list of emergency numbers. To specify multiple emergency numbers, separate each emergency number with a comma. When one of these numbers is dialed, the unit disables processing of CONF, HOLD, and other similar softkeys or buttons to avoid accidentally putting the current call on hold. The phone also disables hook flash event handling. Only the far end can terminate an emergency call. The phone is restored to normalcy after the call is terminated and the receiver is back on-hook. Perform one of the following: to the digits that correspond to the customer emergency service numbers. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Emergency_Number_1_ ua="na"/> In the phone web page, set Emergency Number parameter to the digits that correspond to the customer emergency service numbers. Valid Values: Maximum number length is 63 characters Default: Blank (no emergency number) |
| Section: E911 Geolocation Configuration |
| E911 Enable | Enables or disables the E911 geolocation feature. If set to Yes, the phone will insert geolocation information into the SIP INVITE when placing an emergency call. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <E911_Enable_1_ ua="na" um="y">Yes</E911_Enable_1_> In the phone web page, select Yes to enable this feature or select No to disable it. Options: Yes and No Default: Yes |
| Location Source | Specifies the protocol used to obtain the phone's location information. The supported protocols are: HTTP Enabled Location Delivery (HELD): It contains the device location information in Location URI. If the phone is registered to Webex Calling or BroadWorks, select this option. Link Layer Discovery Protocol-Media Endpoint Discovery (LLDP-MED): It contains the location TLVs that provide the civic location information. The civic location formation contains details about a physical address. If the phone is registered to the call controllers that support LLDP MED TLV Location Identification Support, select this option. Currently, the feature isn't supported on Webex Calling and BroadWorks. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Location_Source_1_ ua="na" um="y">LLDP-MED</Location_Source_1_> Options: HELD and LLDP-MED Default: HELD |
| Company UUID | The Universally Unique Identifier (UUID) assigned to the customer by the emergency call services provider. For example: 07072db6-2dd5-4aa1-b2ff-6d588822dd46 Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Company_UUID_1_ ua="na"/> In the phone web page, enter a valid identifier assigned by the call services provider. Valid Values: Maximum identifier length is 128 characters. Default: Blank |
| Primary Request URL | Encrypted HTTPS phone location request. The request uses the phone IP addresses, MAC address, Network Access Identifier (NAI), and chassis ID and port ID assigned by the network switch manufacturer. The request also includes the location server name and the customer identifier. The server used by the emergency call services provider responds with an Emergency Response Location (ERL) that has a location Uniform Resource Identifier (URI) tied to the user phone IP address. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Primary_Request_URL_1_ ua="na"/> In the phone web page, enter encrypted HTTPS phone location request. For example: https://prod.blueearth.com/e911Locate/held/held_request.action Default: Blank |
| Secondary Request URL | Encrypted HTTPS request sent to the emergency call services provider's backup server to obtain the user's phone location. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Secondary_Request_URL_1_ ua="na"/> In the phone web page, enter the encrypted for the backup server that can return location information. For example: https://prod2.blueearth.com/e911Locate/held/held_request.action Default: Blank |

| 1 | Access the phone web page. |
|---|---|
| 2 | Select Voice > User . The user can select User Login > Voice User . |
| 3 | In the Supplementary Services section, set the Missed Call Led Alert parameter to Enabled . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Missed_Call_Led_Alert ua="rw">Enabled</Missed_Call_Led_Alert> Options: Enabled and Disabled Default: Disabled |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Supplementary Services area, set DND Serv to Yes to enable DND for the phone. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <DND_Serv ua="rw">Yes</DND_Serv> Options: Yes and No Default: No |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > User . |
| 3 | In the Supplementary Services area, set DND Setting to Yes or No to turn on or off DND. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <DND_Setting ua="rw">Yes</DND_Setting> Options: Yes and No Default: No |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Under Supplementary Services , configure the parameters as described in the following table of Parameters for enabling Call Forward . |
| 4 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Cfwd All Serv | Forwards all calls. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_All_Serv ua="na">Yes</Cfwd_All_Serv> In the phone web page, select Yes to forward all calls. Select No to disable it. Options: Yes and No Default: Yes |
| Cfwd Busy Serv | Forwards calls only if the line is busy. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_Busy_Serv ua="na">Yes</Cfwd_Busy_Serv> In the phone web page, select Yes to forward calls when the line is busy. Select No to disable it. Options: Yes and No Default: Yes |
| Cfwd No Ans Serv | Forwards calls only if the line is not answered. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_No_Ans_Serv ua="na">Yes</Cfwd_No_Ans_Serv> In the phone web page, select Yes to forward calls if the line is not answered. Select No to disable it. Options: Yes and No Default: Yes |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > User . |
| 3 | In the Call Forward section, configure the parameters as described in the following table of Call Forward Parameters on User tab . |
| 4 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Cfwd All | Forwards all calls. The setting of this parameter takes precedence over Cfwd Busy and Cfwd No Answer. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_All ua="rw">No</Cfwd_All> In the phone web page, select Yes to forward all calls. Select No to disable it. Options: Yes and No Default: No |
| Cfwd All Dest | Specifies the destination to which all calls are forwarded. The destination can be an alphanumeric input, a phone number, or a SIP URI. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_All_Dest ua="rw"> DestinationNumber </Cfwd_All_Dest> In the phone web page, enter the destination number in the field. When you select Yes for Cfwd All , make sure to configure the parameter. Default: Empty |
| Cfwd Busy | Forwards calls only if the line is busy. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_Busy ua="rw">No</Cfwd_Busy> In the phone web page, select Yes to forward calls when the line is busy. Select No to disable it. Options: Yes and No Default: No |
| Cfwd Busy Dest | Specifies the destination to which calls are forwarded if the line is busy. The destination can be an alphanumeric input, a phone number, or a SIP URI. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_Busy_Dest ua="rw"> DestinationNumber </Cfwd_Busy_Dest> In the phone web page, enter the destination number in the field. When you select Yes for Cfwd Busy, make sure to configure the parameter. Default: Empty |
| Cfwd No Answer | Forwards the incoming call only if the call isn’t answered. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_No_Answer ua="rw">No</Cfwd_No_Answer> In the phone web page, select Yes to forward the incoming call if the call isn't answered. Select No to disable it. Options: Yes and No Default: No |
| Cfwd No Ans Dest | Specifies the phone number of destination to which the incoming call is forwarded if the call isn’t answered. The destination can be an alphanumeric input, a phone number, or a SIP URI. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_No_Answer_Dest ua="rw"> Destination_Number </Cfwd_No_Answer_Dest> In the phone web page, enter the destination number in the field. When you select Yes for Cfwd No Answer, make sure to configure the parameter. Default: Empty |
| Cfwd No Ans Delay | Assigns a response delay time (in seconds) for the no answer scenario. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Cfwd_No_Answer_Delay ua="rw"> DelayTime </Cfwd_No_Answer_Delay> In the phone web page, enter the delay time in the field. Default: 20 |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Under Supplementary Services , configure the parameters as defined  in the following table of Parameters for enabling call transfer . |
| 4 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Attn Transfer Serv | Attended call transfer service. The user answers the call before transferring it. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Attn_Transfer_Serv ua="na">Yes</Attn_Transfer_Serv> In the phone web page, select Yes to enable the transfer service. Select No to disable it. Options: Yes and No Default: Yes |
| Blind Transfer Serv | Blind call transfer service. The user transfers the call without speaking to the caller. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Blind_Transfer_Serv ua="na">Yes</Blind_Transfer_Serv> In the phone web page, select Yes to enable the transfer service. Select No to disable it. Options: Yes and No Default: Yes |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Call Log section, choose the line in the CallLog Associated Line list and select the desired option in the Display Recents From field. Options: Phone\|XSI Server\|Webex Default value of Display Recents From : Phone You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format: <CallLog_Associated_Line ua="na">1</CallLog_Associated_Line> <Display_Recents_From ua="na”>Webex</Display_Recents_From> To display only XSI call logs on the associated line, enter a string in this
            format: <Display_Recents_From ua="na”>XSI Server</Display_Recents_From> The Recents screen on the phone displays only XSI call logs when
            the associated line is selected. |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Webex section, set the Directory Enable to Yes . You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Webex_Directory_Enable ua="na”>Yes</Webex_Directory_Enable> Default value: No |
| 4 | In the Directory Name field, enter a name for the Webex directory. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Webex_Directory_Name ua="na”>wcdir</Webex_Directory_Name> Default value: Empty The name you enter (for example, wcdir ), displays as the Webex directory name on the phone under the directory list. You can modify this name from the phone administration web page or from the configuration XML file string. When the Directory Name field is empty, by default, the Webex directory name on the phone appears as Webex directory . |
| 5 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Regional . |
| 3 | In the Vertical Service Activation Codes section, assign the codes to services as described in the following table of Vertical service activation codes . |

| Parameter | Description |
|---|---|
| Call Return Code | This code calls the last caller. Defaults to *69. |
| Blind Transfer Code | Begins a blind transfer of the current call to the extension specified after the activation code. Defaults to *95. |
| Cfwd All Act Code | Forwards all calls to the extension specified after the activation code. Defaults to *72. |
| Cfwd All Deact Code | Cancels call forward of all calls. Defaults to *73. |
| Cfwd Busy Act Code | Forwards busy calls to the extension specified after the activation code. Defaults to *90. |
| Cfwd Busy Deact Code | Cancels call forward of busy calls. Defaults to *91. |
| Cfwd No Ans Act Code | Forwards no-answer calls to the extension specified after the activation code. Defaults to *92. |
| Cfwd No Ans Deact Code | Cancels call forward of no-answer calls. Defaults to *93. |
| CW Act Code | Enables call waiting on all calls. Defaults to *56. |
| CW Deact Code | Disables call waiting on all calls. Defaults to *57. |
| CW Per Call Act Code | Enables call waiting for the next call. Defaults to *71. |
| CW Per Call Deact Code | Disables call waiting for the next call. Defaults to *70. |
| Block CID Act Code | Blocks caller ID on all outbound calls. Defaults to *61. |
| Block CID Deact Code | Removes caller ID blocking on all outbound calls. Defaults to *62. |
| Block CID Per Call Act Code | Removes caller ID blocking on the next inbound call. Defaults to *81. |
| Block CID Per Call Deact Code | Removes caller ID blocking on the next inbound call. Defaults to *82. |
| Block ANC Act Code | Blocks all anonymous calls. Defaults to *77. |
| Block ANC Deact Code | Removes blocking of all anonymous calls. Defaults to *87. |
| DND Act Code | Enables the do not disturb feature. Defaults to *78. |
| DND Deact Code | Disables the do not disturb feature. Defaults to *79. |
| Secure All Call Act Code | Makes all outbound calls secure. Defaults to *16. |
| Secure No Call Act Code | Makes all outbound calls not secure. Defaults to *17. |
| Secure One Call Act Code | Makes a secure call. Default: *18. |
| Secure One Call Deact Code | Disables secure call feature. Default: *19. |
| Call Park Code | The star code used for parking the current call. Defaults to *68. |
| Call Pickup Code | The star code used for picking up a ringing call. Defaults to *97. |
| Call Unpark Code | The star code used for picking up a call from the call park. Defaults to *88. |
| Group Call Pickup Code | The star code used for picking up a group call. Defaults to *98. |
| Referral Services Codes | These codes tell the IP phone what to do when the user places the current call on hold and is listening to the second dial tone. One or more *code can be configured into this parameter, such as *98, or *97\|*98\|*123, and so on. Max total length is 79 chars. This parameter applies when the user places the current call on hold (by Hook Flash) and is listening to second dial tone. Each *code (and the following valid target number according to current dial plan) entered on the second dial-tone triggers the phone to perform a blind transfer to a target number that is prepended by the service *code. For example, after the user dials *98, the IP phone plays a special dial tone called the Prompt Tone while waiting for the user the enter a target number (which is checked according to dial plan as in normal dialing). When a complete number is entered, the phone sends a blind REFER to the holding party with the Refer-To target equals to *98<target_number>. This feature allows the phone to hand off a call to an application server to perform further processing, such as call park. The *codes should not conflict with any of the other vertical service codes internally processed by the IP phone. You can empty the corresponding *code that you do not want to the phone to process. |
| Feature Dial Services Codes | These codes tell the phone what to do when the user is listening to the first or second dial tone. One or more *code can be configured into this parameter, such as *72, or *72\|*74\|*67\|*82, and so forth. The maximum total length is 79 characters. This parameter applies when the user has a dial tone (first or second dial tone). Enter *code (and the following target number according to current dial plan) entered at the dial tone triggers the phone to call the target number prepended by the *code. For example, after user dials *72, the phone plays a prompt tone awaiting the user to enter a valid target number. When a complete number is entered, the phone sends a INVITE to *72<target_number> as in a normal call. This feature allows the proxy to process features like call forward (*72) or BLock Caller ID (*67). The *codes should not conflict with any of the other vertical service codes internally processed by the phone. You can empty the corresponding *code that you do not want to the phone to process. You can add a parameter to each *code in Features Dial Services Codes to indicate what tone to play after the *code is entered, such as *72‘c‘\|*67‘p‘. Below are a list of allowed tone parameters (note the use of back quotes surrounding the parameter without spaces) • c = Cfwd Dial Tone • d = Dial Tone • m = MWI Dial Tone • o = Outside Dial Tone • p = Prompt Dial Tone • s = Second Dial Tone • x = No tones are place, x is any digit not used above If no tone parameter is specified, the phone plays Prompt tone by default. If the *code is not to be followed by a phone number, such as *73 to cancel call forward, do not include it in this parameter. In that case, simple add that *code in the dial plan and the phone sends INVITE *73@..... as usual when user dials *73. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | Under Supplementary Services , choose Yes for the Conference Serv parameter. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Conference_Serv ua="na">Yes</Conference_Serv> Options: Yes and No Default: Yes |
| 4 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Phone . |
| 3 | In the Help Desk section, choose Yes for the Help Desk Enable parameter. |
| 4 | (Optional) Set the parameter Custom Menu Name to customize the help desk display name on the phone screen. If it's empty, the display name is "Help Desk". |
| 5 | Enter the quick number and relevant name in Quick Number <n> and Name <n> respectively, where <n> represents the sequence number of the number. The maximum number of the quick numbers is 10. If the name is empty and only the quick number is configured, the phone will repeatedly display the quick number as the name. You can also configure the parameters in the phone configuration file with XML(cfg.xml) code: |
| 6 | Click Submit All Changes . |

| 1 | Select Voice > Phone . |
|---|---|
| 2 | In the Miscellaneous Line Key Settings section, for the Call Appearances Per Line parameter, specify the number of calls per line to allow. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Call_Appearances_Per_Line ua="na">2</Call_Appearances_Per_Line> The allowed values range from 2 to 10. The default value is 2. |
| 3 | Click Submit All Changes . |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext(n) , where n is an
          extension number. You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format: <Enable_URI_Dialing_1_ ua="na">Yes</Enable_URI_Dialing_1_> |
| 3 | Select Voice > Phone , you can add a
          string on a line key in this format to enable speed dial with alphanumeric dialing
          capability: fnc=sd;ext=xxxx.yyyy@$PROXY;nme=yyyy,xxxx For example: fnc=sd;ext=first.last@$PROXY;nme=Last,First The above example will enable the user to dial "first.last" to make a call. The supported characters that you can use for alphanumeric dialing are a-z, A-Z, 0-9,
              -, _, ., and +. Phone also supports plus dialing in which you dial E.164 numbers prefixed with a plus
              (+) sign. To dial the + sign, the user needs to press and hold the star (*) key for at
              least 1 second. This applies to dialing the first digit for an on-hook (including edit
              mode) or off-hook call. |

| Digit Sequence | Function |
|---|---|
| 0 1 2 3 4 5 6 7 8 9 0 * # | Characters that represent a key that the user must press on the phone keypad. |
| x | Any character on the phone keypad. |
| [sequence] | Characters within square brackets create a list of accepted key presses. The user
                  can press any one of the keys in the list. A numeric range, for example, [2-9] allows a user to press any
                  one digit from 2 through 9 . A numeric range can include other characters. For example, [35-8*] allows a user to press 3, 5, 6, 7, 8, or *. |
| .  (period) | A period indicates element repetition. The dial plan accepts 0 or more entries of the digit. For example, 01 . allows users to
                  enter 0, 01, 011, 0111, and so forth. |
| <dialed:substituted> | When the user presses 8 followed by a seven-digit number, the system
                  automatically replaces the dialed 8 with the sequence 1650 . If the user dials 85550112 , the system transmits 16505550112 . If the dialed parameter is empty and there is a value in the substituted field, no digits are replaced and the substituted value is
                  always prepended to the transmitted string. For example: <:1>xxxxxxxxxx When the user dials 9725550112 , the number 1 is added at the beginning of
                  the sequence; the system transmits 19725550112 . |
| ,  (comma) | 9, 1xxxxxxxxxx An outside line dial tone plays after the user presses 9 . The
                  tone continues until the user presses 1 . |
| !  (exclamation point) | 1900xxxxxxx! Rejects any 11-digit sequence that begins with 1900. |
| *xx | Allows a user to enter a 2-digit star code. |
| S0 or L0 | For Interdigit Timer Master Override, enter S0 to reduce
                  the short interdigit timer to 0 seconds, or enter L0 to
                  reduce the long interdigit timer to 0 seconds. |
| P | To pause, enter P , the number of seconds to pause, and a space.
                  This feature is typically used for implementation of a hotline and warm line, with
                  a 0 delay for the hot line, and a nonzero delay for a warm line. For example: P5 A pause of 5 seconds is introduced. |

| Terminating Event | Processing |
|---|---|
| Dialed digits have not matched any sequence in the dial plan. | The number is rejected. |
| Dialed digits exactly match one sequence in the dial plan. | If the dial plan allows the sequence, the number is accepted and is transmitted
                  according to the dial plan. If the dial plan blocks the sequence, the number is rejected. |
| A timeout occurs. | The number is rejected if the dialed
                  digits are not matched to a digit sequence in the dial plan within the time that
                  the applicable interdigit timer specifies. The Interdigit Long Timer applies when
                  the dialed digits do not match any digit sequence in the dial plan. Default: 10 seconds. The Interdigit Short Timer applies
                  when the dialed digits match one or more candidate sequences in the dial plan.
                  Default: 3 seconds. |
| A user presses the # key or the dial softkey on the IP phone screen. | If the sequence is complete and is
                  allowed by the dial plan, the number is accepted and is transmitted according to
                  the dial plan. If the sequence is incomplete or is
                  blocked by the dial plan, the number is rejected. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext(n) , where n is an
          extension number. |
| 3 | Scroll to the Dial Plan section. |
| 4 | Enter the digit sequences in the Dial Plan field. The default (US-based) systemwide dial plan appears in the field by default. |
| 5 | Modify the digit sequences. You can delete digit sequences, add digit sequences, or
          replace the entire dial plan with a new dial plan. Separate each digit sequence with a pipe character, and enclose the entire set of digit
            sequences within parentheses. Example: (9,8<:1408>[2-9]xxxxxx \| 9,8,1[2-9]xxxxxxxxx \| 9,8,011xx. \| 9,8,xx.\|[1-8]xx) |
| 6 | Click Submit All Changes . The phone reboots. |
| 7 | Verify that you can successfully complete a call with each digit sequence that you
          entered in the dial plan. If you hear a reorder (fast busy) tone, review your entries
            and modify the dial plan appropriately. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext (n) . |
| 3 | In the Proxy and Registration section, set up Survivability Proxy and Survivability Proxy Fallback Intvl fields as described in the following table: Parameter Description Survivability Proxy The parameter can be configured with an extension that includes a statically-configured SRV record. This allows phone to perform a failover to a survivability gateway. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_n_>hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]]</Survivability_Proxy_n_> In the phone web interface, enter the proxy server address as follows: hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]] Where: ip-list: ip-addr[,ip-addr[,ip-addr…]] Default: port=0 Example: wxclsg.example.com:8933:A=192.169.10.1 where, wxclsg.example.com=Provisioned SGW hostname. It is used for TLS certificate validation when connecting to SGW nodes. 8933=SGW port 192.169.10.1=Provisioned SGW address Compared to SGW, SSE nodes will always have high priority. If there are multiple SGW nodes, try one after the other. Allowed values: String Default: Empty Survivability Proxy Fallback Intvl The interval in seconds after which the phone will attempt to fallback to the SSE nodes. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_Fallback_Intvl_n_>30</Survivability_Proxy_Fallback_Intvl_n_> In the phone web interface, specify the time interval in seconds. Default: 30 seconds | Parameter | Description | Survivability Proxy | The parameter can be configured with an extension that includes a statically-configured SRV record. This allows phone to perform a failover to a survivability gateway. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_n_>hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]]</Survivability_Proxy_n_> In the phone web interface, enter the proxy server address as follows: hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]] Where: ip-list: ip-addr[,ip-addr[,ip-addr…]] Default: port=0 Example: wxclsg.example.com:8933:A=192.169.10.1 where, wxclsg.example.com=Provisioned SGW hostname. It is used for TLS certificate validation when connecting to SGW nodes. 8933=SGW port 192.169.10.1=Provisioned SGW address Compared to SGW, SSE nodes will always have high priority. If there are multiple SGW nodes, try one after the other. Allowed values: String Default: Empty | Survivability Proxy Fallback Intvl | The interval in seconds after which the phone will attempt to fallback to the SSE nodes. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_Fallback_Intvl_n_>30</Survivability_Proxy_Fallback_Intvl_n_> In the phone web interface, specify the time interval in seconds. Default: 30 seconds |
| Parameter | Description |
| Survivability Proxy | The parameter can be configured with an extension that includes a statically-configured SRV record. This allows phone to perform a failover to a survivability gateway. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_n_>hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]]</Survivability_Proxy_n_> In the phone web interface, enter the proxy server address as follows: hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]] Where: ip-list: ip-addr[,ip-addr[,ip-addr…]] Default: port=0 Example: wxclsg.example.com:8933:A=192.169.10.1 where, wxclsg.example.com=Provisioned SGW hostname. It is used for TLS certificate validation when connecting to SGW nodes. 8933=SGW port 192.169.10.1=Provisioned SGW address Compared to SGW, SSE nodes will always have high priority. If there are multiple SGW nodes, try one after the other. Allowed values: String Default: Empty |
| Survivability Proxy Fallback Intvl | The interval in seconds after which the phone will attempt to fallback to the SSE nodes. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_Fallback_Intvl_n_>30</Survivability_Proxy_Fallback_Intvl_n_> In the phone web interface, specify the time interval in seconds. Default: 30 seconds |
| 4 | Select Voice > System . |
| 5 | In the System Configuration section, set up Survivability Test Mode field as described in the following table: Parameter Description Survivability Test Mode If set it to Yes, phone will always register to SGW nodes. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Test_Mode>No</Survivability_Test_Mode> In the phone web interface, select the test mode. Options: Yes\|No Default: No | Parameter | Description | Survivability Test Mode | If set it to Yes, phone will always register to SGW nodes. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Test_Mode>No</Survivability_Test_Mode> In the phone web interface, select the test mode. Options: Yes\|No Default: No |
| Parameter | Description |
| Survivability Test Mode | If set it to Yes, phone will always register to SGW nodes. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Test_Mode>No</Survivability_Test_Mode> In the phone web interface, select the test mode. Options: Yes\|No Default: No |
| 6 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Survivability Proxy | The parameter can be configured with an extension that includes a statically-configured SRV record. This allows phone to perform a failover to a survivability gateway. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_n_>hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]]</Survivability_Proxy_n_> In the phone web interface, enter the proxy server address as follows: hostname[:port][:A=ip-list] [\| hostname2[:port][:A=ip-list]] Where: ip-list: ip-addr[,ip-addr[,ip-addr…]] Default: port=0 Example: wxclsg.example.com:8933:A=192.169.10.1 where, wxclsg.example.com=Provisioned SGW hostname. It is used for TLS certificate validation when connecting to SGW nodes. 8933=SGW port 192.169.10.1=Provisioned SGW address Compared to SGW, SSE nodes will always have high priority. If there are multiple SGW nodes, try one after the other. Allowed values: String Default: Empty |
| Survivability Proxy Fallback Intvl | The interval in seconds after which the phone will attempt to fallback to the SSE nodes. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Proxy_Fallback_Intvl_n_>30</Survivability_Proxy_Fallback_Intvl_n_> In the phone web interface, specify the time interval in seconds. Default: 30 seconds |

| Parameter | Description |
|---|---|
| Survivability Test Mode | If set it to Yes, phone will always register to SGW nodes. In the phone configuration file with XML(cfg.xml), enter a string in this format: <Survivability_Test_Mode>No</Survivability_Test_Mode> In the phone web interface, select the test mode. Options: Yes\|No Default: No |

| 1 | Access the phone web page. |
|---|---|
| 2 | Select Voice > System . |
| 3 | In the System Configuration section, set the Disable
            Speakerphone parameter to Yes . You can configure this parameter in the phone configuration XML file (cfg.xml) by
            entering a string in this format: <Disable_Speakerphone ua="na" um="y">Yes</Disable_Speakerphone> Options: Yes and No Default: No |
| 4 | Click Submit All Changes . |