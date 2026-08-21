---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-ipad-9-3-x-jabi-bk-cceaf656-00-cisco-jabber-video-for-ipad-jabi-bk-cc-1ed46b8d01
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/iPad/9_3_x/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad_chapter_0101.html
retrieved_at: 2026-08-21T19:43:51.801888+00:00
---

Cisco Jabber Video for iPad 9.3.4 Administration Guide

# Cisco Jabber Video for iPad 9.3.4 Administration Guide

Updated: November 22, 2013

Chapter: Set up for Cisco Unified Communications Manager 9.x

## Chapter: Set up for Cisco Unified Communications Manager 9.x

# Set up for Cisco Unified Communications Manager 9.x

This chapter describes how you can set up Cisco Jabber Video for iPad using Cisco Unified Communications Manager 9.x.

## Activate and Start Essential Services

Essential services enable communication between servers and provide capabilities to the client.

- Cisco SIP Proxy

- Cisco Sync Agent

- Cisco XCP Authentication Service

- Cisco XCP Connection Manager

- Cisco XCP Text Conference Manager

- Cisco Presence Engine

Depending on your requirements, you might need to activate and start additional services. See the appropriate Cisco Unified Communications Manager documentation to review available services and determine if your deployment requires additional services.

## Configure Directory Integration

- Synchronize with the directory server.

- Authenticate with the directory server.

### Synchronize with the Directory Server

#### Enable Synchronization

The LDAP System Configuration window opens.

Specify an LDAP attribute for the user ID.

#### Specify an LDAP Attribute for the User ID

When you synchronize from your directory source to Cisco Unified Communications Manager , you can populate the user ID from an attribute in the directory. The default attribute that holds the user ID is sAMAccountName .

If the attribute for the user ID is other than sAMAccountName , you must specify the attribute as the value for the UserAccountName parameter in your client configuration file as follows:

```
< UserAccountName > attribute-name </ UserAccountName >
```

If you do not specify the attribute in your configuration, and the attribute is other than sAMAccountName , the client cannot resolve contacts in your directory. As a result, users do not get presence and cannot send or receive instant messages.

#### Perform Synchronization

- Cisco Unified Presence : Cisco UP Sync Agent

- Cisco Unified Communications Manager IM and Presence : Cisco Sync Agent

This service keeps data synchronized between the presence server and Cisco Unified Communications Manager . When you perform the synchronization with your directory server, Cisco Unified Communications Manager then synchronizes the data with the presence server. However, the Cisco Sync Agent service must be activated and started.

The LDAP Directory window opens.

See the Cisco Unified Communications Manager Administration Guide for more information about the values and formats you can specify.

The amount of time it takes for the synchronization process to complete depends on the number of users that exist in your directory. If you synchronize a large directory with thousands of users, you should expect the process to take some time.

User data from your directory server is synchronized to the Cisco Unified Communications Manager database. Cisco Unified Communications Manager then synchronizes the user data to the presence server database.

### Authenticate with the Directory Server

See the Cisco Unified Communications Manager Administration Guide for information about the fields on the LDAP Authentication window.

## Create a Service Profile

You create a service profile that contains the configuration settings for the services you add on Cisco Unified Communications Manager . You add the service profile to the end user configuration for your users. The client can then retrieve settings for available services from the service profile.

The Find and List Service Profiles window opens.

The Service Profile Configuration window opens.

- Specify a unique name for the service profile in the Name field.

- Specify an optional description in the Description field.

- Select Make this the default service profile for the system , if appropriate.

Complete the steps to set up instant messaging and presence. You can add your service profile to the end user configuration at the same time that you enable users for instant messaging and presence.

## Set Up Instant Messaging and Presence

Instant messaging and presence capabilities let users send and receive instant messages as well as publish and view availability status.

You should begin your deployment by setting up instant messaging and presence. After you successfully set up functionality for chat and availability status, you can build on your deployment by adding other services and provisioning features such as audio and video or voicemail.

### Enable Messaging Settings

Enable and configure instant messaging capabilities.

- Enable instant messaging

- Use DND status when user is on the phone

- Use DND status when user is in a meeting

- Allow clients to log instant message history

### Configure Prompts for Presence Subscription Requests

You can enable or disable prompts for presence subscription requests from contacts within your organization.

The client always prompts users to allow presence subscription requests from contacts outside your organization.

The Presence Settings window opens.

