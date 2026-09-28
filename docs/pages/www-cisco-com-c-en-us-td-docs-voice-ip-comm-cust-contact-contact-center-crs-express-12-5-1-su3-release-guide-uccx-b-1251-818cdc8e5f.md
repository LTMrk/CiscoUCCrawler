---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su3-release-guide-uccx-b-1251-818cdc8e5f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su3/release/guide/uccx_b_1251su3_solution-release-notes/uccx_b_1252solution-release-notes_chapter_010.html
retrieved_at: 2026-08-16T20:57:54.518831+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU3

# Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU3

Updated: May 8, 2023

Chapter: Cisco Unified Intelligence Center

## Chapter: Cisco Unified Intelligence Center

# Cisco Unified Intelligence Center

## New Features

### Accessibility Compliance

This release ensures that the Cisco Unified Intelligence Center reporting application complies with Web Content Accessibility Guidelines (WCAG) 2.0. For more information on the supported JAWS version, see Voluntary
                                 Product Accessibility Templates (VPAT) report for Contact Center at https://www.cisco.com/c/en/us/about/accessibility/voluntary-product-accessibility-templates.html .

### Custom Logon Messages

You can configure custom logon messages for Cisco Unified Intelligence Center. The custom messages appear in a pop-up box
                                 during the sign-in process. The user has to acknowledge this message to proceed further. It is not mandatory to have custom
                                 messages. Administrators can set up the logon messages in Cisco Unified OS Administration. For more information, see the Configure
                                 Custom Logon Messages section in the Administration Console User Guide for Cisco Unified Intelligence Center at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge). For information about supported versions, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Commands

The following commands have been introduced:

#### Allow External Links

The administrator can enable or disable the external links in Unified Intelligence Center dashboard using the set cuic properties allow-external-links { on|off } command.

#### CUIC Logging

In this release, the log trace setting in OAMP interface is removed. The administrator must use the utils cuic logging commands to set the log traces. To change the log level configuration on each node in the cluster, the command must be run
                                 separately on each node.

## Updated Features

## Important Notes

### Allow External Links

After the upgrade, the external links in the Unified Intelligence Center dashboard will be disabled. If required, the administrator
                              can enable the external links again using the set cuic properties allow-external-links command.

If enabled, the contents from external links are rendered within the HTML iFrame in the dashboard. This will include the frame-src* directive in the Content Security Policy of the Unified Intelligence Center web pages.

### Gadget URL

JSP format is not supported for Unified Intelligence Center gadgets (Live Data and Historical). To change the JSP format references
                              to XML format, the administrator must run the following commands on the primary Cisco Finesse server.

utils finesse layout updateCuicGadgetUrl 12.6.1+—Updates the CUIC URL configured in the Cisco Finesse desktop layout to work
                                    with Release 12.6(1) and later versions. For more information, see the Upgrade section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### HTTP Access

Cisco Unified Intelligence Center is not accessible using port 8081 in any manner. From this release, port 8081 is disabled
                              and does not redirect to HTTPS.

### Restart Cisco Unified Intelligence Center Serviceability Service

After upgrading Unified CCX to 12.5(1) SU3, you must restart Cisco Unified Intelligence Center Serviceability Service, once
                              all the services are up. This is done in order to make SNMP Counters of CUIC to work properly.

## Deprecated Features

None.

## Removed and Unsupported Features

None.

## Third Party Software Impact

None.