---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-english-adminguide-w88x-b-wireless-8821-8821ex-admin-guide-w88x--0dde724d24
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/english/adminguide/w88x_b_wireless-8821-8821ex-admin-guide/w88x_b_wireless-8821-8821ex-admin-guide_chapter_010.html
retrieved_at: 2026-08-21T01:56:18.134511+00:00
---

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

# Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

Updated: June 28, 2016

Chapter: Cisco Unified Communications Manager Phone Configuration

## Chapter: Cisco Unified Communications Manager Phone Configuration

# Cisco Unified Communications Manager Phone Configuration

## Determine the MAC Address of the Phone

To add phones to the Cisco Unified Communications Manager, you must determine the MAC address of the phone.

Perform one of the following actions:

- On the phone, access the Settings app, select Phone information > Model information , and look in the MAC address field.

- Remove the battery cover and battery from the phone, and look at the label.

- Display the phone web page and look at the MAC address in the Device information screen.

- If the phone has already been added to the Cisco Unified Communications Manager,  access the Cisco Unified Communications
                                          Manager Administration application, select Device > Phone , search for the phone, and access the Phone Configuration window.

## Before You Register Wireless Phones

Before you register wireless phones with your Cisco Unified Communications Manager, you can set up profiles, groups, and templates.
                              These can simplify the phone setup when you have common information for all phones or groups of phones.

Wi-Fi profiles—you can create a profile for the Wi-Fi network connections.

Wi-Fi profile groups—you can create a group of Wi-Fi profiles that the phones can use.

Custom SIP Profile—the phone needs a special SIP Profile, instead of the standard SIP profiles.

Phone button templates—you can assign lines and features in the Phones app. Use this if you have specific lines or features that you want all your users to access quickly. For example, you can
                                    set up a common speed dial number. Because the wireless phones have some special button requirements, Phone Button Templates will help you with this template.

Softkey templates—you can set up the list of features that users see when they press the More softkey. Because the wireless phones have fewer softkeys than desk phones, Phone Softkey Templates will help you with this template.

Common phone profile—you can set up a profile for the wireless phone with the phone button and softkey templates, and then
                                    use the profile for all your wireless phones.

You can find detailed instructions  about these profiles and templates in the System Configuration Guide for Cisco Unified Communications Manager .

### Set Up a Wi-Fi Profile using Cisco Unified Communications Manager

You can configure a Wi-Fi profile and then assign the profile to the phones that support Wi-Fi. The profile contains the parameters
                                 required for phones to connect to the Cisco Unified Communications Manager with Wi-Fi. When you create and use a Wi-Fi profile,
                                 you or your users do not need to configure the wireless network for individual phones.

Wi-Fi profiles are supported on Cisco Unified Communications Manager Release 10.5(2) or later. EAP-FAST, PEAP-GTC, and PEAP-MSCHAPv2
                                 are supported in Cisco Unified Communications Manager Release 10.0 and later. EAP-TLS is supported in Cisco Unified Communications
                                 Manager Release 11.0 and later.

A Wi-Fi profile enables you to prevent or limit changes to the Wi-Fi configuration on the phone by the user.

We recommend that you use a secure profile with TFTP encryption enabled to protect keys and passwords when you use a Wi-Fi
                                 profile.

When you set up the phones to use EAP-FAST, PEAP-MSCHAPv2, or PEAP-GTC authentication, your users need individual user ids
                                 and passwords to sign into the phone.

The phones support one server certificate per install method (manual, SCEP, or TFTP).

In the Cisco Unified Communications Administration, select Device > Device Settings > Wireless LAN Profile .

Click Add New .

In the Wireless LAN Profile Information section, set the  parameters:

Name —Enter a unique name for the Wi-Fi profile.  This name displays on the phone.

Description —Enter a description for the Wi-Fi profile to help you differentiate this profile from other Wi-Fi profiles.

Allowed —Indicates that the user can make changes to the Wi-Fi  settings from their phone. This option is selected by default.

Disallowed —Indicates that the user cannot make any changes to the Wi-Fi settings on their phone.

Restricted —Indicates that the user can change the Wi-Fi username and password on their phone. But users are not allowed to make changes
                                                            to other Wi-Fi settings on the phone.

In the Wireless Settings section, set the  parameters:

SSID (Network Name) —Enter the network name available in the user environment to which the phone can be connected. This name is displayed under
                                                   the available network list on the phone and the phone can connect to this wireless network.

Frequency Band —Available options are Auto, 2.4 GHz, and 5 GHz. This field determines the frequency band that the wireless connection uses.
                                                   If you select Auto, the phone  attempts to use the 5 GHz band first and only uses the 2.4 GHz band when the 5 GHz is not available.

In the Authentications Settings section, set the Authentication Method to one of these authentication methods: EAP-FAST, EAP-TLS,  PEAP-MSCHAPv2,  PEAP-GTC, PSK, WEP, and None.

After you set this field, you may see extra fields that you need to set.

User certificate —Required for EAP-TLS authentication. Select Manufacturing installed or User installed .  The phone requires a certificate to be installed, either automatically from the SCEP or manually from the administration
                                                   page on the phone.

PSK passphrase —Required for PSK authentication. Enter the 8- 63 character ASCII or 64 HEX character pass phrase.

WEP Key —Required for WEP authentication. Enter the 40/102 or 64/128 ASCII or HEX WEP key.

40/104 ASCII is 5 characters.

64/128 ASCII is 13 characters.

40/104 HEX is 10 characters.

64/128 HEX is 26 characters.

Provide Shared Credentials : Required for  EAP-FAST, PEAP-MSCHAPv2, and   PEAP-GTC authentication.

If the user manages the username and password, leave the Username and Password fields blank.

If all your users share the same username and password, you can input the information in the Username and Password fields.

Enter a description in the Password Description field.

If you need to assign each user a unique username and password, you need to create a profile for each user.

The Network Access Profile field is not supported by the Cisco IP Phone 8821.

Click Save .

#### What to do next

Apply the WLAN Profile Group to a device pool ( System > Device Pool ) or directly to the phone ( Device > Phone ).

### Set Up a Wi-Fi Group using Cisco Unified Communications Manager

You can create a wireless LAN profile group and add any wireless LAN profile to this group. The profile group can then be
                                 assigned to the phone when you set up the phone.

If your users require access to more than one profile, then a profile group can speed up phone configuration. Up to four profiles
                                 can be added to the profile group and you list the profiles in priority order.

In Cisco Unified Communications Administration, select Device > Device Settings > Wireless LAN Profile Group .

You can also define a wireless LAN profile group from System > Device Pool .

Click Add New .

In the Wireless LAN Profile Group Information section, enter a group name and description.

In the Profiles for this Wireless LAN Profile Group section, select an available profile from the Available Profiles list and move the selected profile to the Selected Profiles list.

Click Save .

### Set up a Wireless Phone SIP Profile

Cisco Unified Communication Manager has standard SIP profiles available. However, a custom SIP Profile for your wireless phones
                                 is the preferred profile.

In Cisco Unified Communications Manager Administration, select Device > Device Settings > SIP Profile .

Click Find .

Click the Copy icon beside Standard SIP Profile .

Set the name and description to Custom 8821 SIP Profile .

Set these parameters.

Timer Register Delta (seconds) —Set to 30 (default is 5).

Timer Keep Alive Expires (seconds) —Set to 300 (default is 120).

Timer Subscribe Expires (seconds) —Set to 300 (default is 120).

Timer Subscribe Delta (seconds) —Set to 15 (default is 5).

Click Save .

### Phone Button Templates

You can assign lines and features to the wireless phones with a phone button template. Ideally, you set up the templates before
                                 you register the phones on the network. In this way, you can use a  customized phone button template when you register the
                                 phone. But if you don't set up the template first, you can change the phones later.

The Cisco Wireless IP Phone can have up to six lines and up to 24 connected calls. The default button template uses position
                                 1 for lines and assigns positions 2 through 6 as speed dials. You can assign the following features to button positions:

Service URL

Privacy

Speed dial

Use softkey features in the More menu to access other phone features, such as call park, call forward, redial, hold, resume, and conferencing.

To modify a phone button template, choose Device > Device Settings > Phone Button Template from Cisco Unified Communications Manager Administration. To assign a phone button template to a phone, use the Phone Button
                                 Template field in the Cisco Unified Communications Manager Administration Phone Configuration page. For more information,
                                 see the System Configuration Guide for Cisco Unified Communications Manager .

### Phone Softkey Templates

You can change the order of softkeys for the wireless phone with Cisco Unified Communications Manager Administration. Unlike
                                 other phones that have buttons for some functions, the wireless phone has two nonconfigurable softkeys. One of the softkeys
                                 is usually the More softkey, and when you press More , you get a menu of appropriate actions.

