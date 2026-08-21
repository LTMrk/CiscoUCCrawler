---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-10-5-cjab-bk-d6497e98-00-deployment-installation-guide-ciscojabber-cj-14587909ce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/10_5/CJAB_BK_D6497E98_00_deployment-installation-guide-ciscojabber/CJAB_BK_D6497E98_00_deployment-installation-guide-ciscojabber_chapter_01000.html
retrieved_at: 2026-08-21T05:10:22.630694+00:00
---

Deployment and Installation Guide for Cisco Jabber, Release 10.5

# Deployment and Installation Guide for Cisco Jabber, Release 10.5

Updated: August 14, 2014

Chapter: Configure Conferencing

## Chapter: Configure Conferencing

# Configure Conferencing

## Configure
                        	 Conferencing for an On-Premises Deployment

When you implement an on-premises deployment for Cisco Jabber, you can configure conferencing on-premises with Cisco Webex Meetings Server, or in the cloud in Cisco Webex Meetings Center.

### Configure On-Premises Conferencing using WebEx
                           	 Meetings Server

Authenticate with Cisco WebEx Meetings Server .

Add Cisco Webex Meetings Server on Cisco Unified Communications Manager .

Complete this task if you have Cisco Unified Communications Manager release 9.x and later.

Add Cisco WebEx Meetings Server on Cisco Unified Presence .

Complete this task if you have Cisco Unified Communications Manager Release 8.6 and Cisco Unified Presence.

#### Cisco WebEx
                              	 Meetings Server Installation and Configuration

The first step in
                                    		  setting up integration between Cisco WebEx Meetings
                                       				  Server and the client is to install and
                                    		  configure Cisco WebEx Meetings
                                       				  Server . You should refer to the Cisco WebEx Meetings
                                       				  Server product documentation for
                                    		  installation and configuration procedures.

#### Authenticate with
                              	 Cisco WebEx Meetings Server

For Cisco
                                             				  Jabber for Windows, each user can enter their credentials in the Options window to authenticate directly with Cisco WebEx Meetings
                                                				  Server .

For Cisco
                                             				  Jabber for Mac, each user can enter their credentials in the Meetings tab on the Preferences window to authenticate directly with Cisco WebEx Meetings
                                                				  Server .

If the
                                             				  users' credentials for Cisco WebEx Meetings
                                                				  Server match their credentials for Cisco Unified Communications Manager IM and Presence
                                                				  Service or Cisco Unity Connection , you can set a credentials source.
                                             				  The client then automatically authenticates to Cisco WebEx Meetings
                                                				  Server with the users' credential source.

If you
                                             				  configure SSO with Cisco WebEx Meetings
                                                				  Server , Cisco Jabber can seamlessly integrate with the
                                             				  SSO environment. In this case, you do not need to specify credentials in order
                                             				  for users to authenticate with Cisco WebEx Meetings
                                                				  Server .

#### Add Cisco Webex Meetings Server on Cisco Unified Communications Manager

To configure conferencing on Cisco Unified Communications Manager, you must add a Cisco Webex Meetings Server.

##### Before you begin

Authenticate with Cisco Webex Meetings Server

Open the Cisco
                                                				Unified CM Administration interface and select User
                                                   				  Management > User Settings > UC
                                                   				  Service .

Select Add
                                                				New .

In the Add a
                                                				UC Service section, from the UC
                                                				Service Type drop-down list, select Conferencing and then select Next .

Complete the
                                             			 following fields:

Product Type — Select Webex (Conferencing) .

Name — Enter a name for the configuration. The name
                                                         					 you specify is displayed when you add services to profiles. Ensure the name you
                                                         					 specify is unique, meaningful, and easy to identify.

Hostname/IP Address — Enter the site URL for Cisco Webex Meetings Server. This URL is case sensitive and must match the case that was configured for the site URL in Cisco Webex Meetings Server.

Port — Leave the default value.

Protocol — Select HTTPS .

To use Cisco Webex as the single sign-on (SSO) identity provider, check User web conference server as SSO identity provider .

This field is available only if you select Webex (Conferencing) from the Product Type drop-down list.

Select Save .

##### What to do next

Add the Cisco Webex Meetings Server to a Service Profile

##### Add the Cisco Webex Meetings Server to a Service Profile

After you add Cisco Webex Meetings Server and add it to a service profile, the client can access conferencing features.

###### Before you begin

Create a service
                                       		  profile.

Add Cisco Webex Meetings Server on Cisco Unified Communications Manager

Open the Cisco
                                                   				Unified CM Administration interface and select User
                                                      				  Management > User Settings > Service
                                                      				  Profile

