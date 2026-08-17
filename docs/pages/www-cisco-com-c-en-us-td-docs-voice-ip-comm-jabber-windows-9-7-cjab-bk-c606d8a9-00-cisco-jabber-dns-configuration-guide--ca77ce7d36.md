---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-windows-9-7-cjab-bk-c606d8a9-00-cisco-jabber-dns-configuration-guide--ca77ce7d36
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/Windows/9_7/CJAB_BK_C606D8A9_00_cisco-jabber-dns-configuration-guide/CJAB_BK_C606D8A9_00_cisco-jabber-dns-configuration-guide_chapter_00.html
retrieved_at: 2026-08-17T03:31:51.380161+00:00
---

Cisco Jabber DNS Configuration Guide

# Cisco Jabber DNS Configuration Guide

Updated: September 28, 2017

Chapter: How the Client Uses Domain Name Servers

## Chapter: How the Client Uses Domain Name Servers

Contents

# How the Client Uses Domain Name Servers

- Automatically discover on-premises servers inside the corporate network.

- Locate access points for Expressway Mobile and Remote Access on the public Internet.

- Determine whether the client is inside or outside the corporate network.

- How the Client Finds a Name Server

- How the Client Gets a Services Domain

- How the Client Discovers Available Services

## How the Client Finds a Name Server

- Internal name servers inside the corporate network.

- External name servers on the public Internet.

When the client’s host computer or device gets a network connection, the host computer or device also gets the address of a DNS name server from the DHCP settings. Depending on the network connection, that name server might be internal or external to the corporate network.

Cisco Jabber queries the name server that the host computer or device gets from the DHCP settings.

## How the Client Gets a Services Domain

The services domain is discovered by the Cisco Jabber client in different ways.

- User enters an address in the format username@example.com in the client user interface.

- Cisco Jabber for Android version 9.6 or later

- Cisco Jabber for Mac version 9.6 or later

- Cisco Jabber for iPhone
				  and iPad version 9.6.1 or later

- Cisco Jabber for
				  Windows version 9.6 or later

- The client uses the cached configuration.

- User manually enters an address in the client user interface.

- The client uses the VoiceServicesDomain parameter in the configuration file. This option is available in clients that support the jabber-config.xml file.

- Cisco Jabber for Android version 9.6 or later

- Cisco Jabber for Mac version 9.6 or later

- Cisco Jabber for iPhone
				  and iPad version 9.6.1 or later

- Cisco Jabber for
				  Windows version 9.6 or later

See the  appropriate version of the Installation and Configuration guide , for more detailed information.

After Cisco Jabber gets the services domain, it queries the name server that is configured to the client computer or device.

## How the Client Discovers Available Services

- Checks if the network is inside or outside the firewall and if Expressway Mobile and Remote Access is deployed. A query is sent to  the name server to get DNS Service (SRV) records.

- Starts monitoring for network changes.
When Expressway Mobile and Remote Access is deployed, the client monitors the network to ensure that it can reconnect if the network changes from inside or outside the firewall.

- Issues an HTTP query to a CAS URL for the Cisco WebEx Messenger service.
This query enables the client to determine if the domain is a valid Cisco
				  WebEx domain.

- Determine which services are available.

- Determine if it can connect to the corporate network through Expressway Mobile and Remote Access .

### Client Issues HTTP Query

In addition to querying the name server for SRV records to locate available services, Cisco Jabber sends an HTTP query to the CAS URL for the Cisco WebEx Messenger service. This request enables the client to determine cloud-based deployments and authenticate users to the Cisco WebEx Messenger service.

When the client gets a services domain from the user, it appends that domain to the following HTTP query:

```
http://loginp.webexconnect.com/cas/FederatedSSO?org=
```

For example, if the client gets example.com as the services domain from the user, it issues the following query:

```
http://loginp.webexconnect.com/cas/FederatedSSO?org=example.com
```