When you configure a softkey template for the wireless phone, you configure the Cisco Unified Communications Manager softkeys
                                 and their sequence in the More menu only. The order of softkeys in the softkey template corresponds to the phone softkey list in the More menu. You can control the softkey display based on the call state.

You can copy the Standard User softkey template and set it up as your standard wireless phone softkey template. You can then copy your standard wireless
                                 phone softkey template if some of your users have specific requirements.

For example, if most of your users want the Hold softkey as the first entry in the More menu, and the rest of the users want Transfer in the first entry:

Set up your standard wireless softkey template with the Hold softkey as the first softkey when the phone is in the connected state.

Copy the standard wireless softkey template, give it a new name and set the first softkey to be Transfer when the phone is in the connected state.

When you set up your user and phones, you can assign the appropriate softkey template.

To ensure that users hear the voice-messaging greeting when they are transferred to the voice message system, you must set
                                 up a softkey template with Transfer as the first softkey for a connected call.

Softkey templates support up to 16 softkeys for applications.

For more information, see the System Configuration Guide for Cisco Unified Communications Manager .

### Bulk Deployment Utility

The Bulk Deployment Utility (BDU) for the Cisco Wireless IP Phone 8821 enables you to quickly provision and deploy wireless
                                 phones when unique 802.1x accounts are used with EAP-FAST, PEAP-GTC, or PEAP-MS-CHAPv2, or if a common set of credentials
                                 are used by all phones (for example, WPA2-PSK or a common 802.1x account). You can also use the BDU to support the phones
                                 after they are deployed. The BDU does not support certificate provisioning.

The BDU requires Firmware Release 11.0(3)SR4 or later on the phones.

This version of the BDU is not the same as the BDU for the Cisco Unified Wireless IP Phone 792x Series.

You download the BDU from this location:

https://software.cisco.com/download/type.html?mdfid=286308995&flowid=80142

For more information, see the Bulk Deployment Utility Guide for Cisco Wireless Phone 8821 and 8821-EX that is associated with the BDU software.

## Manual Phone Registration

When a new phone is added to your network, manual phone registration means that you need to configure the phone in your call
                              control system. The configuration includes the directory number, information about the user, and the phone profile.

After you configure the phone in the call control system, you configure the phone to connect to the call control system.

### Add a New Phone

Before the phone can be used, you add it to the Cisco Unified Communications Manager and assign it to a user.  If you do not
                                 set up Wi-Fi profile groups, you or your user need to set up the Wi-Fi network on the phone.

#### Before you begin

You need the following files installed on the Cisco Unified Communications Manager:

Latest phone firmware load

Latest Cisco Unified Communications Manager Device Pack to support the phone

You need the MAC address of the phone.

Your user must be configured in the system.

In Cisco Unified Communications Manager Administration, select Device > Phone .

Click Add New .

Select Cisco 8821 .

If Cisco 8821 does not appear, the Cisco Unified Communications Manager Device Pack to support  the phone is not installed on the server.

Click Next .

Set the phone information.

Required fields are marked with an asterisk (*), although most take the default settings. The fields that need specific entries
                                             are:

MAC address—Enter the MAC address of the phone. You can enter the address with lowercase letters.

Description—Set this field to something meaningful; for example, the user's name.

Device pool—Set this field for the appropriate pool of phones.

Phone Button Template—Select Standard 8821 SIP .

Owner User ID—Select the user's ID.

Device security profile—Select Cisco 8821 Standard SIP Non Secure Profile .

SIP profile—Select Custom 8821 SIP Profile . For more information, see Set up a Wireless Phone SIP Profile .

(Optional) In the Wireless LAN Profile Group field, select the wireless LAN profile group if the profile is not associated with a device pool. For more information, see Set Up a Wi-Fi Profile using Cisco Unified Communications Manager .

Click Save .

Click OK .

Click Apply config .

Click OK .

Click Line[1] — Add a new DN .

Enter a DN.

Click Save and then click Save again.

In the Related links field, select Configure Device and click Go .

Click Save and click OK .

Click Apply config and click OK .

#### What to do next

If you do not use a Wi-Fi profile group, then you need to configure the wireless network on the phone.

## Automatic Phone Registration

If your Cisco Unified Communications Manager is set up to automatically register new phones, you can get new phones working
                              quickly. You need to set up the phone to connect to your Cisco Unified Communications Manager. The new phones are assigned
                              DNs and profiles based on the phone type.

To support autoregistration, you need to set up profiles for the phone models or use the standard profiles.

For more information on autoregistration, see the Cisco Unified Communications Manager documentation.

## Phone Feature Configuration

You can set up phones to have a variety of features, based on the needs of your users. You can apply features to all phones,
                              a group of phones, or to individual phones.

When you set up features, the Cisco Unified
                                 				Communications Manager Administration window displays information that is applicable to all phones and information that is applicable to the phone model. The information
                              that is specific to the phone model is in the Product Specific Configuration Layout area of the window.

For information on the fields applicable to all phone models, see the Cisco Unified
                                 				Communications Manager documentation.

When you set a field, the window that you set the field in is important because there is a precedence to the windows. The
                              precedence order is:

Individual phones (highest precedence)

Group of phones

All phones (lowest precedence)

For example, if you don't want a specific set of users to access the phone Web pages, but the rest of your users can access
                              the pages, you:

Enable access to the phone web pages for all users.

Disable access to the phone web pages for each individual user, or set up a user group and disable access to the phone web
                                    pages for the group of users.

If a specific user in the user group did need access to the phone web pages, you could enable it for that particular user.

### Set Up Phone Features for All Phones

Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator.

Select System > Enterprise Phone Configuration .

Set the fields you want to change.

Check the Override Enterprise Settings check box for any changed fields.

Click Save .

Click Apply Config .

Restart the phones.

This will impact all phones in your organization.

### Set Up Phone Features for a Group of Phones

Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator.

Select Device > Device Settings > Common Phone Profile .

Locate the profile.

Navigate to the Product Specific Configuration Layout pane and set the fields.

Check the Override Enterprise Settings check box for any changed fields.

Click Save .

Click Apply Config .

Restart the phones.

### Set Up Phone Features for a Single Phone

Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator.

Select Device > Phone

Locate the phone associated with the user.

Navigate to the Product Specific Configuration Layout pane and set the fields.

Check the Override Common Settings check box for any changed fields.

Click Save .

Click Apply Config .

Restart the phone.

### Product Specific Configuration Fields

The following table describes the fields in the Product Specific Configuration Layout pane.

Field Name

Field Type

Or Choices

Default

Description

Battery Lifetime Alert

Disabled

Enabled

Disabled

Enables or disables Battery Lifetime alert, Phone SN alert, and Overvoltage alert.

Battery Lifetime Alert Interval

6 Months

12 Months

18 Months

24 Months

24 Months

Specifies the interval time over which the Battery Lifetime Alert is generated.

Battery SN Reminder

Disabled

Enabled

Disabled

Enables or disables Battery SN Reminder.

Disable Speakerphone

Checkbox

Unchecked

Turns off the speakerphone capability of the handset.

See Note 1.

Disable Speakerphone and Headset

Checkbox

Unchecked

Turns off the speakerphone and headset capability of the handset.

See Note 1.

Settings Access

Disabled

Enabled

Restricted

Enabled

Enables, disables, or restricts access to local
                                             					 configuration settings in the Settings app.

With restricted access, the Phone Settings, Bluetooth, and Phone Information menus can be accessed. Some settings in the Wi-Fi
                                             menu are also accessible.

With disabled access, the Settings menu does
                                             					 not display any options.

Web Access

Disabled

Enabled

Disabled

Enables or disables access to the phone web pages through a web browser.

If you enable this field, you may expose sensitive
                                                         information about the phone.

HTTPS Server

HTTP and HTTPS enabled

HTTPS only

HTTP and HTTPS enabled

Controls the type of communication to the phone. If you select HTTPS only, the phone communication is more secure.

Disable TLS 1.0 and TLS 1.1 for Web Access

Disabled

Enabled

Disabled

Controls the use of TLS 1.2 for a web server connection.

Disabled—A phone configured for TLS1.0, TLS 1.1, or TLS1.2 can function as an HTTPS server.

Enabled—Only a phone configured for TLS1.2 can function as an HTTPS server.

Web Admin

Disabled

Enabled

Disabled

Enables or disables administrator access to the phone web pages through a web browser

Admin Password

String of 8–127 characters

Defines the administrator password when you access the phone web pages as an administrator.

Bluetooth

Disabled

Enabled

Enabled

Enables or disables the Bluetooth option on the
                                             					 phone. If disabled, the user cannot enable Bluetooth on the phone.

Out-of-Range Alert

Disabled

Beep once

Beep every 10 seconds

Beep every 30 seconds

Beep every 60 seconds

Disabled

