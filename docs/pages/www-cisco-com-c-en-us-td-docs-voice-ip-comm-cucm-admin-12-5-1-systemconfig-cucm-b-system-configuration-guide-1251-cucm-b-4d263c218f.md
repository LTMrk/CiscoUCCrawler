---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-4d263c218f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_011100.html
retrieved_at: 2026-08-16T17:31:19.162327+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Call Admission Control Overview

## Chapter: Call Admission Control Overview

- Call Admission Control Overview

- About Call Admission Control

- Call Admission Control Configuration

# Call Admission Control Overview

## About Call Admission Control

Use call admission control (CAC) to regulate voice quality over a WAN link.

Voice quality can degrade when too many active calls exist on a link and the amount of bandwidth is oversubscribed. Call admission
                              control regulates voice quality by limiting the number of calls that can be active at the same time on a particular link.
                              Call admission control does not guarantee a particular level of audio quality on the link, but it does allow you to regulate
                              the amount of bandwidth that active calls on the link consume.

Call admission control operates by rejecting a call for bandwidth and policy reasons. When a call is rejected due to call
                              admission control, the phone of the called party does not ring, and the caller receives a busy tone. The caller also receives
                              a message on their phone, such as “Not enough bandwidth.” If you have enabled automated alternate routing (AAR), call admission
                              control automatically diverts calls to alternate public switched telephone network (PSTN) routes when WAN bandwidth is not
                              available.

## Call Admission Control Configuration

Choose from one of the following task flows to implement call admission control (CAC).

Task Flow

Description

Enhanced Locations Call Adminssion Control Task Flow

Use enhanced locations CAC in distributed deployments, where multiple clusters manage devices in the same physical sites
                                          using the same WAN uplinks. Enhanced locations CAC lets you regulate voice quality by limiting the amount of bandwidth that
                                          is available for calls over links between the locations. It also allows you to control call admissions for immersive video
                                          calls, such as TelePresence, separately from other video calls.

RSVP Configuration Task Flow

Use RSVP to implement call admission control in complex, multi-tiered topologies that include IP telephony and videoconferencing
                                          applications. RSVP is also able to handle dynamic changes to bandwidth.

| Task Flow | Description |
|---|---|
| Enhanced Locations Call Adminssion Control Task Flow | Use enhanced locations CAC in distributed deployments, where multiple clusters manage devices in the same physical sites
                                          using the same WAN uplinks. Enhanced locations CAC lets you regulate voice quality by limiting the amount of bandwidth that
                                          is available for calls over links between the locations. It also allows you to control call admissions for immersive video
                                          calls, such as TelePresence, separately from other video calls. |
| RSVP Configuration Task Flow | Use RSVP to implement call admission control in complex, multi-tiered topologies that include IP telephony and videoconferencing
                                          applications. RSVP is also able to handle dynamic changes to bandwidth. |