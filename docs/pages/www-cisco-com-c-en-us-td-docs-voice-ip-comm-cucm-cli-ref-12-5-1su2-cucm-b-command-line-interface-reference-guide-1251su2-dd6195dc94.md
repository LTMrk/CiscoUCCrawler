---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-cli-ref-12-5-1su2-cucm-b-command-line-interface-reference-guide-1251su2-dd6195dc94
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/12_5_1SU2/cucm_b_command-line-interface-reference-guide-1251Su2/cucm_b_command-line-interface-reference-guide-1251Su2_chapter_0110.html
retrieved_at: 2026-08-17T00:00:05.232479+00:00
---

Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU2

# Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU2

Updated: October 3, 2023

Chapter: Set Commands

## Chapter: Set Commands

# Set Commands

## set account
                        	 enable

This command
                              		  enables the OS user account that was disabled because of password inactivity.

set account enable user-id

## Syntax Description

Specifies
                                       					 the user ID of the account that was disabled.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## set account
                        	 name

This command sets
                              		  up a new account on the operating system.

set account name name

## Syntax Description

Represents
                                       					 the username for the new account.

Enter a name comprised of only alphabets or characters comprised of alphanumeric characters (a-z, A-D, 0-9).

### Command Modes

Administrator (admin:)

### Usage Guidelines

After you enter the username, the system prompts you to enter the privilege level (0 or 1) and password for the new account.
                              The privilege levels definitions are as follows:

Specifies an
                                    				  ordinary privilege level. Users with ordinary privileges can run CLI commands
                                    				  with privilege level 0 only.

Specifies an
                                    				  advanced privilege level. Users with advanced privileges can run CLI commands
                                    				  with privilege level 1 and below.

The administrator account that the system creates during Unified Communications Manager installation has a privilege level of 4. The administrator can run all commands in the CLI.

The set account name command includes the following new prompts:

'Allow this User to login to SAML SSO-enabled system through the Recovery URL ? (Yes / No)' — Level 4 administrators can enable or disable the access to the recovery URL sign-in option for new platform administrators
                                    by typing 'Yes' or 'No' on the CLI. The value can be configured to 'Yes' if a user chooses to sign-in using the Recovery URL.

'To authenticate a platform login for SSO, a Unique Identifier (UID) must be provided that identifies this user to LDAP (such
                                       as sAMAccountName or UPN). Please enter the appropriate LDAP Unique Identifier (UID) for this user:[UID]' — Level 4 administrator can type the unique identifier value for each platform administrator for this prompt.

Only the Level 4 administrator has privileges to run all the CLI commands.

The administrator must ensure to perform the following tasks:

Type either 'Yes' or 'No' for the 'Allow this User to login to SAML SSO-enabled system through Recovery URL ? (Yes / No)' prompt. If this prompt value is blank, an error message appears.

Type a value for the 'To authenticate a platform login for SSO, a Unique Identifier (UID) must be provided that identifies this user to LDAP (such
                                                   as sAMAccountName or UPN). Please enter the appropriate LDAP Unique Identifier (UID) for this user:[UID]' prompt. If the prompt value is duplicate, an error message appears. You can hit the Enter key and then, the user account
                                                name is saved by default. After the account is created successfully, the administrator will see the message Account created successfully. Log in to the CLI and update the password before you log in to OS Administration.

In the case of SAML SSO login for Operating System Admin pages, if LDAP user consists of ' & ' character, make sure you create platform user without ' & ' and then map to LDAP user consisting of ' & ' character.

In the case of SAML SSO login for Operating System Admin pages, if LDAP attribute value for User ID is telephonenumber, make
                                                sure you create platform user using consisting of alphanumeric characters or English alphabets only. Do not include platform
                                                user name with only numeric values. Then, map to the appropriate LDAP user having the UID value as telephone number.

### Requirements

Command privilege level: 4

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## set
                        	 accountlocking

This command
                              		  enables or disables account locking for the current administration accounts.

set accountlocking { enable | disable }

## Syntax Description

Enable
                                       					 account locking.

Disable
                                       					 account locking.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After you run this command with enable , the system automatically enables account lockout notification after the system enables the audit logging function.

When the Administration account locking feature is enabled, and the user enters the wrong password more than the accountlocking
                                          count, the account gets locked for a set period. The message that the account is locked is only seen on the VM console and
                                          secure logs.

### Requirements

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## set accountlocking count

This command sets the global consecutive failed sign-in attempt count that triggers locking a user account.

set accountlocking count attempts

## Syntax Description

Parameters

Description

Represents the number of consecutive sign-in attempts before the system locks the account.

Value Range: 2-5

Default value: 3

### Command Modes

Administrator (admin:)

### Usage Guidelines

To change the global value for consecutive failed sign-in attempts before the system locks a user account, execute this command.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## set accountlocking
                        	 unlocktime

This command configures the unlock time for the current Unified Communications Manager admin accounts.

set accountlocking unlocktime seconds

## Syntax Description

Parameters

Description

Specifies the unlock time in seconds.

Value Range: 30-3600

Default value: 300

The account gets automatically unlocked only after the configured unlock time.

This command is only valid when account locking is enabled. If account locking is disabled, the system does not remember the
                                                account locking unlock time and uses the default value, 300, after you enable account locking.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## set account ssorecoveryurlaccess

This command enables or disables the SSO recovery URL access for platform administrators.

By default, the platform administrator Level 4 has access to the recovery URL. If the platform administrator Level 4 attempts
                                          to update the recovery URL access for own self, an error appears.

set account ssorecoveryurlaccess { enable | disable } userid

## Syntax Description

Enable the recovery sign-in option for platform administrators.

Disable the recovery sign-in option for platform administrators.

Specifies a particular Cisco Unified Operating System Administrator account.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If you enable or disable the recovery sign-in option, which is already enabled or disabled, an error appears.

The administrator account that the system creates when Unified Communications Manager installs has a privilege level of 4.
                                                The administrator can run all commands in the CLI.

### Requirements

Command privilege level: 4

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager

## set account ssouidvalue

This command updates the unique identifier value for the existing platform administrators.

set account ssouidvalue userid

## Syntax Description

Specifies a particular Cisco Unified Operating System Administrator account whose unique identifier value needs to be updated.

### Command Modes

Administrator (admin:)

### Usage Guidelines

When you run the set account ssouidvalue userid command, a prompt appears to provide the UID value. If the UID value is blank, then samaccountname is saved as ssouidvalue
                                                by default.

If a duplicate UID value exists, an error appears.

### Requirements

Command privilege level: 4

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager

## set cert bulk consolidate

This command consolidates all the certificates that are available on the unit.

set cert bulk consolidate unit

## Syntax Description

Represents the unit name.

### Command Modes

Administrator (admin:)

### Usage Guidelines

You must specify the SFTP server information to use for cert bulk operations.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set cert bulk export

This command exports all the certificates that are available on the unit.

set cert bulk export unit

## Syntax Description

Exports all the available certificates for this unit in this cluster to the preconfigured SFTP location.

Represents the unit name.

### Command Modes

Administrator (admin:)

### Usage Guidelines

You must specify the SFTP server information to use for cert bulk operations.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set cert bulk export all
Successfully exported tomcat certificate(s) to sftp server.
Successfully exported tftp certificate(s) to sftp server.
```

## set cert bulk import

This command imports the certificates that are in the SFTP location into the specified unit trust-store.

set cert bulk import unit

## Syntax Description

Represents the unit name.

### Command Modes

Administrator (admin:)

### Usage Guidelines

You must specify the SFTP server information to use for cert bulk operations.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set cert bulk import all
Successfully imported tomcat certificates.
Successfully imported tftp certificates.
```

## set cert bulk sftp

This command prompts for the SFTP server information to  use for bulk operations.

set cert bulk sftp

### Command Modes

Administrator (admin:)

### Usage Guidelines

You must specify the SFTP server information to use for cert bulk operations.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set cert default-ca-list disable

This command disables all or particular default CA certificates from all servers in the cluster.

When you try to execute this command, a warning message appears displaying that this operation disables all or particular
                              default Cisco CA certificates.

Please ensure that you are executing this command from the Unified Communications Manager publisher node.

The default CA certificate names can be obtained by executing the show cert default-ca-list command.

## Syntax Description

Parameters

Description

Deletes all the default CA certificates from all servers in the cluster.

Deletes the particular default CA certificate from all servers in the cluster.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Consider the following information after you disable all the default CA certificates.

Restart the "Cisco Tomcat" , "Cisco CallManager" , "Cisco Tftp" , and "Cisco Certificate Authority Proxy Function" services.

Consider the following information after you disable the specific default CA certificate.

Restart the "Cisco CallManager" , "Cisco Tftp" , and "Cisco Certificate Authority Proxy Function" services.

If you are disabling "VeriSign Class 3 Secure Server CA - G3" certificate, then restarting of only "Cisco Tomcat" service is sufficient.

### Requirements

Command privilege level: 1

Applies to: Unified Communications Manager

### Example

```
admin:set cert default-ca-list disable all

WARNING: This operation will disable all Cisco CA certificates that have been installed
by default. You can use the "show cert default-ca-list" to view the list of default 
Cisco CA certificates.
You must restart the "Cisco Tomcat", "Cisco CallManager", "Cisco Tftp" and 
"Cisco Certificate Authority Proxy Function" services after running this command. 
This command should be run from the Publisher.
Do you wish to proceed (yes|no)? yes Successfully disabled the default Cisco CA certificates. 
Please wait for a few min to UI to reflect the correct status.
```

```
admin:set cert default-ca-list disable common-name
Enter the Common Name of Default CA Certificate : CAP-RTP-001 WARNING: This operation will disable the "CAP-RTP-001" Cisco CA certificate.
You must restart the "Cisco CallManager", "Cisco Certificate Authority Proxy Function" and
"Cisco Tftp" services after running this command. This command should be run from the Publisher.
Do you wish to proceed (yes|no)? yes Successfully disabled default "CAP-RTP-001" certificate.

admin:set cert default-ca-list disable common-name
Enter the Common Name of Default CA Certificate : VeriSign Class 3 Secure Server CA - G3 WARNING: This operation will disable the "VeriSign Class 3 Secure Server CA - G3" Cisco CA
certificate. You must restart the "Cisco Tomcat" services after running this command.
This command should be run from the Publisher.
Do you wish to proceed (yes|no)? yes Successfully disabled default "VeriSign Class 3 Secure Server CA - G3" certificate.

admin:set cert default-ca-list enable common-name
Enter the Common Name of Default CA Certificate : capf The capf certificate is not in the list of default Cisco CA certificates.
admin:
```

## set cert default-ca-list enable

This command enables all or particular default CA certificates except CAPF-trust on all servers in the cluster. CAPF-trust
                              certificate enable only on the Unified Communications Manager publisher node not across the cluster.

When you try to execute this command, a warning message appears displaying that this operation enables all or particular default
                              Cisco CA certificates as a trusted certificate.

Please ensure that you are executing this command from the Unified Communications Manger publisher node.

The default CA certificate names can be obtained by executing the show cert default-ca-list command.

## Syntax Description

Parameters

Description

Enables all the default CA certificates on all servers in the cluster.

Enables the particular default CA certificate on all servers in the cluster.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Consider the following information after you enable all the default CA certificates.

Restart the "Cisco Tomcat" , "Cisco CallManager" , "Cisco Tftp" , and "Cisco Certificate Authority Proxy Function" services.

Consider the following information after you enable the specific default CA certificate.

Restart the "Cisco CallManager" , "Cisco Tftp" , and "Cisco Certificate Authority Proxy Function" services.

If you are enabling "VeriSign Class 3 Secure Server CA - G3" certificate, then restarting of only "Cisco Tomcat" service is sufficient.

### Requirements

Command privilege level: 1

Applies to: Unified Communications Manager

### Example

```
admin:set cert default-ca-list enable all

WARNING: This operation will enable all default Cisco CA certificates
as trusted certificates for all nodes in this cluster.
You can use the "show cert default-ca-list" to view the list of default
Cisco CA certificates. You must restart the "Cisco Tomcat", "Cisco CallManager",
"Cisco Tftp" and "Cisco Certificate Authority Proxy Function" services after
running this command. This command should be run from the Publisher.
Do you wish to proceed (yes|no)? yes Successfully enabled the default Cisco CA certificates. 
Please wait for a few minutes for the UI to reflect the correct status.
```

```
admin:set cert default-ca-list enable common-name
Enter the Common Name of Default CA Certificate : CAP-RTP-002 WARNING: This operation will install the "CAP-RTP-002" certificate as a trusted certificate
for all nodes in this cluster. You must restart the "Cisco CallManager",
"Cisco Certificate Authority Proxy Function" and  "Cisco Tftp" services after running this
command. This command should be run from the Publisher.
Do you wish to proceed (yes|no)? yes Successfully enabled default "CAP-RTP-002" certificate.

admin:set cert default-ca-list enable common-name
Enter the Common Name of Default CA Certificate : VeriSign Class 3 Secure Server CA - G3 WARNING: This operation will install the "VeriSign Class 3 Secure Server CA - G3" certificate
as a trusted certificate for all nodes in this cluster. You must restart the "Cisco Tomcat"
services after running this command. This command should be run from the Publisher.
Do you wish to proceed (yes|no)? yes Successfully enabled default "VeriSign Class 3 Secure Server CA - G3" certificate.

admin:set cert default-ca-list enable common-name
Enter the Common Name of Default CA Certificate : CAP-RTP-003 The CAP-RTP-003 certificate is not in the list of default Cisco CA certificates.
admin:
```

