---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-b5de23d8cb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_010110.html
retrieved_at: 2026-08-16T17:30:54.271101+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Translation Patterns

## Chapter: Configure Translation Patterns

# Configure Translation Patterns

## Translation Pattern Overview

You can configure translation patterns to manipulate digits for any type of call. Translation patterns follow the same general
                              rules and use the same wildcards as route patterns. As with route patterns, you assign a translation pattern to a partition.
                              However, when the dialed digits match the translation pattern, Cisco Unified Communications Manager  does not route the call
                              to an outside entity such as a gateway; instead, it performs the translation first and then routes the call again, this time
                              using the calling search space configured within the translation pattern.

## Translation Pattern Prerequisites

Before you configure a translation pattern, you must complete the following tasks:

Partition Configuration Task Flow

Call Routing Configuration Task Flow

For each translation pattern that you create, ensure that the combination of partition, route filter, and numbering plan is
                                          unique. If you receive an error that indicates duplicate entries, check the route pattern or hunt pilot, translation pattern,
                                          directory number, call park number, call pickup number, or meet-me number configuration windows.

## Translation Pattern Configuration Task Flow

Configure Translation Patterns

### Configure Translation Patterns

Configure translation patterns to apply digit manipulations to the calling and called numbers when the dial string matches
                                 the pattern. The system completes the digit translation and then reroutes the call.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Translation Pattern .

Step 2

Choose one of the following options:

- Click Add New to add a new translation pattern.

- Click Find , and select an exisiting translation pattern.

Step 3

In the Translation Pattern field, enter the pattern that you want the system to match to dial strings that use this pattern.

Step 4

From the Partition drop-down list, select the partition where you want to assign this pattern.

Step 5

Complete the remaining fields in the Translation Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 6

Click Save .

| Note | For each translation pattern that you create, ensure that the combination of partition, route filter, and numbering plan is
                                          unique. If you receive an error that indicates duplicate entries, check the route pattern or hunt pilot, translation pattern,
                                          directory number, call park number, call pickup number, or meet-me number configuration windows. |
|---|---|

| Command or Action | Purpose |
|---|---|
| Configure Translation Patterns | Configure translation patterns to specify how to route a call after it is placed. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Translation Pattern . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New to add a new translation pattern. Click Find , and select an exisiting translation pattern. |
| Step 3 | In the Translation Pattern field, enter the pattern that you want the system to match to dial strings that use this pattern. |
| Step 4 | From the Partition drop-down list, select the partition where you want to assign this pattern. |
| Step 5 | Complete the remaining fields in the Translation Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 6 | Click Save . |