---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-d4c9140c47
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01001001.html
retrieved_at: 2026-08-16T17:36:49.131136+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Advanced Call Handling Overview

## Chapter: Advanced Call Handling Overview

- Advanced Call Handling Overview

- About Advanced Call Handling

- Advanced Call Handling Configuration

# Advanced Call Handling Overview

## About Advanced Call Handling

The chapters in this part describe different ways to configure advanced call handling in your system. With the functions outlined
                              in this part, you can configure how your system handles a call at any point in the call flow at a more granular level than
                              basic call handling features such as call forwarding. The task flow in this part lists each call handling function, describes
                              the purpose for configuring it, and links to the applicable chapter that provides further details.

## Advanced Call Handling Configuration

Complete the following task flows to configure advanced call handling for your system.

Step 1

APIC-EM Controller Configuration Task Flow

In order to manage network quality of service (QoS) for SIP calls, deploy a Cisco Application Policy Infrastructure controller
                                          Enterprise module (APIC-EM). APIC-EM applies DSCP markings to media flows created by communication sessions among Cisco Unified
                                          Communications Manager-managed SIP endpoints and trunks. Applying DSCP markings to media flows ensures that audio and video
                                          media will not be blocked by other lower priority network traffic such as email, print jobs, and software downloads.

Step 2

Call Control Discovery Configuration Task Flow

Configure call control discovery to advertise the Cisco Unified Communications Manager to other call control entities that
                                          use the Service Advertisement Framework (SAF) network. These call control entities can use the advertised information to dynamically
                                          configure their routing operations for the call.

Step 3

External Call Control Configuration Task Flow

Configure external call control to have an adjunct route server make call-routing decisions for your system. Unified Communications
                                          Manager issues a route request to an adjunct route server, which provides instructions about how to route the call, along
                                          with any additional call treatment to apply.

Step 4

Call Queuing Task Flow

Configure call queueing to place callers in a queue until hunt members are available to answer them.

Step 5

Call Throttling Configuration

Configure call throttling to automatically throttle or deny new call attempts when system conditions can cause users to experience
                                          a delay in the interval between going off hook and receiving a dial tone. We recommend that you not modify call throttling
                                          parameters unless advised to do so by Cisco customer support.

Step 6

Calling Party Normalization Configuration Task Flow

Configure calling party normalization to reformat incoming phone numbers so that they display on the recipient's phone as
                                          globalized or localized phone numbers. Use this feature to improve callback functionality when a call is routed to multiple
                                          geographic locations, and to map a global calling party number to its localized variant so that a phone can return a call
                                          without modifying the directory number in the call log directories on the phone.

Step 7

Logical Partitioning Configuration Task Flow

Configure logical partitioning to satisfy regulatory requirements in markets where toll bypass is forbidden. For example,
                                          you can configur ea policy prevent users from initiating restricted calls by using midcall features such as conference join
                                          and redirect.

Step 8

Geolocation and Location Conveyance Task Flow

Specify a geolocation for every device and communicate geolocation information across clusters. Geolocations assign a civic
                                          address to devices so that communication between devices can be controlled based on legal requirements in certain countries.

Step 9

Location Awareness Configuration Task Flow

Location Awareness allows administrators to determine the physical location from which a phone connects to the company
                                          network.

Step 10

AAR Configuration Task Flow

Step 11

Multilevel Precendence and Preemption Task Flow

Configure Multilevel Precedence and Preemption (MLPP) if you want to allow validated users to place priority calls. If necessary,
                                          these users can preempt lower priority phone calls.

Step 12

Two Stacks (IPv4 and IPv6) Configuration Task Flow

If you want your endpoints to be able to support both IPv4 and IPv6 addressing, complete these tasks to configure two
                                          stack support for endpoints.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | APIC-EM Controller Configuration Task Flow | In order to manage network quality of service (QoS) for SIP calls, deploy a Cisco Application Policy Infrastructure controller
                                          Enterprise module (APIC-EM). APIC-EM applies DSCP markings to media flows created by communication sessions among Cisco Unified
                                          Communications Manager-managed SIP endpoints and trunks. Applying DSCP markings to media flows ensures that audio and video
                                          media will not be blocked by other lower priority network traffic such as email, print jobs, and software downloads. |
| Step 2 | Call Control Discovery Configuration Task Flow | Configure call control discovery to advertise the Cisco Unified Communications Manager to other call control entities that
                                          use the Service Advertisement Framework (SAF) network. These call control entities can use the advertised information to dynamically
                                          configure their routing operations for the call. |
| Step 3 | External Call Control Configuration Task Flow | Configure external call control to have an adjunct route server make call-routing decisions for your system. Unified Communications
                                          Manager issues a route request to an adjunct route server, which provides instructions about how to route the call, along
                                          with any additional call treatment to apply. |
| Step 4 | Call Queuing Task Flow | Configure call queueing to place callers in a queue until hunt members are available to answer them. |
| Step 5 | Call Throttling Configuration | Configure call throttling to automatically throttle or deny new call attempts when system conditions can cause users to experience
                                          a delay in the interval between going off hook and receiving a dial tone. We recommend that you not modify call throttling
                                          parameters unless advised to do so by Cisco customer support. |
| Step 6 | Calling Party Normalization Configuration Task Flow | Configure calling party normalization to reformat incoming phone numbers so that they display on the recipient's phone as
                                          globalized or localized phone numbers. Use this feature to improve callback functionality when a call is routed to multiple
                                          geographic locations, and to map a global calling party number to its localized variant so that a phone can return a call
                                          without modifying the directory number in the call log directories on the phone. |
| Step 7 | Logical Partitioning Configuration Task Flow | Configure logical partitioning to satisfy regulatory requirements in markets where toll bypass is forbidden. For example,
                                          you can configur ea policy prevent users from initiating restricted calls by using midcall features such as conference join
                                          and redirect. |
| Step 8 | Geolocation and Location Conveyance Task Flow | Specify a geolocation for every device and communicate geolocation information across clusters. Geolocations assign a civic
                                          address to devices so that communication between devices can be controlled based on legal requirements in certain countries. |
| Step 9 | Location Awareness Configuration Task Flow | Location Awareness allows administrators to determine the physical location from which a phone connects to the company
                                          network. |
| Step 10 | AAR Configuration Task Flow | Configure your system to automatically reroute calls through the PSTN or other networks when your system blocks a call due
                                       to insufficient location bandwidth. With automated alternate routing, the caller does not need to hang up and redial the called
                                       party. |
| Step 11 | Multilevel Precendence and Preemption Task Flow | Configure Multilevel Precedence and Preemption (MLPP) if you want to allow validated users to place priority calls. If necessary,
                                          these users can preempt lower priority phone calls. |
| Step 12 | Two Stacks (IPv4 and IPv6) Configuration Task Flow | If you want your endpoints to be able to support both IPv4 and IPv6 addressing, complete these tasks to configure two
                                          stack support for endpoints. |