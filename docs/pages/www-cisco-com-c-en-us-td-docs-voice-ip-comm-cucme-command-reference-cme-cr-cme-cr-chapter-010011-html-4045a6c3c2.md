---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-010011-html-4045a6c3c2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_010011.html
retrieved_at: 2026-08-21T22:57:15.260908+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: U

## Chapter: Cisco Unified CME Commands: U

# Cisco Unified CME Commands: U

## upa

To specify the audio file used for the unauthorized precedence
                              		  announcement, use the upa command in voice MLPP configuration mode. To disable use of
                              		  this audio file, use the no form of this command.

upa audio-url

no upa

### Syntax Description

audio-url

Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory.

### Command Default

No announcement is played.

### Command Modes

Voice MLPP configuration (config-voice-mlpp)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

This command specifies the G.711 a-law or u-law 8-KHz encoded audio
                              		  file (.wav or .au format) for the announcement that plays to callers when they
                              		  attempt to make a precedence call by using a higher level of precedence than
                              		  the highest precedence level that is authorized for their line.

The mlpp indication command must be enabled (default) for a
                              		  phone to play precedence announcements.

This command is not supported by Cisco IOS help. If you type ? , Cisco IOS help does not display a list of
                              		  valid entries.

## Examples

The following example shows the unauthorized precedence announcement
                              		  plays the file named upa.au located in flash:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# upa flash:upa.au
```

### Related Commands

Command

Description

bnea

Specifies the audio file used for the busy station not
                                          						equipped for preemption announcement.

ica

Specifies the audio file used for the isolated code
                                          						announcement.

vca

Specifies the audio file used for the vacant code
                                          						announcement.

mlpp indication

Enables MLPP indication on an SCCP phone or analog FXS
                                          						port.

mlpp preemption

Enables preemption capability on an SCCP phone or analog
                                          						FXS port.

## upgrade (voice register global)

To generate a OS79XX.TXT file for firmware upgrades, use
                              		  the upgrade command in voice register
                              		  global configuration mode. To return to the default, use the no form of this command.

upgrade

no upgrade

### Syntax Description

This command has no arguments or keywords.

### Command Default

No OS79XX.TXT file generated.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

The upgrade command performs the TFTP server alias binding, which can
                              		  be verified with the show voice register tftp-bind command.

## Examples

The following example shows the use of the upgrade command to upgrade Cisco SIP phone
                              		  firmware from SIP [456].x to SIP [567].y with comments:

```
Router(config)# voice register global Router(config-register-global)# load 7960-7940 P00x... !Do not use file extension.
Router(config-register-global)# upgrade !Generates OS79XX.txt file.
Router(config-register-global)# load 7960-7940 POSx... !Do not use file extension. This
                                                       ! is only required if you
                                                       !are upgrading to 7.y.
Router(config-register-global)# create profile !Generates SIPDefault.cnf and other files.
Router(config-register-global)# reset Router(config-register-global)# no upgrade !Returns  to default condition.
```

The P00x... and P0Sx... firmware filenames are required because the
                              		  content in OS79XX.TXT is different from image_version tag in SIPDefault.cnf.

### Related Commands

Description

create profile (voice register global)

Generates configuration profile files required for SIP IP
                                          						phones in Cisco Unified CME.

load (voice register global)

Associates a type of IP phone with a phone firmware file.

mode cme

Enables the mode for configuring SIP IP phones in Cisco
                                          						Unified CME.

reset (voice register pool)

Reboots and reregisters a SIP IP phone, including
                                          						contacting the DHCP server for updated information.

show voice register tftp-bind

Displays the current configuration files accessible to SIP
                                          						phones.

## url (telephony-service)

To provision uniform resource locators (URLs) for Cisco Unified IP
                              		  phones connected to the Cisco Unified CME router, use the url command in telephony-service or group
                              		  configuration mode. To remove a URL association, use the no form of this command.

url { authentication | directories | idle | information | messages | proxy-server | services } url [ line | root ]

no url { authentication | directories | idle | information | messages | proxy-server | services }

### Syntax Description

authentication

Uses the information at the specified URL to validate
                                          						requests made to the phone web server.

directories

Uses the information at the specified URL for the
                                          						Directories button display.

idle

Information at the specified URL displays on the window of
                                          						the IP phone during the idle state.

information

Uses the information at the specified URL for the
                                          						Information button display. This button can be labeled “i” or “?”.

messages

Uses the information at the specified URL for the Messages
                                          						button display.

proxy-server

Specifies the host and port used to enable proxy HTTP
                                          						requests for access to remote host addresses from the phone HTTP client.

services

Uses the information at the specified URL for the Services
                                          						button display.

url

URL as defined in RFC 2396.

line

(optional) Supported only with services keyword. Alphanumeric string of
                                          						1 to 32 characters that is line-services name to be displayed under Services
                                          						button.

root

(optional) Supported only with services keyword and supported in
                                          						telephony-service mode only. Menu of root phone services supported by a CSTA
                                          						client application is displayed under Services button.

### Command Default

The router automatically uses the local directory service.

### Command Modes

Telephony-service configuration (config-telephony) Group configuration (conf-tele-group)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.4(22)T

Cisco Unified CME 7.0(1)

This command was added to VRF group configuration mode.

15.0(1)XA

Cisco Unified CME 8.0

This command was modified. Support for the root keyword was added to this
                                          						command.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

Cisco Unified IP Phones can support URLs in association with the four
                              		  programmable feature buttons on those IP phones: Directories, Information,
                              		  Messages, and Services. The fifth button, Settings, is managed entirely by the phone. Operation of these services
                              		  is determined by the Cisco Unified IP phone capabilities and the content of the
                              		  referenced URL.

This command provisions URLs through the configuration file supplied
                              		  by the Cisco Unified CME router to the Cisco Unified IP phones during phone
                              		  registration.

To use a Cisco Unified CallManager directory as an external directory
                              		  source for Cisco Unified CME phones, the Cisco Unified CallManager must be made
                              		  aware of the phones. You must list the MAC addresses of the Cisco Unified CME
                              		  phones in the Cisco Unified CallManager and reset the phones from the Cisco
                              		  Unified CallManager. It is not necessary for you to assign ephone-dns to the
                              		  phones or for the phones to register with Cisco Unified CallManager.

You can disable the local directory by using the no service local-directory command.

This command must be followed by a complete phone reboot using the reset command.

## Examples

The following example provisions the Directories and Services
                              		  buttons. Note that the Messages button is configured by the voicemail command. The Messages button acts
                              		  like a speed-dial key to retrieve messages from a specified telephone number.

```
Router(config)# telephony-service Router(config-telephony)# url directories http://1.4.212.11/localdirectory Router(config-telephony)# url services http://1.4.212.4/CCMUser/123456/urltest.html
```

### Related Commands

Command

Description

group

Creates a virtual router forwarding (VRF) group for Cisco
                                          						Unified CME users and phones.

reset (ephone)

Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router.

reset (telephony-service)

Performs a complete reboot of one or all phones associated
                                          						with a Cisco Unified CME router.

service local-directory

Enables the availability of the local directory service on
                                          						IP phones.

voicemail

Defines the telephone number that is speed-dialed when the
                                          						Messages button on a Cisco Unified IP phone is pressed.

## url (voice
                        	 register global)

To provision
                              		  uniform resource locators (URLs) for feature buttons on Cisco SIP IP phones
                              		  connected to a Cisco Unified CME router, use the url command
                              		  in voice register global configuration mode. To remove a URL association, use
                              		  the no form of
                              		  this command.

url { authentication | directory | service | idle } url

no url { authentication | directory | service | idle }

## Syntax Description

authentication

Uses
                                          						the information at the specified URL to validate requests made to the phone web
                                          						server.

directory

Uses
                                          						the information at the specified URL for the Directories button display.

service

Uses
                                          						the information at the specified URL for the Services button display.

idle

Uses
                                          						the information at the specified URL to display on the IP phone during the idle
                                          						state.

url

URL as
                                          						defined in RFC 2396.

### Command Default

The router
                              		  automatically uses the local directory service.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

Cisco
                                          						IOS XE Everest 16.6.1

Cisco
                                          						Unified CME 12.0

The idle keyword was added.

12.4(4)T

Cisco
                                          						CME 3.4

This
                                          						command was introduced.

### Usage Guidelines

The Cisco Unified
                              		  IP Phones 7940 and 7940G and Cisco Unified IP Phones 7960 and 7960G can support
                              		  two URLs in association with two programmable feature buttons: Directories and
                              		  Services. Operation of these services is determined by the Cisco IP phone
                              		  capabilities and the content of the specified URL. The Settings button is managed entirely by the phone. The Messages button is
                              		  configured by the voicemail command.

The purpose of
                              		  the url command is to provision the URLs through the
                              		  configuration file supplied by the Cisco Unified CME router to the SIP phones
                              		  during phone registration.

You can disable
                              		  the local directory by specifying the string “none” instead of a URL with the directory keyword, as shown in the following example:

```
Router(config)# voice register global Router(config-register-global)# url directory none
```

After you
                              		  configure this command, restart the phone by using the reset command.

## Examples

The following
                              		  example shows how to provision the Directories and Services buttons:

```
Router(config)# voice register global Router(config-register-global)# url directory http://1.4.212.11/localdirectory Router(config-register-global)# url service http://1.4.212.4/CCMUser/123456/urltest.html
```

## Examples

The following
                              		  example shows that the information at the specified URL is used to validate
                              		  requests made to the phone web server.

```
Router(config)# voice register global Router(config-register-global)# url authentication http://CME IP Address/CCMCIP/authenticate.asp
```

## Examples

The following
                              		  example specifies that the file logo.xml should be displayed on IP phones when
                              		  they are not being used and that the display should be refreshed every 12
                              		  seconds:

```
Router(config)# voice register global Router(config-register-global)# url idle http://mycompany.com/files/logo.xml idle-timeout 12
```

### Related Commands

Commands

Description

reset (voice register pool)

Performs a complete reboot of one phone associated with a Cisco CME router.

reset (voice register global)

Performs a complete reboot of all SIP phones associated with a Cisco CME
                                          						router.

telephony-service

Enters telephony-service configuration mode.

voicemail (voice register template)

Defines the telephone number that is speed-dialed when the Messages button on a
                                          						Cisco IP phone is pressed.

## url (voice
                        	 register template)

To define SIP
                              		  phone URLs to configure dial rules such as Application Dial Rule, Directory
                              		  Lookup Dial Rule, and LDAP server, use url
                                    				AppDialRule , url
                                    				DirLookupRule , and url
                                    				ldapServer commands in voice register template configuration mode. To
                              		  specify a file to display on an IP phone that is not in use, use the url idle command in voice register template configuration mode. To define a URL for
                              		  invoking phone services, use the url service command in voice register template configuration mode.

url { AppDialRule | DirLookupRule | ldapServer | idle | service } { string | url }

## Syntax Description

url AppDialRule string

Application dial rule URL.

url DirLookupRule string

Directory lookup rule URL.

url ldapServer string

LDAP
                                          						server URL.

url idle url

Defines
                                          						the location of a file to display on phones that are not in use and specifies
                                          						the interval between refreshes of the display, in seconds.

url service url

Uses the
                                          						information at the specified URL for invoking phone services.

### Command Default

No file is
                              		  specified.

### Command Modes

Voice register
                              		  template configuration (config-register-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

Cisco
                                          						IOS XE Everest 16.6.1

Unified
                                          						CME 12.0

This
                                          						command was modified to add idle and service keywords.

### Usage Guidelines

You can create the
                              		  application dial rule or directory lookup rule xml files and add these files to
                              		  a tftp server. The Cisco softphone SIP client can download the dial rules using
                              		  the url ldapserver string , url AppDialRule string , and url DirLookupRule string commands.

You can define
                              		  the location of a file to display on phones that are not in use, and specify
                              		  the interval between refreshes of the display using url idle command. You can also define a URL for invoking phone services using the url service command.

## Examples

The following
                              		  example shows how to define SIP phone URLs to configure Application Dial Rule,
                              		  Directory Lookup Dial Rule, LDAP server, idle url, and service url in voice
                              		  register template configuration mode.

```
Router(config-register-temp)# url ldapServer ldap.abcd.com

