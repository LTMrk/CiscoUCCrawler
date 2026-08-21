---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-using-site-templates-html-6c33ae0e8f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/using_site_templates.html
retrieved_at: 2026-08-21T23:38:51.332791+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: September 5, 2012

Chapter: Using Site Templates

## Chapter: Using Site Templates

## Using Site Templat es

Because many site s have common sets of information, Cisco Unified SRST Manager provides site templates. Use these templates to apply configuration settings to new sites.

By default, Cisco Unified SRST Manager includes the following site templates:

- default

You cannot change the name of this site template or delete it, but you can edit its values.

- ESRST_and_Dialplan

- ESRST_only

- SRST_and_Dialplan

- SRST_only

You can also create custom site templates. Table 9 describes the features configured for the default set of site templates. For details about each feature, see Table 10 .

Table 9 Default Site Template Parameters

Site Template

default

—

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ESRST_and_Dialplan

—

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ESRST_only

—

Yes

—

Yes

Yes

Yes

Yes

Yes

Yes

Yes

SRST_and_Dialplan

Yes

Yes

Yes

Yes

—

—

—

—

—

—

SRST_only

Yes

Yes

—

Yes

—

—

—

—

—

—

Step 1 Select Configure > Site Templates .

The system displays the Site Templates page, containing a list of the site templates configured in Cisco Unified SRST Manager.

Step 2 To create a new site template, update an existing site template, or view the details of an existing site template, see Creating, Changing, and Viewing a Site Template .

Step 3 To remove a site template, do the following:

a. Select the site template to delete.

b. Click Remove .

c. Click OK at the warning message.

Related Topics

- Creating, Changing, and Viewing a Site Template

| Site Template | Provision Site as Classic SRST | Auto-Learn Call Forward Settings | Enable Dial Plan configuration | Enable Music on Hold configuration | Enable Hunt Group configuration | Enable Call Park configuration | Enable Call Pickup configuration | Enable Calling Privileges configuration | Enable After Hours configuration | Enable Single Number Reach configuration |
|---|---|---|---|---|---|---|---|---|---|---|
| default | — | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| ESRST_and_Dialplan | — | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| ESRST_only | — | Yes | — | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| SRST_and_Dialplan | Yes | Yes | Yes | Yes | — | — | — | — | — | — |
| SRST_only | Yes | Yes | — | Yes | — | — | — | — | — | — |