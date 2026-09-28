---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-ipad-9-3-x-jabi-bk-cceaf656-00-cisco-jabber-video-for-ipad-jabi-bk-cc-9cbe42ec5e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/iPad/9_3_x/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad_chapter_011.html
retrieved_at: 2026-08-21T19:43:43.242735+00:00
---

Cisco Jabber Video for iPad 9.3.4 Administration Guide

# Cisco Jabber Video for iPad 9.3.4 Administration Guide

Updated: November 22, 2013

Chapter: Set up for Cisco Unified Presence

## Chapter: Set up for Cisco Unified Presence

# Set up for Cisco Unified Presence

This chapter describes how you can set up Cisco Jabber Video for iPad using Cisco Unified Presence.

## Starting Essential Services

Start the following Cisco Unified Presence Extensible Communication Platform (XCP) services on all Cisco Unified Presence nodes in all clusters:

- Cisco Unified Presence XCP Authentication Service

- Cisco Unified Presence XCP Connection Manager

You may also start these Unified Presence XCP services on all Unified Presence nodes in all clusters, depending on what features you want to make available:

- Cisco Unified Presence XCP Text Conference Manager, for group chat

- Cisco Unified Presence XCP SIP Federation Connection Manager, to support federation services with third-party applications that use SIP

- Cisco Unified Presence XCP XMPP Federation Connection Manager, to support federation services with third-party applications that use XMPP

- Cisco Unified Presence XCP Counter Aggregator, if you want system administrators to be able to view statistical data on XMPP components

- Cisco Unified Presence XCP Message Archiver, for automatic archiving of all instant messages

Read the documentation for any feature that you are setting up before you turn on the related services. Additional work might be required.

## Firewall Requirements

Configure hardware firewalls to allow the ports to carry traffic for the application. Hardware firewalls are network devices that provide protection from unwanted traffic at an organizational level. This table lists the ports required for the deployments of Cisco Unified Communications Manager and Cisco Unified Presence. These ports must be open on all firewalls for the application to function properly.

If no port is specified in a TFTP server address, Cisco Jabber Video for iPad will try port 6970 to obtain phone setup files and dial rule files.

7080

HTTPS

## Setting Up Directory Search, IM, and Availability

Review the following topics to set up IM and availability.

Before you begin

Administrators must configure the JABBERIPAD client type if they are using Cisco Unified Presence 8.5 and above. Select Cisco Unified Presence Administration > Application > Client Types from the Cisco Unified Presence menu and ensure JABBERIPAD is included. Refer to the workaround list in caveat CSCtq15767 if this option is not available.

### Setting Up LDAP Servers

Perform this task in Cisco Unified Presence.

Do the following:

- Set up the LDAP attribute map

- Obtain the hostnames or IP addresses of the LDAP directories

LDAP server configuration is done in Cisco Unified Communications Manager starting with Release 9.0.

- TCP—389

- TLS—636

Check the LDAP directory documentation or the LDAP directory configuration for this information.

### Creating LDAP Profiles and Adding Users

Cisco Jabber Video for iPad connects to an LDAP server on a per-search basis. If the connection to the primary server fails, the application attempts the first backup LDAP server, and if it is not available, it then attempts to connect to the second backup server. The application also periodically attempts to return to the primary LDAP server. If an LDAP query is in process when the system fails over, the next available server completes this LDAP query.

Do the following:

- Specify the LDAP server names and addresses

- You must create the LDAP profile before you can add Cisco Jabber Video for iPad users to the profile.

LDAP profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0.

Optional. Enter the administrator-level account information limited to 128 characters. This is the distinguished name with which you bind for authenticated bind.

The syntax for this field depends on the type of LDAP server that you deploy. For details, see the LDAP server documentation.

For non-anonymous bind operations, Cisco Jabber Video for iPad receives one set of credentials. If configured, these credentials must be valid on the backup LDAP servers.

If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use.

### Setting Up the LDAP Attribute Map

Set up the LDAP attribute map on Cisco Unified Presence where you enter LDAP attributes for your environment and map them to the given Cisco Jabber Video for iPad attributes.

If you want to use LDAP to store your employee profile photos, use a third-party extension to upload the photo files to the LDAP server or extend the LDAP directory server schema by other means to create an attribute that the LDAP server can associate with an image.

For Cisco Jabber Video for iPad to display profile photos, in the LDAP attribute map, map the "Photo" value to the appropriate LDAP attribute.

- Contact photos may be cropped when they are displayed in Cisco Jabber Video for iPad .

- The UPC UserID setting in the LDAP attribute map must match the Cisco Unified Communications Manager user ID. This mapping allows a user to add a contact from LDAP to the contact list in Cisco Jabber Video for iPad . This field associates the LDAP user with the corresponding user on Cisco Unified Communications Manager and Cisco Unified Presence.

- You can map an LDAP field to only one field.

Select Cisco Unified CM IM and Presence > Application > Legacy Clients > Settings if you are using Release 9.0.

