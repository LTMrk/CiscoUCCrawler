---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-core-config-dns-html-6e1503cbad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/core_config_dns.html
retrieved_at: 2026-08-21T23:38:59.754204+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Working With DNS Servers

## Chapter: Working With DNS Servers

## Working With DNS Servers

Restriction

You can have a maximum of four DNS servers.

Note DNS server configuration is optional in the Cisco Unified SRST Manger version 11.0. If DNS server is not configured, then it is highly recommended to provide IP address of the Cisco Unified Communications Manager (CUCM) in the GUI at the time of adding CUCM. If host name of the CUCM is provided then ensure that IP address of the CUCM is present in the certificate under alternate host name.

Step 1 Select System > Domain Name System Settings .

The system displays the Domain Name System Settings page.

Step 2 To update the domain name settings, enter values for one or both of the following:

- The hostname of the Cisco Unified SRST Manager system.

- The domain name. Example : Cisco.com

Step 3 To add a DNS server, do the following:

a. Click Add .

b. Enter the IP address of the DNS server.

c. Click Add .

Step 4 To remove a DNS server, do the following:

a. Select the check box next to the DNS server to delete.

b. Click Delete .

c. At the prompt, click OK .

What To Do Next

If you have made any changes, save and then reload the configuration. See Saving and Reloading the Cisco Unified SRST Manager Configuration .