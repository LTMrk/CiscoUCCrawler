---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-118773-configure-kerberos-00-html-a0a79d8bf4
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/118773-configure-kerberos-00.html
retrieved_at: 2026-08-16T18:54:39.608630+00:00
---

Configure SAML SSO Setup with Kerberos Authentication

# Configure SAML SSO Setup with Kerberos Authentication

### Download Options

Updated: January 21, 2015

Document ID: 118773

Contents

## Contents

## Introduction

This document describes how to configure Active Directory and Active Directory Federation Service (AD FS) Version 2.0 in order to enable it to use Kerberos Authentication by Jabber Clients (Microsoft Windows only), which allows users to log in with their Microsoft Windows Logon and not be prompted for credentials.

Caution : This document is based on a lab environment and assumes that you are aware of the impact of changes that you make. Refer to the relevant product documentation in order to understand the impact of changes you make.

## Prerequisites

### Requirements

Cisco recommends that you have:

- AD FS Version 2.0  installed and configured with Cisco Collaboration products as Relying Party Trust

- Collaboration products such as Cisco Unified Communications Manager (CUCM) IM and Presence, Cisco Unity Connection (UCXN), and CUCM enabled in order to use Security Assertion Markup Language (SAML) Single Sign-on (SSO)

### Components Used

The information in this document is based on these software and hardware versions:

- Active Directory 2008 (Hostname: ADFS1.ciscolive.com)

- AD FS Version 2.0 (Hostname: ADFS1.ciscolive.com)

- CUCM (Hostname: CUCM1.ciscolive.com)

- Microsoft Internet Explorer Version 10

- Mozilla Firefox Version 34

- Telerik Fiddler Version 4

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Configure AD FS

Note : AD FS passes the Negotiate security header when Integrated Windows authentication is used in order to authenticate client requests. The Negotiate security header lets clients select between Kerberos authentication and NTLM authentication. The Negotiate process selects Kerberos authentication unless one of these conditions is true: - One of the systems that is involved in the authentication cannot use Kerberos authentication. - The calling application does not provide sufficient information to use Kerberos authentication. - In order to enable the Negotiate process to select the Kerberos protocol for network authentication, the client application must provide an SPN, a User Principal Name (UPN), or a Network Basic Input/Output System (NetBIOS) account name as the target name. Otherwise, the Negotiate process always selects the NTLM protocol as the preferred authentication method.

### Configure Browser

#### Microsoft Internet Explorer

#### Mozilla FireFox

- Close Firefox and re-open.

## Verify

In order to check that the SPNs for the AD FS server are properly created, enter the setspn command and view the output.

Check if the client machines have Kerberos tickets:

Complete these steps in order to verify which authentication (Kerberos or NTLM authentication) is in use.

- Download the Fiddler tool to your client machine and install it.

- Close all Microsoft Internet Explorer windows.

- Run the Fiddler Tool and check that the Capture Traffic option is enabled under the File menu. Fiddler works as a pass-through proxy between the client machine and the server and listens to all traffic.

- Open Microsoft Internet Explorer, browse into your CUCM, and click some links in order to generate traffic.

## Troubleshoot

If all of the configuration and verification steps are completed as described in this document and you still have login issues, then you must consult a Microsoft Windows Active Directory / AD FS Administrator.

### Revision History

1.0

21-Jan-2015

Initial Release

### Contributed by Cisco Engineers

A.M.Mahesh Babu

Cisco TAC Engineer.

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Jan-2015 | Initial Release |