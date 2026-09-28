---
doc_id: developer-cisco-com-docs-finesse-single-sign-on-4b78e4494c
source_url: https://developer.cisco.com/docs/finesse/single-sign-on/
retrieved_at: 2026-09-07T14:06:43.844001+00:00
---

# Single Sign-On

Single Sign-On (SSO) is a mechanism to authenticate users across software systems using a common LDAP identity and this common authentication service provides a token. Multiple applications use this token to authenticate the user across preconfigured applications.

The Single Sign-On (SSO) APIs are used in the Finesse desktop for token related operations and are ready to use in an out of the box Finesse deployment. Third-party desktop applications have to use these APIs independently for SSO token related operations.

## Single Sign-On Components

The following are the SSO components:

IdP is an application that creates, maintains, and manages identity information for users.

IdP offers the user authentication as a service. Third-party applications (for example, web applications) outsource the user authentication mechanism to a trusted IdP which is configured within the Organization. For example, Active Directory Windows Server.

Cisco IdS is the common API endpoint for relaying requests to the IdP by generating the authentication token and validating it.

Cisco IdS implements an authorization endpoint and token endpoint as part of its OAuth (Open Authorization) server implementation.

## Token Types

The following are the token types:

Access Token—It accesses protected resources. Clients are issued an access token that contains identity information for the user that is encrypted by default.

For an SSO enabled user, use the access token in the authorization header of the Finesse REST APIs.

Authorization: Bearer < access token >

Refresh Token—It obtains a new access token before the current access token expires. The IdS generates the refresh token.

The refresh and access token are generated as a pair of tokens. When refreshing the access token, the pair of tokens provide an extra layer of security.

You can configure the expiry time of the refresh token and access token in the IdS administration. When the refresh token expires, you cannot refresh the access token.

## Cisco Contact Center Components

The following are the Cisco Contact Center components that support SSO:

Cisco Finesse

Cisco Unified Intelligence Center

For more information about SSO Solution overview, see https://developer.cisco.com/docs/contact-center-express/#cisco-identity-service-client-sdk-overview .

For more information about the third-party integrations, see https://developer.cisco.com/docs/contact-center-express/#cisco-identity-service-client-sdk-guide/overview .

| Note | For an SSO enabled user, use the access token in the authorization header of the Finesse REST APIs. Authorization: Bearer < access token > |
|---|---|