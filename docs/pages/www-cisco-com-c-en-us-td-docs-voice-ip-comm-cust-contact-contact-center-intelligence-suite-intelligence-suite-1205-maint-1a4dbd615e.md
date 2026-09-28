---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1205-maint-1a4dbd615e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1205/maintain_and_operate/guide/cuic_b_admin-console-user-guide-1205/cuic_b_admin-console-user-guide-1205_chapter_01010.html
retrieved_at: 2026-08-21T04:37:35.717028+00:00
---

Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.5(1)

# Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.5(1)

Updated: January 31, 2020

Chapter: Manage Certificates

## Chapter: Manage Certificates

- Manage Certificates

- Install Certificate Authority (CA) Certificate

- CUIC Server Certificates

# Manage Certificates

## Install Certificate Authority (CA) Certificate

To install or upload certificates on the Cisco Unified Intelligence Center server, perform the following steps:

Step 1

Log in to Cisco Unified Operating System Administration.

Step 2

Navigate to Security > Certificate Management . The Certificate List window appears.

Step 3

Click Generate CSR . The Generate Certificate Signing Request dialog box opens.

Step 4

Select tomcat from the Certificate Purpose list.

Step 5

Click Generate to generate a certificate from a custom or third-party certificate authority.

Step 6

Click Close .

Step 7

Click Download CSR .

Step 8

In the Download Certificate Signing Request screen, click Download CSR to download the Certificate Signing Request to your computer.

Step 9

Use this CSR to obtain the Public certificate and Primary certificate from the Certificate Authority.

Step 10

Log in to OS platform again and navigate to Security > Certificate Management .

Step 11

Click Upload Certificate/Certificate chain . The Upload Certificate/Certificate chain dialog box opens.

Step 12

To upload the certificate chain, select tomcat from the Certificate Purpose list.

Step 13

Select the file to upload. Click the Choose File button and navigate to the file; then, click Open .

Step 14

Click Upload .

Step 15

After successfully uploading the certificate, navigate to Security > Certificate Management .

Step 16

Click Find to open the list of certificates.

Step 17

Click on the uploaded certificate to view Certificate File Data .

Step 18

Restart the node(s) using the CLI command utils system restart .

To upload a custom certificate with alternate hostname, set the alternate hostname using the CLI command set web-security . Configure the alternate hostname and use the procedure above to generate Certificate Signing Request (CSR) and to upload
                                                the certificates. You can access Cisco Unified Intelligence Center by using the alternate hostname as well.

To avoid the certificate exception warning, you must access the servers using the Fully qualified domain name (FQDN) name.
                                                That is, leave the Distribution field in the CSR as the FQDN of the server.

Ensure that the Certificate Authority (CA) certificate is RSA-signed.

Cisco Unified Intelligence Center CSR certificates are signed with sha1WithRSAEncryption using a 2048-bit RSA public key.

Cisco Unified Intelligence Center does not support wildcard certificates.

## CUIC Server Certificates

Two server certificates — intelligencecenter-jms and intelligencecenter-srvr , even though available, are not used anymore. There is no impact even if these certificates expire, and it is not required
                           to regenerate them.

| Step 1 | Log in to Cisco Unified Operating System Administration. |
|---|---|
| Step 2 | Navigate to Security > Certificate Management . The Certificate List window appears. |
| Step 3 | Click Generate CSR . The Generate Certificate Signing Request dialog box opens. |
| Step 4 | Select tomcat from the Certificate Purpose list. |
| Step 5 | Click Generate to generate a certificate from a custom or third-party certificate authority. |
| Step 6 | Click Close . |
| Step 7 | Click Download CSR . |
| Step 8 | In the Download Certificate Signing Request screen, click Download CSR to download the Certificate Signing Request to your computer. |
| Step 9 | Use this CSR to obtain the Public certificate and Primary certificate from the Certificate Authority. |
| Step 10 | Log in to OS platform again and navigate to Security > Certificate Management . |
| Step 11 | Click Upload Certificate/Certificate chain . The Upload Certificate/Certificate chain dialog box opens. |
| Step 12 | To upload the certificate chain, select tomcat from the Certificate Purpose list. |
| Step 13 | Select the file to upload. Click the Choose File button and navigate to the file; then, click Open . |
| Step 14 | Click Upload . |
| Step 15 | After successfully uploading the certificate, navigate to Security > Certificate Management . |
| Step 16 | Click Find to open the list of certificates. |
| Step 17 | Click on the uploaded certificate to view Certificate File Data . |
| Step 18 | Restart the node(s) using the CLI command utils system restart . |

| Note | To upload a custom certificate with alternate hostname, set the alternate hostname using the CLI command set web-security . Configure the alternate hostname and use the procedure above to generate Certificate Signing Request (CSR) and to upload
                                                the certificates. You can access Cisco Unified Intelligence Center by using the alternate hostname as well. To avoid the certificate exception warning, you must access the servers using the Fully qualified domain name (FQDN) name.
                                                That is, leave the Distribution field in the CSR as the FQDN of the server. Ensure that the Certificate Authority (CA) certificate is RSA-signed. Cisco Unified Intelligence Center CSR certificates are signed with sha1WithRSAEncryption using a 2048-bit RSA public key. Cisco Unified Intelligence Center does not support wildcard certificates. |
|---|---|