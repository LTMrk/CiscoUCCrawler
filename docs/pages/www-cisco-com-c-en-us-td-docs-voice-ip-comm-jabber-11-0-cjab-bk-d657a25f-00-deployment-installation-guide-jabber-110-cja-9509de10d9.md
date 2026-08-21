---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-9509de10d9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_01010.html
retrieved_at: 2026-08-21T19:21:04.803031+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: June 25, 2015

Chapter: Configure Client

## Chapter: Configure Client

# Configure Client

## Introduction to
	 Client Configuration

Service
			 Profiles — You can configure some client settings in UC service profiles on
			 Cisco Unified Communications Manager release 9 and later. When users launch the
			 client, it discovers the Cisco Unified Communications Manager home cluster
			 using a DNS SRV record and automatically retrieves the configuration from the
			 UC service profile.

Applies to
			 on-premises deployments only.

Phone
			 Configuration — You can set some client settings in the phone configuration on
			 Cisco Unified Communications Manager release 9 and later. The client retrieves
			 the settings from the phone configuration in addition to the configuration in
			 the UC service profile.

Applies to
			 on-premises deployments only.

Cisco Unified
			 Communications Manager IM and Presence Service — You can enable instant
			 messaging and presence capabilities and configure certain settings such as
			 presence subscription requests.

In the Advanced settings window, if you select either Cisco IM & Presence or Cisco Communications Manager 8.x , the client
			 retrieves UC services from Cisco Unified Presence or Cisco Unified
			 Communications Manager IM and Presence Service. The client does not use service
			 profiles or SSO discovery.

Applies to
			 on-premises deployments only.

Client
			 Configuration Files — You can create XML files that contain configuration
			 parameters. You then host the XML files on a TFTP server. When users sign in,
			 the client retrieves the XML file from the TFTP server and applies the
			 configuration.

Applies to
			 on-premises and cloud-based deployments.

Cisco WebEx
			 Administration Tool — You can configure some client settings with the Cisco
			 WebEx Administration Tool.

You
			 can upload a jabber-config.xml client configuration file into the
			 Cisco WebEx Administration Tool.   You can apply separate configuration files for groups in the Cisco WebEx Messenger Administration Tool. When the client successfully connects to Cisco
			 WebEx Messenger it downloads the XML file and  the
			 configuration is applied.

Settings in Cisco WebEx Messenger Administration Tool

Settings in jabber-config.xml file from Cisco WebEx Messenger Administration Tool.

Group configuration file settings  take priority over the configuration file in Cisco WebEx Messenger Administration Tool.

Settings in jabber-config.xml file from the TFTP server.

If there are any conflicts with configuration
			 settings, the settings set in Cisco WebEx Administration tool will take
			 priority over this configuration file.

Applies to
			 cloud-based deployments only.

## Configure Service
	 Profiles

You can configure
		  some client settings in UC service profiles on Cisco Unified Communications Manager version 9 and
		  later.

Cisco Jabber only retrieves configuration from
					 service profiles on Cisco Unified
						Communications Manager if the client gets the _cisco-uds SRV record from a DNS query.

In a
					 hybrid environment, if the CAS URL lookup is successful Cisco Jabber retrieves the configurations from 
					 Cisco WebEx Messenger service and the _cisco-uds SRV record is ignored.

In an
					 environment with multiple Cisco Unified
						Communications Manager clusters, you can configure the Intercluster
					 Lookup Service (ILS). ILS enables the client to find the user's home cluster
					 and discover services.

If you do
					 not configure ILS, then you must manually configure remote cluster information,
					 similar to the EMCC remote cluster set up. For more information on Remote
					 Cluster Configuration, see the Cisco Unified
						  Communications Manager Features and Services Guide .

### Set Parameters on Service Profile

The client can retrieve UC service configuration and other settings from service profiles.

#### Parameters in
	 Service Profiles

Learn which
		  configuration parameters you can set in service profiles. Review the
		  corresponding parameters in the client configuration file.

##### IM and
		  Presence Service Profile

Parameter

Description

Product type

Unified CM (IM and Presence Service) — Cisco Unified
							 Communications Manager IM and Presence Service is the authenticator.

As of this release, the client issues an HTTP query in addition
								  to the query for SRV records. The HTTP query allows the client to determine if
								  it should authenticate to the Cisco WebEx Messenger service.

As a result of the HTTP query, the client connects to the Cisco
								  WebEx Messenger service in cloud-based deployments before getting the _cisco-uds SRV record. Setting the value of the Product type field to WebEx may have no practical effect if the WebEx
								  service has already been discovered by a CAS lookup.

Not set — If the service profile does not contain an IM and
							 presence service configuration, the authenticator is Cisco Unified
								Communications Manager .

Primary server

On-Premises Deployments — You should specify the fully qualified
							 domain name (FQDN) of Cisco Unified Communications Manager IM and Presence
							 Service.

Cloud-Based Deployments — The client uses the following URL as
							 default when you select WebEx as the value for the Product type parameter:

```
https://loginp.webexconnect.com/cas/auth.do
```

This default URL overrides any value that you set.

##### Voicemail
		  Profile

Parameter

Description

Voicemail
						  server

Specifies connection settings for the voicemail server.

Credentials source for
						  voicemail service

Specifies that the client uses the credentials for the instant
						messaging and presence or conferencing service to authenticate with the
						voicemail service.

Ensure
						that the credentials source that you set match the user's voicemail
						credentials. If you set a value for this parameter, users cannot specify their
						voicemail service credentials in the client user interface.

##### Conferencing
		  Profile

Specifies connection settings for the conferencing server.

Specifies that the client uses the credentials for the instant
						messaging and presence or voicemail service to authenticate with the
						conferencing service.

Ensure
						that the credentials source that you set match the user's conferencing
						credentials.

##### Directory
		  Profile

See the Client
			 Configuration for Directory Integration chapter for information about
		  configuring directory integration in a service profile.

##### CTI
		  Profile

Specifies connection settings for the CTI server.

#### Add Cisco Unified Communications Manager Services

Add Cisco Unified Communications Manager services to specify the address, ports, protocols, and other settings for services such as IM and Presence Service , voicemail, conferencing, and directory.

The Find and List UC Services window opens.

The UC Service Configuration window opens.

Add your UC services to service profiles.

#### Create Service Profiles

After you add and configure Cisco Unified Communications Manager services, you add them to a service profile. You can apply additional configuration in the service profile.

The Find and List UC Services window opens.

The Service Profile Configuration window opens.

On Cisco Unified Communications Manager release 9.x only, users who have only instant messaging capabilities (IM only) must use the default service profile. For this reason, you should set the service profile as the default if you plan to apply the service profile to IM only users.

Apply service profiles to end user configuration.

#### Apply Service Profiles

