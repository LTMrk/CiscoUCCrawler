---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-5-exwy-b-certificate-creation-use-deployment-gui-a919152a35
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-5/exwy_b_certificate-creation-use-deployment-guide/exwy_b_certificate-creation-use-deployment-guide_chapter_01101.html
retrieved_at: 2026-08-16T15:37:43.423764+00:00
---

Cisco Expressway Certificate Creation And Use Deployment Guide (X12.5)

# Cisco Expressway Certificate Creation And Use Deployment Guide (X12.5)

Updated: December 4, 2019

Chapter: Authorize a Request and Generate a Certificate Using Microsoft Certification Authority

## Chapter: Authorize a Request and Generate a Certificate Using Microsoft Certification Authority

- Authorize a Request and Generate a Certificate Using Microsoft Certification Authority

- Authorize a Request and Generate Certificate using Microsoft Certificate Authority

# Authorize a Request and Generate a Certificate Using Microsoft Certification Authority

## Authorize a Request and Generate Certificate using Microsoft Certificate Authority

This section describes how to authorize a certificate request and generate a PEM certificate file using Microsoft Certification
                           Authority.

The CA component of Microsoft Active Directory Certificate Services (AD CS) must be able to issue a certificate that can be
                                       used for authentication of the Expressway as client or server.

AD CS in Windows Server 2008 Standard R2 (and later) can issue these types of certificates, if you create a certificate template
                           for them. Earlier versions of Windows Server Standard Edition are not suitable .

Copy the certificate request file (for example, certcsr.der if generated via OpenSSL) to a location, such as the desktop, on the server where the Microsoft Certification Authority application
                                 is installed.

Submit the certificate request from a command prompt:

To generate a certificate with Server Authentication and Client Authentication, which is required if you want to configure
                                       a neighbor or traversal zone with mutual authentication (TLS verify mode), type:

certreq -submit -attrib "CertificateTemplate:Webclientandserver"

C:\Users\<user>\Desktop\certcsr.der

See Appendix 5: Enable AD CS to Issue "Client and Server" Certificates for details about how to set up the Webclientandserver certificate template.

To generate a certificate with Server Authentication only, type:

certreq -submit -attrib "CertificateTemplate:WebServer" C:\Users\<user>\Desktop\certcsr.der

This triggers the Certification Authority window to open:

The command must be run as the administrator user.

Select the Certification Authority to use (typically only one is offered) and click OK .

When requested, save the certificate (browse to the required folder if the default Libraries > Documents folder is not to be used) calling it server.cer for example.

Rename server.cer to server.pem for use with the Expressway.

### Get the Microsoft CA certificate

In your web browser, go to <IP or URL of the Microsoft Certificate Server>/certsrv and log in.

Select Download a CA certificate, certificate chain or CRL

Select the option Base 64 under Encoding method .

Click Download CA certificate link.

Choose Save File and click OK .

Rename certnew.cer to certnew.pem .

Files server.pem and certnew.pem are now available.

Go to the Load Certificates and Keys Onto Expressway section in this document to know how to upload server.pem and certnew.pem to Expressway.

| Note | The CA component of Microsoft Active Directory Certificate Services (AD CS) must be able to issue a certificate that can be
                                       used for authentication of the Expressway as client or server. |
|---|---|

| Note | The command must be run as the administrator user. |
|---|---|