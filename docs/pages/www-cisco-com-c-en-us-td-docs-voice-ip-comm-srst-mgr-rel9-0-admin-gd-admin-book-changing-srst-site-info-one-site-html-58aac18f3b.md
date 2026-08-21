---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-changing-srst-site-info-one-site-html-58aac18f3b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/changing_srst_site_info_one_site.html
retrieved_at: 2026-08-21T23:38:42.588173+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Changing the Information for a Single Cisco Unified SRST Site

## Chapter: Changing the Information for a Single Cisco Unified SRST Site

## Changing the Information for a Single Cisco Unified SRST Site

Before You Begin

You must have imported at least one site . See Viewing the Cisco Unified SRST References .

Step 1 Select Configure > Sites .

The system displays the Sites page.

Step 2 Click the underlined name of the site for which you want to update the information.

The system displays the Site Profile page. This page contains several categories of information about the site and you can edit many of the details.

Step 3 Update fields.

Table 8 Update Site Parameters

Name

The Cisco Unified SRST reference name retrieved from the Cisco Unified Communications Manager. This field is read-only.

Central Call Agent

Name of the central call agent associated with the site. This field is read-only.

SRST Reference

IP address of the SRST site. This field is read-only.

Site Provisioning Enable

Enable or disable provisioning for the site.

Template

Defines the name of the site template to be used when provisioning the branch device. See Using Site Templates .

Restore Last Working Configuration

Enable or disable command restore for the site.

In case of a provisioning failure, Cisco Unified SRST Manager restores router back to the original configuration state by removing all the new CLI that were added before the failure.

Note By default, command rollback is enabled on all the routers.

Username

Defines the username login credentials for the device at the site.

The login credentials are configured by an administrator for the branch router.

The account must have privilege level 15.

Note It is strongly recommended not to use the weak username/password combination of cisco/cisco.

Password

Defines the password login credentials for the device at the site.

Confirm Password

Confirmation of the password login credentials for the device at the site.

Step 4 Click Update to save this information.

Related Topics

| Parameter | Description |
|---|---|
| Site |
| Name | The Cisco Unified SRST reference name retrieved from the Cisco Unified Communications Manager. This field is read-only. |
| Telephony |
| Central Call Agent | Name of the central call agent associated with the site. This field is read-only. |
| SRST Reference | IP address of the SRST site. This field is read-only. |
| Site Provisioning |
| Site Provisioning Enable | Enable or disable provisioning for the site. |
| Template | Defines the name of the site template to be used when provisioning the branch device. See Using Site Templates . |
| Rollback |
| Restore Last Working Configuration | Enable or disable command restore for the site. In case of a provisioning failure, Cisco Unified SRST Manager restores router back to the original configuration state by removing all the new CLI that were added before the failure. Note By default, command rollback is enabled on all the routers. |
| Router Login Credentials |
| Username | Defines the username login credentials for the device at the site. The login credentials are configured by an administrator for the branch router. The account must have privilege level 15. Note It is strongly recommended not to use the weak username/password combination of cisco/cisco. |
| Password | Defines the password login credentials for the device at the site. |
| Confirm Password | Confirmation of the password login credentials for the device at the site. |