The client does not prompt users for presence subscription requests. The client automatically accepts all presence subscription requests without prompting the users.

The client prompts users to allow presence subscription requests. This setting requires users to allow other users in your organization to view their availability status.

### Add an Instant Messaging and Presence Service

Provide users with instant messaging and presence capabilities.

The Find and List UC Services window opens.

The UC Service Configuration window opens.

- Select Unified CM (IM and Presence) from the Product Type drop-down list.

The name you specify displays when you add the service to a profile. Ensure the name you specify is unique, meaningful, and easy to identify.

- Specify an optional description in the Description field.

- Specify the instant messaging and presence service address in the Host Name/IP Address field.

Add the instant messaging and presence service to your service profile.

#### Apply Instant Messaging and Presence Service

After you add an instant messaging and presence service on Cisco Unified Communications Manager , you must apply it to a service profile so that the client can retrieve the settings.

Create a service profile.

The Find and List Service Profiles window opens.

The Service Profile Configuration window opens.

- Primary

- Secondary

- Tertiary

### Add a Directory Service

Perform the following procedure to add a Directory service that provides users with Directory search capabilities

The Find and List UC Services window opens.

The UC Service Configuration window opens.

- Select Directory from the Product Type dropdown list.

- Specify a name for the service in the Name field. The name you specify displays when you add the service to a profile. Ensure the name you specify is unique, meaningful, and easy to identify.

- Specify an optional description in the Description field.

- Specify the Directory service address in the HostName/IPAddress field.

- Specify the port number used by the LDAP server. The defaults are:

- TCP - 389

- TLS - 636

- Global Catalog - 3268/3269

Add the Directory service to your service profile.

### Apply a Directory Service

After you add a Directory service on Cisco Unified Communications Manager, you must apply it to a service profile so that the client can retrieve the settings.

Create a service profile.

The Find and List Service Profiles window opens.

The Service Profile Configuration window opens.

### Configure Users

To configure users, you enable instant messaging and presence and add a service profile to the users.

#### Configure Users Individually

Enable instant messaging and presence and add your service profile to individual users.

The Find and List Users window opens.

The End User Configuration window opens.

- Select Enable User for Unified CM IM and Presence .

Cisco Unified Communications Manager version 9.x only: If the user has only instant messaging and presence capabilities (IM only), you must select Use Default .

For IM only users, Cisco Unified Communications Manager version 9.x always applies the default service profile regardless of what you select from the UC Service Profile drop-down list.

#### Configure Users in Bulk

Enable instant messaging and presence and add your service profile to multiple users.

The Find and List Users To Update window opens.

The Update Users Configuration window opens.

There are two check boxes for Enable User for Unified CM IM and Presence . To disable instant messaging and presence, you select one check box. To enable instant messaging and presence, you select both check boxes.

Cisco Unified Communications Manager version 9.x only: If the user has only instant messaging and presence capabilities (IM only), you must select Use Default .

For IM only users, Cisco Unified Communications Manager version 9.x always applies the default service profile regardless of what you select from the UC Service Profile drop-down list.

## Set Up Audio and Video Capabilities

Provision users with software phone devices and desk phone devices. Configure dial plan mapping and perform other essential tasks to set up audio and video capabilities.

You should review the Cisco Unified Communications Manager licensing requirements, including information on adjunct licensing, before you provision users with devices.

### Create Software Phone Devices

#### Create a Tablet Phone Device

Use this procedure to create a softphone device for use with an iPad.

The Find and List Phones window opens.

The Phone Configuration window opens.

Tablet Phone Device names must be in uppercase.

A message displays to inform you if the device is added successfully. The Association Information section becomes available on the Phone Configuration window.

#### Add a Directory Number to the Device

You must add directory numbers to devices in Cisco Unified Communications Manager . This topic provides instructions on adding directory numbers using the Device > Phone menu option after you create your device. Under this menu option, only the configuration settings that apply to the phone model or CTI route point display. See the Cisco Unified Communications Manager documentation for more information about different options to configure directory numbers.

The Directory Number Configuration window opens.

- Locate the Users Associated with Line section.

The Find and List Users dialog box opens.

- Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users.

- Select the appropriate users from the list.

The selected users are added to the voicemail profile.

The Apply Configuration window opens.

### Configure User Associations

When you associate a user with a device, you provision that device to the user.

The Find and List Users window opens.

