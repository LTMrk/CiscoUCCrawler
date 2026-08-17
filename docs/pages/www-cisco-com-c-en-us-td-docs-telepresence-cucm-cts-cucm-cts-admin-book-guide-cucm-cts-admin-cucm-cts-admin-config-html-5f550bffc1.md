---
doc_id: www-cisco-com-c-en-us-td-docs-telepresence-cucm-cts-cucm-cts-admin-book-guide-cucm-cts-admin-cucm-cts-admin-config-html-5f550bffc1
source_url: https://www.cisco.com/c/en/us/td/docs/telepresence/cucm_cts/cucm_cts_admin_book/guide/cucm_cts_admin/cucm_cts_admin_config.html
retrieved_at: 2026-08-17T00:09:51.399886+00:00
---

Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

# Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

Updated: April 15, 2014

Chapter: Configuring Cisco Unified Communications Manager for the Cisco TelePresence System

## Chapter: Configuring Cisco Unified Communications Manager for the Cisco TelePresence System

Revised: June 9, 2015, OL-21851-01

## Contents

This chapter explains how to download the Cisco TelePresence Administration Software from the cisco.com web site and configure a new device using the Cisco Unified Communications Manager web interface, and includes the following sections:

## Adding a Cisco TelePresence Image to the Cisco Unified Communications Manager Server

This section describes the steps you take to add a new Cisco TelePresence Device to Cisco Unified Communications Manager (Unified CM) and includes the following topics:

### Downloading the Cisco TelePresence Software

Note Complete these steps prior to using your Cisco TelePresence Touch 12 device.

If you have not yet installed the Cisco TelePresence software onto the Unified CM server, complete the following steps to add it:

Note If you already downloaded the software and added it to the Unified CM server, skip this section and continue to the “Adding a Cisco TelePresence Device to the Unified CM Server” section to add a new device to Unified CM.

Step 1	Navigate to www.cisco.com .

Step 2	Click on the Log In button, then enter your username and password.

Step 3	Click Support .

Step 4	Enter the following search term into the text box:

cisco telepresence administration software

Step 5	Click the Cisco TelePresence Administration Software hyperlink that displays.

Alternatively, you can click the Downloads tab and enter the name of your system into the text box.

Step 6	Click the Download Software hyperlink.

Step 7	Navigate to your product using the navigation tool that displays.

Step 8	Select the software that you require for your installation.

Systems that use a Cisco TelePresence Touch device for call control only require the Cisco TelePresence System and Cisco TelePresence Touch file. Systems that use a Cisco Unified IP phone for call control require the Cisco TelePresence System and the Cisco TelePresence Midlet Phone Application .jad and .jar files.

Step 9	Choose the latest release and click either Add to Cart or Download.

a.	If you choose Add to Cart, click on Download Cart.

b.	If you choose Download, click Accept License Agreement.

Step 10	Click Download and then Accept License Agreement, and follow the prompts to download the file.

Note For systems that use a Cisco TelePresence Touch device, the software to run the Touch device is included with the COP file. For systems that use a Cisco Unified IP phone for call control, the latest MIDlets software version is included with the Unified CM device pack. For more information about the files for systems that use a Cisco TelePresence Touch device, see the “Understanding COP Files” section .

Step 11	Copy these files to a Secure File Transfer Protocol (SFTP) server that is accessible by Unified CM.

Step 12	Load the system image onto the Unified CM server by completing the following steps:

a.	Open a supported web browser.

Note The Cisco Unified CM Administration program requires Internet Explorer version 6, 7, 8 or 9 or Firefox version 3.6, 5 or 9.

b.	In the address bar of the web browser, enter the following URL:

https:// UCM-server-name

Where

UCM-server-name

is the IP address or DNS name of the Cisco Unified Communications Manager server.

c.	Upload the Cisco TelePresence system image to the Unified CM server by completing the steps in the Installing the Cisco TelePresence COP File to the Unified CM Server section that follows.

### Installing the Cisco TelePresence COP File to the Unified CM Server

To install the Cisco TelePresence system files to the Unified CM server, complete the following steps.

Step 13 Log in to the Unified CM administrative GUI.

Step 14	From the Navigation drop-down list, on the top right of the GUI, select Cisco Unified OS Administration . Click Go to go to the Cisco Unified CM Administration home page.

The Cisco Unified Operation System Administration screen displays.

Note Log in with your username and password if prompted to do so.

Step 15	Navigate to Software Upgrades > Install/Upgrade .

Figure 1-1	Cisco Unified Operating System Administration Screen

Step 16	In the Software Location area, specify the following information in the fields:

- In the Source drop-down list, select Remote Filesystem .

- In the Directory field, enter the location of the file on the SFTP server.

- In the Server field, enter the server name or IP address.

- In the User Name and User Password fields, enter the user name and password used to access the SFTP server.

- In the Transfer Protocol drop-down list, select SFTP .

Figure 1-2	Specifying SFTP Server and File Location

Step 17	Click Next .

Unified CM accesses the SFTP server. The Software Location area lists the COP files that Unified CM finds in the directory that you specified.

Step 18 Choose the COP file that you want to install from the available file names in the Options/Upgrades drop-down list.

Figure 1-3	Specifying the COP File

Step 19 Click Next .

The Unified CM GUI shows the COP file being installed.

Figure 1-4	COP File Installation

Step 20	After installation completes, verify the file validity by completing the following steps:

a.	Make a note of the information in the File Checksum Details area. This value is shown in Figure 1-5 .

b.	Log in to the SFTP server and enter the following command:

c. md5sum filename .cop.sgn

where:

filename is the file name of the COP file on the SFTP server.

d.	Make a note of the checksum value that displays as a result of the md5sum command.

e.	Compare the MD5 Hash Value that displays in this area to the MD5 checksum value that you find in the COP file on the server and make sure that they match to ensure that the file is not corrupted.

f.	If the values match, continue to the next step; if the values do not match, retry the file installation.

Figure 1-5 File Checksum Details Area

Step 21	Click Next to begin installation.

The installation log displays the installation progress.

After the .loads, codec and Touch 12 files are extracted, the interface displays a status of Complete in the Installation Status area.

Figure 1-6	Installation Status Area

Step 22	From the Navigation drop-down list on the top right of the GUI, select Cisco Unified Serviceability and click Go .

The Cisco Unified Serviceability window displays.

Note Enter your user ID and password if prompted to do so.

Step 23 Restart the TFTP server by completing the following steps:

a.	Navigate to Tools > Control Center - Feature Services .

Figure 1-7	Cisco Unified Serviceability Window

b.	Choose the correct TFTP server from the drop-down list that displays and click Go .

c.	In the CM Services area click the Cisco Tftp radio button.

d.	Click the Restart button (either the Restart button on the bottom of the page or the button circled in red in Figure 1-8 ).

Figure 1-8 Restart Button in Features Services Page

Step 24	Add the Cisco TelePresence device to the Unified CM server by completing the steps in the “Adding a Cisco TelePresence Device to the Unified CM Server” section

## Configuring Phone Security Profile Information

This section describes how to create and configure a phone security profile for a Cisco TelePresence device using Unified CM. This section contains the following tasks:

### Adding a New Phone Security Profile for CTS

To add a new phone security profile for CTS:

Step 1	Log in to the Cisco Unified CM Administration interface.

Step 2	Choose System > Security Profile and click Phone Security Profile .

Step 3	Click the Add New button at the bottom of the window. The Phone Security Profile Configuration window appears.

Step 4	From the Phone Security Profile Type drop-down menu, choose the phone type .

Step 5	Click Next .

Step 6	From the Select the phone security profile protocol drop-down menu, choose SIP .

Step 7	Click Next . The Phone Security Profile Configuration window appears containing your Product Type and Device Protocol selections.

Step 8	Proceed to Configuring the Phone Security Profile to complete the remaining tasks on the Phone Security Profile Configuration page.

### Configuring the Phone Security Profile

Before You Begin

In the Phone Security Profile Configuration window, verify your Product Type and Device Protocol settings:

- Phone Type—select your Cisco TelePresence system in the drop-down list

- Device Protocol—SIP

Proceed to the following configuration tasks:

### SIP Phone Security Profile Information

If you chose SIP as the device protocol:

Step 1	From the Cisco Unified CM Administration interface, Choose System > Security Profile and click Phone Security Profile .

Step 2	Search for a Phone Security Profile using the search features or follow the steps in Adding a New Phone Security Profile for CTS .

Step 3	Enter configuration information on the Phone Security Profile Information page using the information in Table 1-1 as a guide.

Step 4	Click the Save button to save your settings.

Table 1-1 SIP Phone Security Profile Information Fields

Field

Required

Setting

Name

Yes

Enter a name for the security profile.

When you save the new profile, the name displays in the Device Security Profile drop-down list box in the Phone Configuration window for the phone type and protocol.

Tip	Include the device model and protocol in the security profile name to help you find the correct profile when you are searching for or updating a profile.

Description

—

Enter a description for the security profile.

Nonce Validity Time

Yes

Enter the number of minutes (in seconds) that the nonce value is valid. The default value equals 600 (10 minutes). When the time expires, Cisco Unified CM generates a new value.

Device Security Mode

Yes

Choose Encrypted from the drop-down menu (recommended).

Encrypted mode allows Cisco Unified CM to provide integrity, authentication, and encryption for the phone. A TLS connection that uses AES128/SHA opens for signaling, and SRTP carries the media for all phone calls on all SRTP-capable SIP hops.

Note The Media is Encrypted icon (closed lock) is displayed on the screen only when the Device Security mode is set to encrypted and cluster security mode is set to 1 ( mixed mode ).

To configure and verify cluster security mode, see the Verifying the Cisco Unified Communications Manager Security Mode section of the Cisco TelePresence Security Solutions Guide .

Additional Device Security Mode field choices:

- Non Secure—No security features except image authentication exist for the phone. A TCP connection opens to Cisco Unified CM.

- Authenticated—Cisco Unified CM provides integrity and authentication for the phone. A TLS connection that uses NULL/SHA opens.

Transport Type

Yes

When Device Security Mode is Non Secure, choose one of the following options from the drop-down list box (not all options may display):

- TCP—Choose the Transmission Control Protocol to ensure that packets get received in the same order they are sent. This protocol ensures that no packets get dropped, but the protocol does not provide any security.

- UDP—Choose the User Datagram Protocol to ensure that packets are received quickly. This protocol, which can drop packets, does not ensure that packets are received in the order that they are sent. This protocol does not provide any security.

- TCP + UDP—Choose this option if you want to use a combination of TCP and UDP. This option does not provide any security.