The LDAP server populates the LDAP attribute map with Cisco Jabber user fields and LDAP user fields.

The values are common to all LDAP server hosts. Note the following LDAP directory product mappings:

If you want to stop using the current attribute mappings and use the factory default settings, select Restore Defaults .

### Indexing Active Directory Attributes

Index these Active Directory attributes:

- sAMAccountName

- displayName

- mail

- msRTCSIP-PrimaryUserAddress

In addition, index any attributes that are used for contact resolution. For example, you might need to index these attributes:

- telephoneNumber

- Any other directory phone number attributes that are used to find contacts, depending on the value of the DisableSecondaryNumberLookups key

- ipPhone, if this attribute is used in your environment

### Turning IM Policy On or Off

This procedure describes how to turn on or off IM features for all IM applications in a Cisco Unified Presence cluster. IM features are turned on by default in Cisco Unified Presence.

If you turn off IM features in Cisco Unified Presence, all group chat functionality (ad hoc and persistent chat) will not work in Cisco Unified Presence. Cisco recommends that you do not turn on the Cisco UP XCP Text Conference service or set up an external database for persistent chat in Cisco Unified Presence.

- If you turn on this setting, users can send and receive IMs.

- If you turn off this setting, users cannot send or receive IMs. Users can use IM only for availability and phone operations.

### Specifying IM Policy Settings

You can specify IM policy settings by following these steps.

### Setting Up URL Strings to Fetch Contact Pictures from Web Server

You can set up a parameterized URL string in the Photo field in the LDAP attribute map so that Cisco Jabber Video for iPad can fetch pictures from a web server instead of from the LDAP server. The URL string must contain an LDAP attribute with a query value containing a piece of data that uniquely identifies the photo of the user. Cisco recommends that you use the User ID attribute. However, you can use any LDAP attribute whose query value contains a piece of data that uniquely identifies the photo of the user.

Cisco recommends that you use %%<userID>%% as the substitution string. For example:

- http://mycompany.example.com/photo/std/%%uid%%.jpg

- http://mycompany.example.com/photo/std/%%sAMAccountName%%.jpg

You must include the double percent symbols in this string, and they must enclose the name of the LDAP attribute to substitute. Cisco Jabber Video for iPad removes the percent symbols and replaces the parameter inside with the results of an LDAP query for the user whose photo it resolves.

For example, if a query result contains the attribute "uid" with a value of "johndoe," then a template such as http://mycompany.com/photos/%%uid%%.jpg creates the URL http://mycompany.com/photos/johndoe.jpg . Cisco Jabber Video for iPad attempts to fetch the photo.

This substitution technique works only if Cisco Jabber Video for iPad can use the results of the query and can insert it into the template you specify above to construct a working URL that fetches a JPG photo. If the web server that hosts the photos in a company requires a POST (for example, the name of the user is not in the URL) or uses some other cookie name for the photo instead of the username, this technique does not work.

- Limit a URL length to 50 characters.

- Cisco Jabber Video for iPad does not support authentication for this query; the photo must be retrievable from the web server without credentials.

## Setting Up CCMCIP Profile

Select Cisco Unified CM IM and Presence > Application > Legacy Clients > CCMCIP Profile if you are using Release 9.0.

If the CCMCIP profile is found, no further action is required from you.

Check this option if you want any new users that are added to the system to be placed automatically into this default profile.

Users who are already synchronized to Unified Presence from Unified Communications Manager are not added to the default profile. However, once the default profile is created, any users synchronized after that are added to the default profile.

## Setting Up Proxy Listener and TFTP Addresses

Cisco recommends that you use TCP to communicate with the proxy server. If you use UDP to communicate with the proxy server, availability information of the contacts in Cisco Jabber Video for iPad might be unavailable for large contact lists.

Obtain the host names or IP addresses of the TFTP servers.

Select Cisco Unified CM IM and Presence > Application > Legacy Client > Settings if you are using Release 9.0.

## Setting Up Voicemail Server Names and Addresses on Cisco Unified Presence

Specify voicemail settings on Cisco Unified Presence so that Cisco Jabber Video for iPad can interact with the voice message web service (VMWS) on Cisco Unity Connection. The VMWS service enables the application to move deleted voicemail messages to the correct location. This service also provides message encryption capabilities to support secure messaging.

Perform these tasks:

- Ensure that the voicemail server is set up.

- Obtain the hostname or IP address of the voicemail server. You might need to specify more than one hostname to provide services for the number of users in your environment.

Voicemail server configuration is done in Cisco Unified Communications Manager starting with Release 9.0.

## Setting Up Mailstore Server Names and Addresses on Cisco Unified Presence

Set up Cisco Unified Presence with mailstore information so that Cisco Jabber Video for iPad can connect to the mailstore.

Cisco Unity Connection usually provides a mailstore and hosts the mailstore on the same server.

Perform these tasks:

- Obtain the hostname or IP address of the mailstore server.

- Provision mailstore servers before you can add the servers to the voicemail profiles.

