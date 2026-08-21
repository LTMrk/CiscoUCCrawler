---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-security-html-50a6f2ed9f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/security.html
retrieved_at: 2026-08-21T23:39:12.399368+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: About Security for Cisco Unified SRST Manager

## Chapter: About Security for Cisco Unified SRST Manager

- About Security

- About Security Certificates

- Retrieving Security Certificates from Cisco Unified Communications Manager

## About Security

Security certificates are required to provide a secure connection between systems. Security is needed for the following:

- Between Cisco Unified Communications Manager and Cisco Unified SRST Manager

- Between Cisco Unified SRST Manager and the Cisco Unified SRST or CUCME device at the branch site

## About Security Certificates

Use one of these methods to generate and sign security certificates:

- Trust chains. Trust chains use Certificate Authorities (CAs) to simplify large deployments. Install security certificates for the Cisco Unified Communications Manager and Cisco Unified SRST Manager that were all signed by a CA and the connections are all part of a trusted chain.

- Self-signed certificates. Use self-signed certificates for each device. In this case, Cisco Unified SRST Manager needs the security certificate from each device to which it connects.

The TLS security certificate can be represented in one of two formats: distinguished encoding rules (DER) and privacy-enhanced mode (PEM).

## Retrieving Security Certificates from Cisco Unified Communications Manager

Note Use this method to retrieve the certificates from the Cisco Unified Communications Manager system. You will later add this certificate to the Cisco Unified SRST Manager system.

Step 1 Log in to the Cisco Unified OS Administration interface.

Step 2 Select Security > Certificate Management .

Step 3 Click Find to show the certificates.

Step 4 Click the *.pem or *.der link for the desired certificate.

Step 5 Click Download to save the certificate to the local file system.