---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr1-vcr1-cr-book-vcr-c2-html-19514982e9
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr1/vcr1-cr-book/vcr-c2.html
retrieved_at: 2026-08-16T23:15:27.266411+00:00
---

Cisco IOS Voice Command Reference - A through C

# Cisco IOS Voice Command Reference - A through C

Updated: April 25, 2026

Chapter: call application voice through call denial

## Chapter: call application voice through call denial

# call application voice through call denial

## call application voice

Effective with Cisco IOS Release 12.3(14)T, the call application voice command is replaced by the commands shown in the table below. See these commands for more information.

To define the name of a voice application and specify the location of the Tool Command Language (Tcl) or VoiceXML document
                              to load for this application, use the call application voice command in global configuration mode. To remove the defined application and all configured parameters associated with it,
                              use the no form of this command.

call application voice application-name { location | av-pair }

no call application voice application-name

### Syntax Description

application-name

Character string that defines the name of the voice application.

location

Location of the Tcl script or VoiceXML document in URL format. Valid storage locations are TFTP, FTP, HTTP, and flash memory.

av-pair

Text string that defines attribute-value (AV) pairs specified by the Tcl script and understood by the RADIUS server. Multiple
                                          AV pairs can be enclosed in quotes; up to 512 entries are supported.

### Command Default

None

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XH

This command was introduced.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T. The location argument was added.

12.1(3)T

The av-pair argument was added for AV pairs.

12.1(5)T

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB

This command was modified to support VoiceXML applications and HTTP server locations on the Cisco AS5300, Cisco AS5350, and
                                          Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750.

12.2(4)XM

This command was implemented on the Cisco 1751. Support for other Cisco platforms is not included in this release.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 2600 series, Cisco 3600 series,
                                          Cisco 3725, Cisco 3745, and Cisco 7200 series.

12.2(11)T

This command was implemented for VoiceXML applications. This command is supported on the Cisco AS5300, Cisco AS5350, Cisco
                                          AS5400, Cisco AS5800, and Cisco AS5850 in this release.

12.2(15)T

MCID AV-pairs were added for the av-pair argument; they are mcid-dtmf, mcid-release-timer, and mcid-retry-limit.

12.3(8)T

Support was added to allow up to 512 multiple AV pairs (enclosed in quotes) to be used in a single command.

12.3(14)T

This command was replaced. The call application voice command was replaced by the commands shown in the table below.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

The call application voice command was replaced by the commands shown in the table below.

Command

Command Mode

Purpose

application

Global configuration

Enters application configuration mode to configure voice applications and services.

service

Application configuration

Enters service configuration mode to configure a standalone application, such as a debit card script.

package

Application configuration

Use to load and configure a package. A package is a linkable set of C or Tcl functions that provide functionality invoked
                                          by applications or other packages.

param

Application parameter configuration

Use to configure parameters for services or packages.

Use this command when configuring interactive voice response (IVR) or one of the IVR-related features (such as Debit Card)
                              to define the name of an application and to identify the location of the Tcl script or VoiceXML document associated with the
                              application.

A voice application must be configured by using this command before the application can be configured with the application command in a dial peer.

Tcl scripts and VoiceXML documents can be stored in any of the following locations: on TFTP, FTP, or HTTP servers, in the
                              flash memory of the gateway, or on the removable disks of the Cisco 3600 series. The audio files that they use can be stored
                              in any of these locations, and on Real-Time Streaming Protocol (RTSP) servers.

HTTP is the recommended protocol for loading applications and audio prompts because of its efficient design for loading information
                              over the web. For example, it has methods for determining how long a file can be cached and whether a cached file is still
                              valid.

Include the file type extension in the filename (.vxml or .tcl) when specifying the document used by the application. Tcl
                              files require the extension .tcl, and VoiceXML documents require .vxml.

The no call application voice command causes all related call application commands--for instance, call application voice language and call application voice set-location --to be deleted. The no call application voice application-name command removes the entire application and all parameters, if configured.

## Examples

Effective with Cisco IOS Release 12.3(14)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice Warning: This command has been deprecated. Please use the following:
             application
               service
                 package
					param
```

The following example defines the fax-relay application and the TFTP server location of the associated Tcl script:

```
call application voice fax-relay tftp://keyer/faxrelay.tcl
```

The following example defines the application "prepaid" and the TFTP server location of the associated Tcl script:

```
call application voice prepaid tftp://keyer/debitcard.tcl
```

The following is an example of AV pair configuration:

```
set avsend(h323-ivr-out,)) "payphone:true"
set avsend(323-ivr-out,1) "creditTime:3400"
```

The AV pair (after the array is defined, as in the prior example) must be sent to the server using the authentication, authorization,
                              and accounting (AAA) authenticate or AAA authorize verbs as follows:

```
aaa authenticate $account $password $avsend
```

The script would use this AV pair whenever it is needed to convey information to the RADIUS server that cannot be represented
                              by the standard vendor-specific attributes (VSAs).

The following example shows how to define the VoiceXML application "vapptest1" and the flash memory location of the associated
                              VoiceXML document "demo0.vxml":

```
call application voice vapptest1 flash:demo0.vxml
```

The following example specifies the MCID application name, the TFTP server location of the associated Tcl script, and the
                              AV-pairs associated with the MCID application:

```
call application voice mcid tftp://keyer/app_mcid.2.0.0.40.tcl
call application voice mcid mcid-dtmf #99
call application voice mcid-retry-limit 3
call application voice mcid mcid-release-timer 90
```

### Related Commands

Command

Description

application (dial peer)

Defines the call application in the dial peer.

application (global configuation)

Enters application configuration mode to configure applications.

call application voice language

Defines the language of the audio file for the designated application and passes that information to the application.

call application voice load

Reloads the designated Tcl script or VoiceXML document.

call application voice pin-len

Defines the number of characters in the PIN for the application and passes that information to the application.

call application voice redirect-number

Defines the telephone number to which a call is redirected for the designated application.

call application voice retry-count

Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application.

call application voice security trusted

Sets the security level of a VoiceXML application to trusted so that ANI is not blocked.

call application voice set-location

Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application.

call application voice uid-len

Defines the number of characters in the UID for the designated application and passes that information to the application.

call application voice warning-time

Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application.

package

Enters application parameter configuration mode to load and configure a package.

param

Loads and configures parameters in a package or a service (application) on the gateway.

service

Loads and configures a specific, standalone application on a dial peer.

show call application voice

Displays information about voice applications.

## call application voice access-method

Effective with Cisco IOS Release 12.3(14)T, the call application voice access-method command was replaced by the param access-method command in application parameter configuration mode. See the param access-method command for more information.

To specify the access method for two-stage dialing for the designated application, use the call application voice access-method command in global configuration mode. To restore default values for this command, use the no form of this command.

call application voice application-name access-method { prompt-user | redialer }

no call application voice application-name access-method

### Syntax Description

application-name

Name of the application.

prompt-user

Specifies that no DID is set in the incoming POTS dial peer and that a Tcl script in the incoming POTS dial peer is used for
                                          two-stage dialing.

redialer

Specifies that no DID is set in the incoming POTS dial peer and that the redialer device are used for two-stage dialing.

### Command Default

Prompt-user (when DID is not set in the dial peer)

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into the Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was introduced on the Cisco 1750.

12.3(14)T

This command was replaced by the param access-method command in application parameter configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Use the call application voice access-method command to specify the access method for two-stage dialing when DID is disabled in the POTS dial peer.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice access-method Warning: This command has been deprecated. Please use the following:
             param access-method
```

The following example specifies prompt-user as the access method for two-stage dialing for the app_libretto_onramp9 IVR application:

```
call application voice app_libretto_onramp9 access-method prompt-user
```

### Related Commands

Command

Description

call application voice

Loads a specified application onto the router from the TFTP server and gives it an application name by which it is known on
                                          the router.

call application voice language

Defines the language of the audio file for the designated application and passes that information to the application.

call application voice load

Reloads the designated Tcl script.

call application voice pin len

Defines the number of characters in the PIN for the application and passes that information to the application.

call application voice redirect number

Defines the telephone number to which a call is redirected--for example, the operator telephone number of the service provider--for
                                          the designated application.

call application voice retry count

Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application.

call application voice set location

Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application.

call application voice uid len

Defines the number of characters in the UID for the designated application and passes that information to the application.

call application voice warning time

Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application.

param access-method

Specifies the access method for two-stage dialing for the designated application.

## call application voice account-id-method

Effective with Cisco IOS Release 12.3(14)T, the call application voice account-id-method command is replaced by the param account-id-method command in application parameter configuration mode. See the param account-id-method command for more information.

To configure the fax detection IVR application to use a particular method to assign the account identifier, use the call application voice account id method command in global configuration mode. To remove configuration of this account identifier, use the no form of this command.

call application voice application-name account-id-method { none | ani | dnis | gateway }

no call application voice application-name account-id-method

### Syntax Description

application-name

Name of the defined fax detection IVR application.

none

Account identifier is blank. This is the default.

ani

Account identifier is the calling party telephone number (automatic number identification, or ANI).

dnis

Account identifier is the dialed party telephone number (dialed number identification service, or DNIS).

gateway

Account identifier is a router-specific name derived from the hostname and domain name, displayed in the following format:
                                          router-name.domain-name.

### Command Default

No default behavior or values.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(5)XM

This command was introduced for the Cisco AS5300.

12.2(2)XB

This command was implemented on the Cisco AS5400 and Cisco AS5350.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600
                                          series, Cisco 3725, and Cisco 3745.

12.2(11)T

This command was implemented on the Cisco AS5300, the Cisco AS5350, and Cisco AS5400.

12.3(14)T

This command was replaced by the param account-id-method command in application parameter configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

When an on-ramp application converts a fax into an e-mail, the e-mail contains a field called x-account-id, which can be used
                              for accounting or authentication. The x-account-id field can contain information supplied as a result of this command, such
                              as the calling party’s telephone number ( ani ), the called party’s telephone number ( dnis ), or the name of the gateway ( gateway ).

This command is not supported by Cisco IOS help; that is, if you type the call application voice fax_detect account-id-method command and a question mark (?) , the Cisco IOS help does not supply a list of entries that are valid in place of the question mark.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application fax_detect account-id-method gateway Warning: This command has been deprecated. Please use the following:
             param account-id-method
```

The following example sets the fax detection IVR application account identifier to the router-specific name derived from the
                              hostname and domain name:

```
call application voice fax_detect account-id-method gateway
```

### Related Commands

Command

Description

call application voice

Loads a specified IVR application onto the router from the TFTP server and gives it an application name by which it is known
                                          on the router.

call application voice fax dtmf

Configures the fax detection IVR application to recognize a specified digit that indicates a fax call in default-voice and
                                          default-fax modes.

call application voice mode

Configures the fax detection IVR application to operate in one of its four modes.

call application voice prompt

Configures the fax detection IVR application to use the specified audio file as a user prompt in listen-first mode, default-voice
                                          mode, or default-fax mode.

call application voice voice dtmf

Configures the fax detection IVR application to recognize a specified digit that indicate a voice call in default-voice and
                                          default-fax modes.

param account-id-method

Configures an application to use a particular method to assign the account identifier.

## call application voice authentication enable

Effective with Cisco IOS Release 12.3(14)T, the call application voice authentication enable command is replaced by the param authentication enable command in application configuration mode. See the param authentication enable command for more information.

To enable authentication, authorization, and accounting (AAA) services for a Tool Command Language (TCL) application, use
                              the call application voice authentication enable command in global configuration mode. To disable authentication for a TCL application, use the no form of this command.

call application voice application-name authentication enable

no call application voice application-name authentication enable

### Syntax Description

application-name

Name of the application.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.3(14)T

This command was replaced by the param authentication enable command in application configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command enables AAA authentication services for a TCL application if a AAA authentication method list has been defined
                              using both the aaa authentication command and the call application voice authen-list command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice authentication enable Warning: This command has been deprecated. Please use the following:
			param authentication enable
```

The following example enables a AAA authentication method list (called "sample") to be used with outbound store-and-forward
                              fax.

```
call application voice app_eaample_onramp9 authen-list sample
call application voice app_example_onramp9 authentication enable
```

### Related Commands

Command

Description

aaa authentication

Enables AAA accounting of requested services when you use RADIUS or TACACS+.

call application voice authen-list

Specifies the name of an authentication method list for a TCL application.

call application voice authen-method

Specifies the authentication method for a TCL application.

## call application voice accounting-list

Effective with Cisco IOS Release 12.3(14)T, the call application voice accounting-list command is replaced by the param accounting-list in application configuration mode. See the param accounting-list command for more information.

To define the name of the accounting method list to be used for authentication, authorization, and accounting (AAA) with store-and-forward
                              fax on a voice feature card (VFC), use the call application voice accounting list command in global configuration mode. To undefine the accounting method list, use the no form of this command.

call application voice application-name accounting-list method-list-name

no call application voice application-name accounting-list method-list-name

### Syntax Description

application-name

Name of the application.

method-list-name

Character string used to name a list of accounting methods to be used with store-and-forward fax.

### Command Default

No AAA accounting method list is defined

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745.

12.3(14)T

This command was replaced by the param accounting-list in application configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command defines the name of the AAA accounting method list to be used with store-and-forward fax. The method list itself,
                              which defines the type of accounting services provided for store-and-forward fax, is defined using the aaa accounting command. Unlike standard AAA (in which each defined method list can be applied to specific interfaces and lines), the AAA
                              accounting method lists that are used in store-and-forward fax are applied globally.

After the accounting method lists have been defined, they are enabled by using the mmoip aaa receive-accounting enable command.

This command applies to both on-ramp and off-ramp store-and-forward fax functions on VFCs. The command is not used on modem
                              cards.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice accounting-list Warning: This command has been deprecated. Please use the following:
			param accounting-list
```

The following example defines a AAA accounting method list "example" to be used with store-and-forward fax:

```
aaa new-model
call application voice app_libretto_onramp9 accounting-list example
```

### Related Commands

Command

Description

aaa accounting

Enables AAA accounting of requested services when you use RADIUS or TACACS+.

call application voice accounting enable

Enables AAA accounting for a TCL application.

mmoip aaa receive-accounting enable

Enables on-ramp AAA accounting services.

## call application voice accounting-template

Effective with Cisco IOS Release 12.3(14)T, the call application voice accounting-template command is obsolete. Use the call accounting-template command in application configuration mode to configure a voice accounting template.

To configure T.37 fax accounting with VoIP authentication, authorization, and accounting (AAA) nonblocking Application Programming
                              Interface (API), use the call application voice accounting template command in global configuration mode. To remove the defined application and all configured parameters associated with it,
                              use the no form of this command.

call application voice application-name accounting-template template-name

no call application voice application-name accounting-template template-name

### Syntax Description

application-name

Defines the name of the T.37 voice application.

Use the call application voice command to define the name of a voice application and specify the location of the Tool Command Language (Tcl) or VoiceXML
                                                document to load for this application.

template - name

Defines the name of the template.

Use the call accounting-template voice command to define the template name.

### Command Default

Disabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(1)

This command was introduced.

12.3(14)T

This command is obsolete. Use the call accounting-template command in application configuration mode to configure a voice accounting template.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command enables T.37 fax to be consistent with VoIP AAA accounting services, which uses the Cisco IOS software nonblocking
                              APIs. This command creates accounting templates for faxes by associating the template name with the T.37 onramp or offramp
                              application.

You can define an accounting template to specify information that is included in an accounting packet.

This command applies only to T.37 fax.

Use the show call active fax and the show call history fax commands to check the configuration.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice accounting-template Warning: This command has been deprecated. Please use the following:
             call accounting-template
```

The following is an example configuration using the T.37 accounting template:

```
Router(config)# call application voice t37_onramp accounting-template sample-name Router(config)# call application voice t37_offramp accounting-template sample-name
```

### Related Commands

Command

Description

application

Defines the call application in the dial peer.