Find and
                                                			 select your service profile.

In the Conferencing Profile section, from the Primary , Secondary , and Tertiary drop-down lists, select up to three instances of Cisco Webex Meetings Server.

From the Server Certificate Verification drop-down list, select the
                                                				  appropriate value.

From the Credentials source for web conference service drop-down list, select one
                                                				  of the following:

- Not set —Select this option if the user does not have a credentials source that matches their Cisco Webex Meetings Server credentials or if you use SSO at the meeting site.

- Unified CM - IM and Presence —Select this option if the Cisco Unified Communications Manager IM and Presence Service credentials for the user match their Cisco Webex Meetings Server credentials.

- Voicemail —Select this option if the Cisco Unity Connection credentials for the user match their Cisco Webex Meetings Server credentials.

You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Cisco Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Cisco Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Cisco Webex Meetings Server credentials for that user to match that change.

Select Save .

#### Set Up Cisco WebEx
                              	 Meetings Server on Cisco Unified Presence

The client
                                    		  retrieves Cisco WebEx Meetings
                                       				  Server details from the conferencing
                                    		  profile on Cisco Unified Presence . You must add your details for Cisco WebEx Meetings
                                       				  Server , add Cisco WebEx Meetings
                                       				  Server to a profile, and then add users to
                                    		  the profile.

##### Add Cisco WebEx
                                 	 Meetings Server on Cisco Unified Presence

###### Before you begin

Add the Cisco Webex Meetings Server to a Service Profile

Open the Cisco
                                                   				Unified Presence Administration interface.

Depending on your version of Cisco Unified Presence, select 
                                                			 one of the following:.

- Application > Cisco
                                                         				  Jabber > Conferencing Server

- Application > Cisco Unified Personal
                                                         					 Communicator > Conferencing Server

Select Add
                                                   				New .

Complete the following fields:

Name — Enter
                                                         						a name for the configuration. The name is displayed when you add services to profiles.

Hostname/IP
                                                            						Address — Enter
                                                         					 the site URL for 
                                                         					 Cisco WebEx
                                                         	 Meetings Server.

Port — Accept the default value.

Protocol — Select HTTPS .

Server Type — Select WebEx .

Site ID — You do
                                                         						not need to specify a value for this field.

Partner ID — You do
                                                         						not need to specify a value for this field.

Select Save .

###### What to do next

Add Cisco WebEx Meetings Server to a Profile

##### Add Cisco WebEx
                                 	 Meetings Server to a Profile

After you add 
                                       		  Cisco WebEx
                                       	 Meetings Server  on 
                                       		  Cisco
                                       				Unified Presence and  add 
                                       		  it to a service profile, the client
                                       		  can access conferencing features.

###### Before you begin

Add Cisco WebEx Meetings Server on Cisco Unified Presence

Open the Cisco
                                                   				Unified Presence Administration interface.

Depending on your version of Cisco
                                                				Unified Presence, select 
                                                			 one of the following:

- Application > Cisco
                                                         				  Jabber > Conferencing Profile

- Application > Cisco Unified Personal
                                                         					 Communicator > Conferencing Profile

Select Add
                                                   				New .

Complete the following fields:

Name — Enter a
                                                         					 name for the configuration.

Description — Enter an
                                                         						optional description.

Primary Conferencing
                                                            						Server — Select
                                                         						the primary instance of 
                                                         						Cisco WebEx
                                                         	 Meetings Server.

Backup Conferencing
                                                            						Server — Select
                                                         						the backup instance of 
                                                         						Cisco WebEx
                                                         	 Meetings Server.

From the Server Certificate
                                                   						Verification drop-down list, select one of the following:

- Any Certificate

- Self Signed or
                                                      								Keystore

- Keystore Only

To
                                                			 set this profile as the system default, check Make
                                                   				this the default Conferencing Profile for the system .

In the Users in Profile section, select Add Users to Profile .

In the Find and List Users window, select Find to retrieve a list of users.

Select the
                                                				  appropriate users from the list and then select Add Selected .

Select Save .

### Configure Cloud-Based Conferencing Using WebEx Meeting Center

Integration with Cisco WebEx Meeting Center .

Authentication with Cisco WebEx Meeting Center .

Authenticate the client with Cisco WebEx Meeting Center using tightly coupled integration.

Provide Conferencing Credentials .

Provide conferencing credentials to the client.

Depending on your version of  Cisco Unified Communications Manager, select one of the following:

- If you have Cisco Unified Communications Manager release 9.x and later with Cisco Unified Communications Manager IM and Presence
                                             Service, Add Cisco WebEx Meeting Center .

