---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-fb8e938837
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_01100.html
retrieved_at: 2026-08-21T19:20:56.319302+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: June 25, 2015

Chapter: Install Client

## Chapter: Install Client

# Install Client

## Install Cisco Jabber for Windows

Cisco Jabber for Windows provides an MSI installation package  that you can use in the following ways:

Install Option

Description

Use the Command Line

You can specify arguments in a command line window to set installation properties.

Choose this option if you plan to install multiple instances.

Run the MSI Manually

Run the MSI manually on the file system of the client workstation and then specify connection properties when you start the client.

Choose this option if you plan to install a single instance for testing or evaluation purposes.

Create a Custom Installer

Open the default installation package, specify the required installation properties, and then save a custom installation package.

Choose this option if you plan to distribute an installation package with the same installation properties.

Deploy with Group Policy

Install the client on multiple computers in the same domain.

You must be logged in with local administrative rights.

### Use the  Command Line

Specify installation arguments in a command line window.

```
msiexec.exe /i CiscoJabberSetup.msi
```

```
msiexec.exe /i CiscoJabberSetup.msi argument = value
```

#### Example
	 Installation Commands

Review examples of
		  commands to install Cisco Jabber for Windows.

##### Cisco Unified
		  Communications Manager, Release 9.x

```
msiexec.exe /i CiscoJabberSetup.msi /quiet CLEAR =1
```

- CLEAR =1 —
				Deletes any existing bootstrap file.

- /quiet —
				Specifies a silent installation.

##### Cisco Unified
		  Communications Manager, Release 8.x in Default Mode

```
msiexec.exe /i CiscoJabberSetup.msi /quiet CLEAR =1 AUTHENTICATOR =CUP CUP_ADDRESS =1.2.3.4
```

- CLEAR =1 —
				Deletes any existing bootstrap file.

- AUTHENTICATOR =CUP — Sets Cisco Unified Presence as
				the authenticator.

- CUP_ADDRESS =1.2.3.4 — Sets 1.2.3.4 as the IP address
				of the presence server.

- /quiet —
				Specifies a silent installation.

##### Cisco Unified
		  Communications Manager, Release 8.x in Phone Mode

If you are
		  integrating with UDS when you are installing in phone mode, you must first
		  define the <PresenceDomain> Domain address of your
			 Presence server </PresenceDomain> parameter.

```
msiexec.exe /i CiscoJabberSetup.msi /quiet CLEAR=1 PRODUCT_MODE=Phone_Mode AUTHENTICATOR=CUCM TFTP=1.2.3.4 CTI=5.6.7.8
```

- CLEAR =1 —
				Deletes any existing bootstrap file.

- PRODUCT_MODE =Phone_Mode — Sets the client to phone
				mode.

- AUTHENTICATOR =CUCM — Sets Cisco Unified
				Communications Manager as the authenticator.

- TFTP =1.2.3.4 —
				Sets 1.2.3.4 as the IP address of the TFTP server that hosts the client
				configuration.

- CTI =5.6.7.8 —
				Sets 5.6.7.8 as the IP address of the CTI server.

- /quiet —
				Specifies a silent installation.

##### Cisco WebEx
		  Messenger Service

```
msiexec.exe /i CiscoJabberSetup.msi /quiet CLEAR =1 AUTHENTICATOR =WEBEX
```

- CLEAR =1 —
				Deletes any existing bootstrap file.

- AUTHENTICATOR =WEBEX — Sets the Cisco WebEx Messenger
				service as the authenticator.

- /quiet —
				Specifies a silent installation.

##### Cisco WebEx
		  Messenger Service with SSO

```
msiexec.exe /i CiscoJabberSetup.msi /quiet CLEAR =1 AUTHENTICATOR =WEBEX SSO_ORG_DOMAIN =example.com
```

- CLEAR =1 —
				Deletes any existing bootstrap file.

- AUTHENTICATOR =WEBEX — Sets the Cisco WebEx Messenger
				service as the authenticator.

- SSO_ORG_DOMAIN =example.com — Sets example.com as the single sign-on (SSO) domain.

- /quiet —
				Specifies a silent installation.

#### Command Line Arguments

Review the command line arguments you can specify when you install Cisco Jabber for Windows.

##### Override Argument

The following table describes the parameter you must specify to override any existing bootstrap files from previous installations:

Argument

Value

Description

CLEAR

1

Specifies if the client overrides any existing bootstrap file from previous installations.

The client saves the arguments and values you set during installation to a bootstrap file. The client then loads settings from the bootstrap file at startup.

The client deletes any existing bootstrap file.

The client creates a new bootstrap file.

If no bootstrap file exists, the client creates a bootstrap file during installation.

If a bootstrap file exists, the client does not override that bootstrap file and preserves the existing settings.

The client does not preserve settings from existing bootstrap files. If you specify CLEAR , you must also specify all other installation arguments as appropriate.

The client does not save your installation arguments to an existing bootstrap file. If you want to change the values for installation arguments, or specify additional installation arguments, you must specify CLEAR to override the existing settings.

```
msiexec.exe /i CiscoJabberSetup.msi CLEAR =1
```

##### Mode Type
	 Argument

PRODUCT_MODE

Phone_Mode

Phone_Mode — Cisco Unified Communications Manager is
							 the authenticator.

Choose this value to provision users with audio devices as base
							 functionality.

- When to Set the
	 Product Mode

- Change Product Modes

###### When to Set the
	 Product Mode

Cisco Unified
				Communications Manager, Release 9.x and Later — You should not set PRODUCT_MODE during installation. The client gets the
				authenticator from the service profile. After the user signs in, the client
				requires a restart to enter phone mode.

Cisco Unified
				Communications Manager, Release 8.x — You can specify phone mode during
				installation if you set Cisco Unified Communications Manager as the
				authenticator. The client reads the bootstrap file on the initial launch and
				determines it should start in phone mode. The client then gets Cisco Unified
				Communications Manager as the authenticator from the bootstrap file or manual
				settings. After the user signs in, the client does not require a restart.

###### Change Product Modes

To change the product mode, you must change the authenticator for the client. The client can then determine the product mode from the authenticator.

In all deployments, the user can manually set the authenticator in the Advanced settings window.

In this case, you must instruct the user to change the authenticator in the Advanced settings window to change the product mode. You cannot override the manual settings, even if you uninstall and then reinstall the client.

###### Change Product
	 Modes with Cisco Unified Communications Manager Version 9.x and Later

To change
		  product modes with Cisco Unified Communications Manager version 9.x and later,
		  you change the authenticator in the service profile.

Do not
						provision users with an IM and Presence service.

If the
						service profile does not contain an IM and presence service configuration, the
						authenticator is Cisco Unified Communications Manager.

Provision users with an IM and Presence service.

Unified CM (IM and Presence) the authenticator is
							 Cisco Unified Communications Manager IM and Presence Service.

WebEx (IM and Presence) the authenticator is the
							 Cisco WebEx Messenger service.

When users
				sign in to the client, it retrieves the changes in the service profile and
				signs the user in to the authenticator. The client then determines the product
				mode and prompts the user to restart the client.

After the user
		  restarts the client, the product mode change is complete.

###### Change Product
	 Modes with Cisco Unified Communications Manager Version 8.x

To change product
		  modes with 
		  Cisco Unified Communications Manager version 8.x, you must reinstall 
		  Cisco Jabber for Windows to change the authenticator.