## set cert delete

This command deletes a specific certificate file from the trust unit.

set cert delete unit name

## Syntax Description

Specifies the name of the trust category, as "own" or "trust" .

Certificate file name.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set cert delete cucm siptest.pem
```

## set cert
                        	 import

This command imports
                              		  the specified certificate for the specified certificate type.

set cert import type name [caCert]

## Syntax Description

Specifies
                                       					 the certificate type as "own" or "trust" .

Represents
                                       					 the unit name.

Represents
                                       					 the name of the CA certificate file name.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set cert import trust tomcat
Successfully imported certificate for tomcat.
Please restart services related to tomcat for the new certificate to
become active.
```

## set cert regen

This command regenerates the certificate for the specified unit.

set cert regen name

## Syntax Description

Represents the unit name.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set cert regen tomcat
Successfully regenerated certificate for tomcat.
```

## set cert regen
                        	 ITLRecovery

This command regenerates the ITLRecovery certificate for the specified
                              		  unit.

After you type this command, a warning message appears displaying that
                              		  if you are using a tokenless CTL and if the you are regenerating the
                              		  CallManager certificate, ensure that the CTL file has the updated CallManager
                              		  certificate and that certificate is updated to endpoints. To regenerate the
                              		  certificate, type yes or else type no .

set cert regen ITLRecovery

## Syntax Description

Represents the ITLRecovery certificate.

### Command Modes

Administrator (admin:)

### Requirements

Caution

You must restart the services related to ITLRecovery for the
                                          			 regenerated certificates to become active.

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set cert regen ITLRecovery

WARNING: If you are using a tokenless CTL and if the CallManager certificate is recently 
generated, please ensure that the CTL File already has the new CallManager certificate and is
updated to the endpoints, before generating the ITL Recovery certificate. Are you sure want 
to proceed?

Proceed with regeneration (yes|no)? yes

Successfully Regenerated Certificate for ITLRecovery.

You must restart the services related to ITLRecovery for the regenerated certificates to 
become active.
```

## set cli pagination

For the current CLI session, this command turns automatic pagination On or Off.

set cli pagination { on | off }

## Syntax Description

Turns pagination on.

Turns pagination off.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

```
admin:set cli pagination off
Automatic pagination is turned off
```

## set cli session timeout

This command sets the time, in minutes, after which an active CLI session times out and disconnects.

set cli session timeout minutes

## Syntax Description

Specifies the time, in minutes, that can elapse before an active CLI session times out and disconnects.

Value range: 5-99999 minutes

Default value: 30 minutes

### Command Modes

Administrator (admin:)

### Usage Guidelines

Be aware that the new session timeout value becomes effective immediately for a new CLI session; however, active sessions
                              retain their original timeout value. Also the show cli session timeout command reflects the new value, even if the current
                              session does not use that value.

This setting gets preserved through a software upgrade and does not get reset to the default value.

### Requirements

Command privilege level:  1

Allowed during upgrade:  No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set commandcount

This command changes the CLI command prompt, so it displays how many CLI commands have executed.

set commandcount { enable | disable }

## Syntax Description

Turns on command count.

Turns off command count.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level:  1

Allowed during upgrade:  No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set csr gen

This command
                              		  generates the csr for the unit name.

set csr gen name

## Syntax Description

Specifies
                                       					 the unit on which the certificate is generated.

### Command Modes

Administrator (admin:)

### Requirements

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set csr gen tomcat
Successfully Generated CSR for tomcat.
```

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

## set cuc jetty stderrlog

This command enables or disables the error log getting generated while any standard error occurs during communicating with
                              the Jetty server. This error log gets generated and is available at the path /var/log/active/jetty/ .

set cuc jetty stderrlog { enable | disable }

## Syntax Description

Enables the error log on the Jetty server. Be aware that enable is case sensitive.

Disables the error log on the Jetty server. Be aware that disable is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Caution

You must restart the Jetty services after enabling or disabling the error log on the Jetty server.

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Cisco Unity Connection only.

### Enable Error Log on Jetty Server Example

```
admin:set cuc jetty stderrlog enable

Command is executed successfully
To effect changes restart jetty server
Restart Jetty Server through Unity Connection Serviciabilty .
Go to Tools -> Service Management -> Restart Connection Jetty Service.
Check the logs that should not be generated after running above command.
Check the requestlog by sending one voice message through webinbox. 
Notifications should not come in logs
```

## set cuc jetty stdoutlog

This command enables or disables the standard input and output log getting generated while communicating with Jetty server.
                              This standard input and output log gets generated and is available at the path /var/log/active/jetty/ .

set cuc jetty stdoutlog { enable | disable }

## Syntax Description

Enables the standard input and output log on the Jetty server. Be aware that enable is case sensitive.

Disables the standard input and output log on the Jetty server. Be aware that disable is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Caution

You must restart the Jetty services after enabling or disabling the standard input and output log on the Jetty server.

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Cisco Unity Connection only.

### Enable Standard Input and Output Log on Jetty Server Example

```
admin:set cuc jetty stdoutlog enable

Command is executed successfully
To effect changes restart jetty server
Restart Jetty Server through Unity Connection Serviciabilty .
Go to Tools -> Service Management -> Restart Connection Jetty Service.
Check the logs that should not be generated after running above command.
Check the requestlog by sending one voice message through webinbox. 
Notifications should not  come in logs
```

## set cuc jetty requestlog

This command enables or disables the request log getting generated from the Jetty server while any request is raised for notifications.
                              This request log gets generated and is available at the path /usr/local/jetty/logs/ .

set cuc jetty requestlog { enable | disable }

## Syntax Description

Enables the request log on the Jetty server. Be aware that "enable" is case sensitive.

Disables the request log on the Jetty server. Be aware that "disable" is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Caution

You must restart the Jetty services after enabling or disabling the request log on the Jetty server.

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Cisco Unity Connection only.

### Enable Request Log on Jetty Server Example

```
admin:set cuc jetty requestlog enable