Mailstore configuration is done in Cisco Unified Communications Manager starting with Release 9.0.

## Creating Voicemail Profiles on Cisco Unified Presence

Create voicemail profiles before you can add users to the profiles.

Repeat this procedure for each voicemail profile you want to create.

Perform these tasks:

- Specify voicemail server names and addresses.

- Specify mailstore server names and addresses.

Voicemail profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0

Select one of these options:

- Number —Select the voicemail pilot number for the system. This is the same as the number specified in the Voice Mail > Voice Mail Pilot menu in Cisco Unified Communications Manager Administration.

- No Voice Mail —Select this option if you do not want to send unanswered incoming calls to voicemail.

Users who are already synchronized to Cisco Unified Presence from Cisco Unified CM are not added to the default profile. However, any users who are synchronized after the default profile is created are added to the default profile.

Default folder: INBOX

Default folder: Deleted Items

Turn off this setting if you know that UIDPLUS is not supported and you want to force the system to use Single Folder mode.

Default setting: On

The Microsoft Exchange 2007 server does not support UIDPLUS extensions.

If you configured voicemail parameters in Product Specific Configuration on Cisco Unified Communications Manager, Cisco Jabber Video for iPad will use that configuration and ignore the voicemail settings in the Cisco Unified Presence server.

| Note | Read the documentation for any feature that you are setting up before you turn on the related services. Additional work might be required. |
|---|---|

| Port | Protocol | Description |
|---|---|---|
| Inbound |
| 16384-32766 | UDP | Receives Real-Time Transport Protocol (RTP) media streams for video and audio. You set up these ports in Cisco Unified Communications Manager. |
| Outbound |
| 69, then Ephemeral | TFTP | Connects to the Trivial File Transfer Protocol (TFTP) server to download the TFTP file |
| 80 and 6970 | HTTP | Connects to services such as Cisco WebEx Messenger for meetings and Cisco Unity Connection for voicemail features If no port is specified in a TFTP server address, Cisco Jabber Video for iPad will try port 6970 to obtain phone setup files and dial rule files. |
| 5060 | UDP/TCP | Provides Session Initiation Protocol (SIP) call signaling |
| 5061 | TCP | Provides secure SIP call signaling |
| 8443 | TCP | Connects to the Cisco Unified Communications Manager IP Phone (CCMCIP) server to get a list of currently assigned devices |
| 16384-32766 | UDP | UDP Sends RTP media streams for video and audio |
| 389 | TCP | Connects to the LDAP server for contact searches |
| 443 7080 | VMRest HTTPS | Connects to Cisco Unity Connection to retrieve and manage voice messages. |
| 636 | LDAPS | Connects to the secure LDAP server for contact searches |

| Step 1 | Select Cisco Unified Presence Administration > Application > Cisco Unified Personal Communicator > LDAP Server . Note LDAP server configuration is done in Cisco Unified Communications Manager starting with Release 9.0. | Note | LDAP server configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
|---|---|---|---|
| Note | LDAP server configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
| Step 2 | Select Add New . |
| Step 3 | Enter the LDAP server name. |
| Step 4 | Enter an IP address or an FQDN (Fully Qualified Domain Name) of the LDAP server. |
| Step 5 | Specify the port number used by the LDAP server. The defaults are: TCP—389 TLS—636 Check the LDAP directory documentation or the LDAP directory configuration for this information. |
| Step 6 | Select TCP or TLS for the protocol type. |
| Step 7 | Select Save . |

| Note | LDAP server configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
|---|---|

