---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-exchange-integration-12-5-1-cup0-b-ms-outlook-calendar-inte-7504ef7aae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/exchange_integration/12_5_1/cup0_b_ms-outlook-calendar-integration-1251/cup0_b_ms-outlook-calender-integration-1251_chapter_0101.html
retrieved_at: 2026-08-16T17:27:21.494677+00:00
---

Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 12.5(1)

# Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 12.5(1)

Updated: January 23, 2019

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

Step 1

Configure Office 365 Permissions for Calendar Integration

Configure the Office 365 server with impersonation permissions to allow IM and Presence users to pull calendar information
                                          from Microsoft Outlook.

Step 2

Upload Microsoft Certificates to IM and Presence Service

Download the Microsoft certificates that will be required for integration with the IM and Presence Service.

### Configure Office 365 Permissions for Calendar Integration

Use this procedure on the Office 365 server to configure permissions for IM and Presence calendar integration. To integrate
                                 with the IM and Presence Service, you must assign the ApplicationImpersonation admin role for Discovery Management.

#### Before you begin

This procedure assumes that you have already set up your Office365 deployment. For Office365 configuration, see your Microsoft
                                 documentation.

Step 1

Log in to Office 365.

Step 2

Click the Admin icon

Step 3

In the left navigation bar, select the Admin Center tab (bottom left) and click Exchange .

Step 4

Under Permissions select Admin roles .

Step 5

Select Discovery Management .

Step 6

Click the Pencil icon to edit the role assignments.

Step 7

Add the ApplicationImpersonation role by doing the following:

Under Roles click + .

Select ApplicationImpersonation and click Add .

Click OK .

Step 8

Assign a user as a member of the ApplicationImpersonation role:

Under Members click + .

Select the user account that you want to add and click Add .

Click OK .

Step 9

Click Save .

#### What to do next

Upload Microsoft Certificates to IM and Presence Service

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

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Office 365 Permissions for Calendar Integration | Configure the Office 365 server with impersonation permissions to allow IM and Presence users to pull calendar information
                                          from Microsoft Outlook. |
| Step 2 | Upload Microsoft Certificates to IM and Presence Service | Download the Microsoft certificates that will be required for integration with the IM and Presence Service. |

| Step 1 | Log in to Office 365. |
|---|---|
| Step 2 | Click the Admin icon |
| Step 3 | In the left navigation bar, select the Admin Center tab (bottom left) and click Exchange . |
| Step 4 | Under Permissions select Admin roles . |
| Step 5 | Select Discovery Management . |
| Step 6 | Click the Pencil icon to edit the role assignments. |
| Step 7 | Add the ApplicationImpersonation role by doing the following: Under Roles click + . Select ApplicationImpersonation and click Add . Click OK . |
| Step 8 | Assign a user as a member of the ApplicationImpersonation role: Under Members click + . Select the user account that you want to add and click Add . Click OK . |
| Step 9 | Click Save . |

| Step 1 | Download an Office 365 root certificate, and intermediate certificate: The following site lists all of the root and intermediate certificates that Office 365 supports: https://support.office.com/en-us/article/office-365-certificate-chains-0c03e6b3-e73f-4316-9e2b-bf4091ae96bb |
|---|---|
| Step 2 | Upload all certificates to the cup-trust and tomcat-trust stores on the IM and Presence Service. |

| Note | For additional details on certificates with the IM and Presence Service, refer to the "Security Configuration on IM and Presence
                                             Service" chapter of the Configuration and Administration Guide for IM and Presence Service . |
|---|---|