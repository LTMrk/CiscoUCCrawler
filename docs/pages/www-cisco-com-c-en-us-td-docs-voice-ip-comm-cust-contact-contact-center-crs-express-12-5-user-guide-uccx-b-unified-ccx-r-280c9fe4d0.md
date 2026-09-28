---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-user-guide-uccx-b-unified-ccx-r-280c9fe4d0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/user/guide/uccx_b_unified-ccx-reporting-user-guide-125/uccx_b_unified-ccx-reporting-user-guide-125_chapter_0101.html
retrieved_at: 2026-08-16T21:26:35.004155+00:00
---

Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Permalinks

## Chapter: Permalinks

# Permalinks

## Overview

Permalinks in Cisco Unified Intelligence Center are permanent hyperlinks.

Unified Intelligence Center supports the following types of permalinks for reports:

Excel Link: This permalink is generated only for grid view.

HTML Link: This permalink is generated for grid view, gauge view, and chart view.

XML Link: This permalink is generated only for the grid view. It is used where the data is required in XML format.

For Live Data reports, you will only have the HTML permalink. HTML permalink for Live Data reports always require authentication.

Due to security reasons, permalinks from one Unified Intelligence Center cannot be displayed in the dashboard of another Unified Intelligence Center instance.

## Permalink for a Dashboard

Dashboard permalinks help you to share your Dashboards with other users and view Dashboards of other users.

You can access the Dashboard permalink only from a web browser.

Authenticated Dashboard permalinks are not supported in Cisco Finesse.

When an unauthenticated Dashboard permalink is accessed in an authenticated browser session, access to the permalink is controlled
                                                by the logged in user's permissions.

To use Permalink (both Authenticated and Unauthenticated) for Dashboards, you must do the following for each report:

Set Default Filter

Select Skip filter during the report execution

To view the Dashboard permalink, perform the following steps:

Step 1

From the left navigation pane, click Dashboards .

Step 2

Click the ellipsis icon beside the required Dashboard and click Permalinks .

Step 3

In the Permalinks dialog box, click HTML to display the  Dashboard permalink in the Link text box.

By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard.

When you clear the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication.

Sharing an unauthenticated permalink of your Dashboard shares even the authenticated report permalinks added into the Dashboard.

For Dashboards that contain Live Data report, ensure to select the Authenticate Permalink check box.

Step 4

Copy and paste the permalink in any browser to view the Dashboard.

Step 5

Click Save .

## Permalink for a Report

Report permalinks help you to share your report with other users and view reports of other users.

Authenticated report permalinks are not supported in Cisco Finesse.

Authenticated Excel report permalink is not supported in SSO.

Authenticated Excel report permalink is not supported on Office 365.

When an unauthenticated Report permalink is accessed in an authenticated browser session, access to the permalink is controlled
                                                by the logged in user's permissions.

You cannot drill down to another report from a report permalink.

To view the Report permalink, perform the following steps:

Step 1

From the left navigation pane, click Reports .

Step 2

Click the ellipsis icon beside the required Report and click Permalinks .

Step 3

In the Permalinks dialog box, select from the available Link formats; HTML, Excel, XML to display the corresponding Report permalink in the Link text box.

By default, the Authenticate Permalink check boxes are checked to indicate that the default and variable permalink are authenticated.

For Live Data reports, by default, the Authenticate check box is checked and disabled.

Step 4

To view the report,

HTML and XML Permalink—Copy and paste the permalink (HTML and XML) in any browser

Excel Permalink—

To import permalinks in Excel, use the permalinks with FQDN only.

To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used.

Excel—

Access Excel and navigate to Data > From Web .

In the New Web Query > Address field, paste the report permalink and click Import .

Excel 365—

Access Excel 365 and navigate to Data > From Web .

In the From Web > URL field, paste the report permalink and click OK .

For the first time, you will be prompted to Connect in the Access Web Content dialog box.

In the Navigator dialog box, click Table View > Load .

Step 5

Click Save .

For information on viewing report permalinks in Dashboards as web page widgets, see View Report Permalinks in Dashboards .

For more information on permalinks, see Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html .

## View Report Permalinks in Dashboards

Viewing report permalinks in Dashboards as web page widgets depends on the authentication status of both reports and the dashboards.
                              The following matrix provides different scenarios that supports viewing report permalinks in Dashboards.

Authenticated Report Permalink Same Node

Authenticated Report Permalink Different Node

Unauthenticated Report Permalink Same Node