CLEAR =1 to delete any existing bootstrap file.

AUTHENTICATOR =CUCM to set the authenticator to 
						Cisco Unified Communications Manager.

PRODUCT_MODE =Phone_Mode to set phone mode as the
						product mode.

CLEAR =1 to delete any existing bootstrap file.

CUP to set the authenticator to 
							 Cisco Unified Presence or 
							 Cisco Unified Communications Manager.

WEBEX to set the authenticator to the 
							 Cisco WebEx Messenger service.

##### Authentication
	 Arguments

CUP

CUCM

WEBEX

CUP—Cisco Unified Communications Manager IM and Presence Service.
							 On-premises deployments in the default product mode. The default product mode
							 can be either full UC or IM only.

- CUCM—Cisco Unified
						  Communications Manager. On-premises deployments in phone mode.

- WEBEX—Cisco WebEx
						  Messenger Service. Cloud-based or hybrid cloud-based deployments.

In
						on-premises deployments with Cisco Unified Communications Manager version 9.x
						and later, you should deploy the _cisco-uds SRV record. The client can then automatically determine the authenticator.

CUP_ADDRESS

IP
						address

Hostname

FQDN

Hostname ( hostname )

IP
							 address ( 123.45.254.1 )

FQDN ( hostname.domain.com )

TFTP

IP
						address

Hostname

FQDN

Hostname ( hostname )

IP
							 address ( 123.45.254.1 )

FQDN
							 ( hostname.domain.com )

You
						should specify this argument if you set Cisco Unified Communications Manager as
						the authenticator.

In
							 phone mode—you should specify the address of the TFTP server that hosts the
							 client configuration.

In
							 default mode—you can specify the address of the Cisco Unified Communications
							 Manager TFTP service that hosts the device configuration.

CTI

IP
						address

Hostname

FQDN

Sets the
						address of your CTI server.

You
							 set Cisco Unified Communications Manager as the authenticator.

Users have desk phone devices and require a CTI server.

CCMCIP

IP
						address

Hostname

FQDN

Sets
						the address of your CCMCIP server.

You set Cisco Unified Communications Manager as the
							 authenticator.

The address of your CCMCIP server is not the same as the TFTP
							 server address.

The client can locate the CCMCIP server with the TFTP server
							 address if both addresses are the same.

Cisco
						Unified Communications Manager release 9.x and earlier—If you enable Cisco
						Extension Mobility, the Cisco Extension Mobility service must be activated on
						the Cisco Unified Communications Manager nodes that are used for CCMCIP. For
						information about Cisco Extension Mobility, see the Feature and Services guide for your Cisco Unified
						Communications Manager release.

SERVICES_DOMAIN

Domain

Sets
						the value of the domain where the DNS SRV records for Service Discovery reside.

This
						argument can be set to a domain where no DNS SRV records reside if you want the
						client to use installer settings or manual configuration for this information.
						If this argument is not specified and Service Discovery fails, the user will be
						prompted for services domain information.

VOICE_SERVICES_DOMAIN

- _cisco-uds

- _cuplogin

- _collab-edge

This
						setting is optional and if not specified, the DNS records are queried on the
						Services Domain which is obtained from the SERVICES_DOMAIN , email address input by the user, or
						cached user configuration.

EXCLUDED_SERVICES

- CUP

- WEBEX

- CUCM

Lists the services that you want Jabber to exclude from Service Discovery. For example, you may have done a trial with WebEx which means that your company domain is registered on WebEx, but you do not want Jabber users to authenticate using WebEx. You want Jabber to authenticate with an on-premises CUP CUCM server. In this case set:

EXCLUDED_SERVICES =WEBEX

Possible values are CUP, CUCM, WEBEX.

To exclude more than one service, use comma separated values. For example, to exclude CUP and CUCM, specify: EXCLUDED_SERVICEs =CUP,CUCM . To exclude all services, specify: EXCLUDED_SERVICES =CUP,CUCM,WEBEX

If you
						exclude all services, you need to use manual configuration or bootstrap
						configuration to configure the Jabber client.

UPN_DISCOVERY_ENABLED

true

false

true (default)—The UPN is used to find the User ID and the  domain of the user,
							 which is used during service discovery. 
						  Only the user discovered from UPN can log in to the client.

false—The UPN is not used to find the User ID and domain of the user. The
							 user is prompted to enter credentials to find the domain for service discovery.

Example installation command: msiexec.exe /i CiscoJabberSetup.msi /quiet UPN_DISCOVERY_ENABLED =false

- TFTP Server Address

###### TFTP Server Address

Client
			 configuration files that you create.

Device
			 configuration files that reside on the 
			 Cisco Unified Communications Manager TFTP service when you provision
			 users with devices.

To minimize effort,
		you should host your client configuration files on the 
		Cisco Unified Communications Manager TFTP service. You then have only one
		TFTP server address for all configuration files and can specify that address as
		required.

You can, however,
		host your client configuration on a different TFTP server to the one that
		contains the device configuration. In this case, you have two different TFTP
		server addresses, one address for the TFTP server that hosts device
		configuration and another address for the TFTP server that hosts client
		configuration files.

###### Default
		  Deployments

This section
		  describes how you should handle two different TFTP server addresses in
		  deployments that have a presence server.

Specify the
				address of the TFTP server that hosts the client configuration on the presence
				server.

During
				installation, specify the address of the 
				Cisco Unified Communications Manager TFTP service with the TFTP argument.

Retrieves the
				address of the 
				Cisco Unified Communications Manager TFTP service from the bootstrap
				file.

Gets device
				configuration from the 
				Cisco Unified Communications Manager TFTP service.

Connects to
				the presence server.

Retrieves the
				address of the TFTP service that hosts the client configuration from the
				presence server.

Gets client
				configuration from the TFTP server.

###### Phone Mode Deployments

This section
		  describes how you should handle two different TFTP server addresses in 
		  phone mode deployments.

During
				installation, specify the address of the TFTP server that hosts the client
				configuration with the TFTP argument.

Specify the
				address of the TFTP server that hosts the device configuration in your client
				configuration file with the following parameter: 
				TftpServer1.

Host the
				client configuration file on the TFTP server.

Retrieves the
				address of the TFTP server from the bootstrap file.

Gets client
				configuration from the TFTP server.

Retrieves the
				address of the 
				Cisco Unified Communications Manager TFTP service from the client
				configuration.

Gets device
				configuration from the 
				Cisco Unified Communications Manager TFTP service.

##### Common
	 Installation Arguments

The following
		  table describes command line arguments that are common to all deployments:

LANGUAGE

LCID in decimal

Defines the Locale ID (LCID), in decimal, of the language that
						Cisco Jabber for Windows uses. The value must be an LCID in decimal that
						corresponds to a supported language.

- 1033 specifies English.

- 1036 specifies French.

See the LCID for Languages topic for a full list of the languages
						that you can specify.

This argument is optional.

If
						you do not specify a value, Cisco Jabber for Windows uses the regional language
						for the current user as the default.

From
						Release 11.1(1) onwards, if you do not specify a value, Cisco Jabber for
						Windows checks the value for the UseSystemLanguage parameter. If the UseSystemLanguage parameter is set to true, the same
						language is used as for the operating system. If the UseSystemLanguage parameter is to set to false or not
						defined, then the client uses the regional language for the current user as the
						default.

