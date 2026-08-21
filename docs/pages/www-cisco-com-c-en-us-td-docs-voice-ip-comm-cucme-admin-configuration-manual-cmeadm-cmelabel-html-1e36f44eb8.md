---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmelabel-html-1e36f44eb8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmelabel.html
retrieved_at: 2026-08-21T07:25:21.803233+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Modify Cisco Unified IP Phone Options

## Chapter: Modify Cisco Unified IP Phone Options

# Modify Cisco Unified IP Phone Options

This chapter describes the screen and button features available for
                        		Cisco Unified IP phones connected to Cisco Unified Communications Manager
                        		Express (Cisco Unified CME).

## Information About Cisco Unified IP Phone Options

### Clear Directory
                           	 Entries

Cisco Unified CME
                              		8.6 allows you to clear the display of call-history details such as missed,
                              		placed, and received call entries on your Cisco Unified  SCCP IP phone’s
                              		display screen. You can press the directory services button on most of the
                              		Cisco Unified  IP phones or program a line button on 7931 phone to delete the
                              		display of phone number entries in the missed, placed, and received calls. The
                              		clear call directory feature is supported on Cisco Unified  IP phones, 7960,
                              		7961, 7970. 7971 and 8961.

To enable the clear
                              		directory entries feature, a call-history option is added to the exclude command. For more information on configuring phones to clear call-history
                              		details, see Clear Call-History Details from a SCCP Phone .

### Enable Customized
                           	 Background Images for Cisco Unified IP Phone 7970

The Cisco Unified IP
                              		Phone 7970 and 7971 support customized background images on the phone screen.
                              		To enable your Cisco Unified IP Phone 7970 or 7971 to display a customized
                              		background image, follow the procedure in the technical note at http://www.cisco.com/en/US/products/sw/voicesw/ps4625/products_tech_note09186a008062495a.shtml .

Sample background
                              		images are available in the 7970-backgrounds.tar file at http://www.cisco.com/cgi-bin/tablebuild.pl/ip-iostsp .

### Customized Button
                           	 Layout

Cisco Unified CME
                              		8.5 and later versions allow you to customize the display order of various
                              		button types on a phone using the button layout feature. The button layout
                              		feature allows you to customize the display of the following button types:

Line buttons

Speed Dial
                                       			 buttons

BLF Speed Dial
                                       			 buttons

Feature Buttons

ServiceURL
                                       			 buttons

Cisco Unified CME
                              		8.5 uses the button layout command is to populate buttons in any desired order. All buttons displayed on
                              		the phone follow the button-layout configuration. In the button layout command, the physical button number on the phone is specified under the button-string parameter of the button layout command. Buttons that are not defined under the button layout configuration are
                              		displayed as blank lines. Before configuring button layout on phones, line
                              		buttons, feature buttons (including privacy button), and url buttons must be
                              		configured through line button , feature
                                    			 button and url button commands, respectively.

Line Buttons

The button layout
                              		control feature allows you to populate buttons with corresponding physical line
                              		numbers or line number ranges. Line buttons that are not associated with a
                              		physical line are not displayed on the phone.You can customize any Cisco
                              		Unified SCCP IP phone button to function as a line button using the button
                              		command and specifying the position, button type, and directory number of the
                              		phone. For more information, see Configure Button Layout on SCCP Phones .

For Cisco Unified
                              		SIP phones, the first physical button must be a line button with a valid
                              		directory number. You can customize the other buttons using the button command and specifying the relative position (position index), button type, and
                              		directory number of the button. For more information, see Configure Button Layout on SIP Phones .

Speed Dial Buttons

You can customize
                              		the display of Speed Dial buttons to appear before, after, or between line
                              		buttons using the speed-dial command and specifying the position of the button. The button layout feature
                              		allows you to populate the buttons with corresponding physical line numbers or
                              		line number ranges. Buttons that do not have a physical line associated with
                              		them are not displayed on the phone.

BLF Speed Dial Buttons

The button layout
                              		feature allows you to display the BLF Speed-Dial buttons before, after or
                              		between the line buttons using the blf-speed-dial command with a specific position.
                              		Once the BLF speed-dial button is configured, the system populates the button
                              		with corresponding physical line number or range of line numbers. Buttons
                              		without a physical line association are not displayed on the phone.

Feature Buttons

Currently, privacy
                              		button is the only button available and is presented at the end of all the
                              		above mentioned buttons. With PLK feature you can enable most phone features on
                              		phone’s physical buttons (line keys). This button layout feature requests all
                              		presented buttons to be configured via button , speed-dial , blf-speed-dial , feature-button , or url-button commands. The privacy-button is overridden by feature-button if there is one.
                              		For more information on configuring feature buttons on a line key, see Configure Feature Button on a Cisco Unified SCCP Line Key and Configure Feature Button on a Cisco Unified SIP Phone Line Key .

If the
                                          		  button-layout feature is configured in both ephone-template and logout profile
                                          		  (extension mobility) mode, configuration in the latter takes precedence.
                                          		  Button-layout configuration under ephone mode takes precedence in phones that
                                          		  do not have extension mobility (EM).

Privacy button is
                                          		  counted as a feature button on phones that support privacy button and do not
                                          		  have any feature button configured through the feature-button command.

URL Buttons

The button layout
                              		feature allows you to display the url button before, after, or even between the
                              		line buttons, speed dial buttons, BLF speed dial buttons, or feature buttons.
                              		For more information on configuring the URL button on a line key, see Configure Service URL Button on a SCCP Phone Line Key and Configure Service URL Button on a SIP IP Phone Line Key .

### Customized Phone
                           	 User Interface Services

In Cisco Unified CME
                              		8.5 and later, you can customize the availability of individual service items
                              		such as Extension Mobility, My Phone Apps, and Single Number Reach (SNR) on a
                              		phone’s user interface by assigning individual service item to a button using
                              		the Programmable Line Key (PLK) url-button configuration. For more information,
                              		see Configure Service URL Button on a SCCP Phone Line Key .

You can limit the
                              		availability of an individual service item on a phone’s user interface by
                              		disabling the configuration for services such as EM, My Phone Apps, and Local
                              		Directory and exclude the display of these services from the phone’s user
                              		interface. You can use the exclude command under ephone-template mode to
                              		exclude the display of Extension Mobility (EM), My Phone Apps, and Local
                              		Directory. For more information, see Block Local Services on Phone User Interface .

If a directory
                              		service is enabled through PLK configuration, the PLK configuration takes
                              		precedence over the exclusion of directory services under ephone or ephone
                              		template configuration modes. The service is available through the button
                              		directly regardless of the exclusion of services configured under ephone and
                              		ephone-template modes.

In Cisco Unified CME
                              		8.5 and later versions, you use the exclude command in ephone or ephone-template configuration mode to exclude the
                              		availability of local services such as EM, My Phone Apps, and Local Directory
                              		from a Cisco Unified SCCP IP phone's user interface.

In Cisco Unified CME
                              		9.0 and later versions, you use the exclude command in voice register pool or voice register template configuration mode to
                              		exclude any of these local services from a Cisco Unified SIP IP phone's user
                              		interface.

Before Cisco
                                          		  Unified CME 9.0, you must configure the Local Directory service with the
                                          		  internal URL address.

In Cisco Unified CME 9.0 and later versions, the internal URL address
                                          		  is the default when no external URL address is configured.

### Fixed Line-Feature
                           	 Buttons for Cisco Unified IP Phone 7931G

In Cisco Unified CME
                              		4.0(2) and later versions, you can select from two fixed button-layout formats
                              		to assign functionality to certain line buttons on a Cisco Unified IP Phone
                              		7931G to support key system phone behavior. If you do not select a button set,
                              		no fixed set of feature/line buttons are defined.

The line button
                              		layout for the Cisco Unified IP Phone 7931G is a bottom-up array. Button 1 is
                              		at the bottom right of the array and button 24 is at the top left of the array.

Button set 1
                              		includes two predefined feature buttons: button 24 is Menu and button 23 is
                              		Headset.

Button set 2
                              		includes four predefined feature buttons: button 24 is Menu; button 23 is
                              		Headset; button 22 is Directories; and button 21 is Messages.

For configuration,
                              		see Select Button Layout for a Cisco Unified SCCP IP Phone 7931G .

### Header Bar
                           	 Display

You can customize
                              		the content of an IP phone header bar, which is the top line of the IP phone
                              		display.

The IP phone header
                              		bar, or top line, of a Cisco Unified IP Phone normally replicates the text that
                              		appears next to the first line button. The header bar is shown in Cisco Unified IP Phone Display .
                              		The header bar can, however, contain a user-definable message instead of the
                              		extension number. For example, the header bar can be used to display a name or
                              		the full E.164 number of the phone. If no description is specified, the header
                              		bar replicates the extension number that appears next to the first button on
                              		the phone.

### Phone
                           	 Labels

Phone labels are
                              		configurable text strings that can be displayed instead of extension numbers
                              		next to line buttons on a Cisco Unified IP phone. By default, the number that
                              		is associated to a directory number, and assigned to a phone, is displayed next
                              		to the applicable button. The label feature allows you to enter a meaningful
                              		text string for each directory number so that a phone user with multiple lines
                              		can select a line by label instead of by phone number, thus eliminating the
                              		need to consult in-house phone directories. For configuration information, see Create Labels for Directory Numbers on SCCP Phones or Create Labels for Directory Numbers on a SIP Phone .

### Programmable
                           	 Vendor Parameters for Phones

The vendorConfig
                              		section of the configuration file contains phone and display parameters that
                              		are read and implemented by a phone's firmware when that phone is booted. Only
                              		the parameters supported by the currently loaded firmware are available. The
                              		number and type of parameters may vary from one firmware version to the next.

The IP phone that
                              		downloads the configuration file will implement only those parameters that it
                              		can support and ignore configured parameters that it cannot implement. For
                              		example, a Cisco Unified IP Phone 7970G does not have a backlit display and
                              		cannot implement Backlight parameters regardless of whether they are
                              		configured. The following text shows the format of an entry in the
                              		configuration file:

```
<vendorConfig>
<parameter-name>parameter-value</parameter-name>
</vendorConfig>
```

For configuration
                              		information at the system level, see Modify Vendor Parameters for All SCCP Phones .

For configuration
                              		information for individual phones, see Modify Vendor Parameters for a Specific SCCP Phone .

### Push-to-Talk

This feature allows
                              		one-way Push-to-Talk (PTT) in Cisco Unified CME 7.0 and later versions without
                              		requiring an external server to support the functionality. PTT is supported in
                              		firmware version 1.0.4 and later versions on Cisco Unified Wireless IP Phone
                              		7921 and 7925 with a thumb button.

In the following
                              		figure, button1/DN 1 is configured as the primary line for this phone. Button
                              		6/ DN 10 is configured for PTT and is the line that is triggered by pushing the
                              		thumb button on this phone.

Holding down on
                                       			 the thumb button causes the configured DN on the phone to go off-hook.

The thumb button
                                       			 utilizes an intercom DN that targets a paging number (1050).

The targeted
                                       			 paging group (DN 50) can be unicast or multicast or both.

Users will hear
                                       			 a “zipzip” tone when call path is set up.

All other keys
                                       			 on the phone are locked during this operation.

Releasing the
                                       			 thumb button ends the call.

For configuration
                              		information, see Configure One-Way Push-to-Talk on Cisco Unified SCCP Wireless IP Phones .

### Support for Cisco
                           	 Jabber

For Unified CME 12.5, Cisco Jabber was supported. In this version, the SIP softphone client supports VoIP over WLAN. Unified CME
                              supports supplementary services such as Hold, Resume, Transfer, Call Park, and Call Pickup for the softphone SIP client.

Cisco Jabber versions supported on Unified CME are now End-of-Life. Hence, there is no active support for Cisco Jabber on
                                          Unified CME 14.1 or earlier releases.

#### Feature Support for Cisco Jabber

The following features are supported for Cisco Jabber with Unified CME:

Hold or Resume

Transfer

Shared Line

Mixed Shared Line

Call forward—All, Busy, No Answer, Unregistered

Directed Call Park Pickup

Single Number Reach (SNR)

Voice Hunt Group (Sequential, Parallel)

Hardware Conference

Music On Hold

Video

##### Restrictions

The following features are not supported for Cisco Jabber with Unified CME:

Barge

cBarge

Built-in Bridge (BIB) Conference

Do Not Disturb

KPML Dialing

### Cisco Jabber
                           	 Client Support on CME

Cisco Jabber Client
                              		is a SIP-based soft client with integrated Instant Messaging and presence
                              		functionality, and uses the new Client Services Framework 2nd Generation
                              		(CSF2G) architecture.

CSF is a unified
                              		communications engine that is reused by multiple Cisco PC-based clients and
                              		mobile clients. The client is identified by a device ID name that can be
                              		configured under the voice register pool in Cisco Unified CME. You should
                              		configure the username and password under voice register pool to identify the
                              		user logging into Cisco Unified CME through Cisco Jabber client. The device
                              		discovery process uses HTTPS connection. Therefore, you should configure the
                              		secure HTTP on Cisco Unified CME.