Controls the frequency of audible alerts when the phone is out of range of an AP. The phone does not play audible alerts when
                                             the parameter value is "disabled." The phone can beep one time or regularly at 10, 30, or 60 second intervals. When the phone
                                             is within range of an AP, the alert stops.

Scan Mode

Auto

Single AP

Continuous

Continuous

Controls the scanning by the phone.

Auto—Phone scans when it is in a call or when the received strength signal indicator (RSSI) is low.

Single AP—Phone never scans except when the basic service set (BSS) is lost.

Continuous—Phone scans continuously even when it is not in a call.

Application URL

String of up to 256 characters

Specifies the URL that the phone uses to contact application services, including Push To Talk.

Application Request Timer

5 seconds

20 seconds

5 seconds

Controls the length of the application request timer in seconds. Increase the length of the timer if you see "405" error messages in the log file.

Application Button Activation Timer

Disabled

1 second

2 seconds

3 seconds

4 seconds

5 seconds

Disabled

Specifies the amount of time that the user must hold the Application button to activate the Application URL.

Application Button Priority

Low

Medium

High

Low

Indicates the priority of the Application button relative to the other phone tasks.

Low—Specifies that the Application button works only when the phone is idle and on the main screen.

Medium—Specifies that the button takes precedence over all tasks except when the keypad is locked.

High—Specifies that the button takes precedence over all tasks on the phone.

When the priority is high, the keypad locked and the screen dark, pressing the application button turns on the phone screen.
                                                   The user presses the button a second time to perform the application button function.

Emergency Numbers

String of up to 16 characters, comma separated, no spaces

Sets the list of emergency numbers that the users see when they try to dial without signing in.

Example: 911,411

Dialing Mode

On-hook Dialing

Off-hook Dialing

On-hook Dialing

Sets the default dialing mode for the phones.

Power Off in Multicharger

Disabled

Enabled

Disabled

When disabled, the phone doesn't power off when placed in the multicharger. When enabled, the phone powers off when placed
                                             in the multicharger.

Background Image

String up to 64 characters

Sets the background image that all users see. If you set a background image, the user cannot change the phone to another image.

Home Screen

Application View

Line View

Application View

Sets the home screen to either the Application View or the Line View.

Set the phone to use Line View for users that use multiple lines, speed dials, or make many calls.

Left Softkey

None

Favorites

Local Contacts

Voicemail

Favorites

Controls the left-most softkey on the phone.

None: the softkey is blank

Favorites: the softkey displays Favorites .

Local Contacts: the softkey displays Local contacts .

Voicemail: the softkey displays Voicemail .

Voicemail Access

Disabled

Enabled

Enabled

Controls access to voicemail.

Applications Access

Disabled

Enabled

Enabled

Controls access to the Applications menu.

Recording Tone

Disabled

Enabled

Disabled

Controls the playing of the tone when a user is recording a call

Recording Tone Local Volume

Integer 0–100

100

Controls the volume of the recording tone to the local user.

Recording Tone Remote Volume

Integer 0–100

50

Controls the volume of the recording tone to the remote user.

Recording Tone Duration

Integer 1–3000 milliseconds

Controls the duration of the recording tone.

Remote Log

Disabled

Enabled

Disabled

Controls the ability to send logs to the syslog server.

Log Profile

Default

Preset

Telephony

Preset

Specifies the predefined logging profile.

Log Server

String of up to 256 characters

Identifies the IPv4 syslog server for phone debug output.

The format for the address is: address:<port>@@base=<0-7>;pfs=<0-1>

Cisco Discovery Protocol (CDP)

Disabled

Enabled

Enabled

Controls Cisco Discovery Protocol on
                                             					 the phone.

SSH Access

Disabled

Enabled

Disabled

Controls the  access to the SSH daemon through port 22. Leaving port 22 open leaves the phone vulnerable to Denial of Service
                                             (DoS) attacks.

Ring Locale

Default

Japan

Default

Controls the ringing pattern.

TLS Resumption Timer

Integer 0–3600 seconds

3600

Controls the ability to resume a TLS session without repeating the entire TLS authentication process. If the field is set
                                             to 0, then the TLS session resumption is disabled.

Record Call Log from Shared Line

Disabled

Enabled

Disabled

Specifies whether to record call log from a shared line.

Minimum Ring Volume

Silent

Volume level 1–15

Silent

Controls the minimum ring volume for the phone.

Load Server

String of up to 256 characters

Identifies the alternate IPv4 server that the phone uses
                                             					 to obtain firmware loads and upgrades.

WLAN SCEP Server

String of up to 256 characters

Specifies the SCEP Server that the phone uses to obtain certificates for WLAN authentication. Enter the hostname or the IP
                                             address (using standard IP addressing format) of the server.

WLAN Root CA Fingerprint (SHA256 or SHA1)

String of up to 95 characters

Specifies the SHA256 or SHA1 fingerprint of the Root CA to use for validation during the SCEP process when issuing certificates
                                             for WLAN authentication. We recommend that you use the SHA256 fingerprint, which can be obtained via OpenSSL (e.g. openssl
                                             x509 -in rootca.cer -noout -sha256 -fingerprint) or using a Web Browser to inspect the certificate details.

Enter the 64 hexadecimal character value for the SHA256 fingerprint or the 40 hexadecimal character value for the SHA1 fingerprint
                                             with a common separator (colon, dash, period, space) or without a separator. If using a separator, then the separator should
                                             be consistently placed after every 2, 4, 8, 16, or 32 hexadecimal characters for a SHA256 fingerprint or every 2, 4, or 8
                                             hexadecimal characters for a SHA1 fingerprint.

Console Access

Disabled

Enabled

Disabled

Specifies whether the serial console is enabled or disabled.

Gratuitous ARP

Disabled, Enabled

Disabled

Enables or disables the ability for the phone to
                                             					 learn MAC addresses from Gratuitous ARP. This capability is required to monitor
                                             					 or record voice streams.

Show All Calls on Primary Line

Disabled

Enabled

Disabled

Specifies is all calls presented to this phone will be shown on the primary line or not.

Advertise G.722 and iSAC Codecs

Use System Default

Disabled

Enabled

Use System Default

Indicates whether the phone advertises the G.722
                                             					 and iSAC codecs to the Cisco Unified Communications Manager.

Use System
                                                   						Default—Defers to the setting specified in the enterprise parameter Advertise
                                                   						G.722 Codec.

Disabled—Does not
                                                   						advertise G.722 to the Cisco Unified Communications Manager.

Enabled—Advertises G.722 to the Cisco Unified Communications Manager.

For more information, see Note 2.

Revert to All Calls

Disabled

Enabled

Disabled

Specifies whether the phone will revert to All Calls after any call ends or not if the call is on a filter other than Primary
                                             line, All Calls, or Alerting Calls.

DF bit

0

1

0

Controls how network packets are sent. Packets can be sent in chunks (fragments) of various sizes.

When the DF bit is set to 1 in the packet header, the network payload does not fragment when going through network devices,
                                             such as switches and routers. Removing fragmenting avoids incorrect parsing on the receiving side, but results in slightly
                                             slower speeds.

The DF bit setting does not apply to ICMP, VPN, VXC VPN, or DHCP traffic.

Lowest Alerting Line State Priority

Disabled

Enabled

Disabled

Specifies the alert state when using shared lines. When disabled and there is an incoming call alerting on the shared line,
                                             the LED/Line state icon reflects the alerting state instead of Remote-In-Use. When enabled, the user sees the Remote-In-Use
                                             icon when there is call alerting on the shared line.

Divert Alerting Call

Disabled

Enabled

Enabled

Controls the display of the Decline softkey.

Disabled: the Decline softkey doesn't display when there is an incoming call. The user can't divert or dismiss the incoming call.

Enabled: the Decline softkey displays when there is an incoming call. The user can decline the call.

Allow Vibrate URI When On Call

Disabled

Enabled

Disabled

Controls if the Vibrate URI command from an XSI message is allowed when the phone is active on a call.

Disabled: The handset won't vibrate.

Enabled: The handset will vibrate.

Customer support upload URL

String of up to 256 characters

Identifies the location that the phones use to upload problem reporting tool (PRT) output files.

If you change a user's audio path while they are in the Push to Talk session, the user needs to end the current session and
                                                   restart to get the correct audio path selection.

Codec negotiation involves
                                                   					 two steps:

The phone must advertise the supported codec to the Cisco
                                                         						  Unified Communications Manager (not all endpoints support the same set of
                                                         						  codecs).

When the Cisco Unified Communications Manager gets the
                                                         						  list of supported codecs from all phones involved in the call attempt, it
                                                         						  chooses a commonly supported codec based on various factors, including the
                                                         						  region pair setting.

### Set Up Services

