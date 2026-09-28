---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-7a97261027
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_01000.html
retrieved_at: 2026-08-25T21:46:30.189101+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: June 25, 2015

Chapter: Configure Voicemail

## Chapter: Configure Voicemail

# Configure Voicemail

## Configure
	 Voicemail for an On-Premises Deployment with Cisco Unified Communications Manager Release 
	 9.x and Later

Configure 
				Cisco Unity Connection so that 
				Cisco Jabber can access voicemail services.

After you add
				a mailstore service, you must apply it to a service profile so that the client
				can retrieve the settings.

Configure
				retrieval so that users can access voice mail messages. Configure redirection
				so that users can send incoming calls to voicemail.

This procedure
				applies only if you want to set up a basic voicemail account that allows users
				to dial in to their voice mailbox. This procedure is not required if you want
				to set up visual voicemail.

## Configure
	 Voicemail for an On-Premises Deployment with Cisco Unified Communications Manager Release  8.6

Configure 
				Cisco Unity Connection so that 
				Cisco Jabber can access voicemail services.

Configure retrieval so that users can access voice mail messages. Configure redirection so that users can send incoming calls to voicemail.

## Configure Cisco
	 Unity Connection for Use with Cisco Jabber

You must complete
		  some specific steps to configure 
		  Cisco Unity Connection  so that Cisco Jabber  
		  can access voicemail services. You
		  should refer to the 
		  Cisco Unity Connection documentation for instructions on
		  general tasks such as creating users, passwords, and provisioning users with
		  voicemail access.

Cisco Jabber connects to the voicemail service
				through a REST interface and supports 
				Cisco Unity Connection release 8.5 or later.

- Open the Cisco Unity Connection Serviceability interface.

- Select Tools > Service
						Management .

Connection
							 Jetty

Connection REST
							 Service

- Start the
				  services if required.

- Select Users .

- Select the
				  appropriate user.

- Select Edit > Password
						Settings .

- Select Web Application from the Choose Password menu.

- Uncheck User Must Change at Next Sign-In .

- Select Save .

The Search Class of Service window opens.

- Select the
				  appropriate class of service or add a new class of service.

- Select Allow Users to Use the Web Inbox and RSS Feeds .

- In the Features section, select Allow Users to Use Unified Client to Access Voice
					 Mail .

- Select all
				  other options as appropriate.

- Select Save .

The API Configuration window opens.

Allow Access to Secure
							 Message Recordings through CUMI

Display Message Header
							 Information of Secure Messages through CUMI

Allow Message Attachments
							 through CUMI

- Select Save .

If you have Cisco Unified Communications Manager release 9.x and later, Add a Voicemail Service .

If you have Cisco Unified Communications Manager release  8.x, Add a Voicemail Server .

## Add a Voicemail
	 Service

Add a voicemail service, to allow users to
		  receive voice messages.

Configure Cisco Unity Connection for Use with Cisco Jabber

Product Type — Select Unity Connection .

Name — Enter a
						descriptive name for the server, for example, PrimaryVoicemailServer.

Hostname/IP Address — Enter the IP address or the fully qualified domain name (FQDN) of the voicemail server.

Port —You do not need to specify a
						port number. By default, the client always uses port 443 to connect to the
						voicemail server. For this reason, any value you specify does not take effect.

Protocol Type —You do not need to specify a
						value. By default, the client always uses HTTPS to connect to the voicemail
						server. For this reason, any value you specify does not take effect.

Apply a Voicemail Service

### Apply a Voicemail
	 Service

After you add a
		  voicemail service on 
		  Cisco
				Unified Communications Manager,
		  apply it to a service profile so that the client can retrieve the
		  settings.

Cisco Jabber does not read Voicemail UC Service Profile when it is deployed only in the Phone mode.

For Cisco Jabber to retrieve the voicemail server information, update the jabber-config.xml file with the voicemail parameters.

<Voicemail>

<VoicemailService_UseCredentialsFrom>phone</VoicemailService_UseCredentialsFrom>

<VoicemailPrimaryServer>X.X.X.X</VoicemailPrimaryServer>

</Voicemail>

After updating, upload the jabber-config.xml file to all the CUCM TFTP servers and restart the TFTP service on TFTP server nodes. Then reset the Jabber client.

Add a Voicemail Service