A new phone type, Jabber-CSF-Client has been added to configure the Cisco Jabber client under
                              			voice register pool. This can be used to configure any CSF based Cisco Jabber client. In
                              			Unified CME 10.0, we used the type 'Jabber-Win' to configure Cisco Jabber client. In
                              			Unified CME 10.5, this type is deprecated and the new 'Jabber-CSF-Client' should be used
                              			to configure Cisco Jabber client as well.

Cisco Jabber CSF client can be provisioned in two modes: Full UC mode (with integrated IM and
                              			Presence services) and Phone only mode. The phone-only mode of Cisco Jabber CSF devices
                              			is also supported. This can be configured with the option 'phone-mode phone-only' under
                              			'voice register global' or 'voice register pool' or 'voice register template' config.

If the Jabber client is installed in phone only mode then no extra configuration is required on CME. The normal Jabber configuration
                              should be sufficient.

For more information on installing Jabber client in phone mode for Windows, see https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

For more information on installing Jabber client in phone mode for Mac, see https://www.cisco.com/c/en/us/support/unified-communications/jabber-mac/products-installation-guides-list.html .

If the Jabber
                              		client is installed in Full UC mode and you want to enable the phone only mode
                              		from CME, then the 'phone-mode' configuration is required as mentioned in the
                              		configuration section.

Table 1 lists the Cisco Jabber Client Support versions along with the corresponding CME
                              		and Jabber client versions:

For Unified CME Release 12.5 (On Cisco 4000 Series Integrated Services Router), Cisco Jabber CSF client (softphone mode)
                              Version 12.1.0 for MAC (phone-only) and Windows (phone-only) was supported.

Cisco Jabber client versions supported on Unified CME are now End-of-Life (EOL). Hence, there is no active support on Unified
                                          CME for Cisco Jabber clients.

Cisco CSF Device Type

Unified CME Supported Version

Jabber Client Version

Cisco Jabber for MAC (phone-only) and Windows (phone-only)

10.0

9.1.0

10.5

9.2.1

12.5

12.1.0

Restrictions

The Cisco Jabber CSF client supports only the softphone mode with Cisco Unified
                                    					CME.

Desk phone mode is not supported.

The following Cisco Jabber CSF type of devices are not supported:

Cisco Jabber for iPhone (both full UC mode and phone-only mode)

Cisco Jabber for Android (both full UC mode and phone-only mode)

Cisco Jabber for iPad (both full UC mode and phone-only mode)

For configuration
                              		information, see Configure Cisco Jabber for CSF Client in Unified CME .

For configuration
                              		examples, see Example for Configuring Cisco Jabber CSF Client .

### System Message Display

The System Message Display feature allows you to specify a custom text
                              		or display message to appear in the lower part of the display window on
                              		display-capable IP phones. If you do not set a custom text or display message,
                              		the default message “Cisco Unified CME” is displayed.

When you specify a text message, the number of characters that can be
                              		displayed is not fixed because IP phones typically use a proportional (as
                              		opposed to fixed-width) font. There is room for approximately 30 alphanumeric
                              		characters.

The display message is refreshed with a new message after one of the following events occurs:

Busy phone goes back on-hook.

idle phone receives a keepalive message.

Phone is restarted.

The file-display feature allows you to specify a file to display on display-capable IP phones when they are not in use. You
                              can use this feature to provide the phone display with a system message that is refreshed at configurable intervals, similar
                              to the way that the text message feature provides a message. The difference between the two is that the system text message
                              feature displays a single line of text at the bottom of the phone display, whereas the system display message feature can
                              use the entire display area and contain graphic images.

The System Message command is supported only for SCCP IP phones registered to CME. It is not supported for SIP IP phones in CME mode.

### URL Provisioning
                           	 for Feature Buttons

URL provisioning for
                              		programmable feature buttons allows you to specify alternative XML files to
                              		access using the feature buttons on IP phones.

Certain phones, such
                              		as the Cisco Unified IP Phone 7940, 7940G, 7960, and 7960G, have programmable
                              		feature buttons that invoke noncall-related services. The four
                              		buttons—Services, Directories, Messages, and Information (the i button)—are
                              		linked to appropriate feature operations through URLs. The fifth
                              		button—Settings—is managed entirely by the phone.

The feature buttons
                              		are provisioned with specific URLs. The URLs link to XML web pages formatted
                              		with XML tags that the Cisco Unified IP phone understands and uses. When you
                              		press a feature button, the Cisco Unified IP phone uses the configured URL to
                              		access the appropriate XML web page for instructions. The web page sends
                              		instructions to the Cisco Unified IP phone to display information on the screen
                              		for users to navigate. Phone users can select options and enter information by
                              		using soft keys and the scroll button.

Operation of these
                              		feature buttons is determined by the capabilities of the Cisco Unified IP phone
                              		and the content of the specified URL.

In Cisco Unified CME
                              		4.2 and later versions, up to eight URLs can be configured for the Services
                              		feature button by using an ephone template to apply the configuration to one or
                              		more supported SCCP phones. If you use an ephone template to configure services
                              		URLs for one or SCCP phones and you also configure a system-level services URL
                              		in telephony-service configuration mode, the value set in telephony-service
                              		configuration mode appears first in the list of services displayed when the
                              		phone user presses the Services feature button. Cisco Unified CME self-hosted
                              		services, such as Extension Mobility, always appears last in the list of
                              		options displayed for the Services feature button.

For configuration
                              		information, see Provision URLs for Feature Buttons for SCCP Phones .

### My Phone Apps for Cisco Unified SIP IP Phones

Before Cisco Unified CME 9.0, the My Phone Apps features were only
                              		supported on Cisco Unified SCCP IP phones.

In Cisco Unified CME 9.0 and later versions, support is added for My
                              		Phone Apps feature on Cisco Unified SIP IP phones.

add, modify, or delete Speed Dial

add, modify, or delete Fast Dial

add, modify, or delete BLF Speed Dial

change SNR DN

perform after-hour login

reset the phone

The My Phone Apps features are available on both Extension Mobility (EM)
                              		and non-EM phones. For EM phones, the user login service allows the user to
                              		temporarily access a physical phone other than their own and utilize their
                              		personal settings as if the phone is their own desk phone. Any change in
                              		settings follows the user to the next phone they access. For non-EM phones, any
                              		change in settings remains with the physical phone.

## Configure Cisco Unified IP Phone Options

### Enable Edit User Settings

#### Before you begin

Cisco Unified CME 8.6 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- service phone parameter-name parameter-value

- voice register global

- create profile

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode.

Step 4

service phone parameter-name parameter-value

#### Example:

```
Router(config-telephony)# service phone paramEdibility 1
```

Enables the edit user settings.

Step 5

voice register global

#### Example:

```
Router(config-telephony)# voice register global
```

Enters voice register global configuration mode.

Step 6

create profile

#### Example:

```
Router(config-register-global)# create profile
```

Generates provisioning files required for SIP phones and writes
                                             				the file to the location specified with the tftp-path command.

Step 7

end

#### Example:

```
Router(config-register-global)# end
```

Exits configuration mode and enters privileged EXEC mode.

### Clear Call-History
                           	 Details from a SCCP Phone

To clear the
                                 		  display of Call History details such as Missed Calls, Placed Calls, and
                                 		  Received Calls, from a SCCP IP phone user interface, follow these steps:

#### Before you begin

To enable phones
                                 		  to send an HTTP GET request, url directories must be the default (not
                                 		  configured) or configured as http://<CME's ip address>/localdirectory .

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of the following commands:

- ephone phone-tag

- ephone template template tag