- If you have Cisco Unified Communications Manager Release 8.6 with Cisco Unified Presence, Set Up Cisco WebEx Meeting Center on Cisco Unified Presence .

#### Integration with
                              	 Cisco WebEx Meeting Center

Cloud-based integration — Cisco WebEx Meeting Center provides data, such as participant chat and roster lists, and audio and
                                          video capabilities.

Hybrid cloud-based integration — Cisco WebEx Meeting Center provides data, such as participant
                                          					 chat and roster lists, and a conferencing bridge provides audio and video capabilities.

#### Authentication with Cisco WebEx Meeting Center

You can authenticate the client with Cisco WebEx Meeting
                                       				  Center using tightly coupled integration. Tightly coupled integration refers to a configuration that you set up between Cisco WebEx Messenger and Cisco WebEx Meeting
                                       				  Center . When users authenticate with Cisco WebEx Messenger , it passes an authentication token back to the client. The client then passes that authentication token to Cisco WebEx Meeting
                                       				  Center . See the Overview of Tightly Coupled Integration topic for more information.

#### Provide Conferencing Credentials

Users individually specify their credentials in the Options window.

Users individually specify their credentials in the Meetings tab on the Preferences window.

You specify a credentials source on Cisco Unified Communications Manager when you apply the conferencing service to the service
                                             profile. See the topic in this section that describes how to add the conferencing server to the service profile for instructions.

#### Add Cisco WebEx
                              	 Meeting Center

The first step to
                                    		  setting up conferencing on 
                                    		  Cisco Unified Communications Manager is to add your details for 
                                    		  Cisco WebEx Meeting Center.

Open the Cisco
                                                				Unified CM Administration interface.

Select User
                                                   				  Management > User Settings > UC
                                                   				  Service .

Select Add
                                                				New .

In the Add a UC
                                                				Service section, from the UC
                                                				Service Type drop-down list, select Conferencing and then select Next .

Complete the following fields:

Product Type — Select WebEx (Conferencing) .

Name — Enter a
                                                         						name for the configuration. The name
                                                         						is displayed when you add services to profiles. Ensure the name you
                                                         						specify is unique, meaningful, and easy to identify.

Description — Enter an
                                                         						optional description.

Host Name/IP
                                                            						Address — Enter the Cisco WebEx Meeting Center site hostname. Do not enter an IP address.

Port — Enter the 
                                                         						Cisco WebEx Meeting Center site port number.

Protocol — Select HTTPS .

To use 
                                             						Cisco WebEx as the single sign-on (SSO) identity
                                             						provider, check User
                                                				web conference server as SSO identity provider .

This field
                                                            				  is available only if you select WebEx (Conferencing) as the Product Type .

Select Save .

##### What to do next

Add 
                                    		  Cisco WebEx Meeting Center to a service profile.

##### Add Cisco WebEx Meeting Center to
                                 	 a Profile

After you add 
                                       		  Cisco WebEx Meeting Center on 
                                       		  Cisco Unified Communications Manager, you add 
                                       		  Cisco WebEx Meeting Center to a service profile. The client can
                                       		  then retrieve the details for 
                                       		  Cisco WebEx Meeting Center from the profile and access the
                                       		  conferencing features.

###### Before you begin

Create a service
                                       		  profile.

Open the Cisco
                                                   				Unified CM Administration interface.

Select User
                                                      				  Management > User Settings > Service
                                                      				  Profile .

The Find
                                                      				  and List Service Profiles window opens.

Find and
                                                			 select your service profile.

The Service Profile Configuration window opens.

Configure the Conferencing Profile section as follows:

Select
                                                      				  your service from the Primary drop-down list.

The
                                                                        						  client uses only the service you select from the Primary drop-down list. You do not need to select
                                                                        						  services from the Secondary or Tertiary drop-down lists.

Select the
                                                      				  appropriate value from the Server Certificate Verification drop-down list.

Select one
                                                      				  of the following from the Credentials source for web conference service drop-down list:

Not set — The
                                                               							 user does not have a credentials source that matches their 
                                                               							 Cisco WebEx Meeting Center credentials.

Unified CM - IM and
                                                               							 Presence — The
                                                               						  user’s 
                                                               						  Cisco Unified Communications Manager IM and Presence Service credentials match their 
                                                               						  Cisco WebEx Meeting Center credentials.

Voicemail — The
                                                               						  user’s 
                                                               						  Cisco Unity Connection credentials match their 
                                                               						  Cisco WebEx Meeting Center credentials.

