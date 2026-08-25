---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-ef0cb3d545
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_010001.html
retrieved_at: 2026-08-25T21:46:46.987278+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: February 11, 2016

Chapter: Troubleshooting

## Chapter: Troubleshooting

- Update the SSO Certificate for the Cisco Jabber Domain

# Troubleshooting

## Update the SSO Certificate for the Cisco Jabber Domain

This procedure applies to cloud or hybrid deployments. Use this procedure to upload  an updated single sign-on (SSO) certificate for your Cisco Jabber domain.

Only certificates with 1024, 2048, or 4096 encryption bits and RC4-MD5 algorithms are supported.

The certificate must be in a .CER or .CRT file format.

| Note | Only certificates with 1024, 2048, or 4096 encryption bits and RC4-MD5 algorithms are supported. |
|---|---|

| Step 1 | Log in to the WebEx Org Admin tool at https:/​/​www.webex.com/​go/​connectadmin . |
|---|---|
| Step 2 | After loading the Administration tool, click the Configuration tab. |
| Step 3 | In the left navigation bar, click on Security Settings . |
| Step 4 | Click the link for Organization Certificate Management . Previously imported X.509 certificates are displayed. |
| Step 5 | In the Alias field, enter your company's Cisco WebEx Organization. |
| Step 6 | Click Browse to navigate to the X.509 certificate. The certificate must be in a .CER or .CRT file format. |
| Step 7 | Click Import to import the certificate. If the certificate is not according to the format specified for an X.509 certificate, an error is  displayed. |
| Step 8 | Click Close twice to return to the SSO Related Options screen. |
| Step 9 | Click Save to save your Federated Web single sign-on configuration details. |