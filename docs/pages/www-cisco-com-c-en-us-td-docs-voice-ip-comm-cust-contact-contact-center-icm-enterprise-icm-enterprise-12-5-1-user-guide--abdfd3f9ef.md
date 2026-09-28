---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--abdfd3f9ef
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting_user_guide-1251/ucce_b_cisco-unified-contact-center-enterprise-125_chapter_0100.html
retrieved_at: 2026-08-22T00:01:10.690818+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release12.5(1)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release12.5(1)

Updated: February 4, 2020

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

To view the Dashboard permalink, perform the following steps:

Step 1

From the left navigation pane, click Dashboards .

Step 2

Click the ellipsis icon beside the required Dashboard and click Permalinks .

Step 3

In the Permalinks dialog box, click HTML to display the  Dashboard permalink in the Link text box.

By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard.

When you uncheck the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication.

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

Auth Report Permalink Same Node

Auth Report Permalink Different Node

Auth Report Permalink Different Cluster

Un-Auth Report Permalink Same Node

Un-Auth Report Permalink Different Node

Un-Auth Report Permalink Different Cluster

| Note | For Live Data reports, you will only have the HTML permalink. HTML permalink for Live Data reports always require authentication. |
|---|---|

| Note | Due to security reasons, permalinks from one Unified Intelligence Center cannot be displayed in the dashboard of another Unified Intelligence Center instance. |
|---|---|

| Note | You can access the Dashboard permalink only from a web browser. Authenticated Dashboard permalinks are not supported in Cisco Finesse. When an unauthenticated Dashboard permalink is accessed in an authenticated browser session, access to the permalink is controlled
                                                by the logged in user's permissions. |
|---|---|

| Step 1 | From the left navigation pane, click Dashboards . |
|---|---|
| Step 2 | Click the ellipsis icon beside the required Dashboard and click Permalinks . |
| Step 3 | In the Permalinks dialog box, click HTML to display the  Dashboard permalink in the Link text box. Note By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard. When you uncheck the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication. Sharing an unauthenticated permalink of your Dashboard shares even the authenticated report permalinks added into the Dashboard. For Dashboards that contain Live Data report, ensure to select the Authenticate Permalink check box. | Note | By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard. When you uncheck the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication. Sharing an unauthenticated permalink of your Dashboard shares even the authenticated report permalinks added into the Dashboard. For Dashboards that contain Live Data report, ensure to select the Authenticate Permalink check box. |
| Note | By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard. When you uncheck the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication. Sharing an unauthenticated permalink of your Dashboard shares even the authenticated report permalinks added into the Dashboard. For Dashboards that contain Live Data report, ensure to select the Authenticate Permalink check box. |
| Step 4 | Copy and paste the permalink in any browser to view the Dashboard. |
| Step 5 | Click Save . |

| Note | By default, all Dashboards are authentication enabled. When the Authenticate Permalink check box is enabled, users accessing the permalink are prompted to enter their credentials to view the Dashboard. When you uncheck the Authenticate Permalink check box for a Dashboard, users can view that Dashboard using the permalink, without authentication. Sharing an unauthenticated permalink of your Dashboard shares even the authenticated report permalinks added into the Dashboard. For Dashboards that contain Live Data report, ensure to select the Authenticate Permalink check box. |
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

|  | Auth Report Permalink Same Node | Auth Report Permalink Different Node | Auth Report Permalink Different Cluster | Un-Auth Report Permalink Same Node | Un-Auth Report Permalink Different Node | Un-Auth Report Permalink Different Cluster |
|---|---|---|---|---|---|---|
| Un-Auth Dashboard | Not Supported | Not Supported | Not Supported | Supported | Supported | Supported |
| Auth Dashboard | Supported | Not Supported | Not Supported | Supported | Supported | Supported |
| Dashboard Viewer | Supported | Not Supported | Not Supported | Supported | Supported | Supported |