The Find and List Service Profiles window opens.

The Service Profile Configuration window opens.

Primary

Secondary

Tertiary

Unified CM - IM and Presence — Uses
						  the instant messaging and presence credentials to sign in to the voicemail
						  service. As a result, users do not need to enter their credentials for
						  voicemail services in the client.

Web conferencing — This option is
						  not supported, it uses the conferencing credentials to sign in to the voicemail
						  service. You cannot currently synchronize with conferencing credentials.

Not set — This option is selected
						  for Phone mode deployments.

The Find and List Users window opens.

- Specify
				  the appropriate filters in the Find User where field and then select Find to find a user.

The End User Configuration window opens.

- Under the Service Settings area, check the Home Cluster checkbox.

- For Phone mode deployments, ensure the Enable User for Unified CM IM and Presence
						  (Configure IM and Presence in the associated UC Service Profile) option is not selected. For all other deployments, check the Enable User for Unified CM IM and Presence (Configure IM and
					 Presence in the associated UC Service Profile) checkbox.

- Select
				  your service profile from the UC
					 Service Profile drop-down list.

- Click Save .

Add a Mailstore Service

## Add a Mailstore
	 Service

The mailstore service
		  provides users with visual voicemail capabilities.

Apply a Voicemail Service

Name —Enter a
					 descriptive name for the server, for example, PrimaryMailStoreServer.

Hostname/IP
						Address —Enter the IP address or the Fully Qualified Domain Name
					 (FQDN) of the mailstore server.

Port —You do not
					 need to specify a port number. By default, the client always uses port 443 to
					 connect to the mailstore server. For this reason, any value you specify does
					 not take effect.

Protocol
						Type —You do not need to specify a value. By default, the client
					 always uses HTTPS to connect to the mailstore server. For this reason, any
					 value you specify does not take effect.

Apply Mailstore Service

### Apply Mailstore Service

After you add a mailstore service on Cisco
				Unified Communications Manager, you must apply it to a service profile so that the client can retrieve the settings.

Add a Mailstore Service

The Find and List Service Profiles window opens.

The Service Profile Configuration window opens.

Primary

Secondary

Tertiary

Inbox Folder

Trash Folder

Polling Interval

Configure Retrieval and Redirection

## Add a Voicemail
	 Server

Complete the steps
		  in this task to add your voicemail server on 
		  Cisco
				Unified Presence.

Configure Cisco Unity Connection for Use with Cisco Jabber

In some
				  versions of 
				  Cisco
				Unified Presence, this path is as follows: Application > Cisco Unified Personal
						Communicator > Voicemail Server .

Name —  Enter a
						descriptive name for the server, for example, PrimaryVoicemailServer.

Hostname/IP Address — Enter the IP address or the fully qualified domain name (FQDN) of the voicemail server.

Port — You do not need to specify a
						port number. By default, the client always uses port 443 to connect to the
						voicemail server. For this reason, any value you specify does not take effect.

Protocol Type — You do not need to specify a
						value. By default, the client always uses HTTPS to connect to the voicemail
						server. For this reason, any value you specify does not take effect.

Create a Mailstore

## Create a
	 Mailstore

Complete the steps
		  in this task to create a mailstore on Cisco Unified Presence.

Ensure that you
		  have Cisco Unified Communications Manager release 8.x and Cisco Unified
		  Presence.

If you have Cisco
		  Unified Communications Manager release 9.x or later, see Add a Mailstore Service .

- Application > Cisco
					 Jabber > Mailstore

- Application > Cisco Unified Personal
					 Communicator > Mailstore

Name —Enter a
					 descriptive name for the server, for example, PrimaryMailStoreServer.

Hostname/IP
						Address —Enter the hostname, IP Address, or Fully Qualified Domain
					 Name (FQDN) of the mailstore server.

Port —You do not need to specify a port number. By
					 default, the client always uses port 443 to connect to the mailstore server.
					 For this reason, any value you specify does not take effect.

Protocol Type —You do not need to specify a value. By
					 default, the client always uses HTTPS to connect to the mailstore server. For
					 this reason, any value you specify does not take effect.

## Create a Voicemail Profile

After you add a voicemail server, you must create a voicemail profile and add that server to the profile.

Create a Mailstore

- Application > Cisco Jabber > Voicemail Profile

- Application > Cisco Unified Personal Communicator > Voicemail Profile