Unauthenticated Report Permalink Different Node

## Create Live Data Report Permalink for Finesse

For permalinks of supervisor stock reports, see Permalinks for Supervisor Live Data Reports . To create a permalink for saved stock reports, the procedure is as follows:

Step 1

Copy the permalink of the stock report that you want to customize from Permalinks for Supervisor Live Data Reports and paste it in a text editor.

Example:

Consider the below URL as the permalink. Copy and paste it in a text editor. The underlined ID is the value of viewID.

```
https://<Server Name>:8444/cuicui/permalink/?viewId= 5C90012F10000140000000830A4E5B33 &linkType=htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL
```

Step 2

Click Reports in the left pane.

Step 3

Navigate to the custom report.

Step 4

Click the ellipsis icon beside the report and click Edit .

Step 5

In the List of Views > Manage Views page, select HTML, Excel, or XML to display the corresponding Report permalink in the Link text box.

Step 6

Copy the permalink of the customized report from the Link field, paste it in a text editor, and then copy the viewID value from this link.

Example:

Copy the underlined viewID value from the permalink of the customized report.

```
https://<Server Name>:8444/cuicui/permalink/?viewId= B27986B510000142000004D60A4E5B33 &linkType=htmlType&viewType=Grid
```

Step 7

Replace the viewID value in the stock report permalink with the viewID value from the permalink of the customized report.

Example:

After replacing the viewID value with the viewID of the customized report, the customized report permalink appears as follows:

```
https://<Server Name>:8444/cuicui/permalink/?viewId= B27986B510000142000004D60A4E5B33 &linkType=htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL
```

Step 8

Add the customized gadget URL to Desktop Layout in the Finesse Administration console and save.

Step 9

Log in to Finesse desktop and check the report.

## Permalinks for Supervisor Live Data Reports

The following table presents the permalinks for supervisor reports. Replace <Server Name> with the IP or FQDN address of Unified CCX node.

Permalinks are not supported for agent reports.

Report

View

Permalink

Agent Outbound Team Summary Report

Since Midnight

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
FD919FB9100001440000005D0A4E5B29&linkType=
htmlType&viewType=Grid
```

Short and Long Term Average

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
FD919FB510000144000000470A4E5B29&linkType=
htmlType&viewType=Grid
```

Chat Agent Statistics Report

—

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
F2F1FC17100001440000014E0A4E5D48&linkType=
htmlType&viewType=Grid&ChatAgentStats.agentId=CL
```

Chat CSQ Summary Report

—

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
E42ED788100001440000007B0A4E5CA1&linkType=
htmlType&viewType=Grid&ChatQueueStatistics.queueName=CL
```

Team State Report

—

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
5C90012F10000140000000830A4E5B33&linkType=
htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL
```

Team Summary Report

Since Midnight

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
728283C210000140000000530A4E5B33&linkType=
htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL
```

Short and Long Term Average

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
7291DCB410000140000000890A4E5B33&linkType=
htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL
```

Voice CSQ Agent Detail Report

—

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
9A7A14CE10000140000000ED0A4E5E6B&linkType=
htmlType&viewType=Grid&VoiceCSQDetailsStats.agentId=
CL&VoiceCSQDetailsStats.AgentVoiceCSQNames.agentVoiceCSQName=CL
```

Voice CSQ Summary Report

Snapshot

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
C8E2DB1610000140000000A60A4E5E6B&linkType=
htmlType&viewType=Grid&VoiceIAQStats.esdName=CL
```

Since Midnight

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
C8EF510810000140000000EB0A4E5E6B&linkType=
htmlType&viewType=Grid&VoiceIAQStats.esdName=CL
```

Short and Long Term Average

```
https://<Server Name>:8444/cuicui/permalink/?viewId=
C8EE241910000140000000C30A4E5E6B&linkType=
htmlType&viewType=Grid&VoiceIAQStats.esdName=CL
```

| Note | For Live Data reports, you will only have the HTML permalink. HTML permalink for Live Data reports always require authentication. |
|---|---|

| Note | Due to security reasons, permalinks from one Unified Intelligence Center cannot be displayed in the dashboard of another Unified Intelligence Center instance. |
|---|---|

| Note | You can access the Dashboard permalink only from a web browser. Authenticated Dashboard permalinks are not supported in Cisco Finesse. When an unauthenticated Dashboard permalink is accessed in an authenticated browser session, access to the permalink is controlled
                                                by the logged in user's permissions. To use Permalink (both Authenticated and Unauthenticated) for Dashboards, you must do the following for each report: Set Default Filter Select Skip filter during the report execution |