The End User Configuration window opens.

The User Device Association window opens.

The End User Configuration window opens.

The Find and List Access Control Groups dialog box opens.

- Standard CCM End Users

- Standard CTI Enabled

- Cisco Unified IP Phone 9900 or 8900 series, select Standard CTI Allow Control of Phones supporting Connected Xfer and conf .

- Cisco Unified IP Phone 6900 series, select Standard CTI Allow Control of Phones supporting Rollover Mode .

The Find and List Access Control Groups window closes.

### Specify Your TFTP Server Address

The client gets device configuration from the TFTP server. For this reason, you must specify your TFTP server address when you provision users with devices.

#### Specify Your TFTP Server on Cisco Unified Communications IM and Presence

Complete the steps to specify the address of your TFTP server on Cisco Unified Communications IM and Presence .

The Legacy Client Settings window opens.

- Primary TFTP Server

#### Specify TFTP Servers in Hybrid Cloud-Based Deployments

In hybrid cloud-based deployments, you can specify your TFTP server address with the Cisco WebEx Administration Tool .

### Reset Devices

After you create and associate users with devices, you should reset those devices.

The Find and List Phones window opens.

The Phone Configuration window opens.

The Directory Number Configuration window opens.

The Device Reset dialog box opens.

### Create a CCMCIP Profile

The client gets device lists for users from the CCMCIP server.

The Find and List CCMCIP Profiles window opens.

The CCMCIP Profile Configuration window opens.

- Specify a name for the profile in the Name field.

- Specify the address of your primary CCMCIP service in the Primary CCMCIP Host field.

- Specify the hostname or IP address of your backup CCMCIP service in the Backup CCMCIP Host field.

- Leave the default value for Server Certificate Verification .

The Find and List Users dialog box opens.

- Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users.

- Select the appropriate users from the list.

The selected users are added to the CCMCIP profile.

### Dial Plan Mapping

You configure dial plan mapping to ensure that dialing rules on Cisco Unified Communications Manager match dialing rules on your directory.

#### Application Dial Rules

Application dial rules automatically add or remove digits in phone numbers that users dial. Application dialing rules manipulate numbers that users dial from the client.

For example, you can configure a dial rule that automatically adds the digit 9 to the start of a 7 digit phone number to provide access to outside lines.

#### Directory Lookup Dial Rules

Directory lookup dial rules transform caller ID numbers into numbers that the client can lookup in the directory. Each directory lookup rule you define specifies which numbers to transform based on the initial digits and the length of the number.

For example, you can create a directory lookup rule that automatically removes the area code and two digit prefix digits from 10 digit telephone numbers. An example of this type of rule is to transform 4089023139 into 23139 .

- Publish Dial Rules

#### Publish Dial Rules

Cisco Unified Communications Manager version 8.5 or lower does not automatically publish dial rules to the client. For this reason, you must deploy a COP file to publish your dial rules. This COP file copies your dial rules from the Cisco Unified Communications Manager database to an XML file on your TFTP server. The client can then download that XML file and access your dial rules.

You must deploy the COP file every time you update or modify dial rules on Cisco Unified Communications Manager version 8.5 or lower.

- Create your dial rules in Cisco Unified Communications Manager .

- Download the Cisco Jabber administration package from Cisco.com .

- Navigate to http:// tftp_server_address :6970/CUPC/AppDialRules.xml .

- Navigate to http:// tftp_server_address :6970/CUPC/DirLookupDialRules.xml .

If you can access AppDialRules.xml and DirLookupDialRules.xml with your browser, the client can download your dial rules.

After you repeat the preceding steps on each Cisco Unified Communications Manager instance, restart the client.

## Set Up Voicemail

Setting up voicemail enables users to receive voice mail messages and redirect incoming audio calls to the voicemail service. As part of the task of setting up voicemail, you can also configure a mailstore to enable visual voicemail in the client.

### Configure Cisco Unity Connection

You must create user profiles and provide users with IMAP access to configure Cisco Unity Connection. See the Cisco Unity Connection documentation for specific configuration tasks.

- Open the Cisco Unity Connection administrative interface.

The Edit Class of Service window opens.

- Locate the Licensed Features section.

- Select Allow Users to Access Voice Mail Using an IMAP Client and/or Single Inbox .

- Select Allow IMAP Users to Access Message Bodies .

- Select Save .

- Go to System Settings > Advanced > API Settings .

