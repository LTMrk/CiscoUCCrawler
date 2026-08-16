---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-2-mra-exwy-b-mra-deployment-guide-x142-exwy-m-po-c25541faf2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-2/mra/exwy_b_mra-deployment-guide-x142/exwy_m_post-upgrade-tasks-for-mra-deployments.html
retrieved_at: 2026-08-16T15:21:04.381488+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X14.2)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X14.2)

Updated: August 11, 2022

Chapter: Post-Upgrade Tasks for MRA Deployments

## Chapter: Post-Upgrade Tasks for MRA Deployments

# Post-Upgrade Tasks for MRA Deployments

## To Reconfigure the MRA Access Control Settings

The Check for internal authentication availability setting will be off after the upgrade. Depending on the authentication settings on the Unified CM, this may prevent remote
                                                login by some Cisco Jabber users.

The Exclusive option in X8.9 is now configured by setting Authentication path to SAML SSO authentication . This has the effect of prohibiting authentication by username and password.

### Before you begin

On the , go to Configuration > Unified Communications > Configuration > MRA Access Control .

Do one of the following:

To take advantage of the new MRA access control methods from X8.10, set the appropriate values on this page for your chosen
                                                methods. See the first table below for help about which values to apply.

Or to retain your pre-upgrade authentication approach, set the appropriate values on this page to match your previous settings
                                                on the . See the second table below for help about how to map the old  settings to their new equivalents on the .

If you configure self-describing tokens ( Authorize by OAuth token with refresh ), refresh the Unified CM nodes: Go to Configuration > Unified Communications > <UC server type> and click Refresh servers .

## Settings for MRA Access Control

The fields you actually see in the Web UI depend on whether MRA is enabled ( Unified Communications mode set to Mobile and remote access ) and on the selected authentication path. Not all the fields in the table are necessarily displayed.

Field

Description

Default

Authentication path

Hidden field until MRA is enabled. Defines how MRA authentication is controlled.

SAML SSO authentication : Clients are authenticated by an external IdP.

UCM/LDAP basic authentication : Clients are authenticated locally by the Unified CM against their LDAP credentials.

SAML SSO and UCM/LDAP : Allows either method.

None : No authentication is applied. This is the default setting until MRA is first enabled. The "None" option is needed (rather than just leaving MRA turned off) because some deployments must turn on MRA to allow functions which
                                          are not actually MRA. (Such as the Web Proxy for Meeting Server, or XMPP Federation.) Only these customers should use "None" .

Do not use it in other cases.

None before MRA turned on

UCM/LDAP after MRA turned on

Authorize by OAuth token with refresh

This option requires self-describing tokens for authorization. It's our recommended authorization option for all deployments
                                          that have the infrastructure to support them.

Only Jabber clients are currently capable of using this authorization method. Other MRA endpoints do not currently support
                                          it. The clients must also be in OAuth token with refresh authorization mode.

On

Authorize by OAuth token (previously SSO Mode)

Available if Authentication path is SAML SSO or SAML SSO and UCM/LDAP .

This option requires authentication through the IdP. Currently, only Jabber clients are capable of using this authorization
                                          method, which is not supported by other MRA endpoints.

Off

Authorize by user credentials

Available if Authentication path is UCM/LDAP or SAML SSO and UCM/LDAP .

Clients attempting to perform authentication by user credentials are allowed through MRA. This includes Jabber, and supported
                                          IP phone and TelePresence devices.

Off

Check for internal authentication availability

Available if Authorize by OAuth token with refresh or Authorize by OAuth token is enabled.

The default is No, for optimal security and to reduce network traffic.

Controls how the Expressway-E  reacts to remote client authentication requests by selecting whether or not the Expressway-C
                                          should check the home nodes.

The request asks whether the client may try to authenticate the user by OAuth token, and includes a user identity with which
                                          the Expressway-C can find the user's home cluster:

Yes : The get_edge_sso request will ask the user’s home Unified CM if OAuth tokens are supported. The home Unified CM is determined from the identity
                                          sent by the Jabber client's get_edge_sso request.

No : If the Expressway is configured not to look internally, the same response will be sent to all clients, depending on the
                                          Edge authentication settings.

The option to choose depends on your implementation and security policy. If all Unified CM nodes support OAuth tokens, you
                                          can reduce response time and overall network traffic by selecting No . Or select Yes if you want clients to use either mode of getting the edge configuration - during rollout or because you can't guarantee
                                          OAuth on all nodes.

Setting this to Yes has the potential to allow rogue inbound requests from unauthenticated remote clients. If you specify No for this setting, the Expressway prevents rogue requests.

No

Identity providers: Create or modify IdPs