Router(config-register-temp)# url AppDialRule tftp://10.1.1.1/AppDialRules.xml

Router(config-register-temp)# url DirLookupRule tftp://10.1.1.1/DirLookupRules.xml

Router(config-register-temp)# url idle http://www.mycompany.com/files/logo.xml idle-timeout 12

Router(config-register-temp)# url service http://10.0.0.4/CCMUser/123456/urltest.html
```

### Related Commands

Commands

Description

voice register
                                                							 pool

Enters voice register pool configuration mode.

voice register
                                                							 template

Enters
                                          						voice register template configuration mode.

## url authentication

To instruct IP phones in Cisco Unified CME to send requests for
                              		  authorization to a particular authentication server and include the specified
                              		  credential in the requests, use the url authentication command in telephony-service
                              		  configuration mode. To return to default, use the no form of this command.

url authentication url-address application-name password [0|6] password

no url authentication url-address application-name password [0|6] password

### Syntax Description

url-address

URL adddress of authentication server.

The URL address for the authentication server in Cisco
                                          						Unified CME is: http:// CME IP Address /CCMCIP/authenticate.asp .

application-name

Character string sent by application to identify itself to
                                          						the server. Length of string: 1 to 15 characters.

For applications other than Extension Mobility, the name
                                          						portion of the credential must first be created in the application.

password

[0|6]

Character string sent by application to identify itself to
                                          						the server. Length of string: 1 to 15 characters.

The 0 in the parameter [0|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption.

For applications other than Extension Mobility, the password portion of the credential must first be created in the application.

### Command Default

No authentication server or credential is specified for Cisco Unified
                              		  CME to use for requesting authorization of commands from an application to a
                              		  phone.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command was enhanced for password encryption, based on Unified CME password policy.

### Usage Guidelines

This command specifies to which authentication server an IP phone in
                              		  Cisco Unified CME must send requests for authorization and what credential to
                              		  send in the request.

For Extension Mobility, use this command to instruct Extension
                              		  Mobility phones to send an HTTP GET/POST to request authorization from the
                              		  Cisco Unified CME authentication server before clearing call history when a
                              		  user logs out.

For Extension Mobility, no additional commands are required to create
                              		  or save the credential. The credential for the EM manager in Cisco Unified CME
                              		  is whatever values you specifiy by using this command.

For applications other than Extension Mobility, the requisite
                              		  credential must be created in the application.

To use the authentication server in Cisco Unified CME 4.3 and later
                              		  versions to authorize requests for applications other than Extension Mobility,
                              		  you must also configure the authentication credential command in telephony-service configuration mode.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] . This in accordance with Unified CME Password Policy. The 0 in the parameter [0|6] mentioned in the CLI command represents
                              plain, unencrypted text and 6 represents level 6 password encryption.

## Examples

The following example shows how to configure this command to instruct
                              		  Extension Mobility phones in Cisco Unified CME to request authorization from
                              		  the internal authentication server. The phones include the specified credential
                              		  (extmob psswrd) in the requests.

```
Router(config)# telephony-service Router(config-telephony)# url authentication http://192.0.2.0/CCMCIP/authenticate.asp extmob psswrd Router(config-telephony)# exit Router(config)#
```

### Related Commands

Command

Description

authentication credential

Stores credentials in the database for the Cisco Unified
                                          						CME authentication server.

keep call-history

Disables Automatic Clear Call History for Extension
                                          						Mobility in Cisco Unified CME.

## url idle

To specify a file to display on an IP phone that is not in use, use
                              		  the url idle command in telephony-service configuration
                              		  mode. To disable display of the file, use the no form of this command.

url idle url idle-timeout seconds

no url idle

### Syntax Description

url

URL as defined in RFC 2396.

idle-timeout seconds

Time interval between display refreshes, in seconds. Range
                                          						is from 0 to 300.

### Command Default

No file is specified for display on idle phones.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco ITS 2.1

This command was introduced.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

### Usage Guidelines

The
                                 			 file that is displayed must be encoded in eXtensible Markup Language (XML)
                                 			 using the Cisco XML document type definition (DTD). For more information about
                                 			 Cisco DTD formats, refer to Cisco IP Phone Services Application Development
                                 			 Notes.

This command must be followed by a complete phone reboot using the reset command.

## Examples

The following example specifies that the file logo.xml should be
                              		  displayed on IP phones when they are not being used and that the display should
                              		  be refreshed every 12 seconds:

```
Router(config)# telephony-service Router(config-telephony)# url idle http://mycompany.com/files/logo.xml idle-timeout 12
```

### Related Commands

Description

reset (ephone)

Performs a complete reboot of one phone associated with a
                                          						Cisco CME router.

reset (telephony-service)

Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router.

## url services (ephone-template)

To provision up to eight uniform resource locators (URLs) for the
                              		  Services feature button on individual SCCP phones connected to Cisco Unified
                              		  CME, use the url services command in ephone-template configuration mode. To reset to the
                              		  default, use the no form of this command.

url services url-tag url url-name

no url services url-tag

### Syntax Description

url-tag

Identifier for url being configured for Services feature
                                          						button. Range is 1 to 8.

url

URL as defined in RFC 2396.

url-name

Alpha-numerical string to appear for this URL in Services
                                          						feature button display. Length of string is 1 to 256 contiguous characters
                                          						(a-z, 0-9).

### Command Default

The system-level configuration for the Services button is used.

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XW

Cisco Unified CME 4.2

This command was introduced.

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command displays the information at up to eight URLs for the
                              		  Services feature button display on a supported Cisco Unified IP phone.
                              		  Operation of these services is determined by the capabilities of the Cisco
                              		  Unified IP phone and the content of the specified URL.

If you use an ephone template to apply this command to one or SCCP
                              		  phones and you also use the url command in telephony-service
                              		  configuration mode to configure a services url for all SCCP phones, the value
                              		  set in telephony-service configuration mode appears first in the list of
                              		  options displayed when the phone user presses the Services feature button,
                              		  before any URLs configured by using this command. Cisco Unified CME self-hosted
                              		  services, such as Extension Mobility, always appears last in the list of
                              		  options displayed for the Services feature button.

The number of url-name characters that appear on the IP
                              		  phone display is not fixed because IP phones typically use a proportional font.

After creating an ephone template that contains a services URL, use
                              		  the ephone-template (ephone) command to apply the template to
                              		  individual phones.

## Examples

The following example defines three urls for the Services feature
                              		  button display, one for all SCCP phones and two others in an ephone-template
                              		  that is applied to individual phones. Phones to which the template is applied
                              		  (ephones 11 and 13) will have a second and third option in the Services feature
                              		  button display.

```
telephony-service
 url services http://10.0.0.4/CMEUser/123456/urlsupport.html 
