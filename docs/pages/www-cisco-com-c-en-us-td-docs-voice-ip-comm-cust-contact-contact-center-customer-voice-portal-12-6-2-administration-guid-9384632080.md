---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-administration-guid-9384632080
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/administration/guide/ccvp_b_1262-admin-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-admin-guide-for-cisco-unified-customer-voice-portal_chapter_0110.html
retrieved_at: 2026-08-21T02:56:12.342461+00:00
---

Administration Guide for Cisco Unified Customer Voice Portal 12.6(2)

# Administration Guide for Cisco Unified Customer Voice Portal 12.6(2)

Updated: April 28, 2023

Chapter: Launch Tools

## Chapter: Launch Tools

# Launch Tools

## Launch SNMP Monitor

You can use any
                              		standard SNMP-based monitoring tool to view details of the health of the
                              		Unified CVP solution network. All Unified CVP product components issue SNMP
                              		events, which can be delivered to the network monitoring tool. To specify a
                              		SNMP-based monitoring tool as the destination for SNMP traps and statistics,
                              		you must edit the Log Messages XML file on the Unified CVP Server for each
                              		event that the server generates. For information on editing the Log Message XML
                              		file to send SNMP events to an SNMP monitoring tool, see Edit Log Messages XML File .

You can launch the administration web page for an external SNMP
                              		  monitoring tool from the Tools menu in the Operations Console.

### Before you begin

Before you can launch an SNMP monitor, you must first specify the URL
                              		  of the SNMP monitor web page to launch. For information on configuring the URL
                              		  external tools, see the Links to Tools topic.

To Launch SNMP Monitor, choose Tools > SNMP
                                             				Monitor from the Operations Console.

## Links to Tools

You can store URLs for the tools available from the Tools menu. Once
                              configured, you can launch the administrative web page for each tool by
                              selecting the tool from the Operations Console Tools menu bar.

### Add URL to Tools Menu

To add a URL link to a tool:

Step 1

Select Tools > Configure from the Operations Console.

The Configure Tools window opens, listing the current URL
                                                				configured for each tool listed on the Tools menu.

Step 2

In the Enter New URL text box for the tool you want to configure,
                                             			 enter the URL for each tool to launch.

The web page indicated by this URL is launched when you select the
                                                				tool from the Tools menu.

Step 3

Click Save to save the URLs.

### Remove URL From Tools Menu

To remove a URL link for a tool:

Step 1

Choose Tools > Configure from the Operations Console.

The Configure Tools window opens, listing the current URL for each
                                                				tool.

Step 2

In the Enter New URL text box for the tool you want to configure,
                                             			 delete the URL from the text box, and click Save .

The URL for that tool is removed from the Operations Console,
                                                				which means that no URL is configured for that tool.

### Modify URL on Tools Menu

To modify a URL link for a tool:

Step 1

Select Tools > Configure from the Operations Console.

The Configure Tools window opens, listing the current URL for each
                                                				tool.

Step 2

In the Enter New URL text box for the tool you want to configure,
                                             			 modify the URL and click Save .

This modifies the URL for the selected tool. The web page
                                                				indicated by this URL is launched when you select the tool from the Tools menu.

## Launch NOAMP

Go to Tools > NOAMP .

| To Launch SNMP Monitor, choose Tools > SNMP
                                             				Monitor from the Operations Console. |
|---|

| Step 1 | Select Tools > Configure from the Operations Console. The Configure Tools window opens, listing the current URL
                                                				configured for each tool listed on the Tools menu. |
|---|---|
| Step 2 | In the Enter New URL text box for the tool you want to configure,
                                             			 enter the URL for each tool to launch. The web page indicated by this URL is launched when you select the
                                                				tool from the Tools menu. |
| Step 3 | Click Save to save the URLs. |

| Step 1 | Choose Tools > Configure from the Operations Console. The Configure Tools window opens, listing the current URL for each
                                                				tool. |
|---|---|
| Step 2 | In the Enter New URL text box for the tool you want to configure,
                                             			 delete the URL from the text box, and click Save . The URL for that tool is removed from the Operations Console,
                                                				which means that no URL is configured for that tool. |

| Step 1 | Select Tools > Configure from the Operations Console. The Configure Tools window opens, listing the current URL for each
                                                				tool. |
|---|---|
| Step 2 | In the Enter New URL text box for the tool you want to configure,
                                             			 modify the URL and click Save . This modifies the URL for the selected tool. The web page
                                                				indicated by this URL is launched when you select the tool from the Tools menu. |

| Go to Tools > NOAMP . You are logged in to NOAMP automatically. |
|---|