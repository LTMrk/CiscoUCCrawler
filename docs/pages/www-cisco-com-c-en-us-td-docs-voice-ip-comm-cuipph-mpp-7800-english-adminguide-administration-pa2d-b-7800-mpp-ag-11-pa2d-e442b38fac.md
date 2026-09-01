---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-adminguide-administration-pa2d-b-7800-mpp-ag-11-pa2d-e442b38fac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/adminguide/administration/pa2d_b_7800-mpp-ag-11/pa2d_b_7800-mpp-ag-11_chapter_01010.html
retrieved_at: 2026-09-01T15:41:27.535822+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Updated: April 29, 2019

Chapter: Cisco IP Phone Customization

## Chapter: Cisco IP Phone Customization

# Cisco IP Phone Customization

## Phone Information and Display Settings

The phone web user interface allows you to customize settings such as the phone name, background picture, logo, and screen
                              saver.

### Configure the Phone Name

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Under General , enter the phone name in the Station Display Name field.

This name displays on the phone LCD in the top left corner.

Click Submit All Changes .

### Change Wallpaper from the Phone Page

Your administrator can allow you to change the default wallpaper on your phone to one of the wallpapers available.

On the phone web page, select User Login > Voice > User .

In the Phone Background field of the Screen section, select any of the options as a phone wallpaper.

Default : Phone does not have any wallpaper. If no wallpaper is added to the phone screen, the phone screen displays monochrome wallpaper.

Logo : In the phone web page you can select Logo as your phone background option. The logo that you add in the Logo URL is used as the wallpaper.

Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL .

The logo display area is the center of the phone screen. The logo display area size of the phone is 128x128 pixels. If original
                                                   logo size does not fit display area, the logo scales to fit the display area.

Click Submit All Changes .

### Add a Logo as the Boot Display

If you want your user to see a logo icon when the phone restarts, enable this feature from the phone web page.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > User .

In the Screen section, select Logo from the Boot Display field. In the Logo URL field, enter a URL or path for the location where the logo image is saved.

You can also download a picture and add it as a boot display: select Download Picture from the Boot Display field. In the Picture Download URL field, enter a URL or path for the location where the picture is saved.

The logo must be a .jpg or a .png file. The phone has a fixed display area. So, if the original logo size doesn't fit into
                                             the display area, you need to scale it to fit the screen. For the Cisco IP Phone 7811, 7821, 7841 and 7861 the logo display
                                             area is at the mid-center of the phone screen. The display area size of the Cisco IP Phone 7811 is 48x48. The display area
                                             size of the Cisco IP Phone 7821, 7841, and 7861 is 64x64.

Click Submit All Changes .

### Adjust Backlight Timer from Configuration Utility

You can save energy by disabling the backlight on each phone at a preset time. The phone's desktop remains visible, even with
                                 the backlight off.

User can select User Login > Advanced > Voice > User and can adjust the backlight timer.

Backlights are not supported on the Cisco IP Phone 7811.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > User .

Under Screen, select a setting for the Back Light Timer parameter.

In the LCD Contrast field, enter a number for the desired contrast.

### Configure the Number of Call Appearances Per Line

Phones that support multiple call appearances on a line can be configured to specify the number of calls to allow on the line.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Miscellaneous Line Key Settings section, use the Call Appearances Per Line drop-down list box to specify the number of calls per line to allow.

Click Submit All Changes .

### Reverse Name Lookup for Incoming and Outgoing Calls

Reverse name lookup searches for the name of a number in an incoming, outgoing, conference, or transfer call. The reverse
                                 name lookup acts when the phone cannot find a name using the service provider directory, Call History, or your contacts. Reverse
                                 name lookup needs a valid LDAP Directory or XML Directory configuration.

The reverse name lookup searches the phone's external directories. When a search succeeds, the name is placed in the call
                                 session and in the call history. For simultaneous, multiple phone calls, reverse name lookup searches for a name to match
                                 the first call number. When the second call connects or is placed on hold, reverse name lookup searches for a name to match
                                 the second call.

Reverse name lookup is enabled by default.

Reverse name lookup searches the directories in the following order:

Phone contacts

Call History

LDAP Directory

XML Directory

The phone searches the XML directory using this format: directory_url?n=incoming_call_number .

Example: For a multiplatform phone using a third-party service, the phone number (1234) search query has this format, http://your-service.com/dir.xml?n=1234 .

#### Enable and Disable Reverse Name Lookup

##### Before you begin

Configure one of these directories before you can enable or disable the reverse name lookup:

LDAP Corporate Directory

XML Directory

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Supplementary Services area, set the Reverse Phone Lookup Serv to:

- Yes –Enable the reverse name lookup feature.

- No –Disable the reverse name lookup feature.

Click Submit All Changes .

Alternative method is to use the config.xml file to provision the reverse name lookup feature.

```
<Reverse_Phone_Lookup_Serv ua="na">Yes</Reverse_Phone_Lookup_Serv>
```

## Call Features Configuration

### Enable Call Transfer

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Under Supplementary Services , choose Yes for each of the transfer services that you want to enable:

Attn Transfer Serv —Attended call transfer service. The user answers the call before transferring it.

Blind Transfer Serv —Blind call transfer service. The user transfers the call without speaking to the caller.

To disable a transfer service, set the field to No .

Click Submit All Changes .

### Call Forward

To enable call forwarding, you can enable the feature in two places: on the Voice tab and the User tab of the phone web page.

#### Enable Call Forwarding on Voice Tab

##### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Under Supplementary Services , choose Yes for each of the call forwarding services that you want to enable:

Cfwd All Serv —Forwards all calls.