You
                                                                        						  cannot specify a credentials source if you use an identity provider for
                                                                        						  authentication with 
                                                                        						  Cisco WebEx Meeting Center.

If you
                                                                        						  select a credentials source, you must ensure that those credentials match the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials.

There
                                                                        						  is no mechanism to synchronize the credentials you specify in 
                                                                        						  Cisco Unified Communications Manager with credentials you specify in 
                                                                        						  Cisco WebEx Meeting Center. For example, you specify that a
                                                                        						  user’s instant messaging and presence credentials are synchronized with the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials. The user’s instant
                                                                        						  messaging and presence credentials then change. You must update the user’s 
                                                                        						  Cisco WebEx Meeting Center credentials to match that change.

Select Save .

#### Set Up Cisco WebEx
                              	 Meeting Center on Cisco Unified Presence

Details for 
                                             		  Cisco WebEx Meeting Center

A Cisco WebEx Meeting Center profile

Users to the
                                             		  Cisco WebEx Meeting Center profile

##### Add Cisco WebEx
                                 	 Meeting Center

The first step to
                                       		  setting up conferencing on Cisco Unified Presence is to add your details for 
                                       		  Cisco WebEx Meeting Center.

Open the Cisco
                                                   				Unified Presence Administration interface.

Select Application > Cisco
                                                      				  Jabber > Conferencing Server .

In some
                                                   				versions of 
                                                   				Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal
                                                         					 Communicator > Conferencing Server .

Select Add
                                                   				New .

The Conferencing Server Configuration window opens.

Specify
                                                			 details for 
                                                			 Cisco WebEx Meeting Center in the following fields:

Name — Enter a
                                                         						name for the configuration.
                                                         					 The name
                                                         						you specify displays when you add services to profiles.

You
                                                                        							 must specify a hostname, not an IP address.

Port — Specify
                                                         						a port number for the 
                                                         						Cisco WebEx Meeting Center site.

Protocol — Select HTTPS from the drop-down list.

Server Type — Select WebEx from the drop-down list.

Site ID — Specify
                                                         						the optional primary site ID for 
                                                         						Cisco WebEx Meeting Center.

Partner ID —  Specify
                                                         						the optional appropriate partner ID for 
                                                         						Cisco WebEx Meeting Center.

Select Save .

##### Add Cisco WebEx
                                 	 Meeting Center to a Profile

After you add 
                                       		  Cisco WebEx Meeting Center on 
                                       		  Cisco Unified Presence, you add 
                                       		  Cisco WebEx Meeting Center to a conferencing profile. The
                                       		  client can then retrieve the details for 
                                       		  Cisco WebEx Meeting Center from the profile and access the
                                       		  conferencing features.

Open the Cisco
                                                   				Unified Presence Administration interface.

Select Application > Cisco
                                                      				  Jabber > Conferencing Profile .

In some
                                                   				versions of 
                                                   				Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal
                                                         					 Communicator > Conferencing Profile .

Select Add
                                                   				New .

The Conferencing Profile Configuration window opens.

Specify
                                                			 details for the profile in the following fields:

Name — Enter a
                                                         					 name for the configuration.

Description — Enter an
                                                         						optional description.

Primary Conferencing
                                                            						Server — Select
                                                         						the primary Cisco WebEx Meeting Center site from the drop-down list.

The
                                                                        							 client uses only the site you select from the Primary Conferencing Server drop-down list. You do
                                                                        							 not need to select a site from the Backup Conferencing Server drop-down list.

Any Certificate

Self Signed or
                                                                     								Keystore

Keystore Only

Select the Make
                                                   				this the default Conferencing Profile for the system checkbox to
                                                			 set this profile as the system default.

Add users to
                                                			 the conferencing profile as follows:

Select Add Users to Profile in the Users in Profile section.

The Find and List Users dialog box opens.

Select Find to retrieve a list of users.

Select the
                                                      				  appropriate users from the list.

Select Add Selected .

The
                                                         					 selected users are added to the profile and the Find and List Users dialog box closes.

Select Save .

## Configure Conferencing for Cloud-Based Deployments

### Configure Conferencing for a Cloud-Based Deployment Using Cisco WebEx Meeting Center

Configure the appropriate settings with the Cisco WebEx Administration Tool and assign the meeting and conferencing capabilities
                                 to the appropriate users.

You can add more Cisco WebEx meeting sites in the Cisco Jabber client. However, you cannot   add a meeting site that is configured
                                 for SSO, this site must be created in the Cisco WebEx Administration Tool.

#### Authentication with Cisco WebEx
                              	 Meeting Center