When Device Security Mode is Authenticated or Encrypted, TLS specifies the Transport Type. TLS provides signaling integrity, device authentication, and signaling encryption (encrypted mode only) for SIP phones.

Note If Device Security Mode cannot be configured in the profile, the transport type specifies UDP.

Enable Digest Authentication

—

Not supported on CTS devices. Leave this box unchecked.

TFTP Encrypted Config

—

When this box is checked, Cisco Unified CM encrypts phone downloads from the TFTP server. This option exists for Cisco phones only.

Tip	Cisco recommends that you enable this option and configure a symmetric key to secure digest credentials and administrative passwords.

Exclude Digest Credentials in Configuration File

—

When this box is checked, Cisco Unified CM omits digest credentials in phone downloads from the TFTP server. This option exists for Cisco Unified IP SIP Phone models 7905, 7912, 7940, and 7960 only.

### Phone Security Profile CAPF Information

To configure the Phone Security Profile CAPF Information fields:

Step 1	Enter Phone Security Profile CAPF Information using the information in Table 1-2 as a guide.

Step 2	Click the Save button to save your settings.

Table 1-2 Phone Security Profile CAPF Information

Field

Required

Setting

Authentication Mode

Yes

Choices are:

- By Null String

- By Existing Certificate (precedence to LSC)

- By Existing Certificate (precedence to MIC)

Key Size (Bits)

Yes

Choices are:

- 512

- 1024

- 2048

Note These fields are related to the CAPF Information settings on the Phone Configuration page.

### Parameters Used in Phone Field

To configure the Parameters Used in Phone Field:

Step 1	Enter the SIP Phone Port information using the information in Table 1-3 as a guide.

Step 2	Click the Save button to save your settings.

Table 1-3 Parameters Used in Phone Field

Field

Required

Setting

SIP Phone Port

Yes

This setting applies to SIP phones that are using UDP transport.

Enter the port number for Cisco Unified SIP IP Phones that are using UDP to listen for SIP messages from Cisco Unified CM. The default setting equals 5060.

Phones that are using TCP or TLS ignore this setting.

## Adding a Cisco TelePresence Device to the Unified CM Server

Note Before you begin this procedure, note the MAC address of the Cisco TelePresence device. See the “Before You Begin” section for information about determining the MAC address.

This section includes the steps you take to add a new Cisco TelePresence device to the Unified CM server and includes the following steps:

### Using the Unified CM GUI to Add a Cisco TelePresence Device

To add a new Cisco TelePresence device to the Unified CM server, complete the following steps.

Step 1	Log in to the Cisco Unified CM Administration interface.

Step 2	If required, choose the Cisco Unified CM Administration drop-down choice and click Go .

Step 3	From the Device drop-down menu, choose Phone. The Find and List Phones Page appears.

Step 4	Click the Add New button at the bottom of the window. The Add a New Phone window appears.

Step 5	In the Add a New Phone window, click the Phone Type drop-down list and choose Cisco TelePresence system that corresponds with your device.

You added this phone type when you downloaded and applied the Cisco TelePresence file in the “Installing the Cisco TelePresence COP File to the Unified CM Server” section ,

Step 6	Click Next to display the Phone Configuration window.

Step 7	Fill out the fields in the Phone Configuration window. Refer to Table 1-4 through Table 1-14 for a description of these fields.

Step 8	When you have finished making your changes, click Save to save your settings.

### Device Information Area

Table 1-4 provides you with a description of the fields in the Device Information Area.

Note Fields marked with an asterisk ( * ) in the administration interface are required entries.

Table 1-4 Fields in the Device Information Area

Field

Setting

Registration

Read-only. Indicates whether the system is Registered with Cisco Unified Communications Manager and lists the registered Unified CM address.

IP Address

IP address for the Cisco TelePresence System.

After you add the device, you can click on the address to see information for that phone in a new window.

Active Load ID

View-only field showing the status of the active load.

Device is Active check box

View only field.

Device is Trusted check box

View only field.

MAC Address*

MAC address for the Cisco TelePresence primary codec. For example, 000DD12345A1.

Description

Short, free-format description of the device.

Device Pool*

Your device pools. Choose a device pool from the drop-down menu.

Click View Details to open the Device Details window, which includes the following system setting information:

- Device Pool Settings

- Roaming Sensitive Settings

- Device Mobility Related Information

- Geolocation Configuration

- Incoming Calling Party Settings

- Incoming Called Party Settings

Common Device Configuration

Your configured devices. Leave field as < None> .

Click View Details to open t he Common Device Configuration Detail wi ndow, which includes the following system setting information:

- Common Device Configuration Information

- Multilevel Precedence and Preemption Information

Phone Button Template*

Standard_Cisco_TelePresence.

Note Unless you have created extra button templates, you will see the default button template for your device.

Softkey Template (systems that use a Cisco Unified IP Phone for call control only)

<None>

Note This field is only for systems that use a Cisco Unified IP Phone for call control.

Common Phone Profile*

Standard Common Phone Profile.

Calling Search Space

<None>

Note Information in this field reflects Calling Search Spaces that have been created on this Unified CM.

Media Resource Group List

<None>

Location*

Hub_None.

Additional choice is Phantom.

User Locale

<None>

Note This field supports user locales listed in Table 2-4 .

Network Locale

<None>

Note This field supports network locales listed in Table 2-4 .

Device Mobility Mode*

Default.

Click View Current Device Mobility Settings to open the Device Mobility Details window, which shows the current device mobility settings.

Owner User ID

Saved User IDs. Leave field as <None>.

Phone Load Name

Specify required version of Cisco TelePresence System if no device default is set.

Use Trusted Relay Point*

Default.

Always Use Prime Line*

Default.

Always Use Prime Line for Voice Message*

Default.

Calling Party Transformation CSS

<None>

Geolocation

<None>

Check-Boxes in the Device Information Area

Use Device Pool Calling Party Transformation CSS

Box is checked.

Retry Video Call as Audio

Box is checked.

Ignore Presentation Indicators

Box is un-checked.

Allow Control of Device from CTI

Box is checked.

Logged Into Hunt Group

Box is checked.

Remote Device

Box is un-checked.

Note When you are finished making changes, click Save to save your settings.

### Protocol-Specific Information Area

Table 1-5 provides you with a description of the fields in the Protocol-Specific Information area.

Note Fields marked with an asterisk ( * ) in the administration interface are required entries for basic configuration.

Table 1-5 Fields in the Protocol-Specific Information Area

Field

Setting

Packet Capture Mode*

<None>

Packet Capture Duration

0

Presence Group*

Standard Presence Group

SIP Dial Rules

<None>

MTP Preferred Originating Codec*

711ulaw (default).

Device Security Profile*

Cisco TelePresence name of system - Standard SIP Non-Secure Profile (default)

Note For more information about configuring Cisco Unified CM security features, refer to the Cisco Unified Communications Manager Security Guide, Release 7.1(2) .

Rerouting Calling Search Space

<None>

Note Information in this field reflects Calling Search Spaces that have been created on this Unified CM.

SUBSCRIBE Calling Search Space*

<None>

Note Information in this field reflects Calling Search Spaces that have been created on this Unified CM.

SIP Profile*

Choose Standard SIP Profile .

Information in this field reflects SIP profiles that have been created on this Unified CM.

Digest User

<None>

Check-Boxes

Media Termination point Required

Box is un-checked.

Unattended Port

Box is un-checked.

Allow Presentation Sharing using BFCP

Box is checked.

Note When you are finished making changes, click Save to save your settings.

### Certification Authority Proxy Function (CAPF) Information Area

Table 1-6 describes the fields in the Certification Authority Proxy Function (CAPF) Information area.

Note This option will not be visible unless you have enabled CAPF on the Cisco Unified Communications Manager service parameter. The Security Profile contains additional CAPF settings. For more information about CAPF, refer to the Securing Cisco TelePresence Products document for your software release, available at the following URL: http://www.cisco.com/en/US/partner/products/ps8332/ products_installation_and_configuration_guides_list.html

Note Fields marked with an asterisk ( * ) in the administration interface are required entries for basic configuration.

Table 1-6 Fields in the Certification Authority Proxy Function (CAPF) Information Area

Field

Required?

Setting

Certificate Operation*

Yes

No Pending Operation. Most configuration fields in the CAPF Information window cannot be modified.

Note The drop-down menu allows you to Install/Upgrade, Delete, or Troubleshoot. If you choose one of these options, the remaining fields in the CAPF Information window can be modified.

Authentication Mode*

Yes

If No Pending Operation is chosen in the Certificate Operation field, this field is view only by default.

Authentication String

—

Leave this field unchanged.

Key Size (Bits)*

Yes

If No Pending Operation is chosen in the Certificate Operation field, this field is view only by default.

Operation Completes By

—

If No Pending Operation is chosen in the Certificate Operation field, this field is view only by default.

Certificate Operation Status

—

<None>

Note When you are finished making changes, click Save to save your settings.

### MLPP Information Area

In the MLPP Information area, leave the MLPP Domain field at the default of <None>.

### Product Specific Configuration Layout Area

Table 1-7 contains descriptions of the Product Specific Configuration Layout information fields.

Note Fields marked with an asterisk ( * ) in the administration interface are required entries for basic configuration.

Note Not all choices are available for all devices; some choices are product-specific.

For more information about these fields, see the “Product Specific Configuration Layout” section .

Table 1-7 Fields in the Product Specific Configuration Layout Area

Field

Description

Cisco TelePresence Type*

Indicates the type of Cisco TelePresence system you have installed.

Admin. Web Access*

When enabled, allows access to the Cisco TelePresence Web Administration interface.

Default is Enabled

Room Name

Conference room name as described in Microsoft Exchange or Domino. Used to schedule conference calls. This field accepts a text string with a maximum of 64 characters.

Note If you have the Cisco TelePresence Manager application, the name of the conference room is required. The name must exactly match the resource mailbox (including domain name) as it is entered in the Microsoft Exchange or Domino database. It will be used to schedule conference calls.

Maximum Call Duration (in minutes)

Maximum duration (in minutes) allowed for a Cisco TelePresence conference call.

- Minimum is 0

- Maximum is 10080 (7 days).

- Default is 0 (no call duration set). The default setting disables this feature.

Note This feature is coordinated with the Maximum Call Duration Timer in the Cisco Unified Communications Manager service parameters. If values other than 0 are entered for either of these fields, the smaller value takes precedence.

Quality (per Display)*

Bandwidth used by the system. Higher bandwidth increases video quality, but may also cause packets to be dropped and video to be interrupted.

Choices are:

- Highest Detail, Best Motion: 1080p (default)

