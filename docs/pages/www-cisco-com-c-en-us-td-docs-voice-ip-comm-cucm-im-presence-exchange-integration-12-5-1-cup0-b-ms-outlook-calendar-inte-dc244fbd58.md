---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-exchange-integration-12-5-1-cup0-b-ms-outlook-calendar-inte-dc244fbd58
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/exchange_integration/12_5_1/cup0_b_ms-outlook-calendar-integration-1251su2/cup0_b_ms-outlook-calender-integration-1251su2_chapter_0101.html
retrieved_at: 2026-08-16T17:28:04.575246+00:00
---

Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 12.5(1)SU2 to 12.5(1)SU8

# Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 12.5(1)SU2 to 12.5(1)SU8

Updated: August 3, 2023

Chapter: Configure Microsoft Office 365

## Chapter: Configure Microsoft Office 365

# Configure Microsoft Office 365

## Microsoft Office 365 Calendar Integration

You can configure the IM and Presence Service to integrate with a hosted Office 365 server for Microsoft Outlook calendaring
                              integration. When this feature is configured, the IM and Presence Service pulls user calendar information from the Office
                              365-hosted Microsoft Outlook and displays it as a part of an IM and Presence user's presence status. If the user's Outlook
                              indicates that the user is in a meeting that status displays in the user's presence status.

This integration has been tested successfully with 15,000 IM and Presence users system, where 5,000 users have a meeting at
                              the top of the hour.

## Microsoft Office 365 Calendar Integration Task Flow

Complete these tasks to configure your Microsoft Office 365 deployment for calendar integration between the IM and Presence
                              Service and Microsoft Outlook.

Upload Microsoft Certificates to IM and Presence Service

Download the Microsoft certificates that will be required for integration with the IM and Presence Service.

### Upload Microsoft Certificates to IM and Presence Service

For the IM and Presence Service and the Office 365 deployment to communicate, you must install the Microsoft certificates
                                 on the IM and Presence Service.

Step 1

Download an Office 365 root certificate, and intermediate certificate:

- The following site lists all of the root and intermediate certificates that Office 365 supports: https://support.office.com/en-us/article/office-365-certificate-chains-0c03e6b3-e73f-4316-9e2b-bf4091ae96bb

Step 2

Upload all certificates to the cup-trust and tomcat-trust stores on the IM and Presence Service.

For additional details on certificates with the IM and Presence Service, refer to the "Security Configuration on IM and Presence
                                             Service" chapter of the Configuration and Administration Guide for IM and Presence Service .

#### What to do next

Configure the IM and Presence Service

| Command or Action | Purpose |
|---|---|
| Upload Microsoft Certificates to IM and Presence Service | Download the Microsoft certificates that will be required for integration with the IM and Presence Service. |

| Step 1 | Download an Office 365 root certificate, and intermediate certificate: The following site lists all of the root and intermediate certificates that Office 365 supports: https://support.office.com/en-us/article/office-365-certificate-chains-0c03e6b3-e73f-4316-9e2b-bf4091ae96bb |
|---|---|
| Step 2 | Upload all certificates to the cup-trust and tomcat-trust stores on the IM and Presence Service. |

| Note | For additional details on certificates with the IM and Presence Service, refer to the "Security Configuration on IM and Presence
                                             Service" chapter of the Configuration and Administration Guide for IM and Presence Service . |
|---|---|