call accounting-template

Selects an accounting template at a specific location.

call accounting-template voice

Selects an accounting template at a specific location.

call application voice

Defines the name of a voice application and specifies the location of the Tcl or VoiceXML document to load for this application.

call application voice language

Defines the language of the audio file for the designated application and passes that information to the application.

call application voice load

Reloads the designated Tcl script or VoiceXML document.

call application voice pin-len

Defines the number of characters in the PIN for the application and passes that information to the application.

call application voice redirect-number

Defines the telephone number to which a call is redirected for the designated application.

call application voice retry-count

Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application.

call application voice security trusted

Sets the security level of a VoiceXML application to trusted so that ANI is not blocked.

call application voice set-location

Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application.

call application voice uid-len

Defines the number of characters in the UID for the designated application and passes that information to the application.

call application voice warning-time

Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application.

show call active fax

Displays call information for fax transmissions in progress.

show call application voice

Displays information about voice applications.

show call history fax

Displays the call history table for fax transmissions.

## call application voice authen-list

Effective with Cisco IOS Release 12.3(14)T, the call application voice authen-list command was replaced by the param authen-list command in application configuration mode. See the param authen-list command for more information.

To specify the name of an authentication method list for a Tool Command Language (Tcl) application, use the call application voice authen list command in global configuration mode. To disable the authentication method list for a Tcl application, use the no form of this command.

call application voice application-name authen-list method-list-name

no call application voice application-name authen-list method-list-name

### Syntax Description

application-name

Name of the application.

method-list-name

Character string used to name a list of authentication methods to be used with T.38 fax relay and T.37 store-and-forward fax.

### Command Default

No default behavior or values.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.3(14)T

This command was replaced by the param authen-list command in application configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command defines the name of the authentication, authorization, and accounting (AAA) method list to be used with fax applications
                              on voice feature cards. The method list itself, which defines the type of authentication services provided for store-and-forward
                              fax, is defined using the aaa authentication command. Unlike standard AAA (in which each defined method list can be applied to specific interfaces and lines), AAA method
                              lists that are used with fax applications are applied globally.

After the authentication method lists have been defined, they are enabled by using the call application voice authentication enable command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice authen-list Warning: This command has been deprecated. Please use the following:
			param authen-list
```

The following example defines a AAA authentication method list (called "fax") to be used with T.38 fax relay and T.37 store-and-forward
                              fax:

```
call application voice app_libretto_onramp9 authen-list fax
```

### Related Commands

Command

Description

aaa authentication

Enable AAA accounting of requested services for billing or security purposes.

call application voice authen-method

Specifies the authentication method for a Tcl application.

call application voice authentication enable

Enables AAA authentication services for a Tcl application.

## call application voice authen-method

Effective with Cisco IOS Release 12.3(14)T, the call application voice authen-method command is replaced by the param authen-method command in application configuration mode. See the param authen-method command for more information.

To specify an authentication, authorization, and accounting (AAA) authentication method for a Tool Command Language (Tcl)
                              application, use the call application voice authen-method command in global configuration mode. To disable the authentication method for a Tcl application, use the no form of this command.

call application voice application-name authen-method { prompt-user | ani | dnis | gateway | redialer-id | redialer-dnis }

no call application voice application-name authen-method { prompt-user | ani | dnis | gateway | redialer-id | redialer-dnis }

### Syntax Description

application-name

Name of the application.

prompt user

User is prompted for the Tcl application account identifier.

ani

Calling party telephone number (automatic number identification or ANI) is used as the Tcl application account identifier.

dnis

Called party telephone number (dialed number identification service or DNIS) is used as the Tcl application account identifier.

gateway

Router-specific name derived from the host name and domain name is used as the Tcl application account identifier, displayed
                                          in the following format: router-name.domain-name .

redialer id

Account string returned by the external redialer device is used as the Tcl application account identifier. In this case, the
                                          redialer ID is either the redialer serial number or the redialer account number.

redialer dnis

Called party telephone number (dialed number identification service or DNIS) is used as the Tcl application account identifier
                                          captured by the redialer if a redialer device is present.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.3(14)T

This command was replaced by the param authen-method command in application configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Normally, when AAA is used for simple user authentication, AAA uses the username information defined in the user profile for
                              authentication. With T.37 store-and-forward fax and T.38 real-time fax, you can specify that the ANI, DNIS, gateway ID, redialer
                              ID, or redialer DNIS be used to identify the user for authentication or that the user be prompted for the Tcl application.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice authen-method Warning: This command has been deprecated. Please use the following:
			param authen-method
```

The following example configures the router-specific name derived from the hostname and domain name as the Tcl application
                              account identifier for the app_sample_onramp9 Tcl application:

```
call application voice app_sample_onramp9 authen-method gateway
```

### Related Commands

Command

Description

call application voice authentication enable

Enables AAA authentication services for a Tcl application.

call application voice authen list

Specifies the name of an authentication method list for a Tcl application.

## call application voice accounting enable

Effective with Cisco IOS Release 12.3(14)T, the call application voice accounting enable command is replaced by the param accounting enable command in application configuration mode. See the param accounting enable command for more information.

To enable authentication, authorization, and accounting (AAA) accounting for a Tool Command Language (Tcl) application, use
                              the call application voice accounting enable command in global configuration mode. To disable accounting for a Tcl application, use the no form of this command.

call application voice application-name accounting enable

no call application voice application-name accounting enable

### Syntax Description

application-name

Name of the application.

### Command Default

Disabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.3(14)T

This command was replaced by the param accounting enable command in application configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command enables AAA accounting services if a AAA accounting method list has been defined using both the aaa accounting command and the mmoip aaa method fax accounting command.

This command applies to off-ramp store-and-forward fax functions.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice accounting enable Warning: This command has been deprecated. Please use the following:
			param accounting enable
```

The following example enables AAA accounting to be used with outbound store-and-forward fax:

```
call application voice app_libretto_onramp9 accounting enable
```

### Related Commands

Command

Description

aaa accounting

Enables AAA accounting of requested services when you use RADIUS or TACACS+.

mmoip aaa method fax accounting

Defines the name of the method list to be used for AAA accounting with store-and-forward fax.

## call application voice default disc-prog-ind-at-connect

Effective with Cisco IOS Release 12.3(14)T, the call application voice default disc-prog-ind-at-connect command is replaced. Use one of the following commands:

param convert-discpi-after-connect (application parameter configuration mode)

paramspace session_xwork convert-discpi-after-connect (service configuration mode)

To convert a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) to a regular DISCONNECT message when the
                              call is in the active state, use the call application voice default disc-prog-ind-at-connect command in global configuration mode. To revert to a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8)
                              when the call is in the active state, use the no form of this command.

call application voice default disc-prog-ind-at-connect [ 1 | 0 ]

no call application voice default disc-prog-ind-at-connect [ 1 | 0 ]

### Syntax Description

1

(Optional) Convert a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) to a regular DISCONNECT message
                                          when the call is in the active state.

0

(Optional) Revert to a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) when the call is in the active
                                          state.

### Command Default

The DISCONNECT message has Progress Indicator set to PROG_INBAND (PI=8) when the call is in the active state.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(15)ZJ

This command was introduced.

12.3(4)T

This command was integrated into Cisco IOS Release 12.3(4)T.

12.3(14)T

The call application voice default disc-prog-ind-at-connect command was replaced. Use one of the following commands:

param convert-discpi-after-connect (application parameter configuration mode)

paramspace session_xwork convert-discpi-after-connect (service configuration mode)

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command has no effect if the call is not in the active state.

This command is available for the default voice application. It may not be available when using some Tcl IVR applications.

The Cisco IOS command-line interface command completion and help features do not work with this command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# voice default disc-prog-ind-at-connect Warning: This command has been deprecated. Please use the following:
			param convert-discpi-after-connect
				paramspace session_xwork convert-discpi-after-connec
```

In the following example, a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) is converted to a regular
                              DISCONNECT message when the call is in the active state:

```
call application voice default disc-prog-ind-at-connect 1
```

### Related Commands

Command

Description

param convert-discpi-after-connect

Enables or disables conversion of a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) to a regular DISCONNECT
                                          message when the call is in the active state.

paramspace session_xwork convert-discpi-after-connect

Enables or disables conversion of a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) to a regular DISCONNECT
                                          message when the call is in the active state.

## call application voice dsn-script

Effective with Cisco IOS Release 12.3(14)T, the call application voice dsn-script command is replaced by the param dsn-script command in application parameter configuration mode.

To specify the VoiceXML application to which the off-ramp mail application hands off calls for off-ramp delivery status notification
                              (DSN) and message disposition notification (MDN) e-mail messages, use the call application voice dsn script command in global configuration mode. To remove the application, use the no form of this command.

call application voice mail-application-name dsn-script application-name

no call application voice mail-application-name dsn-script application-name

### Syntax Description

mail-application-name

Name of the off-ramp mail application that launches the 
                                          app_voicemail_offramp.tcl scr
                                          ipt when the gateway receives an e-mail trigger.

application-name

Name of the VoiceXML application to which the off-ramp mail application hands off the call when the destination answers.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.3(14)T

This command was replaced by the param dsn-script command in application parameter configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

When the off-ramp gateway receives a DSN or MDN e-mail message, it handles it in the same way as a voice e-mail trigger message.
                              The dial peer is selected on the basis of dialed number identification service (DNIS), and the mail application hands off
                              the call to the VoiceXML application that is configured with this command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice dsn-script Warning: This command has been deprecated. Please use the following:
			param dsn-script
```

The following example shows how to define the DSN application and how to apply it to a dial peer:

```
call application voice offramp-mapp tftp://sample/tftp-users/tcl/app_voicemail_offramp.tcl
call application voice dsn-mapp-test tftp://sample/tftp-users/vxml/dsn-mapp-test.vxml
call application voice offramp-mapp dsn-script dsn-mapp-test
!
dial-peer voice 1000 mmoip
 application offramp-mapp
 incoming called-number 555....
 information-type voice
```

### Related Commands

Command

Description

application

Defines a specific voice application in the dial peer.

call application voice

Defines the name of a voice application and specifies the location of the document (Tcl or VoiceXML) to load for the application.

param dsn-script

Specifies the VoiceXML application to which the off-ramp mail application hands off calls for off-ramp DSN and MDN e-mail
                                          messages.

show call application voice

Displays information about the configured voice applications.

## call application voice event-log

Effective with Cisco IOS Release 12.3(14)T, the call application voice event-log is obsolete. To enable event logging for a specific voice application, use one of the following commands:

param event-log (application parameter configuration mode)

paramspace appcommon event-log (service configuration mod

To enable event logging for a specific voice application, use the call application voice event-log command in global configuration mode. To reset to the default, use the no form of this command.

call application voice application-name event-log [ disable ]

no call application voice application-name event-log

### Syntax Description

application-name

Name of the voice application.

disable

(Optional) Disables event logging for the named application.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

The call application voice event-log is obsolete. To enable event logging for a specific voice application, use one of the following commands:

param event-log (application parameter configuration mode)

paramspace appcommon event-log (service configuration mode)

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command is application-specific; it takes precedence over the global configuration command, call application event-log , which enables event logging for all voice applications.

Before you can use this command, you must configure the named application on the gateway by using the call application voice command.

To prevent event logging from adversely impacting system resources for production traffic, the gateway uses a throttling mechanism.
                                          When free processor memory drops below 20 percent, the gateway automatically disables all event logging. It resumes event
                                          logging when free memory rises above 30 percent. While throttling is occurring, the gateway does not capture any new event
                                          logs even if event logging is enabled. You should monitor free memory and enable event logging only when necessary for isolating
                                          faults.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call call application voice event-log Warning: This command has been deprecated. Please use the following:
			param event-log 
				paramspace appcommon event-log
```

The following example enables event logging for all instances of the application named sample_app:

```
call application voice sample_app event-log
```

The following example enables event logging for all applications except the application sample_app:

```
call application event-log
call application voice sample_app event-log disable
```

### Related Commands

Command

Description

call application event-log

Enables event logging for voice application instances.

call application event-log max-buffer-size

Sets the maximum size of the event log buffer for each application instance.

call application voice

Defines the name of a voice application and specifies the location of the script to load for the application.

monitor call application event-log

Displays the event log for an active application instance in real-time.

param event-log

Enables or disables logging for linkable Tcl functions (packages).

paramspace appcommon event-log

Enable or disables logging for a service (application).

show call application session-level

Displays event logs and statistics for voice application instances.

## call application voice fax-dtmf

Effective with Cisco IOS Release 12.3(14)T, the call application voice fax-dtmf command is replaced by the param fax-dtmf command in application parameter configuration mode. See
                                          		  the param fax-dtmf command for more information.

To direct the fax detection interactive voice response (IVR)
                              		  application to recognize a specified digit to indicate a fax call in
                              		  default-voice and default-fax modes, use the call application voice fax-dtmf command in global configuration mode. To
                              		  remove configuration of this digit, use the no form of this command.