- Select Allow Access to Secure Message Recordings through CUMI .

### Add a Voicemail Service

Allow users to receive voice messages.

The Find and List UC Services window opens.

The UC Service Configuration window opens.

Select Unity Connection .

Enter a descriptive name for the server, for example, PrimaryVoicemailServer.

Enter an optional description.

- Hostname

- IP Address

- FQDN

Enter the port to connect to the voicemail server.

Select the appropriate protocol.

Add the voicemail service to your service profile.

#### Apply Voicemail Service

After you add a voicemail service on Cisco Unified Communications Manager , you must apply it to a service profile so that the client can retrieve the settings.

Create a service profile if none already exist or you require a separate service profile for voicemail.

The Find and List Service Profiles window opens.

The Service Profile Configuration window opens.

- Primary

- Secondary

- Tertiary

Unified CM - IM and Presence uses the instant messaging and presence credentials to log in to the voicemail service. As a result, users do not need to enter their credentials for voicemail services in the client.

Do not select Web conferencing . This option uses the conferencing credentials to log in to the voicemail service. You cannot currently synchronize with conferencing credentials.

### Add a Mailstore Service

The mailstore service provides users with visual voicemail capabilities.

The Find and List UC Services window opens.

The UC Service Configuration window opens.

Enter a descriptive name for the server, for example, PrimaryMailStoreServer.

Enter an optional description.

- Hostname

- IP Address

- FQDN

Enter the port to connect to the mailstore server.

Select the appropriate protocol.

Add the mailstore service to your service profile.

#### Apply Mailstore Service

After you add a mailstore service on Cisco Unified Communications Manager , you must apply it to a service profile so that the client can retrieve the settings.

Create a service profile if none already exist or you require a separate service profile for the mailstore service.

The Find and List Service Profiles window opens.

The Service Profile Configuration window opens.

- Primary

- Secondary

- Tertiary

- Inbox Folder

- Trash Folder

- Polling Interval

- Select the Allow dual folder mode if your mailstore supports IMAP UIDPLUS extensions.

### Configure Retrieval and Redirection

Configure retrieval so that users can access voice mail messages in the client interface. Configure redirection so that users can send incoming calls to voicemail. You configure retrieval and redirection on Cisco Unified Communications Manager .

The Find and List Voice Mail Pilots window opens.

The Voice Mail Pilot Configuration window opens.

- Specify the appropriate details on the Voice Mail Pilot Configuration window.

- Select Save .

The Find and List Voice Mail Mail Profiles window opens.

- Specify the appropriate filters in the Find Voice Mail Profile where Voice Mail Profile Name field and then select Find to retrieve a list of profiles.

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

| Note | Configuration of Cisco Unified Communications Manager IM and Presence is optional in deployments where Instant Messaging and Presence is not used. |
|---|---|

| Step 1 | Open the Cisco Unified IM and Presence Servicability interface. |
|---|---|
| Step 2 | Select Tools > Control Center - Feature Services . |
| Step 3 | Select the appropriate server from the Server drop-down list. |
| Step 4 | Ensure the following services are started and activated: Cisco SIP Proxy Cisco Sync Agent Cisco XCP Authentication Service Cisco XCP Connection Manager Cisco XCP Text Conference Manager Cisco Presence Engine |
| Step 5 | Select Tools > Control Center - Network Services . |
| Step 6 | Select the appropriate server from the Server drop-down list. |
| Step 7 | Ensure Cisco XCP Router Service is running. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > LDAP > LDAP System . The LDAP System Configuration window opens. |
| Step 3 | Locate the LDAP System Information section. |
| Step 4 | Select Enable Synchronizing from LDAP Server . |
| Step 5 | Select the type of directory server from which you are synchronizing data from the LDAP Server Type drop-down list. |

| Step 1 | Locate the LDAP Attribute for User ID drop-down list on the LDAP System Configuration window. |
|---|---|
| Step 2 | Specify an attribute for the user ID as appropriate and then select Save . Important: If the attribute for the user ID is other than sAMAccountName , you must specify the attribute as the value for the UserAccountName parameter in your client configuration file as follows: < UserAccountName > attribute-name </ UserAccountName > If you do not specify the attribute in your configuration, and the attribute is other than sAMAccountName , the client cannot resolve contacts in your directory. As a result, users do not get presence and cannot send or receive instant messages. |