| Step 1 | Select Cisco Unified Presence Administration > Application > Cisco Unified Personal Communicator > LDAP Profile . Note LDAP profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0. | Note | LDAP profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
|---|---|---|---|
| Note | LDAP profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
| Step 2 | Select Add New . |
| Step 3 | Enter information in the fields. Field Setting Name Enter the profile name limited to 128 characters. Description Optional. Enter a description limited to 128 characters. Bind Distinguished Name Optional. Enter the administrator-level account information limited to 128 characters. This is the distinguished name with which you bind for authenticated bind. The syntax for this field depends on the type of LDAP server that you deploy. For details, see the LDAP server documentation. Anonymous Bind Optional. Uncheck this option to use the user credentials to sign in to this LDAP server. For non-anonymous bind operations, Cisco Jabber Video for iPad receives one set of credentials. If configured, these credentials must be valid on the backup LDAP servers. Note If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. Password Optional. Enter the LDAP bind password limited to 128 characters. This is the password for the administrator-level account that you provided in the Bind Distinguished Name string to allow users to access this LDAP server. Confirm Password Reenter the password you entered in Password . Search Context Optional. Enter the location where you set up all the LDAP users. This location is a container or directory. The name is limited to 256 characters. Use only a single OU/LDAP search context. Recursive Search Optional. Check to perform a recursive search of the directory starting at the search base. Primary LDAP Server and Backup LDAP Server Select the primary LDAP server and optional backup servers. Add Users to Profile Select the button to open the Find and List Users window. Select Find to populate the search results fields. Alternatively, search for a specific user and select Find . To add users to this profile, select the users, and select Add Selected . | Field | Setting | Name | Enter the profile name limited to 128 characters. | Description | Optional. Enter a description limited to 128 characters. | Bind Distinguished Name | Optional. Enter the administrator-level account information limited to 128 characters. This is the distinguished name with which you bind for authenticated bind. The syntax for this field depends on the type of LDAP server that you deploy. For details, see the LDAP server documentation. | Anonymous Bind | Optional. Uncheck this option to use the user credentials to sign in to this LDAP server. For non-anonymous bind operations, Cisco Jabber Video for iPad receives one set of credentials. If configured, these credentials must be valid on the backup LDAP servers. Note If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. | Note | If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. | Password | Optional. Enter the LDAP bind password limited to 128 characters. This is the password for the administrator-level account that you provided in the Bind Distinguished Name string to allow users to access this LDAP server. | Confirm Password | Reenter the password you entered in Password . | Search Context | Optional. Enter the location where you set up all the LDAP users. This location is a container or directory. The name is limited to 256 characters. Use only a single OU/LDAP search context. | Recursive Search | Optional. Check to perform a recursive search of the directory starting at the search base. | Primary LDAP Server and Backup LDAP Server | Select the primary LDAP server and optional backup servers. | Add Users to Profile | Select the button to open the Find and List Users window. Select Find to populate the search results fields. Alternatively, search for a specific user and select Find . To add users to this profile, select the users, and select Add Selected . |
| Field | Setting |
| Name | Enter the profile name limited to 128 characters. |
| Description | Optional. Enter a description limited to 128 characters. |
| Bind Distinguished Name | Optional. Enter the administrator-level account information limited to 128 characters. This is the distinguished name with which you bind for authenticated bind. The syntax for this field depends on the type of LDAP server that you deploy. For details, see the LDAP server documentation. |
| Anonymous Bind | Optional. Uncheck this option to use the user credentials to sign in to this LDAP server. For non-anonymous bind operations, Cisco Jabber Video for iPad receives one set of credentials. If configured, these credentials must be valid on the backup LDAP servers. Note If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. | Note | If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. |
| Note | If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. |
| Password | Optional. Enter the LDAP bind password limited to 128 characters. This is the password for the administrator-level account that you provided in the Bind Distinguished Name string to allow users to access this LDAP server. |
| Confirm Password | Reenter the password you entered in Password . |
| Search Context | Optional. Enter the location where you set up all the LDAP users. This location is a container or directory. The name is limited to 256 characters. Use only a single OU/LDAP search context. |
| Recursive Search | Optional. Check to perform a recursive search of the directory starting at the search base. |
| Primary LDAP Server and Backup LDAP Server | Select the primary LDAP server and optional backup servers. |
| Add Users to Profile | Select the button to open the Find and List Users window. Select Find to populate the search results fields. Alternatively, search for a specific user and select Find . To add users to this profile, select the users, and select Add Selected . |
| Step 4 | Select Save . |

| Note | LDAP profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
|---|---|

| Field | Setting |
|---|---|
| Name | Enter the profile name limited to 128 characters. |
| Description | Optional. Enter a description limited to 128 characters. |
| Bind Distinguished Name | Optional. Enter the administrator-level account information limited to 128 characters. This is the distinguished name with which you bind for authenticated bind. The syntax for this field depends on the type of LDAP server that you deploy. For details, see the LDAP server documentation. |
| Anonymous Bind | Optional. Uncheck this option to use the user credentials to sign in to this LDAP server. For non-anonymous bind operations, Cisco Jabber Video for iPad receives one set of credentials. If configured, these credentials must be valid on the backup LDAP servers. Note If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. | Note | If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. |
| Note | If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. |
| Password | Optional. Enter the LDAP bind password limited to 128 characters. This is the password for the administrator-level account that you provided in the Bind Distinguished Name string to allow users to access this LDAP server. |
| Confirm Password | Reenter the password you entered in Password . |
| Search Context | Optional. Enter the location where you set up all the LDAP users. This location is a container or directory. The name is limited to 256 characters. Use only a single OU/LDAP search context. |
| Recursive Search | Optional. Check to perform a recursive search of the directory starting at the search base. |
| Primary LDAP Server and Backup LDAP Server | Select the primary LDAP server and optional backup servers. |
| Add Users to Profile | Select the button to open the Find and List Users window. Select Find to populate the search results fields. Alternatively, search for a specific user and select Find . To add users to this profile, select the users, and select Add Selected . |

| Note | If you check Anonymous Bind , users can sign in anonymously to the LDAP server with read-only access. Anonymous access might be possible on your directory server, but Cisco does not recommend it. Instead, create a user with read-only privileges on the same directory where the users to be searched are located. Specify the directory number and password in Cisco Unified Presence for the application to use. |
|---|---|

