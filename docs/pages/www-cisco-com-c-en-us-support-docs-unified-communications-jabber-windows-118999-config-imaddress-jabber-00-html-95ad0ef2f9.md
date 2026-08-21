---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-118999-config-imaddress-jabber-00-html-95ad0ef2f9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/118999-config-imaddress-jabber-00.html
retrieved_at: 2026-08-21T06:59:25.172048+00:00
---

Configure the IM Address Scheme for Multiple Domain Support in Cisco Jabber

# Configure the IM Address Scheme for Multiple Domain Support in Cisco Jabber

### Download Options

Updated: June 10, 2015

Document ID: 118999

Contents

## Contents

## Introduction

This document describes the configurations required in order to use flexible instant messaging (IM) address scheme with Cisco Jabber. The feature is supported from Cisco Jabber version 10.6 and later and IM Presence server 10.x. You can deploy this feature if there are users based on multiple domains that coexist in the same presence deployment. Furthermore, a user can still log into Jabber with the respective sAMAccountName attribute, even though the IM address is mapped to the Directory Uniform Resource Identifier (URI) field.

## Prerequisites

### Requirements

Cisco recommends that you have basic knowledge of Cisco Jabber for Windows, Cisco Unified Communications Manager (CUCM) and Cisco Unified Communications Manager IM and Presence.

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Unified Communications Manager IM and Presence version 10.x or later

- Cisco Unified Communications Manager version 10.x or later

- All Jabber clients that run on Windows, Mac, IOS and Android version 10.6 or later

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Configure the Server

The available IM address schemes in the Advanced Presence Settings are:

- UserID@[Default Domain]

- Directory URI

Change the IM address scheme to Directory URI in order to support multiple domains as this procedure shows:

Choose System > LDAP > LDAP Directory . Click the configured LDAP. In the Standard User Fields To Be Synchronized area of the LDAP Directory window verify that the LDAP Attribute field for Directory URI is correct.

Note : From IM and Presence versions 10.x and later, the high availability option is rebranded as Presence Redundancy Groups in Cisco CallManager. Choose System > Presence Redundancy Groups > DefaultCUPSubcluster and uncheck Enable High Availability in order to disable high availability.

- Cisco Presence Engine

- Cisco SIP Proxy

- Cisco XCP Router

- Cisco Sync Agent

- Cisco Client Profile Agent

- Start the services.

### Client Configuration

Configure the parameters in this section in the jabber-config.xml file. In this example, the DirectoryURI field is mapped to the mail attribute in Active Directory.

Jabber for MAC/Mobile Clients Basic Directory Integration (BDI)

```
<Directory> <BDIDirectoryURI>mail</BDIDirectoryURI> <BDIUseSIPURIToResolveContacts>true</BDIUseSIPURIToResolveContacts> <BDISipUri>mail</BDISipUri> <BDIUriPrefix>sip:</BDIUriPrefix> </Directory>
```

Jabber for Windows  Enhanced Directory Integration (EDI)

```
<Directory> <DirectoryURI>mail</DirectoryURI> <UseSIPURIToResolveContacts>true</UseSIPURIToResolveContacts> <SipUri>mail</SipUri> <UriPrefix>sip:</UriPrefix> </Directory>
```

CUCM User Data Service (UDS)

```
<Directory> <DirectoryServerType>UDS</DirectoryServerType> <UdsServer><cucm ip address></UdsServer> <DirectoryURI>mail</DirectoryURI> <UseSIPURIToResolveContacts>true</UseSIPURIToResolveContacts> <SipUri>mail</SipUri> <UriPrefix>sip:</UriPrefix> </Directory>
```

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

- Cisco Jabber 10.6 Deployment and Installation Guide

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

10-Jun-2015

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- Jabber for Mac

- Jabber for Windows

- Unified Communications Manager (CallManager)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Jun-2015 | Initial Release |