Cfwd Busy Serv —Forwards calls only if the line is busy.

Cfwd No Ans Serv —Forwards calls only if the line is not answered.

Click Submit All Changes .

#### Enable Call Forwarding on User Tab

##### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > User .

Under Call Forward , choose Yes for CFWD Setting.

Click Submit All Changes .

### Enable Conferencing

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Under Supplementary Services , choose Yes in the Conference Serv drop-down list box.

Click Submit All Changes .

### Enable Remote Call Recording with SIP REC

You can enable call recording on a phone so that your user can record an active call. The recording mode configured on the
                                 server controls the display of the recording softkeys for each phone.

Recording Mode in Server

Recording Softkeys Available on the Phone

Always

No softkeys available.

Your user can't control recording from the phone. Recording starts automatically when a call is connected.

Always with Pause/Resume

PauseRec

ResumeRec

When a call is connected, recording starts automatically and your user can control the recording.

On Demand

Record

PauseRec

ResumeRec

When a call is connected, recording starts automatically but the recording is not saved until the user presses the Record softkey. Your user sees a message when recording state changes.

On Demand with User Initiated Start

Record

PauseRec

StopRec

ResumeRec

The recording only starts when your user presses the Record softkey. Your user sees a message when recording state changes.

During a recording, your user sees different icons which depend on the recording state. The icons are displayed on the Calls
                                 screen and also on the line key on which the user is recording a call.

Icon

Meaning

Recording in progress.

Recording paused

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Supplementary Services section, click Yes or click No to enable or to disable call recording in the Call Recording Serv field.

(Optional) In the Programmable Softkeys section, to enable softkeys, add a string in this format in the Connected Key List and Conferencing Key List fields.

crdstart;crdstop;crdpause;crdresume

In the phone web page, click the Ext(n) tab that requires call recording.

In the SIP Settings section, in the Call Recording Protocol , select SIPREC as the call recording protocol.

For details on the SIP Settings fields, see SIP Settings .

Click Submit All Changes .

### Enable Remote Call Recording with SIP INFO

You can enable call recording on a phone so that your user can record an active call.

During a recording, your user sees different icons which depend on the recording state. The icons are displayed on the Calls
                                 screen and also on the line key on which the user is recording a call.

Your user presses the following softkeys to control the phone recording:

Record

StopRec

The recording only starts when your user presses the Record softkey. Your user sees a message when recording state changes and the recording icon displays on the call screen.

Once a phone recording starts, the StopRec softkey can work. The recording stops when your user presses the StopRec softkey. Your user sees a message when the recording state changes.

Icon

Meaning

Recording in progress.

#### Before you begin

You need to set up call recording on the call control system.

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Supplementary Services section, click Yes or click No to enable or to disable call recording in the Call Recording Serv field.

(Optional) In the Programmable Softkeys section, to enable softkeys, add a string in this format in the Connected Key List and Conferencing Key List fields.

crdstart;crdstop;crdpause;crdresume

In the phone web page, click the Ext(n) tab that requires call recording.

In the SIP Settings section, in the Call Recording Protocol , select SIPINFO as the call recording protocol.

For details on SIP Settings fields, see SIP Settings .

Click Submit All Changes .

### Configure Missed Call Indication with the Configuration Utility

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > User .

The user can select User Login > Voice > User .

Click Submit All Changes .

### Enable Do Not Disturb

You can allow persons to turn the Do not disturb feature on or off. The caller receives a message that the person is unavailable.
                                 A person can press the Ignore softkey on the phone to divert an incoming call to another destination.

If the feature is enabled for the phone, users can turn the feature on or off with the DND softkey.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Choose Voice > User .

In the Supplementary Services area, select Yes in the DND Setting drop-down list.

Click Submit All Changes .

When you select a line (multiline phone), a Do Not Disturb banner displays at the top of the phone screen.

#### What to do next

Change another setting to ensure that multiline phones correctly display the Do not disturb (currently, a steady, green color)
                                 status for each selected or unselected line. See DND and Call Forwarding Status Sync .

Users can enable or turn off the DND feature for each phone line if you configure star codes for DND.  See Configure Star Codes for DND .

### Configure Star Codes for DND

You can configure star codes that a user dials to turn on or off the do not disturb (DND) feature  on a phone.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Regional .

In the Vertical Service Activation Codes area, enter *78 in the DND Act Code field.

In the Vertical Service Activation Codes area, enter *79 in the DND Deact Code field.

Click Submit All Changes .

## Set Up a Call Center Agent Phone

You can enable a phone with Automatic Call Distribution (ACD) features. This phone acts as a call center agent's phone and
                              can be used to trace a customer call, to escalate any customer call to a supervisor in emergency, to categorize contact numbers
                              using disposition codes, and to view customer call details.

### Before you begin

Set up the phone as a call center phone on the BroadSoft server.

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Ext(n) .

In the ACD Settings section, set up the fields as described in ACD Settings .

Click Submit All Changes .

## Set Up a Phone for Presence

### Before you begin

Set up the Broadsoft server for XMPP.

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Broadsoft XMPP section, set the fields as described in Broadsoft XMPP .

Click Submit All Changes .

## Shared Lines

A shared line is a directory number that appears on more than one phone. You can create a shared line by assigning the same
                              directory number to different phones.

Incoming calls display on all phones that share a line, and anyone can answer the call. Only one call remains active at a
                              time on a phone.

Call information displays on all phones that are sharing a line. If somebody turns on the privacy feature, you do not see
                              the outbound calls made from the phone. However, you see inbound calls to the shared line.