- Highest Detail, Better Motion: 1080p

- Highest Detail, Good Motion: 1080p

- High Detail, Best Motion: 720p

- High Detail, Better Motion: 720p

- High Detail, Good Motion: 720p

- High Detail, Limited Motion: 720p (Lite)

If your system uses a Cisco Unified IP Phone for call control, note the following caveats for the 720p (Lite) choice:

–	The audio addin conf softkey is not available.

–	You must have MIDlets installed on the Unified CM.

- Network friendly for personal systems: 480p

For more information about 720p (Lite), see Quality Per Display - 720p (Lite) .

Note Limited bandwidth mode: 360p may be listed as an option in this field but is not yet available; it is supported in a future release.

Bandwidth Allocation Weights*

Sets the bandwidth allocation ratio between conference video and presentation video. Default value of this parameter is a weight of 8 for main video and a weight of 2 for presentation video for a total weight of 10.

Choices are:

- 9 Main / 1 Presentation

- 8 Main / 2 Presentation (default)

- 6 Main / 4 Presentation

- 4 Main / 6 Presentation

- 3 Main / 7 Presentation

See also the TX Software Features chapter of the Administration Guide for Cisco TelePresence TX Software Release 6.0 .

Main Display Frames Per Second* (TX13x0 and TX9x00 systems only)*

Selects the frame rate, or frames per second (fps), on the main display screen. Choice are:

- 30 fps main

- 60 fps main

Presentation Input Device*

Indicates whether you have a presentation input device. Choices are:

- None (default)

- Document Camera

Note This parameter must correctly reflect how your system is configured. Any discrepancy will cause CTS to function improperly.

Presentation Output Device*

Indicates if you have a presentation output device. Choices are:

- None (default)

- Projector/Display

Note This parameter must correctly reflect how your system is configured. Any discrepancy will cause CTS to function improperly.

Lights*

Defines how the lights operate in a CTS conference room. Choices are:

- On with calls only (default)

- On with display settings

- On all the time

Note On the CTS 500, the lights are powered by the display. When the display turns off according to the display settings in Unified CM, the lights also turn off. However, if you have chosen the “On all the time” setting for the lights, the setting is not honored during power saving/non-business hours (when display settings are not active). To bypass power saving/non-business hours defaults, extend the business hours to all the time in the Display On Duration field.

See also Notes About Auxiliary Control .

Advertise G.722 Codec*

Wideband Codec. Indicates whether Cisco Telepresence endpoints will advertise the G.722 audio codec to Unified CM. When enabled, preference is given to this audio codec.

Choices are:

- Use System Default (default)—This CTS will defer to the setting specified in the enterprise parameter, Advertise G.722 Codec

- Disabled—This CTS will not advertise G.722 to Unified CM

- Enabled—This CTS will advertise G.722 to Unified CM

See the Configuring Wideband Codec section of the Cisco Unified IP Phone 7931G Administration Guide for Cisco Unified Communications Manager 6.1(3) (SCCP) for more information about the G.722 codec.

External SYSLOG Address

Configures the external syslog address. Allowed values: Syslog address format can be either:

- host

or

- host:port

Host is either a hostname or IP address (up to 60 characters long). Port is a number between 0 and 65535. Default is 514.

Alternate CUCM for Directory Lookup

Configures the alternate Cisco Unified CM IP address that the CTS should query in the directory. This field can be either an IP address, domain name, or URL. Maximum length: 64.

TelePresence Recording Server Address

Configures the address (IP address or DNS name) of the Cisco TelePresence Recording Server (CTRS). Maximum length: 64.

Presentation Frames Per Second*

Selects the frames per second (fps) for the external presentation.

Live Desk Number

Specifies the number that the system dials when the user presses the Live Desk button or softkey. For more information, refer to the Live Desk in Cisco Unified CM section of the Release Notes for Cisco TelePresence System Software Release 1.9 .

### User Preferences Area

Table 1-8 shows the fields in the User Preferences area.

Note Fields marked with an asterisk ( * ) in the administration interface are required entries for basic configuration.

Table 1-8 Fields in the User Preferences Area

Field

Description

Days Display Not Active

Specifies the days of the week that the Cisco TelePresence system display remains off by default. Choices are Monday through Sunday. Default is Saturday

To select multiple days, hold down the Control key.

Display On Time

Specifies the time of day that the Cisco TelePresence system display(s) will remain on after being turned on. Enter a value using a 24-hour format where 00:00 indicates 12:00 midnight and 23:59 indicates 11:59 pm.

Default is 07:30.

Note If you clear the default value so that the field is blank, the display(s) turn off after the completion of each call.

Display On Duration

Specifies the length of time the Cisco TelePresence system display(s) will remain on if a “Display On Time” value is defined. Enter a value using a 24-hour format, where 1:30 indicates one hour and thirty minutes. The maximum value is 24:00 (24 hours).

Default is 10:30.

Note If you clear the default value so that the field is blank, then the display turns off at 11:59 pm. The time set in this field affects how the lights operate on the CTS 500. See the “Lights (CTS 500 only)” field description later in this table.

Idle Display*

Selects the idle screen (“home screen”) on the phone interface when CTS is idle. Choices are:

- Default Detailed (default)

- Manual

- Calendar

- Directory

- Favorites

- Default Simple

CTS Auto Answer*

Allows the CTS endpoint to override the Unified CM DN settings on a shared line.

Choices are:

- Follow CUCM DN Settings (default)—

–	Internal calls are set to Auto Answer or No Auto Answer

–	External calls are set to No Auto Answer

Note If your system uses a Cisco Unified IP phone for call control, you must configure the phone in Unified CM so that CTS Auto Answer is turned off. Otherwise, the phone might answer the call instead of the CTS system.

- CTS Override - Auto Answer All—Sets Auto Answer on for both internal and external calls regardless of the DN configuration.

- CTS Override - Auto Answer Internal Only—Sets Auto Answer on for internal calls regardless of the DN configuration.

- CTS Override - Auto Answer External Only—Sets Auto Answer on for external calls regardless of the DN configuration.

Note Auto Answer is set to No by default on the CTS 500 32.”

Second Row Capacity (CTS 32x0 systems only)*

Number of second-row conference room seats supported in a CTS 3210 or TX9200 meeting room. Default is 12 seats.

Table Microphone Count (CTS 1100, CTS 1300 and TX1310 systems only)*

Number of microphones that are available. Choose a number from the drop-down menu.

Note See the “Setting Up the Microphones” section of the Cisco TelePresence System 1300 Assembly, First-Time Setup, and Field-Replaceable Unit Guide for more information.

Maximum Self View Time (in seconds)*

Leave the default setting.

Note Camera loopback is always in self view or flipped mode.

See the “Self View Control” section for information about using the Self View feature.

Check Boxes

Enable Audio Echo Cancellation (AEC)

Check this box to enable audio echo cancellation in the CTS. Default is True.

Note This box is not available for CTS 500-32 and CTS 500-37 systems running Unified CM version 8.5 and higher (but is still available on all other CTS devices). To enable or disable AEC on the CTS 500-32 and CTS 500-37, use the set audio aec disable and set audio aec enable command-line interface (CLI) commands.

Enable Call Termination Ring

Check this box to enable the a ring tone at the termination of a call. Default is True.

Enable Single Microphone Mute

Check this box to enable the single microphone mute feature. Default is disabled.

Note For multiple microphone systems only.

See Single Microphone Mute .

### Optional Hardware

Click the appropriate check boxes in the Optional Hardware area if the following optional hardware devices are installed:

- presentation codec : a CTS 500-37, CTS 1100 Series, CTS 1300-65, or CTS 3000 Series endpoint.

- A/V Expansion Box (audio/video extension unit)

- Auxiliary Control Unit

Note This parameter must correctly reflect how your system is configured. Any discrepancy will cause the CTS to function improperly. See the “Product Specific Configuration Layout Area” section to find the default values for your system. Some check boxes will not appear for some device types. The CTS 1100 and the CTS 1300 use the Auxiliary Control Unit by default, for example, so these boxes are automatically checked.

See the Cisco TelePresence Hardware Options and Upgrade Guide for more information about installing and maintaining optional hardware.

Figure 1-9 and show additional features that you can manage from the Product Specific Configuration Layout window:

### Auxiliary Control Unit

Required if installed. Only the following systems use the Auxiliary Control Unit: Cisco TelePresence Systems 1000, 1100, 1300-65, 3000, 3010, 3200

Choose the appropriate option from the drop-down list for Auxiliary Control Unit Power Control:

- On with calls only, as shown in Figure 1-9 . See Notes About Auxiliary Control .

- On with display settings

- On all the time

Figure 1-9 Auxiliary Control Unit Settings

See the “Product Specific Configuration Layout Area” section to find the default values for your system. See also the Cisco TelePresence Hardware Options and Upgrade Guide for more information about hardware options.

Note The CTS 1100 and the CTS 1300-65 use the Auxiliary Control Unit by default.

### Notes About Auxiliary Control

- Auxiliary Video Input—On some systems, auxiliary video input may be displayed on the primary 65-inch main screen even when the auxiliary presentation display is powered off or is disconnected from the presentation codec.

Ensure that the Auxiliary presentation display is powered on and connected at all times. Consult the manual for your display to make any configuration changes.

- Auxiliary Power Control: On With Calls Only—On some systems when Power Control is configured for “On with calls only” and there is an Auxiliary HDMI port connected (Active Display or Projector), the lights will remain on for 5 minutes after the call has been terminated. If no Auxiliary HDMI port is in use, the lights will go off immediately.

### Dial Plan Area

Provide dial plan information for the Cisco TelePresence device using the descriptions in Table 1-9 . Click Save to save your settings.

Tip Only numeric values are allowed.

Figure 1-10	Dial Plan Settings

Table 1-9 Cisco TelePresence Dial Plan Information

Field

Required?

Description

Site Access Code

—

Specifies the access code of this site (cluster). Maximum field length is 6.

Inter Site Access Code

—

Specifies the access code to dial another site (cluster). Maximum field length is 6.

Off-Net Access Code

—

Specifies the access code to dial outside of the network (PSTN). Maximum field length is 3.

National Dialing Digits

—

Specifies the digits dialed to place a national call. Maximum field length is 6.

International Dialing Digits

—

Specifies the digits dialed to place an international call. Maximum field length is 6.

### Directory Number Area

Provide directory number information for the Cisco TelePresence device using the descriptions in Table 1-10 . Click Save to save your settings.

Tip Only numeric values are accepted.

Figure 1-11	Directory Number Settings

Table 1-10 Cisco TelePresence Directory Number