- exclude [ em | myphoneapp | directory | call-history ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

Enter one of the following commands:

- ephone phone-tag

- ephone template template tag

#### Example:

```
Router(config)# ephone 10
```

Enters ephone configuration mode.

phone-tag —Unique number of the phone for which you want to exclude local services such as Extension Mobility, My Phone Apps, and Local
                                                      Directory.

Step 4

exclude [ em | myphoneapp | directory | call-history ]

#### Example:

```
Router(config-ephone)#exclude call-history
```

Excludes local
                                             				services (EM, My Phone Apps, Local Directory, and Call History) from displaying
                                             				on phone’s user interface.

em—Excludes Extension Mobility (EM) from the phone’s user
                                                      					 interface.

myphoneapp
                                                      					 —Excludes My Phone App service from the phone’s user interface.

directory
                                                      					 —Excludes Local Directory service from the phone’s user interface.

call-history—Excludes entries from Call History on the phone’s
                                                      					 user interface.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows call-history as excluded from ephone 10 and ephone-template 5:

```
!
telephony-service
 max-ephones 40
 max-dn 100
 max-conferences 8 gain -6
 transfer-system full-consult
!
!
ephone-template  5
 exclude call-history
!
!
ephone  10
 exclude call-history
 device-security-mode none
!
```

#### Troubleshooting Tips for Clearing Call-History Details from a SCCP
                              	 Phone

Make sure that the local directory XML tag is configured and
                                          			 provisioned correctly.

Check the attribute for <directoryURL> tag in the xml file (it
                                          			 must be set up with http://<CME's ip address>/localdirectory) and the
                                          			 phone must be restarted with this XML cnf file.

Make sure that the phone sends out an HTTP GET request.

Make sure that the HTTP GET request in the Cisco Unified CME log
                                          			 with “deb ip http url” is enabled.

Make sure that the Clear Directory Entries request is sent to the
                                          			 phone.

Check the Missed Calls, Placed Calls, and Received Calls on your
                                          			 phone’s local directory.

### Configure Dial
                           	 Rules for Cisco Softphone SIP Client

#### Before you begin

Cisco Unified CME
                                 		  8.6 or a later version.

Support for idle url is available only on Unified CME 12.0 and later
                                 		  versions.

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template
                                       				  tag

- url { AppDialRule string | DirLookupRule string | ldapServer string | idle url | service url }

- voice register pool pool
                                       				  tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register template template
                                                				  tag

#### Example:

```
Router(config)#voice register template 8
```

Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME.

Step 4

url { AppDialRule string | DirLookupRule string | ldapServer string | idle url | service url }

#### Example:

```
Router(config-register-temp)# url ldapServer ldap.abcd.com
```

```
Router(config-register-temp)# url AppDialRule tftp://10.1.1.1/AppDialRules.xml
```

```
Router(config-register-temp)# url DirLookupRule tftp://10.1.1.1/DirLookupRules.xml
```

```
Router(config-register-temp)# url idle http://www.mycompany.com/files/logo.xml idle-timeout 12
```

```
Router(config-register-temp)# url service http://10.0.0.4/CCMUser/123456/urltest.html
```

Allows to
                                             				define SIP phone URLs to configure Application Dial Rule, Directory Lookup Dial
                                             				Rule, LDAP server, idle url, and service url in voice register template
                                             				configuration mode.

ldapserver string —LDAP server URL.

AppDialRule string —Application dial rule URL.

DirLookupRule string —Directory lookup rule URL.

idle url —Defines the location of a file to display on
                                                      					 phones that are not in use and specifies the interval between refreshes of the
                                                      					 display, in seconds.

service url —Uses the information at the specified URL for
                                                      					 invoking phone services.

Step 5

voice register pool pool
                                                				  tag

#### Example:

```
Router(config)#voice register pool 8
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

Step 6

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows dial rules configured under voice register template 2:

```
!
voice register template 2
 url ldapServer ldap.abcd.com
 url AppDialRule tftp://10.1.1.1/AppDialRules.xml
 url DirLookupRule tftp://10.1.1.1/DirLookupRules.xml
!
```

The following is a
                                 		  sample of Application Dial Rule content:

```
Router#more flash:AppDialRules.xml
<?xml version="1.0" encoding="UTF-8"?><DialRules>
        <DialRule BeginsWith="+1" NumDigits="12" DigitsToRemove="1" PrefixWith="9"/>
        <DialRule BeginsWith="+1" NumDigits="12" DigitsToRemove="1" PrefixWith="9"/>
        <DialRule BeginsWith="919" NumDigits="10" DigitsToRemove="3" PrefixWith="9"/>
        <DialRule BeginsWith="1" NumDigits="11" DigitsToRemove="0" PrefixWith="9"/>
        <DialRule BeginsWith="" NumDigits="10" DigitsToRemove="0" PrefixWith="91"/>
        <DialRule BeginsWith="" NumDigits="7" DigitsToRemove="0" PrefixWith="9"/>
        <DialRule BeginsWith="+" NumDigits="13" DigitsToRemove="1" PrefixWith="9011"/>
        <DialRule BeginsWith="+" NumDigits="14" DigitsToRemove="1" PrefixWith="9011"/>
        <DialRule BeginsWith="+" NumDigits="15" DigitsToRemove="1" PrefixWith="9011"/>
       
        <DialRule BeginsWith="+" NumDigits="12" DigitsToRemove="1" PrefixWith="9011"/>
        <DialRule BeginsWith="+" NumDigits="11" DigitsToRemove="1" PrefixWith="9011"/>
</DialRules>
```

### Select Button
                           	 Layout for a Cisco Unified SCCP IP Phone 7931G

#### Before you begin

Cisco Unified CME
                                 		  4.0(2) or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- button-layout phone-type { 1 | 2 }

- exit

- ephone phone-tag

- ephone-template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 15
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

Step 4

button-layout phone-type { 1 | 2 }

#### Example:

```
Router(config-ephone-template)# button-layout 7931 2
```

Specifies
                                             				which fixed set of feature buttons appears on a Cisco Unified IP Phone 7931G
                                             				that uses a template in which this is configured.

1 —Includes two predefined feature buttons: button
                                                      					 24 is Menu and button 23 is Headset.

2 —Includes four predefined feature buttons: button
                                                      					 24 is Menu; button 23 is Headset; button 22 is Directories; and button 21 is
                                                      					 Messages.

Step 5

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits from
                                             				this command mode to the next highest mode in the configuration mode hierarchy.

Step 6

ephone phone-tag

#### Example:

```
Router(config)# ephone 1
```

Enters ephone
                                             				configuration mode.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 15
```

Applies an
                                             				ephone template to the ephone that is being configured.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for Phones .

### Configure Button
                           	 Layout on SCCP Phones

#### Before you begin

Cisco Unified
                                          				CME 8.5 or later versions.

Button types
                                          				such as, line, feature, url, speed-dial, and blf-speed-dial are configured
                                          				using commands such as, button , feature-button or privacy-button , url-button , speed-dial ,
                                          				and blf-speed-dial respectively.

First button
                                          				must be configured as line button.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template
                                       				  tag

- button-layout [ button-string | button-type ]

- exit

- ephone phone-tag

- ephone-template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-template template
                                                				  tag

#### Example:

```
Router(config)# ephone 10
```

Enters ephone
                                             				template configuration mode to create an ephone template.

Step 4

button-layout [ button-string | button-type ]

#### Example:

```
Router(config-ephone-template)#button-layout 1 line
Router(config-ephone-template)#button-layout 2,5 speed-dial
Router(config-ephone-template)#button-layout 3,6 blfspeed-dial
Router(config-ephone-template)#button-layout 4,7,9 feature
Router(config-ephone-template)# button-layout 8,11 url
```

Assigns
                                             				physical button numbers or ranges of numbers with button types.

button-string —Specifies a coma separated list of
                                                      					 physical button number or ranges of button numbers.

button-type —Specifies one of the following button
                                                      					 types: Line, Speed-Dial, BLF-Speed-Dial, Feature, URL. Button number specifies
                                                      					 the relative display order of the button within the button type (line button,
                                                      					 speed-dial, blf-speed-dial, feature-button or url-button).

To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button.

When no
                                                         				  feature-buttons are configured, privacy button is counted as a feature button.

Step 5

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits from
                                             				this command mode to the next highest mode in the configuration mode hierarchy.

Step 6

ephone phone-tag

#### Example:

```
Router(config)# ephone 1
```

Enters ephone
                                             				configuration mode.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 10
```

Applies an
                                             				ephone template to the ephone that is being configured.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### Examples

```
Router# show telephony-service ephone-template
ephone-template  10
 button-layout 1 line
 button-layout 2,5 speed-dial
 button-layout 3,6 blf-speed-dial
 button-layout 4,7,9 feature
 button-layout 8,11 url
```

#### What to do next

If you are done
                                 		  modifying parameters for SCCP phones in Cisco Unified CME, restart the phones.

### Configure Button
                           	 Layout on SIP Phones

You can not
                                             			 change the button number in the line button or index command through button
                                             			 layout configuration because the button number specifies the relative display
                                             			 order of the button within the button type (line button, speed-dial,
                                             			 blf-speed-dial, feature button, or url button).

#### Before you begin

Cisco Unified
                                          				CME 8.5 or later versions.

Button types
                                          				(line button, feature button, url-button, speed dial button, and blf speed dial
                                          				button) must be configured before configuring button layout.

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- button-layout [ button-string ] [ button-type ]

- exit

- voice register pool pool-tag

- template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register template template-tag

#### Example:

```
Router(config)# voice register template 5
```

Enters voice
                                             				register template configuration mode to create a SIP phone template.

template-tag—Range: 1 to 10.

Step 4

button-layout [ button-string ] [ button-type ]

#### Example:

```
Router(config-register-template)#button-layout 1 line
Router(config-register-template)#button-layout 2, 5 speed-dial
Router(config-register-template)#button-layout 3, 6 blfspeed-dial
Router(config-register-template)#button-layout 4,7,9 feature-button
Router(config-register-template)# button-layout 8,11 url-button
```

Assigns
                                             				physical button numbers or ranges of numbers with button types.

button-string —Specifies a coma separated list of
                                                      					 physical button number or ranges of button numbers.

button-type —Specifies one of the following button
                                                      					 types: Line, Speed-Dial, BLF-Speed-Dial, Feature, URL.

To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button.

Privacy-button is counted as a feature-button in this
                                                         				  configuration if no feature-button is configured.

Step 5

exit

#### Example:

```
Router(config-register-template)# exit
```

Exits voice
                                             				register template configuration mode.

Step 6

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 10
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

Step 7

template template-tag

#### Example:

```
Router(config-register-pool)# template 5
```

Applies a SIP
                                             				phone template to the phone you are configuring.

template-tag — Template tag that was created with
                                                      					 the voice register template command in Step 3 .

Step 8

end

#### Example:

```
Router(config-register-pool)# end
```

Exits to
                                             				privileged EXEC mode.

#### Examples

```
Router# show voice register template all
!
voice register dn  65
 number 3065
 name SIP-7965
 label SIP3065
!
voice register template  5
 button-layout 1 line
 button-layout 2,5 speed-dial
 button-layout 3,6 blf-speed-dial
 button-layout 4,7,9 feature-button
 button-layout 8,11 url-button
!
voice register template  2
 button-layout 1,5 line<
 button-layout 4 speed-dial
 button-layout 3,6 blf-speed-dial
 button-layout 7,9 feature-button
 button-layout 8,10-11 url-button
!
```

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Configure Service
                           	 URL Button on a SIP IP Phone Line Key

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- url-button [ index number ] [ url location] [ url name ]

- exit

- voice register pool phone-tag

- template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register template template-tag

#### Example:

```
Router(config)# voice register template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                      					 template that is being created. Range: 1 to 10.

Step 4

url-button [ index number ] [ url location] [ url name ]

#### Example:

```
Router(config-register-temp)url-button 1 http:// www.cisco.com
```

Configures a
                                             				service url feature button on a line key.

Index
                                                      					 number—Unique index number. Range: 1 to 8.

url location —Location of the url.

url name —Service
                                                      					 url with maximum length of 31 characters.

Step 5

exit

#### Example:

```
Router(config-register-temp)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 6

voice register pool phone-tag

#### Example:

```
Router(config)# voice register pool 12
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique number that identifies this
                                                      					 ephone during configuration tasks.

Step 7

template template-tag

#### Example:

```
Router(config-register-pool)# template 5
```

Applies the
                                             				ephone template to the phone.

template-tag —Unique identifier of the template
                                                      					 that you created in Step 3 .

Step 8

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows url buttons configured in voice register template 1:

```
Router# show run
      !
      voice register template  1
       
						url-button 1 http://9.10.10.254:80/localdirectory/query My_Dir 
						url-button 5 http://www.yahoo.com Yahoo 
		
      !
      voice register pool  50
      !
```

#### What to do next

If you are done
                                 		  configuring the url buttons for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Configure Service
                           	 URL Button on a SCCP Phone Line Key

### SUMMARY STEPS

- enable

- configure terminal

- ephone template template-tag

- url-button index type | url [ name ]

- exit

- ephone phone-tag

- ephone-template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone template template-tag

#### Example:

```
Router(config)# ephone template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                      					 template that is being created. Range: 1 to 10.

Step 4

url-button index type | url [ name ]

#### Example:

```
Router#(config-ephone-template)#url-button 1 myphoneapp 
				Router(config-ephone-template)#url-button 2 em 
				Router(config-ephone-template)#url-button 3 snr
				Router (config-ephone-template)#url-button 4 http://www.cisco.com
```

Configures a
                                             				service url feature button on a line key.

Index —Unique index number. Range: 1 to 8.

type —Type of service url button. Following types
                                                      					 of url service buttons are available:

myphoneapp: My phone application configured under phone user
                                                               						  interface.

em:
                                                               						  Extension Mobility

snr:
                                                               						  Single Number Reach

url
                                                            						  name —Service url with maximum length of 31 characters.

Step 5

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 6

ephone phone-tag

#### Example:

```
Router(config)#ephone 36
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                      					 this ephone during configuration tasks.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 5
```

Applies an
                                             				ephone template to the ephone that is being configured.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows three url buttons configured for line keys:

```
!
		  !
		  !
		  ephone-template  5
		   url-button 1 em
		   url-button 2 mphoneapp mphoneapp
		   url-button 3 snr
		  !
		  ephone  36
		   ephone-template 5
```

#### What to do next

If you are done
                                 		  configuring the url buttons for phones in Cisco Unified CME, restart the
                                 		  phones.

### Configure Feature
                           	 Button on a Cisco Unified SIP Phone Line Key

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- feature-button [ index ] [ feature identifier ]

- exit

- voice register pool phone-tag

- template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register template template-tag

#### Example:

```
Router(config)# voice register template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                      					 template that is being created. Range: 1 to 10.

Feature
                                                         				  button can be configured under voice register
                                                               						pool or voice register
                                                               						template configuration mode. If both configurations are applied
                                                         				  to the voice register
                                                               						pool , the feature button configuration under voice register
                                                               						pool takes precedence.

Step 4

feature-button [ index ] [ feature identifier ]

#### Example:

```
Router(config-voice-register-template)feature-button 1 DnD
```

```
Router(config-voice-register-template)feature-button 2 EndCall
```

```
Router(config-voice-register-template)feature-button 3 Cfwdall
```

Configures a
                                             				feature button on line key.

index —One of the 12 index numbers for a specific
                                                      					 feature type.

feature identifier —Unique identifier for a
                                                      					 feature. One of the following feature or stimulus IDs: Redial, Hold, Trnsfer,
                                                      					 Cfwdall, Privacy, MeetMe, Confrn, Park, Pickup, Gpickup, Mobility, NewCall,
                                                      					 EndCall, Dnd, ConfList, NewCall, HLog, Trnsfer.

Step 5

exit

#### Example:

```
Router(config-register-temp)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 6

voice register pool phone-tag

#### Example:

```
Router(config)# voice register pool 12
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique number that identifies this
                                                      					 ephone during configuration tasks.

Step 7

template template-tag

#### Example:

```
Router(config-register-pool)# template 5
```

Applies the
                                             				ephone template to the phone.

template-tag —Unique identifier of the template
                                                      					 that you created in Step 3

Step 8

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows three feature buttons configured for line keys:

```
voice register template  5
		   feature-button 1 DnD
		   feature-button 2 EndCall
		   feature-button 3 Cfwdall
		  !
        !
		  voice register pool 12
		  template 5
```

#### What to do next

If you are done
                                 		  configuring the url buttons for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Configure Feature
                           	 Button on a Cisco Unified SCCP Line Key

Answer,
                                                      				  Select, cBarge, Join, and Resume features are not supported as PLKs.

Feature
                                                      				  buttons are only supported on Cisco Unified IP Phones 6911, 7941, 7942, 7945,
                                                      				  7961, 7962, 7965. 7970, 7971, and 7975 with SCCP v12 or later versions.

Any features
                                                      				  available through hard button are not be provisioned. Use the show ephone
                                                      				  register detail command to verify why the features buttons are not provisioned.

Not all
                                                      				  feature buttons are supported on Cisco Unified IP Phone 6911 phone. Call
                                                      				  Forward, Pickup, Group Pickup, and MeetMe are the only feature buttons
                                                      				  supported on the Cisco Unified IP Phone 6911.

The
                                                      				  privacy-button is available on Cisco Unified IP phones running a SCCP v8 or
                                                      				  later. Privacy-buttton is overridden by any other feature-button available.

Locales are
                                                      				  not supported on Cisco Unified IP Phone 7914.

Locales are
                                                      				  not supported for Cancel Call Waiting or Live Recording feature-buttons.

The feature
                                                      				  state for DnD, Hlog, Privacy, Login, and Night Service feature-buttons are
                                                      				  indicated by an LED.

### SUMMARY STEPS

- enable

- configure terminal

- ephone template template-tag

- feature-button index feature
                                       				  identifier

- exit

- ephone phone-tag

- ephone-template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone template template-tag

#### Example:

```
Router(config)# ephone template 10
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone template that is being created. Range: 1 to 10.

Step 4

feature-button index feature
                                                				  identifier

#### Example:

```
Router(config-ephone-template)feature-button 1 hold
```

Configures a
                                             				feature button on line key

index —index number, one from 25 for a specific feature type.

feature identifier —feature ID or stimulus ID.

Step 5

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 6

ephone phone-tag

#### Example:

```
Router(config)# ephone 5
```

Enters ephone configuration mode.

phone-tag —Unique sequence number that identifies this ephone during configuration tasks.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 10
```

Applies an ephone template to the ephone that is being configured.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows feature buttons configured for line keys:

```
! 
		  ! 
		  !
		  ephone-template  10
		   feature-button 1 Park
		   feature-button 2 MeetMe
		   feature-button 3 CallBack
		  !
		  ! 
		  ephone-template 10
```

#### What to do next

If you are done
                                 		  configuring the feature buttons for phones in Cisco Unified CME, restart the
                                 		  phones.

### Block Local
                           	 Services on Phone User Interface

To block the
                                 		  display and availability of local services such as Local Directory, Extension
                                 		  Mobility (EM), and My Phone Apps on a SCCP IP phone’s user interface, perform
                                 		  the following steps.

#### Before you begin

Cisco Unified CME
                                 		  8.5 or later versions.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag or ephone
                                       					 template template
                                       				  tag

- exclude [ em | myphoneapp | directory ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone phone-tag or ephone
                                                					 template template
                                                				  tag

#### Example:

```
Router(config)# ephone 10
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique number of the phone for which you
                                                   					 want to exclude local services such as Extension Mobility, My Phone Apps, and
                                                   					 Local Directory.

Step 4

exclude [ em | myphoneapp | directory ]

#### Example:

```
Router(config-ephone)#exclude directory em
```

Excludes local
                                             				services (EM, My Phone Apps, and Local Directory) from displaying on phone’s
                                             				user interface.

em—Excludes Extension Mobility (EM) from the phone’s user
                                                   					 interface.

myphoneapp
                                                   					 —Excludes My Phone App service from the phone’s user interface.

directory
                                                   					 —Excludes Local Directory service from the phone’s user interface.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows the Local Directory and Extension Mobility services excluded from
                                 		  the phone user interface:

```
ephone  10
 exclude directory em
 device-security-mode none
 description sccp7961
 mac-address 0007.0E57.7561
```

### Modify Header Bar
                           	 Display on SCCP Phones

#### Before you begin

Directory number
                                 		  to be modified is already configured. For configuration information, see Create Directory Numbers for SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- description display-text

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 55
```

Enters
                                             				ephone-dn configuration mode.

Step 4

description display-text

#### Example:

```
Router(config-ephone-dn)# description 408-555-0134
```

Defines a
                                             				description for the header bar of a display-capable IP phone on which this
                                             				ephone-dn appears as the first line.

display-text —Alphanumeric character string, up to
                                                      					 40 characters. String is truncated to 14 characters in the display.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for Phones .

### Modify Header Bar
                           	 Display Supported SIP Phones

Restriction

This feature is
                                             			 supported only on Cisco Unified IP Phone 7940, 7940G, 7960, and 7960G.

#### Before you begin

Cisco CME 3.4 or a
                                 		  a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- description string

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME.

Step 4

description string

#### Example:

```
Router(config-register-pool)# description 408-555-0100
```

Defines a
                                             				customized description that appears in the header bar of supported
                                             				Cisco Unified IP phones

Truncated
                                                      					 to 14 characters in the display.

If string
                                                      					 contains spaces, enclose the string in quotation marks.

Step 5

end

#### Example:

```
Router(config-register-pool)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Verify Header Bar
                           	 Display

Use the show
                                                				  running-config command to verify your configuration. Descriptions
                                          			 for directory numbers are listed in the ephone-dn and voice-register dn
                                          			 portions of the output.

#### Example:

```
Router# show running-config ephone-dn  1  dual-line
		   number 150 secondary 151
		   description 555-0150
		   call-forward busy 160 
		   call-forward noan 160 timeout 10
		   huntstop channel
		   no huntstop
		  !
		  !
		  !
		  voice-register dn 1
		   number 1101 
		   description 555-0101
```

### Troubleshooting
                           	 Header Bar Display

show telephony-service ephone

Use this
                                             				command to ensure that the ephone-dn to which you applied the description
                                             				appears on the first button on the ephone. In the example below, ephone-dn 22
                                             				has the description in the phone display header bar.

```
Router# show telephony-service ephone ephone-dn 22
		   number 2149
		   description 408-555-0149
		  
		  ephone 34
		   mac-address 0030.94C3.F96A
		   button  1:22 2:23 3:24
		   speed-dial 1 5004
		   speed-dial 2 5001
```

### Create Labels for
                           	 Directory Numbers on SCCP Phones

To create a label
                                 		  to display in place of the number next to a line button, perform the following
                                 		  steps.

#### Before you begin

Directory number
                                 		  for which the label is to be created is already configured. For configuration
                                 		  information, see Create Directory Numbers for SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- label label-string

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 1
```

Enters
                                             				ephone-dn configuration mode.

dn-tag —Unique sequence number that identifies the
                                                      					 ephone-dn to which the label is to be associated.

Step 4

label label-string

#### Example:

```
Router(config-ephone-dn)# label user1
```

Creates a
                                             				custom label that is displayed on the phone next to the line button that is
                                             				associated with this ephone-dn. The custom label replaces the default label,
                                             				which is the number that was assigned to this ephone-dn.

label-string —String of up to 30 alphanumeric
                                                      					 characters that provides the label text.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for Phones .

### Create Labels for
                           	 Directory Numbers on a SIP Phone

To create label to
                                 		  be displayed in place of a directory number for a SIP phone, intercom line,
                                 		  voice port, or a message-waiting indicator (MWI), perform the following steps
                                 		  for each label to be created.

Restriction

Only one label
                                             			 is permitted per directory number.

#### Before you begin

Cisco CME 3.4
                                          				or a later version.

Directory
                                          				number for which the label is to be created is already configured and must
                                          				already have a number assigned by using the number (voice register
                                                					 dn) command. For configuration information, see Create Directory Numbers for SIP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- number number

- label string

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register dn dn-tag

#### Example:

```
Router(config-register-global)# voice register dn 17
```

Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI).

Step 4

number number

#### Example:

```
Router(config-register-dn)# number 7001
```

Defines a
                                             				valid number for a directory number.

Step 5

label string

#### Example:

```
Router(config-register-dn)# label user01
```

Creates a text
                                             				identifier, instead of a phone-number display, for a directory number that
                                             				appears on a SIP phone console.

Step 6

end

#### Example:

```
Router(config-register-dn)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Verify
                           	 Labels

Use the show
                                                				  running-config command to verify your configuration. Descriptions
                                          			 for directory numbers are listed in the ephone-dn and voice-register dn
                                          			 portions of the output.

```
Router# show running-config ephone-dn  1  dual-line
		   number 150 secondary 151
		   label MyLine
		   call-forward busy 160 
		   call-forward noan 160 timeout 10
		   huntstop channel
		   no huntstop
		  !
		  !
		  !
		  voice-register dn 1
		   number 1101 
		   label MyLine
```

### Modify System
                           	 Message Display on SCCP Phone Screen

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- system message text-message

- url idle url idle-timeout seconds

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

system message text-message

#### Example:

```
Router(config-telephony)# system message ABC Company
```

Defines a text
                                             				message to display when a phone is idle.

text-message —Alphanumeric string to display.
                                                      					 Display uses proportional-width font, so the number of characters that are
                                                      					 displayed varies based on the width of the characters that are used. The
                                                      					 maximum number of displayed characters is approximately 30.

Step 5

url idle url idle-timeout seconds

#### Example:

```
Router(config-telephony)# url idle http://www.abcwrecking.com/public/logo idle-timeout 35
```

Defines the
                                             				location of a file to display on phones that are not in use and specifies the
                                             				interval between refreshes of the display, in seconds.

url —Any URL that conforms to RFC 2396.

seconds —Time interval between display refreshes,
                                                      					 in seconds. Range is 0 to 300.

Step 6

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

After configuring the url idle command, you must reset phones. See Use the reset Command on SCCP Phones .

### Verify System
                           	 Message Display

Use the show
                                                				  running-config command to verify your configuration. System
                                          			 message display is listed in the telephony-service portion of the output.

```
Router# show running-config telephony-service
		   fxo hook-flash
		   load 7960-7940 P00307020300
		   load 7914 S00104000100
		   max-ephones 100
		   max-dn 500
		   ip source-address 10.153.13.121 port 2000
		   max-redirect 20
		   timeouts ringing 100
		   system message XYZ Company
		   voicemail 7189
		   max-conferences 8 gain -6
		   call-forward pattern .T
		   moh flash:music-on-hold.au
		   multicast moh 239.10.10.1 port 2000
		   web admin system name server1 password server1
		   dn-webedit 
		   time-webedit 
		   transfer-system full-consult
		   transfer-pattern 92......
		   transfer-pattern 91..........
		   transfer-pattern 93......
		   transfer-pattern 94......
		   transfer-pattern 95......
		   transfer-pattern 96......
		   transfer-pattern 97......
		   transfer-pattern 98......
		   transfer-pattern 99......
		   transfer-pattern .T
		   secondary-dialtone 9
		   create cnf-files version-stamp Jan 01 2002 00:00:00
```

### Troubleshooting
                           	 System Message Display

Ensure that
                                          			 the HTTP server is enabled.

### Provision URLs for
                           	 Feature Buttons for SCCP Phones

To customize URLs
                                 		  for feature buttons in the Sep*.conf.xml configuration file for SCCP phones,
                                 		  perform the following steps.

Restriction

Operation of
                                                      				  these services is determined by the Cisco Unified IP phone capabilities and the
                                                      				  content of the specified URL.

Provisioning
                                                      				  a URL to access help screens using the i or ? buttons on a phone is not
                                                      				  supported.

Provisioning
                                                      				  the directory URL to select an external directory resource disables the
                                                      				  Cisco Unified CME local directory service.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- url { directories | information | messages | services } url

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

url { directories | information | messages | services } url

#### Example:

```
Router(config-telephony)# url directories http://10.4.212.4/localdirectory
```

Provisions
                                             				URLs for the four programmable feature buttons (Directories, Information,
                                             				Messages, and Services) on a supported Cisco Unified IP phone.

To use a
                                                      					 Cisco Unified Communications Manager directory as an external directory source,
                                                      					 you must list the MAC addresses of the phones in Cisco Unified Communications
                                                      					 Manager and reset the phones from Cisco Unified Communications Manager. You do
                                                      					 not need to assign ephone-dns to the phones for the phones to register with
                                                      					 Cisco Unified Communications Manager.

The url services command is also available in ephone-template configuration mode. If you use an
                                                      					 ephone template to provision the Services feature button on one or more SCCP
                                                      					 phones and you configure the url services command in telephony-service configuration mode, the value set in
                                                      					 telephony-service configuration mode appears first in the list of options
                                                      					 displayed when the phone user presses the Services feature button.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you want to
                                 		  create an ephone template to provision multiple URLs for the Services feature
                                 		  button on supported individual SCCP phones, see Templates .

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for Phones .

### Provision URLs for
                           	 Feature Buttons on SIP Phones

To customize URLs
                                 		  for feature buttons in the SEPDEFAULT.cnf configuration profile for SIP IP
                                 		  phones, perform the following steps.

Restriction

Operation of
                                                      				  these services is determined by the Cisco Unified IP phone capabilities and the
                                                      				  content of the specified URL.

Provisioning
                                                      				  the directory URL to select an external directory resource disables the
                                                      				  Cisco Unified CME local directory service.

#### Before you begin

Cisco CME 3.4 or a
                                 		  later version.

Support for idle url is available only on Unified CME 12.0 and later
                                 		  versions.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- url { authentication | directory | service | idle } url

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)#
```

Enters
                                             				telephony-service configuration mode.

Step 4

url { authentication | directory | service | idle } url

#### Example:

```
Router(config-register-global)# url directory http://10.0.0.11/localdirectory
```

```
Router(config-register-global)# url service http://10.0.0.4/CCMUser/123456/urltest.html
```

```
Router(config-register-global)# url idle http://www.mycompany.com/files/logo.xml idle-timeout 12
```

Associates a
                                             				URL with the programmable feature buttons on SIP phones.

url authentication url — Uses the information at the specified URL to
                                                      					 validate requests made to the phone web server.

url directory url — Uses the information at the specified URL
                                                      					 for the Directories button display.

url service url [ root ] — Uses the information at the specified URL for
                                                      					 the Services button display.

url idle url — Defines the location of a file to display on
                                                      					 phones that are not in use and specifies the interval between refreshes of the
                                                      					 display, in seconds.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Troubleshooting
                           	 URL Provisioning for Feature Buttons

Ensure the
                                          			 HTTP server is enabled and that there is communication between the
                                          			 Cisco Unified CME router and the server.

### Modify Vendor
                           	 Parameters for All SCCP Phones

To configure
                                 		  programmable phone and display parameters in the vendorConfig section of the
                                 		  SepDefault.conf.xml configuration file for all phones, perform the following
                                 		  steps.

Restriction

Only the
                                                      				  parameters supported by the currently loaded firmware are available.

The number
                                                      				  and type of parameters may vary from one firmware version to the next.

Only those
                                                      				  parameters that are supported by a Cisco Unified IP phone and firmware version
                                                      				  are implemented. Parameters that are not supported are ignored.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- service phone parameter-name parameter-value

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

service phone parameter-name parameter-value

#### Example:

```
Router(config-telephony)# service phone
daysDisplayNotActive 1,2,3,4,5,6,7
Router(config-telephony)# service phone
displayOnTime 07:30
Router(config-telephony)# service phone
displayOnDuration 10:00
Router(config-telephony)# service phone
displayIdleTimeout 00.01
```

Sets display
                                             				and phone functionality for all IP phones that support the configured
                                             				parameters and to which this template is applied.

The
                                                      					 parameter name is word and case-sensitive. See Cisco Unified CME Command
                                                         						Reference for a list of parameters.

This
                                                      					 command can also be configured in ephone- template configuration mode and
                                                      					 applied to one or more phones.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for Phones .

### Modify Vendor
                           	 Parameters for a Specific SCCP Phone

To configure
                                 		  parameters in the vendorConfig section of the Sep*.conf.xml configuration file
                                 		  for an individual SCCP phone, perform the following steps.

Restriction

Cisco Unified CME 4.0 or a later version.

System must
                                                      				  be configured to for per-phone configuration files. For configuration
                                                      				  information, see Define Per-Phone Configuration Files and Alternate Location for SCCP Phones .

Only the
                                                      				  parameters supported by the currently loaded firmware are available.

The number
                                                      				  and type of parameters may vary from one firmware version to the next.

Only those
                                                      				  parameters that are supported by a Cisco Unified IP phone and firmware version
                                                      				  are implemented. Parameters that are not supported are ignored.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- service phone parameter-name parameter-value

- exit

- ephone phone-tag

- ephone-template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-template template-tag

#### Example:

```
Router (config)# ephone-template 15
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

Step 4

service phone parameter-name parameter-value

#### Example:

```
Router(config-telephony)# service phone daysDisplayNotActive 1,2,3,4,5,6,7 
Router(config-telephony)# service phone displayOnTime 07:30 
Router(config-telephony)# service phone displayOnDuration 10:00 
Router(config-telephony)# service phone displayidleTimeout 00.01
```

Sets
                                             				parameters for all IP phones that support the configured functionality and to
                                             				which this template is applied.

The
                                                      					 parameter name is word and case-sensitive. See the Cisco Unified CME Command Reference for a
                                                      					 list of parameters.

This
                                                      					 command can also be configured in telephony-service configuration mode. For
                                                      					 individual phones, the template configuration for this command overrides the
                                                      					 system-level configuration for this command.

Step 5

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits from
                                             				this command mode to the next highest mode in the configuration mode hierarchy.

Step 6

ephone phone-tag

#### Example:

```
Router(config)# ephone 1
```

Enters ephone
                                             				configuration mode.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 15
```

Applies an
                                             				ephone template to the ephone that is being configured.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for Phones .

### Troubleshooting
                           	 Vendor Parameter Configuration

Step 1

Ensure that
                                          			 the templates have been properly applied to the phones.

Step 2

Ensure that
                                          			 you use the create
                                                				  cnf-files command to regenerate configuration files and reset the
                                          			 phones after you apply the templates.

Step 3

Use the show telephony-service
                                                				  tftp-bindings command to display the configuration files that are
                                          			 associated with individual phones

#### Example:

```
Router# show telephony-service tftp-binding tftp-server system:/its/SEPDEFAULT.cnf  
			 tftp-server system:/its/SEPDEFAULT.cnf alias SEPDefault.cnf  
			 tftp-server system:/its/XMLDefault.cnf.xml alias XMLDefault.cnf.xml  
			 tftp-server system:/its/ATADefault.cnf.xml  
			 tftp-server system:/its/XMLDefault7960.cnf.xml alias SEP00036B54BB15.cnf.xml 
			 tftp-server system:/its/germany/7960-font.xml alias German_Germany/7960-font.xml  
			 tftp-server system:/its/germany/7960-dictionary.xml alias German_Germany/7960-dictionary.xml  
			 tftp-server system:/its/germany/7960-kate.xml alias German_Germany/7960-kate.xml  
			 tftp-server system:/its/germany/SCCP-dictionary.xml alias German_Germany/SCCP-dictionary.xml  
			 tftp-server system:/its/germany/7960-tones.xml alias Germany/7960-tones.xml
```

Step 4

Use the debug tftp
                                                				  events command to verify that the phone is accessing the file
                                          			 when you reboot the phone.

### Configure One-Way
                           	 Push-to-Talk on Cisco Unified SCCP Wireless IP Phones

To associate a
                                 		  phone button with the thumb button on a wireless phone for one-way Push-to-Talk
                                 		  (PTT) functionality in Cisco Unified CME, perform the following steps.

Restriction

Supported on
                                             			 Cisco Unified Wireless IP Phone 7921 and 7925 only.

#### Before you begin

Cisco Unified CME 7.0 or a later version.

Cisco phone
                                          				firmware version 1.0.4 or a later version.

System must be
                                          				configured to for per-phone configuration files. For configuration information,
                                          				see Define Per-Phone Configuration Files and Alternate Location for SCCP Phones .

Phone button
                                          				to be associated with the thumb button must be configured with an intercom DN
                                          				that targets a paging number. For configuration information, see Intercom Lines .

Paging group
                                          				to be dialed by the intercom line must be configured. Targeted paging group can
                                          				be unicast or multicast or both. For configuration information, see Paging .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- service phone thumbButton1 PTTH button_number

- exit

- ephone phone-tag

- ephone-template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-template template-tag

#### Example:

```
Router (config)# ephone-template 12
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

Step 4

service phone thumbButton1 PTTH button_number

#### Example:

```
Router(config-ephone-template)# service phone thumbButton1 PTTH6
```

Specifies
                                             				which button is to go off hook when user presses the thumb button.

button_number —Button on phone that is configured
                                                      					 with an intercom dn that targets a paging number. Range is 1 to 6.

There are
                                                      					 no spaces in the PTTH and button_number keyword/argument combination.

This
                                                      					 command can also be configured in telephony-service configuration mode. For
                                                      					 individual phones, the template configuration for this command overrides the
                                                      					 system-level configuration for this command.

Step 5

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits from
                                             				this command mode to the next highest mode in the configuration mode hierarchy.

Step 6

ephone phone-tag

#### Example:

```
Router(config)# ephone 1
```

Enters ephone
                                             				configuration mode.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 12
```

Applies an
                                             				ephone template to the ephone that is being configured.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Configure Cisco Jabber for CSF Client in Unified CME

#### Before you begin

Cisco Jabber versions supported on Unified CME are now End-of-Life (EOL). Hence, there is no active support on Unified CME
                                 for Cisco Jabber clients.

### SUMMARY STEPS

- enable

- configure terminal

- ip http secure-server

- ip http secure-port port number

- voice register dn dn-tag

- number number

- voice register pool phone-tag

- id device-id-name name

- type type

- number number

- username username password password

- description string

- exit

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables the
                                             				privileged EXEC mode. Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters the
                                             				global configuration mode.

Step 3

ip http secure-server

#### Example:

```
Router(config)# ip http secure-server
```

Enables a
                                             				secure HTTP (HTTPS) server. The HTTPS server uses the Secure Sockets Layer
                                             				(SSL) Version 3 protocol.

Step 4

ip http secure-port port number

#### Example:

```
Router(config)# ip http secure-port 8443
```

Sets the HTTPS
                                             				server port number for listening.

Step 5

voice register dn dn-tag

#### Example:

```
Router(config)# voice register dn 1
```

Creates
                                             				directory numbers for the SIP IP phones that are directly connected to Cisco
                                             				Unified CME

Step 6

number number

#### Example:

```
Router(config-register-dn)# number 991001
```

Defines the
                                             				numbers for the SIP IP phones.

Step 7

voice register pool phone-tag

#### Example:

```
Router# voice register pool  1
```

Sets the
                                             				phone type for the SIP IP phones on a Cisco Unified CME system.

Step 8

id device-id-name name

#### Example:

```
Router(config-register-pool)# id device-id-name JabberWIN
```

Specifies the device ID of a phone type.

For a list of supported device IDs, see Cisco Unified Communications Manager Express Command Reference .

Assigns a name to a phone type.

name —String that specifies the SIP soft client device ID name. Device ID name string can be up to 32 characters.

Step 9

type type

#### Example:

```
Router(config-register-pool)# type Jabber-CSF-Client
```

Defines the
                                             				phone type.

Step 10

number number

#### Example:

```
Router(config-register-pool)# number 1
```

Defines the
                                             				numbers for the SIP IP phones.

Step 11

username username password password

#### Example:

```
Router(config-register-pool))# username jabber1 password jabber1
```

Sets the
                                             				username and password.

Username — Specifies the username of the phone type.

Password — Specifies the password of the phone type.

Step 12

description string

#### Example:

```
Router(config-register-pool)# description Jabber-CSF-Client
```

Associates a
                                             				description with the Cisco Jabber client. Enter a string of up to 64
                                             				characters. A maximum of 128 characters, including spaces.

Step 13

exit

#### Example:

```
Router(config-register-pool)# exit
```

Exits the
                                             				voice register-pool configuration mode.

Step 14

end

#### Example:

```
Router(config)# end
```

Exits the
                                             				privileged EXEC configuration mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for Phones .

## Configuration Examples for Cisco Unified IP Phone Options

### Example for Configuring Cisco Jabber

The following example shows phone type Cisco Jabber configured under
                                 		  voice register pool 10:

```
!  
		voice register dn  10
		 number 1089
		 call-forward b2bua busy 1500
		 call-forward b2bua mailbox 1500  
		 call-forward b2bua noan 1500 timeout 20
		 pickup-call any-group
		 pickup-group 1
		 name CME SIP iPhone
		 label CME SIP iPhone
		!         
		!
		voice register pool  8
		registration-timer max 720 min 660
		 park reservation-group 1
		 session-transport tcp
		 type CiscoMobile-iOS 
		 number 1 dn 10
		 dtmf-relay rtp-nte
		!         
		ephone-dn  61
		 number 1061
		 park-slot reservation-group 1 timeout 10 limit 2 recall retry 2 limit 2
		!
```

### Example for
                           	 Configuring Cisco Jabber CSF Client

The following
                                 		  example shows how to configure the Cisco Jabber CSF client installed in full UC
                                 		  mode:

```
!
voice register dn 1
number 991001
name Jabber-CSF-Client-1
label   Jabber-CSF-Client-1
!
voice register pool 1
id device-id-name jabber_csf_1
type Jabber-CSF-Client
number 1 dn 1
username john password john123
codec g711ulaw
camera
video
!
ip http secure-server
ip http secure-port 8443
```

The following
                                 		  example shows how to configure the Cisco Jabber CSF client in phone-only mode
                                 		  from CME under voice register global:

```
voice register global
 phone-mode phone-only
!
voice register pool  1
 id device-id-name winJabber 
 number 1 dn 1
 type Jabber-CSF-Client
 username 1111022 password 1111022
!
```

The following
                                 		  example shows how to configure the Cisco Jabber CSF client in phone-only mode
                                 		  from CME under voice register pool:

```
voice register pool  1
 id device-id-name winJabber 
 number 1 dn 1
 type Jabber-CSF-Client
 username 1111022 password 1111022
 phone-mode phone-only
!
```

The following
                                 		  example shows how to configure the Cisco Jabber CSF client in phone-only mode
                                 		  from CME under voice register template:

```
voice register template  1
 phone-mode phone-only
!
voice register pool  2
 id device-id-name winJabber
 type Jabber-CSF-Client
 number 1 dn 2
 username 1111023 password 1111023
 template 1
!
```

For Cisco Jabber CSF client (version 12.1.0 and onwards) support, Unified CME 12.5 is configured as the DNS Server. The host
                                 machine of the Jabber client is configured to point to Unified CME that is configured as the DNS server. The following example
                                 shows how to configure Unified CME 12.5 as DNS Server to support the Cisco Jabber CSF client, Version 12.1.0 for Mac and Windows
                                 (Phone-only Mode):

```
enable
configure terminal
ip dns server
ip host _sip_tcp.cisco.com srv 0 1 5060 cme.cisco.com
ip host _sip_udp.cisco.com srv 0 1 5060 cme.cisco.com
ip host _sips_tcp.cisco.com srv 0 1 5060 cme.cisco.com
ip host _cisco-uds._tcp.cisco.com srv 0 1 8443 cme.cisco.com
ip host uds._tcp.cisco.com srv 0 1 8443 cme.cisco.com
ip host _collab-edge._tls.cisco.com srv 0 1 8443 cme.cisco.com
ip host cme.cisco.com 10.64.86.106 (Note: IP Address of Unified CME 12.5)
ip host _cisco-phone-http.tcp.cisco.com srv 0 1 8443 cme.cisco.com
```

### Example for Configuring Dial Rules for Cisco Softphone SIP
                           	 Client

The following example shows dial rules configured under voice register
                                 		  template 2:

```
!
voice register template  2
 url ldapServer ldap.abcd.com
 url AppDialRule tftp://10.1.1.1/AppDialRules.xml
 url DirLookupRule tftp://10.1.1.1/DirLookupRules.xml
!
```

The following is a sample of Application Dial Rule content:

```
Router#more flash:AppDialRules.xml
<?xml version="1.0" encoding="UTF-8"?><DialRules<
        <DialRule BeginsWith="+1" NumDigits="12" DigitsToRemove="1" PrefixWith="9"/>
        <DialRule BeginsWith="+1" NumDigits="12" DigitsToRemove="1" PrefixWith="9"/>
        <DialRule BeginsWith="919" NumDigits="10" DigitsToRemove="3" PrefixWith="9"/>
        <DialRule BeginsWith="1" NumDigits="11" DigitsToRemove="0" PrefixWith="9"/>
        <DialRule BeginsWith="" NumDigits="10" DigitsToRemove="0" PrefixWith="91"/>
        <DialRule BeginsWith="" NumDigits="7" DigitsToRemove="0" PrefixWith="9"/>
        <DialRule BeginsWith="+" NumDigits="13" DigitsToRemove="1" PrefixWith="9011"/>
        <DialRule BeginsWith="+" NumDigits="14" DigitsToRemove="1" PrefixWith="9011"/>
        <DialRule BeginsWith="+" NumDigits="15" DigitsToRemove="1" PrefixWith="9011"/>

        <DialRule BeginsWith="+" NumDigits="12" DigitsToRemove="1" PrefixWith="9011"/>
        <DialRule BeginsWith="+" NumDigits="11" DigitsToRemove="1" PrefixWith="9011"/>
</DialRules>
```

### Example for Excluding Local Services from Cisco Unified SIP IP
                           	 Phones

The following example shows how the exclude command is used to exclude from the Cisco Unified SIP IP phone’s user interface
                                 		  the availability of two local services. These services are Local Directory and
                                 		  My Phone Apps.

```
Router(config)# voice register pool 80
Router(config-register-pool)# exclude directory Router(config-register-pool)# exclude myphoneapps
```

### Example to Create Text Labels for Ephone-dns

The following example creates text labels for two ephone-dns:

```
ephone-dn 1
 number 2001
 label Sales
ephone-dn 2
 number 2002
 label Engineering
```

### Example for Phone Header Bar Display

The following example provides the full E.164 number for a phone line
                                 		  in the phone header bar:

```
ephone-dn 55
 number 2149
 description 408-555-0149
ephone-dn 56
 number 2150
ephone 12
 button 1:55 2:56
```

### Example for System Text Message Display

The following example specifies text that should display on IP phones
                                 		  when they are not in use:

```
telephony-service
 system message ABC Company
```

### Example for System File Display

The following example specifies that a file called logo.htm should be
                                 		  displayed on IP phones when they are not in use:

```
telephony-service
 url idle http://www.abcwrecking.com/public/logo.htm idle-timeout 35
```

### Example for URL Provisioning for Directories, Services, and Messages
                           	 Buttons

The following example provisions the Directories, Services, and
                                 		  Messages buttons:

```
telephony-service
 url directories http://10.4.212.4/localdirectory
 url services http://10.4.212.4/CCMUser/123456/urltest.html
 url messages http://10.4.212.4/Voicemail/MessageSummary.asp
```

### Example for Programmable VendorConfig Parameters

The following partial output shows a template in which programmable
                                 		  parameters for phone and display functionality have been configured by using
                                 		  the service phone command:

```
ephone-template 1
		   button-layout 7931 1
		   service phone daysDisplayNotActive 1,2,3,4,5,6,7
		   service phone backlightOnTime 07:30
		   service phone backlightOnDuration 10:00
		   service phone backlightidleTimeout 00.01
```

In the following example, the PC port is disabled on phones 26 and 27.
                                 		  All other phones have the PC port enabled.

```
ephone-template  8
		   service phone pcPort 1
		  !
		  !
		  ephone  26
		   mac-address 1111.1111.1001
		   ephone-template 8
		   type 7960
		   button  1:26
		  !
		  !
		  ephone  27
		   mac-address 1111.2222.2002
		   ephone-template 8
		   type 7960
		   button  1:27
```

### Example for
                           	 Push-to-Talk (PTT) on Cisco Unified Wireless IP Phones in Cisco Unified
                           	 CME

The following
                                 		  partial output shows a template in which one-way PTT is configured by using the service phone
                                       				thumbButton1 command:

```
ephone-template 12
		service phone thumbButton1 PTTH6
		!
      !
      ephone-dn 10
      intercom 1050
      ephone-dn 50
      number 1050
      paging
      !
      !

		ephone 1
		type 7921
		   button 1:1 6:10
		!
		!
		ephone 2
      button 1:2
      paging-dn 50
      ephone 3
      button 1:3
      paging-dn 50
      ephone 4
      button 1:1
      paging-dn 50
```

## Feature
                        	 Information for Cisco Unified IP Phone Options

The following
                           		table provides release information about the feature or features described in
                           		this module. This table lists only the software release that introduced support
                           		for a given feature in a given software release train. Unless noted otherwise,
                           		subsequent releases of that software release train also support that feature.

Use Cisco Feature
                           		Navigator to find information about platform support and Cisco software image
                           		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn .
                           		An account on Cisco.com is not required.

Feature Name

Unified CME Version

Feature
                                       				  Information

Support for Cisco Jabber

12.5

Added Support for Cisco Jabber CSF Client MAC and Windows
                                       								(Phone-only), Version 12.1(0).

Support for Cisco Jabber

8.6

Added
                                       				  support for Cisco Jabber.

My Phone Apps for Cisco Unified SIP IP Phones

9.0

Adds support for My Phone Apps feature on Cisco Unified SIP IP phones.

Clear
                                       				  Directory Entries

8.6

Provides
                                       				  ability to clear the display of call-history details such as missed, placed,
                                       				  and received call entries on a Cisco Unified  SCCP IP phone’s display screen.

Fixed
                                       				  Line/Feature Buttons

4.0(2)

Provides two
                                       				  preconfigured fixed sets of feature buttons for provisioning a Cisco Unified IP
                                       				  Phone 7931G.

Header Bar
                                       				  Display

3.4

Added
                                       				  support for modifying header bar display on SIP phones.

2.01

Phone header
                                       				  bar display is introduced.

Labels for
                                       				  Directory Numbers

3.4

Added
                                       				  support for label display on SIP phones.

3.0

Ephone-dn
                                       				  labels were introduced.

Programmable
                                       				  Vendor Parameters

4.0

Added
                                       				  support for configuring programmable phone and display functionality at a phone
                                       				  level for SCCP phones.

3.4

Added
                                       				  support for configuring programmable phone and display functionality for SIP
                                       				  phones.

3.2.1

Added
                                       				  support for programmable phone and display functionality in vendorConfig
                                       				  portion of configuration file. Implementation of configuration is firmware
                                       				  version dependent.

System
                                       				  Message Display

3.0

System
                                       				  message display on idle phones using text messages was introduced.

2.1

System
                                       				  message display on idle phones using HTML files was introduced.

URL
                                       				  Provisioning for Feature Buttons

12.0

Added
                                       				  support for Idle URL functionality on SIP phones.

4.2

Added
                                       				  support for configuring an ephone template to provision multiple URLs for the
                                       				  Services feature button phones.

3.4

Added
                                       				  support for provisioning customized URLs for programmable feature buttons on
                                       				  supported SIP phones.

2.0

Provisioning customized URLs for programmable feature buttons
                                       				  was introduced.

| Note | If the
                                          		  button-layout feature is configured in both ephone-template and logout profile
                                          		  (extension mobility) mode, configuration in the latter takes precedence.
                                          		  Button-layout configuration under ephone mode takes precedence in phones that
                                          		  do not have extension mobility (EM). |
|---|---|

| Note | Privacy button is
                                          		  counted as a feature button on phones that support privacy button and do not
                                          		  have any feature button configured through the feature-button command. |
|---|---|

| Note | Before Cisco
                                          		  Unified CME 9.0, you must configure the Local Directory service with the
                                          		  internal URL address. In Cisco Unified CME 9.0 and later versions, the internal URL address
                                          		  is the default when no external URL address is configured. |
|---|---|

| Note | Cisco Jabber versions supported on Unified CME are now End-of-Life. Hence, there is no active support for Cisco Jabber on
                                          Unified CME 14.1 or earlier releases. |
|---|---|

| Note | Cisco Jabber client versions supported on Unified CME are now End-of-Life (EOL). Hence, there is no active support on Unified
                                          CME for Cisco Jabber clients. |
|---|---|

| Cisco CSF Device Type | Unified CME Supported Version | Jabber Client Version |
|---|---|---|
| Cisco Jabber for MAC (phone-only) and Windows (phone-only) | 10.0 | 9.1.0 |
| 10.5 | 9.2.1 |
| 12.5 | 12.1.0 |

| Note | The System Message command is supported only for SCCP IP phones registered to CME. It is not supported for SIP IP phones in CME mode. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | service phone parameter-name parameter-value Example: Router(config-telephony)# service phone paramEdibility 1 | Enables the edit user settings. |
| Step 5 | voice register global Example: Router(config-telephony)# voice register global | Enters voice register global configuration mode. |
| Step 6 | create profile Example: Router(config-register-global)# create profile | Generates provisioning files required for SIP phones and writes
                                             				the file to the location specified with the tftp-path command. |
| Step 7 | end Example: Router(config-register-global)# end | Exits configuration mode and enters privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | Enter one of the following commands: ephone phone-tag ephone template template tag Example: Router(config)# ephone 10 | Enters ephone configuration mode. phone-tag —Unique number of the phone for which you want to exclude local services such as Extension Mobility, My Phone Apps, and Local
                                                      Directory. |
| Step 4 | exclude [ em \| myphoneapp \| directory \| call-history ] Example: Router(config-ephone)#exclude call-history | Excludes local
                                             				services (EM, My Phone Apps, Local Directory, and Call History) from displaying
                                             				on phone’s user interface. em—Excludes Extension Mobility (EM) from the phone’s user
                                                      					 interface. myphoneapp
                                                      					 —Excludes My Phone App service from the phone’s user interface. directory
                                                      					 —Excludes Local Directory service from the phone’s user interface. call-history—Excludes entries from Call History on the phone’s
                                                      					 user interface. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template
                                                				  tag Example: Router(config)#voice register template 8 | Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME. |
| Step 4 | url { AppDialRule string \| DirLookupRule string \| ldapServer string \| idle url \| service url } Example: Router(config-register-temp)# url ldapServer ldap.abcd.com Router(config-register-temp)# url AppDialRule tftp://10.1.1.1/AppDialRules.xml Router(config-register-temp)# url DirLookupRule tftp://10.1.1.1/DirLookupRules.xml Router(config-register-temp)# url idle http://www.mycompany.com/files/logo.xml idle-timeout 12 Router(config-register-temp)# url service http://10.0.0.4/CCMUser/123456/urltest.html | Allows to
                                             				define SIP phone URLs to configure Application Dial Rule, Directory Lookup Dial
                                             				Rule, LDAP server, idle url, and service url in voice register template
                                             				configuration mode. ldapserver string —LDAP server URL. AppDialRule string —Application dial rule URL. DirLookupRule string —Directory lookup rule URL. idle url —Defines the location of a file to display on
                                                      					 phones that are not in use and specifies the interval between refreshes of the
                                                      					 display, in seconds. service url —Uses the information at the specified URL for
                                                      					 invoking phone services. |
| Step 5 | voice register pool pool
                                                				  tag Example: Router(config)#voice register pool 8 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. |
| Step 6 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 15 | Enters
                                             				ephone-template configuration mode to create an ephone template. |
| Step 4 | button-layout phone-type { 1 \| 2 } Example: Router(config-ephone-template)# button-layout 7931 2 | Specifies
                                             				which fixed set of feature buttons appears on a Cisco Unified IP Phone 7931G
                                             				that uses a template in which this is configured. 1 —Includes two predefined feature buttons: button
                                                      					 24 is Menu and button 23 is Headset. 2 —Includes four predefined feature buttons: button
                                                      					 24 is Menu; button 23 is Headset; button 22 is Directories; and button 21 is
                                                      					 Messages. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits from
                                             				this command mode to the next highest mode in the configuration mode hierarchy. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone
                                             				configuration mode. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 15 | Applies an
                                             				ephone template to the ephone that is being configured. |
| Step 8 | end Example: Router(config-ephone)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template
                                                				  tag Example: Router(config)# ephone 10 | Enters ephone
                                             				template configuration mode to create an ephone template. |
| Step 4 | button-layout [ button-string \| button-type ] Example: Router(config-ephone-template)#button-layout 1 line
Router(config-ephone-template)#button-layout 2,5 speed-dial
Router(config-ephone-template)#button-layout 3,6 blfspeed-dial
Router(config-ephone-template)#button-layout 4,7,9 feature
Router(config-ephone-template)# button-layout 8,11 url | Assigns
                                             				physical button numbers or ranges of numbers with button types. button-string —Specifies a coma separated list of
                                                      					 physical button number or ranges of button numbers. button-type —Specifies one of the following button
                                                      					 types: Line, Speed-Dial, BLF-Speed-Dial, Feature, URL. Button number specifies
                                                      					 the relative display order of the button within the button type (line button,
                                                      					 speed-dial, blf-speed-dial, feature-button or url-button). Note To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button. Note When no
                                                         				  feature-buttons are configured, privacy button is counted as a feature button. | Note | To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button. | Note | When no
                                                         				  feature-buttons are configured, privacy button is counted as a feature button. |
| Note | To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button. |
| Note | When no
                                                         				  feature-buttons are configured, privacy button is counted as a feature button. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits from
                                             				this command mode to the next highest mode in the configuration mode hierarchy. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone
                                             				configuration mode. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 10 | Applies an
                                             				ephone template to the ephone that is being configured. |
| Step 8 | end Example: Router(config-ephone)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Note | To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button. |
|---|---|

| Note | When no
                                                         				  feature-buttons are configured, privacy button is counted as a feature button. |
|---|---|

| Note | You can not
                                             			 change the button number in the line button or index command through button
                                             			 layout configuration because the button number specifies the relative display
                                             			 order of the button within the button type (line button, speed-dial,
                                             			 blf-speed-dial, feature button, or url button). |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 5 | Enters voice
                                             				register template configuration mode to create a SIP phone template. template-tag—Range: 1 to 10. |
| Step 4 | button-layout [ button-string ] [ button-type ] Example: Router(config-register-template)#button-layout 1 line
Router(config-register-template)#button-layout 2, 5 speed-dial
Router(config-register-template)#button-layout 3, 6 blfspeed-dial
Router(config-register-template)#button-layout 4,7,9 feature-button
Router(config-register-template)# button-layout 8,11 url-button | Assigns
                                             				physical button numbers or ranges of numbers with button types. button-string —Specifies a coma separated list of
                                                      					 physical button number or ranges of button numbers. button-type —Specifies one of the following button
                                                      					 types: Line, Speed-Dial, BLF-Speed-Dial, Feature, URL. Note To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button. Note Privacy-button is counted as a feature-button in this
                                                         				  configuration if no feature-button is configured. | Note | To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button. | Note | Privacy-button is counted as a feature-button in this
                                                         				  configuration if no feature-button is configured. |
| Note | To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button. |
| Note | Privacy-button is counted as a feature-button in this
                                                         				  configuration if no feature-button is configured. |
| Step 5 | exit Example: Router(config-register-template)# exit | Exits voice
                                             				register template configuration mode. |
| Step 6 | voice register pool pool-tag Example: Router(config)# voice register pool 10 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. |
| Step 7 | template template-tag Example: Router(config-register-pool)# template 5 | Applies a SIP
                                             				phone template to the phone you are configuring. template-tag — Template tag that was created with
                                                      					 the voice register template command in Step 3 . |
| Step 8 | end Example: Router(config-register-pool)# end | Exits to
                                             				privileged EXEC mode. |

| Note | To
                                                         				  facilitate phone provisioning, the first line button should always be a line
                                                         				  button. |
|---|---|

| Note | Privacy-button is counted as a feature-button in this
                                                         				  configuration if no feature-button is configured. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                      					 template that is being created. Range: 1 to 10. |
| Step 4 | url-button [ index number ] [ url location] [ url name ] Example: Router(config-register-temp)url-button 1 http:// www.cisco.com | Configures a
                                             				service url feature button on a line key. Index
                                                      					 number—Unique index number. Range: 1 to 8. url location —Location of the url. url name —Service
                                                      					 url with maximum length of 31 characters. |
| Step 5 | exit Example: Router(config-register-temp)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | voice register pool phone-tag Example: Router(config)# voice register pool 12 | Enters ephone
                                             				configuration mode. phone-tag —Unique number that identifies this
                                                      					 ephone during configuration tasks. |
| Step 7 | template template-tag Example: Router(config-register-pool)# template 5 | Applies the
                                             				ephone template to the phone. template-tag —Unique identifier of the template
                                                      					 that you created in Step 3 . |
| Step 8 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone template template-tag Example: Router(config)# ephone template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                      					 template that is being created. Range: 1 to 10. |
| Step 4 | url-button index type \| url [ name ] Example: Router#(config-ephone-template)#url-button 1 myphoneapp 
				Router(config-ephone-template)#url-button 2 em 
				Router(config-ephone-template)#url-button 3 snr
				Router (config-ephone-template)#url-button 4 http://www.cisco.com | Configures a
                                             				service url feature button on a line key. Index —Unique index number. Range: 1 to 8. type —Type of service url button. Following types
                                                      					 of url service buttons are available: myphoneapp: My phone application configured under phone user
                                                               						  interface. em:
                                                               						  Extension Mobility snr:
                                                               						  Single Number Reach url
                                                            						  name —Service url with maximum length of 31 characters. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)#ephone 36 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                      					 this ephone during configuration tasks. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 5 | Applies an
                                             				ephone template to the ephone that is being configured. |
| Step 8 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                      					 template that is being created. Range: 1 to 10. Note Feature
                                                         				  button can be configured under voice register
                                                               						pool or voice register
                                                               						template configuration mode. If both configurations are applied
                                                         				  to the voice register
                                                               						pool , the feature button configuration under voice register
                                                               						pool takes precedence. | Note | Feature
                                                         				  button can be configured under voice register
                                                               						pool or voice register
                                                               						template configuration mode. If both configurations are applied
                                                         				  to the voice register
                                                               						pool , the feature button configuration under voice register
                                                               						pool takes precedence. |
| Note | Feature
                                                         				  button can be configured under voice register
                                                               						pool or voice register
                                                               						template configuration mode. If both configurations are applied
                                                         				  to the voice register
                                                               						pool , the feature button configuration under voice register
                                                               						pool takes precedence. |
| Step 4 | feature-button [ index ] [ feature identifier ] Example: Router(config-voice-register-template)feature-button 1 DnD Router(config-voice-register-template)feature-button 2 EndCall Router(config-voice-register-template)feature-button 3 Cfwdall | Configures a
                                             				feature button on line key. index —One of the 12 index numbers for a specific
                                                      					 feature type. feature identifier —Unique identifier for a
                                                      					 feature. One of the following feature or stimulus IDs: Redial, Hold, Trnsfer,
                                                      					 Cfwdall, Privacy, MeetMe, Confrn, Park, Pickup, Gpickup, Mobility, NewCall,
                                                      					 EndCall, Dnd, ConfList, NewCall, HLog, Trnsfer. |
| Step 5 | exit Example: Router(config-register-temp)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | voice register pool phone-tag Example: Router(config)# voice register pool 12 | Enters ephone
                                             				configuration mode. phone-tag —Unique number that identifies this
                                                      					 ephone during configuration tasks. |
| Step 7 | template template-tag Example: Router(config-register-pool)# template 5 | Applies the
                                             				ephone template to the phone. template-tag —Unique identifier of the template
                                                      					 that you created in Step 3 |
| Step 8 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Feature
                                                         				  button can be configured under voice register
                                                               						pool or voice register
                                                               						template configuration mode. If both configurations are applied
                                                         				  to the voice register
                                                               						pool , the feature button configuration under voice register
                                                               						pool takes precedence. |
|---|---|

| Note | Answer,
                                                      				  Select, cBarge, Join, and Resume features are not supported as PLKs. Feature
                                                      				  buttons are only supported on Cisco Unified IP Phones 6911, 7941, 7942, 7945,
                                                      				  7961, 7962, 7965. 7970, 7971, and 7975 with SCCP v12 or later versions. Any features
                                                      				  available through hard button are not be provisioned. Use the show ephone
                                                      				  register detail command to verify why the features buttons are not provisioned. Not all
                                                      				  feature buttons are supported on Cisco Unified IP Phone 6911 phone. Call
                                                      				  Forward, Pickup, Group Pickup, and MeetMe are the only feature buttons
                                                      				  supported on the Cisco Unified IP Phone 6911. The
                                                      				  privacy-button is available on Cisco Unified IP phones running a SCCP v8 or
                                                      				  later. Privacy-buttton is overridden by any other feature-button available. Locales are
                                                      				  not supported on Cisco Unified IP Phone 7914. Locales are
                                                      				  not supported for Cancel Call Waiting or Live Recording feature-buttons. The feature
                                                      				  state for DnD, Hlog, Privacy, Login, and Night Service feature-buttons are
                                                      				  indicated by an LED. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone template template-tag Example: Router(config)# ephone template 10 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone template that is being created. Range: 1 to 10. |
| Step 4 | feature-button index feature
                                                				  identifier Example: Router(config-ephone-template)feature-button 1 hold | Configures a
                                             				feature button on line key index —index number, one from 25 for a specific feature type. feature identifier —feature ID or stimulus ID. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 5 | Enters ephone configuration mode. phone-tag —Unique sequence number that identifies this ephone during configuration tasks. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 10 | Applies an ephone template to the ephone that is being configured. |
| Step 8 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag or ephone
                                                					 template template
                                                				  tag Example: Router(config)# ephone 10 | Enters ephone
                                             				configuration mode. phone-tag —Unique number of the phone for which you
                                                   					 want to exclude local services such as Extension Mobility, My Phone Apps, and
                                                   					 Local Directory. |
| Step 4 | exclude [ em \| myphoneapp \| directory ] Example: Router(config-ephone)#exclude directory em | Excludes local
                                             				services (EM, My Phone Apps, and Local Directory) from displaying on phone’s
                                             				user interface. em—Excludes Extension Mobility (EM) from the phone’s user
                                                   					 interface. myphoneapp
                                                   					 —Excludes My Phone App service from the phone’s user interface. directory
                                                   					 —Excludes Local Directory service from the phone’s user interface. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 55 | Enters
                                             				ephone-dn configuration mode. |
| Step 4 | description display-text Example: Router(config-ephone-dn)# description 408-555-0134 | Defines a
                                             				description for the header bar of a display-capable IP phone on which this
                                             				ephone-dn appears as the first line. display-text —Alphanumeric character string, up to
                                                      					 40 characters. String is truncated to 14 characters in the display. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | This feature is
                                             			 supported only on Cisco Unified IP Phone 7940, 7940G, 7960, and 7960G. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME. |
| Step 4 | description string Example: Router(config-register-pool)# description 408-555-0100 | Defines a
                                             				customized description that appears in the header bar of supported
                                             				Cisco Unified IP phones Truncated
                                                      					 to 14 characters in the display. If string
                                                      					 contains spaces, enclose the string in quotation marks. |
| Step 5 | end Example: Router(config-register-pool)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Use the show
                                                				  running-config command to verify your configuration. Descriptions
                                          			 for directory numbers are listed in the ephone-dn and voice-register dn
                                          			 portions of the output. Example: Router# show running-config ephone-dn  1  dual-line
		   number 150 secondary 151
		   description 555-0150
		   call-forward busy 160 
		   call-forward noan 160 timeout 10
		   huntstop channel
		   no huntstop
		  !
		  !
		  !
		  voice-register dn 1
		   number 1101 
		   description 555-0101 |
|---|

| show telephony-service ephone Use this
                                             				command to ensure that the ephone-dn to which you applied the description
                                             				appears on the first button on the ephone. In the example below, ephone-dn 22
                                             				has the description in the phone display header bar. Router# show telephony-service ephone ephone-dn 22
		   number 2149
		   description 408-555-0149
		  
		  ephone 34
		   mac-address 0030.94C3.F96A
		   button  1:22 2:23 3:24
		   speed-dial 1 5004
		   speed-dial 2 5001 |
|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 1 | Enters
                                             				ephone-dn configuration mode. dn-tag —Unique sequence number that identifies the
                                                      					 ephone-dn to which the label is to be associated. |
| Step 4 | label label-string Example: Router(config-ephone-dn)# label user1 | Creates a
                                             				custom label that is displayed on the phone next to the line button that is
                                             				associated with this ephone-dn. The custom label replaces the default label,
                                             				which is the number that was assigned to this ephone-dn. label-string —String of up to 30 alphanumeric
                                                      					 characters that provides the label text. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Only one label
                                             			 is permitted per directory number. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config-register-global)# voice register dn 17 | Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI). |