| Note | Contact photos may be cropped when they are displayed in Cisco Jabber Video for iPad . The UPC UserID setting in the LDAP attribute map must match the Cisco Unified Communications Manager user ID. This mapping allows a user to add a contact from LDAP to the contact list in Cisco Jabber Video for iPad . This field associates the LDAP user with the corresponding user on Cisco Unified Communications Manager and Cisco Unified Presence. You can map an LDAP field to only one field. |
|---|---|

| Step 1 | Select Cisco Unified Presence Administration > Application > Cisco Unified Personal Communicator > Settings . Select Cisco Unified CM IM and Presence > Application > Legacy Clients > Settings if you are using Release 9.0. |
|---|---|
| Step 2 | Select a supported LDAP server from Directory Server Type . The LDAP server populates the LDAP attribute map with Cisco Jabber user fields and LDAP user fields. |
| Step 3 | If necessary, make modifications to the LDAP field to match your specific LDAP directory. The values are common to all LDAP server hosts. Note the following LDAP directory product mappings: Product LastName Mapping UserID Mapping Microsoft Active Directory SN sAMAccountName OpenLDAP SN uid | Product | LastName Mapping | UserID Mapping | Microsoft Active Directory | SN | sAMAccountName | OpenLDAP | SN | uid |
| Product | LastName Mapping | UserID Mapping |
| Microsoft Active Directory | SN | sAMAccountName |
| OpenLDAP | SN | uid |
| Step 4 | Select Save . Tip If you want to stop using the current attribute mappings and use the factory default settings, select Restore Defaults . | Tip | If you want to stop using the current attribute mappings and use the factory default settings, select Restore Defaults . |
| Tip | If you want to stop using the current attribute mappings and use the factory default settings, select Restore Defaults . |

| Product | LastName Mapping | UserID Mapping |
|---|---|---|
| Microsoft Active Directory | SN | sAMAccountName |
| OpenLDAP | SN | uid |

| Tip | If you want to stop using the current attribute mappings and use the factory default settings, select Restore Defaults . |
|---|---|

| Caution | If you turn off IM features in Cisco Unified Presence, all group chat functionality (ad hoc and persistent chat) will not work in Cisco Unified Presence. Cisco recommends that you do not turn on the Cisco UP XCP Text Conference service or set up an external database for persistent chat in Cisco Unified Presence. |
|---|---|

| Step 1 | Select Cisco Unified Presence Administration > Messaging > Settings . |
|---|---|
| Step 2 | Select Enable instant messaging . Note If you turn on this setting, users can send and receive IMs. If you turn off this setting, users cannot send or receive IMs. Users can use IM only for availability and phone operations. | Note | If you turn on this setting, users can send and receive IMs. If you turn off this setting, users cannot send or receive IMs. Users can use IM only for availability and phone operations. |
| Note | If you turn on this setting, users can send and receive IMs. If you turn off this setting, users cannot send or receive IMs. Users can use IM only for availability and phone operations. |
| Step 3 | Select Save . |
| Step 4 | Restart the Cisco UP XCP Router service. |

| Note | If you turn on this setting, users can send and receive IMs. If you turn off this setting, users cannot send or receive IMs. Users can use IM only for availability and phone operations. |
|---|---|

| Step 1 | Select Cisco Unified Presence Administration > Presence > Settings . |
|---|---|
| Step 2 | Turn on or off automatic authorization for viewing availability. If you want to… Do this… Turn on automatic authorization so that Unified Presence automatically authorizes all availability subscription requests it receives from users in the local enterprise Check Allow users to view the availability of other users without being prompted for approval . Turn off automatic authorization so that Unified Presence sends all availability subscriptions to where the user is prompted to authorize or reject the subscription Uncheck Allow users to view the availability of other users without being prompted for approval . | If you want to… | Do this… | Turn on automatic authorization so that Unified Presence automatically authorizes all availability subscription requests it receives from users in the local enterprise | Check Allow users to view the availability of other users without being prompted for approval . | Turn off automatic authorization so that Unified Presence sends all availability subscriptions to where the user is prompted to authorize or reject the subscription | Uncheck Allow users to view the availability of other users without being prompted for approval . |
| If you want to… | Do this… |
| Turn on automatic authorization so that Unified Presence automatically authorizes all availability subscription requests it receives from users in the local enterprise | Check Allow users to view the availability of other users without being prompted for approval . |
| Turn off automatic authorization so that Unified Presence sends all availability subscriptions to where the user is prompted to authorize or reject the subscription | Uncheck Allow users to view the availability of other users without being prompted for approval . |
| Step 3 | Select Cisco Unified Presence Administration > Messaging > Settings . |
| Step 4 | Turn on or off these global settings: If you want to… Do this… Globally turn off instant messaging services Uncheck Enable instant messaging . Globally turn on offline instant messaging Uncheck Suppress Offline Instant Messaging . | If you want to… | Do this… | Globally turn off instant messaging services | Uncheck Enable instant messaging . | Globally turn on offline instant messaging | Uncheck Suppress Offline Instant Messaging . |
| If you want to… | Do this… |
| Globally turn off instant messaging services | Uncheck Enable instant messaging . |
| Globally turn on offline instant messaging | Uncheck Suppress Offline Instant Messaging . |
| Step 5 | Select Save . |
| Step 6 | Restart the Cisco UP XCP Router service. |