|---|---|

| Step 1 | From the left navigation pane, click Dashboards . |
|---|---|
| Step 2 | Click the ellipsis icon beside the required Dashboard and click Permalinks . |
| Step 3 | In the Permalinks dialog box, click HTML to display the  Dashboard permalink in the Link text box. Note By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard. When you clear the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication. Sharing an unauthenticated permalink of your Dashboard shares even the authenticated report permalinks added into the Dashboard. For Dashboards that contain Live Data report, ensure to select the Authenticate Permalink check box. | Note | By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard. When you clear the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication. Sharing an unauthenticated permalink of your Dashboard shares even the authenticated report permalinks added into the Dashboard. For Dashboards that contain Live Data report, ensure to select the Authenticate Permalink check box. |
| Note | By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard. When you clear the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication. Sharing an unauthenticated permalink of your Dashboard shares even the authenticated report permalinks added into the Dashboard. For Dashboards that contain Live Data report, ensure to select the Authenticate Permalink check box. |
| Step 4 | Copy and paste the permalink in any browser to view the Dashboard. |
| Step 5 | Click Save . |

| Note | By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard. When you clear the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication. Sharing an unauthenticated permalink of your Dashboard shares even the authenticated report permalinks added into the Dashboard. For Dashboards that contain Live Data report, ensure to select the Authenticate Permalink check box. |
|---|---|

| Note | Authenticated report permalinks are not supported in Cisco Finesse. Authenticated Excel report permalink is not supported in SSO. Authenticated Excel report permalink is not supported on Office 365. When an unauthenticated Report permalink is accessed in an authenticated browser session, access to the permalink is controlled
                                                by the logged in user's permissions. You cannot drill down to another report from a report permalink. |
|---|---|

| Step 1 | From the left navigation pane, click Reports . |
|---|---|
| Step 2 | Click the ellipsis icon beside the required Report and click Permalinks . |
| Step 3 | In the Permalinks dialog box, select from the available Link formats; HTML, Excel, XML to display the corresponding Report permalink in the Link text box. Note By default, the Authenticate Permalink check boxes are checked to indicate that the default and variable permalink are authenticated. For Live Data reports, by default, the Authenticate check box is checked and disabled. | Note | By default, the Authenticate Permalink check boxes are checked to indicate that the default and variable permalink are authenticated. For Live Data reports, by default, the Authenticate check box is checked and disabled. |
| Note | By default, the Authenticate Permalink check boxes are checked to indicate that the default and variable permalink are authenticated. For Live Data reports, by default, the Authenticate check box is checked and disabled. |
| Step 4 | To view the report, HTML and XML Permalink—Copy and paste the permalink (HTML and XML) in any browser Excel Permalink— Note To import permalinks in Excel, use the permalinks with FQDN only. To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used. Excel— Access Excel and navigate to Data > From Web . In the New Web Query > Address field, paste the report permalink and click Import . Excel 365— Access Excel 365 and navigate to Data > From Web . In the From Web > URL field, paste the report permalink and click OK . Note For the first time, you will be prompted to Connect in the Access Web Content dialog box. In the Navigator dialog box, click Table View > Load . | Note | To import permalinks in Excel, use the permalinks with FQDN only. To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used. | Note | For the first time, you will be prompted to Connect in the Access Web Content dialog box. |
| Note | To import permalinks in Excel, use the permalinks with FQDN only. To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used. |
| Note | For the first time, you will be prompted to Connect in the Access Web Content dialog box. |
| Step 5 | Click Save . For information on viewing report permalinks in Dashboards as web page widgets, see View Report Permalinks in Dashboards . For more information on permalinks, see Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html . |

| Note | By default, the Authenticate Permalink check boxes are checked to indicate that the default and variable permalink are authenticated. For Live Data reports, by default, the Authenticate check box is checked and disabled. |
|---|---|

| Note | To import permalinks in Excel, use the permalinks with FQDN only. To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used. |
|---|---|

| Note | For the first time, you will be prompted to Connect in the Access Web Content dialog box. |
|---|---|

|  | Authenticated Report Permalink Same Node | Authenticated Report Permalink Different Node | Unauthenticated Report Permalink Same Node | Unauthenticated Report Permalink Different Node |
|---|---|---|---|---|
| Un-Auth Dashboard | Not Supported | Not Supported | Supported | Supported |
| Auth Dashboard | Supported | Not Supported | Supported | Supported |
| Dashboard Viewer | Supported | Not Supported | Supported | Supported |