| Step 4 | number number Example: Router(config-register-dn)# number 7001 | Defines a
                                             				valid number for a directory number. |
| Step 5 | label string Example: Router(config-register-dn)# label user01 | Creates a text
                                             				identifier, instead of a phone-number display, for a directory number that
                                             				appears on a SIP phone console. |
| Step 6 | end Example: Router(config-register-dn)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Use the show
                                                				  running-config command to verify your configuration. Descriptions
                                          			 for directory numbers are listed in the ephone-dn and voice-register dn
                                          			 portions of the output. Router# show running-config ephone-dn  1  dual-line
		   number 150 secondary 151
		   label MyLine
		   call-forward busy 160 
		   call-forward noan 160 timeout 10
		   huntstop channel
		   no huntstop
		  !
		  !
		  !
		  voice-register dn 1
		   number 1101 
		   label MyLine |
|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | system message text-message Example: Router(config-telephony)# system message ABC Company | Defines a text
                                             				message to display when a phone is idle. text-message —Alphanumeric string to display.
                                                      					 Display uses proportional-width font, so the number of characters that are
                                                      					 displayed varies based on the width of the characters that are used. The
                                                      					 maximum number of displayed characters is approximately 30. |
| Step 5 | url idle url idle-timeout seconds Example: Router(config-telephony)# url idle http://www.abcwrecking.com/public/logo idle-timeout 35 | Defines the
                                             				location of a file to display on phones that are not in use and specifies the
                                             				interval between refreshes of the display, in seconds. url —Any URL that conforms to RFC 2396. seconds —Time interval between display refreshes,
                                                      					 in seconds. Range is 0 to 300. |