After you add UC services and create a service profile, you apply the service profile to users. When users sign in to Cisco Jabber , the client can then retrieve the service profile for that user from Cisco Unified Communications Manager .

The Find and List Users window opens.

The End User Configuration window opens.

Cisco Unified Communications Manager release 9.x only: If the user has only IIM and Presence Service capabilities (IM only), you must select Use Default . For IM only users, Cisco Unified Communications Manager release 9.x always applies the default service profile regardless of what you select from the UC Service Profile drop-down list.

#### Associate Users with Devices

On Cisco Unified Communications Manager version 9.x only, when the client attempts to retrieve the service profile for the user, it first gets the device configuration file from Cisco Unified Communications Manager . The client can then use the device configuration to get the service profile that you applied to the user.

For example, you provision Adam McKenzie with a CSF device named CSFAKenzi . The client retrieves CSFAKenzi.cnf.xml from Cisco Unified Communications Manager when Adam signs in. The client then looks for the following in CSFAKenzi.cnf.xml :

```
<userId  serviceProfileFile=" identifier .cnf.xml">amckenzi</userId>
```

Associate users with devices.

Set the User Owner ID field in the device configuration to the appropriate user. The client will retrieve the Default Service Profile if this value is not set.

A CSF should not be associated to multiple users  if you intend to use different service profiles for these users.

- Open the Unified CM Administration interface.

- Select User Management > End User .

- Find and select the appropriate user. The End User Configuration window opens.

- Select Device Association in the Device Information section.

- Associate the user with devices as appropriate.

- Return to the End User Configuration window and then select Save .

- Select Device > Phone .

- Find and select the appropriate device. The Phone Configuration window opens.

- Locate the Device Information section.

- Select User as the value for the Owner field.

- Select the appropriate user ID from the Owner User ID field.

- Select Save .

### Set Parameters on
	 Phone Configuration for Desktop Clients

The client can
		  retrieve configuration settings in the phone configuration from the following
		  locations on Cisco Unified Communications Manager :

Applies to
				  the entire cluster.

For
						users with only IM and Presence Service capabilities (IM only), you must
						set phone configuration parameters in the Enterprise Phone Configuration window.

Applies to
				  groups of devices and takes priority over the cluster configuration.

Applies to
				  individual CSF devices and takes priority over the group configuration.

#### Parameters in
	 Phone Configuration

This
							 parameter is available only on the CSF device configuration.

Restricts users from transferring specific file types.

Set a
						file extension as the value, for example, .exe .

Use a
						semicolon to delimit multiple values, for example,

```
.exe;.msi;.rar;.zip
```

Specifies the URL to the XML file that holds client update
						information. The client uses this URL to retrieve the XML file from your web
						server.

In
						hybrid cloud-based deployments, you should use the Cisco WebEx Administration
				  Tool to configure automatic updates.

Specifies the URL for the custom script that allows users to
						submit problem reports.

### Set Parameters on
	 Phone Configuration for Mobile Clients

Cisco Dual
				Mode for iPhone (TCT) Configuration 
			  — Applies to
				  individual TCT devices and takes priority over the group configuration.

Cisco Jabber
				for Tablet (TAB) Configuration 
			  — Applies to
				  individual TAB devices and takes priority over the group configuration.

#### Parameters in
	 Phone Configuration

Parameter

Description

On-Demand VPN
						URL

Preset Wi-fi
						Networks

Enter
						the SSIDs for Wi-Fi networks (SSIDs) approved by your organization. Separate
						SSIDs with a forward slash (/). Devices do not connect to secure connect if
						connected to one of the entered Wi-Fi networks.

Default
						Ringtone

Sets the
						default ringtone to Normal or Loud .

Video
						Capabilities

Enabled (default) — Users can send and receive video calls.

Disabled 
						   — Users cannot send or receive video calls.

TCT
						and BOT devices only.

Enabled 
						   — Users can dial via office.

Disabled (default) 
						   — Users cannot dial via office.

## Create and Host
	 Client Configuration Files

For on-premises and
		  hybrid cloud-based deployments, create client configuration files and
		  host them on the Cisco Unified Communications Manager TFTP service.

For cloud-based
		  deployments, configure the client with the 
		  Cisco WebEx Administration Tool. However, you can optionally set up
		  a TFTP server to configure the client with settings that are not available in 
		  Cisco WebEx Administration Tool.

For Cisco Jabber for iPhone and iPad and Cisco Jabber for Android, you
				must create a global configuration file to set up:

Directory
					 integration for on-premises deployments.

Voicemail
					 service credentials for hybrid-cloud deployments.

In
				most environments, Cisco Jabber for Windows and Cisco Jabber for Mac do not require any configuration to connect to
				services. Create a configuration file only if you require custom
				content such as automatic updates, problem reporting, or user policies and options.

Note the following configuration file requirements:

Configuration filenames are case-sensitive. Use lowercase letters in the
						filename to prevent errors and to ensure the client can retrieve the file
						from the TFTP server.

You must use utf-8 encoding for the configuration files.

The client cannot read configuration files that do not have a valid XML
						structure. Check the structure of your configuration file for closing
						elements and confirm that elements are nested correctly.

Valid XML character entity references only are permitted in your
						configuration file. For example, use &amp; instead of & . If your XML contains invalid characters, the client
						cannot parse the configuration file.

To validate your
						configuration file, open the file in Microsoft Internet Explorer.

If Internet
								Explorer displays the entire XML structure, your configuration file
								does is valid.

If Internet
								Explorer displays only part of the XML structure, it is likely that
								your configuration file contains invalid characters or entities.

Specify your TFTP server address for client to enable access to
				your configuration file.

Configure the clients for users in your deployment.

Apply different configuration to different set of users.

Host configuration files on any TFTP server.

Restart the TFTP server before the client can access the
				configuration files.

### Specify Your TFTP Server Address

The client gets configuration files from a TFTP server. The first step in configuring the client is to specify your TFTP server address so the client can access your configuration file.

If Cisco Jabber gets the _cisco-uds SRV record from a DNS query, it can automatically locate the user's home cluster. As a result, the client can also locate the Cisco Unified Communications Manager TFTP service.

You do not need to specify your TFTP server address if you deploy the _cisco-uds SRV record.

#### Specify Your TFTP Server on Cisco Unified Presence

If you are using Cisco Unified Communications Manager release 8.x, complete the steps to  specify the address of your TFTP server on Cisco Unified Presence. If you are using Cisco Unified Communications Manager release 9.x, then you do not need to follow the steps below.

In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > Settings .

The Cisco Jabber Settings window opens.

Cisco Jabber Security Settings

CUPC Global Settings

Primary TFTP Server

Backup TFTP Server

Backup TFTP Server

Ensure that you enter the fully qualified domain name (FQDN) or IP address for the TFTP servers rather than a host name.

#### Specify Your TFTP
	 Server on Cisco Unified Communications Manager IM and Presence Service