Command is executed successfully
To effect changes restart jetty server
Restart Jetty Server through Unity Connection Serviciabilty .
Go to Tools -> Service Management -> Restart Connection Jetty Service.
Check the logs that should not be generated after running above command.
Check the requestlog by sending one voice message through webinbox. 
Notifications should not come in logs
```

## set cuc speechview registration certificate size

This command sets up new certificate bit size for Speech to Text service registration and Voicemail transcription with Nuance
                              server.

set cuc speechview registration certificate size bit_size

## Syntax Description

Specifies the bit_size of certificate. Its allowed values are 1k, 2k or 4k.

### Command Modes

Administrator (admin:)

### Usage Guidelines

To set the desired certificate bit size, use the set cuc speechview registration certificate size (Cisco Unity Connection Only) command. The CLI must be executed on the publisher. It will restart the Connection SpeechView
                              Processor service.

### Requirements

Command privilege level: 4

## set cuc srsv timeout

This command sets the value for SRSV session timeout.

set cuc srsv timeout timeout_value

## Syntax Description

Sets the time for session logout.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Cisco Unity Connection

## set cuc trace

This command enables or disables the specified traces and trace levels.

set cuc trace { enable | disable } trace_name level

## Syntax Description

Enables Connection traces.

Disables Connection traces.

Specifies the name of the trace to enable or disable. Be aware that trace names are case sensitive.

Specifies the level or levels of trace_name that you want to enable or disable. Each trace comprises up to 31 levels, numbered
                                       0 to 30; each level provides a different type of information for the specified trace. When you enable or disable multiple
                                       levels, use a comma to separate levels and a hyphen to indicate a range of levels. Do not include spaces.

### Command Modes

Administrator (admin:)

### Usage Guidelines

To display a list of the traces and trace levels that are currently enabled, use the show cuc trace levels (Cisco Unity Connection Only) command.

### Requirements

Command privilege level:  1

Allowed during upgrade:  No

Applies to: Cisco Unity Connection only.

### Enable VUI Traces 1, 13, and 17 Through 20 Example

```
admin:set cuc trace enable VUI 1,13,17-20
VUI trace levels are now set to: 1,13,17-20
```

### Disable VUI Traces 17 Through 20 While VUI Trace Levels 1 and 13 Remain Set Example

```
admin:set cuc trace disable VUI 17-20
VUI trace levels are now set to: 1,13
```

## set date

This command changes
                              		  the time and date on the server.

set date HH:mm:ss:MM/DD/YY

## Syntax Description

Represents
                                       					 the time format (24 hours format).

Date
                                                      						  format MM/DD/YYYY is also accepted.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the server is configured to synchronize with external NTP servers, this command requires the user to remove all of those
                              NTP servers.

### Requirements

Applies to: Unified
                                 			 Communications Manager and Cisco Unity Connection.

### Set Date and
                              		  Time to 2:10:33 Pm April 13th 2012 Example

```
admin:set date 14:10:33:04/13/12
```

### Requirements

Command privilege level: 1

Allowed during upgrade: No

## set dscp defaults

This command sets the factory default DSCP settings for all of the port tags.

set dscp defaults

### Command Modes

Administrator (admin:)

### Usage Guidelines

All non-default DSCP settings get removed after you run this command.

You can use the command show dscp defaults to see the factory default DSCP settings.

### Requirements

Command privilege level:  1

Allowed during upgrade:  No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set dscp

This command enables or disables DSCP marking on outgoing TCP or UDP packets. You can enable or disable DSCP on a single port
                              tag, or on all port tags at once.

set dscp { enable | disable } { all | port_tag }

## Syntax Description

Disables all DSCP port tags.

Represents a DSCP port tag, which is a string that is mapped to a TCP or UDP port to identify the application that uses the
                                       port. This value is for the portTag field displayed when you use the command show dscp defaults . The set of port tags is predefined.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level:  1

Allowed during upgrade:  No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set dscp marking

This command sets DSCP markings on port tags by using well-known DSCP classes and numeric values.

set dscp marking port_tag value

## Syntax Description

Represents a DSCP port tag, which is a string that is mapped to a TCP or UDP port to identify the application that uses the
                                       port. This value is for the portTag field displayed when you use the command show dscp defaults . The set of port tags is predefined.

A DSCP value. You can enter the name of a well-known DSCP class or a numeric value in decimal or hexadecimal format. Precede
                                       hexadecimal values with 0x or 0X.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The valid class names as defined by DSCP are:

Class Selector: values CS0, CS1, CS2, CS3, CS5, CS6, CS7

The class selector (CS) values correspond to IP Precedence values and are fully compatible with IP Precedence.

Expedited Forwarding: value EF

EF PHB is ideally suited for applications such as VoIP that require low bandwidth, guaranteed bandwidth, low delay, and low
                                    jitter.

Best Effort: value BE

Also called default PHB, this value essentially specifies that a packet be marked with 0x00, which gets

the traditional best-effort service from the network router.

Assured Forwarding: values AF11, AF12, AF13, AF21, AF22, AF23, AF41, AF42, AF43

There are four types of Assured Forwarding classes, each of which has three drop precedence values.

These precedence values define the order in which a packet is dropped (if needed) due to network

congestion. For example, packets in AF13 class are dropped before packets in the AF12 class.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set http min-version HTTP/1.1

This command sets HTTP/1.1 and later as the minimum protocol version for all the inbound HTTP requests.

set http min-version HTTP/1.1

### Command Modes

Administrator (admin:)

### Usage Guidelines

Ensure to restart the following services on all the nodes in the Unified Communications Manager cluster:

Cisco CallManager

Cisco TFTP

Cisco HAProxy

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Unity Connection

## set http min-version HTTP/2

This command sets HTTP/2 as the minimum protocol version for all the inbound HTTP requests.

set http min-version HTTP/2

### Command Modes

Administrator (admin:)

### Usage Guidelines

Warning

Local Push Notification Service (LPNS) utilizes web sockets exclusively over HTTP/1.1 and it will no longer function when
                                          the HTTP minimum version is set to HTTP/2.

Ensure to restart the following services on all the nodes in the cluster:

On the Unified Communications Manager:

Cisco CallManager

Cisco TFTP

Cisco HAProxy

On the IM and Presence Service:

Cisco Tomcat

Cisco Config Agent

Cisco XCP Config Manager

Cisco XCP Router

Cisco XCP Connection Manager

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Unity Connection

## set ipsec
                        	 policy_group

This command enables
                              		  ipsec policies with the specified policy group name.

set ipsec policy_group { ALL | group }

## Syntax Description

Enables all
                                       					 ipsec policy groups.

Specifies
                                       					 the name of a particular ipsec policy group to enable.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified
                                 			 Communications Manager and Cisco Unity Connection.

## set ipsec
                        	 policy_name

This command enables the specified IPSec policy.

set ipsec policy_name { policy_group | | policy_name }

## Syntax Description

Specifies the name of a particular ipsec policy group to enable.

Specifies the name of a particular ipsec policy to enable.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified
                                 			 Communications Manager and Cisco Unity Connection.

## set key regen authz encryption

Run this command on the Unified Communications Manager publisher node to regenerate the symmetric encryption key that encrypts
                              OAuth access tokens and refresh tokens that are used in Cisco Jabber authentication.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during upgrade: No

Applies to: Unified Communications Manager and the IM and Presence Service.

## set key regen authz signing

Run this command on the Unified Communications Manager publisher node to regenerate the asymmetric RSA key pair for signing
                              the OAuth access tokens and refresh tokens that are used in Cisco Jabber authentication.

### Command Modes

Administrator (admin:)

### Usage Guidelines

### Requirements

Command privilege level: 4

Allowed during upgrade: No

Applies to: Unified Communications Manager and the IM and Presence Service.

## set logging

This command allows
                              		  you to enable or disable CLI Admin logs.

set logging { enable | disable }

## Syntax Description

Turns on
                                       					 logging.

Turns off
                                       					 logging.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set Login Grace
                        	 Timeout

This command allows you to configure the LoginGraceTimeout value to
                              		  the mentioned value.

set Login Grace Timeout LoginGraceTimeout
                                 				  value

## Syntax Description

Sets the LoginGraceTimeout value for login grace timeout.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network cluster
                        	 publisher

This command sets
                              		  the network cluster publisher hostname and IP address.

set network cluster publisher { hostname | ip } name

## Syntax Description

Specifies
                                       					 the hostname of the network cluster.

Specifies the IP address of the network cluster.

Hostname or
                                       					 IP address to assign to the network cluster publisher.

### Command Modes

Administrator (admin:)

### Usage Guidelines

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Unity Connection.

## set  network cluster subscriber details

Use this command  to add subscriber to the processnode or appserver table when Tomcat Webserver is server down and GUI is
                              inaccessible.

set network cluster subscriber  details servertype hostname ip domainname

## Syntax Description

Parameter

Description

Choose one of these products for this parameter— Unified Communications Manager , IM and Presence Service, and Cisco Unity Connection. This field is mandatory.

The hostname of the node that you add to the cluster. The hostname is supported on the same domain. This field is mandatory.

The IPv4 address of the node that you add to the cluster. This field is mandatory for IM and Presence publisher and Cisco
                                       Unity Connection.

The domain name of the IM and Presence Service publisher. This field is mandatory for IM and Presence publisher.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to Unified Communications Manager, IM and Presence Service, and Cisco Unity Connection

## set network cluster subscriber dynamic-cluster-configuration

Use this command to enable the 
                              Dynamic Cluster Configuration
                              on the publisher.
                              Use this command to specify the duration in which you can add subscriber nodes to the publisher server table. The addition
                              of subscriber nodes is authenticated
                              immediately and those nodes need not wait for the publisher
                              details during the installation of the subscriber nodes.

set network cluster subscriber dynamic-cluster-configuration { default | no. of hours }

## Syntax Description

Enables the Dynamic Cluster Configuration for 24 hours.

Specifies  a value from 1 to 24 hours.

### Command Modes

Administrator (admin)

### Requirements

Applies to Unified Communications Manager, IM and Presence Service, and Cisco Unity Connection

## set network dhcp eth0

This command enables or disables DHCP for Ethernet interface 0. You cannot configure Ethernet interface 1.

set network dhcp eth0 { enable | disable } { node_ip | net_mask | gateway_ip }

## Syntax Description

Specifies Ethernet interface 0.

This enables DHCP.

This disables DHCP.

Represents the static IP address for the server.

Represents the subnet mask for the server.

Represents the IP address of the default gateway.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Caution

If you continue, this command causes the system to restart. We also recommend that you restart all nodes whenever any IP address
                                          gets changed.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 dns

This command sets
                              		  the IP address for the primary or secondary DNS server.

set network dns { primary | secondary } addr

## Syntax Description

Represents
                                       					 the IP address of the primary or secondary DNS server.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

If you change the IP address for the DNS servers, you must reboot the server through the utils system restart CLI command.

## set network dns options

This command sets DNS options.

set network dns options [ timeout | seconds ] [ attempts | number ] [ rotate ]

## Syntax Description

Sets the DNS timeout.

Sets the number of times to attempt a DNS request.

Causes the system to rotate among the configured DNS servers and distribute the load.

Specifies the DNS timeout period in seconds.

Specifies the number of attempts.

### Usage Guidelines

Running this command causes an automatic system restart.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 domain

This command sets
                              		  the domain name for the system.

Changing the domain name triggers an automatic regeneration of all Unified Communications Manager certificates, including
                                          any third party signed certificates that have been uploaded. After the server reboots automatically, phones running in secure
                                          (mixed) mode cannot connect to the server until after the CTL client updates the new CTL file to the phones.

Reboot the servers
                                          			 one at a time in order for the phones to register correctly. For more
                                          			 information about changing the domain name, see Changing the
                                             				IP Address and Hostname for Cisco Unified Communications Manager .

set network domain [domain-name]

## Syntax Description

Represents
                                       					 the system domain that you want to assign.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The system asks whether you want to continue to execute this command.

Caution

If you continue,
                                          			 this command causes a temporary loss of network connectivity.

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network failover

This command enables and disables Network Fault Tolerance on the Media Convergence Server network interface card.

set network failover { ena | dis }

## Syntax Description

Enables Network Fault Tolerance.

Disables Network Fault Tolerance.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network gateway

This command enables you to configure the IP address of the network gateway.

set network gateway addr

## Syntax Description

Represents the IP address of the network gateway that you want to assign.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The system asks whether you want to continue to execute this command.

Caution

If you continue, this command causes the system to restart.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

## set network
                        	 hostname

This command allows
                              		  an administrator to set the network host name, change the IP address of the
                              		  node, and restart the system.

Before attempting this command, the administrator should have a valid DRF backup. Additionally, before attempting a Hostname
                              (or Hostname and IP address) change, the administrator should perform the following:

verify the cluster configuration does not have any configuration problems by executing show hcs cluster verify detailed

update the cluster configuration by executing set hcs cluster config

validate the cluster configuration by executing show hcs cluster verify detailed

set network hostname hostname

## Syntax Description

Represents
                                       					 the new network hostname of the system.

The host
                                                   						name must follow the rules for ARPANET host names. It must start with an
                                                   						alphabetic character, end with an alphanumeric character, and consist of
                                                   						alphanumeric characters and hyphens. The host name can have a maximum length of
                                                   						63 characters.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The system asks
                              		  whether you want to continue to execute this command.

Caution

If you continue,
                                          			 this command causes the system to restart.

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set network hostname

WARNING: Changing this setting will invalidate software license
on this server. The license will have to be re-hosted.
Continue(y/n):
Continue (y/n)?y

ctrl-c: To quit the input.

*** W A R N I N G ***
Do not close this window without first canceling the command.

This command will automatically restart system services.
The command should not be issued during normal operating
hours.

=======================================================
Note: Please verify that the new hostname is a unique
name across the cluster and, if DNS services are
utilized, any DNS configuration is completed
before proceeding.
=======================================================

Security Warning : This operation will regenerate
all CUCM Certificates including any third party
signed Certificates that have been uploaded.

Enter the hostname:: app-lfwelty5
Would you like to change the network ip address at this time [yes]::

Warning: Do not close this window until command finishes.

ctrl-c: To quit the input.

***   W A R N I N G   ***
=======================================================
 Note: Please verify that the new ip address is unique 
       across the cluster.
 Note: Changing the IP address will automatically restart
       system services cluster wide.
 Note: The command should not be issued during normal operating hours.
=======================================================
```

## set network ip
                        	 eth0

This command sets
                              		  the IP address for Ethernet interface 0. You cannot configure Ethernet
                              		  interface 1.

Before attempting this command, the administrator should have a valid DRF backup. Also, before attempting an IP address change,
                              the administrator should perform the following:

verify that the cluster configuration does not have any configuration problems by executing show hcs cluster verify detailed

update the cluster configuration by executing set hcs cluster config

validate the cluster configuration by executing show hcs cluster verify detailed

set network ip eth0 addr mask gw

## Syntax Description

Specifies
                                       					 Ethernet interface 0.

Represents
                                       					 the IP address that you want to assign.

Represents
                                       					 the IP mask that you want to assign.

Represents the IP default GW that you want to assign.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The system asks
                              		  whether you want to continue to execute this command.

Caution

If you continue, this command restarts the following services:

NIC driver

NTP

CLM

Service Manager

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

### Example

```
admin:set network ip eth0
......

***   W A R N I N G   ***
=======================================================
Note:  Please verify that the new ip address is unique across the cluster
and, if DNS services are utilized, any DNS configuration is 
completed before proceeding.
Note: Changing the IP address will automatically restart
system services cluster wide.
Note: The command should not be issued during normal operating hours.
=======================================================
```

## set network ipv6
                        	 dhcp

This command sets
                              		  the DHCPv6 client on the server and enables IPv6 support. For changes to take
                              		  effect, you must restart the server.

set network ipv6 dhcp { enable | disable } [ reboot ]

## Syntax Description

Sets the
                                       					 DHCPv6 client on the server. By default, the server does not restart after you
                                       					 enable the DHCPv6 client. For your changes to take effect, you must restart the
                                       					 server by either entering the reboot parameter or manually restarting the
                                       					 server.

Enables IPv6
                                       					 support.

Disables
                                       					 IPv6 support.

(Optional)
                                       					 Causes the server to automatically restart after you enter the command.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

## set network ipv6
                        	 gateway

This command sets
                              		  the IPv6 gateway for the server. For changes to take effect, you must restart
                              		  the server.

set network ipv6 gateway addr [ reboot ]

## Syntax Description

Sets the
                                       					 IPv6 gateway for the server. By default, the server does not restart after you
                                       					 set the IPv6 gateway for the server. For your changes to take effect, you must
                                       					 restart the server by either entering the reboot parameter or manually
                                       					 restarting the server.

The IPv6
                                       					 gateway address.

(Optional)
                                       					 Causes the server to automatically restart after you enter the command.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

## set network ipv6
                        	 service

This command enables
                              		  or disables the IPv6 service on the server. For changes to take effect, you
                              		  must restart the server.

set network ipv6 service { enable | disable } [ reboot ]

## Syntax Description

Sets the
                                       					 IPv6 service on the server. By default, the server does not restart after you
                                       					 enable or disable the IPv6 service on the server. For your changes to take
                                       					 effect, you must restart the server by either entering the reboot parameter or
                                       					 manually restarting the server.

Enables IPv6
                                       					 service on the server.

Disables
                                       					 IPv6 service on the server.

(Optional)
                                       					 Causes the server to automatically restart after you enter the command.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

## set network ipv6
                        	 static_address

This command assigns
                              		  the static IPv6 address to the server. For changes to take effect, you must
                              		  restart the server.

set network ipv6 static_address addr mask [ reboot ]

## Syntax Description

Assigns a
                                       					 static IPv6 address to the server. By default, the server does not restart
                                       					 after you assign the static IPv6 address. For your changes to take effect, you
                                       					 must restart the server by either entering the reboot parameter or manually
                                       					 restarting the server.

Specifies
                                       					 the static IPv6 address you assign to the server.

Specifies
                                       					 the IPv6 network mask (0-128).

(Optional)
                                       					 Causes the server to automatically restart after you enter the command.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

## set network
                        	 max_ip_conntrack

This command sets
                              		  the ip_conntrack_max value.

set network max_ip_conntrack ip_conntrack_max value

## Syntax Description

Specifies
                                       					 the value for ip_conntrack_max.

The value
                                                   						of ip_conntrack_max cannot be less than 65536.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

### Example

```
admin:set network max_ip_conntrack 65536
```

## set network
                        	 mtu

This command sets
                              		  the maximum MTU value.

set network mtu mtu_max

## Syntax Description

Specifies
                                       					 the maximum MTU value. The system default MTU value equals 1500.

Caution

When
                                                   						packets on UDP port 8500 that have the DF bit set are exchanged between nodes,
                                                   						if there is any policy on the WAN router to clear the DF bit and fragment large
                                                   						packets, this may cause dbreplication issues.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The system asks whether you want to continue to execute this command.

Caution

If you continue,
                                          			 the system loses network connectivity temporarily.

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

### Example

```
admin:set network mtu 576      W A R N I N G
This will cause the system to temporarily lose network connectivity
     Do you want to continue ?
Enter "yes" to continue or any other key to abort
yes
executing...
```

## set network
                        	 name-service hosts cache-enable

This command
                              		  enables the nscd related cache.

set network name-service
                                 				  hosts cache-enable value

## Syntax Description

The
                                       					 boolean value must be either yes or no .

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service hosts max-db-size

This command sets
                              		  the maximum allowed size for a service.

set network name-service
                                 				  hosts max-db-size value

## Syntax Description

Enter the
                                       					 number of bytes for the database size.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service hosts negative-time-to-live

This command sets
                              		  the time-to-live (TTL) for negative entries or unsuccessful queries in the
                              		  specified cache for service. So, using this command improves the performance if
                              		  there are various files owned by user IDs (UIDs) and are unavailable in system
                              		  databases. For example, files that are available in the Linux kernel sources as
                              		  root. To reduce the cache coherency problems, the number of such files should
                              		  be kept to the minimum.

set network name-service
                                 				  hosts negative-time-to-live value

## Syntax Description

Enter the
                                       					 number of seconds.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service hosts persistent

This command
                              		  retains the content of the cache for service over server restarts. This command
                              		  is useful when paranoia mode is configured.

