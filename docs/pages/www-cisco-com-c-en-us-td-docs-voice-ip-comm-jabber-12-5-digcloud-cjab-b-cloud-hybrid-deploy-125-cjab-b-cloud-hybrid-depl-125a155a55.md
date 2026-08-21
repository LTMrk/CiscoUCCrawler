---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-5-digcloud-cjab-b-cloud-hybrid-deploy-125-cjab-b-cloud-hybrid-depl-125a155a55
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_5/DIGCloud/cjab_b_cloud-hybrid-deploy-125/cjab_b_cloud-hybrid-deploy-125_chapter_010011.html
retrieved_at: 2026-08-21T21:13:41.868241+00:00
---

Cloud and Hybrid Deployments for Cisco Jabber 12.5

# Cloud and Hybrid Deployments for Cisco Jabber 12.5

Updated: April 1, 2024

Chapter: Troubleshooting

## Chapter: Troubleshooting

- Troubleshooting

- Update the SSO Certificate for the Cisco Jabber Domain

- Cisco Jabber Diagnostics Tool

# Troubleshooting

## Update the SSO Certificate for the Cisco Jabber Domain

This procedure applies to cloud or hybrid deployments. Use this procedure to upload  an updated single sign-on (SSO) certificate
                              for your Cisco Jabber domain.

Only certificates with 1024, 2048, or 4096 encryption bits and RC4-MD5 algorithms are supported.

### Before you begin

The certificate must be in a .CER or .CRT file format.

Step 1

Log in to the Webex Org Admin tool at https://www.webex.com/go/connectadmin .

Step 2

After loading the Administration tool, click the Configuration tab.

Step 3

In the left navigation bar, click on Security Settings .

Step 4

Click the link for Organization Certificate Management .

Step 5

In the Alias field, enter your company's Webex Organization.

Step 6

Click Browse to navigate to the X.509 certificate.

Step 7

Click Import to import the certificate.

Step 8

Click Close twice to return to the SSO Related Options screen.

Step 9

Click Save to save your Federated Web single sign-on configuration details.

## Cisco Jabber Diagnostics Tool

### Windows and Mac

Service Discovery

- Webex

Cisco Unified Communications Manager Summary

Cisco Unified Communications Manager Configuration

Voicemail

Certificate Validation

Active Directory

DNS Records

To access the Cisco Jabber Diagnostics Tool window, users must bring the hub window into focus and enter Ctrl + Shift + D .  Users can update the data by clicking the Reload button. Users can also save the information to an html file by clicking the Save button.

The Cisco Jabber Diagnostics Tool is available by default. To disable this tool, you must set the DIAGNOSTICS_TOOL_ENABLED
                              installation parameter to FALSE.  For more information about this installation parameter, see On-Premise Deployment for Cisco Jabber , or Cloud and Hybrid Deployments for Cisco Jabber , depending on your setup.

| Note | Only certificates with 1024, 2048, or 4096 encryption bits and RC4-MD5 algorithms are supported. |
|---|---|

| Step 1 | Log in to the Webex Org Admin tool at https://www.webex.com/go/connectadmin . |
|---|---|
| Step 2 | After loading the Administration tool, click the Configuration tab. |
| Step 3 | In the left navigation bar, click on Security Settings . |
| Step 4 | Click the link for Organization Certificate Management . Previously imported X.509 certificates are displayed. |
| Step 5 | In the Alias field, enter your company's Webex Organization. |
| Step 6 | Click Browse to navigate to the X.509 certificate. The certificate must be in a .CER or .CRT file format. |
| Step 7 | Click Import to import the certificate. If the certificate is not according to the format specified for an X.509 certificate, an error is  displayed. |
| Step 8 | Click Close twice to return to the SSO Related Options screen. |
| Step 9 | Click Save to save your Federated Web single sign-on configuration details. |