| Step 1 | Copy the permalink of the stock report that you want to customize from Permalinks for Supervisor Live Data Reports and paste it in a text editor. Example: Consider the below URL as the permalink. Copy and paste it in a text editor. The underlined ID is the value of viewID. https://<Server Name>:8444/cuicui/permalink/?viewId= 5C90012F10000140000000830A4E5B33 &linkType=htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL |
|---|---|
| Step 2 | Click Reports in the left pane. |
| Step 3 | Navigate to the custom report. |
| Step 4 | Click the ellipsis icon beside the report and click Edit . |
| Step 5 | In the List of Views > Manage Views page, select HTML, Excel, or XML to display the corresponding Report permalink in the Link text box. |
| Step 6 | Copy the permalink of the customized report from the Link field, paste it in a text editor, and then copy the viewID value from this link. Example: Copy the underlined viewID value from the permalink of the customized report. https://<Server Name>:8444/cuicui/permalink/?viewId= B27986B510000142000004D60A4E5B33 &linkType=htmlType&viewType=Grid |
| Step 7 | Replace the viewID value in the stock report permalink with the viewID value from the permalink of the customized report. Example: After replacing the viewID value with the viewID of the customized report, the customized report permalink appears as follows: https://<Server Name>:8444/cuicui/permalink/?viewId= B27986B510000142000004D60A4E5B33 &linkType=htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL |
| Step 8 | Add the customized gadget URL to Desktop Layout in the Finesse Administration console and save. |
| Step 9 | Log in to Finesse desktop and check the report. |

| Note | Permalinks are not supported for agent reports. |
|---|---|

| Report | View | Permalink |
|---|---|---|
| Agent Outbound Team Summary Report | Since Midnight | https://<Server Name>:8444/cuicui/permalink/?viewId=
FD919FB9100001440000005D0A4E5B29&linkType=
htmlType&viewType=Grid |
| Short and Long Term Average | https://<Server Name>:8444/cuicui/permalink/?viewId=
FD919FB510000144000000470A4E5B29&linkType=
htmlType&viewType=Grid |
| Chat Agent Statistics Report | — | https://<Server Name>:8444/cuicui/permalink/?viewId=
F2F1FC17100001440000014E0A4E5D48&linkType=
htmlType&viewType=Grid&ChatAgentStats.agentId=CL |
| Chat CSQ Summary Report | — | https://<Server Name>:8444/cuicui/permalink/?viewId=
E42ED788100001440000007B0A4E5CA1&linkType=
htmlType&viewType=Grid&ChatQueueStatistics.queueName=CL |
| Team State Report | — | https://<Server Name>:8444/cuicui/permalink/?viewId=
5C90012F10000140000000830A4E5B33&linkType=
htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL |
| Team Summary Report | Since Midnight | https://<Server Name>:8444/cuicui/permalink/?viewId=
728283C210000140000000530A4E5B33&linkType=
htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL |
| Short and Long Term Average | https://<Server Name>:8444/cuicui/permalink/?viewId=
7291DCB410000140000000890A4E5B33&linkType=
htmlType&viewType=Grid&ResourceIAQStats.resourceId=CL |
| Voice CSQ Agent Detail Report | — | https://<Server Name>:8444/cuicui/permalink/?viewId=
9A7A14CE10000140000000ED0A4E5E6B&linkType=
htmlType&viewType=Grid&VoiceCSQDetailsStats.agentId=
CL&VoiceCSQDetailsStats.AgentVoiceCSQNames.agentVoiceCSQName=CL |
| Voice CSQ Summary Report | Snapshot | https://<Server Name>:8444/cuicui/permalink/?viewId=
C8E2DB1610000140000000A60A4E5E6B&linkType=
htmlType&viewType=Grid&VoiceIAQStats.esdName=CL |
| Since Midnight | https://<Server Name>:8444/cuicui/permalink/?viewId=
C8EF510810000140000000EB0A4E5E6B&linkType=
htmlType&viewType=Grid&VoiceIAQStats.esdName=CL |
| Short and Long Term Average | https://<Server Name>:8444/cuicui/permalink/?viewId=
C8EE241910000140000000C30A4E5E6B&linkType=
htmlType&viewType=Grid&VoiceIAQStats.esdName=CL |