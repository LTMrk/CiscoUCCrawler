---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-df07d324a0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_0110.html
retrieved_at: 2026-08-25T21:46:20.833757+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: June 25, 2015

Chapter: Configure the IM and Presence Service

## Chapter: Configure the IM and Presence Service

# Configure the IM and Presence Service

## Configure IM and Presence Service  for an On-Premises Deployment

### IM and Presence
	 Service Workflow for an On-Premises Deployment with Cisco Unified
	 Communications Manager 10.5 and later

### IM and Presence
	 Service Workflow for an On-Premises Deployment with Cisco Unified Communications Manager Release 9.x and Later

### IM and Presence
	 Service Workflow for an On-Premises Deployment with Cisco Unified Communications Manager Release 8.6

### Prepopulate Contact Lists in Bulk

You can pre-populate user contact lists with the Bulk
		  Administration Tool (BAT).

In
		  this way you can prepopulate contact lists for users so that they automatically
		  have a set of contacts after the initial launch of the client.

Cisco Jabber supports up to 300 contacts in a client contact
		  list.

For more
				information about using BAT and the format of the CSV file, see the Deployment Guide for Cisco Unified Communications Manager IM
				  & Presence for your release.

### Enable Message
	 Settings

Enable and configure instant messaging capabilities.

Prepopulate Contact Lists in Bulk .

Enable instant
						messaging

Allow clients to log
						instant message history

Allow cut & paste in instant messages

Cisco
					 Jabber does not support the following settings on the Presence Settings window on Cisco Unified
					 Communications Manager IM and Presence Service release 9.0.x:

Use DND status when user is
							 on the phone

Use DND status when user is
							 in a meeting

If you have
				Cisco Unified Communications Manager IM and Presence Service release 9.x and
				later, Add an IM and Presence Service .

If you have
				Cisco Unified Presence Release 8.6, Specify Capabilities Assignments .

### Specify
	 Capabilities Assignments

Complete the steps
		  in this task to provide users with instant messaging and presence capabilities
		  when using Cisco Unified Presence.

Enable Message Settings

The Find
				  and List Capabilities Assignments window opens.

The Capabilities Assignment Configuration window opens.

- Enable CUP

- Enable CUPC

### Add an IM and
	 Presence Service

Provide users with
		  IM and Presence Service capabilities.

The Find
				  and List UC Services window opens.

The UC
				  Service Configuration window opens.

- Select Unified CM (IM and Presence) from the Product Type drop-down list.

The name you
					 specify displays when you add the service to a profile. Ensure the name you
					 specify is unique, meaningful, and easy to identify.

- Specify an
				  optional description in the Description field.

The
						service address must be a fully qualified domain name or IP address.

#### Apply an IM and
	 Presence Service

After you add an
		  IM and Presence Service on 
		  Cisco Unified Communications Manager,
		  you must apply it to a service profile so that the client can retrieve the
		  settings.

Add an IM and Presence Service

The Find
				  and List Service Profiles window opens.

The Service Profile Configuration window opens.

Primary

Secondary

Tertiary

The Find and List Users dialog box opens.

- Specify
				  the appropriate filters in the Find User where field and then select Find to find a user.

The End User Configuration window appears.

- Under the Service Settings area, check the Home Cluster check box.

- Check the Enable User for Unified CM IM and Presence (Configure IM and
					 Presence in the associated UC Service Profile) check box.

- Select
				  your service profile from the UC
					 Service Profile drop-down list.

### Configure Presence
	 in Microsoft SharePoint 2010 and 2013

If your
		  organization defines users' profiles where their IM address is different from
		  their email address, then additional configuration is required to enable
		  presence integration between the client and Microsoft SharePoint 2010 and 2013.

For Cisco Jabber for Windows clients only.

Ensure that
				all sites are in sync with Microsoft SharePoint Central Administration (CA).

Ensure that
				synchronization between Microsoft SharePoint and Active Directory is set up.

- For the SIP Address profile field, leave it blank.

- In the Work email profile field, enter the user profile.
				  For example, john4mail@example.pst .

- For the SIP Address profile field, enter the user profile.
				  For example, john4mail@example.pst

- In the Work email profile field, leave it blank.

### Configure Users with IM and Presence Service

You can enable users for IM and Presence.

#### Configure Users
	 Individually

Enable instant
		  messaging and presence service and add your service profile to individual users.

The Find
				  and List Users window opens.

The End
				  User Configuration window opens.

- Select Home Cluster .

- Select Enable User for Unified CM IM and Presence .

Cisco Unified Communications Manager release 9.x only—If the user has
						  only instant messaging and presence capabilities (IM only), select Use Default . 
						  Cisco Unified Communications Manager release version 9.x applies the default
						  service profile regardless of what you select from the UC Service Profile drop-down list.

#### Configure Users in Bulk

Enable instant messaging and presence and add your service profile to multiple users.

The Find and List Users To Update window opens.

The Update Users Configuration window opens.

There are two check boxes for Enable User for Unified CM IM and Presence . To disable instant messaging and presence, you select one check box. To enable instant messaging and presence, you select both check boxes.

