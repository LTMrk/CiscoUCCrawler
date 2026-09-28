---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-release-guide-uccx-b-1251-fa817d48ad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/release/guide/uccx_b_1251su1solution-release-notes/uccx_b_1252solution-release-notes_chapter_011.html
retrieved_at: 2026-08-16T21:01:23.787400+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU1

# Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU1

Updated: January 31, 2021

Chapter: Cisco Finesse

## Chapter: Cisco Finesse

# Cisco Finesse

## New Features

### Multi-Tab Gadget

This release supports configuring multiple gadgets within a single gadget called the Multi-Tab gadget. The Multi-Tab gadget
                              allows rendering of multiple gadgets, accessible through tabs, in a single desktop view. Shortcut keys can be used to switch
                              between different gadgets tabs easily, so that information presented by each gadget can be accessed in a fast and convenient
                              manner.

With Multi-Tab gadget, you do not have to scroll down the page or navigate between desktop container tabs to see additional
                              information. Gadget tabs are lined up horizontally on the Multi-Tab gadget header, enabling you to access information readily.
                              Multiple instances of Multi-Tab gadgets are supported, which allows you to stack groups of gadgets to customize your desktop.

The Multi-Tab gadget cannot host the Advanced Capabilities gadget and the Manage Chat and Email gadget.

For more information about the Multi-Tab gadget, see the Multi-Tab Gadgets section in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

### New Capabilities for Gadgets in the Multi-Tab Gadget

This release introduces the following desktop capabilities for gadgets when hosted in a Multi-Tab Gadget:

Gadget Notifications

Hide/Unhide Gadgets

Maximize support

Call Control as a Tabbed Gadget

For more information, see the Cisco Unified Contact Center Express Administration and Operations Guide and the Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html and https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html , respectively.

### Connected Agents Gadget

This release introduces the Connected Agents gadget for administrators that lists all the agents currently signed in to Cisco
                                 Finesse. You can use this gadget to determine which agents are signed in to the Publisher and the Subscriber. You can use
                                 this gadget also to filter the client types and identify the client type through which an agent has signed in.

For more information, see the Manage Connected Agents section in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Serviceability Improvements

This release provides the following serviceability improvements:

Trace level logging support ( utils finesse log )

Fine-grained logging control for critical services ( utils finesse log )

ConnectedUsersInfo API to retrieve the list of users signed in to a specific node

Finesse Maintenance Mode Services ( utils finesse maintenance initiate and utils finesse maintenance status )

For more information about logging improvements and Finesse Maintenance Mode Services, refer to the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

For more information about the ConnectedUsersInfo API, see the ConnectedUsersInfo section in the Cisco Finesse Web Services Developer and JavaScript Guide at https://developer.cisco.com/docs/finesse/ .

## Updated Features

## Important Notes

## Deprecated Features

### Notifications over BOSH (Long Polling)

In this release, support for notifications over BOSH (long polling) is deprecated. Notifications over direct XMPP (over TCP)
                              and Websocket-based transports are the replacements.

## Removed and Unsupported Features

### Cisco Finesse Trace Logging

In this release, the following CLIs are removed:

utils finesse trace enable

utils finesse trace disable

The replacement is the utils finesse log commands that are used to add, delete, update, or view a custom log configuration in the Cisco Finesse system.

## Third Party Software Impacts

None.

| Note | The Multi-Tab gadget cannot host the Advanced Capabilities gadget and the Manage Chat and Email gadget. |
|---|---|