The
						regional language is set at Control
							 Panel > Region and Language > Change the date, time, or
							 number format > Formats tab > Format
							 dropdown .

FORGOT_PASSWORD_URL

URL

Specifies the URL where users can reset lost or forgotten
						passwords.

This argument is optional but recommended.

AUTOMATIC_SIGN_IN

true

false

Applies to Release 11.1(1) onwards.

Specifies whether the Sign me in when Cisco Jabber starts check box is
						checked when the user installs the client.

true—The Sign me in when Cisco Jabber starts check box is
							 checked when the user installs the client.

false (default)—The Sign me in when Cisco Jabber starts check box is not
							 checked when the user installs the client.

TFTP_FILE_NAME

Filename

Specifies the unique name of a group configuration file.

You can specify either an unqualified or fully qualified
						filename as the value. The filename you specify as the value for this argument
						takes priority over any other configuration file on your TFTP server.

This argument is optional.

You
							 can specify group configuration files in the Cisco Support Field on the CSF device configuration
							 on Cisco Unified Communications Manager.

LOGIN_RESOURCE

WBX

MUT

Controls user sign in to
						multiple client instances.

WBX—Users can sign in to one instance of Cisco Jabber for
							 Windows at a time.

Cisco Jabber for Windows appends the wbxconnect suffix to the user's JID. Users cannot sign in to any other Cisco Jabber client
							 that uses the wbxconnect suffix.

MUT—Users can sign in to one instance of Cisco Jabber for
							 Windows at a time, but can sign in to other Cisco Jabber clients at the same
							 time.

Each instance of Cisco Jabber for Windows appends the user's JID
							 with a unique suffix.

LOG_DIRECTORY

Absolute path on the local filesystem

Defines
						the directory where the client writes log files.

Use
						quotation marks to escape space characters in the path, as in the following
						example:

"C:\ my_directory \Log
						  Directory"

The path
						you specify must not contain Windows invalid characters.

The
						default value is %USER_PROFILE%\AppData\Local\Cisco\Unified
						  Communications\Jabber\CSF\Logs

CLICK2X

DISABLE

Disables
						click-to-x functionality with Cisco Jabber.

If you
						specify this argument during installation, the client does not register as a
						handler for click-to-x functionality with the operating system. This argument
						prevents the client from writing to the Microsoft Windows registry during
						installation.

You
						must re-install the client and omit this argument to enable click-to-x
						functionality with the client after installation.

ENABLE_PRT

true

false

true (default)—The Report a problem menu item is enabled in the Help menu in the client.

false—The Jabber menu item option Report a problem is removed from the Help menu in the client.

If you
						set the argument to false, users can still manually use the Start
							 Menu > Cisco Jabber directory, or the Program
						files directory and launch the Problem Report Tool manually. If a user manually
						creates a PRT, and this parameter value is set to false, then the zip file
						created from the PRT has no content.

ENABLE_PRT_ENCRYPTION

true

false

true—PRT files sent by Jabber clients are encrypted.

false (default)—PRT files sent by Jabber clients are not
							 encrypted.

PRT
						encryption requires a public/private key pair to encrypt and decrypt the Cisco
						Jabber problem report.

PRT_CERTIFICATE_NAME

Certificate name

Specifies the name of a certificate with a public key in the
						Enterprise Trust or Trusted Root Certificate Authorities certificate store. The
						certificate public key is used to encrypt Jabber Problem reports. You must
						configure this argument with the ENABLE_PRT_ENCRYPTION argument.

INVALID_CERTIFICATE_BEHAVIOR

RejectAndNotify

PromptPerSession

Specifies the client behavior for invalid certificates.

RejectAndNotify—A warning dialog displays and the client doesn't load.

PromptPerSession—A warning dialog displays and the user can accept or reject
							 the invalid certificate.

For
						invalid certificates in FIPS mode, this argument is ignored, the client
						displays a warning message and doesn't load.

Telemetry_Enabled

true

false

Specifies whether analytics data is gathered. The default value
						is true.

To
						improve your experience and product performance, Cisco Jabber may collect and
						send non-personally identifiable usage and performance data to Cisco. The
						aggregated data is used by Cisco to understand trends in how Jabber clients are
						being used and how they are performing.

Full
						details on what analytics data Cisco Jabber does and does not collect can be
						found in the Cisco Jabber Supplement to Cisco’s On-Line Privacy Policy at http:/​/​www.cisco.com/​web/​siteassets/​legal/​privacy_​02Jun10.html .

LOCATION_MODE

ENABLED

DISABLED

ENABLEDNOPROMPT

Specifies whether the Location feature is enabled and whether
						users are notified when new locations are detected.

ENABLED(default)—Location feature is turned on. Users are
							 notified when new locations are detected.

DISABLED—Location feature is turned off. Users are not notified
							 when new locations are detected.

ENABLEDNOPROMPT—Location feature is turned on. Users are not
							 notified when new locations are detected.

FIPS_MODE

true

false

Specifies whether the Cisco Jabber is in FIPS mode.

Cisco Jabber can be in FIPS mode on an operating system that is not FIPS enabled. Only connections with non-Window's APIs are in FIPS mode.

If you don't include this setting, Cisco Jabber will determine the FIPS mode from the operating system.

##### SSO Arguments

This section describes the command line arguments you can use to deploy Cisco Jabber for Windows with single sign on (SSO) capabilities.

- Cloud-Based SSO
	 Arguments

###### Cloud-Based SSO
	 Arguments

Argument

Value

Description

SSO_ORG_DOMAIN

Domain name

Specifies the domain name
						for the Cisco WebEx Org that contains the URL for the
						SSO service.

Cisco Jabber for Windows uses this argument to retrieve the
						URL of the SSO service from the Org. When 
						Cisco Jabber for Windows gets the SSO service URL, it can
						request login tokens to authenticate with 
						Cisco WebEx Messenger.

You specify the URL for the SSO service as the value of the Customer SSO Service
								Login URL in the 
							 Cisco WebEx Administration Tool.

#### LCID for Languages

The following
		  table lists the Locale Identifier (LCID) or Language Identifier (LangID) for the languages that the Cisco Jabber clients support.

Supported Languages

Cisco
						Jabber for Windows

Cisco
						Jabber for Mac

Cisco
						Jabber for Android, Cisco Jabber for iPhone and iPad

LCID/LangID

Arabic 
					 - Saudi Arabia

X

X

1025

Bulgarian 
					 - Bulgaria

X

X

1026

Catalan 
					 - Spain

X

X

1027

Chinese
						(Simplified) - China

X

X

X

2052

Chinese (Traditional)
						- Taiwan

X

X

X

1028

Croatian
						
					 - Croatia

X

X

1050

Czech 
					 - Czech Republic

X

X

1029

Danish 
					 - Denmark

X

X

X

1030

Dutch 
					 - Netherlands

X

X

X

1043

English - United States

X

X

X

1033

Finnish 
					 - Finland

X

X

1035

French
						
					 - France

X

X

X

1036

German
						
					 - Germany

X

X

X

1031

Greek 
					 - Greece

X

X

1032

Hebrew
						
					 - Israel

X

1037

Hungarian 
					 - Hungary

X

X

1038

Italian 
					 - Italy

X

X

X

1040

Japanese 
					 - Japan

X

X

X

1041

Korean
						
					 - Korea

X

X

X

1042

Norwegian 
					 - Norway

X

X

2068