Field

Required?

Description

Country Code

—

Specifies the country code for this site. Maximum field length is 4.

Area Code

—

Specifies the area code for this site. Maximum field length is 6.

Local Number

—

Specifies the subscriber number of this Cisco TelePresence endpoint. Maximum field length is 15.

### Global Location Area

Provide global location information for the Cisco TelePresence device using the descriptions in Table 1-11 as a guide. Click Save to save your settings.

Figure 1-12	Global Location Settings

Table 1-11 Cisco TelePresence Global Location

Field

Required?

Description

Latitude

—

Indicates the site’s latitude. The format for this field is as follows: dd mm ss P

- dd—Degrees. Values are 0 to 89.

- mm—Minutes. Values are 0 to 59.

- ss—Seconds (optional). Values are 0 to 59.

- P—Direction. Values are N (north) or S (south).

Maximum field length is 15 characters.

Longitude

—

Indicates the site’s longitude. The format for this field is as follows: ddd mm ss P

- ddd—Degrees. Values are 0 to 179.

- mm—Minutes. Values are 0 to 59.

- ss—Seconds (optional). Values are 0 to 59.

- P—Direction. Values are E (east) or W (west).

Maximum field length is 15 characters.

### S SH Information Area

Figure 1-13 shows the Secure Shell (SSH) Information window.

Figure 1-13	SSH Information Window

Using the information in Table 1-12 as a guide, provide a username and password for the SSH account that will be used to access the command line interface (CLI) and the Cisco TelePresence Web Administration interface.

Changing the SSH username and password also changes the username and password for the Cisco TelePresence administration interface.

Click Save to save your settings.

Table 1-12 Cisco TelePresence Secure Shell Settings

Field

Required?

Setting

SSH Admin User

Yes

Username for the Secure Shell account. Used for SSH access and to access the Cisco TelePresence administration interface. Cisco Technical Assistance Center (TAC) uses secure shell for troubleshooting and debugging. Contact TAC for further assistance. Default user name is admin. The length of this username can be between 6 and 64 characters. This username supports CLI multi-level access (MLA).

Do not use any of the following user names: apache , daemon , help , helpdesk , nobody , operator , or shutdown .

Usernames and passwords can contain upper and lower case alphanumeric characters and the underscore and dash characters. User names cannot start with a - (dash) or _ (underscore).

Note for SSH admin and SSH helpdesk user names: You cannot swap the SSH admin user name and the SSH Helpdesk user name without performing an interim user name change. For example, given an admin user name of minad and a helpdesk name of deskhelp , perform the following steps to change the admin name to deskhelp and the helpdesk name to minad :

1.	Change the admin user name to a temporary password (for example, admintemp ) and change the helpdesk name to minad .

2.	Click Save , then click Apply Config .

3.	Wait until the “Calls Not Possible” pop-up screen disappears from the Touch Device.

4.	Change the admin user name to deskhelp .

SSH Admin Password

Yes

Password for the SSH account to be used for SSH access and to access the Cisco TelePresence Web Administration interface. Default password is cisco.

- Maximum field length is 64 characters.

- Minimum field length is 6 characters.

SSH Admin Life

Yes

Sets the password expiration duration to ensure that the system is protected when using Cisco TelePresence Command Line Interface (CLI). You must periodically update this password. See Figure 1-13 to see updated SSH fields that are used to update your password.

Password expiration can be set to have a value between 0 and 365. A setting of 0 disables password aging. Default is 60 days. Unless the configured life has been disabled (by being set to 0), password age is set to have 2 days remaining in the following situations:

- New installations and factory resets.

- Software upgrades (if the password age is less than the configured age).

- Password recovery (using the pwrecovery command).

An on-screen warning message is sent to the CLI user when 14 days remain on the current password, and so on until the password expires. If the password is allowed to expire, the system ignores the CLI login attempt and the user cannot access the system unless a new password is created by entering information in the SSH Information Area window.

Save your changes by clicking Restart. This enables the updated configuration to be read, applied to the CTS, and then Calling Service is restarted. Alternately you can click Reset, which causes the CTS to reboot. On startup, the CTS reads the Unified CM configuration and applies any changes.

See the Cisco TelePresence System Command-Line Interface Reference Guide for more information.

SSH Helpdesk User

Yes

Username for the Helpdesk user secure shell account. Used for SSH access and to access the Cisco TelePresence administration interface. Cisco Technical Assistance Center (TAC) uses secure shell for troubleshooting and debugging. Contact TAC for further assistance. Default user name is helpdesk. The length of this username can be between 6 and 64 characters.

The helpdesk user has limited access to the CLI and no set commands are allowed.

Do not use any of the following user names: admin , apache , daemon , nobody , operator , or shutdown .

User names and passwords can contain upper and lower case alphanumeric characters and the underscore and dash characters. User names cannot start with a - (dash) or _ (underscore).

Note for SSH admin and SSH helpdesk user names: You cannot swap the SSH admin user name and the SSH Helpdesk user name without performing an interim user name change. For example, given an admin user name of minad and a helpdesk name of deskhelp , perform the following steps to change the admin name to deskhelp and the helpdesk name to minad :

1.	Change the admin user name to a temporary password (for example, admintemp ) and change the helpdesk name to minad .

2.	Click Save , then click Apply Config .

3.	Wait until the “Calls Not Possible” pop-up screen disappears from the Touch Device.

4.	Change the admin user name to deskhelp .

5.	Click Save , then click Apply Config .

SSH Helpdesk Password

Yes

Password for the SSH account to be used for SSH access and to access the Cisco TelePresence Web Administration interface. Default password is cisco.

- Maximum field length is 64 characters.

- Minimum field length is 6 characters.

SSH Helpdesk Life

Yes

### External CTS Log Destination Area

This subsection comprises six fields. The first four configure the CTS to “push” the captured log file to a remote server:

- External CTS Log Address

- Protocol

- External CTS Log User Name

- External CTS Log User Password

The second two fields configure the CTS to automatically capture logs on a periodic basis:

- Log Period

- Log Start Time

Note These two sets of fields can be configured independently of each other.

Enter external CTS log address information into the fields using the information in Table 1-12 as a guide. Click Save to save your settings.

Table 1-13	Cisco TelePresence External CTS Log Destination Settings

Field

Required?

Setting

External CTS Log Address

—

Configures the external CTS logging address. If populated, when CTS logs are generated, a copy of the logs will be sent to this address using the chosen protocol. You may append a destination path to the address of the remote machine.

Address format can be either:

- host

or

- host:port

Host is either a hostname or IP address (up to 60 characters long). Port is a number between 0 and 65535. Default is 514.

Proto col

—

Selects the protocol to be used to transfer the CTS logs to the Logging Destination. Choose from the following:

- SCP (default)

- SFTP

- FTP

External CTS Log User Name

—

Configures the external CTS logging user name.

Maximum length: 64

External CTS Log User Password

—

Configures the external CTS logging user password. Password is write only.

Maximum length: 64

Log Period

—

The frequency with which the system will automatically generate external CTS log information. Choose from the following:

- Never (default)

- Once per Day

- Once per 3 Days

- Once per Week

Log Start Time

—

Indicates the time of day CTS will generate logs. The value should be in a 24 hour format. Where 00:00 is the beginning of the day and 23:59 is the end of the day. Leaving this field blank will turn off the automatic logging function.

Maximum length: 5

### SNMP Configuration Parameters Area

Using the information in Table 1-14 as a guide, provide the required Simple Network Management Protocol (SNMP) configuration parameters for accessing the SNMP server that is associated with the Cisco TelePresence device. Figure 1-14 shows the SNMP Configuration Parameters screen.

Note Passwords in SNMP parameter fields can only be 32 characters in length.

Figure 1-14 SNMP Configuration Parameters

Note All SNMP fields are marked to reflect the applicable SNMP version.

Table 1-14 Cisco TelePresence SNMP Configuration Parameters

Field

Required?

Setting

Enable SNMP

Yes

Enables or disables SNMP on the CTS. SNMP must be enabled for the Cisco TelePresence system to support SNMP. Options include the following:

- Disabled (default)

- Enabled (v3)

- Enabled (v3/v2)

- Enabled (v2c)

Note SNMP username is automatically configured by the system as “admin”.

SNMP (v3) Security Level

Yes

Level of security supported by the SNMP user. This field is only used for SNMP v3. Choose from the following security levels:

- (v3) Authentication, No Privacy

- (v3) Authentication, Privacy

SNMP (v3) Auth. Algorithm

Yes

Authentication algorithm supported by the SNMP user. This field is only used for SNMP v3. Choose from the following algorithms:

- MD5 —Message-Digest algorithm 5

- SHA —Secure Hash Algorithm

SNMP (v3) Auth. Password

Yes

SNMP administration user authentication password used to gain access to the SNMP v3 server associated with the Cisco TelePresence system. Default password is snmppassword.

- Maximum field length is 32 characters.

- Minimum field length is 8 characters.

SNMP (v3) Privacy Algorithm

Yes

Privacy algorithm supported by the SNMP user. This field is only used for SNMP v3. Choose from the following privacy algorithms:

- DES —Data Encryption Standard

- AES —Advanced Encryption Standard

SNMP (v3) Privacy Password

Yes

SNMP administration privacy password used to gain access via SNMP v3 on the Cisco TelePresence system. Default password is snmppassword.

- Maximum field length is 32 characters.

- Minimum field length is 8 characters.

SNMP System Location

Yes

SNMP System Location associated with this Cisco TelePresence system. Maximum field length is 64 characters.

Default is Location.

SNMP System Contact

Yes

Name of the SNMP system contact associated with this Cisco TelePresence system. Maximum field length is 64 characters.

Default is Contact.

SNMP (v2c) Community Read Only

Yes

SNMP community strings authenticate access to MIB objects and function as embedded passwords. Read-only gives read access to authorized management stations to all objects in the MIB except the community strings, but does not allow write access. This field is only used for SNMP v2c.

Default is readonly.

SNMP (v2c) Community Read Write

Yes

SNMP community strings authenticate access to MIB objects and function as embedded passwords. Read-write gives read and write access to authorized management stations to all objects in the MIB, but does not allow access to the community strings. This field is only used for SNMP v2c.

Default is readwrite.

### SNMP Trap Receiver Parameters Area

Table 1-15 lists the preset SNMP trap receiver parameters that are associated with the Cisco TelePresence device.

Note Using the information in Table 1-15 as a guide, you can set up to five trap destinations.

Table 1-15 Cisco TelePresence SNMP Trap Receiver Parameters

Field

Required?

Setting

SNMP Trap Receiver 1

