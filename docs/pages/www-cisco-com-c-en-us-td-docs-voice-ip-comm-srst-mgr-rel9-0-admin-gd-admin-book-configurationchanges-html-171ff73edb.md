---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-configurationchanges-html-171ff73edb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/configurationchanges.html
retrieved_at: 2026-08-21T23:39:29.421463+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 16, 2015

Chapter: Viewing Configuration Changes

## Chapter: Viewing Configuration Changes

- Latest Configuration Changes

- Complete Configuration Changes

- Viewing t he Configuration Changes

## Viewing Configuration Changes

After provisioning a cisco router successfully, you can view the configuration changes associated with the router under Reports > Site Provisioning History in Cisco Unified SRST Manager GUI. The following columns under Site Provisioning History provides the details of configuration changes associated with a router:

The configuration changes file is created for both Cisco Unified SRST routers and Cisco Unified E-SRST routers. It contains the details of the mode and the time stamp. The configuration changes file can store data to a maximum of 2MB. If configuration changes exceeds 2MB, then the data is overwritten.

## Latest Configuration Changes

Latest Configuration Changes log file provides the list of CLI which are pushed to the router between the latest two successful provisioning. If there are no new CLIs added between the last successful provisioning and the current successful provisioning, then the latest configuration changes section will be empty. If the current provisioning fails, then there is no content in the latest configuration changes. Check the time stamp to confirm the latest configuration changes.

## Complete Configuration Changes

Complete Configuration Changes log file provides details of all the CLI that are pushed to the router from Cisco Unified SRST Manager at any point of time.

Cisco Unified SRST Manager gets the CLI information from the router. Hence, there is possibility that some CLI, which automatically comes with the parent CLI may also be listed. If you have configured some CLI manually, then those CLIs will also be listed.

## Viewing the Configuration Changes

To viewing the CLI log file, refer to Viewing the Site Provisioning History Report .