Tightly Coupled
                                          				Integration with the 
                                          				Cisco WebEx Messenger Service 
                                          			 — Tightly
                                          				  coupled integration refers to a configuration that you set up between 
                                          				  Cisco WebEx Messenger and 
                                          				  Cisco WebEx Meeting Center.

When users
                                          				  authenticate with 
                                          				  Cisco WebEx Messenger, it passes an authentication token
                                          				  back to the client. The client then passes that authentication token to 
                                          				  Cisco WebEx Meeting Center.

See the Overview
                                             					 of Tightly Coupled Integration topic for more information.

Authentication
                                          				with an Identity Provider 
                                          			  — The client can
                                          				  redirect authentication from 
                                          				  Cisco WebEx Meeting Center to an identity provider.

Set up
                                                   						your identity provider as appropriate.

When users
                                                   						attempt to authenticate with 
                                                   						Cisco WebEx Meeting Center, the client redirects that
                                                   						authentication to your identity provider. Your identity provider then validates
                                                   						the credentials and passes an authentication token back to the client. The
                                                   						client then passes that token to 
                                                   						Cisco WebEx Meeting Center to complete the authentication
                                                   						process.

Specify 
                                                   						Cisco WebEx Meeting Center credentials in the client interface.

See the Using SSO
                                             					 with the Cisco WebEx and Cisco WebEx Meeting applications topic for more
                                          				  information about managing user identities with the 
                                          				  Cisco WebEx Messenger service.

You can authenticate the
                                    		  client with 
                                    		  Cisco WebEx Meeting Center using tightly coupled integration.
                                    		  Tightly coupled integration refers to a configuration that you set up between 
                                    		  Cisco WebEx Messenger and 
                                    		  Cisco WebEx Meeting Center. When users authenticate with 
                                    		  Cisco WebEx Messenger, it passes an authentication token
                                    		  back to the client. The client then passes that authentication token to 
                                    		  Cisco WebEx Meeting Center. See the Overview of
                                       			 Tightly Coupled Integration topic for more information.

#### Specify Conferencing Credentials in the Client

Users can specify their credentials in the Meetings tab on the Options window.

To open the Options window, select File > Options .

Users can specify their credentials in the Settings .

On the Settings screen, under Accounts , tap WebEx Meeting .

Users can specify their credentials in the Meetings tab on the Preferences window.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Authenticate with Cisco WebEx Meetings Server . |  |
| Step 2 | Add Cisco Webex Meetings Server on Cisco Unified Communications Manager . | Complete this task if you have Cisco Unified Communications Manager release 9.x and later. |
| Step 3 | Add Cisco WebEx Meetings Server on Cisco Unified Presence . | Complete this task if you have Cisco Unified Communications Manager Release 8.6 and Cisco Unified Presence. |

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface and select User
                                                   				  Management > User Settings > UC
                                                   				  Service . The Find
                                                				and List UC Services window opens. |
|---|---|
| Step 2 | Select Add
                                                				New . |
| Step 3 | In the Add a
                                                				UC Service section, from the UC
                                                				Service Type drop-down list, select Conferencing and then select Next . |
| Step 4 | Complete the
                                             			 following fields: Product Type — Select Webex (Conferencing) . Name — Enter a name for the configuration. The name
                                                         					 you specify is displayed when you add services to profiles. Ensure the name you
                                                         					 specify is unique, meaningful, and easy to identify. Hostname/IP Address — Enter the site URL for Cisco Webex Meetings Server. This URL is case sensitive and must match the case that was configured for the site URL in Cisco Webex Meetings Server. Port — Leave the default value. Protocol — Select HTTPS . |
| Step 5 | To use Cisco Webex as the single sign-on (SSO) identity provider, check User web conference server as SSO identity provider . Note This field is available only if you select Webex (Conferencing) from the Product Type drop-down list. | Note | This field is available only if you select Webex (Conferencing) from the Product Type drop-down list. |
| Note | This field is available only if you select Webex (Conferencing) from the Product Type drop-down list. |
| Step 6 | Select Save . |

| Note | This field is available only if you select Webex (Conferencing) from the Product Type drop-down list. |
|---|---|

| Step 1 | Open the Cisco
                                                   				Unified CM Administration interface and select User
                                                      				  Management > User Settings > Service
                                                      				  Profile |
|---|---|
| Step 2 | Find and
                                                			 select your service profile. |
| Step 3 | In the Conferencing Profile section, from the Primary , Secondary , and Tertiary drop-down lists, select up to three instances of Cisco Webex Meetings Server. |
| Step 4 | From the Server Certificate Verification drop-down list, select the
                                                				  appropriate value. |