| Step 1 | Select System > LDAP > LDAP Directory . |
|---|---|
| Step 2 | Select Add New . The LDAP Directory window opens. |
| Step 3 | Specify the required details on the LDAP Directory window. See the Cisco Unified Communications Manager Administration Guide for more information about the values and formats you can specify. |
| Step 4 | Select Save . |
| Step 5 | Select Peform Full Sync Now . Note The amount of time it takes for the synchronization process to complete depends on the number of users that exist in your directory. If you synchronize a large directory with thousands of users, you should expect the process to take some time. | Note | The amount of time it takes for the synchronization process to complete depends on the number of users that exist in your directory. If you synchronize a large directory with thousands of users, you should expect the process to take some time. |
| Note | The amount of time it takes for the synchronization process to complete depends on the number of users that exist in your directory. If you synchronize a large directory with thousands of users, you should expect the process to take some time. |

| Note | The amount of time it takes for the synchronization process to complete depends on the number of users that exist in your directory. If you synchronize a large directory with thousands of users, you should expect the process to take some time. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > LDAP > LDAP Authentication . |
| Step 3 | Select Use LDAP Authentication for End Users . |
| Step 4 | Specify LDAP credentials and a user search base as appropriate. See the Cisco Unified Communications Manager Administration Guide for information about the fields on the LDAP Authentication window. |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . The Find and List Service Profiles window opens. |
| Step 3 | Select Add New . The Service Profile Configuration window opens. |
| Step 4 | Enter settings on the Service Profile Configuration window as follows: Specify a unique name for the service profile in the Name field. Specify an optional description in the Description field. Select Make this the default service profile for the system , if appropriate. |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > Settings . |
| Step 3 | Select the following options: Enable instant messaging |
| Step 4 | Select other messaging settings as appropriate. |
| Step 5 | Select Save . Important: Cisco Jabber Video for iPad does not support the following settings on the Presence Settings window on Cisco Unified Communications Manager IM and Presence version 9.0.x: Use DND status when user is on the phone Use DND status when user is in a meeting Allow clients to log instant message history |

| Step 1 | Open the Cisco Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Presence > Settings . The Presence Settings window opens. |
| Step 3 | Select Allow users to view the availability of other users without being prompted for approval to disable prompts and automatically accept all presence subscription requests within your organization. This option has the following values: Selected The client does not prompt users for presence subscription requests. The client automatically accepts all presence subscription requests without prompting the users. Cleared The client prompts users to allow presence subscription requests. This setting requires users to allow other users in your organization to view their availability status. |
| Step 4 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > UC Service . The Find and List UC Services window opens. |
| Step 3 | Select Add New . The UC Service Configuration window opens. |
| Step 4 | In the Add a UC Service section, select IM and Presence from the UC Service Type drop-down list. |
| Step 5 | Select Next . |
| Step 6 | Provide details for the instant messaging and presence service as follows: Select Unified CM (IM and Presence) from the Product Type drop-down list. Specify a name for the service in the Name field. The name you specify displays when you add the service to a profile. Ensure the name you specify is unique, meaningful, and easy to identify. Specify an optional description in the Description field. Specify the instant messaging and presence service address in the Host Name/IP Address field. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . The Find and List Service Profiles window opens. |
| Step 3 | Find and select your service profile. The Service Profile Configuration window opens. |
| Step 4 | In the IM and Presence Profile section, select up to three services from the following drop-down lists: Primary Secondary Tertiary |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > UC Service . The Find and List UC Services window opens. |
| Step 3 | Select Add New . The UC Service Configuration window opens. |
| Step 4 | In the Add a UC Service section, select Directory from the UC Service Type drop-down list. |
| Step 5 | Select Next . |
| Step 6 | Provide the details for the Directory service as follows: Select Directory from the Product Type dropdown list. Specify a name for the service in the Name field. The name you specify displays when you add the service to a profile. Ensure the name you specify is unique, meaningful, and easy to identify. Specify an optional description in the Description field. Specify the Directory service address in the HostName/IPAddress field. Specify the port number used by the LDAP server. The defaults are: TCP - 389 TLS - 636 Global Catalog - 3268/3269 |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . The Find and List Service Profiles window opens. |
| Step 3 | Find and select your service profile. The Service Profile Configuration window opens. |
| Step 4 | Configure the Primary service in the Directory Profile section. Note Although three service options are available for configuration, the application only supports using the Primary service value. | Note | Although three service options are available for configuration, the application only supports using the Primary service value. |
| Note | Although three service options are available for configuration, the application only supports using the Primary service value. |
| Step 5 | Select Use Logged On User Credential . |
| Step 6 | Specify authentication accounts against the LDAP Server in the Username and Password fields. |
| Step 7 | Specify the LDAP server search base in the Search Base field. |
| Step 8 | Select Save . |