That query returns an XML response that the client uses to determine if the services domain is a valid Cisco
				  WebEx domain.

If the client determines the services domain is a valid Cisco
				  WebEx domain, it prompts users to enter their Cisco
				  WebEx credentials. The client then authenticates to the Cisco WebEx Messenger service and retrieves the configuration and UC services configured in Cisco
				  WebEx Org Admin.

If the client determines the services domain is not a valid Cisco
				  WebEx domain, it uses the results of the query to the name server to locate available services.

When the client sends the HTTP request to the CAS URL, it uses any configured system proxies. The following	limitations apply when using a proxy for these
HTTP requests:

- Proxy
Authentication is not supported.

- Wildcards
in the bypass list are not supported. Use example.com instead of *.example.com for example.

### Client Queries Name Server

When the client queries a name server, it sends separate, simultaneous requests to the name server for SRV records.

- _cisco-uds

- _cuplogin

- _collab-edge

The client prompts users to manually enter setup and sign-in details.

### Client Connects to Internal Services

When connecting to internal services, the goals are to determine the authenticator, sign users in, and connect to available services.

Cloud-based or hybrid cloud-based deployments.

On-premises deployments in the default product mode. The default product mode can be either full UC or IM only.

On-premises deployments in phone mode.

- Determines that the Cisco WebEx Messenger service is the primary source of authentication.

- Automatically connects to the Cisco WebEx Messenger service.

- Prompts the user for credentials.

- Retrieves client and service configuration.

- Prompts the user for credentials to authenticate with Cisco Unified
				  Communications Manager .

In an environment with multiple Cisco Unified
				  Communications Manager clusters, you must configure the Intercluster Lookup Service (ILS). ILS enables the client to find the user's home cluster.

See the appropriate version of the Cisco Unified
				  Communications Manager Features and Services Guide to learn how to configure ILS.

Cisco Unified Presence or Cisco Unified Communications Manager IM and Presence is the authenticator.

The Cisco WebEx Messenger service is the authenticator.

As of this release, the client issues an HTTP query in addition to the query for SRV records. The HTTP query allows the client to determine if it should authenticate to the Cisco WebEx Messenger service.

As a result of the HTTP query, the client connects to the Cisco WebEx Messenger service in cloud-based deployments. Setting the value of the Product type field to WebEx may have no practical effect if the client already discovered the  WebEx service using a CAS lookup.

If the service profile does not contain an IM and presence service configuration, the authenticator is Cisco Unified
				  Communications Manager .

- Sign in to the authenticator.
After the client signs in, it can determine the product mode.

- Determines that Cisco Unified Presence is the primary source of authentication.

- Automatically connects to the server.

- Prompts the user for credentials.

- Retrieves client and service configuration.

### Client Connects through Expressway Mobile and Remote Access

If the name server returns the _collab-edge SRV record, then the client attempts to connect to internal servers through Expressway Mobile and Remote Access .

The Cisco VCS Control or Cisco Expressway-C server looks up the internal SRV records and provides the records to the Cisco VCS Expressway or Cisco Expressway-E server.

After the client gets the internal SRV records, which must include _cisco-uds , it retrieves service profiles from Cisco Unified
				  Communications Manager . The service profiles then provide the client with the user's home cluster, the primary source of authentication, and configuration.

# How the Client Uses Domain Name Servers

- Automatically discover on-premises servers inside the corporate network.

- Locate access points for Expressway Mobile and Remote Access on the public Internet.

- Determine whether the client is inside or outside the corporate network.

- How the Client Finds a Name Server

- How the Client Gets a Services Domain

- How the Client Discovers Available Services

## How the Client Finds a Name Server

- Internal name servers inside the corporate network.

- External name servers on the public Internet.

When the client’s host computer or device gets a network connection, the host computer or device also gets the address of a DNS name server from the DHCP settings. Depending on the network connection, that name server might be internal or external to the corporate network.

