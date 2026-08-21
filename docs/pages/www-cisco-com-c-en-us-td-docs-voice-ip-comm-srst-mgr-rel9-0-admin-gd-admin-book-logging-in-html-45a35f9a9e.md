---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-logging-in-html-45a35f9a9e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/logging_in.html
retrieved_at: 2026-08-21T23:38:00.813707+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: September 5, 2012

Chapter: Logging In to the Cisco Unified SRST Manager Graphical User Interface

## Chapter: Logging In to the Cisco Unified SRST Manager Graphical User Interface

## Logging In to the Cisco Unified SRST Manager Graphical User Interface

Restrictions

The Cisco Unified SRST Manager graphical user interface (GUI) supports the following web browsers:

- Internet Explorer Releases 6 or later

- Mozilla Firefox

Cookies must be enabled.

Before You Begin

- Install Cisco Unified SRST Manager software. See Installation and Upgrade Guide for Cisco Unified SRST Manager Release 11.0 for information.

- Gather the administrator username and password that you entered during the installation.

Step 1 Open a web browser.

Step 2 Enter the IP address of the Cisco Unified SRST Manager system.

The GUI login screen appears.

Step 3 Enter the administrator user name and password.

Step 4 Click Log In .

The Cisco Unified SRST Manager dashboard appears.

About the Cisco Unified SRST Manager Dashboard

Monitor the status of the system periodically to ensure that the deployment remains ready for failover events. You can monitor the system from the Cisco Unified SRST Manager dashboard.

The dashboard provides an at-a-glance view of the state of the system. The dashboard contains a summary of items that would typically require the attention of the administrator, such as error and warning messages. When the system is functioning normally, with no alerts or activity, the dashboard shows minimal information.

You can return to the dashboard from anywhere in the system by clicking Dashboard on the top right.

The dashboard is comprised of the following areas:

- Provisioning Status: Displays a summary of the results of the most recent provisioning cycle. If all sites have been successfully provisioned, a single success message is displayed. If any sites are disabled, have failed provisioning, or have never been provisioned, the provisioning status panes displays a site count for each provisioning outcome respectively. For provisioning failures, the system generates a system alert message for each site that indicates the reason for the failure. To review site specific results by status, click the corresponding report link.

- System Alerts: Displays the number of critical, warning, error, and informational alert messages that require attention. To review system alert details by level, click the corresponding link. See System Alerts for more description of the alerts.