| Note | Although three service options are available for configuration, the application only supports using the Primary service value. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > End User . The Find and List Users window opens. |
| Step 3 | Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users. |
| Step 4 | Select the appropriate username from the list. The End User Configuration window opens. |
| Step 5 | Locate the Service Settings section and do the following: Select Enable User for Unified CM IM and Presence . Select your service profile from the UC Service Profile drop-down list. Important: Cisco Unified Communications Manager version 9.x only: If the user has only instant messaging and presence capabilities (IM only), you must select Use Default . For IM only users, Cisco Unified Communications Manager version 9.x always applies the default service profile regardless of what you select from the UC Service Profile drop-down list. |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Bulk Administration > Users > Update Users > Query . The Find and List Users To Update window opens. |
| Step 3 | Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users. |
| Step 4 | Select Next . The Update Users Configuration window opens. |
| Step 5 | Select both of the Enable User for Unified CM IM and Presence check boxes. Important: There are two check boxes for Enable User for Unified CM IM and Presence . To disable instant messaging and presence, you select one check box. To enable instant messaging and presence, you select both check boxes. |
| Step 6 | Select the UC Service Profile check box and then select your service profile from the drop-down list. Important: Cisco Unified Communications Manager version 9.x only: If the user has only instant messaging and presence capabilities (IM only), you must select Use Default . For IM only users, Cisco Unified Communications Manager version 9.x always applies the default service profile regardless of what you select from the UC Service Profile drop-down list. |
| Step 7 | In the Job Information section, specify if you want to run the job immediately or at a later time. |
| Step 8 | Select Submit . |

| Step 1 | Open the Cisco Unified CM Administration interface. The Find and List Phones window opens. |
|---|---|
| Step 2 | Select Device > Phone . |
| Step 3 | Select Add New . |
| Step 4 | Select Cisco Jabber for Tablet from the Phone Type dropdown list and select Next . The Phone Configuration window opens. |
| Step 5 | Specify a name for the device in the Device Name field. You should use the format TAB username for tablet device names. For example, you create a device for a user named Tanya Adams, whose username is tadams. In this case, you should specify TABTADAMS as the device name. Note Tablet Phone Device names must be in uppercase. | Note | Tablet Phone Device names must be in uppercase. |
| Note | Tablet Phone Device names must be in uppercase. |
| Step 6 | Specify configuration settings on the Phone Configuration window as appropriate. See the Phone Setup topic in the Cisco Unified Communications Manager documentation for more information about the configuration settings on this window. |
| Step 7 | Select Save . A message displays to inform you if the device is added successfully. The Association Information section becomes available on the Phone Configuration window. |

| Note | Tablet Phone Device names must be in uppercase. |
|---|---|

| Step 1 | Locate the Association Information section on the Phone Configuration window. |
|---|---|
| Step 2 | Select Add a new DN . The Directory Number Configuration window opens. |
| Step 3 | Specify a directory number in the Directory Number field. |
| Step 4 | Specify all other required configuration settings as appropriate. |
| Step 5 | Associate end users with the directory number as follows: Locate the Users Associated with Line section. Select Associate End Users . The Find and List Users dialog box opens. Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users. Select the appropriate users from the list. Select Add Selected . The selected users are added to the voicemail profile. |
| Step 6 | Select Save . |
| Step 7 | Select Apply Config . The Apply Configuration window opens. |
| Step 8 | Follow the prompts on the Apply Configuration window to apply the configuration. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > End User . The Find and List Users window opens. |
| Step 3 | Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users. |
| Step 4 | Select the appropriate user from the list. The End User Configuration window opens. |
| Step 5 | Locate the Device Information section. |
| Step 6 | Select Device Association . The User Device Association window opens. |
| Step 7 | Select the devices to which you want to associate the user. |
| Step 8 | Select Save Selected/Changes . |
| Step 9 | Select User Management > End User and return to the Find and List Users window. |
| Step 10 | Find and select the same user from the list. The End User Configuration window opens. |
| Step 11 | Locate the Permissions Information section. |
| Step 12 | Select Add to Access Control Group . The Find and List Access Control Groups dialog box opens. |
| Step 13 | Select the access control groups to which you want to assign the user. At a minimum you should assign the user to the following access control groups: Standard CCM End Users Standard CTI Enabled Certain phone models require additional control groups, as follows: Cisco Unified IP Phone 9900 or 8900 series, select Standard CTI Allow Control of Phones supporting Connected Xfer and conf . Cisco Unified IP Phone 6900 series, select Standard CTI Allow Control of Phones supporting Rollover Mode . |
| Step 14 | Select Add Selected . The Find and List Access Control Groups window closes. |
| Step 15 | Select Save on the End User Configuration window. |

