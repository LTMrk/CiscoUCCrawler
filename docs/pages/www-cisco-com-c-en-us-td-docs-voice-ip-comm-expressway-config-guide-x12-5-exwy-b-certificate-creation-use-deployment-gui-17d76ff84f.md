---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-5-exwy-b-certificate-creation-use-deployment-gui-17d76ff84f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-5/exwy_b_certificate-creation-use-deployment-guide/exwy_b_certificate-creation-use-deployment-guide_chapter_01010.html
retrieved_at: 2026-08-16T15:37:31.095948+00:00
---

Cisco Expressway Certificate Creation And Use Deployment Guide (X12.5)

# Cisco Expressway Certificate Creation And Use Deployment Guide (X12.5)

Updated: December 4, 2019

Chapter: Convert a DER Certificate File to PEM Format

## Chapter: Convert a DER Certificate File to PEM Format

- Convert a DER Certificate File to PEM Format

- Convert a DER Certificate File to PEM Format

# Convert a DER Certificate File to PEM Format

## Convert a DER Certificate File to PEM Format

A private key, root (CA) certificate and the server / client certificate can be generated using third-party tools (or purchased
                           from a certificate authority), and may be generated as PEM (required format, extension .pem) or DER (extension .cer) format
                           files.

Certificates must be in PEM format for use on the Expressway. Conversion from DER to PEM format is done either using OpenSSL
                           or Windows, as documented in the following sections.

### Convert a DER certificate file to a PEM file using OpenSSL

To convert from DER to PEM format, on a system running openssl, execute the command:

openssl x509 -in <filename>.cer -inform DER -out <filename>.pem -outform PEM

### Convert a DER certificate file to a PEM file using Microsoft Windows

To convert from DER to PEM format using Microsoft Windows:

Double click the DER file to convert (this will likely have a ‘.cer’ extension)

Select the Details tab

Click Copy to File…

On the Welcome page, click Next

Select Base-64 encoded X.509 (.CER) and click Next

Click Browse and select required destination for file (e.g. server.pem ) and then click Next

Click Finish

Change the filename from server.pem.cer to server.pem

This is used in the Load Certificate and Keys Onto Expressway section of this document.