| Step 5 | From the Credentials source for web conference service drop-down list, select one
                                                				  of the following: Not set —Select this option if the user does not have a credentials source that matches their Cisco Webex Meetings Server credentials or if you use SSO at the meeting site. Unified CM - IM and Presence —Select this option if the Cisco Unified Communications Manager IM and Presence Service credentials for the user match their Cisco Webex Meetings Server credentials. Voicemail —Select this option if the Cisco Unity Connection credentials for the user match their Cisco Webex Meetings Server credentials. Note You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Cisco Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Cisco Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Cisco Webex Meetings Server credentials for that user to match that change. | Note | You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Cisco Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Cisco Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Cisco Webex Meetings Server credentials for that user to match that change. |
| Note | You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Cisco Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Cisco Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Cisco Webex Meetings Server credentials for that user to match that change. |
| Step 6 | Select Save . |

| Note | You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Cisco Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Cisco Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Cisco Webex Meetings Server credentials for that user to match that change. |
|---|---|

| Step 1 | Open the Cisco
                                                   				Unified Presence Administration interface. |
|---|---|
| Step 2 | Depending on your version of Cisco Unified Presence, select 
                                                			 one of the following:. Application > Cisco
                                                         				  Jabber > Conferencing Server Application > Cisco Unified Personal
                                                         					 Communicator > Conferencing Server |
| Step 3 | Select Add
                                                   				New . The Conferencing Server Configuration window opens. |
| Step 4 | Complete the following fields: Name — Enter
                                                         						a name for the configuration. The name is displayed when you add services to profiles. Hostname/IP
                                                            						Address — Enter
                                                         					 the site URL for 
                                                         					 Cisco WebEx
                                                         	 Meetings Server. Port — Accept the default value. Protocol — Select HTTPS . Server Type — Select WebEx . Site ID — You do
                                                         						not need to specify a value for this field. Partner ID — You do
                                                         						not need to specify a value for this field. |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco
                                                   				Unified Presence Administration interface. |
|---|---|
| Step 2 | Depending on your version of Cisco
                                                				Unified Presence, select 
                                                			 one of the following: Application > Cisco
                                                         				  Jabber > Conferencing Profile Application > Cisco Unified Personal
                                                         					 Communicator > Conferencing Profile |
| Step 3 | Select Add
                                                   				New . The Conferencing Profile Configuration window opens. |
| Step 4 | Complete the following fields: Name — Enter a
                                                         					 name for the configuration. Description — Enter an
                                                         						optional description. Primary Conferencing
                                                            						Server — Select
                                                         						the primary instance of 
                                                         						Cisco WebEx
                                                         	 Meetings Server. Backup Conferencing
                                                            						Server — Select
                                                         						the backup instance of 
                                                         						Cisco WebEx
                                                         	 Meetings Server. |
| Step 5 | From the Server Certificate
                                                   						Verification drop-down list, select one of the following: Any Certificate Self Signed or
                                                      								Keystore Keystore Only |
| Step 6 | To
                                                			 set this profile as the system default, check Make
                                                   				this the default Conferencing Profile for the system . |
| Step 7 | In the Users in Profile section, select Add Users to Profile . |
| Step 8 | In the Find and List Users window, select Find to retrieve a list of users. |
| Step 9 | Select the
                                                				  appropriate users from the list and then select Add Selected . The
                                                					 selected users are added to the profile. |
| Step 10 | Select Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Integration with Cisco WebEx Meeting Center . |  |
| Step 2 | Authentication with Cisco WebEx Meeting Center . | Authenticate the client with Cisco WebEx Meeting Center using tightly coupled integration. |
| Step 3 | Provide Conferencing Credentials . | Provide conferencing credentials to the client. |
| Step 4 | Depending on your version of  Cisco Unified Communications Manager, select one of the following: If you have Cisco Unified Communications Manager release 9.x and later with Cisco Unified Communications Manager IM and Presence
                                             Service, Add Cisco WebEx Meeting Center . If you have Cisco Unified Communications Manager Release 8.6 with Cisco Unified Presence, Set Up Cisco WebEx Meeting Center on Cisco Unified Presence . |  |

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
                                                				Service Type drop-down list, select Conferencing and then select Next . |
| Step 5 | Complete the following fields: Product Type — Select WebEx (Conferencing) . Name — Enter a
                                                         						name for the configuration. The name
                                                         						is displayed when you add services to profiles. Ensure the name you
                                                         						specify is unique, meaningful, and easy to identify. Description — Enter an
                                                         						optional description. Host Name/IP
                                                            						Address — Enter the Cisco WebEx Meeting Center site hostname. Do not enter an IP address. Port — Enter the 
                                                         						Cisco WebEx Meeting Center site port number. Protocol — Select HTTPS . |