You can provide your users with special phone services. These services are XML applications  that enable the display of interactive
                                 content with text and graphics on the phone. Examples of services include Push to Talk, directories, stock quotes, and weather
                                 reports. Some services, such as Push to Talk, can use the configurable Applications button that is located on the side of the phone.

Cisco does not provide any applications but you can create your own custom applications. For more information, see the Cisco Unified IP Phone Service Application Development Notes , located here: https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-programming-reference-guides-list.html .

Before a user can access any service, these important tasks must be completed:

You use Cisco Unified Communications Manager Administration to configure the available services.

You give information to your users about the services available. See Self Care Portal Overview for a summary of the information that you must provide to your users.

The user subscribes to services using the Self Care portal.

These references will help you understand services:

- "Configure Cisco Unified IP Phone Services" in the System Configuration Guide for Cisco Unified Communications Manager

- "Extension Mobility" in the Feature Configuration Guide for Cisco Unified Communications Manager

#### Before you begin

Gather the URLs for the sites you want to set up and verify that users can access those sites from your corporate IP telephony
                                 network.

In Cisco Unified Communications Manager Administration, choose Device > Device Settings > Phone Services .

Set up the services.

Verify that your users have access to the Self Care portal.

### Problem Report Tool

Users submit problem reports to you with the Problem Report Tool.

The Problem Report Tool logs are required by Cisco TAC when troubleshooting problems. The logs are cleared if you restart
                                             the phone. Collect the logs before you restart the phones.

To issue
                                 		  a problem report, users access the Problem Report Tool and
                                 		  provide the date and time that the problem occurred, and a description of the problem.

You must add a server address to the Customer Support Upload URL field on Cisco Unified Communications Manager.

#### Configure a Customer Support Upload URL

You must use a server with an upload script to receive PRT files. The PRT uses an HTTP POST mechanism, with the following
                                    parameters included in the upload (utilizing multipart MIME encoding):

devicename (example: "SEP001122334455" )

serialno (example: "FCH12345ABC" )

username (the username configured in Cisco Unified Communications Manager, the device owner)

prt_file (example: "probrep-20141021-162840.tar.gz" )

A sample script is
                                    		  shown below. This script is provided for reference only. Cisco does not provide
                                    		  support for the upload script installed on a customer's server.

```
<?php

// NOTE: you may need to edit your php.ini file to allow larger
// size file uploads to work.
// Modify the setting for upload_max_filesize
// I used:  upload_max_filesize = 20M

// Retrieve the name of the uploaded file 
$filename = basename($_FILES['prt_file']['name']);

// Get rid of quotes around the device name, serial number and username if they exist
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

if(!move_uploaded_file($_FILES['prt_file']['tmp_name'], $fullfilename)) {
        header("HTTP/1.0 500 Internal Server Error");
        die("Error: You must select a file to upload.");
}

?>
```

The phones only support HTTP URLs.

Set up a server that can run your PRT upload script.

Write a script that can handle the parameters listed above, or edit the provided sample script to suit your needs.

Upload your script to your server.

In Cisco Unified Communications Manager, go to the Product Specific
                                             			 Configuration Layout area of the individual device configuration window, Common
                                             			 Phone Profile window, or Enterprise Phone Configuration window.

Check Customer support upload URL and
                                             			 enter your upload server URL.

##### Example:

Save your changes.

#### Remote Problem Report Creation with XSI

You can request a PRT with the X/Open System Interface (XSI) CiscoIPPhoneExecute object. For more information, see the Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones .

## Corporate and Personal Directories Setup

You can make it easy for your users to contact coworkers using a corporate directory.

You can also enable users to create personal directories. Each individual user has a personal directory, which they can access
                              from any device.

The corporate and personal directories are set up in the Cisco Unified
                                 				Communications Manager .

### Corporate
                           	 Directory Setup

The Corporate Directory allows a user to look up phone numbers for
                              		coworkers. To support this feature, you must configure corporate directories.

Cisco Unified
                                 				Communications Manager uses a Lightweight Directory Access Protocol (LDAP) directory to store authentication and authorization information about
                              users of Cisco Unified
                                 				Communications Manager applications that interface with Cisco Unified
                                 				Communications Manager . Authentication establishes user rights to access the system. Authorization identifies the telephony resources that a user
                              is permitted to use, such as a specific phone extension.

For more information, see the documentation for your particular Cisco Unified
                                 				Communications Manager release.

After you
                              		complete the LDAP directory configuration, users can use the Corporate
                              		Directory service on their phone to look up users in the corporate directory.

### Personal Directory
                           	 Setup

The Personal Directory allows a user to store a set of personal numbers.

Personal
                              		Directory consists of the following features:

Personal Address
                                    			 Book (PAB)

Speed Dials

Users can
                              		use these methods to access Personal Directory features:

From a web browser—Users can access the PAB and Speed Dials features from the Cisco Unified Communications Self Care Portal.

From the CiscoIP Phone—Choose Contacts to search the corporate directory or the user personal directory.

To
                              		configure Personal Directory from a web browser, users must access their Self
                              		Care Portal. You must provide users with a URL and sign-in information.

## Self Care Portal
                        	 Overview

From the Cisco Unified Communications Self Care Portal, users can
                              		  customize and control phone features and settings.

As the administrator, you control access to the Self Care Portal. You
                              		  must also provide information to your users so that they can access the Self
                              		  Care Portal.

Before a user can access the Cisco Unified Communications Self Care Portal, you must use Cisco Unified
                                 				Communications Manager Administration to add the user to a standard Cisco Unified
                                 				Communications Manager End User group.

You must provide end users with the following information about the Self
                              		Care Portal:

The URL to access the application. This URL is:

https://<server_name:portnumber>/ucmuser/ , where server_name is the host on which the web server is installed, and portnumber is the port number on that host.

A user ID and default password to access  the application.

An overview of the tasks that users can accomplish with  the
                                    			 portal.

These settings correspond to the values that you entered when you added the user to Cisco Unified
                                 				Communications Manager .

For more information, see the documentation for your particular Cisco Unified
                                 				Communications Manager release.

### Set Up User Access to
                           	 the Self Care Portal

Before a user can access the Self Care Portal, you need to authorize the access.

In Cisco Unified
                                             				Communications Manager Administration, select User Management > End User .

Search for the
                                          			 user.

Click the user ID link.

Ensure that
                                          			 the user has a password and PIN configured.

In the Permission Information section, ensure that the Groups list includes Standard CCM End Users .

Select Save .

### Customize the Self Care Portal Display

Most options display on the Self Care Portal. However, you must set the following options by using Enterprise Parameters Configuration
                                 settings in Cisco Unified Communications Manager Administration:

Show Ring Settings

Show Line Label Settings

The settings apply to all Self Care Portal pages at your site.

In Cisco Unified Communications Manager Administration, select System > Enterprise Parameters .

In the Self Care Portal area, set the Self Care Portal Default Server field.

Enable or disable the parameters that the users can access in the portal.

Select Save .

## Custom Wallpaper and Ringtones

You can add custom wallpaper and ringtones to the phones. For example, you might want a wallpaper with your corporate logo.

### Custom Phone
                           	 Rings

The phone ships with three ring tones that are
                                 		  implemented in hardware: Sunshine, Chirp, Chirp1.

Cisco Unified Communications Manager also provides a default set of additional phone ring sounds that are implemented in software
                                 as pulse code modulation (PCM) files. The PCM files, along with an XML file (named Ringlist-wb.xml) that describes the ring
                                 list options that are available at your site, exist in the TFTP directory on each Cisco Unified Communications Manager server.

All file names are case sensitive. If you use Ringlist-wb.xml for the file name, the phone will not apply your changes.

For more information, see the "Custom Phone Rings and Backgrounds" chapter, Feature Configuration Guide for Cisco Unified Communications Manager for Cisco Unified Communications Manager release 12.0(1) or later.

#### Set Up Custom
                              	 Phone Rings

Create a PCM file for each custom ring (one ring per file). Ensure the PCM files comply with the format guidelines that are
                                             listed in Custom Ring File Formats .

Upload the new PCM files that you created to the Cisco TFTP server
                                             			 for each Cisco Unified Communications Manager in your cluster. For more
                                             			 information, see the documentation for your particular Cisco Unified Communications Manager release.

Use a text editor to edit the Ringlist-wb.xml file. See Custom Ring File Formats for information about how to format this file and for a sample Ringlist-wb.xml file.

Save your modifications and close the file.

To cache the new file, stop and start the TFTP
                                             			 service by using Cisco Unified Serviceability or disable and reenable the "Enable Caching of Constant and Bin Files at Startup" TFTP
                                             			 service parameter, located in the Advanced Service Parameters area.

#### Custom Ring File Formats

The Ringlist-wb.xml file defines an XML object that contains a list of phone ring types. This file includes up to 50 ring
                                    types. Each ring type contains a pointer to the PCM file that is used for that ring type and the text that appears on the
                                    Ring Type menu on a phone for that ring. The Cisco TFTP server for each Cisco Unified Communications Manager contains this
                                    file.