set network name-service
                                 				  hosts persistent value

## Syntax Description

Enter a
                                       					 value for a service.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service hosts positive-time-to-live

This command sets the time-to-live (TTL) for positive entries or
                              		  successful queries in the specified cache for service. Configure the value in
                              		  seconds. Larger values increase cache hit rates and reduce mean response times.
                              		  However, such values increase problems with cache coherence.

set network name-service
                                 				  hosts positive-time-to-live value

## Syntax Description

Enter the number of seconds.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service hosts suggested-size

This command changes the internal hash table size.

set network name-service
                                 				  hosts suggested-size value

## Syntax Description

Enter a prime number for optimum efficiency.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service services cache-enable

This command enables the nscd related cache.

set network name-service
                                 				  services cache-enable value

## Syntax Description

The boolean value must be either yes or no .

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service services max-db-size

This command sets the maximum allowed size for the service.

set network name-service
                                 				  services max-db-size value

## Syntax Description

Enter the value in number of bytes.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service services negative-time-to-live

This command sets
                              		  the time-to-live (TTL) for negative entries or unsuccessful queries in the
                              		  specified cache for service. So, using this command improves the performance if
                              		  there are various files owned by user IDs (UIDs) and are unavailable in system
                              		  databases. For example, files that are available in the Linux kernel sources as
                              		  root. To reduce the cache coherency problems, the number of such files should
                              		  be kept to the minimum.

set network name-service
                                 				  services negative-time-to-live value

## Syntax Description

Enter a prime number for optimum efficiency.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service services persistent

This command retains the content of the cache for service over server
                              		  restarts. This command is useful when paranoia mode is configured.

set network name-service
                                 				  services persistent value

## Syntax Description

Enter a value for a service.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service services positive-time-to-live

This command sets the time-to-live (TTL) for positive entries or
                              		  successful queries in the specified cache for service. If you enter a large
                              		  value for this command, it increases cache hit rates and reduces mean response
                              		  times. However, a large value increases issues with cache coherence.

set network name-service
                                 				  services positive-time-to-live value

## Syntax Description

Enter the number of seconds.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service services suggested-size

This command sets the internal hash table size.

set network name-service
                                 				  services suggested-size value

## Syntax Description

Enter a prime number for optimum efficiency.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network nic eth0

This command sets the properties of the Ethernet Interface 0. You cannot configure Ethernet interface 1.

set network nic eth0 { auto |  { en | dis }} { speed |  { 10 | 100 }} { duplex half |  { half | full }}

## Syntax Description

Specifies Ethernet interface 0.

Specifies whether auto negotiation gets enabled or disabled.

Specifies whether the speed of the Ethernet connection: 10 or 100 Mb/s.

Specifies half-duplex or full-duplex.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The system asks whether you want to continue to execute this command.

You can enable only one active NIC at a time.

Caution

If you continue, this command causes a temporary loss of network connections while the NIC gets reset.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

## set network ntp
                        	 option

This command adds the noquery option to the /etc/config file.

set network ntp
                                 				  option

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network pmtud
                        	 state

This command enables
                              		  and disables Path MTU Discovery.

set network pmtud state { enable | disable }

## Syntax Description

Enables Path
                                       					 MTU Discovery.

Disables
                                       					 Path MTU Discovery.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The system asks whether you want to continue to execute this command.

Caution

If you continue,
                                          			 the system loses network connectivity temporarily.

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection.

### Example

```
admin:set network pmtud state enable      W A R N I N G
This will cause the system to temporarily lose network connectivity
     Do you want to continue ?
Enter "yes" to continue or any other key to abort
yes
executing...
```

## set network restore

This command configures the specified Ethernet port to use a specified static IP address.

set network restore eth0 ip-address network-mask gateway

## Syntax Description

Specifies Ethernet interface 0.

Represents the IP address of the primary or secondary DNS server, or the network gateway that you want to assign. If you continue,
                                       this command causes a temporary loss of network connectivity. If you change the IP address for the primary DNS server, you
                                       must also restart the Cisco Tomcat service. For more information, see the utils service command. We also recommend that you restart all nodes whenever any IP address gets changed.

Represents the subnet mask for the server.

Specifies the IP address of the default gateway.

Represents the IP address of the primary or secondary DNS server, or the network gateway that you want to assign. If you continue,
                                       this command causes a temporary loss of network connectivity. If you change the IP address for the primary DNS server, you
                                       must also restart the Cisco Tomcat service. For more information, see the utils service command. We also recommend that you restart all nodes whenever any IP address gets changed.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Caution

Only use this command option if you cannot restore network connectivity through any other set network commands. This command
                                          deletes all previous network settings for the specified network interface, including Network Fault Tolerance. After you run
                                          this command, you must restore your previous network configuration manually.

Caution

The server temporarily loses network connectivity after you run this command.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set network restore eth0   10.94.150.108   255.255.255.0   10.94.150.1
```

## set network status eth0

This command sets the status of Ethernet 0 to up or down. You cannot configure Ethernet interface 1.

set network status eth0 { up | down }

## Syntax Description

Specifies Ethernet interface 0.

Sets the status of Ethernet interface 0 to up.

Sets the status of Ethernet interface 0 to down.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The system asks whether you want to continue to execute this command.

Caution

If you continue, the system loses network connectivity temporarily.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set network
                        	 name-service

This command
                              		  displays name service cache attributes.

set network name-service [ attribute ] [ value ]

## Syntax Description

Bool must
                                       					 be either Yes or No. Enabling paranoia mode causes Name Service to restart
                                       					 itself periodically.

If level
                                       					 is higher than 0, Name Service will create some debug output. Higher the level,
                                       					 more verbose the output.

Sets the
                                       					 number of times a cached record is reloaded before it is pruned from the cache.
                                       					 Each cache record has a timeout. When that timeout expires Name Service will
                                       					 either reload it (query the NSS service again if the data hasn't changed) or
                                       					 drop it.

Sets the
                                       					 restart interval to time seconds if periodic restart is enabled by enabling
                                       					 paranoia mode. The default value is 3600.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

## set password
                        	 complexity minimum-length

This command modifies the value of minimum password length for the OS administration accounts.

Use this command after you enable the character complexity of
                                          			 passwords.

set password complexity
                                 				  minimum-length max-repeat

## Syntax Description

Enter a value of or greater than six .

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password
                        	 age

This command modifies the value for
                              		  password age, in days, for Cisco Collaboration Communication OS (C3OS)
                              		  accounts.

set password age { maximum | minimum } days

## Syntax Description

Specifies
                                       					 the maximum age.

Specifies
                                       					 the minimum age.

Specifies
                                       					 the maximum password age and must be greater-than or equal-to 90 days.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password change-at-login

Use this command to force new or existing users to change their password when they sign in to the system the next time.

set password change-at-login { disable | enable } userid

## Syntax Description

This does not force users to change their password.

This forces users to change their password when they sign in to the system the next time.

Specifies the affected user account.

### Command Modes

Administrator (admin:)

### Usage Guidelines

By default, this command is enabled for new users, so users have to change their password the first time they sign in to the
                              system.

### Requirements

Command privilege level: 4

Allowed during upgrade: No

Applies to: IM and Presence Service on Unified Communications Manager only.

## set password complexity character

Use this command to enable or disable password complexity rules for the type of characters in a password.

After you enable password complexity, this command also enables password history if it has not already been enabled (for more
                                          information, see the set password history command). If you had not previously enabled password history, the password history number parameter value gets set to 10.
                                          If you previously enabled password history with a value of less than 10, the value gets reset to 10 after you execute this
                                          command. If you previously enabled password history with a value of 10 or greater, the value remains unchanged after you execute
                                          this command.

set password complexity character { disable | enable } num-char

## Syntax Description

This turns off password complexity for character types.

This turns on password complexity for character types.

When you disable password complexity, you also turn off password character difference , password character max-repeat , and password history .

This specifies the number of characters required from each of the four character sets: lowercase, uppercase, numbers, and
                                       special characters.

Value range: 0-8

Default value: 1

### Command Modes

Administrator (admin:)

### Usage Guidelines

When you enable password complexity, you must follow these guidelines when you assign a password:

It must have at least the current setting, num-chars, of lower-case character.

It must have at least the current setting, num-chars, of uppercase characters.

It must have at least the current setting, num-chars, of digit characters.

It must have at least the current setting, num-chars, of special characters.

You cannot use adjacent characters on the keyboard; for example, qwerty.

You cannot reuse any of the previous passwords that match the passwords retained by password history.

By default, the admin user password can be changed only once in a 24-hour day.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password complexity character difference

This command specifies the number of characters that the character sequence in a new password must differ from the character
                              sequence in the old password.

set password complexity character difference num-char

## Syntax Description

This specifies the number of characters that the character sequence in a new password must differ from the character sequence
                                       in the old password.

Value range: 0-31

### Command Modes

Administrator (admin:)

### Usage Guidelines

Enter 0 to indicate no difference.

The maximum password length is 31 characters.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password complexity character max-repeat

This command specifies the number of times you can consecutively repeat a single character in a new password.

set password complexity character max-repeat max-repeat

## Syntax Description

This specifies the number of times you can consecutively repeat a single character in a new password.

Value range: 0 – 10

Default value: 0

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password expiry
                        	 maximum-age

This command enables or disables the
                              		  password expiry maximum age settings for Cisco Collaboration Communication OS
                              		  (C3OS) Administrator accounts.

set password expiry maximum-age { enable | disable }

## Syntax Description

Turns on
                                       					 password expiry maximum age settings for Cisco Unified Operating System
                                       					 administrator accounts. The set password expiry enable command sets the value
                                       					 of maximum password age to 3650 days (10 yrs) for Cisco
                                       					 Unified Operating System Administrator accounts.

Turns off
                                       					 password expiry maximum age settings for Cisco Unified Operating System
                                       					 administrator accounts. The set password expiry disable command results in
                                       					 Cisco Unified Operating System Administrator accounts never expiring.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set password expiry maximum-age disable
Operation Successful.
```

## set password
                        	 expiry user maximum-age configure

This command modifies the value of the maximum password age for a
                              		  particular Cisco Collaboration Communication OS Administration account in days.

set password expiry user maximum-age
                                 				  configure userid maximum password
                                 				  age

## Syntax Description

Enter Cisco Collaboration Communication OS (C3OS)
                                       					 Administrator account.

Enter the maximum password age in days. This value must be
                                       					 equal to or greater than 10 days but less than 3650 days (10 years).

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password expiry
                        	 minimum-age

This command enables
                              		  or disables the password expiry minimum age settings for Cisco Unified
                              		  Operating System Administrator accounts.

set password expiry minimum-age { enable | disable }

## Syntax Description

Turns on password expiry
                                       					 minimum age settings for Cisco Unified Operating System administrator accounts.
                                       					 The set password expiry enable command sets the value of minimum password age
                                       					 to one day (24 hrs) for Cisco Collaboration Communication OS (C3OS)
                                       					 Administrator accounts.

Turns off password expiry
                                       					 minimum age settings for Cisco Collaboration Communication OS (C3OS)
                                       					 administrator accounts. This means that passwords for administrator accounts
                                       					 can be changed at any interval.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set password expiry minimum-age disable
Operation Successful.
```

## set password expiry
                        	 user maximum-age

This command
                              		  disables the maximum age password expiry for a particular Cisco Unified
                              		  Operating System Administrator account.

set password expiry user maximum-age { enable | disable } userid

## Syntax Description

Turns on the maximum age
                                       					 password expiry settings for a particular Cisco Collaboration Communication OS
                                       					 (C3OS) administrator account. The set password expiry user enable command sets
                                       					 the value of maximum password age to 3650 days (10 yrs) for the Cisco Unified
                                       					 Operating System Administrator account.

Turns on the maximum age
                                       					 password expiry settings for a particularCisco Collaboration Communication OS
                                       					 (C3OS) administrator account. The set password expiry user enable command sets
                                       					 the value of maximum password age to 3650 days (10 yrs) for the Cisco Unified
                                       					 Operating System Administrator account.

Specifies a particular Cisco
                                       					 Collaboration Communication OS (C3OS) Administrator account.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set password expiry user maximum-age enable
Operation Successful.
```

## set password expiry user minimum-age

This command enables or disables the maximum age password expiry for a particular Cisco Unified Operating System Administrator
                              account.

set password expiry user minimum-age { enable | disable } userid

## Syntax Description

Turns on the minimum age password expiry  settings for a particular Cisco Unified Operating System administrator account.

Turns off the minimum age password expiry  settings for a particular Cisco Unified Operating System administrator account.

