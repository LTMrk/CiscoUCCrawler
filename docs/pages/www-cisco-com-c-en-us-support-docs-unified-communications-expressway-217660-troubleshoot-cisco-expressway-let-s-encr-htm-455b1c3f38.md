---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-217660-troubleshoot-cisco-expressway-let-s-encr-htm-455b1c3f38
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217660-troubleshoot-cisco-expressway-let-s-encr.html
retrieved_at: 2026-08-16T15:44:05.356044+00:00
---

Troubleshoot Expressway Let's Encrypt Revocation of SSL Certificates on Jan 28, 2022

# Troubleshoot Expressway Let's Encrypt Revocation of SSL Certificates on Jan 28, 2022

### Download Options

Updated: January 27, 2022

Document ID: 217660

Contents

## Contents

## Introduction

This document describes how to renew the Cisco Expressway Let's Encrypt revocation of Secure Sockets Layer (SSL) certificates on January 28th, 2022.

## Problem

When you start Expressway x 12.5, the Expressway supports certificate generation via the Automated Certificate Management Environment (ACME) Let's Encrypt.

There are irregularities found in Let's Encrypt's “certificate authority's implementation of "Transport Layer Security (TLS) with the use of the Application-Layer Protocol Negotiation (ALPN)" validation method”. To fix the detected irregularities, changes are implemented on Let's Encrypt site.

All active certificates that were issued and validated with the TLS-ALPN-01 challenge before 00:48 UTC on January 26th, 2022, when the fix was deployed, are considered mis-issued.

To comply with the Let's Encrypt Certificate Policy , which requires the certificate authority to invalidate a certificate within five days under certain conditions, the non-profit must begin to revoke certificates at 16:00 UTC on January 28th, 2022. If a notification email is configured on Expressway, then an email must have been received from ACME.

## Solution

On Expressway, renew the ACME certificate with reference to the procedure on the link. In case you notice a failure status on neighbor/Traversal Zones, call setup failures, or the Mobile and Remote Access (MRA) clients fail to log in.

## Related Information

- 2022.01.25 Issue with TLS-ALPN-01 Validation Method

- Let's Encrypt is revoking lots of SSL certificates in two days

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

26-Jan-2022

Initial Release

### Contributed by Cisco Engineers

Vikram Dutta

Cisco TAC Engineer

Sateesh Katukam

Cisco TAC Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Jan-2022 | Initial Release |