All phones with a shared line ring when a call is made to the line. If you place the shared call on hold, anyone can resume
                              the call by pressing the corresponding line key from a phone that shares the line. You can also press the Select button if the Resume icon is displayed.

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

You can configure each phone independently. Account information is usually the same for all IP phones, but settings such as
                              the dial plan or preferred codec information can vary.

### Configure a Shared Line

You can create a shared line by assigning the same directory number to different phones on the phone web page.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice .

Click the Ext_n tab of the extension that is shared.

Under General in the Line Enable list, choose Yes .

Under Share Line Appearance in the Share Ext list, select Shared .

If you set this extension to Private , the extension does not share calls, regardless of the Share Call Appearance setting on the Phone tab. If you set this extension
                                             to Shared , calls follow the Share Call Appearance setting on the Phone tab.

In the Shared User ID field , enter the user ID of the phone with the extension that is being shared.

In the Subscription Expires field, enter the number of seconds before the SIP subscription expires.  The default is 60 seconds.

Until the subscription expires, the phone gets NOTIFY messages from the SIP server on the status of the shared phone extension.

In the Restrict MWI field, set the message waiting indicator:

- Yes —Lights only for messages on private lines (SIP).

- No —Lights for all messages.

Under Proxy and Registration , enter the IP address of the proxy server in the Proxy field.

Under Subscriber Information, enter a Display Name and User ID (extension number) for the shared extension.

In the Phone tab, under Miscellaneous Line Key Settings , configure SCA Barge-In Enable:

- Yes —Allows users to take over the call on a shared line.

- No —Prevents users from taking over the call on a shared line.

Click Submit All Changes.

## Configure Voice Mail

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Under General , enter the Voice Mail Number .

Click Submit All Changes . The phone reboots.

### Configure Voice Mail for each Extension

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Extn .

Under Call Feature Settings , enter the Voice Mail Server .

(Optional) Enter the Voice Mail Subscribe Interval ; the expiration time in seconds, of a subscription to a voice mail server.

Click Submit All Changes .

The phone reboots.

### Configure the Message Waiting Indicator

You can configure the Message Waiting Indicator for separate extensions on the phone. The Message Waiting Indicator lights
                                 based on the presence of new voicemail messages in the mailbox.

You can  enable the indicator at the top of your IP phone to light when voice mail is left, or display a seeing message waiting
                                 notification.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Extn .

Under Call Feature Settings in the Message Waiting , choose Yes to enable.

## Assign a Ringtone to an Extension

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Ext(n) , where (n) is the number of an extension.

Under Call Feature Settings , use the Default Ring (n) drop-down list box to specify one of the following:

No Ring

Choose one of the available 12 ringtones.

Click Submit All Changes .

## Add Distinctive Ringtone

You can configure the characteristics of each ring tone using a ring tone script. When phone receives SIP Alert-INFO message
                              and the message format is correct, then the phone plays the specified ringtone. Otherwise, the phone plays the default ringtone.

In a ring tone script, assign a name for the ring tone and add the script to configure a distinctive ringtone in the format:

where:

n = ring-tone-name that identifies this ring tone. This name appears on the Ring Tone menu of the phone. The same name can
                                          be used in a SIP Alert-Info header in an inbound INVITE request to tell the phone to play the corresponding ring tone. The
                                          name should contain the same characters allowed in a URL only.

h = hint used to SIP Alert-INFO rule.

w = waveform-id-or-path which is the index of the desired waveform to use in this ring tone. The built-in waveforms are:

1 = Classic phone with mechanical bell

2 = Typical phone ring

3 = Classic ring tone

4 = Wide-band frequency sweep signal

You can also enter a network path (url) to download a ring tone data file from a server. Add the path in this format:

c = is the index of the desired cadence to play the given waveform. 8 cadences (1–8) as defined in <Cadence 1> through <Cadence
                                          8>. Cadence-id can be 0 If w=3,4, or an url. Setting c=0 implies the on-time is the natural length of the ring tone file.

b = break-time that specifies the number of seconds to break between two bursts of ring tone, such as b=2.5.

t = total-time that specifies the total number of seconds to play the ring tone before it times out.

## Configure the Audio Settings

The user can modify volume settings by pressing the volume control button on the phone, then pressing the Save softkey.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > User .

In the Audio Volume section, configure a volume level of 1 (quiet) through 10 (loudest):

Ringer Volume —Sets the ringer volume.

Speaker Volume —Sets the volume for the full-duplex speakerphone.

Headset Volume —Sets the headset volume.

Handset Volume —Sets the handset volume.

Click Submit All Changes .

### Specify Audio Compliance Standard

You can specify a compliance standard for the audio tuning for the phone. When a compliance standard is specified, the acoustic
                                 parameters that conform to the specified standard are loaded to the phone.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Go to Voice > User .

In the Audio Compliance section, choose an option from the Compliant Standard drop-down list as described in Audio Compliance .

Click Submit All Changes .

## User Access Control

The Cisco IP Phone respects only the “ua” user access attribute. For a specific parameter, the “ua” attribute defines access
                           by the user account to the administration web server. If the  “ua” attribute is not specified, the phone applies the  factory
                           default user access for the corresponding parameter. This attribute does not affect access by the admin account.

The value of the element attribute encloses within double quotes.

The “ua” attribute must have one of the following values:

na – no access

ro – read-only

rw – read/write

## Phone Web Server

The web server allows administrators and users to log in to the phone by using a phone web user interface. Administrators
                              and users have different privileges and see different options for the phone based on their role.

### Configure the Web Server from the Phone Screen Interface

Use this procedure to enable the phone web user interface from the phone screen.

Press Applications .

Select Network configuration > Web Server .

Select On to enable or Off to disable.