Specifies a particular Cisco Unified Operating System Administrator account.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:set password expiry user minimum-age disable
Operation Successful.
```

## set password history

This command modifies the number of passwords that get maintained in the history for OS admin accounts. New passwords matching
                              remembered passwords get rejected.

set password history number

## Syntax Description

Specifies the mandatory number of passwords to maintain in history.

### Command Modes

Administrator (admin:)

### Usage Guidelines

To disable, enter 0.

Default specifies 10.

Upper limit specifies 20.

### Requirements

Command privilege level:  1

Allowed during upgrade:  Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password
                        	 inactivity

set password inactivity { enable | disable | period } days

## Syntax Description

Enable the
                                       					 password inactivity globally and update individual OS users according to the
                                       					 setting.

Disable the
                                       					 password inactivity globally and update individual OS users according to the
                                       					 setting.

Configure
                                       					 the password inactivity period globally and update individual OS users
                                       					 according to the setting.

Specify the
                                       					 number of days of inactivity after a password has expired before the account
                                       					 gets disabled. Valid range is 1 - 99.

### Command Modes

Administrator (admin:)

### Usage Guidelines

To enable password inactivity globally, execute the set password inactivity enable command. This command enables the password
                                    inactivity globally and updates individual OS users according to the setting.

To disable password inactivity globally, execute the set password inactivity disable command. This command disables the password
                                    inactivity globally and updates individual OS users according to the setting.

A user whose account is disabled must contact the system administrator to use the system again.

To configure the password inactivity period execute the set password inactivity period days command. This command configures
                                    the password inactivity globally and updates individual OS users according to the setting.

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password
                        	 system bootloader encryptHash

Use this command to configure the encrypted password in the grub.conf file for the system boot loader.

set password system bootloader
                                 				  encryptHash

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password user admin

This command allows you to change the administrator password.

set password user admin

### Command Modes

Administrator (admin:)

### Usage Guidelines

The systems prompts you for the old and new passwords.

You can change the password only for the administrator account that you logged in to.

The password must contain at least six characters, and the system checks it for strength.

### Requirements

Command privilege level:  1

Allowed during upgrade:  No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set password user
                        	 security

This command allows
                              		  you to change the security password.

set password user security

### Command Modes

Administrator (admin:)

### Usage Guidelines

The systems prompts you for the old and new passwords.

The password must contain at least six characters, and the system checks it for strength.

Servers in a cluster
                              		  use the security password to authenticate communication between servers. You
                              		  must reset the cluster after you change the security password.

We recommend that you restart each server after the password is changed on that server.

Change the security password on the publisher server (first node) and then reboot the server (node).

Change the security password on all the subsequent servers and nodes to the same password that you created on the first node
                                                and restart subsequent nodes, including application servers, to propagate the password change.

Failure to reboot the servers
                                          			 (nodes) causes system service problems and problems with the Cisco
                                          			 Collaboration Communication OS (C3OS) Administration windows on the subscriber
                                          			 servers.

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## Set replication-sync monitor

This command enables or disables replication monitoring by the Cisco Replication Watcher service. The Cisco Replication Watcher
                              service blocks other services from starting until database replication is setup and functioning normally.

set replication-sync monitor {enable | disable}

## Syntax Description

Turns on the replication monitoring service.

Turns off the replication monitoring service

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: IM and Presence Service on Unified Communications Manager only

## set samltrace
                        	 level

This command sets
                              		  the SAML trace level.

set samltrace level trace
                                 				  level

## Syntax Description

Specifies the trace level. The available options are:

DEBUG

INFO

WARNING

ERROR

FATAL

The
                                                   						default trace level is INFO.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set session
                        	 maxlimit

This command sets
                              		  the upper limit for concurrent sessions.

set session maxlimit [value]

## Syntax Description

This command sets the upper limit for concurrent sessions. Acceptable values are 1 - 10.

If no upper
                                       					 limit is entered, the default value of 10 is assigned to sshd_config param.

Acceptable values are 1 - 10.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set sip-trunkbusyout disable

This command makes all SIP Trunks respond to the OPTIONS request message with a success (200 OK) message, provided there are
                              no other error conditions. This is a cluster-wide command. A Cisco CallManager Service restart is not necessary.

set sip-trunkbusyout disable

### Requirements

Command privilege level: 1

Applies to: Unified Communications Manager

### Example

```
admin:set sip-trunkbusyout disable
Warning: This command has no impact if OPTIONS ping/keepalive is not enabled
in your deployment. Proceed with this operation(yes|no)? yes
```

## set sip-trunkbusyout enable

This command makes all the SIP trunks respond to the OPTIONS request message with a ‘503 Service Unavailable’ error. This
                              is a cluster-wide command. A Cisco CallManager service restart is not necessary.

set sip-trunkbusyout enable

### Requirements

Command privilege level: 1

Applies to: Unified Communications Manager

### Example

```
admin:set sip-trunkbusyout enable
This command makes all the SIP Trunks respond to the OPTIONS request
message with a '503 Service Unavailable error. This is a clusterwide command.
A Cisco CallManager service restart is not necessary.
********************************************************************
Warning: If OPTIONS Keepalive/Ping is enabled for peer SIP clients 
such as Unified CM, IM and Presence Service, Cisco Unified Border 
Element, or Unity Connection, activating this configuration renders 
the SIP Trunk for this cluster non-operational on those peers. This 
may result in call failures, call rerouting, and other operational 
impacts. Existing calls continue to be active until it is terminated. 
This command has no impact if OPTIONS ping/keepalive is not enabled 
in your deployment.
********************************************************************
Proceed with this operation(yes|no)? yes
```

## set smtp

This command sets the SMTP server hostname.

set smtp hostname

## Syntax Description

Represents the SMTP server name.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set strace enable

This command enables the service trace and sets the trace level.

set strace enable [all] tracevalue servicename

## Syntax Description

Optional parameter to propagate the service trace settings change to all nodes.

Represents allowed trace values. Allowed trace values are [Info|Debug|Warn|Error|Fatal]

Represents the service for which the trace is enabled.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Unified Communications Manager and IM and Presence Service on Unified Communications Manager

## set strace disable

This command disables the service trace.

set strace disable [all] servicename

## Syntax Description

Optional parameter to propagate the service trace settings change to all nodes.

Represents the service for which the trace is enabled.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Unified Communications Manager and IM and Presence Service on Unified Communications Manager

## set timezone

This command lets
                              		  you change the system timezone.

set timezone zone

## Syntax Description

Specifies
                                       					 the new timezone. Enter the appropriate string or zone index id to uniquely
                                       					 identify the timezone. To view a list of valid timezones, use the CLI command: show timezone
                                             						  list .

### Command Modes

Administrator (admin:)

### Usage Guidelines

Enter characters to uniquely identify the new timezone. Be aware that the timezone name is case-sensitive.

Caution

You must restart
                                          			 the system after you change the timezone.

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example Setting
                              		  Timezone to Pacific Time

```
admin:set timezone Pac
```

## set tls min-version

This command sets the minimum version of the Transport Layer Security (TLS) protocol.

Until Release 15SU2, ensure that you configure the minimum TLS version for each node. After you set the minimum TLS version,
                                                the system reboots.

set tls min-version tls minVersion

## Syntax Description

Type one of the following options to set it as the minimum TLS version:

1.0

1.1

1.2

### Command Modes

Administrator (admin:)

### Usage Guidelines

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and IM and Presence Service on Unified Communications Manager

### Example

```
admin: set tls min-version 1.1

This command will result in setting minimum TLS version to 1.1 on all the secure interfaces.
If you have custom applications that makes secure connection to the system, please ensure 
they support the TLS version you have chosen to configure. 
Also, please refer to the Cisco Unified Reporting Administration Guide to ensure the 
endpoints in your deployment supports this feature.

****************************************************************************************************

Warning: This will set the minimum TLS to 1.1 and the server will reboot.

****************************************************************************************************

Do you want to continue (yes/no) ? yes

Successfully set minimum TLS version to 1.1

The system will reboot in few minutes.
```

## set trace disable

This command unsets trace activity for the specified task.

set trace disable tname

## Syntax Description

Unsets the task trace settings.

Represents the task for which you want to disable traces.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set trace enable

This command sets trace activity for the specified task.

set trace enable { Arbitrary | Detailed | Entry_exit | Error | Significant | Special | State_Transition } tname

## Syntax Description

Sets task trace settings to the arbitrary level.

Sets task trace settings to the detailed level.

Sets task trace settings to the entry_exit level.

Sets task trace settings to the error level.

Sets task trace settings to the significant level.

Sets task trace settings to the special level.

Sets task trace settings to the state transition level.

Represents the task for which you want to disable traces.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set
                        	 tlsresumptiontimeout

This command sets the number of seconds after which TLS resumption
                              		  will not work and sessions are invalidated.

set tlsresumptiontimeout seconds

## Syntax Description

Enter a value up to 3600 seconds. The TLS sessions are invalid
                                       					 after the configured value.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set
                        	 tlstrace*

Unified Communications Manager Release 11.0 onwards, you can enable or disable TLS tracing for services. Currently, Tomcat is the only supported service.
                              Use the CLI commands to view the reasons of connection failure of TLS connections to Unified Communications Manager .

Following TLS-based CLI commands are added for TLS tracing:

### set tlstrace
                           	 disable

This CLI command
                                 		  disables the TLS tracing for a service.

set tlstrace disable service

## Syntax Description

Specifies
                                          					 the service that you use to disable TLS tracing.

#### Command Modes

Administrator (admin:)

#### Example

```
admin:set tlstrace disable tomcat
TLS tracing is disabled for: tomcat
```

#### Requirements

Command privilege
                                 		  level: 1

Allowed during
                                 		  upgrade: No

### set tlstrace
                           	 enable

This CLI command
                                 		  enables the TLS tracing for a service.

set tlstrace enable service

## Syntax Description

Specifies
                                          					 the service that you use to enable TLS tracing.

#### Command Modes

Administrator (admin:)

#### Example

```
admin:set tlstrace enable tomcat
TLS tracing is enabled for: tomcat
```

#### Requirements

Command privilege
                                 		  level: 1

Allowed during
                                 		  upgrade: No

## set web-security

This command sets the web security certificate information for the operating system.

set web-security orgunit orgname locality state [country] [alternatehostname]

## Syntax Description

Represents the organizational unit (OU) name.

You can use this command to enter multiple organizational units. To enter more than one organizational unit name, separate
                                       the entries with a comma. For entries that already contain a comma, enter a backslash before the comma that is included as
                                       part of the entry. To enter multiple values for organizational unit, enclose them in quotation marks, as shown in the example
                                       for this command.

For OU’s that already contains a backslash, do not enter one more backslash as SLM registration and CSR generation fails during
                                                   the time of installation.

Represents the organizational name.

Represents the organization location.

Represents the organization state.

(Optional) Represents the organization country.

(Optional) Specifies an alternate name for the host when you generate a web-server (Tomcat) certificate.

You can use alternatehostname to set subject alternate hostname for self signed certificates. Subject alternate hostname for
                                       CSR is defined in the Certificate Management page. If you have set the alternate hostname for CSR using this command, the
                                       CSR generation process replaces the set alternate hostname.

### Command Modes

Administrator (admin:)

### Usage Guidelines

In case you are planning to rebuild the Unified CM server, ensure that you should use the same OU subject parameters. Else,
                              this will create discrepancies when you execute the command show web-security . This is because the platformConfig.xml file will not have the saved parameters information provided before the rebuild as
                              this file is not backed up during DRS backup.

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

This example shows the web-security command with multiple organizational unit names using comma separators. The certificate
                              has three OU fields:

OU=accounting

OU=personnel, CA

OU=personnel, MA

```
admin:set web-security “accounting,personnel\,CA,personnel\,MA” Cisco Milpitas
CA
set web-security "Voice\Video" "Cisco" "RTP" NC
```

## set webapp session timeout

This command sets the time, in minutes, that can elapse before a web application, such as Unified Communications Manager Administration, times out and logs off the user.

For the new webapp session timeout setting to become effective, you must restart the Cisco Tomcat service. Until you restart
                              the Cisco Tomcat service, the show webapp session timeout command reflects the new values, but system continues to use and reflect the old values. This command prompts you to restart
                              the service.

Caution

Restarting the Cisco Tomcat service ends all active sessions and can affect system performance. Cisco recommends that you
                                          only execute this command during off-peak traffic hours.

This setting gets preserved through a software upgrade and does not get reset to the default value.

set webapp session timeout minutes

## Syntax Description

Specifies the time, in minutes, that can elapse before a web application times out and logs off the user.

Value range: 5-99999 minutes

Default value: 30 minutes

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## set webapp session
                        	 maxlimit

This command sets the maximum limit for concurrent web application sessions per user. This applies to the following interfaces:

Cisco Unified CM Administration

Cisco Unified Serviceability

Cisco Unified Reporting

Cisco Unified Communications Self Care Portal

Cisco Unified CM IM and Presence Administration

Cisco Unified IM and Presence Serviceability

Cisco Unified IM and Presence Reporting

For the session maximum limit setting to become effective, the administrator must restart the Cisco Tomcat service.

Caution

Restarting the
                                          			 Cisco Tomcat service ends all active sessions and can affect the system
                                          			 performance. Cisco recommends that you only execute this command during
                                          			 off-peak traffic hours.

This setting
                                          			 gets preserved through a software upgrade and does not get reset to the default
                                          			 value.

set webapp session maxlimit number

## Syntax Description

Specifies the number to limit the concurrent web application sessions.

The value
                                       					 ranges from 1 to 10.

Default
                                       					 value is 10.

If the utils EnhancedSecurityMode is
                                       					 enabled, then the session limit is restricted to 3. For more details on how to
                                       					 Configure Enhanced Security Mode, see the "FIPS
                                          						140-2 Mode Setup" chapter in the Security Guide for Cisco Unified Communications Manager, Release
                                          						11.5(1)SU1 at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

When you exceed the defined sign-in sessions maximum limit, then the interface sign-in page displays the Logon Status message
                                                         as: The Session limit has already been reached for <username>. Please logout from those sessions or wait 30 minutes for inactive
                                                            sessions to be automatically closed.

When Enhanced Security Mode is enabled, then the
                                                         							 session limit is restricted to 3. However, Administrator can change the session
                                                         							 limit using the set webapp session maxlimit command to any value ranging from 1 to 10.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 4

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager, Unified Communications Manager IM and Presence Service and Cisco Unity Connection.

This example details on how to set webapp session maxlimit to 4:

```
admin:set webapp session maxlimit 4

