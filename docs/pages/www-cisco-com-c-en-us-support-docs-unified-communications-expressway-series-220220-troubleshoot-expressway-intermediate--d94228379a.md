---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-series-220220-troubleshoot-expressway-intermediate--d94228379a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway-series/220220-troubleshoot-expressway-intermediate-dig.html
retrieved_at: 2026-08-16T15:43:57.219697+00:00
---

Troubleshoot Expressway Intermediate DigiCert Global Root CA Certificate Expiry on March 8, 2023

# Troubleshoot Expressway Intermediate DigiCert Global Root CA Certificate Expiry on March 8, 2023

### Download Options

Updated: February 13, 2023

Document ID: 220220

Contents

## Contents

## Introduction

This document describes how to replace DigiCert Global Root CA which is set to expire on ‎‎Wednesday, ‎March ‎8, ‎2023. This means those devices that don’t trust "DigiCert Global Root CA" starts certificate warnings and TLS negotiations break on Wednesday, ‎March ‎8, ‎2023.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on Cisco Expressway x14.X.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

DigiCert Global Root CA intermediate CA is planned to expire on 08/Mar/2023. This is an intermediate certificate in the DigiCert certificate chain. Once it is expired, deployments break:

1. Mobile remote access.

1a. Expressway Core root and intermediate CAs are uploaded on Cisco Unified Communications Manager (CUCM) in order to perform Traffic server certificate validation. This TLS negotiation breaks post 08/Mar/2023 If intermediate CA is not updated.

1b. Traversal zone between Core and Expressway - Edge breaks if DigiCert certificates are uploaded on either.

## Troubleshoot Expressway Intermediate DigiCert Global Root CA Certificate Expiry on March ‎8, ‎2023

The " DigiCert Global Root CA " intermediate certificate expires on 08/Mar/2023 , which must be replaced with a certificate.

Name: DigiCert SHA2 Secure Server CA

Issuer: DigiCert Global Root CA Valid until: 08/Mar/2023 Serial #: 01:FD:A3:EB:6E:CA:75:C8:88:43:8B:72:4B:CF:BC:91

Updated new certificate:

Name: DigiCert SHA2 Secure Server CA

Issuer: DigiCert Global Root CA Valid until: 22/Sep/2030 Serial #: 02:74:2e:aa:17:ca:8e:21:c7:17:bb:1f:fc:fd:0c:a0

https://www.digicert.com/kb/digicert-root-certificates.htm

Please refer link to upload the CA certificate on Expressways; https://www.youtube.com/watch?v=aT73FQVDoDo or navigate to Maintenance > Security > Trusted CA certificate as shown in the image.

Refer document to upload the new expressway intermediate CA on CUCM; https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217748-upload-the-root-and-intermediate-certifi.html

### Revision History

1.0

13-Feb-2023

Initial Release

### Contributed by Cisco Engineers

Vikram Dutta

Cisco TAC Engineer

Manjunath Junnur

Cisco Technical Leader

### This Document Applies to These Products

- Expressway Series

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 13-Feb-2023 | Initial Release |