| Step 6 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Use the show
                                                				  running-config command to verify your configuration. System
                                          			 message display is listed in the telephony-service portion of the output. Router# show running-config telephony-service
		   fxo hook-flash
		   load 7960-7940 P00307020300
		   load 7914 S00104000100
		   max-ephones 100
		   max-dn 500
		   ip source-address 10.153.13.121 port 2000
		   max-redirect 20
		   timeouts ringing 100
		   system message XYZ Company
		   voicemail 7189
		   max-conferences 8 gain -6
		   call-forward pattern .T
		   moh flash:music-on-hold.au
		   multicast moh 239.10.10.1 port 2000
		   web admin system name server1 password server1
		   dn-webedit 
		   time-webedit 
		   transfer-system full-consult
		   transfer-pattern 92......
		   transfer-pattern 91..........
		   transfer-pattern 93......
		   transfer-pattern 94......
		   transfer-pattern 95......
		   transfer-pattern 96......
		   transfer-pattern 97......
		   transfer-pattern 98......
		   transfer-pattern 99......
		   transfer-pattern .T
		   secondary-dialtone 9
		   create cnf-files version-stamp Jan 01 2002 00:00:00 |
|---|

| Ensure that
                                          			 the HTTP server is enabled. |
|---|

| Restriction | Operation of
                                                      				  these services is determined by the Cisco Unified IP phone capabilities and the
                                                      				  content of the specified URL. Provisioning
                                                      				  a URL to access help screens using the i or ? buttons on a phone is not
                                                      				  supported. Provisioning
                                                      				  the directory URL to select an external directory resource disables the
                                                      				  Cisco Unified CME local directory service. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | url { directories \| information \| messages \| services } url Example: Router(config-telephony)# url directories http://10.4.212.4/localdirectory | Provisions
                                             				URLs for the four programmable feature buttons (Directories, Information,
                                             				Messages, and Services) on a supported Cisco Unified IP phone. To use a
                                                      					 Cisco Unified Communications Manager directory as an external directory source,
                                                      					 you must list the MAC addresses of the phones in Cisco Unified Communications
                                                      					 Manager and reset the phones from Cisco Unified Communications Manager. You do
                                                      					 not need to assign ephone-dns to the phones for the phones to register with
                                                      					 Cisco Unified Communications Manager. The url services command is also available in ephone-template configuration mode. If you use an
                                                      					 ephone template to provision the Services feature button on one or more SCCP
                                                      					 phones and you configure the url services command in telephony-service configuration mode, the value set in
                                                      					 telephony-service configuration mode appears first in the list of options
                                                      					 displayed when the phone user presses the Services feature button. |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Operation of
                                                      				  these services is determined by the Cisco Unified IP phone capabilities and the
                                                      				  content of the specified URL. Provisioning
                                                      				  the directory URL to select an external directory resource disables the
                                                      				  Cisco Unified CME local directory service. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# | Enters
                                             				telephony-service configuration mode. |