***********************************W A R N I N G**************************************
The Cisco Tomcat service needs to be restarted for the changes to take effect.This will
disconnect active web sessions and all web applications on this node will be unavailable
until the service restarts.This service restart will take several minutes to complete.
Do you want to continue (yes/no) ? yes

*************Restarting Tomcat***************
Service Manager is running
Cisco Tomcat[STOPPING]
Cisco Tomcat[STOPPING]
Cisco Tomcat[STOPPING]
Cisco Tomcat[STOPPING]
Cisco Tomcat[STARTING]
Cisco Tomcat[STARTING]
Cisco Tomcat[STARTED]
The webapp session limit has been successfully set to 4.
```

This example details on how to enable utils EnhancedSecurityMode :

```
admin:utils EnhancedSecurityMode enable

The system is operating in NON-FIPS and NOT operating in Enhanced Security Mode.

Enhanced Security Mode can be enabled only when the system is operating in FIPS mode
Do you wish to enable  FIPS mode as well (yes/no) ? yes

Warning : This operation will modify the password policies

1)Password Length should be between 14 to 127 characters.
2)Password should have at least 1 lowercase, 1 uppercase, 1 digit and 1 special character.
3)Any of the previous 24 passwords cannot be reused.
4)Minimum age of the password is 1 day and Maximum age of the password is 60 days.
5)Any newly generated password's character sequence will need to differ by at least 4 characters from the old password's character sequence. Warning : This mode will limit the total number of concurrent web application sessions to 3. *****************************************************************
This will change the system to Enhanced Security Mode and will reboot
*****************************************************************
Do you want to continue (yes/no) ? yes
The protocol for communication with remote syslog server is already set to tcp. No changes required.

The system is already operating in contact search authentication enable mode; no change required. Exiting. The concurrent web application session limit has been successfully set to 3. Setting password restrictions as part of Enhanced Security Mode enable

Calling fips enable

Security Warning : The operation will regenerate certificates for

1)CallManager
2)Tomcat
3)IPsec
4)TVS
5)CAPF
6)SSH
7)ITLRecovery

