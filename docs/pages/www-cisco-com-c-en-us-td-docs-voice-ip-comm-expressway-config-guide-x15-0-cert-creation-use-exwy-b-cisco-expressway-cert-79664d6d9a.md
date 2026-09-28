---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-cert-creation-use-exwy-b-cisco-expressway-cert-79664d6d9a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/cert-creation-use/exwy_b_cisco-expressway-certificate-creation-and-use-deployment-guide-x150/exwy_m_decode-certificates.html
retrieved_at: 2026-08-16T15:13:51.080201+00:00
---

Cisco Expressway Certificate Creation and Use Deployment Guide (X15.0)

# Cisco Expressway Certificate Creation and Use Deployment Guide (X15.0)

Updated: July 5, 2024

Chapter: Decode Certificates

## Chapter: Decode Certificates

- Decode Certificates

# Decode Certificates

This section describes some methods to decode and view the content of certificates.

## OpenSSL

A PEM file (e.g. cert.pem ) can be decoded by the following command:

openssl x509 -text -in cert.pem

A DER file (e.g. cert.cer ) can be decoded by the following command:

openssl x509 -text –inform DER -in cert.cer

## Firefox

In Firefox, you can view the certificate in use for a website by clicking the Security Information button on the address bar, and then clicking More Information followed by View Certificate .

## Internet Explorer

In Internet Explorer, you can view the certificate in use for a website by clicking the lock icon to the right of the address
                           bar. A Website Identification dialog appears. Click the View Certificates link at the bottom.