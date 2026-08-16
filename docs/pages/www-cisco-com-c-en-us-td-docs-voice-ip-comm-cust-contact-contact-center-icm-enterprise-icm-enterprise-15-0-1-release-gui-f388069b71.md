---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-f388069b71
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct_b_1501_cce-solutions-rns/rcct_m_1501_cisco-finesse-rn.html
retrieved_at: 2026-08-16T19:36:50.182385+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

# Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

Updated: April 30, 2025

Chapter: Cisco Finesse

## Chapter: Cisco Finesse

# Cisco Finesse

## New Features

### Notification Center

Finesse Desktop now has a Notification Center icon that displays all the desktop notification popovers that the agent receives
                              during a session. The notification popover includes chat, email, social media messages, system notification, and so on. For
                              more information, see the Notification Center section in the Cisco Finesse Agent and Supervisor Desktop User Guide .

### Modifying Cisco Finesse Notification Service Properties

Finesse provides a new CLI for modifying the properties of the notification service. You can use the CLI to enable third-party
                                 client subscriptions. For more information, see the Modifying Cisco Finesse Notification Service Properties section in Cisco Finesse Administration Guide .

## Updated Features

### Toaster Notification Enhancement

Finesse now supports toaster notifications for:

Incoming Calls —For incoming calls that are not answered within the configured time limit. If the call times out, a toaster notification
                                    appears on the Finesse desktop to indicate that you missed the call and your status is changed to Not Ready.

Away from your Active Desktop — If you step away from your active desktop and the Finesse server you are logged into becomes unavailable, Finesse will provide
                                    a toaster notification alerting you that the connection to the server has been lost.

Digital channel interactions — For incoming digital channel interactions that are not accepted within the configured time limit. If the interaction times
                                    out, a toaster notification appears on the Finesse desktop to indicate that you missed the interaction and your status is
                                    changed to Not Ready.

For more information on toaster notifications, see the Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html

You can disable the toaster notification for the above scenarios using a new CLI command. For more information, see the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

## Important Notes

### Accessibility Enhancements

Cisco Finesse Desktop adheres to the Web Content Accessibility Guidelines (WCAG) 2.1, Level A and AA, and the ICT Accessibility
                              508 Standards, ensuring accessibility for users with disabilities. The latest enhancements include improved web accessibility,
                              screen reader support, localization labels, color contrast, focus indicators, headers, titles, accessible labels, tool-tips,
                              error messages, search gadget, and skip-to-content landmarks.

For more information on Accessibility for Cisco Finesse, see the Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html

## Deprecated Features

None.

## Removed and Unsupported Features

None.

## Third Party Software Impacts

For the list of third-party software, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.