.
.
.
 create cnf-files
.
.
.
.
ephone-template 1
 url services 1 http://10.0.0.4/CMEUser/123456/cal.html Calendar
 url services 2 http://10.0.0.4/CMEUser/123456/quotes.html StockQuotes
ephone 11
 mac-address F00D.EDAB.1234 
 type 7960 
 button 1:25
 ephone-template 1
ephone 12
 mac-address 0003.B0D5.6541 
 type 7960 
 button 1:26
 logout-profile 1
ephone 13
 mac-address 000D.3666.3D00 
 type 7960 
 ephone-template 1
 logout-profile 1
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies an ephone template to an SCCP phone.

url (telephony-service)

Provisions URLs for programmable feature buttons on
                                          						supported Cisco Unified IP phones.

## url-button

To configure
                              		  service url feature on a line key, use the url-button command in ephone-template mode. To unconfigure the service url feature on a
                              		  line key, use the no form of
                              		  this command.

url-button index { type | url [ name ]}

no url-button index type url [ name ]

### Syntax Description

Unique
                                          						index number. The range is from 1 to 8.

Type of
                                          						service URL button. The following types of URL service buttons are available:

- myphoneapp: My phone
                                             						  application configured under phone user interface.

- em: Extension Mobility

- snr: Single Number Reach

- voicehuntgroups: Displays a
                                             						  list of voice hunt groups

- park-list: Displays a list
                                             						  of parked calls

Service
                                          						url with maximum length of 31 characters.

### Command Default

By default,
                              		  URL-button configuration on a line key is not configured.

### Command Modes