| If you want to… | Do this… |
|---|---|
| Turn on automatic authorization so that Unified Presence automatically authorizes all availability subscription requests it receives from users in the local enterprise | Check Allow users to view the availability of other users without being prompted for approval . |
| Turn off automatic authorization so that Unified Presence sends all availability subscriptions to where the user is prompted to authorize or reject the subscription | Uncheck Allow users to view the availability of other users without being prompted for approval . |

| If you want to… | Do this… |
|---|---|
| Globally turn off instant messaging services | Uncheck Enable instant messaging . |
| Globally turn on offline instant messaging | Uncheck Suppress Offline Instant Messaging . |

| Note | Limit a URL length to 50 characters. Cisco Jabber Video for iPad does not support authentication for this query; the photo must be retrievable from the web server without credentials. |
|---|---|

| Step 1 | Select Cisco Unified Presence Administration > Application > Cisco Unified Personal Communicator > CCMCIP Profile . Select Cisco Unified CM IM and Presence > Application > Legacy Clients > CCMCIP Profile if you are using Release 9.0. |
|---|---|
| Step 2 | Search for the CCMCIP profile in the Find and List CCMCIP Profiles window. If the CCMCIP profile is found, no further action is required from you. |
| Step 3 | If the CCMCIP profile is not found, select Add New . |
| Step 4 | Enter the following information into the fields. Field Setting Name Enter the profile name. Description Enter a profile description. Primary CCMCIP Host and Backup CCMCIP Host Select a primary server and a backup server. Make this the Default CCMCIP Profile for the System Check this option if you want any new users that are added to the system to be placed automatically into this default profile. Users who are already synchronized to Unified Presence from Unified Communications Manager are not added to the default profile. However, once the default profile is created, any users synchronized after that are added to the default profile. | Field | Setting | Name | Enter the profile name. | Description | Enter a profile description. | Primary CCMCIP Host and Backup CCMCIP Host | Select a primary server and a backup server. | Make this the Default CCMCIP Profile for the System | Check this option if you want any new users that are added to the system to be placed automatically into this default profile. Users who are already synchronized to Unified Presence from Unified Communications Manager are not added to the default profile. However, once the default profile is created, any users synchronized after that are added to the default profile. |
| Field | Setting |
| Name | Enter the profile name. |
| Description | Enter a profile description. |
| Primary CCMCIP Host and Backup CCMCIP Host | Select a primary server and a backup server. |
| Make this the Default CCMCIP Profile for the System | Check this option if you want any new users that are added to the system to be placed automatically into this default profile. Users who are already synchronized to Unified Presence from Unified Communications Manager are not added to the default profile. However, once the default profile is created, any users synchronized after that are added to the default profile. |
| Step 5 | Select Add Users to Profile . |
| Step 6 | Use the Find and List Users window to find and select users. |
| Step 7 | Select Add Selected to add users to the profile. |
| Step 8 | Select Save in the main CCMCIP Profile window. |

| Field | Setting |
|---|---|
| Name | Enter the profile name. |
| Description | Enter a profile description. |
| Primary CCMCIP Host and Backup CCMCIP Host | Select a primary server and a backup server. |
| Make this the Default CCMCIP Profile for the System | Check this option if you want any new users that are added to the system to be placed automatically into this default profile. Users who are already synchronized to Unified Presence from Unified Communications Manager are not added to the default profile. However, once the default profile is created, any users synchronized after that are added to the default profile. |

| Step 1 | Select Cisco Unified Presence Administration > Application > Cisco Unified Personal Communicator > Settings . Note Select Cisco Unified CM IM and Presence > Application > Legacy Client > Settings if you are using Release 9.0. | Note | Select Cisco Unified CM IM and Presence > Application > Legacy Client > Settings if you are using Release 9.0. |
|---|---|---|---|
| Note | Select Cisco Unified CM IM and Presence > Application > Legacy Client > Settings if you are using Release 9.0. |
| Step 2 | Select the Proxy Listener Default Cisco SIP Proxy TCP Listener . |
| Step 3 | Assign the primary (required) and backup (optional) TFTP server addresses in the fields provided. You can enter an IP address or an FQDN (Fully Qualified Domain Name). |
| Step 4 | Select Save . |

| Note | Select Cisco Unified CM IM and Presence > Application > Legacy Client > Settings if you are using Release 9.0. |
|---|---|

| Step 1 | Select Cisco Unified Presence Administration > Application > Cisco Unified Personal Communicator > Voicemail Server . Note Voicemail server configuration is done in Cisco Unified Communications Manager starting with Release 9.0. | Note | Voicemail server configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
|---|---|---|---|
| Note | Voicemail server configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
| Step 2 | Select Add New . |
| Step 3 | Select Unity Connection from the Server Type menu |
| Step 4 | Enter the Cisco Unity Connection server name. |
| Step 5 | Enter the hostname or the IP address of the voicemail server. |
| Step 6 | Enter 443 for the Web Service Port value. |
| Step 7 | Select HTTPS in Web Service Protocol menu. |
| Step 8 | Select Save . |

