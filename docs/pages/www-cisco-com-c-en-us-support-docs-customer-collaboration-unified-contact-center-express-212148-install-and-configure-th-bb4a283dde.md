---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-212148-install-and-configure-th-bb4a283dde
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/212148-install-and-configure-the-f5-identity-pr.html
retrieved_at: 2026-08-16T20:54:58.317776+00:00
---

Install and Configure the F5 Identity Provider (IdP) for Cisco Identity Service (IdS) to enable SSO

# Install and Configure the F5 Identity Provider (IdP) for Cisco Identity Service (IdS) to enable SSO

Updated: October 24, 2017

Document ID: 212148

Contents

## Contents

## Introduction

This document describes the configuration on the F5 BIG-IP Identity Provider (IdP) to enable Single Sign On (SSO).

Cisco IdS Deployment Models

Co-resident with CUIC and LD for 2k deployments.

Standalone for 4k and 12k deployments.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Contact Center Express (UCCX) Release 11.6 or Cisco Unified Contact Center Enterprise Release 11.6 or Packaged Contact Center Enterprise (PCCE) Release 11.6 as applicable.

Note : This document references the configuration with respect to the Cisco Identitify Service (IdS) and the Identity Provider (IdP). The document references UCCX in the screenshots and examples, however the configuration is similar with respect to the Cisco Identitify Service (UCCX/UCCE/PCCE) and the IdP.

### Components Used

This document is not restricted to specific software and hardware versions. The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Install

Big-IP is a packaged solution that has multiple features. Access Policy Manager (APM) which co-relates to the Identity Provider service.

Big-IP as APM:

Two IPs in different subnets. One for the management IP

and one for the IdP virtual server

Download the virtual edition image from Big-IP website and deploy the OVA to create a Virtual Machine (VM) that is pre-installed. Obtain the license and install with the basic requirements.

Note : For installation information, refer to Big-IP Installation guide .

## Configure

- Navigate to resource provisioning and enable Access Policy , set provisioning to Nominal

- Create a new VLAN under Network -> VLANs

- Create a new entry for the IP which is used for the IdP under Network -> Self IPs

- Create a profile under Access -> Profile/Policies -> Access profiles

- Create a virtual server

- Add Active Directory (AD) details under Access -> Authentication -> Active Directory

- Create a new IdP service under Access -> Federation - > SAML Identity Provider -> Local IdP Services

Note : If a Common Access Card (CAC) is used for authentication, these attributes need to be added in the SAML Attributes configuration section: Step 1. Create the uid attribute . Name: uid Value: %{session.ldap.last.attr.sAMAccountName} Step 2. Create the user_principal attribute. Name: user_principal Value: %{session.ldap.last.attr.userPrincipalName}

Note : Once the IdP service is created, there is an option to download the metadata with a button Export Metadata under Access -> Federation -> SAML Identity Provider -> Local IdP Services

### Security Assertion Markup Language (SAML) creation

#### SAML Resources

- Navigate to Access -> Federation -> SAML Resources and create a saml resource to associate with the IdP service that was created earlier

#### Webtops

- Create a webtop under Access -> Webtops

#### Virtual Policy Editor

- Navigate to the policy created earlier and click on edit link

- The virtual policy editor opens

- Click on the icon and add elements as described

Step 1. Logon page element - Leave all elements to default.

Step 2. AD Auth -> Choose the ADFS configuration created earlier.

Step 3. AD Query element - Assign the necessary details.

Step 4. Advance Resource Assign - Associate the saml resource and the webtop created earlier.

### Service Provider (SP) Metadata Exchange

- Manually import the certificate of the IdS to Big-IP through System -> Certificate Management -> Traffic Management

Note : Ensure that the certificate consists of BEGIN CERTIFICATE and END CERTIFICATE tags.

- Create a new entry from sp.xml under Access -> Federation -> SAML Identity Provider -> External SP Connectors

- Bind the SP connector to the IdP service under Access -> Federation -> SAML Identity Provider -> Local IdP Services

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

### Common Access Card (CAC) Authentication Failure

If SSO authentication fails for CAC users, check the UCCX ids.log to verify the SAML Attributes were set properly.

If there is a configuration issue, a SAML failure occurs. For example, in this log snippet, the user_principal SAML attribute is not configured on the IdP.

YYYY-MM-DD hh:mm:SS.sss GMT(-0000) [IdSEndPoints-SAML-59] ERROR com.cisco.ccbu.ids IdSSAMLAsyncServlet.java:465 - Could not retrieve from attributes map: user_principal

YYYY-MM-DD hh:mm:SS.sss GMT(-0000) [IdSEndPoints-SAML-59] ERROR com.cisco.ccbu.ids IdSSAMLAsyncServlet.java:298 - SAML response processing failed with exception com.sun.identity.saml.common.SAMLException: Could not retrieve user_principal from saml response

at com.cisco.ccbu.ids.auth.api.IdSSAMLAsyncServlet.getAttributeFromAttributesMap(IdSSAMLAsyncServlet.java:466)

at com.cisco.ccbu.ids.auth.api.IdSSAMLAsyncServlet.processSamlPostResponse(IdSSAMLAsyncServlet.java:263)

at com.cisco.ccbu.ids.auth.api.IdSSAMLAsyncServlet.processIdSEndPointRequest(IdSSAMLAsyncServlet.java:176)

at com.cisco.ccbu.ids.auth.api.IdSEndPoint$1.run(IdSEndPoint.java:269)

at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)

at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)

at java.lang.Thread.run(Thread.java:745)

## Related Information

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

27-Oct-2017

Initial Release

### Contributed by Cisco Engineers

Arundeep Nagaraj

Cisco TAC Engineer

Balakrishnan Doraisamy

Cisco Engineering

Jared Compiano

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Contact Center Express

| Product | Deployment |
|---|---|
| UCCX | Co-resident |
| PCCE | Co-resident with CUIC (Cisco Unified Intelligence Center) and LD (Live Data) |
| UCCE | Co-resident with CUIC and LD for 2k deployments. Standalone for 4k and 12k deployments. |

| Version | 13.0 |
|---|---|
| Type | Virtual Edition(OVA) |
| IPs | Two IPs in different subnets. One for the management IP and one for the IdP virtual server |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 27-Oct-2017 | Initial Release |