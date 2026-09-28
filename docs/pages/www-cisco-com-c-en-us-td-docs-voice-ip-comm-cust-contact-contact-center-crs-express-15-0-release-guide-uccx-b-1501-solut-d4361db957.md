---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-release-guide-uccx-b-1501-solut-d4361db957
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/release/guide/uccx_b_1501_solution-release-notes/uccx_m_1501_cisco-customer-collaboration-platform.html
retrieved_at: 2026-08-16T20:57:08.831171+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 15.0

# Release Notes for Cisco Unified Contact Center Express Solution, Release 15.0

Updated: April 30, 2025

Chapter: Cisco Customer Collaboration Platform

## Chapter: Cisco Customer Collaboration Platform

# Cisco Customer Collaboration Platform

## New Features

### API to get Queue Position and Expected Wait Time

A new API waitingcontactstatus is added, which makes an internal call to Unified CCX to find the Position in Queue (PIQ) and Estimated Wait Time (EWT) of
                                 a chat. For more information about the API, see the Get (queue position and estimated wait time) section in the Customer Collaboration Platform Developer Guide .

## Updated Features

None.

## Important Notes

Before you upgrade, ensure to update the Virtual Machine settings and Virtual Hardware memory settings. For details, see the Update Virtual Machine Settings section in the Cisco Customer Collaboration Platform Installation and Upgrade Guide .

If you switch back from Customer Collaboration Platform 15.0 to any of the previous versions, the chat related information
                                 in the Cassandra database, that are updated for 15.0, will not be synced.

## Deprecated Features

None.

## Removed and Unsupported Features

None.

## Third Party Software Impact

None.