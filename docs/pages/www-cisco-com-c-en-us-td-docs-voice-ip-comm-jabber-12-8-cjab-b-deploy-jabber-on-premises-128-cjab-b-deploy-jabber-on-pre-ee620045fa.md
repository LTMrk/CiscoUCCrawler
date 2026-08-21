---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-8-cjab-b-deploy-jabber-on-premises-128-cjab-b-deploy-jabber-on-pre-ee620045fa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_8/cjab_b_deploy-jabber-on-premises-128/cjab_b_deploy-jabber-on-premises-128_chapter_0110.html
retrieved_at: 2026-08-21T05:20:21.240071+00:00
---

On-Premises Deployment for Cisco Jabber 12.8

# On-Premises Deployment for Cisco Jabber 12.8

Updated: April 1, 2024

Chapter: Configure Voicemail

## Chapter: Configure Voicemail

# Configure Voicemail

## Configure Voicemail Workflow

Step 1

Configure Cisco Unity Connection for Use with Cisco Jabber

Configure Cisco Unity Connection so that Cisco Jabber can access
                                          				voicemail services.

Step 2

Configure Retrieval and Redirection

Configure retrieval so that users can access voice mail messages.
                                          				Configure redirection so that users can send incoming calls to voicemail.

Step 3

Add a Voicemail Service

Add a Voicemail UC service. Jabber uses this information to connect to the voicemail server.

Step 4

Apply a Voicemail Service

Apply the Voicemail UC service to the service profile.

Step 5

Set a Voicemail Credentials Source

Set the credentials for connecting to the Voicemail server.

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

Remember

Cisco Jabber connects to the voicemail service
                                             				through a REST interface and supports 
                                             				Cisco Unity Connection release 8.5 or later.

Step 1

Ensure the Connection Jetty and Connection REST Service services are started.

Open the Cisco Unity Connection Serviceability interface.

Select Tools > Service
                                                   						Management .

Locate the
                                             				  following services in the Optional Services section:

Connection
                                                            							 Jetty

Connection REST
                                                            							 Service

Start the
                                             				  services if required.

Step 2

Open the Cisco
                                          				Unity Connection Administration interface.

Step 3

Edit user
                                       			 password settings.

Select Users .

Select the
                                             				  appropriate user.

Select Edit > Password
                                                   						Settings .

Select Web Application from the Choose Password menu.

Uncheck User Must Change at Next Sign-In .

Select Save .

Step 4

Provide users
                                       			 with access to the web inbox.

Select Class of Service .

The Search Class of Service window opens.

Select the
                                             				  appropriate class of service or add a new class of service.

Select Allow Users to Use the Web Inbox and RSS Feeds .

In the Features section, select Allow Users to Use Unified Client to Access Voice Mail .

Select all
                                             				  other options as appropriate.

Select Save .

Step 5

Select API
                                       			 configuration settings.

Select System
                                                   						Settings > Advanced > API
                                                   						Settings .

The API Configuration window opens.

Select the
                                             				  following options:

Allow Access to Secure
                                                            							 Message Recordings through CUMI

Display Message Header
                                                            							 Information of Secure Messages through CUMI

Allow Message Attachments
                                                            							 through CUMI

Select Save .

### What to do next

If you have Cisco Unified Communications Manager release 9.x and later, Add a Voicemail Service .

## Configure Retrieval and Redirection

Configure retrieval so that users can access voicemail messages in the client interface. Configure redirection so that users
                              can send incoming calls to voicemail. You configure retrieval and redirection on Cisco Unified Communications Manager.

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Configure the voicemail pilot.

Select Advanced Features > Voice Mail > Voice Mail Pilot .

The Find and List Voice Mail Pilots window opens.

Select Add New .

The Voice Mail Pilot Configuration window opens.

Specify the appropriate details on the Voice Mail Pilot Configuration window.

Select Save .

Step 3

Add the voicemail pilot to the voicemail profile.

Select Advanced Features > Voice Mail > Voice Mail Profile .

The Find and List Voice Mail Profiles window opens.

Specify the appropriate filters in the Find Voice Mail  Profile where Voice Mail Profile Name field and then select Find to retrieve a list of profiles.

Select the appropriate profile from the list.

The Voice Mail Pilot Configuration window opens.

Select the voicemail pilot from the Voice Mail Pilot drop-down list.

