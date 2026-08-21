---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-200637-avoid-jabber-authentication-with-the-web-c096292d45
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/200637-Avoid-Jabber-Authentication-with-the-Web.html
retrieved_at: 2026-08-21T07:00:06.474973+00:00
---

Avoid Jabber Authentication with the WebEx Connect Cloud and Instead use an On-Premises Presence Server

# Avoid Jabber Authentication with the WebEx Connect Cloud and Instead use an On-Premises Presence Server

Updated: November 29, 2016

Document ID: 200637

Contents

## Contents

## Introduction

This document describes the solution to the instance when Jabber users are directed to the WebEx Connect cloud for authentication, instead of an on-premises Instant Messaging and Presence (IM&P) server, or through an Expressway (Collaboration Edge) configured for Mobile and Remote Access (MRA).

## Problem

The default behavior of Jabber clients is to use the WebEx Connect cloud if the organisation's domain has ever been provisioned on it.

To check whether your organisation's domain has been provisioned in the WebEx Connect cloud, enter a URL into any Web Browser (such as Internet Explorer, Firefox, Safari or Chrome). For a domain of companydomain.com, enter:

http://loginp.webexconnect.com/cas/FederatedSSO?org=companydomain.com ... as shown:

An errorcode of 7 indicates that the domain is provisioned in the WebEx Connect cloud.

If the companydomain.com is not a WebEx customer, then you can expect an errorcode of 1 , with the reason saying "SSO protocol error."

This URL is the very same URL that you will see in the trace from a Jabber for Windows Problem Report (it will also state "Domain is WebexCustomer but doesn't support WebexSso").

## Solution

The best option to avoid this from occurring is to work directly through the WebEx support organisation and have them completely remove your organisation's domain (e.g. companydomain.com) from their databases. However, this can sometimes take time to resolve. You can also choose to use an IM&P server even though your organisation also has WebEx Connect cloud services.

These are methods that can be used to specify WEBEX in EXCLUDED_SERVICES (per the documentation in the Jabber Deployment and Installation Guides ).

### Option 1.

Use EXCLUDED_SERVICES=WEBEX when Jabber for Windows client gets installed with the Microsoft Installer (MSI).

Note : If you have previously installed Jabber for Windows on the PC then jabber-bootstrap.properties needs to be deleted first (from C:\ProgramData\Cisco Systems\Cisco Jabber on a Windows 7 PC).

msiexec.exe /i CiscoJabberSetup.msi /quiet CLEAR=1 EXCLUDED_SERVICES=WEBEX

See Authentication Arguments in the Install Client chapter of the guide for your version of Jabber, for further explanation.

### Option 2.

Any Jabber for mobile client, or Jabber for Mac client, can click on the link to the URL that follows (from a web page).

Note : The client can first uninstalled, clear cache files, then re-install without starting the software, before the user clicks on the link to start the Jabber application with the required settings.

ciscojabber://provision?ServicesDomain=companydomain.com&ServiceDiscoveryExcludedServices=WEBEX

An example of HTML code that will achieve this for companydomain.com:

```
<HTML>
<BODY>
Mobile and Mac users, please <A HREF="ciscojabber://provision?ServicesDomain=companydomain.com&VoiceServicesDomain=companydomain.com&ServiceDiscoveryExcludedServices=WEBEX"> click here</A> from within a browser (such as Safari/Chrome/Firefox) on your mobile.
</BODY>
</HTML>
```

See Configuration URL in the Service Discovery chapter of the guide for your version of Jabber, for further explanation.

### Option 3.

Use <ServiceDiscoveryExcludedServices> and specify WEBEX , in a configuration file (group or the global jabber-config.xml file).

Note : This method is dependent on the client being able to first log in to CUCM IM&P and can sometimes require that the Jabber clients be on-premises to start with, possibly with communication to the WebEx cloud servers blocked, so that jabber-config.xml can be downloaded and cached.

An example of a jabber-config.xml Global configuration file to exclude WEBEX from Service Discovery:

```
<?xml version="1.0" encoding="utf-8"?> <config version="1.0"> <Policies> <ServiceDiscoveryExcludedServices>WEBEX</ServiceDiscoveryExcludedServices> </Policies> </config>
```

See Create Global Configurations in the Configure Client chapter of the guide for your version of Jabber for further explanation.

### Revision History

1.0

31-Aug-2016

Initial Release

### Contributed by Cisco Engineers

Craig Cooper

Cisco TAC Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 31-Aug-2016 | Initial Release |