Press Set .

### Direct Action URL

If the Enable Direct Action URL
                                 setting is set to "Yes ", these Direct action URLs are
                                 accessible only for the admin. If Admin user is password protected,
                                 the client provides a login prompt before these are accessed.
                                 The Direct Action URLs are accessible via the phone web page via
                                 the path /admin/<direct_action> . The syntax is:

http[s]://<ip_or_hostname>/admin/<direct_action>[?<url>]

For example, http://10.1.1.1/admin/resync?http://server_path/config.xml

The following table provides a list of the different direct avtion URLs that are supported.

direct_action

Description

resync

Initiates a one-time resync of the config file specified by URL. The URL to resync is provided by appending ? followed by
                                             the URL. The URL specified here will not be saved anywhere in the phone settings.

Example

http://10.1.1.1/admin/resync?http://my_provision_server.com/cfg/device.cfg

upgrade

Initiates an upgrade of a phone to the specified load. The load is specified via the upgrade rule. the rule is specified by
                                             appending ? followed by URL path to the load. The upgrade rule specified is one time only and will not be saved in any property
                                             setting.

Example

http://10.1.1.1/admin/upgrade?http://my_upgrade_server.com/loads/sip88xx.11.0.0MP2.123.loads

updateca

Initiates a one-time install of the Custom Certificate Authority (Custom CA) specified by the URL. The URL to download is
                                             provided by appending ? followed by the URL. The URL specified here will not be saved anywhere in the phone settings.

Example

http://10.1.1.1/admin/updateca?http://my_cert_server.com/certs/myCompanyCA.pem

reboot

Initiates a reboot of the phone. Does not take any parameter with ?

Example

http://10.1.1.1/admin/reboot

cfg.xml

Downloads a snapshot of the phone configuration in XML format. The passwords are hidden for security. Most of the information
                                             here corresponds to the properties on the phone web page under Voice tab.

Example

http://10.1.1.1/admin/cfg.xml

status.xml

Downloads a snapshot of the phone status in XML format. Most of the information here corresponds to the Status tab in the phone web page.

Example

http://10.1.1.1/admin/status.xml

screendump.bmp

Downloads a screenshot of the phone LCD UI at the time when this action is initiated.

Example

http://10.1.1.1/admin/screendump.bmp

log.tar

Downloads a set of archived logs stored on the phone.

Example

http://10.1.1.1/admin/log.tar

### Enable Access to Phone Web Interface

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > System .

Under the System Configuration section, choose Yes from the Enable Web Server drop-down list box.

In the Enable Protocol drop-down list box, choose Http or Https.

In the Web Server Port field, enter the port to access the web server. The default is port 80 for HTTP or port 443 for HTTPS.

In the Enable Web Admin Access drop-down list box, you can enable or disable local access to the Admin Login of the phone web user interface. Defaults to Yes (enabled).

In the Admin Password field, enter a password if you want the system administrator to log in to the phone web user interface with a password. The
                                          password prompt appears when an administrator clicks Admin Login . The minimum  password length   can be 4 characters or the maximum password length is 127 characters.

In the User Password field, enter a password if you want users to log in to the phone web user interface with a password. The password prompt
                                          appears when users click User Login . The minimum  password length   can be 4 characters or the maximum password length is 127 characters.

Click Submit All Changes .

## XML Services

The phones provide support for XML services, such as an XML Directory Service or other XML applications. For XML services,
                              only HTTP and HTTPS support is available.

The following Cisco XML objects
                              are supported:

CiscoIPPhoneMenu

CiscoIPPhoneText

CiscoIPPhoneInput

CiscoIPPhoneDirectory

CiscoIPPhoneIconMenu

CiscoIPPhoneStatus

CiscoIPPhoneExecute

CiscoIPPhoneImage

CiscoIPPhoneImageFile

CiscoIPPhoneGraphicMenu

CiscoIPPhoneFileMenu

CiscoIPPhoneStatusFile

CiscoIPPhoneResponse

CiscoIPPhoneError

CiscoIPPhoneGraphicFileMenu

Init:CallHistory

Key:Headset

EditDial:n

The full list of supported URIs is contained in Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones , located here:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/products-programming-reference-guides-list.html

### XML Directory Service

When an XML URL requires authentication, use the parameters XML
                                    UserName and XML Password .

The parameter XML UserName in
                                 XML URL is replaced by $XML UserName.

For example:

The parameter
                                 XML UserName is cisco . The XML Directory Service URL
                                 is http://www.sipurash.compath?username=$XML_User_Name .

This results in the
                                 request URL: http://www.sipurash.com/path?username=cisco .

### XML Applications

When authentication is required for CGI/Execute URL via Post from
                                 an external application (for example, a web application) to the phones,
                                 the parameter CISCO XML EXE Auth Mode is used in 3 different
                                 scenarios:

Trusted—No authentication is performed (local user
                                       password is set or not). This is the default.

Local
                                       Credential—Authentication is based on digest authentication using
                                       the local user password, if the local user password is set. If not set, then no
                                       authentication is performed.

Remote Credential—Authentication is based on digest
                                       authentication using the remote username/password as set in the XML
                                       application on the web page (to access an XML application server).

### Macro Variables

You can use macro variables in XML URLs. The following macro variables are supported:

User ID—UID1, UID2 to UIDn

Display
                                       name—DISPLAYNAME1, DISPLAYNAME2 to DISPLAYNAMEn

Auth ID—AUTHID1,
                                       AUTHID2 to AUTHIDn

Proxy—PROXY1, PROXY2 to PROXYn

MAC Address using lowercase hex digits—MA

Product Name—PN