If you are using Cisco Unified Communications Manager release 9.x, then
		  you do not need to follow the steps below.

The Legacy Client Settings window opens.

Primary TFTP
						Server

Backup TFTP
						Server

Backup TFTP
						Server

#### Specify TFTP Servers in Phone Mode

Users manually enter the TFTP server address when they start the client.

You specify the TFTP server address during installation with the TFTP argument.

You specify the TFTP server address in the Microsoft Windows registry.

#### Specify TFTP
	 Servers with the Cisco WebEx Administration Tool

If the client
		  connects to the 
		  Cisco WebEx Messenger service, you specify your TFTP
		  server address with the 
		  Cisco WebEx Administrator Tool.

### Create Global Configurations

The client downloads the global configuration file from your TFTP server during the login sequence. Configure the client for all users in your deployment.

If the structure of your configuration file is not valid, the client cannot read the values you set. Review the XML  samples in this chapter for more information.

Use lowercase letters in the filename.

Use UTF-8 encoding.

If your environment has  multiple TFTP servers, ensure that the configuration file is the same on all TFTP servers.

### Create Group
	 Configurations

Group
		  configuration files apply to subsets of users and are supported on  Cisco Jabber
		  for desktop (CSF devices) and on Cisco Jabber for mobile devices. Group
		  configuration files take priority over global configuration files.

If you provision
		  users with CSF devices, specify the group configuration filenames in the Cisco
			 Support Field field on the device configuration. If users do not
		  have CSF devices, set a unique configuration filename for each group during
		  installation with the TFTP_FILE_NAME argument.

If you have
				Cisco Unified Communications Manager 8.6, the Cisco Support Field field does not exist. Download
				the ciscocm.addcsfsupportfield.cop COP file from the Cisco Jabber
				administration package to your file system and deploy to Cisco Unified
				Communications Manager. For more information about deploying COP files, see the Cisco Unified Communications Manager documentation.

The COP file
				adds the Cisco Support Field field to CSF devices in the Desktop Client Settings section on the Phone Configuration window.

If the
				structure of your configuration file is not valid, the client cannot read the
				values you set. Review the XML samples in this chapter for more information.

The group
				configuration file can have any appropriate name; for example, jabber-groupa-config.xml .

- Open the Cisco Unified CM Administration interface.

- Select Device > Phone .

- Find and
				  select the appropriate CSF device to which the group configuration applies.

- In the Phone Configuration window, navigate to Product Specific
						Configuration Layout > Desktop Client Settings .

If you
						host the group configuration file on your TFTP server in a location other than
						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml .

Do not
						add more than one group configuration file. The client uses only the first
						group configuration in the Cisco Support Field field.

- Select Save .

### Host Configuration Files

You can host configuration files on any TFTP server. However, Cisco recommends hosting configuration files on the Cisco Unified Communications Manager TFTP server, which is the same as that where the device configuration file resides.

You should leave an empty value in the Directory text box so that the configuration file resides in the default directory of the TFTP server.

### Restart Your TFTP Server

You must restart your TFTP server before the client can access the configuration files.

A window displays to prompt you to confirm the restart.

The Cisco Tftp Service Restart Operation was Successful status displays.

To verify that the configuration file is available on your TFTP server, open the configuration file in any browser. Typically, you can access the global configuration file at the following URL: http:// tftp_server_address :6970/jabber-config.xml

### Configuration
	 File

For detailed information on the jabber-config.xml configuration file structure, group
		  elements, parameters, and examples, see the Parameters Reference Guide for Cisco Jabber .

## Configure Proxy
	 Settings

The client uses
		  proxy settings to connect to services.

- Proxy Authentication is
			 not supported.

- Wildcards in the bypass
			 list are not supported. Use example.com instead of *.example.com .

- Web Proxy Auto-Discovery
			 (WPAD) protocol lookup is only supported for iOS devices.

Cisco Jabber supports proxy for HTTP request using HTTP CONNECT,
				but does not support proxy when using HTTPS CONNECT.

### Configure Proxy
	 Settings for Cisco Jabber for Windows

Configure proxy
		  settings for Windows in the Local Area Network (LAN) settings for Internet
		  properties.

- For automatic
				configuration, specify a .pac file URL.

- For Proxy Server, specify
				an explicit proxy address.

### Configure Proxy
	 Settings for Cisco Jabber for Mac

Configure proxy
		  settings for Mac in System
			 Preferences .

- For automatic
				configuration, specify a .pac file URL.

- For Proxy Server, specify
				an explicit proxy address.

### Configure Proxy
	 Settings for Cisco Jabber iPhone and iPad

Configure proxy settings in the Wi-Fi settings of an iOS device using
		  one of the following methods:

### Configure Proxy
	 Settings for Cisco Jabber for Android

This
					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
					 series devices.

- Specify an explicit proxy
				address in the Wi-Fi
					 Networks > Modify Network > Show Advanced
					 Options > Proxy Settings > Auto tab.

## Problem
	 Reporting

Applies to: Cisco Jabber for Windows

Users submit
				the problem report directly through the client interface.

Users save the
				problem report locally and then upload it at a later time.

The client uses an
		  HTTP POST method to submit problem reports. Create a custom script to accept
		  the POST request and specify the URL of the script on your 
		  HTTP server
		  as a configuration parameter. Because users can save problem reports locally,
		  you should also create an HTML page with a form to enable users to upload
		  problem reports.

- Install and configure an 
			 HTTP server.

- Create a custom script to
			 accept the HTTP POST request.

- Create an HTML page that
			 enables users to upload problem reports that are saved locally. Your HTML page
			 should contain a form that accepts the problem report saved as a .ZIP archive and contains an action to post the
			 problem report using your custom script.

The following is
		  an example form that accepts problem reports:

```
<form name="uploadPrt" action="http://server_name.com/scripts/UploadPrt.php" method="post" enctype="multipart/form-data">
 <input type="file" name="zipFileName" id="zipFileName" /><br />
 <input type="submit" name="submitBtn" id="submitBtn" value="Upload File" />
</form>
```

## Configure
	 Automatic Updates

Applies to: Cisco Jabber for Windows, Cisco Jabber for Mac

If you use
				the Cisco WebEx Messenger service for instant messaging and presence
				capabilities, you should use the Cisco WebEx Administration Tool to configure
				automatic updates.

XML files
				for automatic updates have the following structure:

```
<JabberUpdate>
          <App name=”JabberWin”>
               <LatestBuildNum>12345</LatestBuildNum>
               <LatestVersion>10.5.x</LatestVersion>
               <Mandatory>true</Mandatory>
               <Message>
                  <![CDATA[<b>This new version of Cisco Jabber lets you do the
                  following:</b><ul><li>Feature 1</li><li>Feature 2</li></ul>For
                  more information click <a target="_blank"
                  href="http://cisco.com/go/jabber">here</a>.]]>
               </Message>
               <DownloadURL>http://http_server_name/CiscoJabberSetup.msi</DownloadURL>
          </App>
        </JabberUpdate>
```

