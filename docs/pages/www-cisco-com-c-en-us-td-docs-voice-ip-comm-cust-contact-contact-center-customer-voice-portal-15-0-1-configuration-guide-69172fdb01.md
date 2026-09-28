---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-69172fdb01
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_150-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp-m-1501-tls-cipher-configuration.html
retrieved_at: 2026-08-21T02:59:18.571680+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: March 5, 2025

Chapter: TLS cipher Configuration

## Chapter: TLS cipher Configuration

# TLS Cipher Configuration

## Modifying Default TLS Cipher on CVP server

The sip.properties file in C:/cisco/CVP/conf folder carries the TLS ciphers for all CVP server interfaces.

To modify the default TLS cipher on CVP server, perform the following steps:

Step 1

Log in to the Operations Console and click Device Management > Unified CVP Call Server .

Step 2

Edit the call server record.

Step 3

Go to SIP > Advanced Configurations > Security Properties .

Step 4

Modify the Supported Ciphers field.

Step 5

Click Save & Deploy .

Step 6

Restart the Unified CVP server.

## Configuring TLS Cipher on OAMP Server

To configure TLS cipher on OAMP server, perform the following steps:

Step 1

Log in to the OAMP server.

Step 2

Navigate to C:\Cisco\CVP\conf folder.

Step 3

Open the sip-properties file.

Step 4

Edit the SIP.Secure.Ciphers property field.

Step 5

Click Save .

Step 6

Restart the OAMP server.

## Configuring TLS Cipher on Reporting Server

To configure TLS cipher on Reporting server, perform the following steps:

Step 1

Log in to the Reporting server.

Step 2

Navigate to C:\Cisco\CVP\conf folder.

Step 3

Open the sip-properties file.

Step 4

Edit the SIP.Secure.Ciphers property field.

Step 5

Click Save .

Step 6

Restart the Reporting server.

| Step 1 | Log in to the Operations Console and click Device Management > Unified CVP Call Server . |
|---|---|
| Step 2 | Edit the call server record. |
| Step 3 | Go to SIP > Advanced Configurations > Security Properties . |
| Step 4 | Modify the Supported Ciphers field. |
| Step 5 | Click Save & Deploy . |
| Step 6 | Restart the Unified CVP server. |

| Step 1 | Log in to the OAMP server. |
|---|---|
| Step 2 | Navigate to C:\Cisco\CVP\conf folder. |
| Step 3 | Open the sip-properties file. |
| Step 4 | Edit the SIP.Secure.Ciphers property field. |
| Step 5 | Click Save . |
| Step 6 | Restart the OAMP server. |

| Step 1 | Log in to the Reporting server. |
|---|---|
| Step 2 | Navigate to C:\Cisco\CVP\conf folder. |
| Step 3 | Open the sip-properties file. |
| Step 4 | Edit the SIP.Secure.Ciphers property field. |
| Step 5 | Click Save . |
| Step 6 | Restart the Reporting server. |