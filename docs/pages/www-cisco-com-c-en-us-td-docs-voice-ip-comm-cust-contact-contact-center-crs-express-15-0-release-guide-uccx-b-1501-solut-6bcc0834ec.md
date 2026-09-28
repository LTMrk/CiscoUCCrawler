---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-release-guide-uccx-b-1501-solut-6bcc0834ec
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/release/guide/uccx_b_1501_solution-release-notes/uccx_m_1501_cisco-unified-intelligence-center.html
retrieved_at: 2026-08-16T20:56:59.560457+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 15.0

# Release Notes for Cisco Unified Contact Center Express Solution, Release 15.0

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

### Auto-switching of Database to Load Value List

Previously, the Value List entries were not loaded on a database failure until you manually switched from a primary database to a secondary database.
                              Now, these Value List entries are automatically loaded as the secondary database becomes active without manual intervention, in the event of a
                              primary database failure. This ensures a seamless experience in managing the display of reports during a database failover.

## Deprecated Features

None.

## Removed and Unsupported Features

None.

## Third-Party Software Impact

For the list of third-party softwares, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.