The
				following is example XML file for automatic updates:

```
<JabberUpdate>
<App name="JabberWin">
  <LatestBuildNum> 12345 </LatestBuildNum>
  <LatestVersion> 9.x </LatestVersion>
  <Message> <![CDATA[<b>This new version of Cisco Jabber lets you do the following:</b><ul><li>Feature 1</li><li>Feature 2</li></ul>For 
  more information click <a target="_blank" href="http://cisco.com/go/jabber">here</a>.]]> </Message>
  <DownloadURL> http://http_server_name/CiscoJabberSetup.msi </DownloadURL>
</App>
</JabberUpdate>
```

The
				following is an example XML file for automatic updates for both Cisco Jabber for
				Windows and Cisco Jabber for Mac:

```
<JabberUpdate>
	<App name="JabberMac">
  <LatestBuildNum>12345</LatestBuildNum>
  <LatestVersion>9.6.1</LatestVersion>
  <Message><![CDATA[<b>This new version of Cisco Jabber lets you do the following:</b><ul><li>Feature 1</li><li>Feature 2</li>
  </ul>For more information click <a target="_blank" href="http://cisco.com/go/jabber">here</a>.]]>
  </Message>   
  <DownloadURL>http://http_server_name/Cisco-Jabber-Mac-9.6.1-12345-MrbCdd.zip</DownloadURL>
 </App>
	<App name="JabberWin">
  <LatestBuildNum>12345</LatestBuildNum>
  <LatestVersion>9.0</LatestVersion>
  <Message><![CDATA[<b>This new version of Cisco Jabber lets you do the following:</b><ul><li>Feature 1</li><li>Feature 2
  </li></ul>For more information click <a target="_blank" href="http://cisco.com/go/jabber">here</a>.]]>
  </Message> 
  <DownloadURL>http://http_server_name/CiscoJabberSetup.msi
  </DownloadURL>
</App>
</JabberUpdate>
```

Install and
				configure an HTTP server to host the XML file and installation package.

Ensure users
				have permission to install software updates on their workstations.

Microsoft Windows stops
				update installations if users do not have administrative rights on their
				workstations. You must be logged in with administrative rights to complete
				installation.

JabberWin—The update applies to Cisco Jabber for Windows.

JabberMac—The update applies to Cisco Jabber for Mac.

LatestBuildNum —Build number of the update.

LatestVersion —Version number of the update.

Mandatory —(Windows clients only) True or False.
					 Determines whether users must upgrade their client version when prompted.

Message —HTML in the following format:

```
<![CDATA[ your_html ]]>
```

DownloadURL —URL of the installation package on your
					 HTTP server.

```
Cisco-Jabber-Mac- version - size - dsaSignature .zip
```

## Custom Embedded
	 Tabs

The Jabber embedded browser does not support cookie sharing with pop-ups from SSO enabled webpages. The content on the pop-up window may fail to load.

### Custom Embedded
	 Tab Definitions

```
<jabber-plugin-config>
	<browser-plugin>
		<page refresh="" preload="">
			<tooltip></tooltip>
			<icon></icon>
			<url></url>
		</page>
	</browser-plugin>
</jabber-plugin-config>
```

Cisco Jabber for Windows supports Internet Explorer version 9 or earlier. The client uses Internet Explorer in version 9 mode if a later version is on the workstation.

browser-plugin

Contains all definitions for custom embedded tabs.

The
						value includes all custom tab definitions.

page

Contains one custom embedded tab definition.

refresh

true
							 — Content refreshes each time users select the tab.

false (default) — Content refreshes when users restart the
							 client or sign in.

This parameter is optional
						and is an attribute of the page element.

preload

true
							 — Content loads when the client starts.

false (default) — Content loads when users select the tab.

This
						parameter is optional and is an attribute of the page element.

tooltip

Defines hover text for the
						custom embedded tab.

This parameter is optional.
						If you do not specify the hover text, the client will use Custom tab .

The
						value is string of unicode characters.

icon

Local icon—Specify the URL as follows: file:// file_path / icon_name

Hosted icon—Specify the URL as follows: http:// path / icon_name

You can use any icon that the client browser can render can render, including .JPG, .PNG, and .GIF formats.

This parameter is optional. If you do not specify an icon, the client loads the favicon from the HTML page. If no favicon is available, the client loads the default icon.

url

Specifies the URL where the content for the embedded tab
						resides.

The client uses the browser rendering engine to display the content of the embedded tab. For this reason, you can specify any content that the browser supports.

This parameter is
						required.

### User Custom
	 Tabs

Users can create
		  their own custom embedded tabs through the client user interface.

```
<Options>
  <AllowUserCustomTabs>true</AllowUserCustomTabs>
</Options>
```

User custom
				embedded tabs are set to true by default.

### Custom Icons

Dimensions: 20 x 20 pixels

Transparent background

PNG file
					 format

### Chats and Calls from Custom Tabs

- Use the XMPP: or IM: protocol handler to start chats.

- Use the TEL: protocol handler to start audio and video calls.

### UserID Tokens

You can specify the ${UserID} token as part of the value for the url parameter. When users sign in, the client replaces the ${UserID} token with the username of the logged in user.

You can also specify the ${UserID} token in query strings; for example, www.cisco.com/mywebapp.op?url=${UserID} .

You specify the following in your custom embedded tab:

```
<url>www.cisco.com/${UserID}/profile</url>
```

Mary Smith signs in. Her username is msmith.

The client replaces the ${UserID} token with Mary's username as follows:

```
<url>www.cisco.com/msmith/profile</url>
```

### JavaScript
	 Notifications

You can implement
		  JavaScript notifications in custom embedded tabs. This topic describes the
		  methods the client provides for JavaScript notifications. This topic also gives
		  you an example JavaScript form that you can use to test notifications. It is
		  beyond the scope of this documentation to describe how to implement JavaScript
		  notifications for asynchronous server calls and other custom implementations.
		  You should refer to the appropriate JavaScript documentation for more
		  information.

#### Notification
		  Methods

Empty —
					 An empty value removes any existing notification badge.

A number
					 from 1 to 999

Two
					 digit alphanumeric combinations, for example, A1

onPageSelected() — The client invokes this method when users
				select the custom embedded tab.

onPageDeselected() — The client invokes this method when users
				select another tab.

Not applicable for Jabber for iPhone and iPad

onHubResized() — The client invokes this method when users
				resize or move the client hub window.

onHubActivated() — The client invokes this method when the
				client hub windows is activated.

onHubDeActivated() — The client invokes this method when the
				client hub window is deactivated.

#### Subscribe to
		  Presence in Custom Tabs

