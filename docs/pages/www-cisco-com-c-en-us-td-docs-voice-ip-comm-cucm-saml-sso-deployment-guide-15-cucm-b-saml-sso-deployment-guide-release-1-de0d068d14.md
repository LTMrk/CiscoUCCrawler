---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-saml-sso-deployment-guide-15-cucm-b-saml-sso-deployment-guide-release-1-de0d068d14
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/SAML_SSO_deployment_guide/15/cucm_b_saml-sso-deployment-guide-release-15/cucm_b_saml-sso-deployment-guide-12_5_chapter_011.html
retrieved_at: 2026-08-17T00:39:04.746203+00:00
---

SAML SSO Deployment Guide for Cisco Unified Communications Applications, Release 15 and SUs

# SAML SSO Deployment Guide for Cisco Unified Communications Applications, Release 15 and SUs

Updated: May 26, 2025

Chapter: End User SAML SSO

## Chapter: End User SAML SSO

- End User SAML SSO

- End User SAML SSO Configuration

# End User SAML SSO

## End User SAML SSO Configuration

End user or federated SSO is a standard that allows products to meet customer compliance requirements, reduce the total cost
                              of ownership, and improve end user experience. The foundation for this support in the collaboration products has been introduced
                              in the 10.0 and 10.5 releases. This allows administrators to configure the infrastructure in preparation for end user clients
                              such as Cisco Unity Connection and Cisco Jabber , which is rolling out support for users with release 10.5 in the second half of 2014.

Once an Administrator enables this feature for users it will allow users in a Cisco collaboration application to log in to
                              supported applications with their corporate username and password. If the Cisco application is accessed by way of a browser
                              the user can use the same corporate username and password to log in. If the user has already logged in to another corporate
                              application in that same browser they should be able to access the application without having to provide a username and password.
                              All of these features are available within the customer network or accessible by way of a VPN.

The supported products are:

Product

Supports End User SAML SSO from Release...

More Information

Cisco Unified Communications Manager

10.5

IM and Presence Service

10.5

Cisco Unity Connection

10.5

WebEx Meeting Center

Cloud

WebEx Connect and Messenger

Cloud

Cisco WebEx Meetings Server

1.5 and 2.0

The supported end user clients are:

WebEx IOS

Available with all releases

Click here

WebEx Android

Available with all releases

Click here

WebEx Connect

Available with all releases

Click here

WebEx Messenger

Available with all releases

Click here

Jabber for Windows

10.5

Available in the second half of 2014

Jabber IOS

10.5

Available in the second half of 2014

Jabber for Android

10.5

Available in the second half of 2014

Jabber for Mac

10.5

Available in the second half of 2014

When deploying Cisco Jabber with Cisco WebEx Meeting Server, Unified Communications Manager and the WebEx Meeting Server must be in the same domain.

- When Cisco Jabber is running with SSO on a Mac, Jabber cannot automatically set a cookie once authorized for Jabber services.  Mac behavior,
                                             by default, only allows cookies for sites the user navigates to. Each time Jabber needs to check for authentication it has
                                             to go to the IdP.

- The SAML Assertion must include the email address for WebEx; the SAML Schemas should be aligned to cover that.

To trigger OAuth timer expiration correctly, ensure that the OAuthTokenExpiry value on Unified Communications Manager is greater
                                                than the WebsessionApp expiry value on Tomcat.

| Product | Supports End User SAML SSO from Release... | More Information |
|---|---|---|
| Cisco Unified Communications Manager | 10.5 | Click here |
| IM and Presence Service | 10.5 | Click here |
| Cisco Unity Connection | 10.5 | Click here |
| WebEx Meeting Center | Cloud | Click here |
| WebEx Connect and Messenger | Cloud | Click here |
| Cisco WebEx Meetings Server | 1.5 and 2.0 | Click here |

| Product | Release | More Information |
|---|---|---|
| WebEx IOS | Available with all releases | Click here |
| WebEx Android | Available with all releases | Click here |
| WebEx Connect | Available with all releases | Click here |
| WebEx Messenger | Available with all releases | Click here |
| Jabber for Windows | 10.5 | Available in the second half of 2014 |
| Jabber IOS | 10.5 | Available in the second half of 2014 |
| Jabber for Android | 10.5 | Available in the second half of 2014 |
| Jabber for Mac | 10.5 | Available in the second half of 2014 |

| Note | When deploying Cisco Jabber with Cisco WebEx Meeting Server, Unified Communications Manager and the WebEx Meeting Server must be in the same domain. When Cisco Jabber is running with SSO on a Mac, Jabber cannot automatically set a cookie once authorized for Jabber services.  Mac behavior,
                                             by default, only allows cookies for sites the user navigates to. Each time Jabber needs to check for authentication it has
                                             to go to the IdP. The SAML Assertion must include the email address for WebEx; the SAML Schemas should be aligned to cover that. To trigger OAuth timer expiration correctly, ensure that the OAuthTokenExpiry value on Unified Communications Manager is greater
                                                than the WebsessionApp expiry value on Tomcat. |
|---|---|