| Step 1 | Open the Cisco Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Legacy Clients > Settings . The Legacy Client Settings window opens. |
| Step 3 | Locate the Legacy Client Security Settings section. |
| Step 4 | Specify the IP address of your primary and backup TFTP servers in the following fields: Primary TFTP Server Note TFTP redundancy is not supported. | Note | TFTP redundancy is not supported. |
| Note | TFTP redundancy is not supported. |
| Step 5 | Select Save . |

| Note | TFTP redundancy is not supported. |
|---|---|

| Step 1 | Open the Cisco WebEx Administration Tool . |
|---|---|
| Step 2 | Select the Configuration tab. |
| Step 3 | Select Unified Communications in the Additional Services section. The Unified Communications window opens. |
| Step 4 | Select the Clusters tab. |
| Step 5 | Select the appropriate cluster from the list. The Edit Cluster window opens. |
| Step 6 | Select Advanced Server Settings in the Cisco Unified Communications Manager Server Settings section. |
| Step 7 | Specify the IP address of your primary TFTP server in the TFTP Server field. |
| Step 8 | Specify the IP address of your backup TFTP servers in the Backup Server #1 and Backup Server #2 fields. |
| Step 9 | Select Save . The Edit Cluster window closes. |
| Step 10 | Select Save in the Unified Communications window. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . The Find and List Phones window opens. |
| Step 3 | Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices. |
| Step 4 | Select the appropriate device from the list. The Phone Configuration window opens. |
| Step 5 | Locate the Association Information section. |
| Step 6 | Select the appropriate directory number configuration. The Directory Number Configuration window opens. |
| Step 7 | Select Reset . The Device Reset dialog box opens. |
| Step 8 | Select Reset . |
| Step 9 | Select Close to close the Device Reset dialog box. |

| Step 1 | Open the Cisco Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Application > Legacy Clients > CCMCIP Profile . The Find and List CCMCIP Profiles window opens. |
| Step 3 | Select Add New . The CCMCIP Profile Configuration window opens. |
| Step 4 | Specify service details in the CCMCIP profile as follows: Specify a name for the profile in the Name field. Specify the address of your primary CCMCIP service in the Primary CCMCIP Host field. Specify the hostname or IP address of your backup CCMCIP service in the Backup CCMCIP Host field. Leave the default value for Server Certificate Verification . |
| Step 5 | Add users to the CCMCIP profile as follows: Select Add Users to Profile . The Find and List Users dialog box opens. Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users. Select the appropriate users from the list. Select Add Selected . The selected users are added to the CCMCIP profile. |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco Unified OS Administration interface. |
|---|---|
| Step 2 | Select Software Upgrades > Install/Upgrade . |
| Step 3 | Select Next . |
| Step 4 | Select Next and then select Install . |
| Step 5 | Restart the TFTP service. |
| Step 6 | Open the dial rules XML files in a browser to verify that they are available on your TFTP server. Navigate to http:// tftp_server_address :6970/CUPC/AppDialRules.xml . Navigate to http:// tftp_server_address :6970/CUPC/DirLookupDialRules.xml . If you can access AppDialRules.xml and DirLookupDialRules.xml with your browser, the client can download your dial rules. |
| Step 7 | Repeat the preceding steps for each Cisco Unified Communications Manager instance that runs a TFTP service. |