- Select Add Users to Profile .

- To retrieve a list of users, in the Find User where field, specify the appropriate filters and then select Find .

- Select the appropriate users from the list.

The selected users are added to the voicemail profile.

Configure Retrieval and Redirection

## Configure Retrieval and Redirection

Configure retrieval so that users can access voicemail messages in the client interface. Configure redirection so that users can send incoming calls to voicemail. You configure retrieval and redirection on Cisco Unified Communications Manager.

The Find and List Voice Mail Pilots window opens.

The Voice Mail Pilot Configuration window opens.

- Specify the appropriate details on the Voice Mail Pilot Configuration window.

- Select Save .

The Find and List Voice Mail Profiles window opens.

- Specify the appropriate filters in the Find Voice Mail  Profile where Voice Mail Profile Name field and then select Find to retrieve a list of profiles.

The Voice Mail Pilot Configuration window opens.

- Select the voicemail pilot from the Voice Mail Pilot drop-down list.

- Select Save .

The Find and List Phones window opens.

- Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices.

The Phone Configuration window opens.

- Locate the Association Information section.

The Directory Number Configuration window opens.

- Locate the Directory Number Settings section.

- Select the voicemail profile from the Voice Mail Profile drop-down list.

- Select Save .

Set a Voicemail Credentials Source

## Set a Voicemail Credentials Source

You can specify a
		  voicemail credentials source for users.

In hybrid
			 cloud-based deployments, you can set a voicemail credentials source as part of
			 your configuration file with the VoiceMailService_UseCredentialsForm parameter.

Configure Retrieval and Redirection

Do not
					 select Web Conferencing from the Credentials source for voicemail service drop-down
					 list. You cannot currently use conferencing credentials as a credentials source
					 for voicemail services.

The user's instant
		  messaging and presence credentials match the user's voicemail credentials. As a
		  result, users do not need to specify their voicemail credentials in the client
		  user interface.

There is no
				mechanism to synchronize credentials between servers. If you specify a
				credentials source, you must ensure that those credentials match the user's
				voicemail credentials.

For example,
				you specify that a user's instant messaging and presence credentials match the
				user's 
				Cisco Unity Connection credentials. The user's instant
				messaging and presence credentials then change. You must update the user's 
				Cisco Unity Connection credentials to reflect that change.

Cloud-Based
				deployments can use the configuration file parameter VoicemailService_UseCredentialsFrom . Set this parameter
				to the value phone to use the Cisco Unified Communications Manager credentials to sign in to Cisco Unity Connection.

## Enable Enhanced
	 Message Waiting Indicator

This procedure
		  applies only if you want to set up a basic voicemail account that allows users
		  to dial in to their voice mailbox. This procedure is not required if you want
		  to set up visual voicemail.

To enable the
				basic MWI, follow the instructions in the 
				Cisco Unified Communications Manager documentation for
				your release. There are no unique configurations for this client.

If your
				deployment supports Enhanced MWI, enable this option in
				the 
				Cisco Unity Connection Administration portal.

Set a Voicemail Credentials Source

## Configure Voicemail for Cloud-Based Deployments

### Configure
	 Voicemail

To configure your
		  voicemail settings, use the 
		  Cisco WebEx Administration Tool.

Allow Users to Set Voicemail Server Settings

### Allow Users to Set
	 Voicemail Server Settings

Select an option
		  with the 
		  Cisco WebEx Administration Tool so that users can specify voicemail
		  server settings in the client interface.

Configure Voicemail

The user can access
		  advanced voicemail settings in the Voicemail Accounts tab on the Options window in the client interface.

The user can access
		  advanced voicemail settings in the client interface by tapping Settings > Voicemail .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Cisco Unity Connection for Use with Cisco Jabber | Configure 
				Cisco Unity Connection so that 
				Cisco Jabber can access voicemail services. |
| Step 2 | Add a Voicemail Service |  |
| Step 3 | Add a Mailstore Service |  |
| Step 4 | Apply Mailstore Service | After you add
				a mailstore service, you must apply it to a service profile so that the client
				can retrieve the settings. |
| Step 5 | Configure Retrieval and Redirection | Configure
				retrieval so that users can access voice mail messages. Configure redirection
				so that users can send incoming calls to voicemail. |