SubscribePresence() — Specify a string value using the IM
				address of a user for this method.

IM
					 address

Basic
					 presence (Available, Away, Offline, Do Not Disturb)

Rich
					 presence (In a meeting, On a call, or a custom presence state)

If you subscribe to the presence of a person who is not on your
				  contact list (also called temporary presence subscription ), the subscription
				  expires after 68 minutes. After the subscription expires, you must re-subscribe
				  to the person’s presence in order to continue to receive presence updates.

Jabber for iPad and iPhone only supports OnPresenceStateChanged.

#### Get Locale
		  Information in Custom Tabs

GetUserLocale() — This method enables users to request locale
				information from the client.

OnLocaleInfoAvailable — This method enables users to receive
				locale information from client. You can use a string value that contains the
				client locale information.

Jabber for iPad and iPhone only supports OnLocaleInfoAvailable.

#### Example
		  JavaScript

```
<html>
        <head>
                <script type="text/javascript"> function OnPresenceStateChanged(jid, basicPresence, localizedPresence) 
                                 {
                                          var cell = document.getElementById(jid);
                                          cell.innerText = basicPresence.concat(", ",localizedPresence);                                                   
                                 }              
                                                           
                                 function GetUserLocale()
                                 {
                                          window.external.GetUserLocale();
                                 }
                                                           
                                 function SubscribePresence() 
                                 {
                                          window.external.SubscribePresence('johndoe@example.com');
                                 }
                                                           
                                 function OnLocaleInfoAvailable(currentLocale)
                                 {
                                          var cell = document.getElementById("JabberLocale");
                                          cell.innerText = currentLocale;
                                 } function onHubActivated()
                                 {
                                          var cell = document.getElementById("hubActive");
                                          cell.innerText = "TRUE";
                                 }
                                                                
                                 function onHubDeActivated()
                                 {
                                          var cell = document.getElementById("hubActive");
                                          cell.innerText = "FALSE";
                                 }
 
                                 function onHubResized()
                                 {
                                          alert("Hub Resized or Moved");
                                 }                              
                                                                
                                 function OnLoadMethods()
                                 {
                                          SubscribePresence();
                                          GetUserLocale();
                                 }
                     </script>
               </head>
 
               <body onload="OnLoadMethods()">
                     <table>
                                 <tr>
                                             <td>John Doe</td>
                                             <td id="johndoe@example.com">unknown</td>
                                 </tr>
                    </table>
                    <table>
                                 <tr>
                                             <td>Jabber Locale: </td>
                                             <td id="JabberLocale">Null</td>
                                 </tr>
                                 <tr>
                                             <td>Hub Activated: </td>
                                             <td id="hubActive">---</td>
                                 </tr>     
                   </table>
               </body>
 
</html>
```

To test this
		  example JavaScript form, copy the preceding example into an HTML page and then
		  specify that page as a custom embedded tab.

### Show Call Events in Custom Tabs

You can use the following JavaScript function to show call events in a custom tab:

OnTelephonyConversationStateChanged — An API in the telephony service enables the client to show call events in a custom embedded tab. Custom tabs can implement the OnTelephonyConversationStateChanged JavaScript function. The client calls this function every time a telephony conversation state changes. The function accepts a JSON string that the client parses to get call events.

The following snippet shows the JSON that holds the call events:

```
{
      "conversationId": string,
      "acceptanceState": "Pending" | "Accepted| | "Rejected",
      "state": "Started" | "Ending" | "Ended",
      "callType": "Missed" | "Placed" | "Received" | "Passive" | "Unknown",
      "remoteParticipants": [{participant1}, {participant2}, …, {participantN}],
      "localParticipant": {
      }
}
```

Each participant object in the JSON can have the following properties:

```
{
      "voiceMediaDisplayName": "<displayName>",
      "voiceMediaNumber": "<phoneNumber>",
      "translatedNumber": "<phoneNumber>",
      "voiceMediaPhoneType": "Business" | "Home" | "Mobile" | "Other" | "Unknown",
      "voiceMediaState": "Active" | "Inactive" | "Pending" | "Passive" | "Unknown",
}
```

The following is an example implementation of this function in a custom embedded tab. This example gets the values for the state and acceptanceState properties and shows them in the custom tab.

```
function OnTelephonyConversationStateChanged(json) {
      console.log("OnTelephonyConversationStateChanged");
      try {
        var conversation = JSON.parse(json);
        console.log("conversation id=" + conversation.conversationId);
        console.log("conversation state=" + conversation.state);
        console.log("conversation acceptanceState=" + conversation.acceptanceState);
        console.log("conversation callType=" + conversation.callType);        
      }
      catch(e) {
        console.log("cannot parse conversation:" + e.message);
      }
    }
```

The following is an example implementation of this function with all possible fields:

```
function OnTelephonyConversationStateChanged(json) {
      console.log("OnTelephonyConversationStateChanged");
      try {
        var conversation = JSON.parse(json);
        console.log("conversation state=" + conversation.state);
        console.log("conversation acceptanceState=" + conversation.acceptanceState);
        console.log("conversation callType=" + conversation.callType);
        for (var i=0; i<conversation.remoteParticipants.length; i++) {
          console.log("conversation remoteParticipants[" + i + "]=");
          console.log("voiceMediaDisplayName=" + conversation.remoteParticipants[i].voiceMediaDisplayName);
          console.log("voiceMediaNumber=" + conversation.remoteParticipants[i].voiceMediaNumber);
          console.log("translatedNumber=" + conversation.remoteParticipants[i].translatedNumber);
          console.log("voiceMediaPhoneType=" + conversation.remoteParticipants[i].voiceMediaPhoneType);
          console.log("voiceMediaState=" + conversation.remoteParticipants[i].voiceMediaState);
        }
        console.log("conversation localParticipant=");
        console.log("  voiceMediaDisplayName=" + conversation.localParticipant.voiceMediaDisplayName);
        console.log("  voiceMediaNumber=" + conversation.localParticipant.voiceMediaNumber);
        console.log("  translatedNumber=" + conversation.localParticipant.translatedNumber);
        console.log("  voiceMediaPhoneType=" + conversation.localParticipant.voiceMediaPhoneType);
        console.log("  voiceMediaState=" + conversation.localParticipant.voiceMediaState);
      }
      catch(e) {
        console.log("cannot parse conversation:" + e.message);
      }
    }
```

### Custom Embedded Tab Example

```
<?xml version="1.0" encoding="utf-8"?>
<config version="1.0">
 <Client>
  <jabber-plugin-config>
   <browser-plugin>
     <page refresh ="true" preload="true">
     <tooltip>Cisco</tooltip>
     <icon>https://www.cisco.com/web/fw/i/logo.gif</icon>
     <url>https://www.cisco.com</url>
    </page>
   </browser-plugin>
  </jabber-plugin-config>
 </Client>
</config>
```