Any third party CA signed certificates that have been uploaded for the above
components will need to be re-uploaded.
If the system is operating in mixed mode, then the CTL client needs to be run
again to update the CTL file.
If there are other servers in the cluster, please wait and do not change the
FIPS settings on any other node until the FIPS operation on this node is complete
and the system is back up and running.
*********************************************************************************
This will change the system to FIPS mode and will reboot.
*********************************************************************************
```

## set
                        	 workingdir

This command sets
                              		  the working directory for active, inactive, and installation logs.

set workingdir { activelog | inactivelog | tftp } directory

## Syntax Description

Sets the
                                       					 working directory for active logs. Choose a valid sub-directory of activelog.

Set the
                                       					 working directory for inactive logs. Choose a valid sub-directory of
                                       					 inactivelog.

Sets the
                                       					 working directory for TFTP files.

Represents
                                       					 the current working directory.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

| Parameters | Description |
|---|---|
| user-id | Specifies
                                       					 the user ID of the account that was disabled. |

| Parameters | Description |
|---|---|
| name | Represents
                                       					 the username for the new account. Enter a name comprised of only alphabets or characters comprised of alphanumeric characters (a-z, A-D, 0-9). Note Umlaut characters are not supported. | Note | Umlaut characters are not supported. |
| Note | Umlaut characters are not supported. |

| Note | Umlaut characters are not supported. |
|---|---|

| Note | The administrator account that the system creates during Unified Communications Manager installation has a privilege level of 4. The administrator can run all commands in the CLI. |
|---|---|

| Note | Only the Level 4 administrator has privileges to run all the CLI commands. The administrator must ensure to perform the following tasks: Type either 'Yes' or 'No' for the 'Allow this User to login to SAML SSO-enabled system through Recovery URL ? (Yes / No)' prompt. If this prompt value is blank, an error message appears. Type a value for the 'To authenticate a platform login for SSO, a Unique Identifier (UID) must be provided that identifies this user to LDAP (such
                                                   as sAMAccountName or UPN). Please enter the appropriate LDAP Unique Identifier (UID) for this user:[UID]' prompt. If the prompt value is duplicate, an error message appears. You can hit the Enter key and then, the user account
                                                name is saved by default. After the account is created successfully, the administrator will see the message Account created successfully. Log in to the CLI and update the password before you log in to OS Administration. In the case of SAML SSO login for Operating System Admin pages, if LDAP user consists of ' & ' character, make sure you create platform user without ' & ' and then map to LDAP user consisting of ' & ' character. In the case of SAML SSO login for Operating System Admin pages, if LDAP attribute value for User ID is telephonenumber, make
                                                sure you create platform user using consisting of alphanumeric characters or English alphabets only. Do not include platform
                                                user name with only numeric values. Then, map to the appropriate LDAP user having the UID value as telephone number. |
|---|---|

| Parameters | Description |
|---|---|
| enable | Enable
                                       					 account locking. |
| disable | Disable
                                       					 account locking. |

| Note | After you run this command with enable , the system automatically enables account lockout notification after the system enables the audit logging function. When the Administration account locking feature is enabled, and the user enters the wrong password more than the accountlocking
                                          count, the account gets locked for a set period. The message that the account is locked is only seen on the VM console and
                                          secure logs. |
|---|---|

| Parameters | Description |
|---|---|
| attempts | Represents the number of consecutive sign-in attempts before the system locks the account. Value Range: 2-5 Default value: 3 |

| Note | This command is only valid when account locking is enabled. If account locking is disabled, the system does not remember the
                                       account locking value and uses the default value, 3, after you enable account locking. |
|---|---|

| Parameters | Description |
|---|---|
| seconds | Specifies the unlock time in seconds. Value Range: 30-3600 Default value: 300 |

| Note | The account gets automatically unlocked only after the configured unlock time. This command is only valid when account locking is enabled. If account locking is disabled, the system does not remember the
                                                account locking unlock time and uses the default value, 300, after you enable account locking. |
|---|---|

| Note | By default, the platform administrator Level 4 has access to the recovery URL. If the platform administrator Level 4 attempts
                                          to update the recovery URL access for own self, an error appears. |
|---|---|

| Parameters | Description |
|---|---|
| enable | Enable the recovery sign-in option for platform administrators. |
| disable | Disable the recovery sign-in option for platform administrators. |
| userid | Specifies a particular Cisco Unified Operating System Administrator account. |

| Note | If you enable or disable the recovery sign-in option, which is already enabled or disabled, an error appears. The administrator account that the system creates when Unified Communications Manager installs has a privilege level of 4.
                                                The administrator can run all commands in the CLI. |
|---|---|

| Parameters | Description |
|---|---|
| userid | Specifies a particular Cisco Unified Operating System Administrator account whose unique identifier value needs to be updated. |

| Note | When you run the set account ssouidvalue userid command, a prompt appears to provide the UID value. If the UID value is blank, then samaccountname is saved as ssouidvalue
                                                by default. If a duplicate UID value exists, an error appears. |
|---|---|

| Parameters | Description |
|---|---|
| unit | Represents the unit name. |

| Parameters | Description |
|---|---|
| export | Exports all the available certificates for this unit in this cluster to the preconfigured SFTP location. |
| unit | Represents the unit name. |

| Parameters | Description |
|---|---|
| unit | Represents the unit name. |

| Note | Please ensure that you are executing this command from the Unified Communications Manager publisher node. The default CA certificate names can be obtained by executing the show cert default-ca-list command. |
|---|---|

| Parameters | Description |
|---|---|
| all | Deletes all the default CA certificates from all servers in the cluster. |
| common-name | Deletes the particular default CA certificate from all servers in the cluster. |

| Note | Please ensure that you are executing this command from the Unified Communications Manger publisher node. The default CA certificate names can be obtained by executing the show cert default-ca-list command. |
|---|---|

| Parameters | Description |
|---|---|
| all | Enables all the default CA certificates on all servers in the cluster. |
| common-name | Enables the particular default CA certificate on all servers in the cluster. |

| Parameters | Description |
|---|---|
| unit | Specifies the name of the trust category, as "own" or "trust" . |
| name | Certificate file name. |

| Parameters | Description |
|---|---|
| type | Specifies
                                       					 the certificate type as "own" or "trust" . |
| name | Represents
                                       					 the unit name. |
| [caCert] | Represents
                                       					 the name of the CA certificate file name. |

| Parameters | Description |
|---|---|
| name | Represents the unit name. |

| Parameters | Description |
|---|---|
| ITLRecovery | Represents the ITLRecovery certificate. |

| Caution | You must restart the services related to ITLRecovery for the
                                          			 regenerated certificates to become active. |
|---|---|

| Parameters | Description |
|---|---|
| on | Turns pagination on. |
| off | Turns pagination off. |

| Parameters | Description |
|---|---|
| minutes | Specifies the time, in minutes, that can elapse before an active CLI session times out and disconnects. Value range: 5-99999 minutes Default value: 30 minutes |

| Note | This setting gets preserved through a software upgrade and does not get reset to the default value. |
|---|---|

| Parameters | Description |
|---|---|
| enable | Turns on command count. |
| disable | Turns off command count. |

| Parameters | Description |
|---|---|
| name | Specifies
                                       					 the unit on which the certificate is generated. |

| Parameters | Description |
|---|---|
| enable | Enables the error log on the Jetty server. Be aware that enable is case sensitive. |
| disable | Disables the error log on the Jetty server. Be aware that disable is case sensitive. |

| Caution | You must restart the Jetty services after enabling or disabling the error log on the Jetty server. |
|---|---|

| Parameters | Description |
|---|---|
| enable | Enables the standard input and output log on the Jetty server. Be aware that enable is case sensitive. |
| disable | Disables the standard input and output log on the Jetty server. Be aware that disable is case sensitive. |

| Caution | You must restart the Jetty services after enabling or disabling the standard input and output log on the Jetty server. |
|---|---|

| Parameters | Description |
|---|---|
| enable | Enables the request log on the Jetty server. Be aware that "enable" is case sensitive. |
| disable | Disables the request log on the Jetty server. Be aware that "disable" is case sensitive. |

| Caution | You must restart the Jetty services after enabling or disabling the request log on the Jetty server. |
|---|---|

| Parameters | Description |
|---|---|
| bit_size | Specifies the bit_size of certificate. Its allowed values are 1k, 2k or 4k. |

| Parameters | Description |
|---|---|
| timeout_value | Sets the time for session logout. |

| Parameters | Description |
|---|---|
| enable | Enables Connection traces. |
| disable | Disables Connection traces. |
| trace_name | Specifies the name of the trace to enable or disable. Be aware that trace names are case sensitive. |
| level | Specifies the level or levels of trace_name that you want to enable or disable. Each trace comprises up to 31 levels, numbered
                                       0 to 30; each level provides a different type of information for the specified trace. When you enable or disable multiple
                                       levels, use a comma to separate levels and a hyphen to indicate a range of levels. Do not include spaces. |

| Parameters | Description |
|---|---|
| HH:mm:ss | Represents
                                       					 the time format (24 hours format). |
| MM/DD/YY | Represents
                                       					 the date format. Note Date
                                                      						  format MM/DD/YYYY is also accepted. | Note | Date
                                                      						  format MM/DD/YYYY is also accepted. |
| Note | Date
                                                      						  format MM/DD/YYYY is also accepted. |

| Note | Date
                                                      						  format MM/DD/YYYY is also accepted. |
|---|---|

| Parameters | Description |
|---|---|
| all | Disables all DSCP port tags. |
| port_tag | Represents a DSCP port tag, which is a string that is mapped to a TCP or UDP port to identify the application that uses the
                                       port. This value is for the portTag field displayed when you use the command show dscp defaults . The set of port tags is predefined. |

| Parameters | Description |
|---|---|
| port_tag | Represents a DSCP port tag, which is a string that is mapped to a TCP or UDP port to identify the application that uses the
                                       port. This value is for the portTag field displayed when you use the command show dscp defaults . The set of port tags is predefined. |
| value | A DSCP value. You can enter the name of a well-known DSCP class or a numeric value in decimal or hexadecimal format. Precede
                                       hexadecimal values with 0x or 0X. |

| Warning | Local Push Notification Service (LPNS) utilizes web sockets exclusively over HTTP/1.1 and it will no longer function when
                                          the HTTP minimum version is set to HTTP/2. |
|---|---|

| Parameters | Description |
|---|---|
| ALL | Enables all
                                       					 ipsec policy groups. |
| group | Specifies
                                       					 the name of a particular ipsec policy group to enable. |

| Parameters | Description |
|---|---|
| policy_group | Specifies the name of a particular ipsec policy group to enable. |
| policy_name | Specifies the name of a particular ipsec policy to enable. |

| Parameters | Description |
|---|---|
| enable | Turns on
                                       					 logging. |
| disable | Turns off
                                       					 logging. |

| Parameters | Description |
|---|---|
| LoginGraceTimeout
                                          						value | Sets the LoginGraceTimeout value for login grace timeout. |

| Parameters | Description |
|---|---|
| hostname | Specifies
                                       					 the hostname of the network cluster. |
| ip | Specifies the IP address of the network cluster. |
| name | Hostname or
                                       					 IP address to assign to the network cluster publisher. |

| Parameter | Description |
|---|---|
| servertype | Choose one of these products for this parameter— Unified Communications Manager , IM and Presence Service, and Cisco Unity Connection. This field is mandatory. |
| hostname | The hostname of the node that you add to the cluster. The hostname is supported on the same domain. This field is mandatory. |
| ip | The IPv4 address of the node that you add to the cluster. This field is mandatory for IM and Presence publisher and Cisco
                                       Unity Connection. |
| domainname | The domain name of the IM and Presence Service publisher. This field is mandatory for IM and Presence publisher. |

| Parameter | Description |
|---|---|
| default | Enables the Dynamic Cluster Configuration for 24 hours. |
| no. of hours | Specifies  a value from 1 to 24 hours. |

| Parameters | Description |
|---|---|
| eth0 | Specifies Ethernet interface 0. |
| enable | This enables DHCP. |
| disable | This disables DHCP. |
| node_ip | Represents the static IP address for the server. |
| net_mask | Represents the subnet mask for the server. |
| gateway_ip | Represents the IP address of the default gateway. |

| Caution | If you continue, this command causes the system to restart. We also recommend that you restart all nodes whenever any IP address
                                          gets changed. |
|---|---|

| Parameters | Description |
|---|---|
| primary |  |
| secondary |  |
| addr | Represents
                                       					 the IP address of the primary or secondary DNS server. |

| Note | If you change the IP address for the DNS servers, you must reboot the server through the utils system restart CLI command. |
|---|---|

| Parameters | Description |
|---|---|
| timeout | Sets the DNS timeout. |
| attempts | Sets the number of times to attempt a DNS request. |
| rotate | Causes the system to rotate among the configured DNS servers and distribute the load. |
| seconds | Specifies the DNS timeout period in seconds. |
| number | Specifies the number of attempts. |

| Note | Changing the domain name triggers an automatic regeneration of all Unified Communications Manager certificates, including
                                          any third party signed certificates that have been uploaded. After the server reboots automatically, phones running in secure
                                          (mixed) mode cannot connect to the server until after the CTL client updates the new CTL file to the phones. |
|---|---|

| Note | Reboot the servers
                                          			 one at a time in order for the phones to register correctly. For more
                                          			 information about changing the domain name, see Changing the
                                             				IP Address and Hostname for Cisco Unified Communications Manager . |
|---|---|

| Parameters | Description |
|---|---|
| domain_name | Represents
                                       					 the system domain that you want to assign. |

| Caution | If you continue,
                                          			 this command causes a temporary loss of network connectivity. |
|---|---|

| Parameters | Description |
|---|---|
| ena | Enables Network Fault Tolerance. |
| dis | Disables Network Fault Tolerance. |

| Parameters | Description |
|---|---|
| addr | Represents the IP address of the network gateway that you want to assign. |

| Caution | If you continue, this command causes the system to restart. |
|---|---|

| Parameters | Description |
|---|---|
| hostname | Represents
                                       					 the new network hostname of the system. Note The host
                                                   						name must follow the rules for ARPANET host names. It must start with an
                                                   						alphabetic character, end with an alphanumeric character, and consist of
                                                   						alphanumeric characters and hyphens. The host name can have a maximum length of
                                                   						63 characters. | Note | The host
                                                   						name must follow the rules for ARPANET host names. It must start with an
                                                   						alphabetic character, end with an alphanumeric character, and consist of
                                                   						alphanumeric characters and hyphens. The host name can have a maximum length of
                                                   						63 characters. |
| Note | The host
                                                   						name must follow the rules for ARPANET host names. It must start with an
                                                   						alphabetic character, end with an alphanumeric character, and consist of
                                                   						alphanumeric characters and hyphens. The host name can have a maximum length of
                                                   						63 characters. |

| Note | The host
                                                   						name must follow the rules for ARPANET host names. It must start with an
                                                   						alphabetic character, end with an alphanumeric character, and consist of
                                                   						alphanumeric characters and hyphens. The host name can have a maximum length of
                                                   						63 characters. |
|---|---|

| Caution | If you continue,
                                          			 this command causes the system to restart. |
|---|---|

| Note | The administrator can change both the hostname and IP address by responding yes . To change just the hostname, respond no . |
|---|---|

| Parameters | Description |
|---|---|
| eth0 | Specifies
                                       					 Ethernet interface 0. |
| addr | Represents
                                       					 the IP address that you want to assign. |
| mask | Represents
                                       					 the IP mask that you want to assign. |
| gw | Represents the IP default GW that you want to assign. |

| Caution | If you continue, this command restarts the following services: NIC driver NTP CLM Service Manager |
|---|---|

| Parameters | Description |
|---|---|
| dhcp | Sets the
                                       					 DHCPv6 client on the server. By default, the server does not restart after you
                                       					 enable the DHCPv6 client. For your changes to take effect, you must restart the
                                       					 server by either entering the reboot parameter or manually restarting the
                                       					 server. |
| enable | Enables IPv6
                                       					 support. |
| disable | Disables
                                       					 IPv6 support. |
| reboot | (Optional)
                                       					 Causes the server to automatically restart after you enter the command. |

| Parameters | Description |
|---|---|
| gateway | Sets the
                                       					 IPv6 gateway for the server. By default, the server does not restart after you
                                       					 set the IPv6 gateway for the server. For your changes to take effect, you must
                                       					 restart the server by either entering the reboot parameter or manually
                                       					 restarting the server. |
| addr | The IPv6
                                       					 gateway address. |
| reboot | (Optional)
                                       					 Causes the server to automatically restart after you enter the command. |

| Parameters | Description |
|---|---|
| service | Sets the
                                       					 IPv6 service on the server. By default, the server does not restart after you
                                       					 enable or disable the IPv6 service on the server. For your changes to take
                                       					 effect, you must restart the server by either entering the reboot parameter or
                                       					 manually restarting the server. |
| enable | Enables IPv6
                                       					 service on the server. |
| disable | Disables
                                       					 IPv6 service on the server. |
| reboot | (Optional)
                                       					 Causes the server to automatically restart after you enter the command. |

| Parameters | Description |
|---|---|
| static_address | Assigns a
                                       					 static IPv6 address to the server. By default, the server does not restart
                                       					 after you assign the static IPv6 address. For your changes to take effect, you
                                       					 must restart the server by either entering the reboot parameter or manually
                                       					 restarting the server. |
| addr | Specifies
                                       					 the static IPv6 address you assign to the server. |
| mask | Specifies
                                       					 the IPv6 network mask (0-128). |
| reboot | (Optional)
                                       					 Causes the server to automatically restart after you enter the command. |

| Parameters | Description |
|---|---|
| ip_conntrack_max value | Specifies
                                       					 the value for ip_conntrack_max. Note The value
                                                   						of ip_conntrack_max cannot be less than 65536. | Note | The value
                                                   						of ip_conntrack_max cannot be less than 65536. |
| Note | The value
                                                   						of ip_conntrack_max cannot be less than 65536. |

| Note | The value
                                                   						of ip_conntrack_max cannot be less than 65536. |
|---|---|

| Parameters | Description |
|---|---|
| mtu_max | Specifies
                                       					 the maximum MTU value. The system default MTU value equals 1500. Caution When
                                                   						packets on UDP port 8500 that have the DF bit set are exchanged between nodes,
                                                   						if there is any policy on the WAN router to clear the DF bit and fragment large
                                                   						packets, this may cause dbreplication issues. | Caution | When
                                                   						packets on UDP port 8500 that have the DF bit set are exchanged between nodes,
                                                   						if there is any policy on the WAN router to clear the DF bit and fragment large
                                                   						packets, this may cause dbreplication issues. |
| Caution | When
                                                   						packets on UDP port 8500 that have the DF bit set are exchanged between nodes,
                                                   						if there is any policy on the WAN router to clear the DF bit and fragment large
                                                   						packets, this may cause dbreplication issues. |

| Caution | When
                                                   						packets on UDP port 8500 that have the DF bit set are exchanged between nodes,
                                                   						if there is any policy on the WAN router to clear the DF bit and fragment large
                                                   						packets, this may cause dbreplication issues. |
|---|---|

| Caution | If you continue,
                                          			 the system loses network connectivity temporarily. |
|---|---|

| Parameters | Description |
|---|---|
| value | The
                                       					 boolean value must be either yes or no . |

| Parameters | Description |
|---|---|
| value | Enter the
                                       					 number of bytes for the database size. |

| Parameters | Description |
|---|---|
| value | Enter the
                                       					 number of seconds. |

| Parameters | Description |
|---|---|
| value | Enter a
                                       					 value for a service. |

| Parameters | Description |
|---|---|
| value | Enter the number of seconds. |

| Parameters | Description |
|---|---|
| value | Enter a prime number for optimum efficiency. |

| Parameters | Description |
|---|---|
| value | The boolean value must be either yes or no . |

| Parameters | Description |
|---|---|
| value | Enter the value in number of bytes. |

| Parameters | Description |
|---|---|
| value | Enter a prime number for optimum efficiency. |

| Parameters | Description |
|---|---|
| value | Enter a value for a service. |

| Parameters | Description |
|---|---|
| value | Enter the number of seconds. |

| Parameters | Description |
|---|---|
| value | Enter a prime number for optimum efficiency. |

| Parameters | Description |
|---|---|
| eth0 | Specifies Ethernet interface 0. |
| auto | Specifies whether auto negotiation gets enabled or disabled. |
| speed | Specifies whether the speed of the Ethernet connection: 10 or 100 Mb/s. |
| duplex | Specifies half-duplex or full-duplex. |

| Note | You can enable only one active NIC at a time. |
|---|---|

| Caution | If you continue, this command causes a temporary loss of network connections while the NIC gets reset. |
|---|---|

| Parameters | Description |
|---|---|
| enable | Enables Path
                                       					 MTU Discovery. |
| disable | Disables
                                       					 Path MTU Discovery. |

| Caution | If you continue,
                                          			 the system loses network connectivity temporarily. |
|---|---|

| Parameters | Description |
|---|---|
| eth0 | Specifies Ethernet interface 0. |
| ip-address | Represents the IP address of the primary or secondary DNS server, or the network gateway that you want to assign. If you continue,
                                       this command causes a temporary loss of network connectivity. If you change the IP address for the primary DNS server, you
                                       must also restart the Cisco Tomcat service. For more information, see the utils service command. We also recommend that you restart all nodes whenever any IP address gets changed. |
| network-mask | Represents the subnet mask for the server. |
| gateway | Specifies the IP address of the default gateway. |
| ip-address | Represents the IP address of the primary or secondary DNS server, or the network gateway that you want to assign. If you continue,
                                       this command causes a temporary loss of network connectivity. If you change the IP address for the primary DNS server, you
                                       must also restart the Cisco Tomcat service. For more information, see the utils service command. We also recommend that you restart all nodes whenever any IP address gets changed. |

| Caution | Only use this command option if you cannot restore network connectivity through any other set network commands. This command
                                          deletes all previous network settings for the specified network interface, including Network Fault Tolerance. After you run
                                          this command, you must restore your previous network configuration manually. |
|---|---|

| Caution | The server temporarily loses network connectivity after you run this command. |
|---|---|

| Parameters | Description |
|---|---|
| eth0 | Specifies Ethernet interface 0. |
| up | Sets the status of Ethernet interface 0 to up. |
| down | Sets the status of Ethernet interface 0 to down. |

| Caution | If you continue, the system loses network connectivity temporarily. |
|---|---|

| Attribute | Value |
|---|---|
| Paranoia | Bool must
                                       					 be either Yes or No. Enabling paranoia mode causes Name Service to restart
                                       					 itself periodically. |
| debug-level | If level
                                       					 is higher than 0, Name Service will create some debug output. Higher the level,
                                       					 more verbose the output. |
| reload-count | Sets the
                                       					 number of times a cached record is reloaded before it is pruned from the cache.
                                       					 Each cache record has a timeout. When that timeout expires Name Service will
                                       					 either reload it (query the NSS service again if the data hasn't changed) or
                                       					 drop it. |
| restart-interval | Sets the
                                       					 restart interval to time seconds if periodic restart is enabled by enabling
                                       					 paranoia mode. The default value is 3600. |

| Note | Use this command after you enable the character complexity of
                                          			 passwords. |
|---|---|

| Parameters | Description |
|---|---|
| value | Enter a value of or greater than six . |

| Parameters | Description |
|---|---|
| maximum | Specifies
                                       					 the maximum age. |
| minimum | Specifies
                                       					 the minimum age. |
| days | Specifies
                                       					 the maximum password age and must be greater-than or equal-to 90 days. |

| Parameters | Description |
|---|---|
| disable | This does not force users to change their password. |
| enable | This forces users to change their password when they sign in to the system the next time. |
| userid | Specifies the affected user account. |

| Note | After you enable password complexity, this command also enables password history if it has not already been enabled (for more
                                          information, see the set password history command). If you had not previously enabled password history, the password history number parameter value gets set to 10.
                                          If you previously enabled password history with a value of less than 10, the value gets reset to 10 after you execute this
                                          command. If you previously enabled password history with a value of 10 or greater, the value remains unchanged after you execute
                                          this command. |
|---|---|

| Parameters | Description |
|---|---|
| disable | This turns off password complexity for character types. |
| enable | This turns on password complexity for character types. Note When you disable password complexity, you also turn off password character difference , password character max-repeat , and password history . | Note | When you disable password complexity, you also turn off password character difference , password character max-repeat , and password history . |
| Note | When you disable password complexity, you also turn off password character difference , password character max-repeat , and password history . |
| num-char | This specifies the number of characters required from each of the four character sets: lowercase, uppercase, numbers, and
                                       special characters. Value range: 0-8 Default value: 1 |

| Note | When you disable password complexity, you also turn off password character difference , password character max-repeat , and password history . |
|---|---|

| Parameters | Description |
|---|---|
| num-char | This specifies the number of characters that the character sequence in a new password must differ from the character sequence
                                       in the old password. Value range: 0-31 |

| Note | The maximum password length is 31 characters. |
|---|---|

| Parameters | Description |
|---|---|
| max-repeat | This specifies the number of times you can consecutively repeat a single character in a new password. Value range: 0 – 10 Default value: 0 |

| Parameters | Description |
|---|---|
| enable | Turns on
                                       					 password expiry maximum age settings for Cisco Unified Operating System
                                       					 administrator accounts. The set password expiry enable command sets the value
                                       					 of maximum password age to 3650 days (10 yrs) for Cisco
                                       					 Unified Operating System Administrator accounts. |
| disable | Turns off
                                       					 password expiry maximum age settings for Cisco Unified Operating System
                                       					 administrator accounts. The set password expiry disable command results in
                                       					 Cisco Unified Operating System Administrator accounts never expiring. |

| Parameters | Description |
|---|---|
| userid | Enter Cisco Collaboration Communication OS (C3OS)
                                       					 Administrator account. |
| maximum password
                                          						age | Enter the maximum password age in days. This value must be
                                       					 equal to or greater than 10 days but less than 3650 days (10 years). |

| Parameters | Description |
|---|---|
| enable | Turns on password expiry
                                       					 minimum age settings for Cisco Unified Operating System administrator accounts.
                                       					 The set password expiry enable command sets the value of minimum password age
                                       					 to one day (24 hrs) for Cisco Collaboration Communication OS (C3OS)
                                       					 Administrator accounts. |
| disable | Turns off password expiry
                                       					 minimum age settings for Cisco Collaboration Communication OS (C3OS)
                                       					 administrator accounts. This means that passwords for administrator accounts
                                       					 can be changed at any interval. |

| Parameters | Description |
|---|---|
| enable | Turns on the maximum age
                                       					 password expiry settings for a particular Cisco Collaboration Communication OS
                                       					 (C3OS) administrator account. The set password expiry user enable command sets
                                       					 the value of maximum password age to 3650 days (10 yrs) for the Cisco Unified
                                       					 Operating System Administrator account. |
| disable | Turns on the maximum age
                                       					 password expiry settings for a particularCisco Collaboration Communication OS
                                       					 (C3OS) administrator account. The set password expiry user enable command sets
                                       					 the value of maximum password age to 3650 days (10 yrs) for the Cisco Unified
                                       					 Operating System Administrator account. |
| userid | Specifies a particular Cisco
                                       					 Collaboration Communication OS (C3OS) Administrator account. |

| Parameters | Description |
|---|---|
| enable | Turns on the minimum age password expiry  settings for a particular Cisco Unified Operating System administrator account. |
| disable | Turns off the minimum age password expiry  settings for a particular Cisco Unified Operating System administrator account. |
| userid | Specifies a particular Cisco Unified Operating System Administrator account. |

| Parameters | Description |
|---|---|
| number | Specifies the mandatory number of passwords to maintain in history. |

| Parameters | Description |
|---|---|
| enable | Enable the
                                       					 password inactivity globally and update individual OS users according to the
                                       					 setting. |
| disable | Disable the
                                       					 password inactivity globally and update individual OS users according to the
                                       					 setting. |
| period | Configure
                                       					 the password inactivity period globally and update individual OS users
                                       					 according to the setting. |
| days | Specify the
                                       					 number of days of inactivity after a password has expired before the account
                                       					 gets disabled. Valid range is 1 - 99. |

| Note | You can change the password only for the administrator account that you logged in to. The password must contain at least six characters, and the system checks it for strength. |
|---|---|

| Note | The password must contain at least six characters, and the system checks it for strength. |
|---|---|

| Note | We recommend that you restart each server after the password is changed on that server. Change the security password on the publisher server (first node) and then reboot the server (node). Change the security password on all the subsequent servers and nodes to the same password that you created on the first node
                                                and restart subsequent nodes, including application servers, to propagate the password change. |
|---|---|

| Note | Failure to reboot the servers
                                          			 (nodes) causes system service problems and problems with the Cisco
                                          			 Collaboration Communication OS (C3OS) Administration windows on the subscriber
                                          			 servers. |
|---|---|

| Parameters | Description |
|---|---|
| enable | Turns on the replication monitoring service. |
| disable | Turns off the replication monitoring service |

| Parameters | Description |
|---|---|
| trace level | Specifies the trace level. The available options are: DEBUG INFO WARNING ERROR FATAL Note The
                                                   						default trace level is INFO. | Note | The
                                                   						default trace level is INFO. |
| Note | The
                                                   						default trace level is INFO. |

| Note | The
                                                   						default trace level is INFO. |
|---|---|

| Parameters | Description |
|---|---|
| maxlimit | This command sets the upper limit for concurrent sessions. Acceptable values are 1 - 10. If no upper
                                       					 limit is entered, the default value of 10 is assigned to sshd_config param. |
| value | Acceptable values are 1 - 10. |

| Parameters | Description |
|---|---|
| hostname | Represents the SMTP server name. |

| Parameters | Description |
|---|---|
| all | Optional parameter to propagate the service trace settings change to all nodes. |
| tracevalue | Represents allowed trace values. Allowed trace values are [Info\|Debug\|Warn\|Error\|Fatal] |
| servicename | Represents the service for which the trace is enabled. |

| Parameters | Description |
|---|---|
| all | Optional parameter to propagate the service trace settings change to all nodes. |
| servicename | Represents the service for which the trace is enabled. |

| Parameters | Description |
|---|---|
| zone | Specifies
                                       					 the new timezone. Enter the appropriate string or zone index id to uniquely
                                       					 identify the timezone. To view a list of valid timezones, use the CLI command: show timezone
                                             						  list . |

| Caution | You must restart
                                          			 the system after you change the timezone. |
|---|---|

| Note | Until Release 15SU2, ensure that you configure the minimum TLS version for each node. After you set the minimum TLS version,
                                                the system reboots. |
|---|---|

| Parameters | Description |
|---|---|
| tls minVersion | Type one of the following options to set it as the minimum TLS version: 1.0 1.1 1.2 |

| Parameters | Description |
|---|---|
| disable | Unsets the task trace settings. |
| tname | Represents the task for which you want to disable traces. |

| Parameters | Description |
|---|---|
| Arbitrary | Sets task trace settings to the arbitrary level. |
| Detailed | Sets task trace settings to the detailed level. |
| Entry_exit | Sets task trace settings to the entry_exit level. |
| Error | Sets task trace settings to the error level. |
| Significant | Sets task trace settings to the significant level. |
| Special | Sets task trace settings to the special level. |
| State_transition | Sets task trace settings to the state transition level. |
| tname | Represents the task for which you want to disable traces. |

| Parameters | Description |
|---|---|
| seconds | Enter a value up to 3600 seconds. The TLS sessions are invalid
                                       					 after the configured value. |

| Parameters | Description |
|---|---|
| service | Specifies
                                          					 the service that you use to disable TLS tracing. |

| Parameters | Description |
|---|---|
| service | Specifies
                                          					 the service that you use to enable TLS tracing. |

| Parameters | Description |
|---|---|
| orgunit | Represents the organizational unit (OU) name. You can use this command to enter multiple organizational units. To enter more than one organizational unit name, separate
                                       the entries with a comma. For entries that already contain a comma, enter a backslash before the comma that is included as
                                       part of the entry. To enter multiple values for organizational unit, enclose them in quotation marks, as shown in the example
                                       for this command. Note For OU’s that already contains a backslash, do not enter one more backslash as SLM registration and CSR generation fails during
                                                   the time of installation. | Note | For OU’s that already contains a backslash, do not enter one more backslash as SLM registration and CSR generation fails during
                                                   the time of installation. |
| Note | For OU’s that already contains a backslash, do not enter one more backslash as SLM registration and CSR generation fails during
                                                   the time of installation. |
| orgname | Represents the organizational name. |
| locality | Represents the organization location. |
| state | Represents the organization state. |
| country | (Optional) Represents the organization country. |
| alternatehostname | (Optional) Specifies an alternate name for the host when you generate a web-server (Tomcat) certificate. You can use alternatehostname to set subject alternate hostname for self signed certificates. Subject alternate hostname for
                                       CSR is defined in the Certificate Management page. If you have set the alternate hostname for CSR using this command, the
                                       CSR generation process replaces the set alternate hostname. |

| Note | For OU’s that already contains a backslash, do not enter one more backslash as SLM registration and CSR generation fails during
                                                   the time of installation. |
|---|---|

| Note | The set web-security command when adding in the alternate hostname will apply and will be added to all future generated CSR's
                                       including, Tomcat, CallManager, CAPF, TVS, and IPsec. |
|---|---|

| Caution | Restarting the Cisco Tomcat service ends all active sessions and can affect system performance. Cisco recommends that you
                                          only execute this command during off-peak traffic hours. |
|---|---|

| Note | This setting gets preserved through a software upgrade and does not get reset to the default value. |
|---|---|

| Parameters | Description |
|---|---|
| minutes | Specifies the time, in minutes, that can elapse before a web application times out and logs off the user. Value range: 5-99999 minutes Default value: 30 minutes |

| Caution | Restarting the
                                          			 Cisco Tomcat service ends all active sessions and can affect the system
                                          			 performance. Cisco recommends that you only execute this command during
                                          			 off-peak traffic hours. |
|---|---|

| Note | This setting
                                          			 gets preserved through a software upgrade and does not get reset to the default
                                          			 value. |
|---|---|

| Parameters | Description |
|---|---|
| number | Specifies the number to limit the concurrent web application sessions. The value
                                       					 ranges from 1 to 10. Default
                                       					 value is 10. If the utils EnhancedSecurityMode is
                                       					 enabled, then the session limit is restricted to 3. For more details on how to
                                       					 Configure Enhanced Security Mode, see the "FIPS
                                          						140-2 Mode Setup" chapter in the Security Guide for Cisco Unified Communications Manager, Release
                                          						11.5(1)SU1 at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . Note When you exceed the defined sign-in sessions maximum limit, then the interface sign-in page displays the Logon Status message
                                                         as: The Session limit has already been reached for <username>. Please logout from those sessions or wait 30 minutes for inactive
                                                            sessions to be automatically closed. When Enhanced Security Mode is enabled, then the
                                                         							 session limit is restricted to 3. However, Administrator can change the session
                                                         							 limit using the set webapp session maxlimit command to any value ranging from 1 to 10. | Note | When you exceed the defined sign-in sessions maximum limit, then the interface sign-in page displays the Logon Status message
                                                         as: The Session limit has already been reached for <username>. Please logout from those sessions or wait 30 minutes for inactive
                                                            sessions to be automatically closed. When Enhanced Security Mode is enabled, then the
                                                         							 session limit is restricted to 3. However, Administrator can change the session
                                                         							 limit using the set webapp session maxlimit command to any value ranging from 1 to 10. |
| Note | When you exceed the defined sign-in sessions maximum limit, then the interface sign-in page displays the Logon Status message
                                                         as: The Session limit has already been reached for <username>. Please logout from those sessions or wait 30 minutes for inactive
                                                            sessions to be automatically closed. When Enhanced Security Mode is enabled, then the
                                                         							 session limit is restricted to 3. However, Administrator can change the session
                                                         							 limit using the set webapp session maxlimit command to any value ranging from 1 to 10. |

| Note | When you exceed the defined sign-in sessions maximum limit, then the interface sign-in page displays the Logon Status message
                                                         as: The Session limit has already been reached for <username>. Please logout from those sessions or wait 30 minutes for inactive
                                                            sessions to be automatically closed. When Enhanced Security Mode is enabled, then the
                                                         							 session limit is restricted to 3. However, Administrator can change the session
                                                         							 limit using the set webapp session maxlimit command to any value ranging from 1 to 10. |
|---|---|

| Parameters | Description |
|---|---|
| activelog | Sets the
                                       					 working directory for active logs. Choose a valid sub-directory of activelog. |
| inactivelog | Set the
                                       					 working directory for inactive logs. Choose a valid sub-directory of
                                       					 inactivelog. |
| tftp | Sets the
                                       					 working directory for TFTP files. |
| directory | Represents
                                       					 the current working directory. |