Cisco Unified Communications Manager release 9.x only —  If the user has only instant messaging and presence capabilities (IM only), you must select Use Default .

For IM only users — Cisco Unified Communications Manager release 9.x always applies the default service profile regardless of what you select from the UC Service Profile drop-down list.

## Configure IM and Presence Service for Cloud-Based Deployments

### Configure IM and
	 Presence Service

When users
		  successfully authenticate to the 
		  Cisco WebEx Messenger
		  service, they get IM and Presence Service capabilities. You can
		  optionally configure IM and Presence Service federation with the 
		  Cisco WebEx Administration Tool.

### Configure Privacy Options

You can specify the default settings for presence subscription requests in cloud-based deployments.

Option

Description

Select Allow users to set "Options for contact list requests"

Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change the default option in the Options window.

Do not select Allow users to set "Options for contact list requests"

You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings are not available in the Options window.

Accept requests automatically from all contacts

Accept requests automatically from contacts in my organization

Prompt me for each request

The options for configuring how the client handles contact list requests are as follows:

- Accept requests automatically from all contacts — The client automatically accepts presence subscription requests from any domain. If you specify this setting, users from any domain can automatically add users to their contact list and view their availability status.

When searching for contacts in your organization, users can see the temporary availability status of all users in the organization. However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list.

- Prompt me for each request — The client prompts users to accept each presence subscription request.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Prepopulate Contact Lists in Bulk |  |
| Step 2 | Enable Message Settings |  |
| Step 3 | Configure Presence in Microsoft SharePoint 2010 and 2013 |  |
| Step 4 | Configure Users with IM and Presence Service |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Prepopulate Contact Lists in Bulk |  |
| Step 2 | Enable Message Settings |  |
| Step 3 | Add an IM and Presence Service |  |
| Step 4 | Apply an IM and Presence Service |  |
| Step 5 | Configure Presence in Microsoft SharePoint 2010 and 2013 |  |
| Step 6 | Configure Users with IM and Presence Service |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Prepopulate Contact Lists in Bulk |  |
| Step 2 | Enable Message Settings |  |
| Step 3 | Specify Capabilities Assignments |  |
| Step 4 | Configure Presence in Microsoft SharePoint 2010 and 2013 |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create a CSV
			 file that defines the contact list you want to provide to users. |  |
| Step 2 | Use the BAT to
			 import the contact list in bulk to a set of users. | For more
				information about using BAT and the format of the CSV file, see the Deployment Guide for Cisco Unified Communications Manager IM
				  & Presence for your release. |

| Step 1 | Open the Cisco
				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > Settings . |
| Step 3 | Select the
			 following options: Enable instant
						messaging Allow clients to log
						instant message history Allow cut & paste in instant messages |
| Step 4 | Select other
			 messaging settings as appropriate. |
| Step 5 | Select Save . Important: Cisco
					 Jabber does not support the following settings on the Presence Settings window on Cisco Unified
					 Communications Manager IM and Presence Service release 9.0.x: Use DND status when user is
							 on the phone Use DND status when user is
							 in a meeting |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Licensing > Capabilities
				  Assignment . The Find
				  and List Capabilities Assignments window opens. |
| Step 3 | Specify the
			 appropriate filters in the Find
				Capabilities Assignment where field and then select Find to retrieve a list of users. |
| Step 4 | Select the
			 appropriate users from the list. The Capabilities Assignment Configuration window opens. |
| Step 5 | Select both of
			 the following in the Capabilities Assignment Configuration section: Enable CUP Enable CUPC |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
				  Management > User Settings > UC
				  Service . The Find
				  and List UC Services window opens. |
| Step 3 | Select Add
				New . The UC
				  Service Configuration window opens. |
| Step 4 | In the Add a UC
				Service section, select IM and
				Presence from the UC
				Service Type drop-down list. |
| Step 5 | Select Next . |
| Step 6 | Provide details
			 for the IM and Presence Service as follows: Select Unified CM (IM and Presence) from the Product Type drop-down list. Specify a
				  name for the service in the Name field. The name you
					 specify displays when you add the service to a profile. Ensure the name you
					 specify is unique, meaningful, and easy to identify. Specify an
				  optional description in the Description field. Specify the
				  instant messaging and presence service address in the Host
					 Name/IP Address field. Important: The
						service address must be a fully qualified domain name or IP address. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
				  Management > User Settings > Service
				  Profile . The Find
				  and List Service Profiles window opens. |
| Step 3 | Find and
			 select your service profile. The Service Profile Configuration window opens. |
| Step 4 | In the IM and
				Presence Profile section, select up to three services from the
			 following drop-down lists: Primary Secondary Tertiary |
| Step 5 | Click Save . |
| Step 6 | Add users to
			 the service profile. Select User
						Management > End User . The Find and List Users dialog box opens. Specify
				  the appropriate filters in the Find User where field and then select Find to find a user. Click the
				  user in the list. The End User Configuration window appears. Under the Service Settings area, check the Home Cluster check box. Check the Enable User for Unified CM IM and Presence (Configure IM and
					 Presence in the associated UC Service Profile) check box. Select
				  your service profile from the UC
					 Service Profile drop-down list. |
