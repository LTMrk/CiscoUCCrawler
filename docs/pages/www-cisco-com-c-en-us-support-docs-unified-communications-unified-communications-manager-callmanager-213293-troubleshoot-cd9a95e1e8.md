---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213293-troubleshoot-cd9a95e1e8
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213293-troubleshoot-sso-in-cucm.html
retrieved_at: 2026-08-21T13:57:35.323277+00:00
---

Troubleshoot SSO in Cisco Unified Communications Manager

# Troubleshoot SSO in Cisco Unified Communications Manager

Updated: April 28, 2018

Document ID: 213293

Contents

## Contents

## Introduction

This document describes how to configure Single Sign-On (SSO) in Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of the topics:

- CUCM

- Active Directory Federation Services (ADFS)

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM 11.5.1.13900-52 (11.5.1SU2)

- ADFS 2.0.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

Refer to Configuration of Single Sign on in CUCM.

- https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-version-105/118770-configure-cucm-00.html

- https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/211302-Configure-Single-Sign-On-using-CUCM-and.html

SAML SSO Deployment Guide for Cisco Unified Communications Applications, Release 11.5(1).

- https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/SAML_SSO_deployment_guide/11_5_1/CUCM_BK_S12EF288_00_saml-sso-deployment-guide--1151.html

SAML RFC 6596.

- https://tools.ietf.org/html/rfc6595

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

### Login Flow in SSO

### Decoding SAML Response

Using Plugins in Notepad++

Install these Plugins:

```
Notepad++ Plugin -> MIME Tools--SAML DECODE Notepad++ Plugin -> XML Tools -> Pretty Print(XML only – with line breaks)
```

In SSO logs search for the string "authentication.SAMLAuthenticator - SAML Response is ::" which contains the encoded response.

Use this plugin or online SAML Decode in order to get the XML response. The response can be adjusted in a readable format with the use installed Pretty Print plugin.

In the newer version of CUCM SAML response is in XML format which can be found by searching "SPACSUtils.getResponse: got response=<samlp:

Response xmlns:samlp=“and then print with the use of Pretty Print plugin.

Use Fiddler:

This utility can be used to get the real-time traffic and decode it. Here is the guide for the same; https://www.techrepublic.com/blog/software-engineer/using-fiddler-to-debug-http/ .

SAML Request:

```
ID="s24c2d07a125028bfffa7757ea85ab39462ae7751f" Version="2.0" IssueInstant="2017-07-15T11:48:26Z" Destination="https://win-91uhcn8tt3l.emeacucm.com/adfs/ls/" ForceAuthn="false" IsPassive="false" AssertionConsumerServiceIndex="0">
<saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">cucmsso.emeacucm.com</saml:Issuer>
<samlp:NameIDPolicy xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient" SPNameQualifier="cucmsso.emeacucm.com" AllowCreate="true"/>
</samlp:AuthnRequest>
```

SAML Response (unencrypted):