| Step 4 | url { authentication \| directory \| service \| idle } url Example: Router(config-register-global)# url directory http://10.0.0.11/localdirectory Router(config-register-global)# url service http://10.0.0.4/CCMUser/123456/urltest.html Router(config-register-global)# url idle http://www.mycompany.com/files/logo.xml idle-timeout 12 | Associates a
                                             				URL with the programmable feature buttons on SIP phones. url authentication url — Uses the information at the specified URL to
                                                      					 validate requests made to the phone web server. url directory url — Uses the information at the specified URL
                                                      					 for the Directories button display. url service url [ root ] — Uses the information at the specified URL for
                                                      					 the Services button display. url idle url — Defines the location of a file to display on
                                                      					 phones that are not in use and specifies the interval between refreshes of the
                                                      					 display, in seconds. |
| Step 5 | end Example: Router(config-register-global)# end | Returns to
                                             				privileged EXEC mode. |

| Ensure the
                                          			 HTTP server is enabled and that there is communication between the
                                          			 Cisco Unified CME router and the server. |
|---|

| Restriction | Only the
                                                      				  parameters supported by the currently loaded firmware are available. The number
                                                      				  and type of parameters may vary from one firmware version to the next. Only those
                                                      				  parameters that are supported by a Cisco Unified IP phone and firmware version
                                                      				  are implemented. Parameters that are not supported are ignored. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | service phone parameter-name parameter-value Example: Router(config-telephony)# service phone