ephone template  (config-ephone-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(3)T

Cisco
                                          						Unified CME 8.5

This
                                          						command was introduced.

15.4(3)M

Cisco
                                          						Unified CME 10.5

This
                                          						command was modified to add voice hunt groups and park-list as new types .

### Usage Guidelines

You can configure
                              		  url-button feature on a line key to function as an extension mobility (EM), My
                              		  Phone Apps, or single number reach (SNR). You can also configure the url-button
                              		  feature on a line button to function as a service URL. by configuring a URL
                              		  name of a maximum length of 31 characters.

## Examples

The following
                              		  examples shows three URL buttons configured on a line key:

```
!
telephony-service
 max-ephones 25
 max-conferences 12 gain -6
 transfer-system full-consult
!
!
ephone-template  5
 url-button 1 em
 url-button 2 mphoneapp 
 url-button 3 snr
 url-button 4 voicehuntgroups
 url-button 5 park-list
!
ephone-template 6
conference drop-mode never
conference add-mode all
conference admin: No
max-calls-per-button 8
busy-trigger-per-button 0
privacy default
url-button 1 em
url-button 2 www.cisco.com www.cisco.com
url-button 3 snr
url-button 4 help help
url-button 7 myphoneapp
!
!
```

### Related Commands

Command

Description

show telephony-service ephone-template

Displays the contents of all the ephone templates defined.

## url-button (voice-register-template)

To configure service url feature button on a line key, use the
                              		  url-button command in voice register template mode. To disable the service url
                              		  feature button configuration on a line key, use the no form of this command.

url-button [ index number ] [ url location | url name ]

no url-button [ index number ] [ url location | url name ]

### Syntax Description

index number

Unique index number. Range: 1 to 8.

url location

Location of the url.

url name

Service url with maximum length of 31 characters.

### Command Default

URL-button configuration on a line key is disabled.

### Command Modes

Voice register template configuration (config-register-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to configure a url-button on a phone’s line key.You
                              		  can configure a line key to function as a url-button. You can also configure a
                              		  line button to function as a service url by configuring a url name of a maximum
                              		  length of 31 characters.

## Examples

The following example shows url-button configured in voice register
                              		  template 1:

```
Router# show run
!
!
voice register template  1
 url-button 1 http://www.cisco.com cisco
 button-layout 1 line
 button-layout 2,5 speed-dial
!
voice register pool  50
 id mac 001E.7AC4.DC73
 feature-button 1 NewCall
 type 7965
 number 1 dn 65
 template 1
 dtmf-relay rtp-nte
 speed-dial 1 2001 label "SD1-2001"
```

### Related Commands

Command

Description

show voice register pool

Displays all configuration information associated with a particular voice register pool.

show voice register template

Displays all configuration information associated with a
                                          						SIP phone template,

## user (voice logout-profile)

To create an authentication credential for use by Telephone
                              		  Application Programming Interface (TAPI) phone devices and certain other
                              		  applications to log into Cisco Unified CME, use the username command in voice logout-profile
                              		  configuration mode. To remove the credential, use the no form of this command.

user username password [0|6] password

no user name password [0|6] password

### Syntax Description

name

Unique alphanumeric string to be used by a TAPI phone
                                          						device to log into Cisco Unified CME. String can contain a maximum of 15
                                          						alphanumeric characters.

password

Password to be used with this username for authentication
                                          						purposes.

Alphanumeric string.

The 0 in the parameter [0|6] represents plain, unencrypted text and 6 represents level 6 password encryption.

### Command Default

No authentication credential is created.

### Command Modes

Voice logout-profile configuration (voice-logout-profile)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW

Cisco Unified CME 4.2

This command was introduced.

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command was enhanced for password encryption, based on Unified CME password policy.

### Usage Guidelines

Use this command in voice logout-profile configuration mode to add an
                              		  authentication credential to a logout profile for Extension Mobility. The
                              		  authentication credential is used by TAPI phone devices and certain other
                              		  applications to log into Cisco Unified CME via an IP phone that is enabled for
                              		  Extension Mobility and on which the logout profile is downloaded.

The user name parameter of any authentication credential must be
                              		  unique. Do not use the same value for a user name when you configure any two or
                              		  more authentication credentials in Cisco Unified CME, such as the username for
                              		  any Cisco United CME GUI account and the user name in a profile for Extension
                              		  Mobility.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] . This in accordance with Unified CME Password Policy. The 0 in the parameter [0|6] mentioned in the CLI command represents
                              plain, unencrypted text and 6 represents level 6 password encryption.

## Examples

The following example shows the configuration for a logout profile
                              		  that defines the default appearance for a Cisco Unified IP phone that is
                              		  enabled for Extension Mobility, including the username (23C2-8) and password
                              		  (43214) to be used by a TAPI phone device to log into Cisco Unified CME:

```
pin 9999
 user 23C2-8 password 43214
 number 3001 type silent-ring
 number 3002 type beep-ring
 number 3003 type feature-ring
 number 3004 type monitor-ring
 number 3005,3006 type overlay
 number 3007,3008 type cw-overly
 speed-dial 1 2000
 speed-dial 2 2001 blf
```

### Related Commands

Command

Description

logout-profile

Enables a Cisco Unified IP phone for extension mobility and
                                          						assigns a logout profile to this phone.

reset (voice logout-profile and voice user-profile)

Performs a complete reboot of all IP phones to which a
                                          						particular logout-profile or user-profile is downloaded.

## user (voice user-profile)

To create an authentication credential to be used by Extension
                              		  Mobility in Cisco Unified CME, use the username command in voice user-profile
                              		  configuration mode. To remove the credential, use the no form of this command.

user name password password

no user name password password

name

Unique alphanumeric string to identify a user for this
                                       					 authentication credential only. String can contain a maximum of 15 alphanumeric
                                       					 characters.

password

Password to be used with this user name for authentication
                                       					 purposes.

password

Alphanumeric string.

### Command Default

Credential is not created.

### Command Modes

Voice user-profile configuration (config-user-profile)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW

Cisco Unified CME 4.2

This command was introduced.

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command in voice user-profile configuration mode creates a
                              		  credential to be authenticated by Cisco Unified CME before a phone user can log
                              		  into a Cisco Unified IP phone that is enabled for Extension Mobility

The user name parameter of any authentication credential must be
                              		  unique. Do not use the same value for a user name when you configure any two or
                              		  more authentication credentials in Cisco Unified CME, such as the username for
                              		  any Cisco United CME GUI account and the user name in a profile for Extension
                              		  Mobility.

When a user logs into an extension mobility enabled phone, Cisco
                              		  Unified CME retrieves the appropriate user profile, based on username and
                              		  password match, and replace the phone’s default logout profile with the user’s
                              		  profile.

## Examples

The following example shows the configuration to be downloaded after
                              		  a user enters the username and password configured in this profile, and Cisco
                              		  Unified CME matches the entry to the credentials in a user profile database:

```
voice user-profile 1
 pin  12345
 user me password pass123
 number 2001 type silent-ring
 number 2002 type beep-ring
 number 2003 type feature-ring
 number 2004 type monitor-ring
 number 2005,2006 type overlay
 number 2007,2008 type cw-overly
 speed-dial 1 3001
 speed-dial 2 3002 blf
```

### Related Commands

Command

Description

reset (voice logout-profile and voice user-profile)

Preforms complete reboot of all IP phones on which a
                                          						particular logout-profile or user-profile is downloaded.

## user-locale (ephone-template)

To specify a user locale in an ephone template, use the user-locale command in ephone-template
                              		  configuration mode. To reset to the default user locale, use the no form of this command.

user-locale user-locale-tag

no user-locale

### Syntax Description

user-locale-tag

Locale identifier that was assigned to the user locale
                                          						using the user-locale (telephony-service) command.

### Command Default

The default user locale (user-locale 0) is used.

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

To apply user locales to individual ephones, you must specify
                              		  per-phone configuration files using the cnf-file perphone command and identify the locales using the user-locale (telephony-service) command.

After creating an ephone template that contains a locale tag, use the ephone-template (ephone) command to apply the template to
                              		  individual ephones.

## Examples

The following example defines three alternative locales: JP (Japan),
                              		  FR (France), and ES (Spain). The default is US for all phones that do not have
                              		  the alternatives applied using ephone templates. In this example, ephone 11
                              		  uses JP for its locales, ephone 12 uses FR, ephone 13 uses ES, and ephone 14
                              		  uses the default, US.

```
telephony-service
 cnf-file location flash:
 cnf-file perphone
 user-locale 1 JP
 user-locale 2 FR
 user-locale 3 ES
 network-locale 1 JP
 network-locale 2 FR
 network-locale 3 ES
 create cnf-files
ephone-template 1
 user-locale 1
 network-locale 1
ephone-template 2
 user-locale 2
 network-locale 2
ephone-template 3
 user-locale 3
 network-locale 3
ephone 11
 button 1:25
 ephone-template 1
ephone 12
 button 1:26
 ephone-template 2
ephone 13
 button 1:27
 ephone-template 3
ephone 14
 button 1:28
```

### Related Commands

Description

cnf-file

Specifies the type of configuration files that phones use.

ephone-template (ephone)

Applies an ephone template to an ephone.

user-locale (telephony-service)

Sets the language for displays on supported phone types.

## user-locale (telephony-service)

To define languages for displays on supported phones, use the user-locale command in telephony-service
                              		  configuration mode. To remove a locale configuration, use the no form of this command.

user-locale [user-locale-tag] [user-defined-code] country-code [ load TAR-filename ]

no user-locale [user-locale-tag] country-code

### Syntax Description

user-locale-tag

(Optional) Identifier for the specified locale. Required to
                                          						configure multiple locales only. Range is 0 to 4. Default is 0.

user-defined-code

(Optional) Label for locale that is not one of the 12
                                          						standard ISO 366 locales. Use each label for only one user-locale-tag at a time. Values
                                          						are U1 , U2 , U3 , U4 , and U5 .

country-code

- DE —Germany

- DK —Denmark

- ES —Spain

- FR —France

- IT —Italy

- JP —Japan

- NL —Netherlands

- NO —Norway

- PT —Portual

- RU —Russia

- SE —Sweden

- US —United States

- Any valid ISO 639 code to be associated with the user-defined-code argument (U1 to
                                             						  U5) only. Code must be for a supported locale that is not listed above and for
                                             						  which the XML files can be downloaded to flash, slot 0, or a TFTP server.

- U1 , U2 , U3 , U4 , U5 —Only when used with the load keyword and where U1 to U5
                                             						  corresponds to a user-defined locale for which the TAR file is downloaded to
                                             						  flash, slot 0, or a TFTP server.

load

(Optional) Extracts contents of a TAR file to the location
                                          						specified by using the cnf-file location command. This keyword is supported in Cisco Unified
                                          						CME 7.0(1) and later versions.

TAR-filename

TAR file containing the language JAR file and the
                                          						tg3-tones.xml file for country-specific network tones and cadences.

### Command Default

The default user-locale tag is 0 and the default locale is US (United
                              		  States).

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco ITS 2.1

This command was introduced.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

12.2(15)ZJ

Cisco CME 3.0

The following keywords were added: DK , NL , NO , PT , RU , and SE .

12.3(4)T

Cisco CME 3.0

The keywords added for Cisco CME 3.0 were integrated into
                                          						Cisco IOS Release 12.3(4)T.

12.4(4)XC

Cisco Unified CME 4.0

The user- locale-tag and user-defined-code arguments were added.

12.4(9)T

Cisco Unified CME 4.0

The user-locale-tag and user-defined-code arguments were integrated into Cisco
                                          						IOS Release 12.4(9)T.

12.4(20)YA

Cisco Unified CME 7.0(1)

The load TAR-filename keyword/argument combination for the locale installer was added.

12.4(22)T

Cisco Unified CME 7.0(1)

This command was integrated into Cisco IOS Release
                                          						12.4(22)T.

### Usage Guidelines

This command sets the language for displays on supported phone types.

The show telephony-service tftp-bindings command displays the locale that is set using this command.
                              		  This locale is associated with the dictionary and language files.

Follow this command with a complete phone reboot using the reset command.

User-locale 0 always holds the default language that is used for all
                              		  SCCP phones that are not assigned alternative user locales or user-defined user
                              		  locales. The system default is US (United States) unless you use this command
                              		  to designate a different locale for user-locale 0.

Alternative User Locales

In Cisco Unified CME 4.0 or a later version, the user- locale-tag argument allows you to
                              		  specify up to five alternative user locales. For example, a company can specify
                              		  French for phones A, B, and C; German for phones D, E, and F; and United States
                              		  for phones G, H, and I.

Each of the five user locales that you can use in a multi locale
                              		  system is identified with the user-locale-tag argument. The identifier 0
                              		  always holds the default locale, although you can define this default to be any
                              		  language code that is supported in the system and is listed in CLI help for the
                              		  command. For example, if you define locale-tag 0 to be JP (Japanese), the
                              		  default user locale for the router is JP. If you do not specify a locale for
                              		  identifier 0, the default is US (United States). If you are using this command
                              		  to configure a default locale for all SCCP phones in your system, you are not
                              		  required to include user-locale-tag 0 in the command.

To apply alternative user locales to different phones, you must use
                              		  the cnf-files command to specify per-phone
                              		  configuration files. When you use per-phone configuration files, a phone's
                              		  configuration file automatically uses the default locales in user locale 0 and
                              		  network locale 0. You can override this default for individual ephones by
                              		  assigning locale tags to the alternative language codes that you want to use.
                              		  Use ephone templates to assign the locale tag to individual ephones. For
                              		  example, you can assign user-locale-tag 2 to the language code RU (Russian).

Use the user-locale command in ephone-template mode
                              		  to apply a locale tag to an ephone template. Use the ephone-template command in ephone
                              		  configuration mode to apply the template a phones that should use the
                              		  alternative language.

User-Defined User Locales

In Cisco Unified CME 4.0 and later versions, you can install XML
                              		  files to support up to five user and network locales that are not standard in
                              		  your system. These files cannot be installed in the system storage location. To
                              		  support user-defined locales, you must use the cnf-files perphone and cnf-file location commands and copy the appropriate XML language files into slot
                              		  0, flash, or TFTP memory. The user locales and network locales that are stored
                              		  in this way can then be used as default or alternative entries for all or some
                              		  phones.

For example, if you have a site at which the phones should use the
                              		  displays and tones for Traditional Chinese, which is not one of the standard
                              		  languages, you must download the XML files for Traditional Chinese to use this
                              		  user-defined locale on a phone.

Locale Installer

In Cisco Unified CME 7.0(1) and later versions, this command with the load keyword is a locale installer that extracts the contents of the
                              		  locale TAR file to the location specified by the cnf-file location command. Before Cisco Unified CME 7.0(1), you had to manually
                              		  extract the files to flash, slot 0, or an external TFTP server.

Before using this command as a locale installer, you must manually
                              		  create the required locale folders in the root directory of the external TFTP
                              		  server.

## Examples

The following example sets the default language tag for the IP phone
                              		  display to French:

```
telephony-service
 user-locale FR
```

The following example sets the default language tag for the IP phone
                              		  display to French. It shows another way to change the default:

```
telephony-service
 user-locale 0 FR
```

The following example sets the alternative language tag 1 to German:

```
telephony-service
 user-locale 1 DE
```

## Examples

The following example defines three alternative locales: JP (Japan),
                              		  FR (France), and ES (Spain). The default is US for all phones that do not have
                              		  the alternatives applied using ephone templates. In this example, ephone 11
                              		  uses JP for its locales, ephone 12 uses FR, ephone 13 uses ES, and ephone 14
                              		  uses the default, US.

```
telephony-service
 cnf-file location flash:
 cnf-file perphone
 user-locale 1 JP
 user-locale 2 FR
 user-locale 3 ES
 network-locale 1 JP
 network-locale 2 FR
 network-locale 3 ES
 create cnf-files
ephone-template 1
 user-locale 1
 network-locale 1
ephone-template 2
 user-locale 2
 network-locale 2
ephone-template 3
 user-locale 3
 network-locale 3
ephone 11
 button 1:25
 ephone-template 1
ephone 12
 button 1:26
 ephone-template 2
ephone 13
 button 1:27
 ephone-template 3
ephone 14
 button 1:28
```

## Examples

The following example applies locale tag 4 to the user-defined code
                              		  U1, which is defined as ZH. ZH is the code that represents Traditional Chinese
                              		  in ISO 639, the Language Code Reference . Because the code for Traditional
                              		  Chinese is not one of those that is provided in the system, the user must
                              		  download the appropriate XML files to support this language.

In addition to the user-defined code, the example defines three
                              		  alternative locales: JP (Japan), FR (France), and ES (Spain). The default is US
                              		  for all phones that do not have the alternatives applied using ephone
                              		  templates. In this example, ephone 11 uses JP for its locales; ephone 12 uses
                              		  FR; ephone 13 uses ES; ephone 14 uses the default, US; and ephone 15 uses the
                              		  user-defined language, ZH (Traditional Chinese).

```
telephony-service
 cnf-file location flash:
 cnf-file perphone
 user-locale 1 JP
 user-locale 2 FR
 user-locale 3 ES
 user-locale 4 U1 ZH
 network-locale 1 JP
 network-locale 2 FR
 network-locale 3 ES
 network-locale 4 U1 ZH
 create cnf-files
ephone-template 1
 user-locale 1
 network-locale 1
ephone-template 2
 user-locale 2
 network-locale 2
ephone-template 3
 user-locale 3
 network-locale 3
ephone-template 4
 user-locale 4
 network-locale 4
ephone 11
 button 1:25
 ephone-template 1
ephone 12
 button 1:26
 ephone-template 2
ephone 13
 button 1:27
 ephone-template 3
ephone 14
 button 1:28
ephone 15
 button 1:29
 ephone-template 4
```

## Examples

The following example is the output from the user-locale command when the user-defined
                              		  locale is on the default locale index (0) and the country-code is U2 for
                              		  user-defined Finnish. The contents of the TAR file are extracted to flash, slot
                              		  0, or a TFTP server as previously specified by the cnf-file location command.

```
Router(config-telephone)# user-locale U2 load CME-locale-fi_FI-7.0.1.1.tar Updating CNF files
LOCALE INSTALLER MESSAGE: VER:1
LOCALE INSTALLER MESSAGE: Langcode:fi
LOCALE INSTALLER MESSAGE: Language:Finnish
LOCALE INSTALLER MESSAGE: Filename: 7905-dictionary.xml
LOCALE INSTALLER MESSAGE: Filename: 7905-kate.xml
LOCALE INSTALLER MESSAGE: Filename: 7920-dictionary.xml
LOCALE INSTALLER MESSAGE: Filename: 7960-dictionary.xml
LOCALE INSTALLER MESSAGE: Filename: 7960-font.xml
LOCALE INSTALLER MESSAGE: Filename: 7960-kate.xml
LOCALE INSTALLER MESSAGE: Filename: 7960-tones.xml
LOCALE INSTALLER MESSAGE: Filename: mk-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: tc-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: td-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: tags_file
LOCALE INSTALLER MESSAGE: Filename: utf8_tags_file
LOCALE INSTALLER MESSAGE: Filename: g3-tones.xml
LOCALE INSTALLER MESSAGE: Filename: SCCP-dictionary.utf-8.xml
LOCALE INSTALLER MESSAGE: Filename: SCCP-dictionary.xml
LOCALE INSTALLER MESSAGE: Filename: ipc-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: gp-sccp.jar
LOCALE INSTALLER MESSAGE: New Locale configured
Processing file:flash:/its/user_define_2_tags_file
Processing file:flash:/its/user_define_2_utf8_tags_file
CNF-FILES: Clock is not set or synchronized, retaining old versionStamps
CNF files updating complete
 
Router(config-telephony)# create cnf-files Router(config-telephony)# ephone 3 Router(config-ephone)# reset
```

### Related Commands

Command

Description

cnf-file location

Specifies a storage location for XML configuration files.

cnf-files

Specifies the type of phone configuration files to be
                                          						created.

ephone-template (ephone)

Applies an ephone template to an ephone.

network-locale (telephony-service)

Selects a code for a geographically specific set of tones
                                          						and cadences on supported phone types.

reset (ephone)

Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router.

reset (telephony-service)

Performs a complete reboot of one or all phones associated
                                          						with a Cisco Unified CME router.

show telephony-service tftp-bindings

Displays the current configuration files that are
                                          						accessible by IP phones.

user-locale (ephone-template)

Applies a user locale tag to an ephone template.

## user-locale (voice register)

To define languages for display on supported Cisco Unified SIP IP
                              		  phones, use the user-locale command in voice register global or voice register
                              		  template configuration mode. To remove a locale configuration, use the no form
                              		  of this command.

user-locale [user-locale-tag] { [user-defined-code]
                                 					 country-code } [load
                                 				  TAR- filename ]

no user-locale [user-locale-tag] { [user-defined-code]
                                 					 country-code } [load
                                 				  TAR- filename ]

## Syntax Description

(Optional) Identifier for the specified locale. Required to
                                       					 configure multiple locales only. Range is 0 to 4. Default is 0.

(Optional) Label for locale that is not one of the 12 standard
                                       					 ISO 366 locales. Use each label for only one user-locale-tag at a time. Values
                                       					 are U1 , U2 , U3 , U4 , and U5 .

- DE —Germany

- DK —Denmark

- ES —Spain

- FR —France

- IT —Italy

- JP —Japan

- NL —Netherlands

- NO —Norway

- PT —Portugal

- RU —Russia

- SE —Sweden

- U1 —User defined
                                          						user-locale 1

- U2 —User
                                          						defined user-locale 2

- U3 —User
                                          						defined user-locale 3

- U4 —User
                                          						defined user-locale 4

- U5 —User
                                          						defined user-locale 5

- US —United
                                          						States

Any valid ISO 639 code to be associated with the
                                             						  user-defined-code argument (U1 to U5) only. Code must be for a supported locale
                                             						  that is not listed above and for which the XML files can be downloaded to
                                             						  flash, slot 0, or a TFTP server.

U1 , U2 , U3 , U4 , U5 —Only when U1 to U5 corresponds
                                             						  to a user-defined locale for which the TAR file is downloaded to flash, slot 0,
                                             						  or a TFTP server.

(Optional) Loads the specified localization package file.

### Command Default

The default user-locale tag is 0 and the default locale is US (United
                              		  States).

### Command Modes

Voice register global (config-register-global) Voice register template (config-register-temp)

## Command History

15.1(4)M

Cisco Unified CME 8.6

This command was introduced.

15.2(2)T

Cisco Unified CME 9.0

This command was introduced.

### Usage Guidelines

This command sets the language for displays on supported phone types.

The show voice register global command displays the language (locale) that is set
                              		  using this command. This locale is associated with the dictionary and language
                              		  files.

Follow this command with a complete phone reboot using
                              		  the reset (voice register global) command.

User-locale 0 always holds the default language that is used for all
                              		  SIP phones that are not assigned alternative user locales or user-defined user
                              		  locales. The system default is US (United States) unless you use this command
                              		  to designate a different locale for user-locale 0.

The user-locale-tag argument allows you to specify up to five
                              		  alternative user locales. For example, a company can specify French for phones
                              		  A, B, and C; German for phones D, E, and F; and United States for phones G, H,
                              		  and I.

Each of the five user locales that you can use in a multilocale system
                              		  is identified with the user-locale-tag argument. The identifier 0 always holds
                              		  the default locale, although you can define this default to be any language
                              		  code that is supported in the system and is listed in CLI help for the command.
                              		  For example, if you define locale-tag 0 to be JP (Japanese), the default user
                              		  locale for the router is JP. If you do not specify a locale for identifier 0,
                              		  the default is US (United States). If you are using this command to configure a
                              		  default locale for all SIP phones in your system, you are not required to
                              		  include user-locale-tag 0 in the command.

Use the user-locale command in voice register template configuration mode
                              		  to apply a locale tag to a voice register template. Use the voice
                                    				register template command in global configuration mode to apply
                              		  the template to phones that should use the alternative language.

## Examples

The following example sets the default language tag for the IP phone
                              		  display to French:

```
voice register global
user-locale 0 FR
```

```
Tftp path is flash:
Generate text file is disabled
Tftp files are created, current syncinfo 0202310605309206
OS79XX.TXT is not created
timeout interdigit 10
network-locale[0] US (This is the default network locale for this box)
network-locale[1] US
network-locale[2] US
network-locale[3] US
network-locale[4] US
user-locale[0] U2 language code CH (This is the default user locale for this
box)
user-locale[1] US
user-locale[2] US
user-locale[3] US
user-locale[4] US Active registrations : 2
Total SIP phones registered: 2
Total Registration Statistics
Registration requests : 4
```

The following example sets user-locale 2 and 3 for voice register
                              		  template 5 and 6, respectively:

```
voice register template 1
softkeys hold Resume Newcall
softkeys idle Redial DND Gpickup Pickup Cfwdall
softkeys connected Endcall Hold Confrn Park Trnsfer
softkeys remote-in-use Barge Newcall cBarge
no transfer-blind enable
!
voice register template 5
user-locale 2
!
voice register template 6
user-locale 3
!
```

The following example loads the locale package file for Germany:

```
Router(config)# voice register global
Router(config-register-global)# user-locale 2 DE load CME-locale-de_DE-German-8.6.3.0.tar
```

The following example loads the locale package file for Italy:

```
Router(config)#voice register global
Router(config-register-global)# user-locale IT load CME-locale-it_IT-Italian-8.6.2.4.tar LOCALE INSTALLER MESSAGE (SIP):Loading Locale Package...
LOCALE INSTALLER MESSAGE: VER:2
LOCALE INSTALLER MESSAGE: Langcode:it_IT
LOCALE INSTALLER MESSAGE: Language:Italian
LOCALE INSTALLER MESSAGE: Filename: g3-tones.xml
LOCALE INSTALLER MESSAGE: Filename: tags_file
LOCALE INSTALLER MESSAGE: Filename: utf8_tags_file
LOCALE INSTALLER MESSAGE: Filename: gd-sip.jar
LOCALE INSTALLER MESSAGE: Filename: g4-tones.xml
LOCALE INSTALLER MESSAGE: New Locale configured
```

### Related Commands

Command

Description

reset (voice register global)

Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router.

show voice register global

Displays the current configuration files that are accessible
                                          						to the Cisco Unified SIP IP phones.

voice register global

Sets global parameters for all supported Cisco SIP IP phones
                                          						in a Cisco Unified CME environment.

voice register template

Defines a template of common parameters for Cisco Unified
                                          						SIP IP phones.

## username (ephone)

To assign a login account username and password to a phone user so
                              		  that the user can log in to the Cisco Unified CME router through a web browser,
                              		  use the username command in ephone configuration
                              		  mode. To disable the username and password, use the no form of this command.

username username password [0|6] password

no username username password [0|6] password

### Syntax Description

username

Unique alphanumeric string to identify a user for this
                                          						authentication credential only. String can contain a maximum of 28 alphanumeric
                                          						characters. Default is Admin.

password

Enables password for the Cisco Unified IP phone user.

password

Password string.

### Command Default

The default username for the administrator is Admin.

### Command Modes

Ephone configuration (config-ephone)

## Command History

Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.1

This command was introduced.

12.2(8)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command was enhanced for password encryption, based on Unified CME password policy.

### Usage Guidelines

This command assigns a login account username and password for a
                              		  phone user and establishes a login account for each Cisco Unified IP phone.
                              		  This configuration can be completed only by the local system administrator of
                              		  the Cisco Unified CME router.

You must also create a login account to allow Telephone Application
                              		  Programming Interface (TAPI)-aware PC applications to register with the Cisco
                              		  router and exercise remote-control operation of a Cisco Unified IP phone.

The user name parameter of any authentication credential must be
                              		  unique. Do not use the same value for a user name when you configure any two or
                              		  more authentication credentials in Cisco Unified CME, such as the username for
                              		  any Cisco United CME GUI account and the user name in a profile for Extension
                              		  Mobility.

This configuration permits the phone user to log in to Cisco Unified
                              		  CME to view and change attributes associated only with the user’s IP phone.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] . This in accordance with Unified CME Password Policy. The 0 in the parameter [0|6] mentioned in the CLI command represents
                              plain, unencrypted text and 6 represents level 6 password encryption.