| Step 7 | Click Save . |

| Step 1 | If you have
			 Microsoft SharePoint 2013, update the SharePoint CA profile pages for users
			 with the following information: For the SIP Address profile field, leave it blank. In the Work email profile field, enter the user profile.
				  For example, john4mail@example.pst . |
|---|---|
| Step 2 | If you have
			 Microsoft SharePoint 2010, update the SharePoint CA profile pages for users
			 with the following information: For the SIP Address profile field, enter the user profile.
				  For example, john4mail@example.pst In the Work email profile field, leave it blank. |

| Step 1 | Open the Cisco
				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
				  Management > End User . The Find
				  and List Users window opens. |
| Step 3 | Specify the
			 appropriate filters in the Find
				User where field and then select Find to retrieve a list of users. |
| Step 4 | Select the
			 appropriate username from the list. The End
				  User Configuration window opens. |
| Step 5 | Locate the Service
				Settings section and do the following: Select Home Cluster . Select Enable User for Unified CM IM and Presence . Select your
				  service profile from the UC
					 Service Profile drop-down list. Important: Cisco Unified Communications Manager release 9.x only—If the user has
						  only instant messaging and presence capabilities (IM only), select Use Default . 
						  Cisco Unified Communications Manager release version 9.x applies the default
						  service profile regardless of what you select from the UC Service Profile drop-down list. |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Bulk Administration > Users > Update Users > Query . The Find and List Users To Update window opens. |
| Step 3 | Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users. |
| Step 4 | Select Next . The Update Users Configuration window opens. |
| Step 5 | Select both of the Enable User for Unified CM IM and Presence check boxes. Important: There are two check boxes for Enable User for Unified CM IM and Presence . To disable instant messaging and presence, you select one check box. To enable instant messaging and presence, you select both check boxes. |
| Step 6 | Select the UC Service Profile check box and then select your service profile from the drop-down list. Important: Cisco Unified Communications Manager release 9.x only —  If the user has only instant messaging and presence capabilities (IM only), you must select Use Default . For IM only users — Cisco Unified Communications Manager release 9.x always applies the default service profile regardless of what you select from the UC Service Profile drop-down list. |
| Step 7 | In the Job Information section, specify if you want to run the job immediately or at a later time. |
| Step 8 | Select Submit . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure IM and Presence Service |  |
| Step 2 | Configure Presence in Microsoft SharePoint 2010 and 2013 |  |
| Step 3 | Configure Privacy Options |  |

| Step 1 | Open the Cisco WebEx Administration Tool. |
|---|---|
| Step 2 | Select the Configuration tab. |
| Step 3 | Select General IM in the Connect Client section. The General IM pane opens. |
| Step 4 | Select the appropriate options for contact list requests as follows: Option Description Select Allow users to set "Options for contact list requests" Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change the default option in the Options window. Do not select Allow users to set "Options for contact list requests" You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings are not available in the Options window. Select one of the following options: Accept requests automatically from all contacts Accept requests automatically from contacts in my organization Prompt me for each request The options for configuring how the client handles contact list requests are as follows: Accept requests automatically from all contacts — The client automatically accepts presence subscription requests from any domain. If you specify this setting, users from any domain can automatically add users to their contact list and view their availability status. Accept requests automatically from contacts in my organization — The client automatically accepts presence subscription requests only from users in the domains you specify. To specify a domain, select Domain(s) in the System Settings section on the Configuration tab. Note When searching for contacts in your organization, users can see the temporary availability status of all users in the organization. However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. Prompt me for each request — The client prompts users to accept each presence subscription request. | Option | Description | Select Allow users to set "Options for contact list requests" | Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change the default option in the Options window. | Do not select Allow users to set "Options for contact list requests" | You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings are not available in the Options window. Select one of the following options: Accept requests automatically from all contacts Accept requests automatically from contacts in my organization Prompt me for each request | Note | When searching for contacts in your organization, users can see the temporary availability status of all users in the organization. However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. |
| Option | Description |
| Select Allow users to set "Options for contact list requests" | Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change the default option in the Options window. |
| Do not select Allow users to set "Options for contact list requests" | You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings are not available in the Options window. Select one of the following options: Accept requests automatically from all contacts Accept requests automatically from contacts in my organization Prompt me for each request |
| Note | When searching for contacts in your organization, users can see the temporary availability status of all users in the organization. However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. |
| Step 5 | Select Save . |

| Option | Description |
|---|---|
| Select Allow users to set "Options for contact list requests" | Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change the default option in the Options window. |
| Do not select Allow users to set "Options for contact list requests" | You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings are not available in the Options window. Select one of the following options: Accept requests automatically from all contacts Accept requests automatically from contacts in my organization Prompt me for each request |

| Note | When searching for contacts in your organization, users can see the temporary availability status of all users in the organization. However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. |
|---|---|