SNMP (v3) Trap Receiver Address

—

IPV4 IP address or hostname of the SNMP trap receiver (the remote SNMP system) where SNMP traps will be sent. Maximum field length is 64 characters.

SNMP (v3) Trap Username

—

SNMP v3 only. Username used to access the system where SNMP traps are received. Maximum field length is 32 characters. Username must begin with a letter.

Note: Do not use a username of admin in this field.

SNMP Security Level

Yes

SNMP v3 only. Level of security supported by the SNMP Trap Receiver. Possible field values are:

- (v3) No Authentication, No Privacy (default)

- (v3) Authentication, No Privacy

- (v3) Authentication, Privacy

- (v2c) Notification

SNMP (v3) Auth. Algorithm

Yes

SNMP v3 only. Choose from the following authenticated algorithms:

- MD5 —Message-Digest algorithm 5

- SHA —Secure Hash Algorithm

SNMP (v3) Auth. Password

Yes

SNMP v3 only. Password used to gain access to the SNMP server associated with the Cisco TelePresence system. Default password is snmppassword.

- Maximum field length is 32 characters.

- Minimum field length is 8 characters.

Note Each algorithm requires different privacy and authentication passwords.

SNMP (v3) Privacy Algorithm

Yes

SNMP v3 only. Choose from the following privacy algorithms:

- AES —Advanced Encryption Standard

- DES —Data Encryption Standard

SNMP (v3) Privacy Password

Yes

SNMP v3 only. Default password is snmppassword1.

- Maximum field length is 32 characters.

- Minimum field length is 8 characters.

Note Each algorithm requires different privacy and authentication passwords.

SNMP(v2c) Community String

Yes

Community string supported by the Trap Receiver. This field is only used for SNMP v2c.

Default is communityString. Maximum length: 64

### Managing SNMP MIBs and SNMP Traps

See the Cisco TelePresence System Message Guide for information about managing SNMP MIBs and Traps.

### Saving Your Settings

When you have finished making changes to the parameters in the Phone Configuration window, click Save then Apply Config. The Apply Configuration Information window appears showing the chosen device name.

Note You must save the configuration before continuing. When you click Apply Config, the device might go through a restart. When restart is initiated, connected calls will be preserved but calls in progress may be dropped.

## Configuring the Directory Number for the Cisco TelePresence Device

Note You must restart your system after you have completed the configuration tasks in this section.

Use the information in the following sections to configure the directory number in the Directory Number Configuration window. When you have finished entering configuration information, click Save and follow the prompts to restart the system.

### Directory Number Information

To configure settings in the Directory Number Information box, complete the following steps:

Step 1	If you have not already done so, click Add a new DN in the Association Information box to open the Directory Number Configuration window.

Step 2	Enter the directory information using the information in Table 1-16 as a guide.

Table 1-16 Cisco TelePresence Device Directory Number Information

Field

Required?

Setting

Directory Number

Yes

Phone number for the Cisco TelePresence device.

Note To use Cisco WebEx features, the phone number that is entered in Cisco Unified CM administration must be configured in full, including the country code, and must exactly match the phone number that is entered in the CTMS administration Dial In Number field.

Route Partition

—

Choose from the drop-down menu or leave the default, <None>.

Description

—

Optional. Enter a device description.

Alerting Name

Yes

Enter the CTS endpoint name.

ASCII Alerting Name

—

Optional. Enter the ASCII alerting name.

Step 3	Make sure that the check box at the bottom of the Directory Number Information section is marked as indicated: Active: Checked

Step 4	Click Save to save your settings.

### Directory Number Settings

The fields described in Table 1-17 are left unchanged in the Directory Number Settings box:

Table 1-17 Cisco TelePresence Device Directory Number Settings

Field

Required?

Setting

Voice Mail Profile

—

Set to “NoVoiceMail” if you do not have voicemail capability.

Calling Search Space

—

<None>

Presence Group

Yes

Leave the default setting.

User Hold MOH Audio Source

—

<None>

Network Hold MOH Audio Source

—

<None>

Auto Answer

Yes

Leave the default setting.

Additional drop-down menu choices:

- Auto Answer Off

Note Optionally, you can set Auto Answer Off and instead configure the Product Specific Configuration Layout Area “CTS Auto Answer” setting to have the CTS pick up the call.

- Auto Answer with Headset

- Auto Answer with Speakerphone

Note To assign a directory number for the shared-line Cisco Unified IP Phone, choose Auto Answer with Speakerphone. See the “Assigning a Directory Number for the Shared-Line Cisco Unified IP Phone” section .

Note If you are using the IP Phone and the call is connected as audio only, verify that the following check-boxes are checked: —Disable Speakerphone —Disable Speakerphone and Headset

### AAR Settings

The fields described in Table 1-18 are left unchanged in the AAR Settings box:

Table 1-18 Cisco TelePresence Device AAR Settings

Field

Required?

Setting

AAR

—

Voice Mail

Check the box to select.

AAR Destination Mask

AAR Destination Mask details.

AAR Group

Leave the default setting in the drop-down menu.

Note Check the box to retain the current destination information in the call forwarding history.

### Call Forward and Call Pickup Settings

The fields described in Table 1-19 are left unchanged in the Call Forward and Call Pickup Settings box:

Table 1-19 Cisco TelePresence Device Call Forward and Call Pickup Settings

Field

Required?

Setting

Calling Search Space Activation Policy

—

Calling Search Space

Use System Default.

Additional drop-down menu choices:

- With Configured CSS

- With Activating Device/Line CSS

Forward All

—

Voice Mail

Check the box to select.

Destination

Destination details.

Calling Search Space

Leave field as <None>.

Secondary Calling Search Space for Fall Forward

Forward Busy Internal

—

Voice Mail

Check the box to select.

Destination

Destination details.

Calling Search Space

Leave field as <None>.

Forward Busy External

—

Forward No Answer Internal

Yes (if no voicemail capability)

Forward No Answer External

Yes (if no voicemail capability)

Forward No Coverage Internal

—

Voice Mail

Check the box to select.

Destination

Destination details.

Calling Search Space

Leave field as <None>.

Forward No Coverage External

—

Forward on CTI Failure

—

Forward Unregistered Internal

—

Forward Unregistered External

—

Forward Unregistered External

—

Call Pickup Group

—

### MLPP Alternate Party Settings

The fields described in Table 1-20 are left unchanged in the multilevel precedence and preemption (MLPP) Alternate Party Settings box:

Table 1-20 Cisco TelePresence Device MLPP Alternate Party Settings

Field

Required?

Setting

Target (Destination)

—

Leave the default setting. Supported characters: 0-9, +, *, #.

MLPP Calling Search Space

—

<None>

AARMLPP No Answer Ring Duration (seconds)

—

Leave the default setting.

### Line Settings for All Devices

The fields described in Table 1-21 are left unchanged in the Line Settings for All Devices Settings box:

Table 1-21 Cisco TelePresence Device Line Settings for All Devices Settings

Field

Required?

Setting

Hold Reversion Ring Duration (seconds)

—

Leave the default setting.

Note Setting the Hold Reversion Ring Duration to zero will disable the feature.

Hold Reversion Notification Interval (seconds)

—

Leave the default setting.

Note Setting the Hold Reversion Notification Interval to zero will disable the feature.

### Line X on Device X

Manage the TFTP profile for the Cisco TelePresence endpoint by configuring the meeting room name so that the room name appears on the Cisco WebEx Participant List , as shown in Figure 1-15 .

Figure 1-15 Display (Internal Caller ID) Fields

Line X on Device X Fields are described in Table 1-22 .

Table 1-22 Cisco TelePresence Device Line X on Device X Settings

Field

Required?

Setting

Display (Internal Caller ID)

—

Leave the default setting. For Cisco WebEx, enter your room name so that the room name appears on the Cisco WebEx Participant List .

Note Display text for a line appearance is intended for displaying text such as a name instead of a directory number for internal calls. If you specify a number, the person receiving a call may not see the proper identity of the caller.

ASCII Display (Internal Caller ID)

—

Leave the default setting. For Cisco WebEx, enter your room name so that the room name appears on the Cisco WebEx Participant List .

External Phone Number Mask

—

Leave the default setting.

Visual Message Waiting Indicator Policy

Yes

Leave the default setting.

Audible Message Waiting Indicator Policy

Yes

Leave the default setting.

Ring Setting (Phone Idle)

Yes

Leave the default setting.

Ring Setting (Phone Active)

—

Leave the default setting. Applies to this line when any line on the phone has a call in progress.

Call Pickup Group Audio Alert Setting (Phone Idle)

—

Leave the default setting.

Recording Option

Yes

Leave the default setting.

Recording Profile

—

<None>

Monitoring Calling Search Space

—

<None>

### Multiple Call/Call Waiting Settings on Device SEPXXXXXXXXXXXX

The Multiple Call/Call Waiting settings make it possible to place a meeting on hold, dial a phone number, and have up to four active calls on one device. This feature is useful for adding phone calls to a Cisco TelePresence meeting.

The default setting for the maximum number of additional phone calls allowed on the CTS Cisco Unified IP phone is 4.

Note Valid range for Maximum Number of calls is 1-46.

To configure multiple call waiting settings on a specific device:

Step 1	Enter configuration settings in the fields provided using the information in Table 1-23 as a guide.

Step 2	Click Save to save your settings.

Table 1-23 Cisco TelePresence Device Multiple Call/Call Waiting Settings

Field

Required?

Setting

Maximum Number of Calls

Yes

Up to 4.

Busy Trigger

Yes

2 (Recommended)

Note Less than or equal to the maximum number of calls. By default, after two calls are started, a third attempt at connecting to the IP phone results in a busy signal.

### Forwarded Call Information Display on Device SEPXXXXXXXXXXXX

Leave the following information unchanged in the Forwarded Call Information Display on Device X Settings box:

- Caller Name

- Caller Number

- Redirected Number

- Dialed Number

## Where to Go Next

If you have an IP Phone, proceed to Chapter5, “Configuring and Managing the Cisco Unified IP Phone”