Cisco Jabber queries the name server that the host computer or device gets from the DHCP settings.

## How the Client Gets a Services Domain

The services domain is discovered by the Cisco Jabber client in different ways.

- User enters an address in the format username@example.com in the client user interface.

- Cisco Jabber for Android version 9.6 or later

- Cisco Jabber for Mac version 9.6 or later

- Cisco Jabber for iPhone
				  and iPad version 9.6.1 or later

- Cisco Jabber for
				  Windows version 9.6 or later

- The client uses the cached configuration.

- User manually enters an address in the client user interface.

- The client uses the VoiceServicesDomain parameter in the configuration file. This option is available in clients that support the jabber-config.xml file.

- Cisco Jabber for Android version 9.6 or later

- Cisco Jabber for Mac version 9.6 or later

- Cisco Jabber for iPhone
				  and iPad version 9.6.1 or later

- Cisco Jabber for
				  Windows version 9.6 or later

See the  appropriate version of the Installation and Configuration guide , for more detailed information.

After Cisco Jabber gets the services domain, it queries the name server that is configured to the client computer or device.

## How the Client Discovers Available Services

- Checks if the network is inside or outside the firewall and if Expressway Mobile and Remote Access is deployed. A query is sent to  the name server to get DNS Service (SRV) records.

- Starts monitoring for network changes.
When Expressway Mobile and Remote Access is deployed, the client monitors the network to ensure that it can reconnect if the network changes from inside or outside the firewall.

- Issues an HTTP query to a CAS URL for the Cisco WebEx Messenger service.
This query enables the client to determine if the domain is a valid Cisco
				  WebEx domain.

- Determine which services are available.

- Determine if it can connect to the corporate network through Expressway Mobile and Remote Access .

### Client Issues HTTP Query

In addition to querying the name server for SRV records to locate available services, Cisco Jabber sends an HTTP query to the CAS URL for the Cisco WebEx Messenger service. This request enables the client to determine cloud-based deployments and authenticate users to the Cisco WebEx Messenger service.

When the client gets a services domain from the user, it appends that domain to the following HTTP query:

```
http://loginp.webexconnect.com/cas/FederatedSSO?org=
```

For example, if the client gets example.com as the services domain from the user, it issues the following query:

```
http://loginp.webexconnect.com/cas/FederatedSSO?org=example.com
```

That query returns an XML response that the client uses to determine if the services domain is a valid Cisco
				  WebEx domain.

If the client determines the services domain is a valid Cisco
				  WebEx domain, it prompts users to enter their Cisco
				  WebEx credentials. The client then authenticates to the Cisco WebEx Messenger service and retrieves the configuration and UC services configured in Cisco
				  WebEx Org Admin.

If the client determines the services domain is not a valid Cisco
				  WebEx domain, it uses the results of the query to the name server to locate available services.

When the client sends the HTTP request to the CAS URL, it uses any configured system proxies. The following	limitations apply when using a proxy for these
HTTP requests:

- Proxy
Authentication is not supported.

- Wildcards
in the bypass list are not supported. Use example.com instead of *.example.com for example.

### Client Queries Name Server

When the client queries a name server, it sends separate, simultaneous requests to the name server for SRV records.

- _cisco-uds

- _cuplogin

- _collab-edge

The client prompts users to manually enter setup and sign-in details.

### Client Connects to Internal Services

When connecting to internal services, the goals are to determine the authenticator, sign users in, and connect to available services.

Cloud-based or hybrid cloud-based deployments.

On-premises deployments in the default product mode. The default product mode can be either full UC or IM only.

On-premises deployments in phone mode.

- Determines that the Cisco WebEx Messenger service is the primary source of authentication.

- Automatically connects to the Cisco WebEx Messenger service.

- Prompts the user for credentials.

- Retrieves client and service configuration.

- Prompts the user for credentials to authenticate with Cisco Unified
				  Communications Manager .

