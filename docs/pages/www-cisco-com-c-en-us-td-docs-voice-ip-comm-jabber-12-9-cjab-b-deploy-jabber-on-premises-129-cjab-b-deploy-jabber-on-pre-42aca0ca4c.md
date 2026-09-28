---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-9-cjab-b-deploy-jabber-on-premises-129-cjab-b-deploy-jabber-on-pre-42aca0ca4c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_9/cjab_b_deploy-jabber-on-premises-129/cjab_b_deploy-jabber-on-premises-129_chapter_0100.html
retrieved_at: 2026-08-21T05:23:11.808987+00:00
---

On-Premises Deployment for Cisco Jabber 12.9

# On-Premises Deployment for Cisco Jabber 12.9

Updated: April 1, 2024

Chapter: Contact Source

## Chapter: Contact Source

# Contact Source

## Configure Contact Source Workflow

Step 1

Configure directory integration:

- Configure Directory Integration in a Service Profile

- Advanced Directory Integration in the Configuration File

Configure directory integration through service profiles using Cisco Unified Communications Manager or with the configuration
                                          file.

Step 2

Optional: Configure Photos

Review the options for configuring photos for users.

Step 3

Optional: Configure Intradomain Federation for CDI

Let Cisco Jabber users communicate with users who are provisioned on different systems and who are using client applications
                                          other than Cisco Jabber.

## Client
                        	 Configuration for Directory Integration

You can configure
                              		  directory integration through service profiles using Cisco Unified
                              		  Communications Manager release 9 or later or with the configuration file. Use
                              		  this section to learn how to configure the client for directory integration.

When both a
                              		  service profile and a configuration file are present, the following table
                              		  describes which parameter value takes precedence.

Service
                                          						Profile

Configuration File

Which
                                          						Parameter Value Takes Precedence?

Parameter value is set

Parameter value is set

Service
                                          						profile

Parameter value is set

Parameter value is blank

Service
                                          						profile

Parameter value is blank

Parameter value is set

Configuration file

Parameter value is blank

Parameter value is blank

Service
                                          						profile blank (default) value

### Configure Directory Integration in a Service Profile

With Cisco Unified Communications Manager release 9 and later, you can provision users with
                                 		  service profiles and deploy the _cisco-uds SRV record on your internal domain server. 
                                 		The client can
                                 		  then automatically discover Cisco Unified Communications Manager and retrieve
                                 		  the service profile to get directory integration configuration.

Step 1

Add a Directory Service

Create a Directory UC Service.

Step 2

Apply Directory Service to a Service Profile

Add the Directory UC Service to the Service Profile.

#### Add a Directory
                              	 Service

Step 1

Open the Cisco
                                                				Unified CM Administration interface.

Step 2

Select User
                                                   				  Management > User Settings > UC
                                                   				  Service .

Step 3

Select Add
                                                				New .

Step 4

Select Directory from the UC
                                                				Service Type menu and then select Next .

Step 5

Set all
                                             			 appropriate values for the directory service.

Port —3268

Protocol —TCP

Step 6

Select Save .

##### What to do next

Apply Directory
                                    		  Service.

#### Apply Directory
                              	 Service to a Service Profile

Step 1

Select User Management > User
                                                   				  Settings > Service Profile .

Step 2

Select Add New .

Step 3

Add the directory services to the directory profile. See the Directory Profile Parameters topic for information about
                                             			 the specific settings that are needed for the directory profile.

Step 4

Select Save .

##### Directory Profile
                                 	 Parameters

The following table lists the configuration parameters you can set in the directory profile:

Directory Service Configuration

Description

Primary server

Specifies the address of the primary directory server.

This parameter is required for manual connections where the client cannot automatically discover the directory server.

Secondary server

Specifies the address of the backup directory server.

Use UDS for Contact Resolution

Specifies if the client uses UDS as a contact source.

By default, UDS provides contact resolution when users connect to the corporate network through Expressway for Mobile and
                                                   Remote Access.

Use Logged On User Credential

Specifies if the client uses the logged on username and password for LDAP contact resolution.

If you have configured Active Directory (AD) SSO, this will take priority over this setting.

When you have SSO configured, Jabber uses those credentials before using the ConnectionUsername and ConnectionPassword parameters.

You must specify the logged on user credentials with the following parameters:

ConnectionUsername

ConnectionPassword

Username

Lets you manually specify a shared username that the client can use to authenticate with the directory server.

By default, Cisco Jabber desktop clients use Kerberos or client certificate authentication.