Product Series Number—PSN

Serial Number—SERIAL_NUMBER

The following table shows
                                 the list of macros supported on the phones:

Macro Name

Macro Expansion

$

The form $$ expands to a single $ character.

A through P

Replaced by general-purpose parameters GPP_A through GPP_P.

SA through SD

Replaced by special purpose parameters GPP_SA through GPP_SD.
                                             These parameters hold keys or passwords used in provisioning.

$SA through $SD are recognized as arguments to the optional
                                                         resync URL qualifier, --key.

MA

MAC address using lowercase hex digits (000e08aabbcc).

MAU

MAC address using uppercase hex digits (000E08AABBCC).

MAC

MAC address using lowercase hex digits with a colon to separate hex digit pairs (00:0e:08:aa:bb:cc).

PN

Product Name; for example, IP Phone 7861.

PSN

Product Series Number; for example, 7861.

SN

Serial Number string; for example, 88012BA01234.

CCERT

SSL Client Certificate status, installed or not installed.

IP

IP address of the phone within its local subnet; for example, 192.168.1.100.

EXTIP

External IP of the phone, as seen on the internet; for example, 66.43.16.52.

SWVER

Software version string; for example, 2.0.6(b). Use the software version string to compare against the current phone's firmware
                                             load, with one of the following methods:

With quotes, "$SWVER" –Variable acts as a string in firmware load name comparisons. For "$SWVER" eq "sip8845_65.1-0129-18-0356dev.loads" , the phone model number and load number are part of the comparison.

Without quotes, $SWVER –Variable is parsed to determine a build number, plus major, minor, and micro revision numbers. For example, when the sip88xx.11-1-1MSR-1dev.loads and sip8845_65.11-1-1MSR-1dev.loads firmware names are parsed, the result ignores the model number and load number. The result for both firmware names yields
                                                   a major revision= 1 , minor revision= 1 , micro revision= 1MSR , and build number= 1 .

HWVER

Hardware version string; for example, 1.88.1.

PRVST

Provisioning State (a numeric string):

-1 = explicit resync request

0 = power-up resync

1 = periodic resync

2 = resync failed, retry attempted

UPGST

Upgrade State (a numeric string):

1 = first upgrade attempt

2 = upgrade failed, retry attempt

UPGERR

Result message (ERR) of previous upgrade attempt; for example, http_get failed.

PRVTMR

Seconds since last resync attempt.

UPGTMR

Seconds since last upgrade attempt.

REGTMR1

Seconds since Line 1 lost registration with SIP server.

REGTMR2

Seconds since Line 2 lost registration with SIP server.

UPGCOND

Legacy macro name.

SCHEME

File access scheme (TFTP, HTTP, or HTTPS, obtained after parsing
                                             resync or upgrade URL).

METH

Deprecated alias for SCHEME, do not use.

SERV

Request target server hostname.

SERVIP

Request target server IP address (following DNS lookup).

PORT

Request target UDP/TCP port.

PATH

Request target file path.

ERR

Result message of resync or upgrade attempt.

UIDn

The contents of the Line n UserID configuration parameter.

ISCUST

If unit is customized, value=1, otherwise 0.

Customization status viewable on Web UI Info page.

INCOMINGNAME

Name associated with first connected, ringing, or inbound call.

REMOTENUMBER

Phone number of first connected, ringing, or inbound call. If there are multiple calls, the data associated with the first
                                             call found is provided.

DISPLAYNAMEn

The contents of the Line N Display Name configuration
                                             parameter.

AUTHIDn

The contents of the Line N auth ID configuration parameter.

### Configure a Phone to Connect to an XML Directory Service

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Enter this information:

XML Directory Service Name—Name of the XML Directory. Displays on
                                                   the user's phone as a directory choice.

XML Directory Service URL—URL where the XML Directory is located.

Click Submit All Changes .

#### Configure a Phone to Connect to an XML Application

##### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Enter this information:

XML Application Service Name—Name of the XML application. Displays on the user's phone as a menu item.

XML Application Service URL—URL where the XML application is
                                                      located.

If you configure an unused line button to connect to an XML
                                                application, the button connects to the URL configured above. If this is not what you want, you need to enter a different
                                                URL when you configure the line button.

Click Submit All Changes .

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under General , enter the phone name in the Station Display Name field. This name displays on the phone LCD in the top left corner. |
| Step 3 | Click Submit All Changes . |

| Step 1 | On the phone web page, select User Login > Voice > User . |
|---|---|
| Step 2 | In the Phone Background field of the Screen section, select any of the options as a phone wallpaper. Default : Phone does not have any wallpaper. If no wallpaper is added to the phone screen, the phone screen displays monochrome wallpaper. Logo : In the phone web page you can select Logo as your phone background option. The logo that you add in the Logo URL is used as the wallpaper. Caution Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . The logo display area is the center of the phone screen. The logo display area size of the phone is 128x128 pixels. If original
                                                   logo size does not fit display area, the logo scales to fit the display area. | Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
| Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
| Step 3 | Click Submit All Changes . |

| Caution | Do not exceed a maximum length of 255 characters for the Logo URL or Picture Download URL . |
|---|---|

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Screen section, select Logo from the Boot Display field. In the Logo URL field, enter a URL or path for the location where the logo image is saved. You can also download a picture and add it as a boot display: select Download Picture from the Boot Display field. In the Picture Download URL field, enter a URL or path for the location where the picture is saved. The logo must be a .jpg or a .png file. The phone has a fixed display area. So, if the original logo size doesn't fit into
                                             the display area, you need to scale it to fit the screen. For the Cisco IP Phone 7811, 7821, 7841 and 7861 the logo display
                                             area is at the mid-center of the phone screen. The display area size of the Cisco IP Phone 7811 is 48x48. The display area
                                             size of the Cisco IP Phone 7821, 7841, and 7861 is 64x64. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | Under Screen, select a setting for the Back Light Timer parameter. |
