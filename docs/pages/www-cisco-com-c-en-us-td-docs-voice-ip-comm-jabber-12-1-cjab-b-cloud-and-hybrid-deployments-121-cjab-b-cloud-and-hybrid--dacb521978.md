---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-1-cjab-b-cloud-and-hybrid-deployments-121-cjab-b-cloud-and-hybrid--dacb521978
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_1/cjab_b_cloud-and-hybrid-deployments_121/cjab_b_cloud-and-hybrid-deployments_121_chapter_01111.html
retrieved_at: 2026-08-21T21:14:50.472944+00:00
---

Cloud and Hybrid Deployments for Cisco Jabber 12.1

# Cloud and Hybrid Deployments for Cisco Jabber 12.1

Updated: July 17, 2018

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

Log in to the Webex Org Admin tool at https://www.webex.com/go/connectadmin .

After loading the Administration tool, click the Configuration tab.

In the left navigation bar, click on Security Settings .

Click the link for Organization Certificate Management .

In the Alias field, enter your company's Cisco Webex Organization.

Click Browse to navigate to the X.509 certificate.

Click Import to import the certificate.

Click Close twice to return to the SSO Related Options screen.

Click Save to save your Federated Web single sign-on configuration details.

## Cisco Jabber Diagnostics Tool

### Windows and Mac

Service Discovery

- Cisco Webex

Cisco Unified Communications Manager Summary

Cisco Unified Communications Manager Configuration

Voicemail

Certificate Validation

Active Directory

DNS Records

To access the Cisco Jabber Diagnostics Tool window, users must bring the hub window into focus and enter Ctrl + Shift + D .  Users can update the data by clicking the Reload button. Users can also save the information to an html file by clicking the Save button.

The Cisco Jabber Diagnostics Tool is available by default. To disable this tool, you must set the DIAGNOSTICS_TOOL_ENABLED
                              installation parameter to FALSE.  For more information about this installation parameter, see On-Premise Deployment for Cisco Jabber , or Cloud and Hybrid Deployments for Cisco Jabber , depending on your setup.

### Android, iPhone, and iPad

If users are unable to sign into Cisco Jabber or your Cisco Jabber IM and Phone services aren’t connected, they can use the Diagnose Error option to check what’s causing the issue.

Users can tap Diagnose Error option either from the Sign In page or from the warning notification they get when connecting to Cisco Jabber services. Cisco Jabber then verifies:

If there are any network issues

If Cisco Jabber servers are reachable

If Cisco Jabber can reconnect

| Note | Only certificates with 1024, 2048, or 4096 encryption bits and RC4-MD5 algorithms are supported. |
|---|---|

| Step 1 | Log in to the Webex Org Admin tool at https://www.webex.com/go/connectadmin . |
|---|---|
| Step 2 | After loading the Administration tool, click the Configuration tab. |
| Step 3 | In the left navigation bar, click on Security Settings . |
| Step 4 | Click the link for Organization Certificate Management . Previously imported X.509 certificates are displayed. |
| Step 5 | In the Alias field, enter your company's Cisco Webex Organization. |
| Step 6 | Click Browse to navigate to the X.509 certificate. The certificate must be in a .CER or .CRT file format. |
| Step 7 | Click Import to import the certificate. If the certificate is not according to the format specified for an X.509 certificate, an error is  displayed. |
| Step 8 | Click Close twice to return to the SSO Related Options screen. |
| Step 9 | Click Save to save your Federated Web single sign-on configuration details. |