You should use this parameter only in deployments where you cannot authenticate with the directory server using either Kerberos
                                                   or client certificate authentication.

Use only a well-known or public set of credentials for an account that has read-only permissions.

Password

Lets you manually specify a shared password that the client can use to authenticate with the directory server.

By default, Cisco Jabber desktop clients use Kerberos or client certificate authentication.

You should use this parameter only in deployments where you cannot authenticate with the directory server using either Kerberos
                                                   or client certificate authentication.

Use only a well-known or public set of credentials for an account that has read-only permissions.

Search Base 1

Search Base 2

Search Base 3

Search Base 4

Search Base 5

Specifies a location in the directory server from which searches begin. In other words, a search base is the root from which
                                                   the client executes a search.

By default, the client searches from the root of the directory tree. You can specify the value of up to three search bases
                                                   in your OU to override the default behavior.

Active Directory does not typically require a search base. Specify search bases for Active Directory only for specific performance
                                                   requirements.

Specify a search base for directory servers other than Active Directory to create bindings to specific locations in the directory.

Tip

Specify an OU to restrict searches to certain user groups.

For example, a subset of your users have instant messaging capabilities only. Include those users in an OU and then specify
                                                               that as a search base.

Recursive Search on All Search Bases

Select this option to perform a recursive search of the directory starting at the search base. Use recursive searches to allow
                                                   the Cisco Jabber client contact search queries to search all of the LDAP directory tree from a given search context (search
                                                   base). This is a common option when searching LDAP.

This is a required field.

The default value is True.

Search Timeout

Specifies the timeout period for directory queries in seconds.

The default value is 5.

Base Filter

Specifies a base filter for Active Directory queries.

Specify a directory subkey name only to retrieve objects other than user objects when you query the directory.