| Step 3 | In the LCD Contrast field, enter a number for the desired contrast. |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Miscellaneous Line Key Settings section, use the Call Appearances Per Line drop-down list box to specify the number of calls per line to allow. |
| Step 3 | Click Submit All Changes . |

| Note | The phone searches the XML directory using this format: directory_url?n=incoming_call_number . Example: For a multiplatform phone using a third-party service, the phone number (1234) search query has this format, http://your-service.com/dir.xml?n=1234 . |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Supplementary Services area, set the Reverse Phone Lookup Serv to: Yes –Enable the reverse name lookup feature. No –Disable the reverse name lookup feature. |
| Step 3 | Click Submit All Changes . |
| Step 4 | Alternative method is to use the config.xml file to provision the reverse name lookup feature. <Reverse_Phone_Lookup_Serv ua="na">Yes</Reverse_Phone_Lookup_Serv> |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under Supplementary Services , choose Yes for each of the transfer services that you want to enable: Attn Transfer Serv —Attended call transfer service. The user answers the call before transferring it. Blind Transfer Serv —Blind call transfer service. The user transfers the call without speaking to the caller. |
| Step 3 | To disable a transfer service, set the field to No . |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under Supplementary Services , choose Yes for each of the call forwarding services that you want to enable: Cfwd All Serv —Forwards all calls. Cfwd Busy Serv —Forwards calls only if the line is busy. Cfwd No Ans Serv —Forwards calls only if the line is not answered. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | Under Call Forward , choose Yes for CFWD Setting. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under Supplementary Services , choose Yes in the Conference Serv drop-down list box. |
| Step 3 | Click Submit All Changes . |

| Recording Mode in Server | Recording Softkeys Available on the Phone |
|---|---|
| Always | No softkeys available. Your user can't control recording from the phone. Recording starts automatically when a call is connected. |
| Always with Pause/Resume | PauseRec ResumeRec When a call is connected, recording starts automatically and your user can control the recording. |
| On Demand | Record PauseRec ResumeRec When a call is connected, recording starts automatically but the recording is not saved until the user presses the Record softkey. Your user sees a message when recording state changes. |
| On Demand with User Initiated Start | Record PauseRec StopRec ResumeRec The recording only starts when your user presses the Record softkey. Your user sees a message when recording state changes. |

| Icon | Meaning |
|---|---|
|  | Recording in progress. |
|  | Recording paused |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Supplementary Services section, click Yes or click No to enable or to disable call recording in the Call Recording Serv field. |
| Step 3 | (Optional) In the Programmable Softkeys section, to enable softkeys, add a string in this format in the Connected Key List and Conferencing Key List fields. crdstart;crdstop;crdpause;crdresume |
| Step 4 | In the phone web page, click the Ext(n) tab that requires call recording. |
| Step 5 | In the SIP Settings section, in the Call Recording Protocol , select SIPREC as the call recording protocol. For details on the SIP Settings fields, see SIP Settings . |
| Step 6 | Click Submit All Changes . |

| Icon | Meaning |
|---|---|
|  | Recording in progress. |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Supplementary Services section, click Yes or click No to enable or to disable call recording in the Call Recording Serv field. |
| Step 3 | (Optional) In the Programmable Softkeys section, to enable softkeys, add a string in this format in the Connected Key List and Conferencing Key List fields. crdstart;crdstop;crdpause;crdresume |
| Step 4 | In the phone web page, click the Ext(n) tab that requires call recording. |
| Step 5 | In the SIP Settings section, in the Call Recording Protocol , select SIPINFO as the call recording protocol. For details on SIP Settings fields, see SIP Settings . |
| Step 6 | Click Submit All Changes . |

| Step 1 | Select Voice > User . The user can select User Login > Voice > User . |
|---|---|
| Step 2 | Click Submit All Changes . |

| Step 1 | Choose Voice > User . |
|---|---|
| Step 2 | In the Supplementary Services area, select Yes in the DND Setting drop-down list. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Regional . |
|---|---|
| Step 2 | In the Vertical Service Activation Codes area, enter *78 in the DND Act Code field. |
| Step 3 | In the Vertical Service Activation Codes area, enter *79 in the DND Deact Code field. |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext(n) . |
|---|---|
| Step 2 | In the ACD Settings section, set up the fields as described in ACD Settings . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Broadsoft XMPP section, set the fields as described in Broadsoft XMPP . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice . |
|---|---|
| Step 2 | Click the Ext_n tab of the extension that is shared. |
| Step 3 | Under General in the Line Enable list, choose Yes . |
| Step 4 | Under Share Line Appearance in the Share Ext list, select Shared . If you set this extension to Private , the extension does not share calls, regardless of the Share Call Appearance setting on the Phone tab. If you set this extension
                                             to Shared , calls follow the Share Call Appearance setting on the Phone tab. |
