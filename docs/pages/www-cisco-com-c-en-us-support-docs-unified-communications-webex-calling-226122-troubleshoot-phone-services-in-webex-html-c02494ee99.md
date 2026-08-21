---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-226122-troubleshoot-phone-services-in-webex-html-c02494ee99
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/226122-troubleshoot-phone-services-in-webex.html
retrieved_at: 2026-08-21T07:16:02.105948+00:00
---

Troubleshoot Phone Services in Webex Unified CM

# Troubleshoot Phone Services in Webex Unified CM

### Download Options

Updated: July 7, 2026

Document ID: 226122

Contents

## Contents

## Introduction

This document describes what to do in different scenarios for Phone Services not registering in Webex Unified CM.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Webex

- Cisco Unified Communications Manager (CUCM)

- Cisco Mobile and Remote Access (MRA)

- Single Sign-On (SSO)

### Components Used

- Cisco Webex

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Troubleshooting

When Phone services do not connect, Webex provides a specific error code. All of the different error codes are listed in this link. This section describes how to solve the most common ones.

#### SSOStartSessionError. Error: 1000:500

Failed to start a new SSO session. Try again.

Solution

Remove the CUCM server from the Expressway-C and re-add it. If the issue happens also on mobile, delete the Webex app and re-install it.

#### SSOUnknownError. Error: 1000:600

Can't load SSO browser page. Try again.

Solution

Most of the times this is an issue with the Identity Provider (IdP). Webex is not receiving the token and this requires deeper troubleshooting. Open a TAC case to troubleshoot this issue.

#### SSOInvalidUserSwitch. Error: 1000:604

Sign into your account to use your phone services.

Solution

Ensure that the Mail ID of the CUCM user matches with the User ID of the user in Control Hub.

#### CredentialsRequired. Error: 1000:611

Sign into your account to use your phone services.

Solution

When the user log in to Webex and the Phone services credentials are not auto-populated, Webex fails with this error. To solve it, the user must manually enter the Phone services credentials.

#### ServiceDiscoveryAuthenticationFailure. Error: 1000:1002

Incorrect username or password.

Solution

Review that the user is able to log in to the Self-care portal. If they cannot log in, there is a Lightweight Directory Access Protocol (LDAP) issue. If they can log in, review that the certificates are valid and trusted.

#### ServiceDiscoveryCannotConnectToCucmServer. Error: 1000:1003

Can't communicate with Unified CM server. Check your phone service preferences.

Solution

Ensure that the End user has the proper Role: Standard CCM End User . If the issue happens only over MRA, ensure that the communication between CUCM and the Expressway-C is in a good state. If needed, review that the certificates are exchanged between CUCM and Expressway-C and refresh the connection in Expressway-C.

#### ServiceDiscoveryNoSRVRecordsFound. Error: 1000:1005

Can't find your SRV record. Check your phone service preferences.

Solution

Webex neither finds the cisco-uds nor the collab-edge SRV records. To resolve this, configure the SRV records as per the guide.

#### ServiceDiscoveryUntrustedCertificate. Error: 1000:1008

No service discovered due to an untrusted certificate from server.

Solution

Validate this:

- The certificate presented to Webex is not expired.

- The certificate is CA-signed or the certificate is Self-signed and it is installed in the Trusted Root Certification of the PC.

- The URLs in the Certificate Revocation List (CRL) from the certificate are reachable.

- The server list in CUCM has the nodes listed as Fully Qualified Domain Name (FQDN), not as IP or hostname.

- If the client is from Apple, the certificate must have a validity period of less that 825 days.

#### ServiceDiscoveryServersUdsRequestFailure. Error: 1000:1017

Webex failed to fetch UDS Servers from CUCM.

Solution

In CUCM, ensure the End user has the Client Services Framework (CSF) device assigned. In Control Hub, ensure that the user has the Unified CM license assigned.

#### ServiceDiscoverySSOQueryFailure. Error: 1000:1018

Webex failed to query SSO status from CUCM during on-premises connection.

Solution

Ensure that the device can reach the CUCM server. Also, ensure that the SRV records are configured as per the guide.

#### ServiceDiscoveryEdgeGetOAuthCbRequestFailed. Error: 1000:1020

Webex failed to query SSO status from Expressway during MRA connection.

Solution

Ensure that the device can reach the Expressway-E. Also, ensure that the SRV records are configured as per the guide.

#### ServiceDiscoveryEdgeGetEdgeSSORequestFailed. Error: 1000:1021

Webex failed to fetch SSO authenticate URL from Expressway during MRA connection.

Solution

Ensure that the device can reach the Expressway-E. Also, ensure that the SRV records are configured as per the guide.

#### ServiceDiscoveryLocatorUDSNoHomeUDSFound. Error: 1000:1032

No Home cluster found.

Solution

Ensure the Home cluster checkbox is enabled for the affected user. If multiple clusters, ensure the Home cluster checkbox is enabled only on one cluster.

#### ServiceDiscoveryCreateDeviceFailedServerError. Error: 1000:1042

Failed to create device and CUCM replied with HTTP 500 error.

Solution

Ensure that the affected End user has a CSF device created and associated.

#### ServiceDiscoveryCreateDeviceFailedExtensionNotAssociated. Error: 1000:1044

Failed to create device because no extension DN is associated with the userId in CUCM. CUCM replied with HTTP 601 error.

Solution

This error occurs when Auto-provisioning is enabled. For this feature to work, the End user must have a Primary extension. Add the Primary extenstion to solve the issue.

### Revision History

1.0

07-Jul-2026

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Jul-2026 | Initial Release |