## Examples

The following example shows how to set the username and password:

```
Router(config)# ephone 1 Router(config-ephone)# username smith password 9golf
```

### Related Commands

Description

admin - password

Sets a password for the local system administrator of the
                                          						Cisco IOS Telephony Service.

admin - username

Sets the username for the local system administrator of the
                                          						Cisco IOS Telephony Service router.

## username (voice register pool)

To assign an authentication credential to a phone user so that the SIP phone can register in Cisco CallManager Express (Cisco
                              CME), use the username command in voice register pool configuration mode. To disable a username and password, use the no form of this command.

username username [ password [0|6] password ]

no username username [ password [0|6] password ]

### Syntax Description

username

Username of the local Cisco IP phone user. Default: Admin.

password

Enables password for the Cisco IP phone user.

password

Password string.

### Command Default

Authentication credential is not created.

### Command Modes

Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command was enhanced for password encryption, based on Unified CME password policy.

### Usage Guidelines

Creates an authentication credential for SIP IP phone registration.
                              		  This command is required if authentication is enabled with the authenticate command.

You must configure the voice register pool before configuring an
                              		  authentication credential.

All lines in a phone share the same credential.

This configuration also permits the phone user to log in to Cisco Unified CME to view and change attributes associated only
                              with the user’s SIP IP phone.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] . This in accordance with Unified CME Password Policy. The 0 in the parameter [0|6] mentioned in the CLI command represents
                              plain, unencrypted text and 6 represents level 6 password encryption.