```
<samlp:Response ID="_53c5877a-0fff-4420-a929-1e94ce33120a" Version="2.0" IssueInstant="2017-07-01T16:50:59.105Z" Destination="https://cucmsso.emeacucm.com:8443/ssosp/saml/SSO/alias/cucmsso.emeacucm.com" Consent="urn:oasis:names:tc:SAML:2.0:consent:unspecified" InResponseTo="s24c2d07a125028bfffa7757ea85ab39462ae7751f" xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol">
<Issuer xmlns="urn:oasis:names:tc:SAML:2.0:assertion">http://win-91uhcn8tt3l.emeacucm.com/adfs/services/trust</Issuer>
<samlp:Status>
<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success" />
</samlp:Status>
<Assertion ID="_0523022c-1e9e-473d-9914-6a93133ccfc7" IssueInstant="2017-07-01T16:50:59.104Z" Version="2.0" xmlns="urn:oasis:names:tc:SAML:2.0:assertion">
<Issuer>http://win-91uhcn8tt3l.emeacucm.com/adfs/services/trust</Issuer>
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
<ds:SignedInfo>
<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
<ds:Reference URI="#_0523022c-1e9e-473d-9914-6a93133ccfc7">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
<ds:DigestValue>9OvwrpJVeOQsDBNghwvkLIdnf3bc7aW82qmo7Zdm/Z4=</ds:DigestValue>
</ds:Reference>
</ds:SignedInfo>
<ds:SignatureValue>VbWcKUwvwiNDhUg5AkdqSzQOmP0qs5OT2VT+u1LivWx7h9U8/plyhK3kJMUuxoG/HXPQJgVQaMOwNq/Paz7Vg2uGNFigA2AFQsKgGo9hAA4etfucIQlMmkeVg+ocvGY+8IzaNVfaUXSU5laN6zriTArxXwxCK0+thgRgQ8/46vm91Skq2Fa5Wt5uRPJ3F4eZPOEPdtKxOmUuHi3Q2pXTw4ywZ/y89xPfSixNQEmr10hpPAdyfPsIFGdNJJwWJV4WjNmfcAqClzaG8pB74e5EawLmwrfV3/i8QfR1DyU5yCCpxj02rgE6Wi/Ew/X/l6qSCzOZEpl7D8LwAn74KijO+Q==</ds:SignatureValue>
<KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#">
<ds:X509Data>
<ds:X509Certificate>MIIC5DCCAcygAwIBAgIQZLLskb6vppxCiYP8xOahQDANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNBREZTIFNpZ25pbmcgLSBXSU4ySzEyLnJrb3R1bGFrLmxhYjAeFw0xNTA2MjIxOTE2NDRaFw0xNjA2MjExOTE2NDRaMC4xLDAqBgNVBAMTI0FERlMgU2lnbmluZyAtIFdJTjJLMTIucmtvdHVsYWsubGFiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApEe09jnZXEcEC7s1VJ7fMXAHPXj7jgOOcs9/Lzxrx4c68tePGItrEYnzW9vLe0Dj8OJET/Rd6LsKvuMQHfcGYqA+XugZyHBrpc18wlhSmMfvfa0jN0Qc0lf+a3j72xfI9+hLtsqSPSnMp9qby3qSiQutP3/ZyXRN/TnzYDEmzur2MA+GP7vdeVOFXlpENrRfaINzc8INqGRJ+1jZrm+vLFvX7YwIL6aOpmjaxcPoxDcjgEGMYO/TaoP3eXutX4FuJV5R9oAvbqD2F+73XrvP4e/wHi5aNrHrgiCnuBJTIxHwRGSoichdpZlvSB15v8DFaQSVAiEMPj1vP/4rMkacNQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA5uJZI0K1Xa40H3s5MAo1SG00bnn6+sG14eGIBe7BugZMw/FTgKd3VRsmlVuUWCabO9EgyfgdI1nYZCciyFhts4W9Y4BgTH0j4+VnEWiQg7dMqp2M5lykZWPS6vV2uD010sX5V0avyYi3Qr88vISCtniIZpl24c3TqTn/5j+H7LLRVI/ZU38Oa17wuSNPyed6/N4BfWhhCRZAdJgijapRG+JIBeoA1vNqN7bgFQMe3wJzSlLkTIoERWYgJGBciMPS3H9nkQlP2tGvmn0uwacWPglWR/LJG3VYoisFm/oliNUF1DONK7QYiDzIE+Ym+vzYgIDS7MT+ZQ3XwHg0Jxtr8</ds:X509Certificate>
</ds:X509Data>
</KeyInfo>
</ds:Signature>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient" NameQualifier="http:///win-91uhcn8tt3l.emeacucm.com/com/adfs/services/trust" SPNameQualifier="cucmsso.emeacucm.com">CHANDMIS\chandmis</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData InResponseTo="s24c2d07a125028bfffa7757ea85ab39462ae7751f" NotOnOrAfter="2017-07-01T16:55:59.105Z" Recipient="https://cucmsso.emeacucm.com:8443/ssosp/saml/SSO/alias/cucmsso.emeacucm.com" />
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2017-07-01T16:50:59.102Z" NotOnOrAfter="2017-07-01T17:50:59.102Z">
<AudienceRestriction>
<Audience>ccucmsso.emeacucm.com</Audience>
</AudienceRestriction>
</Conditions>
<AttributeStatement>
<Attribute Name="uid">
<AttributeValue>chandmis</AttributeValue>
</Attribute>
</AttributeStatement>
<AuthnStatement AuthnInstant="2017-07-01T16:50:59.052Z" SessionIndex="_0523022c-1e9e-473d-9914-6a93133ccfc7">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>
```

</samlp:Response>