| Field | Required | Setting |
|---|---|---|
| Name | Yes | Enter a name for the security profile. When you save the new profile, the name displays in the Device Security Profile drop-down list box in the Phone Configuration window for the phone type and protocol. Tip	Include the device model and protocol in the security profile name to help you find the correct profile when you are searching for or updating a profile. |
| Description | — | Enter a description for the security profile. |
| Nonce Validity Time | Yes | Enter the number of minutes (in seconds) that the nonce value is valid. The default value equals 600 (10 minutes). When the time expires, Cisco Unified CM generates a new value. |
| Device Security Mode | Yes | Choose Encrypted from the drop-down menu (recommended). Encrypted mode allows Cisco Unified CM to provide integrity, authentication, and encryption for the phone. A TLS connection that uses AES128/SHA opens for signaling, and SRTP carries the media for all phone calls on all SRTP-capable SIP hops. Note The Media is Encrypted icon (closed lock) is displayed on the screen only when the Device Security mode is set to encrypted and cluster security mode is set to 1 ( mixed mode ). To configure and verify cluster security mode, see the Verifying the Cisco Unified Communications Manager Security Mode section of the Cisco TelePresence Security Solutions Guide . Additional Device Security Mode field choices: Non Secure—No security features except image authentication exist for the phone. A TCP connection opens to Cisco Unified CM. Authenticated—Cisco Unified CM provides integrity and authentication for the phone. A TLS connection that uses NULL/SHA opens. |
| Transport Type | Yes | When Device Security Mode is Non Secure, choose one of the following options from the drop-down list box (not all options may display): TCP—Choose the Transmission Control Protocol to ensure that packets get received in the same order they are sent. This protocol ensures that no packets get dropped, but the protocol does not provide any security. UDP—Choose the User Datagram Protocol to ensure that packets are received quickly. This protocol, which can drop packets, does not ensure that packets are received in the order that they are sent. This protocol does not provide any security. TCP + UDP—Choose this option if you want to use a combination of TCP and UDP. This option does not provide any security. When Device Security Mode is Authenticated or Encrypted, TLS specifies the Transport Type. TLS provides signaling integrity, device authentication, and signaling encryption (encrypted mode only) for SIP phones. Note If Device Security Mode cannot be configured in the profile, the transport type specifies UDP. |
| Enable Digest Authentication | — | Not supported on CTS devices. Leave this box unchecked. |
| TFTP Encrypted Config | — | When this box is checked, Cisco Unified CM encrypts phone downloads from the TFTP server. This option exists for Cisco phones only. Tip	Cisco recommends that you enable this option and configure a symmetric key to secure digest credentials and administrative passwords. |
| Exclude Digest Credentials in Configuration File | — | When this box is checked, Cisco Unified CM omits digest credentials in phone downloads from the TFTP server. This option exists for Cisco Unified IP SIP Phone models 7905, 7912, 7940, and 7960 only. |

| Field | Required | Setting |
|---|---|---|
| Authentication Mode | Yes | Choices are: By Null String By Existing Certificate (precedence to LSC) By Existing Certificate (precedence to MIC) |
| Key Size (Bits) | Yes | Choices are: 512 1024 2048 |
| Note These fields are related to the CAPF Information settings on the Phone Configuration page. |

| Field | Required | Setting |
|---|---|---|
| SIP Phone Port | Yes | This setting applies to SIP phones that are using UDP transport. Enter the port number for Cisco Unified SIP IP Phones that are using UDP to listen for SIP messages from Cisco Unified CM. The default setting equals 5060. Phones that are using TCP or TLS ignore this setting. |

| Field | Setting |
|---|---|
| Registration | Read-only. Indicates whether the system is Registered with Cisco Unified Communications Manager and lists the registered Unified CM address. |
| IP Address | IP address for the Cisco TelePresence System. After you add the device, you can click on the address to see information for that phone in a new window. |
| Active Load ID | View-only field showing the status of the active load. |
| Device is Active check box | View only field. |
| Device is Trusted check box | View only field. |
| MAC Address* | MAC address for the Cisco TelePresence primary codec. For example, 000DD12345A1. |
| Description | Short, free-format description of the device. |
| Device Pool* | Your device pools. Choose a device pool from the drop-down menu. Click View Details to open the Device Details window, which includes the following system setting information: Device Pool Settings Roaming Sensitive Settings Device Mobility Related Information Geolocation Configuration Incoming Calling Party Settings Incoming Called Party Settings |
| Common Device Configuration | Your configured devices. Leave field as < None> . Click View Details to open t he Common Device Configuration Detail wi ndow, which includes the following system setting information: Common Device Configuration Information Multilevel Precedence and Preemption Information |
| Phone Button Template* | Standard_Cisco_TelePresence. Note Unless you have created extra button templates, you will see the default button template for your device. |
| Softkey Template (systems that use a Cisco Unified IP Phone for call control only) | <None> Note This field is only for systems that use a Cisco Unified IP Phone for call control. |
| Common Phone Profile* | Standard Common Phone Profile. |
| Calling Search Space | <None> Note Information in this field reflects Calling Search Spaces that have been created on this Unified CM. |
| Media Resource Group List | <None> |
| Location* | Hub_None. Additional choice is Phantom. |
| User Locale | <None> Note This field supports user locales listed in Table 2-4 . |
| Network Locale | <None> Note This field supports network locales listed in Table 2-4 . |
| Device Mobility Mode* | Default. Click View Current Device Mobility Settings to open the Device Mobility Details window, which shows the current device mobility settings. |
| Owner User ID | Saved User IDs. Leave field as <None>. |
| Phone Load Name | Specify required version of Cisco TelePresence System if no device default is set. |
| Use Trusted Relay Point* | Default. |
| Always Use Prime Line* | Default. |
| Always Use Prime Line for Voice Message* | Default. |
| Calling Party Transformation CSS | <None> |
| Geolocation | <None> |
| Check-Boxes in the Device Information Area |
| Use Device Pool Calling Party Transformation CSS | Box is checked. |
| Retry Video Call as Audio | Box is checked. |
| Ignore Presentation Indicators | Box is un-checked. |
| Allow Control of Device from CTI | Box is checked. |
| Logged Into Hunt Group | Box is checked. |
| Remote Device | Box is un-checked. |
| Note When you are finished making changes, click Save to save your settings. |

| Field | Setting |
|---|---|
| Packet Capture Mode* | <None> |
| Packet Capture Duration | 0 |
| Presence Group* | Standard Presence Group |
| SIP Dial Rules | <None> |
| MTP Preferred Originating Codec* | 711ulaw (default). |
| Device Security Profile* | Cisco TelePresence name of system - Standard SIP Non-Secure Profile (default) Note For more information about configuring Cisco Unified CM security features, refer to the Cisco Unified Communications Manager Security Guide, Release 7.1(2) . |
| Rerouting Calling Search Space | <None> Note Information in this field reflects Calling Search Spaces that have been created on this Unified CM. |
| SUBSCRIBE Calling Search Space* | <None> Note Information in this field reflects Calling Search Spaces that have been created on this Unified CM. |
| SIP Profile* | Choose Standard SIP Profile . Information in this field reflects SIP profiles that have been created on this Unified CM. |
| Digest User | <None> |
| Check-Boxes |
| Media Termination point Required | Box is un-checked. |
| Unattended Port | Box is un-checked. |
| Allow Presentation Sharing using BFCP | Box is checked. |
| Note When you are finished making changes, click Save to save your settings. |

| Field | Required? | Setting |
|---|---|---|
| Certificate Operation* | Yes | No Pending Operation. Most configuration fields in the CAPF Information window cannot be modified. Note The drop-down menu allows you to Install/Upgrade, Delete, or Troubleshoot. If you choose one of these options, the remaining fields in the CAPF Information window can be modified. |
| Authentication Mode* | Yes | If No Pending Operation is chosen in the Certificate Operation field, this field is view only by default. |
| Authentication String | — | Leave this field unchanged. |
| Key Size (Bits)* | Yes | If No Pending Operation is chosen in the Certificate Operation field, this field is view only by default. |
| Operation Completes By | — | If No Pending Operation is chosen in the Certificate Operation field, this field is view only by default. |
| Certificate Operation Status | — | <None> |
| Note When you are finished making changes, click Save to save your settings. |

| Field | Description |
|---|---|
| Cisco TelePresence Type* | Indicates the type of Cisco TelePresence system you have installed. |
| Admin. Web Access* | When enabled, allows access to the Cisco TelePresence Web Administration interface. Default is Enabled |
| Room Name | Conference room name as described in Microsoft Exchange or Domino. Used to schedule conference calls. This field accepts a text string with a maximum of 64 characters. Note If you have the Cisco TelePresence Manager application, the name of the conference room is required. The name must exactly match the resource mailbox (including domain name) as it is entered in the Microsoft Exchange or Domino database. It will be used to schedule conference calls. |
| Maximum Call Duration (in minutes) | Maximum duration (in minutes) allowed for a Cisco TelePresence conference call. Minimum is 0 Maximum is 10080 (7 days). Default is 0 (no call duration set). The default setting disables this feature. Note This feature is coordinated with the Maximum Call Duration Timer in the Cisco Unified Communications Manager service parameters. If values other than 0 are entered for either of these fields, the smaller value takes precedence. |
| Quality (per Display)* | Bandwidth used by the system. Higher bandwidth increases video quality, but may also cause packets to be dropped and video to be interrupted. Choices are: Highest Detail, Best Motion: 1080p (default) Highest Detail, Better Motion: 1080p Highest Detail, Good Motion: 1080p High Detail, Best Motion: 720p High Detail, Better Motion: 720p High Detail, Good Motion: 720p High Detail, Limited Motion: 720p (Lite) If your system uses a Cisco Unified IP Phone for call control, note the following caveats for the 720p (Lite) choice: –	The audio addin conf softkey is not available. –	You must have MIDlets installed on the Unified CM. Network friendly for personal systems: 480p For more information about 720p (Lite), see Quality Per Display - 720p (Lite) . Note Limited bandwidth mode: 360p may be listed as an option in this field but is not yet available; it is supported in a future release. |
| Bandwidth Allocation Weights* | Sets the bandwidth allocation ratio between conference video and presentation video. Default value of this parameter is a weight of 8 for main video and a weight of 2 for presentation video for a total weight of 10. Choices are: 9 Main / 1 Presentation 8 Main / 2 Presentation (default) 6 Main / 4 Presentation 4 Main / 6 Presentation 3 Main / 7 Presentation See also the TX Software Features chapter of the Administration Guide for Cisco TelePresence TX Software Release 6.0 . |
| Main Display Frames Per Second* (TX13x0 and TX9x00 systems only)* | Selects the frame rate, or frames per second (fps), on the main display screen. Choice are: 30 fps main 60 fps main |
| Presentation Input Device* | Indicates whether you have a presentation input device. Choices are: None (default) Document Camera Note This parameter must correctly reflect how your system is configured. Any discrepancy will cause CTS to function improperly. |
| Presentation Output Device* | Indicates if you have a presentation output device. Choices are: None (default) Projector/Display Note This parameter must correctly reflect how your system is configured. Any discrepancy will cause CTS to function improperly. |
| Lights* | Defines how the lights operate in a CTS conference room. Choices are: On with calls only (default) On with display settings On all the time Note On the CTS 500, the lights are powered by the display. When the display turns off according to the display settings in Unified CM, the lights also turn off. However, if you have chosen the “On all the time” setting for the lights, the setting is not honored during power saving/non-business hours (when display settings are not active). To bypass power saving/non-business hours defaults, extend the business hours to all the time in the Display On Duration field. See also Notes About Auxiliary Control . |
| Advertise G.722 Codec* | Wideband Codec. Indicates whether Cisco Telepresence endpoints will advertise the G.722 audio codec to Unified CM. When enabled, preference is given to this audio codec. Choices are: Use System Default (default)—This CTS will defer to the setting specified in the enterprise parameter, Advertise G.722 Codec Disabled—This CTS will not advertise G.722 to Unified CM Enabled—This CTS will advertise G.722 to Unified CM See the Configuring Wideband Codec section of the Cisco Unified IP Phone 7931G Administration Guide for Cisco Unified Communications Manager 6.1(3) (SCCP) for more information about the G.722 codec. |
| External SYSLOG Address | Configures the external syslog address. Allowed values: Syslog address format can be either: host or host:port Host is either a hostname or IP address (up to 60 characters long). Port is a number between 0 and 65535. Default is 514. |
| Alternate CUCM for Directory Lookup | Configures the alternate Cisco Unified CM IP address that the CTS should query in the directory. This field can be either an IP address, domain name, or URL. Maximum length: 64. |
| TelePresence Recording Server Address | Configures the address (IP address or DNS name) of the Cisco TelePresence Recording Server (CTRS). Maximum length: 64. |
| Presentation Frames Per Second* | Selects the frames per second (fps) for the external presentation. |
| Live Desk Number | Specifies the number that the system dials when the user presses the Live Desk button or softkey. For more information, refer to the Live Desk in Cisco Unified CM section of the Release Notes for Cisco TelePresence System Software Release 1.9 . |