call application
                                 				  voice application-name fax-dtmf { 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | * | # }

no call application
                                 				  voice application-name fax-dtmf { 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | * | # }

### Syntax Description

application-name

The name of the fax detection IVR application that you
                                          						defined when you loaded the application on the router.

0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | * | #

The telephone keypad digit processedby the calling party to
                                          						indicate a fax call, in response to the audio prompt that plays during the
                                          						default-voice or default-fax mode of the fax detection IVR application.

### Command Default

2

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(5)XM

This command was introduced for the Cisco AS5300.

12.2(2)T

This command was integrated into Cisco IOS Release
                                          						12.2(2)T.

12.2(2)XB

This command was implemented on the Cisco AS5400 and Cisco
                                          						AS5350.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600
                                          						series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.2(11)T

This command was implemented on the Cisco AS5300, Cisco
                                          						AS5350, and Cisco AS5400.

12.3(14)T

This command was replaced by the param fax-dtmf command in application parameter configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the
                                          						new CLI is replaced with an explicit error message.

### Usage Guidelines

This command is useful only when the fax detection IVR application is
                              		  being configured in default-voice mode or default-fax mode as defined by the call application voice mode command.

Only one digit can be specified in this command, and that digit must
                              		  be different from the digit specified in the call application voice voice-dtmf command. You are not notified immediately if you make the error
                              		  of configuring them both to the same digit. To find this error, you must start
                              		  the debugging with the debug voip ivr script command and then observe some failing
                              		  calls.

This command is not supported by Cisco IOS help; that is, if you
                              		  type call application voice fax_detect fax-dtmf and a question mark (?) , Cisco IOS help does not supply a list of entries that are valid
                              		  in place of the question mark.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning
                              		  message is displayed to direct users to the replacement command options:

```
Router(config)# call application voice fax-dtmf Warning: This command has been deprecated. Please use the following:
			param fax-dtmf
```

The following example selects DTMF digit 1 to indicate a fax call:

```
call application voice fax_detect script_url
call application voice fax_detect fax-dtmf 1
dial-peer voice 302 pots
 application fax_detect
```

### Related Commands

Command

Description

call application voice

Loads an IVR application onto a router and gives it an
                                          						application name.

call application voice account-id-method

Configures the fax detection IVR application to use a
                                          						particular method to assign the account identifier.

call application voice mode

Configures the fax detection IVR application to operate in
                                          						one of its four modes.

call application voice prompt

Configures the fax detection IVR application to use the
                                          						specified audio file as a user prompt.

call application voice voice-dtmf

Configures the fax detection IVR application to recognize
                                          						the specified digit to indicate a voice call.

debug voip ivr script

Displays debug information from the fax detection IVR
                                          						script.

param fax-dtmf

Directs the fax detection IVR application to recognize a
                                          						specified digit to indicate a fax call in default-voice and default-fax modes.

## call application voice global-password

Effective with Cisco IOS Release 12.3(14)T, the call application voice global-password command is replaced by the param global-password command in application parameter configuration mode. See the param global-password command for more information.

To define a password to be used with CiscoSecure for Windows NT when using store-and-forward fax on a voice feature card,
                              use the call application voice global password command in global configuration mode. To restore the default value, use the no form of this command.

call application voice application-name global-password password

no call application voice application-name global-password password

### Syntax Description

application-name

The name of the application.

password

Character string used to define the CiscoSecure for Windows NT password to be used with store-and-forward fax. The maximum
                                          length is 64 alphanumeric characters.

### Command Default

No password is defined

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.3(14)T

This command is replaced by the param global-password command in application parameter configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

CiscoSecure for Windows NT might require a separate password to complete authentication, no matter what security protocol
                              you use. This command defines the password to be used with CiscoSecure for Windows NT. All records on the Windows NT server
                              use this defined password.

This command applies to on-ramp store-and-forward fax functions on Cisco AS5300 universal access server voice feature cards.
                              It is not used on modem cards.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice global-password Warning: This command has been deprecated. Please use the following:
			param global-password
```

The following example shows a password (abercrombie) being used by AAA for the app_sample_onramp9
                              Tcl 
                              application:

```
call application voice app_sample_onramp9 global-password abercrombie
```

### Related Commands

Command

Description

param global-password

Defines a password to be used with CiscoSecure for Windows NT when using store-and-forward fax on a voice feature card.

## call application voice language

Effective with Cisco IOS Release 12.3(14)T, the call application voice language is replaced by the following commands:

param language (application parameter configuration mode)

paramspace language (service configuration mode)

See these commands for more information.

To specify the language for dynamic prompts used by an interactive voice response (IVR) application (Tool Command Language
                              (Tcl) or VoiceXML), use the call application voice language command in global configuration mode. To remove this language specification from the application, use the no form of this command.

call application voice application-name language digit language

no call application voice application-name language digit language

### Syntax Description

application-name

Name of the application to which the language parameters are being passed.

digit

Number that identifies the language used by the audio files. Any number can represent any language. Enter 1 to indicate the
                                          primary language and 2 to indicate the secondary language. Range is from 0 to 9.

language

Two-character code that identifies the language of the associated audio files. Valid entries are as follows:

en --English

sp --Spanish

ch --Mandarin

aa --all

### Command Default

If this command is not configured, the default language is English.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(7)T

This command was introduced.

12.1(5)T

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB

This command was modified to support VoiceXML applications on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(4)XM

This command was implemented on the Cisco 1751.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series. Support for the Cisco
                                          AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800 and Cisco AS5850 is not included in this release.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T for VoiceXML applications. This command is supported on the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco 5800, and Cisco AS5850 in this release.

12.3(14)T

The call application voice language was replaced by the following commands:

param language (application parameter configuration mode)

paramspace language (service configuration mode)

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command identifies the number that users enter for a language; for example, "Enter 1 for English. Enter 2 for French."

This number is used only with the Tcl IVR Debit Card feature. Although it is not used by VoiceXML, you still must enter a
                              number from 0 to 9.

Instead of using this command, you can configure the language and location of the prerecorded audio files within a Tcl script
                              or VoiceXML document. For more information, see the Tcl IVR API Version 2.0 Programmer’s Guide or Cisco VoiceXML Programmer’s Guide, respectively.

To identify the location of the language audio files that are used for the dynamic prompts, use the call application voice set-location command.

Tcl scripts and VoiceXML documents can be stored in any of the following locations: On the TFTP, FTP, or HTTP servers, in
                              the flash memory of the gateway, or on the removable disks of the Cisco 3600 series. The audio files that they use can be
                              stored in any of these locations, and on RTSP servers.

With the Pre-Paid Debitcard Multi-Language feature, you can create Tcl scripts and a two-character code for any language.
                              See the Cisco Pre-Paid Debitcard Multi-Language Programmer's Reference .

With the multilanguage support for Cisco IOS IVR, you can create a Tcl language module for any language and any set of TTS
                              notations for use with Tcl and VoiceXML applications. See the Enhanced Multi-Language Support for Cisco IOS Interactive Voice
                              Response document.

The table below lists Tcl script names and the corresponding commands that are required for each Tcl script.

Tcl Script Name

Description

Commands to Configure

app_libretto_onramp9.tcl

Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS.

None

app_libretto_offramp5.tcl

Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID.

None

clid_4digits_npw_3_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI.

call application voice uid-length Range is 1 to 20. The default is 10.

call application voice pin-length Range is 0 to 10. The default is 4.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_col_npw_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_collect_cli.tcl

This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_3_cli.tcl

This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_npw_cli.tcl

This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together.

call application voice retry-count Range is 1 to 5. The default is 3.

fax_rollover_on_busy.tcl

Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy.

voice hunt user-busy

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# 
call application voice language
        Warning: This command has been deprecated. Please use the following:
			param language 
				paramspace language
```

The following example shows how to define the application "prepaid" and then selects English and Spanish as the languages
                              of the audio files that are associated with the application:

```
call application voice prepaid tftp://keyer/debitcard.tcl
call application voice prepaid language 1 en
call application voice prepaid language 2 sp
```

### Related Commands

Command

Description

call application voice

Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application.

call application voice load

Reloads the designated Tcl script.

call application voice pin-len

Defines the number of characters in the PIN for the application and passes that information to the application.

call application voice redirect-number

Specifies the telephone number to which a call is redirected for the designated application.

call application voice retry-count

Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application.

call application voice set-location

Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application.

call application voice uid-len

Defines the number of characters in the UID for the designated application and passes that information to the application.

call application voice warning-time

Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application.

param language

Configures the language parameter in a service or package on the gateway.

paramspace language

Defines the category and location of audio files that are used for dynamic prompts by an IVR application (Tcl or VoiceXML).

show call application voice

Displays information about voice applications.

## call application voice load

To reload the selected voice application script after it has been modified, use the call application voice load command in privileged EXEC mode. This command does not have a no form.

call application voice load application-name

### Syntax Description

application-name

Name of the Tcl or VoiceXML application to reload.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(7)T

This command was introduced on the Cisco 2600 series and Cisco 3600 series (except for the Cisco 3660), and on the Cisco AS5300.

12.1(3)T

Support for dynamic script loading of Media Gateway Control Protocol (MGCP) was added.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB

This command was modified to support VoiceXML applications.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1751.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750.

12.2(8)T

This command and implemented on the Cisco 7200 series.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T for VoiceXML applications. This command is supported on the Cisco
                                          AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and the Cisco  AS5850 in this release.

### Usage Guidelines

Use this command to reload an application Tcl script or VoiceXML document onto the gateway after it has been modified.

The location of the Tcl script or VoiceXML document for the specified application must have already been configured using
                              the call application voice command.

Do not include the file type extension in the filename (.vxml or .tcl) when specifying the document used by the application.

Tcl scripts and VoiceXML documents can be stored in any of the following locations: on TFTP, FTP, or HTTP servers, in the
                              flash memory of the gateway, or on the removable disks of the Cisco 3600 series. The audio files that they use can be stored
                              on any of these locations, and on RTSP servers.

Before Cisco IOS Release 12.1(3)T, the software checked the signature in a Tcl script to ensure that it was supported by Cisco.
                              A signature on Tcl scripts is no longer required. A signature has never been required for VoiceXML documents.

A Tcl script or VoiceXML document cannot be reloaded if it has active calls. Use the show call application voice command to verify that no active calls are using this application.

Tip

If the call application voice load command fails to load the Tcl script or VoiceXML document that is associated with the application, enable the debug voip ivr command and retry. This debugging command can provide information on why loading fails.

MGCP scripting is not supported on the Cisco 1750 router or on Cisco 7200 series routers.

## Examples

The following example shows the loading of a Tcl script called "clid_4digits_npw_3.tcl":

```
call application voice load clid_4digits_npw_3.tcl
```

The following example shows how to reload the VoiceXML application called " vapptest":

```
call application voice load vapptest
```

### Related Commands

Command

Description

call application cache reload time

Configures the interval for reloading MGCP scripts.

call application voice

Creates and calls the application that interacts with the IVR feature.

debug http client

Displays information about the load an application that was loaded with HTTP.

show call application voice

Displays a list of the voice applications that are configured.

## call application voice mail-script

Effective with Cisco IOS Release 12.3(14)T, the call application voice mail-script command is replaced by the param mail-script command in application parameter configuration mode. See the param mail-script command for more information.

To specify the VoiceXML application to which the off-ramp mail application hands off a call when the destination telephone
                              answers, use the call application voice mail-script command in global configuration mode. To remove the application, use the no form of this command.

call application voice mail-application-name mail-script application-name

no call application voice mail-application-name mail-script application-name

### Syntax Description

mail-application-name

Name of the off-ramp mail application that launches the 
                                          app_voicemail_offramp.tcl script
                                          when the gateway receives an e-mail trigger.

application-name

Name of the VoiceXML application to which the off-ramp mail application hands off the call when the destination answers.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.3(14)T

This command was replaced by the param mail-script command in application parameter configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

To load the mail application onto the gateway, use the call application voice command.

The off-ramp mail application must be configured in the Multimedia Mail over Internet Protocol (MMoIP) dial peer that matches
                              the telephone number contained in the header of the incoming e-mail message.

The off-ramp mail application must use the Tool Command Language (Tcl) script named 
                              "app_voicemail_offramp.tcl"
                              that is provided by Cisco. This Tcl script can be downloaded from the Cisco website by following this path: Cisco > Technical
                              Support Help - TAC > Select & Download Software > Software Center > Access Software > TclWare.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice mail-script Warning: This command has been deprecated. Please use the following:
			param mail-script
```

The following example shows that the off-ramp mail application named "offramp-mapp" hands calls to the application named "mapp-test"
                              if the telephone number in the e-mail header is seven digits beginning with 555
                              :

```
call application voice offramp-mapp tftp://sample/tftp-users/tcl/app_voicemail_offramp.tcl
call application voice mapp-test tftp://sample/tftp-users/vxml/user-test.vxml
call application voice offramp-mapp mail-script mapp-test
!
dial-peer voice 1001 mmoip
 application offramp-mapp
 incoming called-number 555....
 information-type voice
```

### Related Commands

Command

Description

application

Defines a specific voice application in the dial peer.

call application voice

Defines the name of a voice application and specifies the location of the document (Tcl or VoiceXML) to load for the application.

param mail-script

Specifies the VoiceXML application to which the off-ramp mail application hands off a call when the destination telephone
                                          answers.

show call application voice

Displays information about the configured voice applications.

## call application voice mode

Effective with Cisco IOS Release 12.3(14)T, the call application voice mode command is replaced by the param mode command in application parameter configuration mode. See the param mode command for more information.

To direct the fax detection interactive voice response (IVR) application to operate in one of its four connection modes,
                              use the call application voice mode command in global configuration mode. To return to the default connection mode, use the no form of this command.

call application voice application-name mode { connect-first | listen-first | default-voice | default-fax }

no call application voice application-name mode { connect-first | listen-first | default-voice | default-fax }

### Syntax Description

application-name

Fax detection IVR application that was defined when the application was loaded on the router.

connect first

Incoming calls are connected to the Real-Time Streaming Protocol (RTSP) server. This is the default.

listen-first

The gateway listens to the call first and then connects to the RTSP server. Any Dual tone multifrequency (DTMF) tones take
                                          the call to the voice server, but subsequent DTMF is forwarded as configured.

default voice

Incoming calls are connected as voice calls to the RTSP server.

default fax

Incoming calls are connected to the fax relay or store-and-forward fax application that is configured on the gateway.

### Command Default

connect first

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(5)XM

This command was introduced on the Cisco AS5300.

12.2(2)XB

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600
                                          series, Cisco 3725, and Cisco 3745.

12.2(11)T

This command is supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release.

12.3(14)T

This command was replaced by the param mode command in application parameter configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

The call application voice mode commands control the way that the gateway handles fax detection IVR applications calls.

When the connect-first keyword is selected and CNG (calling) tones from the originating fax machine are detected, the voice application is disconnected
                              and the call is passed to the configured fax application. If the listen-first keyword is selected, the gateway listens for CNG and, if it is detected, passes the call to the fax relay or store-and-forward
                              fax application, whichever is configured on the gateway. When the default-voice and default-fax keywords are selected, the gateway defaults to voice after listening for CNG or passes the call to the fax relay or store-and-forward
                              fax application, whichever was configured on the gateway. If the gateway hears the Dual tone multifrequency (DTMF) tones that
                              are specified in the call application voice voice-dtmf or call application voice fax-dtmf commands , the call is forwarded as appropriate.

Note that in all four connection modes, the router continues to listen for CNG throughout the call, even if the call has
                              been connected to the voice server; if CNG is detected, the call is connected to fax relay or store-and-forward fax, whichever
                              has been configured.

This command is not supported by Cisco IOS help. If you type the call application voice fax_detect mode command and a question mark (?), Cisco IOS help does not supply a list of valid entries in place of the question mark.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice mode Warning: This command has been deprecated. Please use the following:
			param mode
```

The following example shows a selection of default-voice mode for the fax detection application:

```
call application voice fax_detect script_url
call application voice fax_detect mode default-voice
dial-peer voice 302 pots
 application fax_detect
```

### Related Commands

Command

Description

call application voice

Loads a specified IVR application onto the router from the TFTP server and gives it an application name by which it is known
                                          on the router.

call application voice account-id-method

Configures the fax detection IVR application to use a particular method to assign the account identifier.

call application voice fax-dtmf

Configures the fax detection IVR application to recognize a specified digit to indicate a fax call .

call application voice prompt

Configures the fax detection IVR application to use the specified audio file as a user prompt in listen-first mode, default-voice
                                          mode, or default-fax mode.

call application voice voice-dtmf

Configures the fax detection IVR application to recognize a specified digit to indicate a voice call.

param mode

Configures the call transfer mode for a package.

## call application voice pin-len

Effective with Cisco IOS Release 12.3(14)T, the call application voice pin-len command is replaced with the param pin-len command in application parameter configuration mode. See the param pin-len command for more information.

To define the number of characters in the personal identification number (PIN) for the designated application, use the call application voice pin len command in global configuration mode. To disable the PIN for the designated application, use the no form of this command.

call application voice application-name pin-len number

no call application voice application-name pin-len number

### Syntax Description

application-name

Application name to which the PIN length parameter is being passed.

number

Number of allowable characters in PINs associated with the specified application. Range is from 0 to 10. The default is 4.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(7)T

This command was introduced.

12.1(5)T

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750.

12.2(4)XM

This command was implemented on the Cisco 1751.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series.

12.2(11)T

This command is supported on the Cisco AS5350, Cisco AS5400 Cisco AS5800, and the Cisco AS5850 in this release.

12.3(14)T

The call application voice pin-len command was replaced with the param pin-len command in application parameter configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Use this command when configuring interactive voice response (IVR)--depending on the Tool Command Language (Tcl) script being
                              used--or one of the IVR-related features (such as Debit Card) to define the number of allowable characters in a PIN for the
                              specified application and to pass that information to the specified application.

The table below lists Tcl script names and the corresponding commands that are required for each Tcl script.

Tcl Script Name

Description

Commands to Configure

app_libretto_onramp9.tcl

Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS.

None

app_libretto_offramp5.tcl

Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID.

None

clid_4digits_npw_3_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI.

call application voice uid-length Range is 1 to 20. The default is 10.

call application voice pin-length Range is 0 to 10. The default is 4

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_col_npw_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_collect_cli.tcl

This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_3_cli.tcl

This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_npw_cli.tcl

This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together.

call application voice retry-count Range is 1 to 5. The default is 3.

fax_rollover_on_busy.tcl

Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy.

voice hunt user-busy

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice pin-len Warning: This command has been deprecated. Please use the following:
			param pin-len
```

The following example shows how to define a PIN length of 4 characters for the application named "prepaid":

```
call application voice prepaid pin-len 4
```

### Related Commands

Command

Description

call application voice

Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          the application.

call application voice language

Specifies the language of the audio file for the designated application and passes that information to the application.

call application voice load

Reloads the designated Tcl script.

call application voice redirect-number

Specifies the telephone number to which a call is redirected for the designated application.

call application voice retry-count

Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application.

call application voice set-location

Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application.

call application voice uid-len

Defines the number of characters in the UID for the designated application and passes that information to the application.

call application voice warning-time

Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application.

param pin-len

Defines the number of characters in the PIN for an application.

## call application voice prompt

Effective with Cisco IOS Release 12.3(14)T, the call application voice prompt command is replaced by the param prompt command. See the param prompt command for more information.

To direct the fax detection interactive voice response (IVR) application to use the specified audio file as a user prompt,
                              use the call application voice prompt command in global configuration mode. To disable use of this audio file, use the no form of this command.

call application voice application-name prompt prompt-url

no call application voice application-name prompt prompt-url

### Syntax Description

application-name

Name of the fax detection IVR application that you defined when you loaded the application on the router.

prompt-url

URL or Cisco IOS file system location on the TFTP server for the audio file containing the prompt for the application.

### Command Default

The prompt space is empty and no prompt is played.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(5)XM

This command was introduced for the Cisco AS5300.

12.2(2)XB

This command was implemented on the Cisco AS5400 and Cisco AS5350.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600
                                          series, Cisco 3725, and Cisco 3745.

12.2(11)T

This command was implemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.3(14)T

This command was replaced by the param prompt command.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command is useful only in the listen-first, default-voice, and default-fax modes of the fax detection application.

Audio files should be a minimum of 9 seconds long so that callers do not hear silence during the initial CNG detection period.
                              Any .au file can be used; formats are described in the Cisco IOS Voice, Video, and Fax Configuration Guide, Release 12.4.

This command is not supported by Cisco IOS help. If you type the c all application voice fax_detect prompt command with a question (?), the Cisco IOS help does not supply a list of entries that are valid in place of the question
                              mark.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice prompt Warning: This command has been deprecated. Please use the following:
			param prompt
```

The following example associates the audio file" promptfile.au" with the application file "fax_detect" , and the application with the inbound POTS dial peer:

```
call application voice fax_detect script_url
call application voice fax_detect mode default-voice
call application voice fax_detect prompt promptfile.au
dial-peer voice 302 pots
 application fax_detect
```

### Related Commands

Command

Description

call application voice

Loads a specified IVR application onto the router from the TFTP server and gives it an application name by which it is known
                                          on the router.

call application voice account-id-method

Configures the fax detection IVR application to use a particular method to assign the account identifier.

call application voice fax-dtmf

Configures the fax detection IVR application to recognize a specified digit to indicate a fax call.

call application voice mode

Configures the fax detection IVR application to operate in one of its four modes.

call application voice voice-dtmf

Configures the fax detection IVR application to recognize a specified digit to indicate a voice call.

param prompt

Directs the fax detection IVR application to use the specified audio file as a user prompt.

## call application voice redirect-number

Effective with Cisco IOS Release 12.3(14)T, the call application voice redirect-number command is replaced with the param redirect-number command in application parameter configuration mode. See the the param redirect-number command for more information.

To define the telephone number to which a call is redirected--for example, the operator telephone number of the service provider--for
                              the designated application, use the call application voice redirect number command in global configuration mode. To cancel the redirect telephone number, use the no form of this command.

call application voice application-name redirect-number number

no call application voice application-name redirect-number number

### Syntax Description

application name

Name of the application to which the redirect telephone number parameter is being passed.

number

Designated operator telephone number of the service provider (or any other number designated by the customer). This is the
                                          number where calls are terminated when, for example, allowed debit time has run out or the debit amount is exceeded.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(7)T

This command was introduced on the Cisco 2600 series, the Cisco 3600 series, and the Cisco AS5300.

12.1(5)T

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1751.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series. Support for the Cisco
                                          AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release.

12.3(14)T

This command was replaced by the param redirect-number .

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Use this command when configuring interactive voice response (IVR)--depending on the Tool Command Language (Tcl) script being
                              used--or one of the IVR-related features (such as Debit Card) to define the telephone number to which a call is redirected.

The table below lists Tcl script names and the corresponding commands that are required for each Tcl script.

Tcl Script Name

Description

Commands to Configure

app_libretto_onramp9.tcl

Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS.

None

app_libretto_offramp5.tcl

Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID.

None

clid_4digits_npw_3_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI.

call application voice uid-length Range is 1 to 20. The default is 10.

call application voice pin-length Range is 0 to 10. The default is 4.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_col_npw_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_collect_cli.tcl

This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_3_cli.tcl

This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_npw_cli.tcl

This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together.

call application voice retry-count Range is 1 to 5. The default is 3.

fax_rollover_on_busy.tcl

Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy.

voice hunt user-busy

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice redirect-number Warning: This command has been deprecated. Please use the following:
			param redirect-number
```

The following example shows how to define a redirect number for the application named "prepaid":

```
call application voice prepaid redirect-number 5550111
```

### Related Commands

Command

Description

call application voice

Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application.

call application voice language

Specifies the language of the audio file for the designated application and passes that information to the application.

call application voice load

Reloads the designated Tcl script.

call application voice pin-len

Defines the number of characters in the PIN for the application and passes that information to the application.

call application voice retry-count

Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application.

call application voice set-location

Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application.

call application voice uid-len

Defines the number of characters in the UID for the designated application and passes that information to the application.

call application voice warning-time

Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application.

param redirect-number

Defines the telephone number to which a call is redirected--for example, the operator telephone number of the service provider--for
                                          an application.

## call application voice retry-count

Effective with Cisco IOS Release 12.3(14)T, the call application voice retry-count command is replaced by the param retry-count command in application parameter configuration mode. See the the param retry-count command for more information.

To define the number of times that a caller is permitted to reenter the personal identification number (PIN) for the designated
                              application, use the call application voice retry count command in global configuration mode. To cancel the retry count, use the no form of this command.

call application voice application-name retry-count number

no call application voice application-name retry-count number

### Syntax Description

application name

Name of the application to which the number of possible retries is being passed.

number

Number of times the caller is permitted to reenter PIN digits. Range is 1 to 5. The default is 3.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(7)T

This command was introduced.

12.1(5)T

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1751.

12.2(4)T

This command was introduced on the Cisco 1750.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series. Support for the Cisco
                                          AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5350, Cisco AS5400,
                                          Cisco AS5800, and Cisco AS5850 in this release.

12.3(14)T

This command was replaced by the param retry-count command.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Use this command when configuring interactive voice response (IVR)--depending on the Tool Command Language (Tcl) script being
                              used--or one of the IVR-related features (such as Debit Card) to define how many times a user can reenter a PIN.

The table below lists Tcl script names and the corresponding commands that are required for each Tcl script.

Tcl Script Name

Description

Commands to Configure

app_libretto_onramp9.tcl

Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS.

None

app_libretto_offramp5.tcl

Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID.

None

clid_4digits_npw_3_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI.

call application voice uid-length Range is 1 to 20. The default is 10.

call application voice pin-length Range is 0 to 10. The default is 4.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_col_npw_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_collect_cli.tcl

This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_3_cli.tcl

This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_npw_cli.tcl

This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together.

call application voice retry-count Range is 1 to 5. The default is 3.

fax_rollover_on_busy.tcl

Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy.

voice hunt user-busy

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application retry-count Warning: This command has been deprecated. Please use the following:
			param retry-count
```

The following example shows how to define that for the application named "prepaid" that a user can reenter a PIN three times
                              before being disconnected:

```
call application voice prepaid retry-count 3
```

### Related Commands

Command

Description

call application voice

Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application.

call application voice language

Specifies the language of the audio file for the designated application and passes that information to the application.

call application voice load

Reloads the designated Tcl script.

call application voice pin-len

Defines the number of characters in the PIN for the application and passes that information to the application.

call application voice redirect-number

Specifies the telephone number to which a call is redirected for the designated application.

call application voice set-location

Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application.

call application voice uid-len

Defines the number of characters in the UID for the designated application and passes that information to the application.

call application voice warning-time

Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application.

param retry-count

Defines the number of times that a caller is permitted to reenter the PIN for a package.

## call application voice security trusted

Effective with Cisco IOS Release 12.3(14)T, the call application voice security trusted command is replaced by the the following commands:

param security trusted (application parameter configuration mode)

paramspace appcommon security trusted (service configuration mode)

See these commands for more information.

To set the security level of a VoiceXML application to "trusted" so that automatic number identification (ANI) is not blocked,
                              use the call application voice security trusted command in global configuration mode. To restore the default condition, use the no form of this command.

call application voice application-name security trusted

no call application voice application-name security trusted

### Syntax Description

application name

Name of the application being configured as trusted.

### Command Default

The security level of the application is not set to trusted, and ANI is blocked.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(2)XB

This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco 3640 and Cisco 3660.

12.3(14)T

The call application voice security trusted command was replaced by the following commands:

param security trusted (application parameter configuration mode)

paramspace appcommon security trusted (service configuration mode)

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command is applicable only for VoiceXML applications.

Tool Command Language (Tcl) applications provide the security parameter to the application but do not use it.

If an application is configured as a trusted application, it is trusted not to provide the calling number to the destination
                              party, so ANI is always provided if available.

Normally, the voice gateway does not provide the calling number (ANI) to a VoiceXML application if the caller ID is blocked.
                              Caller ID is blocked if a call that comes into the voice gateway has the presentation indication field set to "presentation
                              restricted". The session.telephone.ani variable is set to "blocked". When the call application voice security trusted command is configured, the gateway does not block caller ID; it provides the calling number to the VoiceXML application.

If the keyword of this command is set to anything other than trusted , the value is accepted and the application is treated as not trusted. For example, in the following configuration, the application
                              "sample" is treated as not trusted, and caller ID is blocked:

```
call application voice sample security not_trusted
```

To enable Generic Transparency Descriptor (GTD) parameters in call signaling messages to map to VoiceXML and Tcl session
                              variables, configure the call application voice security trusted command. If this command is not configured, the VoiceXML variables that correspond to GTD parameters are marked as not available.
                              For a detailed description of the VoiceXML and Tcl session variables, see the Cisco VoiceXML Programmer’s Guide and the Tcl IVR API Version 2.0 Programmer’s Guide , respectively.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice security trusted Warning: This command has been deprecated. Please use the following:
			param security trusted (application parameter configuration mode)
				paramspace appcommon security trusted
```

The following example configures the application "sample" as a trusted application. Caller ID is available to this VoiceXML
                              application if it is supported by the service provider.

```
call application voice sample flash:sample.vxml
call application voice sample security trusted
```

The following example configures the application "example" as not trusted. Caller ID can be blocked.

```
call application voice coldcall tftp://joeserver/sellcars.vxml
no call application voice example security trusted
```

### Related Commands

Command

Description

call application voice

Defines the name of a voice application and specifies the location of the document (Tcl or VoiceXML) to load for the application.

call application voice language

Defines the language of the audio files used for dynamic prompts by the designated application.

call application voice load

Reloads a Tcl or VoiceXML document.

call application voice pin-len

Defines the number of characters in the PIN for the Tcl application.

call application voice redirect-number

Defines the telephone number to which a call is redirected for the designated application.

call application voice retry-count

Defines the number of times that a caller is permitted to reenter the PIN for a designated application.

call application voice uid-len

Defines the number of characters in the UID for the designated application.

call application voice warning-time

Defines the number of seconds for which a warning prompt is played before a user’s account time runs out.

param security

Configures security for linkable Tcl functions (packages).

paramspace appcommon security

Configures security for a service (application).

show call application voice

Displays the following information associated with a voice application: the audio files, the prompts, the caller interaction,
                                          and the abort key operation.

## call application voice set-location

Effective with Cisco IOS Release 12.3(14)T, the call application voice set-location command is replaced by the paramspace language command. See the paramspace language command for more information.

To define the category and location of audio files that are used for dynamic prompts by the specified IVR application (Tcl
                              or VoiceXML), use the call application voice set location command in global configuration mode. To remove these definitions, use the no form of this command.

call application voice application-name set-location language category location

no call application voice application-name set-location language category location

### Syntax Description

application name

Name of the application to which the set location parameters are being passed.

language

Two-character code that identifies the language associated with the audio files. Valid entries are as follows:

en --English

sp --Spanish

ch --Mandarin

aa --All

This is the same language code that was entered when configuring the call application voice language command .

category

Category group of the audio files (from 0 to 4). For example, audio files representing the days and months can be category
                                          1, audio files representing units of currency can be category 2, and audio files representing units of time--seconds, minutes,
                                          and hours--can be category 3. Range is from 0 to 4; 0 means all categories.

location

URL of the audio files. Valid URLs refer to TFTP, FTP, HTTP, or RTSP servers, flash memory, or the removable disks on the
                                          Cisco 3600 series.

### Command Default

No location or category is set.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(7)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco AS5300.

12.1(5)T

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB

This command was modified to support VoiceXML applications on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1751.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T for VoiceXML applications. This command is supported on the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release.

12.3(14)T

This command was replaced by the paramspace language command.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Instead of using this command, you can configure the language and location of prerecorded audio files within a Tcl script
                              or VoiceXML document. For more information, see the Tcl IVR API Version 2.0 Programmer’s Guide or Cisco VoiceXML Programmer’s Guide, respectively.

To identify the language of the audio files, use the call application voice language command.

Tcl scripts and VoiceXML documents can be stored in any of the following locations: On TFTP, FTP, or HTTP servers, in the
                              flash memory on the gateway, or on the removable disks of the Cisco 3600 series. The audio files that they use can be stored
                              in any of these locations, and on RTSP servers.

You can configure multiple set-location lines for a single application.

With the Pre-Paid Debitcard Multi-Language feature, you can create Tcl scripts and a two-character code for any language.
                              See the Cisco Pre-Paid Debitcard Multi-Language Programmer's Reference .

With the multilanguage support for Cisco IOS IVR, you can create a Tcl language module for any language and any set of Text-to-Speech
                              (TTS) notations for use with Tcl and VoiceXML applications. See the Enhanced Multi-Language Support for Cisco IOS Interactive
                              Voice Response document.

The table below lists Tcl script names and the corresponding commands that are required for each Tcl script.

Tcl Script Name

Description

Commands to Configure

app_libretto_onramp9.tcl

Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS.

None

app_libretto_offramp5.tcl

Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID.

None

clid_4digits_npw_3_cli.tcl

Authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for the account
                                          number and password, respectively, are configurable through the command-line interface (CLI). If the authentication fails,
                                          the script allows the caller to retry. The retry number is also configured through the CLI.

call application voice uid-length Range is 1 to 20. The default is 10.

call application voice pin-length Range is 0 to 10. The default is 4.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_col_npw_cli.tcl

Authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_collect_cli.tcl

Authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the caller to
                                          retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_3_cli.tcl

Authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_npw_cli.tcl

Authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller to retry.
                                          The retry number is configured through the CLI. The account number and PIN are collected together.

call application voice retry-count Range is 1 to 5. The default is 3.

fax_rollover_on_busy.tcl

Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy.

voice hunt user-busy

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice set-location Warning: This command has been deprecated. Please use the following:
			paramspace language
```

The following example shows how to configure the call application voice set-location command for the application named "prepaid." In this example, the language specified is English, the category into which
                              the audio files are grouped is category 0 (meaning all), and the location is the keyer directory on the TFTP server.

```
call application voice prepaid set-location en 0 tftp://keyer/
```

The following example shows how to configure the call application voice set-location command for a fictitious VoiceXML application named "sample." In this example, as in the preceding example, the language
                              defined is English, the category into which the audio files are grouped is category 0 (meaning "all") and the location is
                              the example directory on an HTTP server.

```
call application voice sample set-location en 0 http://example/
```

The following example shows how to configure the call application voice set-location command for multiple set locations:

```
call application voice sample set-location en 0 http://example/en_msg/
call application voice sample set-location sp 0 http://example/sp_msg/
call application voice sample set-location ch 0 http://example/ch_msg/
```

### Related Commands

Command

Description

call application voice

Specifies the application name and indicates the location of the IVR script to be used with this application.

call application voice language

Specifies the audio file language for the designated application.

call application voice load

Reloads the designated Tcl script.

call application voice pin-len

Specifies the number of characters in the PIN.

call application voice redirect-number

Specifies the telephone number to which a call is redirected.

call application voice retry-count

Defines the number of times a caller is permitted to reenter the PIN.

call application voice uid-len

Defines the number of characters in the UID for the designated application.

call application voice warning-time

Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application.

paramspace language

Defines the category and location of audio files that are used for dynamic prompts by an IVR application (Tcl or VoiceXML).

show call application voice

Displays information about voice applications.

## call application voice transfer mode

Effective with Cisco IOS Release 12.3(14)T, the call application voice transfer mode command is replaced by the following commands:

param mode (application parameter configuration mode)

paramspace callsetup mode (service configuration mode)

See these commands for more information.

To specify the call-transfer method for Tool Command Language (Tcl) or VoiceXML applications, use the call application voice transfer mode command in global configuration mode. To reset to the default, use the no form of this command.

call application voice application-name transfer mode { redirect | redirect-at-alert | redirect-at-connect | redirect-rotary | rotary }

no call application voice application-name transfer mode

### Syntax Description

application-name

Name of the voice application for which the transfer method is set.

redirect

Gateway redirects the call leg to the redirected destination number.

redirect-at-alert

Gateway places a new call to the redirected destination number and initiates a call transfer when the outgoing call leg is
                                          in the alert state. If the call transfer is successful, the two call legs are disconnected on the gateway. If the transfer
                                          fails, the gateway bridges the two call legs. Provides support for Two B-Channel Transfer (TBCT).

redirect-at-connect

Gateway places a new call to the redirected destination number and initiates a call transfer when the outgoing call leg is
                                          in the connect state. If the call transfer is successful, the two call legs are disconnected on the gateway. If the transfer
                                          fails, the gateway bridges the two call legs. Provides support for TBCT.

redirect-rotary

Gateway redirects the call leg to the redirected destination number. If redirection fails, the gateway places a rotary call
                                          to the redirected destination number and hairpins the two call legs. For TBCT, this mode is the same as for the redirect-at-connect keyword.

rotary

Gateway places a rotary call for the outgoing call leg and hairpins the two call legs. Call redirection is not invoked. This
                                          is the default.

### Command Default

Rotary method; call redirection is not invoked.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(1)

This command was introduced.

12.3(14)T

This command was replaced by the following commands:

param mode (application parameter configuration mode)

paramspace callsetup mode (service configuration mode)

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command determines whether a voice application can invoke TBCT or RTPvt. Before you can use this command, you must configure
                              the named application on the gateway by using the call application voice command.

Redirect-rotary is the preferred transfer method because it ensures that a call-redirect method is always selected if the
                              call leg is capable of it.

Tcl scripts can read the value of this command by using the info tag get cfg_avpair transfer-mode statement. For detailed
                              information, see the Tcl IVR API Version 2.0 Programmer’s Guide .

For VoiceXML applications, the value of this command becomes the default behavior if the com.cisco.transfer.mode property
                              is not specified in the VoiceXML document. For detailed information, see the Cisco VoiceXML Programmer's Guide. The VoiceXML
                              document property takes precedence over the gateway configuration.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice transfer mode Warning: This command has been deprecated. Please use the following:
		param mode
			paramspace callsetup mode
```

The following example sets the transfer method to redirect for the application callme:

```
Router(config)# call application voice callme transfer mode redirect
```

### Related Commands

Command

Description

application

Enables a voice application on a dial peer.

call application voice

Defines the name of a voice application and specifies the location of the Tcl or VoiceXML document to load for this application.

call application voice transfer reroute-mode

Specifies the call-forwarding behavior of a Tcl application.

debug voip ivr callsetup redirect

Displays debugging information about H.450 calls that are redirected during setup.

debug voip ivr redirect

Displays debugging information about redirected H.450 calls.

isdn supp-service tbct

Enables ISDN TBCT on PRI trunks.

param mode

Configures the call transfer mode for a package.

paramspace callsetup mode

Configures the call transfer mode for an application.

show call active voice redirect

Displays information about active calls that are being redirected using RTPvt or TBCT.

show call application voice

Displays information about voice applications.

show call history voice redirect

Displays history information about calls that were redirected using RTPvt or TBCT.

## call application voice transfer reroute-mode

Effective with Cisco IOS Release 12.3(14)T, the call application voice transfer reroute-mode command is replaced by the following commands:

param reroutemode (application parameter configuration mode)

paramspace callsetup reroutemode (service configuration mode)

See these commands for more information.

To specify the call-forwarding behavior of a Tool Command Language (Tcl) application, use the call application voice transfer reroute-mode command in global configuration mode. To reset to the default, use the no form of this command.

call application voice application-name transfer reroute-mode { none | redirect | redirect-rotary | rotary }

no call application voice application-name transfer reroute-mode

### Syntax Description

application-name

Name of the voice application for which the transfer reroute method is set.

none

Call forwarding is not performed by the voice application.

redirect

Two call legs are directly connected. Provides support for RTPvt.

redirect-rotary

Two call legs are directly connected (redirect). If that fails, the two call legs are hairpinned on the gateway (rotary).

rotary

Gateway places a rotary call for the outgoing call leg and hairpins the two calls together. RTPvt is not invoked. This is
                                          the default.

### Command Default

Rotary method; RTPvt is not invoked.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(1)

This command was introduced.

12.3(14)T

This command was replaced by the following commands:

param reroutemode (application parameter configuration mode)

paramspace callsetup reroutemode (service configuration mode)

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Before you can use this command, you must configure the named application on the gateway by using the call application voice command. This command is not supported for VoiceXML applications or for TBCT.

Redirect-rotary is the preferred transfer method because it ensures that a call-redirect method is always selected, provided
                              that the call leg is capable of it.

Tcl scripts can read the value of this command by using the info tag get cfg_avpair reroute-mode statement. For detailed information,
                              see the Tcl IVR API Version 2.0 Programmer’s Guide .

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice transfer reroute-mode Warning: This command has been deprecated. Please use the following:
		param reroutemode (application parameter configuration mode)
			paramspace callsetup reroutemode
```

The following example sets the call forwarding method to redirect for the application callme:

```
Router(config)# call application voice callme transfer reroute-mode redirect
```

### Related Commands

Command

Description

application

Enables a voice application on a dial peer.

call application voice

Defines the name of a voice application and specifies the location of the Tcl or VoiceXML document to load for this application.

call application voice transfer mode

Specifies the call-transfer behavior of a Tcl or VoiceXML application.

isdn supp-service tbct

Enables ISDN TBCT on PRI trunks.

param reroutemode

Configures the call transfer reroutemode (call forwarding) for a package.

paramspace callsetup reroutemode

Configures the call reroute mode (call forwarding) for an application.

show call active voice redirect

Displays information about active calls that are being redirected using RTPvt or TBCT.

show call application voice

Displays information about voice applications.

show call history voice redirect

Displays history information about calls that were redirected using RTPvt or TBCT.

## call application voice uid-length

Effective with Cisco IOS Release 12.3(14)T, the call application voice uid-length command is replaced by the param uid-len command. See the param uid-len command for more information.

To define the number of characters in the user identification (UID) number for the designated application and to pass that
                              information to the specified application, use the call application voice uid-length command in global configuration mode. To restore the default setting for this command, use the no form of this command.

call application voice application-name uid-length number

no call application voice application-name uid-length number

### Syntax Description

application-name

Name of the application to which the UID length parameter is passed.

number

Number of allowable characters in UIDs that are associated with the specified application. Range is from 1 to 20. The default
                                          is 10.

### Command Default

number

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(7)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco AS5300.

12.1(5)T

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1751. This release does not support any other Cisco platforms.

12.2(4)T

Support was added for the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 7200 series.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release.

12.3(14)T

This command was replaced by the param uid-len command.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Use this command when configuring interactive voice response (IVR)--depending on the Tool Command Language (Tcl) script being
                              used--or one of the IVR-related features (such as Debit Card) to define the number of allowable characters in a UID for the
                              specified application and to pass that information to the specified application.

The table below lists Tcl script names and the corresponding commands that are required for each Tcl script.

Tcl Script Name

Description

Commands to Configure

app_libretto_onramp9.tcl

Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS.

None

app_libretto_offramp5.tcl

Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID.

None

clid_4digits_npw_3_cli.tcl

Authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for the account
                                          number and password, respectively, are configurable through the command-line interface (CLI). If the authentication fails,
                                          the script allows the caller to retry. The retry number is also configured through the CLI.

call application voice uid-length Range is 1 to 20. The default is 10.

call application voice pin-length Range is 0 to 10. The default is 4.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_col_npw_cli.tcl

Authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_collect_cli.tcl

Authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the caller to
                                          retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_3_cli.tcl

Authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_npw_cli.tcl

Authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller to retry.
                                          The retry number is configured through the CLI. The account number and PIN are collected together.

call application voice retry-count Range is 1 to 5. The default is 3.

fax_rollover_on_busy.tcl

Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy.

voice hunt user-busy

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice uid-length Warning: This command has been deprecated. Please use the following:
		param uid-len
```

The following example shows how to configure four allowable characters in the UID for the application named "sample":

```
Router(config)# all application voice sample uid-length 4
```

### Related Commands

Command

Description

call application voice

Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application.

call application voice language

Specifies the language of the audio file for the designated application and passes that information to the application.

call application voice load

Reloads the designated Tcl script.

call application voice pin-len

Defines the number of characters in the PIN for the application and passes that information to the application.

call application voice redirect-number

Specifies the telephone number to which a call is redirected for the designated application.

call application voice retry-count

Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application.

call application voice set-location

Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application.

call application voice warning-time

Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application.

param uid-length

Defines the number of characters in the UID for a package.

## call application voice voice-dtmf

Effective with Cisco IOS Release 12.3(14)T, the call application voice voice-dtmf command is replaced by the param voice-dtmf command. See the param voice-dtmf command for more information.

To direct the fax detection interactive voice response (IVR) application to recognize a specified digit to indicate a voice
                              call, use the call application voice voice-dtmf command in global configuration mode. To remove configuration of this digit, use the no form of this command.

call application voice application-name voice-dtmf keypad-character

no call application voice application-name voice-dtmf keypad-character

### Syntax Description

application-name

The name of the fax detection application that you defined when you loaded the application on the router.

keypad-character

Single character that can be dialed on a telephone keypad pressed by the calling party to indicate a voice call, in response
                                          to the audio prompt configured in default-voice and default-fax mode of the fax detection IVR application. Default is 1.

### Command Default

1

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(5)XM

This command was introduced for the Cisco AS5300.

12.2(2)XB

This command was implemented on the Cisco AS5400 and Cisco AS5350.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600
                                          series, Cisco 3725, and Cisco 3745. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not included in this release.

12.2(11)T

This command was supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release.

12.3(14)T

This command was replaced by the param voice-dtmf command.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command is useful only when the fax detection IVR application is being configured in default-voice mode or default-fax
                              mode, as defined by the call application voice mode command. Only one digit can be specified in this command, and that digit must be different from the digit specified in the call application voice fax-dtmf command . You are not notified immediately if you make the error of configuring them both to the same digit. To find this error, you
                              must start debugging with the debug voip ivr script command and then observe some failing calls.

This command is not supported by Cisco IOS help. If you type the call application voice fax_detect voice-dtmf command and a question mark ( ? ), the Cisco IOS help does not supply a list of entries that are valid in place of the question mark.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice voice-dtmf Warning: This command has been deprecated. Please use the following:
		param voice-dtmf
```

The following example selects digit 2 dual tone multifrequency (DTMF) to indicate a voice call:

```
call application voice fax_detect script_url
call application voice fax_detect voice-dtmf 2
dial-peer voice 302 pots
 application fax_detect
```

### Related Commands

Command

Description

call application voice

Loads a specified IVR application onto the router from the TFTP server and gives it an application name by which it is known
                                          on the router.

call application voice account-id-method

Configures the fax detection IVR application to use a particular method to assign the account identifier.

call application voice fax-dtmf

Configures the fax detection IVR application to recognize a specified digit to indicate a fax call.

call application voice mode

Configures the fax detection IVR application to operate in one of its four modes.

call application voice prompt

Configures the fax detection IVR application to use the specified audio file as a user prompt.

param voice-dtmf

Directs the fax detection IVR application to recognize a specified digit to indicate a voice call.

## call application voice warning-time

Effective with Cisco IOS Release 12.3(14)T, the call application voice warning-time command is replaced by the param warning-time command. See the param warning-time command for more information.

To define the number of seconds of warning that a user receives before the allowed calling time expires use the call application voice warning-time command in global configuration mode. To remove the configured warning period, use the no form of this command.

call application voice application-name warning-time seconds

no call application voice application-name warning-time seconds

### Syntax Description

application-name

Name of the application to which the warning time parameter is being passed.

seconds

Length of the warning period, in seconds, before the allowed calling time expires. Range is from 10 to 600. This argument
                                          has no default value.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(7)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco AS5300.

12.1(5)T

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1751. Support for other Cisco platforms is not included in this release.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 7200 series.

12.2(11)T

This command was implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release.

12.3(14)T

This command was replaced by the param warning-time command.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Use this command when configuring interactive voice response (IVR)--depending on the Tool Command Language (Tcl) script being
                              used--or one of the IVR-related features (such as Debit Card) to define the number of seconds in the warning period before
                              the allowed calling time expires for the specified application and to pass that information to the specified application.

The table below lists Tcl script names and the corresponding commands that are required for each Tcl script.

Tcl Script Name

Description

Commands to Configure

app_libretto_onramp9.tcl

Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS.

None

app_libretto_offramp5.tcl

Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID.

None

clid_4digits_npw_3_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI.

call application voice uid-length Range is 1 to 20. The default is 10.

call application voice pin-length Range is 0 to 10. The default is 4.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_col_npw_cli.tcl

This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_authen_collect_cli.tcl

This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_3_cli.tcl

This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI.

call application voice retry-count Range is 1 to 5. The default is 3.

clid_col_npw_npw_cli.tcl

This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together.

call application voice retry-count Range is 1 to 5. The default is 3.

fax_rollover_on_busy.tcl

Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy.

voice hunt user-busy

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application voice param warning-time Warning: This command has been deprecated. Please use the following:
		param warning-time
```

The following example shows how to configure a 30-second warning time for the application named "sample":

```
Router(config)# call application voice sample warning-time 30
```

### Related Commands

Command

Description

call application voice language

Specifies the language of the audio file for the designated application and passes that information to the application.

call application voice load

Reloads the designated Tcl script.

call application voice location

Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application.

call application voice pin-len

Defines the number of characters in the PIN for the application and passes that information to the application.

call application voice redirect-number

Specifies the telephone number to which a call is redirected for the designated application.

call application voice retry-count

Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application.

call application voice set-location

Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application.

call application voice uid-length

Defines the number of characters in the UID for the designated application and passes that information to the application.

param warning-time

Defines the number of seconds of warning that a user receives before the allowed calling time expires.

## call-block (dial peer)

To enable blocking of incoming calls, use the call-block command in dial peer configuration mode. To return to the default value, use the no form of this command.

call-block { disconnect-cause incoming { call-reject | invalid-number | unassigned-number | user-busy } | translation-profile incoming name }

no call-block { disconnect-cause incoming { call-reject | invalid-number | unassigned-number | user-busy } | translation-profile incoming name }

### Syntax Description

disconnect-cause incoming

Associates a disconnect cause of incoming calls.

call-reject

Specifies call rejection as the cause for blocking a call during incoming call-number translation.

invalid-number

Specifies invalid number as the cause for blocking a call during incoming call-number translation.

unassigned-number

Specifies unassigned number as the cause for blocking a call during incoming call-number translation.

user-busy

Specifies busy as the cause for blocking a call during incoming call-number translation.

translation-profile incoming

Associates the translation profile for incoming calls.

name

Name of the translation profile.

### Command Default

Disconnect cause: No Service (once the call-blocking translation profile is defined)
                              Translation profile: No default behavior or values

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

An incoming call can be blocked from the gateway if one of the call numbers (calling, called, or redirect) is matched with
                              the reject translation rule of the incoming call-blocking translation profile.

The cause value is returned to the source of the call when a call is blocked during the incoming call-number translation.

This command is supported in POTS, VoIP, VoFR, and VoATM dial-peer configuration. For VoATM, only ATM Adaptation Layer 5 (AAL5)
                              calls are supported.

The only option for call blocking is in the incoming direction. From the perspective of the voice gateway, the incoming direction
                              can be either of the following:

Incoming from a telephony device directly attached to a voice port on the gateway toward the gateway itself

Incoming by way of an inbound Voice over X (VoX) call from a peer gateway

To configure incoming call blocking, define a translation rule with a reject keyword. For example:

```
voice translation-rule 1
 rule 1 reject /408252*/
```

Apply the rule to a translation profile for called, calling, or redirect-called numbers, such as:

```
voice translation profile call_block_profile
 translate calling 1
```

Include the translation profile within a dial peer definition. For example:

```
dial-peer voice 111 pots
 call-block translation-profile incoming call_block_profile
 call-block disconnect-cause incoming invalid_number
```

In this example, the gateway blocks any incoming time-division multiplexing (TDM) call that successfully matches inbound dial-peer
                              111 and has a calling number that starts with 408252. The gateway also returns the disconnect cause "invalid number" to the
                              source of the call. (Other disconnect causes can be assigned: unassigned-number, user-busy, or call-rejected.)

## Examples

The following example assigns the translation profile "example" to be used for incoming calls and returns the message "invalid
                              number" as a cause for blocked calls:

```
Router(config)# dial-peer voice 5 pots Router(config-dial-peer)# call-block translation-profile incoming example Router(config-dial-peer)# call-block disconnect-cause incoming invalid-number
```

Following are two possible call-blocking scenarios:

## Examples

We place the rejection profile on a POTS dial peer that is associated with the voice port on which we expect the inbound call.
                              When the inbound call attempt is made, we see in the CCAPI debugs that POTS dial-peer 9 is matched for the telephony call
                              leg. The call-block rule is checked and we send back user-busy to the switch.

```
voice translation-rule 1
 rule 1 reject /9193927582/   <<<<-------- filter out calls from this CallerID
voice translation-profile reject_ANI
 translate calling 1
dial-peer voice 9 pots
 destination-pattern 9T
 direct-inward-dial
 port 1/0:23
 call-block translation-profile incoming reject_ANI
 call-block disconnect-cause incoming user-busy
```

## Examples

We place the rejection profile on a VoIP/VoATM/VoFR dial peer that matches an inbound VoX call attempt. When the inbound call
                              attempt is made, we see in the CCAPI debugs that VoIP dial-peer 7 is matched for the IP call leg. The call-block rule is checked
                              and we send back user-busy to the switch.

```
voice translation-rule 1
 rule 1 reject /9193927582/   <<<<-------- filter out calls from this CallerID
voice translation-profile reject_ANI
 translate calling 1
dial-peer voice 7 voip
 destination-pattern 7T
 session target ipv4:A.B.C.D
 incoming called-number .   <<<<-------- force inbound IP call-leg match
 call-block translation-profile incoming reject_ANI
 call-block disconnect-cause incoming user-busy
```

### Related Commands

Command

Description

dial-peer voice

Initiates the dial-peer voice configuration mode.

voice translation-profile

Defines a translation profile for voice calls.

voice translation-rule

Defines a translation rule for voice calls.

## call-denial

The call
                              -
                              denial command is replaced by the call threshold global command. See the call threshold global command for more information.

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice command is replaced by the commands shown in the table below. See these commands for more information. |
|---|---|

| application-name | Character string that defines the name of the voice application. |
|---|---|
| location | Location of the Tcl script or VoiceXML document in URL format. Valid storage locations are TFTP, FTP, HTTP, and flash memory. |
| av-pair | Text string that defines attribute-value (AV) pairs specified by the Tcl script and understood by the RADIUS server. Multiple
                                          AV pairs can be enclosed in quotes; up to 512 entries are supported. |

| Release | Modification |
|---|---|
| 12.0(4)XH | This command was introduced. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. The location argument was added. |
| 12.1(3)T | The av-pair argument was added for AV pairs. |
| 12.1(5)T | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB | This command was modified to support VoiceXML applications and HTTP server locations on the Cisco AS5300, Cisco AS5350, and
                                          Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750. |
| 12.2(4)XM | This command was implemented on the Cisco 1751. Support for other Cisco platforms is not included in this release. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 2600 series, Cisco 3600 series,
                                          Cisco 3725, Cisco 3745, and Cisco 7200 series. |
| 12.2(11)T | This command was implemented for VoiceXML applications. This command is supported on the Cisco AS5300, Cisco AS5350, Cisco
                                          AS5400, Cisco AS5800, and Cisco AS5850 in this release. |
| 12.2(15)T | MCID AV-pairs were added for the av-pair argument; they are mcid-dtmf, mcid-release-timer, and mcid-retry-limit. |
| 12.3(8)T | Support was added to allow up to 512 multiple AV pairs (enclosed in quotes) to be used in a single command. |
| 12.3(14)T | This command was replaced. The call application voice command was replaced by the commands shown in the table below. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Command Mode | Purpose |
|---|---|---|
| application | Global configuration | Enters application configuration mode to configure voice applications and services. |
| service | Application configuration | Enters service configuration mode to configure a standalone application, such as a debit card script. |
| package | Application configuration | Use to load and configure a package. A package is a linkable set of C or Tcl functions that provide functionality invoked
                                          by applications or other packages. |
| param | Application parameter configuration | Use to configure parameters for services or packages. |

| Note | The no call application voice command causes all related call application commands--for instance, call application voice language and call application voice set-location --to be deleted. The no call application voice application-name command removes the entire application and all parameters, if configured. |
|---|---|

| Command | Description |
|---|---|
| application (dial peer) | Defines the call application in the dial peer. |
| application (global configuation) | Enters application configuration mode to configure applications. |
| call application voice language | Defines the language of the audio file for the designated application and passes that information to the application. |
| call application voice load | Reloads the designated Tcl script or VoiceXML document. |
| call application voice pin-len | Defines the number of characters in the PIN for the application and passes that information to the application. |
| call application voice redirect-number | Defines the telephone number to which a call is redirected for the designated application. |
| call application voice retry-count | Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application. |
| call application voice security trusted | Sets the security level of a VoiceXML application to trusted so that ANI is not blocked. |
| call application voice set-location | Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application. |
| call application voice uid-len | Defines the number of characters in the UID for the designated application and passes that information to the application. |
| call application voice warning-time | Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application. |
| package | Enters application parameter configuration mode to load and configure a package. |
| param | Loads and configures parameters in a package or a service (application) on the gateway. |
| service | Loads and configures a specific, standalone application on a dial peer. |
| show call application voice | Displays information about voice applications. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice access-method command was replaced by the param access-method command in application parameter configuration mode. See the param access-method command for more information. |
|---|---|

| application-name | Name of the application. |
|---|---|
| prompt-user | Specifies that no DID is set in the incoming POTS dial peer and that a Tcl script in the incoming POTS dial peer is used for
                                          two-stage dialing. |
| redialer | Specifies that no DID is set in the incoming POTS dial peer and that the redialer device are used for two-stage dialing. |

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into the Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was introduced on the Cisco 1750. |
| 12.3(14)T | This command was replaced by the param access-method command in application parameter configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application voice | Loads a specified application onto the router from the TFTP server and gives it an application name by which it is known on
                                          the router. |
| call application voice language | Defines the language of the audio file for the designated application and passes that information to the application. |
| call application voice load | Reloads the designated Tcl script. |
| call application voice pin len | Defines the number of characters in the PIN for the application and passes that information to the application. |
| call application voice redirect number | Defines the telephone number to which a call is redirected--for example, the operator telephone number of the service provider--for
                                          the designated application. |
| call application voice retry count | Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application. |
| call application voice set location | Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application. |
| call application voice uid len | Defines the number of characters in the UID for the designated application and passes that information to the application. |
| call application voice warning time | Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application. |
| param access-method | Specifies the access method for two-stage dialing for the designated application. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice account-id-method command is replaced by the param account-id-method command in application parameter configuration mode. See the param account-id-method command for more information. |
|---|---|

| application-name | Name of the defined fax detection IVR application. |
|---|---|
| none | Account identifier is blank. This is the default. |
| ani | Account identifier is the calling party telephone number (automatic number identification, or ANI). |
| dnis | Account identifier is the dialed party telephone number (dialed number identification service, or DNIS). |
| gateway | Account identifier is a router-specific name derived from the hostname and domain name, displayed in the following format:
                                          router-name.domain-name. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced for the Cisco AS5300. |
| 12.2(2)XB | This command was implemented on the Cisco AS5400 and Cisco AS5350. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600
                                          series, Cisco 3725, and Cisco 3745. |
| 12.2(11)T | This command was implemented on the Cisco AS5300, the Cisco AS5350, and Cisco AS5400. |
| 12.3(14)T | This command was replaced by the param account-id-method command in application parameter configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application voice | Loads a specified IVR application onto the router from the TFTP server and gives it an application name by which it is known
                                          on the router. |
| call application voice fax dtmf | Configures the fax detection IVR application to recognize a specified digit that indicates a fax call in default-voice and
                                          default-fax modes. |
| call application voice mode | Configures the fax detection IVR application to operate in one of its four modes. |
| call application voice prompt | Configures the fax detection IVR application to use the specified audio file as a user prompt in listen-first mode, default-voice
                                          mode, or default-fax mode. |
| call application voice voice dtmf | Configures the fax detection IVR application to recognize a specified digit that indicate a voice call in default-voice and
                                          default-fax modes. |
| param account-id-method | Configures an application to use a particular method to assign the account identifier. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice authentication enable command is replaced by the param authentication enable command in application configuration mode. See the param authentication enable command for more information. |
|---|---|

| application-name | Name of the application. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.3(14)T | This command was replaced by the param authentication enable command in application configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| aaa authentication | Enables AAA accounting of requested services when you use RADIUS or TACACS+. |
| call application voice authen-list | Specifies the name of an authentication method list for a TCL application. |
| call application voice authen-method | Specifies the authentication method for a TCL application. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice accounting-list command is replaced by the param accounting-list in application configuration mode. See the param accounting-list command for more information. |
|---|---|

| application-name | Name of the application. |
|---|---|
| method-list-name | Character string used to name a list of accounting methods to be used with store-and-forward fax. |

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745. |
| 12.3(14)T | This command was replaced by the param accounting-list in application configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| aaa accounting | Enables AAA accounting of requested services when you use RADIUS or TACACS+. |
| call application voice accounting enable | Enables AAA accounting for a TCL application. |
| mmoip aaa receive-accounting enable | Enables on-ramp AAA accounting services. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice accounting-template command is obsolete. Use the call accounting-template command in application configuration mode to configure a voice accounting template. |
|---|---|

| application-name | Defines the name of the T.37 voice application. Use the call application voice command to define the name of a voice application and specify the location of the Tool Command Language (Tcl) or VoiceXML
                                                document to load for this application. |
|---|---|
| template - name | Defines the name of the template. Use the call accounting-template voice command to define the template name. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |
| 12.3(14)T | This command is obsolete. Use the call accounting-template command in application configuration mode to configure a voice accounting template. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Note | This command applies only to T.37 fax. |
|---|---|

| Command | Description |
|---|---|
| application | Defines the call application in the dial peer. |
| call accounting-template | Selects an accounting template at a specific location. |
| call accounting-template voice | Selects an accounting template at a specific location. |
| call application voice | Defines the name of a voice application and specifies the location of the Tcl or VoiceXML document to load for this application. |
| call application voice language | Defines the language of the audio file for the designated application and passes that information to the application. |
| call application voice load | Reloads the designated Tcl script or VoiceXML document. |
| call application voice pin-len | Defines the number of characters in the PIN for the application and passes that information to the application. |
| call application voice redirect-number | Defines the telephone number to which a call is redirected for the designated application. |
| call application voice retry-count | Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application. |
| call application voice security trusted | Sets the security level of a VoiceXML application to trusted so that ANI is not blocked. |
| call application voice set-location | Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application. |
| call application voice uid-len | Defines the number of characters in the UID for the designated application and passes that information to the application. |
| call application voice warning-time | Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application. |
| show call active fax | Displays call information for fax transmissions in progress. |
| show call application voice | Displays information about voice applications. |
| show call history fax | Displays the call history table for fax transmissions. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice authen-list command was replaced by the param authen-list command in application configuration mode. See the param authen-list command for more information. |
|---|---|

| application-name | Name of the application. |
|---|---|
| method-list-name | Character string used to name a list of authentication methods to be used with T.38 fax relay and T.37 store-and-forward fax. |

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.3(14)T | This command was replaced by the param authen-list command in application configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| aaa authentication | Enable AAA accounting of requested services for billing or security purposes. |
| call application voice authen-method | Specifies the authentication method for a Tcl application. |
| call application voice authentication enable | Enables AAA authentication services for a Tcl application. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice authen-method command is replaced by the param authen-method command in application configuration mode. See the param authen-method command for more information. |
|---|---|

| application-name | Name of the application. |
|---|---|
| prompt user | User is prompted for the Tcl application account identifier. |
| ani | Calling party telephone number (automatic number identification or ANI) is used as the Tcl application account identifier. |
| dnis | Called party telephone number (dialed number identification service or DNIS) is used as the Tcl application account identifier. |
| gateway | Router-specific name derived from the host name and domain name is used as the Tcl application account identifier, displayed
                                          in the following format: router-name.domain-name . |
| redialer id | Account string returned by the external redialer device is used as the Tcl application account identifier. In this case, the
                                          redialer ID is either the redialer serial number or the redialer account number. |
| redialer dnis | Called party telephone number (dialed number identification service or DNIS) is used as the Tcl application account identifier
                                          captured by the redialer if a redialer device is present. |

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.3(14)T | This command was replaced by the param authen-method command in application configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application voice authentication enable | Enables AAA authentication services for a Tcl application. |
| call application voice authen list | Specifies the name of an authentication method list for a Tcl application. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice accounting enable command is replaced by the param accounting enable command in application configuration mode. See the param accounting enable command for more information. |
|---|---|

| application-name | Name of the application. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.3(14)T | This command was replaced by the param accounting enable command in application configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| aaa accounting | Enables AAA accounting of requested services when you use RADIUS or TACACS+. |
| mmoip aaa method fax accounting | Defines the name of the method list to be used for AAA accounting with store-and-forward fax. |

| 1 | (Optional) Convert a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) to a regular DISCONNECT message
                                          when the call is in the active state. |
|---|---|
| 0 | (Optional) Revert to a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) when the call is in the active
                                          state. |

| Release | Modification |
|---|---|
| 12.2(15)ZJ | This command was introduced. |
| 12.3(4)T | This command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.3(14)T | The call application voice default disc-prog-ind-at-connect command was replaced. Use one of the following commands: param convert-discpi-after-connect (application parameter configuration mode) paramspace session_xwork convert-discpi-after-connect (service configuration mode) |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| param convert-discpi-after-connect | Enables or disables conversion of a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) to a regular DISCONNECT
                                          message when the call is in the active state. |
| paramspace session_xwork convert-discpi-after-connect | Enables or disables conversion of a DISCONNECT message with Progress Indicator set to PROG_INBAND (PI=8) to a regular DISCONNECT
                                          message when the call is in the active state. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice dsn-script command is replaced by the param dsn-script command in application parameter configuration mode. |
|---|---|

| mail-application-name | Name of the off-ramp mail application that launches the 
                                          app_voicemail_offramp.tcl scr
                                          ipt when the gateway receives an e-mail trigger. |
|---|---|
| application-name | Name of the VoiceXML application to which the off-ramp mail application hands off the call when the destination answers. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.3(14)T | This command was replaced by the param dsn-script command in application parameter configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| application | Defines a specific voice application in the dial peer. |
| call application voice | Defines the name of a voice application and specifies the location of the document (Tcl or VoiceXML) to load for the application. |
| param dsn-script | Specifies the VoiceXML application to which the off-ramp mail application hands off calls for off-ramp DSN and MDN e-mail
                                          messages. |
| show call application voice | Displays information about the configured voice applications. |

| application-name | Name of the voice application. |
|---|---|
| disable | (Optional) Disables event logging for the named application. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | The call application voice event-log is obsolete. To enable event logging for a specific voice application, use one of the following commands: param event-log (application parameter configuration mode) paramspace appcommon event-log (service configuration mode) |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Note | To prevent event logging from adversely impacting system resources for production traffic, the gateway uses a throttling mechanism.
                                          When free processor memory drops below 20 percent, the gateway automatically disables all event logging. It resumes event
                                          logging when free memory rises above 30 percent. While throttling is occurring, the gateway does not capture any new event
                                          logs even if event logging is enabled. You should monitor free memory and enable event logging only when necessary for isolating
                                          faults. |
|---|---|

| Command | Description |
|---|---|
| call application event-log | Enables event logging for voice application instances. |
| call application event-log max-buffer-size | Sets the maximum size of the event log buffer for each application instance. |
| call application voice | Defines the name of a voice application and specifies the location of the script to load for the application. |
| monitor call application event-log | Displays the event log for an active application instance in real-time. |
| param event-log | Enables or disables logging for linkable Tcl functions (packages). |
| paramspace appcommon event-log | Enable or disables logging for a service (application). |
| show call application session-level | Displays event logs and statistics for voice application instances. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice fax-dtmf command is replaced by the param fax-dtmf command in application parameter configuration mode. See
                                          		  the param fax-dtmf command for more information. |
|---|---|

| application-name | The name of the fax detection IVR application that you
                                          						defined when you loaded the application on the router. |
|---|---|
| 0 \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \| 8 \| 9 \| * \| # | The telephone keypad digit processedby the calling party to
                                          						indicate a fax call, in response to the audio prompt that plays during the
                                          						default-voice or default-fax mode of the fax detection IVR application. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced for the Cisco AS5300. |
| 12.2(2)T | This command was integrated into Cisco IOS Release
                                          						12.2(2)T. |
| 12.2(2)XB | This command was implemented on the Cisco AS5400 and Cisco
                                          						AS5350. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600
                                          						series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.2(11)T | This command was implemented on the Cisco AS5300, Cisco
                                          						AS5350, and Cisco AS5400. |
| 12.3(14)T | This command was replaced by the param fax-dtmf command in application parameter configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the
                                          						new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application voice | Loads an IVR application onto a router and gives it an
                                          						application name. |
| call application voice account-id-method | Configures the fax detection IVR application to use a
                                          						particular method to assign the account identifier. |
| call application voice mode | Configures the fax detection IVR application to operate in
                                          						one of its four modes. |
| call application voice prompt | Configures the fax detection IVR application to use the
                                          						specified audio file as a user prompt. |
| call application voice voice-dtmf | Configures the fax detection IVR application to recognize
                                          						the specified digit to indicate a voice call. |
| debug voip ivr script | Displays debug information from the fax detection IVR
                                          						script. |
| param fax-dtmf | Directs the fax detection IVR application to recognize a
                                          						specified digit to indicate a fax call in default-voice and default-fax modes. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice global-password command is replaced by the param global-password command in application parameter configuration mode. See the param global-password command for more information. |
|---|---|

| application-name | The name of the application. |
|---|---|
| password | Character string used to define the CiscoSecure for Windows NT password to be used with store-and-forward fax. The maximum
                                          length is 64 alphanumeric characters. |

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.3(14)T | This command is replaced by the param global-password command in application parameter configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| param global-password | Defines a password to be used with CiscoSecure for Windows NT when using store-and-forward fax on a voice feature card. |

| application-name | Name of the application to which the language parameters are being passed. |
|---|---|
| digit | Number that identifies the language used by the audio files. Any number can represent any language. Enter 1 to indicate the
                                          primary language and 2 to indicate the secondary language. Range is from 0 to 9. |
| language | Two-character code that identifies the language of the associated audio files. Valid entries are as follows: en --English sp --Spanish ch --Mandarin aa --all |

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced. |
| 12.1(5)T | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB | This command was modified to support VoiceXML applications on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(4)XM | This command was implemented on the Cisco 1751. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series. Support for the Cisco
                                          AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800 and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T for VoiceXML applications. This command is supported on the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco 5800, and Cisco AS5850 in this release. |
| 12.3(14)T | The call application voice language was replaced by the following commands: param language (application parameter configuration mode) paramspace language (service configuration mode) |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Tcl Script Name | Description | Commands to Configure |
|---|---|---|
| app_libretto_onramp9.tcl | Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS. | None |
| app_libretto_offramp5.tcl | Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID. | None |
| clid_4digits_npw_3_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI. | call application voice uid-length Range is 1 to 20. The default is 10. call application voice pin-length Range is 0 to 10. The default is 4. call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_col_npw_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_collect_cli.tcl | This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_3_cli.tcl | This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_npw_cli.tcl | This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together. | call application voice retry-count Range is 1 to 5. The default is 3. |
| fax_rollover_on_busy.tcl | Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy. | voice hunt user-busy |

| Command | Description |
|---|---|
| call application voice | Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application. |
| call application voice load | Reloads the designated Tcl script. |
| call application voice pin-len | Defines the number of characters in the PIN for the application and passes that information to the application. |
| call application voice redirect-number | Specifies the telephone number to which a call is redirected for the designated application. |
| call application voice retry-count | Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application. |
| call application voice set-location | Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application. |
| call application voice uid-len | Defines the number of characters in the UID for the designated application and passes that information to the application. |
| call application voice warning-time | Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application. |
| param language | Configures the language parameter in a service or package on the gateway. |
| paramspace language | Defines the category and location of audio files that are used for dynamic prompts by an IVR application (Tcl or VoiceXML). |
| show call application voice | Displays information about voice applications. |

| application-name | Name of the Tcl or VoiceXML application to reload. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced on the Cisco 2600 series and Cisco 3600 series (except for the Cisco 3660), and on the Cisco AS5300. |
| 12.1(3)T | Support for dynamic script loading of Media Gateway Control Protocol (MGCP) was added. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB | This command was modified to support VoiceXML applications. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1751. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750. |
| 12.2(8)T | This command and implemented on the Cisco 7200 series. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T for VoiceXML applications. This command is supported on the Cisco
                                          AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and the Cisco  AS5850 in this release. |

| Tip | If the call application voice load command fails to load the Tcl script or VoiceXML document that is associated with the application, enable the debug voip ivr command and retry. This debugging command can provide information on why loading fails. |
|---|---|

| Note | MGCP scripting is not supported on the Cisco 1750 router or on Cisco 7200 series routers. |
|---|---|

| Command | Description |
|---|---|
| call application cache reload time | Configures the interval for reloading MGCP scripts. |
| call application voice | Creates and calls the application that interacts with the IVR feature. |
| debug http client | Displays information about the load an application that was loaded with HTTP. |
| show call application voice | Displays a list of the voice applications that are configured. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice mail-script command is replaced by the param mail-script command in application parameter configuration mode. See the param mail-script command for more information. |
|---|---|

| mail-application-name | Name of the off-ramp mail application that launches the 
                                          app_voicemail_offramp.tcl script
                                          when the gateway receives an e-mail trigger. |
|---|---|
| application-name | Name of the VoiceXML application to which the off-ramp mail application hands off the call when the destination answers. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.3(14)T | This command was replaced by the param mail-script command in application parameter configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| application | Defines a specific voice application in the dial peer. |
| call application voice | Defines the name of a voice application and specifies the location of the document (Tcl or VoiceXML) to load for the application. |
| param mail-script | Specifies the VoiceXML application to which the off-ramp mail application hands off a call when the destination telephone
                                          answers. |
| show call application voice | Displays information about the configured voice applications. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice mode command is replaced by the param mode command in application parameter configuration mode. See the param mode command for more information. |
|---|---|

| application-name | Fax detection IVR application that was defined when the application was loaded on the router. |
|---|---|
| connect first | Incoming calls are connected to the Real-Time Streaming Protocol (RTSP) server. This is the default. |
| listen-first | The gateway listens to the call first and then connects to the RTSP server. Any Dual tone multifrequency (DTMF) tones take
                                          the call to the voice server, but subsequent DTMF is forwarded as configured. |
| default voice | Incoming calls are connected as voice calls to the RTSP server. |
| default fax | Incoming calls are connected to the fax relay or store-and-forward fax application that is configured on the gateway. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced on the Cisco AS5300. |
| 12.2(2)XB | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600
                                          series, Cisco 3725, and Cisco 3745. |
| 12.2(11)T | This command is supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release. |
| 12.3(14)T | This command was replaced by the param mode command in application parameter configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application voice | Loads a specified IVR application onto the router from the TFTP server and gives it an application name by which it is known
                                          on the router. |
| call application voice account-id-method | Configures the fax detection IVR application to use a particular method to assign the account identifier. |
| call application voice fax-dtmf | Configures the fax detection IVR application to recognize a specified digit to indicate a fax call . |
| call application voice prompt | Configures the fax detection IVR application to use the specified audio file as a user prompt in listen-first mode, default-voice
                                          mode, or default-fax mode. |
| call application voice voice-dtmf | Configures the fax detection IVR application to recognize a specified digit to indicate a voice call. |
| param mode | Configures the call transfer mode for a package. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice pin-len command is replaced with the param pin-len command in application parameter configuration mode. See the param pin-len command for more information. |
|---|---|

| application-name | Application name to which the PIN length parameter is being passed. |
|---|---|
| number | Number of allowable characters in PINs associated with the specified application. Range is from 0 to 10. The default is 4. |

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced. |
| 12.1(5)T | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750. |
| 12.2(4)XM | This command was implemented on the Cisco 1751. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series. |
| 12.2(11)T | This command is supported on the Cisco AS5350, Cisco AS5400 Cisco AS5800, and the Cisco AS5850 in this release. |
| 12.3(14)T | The call application voice pin-len command was replaced with the param pin-len command in application parameter configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Tcl Script Name | Description | Commands to Configure |
|---|---|---|
| app_libretto_onramp9.tcl | Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS. | None |
| app_libretto_offramp5.tcl | Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID. | None |
| clid_4digits_npw_3_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI. | call application voice uid-length Range is 1 to 20. The default is 10. call application voice pin-length Range is 0 to 10. The default is 4 call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_col_npw_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_collect_cli.tcl | This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_3_cli.tcl | This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_npw_cli.tcl | This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together. | call application voice retry-count Range is 1 to 5. The default is 3. |
| fax_rollover_on_busy.tcl | Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy. | voice hunt user-busy |

| Command | Description |
|---|---|
| call application voice | Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          the application. |
| call application voice language | Specifies the language of the audio file for the designated application and passes that information to the application. |
| call application voice load | Reloads the designated Tcl script. |
| call application voice redirect-number | Specifies the telephone number to which a call is redirected for the designated application. |
| call application voice retry-count | Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application. |
| call application voice set-location | Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application. |
| call application voice uid-len | Defines the number of characters in the UID for the designated application and passes that information to the application. |
| call application voice warning-time | Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application. |
| param pin-len | Defines the number of characters in the PIN for an application. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice prompt command is replaced by the param prompt command. See the param prompt command for more information. |
|---|---|

| application-name | Name of the fax detection IVR application that you defined when you loaded the application on the router. |
|---|---|
| prompt-url | URL or Cisco IOS file system location on the TFTP server for the audio file containing the prompt for the application. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced for the Cisco AS5300. |
| 12.2(2)XB | This command was implemented on the Cisco AS5400 and Cisco AS5350. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600
                                          series, Cisco 3725, and Cisco 3745. |
| 12.2(11)T | This command was implemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.3(14)T | This command was replaced by the param prompt command. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application voice | Loads a specified IVR application onto the router from the TFTP server and gives it an application name by which it is known
                                          on the router. |
| call application voice account-id-method | Configures the fax detection IVR application to use a particular method to assign the account identifier. |
| call application voice fax-dtmf | Configures the fax detection IVR application to recognize a specified digit to indicate a fax call. |
| call application voice mode | Configures the fax detection IVR application to operate in one of its four modes. |
| call application voice voice-dtmf | Configures the fax detection IVR application to recognize a specified digit to indicate a voice call. |
| param prompt | Directs the fax detection IVR application to use the specified audio file as a user prompt. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice redirect-number command is replaced with the param redirect-number command in application parameter configuration mode. See the the param redirect-number command for more information. |
|---|---|

| application name | Name of the application to which the redirect telephone number parameter is being passed. |
|---|---|
| number | Designated operator telephone number of the service provider (or any other number designated by the customer). This is the
                                          number where calls are terminated when, for example, allowed debit time has run out or the debit amount is exceeded. |

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced on the Cisco 2600 series, the Cisco 3600 series, and the Cisco AS5300. |
| 12.1(5)T | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1751. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series. Support for the Cisco
                                          AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release. |
| 12.3(14)T | This command was replaced by the param redirect-number . |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Tcl Script Name | Description | Commands to Configure |
|---|---|---|
| app_libretto_onramp9.tcl | Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS. | None |
| app_libretto_offramp5.tcl | Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID. | None |
| clid_4digits_npw_3_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI. | call application voice uid-length Range is 1 to 20. The default is 10. call application voice pin-length Range is 0 to 10. The default is 4. call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_col_npw_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_collect_cli.tcl | This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_3_cli.tcl | This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_npw_cli.tcl | This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together. | call application voice retry-count Range is 1 to 5. The default is 3. |
| fax_rollover_on_busy.tcl | Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy. | voice hunt user-busy |

| Command | Description |
|---|---|
| call application voice | Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application. |
| call application voice language | Specifies the language of the audio file for the designated application and passes that information to the application. |
| call application voice load | Reloads the designated Tcl script. |
| call application voice pin-len | Defines the number of characters in the PIN for the application and passes that information to the application. |
| call application voice retry-count | Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application. |
| call application voice set-location | Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application. |
| call application voice uid-len | Defines the number of characters in the UID for the designated application and passes that information to the application. |
| call application voice warning-time | Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application. |
| param redirect-number | Defines the telephone number to which a call is redirected--for example, the operator telephone number of the service provider--for
                                          an application. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice retry-count command is replaced by the param retry-count command in application parameter configuration mode. See the the param retry-count command for more information. |
|---|---|

| application name | Name of the application to which the number of possible retries is being passed. |
|---|---|
| number | Number of times the caller is permitted to reenter PIN digits. Range is 1 to 5. The default is 3. |

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced. |
| 12.1(5)T | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1751. |
| 12.2(4)T | This command was introduced on the Cisco 1750. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series. Support for the Cisco
                                          AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5350, Cisco AS5400,
                                          Cisco AS5800, and Cisco AS5850 in this release. |
| 12.3(14)T | This command was replaced by the param retry-count command. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Tcl Script Name | Description | Commands to Configure |
|---|---|---|
| app_libretto_onramp9.tcl | Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS. | None |
| app_libretto_offramp5.tcl | Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID. | None |
| clid_4digits_npw_3_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI. | call application voice uid-length Range is 1 to 20. The default is 10. call application voice pin-length Range is 0 to 10. The default is 4. call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_col_npw_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_collect_cli.tcl | This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_3_cli.tcl | This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_npw_cli.tcl | This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together. | call application voice retry-count Range is 1 to 5. The default is 3. |
| fax_rollover_on_busy.tcl | Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy. | voice hunt user-busy |

| Command | Description |
|---|---|
| call application voice | Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application. |
| call application voice language | Specifies the language of the audio file for the designated application and passes that information to the application. |
| call application voice load | Reloads the designated Tcl script. |
| call application voice pin-len | Defines the number of characters in the PIN for the application and passes that information to the application. |
| call application voice redirect-number | Specifies the telephone number to which a call is redirected for the designated application. |
| call application voice set-location | Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application. |
| call application voice uid-len | Defines the number of characters in the UID for the designated application and passes that information to the application. |
| call application voice warning-time | Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application. |
| param retry-count | Defines the number of times that a caller is permitted to reenter the PIN for a package. |

| application name | Name of the application being configured as trusted. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco 3640 and Cisco 3660. |
| 12.3(14)T | The call application voice security trusted command was replaced by the following commands: param security trusted (application parameter configuration mode) paramspace appcommon security trusted (service configuration mode) |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Note | Tool Command Language (Tcl) applications provide the security parameter to the application but do not use it. |
|---|---|

| Command | Description |
|---|---|
| call application voice | Defines the name of a voice application and specifies the location of the document (Tcl or VoiceXML) to load for the application. |
| call application voice language | Defines the language of the audio files used for dynamic prompts by the designated application. |
| call application voice load | Reloads a Tcl or VoiceXML document. |
| call application voice pin-len | Defines the number of characters in the PIN for the Tcl application. |
| call application voice redirect-number | Defines the telephone number to which a call is redirected for the designated application. |
| call application voice retry-count | Defines the number of times that a caller is permitted to reenter the PIN for a designated application. |
| call application voice uid-len | Defines the number of characters in the UID for the designated application. |
| call application voice warning-time | Defines the number of seconds for which a warning prompt is played before a user’s account time runs out. |
| param security | Configures security for linkable Tcl functions (packages). |
| paramspace appcommon security | Configures security for a service (application). |
| show call application voice | Displays the following information associated with a voice application: the audio files, the prompts, the caller interaction,
                                          and the abort key operation. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice set-location command is replaced by the paramspace language command. See the paramspace language command for more information. |
|---|---|

| application name | Name of the application to which the set location parameters are being passed. |
|---|---|
| language | Two-character code that identifies the language associated with the audio files. Valid entries are as follows: en --English sp --Spanish ch --Mandarin aa --All This is the same language code that was entered when configuring the call application voice language command . |
| category | Category group of the audio files (from 0 to 4). For example, audio files representing the days and months can be category
                                          1, audio files representing units of currency can be category 2, and audio files representing units of time--seconds, minutes,
                                          and hours--can be category 3. Range is from 0 to 4; 0 means all categories. |
| location | URL of the audio files. Valid URLs refer to TFTP, FTP, HTTP, or RTSP servers, flash memory, or the removable disks on the
                                          Cisco 3600 series. |

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco AS5300. |
| 12.1(5)T | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB | This command was modified to support VoiceXML applications on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1751. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T for VoiceXML applications. This command is supported on the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release. |
| 12.3(14)T | This command was replaced by the paramspace language command. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Tcl Script Name | Description | Commands to Configure |
|---|---|---|
| app_libretto_onramp9.tcl | Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS. | None |
| app_libretto_offramp5.tcl | Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID. | None |
| clid_4digits_npw_3_cli.tcl | Authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for the account
                                          number and password, respectively, are configurable through the command-line interface (CLI). If the authentication fails,
                                          the script allows the caller to retry. The retry number is also configured through the CLI. | call application voice uid-length Range is 1 to 20. The default is 10. call application voice pin-length Range is 0 to 10. The default is 4. call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_col_npw_cli.tcl | Authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_collect_cli.tcl | Authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the caller to
                                          retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_3_cli.tcl | Authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_npw_cli.tcl | Authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller to retry.
                                          The retry number is configured through the CLI. The account number and PIN are collected together. | call application voice retry-count Range is 1 to 5. The default is 3. |
| fax_rollover_on_busy.tcl | Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy. | voice hunt user-busy |

| Command | Description |
|---|---|
| call application voice | Specifies the application name and indicates the location of the IVR script to be used with this application. |
| call application voice language | Specifies the audio file language for the designated application. |
| call application voice load | Reloads the designated Tcl script. |
| call application voice pin-len | Specifies the number of characters in the PIN. |
| call application voice redirect-number | Specifies the telephone number to which a call is redirected. |
| call application voice retry-count | Defines the number of times a caller is permitted to reenter the PIN. |
| call application voice uid-len | Defines the number of characters in the UID for the designated application. |
| call application voice warning-time | Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application. |
| paramspace language | Defines the category and location of audio files that are used for dynamic prompts by an IVR application (Tcl or VoiceXML). |
| show call application voice | Displays information about voice applications. |

| application-name | Name of the voice application for which the transfer method is set. |
|---|---|
| redirect | Gateway redirects the call leg to the redirected destination number. |
| redirect-at-alert | Gateway places a new call to the redirected destination number and initiates a call transfer when the outgoing call leg is
                                          in the alert state. If the call transfer is successful, the two call legs are disconnected on the gateway. If the transfer
                                          fails, the gateway bridges the two call legs. Provides support for Two B-Channel Transfer (TBCT). |
| redirect-at-connect | Gateway places a new call to the redirected destination number and initiates a call transfer when the outgoing call leg is
                                          in the connect state. If the call transfer is successful, the two call legs are disconnected on the gateway. If the transfer
                                          fails, the gateway bridges the two call legs. Provides support for TBCT. |
| redirect-rotary | Gateway redirects the call leg to the redirected destination number. If redirection fails, the gateway places a rotary call
                                          to the redirected destination number and hairpins the two call legs. For TBCT, this mode is the same as for the redirect-at-connect keyword. |
| rotary | Gateway places a rotary call for the outgoing call leg and hairpins the two call legs. Call redirection is not invoked. This
                                          is the default. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |
| 12.3(14)T | This command was replaced by the following commands: param mode (application parameter configuration mode) paramspace callsetup mode (service configuration mode) |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| application | Enables a voice application on a dial peer. |
| call application voice | Defines the name of a voice application and specifies the location of the Tcl or VoiceXML document to load for this application. |
| call application voice transfer reroute-mode | Specifies the call-forwarding behavior of a Tcl application. |
| debug voip ivr callsetup redirect | Displays debugging information about H.450 calls that are redirected during setup. |
| debug voip ivr redirect | Displays debugging information about redirected H.450 calls. |
| isdn supp-service tbct | Enables ISDN TBCT on PRI trunks. |
| param mode | Configures the call transfer mode for a package. |
| paramspace callsetup mode | Configures the call transfer mode for an application. |
| show call active voice redirect | Displays information about active calls that are being redirected using RTPvt or TBCT. |
| show call application voice | Displays information about voice applications. |
| show call history voice redirect | Displays history information about calls that were redirected using RTPvt or TBCT. |

| application-name | Name of the voice application for which the transfer reroute method is set. |
|---|---|
| none | Call forwarding is not performed by the voice application. |
| redirect | Two call legs are directly connected. Provides support for RTPvt. |
| redirect-rotary | Two call legs are directly connected (redirect). If that fails, the two call legs are hairpinned on the gateway (rotary). |
| rotary | Gateway places a rotary call for the outgoing call leg and hairpins the two calls together. RTPvt is not invoked. This is
                                          the default. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |
| 12.3(14)T | This command was replaced by the following commands: param reroutemode (application parameter configuration mode) paramspace callsetup reroutemode (service configuration mode) |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| application | Enables a voice application on a dial peer. |
| call application voice | Defines the name of a voice application and specifies the location of the Tcl or VoiceXML document to load for this application. |
| call application voice transfer mode | Specifies the call-transfer behavior of a Tcl or VoiceXML application. |
| isdn supp-service tbct | Enables ISDN TBCT on PRI trunks. |
| param reroutemode | Configures the call transfer reroutemode (call forwarding) for a package. |
| paramspace callsetup reroutemode | Configures the call reroute mode (call forwarding) for an application. |
| show call active voice redirect | Displays information about active calls that are being redirected using RTPvt or TBCT. |
| show call application voice | Displays information about voice applications. |
| show call history voice redirect | Displays history information about calls that were redirected using RTPvt or TBCT. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice uid-length command is replaced by the param uid-len command. See the param uid-len command for more information. |
|---|---|

| application-name | Name of the application to which the UID length parameter is passed. |
|---|---|
| number | Number of allowable characters in UIDs that are associated with the specified application. Range is from 1 to 20. The default
                                          is 10. |

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco AS5300. |
| 12.1(5)T | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1751. This release does not support any other Cisco platforms. |
| 12.2(4)T | Support was added for the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 7200 series. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release. |
| 12.3(14)T | This command was replaced by the param uid-len command. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Tcl Script Name | Description | Commands to Configure |
|---|---|---|
| app_libretto_onramp9.tcl | Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS. | None |
| app_libretto_offramp5.tcl | Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID. | None |
| clid_4digits_npw_3_cli.tcl | Authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for the account
                                          number and password, respectively, are configurable through the command-line interface (CLI). If the authentication fails,
                                          the script allows the caller to retry. The retry number is also configured through the CLI. | call application voice uid-length Range is 1 to 20. The default is 10. call application voice pin-length Range is 0 to 10. The default is 4. call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_col_npw_cli.tcl | Authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_collect_cli.tcl | Authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the caller to
                                          retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_3_cli.tcl | Authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_npw_cli.tcl | Authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller to retry.
                                          The retry number is configured through the CLI. The account number and PIN are collected together. | call application voice retry-count Range is 1 to 5. The default is 3. |
| fax_rollover_on_busy.tcl | Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy. | voice hunt user-busy |

| Command | Description |
|---|---|
| call application voice | Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application. |
| call application voice language | Specifies the language of the audio file for the designated application and passes that information to the application. |
| call application voice load | Reloads the designated Tcl script. |
| call application voice pin-len | Defines the number of characters in the PIN for the application and passes that information to the application. |
| call application voice redirect-number | Specifies the telephone number to which a call is redirected for the designated application. |
| call application voice retry-count | Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application. |
| call application voice set-location | Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application. |
| call application voice warning-time | Defines, in seconds, how long in advance a user is warned before the allowed calling time expires for the designated application. |
| param uid-length | Defines the number of characters in the UID for a package. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice voice-dtmf command is replaced by the param voice-dtmf command. See the param voice-dtmf command for more information. |
|---|---|

| application-name | The name of the fax detection application that you defined when you loaded the application on the router. |
|---|---|
| keypad-character | Single character that can be dialed on a telephone keypad pressed by the calling party to indicate a voice call, in response
                                          to the audio prompt configured in default-voice and default-fax mode of the fax detection IVR application. Default is 1. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced for the Cisco AS5300. |
| 12.2(2)XB | This command was implemented on the Cisco AS5400 and Cisco AS5350. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600
                                          series, Cisco 3725, and Cisco 3745. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not included in this release. |
| 12.2(11)T | This command was supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release. |
| 12.3(14)T | This command was replaced by the param voice-dtmf command. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application voice | Loads a specified IVR application onto the router from the TFTP server and gives it an application name by which it is known
                                          on the router. |
| call application voice account-id-method | Configures the fax detection IVR application to use a particular method to assign the account identifier. |
| call application voice fax-dtmf | Configures the fax detection IVR application to recognize a specified digit to indicate a fax call. |
| call application voice mode | Configures the fax detection IVR application to operate in one of its four modes. |
| call application voice prompt | Configures the fax detection IVR application to use the specified audio file as a user prompt. |
| param voice-dtmf | Directs the fax detection IVR application to recognize a specified digit to indicate a voice call. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application voice warning-time command is replaced by the param warning-time command. See the param warning-time command for more information. |
|---|---|

| application-name | Name of the application to which the warning time parameter is being passed. |
|---|---|
| seconds | Length of the warning period, in seconds, before the allowed calling time expires. Range is from 10 to 600. This argument
                                          has no default value. |

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco AS5300. |
| 12.1(5)T | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1751. Support for other Cisco platforms is not included in this release. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 7200 series. |
| 12.2(11)T | This command was implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release. |
| 12.3(14)T | This command was replaced by the param warning-time command. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Tcl Script Name | Description | Commands to Configure |
|---|---|---|
| app_libretto_onramp9.tcl | Authenticates the account and personal identification number (PIN) using the following: prompt-user, using automatic number
                                          identification (ANI), dialed number identification service (DNIS), gateway ID, redialer ID, and redialer DNIS. | None |
| app_libretto_offramp5.tcl | Authenticates the account and PIN using the following: envelope-from, envelope-to, gateway ID, and x-account ID. | None |
| clid_4digits_npw_3_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. The number of digits allowed for
                                          the account number and password, respectively, are configurable through the command-line interface (CLI). If the authentication
                                          fails, the script allows the caller to retry. The retry number is also configured through the CLI. | call application voice uid-length Range is 1 to 20. The default is 10. call application voice pin-length Range is 0 to 10. The default is 4. call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_col_npw_cli.tcl | This script authenticates the account number and PIN, respectively, using ANI and NULL. If the authentication fails, it allows
                                          the caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_authen_collect_cli.tcl | This script authenticates the account number and PIN using ANI and DNIS. If the authentication fails, the script allows the
                                          caller to retry. The retry number is configured through the CLI. The account number and PIN are collected separately. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_3_cli.tcl | This script authenticates using ANI and NULL for account numbers and PINs, respectively. If the authentication fails, it
                                          allows the caller to retry. The retry number is configured through the CLI. | call application voice retry-count Range is 1 to 5. The default is 3. |
| clid_col_npw_npw_cli.tcl | This script authenticates using ANI and NULL for account and PIN, respectively. If authentication fails, it allows the caller
                                          to retry. The retry number is configured through the CLI. The account number and PIN are collected together. | call application voice retry-count Range is 1 to 5. The default is 3. |
| fax_rollover_on_busy.tcl | Used for on-ramp T.38 fax rollover to T.37 fax when the destination fax line is busy. | voice hunt user-busy |

| Command | Description |
|---|---|
| call application voice language | Specifies the language of the audio file for the designated application and passes that information to the application. |
| call application voice load | Reloads the designated Tcl script. |
| call application voice location | Specifies the name to be used for an application and indicates the location of the appropriate IVR script to be used with
                                          this application. |
| call application voice pin-len | Defines the number of characters in the PIN for the application and passes that information to the application. |
| call application voice redirect-number | Specifies the telephone number to which a call is redirected for the designated application. |
| call application voice retry-count | Defines the number of times a caller is permitted to reenter the PIN for a designated application and passes that information
                                          to the application. |
| call application voice set-location | Defines the location, language, and category of the audio files for the designated application and passes that information
                                          to the application. |
| call application voice uid-length | Defines the number of characters in the UID for the designated application and passes that information to the application. |
| param warning-time | Defines the number of seconds of warning that a user receives before the allowed calling time expires. |

| disconnect-cause incoming | Associates a disconnect cause of incoming calls. |
|---|---|
| call-reject | Specifies call rejection as the cause for blocking a call during incoming call-number translation. |
| invalid-number | Specifies invalid number as the cause for blocking a call during incoming call-number translation. |
| unassigned-number | Specifies unassigned number as the cause for blocking a call during incoming call-number translation. |
| user-busy | Specifies busy as the cause for blocking a call during incoming call-number translation. |
| translation-profile incoming | Associates the translation profile for incoming calls. |
| name | Name of the translation profile. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| dial-peer voice | Initiates the dial-peer voice configuration mode. |
| voice translation-profile | Defines a translation profile for voice calls. |
| voice translation-rule | Defines a translation rule for voice calls. |