| Note | Group configuration file settings  take priority over the configuration file in Cisco WebEx Messenger Administration Tool. |
|---|---|

| Parameter | Description |
|---|---|
| Product type | Provides the source of authentication to Cisco Jabber and has
						the following values: Unified CM (IM and Presence Service) — Cisco Unified
							 Communications Manager IM and Presence Service is the authenticator. WebEx (IM and Presence Service) — The Cisco WebEx Messenger
							 service is the authenticator. Note As of this release, the client issues an HTTP query in addition
								  to the query for SRV records. The HTTP query allows the client to determine if
								  it should authenticate to the Cisco WebEx Messenger service. As a result of the HTTP query, the client connects to the Cisco
								  WebEx Messenger service in cloud-based deployments before getting the _cisco-uds SRV record. Setting the value of the Product type field to WebEx may have no practical effect if the WebEx
								  service has already been discovered by a CAS lookup. Not set — If the service profile does not contain an IM and
							 presence service configuration, the authenticator is Cisco Unified
								Communications Manager . | Note | As of this release, the client issues an HTTP query in addition
								  to the query for SRV records. The HTTP query allows the client to determine if
								  it should authenticate to the Cisco WebEx Messenger service. As a result of the HTTP query, the client connects to the Cisco
								  WebEx Messenger service in cloud-based deployments before getting the _cisco-uds SRV record. Setting the value of the Product type field to WebEx may have no practical effect if the WebEx
								  service has already been discovered by a CAS lookup. |
| Note | As of this release, the client issues an HTTP query in addition
								  to the query for SRV records. The HTTP query allows the client to determine if
								  it should authenticate to the Cisco WebEx Messenger service. As a result of the HTTP query, the client connects to the Cisco
								  WebEx Messenger service in cloud-based deployments before getting the _cisco-uds SRV record. Setting the value of the Product type field to WebEx may have no practical effect if the WebEx
								  service has already been discovered by a CAS lookup. |
| Primary server | Specifies the address of your primary presence server. On-Premises Deployments — You should specify the fully qualified
							 domain name (FQDN) of Cisco Unified Communications Manager IM and Presence
							 Service. Cloud-Based Deployments — The client uses the following URL as
							 default when you select WebEx as the value for the Product type parameter: https://loginp.webexconnect.com/cas/auth.do This default URL overrides any value that you set. |

| Note | As of this release, the client issues an HTTP query in addition
								  to the query for SRV records. The HTTP query allows the client to determine if
								  it should authenticate to the Cisco WebEx Messenger service. As a result of the HTTP query, the client connects to the Cisco
								  WebEx Messenger service in cloud-based deployments before getting the _cisco-uds SRV record. Setting the value of the Product type field to WebEx may have no practical effect if the WebEx
								  service has already been discovered by a CAS lookup. |
|---|---|

| Parameter | Description |
|---|---|
| Voicemail
						  server | Specifies connection settings for the voicemail server. |
| Credentials source for
						  voicemail service | Specifies that the client uses the credentials for the instant
						messaging and presence or conferencing service to authenticate with the
						voicemail service. Ensure
						that the credentials source that you set match the user's voicemail
						credentials. If you set a value for this parameter, users cannot specify their
						voicemail service credentials in the client user interface. |

| Conferencing Service Configuration | Description |
|---|---|
| Conferencing
						server | Specifies connection settings for the conferencing server. |
| Credentials source for
						web conference service | Specifies that the client uses the credentials for the instant
						messaging and presence or voicemail service to authenticate with the
						conferencing service. Ensure
						that the credentials source that you set match the user's conferencing
						credentials. |

| CTI Service Configuration | Description |
|---|---|
| CTI server | Specifies connection settings for the CTI server. |

| Step 1 | Open the Cisco Unified CM
Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > UC Service . The Find and List UC Services window opens. |
| Step 3 | Select Add New . The UC Service Configuration window opens. |
| Step 4 | Select the UC service type you want to add and then select Next . |
| Step 5 | Configure the UC service as appropriate and then select Save . |

| Step 1 | Open the Cisco Unified CM
Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . The Find and List UC Services window opens. |
| Step 3 | Select Add New . The Service Profile Configuration window opens. |
| Step 4 | Enter a name for the service profile in the Name field. |
| Step 5 | Select Make this the default service profile for the system if you want the service profile to be the default for the cluster. Note On Cisco Unified Communications Manager release 9.x only, users who have only instant messaging capabilities (IM only) must use the default service profile. For this reason, you should set the service profile as the default if you plan to apply the service profile to IM only users. | Note | On Cisco Unified Communications Manager release 9.x only, users who have only instant messaging capabilities (IM only) must use the default service profile. For this reason, you should set the service profile as the default if you plan to apply the service profile to IM only users. |
| Note | On Cisco Unified Communications Manager release 9.x only, users who have only instant messaging capabilities (IM only) must use the default service profile. For this reason, you should set the service profile as the default if you plan to apply the service profile to IM only users. |
| Step 6 | Add your UC services, apply any additional configuration, and then select Save . |

| Note | On Cisco Unified Communications Manager release 9.x only, users who have only instant messaging capabilities (IM only) must use the default service profile. For this reason, you should set the service profile as the default if you plan to apply the service profile to IM only users. |
|---|---|

| Step 1 | Open the Cisco Unified CM
Administration interface. |
|---|---|
| Step 2 | Select User Management > End User . The Find and List Users window opens. |
| Step 3 | Enter the appropriate search criteria to find existing users and then select a user from the list. The End User Configuration window opens. |
| Step 4 | Locate the Service Settings section. |
| Step 5 | Select a service profile to apply to the user from the UC Service Profile drop-down list. Important: Cisco Unified Communications Manager release 9.x only: If the user has only IIM and Presence Service capabilities (IM only), you must select Use Default . For IM only users, Cisco Unified Communications Manager release 9.x always applies the default service profile regardless of what you select from the UC Service Profile drop-down list. |
| Step 6 | Apply any other configuration as appropriate and then select Save . |

| Note | A CSF should not be associated to multiple users  if you intend to use different service profiles for these users. |
|---|---|

| Step 1 | Associate users with devices. Open the Unified CM Administration interface. Select User Management > End User . Find and select the appropriate user. The End User Configuration window opens. Select Device Association in the Device Information section. Associate the user with devices as appropriate. Return to the End User Configuration window and then select Save . |
|---|---|
| Step 2 | Set the User Owner ID field in the device configuration. Select Device > Phone . Find and select the appropriate device. The Phone Configuration window opens. Locate the Device Information section. Select User as the value for the Owner field. Select the appropriate user ID from the Owner User ID field. Select Save . |

| Note | For
						users with only IM and Presence Service capabilities (IM only), you must
						set phone configuration parameters in the Enterprise Phone Configuration window. |
|---|---|

