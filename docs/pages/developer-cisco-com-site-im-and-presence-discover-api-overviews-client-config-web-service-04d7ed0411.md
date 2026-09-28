---
doc_id: developer-cisco-com-site-im-and-presence-discover-api-overviews-client-config-web-service-04d7ed0411
source_url: https://developer.cisco.com/site/im-and-presence/discover/api_overviews/client_config_web_service/
retrieved_at: 2026-09-01T17:45:47.418010+00:00
---

# About the Client Configuration Web Service

The Client Configuration Web Service is an interface that allows client applications to manage user preference information on Cisco Unified Presence. The Client Configuration Web Service provisions information such as contacts, contact groups, presence rules, access control lists, and calendaring options on Cisco Unified Presence.

The Client Configuration Web Service is a Simple Object Access Protocol (SOAP) interface. The request and response messages are sent in the form of XML. A client application sends a SOAP request; the web service processes the request and sends a SOAP response.

To improve backward compatibility, versions of the Client Configuration Web Service are numbered in accordance with Cisco Unified Presence releases. Each version of the Client Configuration Web Service is accessed by appending a version number to the following URI:

- https://server_name/EPASSoap/service/< version URI >

Cisco Unified Presence accepts SOAP requests both on the interface version specified in the URI, and on the previous version of the interface. For example, Cisco Unified Presence version 8.0 will accept SOAP requests from the following URIs:

- https://server_name/EPASSoap/service/v80

- https://server_name/EPASSoap/service/v70

The login response contains information on the Client Configuration Web Service versions available on the Cisco Unified Presence server. The login method is always available on the nonversioned URI:

- https://server_name/EPASSoap/service

Following a successful login response, the client selects which version of the Client Configuration Web Service they wish to use for subsequent methods.

The Client Configuration Web Service is available over HTTPS on port 8443.

To access a description of the latest Cisco Unified Presence SOAP schema, enter the following URL at a computer that has access to your Cisco Unified Presence server:

- http://server_name/EPASSoap/service?wsdl

## Overview of Functions

A client application uses the Client Configuration Web Service to perform the following functions:

- Log in and out of Cisco Unified Presence

- Get SASL Cisco-VTG-Token

- Get system configuration information

- Get and set user configurations

- Contact list management

- Get a list of federated domains

- Download dialing rules

- Get licensing features

- Get, add and delete the Access Control Lists (ACL)

- Get and set calendaring options

- Get and set phone presence option

- User public data search

- Get Cluster Information

## Login and Authentication

To log in to the Client Configuration Web Service, a client application sends a username and password in the login request for authentication. Cisco Unified Presence creates a session key, an opaque string, if the user credentials are verified. The client includes the session key in the SOAP header portion of subsequent SOAP requests to the Client Configuration Web Service, including logout requests.

The Client Configuration Web Service supports the following login scenarios:

- The client application sends a username and password for an end user in the login request for authentication, and Cisco Unified Presence returns a unique session key for the end user.

- The client application logs in to Cisco Unified Presence as an "application user" using an application username and password. The client application can then log in an end user by passing the session key for an application user, and the username for an end user in the login request; a unique session key for the end user is returned.

If an application user is disconnected, any associated end users are automatically logged out.

The Client Configuration Web Service supports multiple logins for the same user from different client applications. Cisco Unified Presence stores a separate session key per login to each client application for a user.

## Contact Management

Using the Client Configuration Web Service, users can manage their non-presence contacts. In addition, users can also add and modify the auxiliary information associated with a contact such as home number, work number, mobile number, email and so on.

The following contact management functionality is supported:

- Add a contact

- Modify a contact

- Delete a contact

- Get auxiliary information for a contact

- Modify auxiliary information for a contact

## Federated Domain Support

The Client Configuration Web Service allows users of the client application to interact with users in permitted foreign domains (known as federated domains). Since the Client Configuration Web Service supports contacts from federated domains, not all contacts in the user contact list will be Cisco Unified Presence users.

The client application uses the get-federated-domains request to obtain a list of foreign domains (configured on Cisco Unified Presence) to which federation is permitted or blocked. This list informs the user which foreign domains, and foreign contacts, they can successfully interact with.

The client application can authorize or deny foreign watchers using the Access Control Lists (ACL). When a user approves or denies a foreign watcher, the client application uses the add-acl request to add the user to the ACL with a policy of allowed or denied, and sends the updated ACL to Cisco Unified Presence.

# More Information on Client Configuration Web Service

For more information on the Cisco Unified Presence Client Configuration Web Service, including protocol messaging flows and protocol syntax examples, please refer to the "Developer Guide for Cisco Unified Presence" for the particular version of Cisco Unified Presence which you have deployed.

Download Developer Guide