| Step 1 | Create user profiles on Cisco Unity Connection. |
|---|---|
| Step 2 | Provide users with IMAP access. Open the Cisco Unity Connection administrative interface. Select Class of Service . The Edit Class of Service window opens. Locate the Licensed Features section. Select Allow Users to Access Voice Mail Using an IMAP Client and/or Single Inbox . Select Allow IMAP Users to Access Message Bodies . Select Save . |
| Step 3 | Enable access to security message. Go to System Settings > Advanced > API Settings . Select Allow Access to Secure Message Recordings through CUMI . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > UC Service . The Find and List UC Services window opens. |
| Step 3 | Select Add New . The UC Service Configuration window opens. |
| Step 4 | In the Add a UC Service section, select Voicemail from the UC Service Type drop-down list. |
| Step 5 | Select Next . |
| Step 6 | Specify details for the voicemail service as follows: Product Type Select Unity Connection . Name Enter a descriptive name for the server, for example, PrimaryVoicemailServer. Description Enter an optional description. Hostname/IP Address Enter the address of the voicemail server in one of the following formats: Hostname IP Address FQDN Port Enter the port to connect to the voicemail server. Protocol Type Select the appropriate protocol. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . The Find and List Service Profiles window opens. |
| Step 3 | Find and select your service profile. The Service Profile Configuration window opens. |
| Step 4 | Configure the Voicemail Profile section as follows: Select up to three services from the following drop-down lists: Primary Secondary Tertiary To synchronize credentials with the voicemail service, select Unified CM - IM and Presence from the Credentials source for voicemail service drop-down list. Unified CM - IM and Presence uses the instant messaging and presence credentials to log in to the voicemail service. As a result, users do not need to enter their credentials for voicemail services in the client. Note Do not select Web conferencing . This option uses the conferencing credentials to log in to the voicemail service. You cannot currently synchronize with conferencing credentials. | Note | Do not select Web conferencing . This option uses the conferencing credentials to log in to the voicemail service. You cannot currently synchronize with conferencing credentials. |
| Note | Do not select Web conferencing . This option uses the conferencing credentials to log in to the voicemail service. You cannot currently synchronize with conferencing credentials. |
| Step 5 | Select Save . |

| Note | Do not select Web conferencing . This option uses the conferencing credentials to log in to the voicemail service. You cannot currently synchronize with conferencing credentials. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > UC Service . The Find and List UC Services window opens. |
| Step 3 | Select Add New . The UC Service Configuration window opens. |
| Step 4 | In the Add a UC Service section, select MailStore from the UC Service Type drop-down list. |
| Step 5 | Select Next . |
| Step 6 | Provide details for the mailstore service as follows: Name Enter a descriptive name for the server, for example, PrimaryMailStoreServer. Description Enter an optional description. Hostname/IP Address Enter the address of the mailstore server in one of the following formats: Hostname IP Address FQDN Port Enter the port to connect to the mailstore server. Protocol Type Select the appropriate protocol. |
| Step 7 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . The Find and List Service Profiles window opens. |
| Step 3 | Find and select your service profile. The Service Profile Configuration window opens. |
| Step 4 | Configure the MailStore Profile section as follows: Select up to three services from the following drop-down lists: Primary Secondary Tertiary Specify appropriate values for the following fields: Inbox Folder Trash Folder Polling Interval Select the Allow dual folder mode if your mailstore supports IMAP UIDPLUS extensions. |
| Step 5 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Configure the voicemail pilot. Select Advanced Features > Voice Mail > Voice Mail Pilot . The Find and List Voice Mail Pilots window opens. Select Add New . The Voice Mail Pilot Configuration window opens. Specify the appropriate details on the Voice Mail Pilot Configuration window. Select Save . |
| Step 3 | Add the voicemail pilot to the voicemail profile. Select Advanced Features > Voice Mail > Voice Mail Profile . The Find and List Voice Mail Mail Profiles window opens. Specify the appropriate filters in the Find Voice Mail Profile where Voice Mail Profile Name field and then select Find to retrieve a list of profiles. Select the appropriate profile from the list. The Voice Mail Pilot Configuration window opens. Select the voicemail pilot from the Voice Mail Pilot drop-down list. Select Save . |
| Step 4 | Specify the voicemail profile in the directory number configuration. Select Device > Phone . The Find and List Phones window opens. Specify the appropriate filters in the Find Phone where field and then select Find to retrieve a list of devices. Select the appropriate device from the list. The Phone Configuration window opens. Locate the Association Information section. Select the appropriate device number. The Directory Number Configuration window opens. Locate the Directory Number Settings section. Select the voicemail profile from the Voice Mail Profile drop-down list. Select Save . |