---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-118771-configure-sa-d0a74608f7
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/118771-configure-samlsso-00.html
retrieved_at: 2026-08-16T18:51:55.744705+00:00
---

AD FS Version 2.0 Setup for SAML SSO Configuration Example

# AD FS Version 2.0 Setup for SAML SSO Configuration Example

### Download Options

Updated: February 27, 2018

Document ID: 118771

Contents

## Contents

## Introduction

This document describes how to configure Active Directory Federation Service (AD FS) Version 2.0 in order to enable Security Assertion Markup Language (SAML) Single Sign-on (SSO) for Cisco Collaboration products like Cisco Unified Communications Manager (CUCM), Cisco Unity Connection (UCXN), CUCM IM and Presence, and Cisco Prime Collaboration.

## Prerequisites

### Requirements

AD FS Version 2.0 must be installed and tested.

Caution : This installation guide is based on a lab setup and AD FS Version 2.0 is assumed to be used only for SAML SSO with Cisco Collaboration products. In case it is used by other business-critical applications, then necessary customization must be done as per official Microsoft Documentation.

### Components Used

The information in this document is based on these software and hardware versions:

- AD FS Version 2.0

- Microsoft Internet Explorer 10

- CUCM Version 10.5

- Cisco IM and Presence Server Version 10.5

- UCXN Version 10.5

- Cisco Prime Collaboration Provisioning 10.5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Download AD FS Version 2.0 Identity Provider (IdP) Metadata

In order to download IdP metadata, run this link on you browser: https://<FQDN of ADFS>/FederationMetadata/2007-06/FederationMetadata.xml.

### Download Collaboration Server (SP) Metadata

#### CUCM IM and Presence Service

Open a web browser, log into CUCM as administrator, and navigate to System > SAML Single Sign On .

#### Unity Connection

Open a web browser, log into UCXN as administrator, and navigate to System Settings > SAML Single Sign On .

#### Cisco Prime Collaboration Provisioning

Open a web browser, log into Prime Collaboration Assurance as globaladmin, and navigate to Administration > System Setup > Single Sign On .

### Add CUCM as Relying Party Trust

- Log into the AD FS server and launch AD FS Version 2.0 from the Microsoft Windows Programs menu.

Note : - The Lightweight Directory Access Protocol (LDAP) attribute should match the Directory Sync attribute on CUCM. -  “uid” should be in lower case.

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]=> issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:transient", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/namequalifier"] = "http://<FQDN of ADFS>/com/adfs/services/trust", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/spnamequalifier"] = "<FQDN of CUCM>");
```

Note : - CUCM and ADFS Fully Qualified Domain Name (FQDN) is prepopulated with the lab CUCM and AD FS in this example and must be modified to match your environment. - FQDN of CUCM/ADFS are case-sensitive and must match with the metadata files.

- Click Finish .

- Click Apply and then OK.

- Restart the AD FS Version 2.0 service from Services.msc .

### Add CUCM IM and Presence as Relying Party Trust

- Repeat Steps 1 to 11 as described for Add CUCM as Relying Party Trust and proceed to Step 2.

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]=> issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:transient", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/namequalifier"] = "http://<FQDN of ADFS>/com/adfs/services/trust", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/spnamequalifier"] = "<FQDN of IMP>");
```

- Click Finish .

- Click Apply and then OK.

- Restart the AD FS Version 2.0 service from Services.msc.

### Add UCXN as Relying Party Trust

- Repeat Steps 1 to 12 as described for Add CUCM as Relying Party Trust and proceed to Step 2.

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]=> issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:transient", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/namequalifier"] = "http://<FQDN of ADFS>/com/adfs/services/trust", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/spnamequalifier"] = "<FQDN of UCXN>");
```

- Click Finish .

- Click Apply and then OK .

- Restart the AD FS Version 2.0 service from Services.msc.

### Add Cisco Prime Collaboration Provisioning as Relying Party Trust

- Repeat Steps 1 to 12 as described for Add CUCM as Relying Party Trust and proceed to Step 2.

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]=> issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:transient", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/namequalifier"] = "http://<FQDN of ADFS>/com/adfs/services/trust", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/spnamequalifier"] = "<FQDN of PCP>");
```

- Click Finish .

- Click Apply and then OK .

- Restart the AD FS Version 2.0 service from Services.msc .

Once you set up AD FS Version 2.0, proceed to enable SAML SSO on Cisco Collaboration products.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

AD FS logs diagnostic data to the system Event Log.  From Server Manager on the AD FS server open Diagnostics -> Event Viewer -> Applications and Services -> AD FS 2.0 -> Admin

Look for errors logged for AD FS activity

### Revision History

1.0

20-Jan-2015

Initial Release

### Contributed by Cisco Engineers

A M Mahesh Babu

Cisco TAC

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

- Unity Connection

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 20-Jan-2015 | Initial Release |