| Desktop Client Settings Configuration | Description |
|---|---|
| Video Calling | Enables
						or disables video capabilities. Enabled (default) Users can send and receive video calls. Disabled Users cannot send or receive video calls. Restriction: This
							 parameter is available only on the CSF device configuration. |
| File Types to Block in File
						Transfer | Restricts users from transferring specific file types. Set a
						file extension as the value, for example, .exe . Use a
						semicolon to delimit multiple values, for example, .exe;.msi;.rar;.zip |
| Automatically Start in
						Phone Control | Sets the
						phone type for users when the client starts for the first time. Users can
						change their phone type after the initial start. The client then saves the user
						preference and uses it for subsequent starts. Enabled Use
							 the desk phone device for calls. Disabled (default) Use the software phone (CSF) device for calls. |
| Jabber For Windows Software
						Update Server URL | Specifies the URL to the XML file that holds client update
						information. The client uses this URL to retrieve the XML file from your web
						server. In
						hybrid cloud-based deployments, you should use the Cisco WebEx Administration
				  Tool to configure automatic updates. |
| Problem Report Server
						URL | Specifies the URL for the custom script that allows users to
						submit problem reports. |

| Parameter | Description |
|---|---|
| On-Demand VPN
						URL | URL for
						initiating on-demand VPN. Note Applicable for iOS
						  only. | Note | Applicable for iOS
						  only. |
| Note | Applicable for iOS
						  only. |
| Preset Wi-fi
						Networks | Enter
						the SSIDs for Wi-Fi networks (SSIDs) approved by your organization. Separate
						SSIDs with a forward slash (/). Devices do not connect to secure connect if
						connected to one of the entered Wi-Fi networks. |
| Default
						Ringtone | Sets the
						default ringtone to Normal or Loud . |
| Video
						Capabilities | Enables
						or disables video capabilities. Enabled (default) — Users can send and receive video calls. Disabled 
						   — Users cannot send or receive video calls. |
| Dial via Office Note TCT
						and BOT devices only. | Note | TCT
						and BOT devices only. | Enables
						or disables Dial via Office. Enabled 
						   — Users can dial via office. Disabled (default) 
						   — Users cannot dial via office. |
| Note | TCT
						and BOT devices only. |

| Note | Applicable for iOS
						  only. |
|---|---|

| Note | TCT
						and BOT devices only. |
|---|---|

| Note | In
				most environments, Cisco Jabber for Windows and Cisco Jabber for Mac do not require any configuration to connect to
				services. Create a configuration file only if you require custom
				content such as automatic updates, problem reporting, or user policies and options. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Specify Your TFTP Server Address | Specify your TFTP server address for client to enable access to
				your configuration file. |
| Step 2 | Create Global Configurations | Configure the clients for users in your deployment. |
| Step 3 | Create Group Configurations | Apply different configuration to different set of users. |
| Step 4 | Host Configuration Files | Host configuration files on any TFTP server. |
| Step 5 | Restart Your TFTP Server | Restart the TFTP server before the client can access the
				configuration files. |

| Step 1 | Open the Cisco Unified Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Cisco Jabber > Settings . Note In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > Settings . The Cisco Jabber Settings window opens. | Note | In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > Settings . |
| Note | In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > Settings . |
| Step 3 | Locate the fields to specify TFTP servers in one of the following sections, depending on your version of Cisco Unified Presence: Cisco Jabber Security Settings CUPC Global Settings |
| Step 4 | Specify the IP address of your primary and backup TFTP servers in the following fields: Primary TFTP Server Backup TFTP Server Backup TFTP Server Note Ensure that you enter the fully qualified domain name (FQDN) or IP address for the TFTP servers rather than a host name. | Note | Ensure that you enter the fully qualified domain name (FQDN) or IP address for the TFTP servers rather than a host name. |
| Note | Ensure that you enter the fully qualified domain name (FQDN) or IP address for the TFTP servers rather than a host name. |
| Step 5 | Select Save . |

| Note | In some versions of Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal Communicator > Settings . |
|---|---|

| Note | Ensure that you enter the fully qualified domain name (FQDN) or IP address for the TFTP servers rather than a host name. |
|---|---|

| Step 1 | Open the Cisco
				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Legacy
				  Clients > Settings . The Legacy Client Settings window opens. |
| Step 3 | Locate the Legacy
				Client Security Settings section. |
| Step 4 | Specify the IP
			 address of your primary and backup TFTP servers in the following fields: Primary TFTP
						Server Backup TFTP
						Server Backup TFTP
						Server |
| Step 5 | Select Save . |

| Step 1 | Open the 
			 Cisco WebEx Administrator Tool. |
|---|---|
| Step 2 | Select the Configuration tab. |
| Step 3 | Select Unified Communications in the Additional Services section. The Unified Communications window opens. |
| Step 4 | Select the Clusters tab. |
| Step 5 | Select the
			 appropriate cluster from the list. The Edit
				Cluster window opens. |
| Step 6 | Select Advanced Server Settings in the Cisco
				Unified Communications Manager Server Settings section. |
| Step 7 | Specify the IP
			 address of your primary TFTP server in the TFTP
				Server field. |
| Step 8 | Specify the IP
			 address of your backup TFTP servers in the Backup
				Server #1 and Backup
				Server #2 fields. |
| Step 9 | Select Save . The Edit
				Cluster window closes. |
| Step 10 | Select Save in the Unified Communications window. |

| Step 1 | Create a file named jabber-config.xml with any text editor. Use lowercase letters in the filename. Use UTF-8 encoding. |
|---|---|
| Step 2 | Define the required configuration parameters in jabber-config.xml . |
| Step 3 | Host the group configuration file on your TFTP server. If your environment has  multiple TFTP servers, ensure that the configuration file is the same on all TFTP servers. |

| Step 1 | Create an XML
			 group configuration file with any text editor. The group
				configuration file can have any appropriate name; for example, jabber-groupa-config.xml . |
|---|---|
| Step 2 | Define the
			 required configuration parameters in the group configuration file. |
| Step 3 | Add the group
			 configuration file to applicable CSF devices. Open the Cisco Unified CM Administration interface. Select Device > Phone . Find and
				  select the appropriate CSF device to which the group configuration applies. In the Phone Configuration window, navigate to Product Specific
						Configuration Layout > Desktop Client Settings . In the Cisco Support Field field, enter configurationfile= group_configuration_file_name.xml . For
				  example, enter configurationfile=groupa-config.xml . Note If you
						host the group configuration file on your TFTP server in a location other than
						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml . Do not
						add more than one group configuration file. The client uses only the first
						group configuration in the Cisco Support Field field. Select Save . | Note | If you
						host the group configuration file on your TFTP server in a location other than
						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml . Do not
						add more than one group configuration file. The client uses only the first
						group configuration in the Cisco Support Field field. |
