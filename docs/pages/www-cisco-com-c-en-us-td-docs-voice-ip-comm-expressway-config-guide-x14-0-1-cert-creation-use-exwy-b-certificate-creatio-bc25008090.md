---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-1-cert-creation-use-exwy-b-certificate-creatio-bc25008090
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0-1/cert_creation_use/exwy_b_certificate-creation-and-use-deployment-guide-x1401/exwy_b_certificate-creation-use-deployment-guide_chapter_01011.html
retrieved_at: 2026-08-16T15:24:42.349970+00:00
---

Cisco Expressway Certificate Creation and Use Deployment Guide (X14.0.1)

# Cisco Expressway Certificate Creation and Use Deployment Guide (X14.0.1)

Updated: July 1, 2021

Chapter: Decode Certificates

## Chapter: Decode Certificates

- Decode Certificates

- Decode Certificates

# Decode Certificates

## Decode Certificates

This section describes some methods to decode and view the content of certificates.

### OpenSSL

A PEM file (e.g. cert.pem ) can be decoded by the following command:

openssl x509 -text -in cert.pem

A DER file (e.g. cert.cer ) can be decoded by the following command:

openssl x509 -text –inform DER -in cert.cer

### Firefox

In Firefox, you can view the certificate in use for a website by clicking the Security Information button on the address bar, and then clicking More Information followed by View Certificate .

### Internet Explorer

In Internet Explorer, you can view the certificate in use for a website by clicking the lock icon to the right of the address
                              bar. A Website Identification dialog appears. Click the View Certificates link at the bottom.