---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-6-cjab-b-planning-guide-cisco-jabber-116-cjab-b-planning-guide-cis-9db0ca4e52
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_6/cjab_b_planning-guide-cisco-jabber-116/cjab_b_planning-guide-cisco-jabber-116_chapter_0110.html
retrieved_at: 2026-08-21T19:44:16.162294+00:00
---

Planning Guide for Cisco Jabber 11.6

# Planning Guide for Cisco Jabber 11.6

Updated: April 20, 2016

Chapter: Contact Source

## Chapter: Contact Source

# Contact Source

## Directory Servers

Cisco Jabber for Windows, Cisco Jabber for Mac , Cisco Jabber for iPhone
                                                				  and iPad , and Cisco Jabber for Android support the LDAPv3 standard for directory integration. Any directory server that supports this standard should be compatible
                                             with these clients.

Active Directory Domain Services for Windows Server 2012 R2

Active Directory Domain Services for Windows Server 2008 R2

Cisco Unified
                                          				  Communications Manager User Data Server (UDS)

- Cisco Unified
                                                				  Communications Manager , version 9.1(2), with the following Cisco Options Package (COP) file: cmterm-cucm-uds-912-5.cop.sgn .

- Cisco Unified
                                                				  Communications Manager , version 10.0(1). No COP file is required.

OpenLDAP

Active Directory Lightweight Directory Service (AD LDS) or Active Directory Application Mode (ADAM)

Directory integration with OpenLDAP , AD LDS, or ADAM requires that you define specific parameters in a Cisco Jabber configuration file.

## What is a Contact
                        	 Source?

A contact source is a collection of data for users. When users search
                              		  for contacts or add contacts in the Cisco Jabber client, the contact
                              		  information is read from a contact source.

Cisco Jabber retrieves the information from the contact source to
                              		  populate contact lists, update contact cards in the client and other areas that
                              		  display contact information. When the client receives any incoming
                              		  communications, for example an instant message or a voice/video call, the
                              		  contact source is used to resolve the contact information.

## When to Configure
                        	 Directory Integration

Install Cisco Jabber for Windows on a workstation that is registered to an Active Directory domain. In this environment, you do not need to configure Cisco
                                             Jabber for Windows to connect to the directory. The client automatically discovers the directory and connects to a Global Catalog server in
                                             that domain.

Domain Controller

Cisco Unified Communications Manager User Data Service

OpenLDAP

Active Directory Lightweight Directory Service

Active Directory Application Mode

Change the
                                       				default attribute mappings.

Adjust
                                       				directory query settings.

Specify how
                                       				the client retrieves contact photos.

Perform
                                       				intradomain federation.

## Why Do I Need a
                        	 Contact Source?

Users search for a contact—The client takes the information
                                       				entered and searches in the contact source. Information is retrieved from the
                                       				contact source and the client will display the available methods to interact
                                       				with the contact.

Client receives incoming notification—The client will take the
                                       				information from the incoming notification and resolve the URI, number,
                                       				JabberID with a contact from the contact source. The client will display the
                                       				contact details in the alert.

## Contact Source Options

In on-premises deployments, the client requires one of the following
                              		  contact sources to resolve directory look ups for user information:

Enhanced Directory Integration (EDI)—Select this option to deploy Cisco Jabber for Windows.

Basic Directory Integration (BDI)—Select this option to deploy Cisco Jabber for Mac, iOS, and Android.

Cisco Directory Integration (CDI)—Use this contact source option to deploy all clients.

Cisco Unified Communications Manager User Data Service (UDS)—If
                                    				you do not have a corporate directory or if your deployment includes users
                                    				connecting with Expressway Mobile and Remote Access, you can use this option.

### LDAP Options: EDI and BDI

#### Enhanced Directory
                              	 Integration

EDI uses native 
                                    		  Microsoft Windows APIs to retrieve contact data from
                                    		  the directory service.

Cisco Jabber integrates with 
                                             				Active Directory as the contact source.

Cisco Jabber automatically discovers and connects
                                             				to a 
                                             				Global Catalog.

Gets the DNS
                                             				domain from the workstation and looks up the SRV record for the 
                                             				Global Catalog.

Retrieves the
                                             				address of the 
                                             				Global Catalog from the SRV record.

Connects to
                                             				the 
                                             				Global Catalog with the logged in user's
                                             				credentials.

##### Domain Name
                                 	 Retrieval

Cisco Jabber for Windows retrieves the fully qualified DNS domain from the USERDNSDOMAIN environment variable on the client workstation.

After the client
                                    		gets the DNS domain, it can locate the Domain Name Server and retrieve SRV
                                    		records.