In an environment with multiple Cisco Unified
				  Communications Manager clusters, you must configure the Intercluster Lookup Service (ILS). ILS enables the client to find the user's home cluster.

See the appropriate version of the Cisco Unified
				  Communications Manager Features and Services Guide to learn how to configure ILS.

Cisco Unified Presence or Cisco Unified Communications Manager IM and Presence is the authenticator.

The Cisco WebEx Messenger service is the authenticator.

As of this release, the client issues an HTTP query in addition to the query for SRV records. The HTTP query allows the client to determine if it should authenticate to the Cisco WebEx Messenger service.

As a result of the HTTP query, the client connects to the Cisco WebEx Messenger service in cloud-based deployments. Setting the value of the Product type field to WebEx may have no practical effect if the client already discovered the  WebEx service using a CAS lookup.

If the service profile does not contain an IM and presence service configuration, the authenticator is Cisco Unified
				  Communications Manager .

- Sign in to the authenticator.
After the client signs in, it can determine the product mode.

- Determines that Cisco Unified Presence is the primary source of authentication.

- Automatically connects to the server.

- Prompts the user for credentials.

- Retrieves client and service configuration.

### Client Connects through Expressway Mobile and Remote Access

If the name server returns the _collab-edge SRV record, then the client attempts to connect to internal servers through Expressway Mobile and Remote Access .

The Cisco VCS Control or Cisco Expressway-C server looks up the internal SRV records and provides the records to the Cisco VCS Expressway or Cisco Expressway-E server.

After the client gets the internal SRV records, which must include _cisco-uds , it retrieves service profiles from Cisco Unified
				  Communications Manager . The service profiles then provide the client with the user's home cluster, the primary source of authentication, and configuration.

### Customers Also Viewed

- Cisco Jabber DNS Configuration Guide --- Service (SRV) Records

| Note | Refer to the latest version of your Cisco Jabber client Installation and Configuration Guide for further information on configuring available services. |
|---|---|

| Note | When the client sends the HTTP request to the CAS URL, it uses any configured system proxies. The following	limitations apply when using a proxy for these
HTTP requests: Proxy
Authentication is not supported. Wildcards
in the bypass list are not supported. Use example.com instead of *.example.com for example. |
|---|---|

| Note | As of this release, the client issues an HTTP query in addition to the query for SRV records. The HTTP query allows the client to determine if it should authenticate to the Cisco WebEx Messenger service. As a result of the HTTP query, the client connects to the Cisco WebEx Messenger service in cloud-based deployments. Setting the value of the Product type field to WebEx may have no practical effect if the client already discovered the  WebEx service using a CAS lookup. |
|---|---|

| Note | The Cisco VCS Control or Cisco Expressway-C server looks up the internal SRV records and provides the records to the Cisco VCS Expressway or Cisco Expressway-E server. |
|---|---|

| Note | Refer to the latest version of your Cisco Jabber client Installation and Configuration Guide for further information on configuring available services. |
|---|---|

| Note | When the client sends the HTTP request to the CAS URL, it uses any configured system proxies. The following	limitations apply when using a proxy for these
HTTP requests: Proxy
Authentication is not supported. Wildcards
in the bypass list are not supported. Use example.com instead of *.example.com for example. |
|---|---|

| Note | As of this release, the client issues an HTTP query in addition to the query for SRV records. The HTTP query allows the client to determine if it should authenticate to the Cisco WebEx Messenger service. As a result of the HTTP query, the client connects to the Cisco WebEx Messenger service in cloud-based deployments. Setting the value of the Product type field to WebEx may have no practical effect if the client already discovered the  WebEx service using a CAS lookup. |
|---|---|

| Note | The Cisco VCS Control or Cisco Expressway-C server looks up the internal SRV records and provides the records to the Cisco VCS Expressway or Cisco Expressway-E server. |
|---|---|