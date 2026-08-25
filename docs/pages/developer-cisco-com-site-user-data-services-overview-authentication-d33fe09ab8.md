---
doc_id: developer-cisco-com-site-user-data-services-overview-authentication-d33fe09ab8
source_url: https://developer.cisco.com/site/user-data-services/overview/authentication/
retrieved_at: 2026-08-25T21:03:04.164369+00:00
---

# Authentication

As of Unified CM 10.5, UDS supports both Cisco Unified CM Single Sign On (SSO) authentication and original Basic Authentication options.  Depending on your infrastructure and environment configuration, you may be able to take advantage of one or both alternatives.

### What is SSO (Single Sign-On)?

Single Sign On (SSO) simplifies the login process for Users and Administrators in Cisco Unified Communications Products (Unified CM and Unity Connection releases 10.5).

SSO offers an easier, more consistent way for users and administrators to authenticate access to secured resources.

Instead of each product requiring a separate user name and password login, a single returned credential allows access to all enabled product interfaces.

Think of SSO as supplying the "skeleton key" to every enabled, authorized service and interface in your environment.

For an example and details on obtaining a UC Manager SSO token with a web application, click here

For an example and details on using a UC Manager SSO token with UDS, click here .

## Basic Authentication

Overview

The Cisco UDS limits access to its services through HTTP Basic Access Authentication. It is a transaction scheme described in RFC 2617 . This neatly aligns with the resource-based REST transactions that UDS uses to provide services.

The advantage to HTTP Basic Access Authentication is that it's simple to implement. It uses only standard HTTP headers and, when using a Web browser, the browser implements and manages the login dialog.

Using Basic Authentication

HTTP Basic Access Authentication requires authorization credentials in the form of a user name and password before granting access to a specific URL. The client application can obtain the user name and password through a challenge dialog, or it can use previously stored values. The user name and password are passed as Base64 encoded text in the header of a subsequent HTTP transaction.

Many, but not all, UDS API requests require authentication for access. Use an end user account created by the CUCM administrator to make API calls that require authentication.

UDS resources that require authentication

- credentials

- device(s)

- extenstion(s)

- remoteDestination(s)

- speedDial(s)

- subscribedService(s)

- user

- userPolicy

UDS resources that do not require authentication

- clusterUser

- installedLocales

- models

- options

- phoneService(s)

- servers

- timezones

- users

- version

Security

Cisco requires that all UDS transactions be conducted over a secure session, such as HTTPS or SSL. Any non-HTTPS requests will be redirected to the HTTPS port.

Depending on the connection technology used, you may need to manually install the Unified Communication Manager's self-signed certificate into a local trust store for your application.

## Authentication Best Practices

The client application must maintain the session by supplying a session cookie that the server sends when it makes subsequent requests. If the client fails to do so, it may receive HTTP 503 "Service Unavailable" response to some of its requests.

Client sessions authenticating with UDS are given the following cookies:

- JSESSIONID for their UDS sessions

- JSESSIONIDSSO for their single sign-on sessions

The SSO cookie can be used for communications with the node that returned the cookie.

A developer should configure the client to properly handle sessions. In most HTTP libraries, this is simple and usually involves only a few lines of code. Example code for popular libraries is provided in Configure HTTP Sessions .

## Configure HTTP Sessions

How to configure your HTTP library for proper session management

Learn More

## FAQ's

Visit our FAQ page to get answers to the most common questions

FAQ'''s

| credentials device(s) extenstion(s) remoteDestination(s) | speedDial(s) subscribedService(s) user userPolicy |
|---|---|

| clusterUser installedLocales models options phoneService(s) | servers timezones users version |
|---|---|