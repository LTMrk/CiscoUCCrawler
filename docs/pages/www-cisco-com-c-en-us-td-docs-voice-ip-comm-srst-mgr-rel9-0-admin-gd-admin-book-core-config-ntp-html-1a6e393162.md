---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-core-config-ntp-html-1a6e393162
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/core_config_ntp.html
retrieved_at: 2026-08-21T23:39:04.006446+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Working With Network Time and Time Zone Settings

## Chapter: Working With Network Time and Time Zone Settings

## Working With Network Time and Time Zone Settings

You must add an NTP server to Cisco Unified SRST Manager and configure the time zone to ensure that system processes have the correct date and time associated with them.

Restriction

You can have a maximum of four NTP servers.

Step 1 Select System > Network Time & Time Zone Settings .

The system displays the Network Time & Time Zone Settings page.

Step 2 To add an NTP server, do the following:

a. Click Add . The system displays the Add a NTP Server page.

b. Enter the IP address of the NTP server.

c. Select the Preferred check box to make this the preferred NTP server.

d. Click Add .

Step 3 To remove an NTP server, do the following:

a. Select the check box next to the NTP server that you want to delete.

b. Click Delete .

c. At the prompt, click OK .

Step 4 To update the time zone settings, change the values for the country or time zone where the Cisco Unified SRST Manager system resides. Click Apply .

What To Do Next

If you have made any changes, save and then reload the configuration. See Saving and Reloading the Cisco Unified SRST Manager Configuration .