The CiscoIPPhoneRinglist XML object uses the following simple
                                    		tag set to describe the information:

```
<CiscoIPPhoneRingList>   
   <Ring>
      <DisplayName/>
      <FileName/>
   </Ring>
</CiscoIPPhoneRingList>
```

The following characteristics apply to the definition names.
                                    		You must include the required DisplayName and FileName for each phone ring
                                    		type.

DisplayName specifies the name of the custom ring for the associated
                                          			 PCM file that displays on the Ring Type menu of the phone.

FileName specifies the name of the PCM file for the custom ring to
                                          			 associate with DisplayName.

The DisplayName and FileName fields must not exceed 25 characters in length.

This example shows a Ringlist-wb.xml file that defines two phone ring types:

```
<CiscoIPPhoneRingList>   
   <Ring>
      <DisplayName>Analog Synth 1</DisplayName>
      <FileName>Analog1.rwb</FileName>
   </Ring>
   <Ring>
      <DisplayName>Analog Synth 2</DisplayName>
      <FileName>Analog2.rwb</FileName>
   </Ring>
</CiscoIPPhoneRingList>
```

The PCM files for the rings must meet the following
                                    		requirements for proper playback on the phones:

Raw PCM (no header)

8000 samples per second

8 bits per sample

Mu-law compression

Maximum ring size = 16080 samples

Minimum ring size =  240 samples

Number of samples in the ring = multiple of 240.

Ring start and end at zero crossing.

To create PCM files for custom phone rings,  use any
                                    		standard audio editing package that supports these file format requirements.

### Custom Background
                           	 Images

You can
                                 		  provide users with a choice of background images (or wallpaper) for the LCD
                                 		  screen on their phones. Users can select a background image by accessing the Settings app and choosing Phone settings > Display > Wallpaper on the phone.

The image
                                 		  choices that users see come from PNG images and an XML file (called List.xml)
                                 		  that are stored on the TFTP server that the phone uses. By storing your own PNG
                                 		  files and editing the XML file on the TFTP server, you can designate the
                                 		  background images from which users can choose. In this way, you can provide
                                 		  custom images, such as your company logo.

The dimensions for the PNG and List.xml images must be within 240x320x24.

If you create your own custom wallpaper, you must make sure that it will display correctly on the wireless phone. The phone
                                 uses white letters, so wallpapers with white or light-colored areas are not suitable.

All file names
                                             			 are case sensitive. If you use list.xml for the file name, the phone will not
                                             			 apply your changes.

You can disable the option for users to select a background image. To do this, you uncheck the Enable End User Access to Phone Background Image Setting check box from the Common Phone Profile Configuration window in Cisco Unified Communications Manager Administration ( Device > Device Settings > Common Phone Profile ). When this check box is unchecked, the wallpaper menu does not display on the phone.

#### Set Up a Custom Background Image

Create two PNG
                                             			 files for each image (a full-size version and a thumbnail version). Ensure the
                                             			 PNG files comply with the format guidelines that are listed in Custom Background File Formats .

Upload the new
                                             			 PNG files that you created to the following subdirectory in the TFTP server for
                                             			 the Cisco Unified Communications Manager:

Desktops/240x320x24

The file
                                                            				  name and subdirectory parameters are case sensitive. Be sure to use the forward
                                                            				  slash "/" when
                                                            				  you specify the subdirectory path.

To upload the
                                                				files, choose Software
                                                      					 Upgrades > Upload TFTP Server File in Cisco
                                                				Unified Communications Operating System Administration. For more information,
                                                				see the documentation for your particular Cisco Unified Communications Manager release.

If the
                                                            				  folder does not exist, the folder gets created and the files get uploaded to
                                                            				  the folder.

You must also
                                             			 copy the customized images and files to the other TFTP servers that the phone
                                             			 may contact to obtain these files.

We
                                                            				  recommend that you store backup copies of custom image files in a different
                                                            				  location. You can use these backup copies if the customized files are
                                                            				  overwritten when you upgrade Cisco Unified Communications Manager.

Use a text
                                             			 editor to edit the List.xml file. See Custom Background File Formats for the file location, file,
                                             			 formatting requirements, and a sample file.

Save your
                                             			 modifications and close the List.xml file.

When you
                                                            				  upgrade Cisco Unified Communications Manager, a default List.xml file replaces
                                                            				  your customized List.xml file. After you customize the List.xml file, make a
                                                            				  copy of the file and store it in a different location. After upgrading Cisco
                                                            				  Unified Communications Manager, replace the default List.xml file with your
                                                            				  stored copy.

To cache the
                                             			 new List.xml file, stop and start the TFTP service by using Cisco Unified
                                             			 Serviceability or disable and reenable the Enable Caching of Constant and Bin
                                             			 Files at Startup TFTP service parameter that is located in the Advanced Service
                                             			 Parameters area.

#### Custom Background
                              	 File Formats

The
                                    		  List.xml file defines an XML object that contains a list of background images.
                                    		  The List.xml file is stored in the following subdirectory on the TFTP server:

Desktops/240x320x24

If you are
                                                			 manually creating the directory structure and the List.xml file, you must
                                                			 ensure that the directories and files can be accessed by the user\CCMService,
                                                			 which is used by the TFTP service.

For more
                                    		  information, see the documentation for your particular Cisco Unified Communications Manager release.

The
                                    		  List.xml file can include up to 50 background images. The images are in the
                                    		  order that they appear in the Background Images menu on the phone. For each
                                    		  image, the List.xml file contains one element type, called ImageItem. The
                                    		  ImageItem element includes these two attributes:

Image—Uniform resource identifier (URI) that specifies where the phone obtains the thumbnail image that appears on the Background
                                          Images menu on a phone.

URL—URI that specifies where the phone obtains the full-size image.

The
                                    		  following example shows a List.xml file that defines two images. The required
                                    		  Image and URL attributes must be included for each image. The TFTP URI that is
                                    		  shown in the example is the only supported method for linking to full-size and
                                    		  thumbnail images. HTTP URL support is not provided.

List.xml
                                    		  Example

```
<CiscoIPPhoneImageList>
<ImageItem Image="TFTP:Desktops/240x320x24/TN-Fountain.png" URL="TFTP:Desktops/800x480x24/Fountain.png"/> 
<ImageItem Image="TFTP:Desktops/240x320x24/TN-FullMoon.png" URL="TFTP:Desktops/800x480x24/FullMoon.png"/> 
</CiscoIPPhoneImageList>
```

The phone firmware includes a default background image. The List.xml file does
                                    		  not define this image. The default image is always the first image that appears
                                    		  in the Background Images menu on the phone.

Each
                                    		  background image requires two PNG files:

Full size image—Version that appears on the on the phone.

Thumbnail image—Version that displays on the Background Images screen from which users can select an image. Must be 25% of
                                          the size of the full-size image.

Many graphics
                                                			 programs provide a feature that resizes a graphic. An easy way to create a
                                                			 thumbnail image is to first create and save the full-size image, then use the
                                                			 sizing feature in the graphics program to create a version of that image that
                                                			 is 25% of the original size. Save the thumbnail version by using a different
                                                			 name.

The PNG
                                    		  files for background images must meet the following requirements for proper
                                    		  display on the phone:

Full size image—240 pixels (width) x 320 pixels (height).

Thumbnail image—117 pixels (width) x 117 pixels (height).

If you are using
                                                			 a graphics program that supports a posterize feature for grayscale, set the
                                                			 number of tonal levels per channel to 16, and the image posterizes to 16 shades
                                                			 of grayscale.

| Perform one of the following actions: On the phone, access the Settings app, select Phone information > Model information , and look in the MAC address field. Remove the battery cover and battery from the phone, and look at the label. Display the phone web page and look at the MAC address in the Device information screen. If the phone has already been added to the Cisco Unified Communications Manager,  access the Cisco Unified Communications
                                          Manager Administration application, select Device > Phone , search for the phone, and access the Phone Configuration window. |
|---|

| Step 1 | In the Cisco Unified Communications Administration, select Device > Device Settings > Wireless LAN Profile . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Wireless LAN Profile Information section, set the  parameters: Name —Enter a unique name for the Wi-Fi profile.  This name displays on the phone. Description —Enter a description for the Wi-Fi profile to help you differentiate this profile from other Wi-Fi profiles. User Modifiable —Select an option: Allowed —Indicates that the user can make changes to the Wi-Fi  settings from their phone. This option is selected by default. Disallowed —Indicates that the user cannot make any changes to the Wi-Fi settings on their phone. Restricted —Indicates that the user can change the Wi-Fi username and password on their phone. But users are not allowed to make changes
                                                            to other Wi-Fi settings on the phone. |