## Examples

The following example shows how to set the username and password:

```
Router(config)# voice register pool 1 Router(config-register-pool)# username smith password 0 9golf
```

### Related Commands

Description

authenticate (voice register global)

Enables authentication for registration requests in which
                                          						the MAC address cannot be identified by using other methods

## utf8

To define Unicode UTF-8 support for a phone type, use the utf8 command in ephone-type configuration mode. To reset to the
                              		  default value, use the no form of this command.

utf8

no utf8

### Syntax Description

This command has no arguments or keywords.

### Command Default

Phone type supports Unicode UTF-8.

### Command Modes

Ephone-type configuration (config-ephone-type)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3 Cisco Unified SRST 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command specifies whether Unicode UTF-8 is supported by the type
                              		  of phone that is being added with the phone-type template.

## Examples

The following example shows that UTF-8 support is set to disabled for
                              		  the Nokia E61 when creating the ephone-type template:

```
Router(config)# ephone-type E61 Router(config-ephone-type)# no utf8
```

### Related Commands

Command

Description

device-id

Specifies the device ID for a phone type.

type

Assigns the phone type to an SCCP phone.

| audio-url | Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| bnea | Specifies the audio file used for the busy station not
                                          						equipped for preemption announcement. |
| ica | Specifies the audio file used for the isolated code
                                          						announcement. |
