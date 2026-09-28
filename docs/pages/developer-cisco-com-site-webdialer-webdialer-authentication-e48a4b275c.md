---
doc_id: developer-cisco-com-site-webdialer-webdialer-authentication-e48a4b275c
source_url: https://developer.cisco.com/site/webdialer/webdialer/authentication/
retrieved_at: 2026-08-25T21:03:29.688316+00:00
---

# Authentication

All Cisco WebDialer API requests require authentication. Depending on the specific request, the
                credentials provided may be:

- End-user or Application-user making calls using devices associated with their user. This user must
                    be a member of the 'Standard CCM End Users' group and have a WebDialer supported device
                    associated.

- End-user or Application-user making calls on behalf of another user. This account must be a member
                    of the 'Standard EM Authentication Proxy Rights' group.

As of Cisco Unified Communications Manager (Unified CM) 10.5, Cisco WebDialer supports both Unified CM
                Single Sign On (SSO) authentication and the previous XML username+password authentication mechanism.
                Note that the WebDialer HTML implementation handles user authentication automatically within its
                provided UI, and will use SSO automatically if configured on the system.

## WebDialer SOAP Credentials

The WebDialer SOAP implementation accepts user credentials provided within the XML request. Note, these
                credentials are sent as clear text within the XML, and it is highly recommended that applications use a
                HTTPS secure connection when accessing WebDialer SOAP services. The credentials may be comprised of a
                userID+password combination, or an SSO token (if SSO is enabled.)

Note: The WebDialer SOAP API is not supported by the UC Manager CORS feature. Browser-based applications
                may encounter security errors when attempting to make WebDialer SOAP requests directly (e.g. via
                xmlHttpRequest.) Using a reverse proxy on the application server may provide a workaround.

Example credential using userID and password:

1

2

3

4

< in0 xsi:type = "urn:Credential" >

< userID xsi:type = "xsd:string" >bill</ userID >

< password xsi:type = "xsd:string" >123</ password >

</ in0 >

Example credential using SSO token:

1

2

3

< in0 xsi:type = "urn:Credential" >

< token xsi:type = "xsd:string" >MjpjMTAzNDk4NC00ZjhhLTQzMTMtYjdlNS0xMTI2MDgzNzNlZDg</ token >

</ in0 >

## What is SSO (Single Sign-On)?

Single Sign On (SSO) simplifies the login process for Users and Administrators in Cisco Unified
                Communications Products (Unified CM and Unity Connection releases 10.5).

SSO offers an easier, more consistent way for users and administrators to authenticate access to secured
                resources.

Instead of each product requiring a separate user name and password login, a single returned credential
                allows access to all enabled product interfaces.

Think of SSO as supplying the "skeleton key" to every enabled, authorized service and interface
                in your environment.

For an example and details on obtaining a UC Manager SSO token with a web application, click here

| 1 2 3 4 | < in0 xsi:type = "urn:Credential" > < userID xsi:type = "xsd:string" >bill</ userID > < password xsi:type = "xsd:string" >123</ password > </ in0 > |
|---|---|

| 1 2 3 | < in0 xsi:type = "urn:Credential" > < token xsi:type = "xsd:string" >MjpjMTAzNDk4NC00ZjhhLTQzMTMtYjdlNS0xMTI2MDgzNzNlZDg</ token > </ in0 > |
|---|---|