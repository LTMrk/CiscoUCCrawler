---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-cucm-b-feature-configuration-guide-for-cisco1251su1-cuc-1b851b8c5f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/cucm_b_feature-configuration-guide-for-cisco1251SU1/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_0111001.html
retrieved_at: 2026-08-16T17:20:44.722547+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Configure Call Throttling

## Chapter: Configure Call Throttling

# Configure Call Throttling

## Call Throttling Overview

Call Throttling allows 
                           		your system to automatically throttle or deny new call
                           		attempts. The system takes this action when conditions cause users to experience a delay in the interval between going off
                           hook and receiving a dial tone.

Some factors that can result in this delay are as follows:

Heavy call activity

Low CPU availability

Routing loops

Disk I/O limitations

Disk fragmentation

The system uses the values
                           		  that are specified in the call throttling parameters to determine a possible delay to dialtone and also to determine when
                           conditions no
                           		  longer require call throttling.

When throttling is necessary to prevent
                           		  excessive delay to dialtone, 
                           		  the system  enters a Code Yellow state and new
                           		  call attempts are throttled (denied).

When the system calculates the delay to dialtone as being over the threshold that is configured in the call throttling service
                           parameters, Unified Communications Manager rejects new calls. When call throttling activates, a user who attempts a new call
                           receives a reorder tone and, depending on the phone model, may also receive a prompt on the phone display.

Call throttling effectively prevents the type of excessive delays that can cause a user to complain to the system administrator
                           or question whether the system is
                           		  down or the phone is broken. 
                           		  Your system constantly
                           		  monitor the system to anticipate when such latency could occur.

When the delay to dialtone is within the guidelines of the call throttling service parameters, Unified Communications Manager
                           stops throttling calls by exiting the Code Yellow state and new calls are again allowed.

## Call Throttling Configuration Task Flow

Step 1

Configure Call Throttling

Enables Call throttling automatically when your system detects conditions such as heavy call activity, low CPU availability,
                                          and disk fragmentation.

Step 2

Configure Memory Throttling

Configures memory throttling for your system.

### Configure Call Throttling

Call throttling occurs automatically when your system detects conditions such as heavy call activity, low CPU availability,
                                 and disk fragmentation. The system automatically exits throttling when these conditions are fixed. Call Throttling is configured
                                 via advanced service parameters. For many deployments, the default settings are sufficient.

Caution

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose a server.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

Click Advanced .

Step 5

Under Call Throttling , configure values for the cll throttling service parameters. For parameter help descriptions, click the parameter name in
                                          the GUI.

- Code Yellow Entry Latency

- Code Yellow Exit Latency Calendar

- Code Yellow Duration

- Max Events Allowed

- System Throttle Sample Size

Step 6

Click Save .

### Configure Memory Throttling

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, select a Unified Communications Manager server.

Step 3

From the Service drop-down list, select Cisco CallManager .

Step 4

Click Advanced .

Step 5

Set the Enable Memory Throttling parameter to True .

Step 6

Configure values for the additional service parameters in the Memory Throttling area. For parameter help, click the parameter name in the GUI.

Step 7

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Call Throttling | Enables Call throttling automatically when your system detects conditions such as heavy call activity, low CPU availability,
                                          and disk fragmentation. |
| Step 2 | Configure Memory Throttling | Configures memory throttling for your system. |

| Caution | We recommend that you not modify call throttling parameters unless advised to do so by customer support. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose a server. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | Click Advanced . |
| Step 5 | Under Call Throttling , configure values for the cll throttling service parameters. For parameter help descriptions, click the parameter name in
                                          the GUI. Code Yellow Entry Latency Code Yellow Exit Latency Calendar Code Yellow Duration Max Events Allowed System Throttle Sample Size |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, select a Unified Communications Manager server. |
| Step 3 | From the Service drop-down list, select Cisco CallManager . |
| Step 4 | Click Advanced . |
| Step 5 | Set the Enable Memory Throttling parameter to True . |
| Step 6 | Configure values for the additional service parameters in the Memory Throttling area. For parameter help, click the parameter name in the GUI. |
| Step 7 | Click Save . |