The default value is (&(&(objectCategory=person)( objectClass=user) .

Predictive Search Filter

Defines filters to apply to predictive search queries.

You can define multiple, comma-separated values to filter search queries.

The default value is ANR .

When Cisco Jabber performs a predictive search, it issues a query using Ambiguous Name Resolution (ANR). This query disambiguates
                                                   the search string and returns results that match the attributes that are set for ANR on your directory server.

Important

Configure your directory server to set attributes for ANR if you want the client to search for those attributes.

###### Attribute
                                       		  Mappings

It is not
                                       		  possible to change the default attribute mappings in a service profile. If you
                                       		  plan to change any default attribute mappings, you must define the required
                                       		  mappings in a client configuration file.

### Configure
                           	 Photos

Cisco Jabber uses the following methods to configure Photos for users:

Active Directory Binary Objects —No configuration needed, Cisco Jabber retrieves the binary photo from the thumbnailPhoto attribute.

PhotoURL attribute —Use the PhotoSource parameter in the jabber-config.xml file to specify an attribute in your directory. The client will retrieve the attribute
                                       and determine if it is a URL or binary data and display the photo from either source.

CDI parameter: PhotoSource

Example:

```
<Directory>
 <PhotoSource>url</PhotoSource> 
</Directory>
```

URI Substitution —For your directory server type, use the following parameters in the jabber-config.xml file:

CDI parameters:

PhotoUriSubstitutionEnabled

PhotoUriWithToken

PhotoUriSubstitutionToken

Example:

```
<PhotoUriSubstitutionEnabled>True</PhotoUriSubstitutionEnabled> 
<PhotoUriSubstitutionToken>sAMAccountName</PhotoUriSubstitutionToken> 
<PhotoUriWithToken>http://example.com/photo/sAMAccountName.jpg</PhotoUriWithToken>
```

UDS parameters:

UdsPhotoUriWithToken

Example:

```
<UDSPhotoUriWithToken>http://example.com/photo/sAMAccountName.jpg</UDSPhotoUriWithToken>
```

### Advanced Directory
                           	 Integration in the Configuration File

You can configure
                                 		  directory integration in the Cisco Jabber configuration file. For more
                                 		  information see the Directory chapter in the Parameters Reference Guide for Cisco Jabber .

Important

## Federation

Federation lets Cisco Jabber users communicate with users who are provisioned on different systems and who are using client
                           applications other than Cisco Jabber.

### Configure Intradomain Federation for CDI

In addition to configuring intradomain federation on the presence server, you might need to specify some configuration settings
                                 in the Cisco Jabber configuration files.

To resolve contacts during contact search or retrieve contact information from your directory, Cisco Jabber requires the contact
                                 ID for each user. Cisco Unified Communications Manager IM & Presence server uses a specific format for resolving contact information
                                 that does not always match the format on other presence servers such as Microsoft Office Communications Server or Microsoft
                                 Live Communications Server.

Step 1

Set the value of the UseSIPURIToResolveContacts parameter to true :

Step 2

Specify an attribute that contains the Cisco Jabber contact ID that the client uses to retrieve contact information. The default
                                          value is msRTCSIP-PrimaryUserAddress , or you can specify another attribute in the SipUri parameter.

sAMAccountName@domain

UserPrincipleName (UPN)@domain

EmailAddress@domain

employeeNumber@domain

phoneNumber@domain

Step 3

In the UriPrefix parameter, specify any prefix text that precedes each contact ID in the SipUri parameter.

#### Example:

#### Example

```
<Directory>
  <UseSIPURIToResolveContacts>true</UseSIPURIToResolveContacts>
  <SipUri> non-default-attribute </SipUri>
  <UriPrefix>sip:</UriPrefix>
</Directory>
```

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure directory integration: Configure Directory Integration in a Service Profile Advanced Directory Integration in the Configuration File | Configure directory integration through service profiles using Cisco Unified Communications Manager or with the configuration
                                          file. |
| Step 2 | Optional: Configure Photos | Review the options for configuring photos for users. |
| Step 3 | Optional: Configure Intradomain Federation for CDI | Let Cisco Jabber users communicate with users who are provisioned on different systems and who are using client applications
                                          other than Cisco Jabber. |

| Service
                                          						Profile | Configuration File | Which
                                          						Parameter Value Takes Precedence? |
|---|---|---|
| Parameter value is set | Parameter value is set | Service
                                          						profile |
| Parameter value is set | Parameter value is blank | Service
                                          						profile |
| Parameter value is blank | Parameter value is set | Configuration file |
| Parameter value is blank | Parameter value is blank | Service
                                          						profile blank (default) value |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add a Directory Service | Create a Directory UC Service. |
| Step 2 | Apply Directory Service to a Service Profile | Add the Directory UC Service to the Service Profile. |

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
| Step 4 | Select Directory from the UC
                                                				Service Type menu and then select Next . |
| Step 5 | Set all
                                             			 appropriate values for the directory service. To configure Cisco Jabber directory searches on the Global Catalog, add the following values: Port —3268 Protocol —TCP |
| Step 6 | Select Save . |

| Step 1 | Select User Management > User
                                                   				  Settings > Service Profile . The Find and List Service Profiles window opens. |
|---|---|
| Step 2 | Select Add New . The Service Profile Configuration window opens. |
| Step 3 | Add the directory services to the directory profile. See the Directory Profile Parameters topic for information about
                                             			 the specific settings that are needed for the directory profile. |
| Step 4 | Select Save . |

| Directory Service Configuration | Description |
|---|---|
| Primary server | Specifies the address of the primary directory server. This parameter is required for manual connections where the client cannot automatically discover the directory server. |
| Secondary server | Specifies the address of the backup directory server. |
| Use UDS for Contact Resolution | Specifies if the client uses UDS as a contact source. True (Default) Use UDS as a contact source. When this option is selected the following parameters in this table are not used. False Use CDI as a contact source. The following parameters are used to connect to the LDAP server. By default, UDS provides contact resolution when users connect to the corporate network through Expressway for Mobile and
                                                   Remote Access. |
| Use Logged On User Credential | Specifies if the client uses the logged on username and password for LDAP contact resolution. If you have configured Active Directory (AD) SSO, this will take priority over this setting. True (default) Use logged on user credentials. This is the same as specifying CUCM as the value for the LDAP_UseCredentialsFrom parameter. False Do not use logged on user credentials. When you have SSO configured, Jabber uses those credentials before using the ConnectionUsername and ConnectionPassword parameters. You must specify the logged on user credentials with the following parameters: ConnectionUsername ConnectionPassword |
| Username | Lets you manually specify a shared username that the client can use to authenticate with the directory server. By default, Cisco Jabber desktop clients use Kerberos or client certificate authentication. You should use this parameter only in deployments where you cannot authenticate with the directory server using either Kerberos
                                                   or client certificate authentication. Use only a well-known or public set of credentials for an account that has read-only permissions. |
| Password | Lets you manually specify a shared password that the client can use to authenticate with the directory server. By default, Cisco Jabber desktop clients use Kerberos or client certificate authentication. You should use this parameter only in deployments where you cannot authenticate with the directory server using either Kerberos
                                                   or client certificate authentication. Use only a well-known or public set of credentials for an account that has read-only permissions. |
| Search Base 1 Search Base 2 Search Base 3 Search Base 4 Search Base 5 | Specifies a location in the directory server from which searches begin. In other words, a search base is the root from which
                                                   the client executes a search. By default, the client searches from the root of the directory tree. You can specify the value of up to three search bases
                                                   in your OU to override the default behavior. Active Directory does not typically require a search base. Specify search bases for Active Directory only for specific performance
                                                   requirements. Specify a search base for directory servers other than Active Directory to create bindings to specific locations in the directory. Tip Specify an OU to restrict searches to certain user groups. For example, a subset of your users have instant messaging capabilities only. Include those users in an OU and then specify
                                                               that as a search base. | Tip | Specify an OU to restrict searches to certain user groups. For example, a subset of your users have instant messaging capabilities only. Include those users in an OU and then specify
                                                               that as a search base. |
| Tip | Specify an OU to restrict searches to certain user groups. For example, a subset of your users have instant messaging capabilities only. Include those users in an OU and then specify
                                                               that as a search base. |
| Recursive Search on All Search Bases | Select this option to perform a recursive search of the directory starting at the search base. Use recursive searches to allow
                                                   the Cisco Jabber client contact search queries to search all of the LDAP directory tree from a given search context (search
                                                   base). This is a common option when searching LDAP. This is a required field. The default value is True. |
| Search Timeout | Specifies the timeout period for directory queries in seconds. The default value is 5. |
| Base Filter | Specifies a base filter for Active Directory queries. Specify a directory subkey name only to retrieve objects other than user objects when you query the directory. The default value is (&(&(objectCategory=person)( objectClass=user) . |
| Predictive Search Filter | Defines filters to apply to predictive search queries. You can define multiple, comma-separated values to filter search queries. The default value is ANR . When Cisco Jabber performs a predictive search, it issues a query using Ambiguous Name Resolution (ANR). This query disambiguates
                                                   the search string and returns results that match the attributes that are set for ANR on your directory server. Important Configure your directory server to set attributes for ANR if you want the client to search for those attributes. | Important | Configure your directory server to set attributes for ANR if you want the client to search for those attributes. |
| Important | Configure your directory server to set attributes for ANR if you want the client to search for those attributes. |

| Tip | Specify an OU to restrict searches to certain user groups. For example, a subset of your users have instant messaging capabilities only. Include those users in an OU and then specify
                                                               that as a search base. |
|---|---|

| Important | Configure your directory server to set attributes for ANR if you want the client to search for those attributes. |
|---|---|

| Important | When a Service Profile and a configuration file are present,
                                             			 settings in the Service Profile always take priority. |
|---|---|

| Step 1 | Set the value of the UseSIPURIToResolveContacts parameter to true : |
|---|---|
| Step 2 | Specify an attribute that contains the Cisco Jabber contact ID that the client uses to retrieve contact information. The default
                                          value is msRTCSIP-PrimaryUserAddress , or you can specify another attribute in the SipUri parameter. Note When you deploy intradomain federation and the client connects with Expressway for Mobile and Remote Access from outside the
                                                         firewall, contact search is supported only when the contact ID uses one of the following formats: sAMAccountName@domain UserPrincipleName (UPN)@domain EmailAddress@domain employeeNumber@domain phoneNumber@domain | Note | When you deploy intradomain federation and the client connects with Expressway for Mobile and Remote Access from outside the
                                                         firewall, contact search is supported only when the contact ID uses one of the following formats: sAMAccountName@domain UserPrincipleName (UPN)@domain EmailAddress@domain employeeNumber@domain phoneNumber@domain |
| Note | When you deploy intradomain federation and the client connects with Expressway for Mobile and Remote Access from outside the
                                                         firewall, contact search is supported only when the contact ID uses one of the following formats: sAMAccountName@domain UserPrincipleName (UPN)@domain EmailAddress@domain employeeNumber@domain phoneNumber@domain |
| Step 3 | In the UriPrefix parameter, specify any prefix text that precedes each contact ID in the SipUri parameter. Example: For example, you specify msRTCSIP-PrimaryUserAddress as the value of SipUri . In your directory the value of msRTCSIP-PrimaryUserAddress for each user has the following format: sip: username@domain . |

| Note | When you deploy intradomain federation and the client connects with Expressway for Mobile and Remote Access from outside the
                                                         firewall, contact search is supported only when the contact ID uses one of the following formats: sAMAccountName@domain UserPrincipleName (UPN)@domain EmailAddress@domain employeeNumber@domain phoneNumber@domain |
|---|---|