| Step 5 | In the Shared User ID field , enter the user ID of the phone with the extension that is being shared. |
| Step 6 | In the Subscription Expires field, enter the number of seconds before the SIP subscription expires.  The default is 60 seconds. Until the subscription expires, the phone gets NOTIFY messages from the SIP server on the status of the shared phone extension. |
| Step 7 | In the Restrict MWI field, set the message waiting indicator: Yes —Lights only for messages on private lines (SIP). No —Lights for all messages. |
| Step 8 | Under Proxy and Registration , enter the IP address of the proxy server in the Proxy field. |
| Step 9 | Under Subscriber Information, enter a Display Name and User ID (extension number) for the shared extension. |
| Step 10 | In the Phone tab, under Miscellaneous Line Key Settings , configure SCA Barge-In Enable: Yes —Allows users to take over the call on a shared line. No —Prevents users from taking over the call on a shared line. |
| Step 11 | Click Submit All Changes. |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under General , enter the Voice Mail Number . |
| Step 3 | Click Submit All Changes . The phone reboots. |

| Step 1 | Select Voice > Extn . |
|---|---|
| Step 2 | Under Call Feature Settings , enter the Voice Mail Server . |
| Step 3 | (Optional) Enter the Voice Mail Subscribe Interval ; the expiration time in seconds, of a subscription to a voice mail server. |
| Step 4 | Click Submit All Changes . The phone reboots. |

| Step 1 | Select Voice > Extn . |
|---|---|
| Step 2 | Under Call Feature Settings in the Message Waiting , choose Yes to enable. |

| Step 1 | Select Voice > Ext(n) , where (n) is the number of an extension. |
|---|---|
| Step 2 | Under Call Feature Settings , use the Default Ring (n) drop-down list box to specify one of the following: No Ring Choose one of the available 12 ringtones. |
| Step 3 | Click Submit All Changes . |