daysDisplayNotActive 1,2,3,4,5,6,7
Router(config-telephony)# service phone
displayOnTime 07:30
Router(config-telephony)# service phone
displayOnDuration 10:00
Router(config-telephony)# service phone
displayIdleTimeout 00.01 | Sets display
                                             				and phone functionality for all IP phones that support the configured
                                             				parameters and to which this template is applied. The
                                                      					 parameter name is word and case-sensitive. See Cisco Unified CME Command
                                                         						Reference for a list of parameters. This
                                                      					 command can also be configured in ephone- template configuration mode and
                                                      					 applied to one or more phones. |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Cisco Unified CME 4.0 or a later version. System must
                                                      				  be configured to for per-phone configuration files. For configuration
                                                      				  information, see Define Per-Phone Configuration Files and Alternate Location for SCCP Phones . Only the
                                                      				  parameters supported by the currently loaded firmware are available. The number
                                                      				  and type of parameters may vary from one firmware version to the next. Only those
                                                      				  parameters that are supported by a Cisco Unified IP phone and firmware version
                                                      				  are implemented. Parameters that are not supported are ignored. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router (config)# ephone-template 15 | Enters
                                             				ephone-template configuration mode to create an ephone template. |
| Step 4 | service phone parameter-name parameter-value Example: Router(config-telephony)# service phone daysDisplayNotActive 1,2,3,4,5,6,7 
Router(config-telephony)# service phone displayOnTime 07:30 
Router(config-telephony)# service phone displayOnDuration 10:00 
Router(config-telephony)# service phone displayidleTimeout 00.01 | Sets
                                             				parameters for all IP phones that support the configured functionality and to
                                             				which this template is applied. The
                                                      					 parameter name is word and case-sensitive. See the Cisco Unified CME Command Reference for a
                                                      					 list of parameters. This
                                                      					 command can also be configured in telephony-service configuration mode. For
                                                      					 individual phones, the template configuration for this command overrides the
                                                      					 system-level configuration for this command. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits from
                                             				this command mode to the next highest mode in the configuration mode hierarchy. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone
                                             				configuration mode. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 15 | Applies an
                                             				ephone template to the ephone that is being configured. |