| Note | Voicemail server configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
|---|---|

| Step 1 | Select Cisco Unified Presence Administration > Application > Cisco Unified Personal Communicator > Mailstore . Note Mailstore configuration is done in Cisco Unified Communications Manager starting with Release 9.0. | Note | Mailstore configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
|---|---|---|---|
| Note | Mailstore configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
| Step 2 | Select Add New . |
| Step 3 | Enter the mailstore server name. |
| Step 4 | Enter the hostname or the IP address of the mailstore server. |
| Step 5 | Specify the port number set up for the server and the corresponding protocol to use when Cisco Jabber Video for iPad contacts this server. |
| Step 6 | Select Save . |

| Note | Mailstore configuration is done in Cisco Unified Communications Manager starting with Release 9.0. |
|---|---|

| Step 1 | Select Cisco Unified Presence Administration > Application > Cisco Unified Personal Communicator > Voicemail Profile . Note Voicemail profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0 | Note | Voicemail profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0 |
|---|---|---|---|
| Note | Voicemail profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0 |
| Step 2 | Select Add New . |
| Step 3 | Enter the profile name and description. |
| Step 4 | Enter the following information: Field Description Voice Messaging Pilot The voicemail pilot number is the directory number that a user dials to access their voice messages. Each pilot number can belong to a different voice-messaging system. Select one of these options: Number —Select the voicemail pilot number for the system. This is the same as the number specified in the Voice Mail > Voice Mail Pilot menu in Cisco Unified Communications Manager Administration. No Voice Mail —Select this option if you do not want to send unanswered incoming calls to voicemail. Primary Voicemail Server Select a primary server. Select one of the voicemail servers you specified. Backup Voicemail Server Enter the name of your backup voicemail server. If you do not want a backup voicemail server, select None . Primary Mailstore Select the primary mailstore server. Select one of the mailstore servers you specified. Backup Mailstore Enter the name of your backup mailstore server. If you do not want a backup voicemail server, select None . Make this the default Voicemail Profile for the system Check this option if you want new users to be automatically added to the default profile. Users who are already synchronized to Cisco Unified Presence from Cisco Unified CM are not added to the default profile. However, any users who are synchronized after the default profile is created are added to the default profile. | Field | Description | Voice Messaging Pilot | The voicemail pilot number is the directory number that a user dials to access their voice messages. Each pilot number can belong to a different voice-messaging system. Select one of these options: Number —Select the voicemail pilot number for the system. This is the same as the number specified in the Voice Mail > Voice Mail Pilot menu in Cisco Unified Communications Manager Administration. No Voice Mail —Select this option if you do not want to send unanswered incoming calls to voicemail. | Primary Voicemail Server | Select a primary server. Select one of the voicemail servers you specified. | Backup Voicemail Server | Enter the name of your backup voicemail server. If you do not want a backup voicemail server, select None . | Primary Mailstore | Select the primary mailstore server. Select one of the mailstore servers you specified. | Backup Mailstore | Enter the name of your backup mailstore server. If you do not want a backup voicemail server, select None . | Make this the default Voicemail Profile for the system | Check this option if you want new users to be automatically added to the default profile. Users who are already synchronized to Cisco Unified Presence from Cisco Unified CM are not added to the default profile. However, any users who are synchronized after the default profile is created are added to the default profile. |
| Field | Description |
| Voice Messaging Pilot | The voicemail pilot number is the directory number that a user dials to access their voice messages. Each pilot number can belong to a different voice-messaging system. Select one of these options: Number —Select the voicemail pilot number for the system. This is the same as the number specified in the Voice Mail > Voice Mail Pilot menu in Cisco Unified Communications Manager Administration. No Voice Mail —Select this option if you do not want to send unanswered incoming calls to voicemail. |
| Primary Voicemail Server | Select a primary server. Select one of the voicemail servers you specified. |
| Backup Voicemail Server | Enter the name of your backup voicemail server. If you do not want a backup voicemail server, select None . |
| Primary Mailstore | Select the primary mailstore server. Select one of the mailstore servers you specified. |
| Backup Mailstore | Enter the name of your backup mailstore server. If you do not want a backup voicemail server, select None . |
| Make this the default Voicemail Profile for the system | Check this option if you want new users to be automatically added to the default profile. Users who are already synchronized to Cisco Unified Presence from Cisco Unified CM are not added to the default profile. However, any users who are synchronized after the default profile is created are added to the default profile. |
| Step 5 | Enter the following information: Field Description Inbox Folder Enter the name of the folder on the mailstore server in which new messages are stored. Only change this value if the mailstore server uses a different folder name from the default folder. Default folder: INBOX Trash Folder Enter the name of the folder on the mailstore server in which deleted messages are stored. Only change this value if the mailstore server uses a different folder name from the default folder. Default folder: Deleted Items Allow dual folder mode Turn off this setting if you know that UIDPLUS is not supported and you want to force the system to use Single Folder mode. Default setting: On Note The Microsoft Exchange 2007 server does not support UIDPLUS extensions. | Field | Description | Inbox Folder | Enter the name of the folder on the mailstore server in which new messages are stored. Only change this value if the mailstore server uses a different folder name from the default folder. Default folder: INBOX | Trash Folder | Enter the name of the folder on the mailstore server in which deleted messages are stored. Only change this value if the mailstore server uses a different folder name from the default folder. Default folder: Deleted Items | Allow dual folder mode | Turn off this setting if you know that UIDPLUS is not supported and you want to force the system to use Single Folder mode. Default setting: On Note The Microsoft Exchange 2007 server does not support UIDPLUS extensions. | Note | The Microsoft Exchange 2007 server does not support UIDPLUS extensions. |
| Field | Description |
| Inbox Folder | Enter the name of the folder on the mailstore server in which new messages are stored. Only change this value if the mailstore server uses a different folder name from the default folder. Default folder: INBOX |
| Trash Folder | Enter the name of the folder on the mailstore server in which deleted messages are stored. Only change this value if the mailstore server uses a different folder name from the default folder. Default folder: Deleted Items |
| Allow dual folder mode | Turn off this setting if you know that UIDPLUS is not supported and you want to force the system to use Single Folder mode. Default setting: On Note The Microsoft Exchange 2007 server does not support UIDPLUS extensions. | Note | The Microsoft Exchange 2007 server does not support UIDPLUS extensions. |
| Note | The Microsoft Exchange 2007 server does not support UIDPLUS extensions. |
| Step 6 | Select Add Users to Profile . |
| Step 7 | Use the Find and List Users window to find and select users, and select Add Selected to add users to the profile. |
| Step 8 | Select Save . Note If you configured voicemail parameters in Product Specific Configuration on Cisco Unified Communications Manager, Cisco Jabber Video for iPad will use that configuration and ignore the voicemail settings in the Cisco Unified Presence server. | Note | If you configured voicemail parameters in Product Specific Configuration on Cisco Unified Communications Manager, Cisco Jabber Video for iPad will use that configuration and ignore the voicemail settings in the Cisco Unified Presence server. |
| Note | If you configured voicemail parameters in Product Specific Configuration on Cisco Unified Communications Manager, Cisco Jabber Video for iPad will use that configuration and ignore the voicemail settings in the Cisco Unified Presence server. |

