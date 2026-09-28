---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-release-guide-uccx-b-1251-ea08a071cb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/release/guide/uccx_b_1251su2_solution-release-notes/uccx_b_1252solution-release-notes_chapter_0100.html
retrieved_at: 2026-08-16T21:00:54.436244+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU2

# Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU2

Updated: April 11, 2022

Chapter: Cisco Customer Collaboration Platform

## Chapter: Cisco Customer Collaboration Platform

# Cisco Customer Collaboration Platform

## New Features

### VPN-less Access to Finesse Desktop

This feature provides the flexibility for agents and supervisors to access the Finesse desktop from anywhere through the Internet
                              without requiring VPN connectivity. To enable this feature, a reverse-proxy pair must be deployed in the DMZ.

When deployed with VPN-less reverse-proxy, Customer Collaboration Platform can be deployed within the DMZ or can be moved
                              within the enterprise.

For more information on this feature, see the VPN-less Access to Finesse Desktop sections in the following guides:

Solution Design Guide for Cisco Unified Contact Center Express at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-implementation-design-guides-list.html

Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html

### ECDSA Certificate Support

Elliptic Curve Digital Signature Algorithm (ECDSA) offers a variant of the Digital Signature Algorithm (DSA) which uses elliptic
                              curve cryptography. ECDSA is an alternate algorithm to RSA.

Customer Collaboration Platform now supports ECDSA and you can make it the default signature algorithm.

For details on how to enable ECDSA, see the show and set commands in the Command Line Interface in Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html

WxM does not support Elliptic Curve (EC) certificates.

## Updated Features

None.

## Important Notes

After upgrading Customer Collaboration Platform, the CAs that are not approved by Cisco are removed from the platform trust
                           store. However, you can add them back, if necessary.

For information about the list of CAs that Cisco supports, see Cisco Trusted External Root Bundle section in https://www.cisco.com/security/pki

For information about adding a certificate, see the Customer Collaboration Platform Configurations section in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html

## Deprecated Features

None.

## Removed and Unsupported Features

The standalone Customer Collaboration Platform features such as Facebook page, Twitter, RSS Feeds, Standalone single session
                           chat, associated features like filters and notifications have been removed.

## Third Party Software Impacts

None.

| Note | WxM does not support Elliptic Curve (EC) certificates. |
|---|---|