Available if Authentication path is SAML SSO or SAML SSO and UCM/LDAP .

Selecting an Identity Provider

Cisco Collaboration solutions use SAML 2.0 (Security Assertion Markup Language) to enable SSO (single sign-on) for clients
                                          consuming Unified Communications services.

If you choose SAML-based SSO for your environment, note the following:

SAML 2.0 is not compatible with SAML 1.1 and you must select an IdP that uses the SAML 2.0 standard.

SAML-based identity management is implemented in different ways by vendors in the computing and networking industry, and there
                                                are no widely accepted regulations for compliance to the SAML standards.

The configuration of and policies governing your selected IdP are outside the scope of Cisco TAC (Technical Assistance Center)
                                                support. Please use your relationship and support contract with your IdP Vendor to assist in configuring the IdP properly.
                                                Cisco cannot accept responsibility for any errors, limitations, or specific configuration of the IdP.

Although Cisco Collaboration infrastructure may prove to be compatible with other IdPs claiming SAML 2.0 compliance, only
                                          the following IdPs have been tested with Cisco Collaboration solutions:

OpenAM 10.0.1

Active Directory Federation Services 2.0 (AD FS 2.0)

PingFederate®6.10.0.4

-

Identity providers: Export SAML data

Available if Authentication path is SAML SSO or SAML SSO and UCM/LDAP .

For details about working with SAML data, see SAML SSO Authentication Over the Edge .

-

Allow Jabber iOS clients to use embedded Safari

By default the IdP or Unified CM authentication page is displayed in an embedded web browser (not the Safari browser) on iOS
                                          devices. That default browser is unable to access the iOS trust store, and so cannot use any certificates deployed to the
                                          devices.

This setting optionally allows Jabber on iOS devices to use the native Safari browser. Because the Safari browser is able
                                          to access the device trust store, you can now enable password-less authentication or two factor authentication in your OAuth
                                          deployment.

A potential security issue exists for this option. The mechanism to return browser control from Safari to Jabber after the
                                          authentication completes, uses a custom URL scheme that invokes a custom protocol handler. It's possible that another application
                                          other than Jabber could intercept the scheme and gain control from iOS. In that case, the application would have access to
                                          the OAuth token in the URL.

If you are confident that your iOS devices will not have other applications that register the Jabber custom URL scheme, for
                                          example because all mobile devices are managed, then it's safe to enable the option. If you are concerned about the possibility
                                          of another app intercepting the custom Jabber URL, then do not enable the embedded Safari browser.

No

SIP token extra time to live

Available if Authorize by OAuth token is On .

Optionally extends the time-to-live for simple OAuth tokens (in seconds). Gives users a short window to accept calls after
                                          their credentials expire. However, it increases the potential security exposure.

0 seconds

## MRA Access Control Values Applied by the Upgrade

Option

Value after upgrade

Previously on...

Now on...

Authentication path

Pre-upgrade setting is applied

SSO mode = Off in X8.9 is two settings in X8.10:

Authentication path = UCM/LDAP

Authorize by user credentials = On

SSO Mode = Exclusive in X8.9 is two settings in X8.10:

Authentication path = SAML SSO

Authorize by OAuth token = On

SSO Mode = On in X8.9 is three settings in X8.10:

Authentication path = SAML SSO/and UCM/LDAP

Authorize by OAuth token = On

Authorize by user credentials = On

Both

Expressway-C

Authorize by OAuth token with refresh

On

-

Expressway-C

Authorize by OAuth token (previously SSO Mode)

Pre-upgrade setting is applied

Both

Expressway-C

Authorize by user credentials

Pre-upgrade setting is applied

Both

Expressway-C

Check for internal authentication availability

No

Expressway-E

Expressway-C

Identity providers: Create or modify IdPs

Pre-upgrade setting is applied

Expressway-C

Expressway-C (no change)

Identity providers: Export SAML data

Pre-upgrade setting is applied

Expressway-C

Expressway-C (no change)

Allow Jabber iOS clients to use embedded Safari

No

Expressway-E

Expressway-C

SIP token extra time to live

Pre-upgrade setting is applied

Expressway-C

Expressway-C (no change)

| Important | The Check for internal authentication availability setting will be off after the upgrade. Depending on the authentication settings on the Unified CM, this may prevent remote
                                                login by some Cisco Jabber users. The Exclusive option in X8.9 is now configured by setting Authentication path to SAML SSO authentication . This has the effect of prohibiting authentication by username and password. |
|---|---|

| Step 1 | On the , go to Configuration > Unified Communications > Configuration > MRA Access Control . |
|---|---|
| Step 2 | Do one of the following: To take advantage of the new MRA access control methods from X8.10, set the appropriate values on this page for your chosen
                                                methods. See the first table below for help about which values to apply. Or to retain your pre-upgrade authentication approach, set the appropriate values on this page to match your previous settings
                                                on the . See the second table below for help about how to map the old  settings to their new equivalents on the . |