Polish
						
					 - Poland

X

X

1045

Portuguese - Brazil

X

X

X

1046

Portuguese - Portugal

X

X

2070

Romanian 
					 - Romania

X

X

1048

Russian 
					 - Russia

X

X

X

1049

Serbian

X

X

1050

Slovak
						
					 - Slovakian

X

X

1051

Slovenian 
					 -Slovenia

X

X

1060

Spanish 
					 - Spain (Modern Sort)

X

X

X

3082

Swedish 
					 - Sweden

X

X

X

5149

Thai 
					 - Thailand

X

X

1054

Turkish

X

X

1055

### Run the MSI Manually

You can run the installation program manually to install a single instance of the client and specify connection settings in the Advanced settings window.

The installation program opens a window to guide you through the installation process.

The Advanced settings window opens.

### Create a Custom Installer

You can transform the default installation package to create a custom installer.

You use Microsoft Orca to create custom installers. Microsoft Orca is available as part of the Microsoft Windows SDK for Windows 7 and .NET Framework 4.

Download and install Microsoft Windows SDK for Windows 7 and .NET Framework 4 from the Microsoft website .

You must have the default transform file to modify the installation package with Microsoft Orca.

Transform files contain installation properties that you apply to the installer.

Apply a transform file to customize the installer.

#### Get the Default Transform File

You must have the default transform file to modify the installation package with Microsoft Orca.

Create Custom Transform Files

#### Create Custom Transform Files

To create a custom installer, you use a transform file. Transform files contain installation properties that you apply to the installer.

The default transform file lets you specify values for properties when you transform the installer. You should use the default transform file if you are creating one custom installer.

You can optionally create custom transform files. You specify values for properties in a custom transform file and then apply it to the installer.

Create custom transform files if you require more than one custom installer with different property values. For example, create one transform file that sets the default language to French and another transform file that sets the default language to Spanish. You can then apply each transform file to the installation package separately. The result is that you  create two installers, one for each language.

Get the Default Transform File

- Select Transform > Generate Transform .

- Select a location on your file system to save the transform file.

- Specify a name for the transform file and select Save .

The transform file you created is saved as file_name .mst . You can apply this transform file to modify the properties of CiscoJabberSetup.msi .

Transform the Installer

#### Transform the
		Installer

Apply a transform
		  file to customize the installer.

Applying
				transform files will alter the digital signature of CiscoJabberSetup.msi . Attempts to modify or rename CiscoJabberSetup.msi will remove the signature
				entirely.

Create Custom Transform Files

- Select File > Open .

- Browse to
				  the location of CiscoJabberSetup.msi on your file system.

- Select CiscoJabberSetup.msi and then select Open .

The
				installation package opens in 
				Microsoft Orca. The list of tables for the
				installer opens in the Tables pane.

You must
					 remove all language codes from the custom installer except for 1033 (English).

Microsoft Orca does not retain any language files
					 in custom installers except for the default, which is 1033. If you do not
					 remove all language codes from the custom installer, you cannot run the
					 installer on any operating system where the language is other than English.

The Edit Summary Information window displays.

- Locate
				  the Languages field.

- Delete
				  all language codes except for 1033.

- Select OK .

English is
				set as the language for your custom installer.

- Select Transform > Apply
						Transform .

- Browse to
				  the location of the transform file on your file system.

- Select the
				  transform file and then select Open .

The list of
				properties for CiscoJabberSetup.msi opens in the right panel of the
				application window.

Values
					 are case sensitive. Ensure the value you enter matches the value in this
					 document.

Set the
					 value of the CLEAR property to 1 to override any existing bootstrap file from
					 previous installations. If you do not override existing bootstrap files, the
					 values you set in the custom installer do not take effect.

- Right-click the property you want to remove.

- Select Drop Row .

- Select OK when 
				  Microsoft Orca prompts you to continue.

- Select Tools > Options .

- Select
				  the Database tab.

- Select Copy embedded streams during 'Save As' .

- Select Apply and then OK .

- Select File > Save Transformed
						As .

- Select a
				  location on your file system to save the installer.

- Specify
				  a name for the installer and then select Save .

#### Installer Properties

CLEAR

PRODUCT_MODE

AUTHENTICATOR

CUP_ADDRESS

TFTP

CTI

CCMCIP

LANGUAGE

TFTP_FILE_NAME

FORGOT_PASSWORD_URL

SSO_ORG_DOMAIN

LOGIN_RESOURCE

LOG_DIRECTORY

CLICK2X

- SERVICES_DOMAIN

These properties correspond to the installation arguments and have the same values.

### Deploy with Group Policy

Install Cisco Jabber for Windows with Group Policy using the Microsoft Group Policy Management Console (GPMC) on Microsoft Windows Server.

To install Cisco Jabber for Windows with Group Policy, all computers or users to which you plan to deploy Cisco Jabber for Windows must be in the same domain.

You must use this procedure and set the Language field to 1033 only if the MSI is to be modified by Orca in any way.

Deploy Cisco Jabber for Windows with Group Policy.

#### Set a Language Code

Altering the installation language is not necessary in Group Policy deployment scenarios where the exact MSI file provided by Cisco will be used. The installation language will be determined from the Windows User Locale (Format) in these situations. You must use this procedure and set the Language field to 1033 only if the MSI is to be modified by Orca in any way.

Microsoft Orca is available as part of the Microsoft Windows SDK for Windows 7 and ,NET Framework 4 that you can download from the Microsoft website.

- Select File > Open .

- Browse to the location of CiscoJabberSetup.msi on your file system.

- Select CiscoJabberSetup.msi and then select Open .

- Select Tools > Options .

- Select the Database tab.

- Select Copy embedded streams during 'Save As' .

- Select Apply and then OK .

- Select File > Save Transformed As .

- Select a location on your file system to save the installer.

- Specify a name for the installer and then select Save .

Deploy the Client with Group Policy

#### Deploy the Client  with Group Policy

Complete the steps in this task to deploy Cisco Jabber for Windows with Group Policy.

Set a Language Code

All computers or users to which you plan to deploy Cisco Jabber for Windows must be able to access the installation package on the distribution point.

```
GPMC.msc
```

The Group Policy Management console opens.

- Right-click on the appropriate domain in the left pane.

The New GPO window opens.

- Enter a name for the group policy object in the Name field.

The new group policy displays in the list of group policies for the domain.

The group policy object displays in the right pane.

The Select User, Computer, or Group window opens.

- Specify the computers and users to which you want to deploy Cisco Jabber for
			 Windows .

The Group Policy Management Editor opens.

- Select Computer Configuration and then select Policies > Software Settings .

- Right-click Software Installation and then select New > Package .

You must enter a Uniform Naming Convention (UNC) path as the location of the installation package. If you do not enter a UNC path, Group Policy cannot deploy Cisco Jabber for Windows.

- Select the installation package and then select Open .

- In the Deploy Software dialog box, select Assigned and then OK .

Group Policy installs Cisco Jabber for Windows on each computer the next time each computer starts.

### Cisco Media
	 Services Interface

Cisco Jabber for
				  Windows supports Cisco Media Services
			 Interface version 4.1.2 for Microsoft
		  Windows 7 and later.

Cisco Jabber for Mac supports Cisco Media Services
			 Interface version 4.0.2 or later.

#### Desk Phone Video Capabilities

Discover the desk phone device.

Establish and maintain a connection to the desk phone device using the CAST protocol.