Select Save .

Step 4

Specify the voicemail profile in the directory number configuration.

Select Device > Phone .

The Find and List Phones window opens.

Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices.

Select the appropriate device from the list.

The Phone Configuration window opens.

Locate the Association Information section.

Select the appropriate device number.

The Directory Number Configuration window opens.

Locate the Directory Number Settings section.

Select the voicemail profile from the Voice Mail Profile drop-down list.

Select Save .

### What to do next

Set a Voicemail Credentials Source

## Add a Voicemail
                        	 Service

Add a voicemail service, to allow users to
                              		  receive voice messages.

### Before you begin

Configure Cisco Unity Connection for Use with Cisco Jabber

Step 1

Open the Cisco
                                          				Unified CM Administration interface.

Step 2

Select User
                                             				  Management > User Settings > UC
                                             				  Service .

Step 3

In the Find
                                          				  and List UC Services window, select Add
                                          				New .

Step 4

In the Add a UC
                                          				Service section, select Voicemail from the UC
                                          				Service Type drop-down list and select Next

Step 5

Specify details
                                       			 for the voicemail service as follows:

Product Type — Select Unity Connection .

Name — Enter a
                                                						descriptive name for the server, for example, PrimaryVoicemailServer.

Hostname/IP Address — Enter the IP address or the fully qualified domain name (FQDN) of the voicemail server.

Port —You do not need to specify a port number. By default, the client always uses port 443 to connect to the voicemail server.
                                                For this reason, any value you specify does not take effect.

Protocol Type —You do not need to specify a value. By default, the client always uses HTTPS to connect to the voicemail server. For this
                                                reason, any value you specify does not take effect.

Step 6

Select Save .

### What to do next

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

After updating, upload the jabber-config.xml file to all the Cisco Unified Communications Manager TFTP servers and restart the TFTP service on TFTP server nodes. Then
                                             reset the Jabber client.

#### Before you begin

Add a Voicemail Service

Step 1

Open the Cisco
                                             				Unified CM Administration interface.

Step 2

Select User
                                                				  Management > User Settings > Service
                                                				  Profile .

The Find and List Service Profiles window opens.

Step 3

Find and
                                          			 select your service profile.

The Service Profile Configuration window opens.

Step 4

Configure the Voicemail Profile section as follows:

Select up
                                                				  to three services from the following drop-down lists:

Primary

Secondary

Tertiary

For Credentials source for voicemail service ,
                                                				  select one of the following:

Unified CM - IM and Presence — Uses
                                                            						  the instant messaging and presence credentials to sign in to the voicemail
                                                            						  service. As a result, users do not need to enter their credentials for
                                                            						  voicemail services in the client.

Web conferencing — This option is
                                                            						  not supported, it uses the conferencing credentials to sign in to the voicemail
                                                            						  service. You cannot currently synchronize with conferencing credentials.

Not set — This option is selected
                                                            						  for Phone mode deployments.

Step 5

Click Save .

## Set a Voicemail Credentials Source

You can specify a
                              		  voicemail credentials source for users.

Tip

In hybrid
                                          			 cloud-based deployments, you can set a voicemail credentials source as part of
                                          			 your configuration file with the VoiceMailService_UseCredentialsForm parameter.

### Before you begin

Configure Retrieval and Redirection

Step 1

Open the Cisco
                                          				Unified CM Administration interface.

Step 2

Select User
                                             				  Management > User Settings > Service
                                             				  Profile .

Step 3

Select the
                                       			 appropriate service profile to open the Service Profile Configuration window.

Step 4

In the Voicemail Profile section, select Unified CM - IM and Presence from the Credentials source for voicemail service drop-down
                                       			 list.

Do not
                                                         					 select Web Conferencing from the Credentials source for voicemail service drop-down
                                                         					 list. You cannot currently use conferencing credentials as a credentials source
                                                         					 for voicemail services.

The user's instant
                              		  messaging and presence credentials match the user's voicemail credentials. As a
                              		  result, users do not need to specify their voicemail credentials in the client
                              		  user interface.

### What to do next

Important

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

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Cisco Unity Connection for Use with Cisco Jabber | Configure Cisco Unity Connection so that Cisco Jabber can access
                                          				voicemail services. |