If the USERDNSDOMAIN environment variable is not present, you can deploy the LdapUserDomain configuration parameter to specify which domain to execute the request for the LDAP service. If that parameter is not configured,
                                    then Jabber uses the domain from the email address screen.

In some instances,
                                    		the value of the USERDNSDOMAIN environment variable does not resolve
                                    		to the DNS domain that corresponds to the domain of the entire forest. For
                                    		example, when an organization uses a sub-domain or resource domain. In this
                                    		case, the USERDNSDOMAIN environment variable resolves to a
                                    		child domain, not the parent domain. As a result, the client cannot access
                                    		information for all users in the organization.

If the USERDNSDOMAIN environment variable resolves to a child domain, you can use one of the following options to enable Cisco Jabber for Windows to connect to a service in the parent domain:

Ensure that the
                                          			 Global Catalog or LDAP directory server can access all users in the
                                          			 organization.

Configure your DNS server to direct the client to a server that can access all users in the organization when Cisco Jabber
                                          for Windows requests a Global Catalog or LDAP directory server.

Configure Cisco Jabber for Windows to use the FQDN of the domain controller.

```
<PrimaryServerName> parent-domain-fqdn </PrimaryServerName>
```

##### Directory Server Discovery

The workstation on which you install Cisco Jabber automatically detects the workstation by determining the user domain.

The workstation retrieves the server connection address from the DNS SRV record.

Directory Server

SRV Record

Global Catalog

_gc._msdcs._tcp. domain.com

Domain Controller

LDAP-based directory servers

_ldap._msdcs._tcp. domain.com

#### Basic Directory
                              Integration

The client retrieves contact data from the directory service as follows.

The client
                                       connects to the Cisco Unified Communication Manager
                                       IM and Presence Service node.

The client gets the LDAP profile configuration section in the service profile from the Cisco Unified Communication Manager
                                       IM and Presence Service
                                       node.

The service
                                       profile contains the location of Cisco Unified Communication Manager (TFTP)
                                       node. Depending on your configuration, the service profile can also contain the credentials to authenticate with the directory.

The client
                                       connects to the Cisco Unified Communication Manager node.

The client
                                       downloads the client configuration file from the Cisco Unified Communication
                                       Manager node.

The client
                                       configuration file contains the location of the directory. Depending on your configuration, the client configuration file
                                       can also contain the credentials
                                       to authenticate with the directory.

The client uses
                                       the directory location and the authentication credentials to connect to the
                                       directory.

### Cisco Unified Communications Manager User Data Service

User Data Service (UDS) is a REST interface on Cisco Unified Communications Manager that provides contact resolution.

If you set the DirectoryServerType parameter to use a value of UDS in the client configuration file.

With this configuration, the client uses UDS for contact resolution when it is inside or outside of the corporate firewall.

If you deploy Expressway for Remote and Mobile Access.

With this configuration, the client automatically uses UDS for contact resolution when it is outside of the corporate firewall.

You synchronize contact data into Cisco Unified Communications Manager from a directory server. Cisco Jabber then automatically
                                 retrieves that contact data from UDS.

#### Contact Resolution
                              	 with Multiple Clusters

For contact
                                 		resolution with multiple Cisco Unified Communications Manager clusters, synchronize all users on
                                 		the corporate directory to each cluster. Provision a subset of those users on
                                 		the appropriate cluster.

cucm-cluster-na for North America

cucm-cluster-eu for Europe

When users in
                                 		Europe call users in North America, 
                                 		Cisco Jabber retrieves the contact details for
                                 		the user in Europe from cucm-cluster-na .

When users in North
                                 		America call users in Europe, 
                                 		Cisco Jabber retrieves the contact details for
                                 		the user in North America from cucm-cluster-eu .

## LDAP
                        	 Prerequisites

Cisco Jabber
                              		  searches the contact source using various attributes, not all of these
                              		  attributes are indexed by default. To ensure efficient searches the attributes
                              		  used by Cisco Jabber must be indexed.

sAMAccountName

displayName

sn

name

proxyAddresses

mail

department

givenName

telephoneNumber

otherTelephone

mobile

homePhone

msRTCSIP-PrimaryUserAddress

### LDAP Service
                           	 Account

Cisco Jabber uses
                                 		  an account to authenticate with the directory server. We recommend that this
                                 		  account has read-only access to the directory and is a commonly known public
                                 		  set of credentials.

Configure Cisco Jabber to connect to a directory server using a service profile or using parameters in the jabber-config.xml file. Cisco Jabber for all clients for Windows connects to a Global Catalog server by default and this is the recommended method for Cisco Jabber for all clients for Windows , you do not need to configure Cisco Jabber for all clients for Windows to connect to the directory.