#### Install Cisco
	 Media Services Interface

See the
				appropriate 
				Cisco Medianet documentation for installing 
				Cisco Media Services Interface.

### Uninstall Cisco Jabber for
	 Windows

You can uninstall 
		  Cisco Jabber for Windows using either the command line or the Microsoft Windows  control panel. This document
		  describes how to uninstall 
		  Cisco Jabber for Windows using the command line.

#### Use the Installer

If the installer is available on the file system, use it to remove Cisco Jabber for Windows.

```
msiexec.exe /x path_to_ CiscoJabberSetup.msi
```

```
msiexec.exe /x C:\Windows\Installer\ CiscoJabberSetup.msi /quiet
```

The command removes Cisco Jabber for Windows from the computer.

#### Use the Product Code

If the installer is not available on the file system, use the product code to remove Cisco Jabber for Windows.

- Open the Microsoft Windows registry editor.

- Locate the following registry key: HKEY_CLASSES_ROOT\Installer\Products

- Select Edit > Find .

- Enter Cisco Jabber in the Find what text box in the Find window and select Find Next .

The product code is the value of  the ProductIcon key, for example, C:\Windows\Installer\{ product_code }\ARPPRODUCTICON.exe .

The product code changes with each version of Cisco Jabber for Windows.

```
msiexec.exe /x product_code
```

```
msiexec.exe /x 45992224-D2DE-49BB-B085-6524845321C7 /quiet
```

The command removes Cisco Jabber for Windows from the computer.

## Install Cisco Jabber for Mac

### Distribute the Cisco Jabber for Mac client

Visit the Cisco Software Center to download the Cisco Jabber for Mac client.

Upgrading in the Mac OS X environment is performed automatically by the application, with permission from the user.

## Install Cisco Jabber Mobile Clients

| Install Option | Description |
|---|---|
| Use the Command Line | You can specify arguments in a command line window to set installation properties. Choose this option if you plan to install multiple instances. |
| Run the MSI Manually | Run the MSI manually on the file system of the client workstation and then specify connection properties when you start the client. Choose this option if you plan to install a single instance for testing or evaluation purposes. |
| Create a Custom Installer | Open the default installation package, specify the required installation properties, and then save a custom installation package. Choose this option if you plan to distribute an installation package with the same installation properties. |
| Deploy with Group Policy | Install the client on multiple computers in the same domain. |

| Step 1 | Open a command line window. |
|---|---|
| Step 2 | Enter the following command: msiexec.exe /i CiscoJabberSetup.msi |
| Step 3 | Specify command line arguments as parameter=value pairs. msiexec.exe /i CiscoJabberSetup.msi argument = value |
| Step 4 | Run the command to install Cisco Jabber for Windows . |

| Argument | Value | Description |
|---|---|---|
| CLEAR | 1 | Specifies if the client overrides any existing bootstrap file from previous installations. The client saves the arguments and values you set during installation to a bootstrap file. The client then loads settings from the bootstrap file at startup. |

| Note | If you are reinstalling  Cisco Jabber for Windows, you should consider the following: The client does not preserve settings from existing bootstrap files. If you specify CLEAR , you must also specify all other installation arguments as appropriate. The client does not save your installation arguments to an existing bootstrap file. If you want to change the values for installation arguments, or specify additional installation arguments, you must specify CLEAR to override the existing settings. |
|---|---|

| Argument | Value | Description |
|---|---|---|
| PRODUCT_MODE | Phone_Mode | Specifies the product mode for the client. You can set the
						following value: Phone_Mode — Cisco Unified Communications Manager is
							 the authenticator. Choose this value to provision users with audio devices as base
							 functionality. |

| Note | In all deployments, the user can manually set the authenticator in the Advanced settings window. In this case, you must instruct the user to change the authenticator in the Advanced settings window to change the product mode. You cannot override the manual settings, even if you uninstall and then reinstall the client. |
|---|---|

| Step 1 | Change the
			 authenticator in the service profiles for the appropriate users. Change
					 Default Mode > Phone Mode Do not
						provision users with an IM and Presence service. If the
						service profile does not contain an IM and presence service configuration, the
						authenticator is Cisco Unified Communications Manager. Change
					 Phone Mode > Default Mode Provision users with an IM and Presence service. If you
						set the value of the Product type field in the IM and Presence profile
						to: Unified CM (IM and Presence) the authenticator is
							 Cisco Unified Communications Manager IM and Presence Service. WebEx (IM and Presence) the authenticator is the
							 Cisco WebEx Messenger service. |
|---|---|
| Step 2 | Instruct
			 users to sign out and then sign in again. When users
				sign in to the client, it retrieves the changes in the service profile and
				signs the user in to the authenticator. The client then determines the product
				mode and prompts the user to restart the client. |

| Argument | Value | Description |
|---|---|---|
| AUTHENTICATOR | CUP CUCM WEBEX | Specifies the source of authentication for the client. This
						value is used if Service Discovery fails. Set one of the following as the
						value: CUP—Cisco Unified Communications Manager IM and Presence Service.
							 On-premises deployments in the default product mode. The default product mode
							 can be either full UC or IM only. CUCM—Cisco Unified
						  Communications Manager. On-premises deployments in phone mode. WEBEX—Cisco WebEx
						  Messenger Service. Cloud-based or hybrid cloud-based deployments. In
						on-premises deployments with Cisco Unified Communications Manager version 9.x
						and later, you should deploy the _cisco-uds SRV record. The client can then automatically determine the authenticator. |
| CUP_ADDRESS | IP
						address Hostname FQDN | Specifies the address of Cisco Unified Communications Manager IM
						and Presence Service. Set one of the following as the value: Hostname ( hostname ) IP
							 address ( 123.45.254.1 ) FQDN ( hostname.domain.com ) |
| TFTP | IP
						address Hostname FQDN | Specifies the address of your TFTP server. Set one of the
						following as the value: Hostname ( hostname ) IP
							 address ( 123.45.254.1 ) FQDN
							 ( hostname.domain.com ) You
						should specify this argument if you set Cisco Unified Communications Manager as
						the authenticator. If you
						deploy: In
							 phone mode—you should specify the address of the TFTP server that hosts the
							 client configuration. In
							 default mode—you can specify the address of the Cisco Unified Communications
							 Manager TFTP service that hosts the device configuration. |
| CTI | IP
						address Hostname FQDN | Sets the
						address of your CTI server. Specify
						this argument if: You
							 set Cisco Unified Communications Manager as the authenticator. Users have desk phone devices and require a CTI server. |
| CCMCIP | IP
						address Hostname FQDN | Sets
						the address of your CCMCIP server. Specify this argument if: You set Cisco Unified Communications Manager as the
							 authenticator. The address of your CCMCIP server is not the same as the TFTP
							 server address. The client can locate the CCMCIP server with the TFTP server
							 address if both addresses are the same. Cisco
						Unified Communications Manager release 9.x and earlier—If you enable Cisco
						Extension Mobility, the Cisco Extension Mobility service must be activated on
						the Cisco Unified Communications Manager nodes that are used for CCMCIP. For
						information about Cisco Extension Mobility, see the Feature and Services guide for your Cisco Unified
						Communications Manager release. |
| SERVICES_DOMAIN | Domain | Sets
						the value of the domain where the DNS SRV records for Service Discovery reside. This
						argument can be set to a domain where no DNS SRV records reside if you want the
						client to use installer settings or manual configuration for this information.
						If this argument is not specified and Service Discovery fails, the user will be
						prompted for services domain information. |
