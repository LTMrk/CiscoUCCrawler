---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1261-admin-guide-cfin-b-1261-cis-f632de5597
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1261/admin/guide/cfin_b_1261-cisco-finesse-administration-guide/cfin_m_1261-certificates-for-cisco-identity-service.html
retrieved_at: 2026-08-21T16:00:16.372069+00:00
---

Cisco Finesse Administration Guide, Release 12.6(1)

# Cisco Finesse Administration Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Certificates for Cisco Identity Service

## Chapter: Certificates for Cisco Identity Service

- Certificates for Cisco Identity Service

- Export Cisco Identity Service Certificates

- Import Cisco IdS Certificates

# Certificates for Cisco Identity Service

## Export Cisco Identity Service Certificates

Step 1

Sign in to Cisco Unified Operating System Administration on the Cisco IdS server using the following URL: https:// hostname of Cisco IdS server: 8443 /cmplatform.

Step 2

Select Security > Certificate Management .

Step 3

Enter the search criteria as tomcat-trust and then click Find to filter the certificate.

The tomcat-trust certificates list is displayed. If you do not find the tomcat certificate for your server in the Certificate List , then click Generate Self-signed . When the certificate generation is complete, reboot your server. Then restart this procedure. For more information on generating
                                          the self-signed certificate, see Cisco Unified Operating System Administration Online Help .

Step 4

Click the tomcat-trust certificate hyperlink in the Common Name column.

Step 5

Click Download .PEM File .

Step 6

Save the .PEM file in your local machine.

### What to do next

Perform the same steps for both the primary and secondary Finesse nodes.

Import the Cisco IdS certificates into the Finesse trust store as tomcat-trust.

## Import Cisco IdS Certificates

Step 1

Sign in to Cisco Unified Operating System Administration on the Finesse server using the following URL: https:// FQDN of Finesse server: 8443 /cmplatform.

Step 2

Select Security > Certificate Management > Upload Certificate/Certificate chain .

Step 3

From the Certificate Purpose drop-down list, select tomcat-trust .

Step 4

In the Upload File field, click Choose File and browse to the tomcat.pem file that you saved on your system.

Step 5

Click Upload .

Step 6

Reboot the Cisco Finesse node.

Perform the same steps for both the primary and secondary Finesse nodes.

| Step 1 | Sign in to Cisco Unified Operating System Administration on the Cisco IdS server using the following URL: https:// hostname of Cisco IdS server: 8443 /cmplatform. |
|---|---|
| Step 2 | Select Security > Certificate Management . |
| Step 3 | Enter the search criteria as tomcat-trust and then click Find to filter the certificate. The tomcat-trust certificates list is displayed. If you do not find the tomcat certificate for your server in the Certificate List , then click Generate Self-signed . When the certificate generation is complete, reboot your server. Then restart this procedure. For more information on generating
                                          the self-signed certificate, see Cisco Unified Operating System Administration Online Help . |
| Step 4 | Click the tomcat-trust certificate hyperlink in the Common Name column. The tomcat Certificate Details dialog box is displayed. |
| Step 5 | Click Download .PEM File . |
| Step 6 | Save the .PEM file in your local machine. |

| Step 1 | Sign in to Cisco Unified Operating System Administration on the Finesse server using the following URL: https:// FQDN of Finesse server: 8443 /cmplatform. |
|---|---|
| Step 2 | Select Security > Certificate Management > Upload Certificate/Certificate chain . |
| Step 3 | From the Certificate Purpose drop-down list, select tomcat-trust . |
| Step 4 | In the Upload File field, click Choose File and browse to the tomcat.pem file that you saved on your system. |
| Step 5 | Click Upload . |
| Step 6 | Reboot the Cisco Finesse node. Note Perform the same steps for both the primary and secondary Finesse nodes. | Note | Perform the same steps for both the primary and secondary Finesse nodes. |
| Note | Perform the same steps for both the primary and secondary Finesse nodes. |

| Note | Perform the same steps for both the primary and secondary Finesse nodes. |
|---|---|