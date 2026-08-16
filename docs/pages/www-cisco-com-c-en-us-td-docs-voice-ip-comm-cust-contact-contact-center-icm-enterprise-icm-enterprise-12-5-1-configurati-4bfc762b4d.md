---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-4bfc762b4d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified12_5/ucce_b_serviceability-guide-for-cisco-unified12_5_chapter_01100.html
retrieved_at: 2026-08-16T14:50:18.851470+00:00
---

Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

# Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

Updated: July 26, 2022

Chapter: Cisco Identity Service Serviceability

## Chapter: Cisco Identity Service Serviceability

- Cisco Identity Service Serviceability

- Cisco Identity Service Logs

- Set up a Remote Syslog Server

# Cisco Identity Service Serviceability

## Cisco Identity Service Logs

The Cisco Identity Service generates logs, which you can view in the Real Time Monitoring Tool.

You set the level of logging you want by using Cisco Identity Service Management.

## Set up a Remote Syslog Server

To help in troubleshooting, you can  identify a remote Syslog server as a repository for receiving errors in Syslog format.

Step 1

In Unified CCE Administration, navigate to System > Single Sign-On .

Step 2

Click Identity Service Management .

Step 3

Enter your user name, and then click Next .

Step 4

Enter your password, and then click Sign In .

Step 5

Click Settings .

Step 6

From the Settings page, click Troubleshooting .

Step 7

To receive errors in Syslog format, enter the name of the Remote Syslog Server in the Host (Optional) field.

Step 8

Click Save .

| Step 1 | In Unified CCE Administration, navigate to System > Single Sign-On . |
|---|---|
| Step 2 | Click Identity Service Management . The Identity Service Management window opens. |
| Step 3 | Enter your user name, and then click Next . |
| Step 4 | Enter your password, and then click Sign In . The Cisco Identity Service Management page opens, showing the Nodes , Settings , and Clients icons in the left pane. |
| Step 5 | Click Settings . |
| Step 6 | From the Settings page, click Troubleshooting . |
| Step 7 | To receive errors in Syslog format, enter the name of the Remote Syslog Server in the Host (Optional) field. |
| Step 8 | Click Save . Note The remote syslog server setting applies across the cluster. | Note | The remote syslog server setting applies across the cluster. |
| Note | The remote syslog server setting applies across the cluster. |

| Note | The remote syslog server setting applies across the cluster. |
|---|---|