| vca | Specifies the audio file used for the vacant code
                                          						announcement. |
| mlpp indication | Enables MLPP indication on an SCCP phone or analog FXS
                                          						port. |
| mlpp preemption | Enables preemption capability on an SCCP phone or analog
                                          						FXS port. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| create profile (voice register global) | Generates configuration profile files required for SIP IP
                                          						phones in Cisco Unified CME. |
| load (voice register global) | Associates a type of IP phone with a phone firmware file. |
| mode cme | Enables the mode for configuring SIP IP phones in Cisco
                                          						Unified CME. |
| reset (voice register pool) | Reboots and reregisters a SIP IP phone, including
                                          						contacting the DHCP server for updated information. |
| show voice register tftp-bind | Displays the current configuration files accessible to SIP
                                          						phones. |

| authentication | Uses the information at the specified URL to validate
                                          						requests made to the phone web server. |
|---|---|
| directories | Uses the information at the specified URL for the
                                          						Directories button display. |
| idle | Information at the specified URL displays on the window of
                                          						the IP phone during the idle state. |
| information | Uses the information at the specified URL for the
                                          						Information button display. This button can be labeled “i” or “?”. Note Cisco Unified CME does not support the use of this URL. | Note | Cisco Unified CME does not support the use of this URL. |
| Note | Cisco Unified CME does not support the use of this URL. |
| messages | Uses the information at the specified URL for the Messages
                                          						button display. |
| proxy-server | Specifies the host and port used to enable proxy HTTP
                                          						requests for access to remote host addresses from the phone HTTP client. |
| services | Uses the information at the specified URL for the Services
                                          						button display. |
| url | URL as defined in RFC 2396. |
| line | (optional) Supported only with services keyword. Alphanumeric string of
                                          						1 to 32 characters that is line-services name to be displayed under Services
                                          						button. |
| root | (optional) Supported only with services keyword and supported in
                                          						telephony-service mode only. Menu of root phone services supported by a CSTA
                                          						client application is displayed under Services button. |

| Note | Cisco Unified CME does not support the use of this URL. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(22)T | Cisco Unified CME 7.0(1) | This command was added to VRF group configuration mode. |
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was modified. Support for the root keyword was added to this
                                          						command. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Note | Cisco Unified CME does not support provisioning an information URL
                                       		  to access help using the i or ? buttons on a phone. |
|---|---|

| Note | Provisioning of the directory URL to select an external directory
                                       		  resource disables the Cisco Unified CME local directory service. |
|---|---|

| Command | Description |
|---|---|
| group | Creates a virtual router forwarding (VRF) group for Cisco
                                          						Unified CME users and phones. |
| reset (ephone) | Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router. |
| reset (telephony-service) | Performs a complete reboot of one or all phones associated
                                          						with a Cisco Unified CME router. |
| service local-directory | Enables the availability of the local directory service on
                                          						IP phones. |
| voicemail | Defines the telephone number that is speed-dialed when the
                                          						Messages button on a Cisco Unified IP phone is pressed. |

| authentication | Uses
                                          						the information at the specified URL to validate requests made to the phone web
                                          						server. |
|---|---|
| directory | Uses
                                          						the information at the specified URL for the Directories button display. |
| service | Uses
                                          						the information at the specified URL for the Services button display. |
| idle | Uses
                                          						the information at the specified URL to display on the IP phone during the idle
                                          						state. |
| url | URL as
                                          						defined in RFC 2396. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| Cisco
                                          						IOS XE Everest 16.6.1 | Cisco
                                          						Unified CME 12.0 | The idle keyword was added. |
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |

| Note | Provisioning
                                       		  the directory URL to select an external directory resource disables Cisco
                                       		  Unified CME local directory service. |
|---|---|

| Commands | Description |
|---|---|
| reset (voice register pool) | Performs a complete reboot of one phone associated with a Cisco CME router. |
| reset (voice register global) | Performs a complete reboot of all SIP phones associated with a Cisco CME
                                          						router. |
| telephony-service | Enters telephony-service configuration mode. |
| voicemail (voice register template) | Defines the telephone number that is speed-dialed when the Messages button on a
                                          						Cisco IP phone is pressed. |

| url AppDialRule string | Application dial rule URL. |
|---|---|
| url DirLookupRule string | Directory lookup rule URL. |
| url ldapServer string | LDAP
                                          						server URL. |
| url idle url | Defines
                                          						the location of a file to display on phones that are not in use and specifies
                                          						the interval between refreshes of the display, in seconds. |
| url service url | Uses the
                                          						information at the specified URL for invoking phone services. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| Cisco
                                          						IOS XE Everest 16.6.1 | Unified
                                          						CME 12.0 | This
                                          						command was modified to add idle and service keywords. |

| Commands | Description |
|---|---|
| voice register
                                                							 pool | Enters voice register pool configuration mode. |
| voice register
                                                							 template | Enters
                                          						voice register template configuration mode. |

| url-address | URL adddress of authentication server. The URL address for the authentication server in Cisco
                                          						Unified CME is: http:// CME IP Address /CCMCIP/authenticate.asp . |
|---|---|
| application-name | Character string sent by application to identify itself to
                                          						the server. Length of string: 1 to 15 characters. For applications other than Extension Mobility, the name
                                          						portion of the credential must first be created in the application. |
