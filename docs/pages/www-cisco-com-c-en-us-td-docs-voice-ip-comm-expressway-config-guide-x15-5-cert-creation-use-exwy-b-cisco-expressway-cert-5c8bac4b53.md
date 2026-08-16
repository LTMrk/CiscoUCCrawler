---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-5-cert-creation-use-exwy-b-cisco-expressway-cert-5c8bac4b53
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-5/cert-creation-use/exwy_b_cisco-expressway-certificate-creation-and-use-deployment-guide-x155/exwy_m_convert-a-der-certificate-file.html
retrieved_at: 2026-08-16T15:10:33.706349+00:00
---

Cisco Expressway Certificate Creation and Use Deployment Guide (X15.5)

# Cisco Expressway Certificate Creation and Use Deployment Guide (X15.5)

Updated: July 29, 2026

Chapter: Convert a DER Certificate File to PEM Format

## Chapter: Convert a DER Certificate File to PEM Format

- Convert a DER Certificate File to PEM Format

# Convert a DER Certificate File to PEM Format

A private key, root (CA) certificate and the server / client certificate can be generated using third-party tools (or purchased
                        from a certificate authority), and may be generated as PEM (required format, extension .pem) or DER (extension .cer) format
                        files.

Certificates must be in PEM format for use on the Expressway. Conversion from DER to PEM format is done either using OpenSSL
                        or Windows, as documented in the following sections.

## Convert a DER certificate file to a PEM file using OpenSSL

To convert from DER to PEM format, on a system running openssl, execute the command:

openssl x509 -in <filename>.cer -inform DER -out <filename>.pem -outform PEM

## Convert a DER certificate file to a PEM file using Microsoft Windows

To convert from DER to PEM format using Microsoft Windows:

Double click the DER file to convert (this will likely have a ‘.cer’ extension)

Select the Details tab

Click Copy to File…

On the Welcome page, click Next

Select Base-64 encoded X.509 (.CER) and click Next

Click Browse and select required destination for file (e.g. server.pem ) and then click Next

Click Finish

Change the filename from server.pem.cer to server.pem

This is used in the Load Certificates and Keys Onto Expressway section of this document.