| Step 6 | To use 
                                             						Cisco WebEx as the single sign-on (SSO) identity
                                             						provider, check User
                                                				web conference server as SSO identity provider . Note This field
                                                            				  is available only if you select WebEx (Conferencing) as the Product Type . | Note | This field
                                                            				  is available only if you select WebEx (Conferencing) as the Product Type . |
| Note | This field
                                                            				  is available only if you select WebEx (Conferencing) as the Product Type . |
| Step 7 | Select Save . |

| Note | This field
                                                            				  is available only if you select WebEx (Conferencing) as the Product Type . |
|---|---|

| Step 1 | Open the Cisco
                                                   				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
                                                      				  Management > User Settings > Service
                                                      				  Profile . The Find
                                                      				  and List Service Profiles window opens. |
| Step 3 | Find and
                                                			 select your service profile. The Service Profile Configuration window opens. |
| Step 4 | Configure the Conferencing Profile section as follows: Select
                                                      				  your service from the Primary drop-down list. Note The
                                                                        						  client uses only the service you select from the Primary drop-down list. You do not need to select
                                                                        						  services from the Secondary or Tertiary drop-down lists. Select the
                                                      				  appropriate value from the Server Certificate Verification drop-down list. Select one
                                                      				  of the following from the Credentials source for web conference service drop-down list: Not set — The
                                                               							 user does not have a credentials source that matches their 
                                                               							 Cisco WebEx Meeting Center credentials. Unified CM - IM and
                                                               							 Presence — The
                                                               						  user’s 
                                                               						  Cisco Unified Communications Manager IM and Presence Service credentials match their 
                                                               						  Cisco WebEx Meeting Center credentials. Voicemail — The
                                                               						  user’s 
                                                               						  Cisco Unity Connection credentials match their 
                                                               						  Cisco WebEx Meeting Center credentials. Restriction You
                                                                        						  cannot specify a credentials source if you use an identity provider for
                                                                        						  authentication with 
                                                                        						  Cisco WebEx Meeting Center. Important If you
                                                                        						  select a credentials source, you must ensure that those credentials match the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials. There
                                                                        						  is no mechanism to synchronize the credentials you specify in 
                                                                        						  Cisco Unified Communications Manager with credentials you specify in 
                                                                        						  Cisco WebEx Meeting Center. For example, you specify that a
                                                                        						  user’s instant messaging and presence credentials are synchronized with the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials. The user’s instant
                                                                        						  messaging and presence credentials then change. You must update the user’s 
                                                                        						  Cisco WebEx Meeting Center credentials to match that change. | Note | The
                                                                        						  client uses only the service you select from the Primary drop-down list. You do not need to select
                                                                        						  services from the Secondary or Tertiary drop-down lists. | Restriction | You
                                                                        						  cannot specify a credentials source if you use an identity provider for
                                                                        						  authentication with 
                                                                        						  Cisco WebEx Meeting Center. | Important | If you
                                                                        						  select a credentials source, you must ensure that those credentials match the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials. There
                                                                        						  is no mechanism to synchronize the credentials you specify in 
                                                                        						  Cisco Unified Communications Manager with credentials you specify in 
                                                                        						  Cisco WebEx Meeting Center. For example, you specify that a
                                                                        						  user’s instant messaging and presence credentials are synchronized with the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials. The user’s instant
                                                                        						  messaging and presence credentials then change. You must update the user’s 
                                                                        						  Cisco WebEx Meeting Center credentials to match that change. |
| Note | The
                                                                        						  client uses only the service you select from the Primary drop-down list. You do not need to select
                                                                        						  services from the Secondary or Tertiary drop-down lists. |
| Restriction | You
                                                                        						  cannot specify a credentials source if you use an identity provider for
                                                                        						  authentication with 
                                                                        						  Cisco WebEx Meeting Center. |
| Important | If you
                                                                        						  select a credentials source, you must ensure that those credentials match the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials. There
                                                                        						  is no mechanism to synchronize the credentials you specify in 
                                                                        						  Cisco Unified Communications Manager with credentials you specify in 
                                                                        						  Cisco WebEx Meeting Center. For example, you specify that a
                                                                        						  user’s instant messaging and presence credentials are synchronized with the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials. The user’s instant
                                                                        						  messaging and presence credentials then change. You must update the user’s 
                                                                        						  Cisco WebEx Meeting Center credentials to match that change. |
| Step 5 | Select Save . |

