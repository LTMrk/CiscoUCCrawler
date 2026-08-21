---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-creating-site-templates-html-c8e5941de3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/creating_site_templates.html
retrieved_at: 2026-08-21T23:38:55.351588+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Creating, Changing, and Viewing a Site Template

## Chapter: Creating, Changing, and Viewing a Site Template

## Creating, Changing, and Viewing a Site Template

Step 1 Select Configure > Site Templates .

The system displays the Site Templates page, containing a list of the site templates configured in Cisco Unified SRST Manager.

Step 2 Do one of the following:

- To create a new site template, click Add .

Note You can create a maximum of 10 site templates.

- To view the details of an existing site template or to change a site template, click the underlined name of the site template.

The system displays the Site Template Profile page, including the following information.

Note Some of the parameters are hidden in the initial view. Click the “Show Individual Feature Configuration” link to display all of the parameters.

Note Ensure that there are no active calls on a gateway when switching a site template from Cisco Unified SRST to E-SRST.

Table 10 Site Template Profile Parameters

Name

The name of the site template.

Restriction: The name cannot have spaces in it.

Provision Site as Classic SRST

Provision the site as classic SRST. The larger feature set that E-SRST enables will not be provisioned.

Auto-Learn Call Forward Settings

Cisco Unified SRST Manager retrieves call forward settings from Cisco Unified Communications Manager and provisions the settings on the site.

If disabled, specify a number in the “Call Forward Number” field for Cisco Unified SRST Manager to use to provision on the site.

Call Forward Number

If Auto Learn Call Forward Settings is disabled, the number specified here (instead of the voicemail pilot on CUCM) will be used by Cisco Unified SRST Manager to configure the call forward settings on the site.

If using a centralized voicemail server, consider entering the number of a local receptionist to ensure that forwarded calls are handled correctly when the WAN link is down and the central voicemail server is unreachable.

Enable Dial Plan configuration

Cisco Unified SRST Manager retrieves dial plan information from the CUCM and provisions the dial plan configuration on the site branch router.

Enable Music on Hold configuration

Cisco Unified SRST Manager provisions the music on hold (MOH) configuration on the site branch router.

Enable Hunt Group configuration

Cisco Unified SRST Manager retrieves hunt group information from the CUCM and provisions the hunt group configuration on the site branch router.

Enable Call Park configuration

Cisco Unified SRST Manager retrieves call park information from the CUCM and provisions the call park configuration on the site branch router.

Enable Call Pickup configuration

Cisco Unified SRST Manager retrieves call pickup information from the CUCM and provisions the call pickup configuration on the site branch router.

Enable Calling Privileges configuration

Cisco Unified SRST Manager retrieves call restrictions (calling search spaces, partitions, and so on) information from the CUCM and provisions the call restriction configuration on the site branch router.

Enable After Hours configuration

Cisco Unified SRST Manager retrieves time-based calling restrictions information from the CUCM and provisions the configuration on the site branch router.

Enable Single Number Reach configuration

Cisco Unified SRST Manager retrieves single number reach information from the CUCM and provisions the single number reach configuration on the site branch router.

Step 3 Enter information in the fields. See Table 10 .

Step 4 Click Update .

Related Topics

- Using Site Templates

| Parameter | Description |
|---|---|
| Template |
| Name | The name of the site template. Restriction: The name cannot have spaces in it. |
| Site Feature Configuration |
| Provision Site as Classic SRST | Provision the site as classic SRST. The larger feature set that E-SRST enables will not be provisioned. |
| Auto-Learn Call Forward Settings | Cisco Unified SRST Manager retrieves call forward settings from Cisco Unified Communications Manager and provisions the settings on the site. If disabled, specify a number in the “Call Forward Number” field for Cisco Unified SRST Manager to use to provision on the site. |
| Call Forward Number | If Auto Learn Call Forward Settings is disabled, the number specified here (instead of the voicemail pilot on CUCM) will be used by Cisco Unified SRST Manager to configure the call forward settings on the site. If using a centralized voicemail server, consider entering the number of a local receptionist to ensure that forwarded calls are handled correctly when the WAN link is down and the central voicemail server is unreachable. |
| Enable Dial Plan configuration | Cisco Unified SRST Manager retrieves dial plan information from the CUCM and provisions the dial plan configuration on the site branch router. |
| Enable Music on Hold configuration | Cisco Unified SRST Manager provisions the music on hold (MOH) configuration on the site branch router. |
| Enable Hunt Group configuration | Cisco Unified SRST Manager retrieves hunt group information from the CUCM and provisions the hunt group configuration on the site branch router. |
| Enable Call Park configuration | Cisco Unified SRST Manager retrieves call park information from the CUCM and provisions the call park configuration on the site branch router. |
| Enable Call Pickup configuration | Cisco Unified SRST Manager retrieves call pickup information from the CUCM and provisions the call pickup configuration on the site branch router. |
| Enable Calling Privileges configuration | Cisco Unified SRST Manager retrieves call restrictions (calling search spaces, partitions, and so on) information from the CUCM and provisions the call restriction configuration on the site branch router. |
| Enable After Hours configuration | Cisco Unified SRST Manager retrieves time-based calling restrictions information from the CUCM and provisions the configuration on the site branch router. |
| Enable Single Number Reach configuration | Cisco Unified SRST Manager retrieves single number reach information from the CUCM and provisions the single number reach configuration on the site branch router. |