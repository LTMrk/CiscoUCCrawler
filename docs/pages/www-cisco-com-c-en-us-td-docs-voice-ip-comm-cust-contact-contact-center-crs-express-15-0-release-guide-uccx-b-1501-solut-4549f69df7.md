---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-release-guide-uccx-b-1501-solut-4549f69df7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/release/guide/uccx_b_1501_solution-release-notes/uccx_m_1501_cisco-finesse.html
retrieved_at: 2026-08-16T20:57:03.761245+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 15.0

# Release Notes for Cisco Unified Contact Center Express Solution, Release 15.0

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

## Updated Features

None.

## Important Notes

None.

## Deprecated Features

None.

## Removed and Unsupported Features

None.

## Third Party Software Impact

None.