| Step 8 | end Example: Router(config-ephone)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Step 1 | Ensure that
                                          			 the templates have been properly applied to the phones. |
|---|---|
| Step 2 | Ensure that
                                          			 you use the create
                                                				  cnf-files command to regenerate configuration files and reset the
                                          			 phones after you apply the templates. |
| Step 3 | Use the show telephony-service
                                                				  tftp-bindings command to display the configuration files that are
                                          			 associated with individual phones Example: Router# show telephony-service tftp-binding tftp-server system:/its/SEPDEFAULT.cnf  
			 tftp-server system:/its/SEPDEFAULT.cnf alias SEPDefault.cnf  
			 tftp-server system:/its/XMLDefault.cnf.xml alias XMLDefault.cnf.xml  
			 tftp-server system:/its/ATADefault.cnf.xml  
			 tftp-server system:/its/XMLDefault7960.cnf.xml alias SEP00036B54BB15.cnf.xml 
			 tftp-server system:/its/germany/7960-font.xml alias German_Germany/7960-font.xml  
			 tftp-server system:/its/germany/7960-dictionary.xml alias German_Germany/7960-dictionary.xml  
			 tftp-server system:/its/germany/7960-kate.xml alias German_Germany/7960-kate.xml  
			 tftp-server system:/its/germany/SCCP-dictionary.xml alias German_Germany/SCCP-dictionary.xml  
			 tftp-server system:/its/germany/7960-tones.xml alias Germany/7960-tones.xml |
| Step 4 | Use the debug tftp
                                                				  events command to verify that the phone is accessing the file
                                          			 when you reboot the phone. |

| Restriction | Supported on
                                             			 Cisco Unified Wireless IP Phone 7921 and 7925 only. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router (config)# ephone-template 12 | Enters
                                             				ephone-template configuration mode to create an ephone template. |
| Step 4 | service phone thumbButton1 PTTH button_number Example: Router(config-ephone-template)# service phone thumbButton1 PTTH6 | Specifies
                                             				which button is to go off hook when user presses the thumb button. button_number —Button on phone that is configured
                                                      					 with an intercom dn that targets a paging number. Range is 1 to 6. There are
                                                      					 no spaces in the PTTH and button_number keyword/argument combination. This
                                                      					 command can also be configured in telephony-service configuration mode. For
                                                      					 individual phones, the template configuration for this command overrides the
                                                      					 system-level configuration for this command. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits from
                                             				this command mode to the next highest mode in the configuration mode hierarchy. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone
                                             				configuration mode. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 12 | Applies an
                                             				ephone template to the ephone that is being configured. |
| Step 8 | end Example: Router(config-ephone)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables the
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters the
                                             				global configuration mode. |
| Step 3 | ip http secure-server Example: Router(config)# ip http secure-server | Enables a
                                             				secure HTTP (HTTPS) server. The HTTPS server uses the Secure Sockets Layer
                                             				(SSL) Version 3 protocol. |
| Step 4 | ip http secure-port port number Example: Router(config)# ip http secure-port 8443 | Sets the HTTPS
                                             				server port number for listening. |
| Step 5 | voice register dn dn-tag Example: Router(config)# voice register dn 1 | Creates
                                             				directory numbers for the SIP IP phones that are directly connected to Cisco
                                             				Unified CME |
| Step 6 | number number Example: Router(config-register-dn)# number 991001 | Defines the
                                             				numbers for the SIP IP phones. |
| Step 7 | voice register pool phone-tag Example: Router# voice register pool  1 | Sets the
                                             				phone type for the SIP IP phones on a Cisco Unified CME system. |
| Step 8 | id device-id-name name Example: Router(config-register-pool)# id device-id-name JabberWIN | Specifies the device ID of a phone type. For a list of supported device IDs, see Cisco Unified Communications Manager Express Command Reference . Assigns a name to a phone type. name —String that specifies the SIP soft client device ID name. Device ID name string can be up to 32 characters. |
| Step 9 | type type Example: Router(config-register-pool)# type Jabber-CSF-Client | Defines the
                                             				phone type. |
| Step 10 | number number Example: Router(config-register-pool)# number 1 | Defines the
                                             				numbers for the SIP IP phones. |
| Step 11 | username username password password Example: Router(config-register-pool))# username jabber1 password jabber1 | Sets the
                                             				username and password. Username — Specifies the username of the phone type. Password — Specifies the password of the phone type. |
| Step 12 | description string Example: Router(config-register-pool)# description Jabber-CSF-Client | Associates a
                                             				description with the Cisco Jabber client. Enter a string of up to 64
                                             				characters. A maximum of 128 characters, including spaces. |
| Step 13 | exit Example: Router(config-register-pool)# exit | Exits the
                                             				voice register-pool configuration mode. |
| Step 14 | end Example: Router(config)# end | Exits the
                                             				privileged EXEC configuration mode. |

| Feature Name | Unified CME Version | Feature
                                       				  Information |
|---|---|---|
| Support for Cisco Jabber | 12.5 | Added Support for Cisco Jabber CSF Client MAC and Windows
                                       								(Phone-only), Version 12.1(0). |
| Support for Cisco Jabber | 8.6 | Added
                                       				  support for Cisco Jabber. |
| My Phone Apps for Cisco Unified SIP IP Phones | 9.0 | Adds support for My Phone Apps feature on Cisco Unified SIP IP phones. |
| Clear
                                       				  Directory Entries | 8.6 | Provides
                                       				  ability to clear the display of call-history details such as missed, placed,
                                       				  and received call entries on a Cisco Unified  SCCP IP phone’s display screen. |
| Fixed
                                       				  Line/Feature Buttons | 4.0(2) | Provides two
                                       				  preconfigured fixed sets of feature buttons for provisioning a Cisco Unified IP
                                       				  Phone 7931G. |
| Header Bar
                                       				  Display | 3.4 | Added
                                       				  support for modifying header bar display on SIP phones. |
| 2.01 | Phone header
                                       				  bar display is introduced. |
| Labels for
                                       				  Directory Numbers | 3.4 | Added
                                       				  support for label display on SIP phones. |
| 3.0 | Ephone-dn
                                       				  labels were introduced. |
| Programmable
                                       				  Vendor Parameters | 4.0 | Added
                                       				  support for configuring programmable phone and display functionality at a phone
                                       				  level for SCCP phones. |
| 3.4 | Added
                                       				  support for configuring programmable phone and display functionality for SIP
                                       				  phones. |
| 3.2.1 | Added
                                       				  support for programmable phone and display functionality in vendorConfig
                                       				  portion of configuration file. Implementation of configuration is firmware
                                       				  version dependent. |
| System
                                       				  Message Display | 3.0 | System
                                       				  message display on idle phones using text messages was introduced. |
| 2.1 | System
                                       				  message display on idle phones using HTML files was introduced. |
| URL
                                       				  Provisioning for Feature Buttons | 12.0 | Added
                                       				  support for Idle URL functionality on SIP phones. |
| 4.2 | Added
                                       				  support for configuring an ephone template to provision multiple URLs for the
                                       				  Services feature button phones. |
| 3.4 | Added
                                       				  support for provisioning customized URLs for programmable feature buttons on
                                       				  supported SIP phones. |
| 2.0 | Provisioning customized URLs for programmable feature buttons
                                       				  was introduced. |