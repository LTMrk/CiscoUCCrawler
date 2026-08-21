---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-changing-srst-site-info-multiple-sites-h-cf4e1243ce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/changing_srst_site_info_multiple_sites.html
retrieved_at: 2026-08-21T23:38:46.901778+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Changing the Information for Multiple Cisco Unified SRST Sites at Once

## Chapter: Changing the Information for Multiple Cisco Unified SRST Sites at Once

## Changing the Information for Multiple Cisco Unified SRST Sites at Once

Before You Begin

You must have imported at least one site . See Viewing the Cisco Unified SRST References .

Restrictions

- You must configure all Cisco Unified SRST sites with a user name and password for provisioning to succeed.

- Do not use the Bulk Edit Selected Sites feature if each Cisco Unified SRST site has a unique user name and password. When you use the Bulk Edit Selected Sites feature, the system changes each Cisco Unified SRST site user name and password on Cisco Unified SRST Manager to the same values. These new values must match the values configured on the individual Cisco Unified SRST sites.

Step 1 Select Configure > Sites .

The system displays the Sites page.

Step 2 Select the check boxes next to the sites that you want to modify.

Step 3 Click Bulk Edit Selected Sites .

The system displays the Site Profile Bulk Edit page.

Step 4 To make changes, select the checkbox next to a field name and enter a value for any or all of the following:

- Site Provisioning Enable

- Restore Last Working Configuration

- Template

- Router Login Credentials: Username

- Router Login Credentials: Password

Step 5 Click Update .

The system applies the changes to each of the sites.

Related Topics