| VOICE_SERVICES_DOMAIN | Domain | In
						Hybrid Deployments the domain required to discover Webex via CAS lookup may be
						a different domain than where the DNS records are deployed. If this is the case
						then set the SERVICES_DOMAIN to be the domain used for Webex
						discovery (or let the user enter an email address) and set the VOICE_SERVICES_DOMAIN to be the domain where DNS
						records are deployed. If this setting is specified, the client will use the
						value of VOICE_SERVICES_DOMAIN to lookup the following DNS
						records for the purposes of Service Discovery and Edge Detection: _cisco-uds _cuplogin _collab-edge This
						setting is optional and if not specified, the DNS records are queried on the
						Services Domain which is obtained from the SERVICES_DOMAIN , email address input by the user, or
						cached user configuration. |
| EXCLUDED_SERVICES | One
						or more of: CUP WEBEX CUCM | Lists the services that you want Jabber to exclude from Service Discovery. For example, you may have done a trial with WebEx which means that your company domain is registered on WebEx, but you do not want Jabber users to authenticate using WebEx. You want Jabber to authenticate with an on-premises CUP CUCM server. In this case set: EXCLUDED_SERVICES =WEBEX Possible values are CUP, CUCM, WEBEX. To exclude more than one service, use comma separated values. For example, to exclude CUP and CUCM, specify: EXCLUDED_SERVICEs =CUP,CUCM . To exclude all services, specify: EXCLUDED_SERVICES =CUP,CUCM,WEBEX If you
						exclude all services, you need to use manual configuration or bootstrap
						configuration to configure the Jabber client. |
| UPN_DISCOVERY_ENABLED | true false | Allows
						you to define whether the client uses the User Principal Name (UPN) of a
						Windows session to get the User ID and domain for a user when discovering services. true (default)—The UPN is used to find the User ID and the  domain of the user,
							 which is used during service discovery. 
						  Only the user discovered from UPN can log in to the client. false—The UPN is not used to find the User ID and domain of the user. The
							 user is prompted to enter credentials to find the domain for service discovery. Example installation command: msiexec.exe /i CiscoJabberSetup.msi /quiet UPN_DISCOVERY_ENABLED =false |

| Argument | Value | Description |
|---|---|---|
| LANGUAGE | LCID in decimal | Defines the Locale ID (LCID), in decimal, of the language that
						Cisco Jabber for Windows uses. The value must be an LCID in decimal that
						corresponds to a supported language. For example, you can specify one of the following: 1033 specifies English. 1036 specifies French. See the LCID for Languages topic for a full list of the languages
						that you can specify. This argument is optional. If
						you do not specify a value, Cisco Jabber for Windows uses the regional language
						for the current user as the default. From
						Release 11.1(1) onwards, if you do not specify a value, Cisco Jabber for
						Windows checks the value for the UseSystemLanguage parameter. If the UseSystemLanguage parameter is set to true, the same
						language is used as for the operating system. If the UseSystemLanguage parameter is to set to false or not
						defined, then the client uses the regional language for the current user as the
						default. The
						regional language is set at Control
							 Panel > Region and Language > Change the date, time, or
							 number format > Formats tab > Format
							 dropdown . |
| FORGOT_PASSWORD_URL | URL | Specifies the URL where users can reset lost or forgotten
						passwords. This argument is optional but recommended. Note In cloud-based
						deployments, you can specify a forgot password URL using the Cisco WebEx
						Administration Tool. However, the client cannot retrieve that forgot password
						URL until users sign in. | Note | In cloud-based
						deployments, you can specify a forgot password URL using the Cisco WebEx
						Administration Tool. However, the client cannot retrieve that forgot password
						URL until users sign in. |
| Note | In cloud-based
						deployments, you can specify a forgot password URL using the Cisco WebEx
						Administration Tool. However, the client cannot retrieve that forgot password
						URL until users sign in. |
| AUTOMATIC_SIGN_IN | true false | Applies to Release 11.1(1) onwards. Specifies whether the Sign me in when Cisco Jabber starts check box is
						checked when the user installs the client. true—The Sign me in when Cisco Jabber starts check box is
							 checked when the user installs the client. false (default)—The Sign me in when Cisco Jabber starts check box is not
							 checked when the user installs the client. |
| TFTP_FILE_NAME | Filename | Specifies the unique name of a group configuration file. You can specify either an unqualified or fully qualified
						filename as the value. The filename you specify as the value for this argument
						takes priority over any other configuration file on your TFTP server. This argument is optional. Remember: You
							 can specify group configuration files in the Cisco Support Field on the CSF device configuration
							 on Cisco Unified Communications Manager. |
| LOGIN_RESOURCE | WBX MUT | Controls user sign in to
						multiple client instances. By default, users can sign in to multiple instances of Cisco
						Jabber at the same time. Set one of the following values to change the default
						behavior: WBX—Users can sign in to one instance of Cisco Jabber for
							 Windows at a time. Cisco Jabber for Windows appends the wbxconnect suffix to the user's JID. Users cannot sign in to any other Cisco Jabber client
							 that uses the wbxconnect suffix. MUT—Users can sign in to one instance of Cisco Jabber for
							 Windows at a time, but can sign in to other Cisco Jabber clients at the same
							 time. Each instance of Cisco Jabber for Windows appends the user's JID
							 with a unique suffix. |
| LOG_DIRECTORY | Absolute path on the local filesystem | Defines
						the directory where the client writes log files. Use
						quotation marks to escape space characters in the path, as in the following
						example: "C:\ my_directory \Log
						  Directory" The path
						you specify must not contain Windows invalid characters. The
						default value is %USER_PROFILE%\AppData\Local\Cisco\Unified
						  Communications\Jabber\CSF\Logs |
| CLICK2X | DISABLE | Disables
						click-to-x functionality with Cisco Jabber. If you
						specify this argument during installation, the client does not register as a
						handler for click-to-x functionality with the operating system. This argument
						prevents the client from writing to the Microsoft Windows registry during
						installation. You
						must re-install the client and omit this argument to enable click-to-x
						functionality with the client after installation. |
| ENABLE_PRT | true false | true (default)—The Report a problem menu item is enabled in the Help menu in the client. false—The Jabber menu item option Report a problem is removed from the Help menu in the client. If you
						set the argument to false, users can still manually use the Start
							 Menu > Cisco Jabber directory, or the Program
						files directory and launch the Problem Report Tool manually. If a user manually
						creates a PRT, and this parameter value is set to false, then the zip file
						created from the PRT has no content. |
| ENABLE_PRT_ENCRYPTION | true false | Enables problem report encryption. You must configure this
						argument with the PRT_CERTIFICATE_NAME argument. true—PRT files sent by Jabber clients are encrypted. false (default)—PRT files sent by Jabber clients are not
							 encrypted. PRT
						encryption requires a public/private key pair to encrypt and decrypt the Cisco
						Jabber problem report. |
| PRT_CERTIFICATE_NAME | Certificate name | Specifies the name of a certificate with a public key in the
						Enterprise Trust or Trusted Root Certificate Authorities certificate store. The
						certificate public key is used to encrypt Jabber Problem reports. You must
						configure this argument with the ENABLE_PRT_ENCRYPTION argument. |