## Jabber ID
                        	 Attribute Mapping

The LDAP attribute for user ID is sAMAccountName. This is the default attribute.

If the attribute for the user ID is other than sAMAccountName, and you're using the default IM address scheme in Cisco Unified
                              Communications Manager IM and Presence Service, you must specify the attribute as the value for the parameter in your client
                              configuration file as follows:

The EDI parameter is UserAccountName. <UserAccountName>attribute-name</UserAccountName>

The BDI parameter is BDIUserAccountName. <BDIUserAccountName>attribute-name</BDIUserAccountName>

If you do not specify the attribute in your configuration, and the
                              		  attribute is other than sAMAccountName, the client cannot resolve contacts in
                              		  your directory. As a result, users do not get presence and cannot send or
                              		  receive instant messages.

### Search Jabber
                           	 IDs

Cisco Jabber uses the Jabber ID to search for contact information in
                                 		  the directory. There are a few options to optimize searching in the directory:

Search base—By default the client will start a search at the root
                                       				of a directory tree. You can use search bases to specify a different search
                                       				start or to restrict searches to specific groups. For example, a subset of your
                                       				users have instant messaging capabilities only. Include those users in an OU
                                       				and then specify that as a search base.

Base Filter—Specify a directory subkey name only to retrieve
                                       				objects other than user objects when you query the directory.

Predictive Search Filter—You can define multiple, comma-separated
                                       				values to filter search queries. The default value is ANR(Ambiguous name
                                       				resolution.)

## Local Contact
                        	 Sources

Local contacts
                                       				stored in Microsoft Outlook are accessed by Cisco Jabber for Windows.

Local contacts stored in IBM Notes are accessed by Cisco Jabber for Windows (from release 11.1).

Local address
                                       				book contacts are accessed by Cisco Jabber for Mac, Cisco Jabber for Android
                                       				and Cisco Jabber for iPhone and iPad.

## Custom Contact
                        	 Sources

Cisco Jabber for all clients for Windows provides users with the ability to import custom contacts into their client. For more information see the Import contact lists topic in the Cisco Jabber for all clients for Windows User Guide.

## Contact
                        	 Caching

Cisco Jabber creates a local cache of the users contact list. When a
                              		  user searches for somebody in their contact list, Cisco Jabber searches the
                              		  local cache for a match before starting a directory search.

If a user searches for somebody who is not in their contact list,
                              		  Cisco Jabber will search the local cache for a match and then Cisco Jabber will
                              		  search the company directory for a match. If the user starts a chat or a call
                              		  with this contact, the contact information is added to the local cache.
                              		  Subsequent searches for this contact will return the contact information in a Contacts or recents list.

The local cache information expires after 24 hours.

## Dial Plan
                           		Mapping

You configure dial
                              		  plan mapping to ensure that dialing rules on 
                              		  Cisco Unified Communications Manager match dialing rules on your
                              		  directory.

### Application
                              		  Dial Rules

Application dial
                              		  rules automatically add or remove digits in phone numbers that users dial.
                              		  Application dialing rules manipulate numbers that users dial from the client.

For example, you
                              		  can configure a dial rule that automatically adds the digit 9 to the start of a
                              		  7 digit phone number to provide access to outside lines.

### Directory
                              		  Lookup Dial Rules

Directory lookup
                              		  dial rules transform caller ID numbers into numbers that the client can lookup
                              		  in the directory. Each directory lookup rule you define specifies which numbers
                              		  to transform based on the initial digits and the length of the number.

For example, you
                              		  can create a directory lookup rule that automatically removes the area code and
                              		  two-digit prefix digits from 10-digit phone numbers. An example of this type of
                              		  rule is to transform 4089023139 into 23139 .

## Cisco Unified
                        	 Communication Manager UDS for Mobile and Remote Access

Cisco Unified Communication Manager UDS is the contact source used
                              		  when Cisco Jabber connects using Expressway for Mobile and Remote Access. If
                              		  you deploy LDAP within the corporate firewall, we recommend that you
                              		  synchronize your LDAP directory server with Cisco Unified Communications
                              		  Manager to allow the client to connect with UDS when users are outside the
                              		  corporate firewall.

## Cloud Contact Source

### Cisco Webex Contact Source

For Cloud deployments, contact data is configured in Cisco Webex Messenger Administration Tool or by user updates. The contact information can be imported using the Cisco Webex Messenger Administration Tool. For more information see the User Management section of the Cisco Webex Messenger Administration Guide.

## Contact Photo Formats and Dimensions