| Step 6 | Set a Voicemail Credentials Source |  |
| Step 7 | Enable Enhanced Message Waiting Indicator | This procedure
				applies only if you want to set up a basic voicemail account that allows users
				to dial in to their voice mailbox. This procedure is not required if you want
				to set up visual voicemail. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Cisco Unity Connection for Use with Cisco Jabber | Configure 
				Cisco Unity Connection so that 
				Cisco Jabber can access voicemail services. |
| Step 2 | Add a Voicemail Server |  |
| Step 3 | Create a Mailstore |  |
| Step 4 | Create a Voicemail Profile |  |
| Step 5 | Configure Retrieval and Redirection | Configure retrieval so that users can access voice mail messages. Configure redirection so that users can send incoming calls to voicemail. |
| Step 6 | Set a Voicemail Credentials Source |  |

| Step 1 | Ensure the Connection Jetty and Connection REST Service services are started. Open the Cisco Unity Connection Serviceability interface. Select Tools > Service
						Management . Locate the
				  following services in the Optional Services section: Connection
							 Jetty Connection REST
							 Service Start the
				  services if required. |
|---|---|
| Step 2 | Open the Cisco
				Unity Connection Administration interface. |
| Step 3 | Edit user
			 password settings. Select Users . Select the
				  appropriate user. Select Edit > Password
						Settings . Select Web Application from the Choose Password menu. Uncheck User Must Change at Next Sign-In . Select Save . |
| Step 4 | Provide users
			 with access to the web inbox. Select Class of Service . The Search Class of Service window opens. Select the
				  appropriate class of service or add a new class of service. Select Allow Users to Use the Web Inbox and RSS Feeds . In the Features section, select Allow Users to Use Unified Client to Access Voice
					 Mail . Select all
				  other options as appropriate. Select Save . |
| Step 5 | Select API
			 configuration settings. Select System
						Settings > Advanced > API
						Settings . The API Configuration window opens. Select the
				  following options: Allow Access to Secure
							 Message Recordings through CUMI Display Message Header
							 Information of Secure Messages through CUMI Allow Message Attachments
							 through CUMI Select Save . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
				  Management > User Settings > UC
				  Service . The Find
				  and List UC Services window opens. |
| Step 3 | In the Find
				  and List UC Services window, select Add
				New . UC Service Configuration window opens. |
| Step 4 | In the Add a UC
				Service section, select Voicemail from the UC
				Service Type drop-down list and select Next |
| Step 5 | Specify details
			 for the voicemail service as follows: Product Type — Select Unity Connection . Name — Enter a
						descriptive name for the server, for example, PrimaryVoicemailServer. Hostname/IP Address — Enter the IP address or the fully qualified domain name (FQDN) of the voicemail server. Port —You do not need to specify a
						port number. By default, the client always uses port 443 to connect to the
						voicemail server. For this reason, any value you specify does not take effect. Protocol Type —You do not need to specify a
						value. By default, the client always uses HTTPS to connect to the voicemail
						server. For this reason, any value you specify does not take effect. |
| Step 6 | Select Save . |

| Note | Cisco Jabber does not read Voicemail UC Service Profile when it is deployed only in the Phone mode. For Cisco Jabber to retrieve the voicemail server information, update the jabber-config.xml file with the voicemail parameters. <Voicemail> <VoicemailService_UseCredentialsFrom>phone</VoicemailService_UseCredentialsFrom> <VoicemailPrimaryServer>X.X.X.X</VoicemailPrimaryServer> </Voicemail> After updating, upload the jabber-config.xml file to all the CUCM TFTP servers and restart the TFTP service on TFTP server nodes. Then reset the Jabber client. |
|---|---|

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
				  Management > User Settings > Service
				  Profile . The Find and List Service Profiles window opens. |
| Step 3 | Find and
			 select your service profile. The Service Profile Configuration window opens. |
| Step 4 | Configure the Voicemail Profile section as follows: Select up
				  to three services from the following drop-down lists: Primary Secondary Tertiary For Credentials source for voicemail service ,
				  select one of the following: Unified CM - IM and Presence — Uses
						  the instant messaging and presence credentials to sign in to the voicemail
						  service. As a result, users do not need to enter their credentials for
						  voicemail services in the client. Web conferencing — This option is
						  not supported, it uses the conferencing credentials to sign in to the voicemail
						  service. You cannot currently synchronize with conferencing credentials. Not set — This option is selected
						  for Phone mode deployments. |