| Field | Description |
|---|---|
| Days Display Not Active | Specifies the days of the week that the Cisco TelePresence system display remains off by default. Choices are Monday through Sunday. Default is Saturday To select multiple days, hold down the Control key. |
| Display On Time | Specifies the time of day that the Cisco TelePresence system display(s) will remain on after being turned on. Enter a value using a 24-hour format where 00:00 indicates 12:00 midnight and 23:59 indicates 11:59 pm. Default is 07:30. Note If you clear the default value so that the field is blank, the display(s) turn off after the completion of each call. |
| Display On Duration | Specifies the length of time the Cisco TelePresence system display(s) will remain on if a “Display On Time” value is defined. Enter a value using a 24-hour format, where 1:30 indicates one hour and thirty minutes. The maximum value is 24:00 (24 hours). Default is 10:30. Note If you clear the default value so that the field is blank, then the display turns off at 11:59 pm. The time set in this field affects how the lights operate on the CTS 500. See the “Lights (CTS 500 only)” field description later in this table. |
| Idle Display* | Selects the idle screen (“home screen”) on the phone interface when CTS is idle. Choices are: Default Detailed (default) Manual Calendar Directory Favorites Default Simple |
| CTS Auto Answer* | Allows the CTS endpoint to override the Unified CM DN settings on a shared line. Choices are: Follow CUCM DN Settings (default)— –	Internal calls are set to Auto Answer or No Auto Answer –	External calls are set to No Auto Answer Note If your system uses a Cisco Unified IP phone for call control, you must configure the phone in Unified CM so that CTS Auto Answer is turned off. Otherwise, the phone might answer the call instead of the CTS system. CTS Override - Auto Answer All—Sets Auto Answer on for both internal and external calls regardless of the DN configuration. CTS Override - Auto Answer Internal Only—Sets Auto Answer on for internal calls regardless of the DN configuration. CTS Override - Auto Answer External Only—Sets Auto Answer on for external calls regardless of the DN configuration. Note Auto Answer is set to No by default on the CTS 500 32.” |
| Second Row Capacity (CTS 32x0 systems only)* | Number of second-row conference room seats supported in a CTS 3210 or TX9200 meeting room. Default is 12 seats. |
| Table Microphone Count (CTS 1100, CTS 1300 and TX1310 systems only)* | Number of microphones that are available. Choose a number from the drop-down menu. Note See the “Setting Up the Microphones” section of the Cisco TelePresence System 1300 Assembly, First-Time Setup, and Field-Replaceable Unit Guide for more information. |
| Maximum Self View Time (in seconds)* | Leave the default setting. Note Camera loopback is always in self view or flipped mode. See the “Self View Control” section for information about using the Self View feature. |
| Check Boxes |
| Enable Audio Echo Cancellation (AEC) | Check this box to enable audio echo cancellation in the CTS. Default is True. Note This box is not available for CTS 500-32 and CTS 500-37 systems running Unified CM version 8.5 and higher (but is still available on all other CTS devices). To enable or disable AEC on the CTS 500-32 and CTS 500-37, use the set audio aec disable and set audio aec enable command-line interface (CLI) commands. |
| Enable Call Termination Ring | Check this box to enable the a ring tone at the termination of a call. Default is True. |
| Enable Single Microphone Mute | Check this box to enable the single microphone mute feature. Default is disabled. Note For multiple microphone systems only. See Single Microphone Mute . |

| Field | Required? | Description |
|---|---|---|
| Site Access Code | — | Specifies the access code of this site (cluster). Maximum field length is 6. |
| Inter Site Access Code | — | Specifies the access code to dial another site (cluster). Maximum field length is 6. |
| Off-Net Access Code | — | Specifies the access code to dial outside of the network (PSTN). Maximum field length is 3. |
| National Dialing Digits | — | Specifies the digits dialed to place a national call. Maximum field length is 6. |
| International Dialing Digits | — | Specifies the digits dialed to place an international call. Maximum field length is 6. |

| Field | Required? | Description |
|---|---|---|
| Country Code | — | Specifies the country code for this site. Maximum field length is 4. |
| Area Code | — | Specifies the area code for this site. Maximum field length is 6. |
| Local Number | — | Specifies the subscriber number of this Cisco TelePresence endpoint. Maximum field length is 15. |

| Field | Required? | Description |
|---|---|---|
| Latitude | — | Indicates the site’s latitude. The format for this field is as follows: dd mm ss P dd—Degrees. Values are 0 to 89. mm—Minutes. Values are 0 to 59. ss—Seconds (optional). Values are 0 to 59. P—Direction. Values are N (north) or S (south). Maximum field length is 15 characters. |
| Longitude | — | Indicates the site’s longitude. The format for this field is as follows: ddd mm ss P ddd—Degrees. Values are 0 to 179. mm—Minutes. Values are 0 to 59. ss—Seconds (optional). Values are 0 to 59. P—Direction. Values are E (east) or W (west). Maximum field length is 15 characters. |

| Field | Required? | Setting |
|---|---|---|
| SSH Admin User | Yes | Username for the Secure Shell account. Used for SSH access and to access the Cisco TelePresence administration interface. Cisco Technical Assistance Center (TAC) uses secure shell for troubleshooting and debugging. Contact TAC for further assistance. Default user name is admin. The length of this username can be between 6 and 64 characters. This username supports CLI multi-level access (MLA). Do not use any of the following user names: apache , daemon , help , helpdesk , nobody , operator , or shutdown . Usernames and passwords can contain upper and lower case alphanumeric characters and the underscore and dash characters. User names cannot start with a - (dash) or _ (underscore). Note for SSH admin and SSH helpdesk user names: You cannot swap the SSH admin user name and the SSH Helpdesk user name without performing an interim user name change. For example, given an admin user name of minad and a helpdesk name of deskhelp , perform the following steps to change the admin name to deskhelp and the helpdesk name to minad : 1.	Change the admin user name to a temporary password (for example, admintemp ) and change the helpdesk name to minad . 2.	Click Save , then click Apply Config . 3.	Wait until the “Calls Not Possible” pop-up screen disappears from the Touch Device. 4.	Change the admin user name to deskhelp . |
| SSH Admin Password | Yes | Password for the SSH account to be used for SSH access and to access the Cisco TelePresence Web Administration interface. Default password is cisco. Maximum field length is 64 characters. Minimum field length is 6 characters. |
| SSH Admin Life | Yes | Sets the password expiration duration to ensure that the system is protected when using Cisco TelePresence Command Line Interface (CLI). You must periodically update this password. See Figure 1-13 to see updated SSH fields that are used to update your password. Password expiration can be set to have a value between 0 and 365. A setting of 0 disables password aging. Default is 60 days. Unless the configured life has been disabled (by being set to 0), password age is set to have 2 days remaining in the following situations: New installations and factory resets. Software upgrades (if the password age is less than the configured age). Password recovery (using the pwrecovery command). An on-screen warning message is sent to the CLI user when 14 days remain on the current password, and so on until the password expires. If the password is allowed to expire, the system ignores the CLI login attempt and the user cannot access the system unless a new password is created by entering information in the SSH Information Area window. Save your changes by clicking Restart. This enables the updated configuration to be read, applied to the CTS, and then Calling Service is restarted. Alternately you can click Reset, which causes the CTS to reboot. On startup, the CTS reads the Unified CM configuration and applies any changes. See the Cisco TelePresence System Command-Line Interface Reference Guide for more information. |
| SSH Helpdesk User | Yes | Username for the Helpdesk user secure shell account. Used for SSH access and to access the Cisco TelePresence administration interface. Cisco Technical Assistance Center (TAC) uses secure shell for troubleshooting and debugging. Contact TAC for further assistance. Default user name is helpdesk. The length of this username can be between 6 and 64 characters. The helpdesk user has limited access to the CLI and no set commands are allowed. Do not use any of the following user names: admin , apache , daemon , nobody , operator , or shutdown . User names and passwords can contain upper and lower case alphanumeric characters and the underscore and dash characters. User names cannot start with a - (dash) or _ (underscore). Note for SSH admin and SSH helpdesk user names: You cannot swap the SSH admin user name and the SSH Helpdesk user name without performing an interim user name change. For example, given an admin user name of minad and a helpdesk name of deskhelp , perform the following steps to change the admin name to deskhelp and the helpdesk name to minad : 1.	Change the admin user name to a temporary password (for example, admintemp ) and change the helpdesk name to minad . 2.	Click Save , then click Apply Config . 3.	Wait until the “Calls Not Possible” pop-up screen disappears from the Touch Device. 4.	Change the admin user name to deskhelp . 5.	Click Save , then click Apply Config . |
| SSH Helpdesk Password | Yes | Password for the SSH account to be used for SSH access and to access the Cisco TelePresence Web Administration interface. Default password is cisco. Maximum field length is 64 characters. Minimum field length is 6 characters. |
| SSH Helpdesk Life | Yes |  |