| password [0\|6] | Character string sent by application to identify itself to
                                          						the server. Length of string: 1 to 15 characters. The 0 in the parameter [0\|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption. For applications other than Extension Mobility, the password portion of the credential must first be created in the application. |

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command was enhanced for password encryption, based on Unified CME password policy. |

| Command | Description |
|---|---|
| authentication credential | Stores credentials in the database for the Cisco Unified
                                          						CME authentication server. |
| keep call-history | Disables Automatic Clear Call History for Extension
                                          						Mobility in Cisco Unified CME. |

| url | URL as defined in RFC 2396. |
|---|---|
| idle-timeout seconds | Time interval between display refreshes, in seconds. Range
                                          						is from 0 to 300. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |

|  | Description |
|---|---|
| reset (ephone) | Performs a complete reboot of one phone associated with a
                                          						Cisco CME router. |
| reset (telephony-service) | Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router. |

| url-tag | Identifier for url being configured for Services feature
                                          						button. Range is 1 to 8. |
|---|---|
| url | URL as defined in RFC 2396. |
| url-name | Alpha-numerical string to appear for this URL in Services
                                          						feature button display. Length of string is 1 to 256 contiguous characters
                                          						(a-z, 0-9). |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XW | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies an ephone template to an SCCP phone. |
| url (telephony-service) | Provisions URLs for programmable feature buttons on
                                          						supported Cisco Unified IP phones. |

| index | Unique
                                          						index number. The range is from 1 to 8. |
|---|---|
| type | Type of
                                          						service URL button. The following types of URL service buttons are available: myphoneapp: My phone
                                             						  application configured under phone user interface. em: Extension Mobility snr: Single Number Reach voicehuntgroups: Displays a
                                             						  list of voice hunt groups park-list: Displays a list
                                             						  of parked calls |
| url-button | Service
                                          						url with maximum length of 31 characters. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco
                                          						Unified CME 8.5 | This
                                          						command was introduced. |
| 15.4(3)M | Cisco
                                          						Unified CME 10.5 | This
                                          						command was modified to add voice hunt groups and park-list as new types . |

| Command | Description |
|---|---|
| show telephony-service ephone-template | Displays the contents of all the ephone templates defined. |

| index number | Unique index number. Range: 1 to 8. |
|---|---|
| url location | Location of the url. |
| url name | Service url with maximum length of 31 characters. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| show voice register template | Displays all configuration information associated with a
                                          						SIP phone template, |

| name | Unique alphanumeric string to be used by a TAPI phone
                                          						device to log into Cisco Unified CME. String can contain a maximum of 15
                                          						alphanumeric characters. |
|---|---|
| password | Password to be used with this username for authentication
                                          						purposes. |
| password [0\|6] | Alphanumeric string. The 0 in the parameter [0\|6] represents plain, unencrypted text and 6 represents level 6 password encryption. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command was enhanced for password encryption, based on Unified CME password policy. |

| Command | Description |
|---|---|
| logout-profile | Enables a Cisco Unified IP phone for extension mobility and
                                          						assigns a logout profile to this phone. |
| reset (voice logout-profile and voice user-profile) | Performs a complete reboot of all IP phones to which a
                                          						particular logout-profile or user-profile is downloaded. |

| name | Unique alphanumeric string to identify a user for this
                                       					 authentication credential only. String can contain a maximum of 15 alphanumeric
                                       					 characters. |
|---|---|
| password | Password to be used with this user name for authentication
                                       					 purposes. |
| password | Alphanumeric string. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| reset (voice logout-profile and voice user-profile) | Preforms complete reboot of all IP phones on which a
                                          						particular logout-profile or user-profile is downloaded. |

| user-locale-tag | Locale identifier that was assigned to the user locale
                                          						using the user-locale (telephony-service) command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| cnf-file | Specifies the type of configuration files that phones use. |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| user-locale (telephony-service) | Sets the language for displays on supported phone types. |

| user-locale-tag | (Optional) Identifier for the specified locale. Required to
                                          						configure multiple locales only. Range is 0 to 4. Default is 0. |
|---|---|
| user-defined-code | (Optional) Label for locale that is not one of the 12
                                          						standard ISO 366 locales. Use each label for only one user-locale-tag at a time. Values
                                          						are U1 , U2 , U3 , U4 , and U5 . |
| country-code | DE —Germany DK —Denmark ES —Spain FR —France IT —Italy JP —Japan NL —Netherlands NO —Norway PT —Portual RU —Russia SE —Sweden US —United States Any valid ISO 639 code to be associated with the user-defined-code argument (U1 to
                                             						  U5) only. Code must be for a supported locale that is not listed above and for
                                             						  which the XML files can be downloaded to flash, slot 0, or a TFTP server. U1 , U2 , U3 , U4 , U5 —Only when used with the load keyword and where U1 to U5
                                             						  corresponds to a user-defined locale for which the TAR file is downloaded to
                                             						  flash, slot 0, or a TFTP server. |
| load | (Optional) Extracts contents of a TAR file to the location
                                          						specified by using the cnf-file location command. This keyword is supported in Cisco Unified
                                          						CME 7.0(1) and later versions. |
| TAR-filename | TAR file containing the language JAR file and the
                                          						tg3-tones.xml file for country-specific network tones and cadences. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The following keywords were added: DK , NL , NO , PT , RU , and SE . |
| 12.3(4)T | Cisco CME 3.0 | The keywords added for Cisco CME 3.0 were integrated into
                                          						Cisco IOS Release 12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The user- locale-tag and user-defined-code arguments were added. |
| 12.4(9)T | Cisco Unified CME 4.0 | The user-locale-tag and user-defined-code arguments were integrated into Cisco
                                          						IOS Release 12.4(9)T. |
| 12.4(20)YA | Cisco Unified CME 7.0(1) | The load TAR-filename keyword/argument combination for the locale installer was added. |
| 12.4(22)T | Cisco Unified CME 7.0(1) | This command was integrated into Cisco IOS Release
                                          						12.4(22)T. |

| Command | Description |
|---|---|
| cnf-file location | Specifies a storage location for XML configuration files. |
| cnf-files | Specifies the type of phone configuration files to be
                                          						created. |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| network-locale (telephony-service) | Selects a code for a geographically specific set of tones
                                          						and cadences on supported phone types. |
| reset (ephone) | Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router. |
| reset (telephony-service) | Performs a complete reboot of one or all phones associated
                                          						with a Cisco Unified CME router. |
| show telephony-service tftp-bindings | Displays the current configuration files that are
                                          						accessible by IP phones. |
| user-locale (ephone-template) | Applies a user locale tag to an ephone template. |

| user-locale-tag | (Optional) Identifier for the specified locale. Required to
                                       					 configure multiple locales only. Range is 0 to 4. Default is 0. |
|---|---|
| user-defined-code | (Optional) Label for locale that is not one of the 12 standard
                                       					 ISO 366 locales. Use each label for only one user-locale-tag at a time. Values
                                       					 are U1 , U2 , U3 , U4 , and U5 . This option is only available after the tftp-path command is configured in voice register global
                                    				  configuration mode and the directory in which the configuration files are
                                    				  written is specified (flash, slot, or an external TFTP server). |
| country-code | DE —Germany DK —Denmark ES —Spain FR —France IT —Italy JP —Japan NL —Netherlands NO —Norway PT —Portugal RU —Russia SE —Sweden U1 —User defined
                                          						user-locale 1 U2 —User
                                          						defined user-locale 2 U3 —User
                                          						defined user-locale 3 U4 —User
                                          						defined user-locale 4 U5 —User
                                          						defined user-locale 5 US —United
                                          						States Any valid ISO 639 code to be associated with the
                                             						  user-defined-code argument (U1 to U5) only. Code must be for a supported locale
                                             						  that is not listed above and for which the XML files can be downloaded to
                                             						  flash, slot 0, or a TFTP server. U1 , U2 , U3 , U4 , U5 —Only when U1 to U5 corresponds
                                             						  to a user-defined locale for which the TAR file is downloaded to flash, slot 0,
                                             						  or a TFTP server. |
| load TAR-filename | (Optional) Loads the specified localization package file. Note Use the complete filename, including the file suffix
                                                					 (.tar), when you configure the user-locale command for all Cisco Unified SIP IP
                                                					 phone types. | Note | Use the complete filename, including the file suffix
                                                					 (.tar), when you configure the user-locale command for all Cisco Unified SIP IP
                                                					 phone types. |
| Note | Use the complete filename, including the file suffix
                                                					 (.tar), when you configure the user-locale command for all Cisco Unified SIP IP
                                                					 phone types. |

| Note | Use the complete filename, including the file suffix
                                                					 (.tar), when you configure the user-locale command for all Cisco Unified SIP IP
                                                					 phone types. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(4)M | Cisco Unified CME 8.6 | This command was introduced. |
| 15.2(2)T | Cisco Unified CME 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| reset (voice register global) | Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router. |
| show voice register global | Displays the current configuration files that are accessible
                                          						to the Cisco Unified SIP IP phones. |
| voice register global | Sets global parameters for all supported Cisco SIP IP phones
                                          						in a Cisco Unified CME environment. |
| voice register template | Defines a template of common parameters for Cisco Unified
                                          						SIP IP phones. |

| username | Unique alphanumeric string to identify a user for this
                                          						authentication credential only. String can contain a maximum of 28 alphanumeric
                                          						characters. Default is Admin. |
|---|---|
| password | Enables password for the Cisco Unified IP phone user. |
| password | Password string. |

| Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command was enhanced for password encryption, based on Unified CME password policy. |

|  | Description |
|---|---|
| admin - password | Sets a password for the local system administrator of the
                                          						Cisco IOS Telephony Service. |
| admin - username | Sets the username for the local system administrator of the
                                          						Cisco IOS Telephony Service router. |

| username | Username of the local Cisco IP phone user. Default: Admin. |
|---|---|
| password | Enables password for the Cisco IP phone user. |
| password | Password string. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command was enhanced for password encryption, based on Unified CME password policy. |

| Note | This command is not for SIP proxy registration. |
|---|---|

|  | Description |
|---|---|
| authenticate (voice register global) | Enables authentication for registration requests in which
                                          						the MAC address cannot be identified by using other methods |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| device-id | Specifies the device ID for a phone type. |
| type | Assigns the phone type to an SCCP phone. |