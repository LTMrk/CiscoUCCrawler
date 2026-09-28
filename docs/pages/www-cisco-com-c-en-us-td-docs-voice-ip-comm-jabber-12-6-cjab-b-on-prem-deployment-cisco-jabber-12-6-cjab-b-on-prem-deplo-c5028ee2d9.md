---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-6-cjab-b-on-prem-deployment-cisco-jabber-12-6-cjab-b-on-prem-deplo-c5028ee2d9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_6/cjab_b_on-prem-deployment-cisco-jabber_12-6/cjab_b_on-prem-deployment-cisco-jabber_12-6_chapter_0111.html
retrieved_at: 2026-08-21T21:07:49.833082+00:00
---

On-Premises Deployment for Cisco Jabber 12.6

# On-Premises Deployment for Cisco Jabber 12.6

Updated: April 1, 2024

Chapter: Configure Webex Conferencing

## Chapter: Configure Webex Conferencing

# Configure Webex Conferencing

## Configure
                        	 Conferencing for an On-Premises Deployment

When you implement an on-premises deployment for Cisco Jabber, you can configure conferencing on-premises with Webex Meetings Server, or in the cloud in Webex Meetings Center.

### Configure On-Premises Conferencing using Webex Meetings Server

Step 1

Authenticate Webex Meetings Server .

Step 2

Add Webex Meetings Server on Cisco Unified Communications Manager .

#### Authenticate Webex Meetings Server

To authenticate with Webex Meetings Server, complete one of the following options:

- Configure single sign-on (SSO) with Webex Meetings Server to integrate with the SSO environment. In this case, you do not need to specify credentials for users to authenticate
                                                with Webex Meetings Server

- Set a credentials source on Cisco Unified Communications Manager. If the users' credentials for Webex Meetings Server match their credentials for Cisco Unified Communications Manager IM and Presence Service or Cisco Unity Connection,
                                                you can set a credentials source. The client then automatically authenticates to Webex Meetings Server with the users' credential source.

- Instruct users to manually enter credentials in the client.

##### What to do next

Add Webex Meetings Server on Cisco Unified Communications Manager

#### Add Webex Meetings Server on Cisco Unified Communications Manager

To configure conferencing on Cisco Unified Communications Manager, you must add a Webex Meetings Server.

##### Before you begin

Authenticate with Webex Meetings Server

Step 1

Open the Cisco
                                                				Unified CM Administration interface and select User
                                                   				  Management > User Settings > UC
                                                   				  Service .

Step 2

Select Add
                                                				New .

Step 3

In the Add a
                                                				UC Service section, from the UC
                                                				Service Type drop-down list, select Conferencing and then select Next .

Step 4

Complete the
                                             			 following fields:

Product Type — Select Webex (Conferencing) .

Name — Enter a name for the configuration. The name
                                                         					 you specify is displayed when you add services to profiles. Ensure the name you
                                                         					 specify is unique, meaningful, and easy to identify.

Hostname/IP Address — Enter the site URL for Webex Meetings Server. This URL is case sensitive and must match the case that was configured for the site URL in Webex Meetings Server.

Port — Leave the default value.

Protocol — Select HTTPS .

Step 5

To use Webex as the single sign-on (SSO) identity provider, check User web conference server as SSO identity provider .

This field is available only if you select Webex (Conferencing) from the Product Type drop-down list.

Step 6

Select Save .

##### What to do next

Add the Webex Meetings Server to a Service Profile

##### Add the Webex Meetings Server to a Service Profile

After you add Webex Meetings Server and add it to a service profile, the client can access conferencing features.

###### Before you begin

Create a service
                                       		  profile.

Add Webex Meetings Server on Cisco Unified Communications Manager

Step 1

Open the Cisco
                                                   				Unified CM Administration interface and select User
                                                      				  Management > User Settings > Service
                                                      				  Profile

Step 2

Find and
                                                			 select your service profile.

Step 3

In the Conferencing Profile section, from the Primary , Secondary , and Tertiary drop-down lists, select up to three instances of Webex Meetings Server.

Step 4

From the Server Certificate Verification drop-down list, select the
                                                				  appropriate value.

Step 5

From the Credentials source for web conference service drop-down list, select one
                                                				  of the following:

- Not set —Select this option if the user does not have a credentials source that matches their Webex Meetings Server credentials or if you use SSO at the meeting site.

- Unified CM - IM and Presence —Select this option if the Cisco Unified Communications Manager IM and Presence Service credentials for the user match their Webex Meetings Server credentials.

- Voicemail —Select this option if the Cisco Unity Connection credentials for the user match their Webex Meetings Server credentials.

You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Webex Meetings Server credentials for that user to match that change.

Step 6

Select Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Authenticate Webex Meetings Server . |  |
| Step 2 | Add Webex Meetings Server on Cisco Unified Communications Manager . |  |

| To authenticate with Webex Meetings Server, complete one of the following options: Configure single sign-on (SSO) with Webex Meetings Server to integrate with the SSO environment. In this case, you do not need to specify credentials for users to authenticate
                                                with Webex Meetings Server Set a credentials source on Cisco Unified Communications Manager. If the users' credentials for Webex Meetings Server match their credentials for Cisco Unified Communications Manager IM and Presence Service or Cisco Unity Connection,
                                                you can set a credentials source. The client then automatically authenticates to Webex Meetings Server with the users' credential source. Instruct users to manually enter credentials in the client. |
|---|

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
                                                         					 specify is unique, meaningful, and easy to identify. Hostname/IP Address — Enter the site URL for Webex Meetings Server. This URL is case sensitive and must match the case that was configured for the site URL in Webex Meetings Server. Port — Leave the default value. Protocol — Select HTTPS . |
| Step 5 | To use Webex as the single sign-on (SSO) identity provider, check User web conference server as SSO identity provider . Note This field is available only if you select Webex (Conferencing) from the Product Type drop-down list. | Note | This field is available only if you select Webex (Conferencing) from the Product Type drop-down list. |
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
| Step 3 | In the Conferencing Profile section, from the Primary , Secondary , and Tertiary drop-down lists, select up to three instances of Webex Meetings Server. |
| Step 4 | From the Server Certificate Verification drop-down list, select the
                                                				  appropriate value. |
| Step 5 | From the Credentials source for web conference service drop-down list, select one
                                                				  of the following: Not set —Select this option if the user does not have a credentials source that matches their Webex Meetings Server credentials or if you use SSO at the meeting site. Unified CM - IM and Presence —Select this option if the Cisco Unified Communications Manager IM and Presence Service credentials for the user match their Webex Meetings Server credentials. Voicemail —Select this option if the Cisco Unity Connection credentials for the user match their Webex Meetings Server credentials. Note You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Webex Meetings Server credentials for that user to match that change. | Note | You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Webex Meetings Server credentials for that user to match that change. |
| Note | You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Webex Meetings Server credentials for that user to match that change. |
| Step 6 | Select Save . |

| Note | You cannot synchronize the credentials you specify in Cisco Unified Communications Manager with credentials you specify in Webex Meetings Server. For example, if you specify that instant messaging and presence credentials for a user are synchronized with their Webex Meetings Server credentials, the instant messaging and presence credentials for that user change. You must update the Webex Meetings Server credentials for that user to match that change. |
|---|---|