---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-telepresence-video-communication-server-expressway-226221-unde-a4d7a5a914
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/telepresence-video-communication-server-expressway/226221-understand-effect-of-godaddy-root.html
retrieved_at: 2026-09-14T20:03:08.694504+00:00
---

Understand Effect of GoDaddy Root Migration on Expressway MRA

# Understand Effect of GoDaddy Root Migration on Expressway MRA

### Download Options

Updated: August 5, 2026

Document ID: 226221

Contents

## Contents

## Introduction

This document describes the effect of migrating the GoDaddy root certificate from G2 to (R1 + R1V1).

## Background

GoDaddy is transitioning from the Old Root (G2) policy to the new R1 root certificate chain. N ew certificates must include only the Server Authentication EKU.

This transition affects expressways and other edge products who have installed Good daddy certificates.

The roots transition takes place due to:

- G2 signing/issuing intermediates do not have any EKU listed, which makes that hierarchy out of compliance with the Chrome Root Program requirement. As a result, issuance from the affected G2 intermediates must stop by that date.

- No EKU means all purposes are served by certificate.

## Certificate Specifics

### Old Root

CN: GoDaddy Root Certificate Authority - G2

Expiry ‎Friday, ‎January ‎1, ‎2038 5:29:59 AM

SN           00

This old root is replaced by the new root R1.

### New Root

CN = GoDaddy TLS Root CA – R1

Expiry ‎Friday, ‎August ‎24, ‎2040 5:29:59 PM

SN 00da62ff9e2619b1257a4809368ee8e3f7

The new R1 root signs the new intermediate as outlined in the next sections.

### New Intermediate

CN = GoDaddy TLS Intermediate CA DV - R1v1

Expiry ‎Friday, ‎August ‎24, ‎2040 5:29:59 PM

SN 008aaa80515c0bc688c7955d70f27758ac

OS trust stores which have old G2 root , wont trust new chain of certs (R1 + R1V1) for this purpose GoDaddy has created a cross – sign trust path, where

new R1 root certificate trusts old G2 root certificate.

### Cross Sign Certificate

CN = GoDaddy TLS Root CA - R1

‎Expiry Friday, ‎January ‎1, ‎2038 5:29:59 AM

SN 0090de6c7fb3b50b3c0617724fc13402ad

If you do not have correct chain installed, or you only have new chain (R1 + R1v1) installed on Expressway Trust store, MRA  IP phone registration stalls.

The error seen in expressway Pcap is an unknown CA coming from an IP phone. You can assume there is a missing CA on the IP phone trust store.

88xx ip phone 135.x.x.25

172.x.x.34   Expressway

There is also e a situation where the Expressway trust store does not accept the cross-sign certificate because the new root certificate and cross sign certificate have same CN name, as in CN = GoDaddy TLS Root CA - R1.

If this is the case:

1. Do not delete New Root R1 certificate SN 00da62ff9e2619b1257a4809368ee8e3f7.

2. Upload Cross sign certificate SN 0090de6c7fb3b50b3c0617724fc13402ad CN = GoDaddy TLS Root CA - R1.

### Certificate Tree ( New to Old)

## Important Files

The leaf certificate is issued under the R1 DV issuing CA, but clients validate it by building a chain to GoDaddy Class 2 Root – G2 using the published R1→G2 cross certificate. The relevant artifacts in the repository are the G2 trust anchor ( gdroot-g2 ), the cross certificate ( gd_tls_root-r1-cross-g2 ), the R1 DV issuing intermediate ( gd_tls_issuing_dv-r1v1 ), and the native hierarchy root ( gd_tls_root-r1 ) certs.godaddy.com. This cross-sign approach allows browsers to validate the chain today (anchoring at G2), while R1 trust propagates over time.

## Related Information

Details on transitioning from the old root to new root are documented here:

- Why is GoDaddy removing ClientAuth EKU and transitioning to the R1 root hierarchy for DV TLS issuance?

In case you encounter this issue, here is the Godaddy repository to download certificate:

- GoDaddy Repository

### Revision History

1.0

05-Aug-2026

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Aug-2026 | Initial Release |