| Step 4 | In the Wireless Settings section, set the  parameters: SSID (Network Name) —Enter the network name available in the user environment to which the phone can be connected. This name is displayed under
                                                   the available network list on the phone and the phone can connect to this wireless network. Frequency Band —Available options are Auto, 2.4 GHz, and 5 GHz. This field determines the frequency band that the wireless connection uses.
                                                   If you select Auto, the phone  attempts to use the 5 GHz band first and only uses the 2.4 GHz band when the 5 GHz is not available. |
| Step 5 | In the Authentications Settings section, set the Authentication Method to one of these authentication methods: EAP-FAST, EAP-TLS,  PEAP-MSCHAPv2,  PEAP-GTC, PSK, WEP, and None. After you set this field, you may see extra fields that you need to set. User certificate —Required for EAP-TLS authentication. Select Manufacturing installed or User installed .  The phone requires a certificate to be installed, either automatically from the SCEP or manually from the administration
                                                   page on the phone. PSK passphrase —Required for PSK authentication. Enter the 8- 63 character ASCII or 64 HEX character pass phrase. WEP Key —Required for WEP authentication. Enter the 40/102 or 64/128 ASCII or HEX WEP key. 40/104 ASCII is 5 characters. 64/128 ASCII is 13 characters. 40/104 HEX is 10 characters. 64/128 HEX is 26 characters. Provide Shared Credentials : Required for  EAP-FAST, PEAP-MSCHAPv2, and   PEAP-GTC authentication. If the user manages the username and password, leave the Username and Password fields blank. If all your users share the same username and password, you can input the information in the Username and Password fields. Enter a description in the Password Description field. Note If you need to assign each user a unique username and password, you need to create a profile for each user. Note The Network Access Profile field is not supported by the Cisco IP Phone 8821. | Note | If you need to assign each user a unique username and password, you need to create a profile for each user. | Note | The Network Access Profile field is not supported by the Cisco IP Phone 8821. |
| Note | If you need to assign each user a unique username and password, you need to create a profile for each user. |
| Note | The Network Access Profile field is not supported by the Cisco IP Phone 8821. |
| Step 6 | Click Save . |

| Note | If you need to assign each user a unique username and password, you need to create a profile for each user. |
|---|---|

| Note | The Network Access Profile field is not supported by the Cisco IP Phone 8821. |
|---|---|

| Step 1 | In Cisco Unified Communications Administration, select Device > Device Settings > Wireless LAN Profile Group . You can also define a wireless LAN profile group from System > Device Pool . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Wireless LAN Profile Group Information section, enter a group name and description. |
| Step 4 | In the Profiles for this Wireless LAN Profile Group section, select an available profile from the Available Profiles list and move the selected profile to the Selected Profiles list. |
| Step 5 | Click Save . |

| Step 1 | In Cisco Unified Communications Manager Administration, select Device > Device Settings > SIP Profile . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Click the Copy icon beside Standard SIP Profile . |
| Step 4 | Set the name and description to Custom 8821 SIP Profile . |
| Step 5 | Set these parameters. Timer Register Delta (seconds) —Set to 30 (default is 5). Timer Keep Alive Expires (seconds) —Set to 300 (default is 120). Timer Subscribe Expires (seconds) —Set to 300 (default is 120). Timer Subscribe Delta (seconds) —Set to 15 (default is 5). |
| Step 6 | Click Save . |

| Note | This version of the BDU is not the same as the BDU for the Cisco Unified Wireless IP Phone 792x Series. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Select Cisco 8821 . If Cisco 8821 does not appear, the Cisco Unified Communications Manager Device Pack to support  the phone is not installed on the server. |
| Step 4 | Click Next . |
| Step 5 | Set the phone information. Required fields are marked with an asterisk (*), although most take the default settings. The fields that need specific entries
                                             are: MAC address—Enter the MAC address of the phone. You can enter the address with lowercase letters. Description—Set this field to something meaningful; for example, the user's name. Device pool—Set this field for the appropriate pool of phones. Phone Button Template—Select Standard 8821 SIP . Owner User ID—Select the user's ID. Device security profile—Select Cisco 8821 Standard SIP Non Secure Profile . SIP profile—Select Custom 8821 SIP Profile . For more information, see Set up a Wireless Phone SIP Profile . |
| Step 6 | (Optional) In the Wireless LAN Profile Group field, select the wireless LAN profile group if the profile is not associated with a device pool. For more information, see Set Up a Wi-Fi Profile using Cisco Unified Communications Manager . |
| Step 7 | Click Save . |
| Step 8 | Click OK . |
| Step 9 | Click Apply config . |
| Step 10 | Click OK . |
| Step 11 | Click Line[1] — Add a new DN . |
| Step 12 | Enter a DN. |
| Step 13 | Click Save and then click Save again. |
| Step 14 | In the Related links field, select Configure Device and click Go . |
| Step 15 | Click Save and click OK . |
| Step 16 | Click Apply config and click OK . |

| Step 1 | Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator. |
|---|---|
| Step 2 | Select System > Enterprise Phone Configuration . |
| Step 3 | Set the fields you want to change. |
| Step 4 | Check the Override Enterprise Settings check box for any changed fields. |
| Step 5 | Click Save . |
| Step 6 | Click Apply Config . |
| Step 7 | Restart the phones. Note This will impact all phones in your organization. | Note | This will impact all phones in your organization. |
| Note | This will impact all phones in your organization. |

| Note | This will impact all phones in your organization. |
|---|---|

| Step 1 | Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator. |
|---|---|
| Step 2 | Select Device > Device Settings > Common Phone Profile . |
| Step 3 | Locate the profile. |
| Step 4 | Navigate to the Product Specific Configuration Layout pane and set the fields. |
| Step 5 | Check the Override Enterprise Settings check box for any changed fields. |
| Step 6 | Click Save . |
| Step 7 | Click Apply Config . |
| Step 8 | Restart the phones. |

| Step 1 | Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator. |
|---|---|
| Step 2 | Select Device > Phone |
| Step 3 | Locate the phone associated with the user. |
| Step 4 | Navigate to the Product Specific Configuration Layout pane and set the fields. |
| Step 5 | Check the Override Common Settings check box for any changed fields. |
| Step 6 | Click Save . |
| Step 7 | Click Apply Config . |
| Step 8 | Restart the phone. |

| Field Name | Field Type Or Choices | Default | Description |
|---|---|---|---|
| Battery Lifetime Alert | Disabled Enabled | Disabled | Enables or disables Battery Lifetime alert, Phone SN alert, and Overvoltage alert. |
| Battery Lifetime Alert Interval | 6 Months 12 Months 18 Months 24 Months | 24 Months | Specifies the interval time over which the Battery Lifetime Alert is generated. |
| Battery SN Reminder | Disabled Enabled | Disabled | Enables or disables Battery SN Reminder. |
| Disable Speakerphone | Checkbox | Unchecked | Turns off the speakerphone capability of the handset. See Note 1. |
| Disable Speakerphone and Headset | Checkbox | Unchecked | Turns off the speakerphone and headset capability of the handset. See Note 1. |
| Settings Access | Disabled Enabled Restricted | Enabled | Enables, disables, or restricts access to local
                                             					 configuration settings in the Settings app. With restricted access, the Phone Settings, Bluetooth, and Phone Information menus can be accessed. Some settings in the Wi-Fi
                                             menu are also accessible. With disabled access, the Settings menu does
                                             					 not display any options. |
| Web Access | Disabled Enabled | Disabled | Enables or disables access to the phone web pages through a web browser. Caution If you enable this field, you may expose sensitive
                                                         information about the phone. | Caution | If you enable this field, you may expose sensitive
                                                         information about the phone. |
| Caution | If you enable this field, you may expose sensitive
                                                         information about the phone. |
| HTTPS Server | HTTP and HTTPS enabled HTTPS only | HTTP and HTTPS enabled | Controls the type of communication to the phone. If you select HTTPS only, the phone communication is more secure. |
| Disable TLS 1.0 and TLS 1.1 for Web Access | Disabled Enabled | Disabled | Controls the use of TLS 1.2 for a web server connection. Disabled—A phone configured for TLS1.0, TLS 1.1, or TLS1.2 can function as an HTTPS server. Enabled—Only a phone configured for TLS1.2 can function as an HTTPS server. |
| Web Admin | Disabled Enabled | Disabled | Enables or disables administrator access to the phone web pages through a web browser |
| Admin Password | String of 8–127 characters |  | Defines the administrator password when you access the phone web pages as an administrator. |
| Bluetooth | Disabled Enabled | Enabled | Enables or disables the Bluetooth option on the
                                             					 phone. If disabled, the user cannot enable Bluetooth on the phone. |