| Step 3 | If you configure self-describing tokens ( Authorize by OAuth token with refresh ), refresh the Unified CM nodes: Go to Configuration > Unified Communications > <UC server type> and click Refresh servers . |

| Field | Description | Default |
|---|---|---|
| Authentication path | Hidden field until MRA is enabled. Defines how MRA authentication is controlled. SAML SSO authentication : Clients are authenticated by an external IdP. UCM/LDAP basic authentication : Clients are authenticated locally by the Unified CM against their LDAP credentials. SAML SSO and UCM/LDAP : Allows either method. None : No authentication is applied. This is the default setting until MRA is first enabled. The "None" option is needed (rather than just leaving MRA turned off) because some deployments must turn on MRA to allow functions which
                                          are not actually MRA. (Such as the Web Proxy for Meeting Server, or XMPP Federation.) Only these customers should use "None" . Note Do not use it in other cases. | Note | Do not use it in other cases. | None before MRA turned on UCM/LDAP after MRA turned on |
| Note | Do not use it in other cases. |
| Authorize by OAuth token with refresh | This option requires self-describing tokens for authorization. It's our recommended authorization option for all deployments
                                          that have the infrastructure to support them. Only Jabber clients are currently capable of using this authorization method. Other MRA endpoints do not currently support
                                          it. The clients must also be in OAuth token with refresh authorization mode. | On |
| Authorize by OAuth token (previously SSO Mode) | Available if Authentication path is SAML SSO or SAML SSO and UCM/LDAP . This option requires authentication through the IdP. Currently, only Jabber clients are capable of using this authorization
                                          method, which is not supported by other MRA endpoints. | Off |
| Authorize by user credentials | Available if Authentication path is UCM/LDAP or SAML SSO and UCM/LDAP . Clients attempting to perform authentication by user credentials are allowed through MRA. This includes Jabber, and supported
                                          IP phone and TelePresence devices. | Off |
| Check for internal authentication availability | Available if Authorize by OAuth token with refresh or Authorize by OAuth token is enabled. The default is No, for optimal security and to reduce network traffic. Controls how the Expressway-E  reacts to remote client authentication requests by selecting whether or not the Expressway-C
                                          should check the home nodes. The request asks whether the client may try to authenticate the user by OAuth token, and includes a user identity with which
                                          the Expressway-C can find the user's home cluster: Yes : The get_edge_sso request will ask the user’s home Unified CM if OAuth tokens are supported. The home Unified CM is determined from the identity
                                          sent by the Jabber client's get_edge_sso request. No : If the Expressway is configured not to look internally, the same response will be sent to all clients, depending on the
                                          Edge authentication settings. The option to choose depends on your implementation and security policy. If all Unified CM nodes support OAuth tokens, you
                                          can reduce response time and overall network traffic by selecting No . Or select Yes if you want clients to use either mode of getting the edge configuration - during rollout or because you can't guarantee
                                          OAuth on all nodes. Caution Setting this to Yes has the potential to allow rogue inbound requests from unauthenticated remote clients. If you specify No for this setting, the Expressway prevents rogue requests. | Caution | Setting this to Yes has the potential to allow rogue inbound requests from unauthenticated remote clients. If you specify No for this setting, the Expressway prevents rogue requests. | No |
| Caution | Setting this to Yes has the potential to allow rogue inbound requests from unauthenticated remote clients. If you specify No for this setting, the Expressway prevents rogue requests. |
| Identity providers: Create or modify IdPs | Available if Authentication path is SAML SSO or SAML SSO and UCM/LDAP . Selecting an Identity Provider Cisco Collaboration solutions use SAML 2.0 (Security Assertion Markup Language) to enable SSO (single sign-on) for clients
                                          consuming Unified Communications services. If you choose SAML-based SSO for your environment, note the following: SAML 2.0 is not compatible with SAML 1.1 and you must select an IdP that uses the SAML 2.0 standard. SAML-based identity management is implemented in different ways by vendors in the computing and networking industry, and there
                                                are no widely accepted regulations for compliance to the SAML standards. The configuration of and policies governing your selected IdP are outside the scope of Cisco TAC (Technical Assistance Center)
                                                support. Please use your relationship and support contract with your IdP Vendor to assist in configuring the IdP properly.
                                                Cisco cannot accept responsibility for any errors, limitations, or specific configuration of the IdP. Although Cisco Collaboration infrastructure may prove to be compatible with other IdPs claiming SAML 2.0 compliance, only
                                          the following IdPs have been tested with Cisco Collaboration solutions: OpenAM 10.0.1 Active Directory Federation Services 2.0 (AD FS 2.0) PingFederate®6.10.0.4 | - |
