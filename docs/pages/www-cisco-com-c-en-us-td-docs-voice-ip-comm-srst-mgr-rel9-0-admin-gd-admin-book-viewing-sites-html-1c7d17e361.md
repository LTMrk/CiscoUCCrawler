---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-viewing-sites-html-1c7d17e361
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/viewing_sites.html
retrieved_at: 2026-08-21T23:38:38.597096+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: September 5, 2012

Chapter: Viewing and Provisioning Sites

## Chapter: Viewing and Provisioning Sites

## Viewing and Provisioning Sites

Before You Begin

Import at least one site . See Viewing the Cisco Unified SRST References .

Note If provisioning is not enabled on a site, the site will not be provisioned.

Step 1 Select Configure > Sites .

The system displays the Sites page, listing the sites that have been added to Cisco Unified SRST Manager. For each site, the following information is listed:

Site

Name of the site.

Provisioning Enabled

Displays a green check mark if provisioning is enabled.

Note By default, provisioning is not enabled for new SRST references retrieved from the Cisco Unified Communications Manager. See Changing the Information for a Single Cisco Unified SRST Site and Changing the Information for Multiple Cisco Unified SRST Sites at Once .

Branch Call Agent

Indicates the branch call agent for the site.

Site Template Name

Name of the site template associated with the site. See Using Site Templates .

SRST Type

Enhanced SRST (Cisco Unified CME) or Classic SRST.

Dial Plan Configuration Enabled

If a check mark appears, then dial plan configuration will be provisioned for the site.

Step 2 To filter the list of sites, do the following:

a. Select a filter from the Filter drop-down list.

b. Select a condition from the Match if drop-down list.

c. Enter a keyword.

d. Click Go .

To clear the values, click Clear Filter and click Go .

Step 3 To provision sites, do the following:

a. Select the check box next to the name of the site or sites that you want to provision.

b. Click Provision Selected Sites . The system displays a warning message stating that the system will immediately contact the Cisco Unified Communications Manager system and download all the information about the selected sites.

c. Click OK to continue. The Provisioning Status page appears, displaying the site provisioning status.

Note For more information about provisioning, including the difference between automatic (scheduled) and manual provisioning, see About Provisioning Branch Site Devices .

Step 4 To view provisioning status or edit information about sites, do one of the following:

- To view the status of the provisioning at any time, select Monitor > Provisioning Status . See Monitoring the Provisioning Status of a Branch Device .

- To view or edit information about a specific site, click the underlined name of the site. See Changing the Information for a Single Cisco Unified SRST Site .

- To edit more than one site at a time, select the check boxes for more than one site, and click Bulk Edit Selected Sites . See Changing the Information for Multiple Cisco Unified SRST Sites at Once .

About Provisioning Branch Site Devices

Cisco Unified SRST Manager provisions branch call agents.

There are two ways you can provision a branch device: automatically according to a schedule or manually.

Typically, provisioning takes place based on the Cisco Unified Communications Manager provisioning schedule. The schedule defines a recurrence frequency that dictates how often the Cisco Unified SRST Manager will synchronize configuration data from the central office to the branch office.

Configuration Requirements for Branch Site Devices

To operate with E-SRST functionality, branch site devices require the following:

- A username/password configuration used for connecting to the branch router by telnet or ssh. It is recommended not to use cisco/cisco as the username/password for a branch router.

- Configuration for an http server and for https.

- Configuration of lines with:

– Privilege level 15

– Transport protocols—minimally, telnet, http, and ssh (for modules)

For branch routers with access lists configured, verify that Cisco Unified SRST Manager can access the branch router.

– If you are not using TLS, verify that Cisco Unified SRST Manager can access the branch router using telnet.

– If you are using TLS, verify that Cisco Unified SRST Manager can access the branch router using ssh.

Note For additional information, see Configuring the Cisco Unified Communications Manager Express Branch Call Agent to Prepare for E-SRST Provisioning .

About Scheduled Provisioning

Cisco Unified SRST Manager scheduled provisioning can be enabled or disabled based on your requirement. If scheduled provisioning is enabled, then Cisco Unified SRST Manager initiates the provisioning based on the schedule configured. Provisioning scheduled times are relative to the time zone of the Cisco Unified Communications Manager. This enables you to accurately select the time of day when the Cisco Unified Communications Manager call load is the lowest. Cisco Unified SRST Manager automatically adjusts the provisioning start and end times based on the time difference between the Cisco Unified SRST Manager and the configured call agent time zone.

For example, if Cisco Unified SRST Manager is in the U.S. EST time zone and the Cisco Unified Communications Manager is in the U.S. PST time zone, if the provisioning schedule is configured to run at 1:00 a.m. daily, Cisco Unified SRST Manager will wait until 4:00 a.m. EST to provision sites.

Cisco Unified SRST Manager checks the need for provisioning and only then triggers the provisioning. The provisioning is triggered based on the following factors:

- If there is a change in the configuration to Cisco Unified SRST reference such as phone is added or deleted in the Cisco Unified Communications Manager, name change or DNS change.

- If there are any changes in the mode, which is SRST to ESRST and vice-versa on the site

- If there are any changes in the call forward number

If the above mentioned factors are not present, then the provisioning is not triggered.

See Table 6 for more information about the provisioning schedule.

Manually Provisioning a Site

You can manually provision sites from the Configure > Sites page. During the provisioning cycle, the system contacts the Cisco Unified Communications Manager. We recommend that you perform this procedure when the central systems are not busy.

| Parameter | Description |
|---|---|
| Site | Name of the site. |
| Provisioning Enabled | Displays a green check mark if provisioning is enabled. Note By default, provisioning is not enabled for new SRST references retrieved from the Cisco Unified Communications Manager. See Changing the Information for a Single Cisco Unified SRST Site and Changing the Information for Multiple Cisco Unified SRST Sites at Once . |
| Branch Call Agent | Indicates the branch call agent for the site. |
| Site Template Name | Name of the site template associated with the site. See Using Site Templates . |
| SRST Type | Enhanced SRST (Cisco Unified CME) or Classic SRST. |
| Dial Plan Configuration Enabled | If a check mark appears, then dial plan configuration will be provisioned for the site. |