| INVALID_CERTIFICATE_BEHAVIOR | RejectAndNotify PromptPerSession | Specifies the client behavior for invalid certificates. RejectAndNotify—A warning dialog displays and the client doesn't load. PromptPerSession—A warning dialog displays and the user can accept or reject
							 the invalid certificate. For
						invalid certificates in FIPS mode, this argument is ignored, the client
						displays a warning message and doesn't load. |
| Telemetry_Enabled | true false | Specifies whether analytics data is gathered. The default value
						is true. To
						improve your experience and product performance, Cisco Jabber may collect and
						send non-personally identifiable usage and performance data to Cisco. The
						aggregated data is used by Cisco to understand trends in how Jabber clients are
						being used and how they are performing. Full
						details on what analytics data Cisco Jabber does and does not collect can be
						found in the Cisco Jabber Supplement to Cisco’s On-Line Privacy Policy at http:/​/​www.cisco.com/​web/​siteassets/​legal/​privacy_​02Jun10.html . |
| LOCATION_MODE | ENABLED DISABLED ENABLEDNOPROMPT | Specifies whether the Location feature is enabled and whether
						users are notified when new locations are detected. ENABLED(default)—Location feature is turned on. Users are
							 notified when new locations are detected. DISABLED—Location feature is turned off. Users are not notified
							 when new locations are detected. ENABLEDNOPROMPT—Location feature is turned on. Users are not
							 notified when new locations are detected. |
| FIPS_MODE | true false | Specifies whether the Cisco Jabber is in FIPS mode. Cisco Jabber can be in FIPS mode on an operating system that is not FIPS enabled. Only connections with non-Window's APIs are in FIPS mode. If you don't include this setting, Cisco Jabber will determine the FIPS mode from the operating system. |

| Note | In cloud-based
						deployments, you can specify a forgot password URL using the Cisco WebEx
						Administration Tool. However, the client cannot retrieve that forgot password
						URL until users sign in. |
|---|---|

| Argument | Value | Description |
|---|---|---|
| SSO_ORG_DOMAIN | Domain name | Specifies the domain name
						for the Cisco WebEx Org that contains the URL for the
						SSO service. Cisco Jabber for Windows uses this argument to retrieve the
						URL of the SSO service from the Org. When 
						Cisco Jabber for Windows gets the SSO service URL, it can
						request login tokens to authenticate with 
						Cisco WebEx Messenger. Note You specify the URL for the SSO service as the value of the Customer SSO Service
								Login URL in the 
							 Cisco WebEx Administration Tool. | Note | You specify the URL for the SSO service as the value of the Customer SSO Service
								Login URL in the 
							 Cisco WebEx Administration Tool. |
| Note | You specify the URL for the SSO service as the value of the Customer SSO Service
								Login URL in the 
							 Cisco WebEx Administration Tool. |

| Note | You specify the URL for the SSO service as the value of the Customer SSO Service
								Login URL in the 
							 Cisco WebEx Administration Tool. |
|---|---|

| Supported Languages | Cisco
						Jabber for Windows | Cisco
						Jabber for Mac | Cisco
						Jabber for Android, Cisco Jabber for iPhone and iPad | LCID/LangID |
|---|---|---|---|---|
| Arabic 
					 - Saudi Arabia | X |  | X | 1025 |
| Bulgarian 
					 - Bulgaria | X | X |  | 1026 |
| Catalan 
					 - Spain | X | X |  | 1027 |
| Chinese
						(Simplified) - China | X | X | X | 2052 |
| Chinese (Traditional)
						- Taiwan | X | X | X | 1028 |
| Croatian
						
					 - Croatia | X | X |  | 1050 |
| Czech 
					 - Czech Republic | X | X |  | 1029 |
| Danish 
					 - Denmark | X | X | X | 1030 |
| Dutch 
					 - Netherlands | X | X | X | 1043 |
| English - United States | X | X | X | 1033 |
| Finnish 
					 - Finland | X | X |  | 1035 |
| French
						
					 - France | X | X | X | 1036 |
| German
						
					 - Germany | X | X | X | 1031 |
| Greek 
					 - Greece | X | X |  | 1032 |
| Hebrew
						
					 - Israel | X |  |  | 1037 |
| Hungarian 
					 - Hungary | X | X |  | 1038 |
| Italian 
					 - Italy | X | X | X | 1040 |
| Japanese 
					 - Japan | X | X | X | 1041 |
| Korean
						
					 - Korea | X | X | X | 1042 |
| Norwegian 
					 - Norway | X | X |  | 2068 |
| Polish
						
					 - Poland | X | X |  | 1045 |
| Portuguese - Brazil | X | X | X | 1046 |
| Portuguese - Portugal | X | X |  | 2070 |
| Romanian 
					 - Romania | X | X |  | 1048 |
| Russian 
					 - Russia | X | X | X | 1049 |
| Serbian | X | X |  | 1050 |
| Slovak
						
					 - Slovakian | X | X |  | 1051 |
| Slovenian 
					 -Slovenia | X | X |  | 1060 |
| Spanish 
					 - Spain (Modern Sort) | X | X | X | 3082 |
| Swedish 
					 - Sweden | X | X | X | 5149 |
| Thai 
					 - Thailand | X | X |  | 1054 |
| Turkish | X | X |  | 1055 |

| Step 1 | Launch CiscoJabberSetup.msi . The installation program opens a window to guide you through the installation process. |
|---|---|
| Step 2 | Follow the steps to complete the installation process. |
| Step 3 | Start Cisco Jabber for Windows . |
| Step 4 | Select Manual setup and sign in . The Advanced settings window opens. |
| Step 5 | Specify values for the connection settings properties. |
| Step 6 | Select Save . |

| Note | You use Microsoft Orca to create custom installers. Microsoft Orca is available as part of the Microsoft Windows SDK for Windows 7 and .NET Framework 4. Download and install Microsoft Windows SDK for Windows 7 and .NET Framework 4 from the Microsoft website . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Get the Default Transform File | You must have the default transform file to modify the installation package with Microsoft Orca. |
| Step 2 | Create Custom Transform Files | Transform files contain installation properties that you apply to the installer. |
| Step 3 | Transform the Installer | Apply a transform file to customize the installer. |

| Step 1 | Download the  Cisco Jabber administration package from Software Download page . |
|---|---|
| Step 2 | Copy CiscoJabberProperties.msi from the  Cisco Jabber administration package   to your file system. |

| Step 1 | Start Microsoft Orca. |
|---|---|
| Step 2 | Open CiscoJabberSetup.msi and then apply CiscoJabberProperties.msi . |
| Step 3 | Specify values for the appropriate installer properties. |
| Step 4 | Generate and save the transform file. Select Transform > Generate Transform . Select a location on your file system to save the transform file. Specify a name for the transform file and select Save . |

| Note | Applying
				transform files will alter the digital signature of CiscoJabberSetup.msi . Attempts to modify or rename CiscoJabberSetup.msi will remove the signature
				entirely. |
|---|---|

| Step 1 | Start 
			 Microsoft Orca. |
|---|---|
| Step 2 | Open CiscoJabberSetup.msi in 
			 Microsoft Orca. Select File > Open . Browse to
				  the location of CiscoJabberSetup.msi on your file system. Select CiscoJabberSetup.msi and then select Open . The
				installation package opens in 
				Microsoft Orca. The list of tables for the
				installer opens in the Tables pane. |