| In a ring tone script, assign a name for the ring tone and add the script to configure a distinctive ringtone in the format: n=ring-tone-name;h=hint;w=waveform-id-or-path;c=cadence-id;b=break-time;t=total-time where: n = ring-tone-name that identifies this ring tone. This name appears on the Ring Tone menu of the phone. The same name can
                                          be used in a SIP Alert-Info header in an inbound INVITE request to tell the phone to play the corresponding ring tone. The
                                          name should contain the same characters allowed in a URL only. h = hint used to SIP Alert-INFO rule. w = waveform-id-or-path which is the index of the desired waveform to use in this ring tone. The built-in waveforms are: 1 = Classic phone with mechanical bell 2 = Typical phone ring 3 = Classic ring tone 4 = Wide-band frequency sweep signal You can also enter a network path (url) to download a ring tone data file from a server. Add the path in this format: w=[tftp://]hostname[:port]/path c = is the index of the desired cadence to play the given waveform. 8 cadences (1–8) as defined in <Cadence 1> through <Cadence
                                          8>. Cadence-id can be 0 If w=3,4, or an url. Setting c=0 implies the on-time is the natural length of the ring tone file. b = break-time that specifies the number of seconds to break between two bursts of ring tone, such as b=2.5. t = total-time that specifies the total number of seconds to play the ring tone before it times out. |
|---|

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Audio Volume section, configure a volume level of 1 (quiet) through 10 (loudest): Ringer Volume —Sets the ringer volume. Speaker Volume —Sets the volume for the full-duplex speakerphone. Headset Volume —Sets the headset volume. Handset Volume —Sets the handset volume. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Go to Voice > User . |
|---|---|
| Step 2 | In the Audio Compliance section, choose an option from the Compliant Standard drop-down list as described in Audio Compliance . |
| Step 3 | Click Submit All Changes . |

| Note | The value of the element attribute encloses within double quotes. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Network configuration > Web Server . |
| Step 3 | Select On to enable or Off to disable. |
| Step 4 | Press Set . |

| direct_action | Description |
|---|---|
| resync | Initiates a one-time resync of the config file specified by URL. The URL to resync is provided by appending ? followed by
                                             the URL. The URL specified here will not be saved anywhere in the phone settings. Example http://10.1.1.1/admin/resync?http://my_provision_server.com/cfg/device.cfg |
| upgrade | Initiates an upgrade of a phone to the specified load. The load is specified via the upgrade rule. the rule is specified by
                                             appending ? followed by URL path to the load. The upgrade rule specified is one time only and will not be saved in any property
                                             setting. Example http://10.1.1.1/admin/upgrade?http://my_upgrade_server.com/loads/sip88xx.11.0.0MP2.123.loads |
| updateca | Initiates a one-time install of the Custom Certificate Authority (Custom CA) specified by the URL. The URL to download is
                                             provided by appending ? followed by the URL. The URL specified here will not be saved anywhere in the phone settings. Example http://10.1.1.1/admin/updateca?http://my_cert_server.com/certs/myCompanyCA.pem |
| reboot | Initiates a reboot of the phone. Does not take any parameter with ? Example http://10.1.1.1/admin/reboot |
| cfg.xml | Downloads a snapshot of the phone configuration in XML format. The passwords are hidden for security. Most of the information
                                             here corresponds to the properties on the phone web page under Voice tab. Example http://10.1.1.1/admin/cfg.xml |
| status.xml | Downloads a snapshot of the phone status in XML format. Most of the information here corresponds to the Status tab in the phone web page. Example http://10.1.1.1/admin/status.xml |
| screendump.bmp | Downloads a screenshot of the phone LCD UI at the time when this action is initiated. Example http://10.1.1.1/admin/screendump.bmp |
| log.tar | Downloads a set of archived logs stored on the phone. Example http://10.1.1.1/admin/log.tar |

| Step 1 | Select Voice > System . |
|---|---|
| Step 2 | Under the System Configuration section, choose Yes from the Enable Web Server drop-down list box. |
| Step 3 | In the Enable Protocol drop-down list box, choose Http or Https. |
| Step 4 | In the Web Server Port field, enter the port to access the web server. The default is port 80 for HTTP or port 443 for HTTPS. |
| Step 5 | In the Enable Web Admin Access drop-down list box, you can enable or disable local access to the Admin Login of the phone web user interface. Defaults to Yes (enabled). |
| Step 6 | In the Admin Password field, enter a password if you want the system administrator to log in to the phone web user interface with a password. The
                                          password prompt appears when an administrator clicks Admin Login . The minimum  password length   can be 4 characters or the maximum password length is 127 characters. Note The password can contain any character except the Space key. | Note | The password can contain any character except the Space key. |
| Note | The password can contain any character except the Space key. |
| Step 7 | In the User Password field, enter a password if you want users to log in to the phone web user interface with a password. The password prompt
                                          appears when users click User Login . The minimum  password length   can be 4 characters or the maximum password length is 127 characters. Note The password can contain any character except the Space key. | Note | The password can contain any character except the Space key. |
| Note | The password can contain any character except the Space key. |
| Step 8 | Click Submit All Changes . |

| Note | The password can contain any character except the Space key. |
|---|---|

| Note | The password can contain any character except the Space key. |
|---|---|

| Macro Name | Macro Expansion |
|---|---|
| $ | The form $$ expands to a single $ character. |
| A through P | Replaced by general-purpose parameters GPP_A through GPP_P. |
| SA through SD | Replaced by special purpose parameters GPP_SA through GPP_SD.
                                             These parameters hold keys or passwords used in provisioning. Note $SA through $SD are recognized as arguments to the optional
                                                         resync URL qualifier, --key. | Note | $SA through $SD are recognized as arguments to the optional
                                                         resync URL qualifier, --key. |
| Note | $SA through $SD are recognized as arguments to the optional
                                                         resync URL qualifier, --key. |
| MA | MAC address using lowercase hex digits (000e08aabbcc). |
| MAU | MAC address using uppercase hex digits (000E08AABBCC). |
| MAC | MAC address using lowercase hex digits with a colon to separate hex digit pairs (00:0e:08:aa:bb:cc). |
| PN | Product Name; for example, IP Phone 7861. |
| PSN | Product Series Number; for example, 7861. |
| SN | Serial Number string; for example, 88012BA01234. |
| CCERT | SSL Client Certificate status, installed or not installed. |
| IP | IP address of the phone within its local subnet; for example, 192.168.1.100. |
| EXTIP | External IP of the phone, as seen on the internet; for example, 66.43.16.52. |
| SWVER | Software version string; for example, 2.0.6(b). Use the software version string to compare against the current phone's firmware
                                             load, with one of the following methods: With quotes, "$SWVER" –Variable acts as a string in firmware load name comparisons. For "$SWVER" eq "sip8845_65.1-0129-18-0356dev.loads" , the phone model number and load number are part of the comparison. Without quotes, $SWVER –Variable is parsed to determine a build number, plus major, minor, and micro revision numbers. For example, when the sip88xx.11-1-1MSR-1dev.loads and sip8845_65.11-1-1MSR-1dev.loads firmware names are parsed, the result ignores the model number and load number. The result for both firmware names yields
                                                   a major revision= 1 , minor revision= 1 , micro revision= 1MSR , and build number= 1 . |
| HWVER | Hardware version string; for example, 1.88.1. |
| PRVST | Provisioning State (a numeric string): -1 = explicit resync request 0 = power-up resync 1 = periodic resync 2 = resync failed, retry attempted |
| UPGST | Upgrade State (a numeric string): 1 = first upgrade attempt 2 = upgrade failed, retry attempt |
| UPGERR | Result message (ERR) of previous upgrade attempt; for example, http_get failed. |
| PRVTMR | Seconds since last resync attempt. |
| UPGTMR | Seconds since last upgrade attempt. |
| REGTMR1 | Seconds since Line 1 lost registration with SIP server. |
| REGTMR2 | Seconds since Line 2 lost registration with SIP server. |
| UPGCOND | Legacy macro name. |
| SCHEME | File access scheme (TFTP, HTTP, or HTTPS, obtained after parsing
                                             resync or upgrade URL). |
| METH | Deprecated alias for SCHEME, do not use. |
| SERV | Request target server hostname. |
| SERVIP | Request target server IP address (following DNS lookup). |
| PORT | Request target UDP/TCP port. |
| PATH | Request target file path. |
| ERR | Result message of resync or upgrade attempt. |
| UIDn | The contents of the Line n UserID configuration parameter. |
| ISCUST | If unit is customized, value=1, otherwise 0. Note Customization status viewable on Web UI Info page. | Note | Customization status viewable on Web UI Info page. |
| Note | Customization status viewable on Web UI Info page. |
| INCOMINGNAME | Name associated with first connected, ringing, or inbound call. |
| REMOTENUMBER | Phone number of first connected, ringing, or inbound call. If there are multiple calls, the data associated with the first
                                             call found is provided. |
| DISPLAYNAMEn | The contents of the Line N Display Name configuration
                                             parameter. |
| AUTHIDn | The contents of the Line N auth ID configuration parameter. |

| Note | $SA through $SD are recognized as arguments to the optional
                                                         resync URL qualifier, --key. |
|---|---|

| Note | Customization status viewable on Web UI Info page. |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Enter this information: XML Directory Service Name—Name of the XML Directory. Displays on
                                                   the user's phone as a directory choice. XML Directory Service URL—URL where the XML Directory is located. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Enter this information: XML Application Service Name—Name of the XML application. Displays on the user's phone as a menu item. XML Application Service URL—URL where the XML application is
                                                      located. If you configure an unused line button to connect to an XML
                                                application, the button connects to the URL configured above. If this is not what you want, you need to enter a different
                                                URL when you configure the line button. |
| Step 3 | Click Submit All Changes . |