| Step 5 | Click Save . |
| Step 6 | Add users to
			 the service profile. Select User
						Management > End User . The Find and List Users window opens. Specify
				  the appropriate filters in the Find User where field and then select Find to find a user. Click the
				  user in the list. The End User Configuration window opens. Under the Service Settings area, check the Home Cluster checkbox. For Phone mode deployments, ensure the Enable User for Unified CM IM and Presence
						  (Configure IM and Presence in the associated UC Service Profile) option is not selected. For all other deployments, check the Enable User for Unified CM IM and Presence (Configure IM and
					 Presence in the associated UC Service Profile) checkbox. Select
				  your service profile from the UC
					 Service Profile drop-down list. Click Save . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
				  Management > User Settings > UC
				  Service . The Find
				and List UC Services window opens. |
| Step 3 | Select Add
				New . |
| Step 4 | In the Add a UC
				Service section, from the UC
				Service Type drop-down list, select MailStore and then click Next . |
| Step 5 | Provide details
			 for the mailstore service as follows: Name —Enter a
					 descriptive name for the server, for example, PrimaryMailStoreServer. Hostname/IP
						Address —Enter the IP address or the Fully Qualified Domain Name
					 (FQDN) of the mailstore server. Port —You do not
					 need to specify a port number. By default, the client always uses port 443 to
					 connect to the mailstore server. For this reason, any value you specify does
					 not take effect. Protocol
						Type —You do not need to specify a value. By default, the client
					 always uses HTTPS to connect to the mailstore server. For this reason, any
					 value you specify does not take effect. |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . The Find and List Service Profiles window opens. |
| Step 3 | Find and select your service profile. The Service Profile Configuration window opens. |
| Step 4 | Configure  the MailStore Profile section as follows: Select up to three services from the following drop-down lists: Primary Secondary Tertiary Specify appropriate values for the following fields: Inbox Folder Trash Folder Polling Interval |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco
				Unified Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Cisco
				  Jabber > Voicemail Server . Note In some
				  versions of 
				  Cisco
				Unified Presence, this path is as follows: Application > Cisco Unified Personal
						Communicator > Voicemail Server . The Find
				  and List Voicemail Servers window opens. | Note | In some
				  versions of 
				  Cisco
				Unified Presence, this path is as follows: Application > Cisco Unified Personal
						Communicator > Voicemail Server . |
| Note | In some
				  versions of 
				  Cisco
				Unified Presence, this path is as follows: Application > Cisco Unified Personal
						Communicator > Voicemail Server . |
| Step 3 | Select Add
				New . |
| Step 4 | Select Unity
				Connection from the Server
				Type drop-down list. |
| Step 5 | Specify
			 details in the Voicemail Server Configuration section as follows: Name —  Enter a
						descriptive name for the server, for example, PrimaryVoicemailServer. Hostname/IP Address — Enter the IP address or the fully qualified domain name (FQDN) of the voicemail server. Port — You do not need to specify a
						port number. By default, the client always uses port 443 to connect to the
						voicemail server. For this reason, any value you specify does not take effect. Protocol Type — You do not need to specify a
						value. By default, the client always uses HTTPS to connect to the voicemail
						server. For this reason, any value you specify does not take effect. |
| Step 6 | Select Save . |

| Note | In some
				  versions of 
				  Cisco
				Unified Presence, this path is as follows: Application > Cisco Unified Personal
						Communicator > Voicemail Server . |
|---|---|

| Step 1 | Open the Cisco
				Unified Presence Administration interface. |
|---|---|
| Step 2 | Depending on
			 your version of Cisco Unified Presence, select one of the following paths: Application > Cisco
					 Jabber > Mailstore Application > Cisco Unified Personal
					 Communicator > Mailstore The Find
				and List Mailstore Servers window opens. |
| Step 3 | Select Add
				New . The Mailstore Configuration window opens. |
| Step 4 | Specify
			 details as follows: Name —Enter a
					 descriptive name for the server, for example, PrimaryMailStoreServer. Hostname/IP
						Address —Enter the hostname, IP Address, or Fully Qualified Domain
					 Name (FQDN) of the mailstore server. Port —You do not need to specify a port number. By
					 default, the client always uses port 443 to connect to the mailstore server.
					 For this reason, any value you specify does not take effect. Protocol Type —You do not need to specify a value. By
					 default, the client always uses HTTPS to connect to the mailstore server. For
					 this reason, any value you specify does not take effect. |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco Unified Presence Administration interface. |
