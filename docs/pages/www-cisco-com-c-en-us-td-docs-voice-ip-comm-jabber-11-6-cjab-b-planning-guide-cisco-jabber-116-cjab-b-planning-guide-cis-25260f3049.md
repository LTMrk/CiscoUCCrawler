---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-6-cjab-b-planning-guide-cisco-jabber-116-cjab-b-planning-guide-cis-25260f3049
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_6/cjab_b_planning-guide-cisco-jabber-116/cjab_b_planning-guide-cisco-jabber-116_chapter_0100.html
retrieved_at: 2026-08-25T21:47:31.881160+00:00
---

Planning Guide for Cisco Jabber 11.6

# Planning Guide for Cisco Jabber 11.6

Updated: April 20, 2016

Chapter: User Management

## Chapter: User Management

# User Management

## Jabber IDs

Cisco Jabber uses
                              		  a Jabber ID to identify the contact information in the contact source.

The default Jabber
                              		  ID is created using the user ID and the presence domain.

For example, Adam McKenzie has a user ID of amckenzie , his domain is example.com and his Jabber ID is amckenzie@example.com .

Uppercase characters (A to Z)

Lowercase characters (a to z)

Numbers (0-9)

Period (.)

Hyphen (-)

Underscore (_)

Tilde (~)

When populating
                              		  the contact list the client will search the contact source using the Jabber IDs
                              		  to resolve the contacts and display the firstname, lastname, and any other
                              		  contact information.

## IM Address
                        	 Scheme

Cisco Jabber 10.6 and later supports multiple presence domain
                              		  architecture models for on premises deployments when the domains are on the
                              		  same presence architecture, for example users in example-us.com and
                              		  example-uk.com. Cisco Jabber supports flexible IM Address Scheme using Cisco
                              		  Unified Communications Manager IM and Presence 10.x or later. The IM Address
                              		  scheme is the Jabber ID that identifies the Cisco Jabber users.

Cisco Unified Communications IM and Presence server nodes and call
                                       				control nodes version 10.x or later.

All clients running on Windows, Mac, IOS and Android version 10.6
                                       				or later.

Cisco Jabber 10.6 or later is deployed as a new installation to
                                       				all users in your organization on all platforms (Windows, Mac, IOS and Android,
                                       				including Android based IP Phones such as the DX series).

Before making any domain or IM address changes on the presence
                                       				server, Cisco Jabber is upgraded to version 10.6 or later for all users on all
                                       				platforms (Windows, Mac, IOS and Android, including Android based IP Phones
                                       				such as the DX series).

UserID@[Default Domain]

Directory URI

### UserID@[Default Domain]

The User ID field is mapped to an LDAP field. This is the default IM
                              		  Address Scheme.

For example, user Anita Perez has an account name aperez and the User
                              		  ID field is mapped to the sAMAccountName LDAP field. The address scheme used is
                              		  aperez@example.com.

### Directory URI

The Directory URI is mapped to the mail or msRTCSIP-primaryuseraddress LDAP fields. This
                              		  option provides a scheme that is independent of the user ID for authentication.

For example, user Anita Perez has an account name aperez, the mail
                              		  field is Anita.Perez@domain.com, the address scheme used is
                              		  Anita.Perez@domain.com.

## Service Discovery
                        	 using Jabber IDs

In Cisco Jabber for Windows this is done using the SERVICES_DOMAIN command line argument.

In Cisco Jabber for Mac, Cisco Jabber for Android, or Cisco Jabber
                                       				for iPhone and iPad the service discovery domain can be set using the ServicesDomain parameter used with URL
                                       				configuration.

## SIP URI

A SIP URI is associated with each user. The SIP URI can be an email
                              		  address, an IMAddress, or a UPN.

mail

msRTCSIP-primaryuseraddress

Users can search for contacts and dial contacts by entering a SIP URI.

## LDAP User
                        	 ID

When you synchronize from your directory source to Cisco Unified
                              		  Communications Manager, the user ID is populated from an attribute in the
                              		  directory. The default attribute that holds the user ID is sAMAccountName .

## User ID Planning
                        	 for Federation

For federation, Cisco Jabber requires the contact ID or user ID for
                              		  each user to resolve contacts during contact searches.

In the jabber-config.xml file you set the attribute for the user ID in the SipUri BDISipUri parameter. The default value is msRTCSIP-PrimaryUserAddress . If there is a prefix to remove from your user ID you can set a value in the UriPrefix BDIUriPrefix parameter.

## Proxy Addresses
                        	 for User Contact Photos

Cisco Jabber accesses the photo server to retrieve contact photos. If
                              		  your network configuration contains a Web Proxy, you need to ensure that Cisco
                              		  Jabber can access the Photo Server.

## Authentication and Authorization

### Cisco Unified
                           	 Communications Manager LDAP Authentication

LDAP authentication is configured on Cisco Unified Communications
                                 		  Manager to authenticate with the directory server.

When users sign in to the client, the presence server routes that
                                 		  authentication to Cisco Unified Communications Manager. Cisco Unified
                                 		  Communications Manager then proxies that authentication to the directory
                                 		  server.

### Cisco Webex Messenger Login Authentication

Cisco Webex Messenger authentication is configured using the Cisco Webex Administration tool.

When users sign in to the client, the information is sent to the Cisco Webex Messenger and an authentication token is sent back to the client.

### Single Sign-On
                           	 Authentication

Single Sign on authentication is configured using an Identity Provider
                                 		  (IdP) and services.

When users sign in to the client, the information is sent to the IdP
                                 		  and once the credentials are accepted an authentication token is sent back to
                                 		  Cisco Jabber.

### Voicemail
                           	 Authentication

Users need to exist on Cisco Unity Connection. Cisco Unity Connection
                                 		  supports multiple authentication types. If Cisco Unified Communications Manager
                                 		  and Cisco Unity Connection use the same authentication then we recommend that
                                 		  Cisco Jabber is configured to use the same credentials.

## Multiple Resource
                        	 Login

On-Premises Deployments: Cisco Unified Communications Manager IM and Presence Service.

Cloud Deployments: Cisco Webex .

When a new IM session is initiated between two users, the first incoming message is broadcast to all of the registered clients
                                       of the receiving user.

The IM and Presence Service node waits for the first response from one of the registered clients.

The first client to respond then receives the remainder of the incoming messages until the user starts responding using another
                                       registered client.

The node then reroutes subsequent messages to this new client.

| Note | If there is no active resource when a user is logged into multiple devices, then priority is given to the client with the
                                          highest presence priority. If the presence priority is the same on all devices, then priority is given to the latest client
                                          the user logged in to. |
|---|---|