| Out-of-Range Alert | Disabled Beep once Beep every 10 seconds Beep every 30 seconds Beep every 60 seconds | Disabled | Controls the frequency of audible alerts when the phone is out of range of an AP. The phone does not play audible alerts when
                                             the parameter value is "disabled." The phone can beep one time or regularly at 10, 30, or 60 second intervals. When the phone
                                             is within range of an AP, the alert stops. |
| Scan Mode | Auto Single AP Continuous | Continuous | Controls the scanning by the phone. Auto—Phone scans when it is in a call or when the received strength signal indicator (RSSI) is low. Single AP—Phone never scans except when the basic service set (BSS) is lost. Continuous—Phone scans continuously even when it is not in a call. |
| Application URL | String of up to 256 characters |  | Specifies the URL that the phone uses to contact application services, including Push To Talk. |
| Application Request Timer | 5 seconds 20 seconds | 5 seconds | Controls the length of the application request timer in seconds. Increase the length of the timer if you see "405" error messages in the log file. |
| Application Button Activation Timer | Disabled 1 second 2 seconds 3 seconds 4 seconds 5 seconds | Disabled | Specifies the amount of time that the user must hold the Application button to activate the Application URL. |
| Application Button Priority | Low Medium High | Low | Indicates the priority of the Application button relative to the other phone tasks. Low—Specifies that the Application button works only when the phone is idle and on the main screen. Medium—Specifies that the button takes precedence over all tasks except when the keypad is locked. High—Specifies that the button takes precedence over all tasks on the phone. When the priority is high, the keypad locked and the screen dark, pressing the application button turns on the phone screen.
                                                   The user presses the button a second time to perform the application button function. |
| Emergency Numbers | String of up to 16 characters, comma separated, no spaces |  | Sets the list of emergency numbers that the users see when they try to dial without signing in. Example: 911,411 |
| Dialing Mode | On-hook Dialing Off-hook Dialing | On-hook Dialing | Sets the default dialing mode for the phones. |
| Power Off in Multicharger | Disabled Enabled | Disabled | When disabled, the phone doesn't power off when placed in the multicharger. When enabled, the phone powers off when placed
                                             in the multicharger. |
| Background Image | String up to 64 characters |  | Sets the background image that all users see. If you set a background image, the user cannot change the phone to another image. |
| Home Screen | Application View Line View | Application View | Sets the home screen to either the Application View or the Line View. Set the phone to use Line View for users that use multiple lines, speed dials, or make many calls. |
| Left Softkey | None Favorites Local Contacts Voicemail | Favorites | Controls the left-most softkey on the phone. None: the softkey is blank Favorites: the softkey displays Favorites . Local Contacts: the softkey displays Local contacts . Voicemail: the softkey displays Voicemail . |
| Voicemail Access | Disabled Enabled | Enabled | Controls access to voicemail. |
| Applications Access | Disabled Enabled | Enabled | Controls access to the Applications menu. |
| Recording Tone | Disabled Enabled | Disabled | Controls the playing of the tone when a user is recording a call |
| Recording Tone Local Volume | Integer 0–100 | 100 | Controls the volume of the recording tone to the local user. |
| Recording Tone Remote Volume | Integer 0–100 | 50 | Controls the volume of the recording tone to the remote user. |
| Recording Tone Duration | Integer 1–3000 milliseconds |  | Controls the duration of the recording tone. |
| Remote Log | Disabled Enabled | Disabled | Controls the ability to send logs to the syslog server. |
| Log Profile | Default Preset Telephony | Preset | Specifies the predefined logging profile. |
| Log Server | String of up to 256 characters |  | Identifies the IPv4 syslog server for phone debug output. The format for the address is: address:<port>@@base=<0-7>;pfs=<0-1> |
| Cisco Discovery Protocol (CDP) | Disabled Enabled | Enabled | Controls Cisco Discovery Protocol on
                                             					 the phone. |
| SSH Access | Disabled Enabled | Disabled | Controls the  access to the SSH daemon through port 22. Leaving port 22 open leaves the phone vulnerable to Denial of Service
                                             (DoS) attacks. |
| Ring Locale | Default Japan | Default | Controls the ringing pattern. |
| TLS Resumption Timer | Integer 0–3600 seconds | 3600 | Controls the ability to resume a TLS session without repeating the entire TLS authentication process. If the field is set
                                             to 0, then the TLS session resumption is disabled. |
| Record Call Log from Shared Line | Disabled Enabled | Disabled | Specifies whether to record call log from a shared line. |
| Minimum Ring Volume | Silent Volume level 1–15 | Silent | Controls the minimum ring volume for the phone. |
| Load Server | String of up to 256 characters |  | Identifies the alternate IPv4 server that the phone uses
                                             					 to obtain firmware loads and upgrades. |
| WLAN SCEP Server | String of up to 256 characters |  | Specifies the SCEP Server that the phone uses to obtain certificates for WLAN authentication. Enter the hostname or the IP
                                             address (using standard IP addressing format) of the server. |
| WLAN Root CA Fingerprint (SHA256 or SHA1) | String of up to 95 characters |  | Specifies the SHA256 or SHA1 fingerprint of the Root CA to use for validation during the SCEP process when issuing certificates
                                             for WLAN authentication. We recommend that you use the SHA256 fingerprint, which can be obtained via OpenSSL (e.g. openssl
                                             x509 -in rootca.cer -noout -sha256 -fingerprint) or using a Web Browser to inspect the certificate details. Enter the 64 hexadecimal character value for the SHA256 fingerprint or the 40 hexadecimal character value for the SHA1 fingerprint
                                             with a common separator (colon, dash, period, space) or without a separator. If using a separator, then the separator should
                                             be consistently placed after every 2, 4, 8, 16, or 32 hexadecimal characters for a SHA256 fingerprint or every 2, 4, or 8
                                             hexadecimal characters for a SHA1 fingerprint. |
| Console Access | Disabled Enabled | Disabled | Specifies whether the serial console is enabled or disabled. |
| Gratuitous ARP | Disabled, Enabled | Disabled | Enables or disables the ability for the phone to
                                             					 learn MAC addresses from Gratuitous ARP. This capability is required to monitor
                                             					 or record voice streams. |
| Show All Calls on Primary Line | Disabled Enabled | Disabled | Specifies is all calls presented to this phone will be shown on the primary line or not. |
| Advertise G.722 and iSAC Codecs | Use System Default Disabled Enabled | Use System Default | Indicates whether the phone advertises the G.722
                                             					 and iSAC codecs to the Cisco Unified Communications Manager. Use System
                                                   						Default—Defers to the setting specified in the enterprise parameter Advertise
                                                   						G.722 Codec. Disabled—Does not
                                                   						advertise G.722 to the Cisco Unified Communications Manager. Enabled—Advertises G.722 to the Cisco Unified Communications Manager. For more information, see Note 2. |
| Revert to All Calls | Disabled Enabled | Disabled | Specifies whether the phone will revert to All Calls after any call ends or not if the call is on a filter other than Primary
                                             line, All Calls, or Alerting Calls. |
| DF bit | 0 1 | 0 | Controls how network packets are sent. Packets can be sent in chunks (fragments) of various sizes. When the DF bit is set to 1 in the packet header, the network payload does not fragment when going through network devices,
                                             such as switches and routers. Removing fragmenting avoids incorrect parsing on the receiving side, but results in slightly
                                             slower speeds. The DF bit setting does not apply to ICMP, VPN, VXC VPN, or DHCP traffic. |
| Lowest Alerting Line State Priority | Disabled Enabled | Disabled | Specifies the alert state when using shared lines. When disabled and there is an incoming call alerting on the shared line,
                                             the LED/Line state icon reflects the alerting state instead of Remote-In-Use. When enabled, the user sees the Remote-In-Use
                                             icon when there is call alerting on the shared line. |
| Divert Alerting Call | Disabled Enabled | Enabled | Controls the display of the Decline softkey. Disabled: the Decline softkey doesn't display when there is an incoming call. The user can't divert or dismiss the incoming call. Enabled: the Decline softkey displays when there is an incoming call. The user can decline the call. |
| Allow Vibrate URI When On Call | Disabled Enabled | Disabled | Controls if the Vibrate URI command from an XSI message is allowed when the phone is active on a call. Disabled: The handset won't vibrate. Enabled: The handset will vibrate. |
| Customer support upload URL | String of up to 256 characters |  | Identifies the location that the phones use to upload problem reporting tool (PRT) output files. |

| Caution | If you enable this field, you may expose sensitive
                                                         information about the phone. |
|---|---|

| Note | If you change a user's audio path while they are in the Push to Talk session, the user needs to end the current session and
                                                   restart to get the correct audio path selection. Codec negotiation involves
                                                   					 two steps: The phone must advertise the supported codec to the Cisco
                                                         						  Unified Communications Manager (not all endpoints support the same set of
                                                         						  codecs). When the Cisco Unified Communications Manager gets the
                                                         						  list of supported codecs from all phones involved in the call attempt, it
                                                         						  chooses a commonly supported codec based on various factors, including the
                                                         						  region pair setting. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, choose Device > Device Settings > Phone Services . |
