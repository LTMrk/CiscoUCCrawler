---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-admin-guide-cfin-b-150-cisc-a6c3325055
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/admin/guide/cfin_b_150_cisco-finesse-administration-guide/cfin_m_150_certificates-for-live-data.html
retrieved_at: 2026-08-21T12:05:25.240845+00:00
---

Cisco Finesse Administration Guide, Release 15.0(1)

# Cisco Finesse Administration Guide, Release 15.0(1)

Updated: December 12, 2025

Chapter: Certificates for Live Data

## Chapter: Certificates for Live Data

# Certificates for Live Data

## Certificates and Secure Communications

For secure Cisco Finesse, Cisco Unified Intelligence Center, AWDB, and Live Data server-to-server communication, perform any of the following:

Use the self-signed certificates provided with Live Data.

When using self-signed certificates, agents must accept the Live Data certificates in the Finesse desktop when they sign in
                                             before they can use the Live Data gadget.

Obtain and install a Certification Authority (CA) certificate from a third-party vendor.

Produce a Certification Authority (CA) certificate internally.

After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. You can add
                                       them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki .

For information about adding a certificate, see Insert a new tomcat-trust certificate .

## Export Self-Signed Live Data Certificates

Live Data installation includes the generation of self-signed certificates. If you choose to work with these self-signed
                              certificates (rather than producing your own CA certificate or obtaining a CA certificate from a third-party certificate vendor),
                              first export the certificates from Live Data and Cisco Unified Intelligence Center. You must export from both Side A and Side
                              B of the Live Data and Cisco Unified Intelligence Center servers. Once done, import the certificates into Finesse, importing
                              both Side A and Side B certificates into each side of the Finesse servers.

When using other self-signed certificates, agents must accept the Live Data certificates in the Finesse desktop when they
                              sign in to use the Live Data gadget.

Step 1

Sign in to Cisco Unified Operating System Administration on the Live Data server using the following URL: https :// hostname of Live Data server /cmplatform.

Step 2

From the Security menu, choose Certificate Management .

Step 3

Click Find .

Step 4

Perform one of the following:

If the tomcat-trust certificate for your server is not on the list, click Generate New . When the certificate generation is complete, reboot your server. Then restart this procedure.

If the tomcat-trust certificate for your server is on the list, click the certificate to select it. (Ensure that the certificate
                                                you select includes the hostname for the server.)

Step 5

Click Download .PEM File and save the file to your desktop.

Perform these steps for both Side A and Side B.

Step 6

After you have downloaded the Live Data certificates, sign in to Cisco Unified Operating System Administration on the Cisco
                                       Unified Intelligence Center server using the following URL: https :// hostname of CUIC server /cmplatform, and repeat steps 2 to 5.

### What to do next

Import the Live Data and Cisco Unified Intelligence Center certificates into the Finesse servers.

## Import Self-Signed Live Data Certificates

To import the certificates into the Finesse servers, use the following procedure:

Step 1

Sign in to Cisco Unified Operating System Administration on the Finesse server using the following URL:

https :// FQDN of Finesse server :8443/cmplatform

Step 2

From the Security menu, choose Certificate Management .

Step 3

Click Upload Certificate .

Step 4

From the Certificate Name drop-down list, choose tomcat-trust .

Step 5

Click Browse and browse to the location of the Live Data or Cisco Unified Intelligence Center certificate (with the .pem file extension).

Step 6

Select the file, and click Upload File .

Step 7

Repeat steps 3 to 6 for the remaining unloaded certificate.

Step 8

Reboot the Cisco Finesse server to apply the certificate changes.

### What to do next

Perform these steps for both Side A and Side B.

## Obtain and Upload Third-party CA Certificate

You can use a Certification Authority (CA) certificate provided by a third-party vendor to establish an HTTPS connection between
                              the Live Data, Finesse, and Cisco Unified Intelligence Center servers.

To use third-party CA certificates:

From the Live Data servers, generate and download Certificate Signing Requests (CSR) for root and application certificates.

Obtain root and application certificates from the third-party vendor.

Upload the appropriate certificates to the Live Data, Unified Intelligence Center, and Finesse servers.

Follow the instructions provided in the Unified CCE Solution: Procedure to Obtain and Upload Third-Party CA certificates (Version 11.x) technical note at : https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-enterprise-1101/200286-Unified-CCE-Solution-Procedure-to-Obtai.html .

| Note | When using self-signed certificates, agents must accept the Live Data certificates in the Finesse desktop when they sign in
                                             before they can use the Live Data gadget. |
|---|---|

| Note | After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. You can add
                                       them back, if necessary. For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle at https://www.cisco.com/security/pki . For information about adding a certificate, see Insert a new tomcat-trust certificate . |
|---|---|

| Step 1 | Sign in to Cisco Unified Operating System Administration on the Live Data server using the following URL: https :// hostname of Live Data server /cmplatform. |
|---|---|
| Step 2 | From the Security menu, choose Certificate Management . |
| Step 3 | Click Find . |
| Step 4 | Perform one of the following: If the tomcat-trust certificate for your server is not on the list, click Generate New . When the certificate generation is complete, reboot your server. Then restart this procedure. If the tomcat-trust certificate for your server is on the list, click the certificate to select it. (Ensure that the certificate
                                                you select includes the hostname for the server.) |
| Step 5 | Click Download .PEM File and save the file to your desktop. Perform these steps for both Side A and Side B. |
| Step 6 | After you have downloaded the Live Data certificates, sign in to Cisco Unified Operating System Administration on the Cisco
                                       Unified Intelligence Center server using the following URL: https :// hostname of CUIC server /cmplatform, and repeat steps 2 to 5. |

| Step 1 | Sign in to Cisco Unified Operating System Administration on the Finesse server using the following URL: https :// FQDN of Finesse server :8443/cmplatform |
|---|---|
| Step 2 | From the Security menu, choose Certificate Management . |
| Step 3 | Click Upload Certificate . |
| Step 4 | From the Certificate Name drop-down list, choose tomcat-trust . |
| Step 5 | Click Browse and browse to the location of the Live Data or Cisco Unified Intelligence Center certificate (with the .pem file extension). |
| Step 6 | Select the file, and click Upload File . |
| Step 7 | Repeat steps 3 to 6 for the remaining unloaded certificate. |
| Step 8 | Reboot the Cisco Finesse server to apply the certificate changes. |