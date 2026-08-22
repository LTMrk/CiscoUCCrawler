---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--5905c146d5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting-concepts-for-cisco-unified12_5/ucce_b_reporting-concepts-for-cisco-unified12_5_chapter_01100.html
retrieved_at: 2026-08-22T00:03:11.272937+00:00
---

Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Bucket Intervals for Cisco Unified Intelligence Center

## Chapter: Bucket Intervals for Cisco Unified Intelligence Center

- Bucket Intervals for Cisco Unified Intelligence Center

- Bucket Interval Reports

# Bucket Intervals for Cisco Unified Intelligence Center

## Bucket Intervals

Bucket intervals allow you to track data for calls
                              abandoned or answered within specific time increments. For example, you can track data for calls abandoned or answered between
                              0
                              and 8 seconds, or under 60 seconds.

Bucket intervals are associated with the following:

Call types

Skill groups

Precision queues

You can set bucket intervals  for the system as a whole and for individual call types, skill groups, and precision queues.
                              Settings for individual entities  override settings set at the system level.

Currently the global setting is available only for call types.

Service
                              level tells you what percentage of calls are being answered within a certain
                              time, but does not tell you how closely to the service level calls are being
                              answered or abandoned. Call type intervals provide more insight into how
                              long callers are waiting before their calls are answered or before they
                              abandon.

For example, if your service level is two minutes, you
                              might want to set up intervals for 30 seconds, one minute, 90 seconds, 120
                              seconds, 180 seconds, 210 seconds, and 240 seconds. Using these intervals, you
                              can see whether calls are being answered in the 30 seconds after the
                              service level threshold of 180 seconds or if most are waiting a full minute
                              longer to be answered.

The intervals also give you insight into
                              how long callers are willing to wait before abandoning. Many callers do
                              not abandon until two minutes past the service level. This might indicate that
                              you can modify your service level goal.

To avoid inconsistencies in reporting, create a new Bucket Interval List with your desired parameters. Follow this updated
                              Bucket Interval parameter for Call Types, Skill Groups or Precision Queues only at specific times (that is, end of the day,
                              week, or month). Ensure that no one is running the reports for the intervals, while you modify the boundaries.

### Bucket Interval Reports

The following  reports display
                                 bucket interval data:

Unified Intelligence Center: Call Type
                                       Abandon/Answer Distribution Historical

Skill Group Abandon/Answer Distribution

Precision Queue Abandon/Answer Distribution

| Note | Currently the global setting is available only for call types. |
|---|---|