| Note | The
                                                                        						  client uses only the service you select from the Primary drop-down list. You do not need to select
                                                                        						  services from the Secondary or Tertiary drop-down lists. |
|---|---|

| Restriction | You
                                                                        						  cannot specify a credentials source if you use an identity provider for
                                                                        						  authentication with 
                                                                        						  Cisco WebEx Meeting Center. |
|---|---|

| Important | If you
                                                                        						  select a credentials source, you must ensure that those credentials match the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials. There
                                                                        						  is no mechanism to synchronize the credentials you specify in 
                                                                        						  Cisco Unified Communications Manager with credentials you specify in 
                                                                        						  Cisco WebEx Meeting Center. For example, you specify that a
                                                                        						  user’s instant messaging and presence credentials are synchronized with the
                                                                        						  user’s 
                                                                        						  Cisco WebEx Meeting Center credentials. The user’s instant
                                                                        						  messaging and presence credentials then change. You must update the user’s 
                                                                        						  Cisco WebEx Meeting Center credentials to match that change. |
|---|---|

| Step 1 | Open the Cisco
                                                   				Unified Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Cisco
                                                      				  Jabber > Conferencing Server . In some
                                                   				versions of 
                                                   				Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal
                                                         					 Communicator > Conferencing Server . |
| Step 3 | Select Add
                                                   				New . The Conferencing Server Configuration window opens. |
| Step 4 | Specify
                                                			 details for 
                                                			 Cisco WebEx Meeting Center in the following fields: Name — Enter a
                                                         						name for the configuration.
                                                         					 The name
                                                         						you specify displays when you add services to profiles. Hostname/IP
                                                         						Address — Specify
                                                         						the hostname of the 
                                                         						Cisco WebEx Meeting Center site. Note You
                                                                        							 must specify a hostname, not an IP address. Port — Specify
                                                         						a port number for the 
                                                         						Cisco WebEx Meeting Center site. Protocol — Select HTTPS from the drop-down list. Server Type — Select WebEx from the drop-down list. Site ID — Specify
                                                         						the optional primary site ID for 
                                                         						Cisco WebEx Meeting Center. Partner ID —  Specify
                                                         						the optional appropriate partner ID for 
                                                         						Cisco WebEx Meeting Center. | Note | You
                                                                        							 must specify a hostname, not an IP address. |
| Note | You
                                                                        							 must specify a hostname, not an IP address. |
| Step 5 | Select Save . |

| Note | You
                                                                        							 must specify a hostname, not an IP address. |
|---|---|

| Step 1 | Open the Cisco
                                                   				Unified Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Cisco
                                                      				  Jabber > Conferencing Profile . In some
                                                   				versions of 
                                                   				Cisco Unified Presence, this path is as follows: Application > Cisco Unified Personal
                                                         					 Communicator > Conferencing Profile . |
| Step 3 | Select Add
                                                   				New . The Conferencing Profile Configuration window opens. |
| Step 4 | Specify
                                                			 details for the profile in the following fields: Name — Enter a
                                                         					 name for the configuration. Description — Enter an
                                                         						optional description. Primary Conferencing
                                                            						Server — Select
                                                         						the primary Cisco WebEx Meeting Center site from the drop-down list. Note The
                                                                        							 client uses only the site you select from the Primary Conferencing Server drop-down list. You do
                                                                        							 not need to select a site from the Backup Conferencing Server drop-down list. Server Certificate
                                                            						Verification — Select
                                                         						one of the following from the drop-down list: Any Certificate Self Signed or
                                                                     								Keystore Keystore Only | Note | The
                                                                        							 client uses only the site you select from the Primary Conferencing Server drop-down list. You do
                                                                        							 not need to select a site from the Backup Conferencing Server drop-down list. |
| Note | The
                                                                        							 client uses only the site you select from the Primary Conferencing Server drop-down list. You do
                                                                        							 not need to select a site from the Backup Conferencing Server drop-down list. |
| Step 5 | Select the Make
                                                   				this the default Conferencing Profile for the system checkbox to
                                                			 set this profile as the system default. |
| Step 6 | Add users to
                                                			 the conferencing profile as follows: Select Add Users to Profile in the Users in Profile section. The Find and List Users dialog box opens. Select Find to retrieve a list of users. Select the
                                                      				  appropriate users from the list. Select Add Selected . The
                                                         					 selected users are added to the profile and the Find and List Users dialog box closes. |
| Step 7 | Select Save . |

| Note | The
                                                                        							 client uses only the site you select from the Primary Conferencing Server drop-down list. You do
                                                                        							 not need to select a site from the Backup Conferencing Server drop-down list. |
|---|---|