To achieve the best result with Cisco Jabber, your contact photos should have specific formats and dimensions. Review supported
                              formats and optimal dimensions. Learn about adjustments the client makes to contact photos.

### Contact Photo
                           	 Formats

JPG

PNG

BMP

Cisco Jabber does not apply any modifications to
                                                				enhance rendering for contact photos in GIF format. As a result, contact photos
                                                				in GIF format might render incorrectly or with less than optimal quality. To
                                                				obtain the best quality, use PNG format for your contact photos.

### Contact Photo
                           	 Dimensions

The optimum
                                                				dimensions for contact photos are 128 pixels by 128 pixels with an aspect ratio
                                                				of 1:1.

128
                                                				pixels by 128 pixels are the maximum dimensions for local contact photos in
                                                				Microsoft Outlook.

Location

Dimensions

Audio
                                                						call window

128
                                                						pixels by 128 pixels

Incoming call windows

Meeting reminder windows

64
                                                						pixels by 64 pixels

Contact lists

Participant rosters

Call
                                                         							 history

Voicemail messages

32
                                                						pixels by 32 pixels

### Contact Photo
                           	 Adjustments

Resizing
                                                      					 contact photos can result in less than optimal resolution. For this reason, use
                                                      					 contact photos that are 128 pixels by 128 pixels so that the client does not
                                                      					 automatically resize them.

Cropping—Cisco
                                       				Jabber automatically crops nonsquare contact photos to a square aspect ratio,
                                       				or an aspect ratio of 1:1 where the width is the same as the height.

Portrait
                                       				orientation—If contact photos in your directory have portrait orientation, the
                                       				client crops 30 percent from the top and 70 percent from the bottom.

For example,
                                       				if contact photos in your directory have a width of 100 pixels and a height of
                                       				200 pixels, Cisco Jabber needs to crop 100 pixels from the height to achieve an
                                       				aspect ratio of 1:1. In this case, the client crops 30 pixels from the top of
                                       				the photos and 70 pixels from the bottom of the photos.

Landscape
                                       				orientation—If contact photos in your directory have landscape orientation, the
                                       				client crops 50 percent from each side.

For example,
                                       				if contact photos in your directory have a width of 200 pixels and a height of
                                       				100 pixels, Cisco Jabber needs to crop 100 pixels from the width to achieve an
                                       				aspect ratio of 1:1. In this case, the client crops 50 pixels from the right
                                       				side of the photos and 50 pixels from the left side of the photos.

| Note | Cisco Jabber for Windows, Cisco Jabber for Mac , Cisco Jabber for iPhone
                                                				  and iPad , and Cisco Jabber for Android support the LDAPv3 standard for directory integration. Any directory server that supports this standard should be compatible
                                             with these clients. |
|---|---|

| Restriction | Directory integration with OpenLDAP , AD LDS, or ADAM requires that you define specific parameters in a Cisco Jabber configuration file. |
|---|---|

| Note | Install Cisco Jabber for Windows on a workstation that is registered to an Active Directory domain. In this environment, you do not need to configure Cisco
                                             Jabber for Windows to connect to the directory. The client automatically discovers the directory and connects to a Global Catalog server in
                                             that domain. |
|---|---|

| Directory Server | SRV Record |
|---|---|
| Global Catalog | _gc._msdcs._tcp. domain.com |
| Domain Controller LDAP-based directory servers | _ldap._msdcs._tcp. domain.com |

| Important | Cisco Jabber does not apply any modifications to
                                                				enhance rendering for contact photos in GIF format. As a result, contact photos
                                                				in GIF format might render incorrectly or with less than optimal quality. To
                                                				obtain the best quality, use PNG format for your contact photos. |
|---|---|

| Tip | The optimum
                                                				dimensions for contact photos are 128 pixels by 128 pixels with an aspect ratio
                                                				of 1:1. 128
                                                				pixels by 128 pixels are the maximum dimensions for local contact photos in
                                                				Microsoft Outlook. |
|---|---|

| Location | Dimensions |
|---|---|
| Audio
                                                						call window | 128
                                                						pixels by 128 pixels |
| Invitations and reminders, for example: Incoming call windows Meeting reminder windows | 64
                                                						pixels by 64 pixels |
| Lists of
                                                						contacts, for example: Contact lists Participant rosters Call
                                                         							 history Voicemail messages | 32
                                                						pixels by 32 pixels |

| Tip | Resizing
                                                      					 contact photos can result in less than optimal resolution. For this reason, use
                                                      					 contact photos that are 128 pixels by 128 pixels so that the client does not
                                                      					 automatically resize them. |
|---|---|