| Identity providers: Export SAML data | Available if Authentication path is SAML SSO or SAML SSO and UCM/LDAP . For details about working with SAML data, see SAML SSO Authentication Over the Edge . | - |
| Allow Jabber iOS clients to use embedded Safari | By default the IdP or Unified CM authentication page is displayed in an embedded web browser (not the Safari browser) on iOS
                                          devices. That default browser is unable to access the iOS trust store, and so cannot use any certificates deployed to the
                                          devices. This setting optionally allows Jabber on iOS devices to use the native Safari browser. Because the Safari browser is able
                                          to access the device trust store, you can now enable password-less authentication or two factor authentication in your OAuth
                                          deployment. A potential security issue exists for this option. The mechanism to return browser control from Safari to Jabber after the
                                          authentication completes, uses a custom URL scheme that invokes a custom protocol handler. It's possible that another application
                                          other than Jabber could intercept the scheme and gain control from iOS. In that case, the application would have access to
                                          the OAuth token in the URL. If you are confident that your iOS devices will not have other applications that register the Jabber custom URL scheme, for
                                          example because all mobile devices are managed, then it's safe to enable the option. If you are concerned about the possibility
                                          of another app intercepting the custom Jabber URL, then do not enable the embedded Safari browser. | No |
| SIP token extra time to live | Available if Authorize by OAuth token is On . Optionally extends the time-to-live for simple OAuth tokens (in seconds). Gives users a short window to accept calls after
                                          their credentials expire. However, it increases the potential security exposure. | 0 seconds |

| Note | Do not use it in other cases. |
|---|---|

| Caution | Setting this to Yes has the potential to allow rogue inbound requests from unauthenticated remote clients. If you specify No for this setting, the Expressway prevents rogue requests. |
|---|---|

| Option | Value after upgrade | Previously on... | Now on... |
|---|---|---|---|
| Authentication path | Pre-upgrade setting is applied Note SSO mode = Off in X8.9 is two settings in X8.10: Authentication path = UCM/LDAP Authorize by user credentials = On SSO Mode = Exclusive in X8.9 is two settings in X8.10: Authentication path = SAML SSO Authorize by OAuth token = On SSO Mode = On in X8.9 is three settings in X8.10: Authentication path = SAML SSO/and UCM/LDAP Authorize by OAuth token = On Authorize by user credentials = On | Note | SSO mode = Off in X8.9 is two settings in X8.10: Authentication path = UCM/LDAP Authorize by user credentials = On SSO Mode = Exclusive in X8.9 is two settings in X8.10: Authentication path = SAML SSO Authorize by OAuth token = On SSO Mode = On in X8.9 is three settings in X8.10: Authentication path = SAML SSO/and UCM/LDAP Authorize by OAuth token = On Authorize by user credentials = On | Both | Expressway-C |
| Note | SSO mode = Off in X8.9 is two settings in X8.10: Authentication path = UCM/LDAP Authorize by user credentials = On SSO Mode = Exclusive in X8.9 is two settings in X8.10: Authentication path = SAML SSO Authorize by OAuth token = On SSO Mode = On in X8.9 is three settings in X8.10: Authentication path = SAML SSO/and UCM/LDAP Authorize by OAuth token = On Authorize by user credentials = On |
| Authorize by OAuth token with refresh | On | - | Expressway-C |
| Authorize by OAuth token (previously SSO Mode) | Pre-upgrade setting is applied | Both | Expressway-C |
| Authorize by user credentials | Pre-upgrade setting is applied | Both | Expressway-C |
| Check for internal authentication availability | No | Expressway-E | Expressway-C |
| Identity providers: Create or modify IdPs | Pre-upgrade setting is applied | Expressway-C | Expressway-C (no change) |
| Identity providers: Export SAML data | Pre-upgrade setting is applied | Expressway-C | Expressway-C (no change) |
| Allow Jabber iOS clients to use embedded Safari | No | Expressway-E | Expressway-C |
| SIP token extra time to live | Pre-upgrade setting is applied | Expressway-C | Expressway-C (no change) |

| Note | SSO mode = Off in X8.9 is two settings in X8.10: Authentication path = UCM/LDAP Authorize by user credentials = On SSO Mode = Exclusive in X8.9 is two settings in X8.10: Authentication path = SAML SSO Authorize by OAuth token = On SSO Mode = On in X8.9 is three settings in X8.10: Authentication path = SAML SSO/and UCM/LDAP Authorize by OAuth token = On Authorize by user credentials = On |
|---|---|