| Field | Required? | Setting |
|---|---|---|
| External CTS Log Address | — | Configures the external CTS logging address. If populated, when CTS logs are generated, a copy of the logs will be sent to this address using the chosen protocol. You may append a destination path to the address of the remote machine. Address format can be either: host or host:port Host is either a hostname or IP address (up to 60 characters long). Port is a number between 0 and 65535. Default is 514. |
| Proto col | — | Selects the protocol to be used to transfer the CTS logs to the Logging Destination. Choose from the following: SCP (default) SFTP FTP |
| External CTS Log User Name | — | Configures the external CTS logging user name. Maximum length: 64 |
| External CTS Log User Password | — | Configures the external CTS logging user password. Password is write only. Maximum length: 64 |
| Log Period | — | The frequency with which the system will automatically generate external CTS log information. Choose from the following: Never (default) Once per Day Once per 3 Days Once per Week |
| Log Start Time | — | Indicates the time of day CTS will generate logs. The value should be in a 24 hour format. Where 00:00 is the beginning of the day and 23:59 is the end of the day. Leaving this field blank will turn off the automatic logging function. Maximum length: 5 |

| Field | Required? | Setting |
|---|---|---|
| Enable SNMP | Yes | Enables or disables SNMP on the CTS. SNMP must be enabled for the Cisco TelePresence system to support SNMP. Options include the following: Disabled (default) Enabled (v3) Enabled (v3/v2) Enabled (v2c) Note SNMP username is automatically configured by the system as “admin”. |
| SNMP (v3) Security Level | Yes | Level of security supported by the SNMP user. This field is only used for SNMP v3. Choose from the following security levels: (v3) Authentication, No Privacy (v3) Authentication, Privacy |
| SNMP (v3) Auth. Algorithm | Yes | Authentication algorithm supported by the SNMP user. This field is only used for SNMP v3. Choose from the following algorithms: MD5 —Message-Digest algorithm 5 SHA —Secure Hash Algorithm |
| SNMP (v3) Auth. Password | Yes | SNMP administration user authentication password used to gain access to the SNMP v3 server associated with the Cisco TelePresence system. Default password is snmppassword. Maximum field length is 32 characters. Minimum field length is 8 characters. |
| SNMP (v3) Privacy Algorithm | Yes | Privacy algorithm supported by the SNMP user. This field is only used for SNMP v3. Choose from the following privacy algorithms: DES —Data Encryption Standard AES —Advanced Encryption Standard |
| SNMP (v3) Privacy Password | Yes | SNMP administration privacy password used to gain access via SNMP v3 on the Cisco TelePresence system. Default password is snmppassword. Maximum field length is 32 characters. Minimum field length is 8 characters. |
| SNMP System Location | Yes | SNMP System Location associated with this Cisco TelePresence system. Maximum field length is 64 characters. Default is Location. |
| SNMP System Contact | Yes | Name of the SNMP system contact associated with this Cisco TelePresence system. Maximum field length is 64 characters. Default is Contact. |
| SNMP (v2c) Community Read Only | Yes | SNMP community strings authenticate access to MIB objects and function as embedded passwords. Read-only gives read access to authorized management stations to all objects in the MIB except the community strings, but does not allow write access. This field is only used for SNMP v2c. Default is readonly. |
| SNMP (v2c) Community Read Write | Yes | SNMP community strings authenticate access to MIB objects and function as embedded passwords. Read-write gives read and write access to authorized management stations to all objects in the MIB, but does not allow access to the community strings. This field is only used for SNMP v2c. Default is readwrite. |

| Field | Required? | Setting |
|---|---|---|
| SNMP Trap Receiver 1 |
| SNMP (v3) Trap Receiver Address | — | IPV4 IP address or hostname of the SNMP trap receiver (the remote SNMP system) where SNMP traps will be sent. Maximum field length is 64 characters. |
| SNMP (v3) Trap Username | — | SNMP v3 only. Username used to access the system where SNMP traps are received. Maximum field length is 32 characters. Username must begin with a letter. Note: Do not use a username of admin in this field. |
| SNMP Security Level | Yes | SNMP v3 only. Level of security supported by the SNMP Trap Receiver. Possible field values are: (v3) No Authentication, No Privacy (default) (v3) Authentication, No Privacy (v3) Authentication, Privacy (v2c) Notification |
| SNMP (v3) Auth. Algorithm | Yes | SNMP v3 only. Choose from the following authenticated algorithms: MD5 —Message-Digest algorithm 5 SHA —Secure Hash Algorithm |
| SNMP (v3) Auth. Password | Yes | SNMP v3 only. Password used to gain access to the SNMP server associated with the Cisco TelePresence system. Default password is snmppassword. Maximum field length is 32 characters. Minimum field length is 8 characters. Note Each algorithm requires different privacy and authentication passwords. |
| SNMP (v3) Privacy Algorithm | Yes | SNMP v3 only. Choose from the following privacy algorithms: AES —Advanced Encryption Standard DES —Data Encryption Standard |
| SNMP (v3) Privacy Password | Yes | SNMP v3 only. Default password is snmppassword1. Maximum field length is 32 characters. Minimum field length is 8 characters. Note Each algorithm requires different privacy and authentication passwords. |
| SNMP(v2c) Community String | Yes | Community string supported by the Trap Receiver. This field is only used for SNMP v2c. Default is communityString. Maximum length: 64 |

| Field | Required? | Setting |
|---|---|---|
| Directory Number | Yes | Phone number for the Cisco TelePresence device. Note To use Cisco WebEx features, the phone number that is entered in Cisco Unified CM administration must be configured in full, including the country code, and must exactly match the phone number that is entered in the CTMS administration Dial In Number field. |
| Route Partition | — | Choose from the drop-down menu or leave the default, <None>. |
| Description | — | Optional. Enter a device description. |
| Alerting Name | Yes | Enter the CTS endpoint name. |
| ASCII Alerting Name | — | Optional. Enter the ASCII alerting name. |

| Field | Required? | Setting |
|---|---|---|
| Voice Mail Profile | — | Set to “NoVoiceMail” if you do not have voicemail capability. |
| Calling Search Space | — | <None> |
| Presence Group | Yes | Leave the default setting. |
| User Hold MOH Audio Source | — | <None> |
| Network Hold MOH Audio Source | — | <None> |
| Auto Answer | Yes | Leave the default setting. Additional drop-down menu choices: Auto Answer Off Note Optionally, you can set Auto Answer Off and instead configure the Product Specific Configuration Layout Area “CTS Auto Answer” setting to have the CTS pick up the call. Auto Answer with Headset Auto Answer with Speakerphone Note To assign a directory number for the shared-line Cisco Unified IP Phone, choose Auto Answer with Speakerphone. See the “Assigning a Directory Number for the Shared-Line Cisco Unified IP Phone” section . Note If you are using the IP Phone and the call is connected as audio only, verify that the following check-boxes are checked: —Disable Speakerphone —Disable Speakerphone and Headset |

| Field | Required? | Setting |
|---|---|---|
| AAR | — | Voice Mail Check the box to select. AAR Destination Mask AAR Destination Mask details. AAR Group Leave the default setting in the drop-down menu. |
| Note Check the box to retain the current destination information in the call forwarding history. |

| Field | Required? | Setting |
|---|---|---|
| Calling Search Space Activation Policy |
|  | — | Calling Search Space Use System Default. Additional drop-down menu choices: With Configured CSS With Activating Device/Line CSS |
| Forward All | — | Voice Mail Check the box to select. Destination Destination details. Calling Search Space Leave field as <None>. |
| Secondary Calling Search Space for Fall Forward |
| Forward Busy Internal | — | Voice Mail Check the box to select. Destination Destination details. Calling Search Space Leave field as <None>. |
| Forward Busy External | — |
| Forward No Answer Internal | Yes (if no voicemail capability) |
| Forward No Answer External | Yes (if no voicemail capability) |
| Forward No Coverage Internal | — | Voice Mail Check the box to select. Destination Destination details. Calling Search Space Leave field as <None>. |
| Forward No Coverage External | — |
| Forward on CTI Failure | — |
| Forward Unregistered Internal | — |
| Forward Unregistered External | — |
| Forward Unregistered External | — |
| Call Pickup Group | — |

| Field | Required? | Setting |
|---|---|---|
| Target (Destination) | — | Leave the default setting. Supported characters: 0-9, +, *, #. |
| MLPP Calling Search Space | — | <None> |
| AARMLPP No Answer Ring Duration (seconds) | — | Leave the default setting. |

| Field | Required? | Setting |
|---|---|---|
| Hold Reversion Ring Duration (seconds) | — | Leave the default setting. Note Setting the Hold Reversion Ring Duration to zero will disable the feature. |
| Hold Reversion Notification Interval (seconds) | — | Leave the default setting. Note Setting the Hold Reversion Notification Interval to zero will disable the feature. |

| Field | Required? | Setting |
|---|---|---|
| Display (Internal Caller ID) | — | Leave the default setting. For Cisco WebEx, enter your room name so that the room name appears on the Cisco WebEx Participant List . Note Display text for a line appearance is intended for displaying text such as a name instead of a directory number for internal calls. If you specify a number, the person receiving a call may not see the proper identity of the caller. |
| ASCII Display (Internal Caller ID) | — | Leave the default setting. For Cisco WebEx, enter your room name so that the room name appears on the Cisco WebEx Participant List . |
| External Phone Number Mask | — | Leave the default setting. |
| Visual Message Waiting Indicator Policy | Yes | Leave the default setting. |
| Audible Message Waiting Indicator Policy | Yes | Leave the default setting. |
| Ring Setting (Phone Idle) | Yes | Leave the default setting. |
| Ring Setting (Phone Active) | — | Leave the default setting. Applies to this line when any line on the phone has a call in progress. |
| Call Pickup Group Audio Alert Setting (Phone Idle) | — | Leave the default setting. |
| Recording Option | Yes | Leave the default setting. |
| Recording Profile | — | <None> |
| Monitoring Calling Search Space | — | <None> |

| Field | Required? | Setting |
|---|---|---|
| Maximum Number of Calls | Yes | Up to 4. |
| Busy Trigger | Yes | 2 (Recommended) Note Less than or equal to the maximum number of calls. By default, after two calls are started, a third attempt at connecting to the IP phone results in a busy signal. |