| Note | If you
						host the group configuration file on your TFTP server in a location other than
						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml . Do not
						add more than one group configuration file. The client uses only the first
						group configuration in the Cisco Support Field field. |
| Step 4 | Host the group
			 configuration file on your TFTP server. |

| Note | If you
						host the group configuration file on your TFTP server in a location other than
						the default directory, you must specify the path and the filename; for example, configurationfile=/customFolder/groupa-config.xml . Do not
						add more than one group configuration file. The client uses only the first
						group configuration in the Cisco Support Field field. |
|---|---|

| Step 1 | Open the Cisco Unified OS Administration interface on Cisco Unified Communications Manager . |
|---|---|
| Step 2 | Select Software Upgrades > TFTP File Management . |
| Step 3 | Select Upload File . |
| Step 4 | Select Browse in the Upload File section. |
| Step 5 | Select the configuration file on the file system. |
| Step 6 | Do not specify a value in the Directory text box in the Upload File section. You should leave an empty value in the Directory text box so that the configuration file resides in the default directory of the TFTP server. |
| Step 7 | Select Upload File . |

| Step 1 | Open the Cisco Unified Serviceability interface on Cisco Unified Communications Manager . |
|---|---|
| Step 2 | Select Tools > Control Center - Feature Services . |
| Step 3 | Select Cisco Tftp from the CM Services section. |
| Step 4 | Select Restart . A window displays to prompt you to confirm the restart. |
| Step 5 | Select OK . The Cisco Tftp Service Restart Operation was Successful status displays. |
| Step 6 | Select Refresh to ensure the Cisco Tftp service starts successfully. |

| Step 1 | In the Connections tab select LAN
				Settings . |
|---|---|
| Step 2 | Configure a
			 proxy using one of the following options: For automatic
				configuration, specify a .pac file URL. For Proxy Server, specify
				an explicit proxy address. |

| Step 1 | Select System
				  Preferences > Network |
|---|---|
| Step 2 | Choose your
			 network service from the list and select Advanced > Proxies . |
| Step 3 | Configure a
			 proxy using one of the following options: For automatic
				configuration, specify a .pac file URL. For Proxy Server, specify
				an explicit proxy address. |

| Step 1 | Select Wi-Fi > HTTP
				  PROXY > Auto and specify a .pac file URL as the automatic configuration script. |
|---|---|
| Step 2 | Select Wi-Fi > HTTP
				  PROXY > Manual and specify an
			 explicit proxy address. |

| Configure
			 proxy settings in the Wi-Fi settings of an Android device using one of the
			 following methods: Specify a .pac file URL as
				the automatic configuration script in the Wi-Fi > Modify
					 Network > Show Advanced Options > Proxy
					 Settings > Auto tab. Note This
					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
					 series devices. Specify an explicit proxy
				address in the Wi-Fi
					 Networks > Modify Network > Show Advanced
					 Options > Proxy Settings > Auto tab. | Note | This
					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
					 series devices. |
|---|---|---|
| Note | This
					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
					 series devices. |

| Note | This
					 method is only supported on devices with Android OS 5.0 and later, and Cisco DX
					 series devices. |
|---|---|

| Step 1 | Host your
			 custom script on your 
			 HTTP server. |
|---|---|
| Step 2 | Specify the
			 URL of your script as the value of the PrtLogServerUrl parameter in your configuration file. |

| Note | If you use
				the Cisco WebEx Messenger service for instant messaging and presence
				capabilities, you should use the Cisco WebEx Administration Tool to configure
				automatic updates. |
|---|---|

| Step 1 | Host the
			 update installation program on your HTTP server. |
|---|---|
| Step 2 | Create an
			 update XML file with any text editor. |
| Step 3 | Specify
			 values in the XML as follows: name —Specify the following ID as the value of the name attribute for the App element: JabberWin—The update applies to Cisco Jabber for Windows. JabberMac—The update applies to Cisco Jabber for Mac. LatestBuildNum —Build number of the update. LatestVersion —Version number of the update. Mandatory —(Windows clients only) True or False.
					 Determines whether users must upgrade their client version when prompted. Message —HTML in the following format: <![CDATA[ your_html ]]> DownloadURL —URL of the installation package on your
					 HTTP server. For Cisco Jabber for Mac
					 the URL file must be in the following format: Cisco-Jabber-Mac- version - size - dsaSignature .zip |
| Step 4 | Save and
			 close your update XML file. |
| Step 5 | Host your
			 update XML file on your HTTP server. |
| Step 6 | Specify the
			 URL of your update XML file as the value of the UpdateUrl parameter in your configuration file. |

| Note | The Jabber embedded browser does not support cookie sharing with pop-ups from SSO enabled webpages. The content on the pop-up window may fail to load. |
|---|---|

| Parameter | Description |
|---|---|
| browser-plugin | Contains all definitions for custom embedded tabs. The
						value includes all custom tab definitions. |
| page | Contains one custom embedded tab definition. |
| refresh | Controls when the content
						refreshes. true
							 — Content refreshes each time users select the tab. false (default) — Content refreshes when users restart the
							 client or sign in. This parameter is optional
						and is an attribute of the page element. |
| preload | Controls when the content
						loads. true
							 — Content loads when the client starts. false (default) — Content loads when users select the tab. This
						parameter is optional and is an attribute of the page element. |
| tooltip | Defines hover text for the
						custom embedded tab. This parameter is optional.
						If you do not specify the hover text, the client will use Custom tab . The
						value is string of unicode characters. |
| icon | Specifies an icon for the tab. You can specify a local or hosted icon as follows: Local icon—Specify the URL as follows: file:// file_path / icon_name Hosted icon—Specify the URL as follows: http:// path / icon_name You can use any icon that the client browser can render can render, including .JPG, .PNG, and .GIF formats. This parameter is optional. If you do not specify an icon, the client loads the favicon from the HTML page. If no favicon is available, the client loads the default icon. |
| url | Specifies the URL where the content for the embedded tab
						resides. The client uses the browser rendering engine to display the content of the embedded tab. For this reason, you can specify any content that the browser supports. This parameter is
						required. |

| Note | User custom
				embedded tabs are set to true by default. |
|---|---|

| Tip | You can also specify the ${UserID} token in query strings; for example, www.cisco.com/mywebapp.op?url=${UserID} . |
|---|---|

| Note | Not applicable for Jabber for iPhone and iPad |
|---|---|

| Note | If you subscribe to the presence of a person who is not on your
				  contact list (also called temporary presence subscription ), the subscription
				  expires after 68 minutes. After the subscription expires, you must re-subscribe
				  to the person’s presence in order to continue to receive presence updates. Jabber for iPad and iPhone only supports OnPresenceStateChanged. |
|---|---|

| Note | Jabber for iPad and iPhone only supports OnLocaleInfoAvailable. |
|---|---|