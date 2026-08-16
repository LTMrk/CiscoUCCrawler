---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-user-guide--004d7cfba8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/user/guide/ucce_b_cisco-unified-contact-center-enterprise-reporting-user-guide-release1501/ucce_b_cisco-unified-contact-center-enterprise-1261_chapter_0100.html
retrieved_at: 2026-08-16T20:33:57.191527+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release 15.0(1)

Updated: April 30, 2025

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

You can uncheck the Authenticate Permalink check boxes if you want the permalink (Variable and Default) to be accessible without authentication.

For Live Data reports, by default, the Authenticate check box is checked and disabled.

Step 4

To view the report,

HTML and XML Permalink—Copy and paste the permalink (HTML and XML) in any browser

Excel Permalink—

To import permalinks in Excel, use the permalinks with FQDN only.

To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used.

The browser prompts you to download and save the file (Excel format) to the local drive.

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

| Note | Authenticated report permalinks are not supported in Cisco Finesse. When an unauthenticated Report permalink is accessed in an authenticated browser session, access to the permalink is controlled
                                                by the logged in user's permissions. You cannot drill down to another report from a report permalink. |
|---|---|

| Step 1 | From the left navigation pane, click Reports . |
|---|---|
| Step 2 | Click the ellipsis icon beside the required Report and click Permalinks . |
| Step 3 | In the Permalinks dialog box, select from the available Link formats; HTML, Excel, XML to display the corresponding Report permalink in the Link text box. Note You can uncheck the Authenticate Permalink check boxes if you want the permalink (Variable and Default) to be accessible without authentication. For Live Data reports, by default, the Authenticate check box is checked and disabled. | Note | You can uncheck the Authenticate Permalink check boxes if you want the permalink (Variable and Default) to be accessible without authentication. For Live Data reports, by default, the Authenticate check box is checked and disabled. |
| Note | You can uncheck the Authenticate Permalink check boxes if you want the permalink (Variable and Default) to be accessible without authentication. For Live Data reports, by default, the Authenticate check box is checked and disabled. |
| Step 4 | To view the report, HTML and XML Permalink—Copy and paste the permalink (HTML and XML) in any browser Excel Permalink— Note To import permalinks in Excel, use the permalinks with FQDN only. To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used. The browser prompts you to download and save the file (Excel format) to the local drive. | Note | To import permalinks in Excel, use the permalinks with FQDN only. To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used. |
| Note | To import permalinks in Excel, use the permalinks with FQDN only. To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used. |
| Step 5 | Click Save . For information on viewing report permalinks in Dashboards as web page widgets, see View Report Permalinks in Dashboards . For more information on permalinks, see Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html . |

| Note | You can uncheck the Authenticate Permalink check boxes if you want the permalink (Variable and Default) to be accessible without authentication. For Live Data reports, by default, the Authenticate check box is checked and disabled. |
|---|---|

| Note | To import permalinks in Excel, use the permalinks with FQDN only. To embed excel permalink content as external data within excel on macOS, add tomcat certificate from Certificate Management to the trust store of macOS in case self-signed certificates are being used. |
|---|---|

|  | Auth Report Permalink Same Node | Auth Report Permalink Different Node | Auth Report Permalink Different Cluster | Un-Auth Report Permalink Same Node | Un-Auth Report Permalink Different Node | Un-Auth Report Permalink Different Cluster |
|---|---|---|---|---|---|---|
| Un-Auth Dashboard | Not Supported | Not Supported | Not Supported | Supported | Supported | Supported |
| Auth Dashboard | Supported | Not Supported | Not Supported | Supported | Supported | Supported |
| Dashboard Viewer | Supported | Not Supported | Not Supported | Supported | Supported | Supported |