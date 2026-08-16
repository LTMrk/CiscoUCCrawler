---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-c7cee0b267
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct_b_1501_cce-solutions-rns/rcct_m_1501_cuic.html
retrieved_at: 2026-08-16T19:36:46.168054+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

# Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

Updated: April 30, 2025

Chapter: Cisco Unified Intelligence Center

## Chapter: Cisco Unified Intelligence Center

# Cisco Unified Intelligence Center

## New Features

### API Rate Limit

To ensure system stability and maintain performance, a rate limit for the user API and permission API has been introduced.
                              You can use CLI commands to manage this rate limit, controlling the number of users interacting with the Unified Intelligence
                              Center and managing user permissions for accessing reports and functionalities.

The default rate limit is 100 requests per second for both the user API and permission API.

For more information, see the Command Line Interface chapter in the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

### Frame-ancestor Directive for Improved Security

The Content Security Policy (CSP) header now includes the frame-ancestors directive which specifies the authorized domains
                              allowed to embed Unified Intelligence Center content within an HTML frame or an object tag. You can add, remove, and view
                              the list of authorized domains using the CLI commands. By utilizing this directive, the security and reliability of the Unified
                              Intelligence Center are enhanced.

For more information, see the Command Line Interface chapter in the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html

## Updated Features

### Display Numerical Gauge Value as Whole Number

In New Gauge Chart View window, under the Preview and Format tab, a new check box Round up the value to the next whole number is available. By checking the Round up the value to the next whole number check box, the numeric gauge values that were displayed earlier in decimal number format are now displayed in a whole number
                              format.

For more information about the gauge report, see the section Chart Type of the chapter Reports in Cisco Unified Intelligence Center User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html .

### Delete User with Entities

Administrators can now delete a Unified Intelligence Center user who owns entities such as Dashboards, Reports, Report Definitions,
                              Schedules, Value List, and Collections. Upon deleting the Unified Intelligence Center user, all the entities associated with
                              the user are automatically reassigned to the administrator.

For more information about deleting a user, see the section Users Action of the chapter Configure in Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html .

## Important Notes

### Accessibility Enhancements

Cisco Unified Intelligence Center include accessibility enhancements for users with disabilities. The latest enhancements
                              include improved web accessibility, screen reader support, localization labels, color contrast, focus indicators, headers,
                              titles, accessible labels, tool-tips, error messages, search gadget, and skip-to-content landmarks.

For more information on Accessibility for Cisco Unified Intelligence Center, see the Cisco Unified Intelligence Center User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-user-guide-list.html

### Auto-switching of Database to Load Value List

Previously, the Value List entries were not loaded on a database failure until you manually switched from a primary database to a secondary database.
                              Now, these Value List entries are automatically loaded as the secondary database becomes active without manual intervention, in the event of a
                              primary database failure. This ensures a seamless experience in managing the display of reports during a database failover.

### Dynamic Real-time Data Source Switching

Previously, Cisco Unified Intelligence Center Live Data gadgets were not loaded in Cisco Finesse Desktop when the primary
                              Unified CCE real-time data source was down during an agent's login. Now, with automatic switch to the secondary Unified CCE
                              real-time data source, the Live Data gadgets are loaded even if the primary data source fails. This ensures continuous availability
                              of real-time data for agents and supervisors, leading to enhanced customer experience.

## Deprecated Features

None.

## Removed and Unsupported Features

None.

## Third Party Software Impacts

For the list of third-party software, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.