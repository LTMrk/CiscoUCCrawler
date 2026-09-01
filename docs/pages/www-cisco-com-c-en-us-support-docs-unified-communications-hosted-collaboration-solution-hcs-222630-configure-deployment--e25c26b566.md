---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-hcs-222630-configure-deployment--e25c26b566
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-hcs/222630-configure-deployment-mode-from-hcs-to-en.html
retrieved_at: 2026-09-01T14:57:57.383726+00:00
---

Configure Deployment Mode from HCS to Enterprise Using SOAP API

# Configure Deployment Mode from HCS to Enterprise Using SOAP API

### Download Options

Updated: November 22, 2024

Document ID: 222630

Contents

## Contents

## Introduction

This document describes how to change the deployment type from Hosted Collaboration Solution (HCS) to Enterprise through a SOAP request.

## Problem

As of version 15, Unified Communication Applications (UC Apps) are no longer supported in Hosted Collaboration Solutions (HCS) mode.

For prior versions, there were cop files available to download, which allowed us to easily change deployment mode from Enterprise to HCS and vice versa.

You can find them here:

For versions lower than 14 SU1 .

For versions higher than 14 SU1 , but not 15.

The issue occurs if you forget to change the deployment type to HCS before an upgrade to version 15, as no official COP file from Cisco permits the change.

## Solution

To change solution mode to HCS the only viable option is to use SOAP request.

For this task, you can use the Postman tool.

First, you must confirm the deployment type.

Use this URL in the address field:

```
https://CUCM-ADDRESS/platform-services/services/DeploymentModeService
```

Use basic authentication with an account that has "Standard AXL API Access" privileges set:

Configure the request type as POST and paste raw code as shown to check the deployment type:

```
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
<wsa:Action>urn:getDeploymentMode</wsa:Action>
<wsa:ReplyTo>
<wsa:Address>http://www.w3.org/2005/08/addressing/anonymous</wsa:Address>
</wsa:ReplyTo>
<wsa:MessageID>uuid:26634481-3273-4a70-b537-ab4b874e4d6b</wsa:MessageID>
</soapenv:Header>
<soapenv:Body />
</soapenv:Envelope>
```

Verify if this looks as shown in the screenshot:

Click the Send button. The result returned confirms HCS mode.

Now, create a SOAP request to change the deployment type to Enterprise:

```
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ser="http://services.api.platform.vos.cisco.com">
<soapenv:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
<wsa:Action>urn:setDeploymentMode</wsa:Action>
<wsa:ReplyTo xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">
<wsa:Address>http://www.w3.org/2005/08/addressing/anonymous</wsa:Address>
</wsa:ReplyTo>
<wsa:MessageID>uuid:26634481-3273-4a70-b537-
ab4b874e4d6b</wsa:MessageID>
<wsa:To xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">
</wsa:To>
</soapenv:Header>
<soapenv:Body>
<ser:setDeploymentMode>
<ser:args0>Enterprise</ser:args0>
</ser:setDeploymentMode>
</soapenv:Body>
</soapenv:Envelope>
```

Verify if this looks as shown in the screenshot:

A successful result indicates request completed:

Restart the publisher node as the final step of the procedure.

### Revision History

1.0

22-Nov-2024

Initial Release

### Contributed by Cisco Engineers

Michal Myszor

Technical Consulting Engineer

### This Document Applies to These Products

- Hosted Collaboration Solution (HCS)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 22-Nov-2024 | Initial Release |