|---|---|
| Step 2 | Set up the services. |
| Step 3 | Verify that your users have access to the Self Care portal. |

| Note | The Problem Report Tool logs are required by Cisco TAC when troubleshooting problems. The logs are cleared if you restart
                                             the phone. Collect the logs before you restart the phones. |
|---|---|

| Note | The phones only support HTTP URLs. |
|---|---|

| Step 1 | Set up a server that can run your PRT upload script. |
|---|---|
| Step 2 | Write a script that can handle the parameters listed above, or edit the provided sample script to suit your needs. |
| Step 3 | Upload your script to your server. |
| Step 4 | In Cisco Unified Communications Manager, go to the Product Specific
                                             			 Configuration Layout area of the individual device configuration window, Common
                                             			 Phone Profile window, or Enterprise Phone Configuration window. |
| Step 5 | Check Customer support upload URL and
                                             			 enter your upload server URL. Example: http://example.com/prtscript.php |
| Step 6 | Save your changes. |

| Step 1 | In Cisco Unified
                                             				Communications Manager Administration, select User Management > End User . |
|---|---|
| Step 2 | Search for the
                                          			 user. |
| Step 3 | Click the user ID link. |
| Step 4 | Ensure that
                                          			 the user has a password and PIN configured. |
| Step 5 | In the Permission Information section, ensure that the Groups list includes Standard CCM End Users . |
| Step 6 | Select Save . |

| Note | The settings apply to all Self Care Portal pages at your site. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, select System > Enterprise Parameters . |
|---|---|
| Step 2 | In the Self Care Portal area, set the Self Care Portal Default Server field. |
| Step 3 | Enable or disable the parameters that the users can access in the portal. |
| Step 4 | Select Save . |

| Attention | All file names are case sensitive. If you use Ringlist-wb.xml for the file name, the phone will not apply your changes. |
|---|---|

| Step 1 | Create a PCM file for each custom ring (one ring per file). Ensure the PCM files comply with the format guidelines that are
                                             listed in Custom Ring File Formats . |
|---|---|
| Step 2 | Upload the new PCM files that you created to the Cisco TFTP server
                                             			 for each Cisco Unified Communications Manager in your cluster. For more
                                             			 information, see the documentation for your particular Cisco Unified Communications Manager release. |
| Step 3 | Use a text editor to edit the Ringlist-wb.xml file. See Custom Ring File Formats for information about how to format this file and for a sample Ringlist-wb.xml file. |
| Step 4 | Save your modifications and close the file. |
| Step 5 | To cache the new file, stop and start the TFTP
                                             			 service by using Cisco Unified Serviceability or disable and reenable the "Enable Caching of Constant and Bin Files at Startup" TFTP
                                             			 service parameter, located in the Advanced Service Parameters area. |

| Note | The DisplayName and FileName fields must not exceed 25 characters in length. |
|---|---|

| Note | The dimensions for the PNG and List.xml images must be within 240x320x24. |
|---|---|

| Attention | All file names
                                             			 are case sensitive. If you use list.xml for the file name, the phone will not
                                             			 apply your changes. |
|---|---|

| Step 1 | Create two PNG
                                             			 files for each image (a full-size version and a thumbnail version). Ensure the
                                             			 PNG files comply with the format guidelines that are listed in Custom Background File Formats . |
|---|---|
| Step 2 | Upload the new
                                             			 PNG files that you created to the following subdirectory in the TFTP server for
                                             			 the Cisco Unified Communications Manager: Desktops/240x320x24 Note The file
                                                            				  name and subdirectory parameters are case sensitive. Be sure to use the forward
                                                            				  slash "/" when
                                                            				  you specify the subdirectory path. To upload the
                                                				files, choose Software
                                                      					 Upgrades > Upload TFTP Server File in Cisco
                                                				Unified Communications Operating System Administration. For more information,
                                                				see the documentation for your particular Cisco Unified Communications Manager release. Note If the
                                                            				  folder does not exist, the folder gets created and the files get uploaded to
                                                            				  the folder. | Note | The file
                                                            				  name and subdirectory parameters are case sensitive. Be sure to use the forward
                                                            				  slash "/" when
                                                            				  you specify the subdirectory path. | Note | If the
                                                            				  folder does not exist, the folder gets created and the files get uploaded to
                                                            				  the folder. |
| Note | The file
                                                            				  name and subdirectory parameters are case sensitive. Be sure to use the forward
                                                            				  slash "/" when
                                                            				  you specify the subdirectory path. |
| Note | If the
                                                            				  folder does not exist, the folder gets created and the files get uploaded to
                                                            				  the folder. |
| Step 3 | You must also
                                             			 copy the customized images and files to the other TFTP servers that the phone
                                             			 may contact to obtain these files. Note We
                                                            				  recommend that you store backup copies of custom image files in a different
                                                            				  location. You can use these backup copies if the customized files are
                                                            				  overwritten when you upgrade Cisco Unified Communications Manager. | Note | We
                                                            				  recommend that you store backup copies of custom image files in a different
                                                            				  location. You can use these backup copies if the customized files are
                                                            				  overwritten when you upgrade Cisco Unified Communications Manager. |
| Note | We
                                                            				  recommend that you store backup copies of custom image files in a different
                                                            				  location. You can use these backup copies if the customized files are
                                                            				  overwritten when you upgrade Cisco Unified Communications Manager. |
| Step 4 | Use a text
                                             			 editor to edit the List.xml file. See Custom Background File Formats for the file location, file,
                                             			 formatting requirements, and a sample file. |
| Step 5 | Save your
                                             			 modifications and close the List.xml file. Note When you
                                                            				  upgrade Cisco Unified Communications Manager, a default List.xml file replaces
                                                            				  your customized List.xml file. After you customize the List.xml file, make a
                                                            				  copy of the file and store it in a different location. After upgrading Cisco
                                                            				  Unified Communications Manager, replace the default List.xml file with your
                                                            				  stored copy. | Note | When you
                                                            				  upgrade Cisco Unified Communications Manager, a default List.xml file replaces
                                                            				  your customized List.xml file. After you customize the List.xml file, make a
                                                            				  copy of the file and store it in a different location. After upgrading Cisco
                                                            				  Unified Communications Manager, replace the default List.xml file with your
                                                            				  stored copy. |
| Note | When you
                                                            				  upgrade Cisco Unified Communications Manager, a default List.xml file replaces
                                                            				  your customized List.xml file. After you customize the List.xml file, make a
                                                            				  copy of the file and store it in a different location. After upgrading Cisco
                                                            				  Unified Communications Manager, replace the default List.xml file with your
                                                            				  stored copy. |
| Step 6 | To cache the
                                             			 new List.xml file, stop and start the TFTP service by using Cisco Unified
                                             			 Serviceability or disable and reenable the Enable Caching of Constant and Bin
                                             			 Files at Startup TFTP service parameter that is located in the Advanced Service
                                             			 Parameters area. |

| Note | The file
                                                            				  name and subdirectory parameters are case sensitive. Be sure to use the forward
                                                            				  slash "/" when
                                                            				  you specify the subdirectory path. |
|---|---|

| Note | If the
                                                            				  folder does not exist, the folder gets created and the files get uploaded to
                                                            				  the folder. |
|---|---|

| Note | We
                                                            				  recommend that you store backup copies of custom image files in a different
                                                            				  location. You can use these backup copies if the customized files are
                                                            				  overwritten when you upgrade Cisco Unified Communications Manager. |
|---|---|

| Note | When you
                                                            				  upgrade Cisco Unified Communications Manager, a default List.xml file replaces
                                                            				  your customized List.xml file. After you customize the List.xml file, make a
                                                            				  copy of the file and store it in a different location. After upgrading Cisco
                                                            				  Unified Communications Manager, replace the default List.xml file with your
                                                            				  stored copy. |
|---|---|

| Tip | If you are
                                                			 manually creating the directory structure and the List.xml file, you must
                                                			 ensure that the directories and files can be accessed by the user\CCMService,
                                                			 which is used by the TFTP service. |
|---|---|

| Tip | Many graphics
                                                			 programs provide a feature that resizes a graphic. An easy way to create a
                                                			 thumbnail image is to first create and save the full-size image, then use the
                                                			 sizing feature in the graphics program to create a version of that image that
                                                			 is 25% of the original size. Save the thumbnail version by using a different
                                                			 name. |
|---|---|

| Tip | If you are using
                                                			 a graphics program that supports a posterize feature for grayscale, set the
                                                			 number of tonal levels per channel to 16, and the image posterizes to 16 shades
                                                			 of grayscale. |
|---|---|