| Step 3 | Remove all
			 language codes except for 1033 (English). Restriction: You must
					 remove all language codes from the custom installer except for 1033 (English). Microsoft Orca does not retain any language files
					 in custom installers except for the default, which is 1033. If you do not
					 remove all language codes from the custom installer, you cannot run the
					 installer on any operating system where the language is other than English. Select View > Summary
						Information . The Edit Summary Information window displays. Locate
				  the Languages field. Delete
				  all language codes except for 1033. Select OK . English is
				set as the language for your custom installer. |
| Step 4 | Apply a
			 transform file. Select Transform > Apply
						Transform . Browse to
				  the location of the transform file on your file system. Select the
				  transform file and then select Open . |
| Step 5 | Select Property from the list of tables in the Tables pane. The list of
				properties for CiscoJabberSetup.msi opens in the right panel of the
				application window. |
| Step 6 | Specify
			 values for the properties you require. Tip Values
					 are case sensitive. Ensure the value you enter matches the value in this
					 document. Tip Set the
					 value of the CLEAR property to 1 to override any existing bootstrap file from
					 previous installations. If you do not override existing bootstrap files, the
					 values you set in the custom installer do not take effect. | Tip | Values
					 are case sensitive. Ensure the value you enter matches the value in this
					 document. | Tip | Set the
					 value of the CLEAR property to 1 to override any existing bootstrap file from
					 previous installations. If you do not override existing bootstrap files, the
					 values you set in the custom installer do not take effect. |
| Tip | Values
					 are case sensitive. Ensure the value you enter matches the value in this
					 document. |
| Tip | Set the
					 value of the CLEAR property to 1 to override any existing bootstrap file from
					 previous installations. If you do not override existing bootstrap files, the
					 values you set in the custom installer do not take effect. |
| Step 7 | Remove any
			 properties that you do not require. It is essential to remove any properties that are not being set,
			 otherwise the properties being set will not take effect. Remove each property
			 that is not needed one at a time. Right-click the property you want to remove. Select Drop Row . Select OK when 
				  Microsoft Orca prompts you to continue. |
| Step 8 | Enable your
			 custom installer to save embedded streams. Select Tools > Options . Select
				  the Database tab. Select Copy embedded streams during 'Save As' . Select Apply and then OK . |
| Step 9 | Save your
			 custom installer. Select File > Save Transformed
						As . Select a
				  location on your file system to save the installer. Specify
				  a name for the installer and then select Save . |

| Tip | Values
					 are case sensitive. Ensure the value you enter matches the value in this
					 document. |
|---|---|

| Tip | Set the
					 value of the CLEAR property to 1 to override any existing bootstrap file from
					 previous installations. If you do not override existing bootstrap files, the
					 values you set in the custom installer do not take effect. |
|---|---|

| Note | To install Cisco Jabber for Windows with Group Policy, all computers or users to which you plan to deploy Cisco Jabber for Windows must be in the same domain. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Set a Language Code | You must use this procedure and set the Language field to 1033 only if the MSI is to be modified by Orca in any way. |
| Step 2 | Deploy the Client with Group Policy | Deploy Cisco Jabber for Windows with Group Policy. |

| Step 1 | Start Microsoft Orca. Microsoft Orca is available as part of the Microsoft Windows SDK for Windows 7 and ,NET Framework 4 that you can download from the Microsoft website. |
|---|---|
| Step 2 | Open CiscoJabberSetup.msi . Select File > Open . Browse to the location of CiscoJabberSetup.msi on your file system. Select CiscoJabberSetup.msi and then select Open . |
| Step 3 | Select View > Summary Information . |
| Step 4 | Locate the Languages field. |
| Step 5 | Set the Languages field to 1033. |
| Step 6 | Select OK . |
| Step 7 | Enable your custom installer  to save embedded streams. Select Tools > Options . Select the Database tab. Select Copy embedded streams during 'Save As' . Select Apply and then OK . |
| Step 8 | Save your custom installer. Select File > Save Transformed As . Select a location on your file system to save the installer. Specify a name for the installer and then select Save . |

| Step 1 | Copy the installation package to a software distribution point for deployment. All computers or users to which you plan to deploy Cisco Jabber for Windows must be able to access the installation package on the distribution point. |
|---|---|
| Step 2 | Select Start > Run and then enter the following command: GPMC.msc The Group Policy Management console opens. |
| Step 3 | Create a new group policy object. Right-click on the appropriate domain in the left pane. Select Create a GPO in this Domain, and Link it here . The New GPO window opens. Enter a name for the group policy object in the Name field. Leave the default value or select an appropriate option from the Source Starter GPO drop-down list and then select OK . The new group policy displays in the list of group policies for the domain. |
| Step 4 | Set the scope of your deployment. Select the group policy object under the domain in the left pane. The group policy object displays in the right pane. Select Add in the Security Filtering section of the Scope tab. The Select User, Computer, or Group window opens. Specify the computers and users to which you want to deploy Cisco Jabber for
			 Windows . |
| Step 5 | Specify the installation package. Right-click the group policy object in the left pane and then select Edit . The Group Policy Management Editor opens. Select Computer Configuration and then select Policies > Software Settings . Right-click Software Installation and then select New > Package . Enter the location of the installation package next to File Name ; for example, \\server\software_distribution . Important: You must enter a Uniform Naming Convention (UNC) path as the location of the installation package. If you do not enter a UNC path, Group Policy cannot deploy Cisco Jabber for Windows. Select the installation package and then select Open . In the Deploy Software dialog box, select Assigned and then OK . |

| Step 1 | Download the 
			 Cisco
				Media Services Interface installation program from the download
			 site on cisco.com. |
|---|---|
| Step 2 | Install 
			 Cisco Media Services Interface on each computer on which you
			 install 
			 Cisco Jabber. See the
				appropriate 
				Cisco Medianet documentation for installing 
				Cisco Media Services Interface. |

| Step 1 | Open a command line window. |
|---|---|
| Step 2 | Enter the following command: msiexec.exe /x path_to_ CiscoJabberSetup.msi For example, msiexec.exe /x C:\Windows\Installer\ CiscoJabberSetup.msi /quiet Where /quiet specifies a silent uninstall. |

| Step 1 | Find the product code. Open the Microsoft Windows registry editor. Locate the following registry key: HKEY_CLASSES_ROOT\Installer\Products Select Edit > Find . Enter Cisco Jabber in the Find what text box in the Find window and select Find Next . Find the value of  the ProductIcon key. The product code is the value of  the ProductIcon key, for example, C:\Windows\Installer\{ product_code }\ARPPRODUCTICON.exe . Note The product code changes with each version of Cisco Jabber for Windows. | Note | The product code changes with each version of Cisco Jabber for Windows. |
|---|---|---|---|
| Note | The product code changes with each version of Cisco Jabber for Windows. |
| Step 2 | Open a command line window. |
| Step 3 | Enter the following command: msiexec.exe /x product_code For example, msiexec.exe /x 45992224-D2DE-49BB-B085-6524845321C7 /quiet Where /quiet specifies a silent uninstall. |

| Note | The product code changes with each version of Cisco Jabber for Windows. |
|---|---|

| Step 1 | To install Cisco Jabber for Android, download the app from Google Play from your mobile device. |
|---|---|
| Step 2 | To install Cisco Jabber for iPhone and iPad, download the app from the App Store from your mobile device. |