| Step 2 | Configure Retrieval and Redirection | Configure retrieval so that users can access voice mail messages.
                                          				Configure redirection so that users can send incoming calls to voicemail. |
| Step 3 | Add a Voicemail Service | Add a Voicemail UC service. Jabber uses this information to connect to the voicemail server. |
| Step 4 | Apply a Voicemail Service | Apply the Voicemail UC service to the service profile. |
| Step 5 | Set a Voicemail Credentials Source | Set the credentials for connecting to the Voicemail server. |

| Remember | Cisco Jabber connects to the voicemail service
                                             				through a REST interface and supports 
                                             				Cisco Unity Connection release 8.5 or later. |
|---|---|

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
                                             				  appropriate class of service or add a new class of service. Select Allow Users to Use the Web Inbox and RSS Feeds . In the Features section, select Allow Users to Use Unified Client to Access Voice Mail . Select all
                                             				  other options as appropriate. Select Save . |
| Step 5 | Select API
                                       			 configuration settings. Select System
                                                   						Settings > Advanced > API
                                                   						Settings . The API Configuration window opens. Select the
                                             				  following options: Allow Access to Secure
                                                            							 Message Recordings through CUMI Display Message Header
                                                            							 Information of Secure Messages through CUMI Allow Message Attachments
                                                            							 through CUMI Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Configure the voicemail pilot. Select Advanced Features > Voice Mail > Voice Mail Pilot . The Find and List Voice Mail Pilots window opens. Select Add New . The Voice Mail Pilot Configuration window opens. Specify the appropriate details on the Voice Mail Pilot Configuration window. Select Save . |
| Step 3 | Add the voicemail pilot to the voicemail profile. Select Advanced Features > Voice Mail > Voice Mail Profile . The Find and List Voice Mail Profiles window opens. Specify the appropriate filters in the Find Voice Mail  Profile where Voice Mail Profile Name field and then select Find to retrieve a list of profiles. Select the appropriate profile from the list. The Voice Mail Pilot Configuration window opens. Select the voicemail pilot from the Voice Mail Pilot drop-down list. Select Save . |
| Step 4 | Specify the voicemail profile in the directory number configuration. Select Device > Phone . The Find and List Phones window opens. Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices. Select the appropriate device from the list. The Phone Configuration window opens. Locate the Association Information section. Select the appropriate device number. The Directory Number Configuration window opens. Locate the Directory Number Settings section. Select the voicemail profile from the Voice Mail Profile drop-down list. Select Save . |

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
                                                						descriptive name for the server, for example, PrimaryVoicemailServer. Hostname/IP Address — Enter the IP address or the fully qualified domain name (FQDN) of the voicemail server. Port —You do not need to specify a port number. By default, the client always uses port 443 to connect to the voicemail server.
                                                For this reason, any value you specify does not take effect. Protocol Type —You do not need to specify a value. By default, the client always uses HTTPS to connect to the voicemail server. For this
                                                reason, any value you specify does not take effect. |
| Step 6 | Select Save . |

| Note | Cisco Jabber does not read Voicemail UC Service Profile when it is deployed only in the Phone mode. For Cisco Jabber to retrieve the voicemail server information, update the jabber-config.xml file with the voicemail parameters. <Voicemail> <VoicemailService_UseCredentialsFrom>phone</VoicemailService_UseCredentialsFrom> <VoicemailPrimaryServer>X.X.X.X</VoicemailPrimaryServer> </Voicemail> After updating, upload the jabber-config.xml file to all the Cisco Unified Communications Manager TFTP servers and restart the TFTP service on TFTP server nodes. Then
                                             reset the Jabber client. |
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

| Important | There is no
                                             				mechanism to synchronize credentials between servers. If you specify a
                                             				credentials source, you must ensure that those credentials match the user's
                                             				voicemail credentials. For example,
                                             				you specify that a user's instant messaging and presence credentials match the
                                             				user's 
                                             				Cisco Unity Connection credentials. The user's instant
                                             				messaging and presence credentials then change. You must update the user's 
                                             				Cisco Unity Connection credentials to reflect that change. Cloud-Based
                                             				deployments can use the configuration file parameter VoicemailService_UseCredentialsFrom . Set this parameter
                                             				to the value phone to use the Cisco Unified Communications Manager credentials to sign in to Cisco Unity Connection. |
|---|---|