| Note | Voicemail profile configuration is done in Cisco Unified Communications Manager starting with Release 9.0 |
|---|---|

| Field | Description |
|---|---|
| Voice Messaging Pilot | The voicemail pilot number is the directory number that a user dials to access their voice messages. Each pilot number can belong to a different voice-messaging system. Select one of these options: Number —Select the voicemail pilot number for the system. This is the same as the number specified in the Voice Mail > Voice Mail Pilot menu in Cisco Unified Communications Manager Administration. No Voice Mail —Select this option if you do not want to send unanswered incoming calls to voicemail. |
| Primary Voicemail Server | Select a primary server. Select one of the voicemail servers you specified. |
| Backup Voicemail Server | Enter the name of your backup voicemail server. If you do not want a backup voicemail server, select None . |
| Primary Mailstore | Select the primary mailstore server. Select one of the mailstore servers you specified. |
| Backup Mailstore | Enter the name of your backup mailstore server. If you do not want a backup voicemail server, select None . |
| Make this the default Voicemail Profile for the system | Check this option if you want new users to be automatically added to the default profile. Users who are already synchronized to Cisco Unified Presence from Cisco Unified CM are not added to the default profile. However, any users who are synchronized after the default profile is created are added to the default profile. |

| Field | Description |
|---|---|
| Inbox Folder | Enter the name of the folder on the mailstore server in which new messages are stored. Only change this value if the mailstore server uses a different folder name from the default folder. Default folder: INBOX |
| Trash Folder | Enter the name of the folder on the mailstore server in which deleted messages are stored. Only change this value if the mailstore server uses a different folder name from the default folder. Default folder: Deleted Items |
| Allow dual folder mode | Turn off this setting if you know that UIDPLUS is not supported and you want to force the system to use Single Folder mode. Default setting: On Note The Microsoft Exchange 2007 server does not support UIDPLUS extensions. | Note | The Microsoft Exchange 2007 server does not support UIDPLUS extensions. |
| Note | The Microsoft Exchange 2007 server does not support UIDPLUS extensions. |

| Note | The Microsoft Exchange 2007 server does not support UIDPLUS extensions. |
|---|---|

| Note | If you configured voicemail parameters in Product Specific Configuration on Cisco Unified Communications Manager, Cisco Jabber Video for iPad will use that configuration and ignore the voicemail settings in the Cisco Unified Presence server. |
|---|---|