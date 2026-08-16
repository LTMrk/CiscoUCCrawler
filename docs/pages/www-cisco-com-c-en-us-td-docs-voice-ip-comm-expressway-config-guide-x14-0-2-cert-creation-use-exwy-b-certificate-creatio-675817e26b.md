---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-2-cert-creation-use-exwy-b-certificate-creatio-675817e26b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0-2/cert_creation_use/exwy_b_certificate-creation-and-use-deployment-guide-x1402/exwy_b_certificate-creation-use-deployment-guide_chapter_01100.html
retrieved_at: 2026-08-16T15:23:27.050688+00:00
---

Cisco Expressway Certificate Creation and Use Deployment Guide (X14.0.2)

# Cisco Expressway Certificate Creation and Use Deployment Guide (X14.0.2)

Updated: July 23, 2021

Chapter: Enable AD CS to Issue "Client and Server" Certificates

## Chapter: Enable AD CS to Issue "Client and Server" Certificates

- Enable AD CS to Issue "Client and Server" Certificates

- Enable AD CS to Issue "Client and Server" Certificates

# Enable AD CS to Issue "Client and Server" Certificates

## Enable AD CS to Issue "Client and Server" Certificates

The CA component of Microsoft Active Directory Certificate Services (AD CS) must be able to issue a certificate that can be
                                          used for authentication of the Expressway as client or server.

AD CS in Windows Server 2008 Standard R2 (and later) can issue these types of certificates, if you create a certificate template
                              for them. Earlier versions of Windows Server Standard Edition are not suitable.

The default "Web Server" certificate template in AD CS creates a certificate for Server Authentication. The server certificate
                              for the Expressway also needs Client Authentication if you want to configure a neighbor or traversal zone with mutual authentication
                              (where TLS verify mode is enabled).

To set up a certificate template with both Server and Client authentication:

In Windows, launch Server Manager ( Start > Administrative Tools > Server Manager ).

(Server Manager is a feature included with server editions of Windows.)

Expand the Server Manager navigation tree to Roles > Active Directory Certificate Services > Certificate Templates (<domain>) .

Right-click on Web Server and select Duplicate Template .

Select Windows Server 2003 Enterprise and click OK .

On the General tab, enter the Template display name and Template name , for example Web client and server and Webclientandserver .

On the Extensions tab, select Application Policies and click Edit .

Add Client Authentication to the set of application policies:

Click Add

Select Client Authentication and click OK

Click OK

Click OK to complete the addition of the new template.

Add the new template to the Certificate Authority:

Go to Roles > Active Directory Certificate Services > <your certificate authority> .

Right-click Certificate Templates and select New > Certificate Template to Issue

Select your new Web client and server template and click OK .

The new Web client and server template can now be used when submitting a certificate request to the Microsoft Certification Authority.

| Note | The CA component of Microsoft Active Directory Certificate Services (AD CS) must be able to issue a certificate that can be
                                          used for authentication of the Expressway as client or server. |
|---|---|