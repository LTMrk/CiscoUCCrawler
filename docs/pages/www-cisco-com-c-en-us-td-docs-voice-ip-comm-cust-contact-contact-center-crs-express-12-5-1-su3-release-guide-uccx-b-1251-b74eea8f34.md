---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su3-release-guide-uccx-b-1251-b74eea8f34
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su3/release/guide/uccx_b_1251su3_solution-release-notes/uccx_b_1252solution-release-notes_chapter_011.html
retrieved_at: 2026-08-16T20:57:58.436054+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU3

# Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU3

Updated: May 8, 2023

Chapter: Cisco Finesse

## Chapter: Cisco Finesse

# Cisco Finesse

## New Features

### View Locked Out Users

To view the locked out users, a new CLI utils finesse locked_out_users list command is added. For more information, refer to the Desktop Properties section in the Cisco Finesse Administration Guide .

### Desktop Interface APIs

Three new APIs are introduced. These APIs can be used for desktop development. The new APIs are as follows:

Desktop Configuration

Languages List

Verify Desktop and Third-Party URLs

For more information on the APIs, see the Cisco Finesse Desktop Interface API Guide on DevNet .

## Updated Features

SystemInfo API is now authenticated when accessed through VPN-less reverse-proxy. To use alternatives in nonauthenticated
                              mode, refer to the Cisco Finesse Desktop Interface API Guide on DevNet .

## Important Notes

None.

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