|---|---|
| Step 2 | Depending on your version of Cisco Unified Presence, select one of the following: Application > Cisco Jabber > Voicemail Profile Application > Cisco Unified Personal Communicator > Voicemail Profile The Find and List Voicemail Profiles window opens. |
| Step 3 | Select Add New . The Voicemail Profile Configuration window opens. |
| Step 4 | Specify the required details. |
| Step 5 | Add users to the voicemail profile as follows: Select Add Users to Profile . To retrieve a list of users, in the Find User where field, specify the appropriate filters and then select Find . Select the appropriate users from the list. Select Add Selected . The selected users are added to the voicemail profile. |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Configure the voicemail pilot. Select Advanced Features > Voice Mail > Voice Mail Pilot . The Find and List Voice Mail Pilots window opens. Select Add New . The Voice Mail Pilot Configuration window opens. Specify the appropriate details on the Voice Mail Pilot Configuration window. Select Save . |
| Step 3 | Add the voicemail pilot to the voicemail profile. Select Advanced Features > Voice Mail > Voice Mail Profile . The Find and List Voice Mail Profiles window opens. Specify the appropriate filters in the Find Voice Mail  Profile where Voice Mail Profile Name field and then select Find to retrieve a list of profiles. Select the appropriate profile from the list. The Voice Mail Pilot Configuration window opens. Select the voicemail pilot from the Voice Mail Pilot drop-down list. Select Save . |
| Step 4 | Specify the voicemail profile in the directory number configuration. Select Device > Phone . The Find and List Phones window opens. Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices. Select the appropriate device from the list. The Phone Configuration window opens. Locate the Association Information section. Select the appropriate device number. The Directory Number Configuration window opens. Locate the Directory Number Settings section. Select the voicemail profile from the Voice Mail Profile drop-down list. Select Save . |

| Tip | In hybrid
			 cloud-based deployments, you can set a voicemail credentials source as part of
			 your configuration file with the VoiceMailService_UseCredentialsForm parameter. |
|---|---|

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
				  Management > User Settings > Service
				  Profile . |
| Step 3 | Select the
			 appropriate service profile to open the Service Profile Configuration window. |
| Step 4 | In the Voicemail Profile section, select Unified CM - IM and Presence from the Credentials source for voicemail service drop-down
			 list. Note Do not
					 select Web Conferencing from the Credentials source for voicemail service drop-down
					 list. You cannot currently use conferencing credentials as a credentials source
					 for voicemail services. | Note | Do not
					 select Web Conferencing from the Credentials source for voicemail service drop-down
					 list. You cannot currently use conferencing credentials as a credentials source
					 for voicemail services. |
| Note | Do not
					 select Web Conferencing from the Credentials source for voicemail service drop-down
					 list. You cannot currently use conferencing credentials as a credentials source
					 for voicemail services. |

| Note | Do not
					 select Web Conferencing from the Credentials source for voicemail service drop-down
					 list. You cannot currently use conferencing credentials as a credentials source
					 for voicemail services. |
|---|---|

| Note | To enable the
				basic MWI, follow the instructions in the 
				Cisco Unified Communications Manager documentation for
				your release. There are no unique configurations for this client. If your
				deployment supports Enhanced MWI, enable this option in
				the 
				Cisco Unity Connection Administration portal. |
|---|---|

| Step 1 | Open the Cisco
				Unity Connection Administration interface. |
|---|---|
| Step 2 | In the left
			 pane, navigate to Telephony
				  Integrations > Phone System . |
| Step 3 | Select the
			 link for the desired phone system. |
| Step 4 | In the Message
			 Waiting Indicators section, select the Send
				Message Counts check box. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Voicemail |  |
| Step 2 | Allow Users to Set Voicemail Server Settings |  |

| Step 1 | Open the 
			 Cisco WebEx Administration Tool. |
|---|---|
| Step 2 | Select Configuration > Unified
				  Communications . |
| Step 3 | Select the Voicemail tab. |
| Step 4 | Select Allow
				user to enter manual settings . |