```
Version="2.0"  :- The version of SAML being used.
 
InResponseTo="s24c2d07a125028bfffa7757ea85ab39462ae7751f" :- The id for SAML Request to which this reponse corresponds to
 
samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success :- Status Code of SAML reponse. In this case it is Success.
 
<Issuer>http://win-91uhcn8tt3l.emeacucm.com/adfs/services/trust</Issuer> :- IdP FQDN
 
SPNameQualifier="cucmsso.emeacucm.com" :- Service Provider(CUCM) FQDN
 
Conditions NotBefore="2017-07-01T16:50:59.102Z" NotOnOrAfter="2017-07-01T17:50:59.102Z :- Time range for which the session will be valid.
 
<AttributeValue>chandmis</AttributeValue> :- UserID entered during the login
```

In case the SAML response is encrypted then you won't be able to see the complete information and have to disable encryption on Intrusion Detection & Prevention ( IDP) to see the complete response. The certificate detail used for encryption is under " ds :X509IssuerSerial " of the SAML response.

### Logs and CLI Commands

CLI Commands:

utils sso disable

This command disables both (OpenAM SSO or SAML SSO) based authentication. This command lists the web applications for which SSO is enabled. Enter Yes when prompted in order to disable SSO for the specified application. You must run this command on both the nodes if in a cluster. SSO can also be disabled from Graphical User Interface (GUI) and select the Disable button, under specific SSO in Cisco Unity Connection Administration.

Command Syntax utils sso disable

utils sso status

This command displays the status and configuration parameters of SAML SSO. It helps to verify the SSO status, enabled or disabled, on each node individually.

Command Syntax utils sso status

utils sso enable

This command returns an informational text message that prompts that the administrator can enable SSO feature only from GUI. Both OpenAM based SSO and SAML based SSO cannot be enabled with this command.

Command Syntax utils sso enable

utils sso recovery-url enable

This command enables the Recovery URL SSO mode. It also verifies that this URL works successfully. You must run this command on both the nodes if in a cluster.

Command Syntax utils sso recovery-url enable

utils sso recovery-url disable

This command disables the Recovery URL SSO mode on that node. You must run this command on both the nodes if in a cluster.

Command syntax utils sso recovery-url disable

set samltrace level <trace-level>

This command enables the specific traces and trace-levels that can locate any error, debug, information, warning or fatal. You must run this command on both the nodes if in a cluster.

Command syntax set samltrace level <trace-level>

show samltrace level

This command displays the log level set for SAML SSO. You must run this command on both the nodes if in a cluster.

Command syntax show samltrace level

Traces to look at the time of troubleshoot:

SSO logs are not set to detailed level by default.

First run the command set samltrace level debug in order to set the log levels to debug, reproduce the issue and the collect these set of logs.

From RTMT:

Cisco Tomcat

Cisco Tomcat Security

Cisco SSO

### Common Issues

Incorrect Value for Unique Indentifier (UID):

It should exactly be UID and if it’s not the case, CUCM is unable to understand that.

Incorrect Claim Rule or Wrong NameID policy:

Most likely no username and password is prompt up in this scenario.

There won’t be any valid assertion in the SAML response and Status Code will be like:

```
<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:InvalidNameIDPolicy"/>
```

Verify that the claim rule is correctly defined at the IDP side.

Difference in case/name Defined in Claim Rule:

CUCM FQDN in claim rule should exactly match with the one specified on the actual server.

You can compare the entry in metadata xml file of IDP with the one on CUCM by running show network cluster / show network etho details command on CLI of CUCM.

Incorrect Time:

NTP between CUCM and IDP has a difference greater than the 3 seconds allowed in the Deployment Guide.

Assertion Signer Not Trusted:

At the time of the exchange of the metadata between IDP and CUCM (service provider).

Certificates are exchanged and if there is any revocation of certificate done, metadata should be exchanged again.

DNS Misconfiguration/No Configuration

DNS is the primary requirement for SSO to work. Run show network etho detail , utils diagnose test on the CLI in order to verify DNS/Domain is configured correctly.

## Known Defects

CSCuj66703

ADFS Signing Certificate renews and adds two signing certs to IDP responses back to CUCM (SP) thus causes you to run into defect. You have to delete the signing certificate which is not required

CSCvf63462

When you navigate to the SAML SSO page from CCM Admin you are prompted with "The following servers failed during attempt to get SSO Status" followed by the node name.

CSCvf96778

CTI based SSO fails when defining CUCM server as IP address in CCMAdmin//System/Sever.