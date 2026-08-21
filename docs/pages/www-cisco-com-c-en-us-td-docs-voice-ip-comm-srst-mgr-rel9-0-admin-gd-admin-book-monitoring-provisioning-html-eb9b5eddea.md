---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-monitoring-provisioning-html-eb9b5eddea
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/monitoring_provisioning.html
retrieved_at: 2026-08-21T23:39:20.734494+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Monitoring the Provisioning Status of a Branch Device

## Chapter: Monitoring the Provisioning Status of a Branch Device

## Monitoring the Provisioning Status of a Branch Device

While Cisco Unified SRST Manager is actively provisioning branch call agent devices, you can view the realtime status of the provisioning process. To view the status, select Monitor > Provisioning Status . If the provisioning cycle was started manually, the system automatically displays the provisioning monitor page.

The system automatically refreshes the Provisioning Status page until all the selected sites have finished the provisioning cycle. During this time, you can navigate away from this page and return later to review the updated status. If the provisioning has not finished, the page will display the updated status for individual sites.

- Site—The name of the site being provisioned.

- Progress—The current state of provisioning:

– Not Started

– In Progress

– Complete

- Result—Indicates the outcome of the provisioning process for the site (or indicates that the provisioning is still in progress):

– In Progress

– Success

– Failed

If the system is not currently provisioning any sites, the system displays an informational message stating this.

Related Topics

- For information about generating the Site Provisioning report, see Viewing the Site Provisioning History Report .

- For descriptions of all alerts, see System Alerts .