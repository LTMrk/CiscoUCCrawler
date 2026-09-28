---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--fc170fdb8e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting-concepts-for-cisco-unified12_5/ucce_b_reporting-concepts-for-cisco-unified12_5_chapter_011.html
retrieved_at: 2026-08-22T00:02:33.769878+00:00
---

Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Why  Report Data Can Differ

## Chapter: Why  Report Data Can Differ

# Why  Report Data Can Differ

## Automatic Call Distributor and Unified Contact Center Enterprise Reports

Data collected and presented in Unified CCE reports to measure customer experience and agent performance differs from data collected and presented in ACD reports. This is also the case for parent/child reporting in a Unified CCE deployment.

Unified CCE reports give an enterprise-wide view of all your call centers. Each ACD report is specific to a particular call center. For most accurate data, report at the source.

Here are some of the reasons that
                              cause variations:

Differences due to timing and transmission delays. All times computed in Unified CCE reports, such as various state transitions, are based on event arrival time at Unified CCE Central Controller, not on the actual event occurrence on the ACD. Network transmission delays cause variations in reported
                                    times between reporting data seen on Unified CCE reports and ACD reports.

Differences in supported concepts and terminology. Differences in supported concepts and the way that similar concepts are
                                    implemented can cause variations in the data available to measure agent
                                    performance and customer experience.

For example, while Unified CCE and an ACD might both support the concept of agent states, the ACD might not support as many state options as Unified CCE software. In addition, some similarly named agent states might not have the same definition on both systems.

Differences in configuration. Differences in configuration on the ACD and the Configuration Manager can lead
                                    to discrepancies in reporting. If devices are not configured in Configuration
                                    Manager or if they are configured with different settings than on the ACD,
                                    reports might not track certain statistics at all or might report different
                                    metrics.

Different methods of measuring and storing data. Unified CCE and the ACD might differ in how data segments are defined and counted. One example is how the individual agent's time is
                                    measured and stored in relation to how that agent's time spent in a conference call is measured and stored.

Different methodologies for sampling data. For example, Unified CCE and the ACD might differ as to when an event is considered to start and to end.

Differences in terminology and in the definitions of data elements. On the surface, naming conventions might appear to be the same but, in fact, are not. For example, Unified CCE and the ACD might use different criteria to evaluate what constitutes an 'offered call'.

Refer to the ACD Supplement Guides for details.

## Real Time and Historical Reports

Counts in real time data (for example CallsHandledTo5) do not
                              match up with counts in the historical interval records (for example,
                              CallsHandled) because the real time data is moved to the historical database at
                              the end of each half-hour interval.

Consider this
                              example: at 8:55 a call comes into the contact center and is answered by an
                              agent.

The real time count for CallsAnswered
                                    increases by one (+1).

Between 8:55 and 9:00, the
                                    real time data shows the answered call.

The answered call
                                    does not populate the Historical half-hour data until 9:00, when the 8:30 to 8:59:59
                                       interval ends .

## Interval Boundaries

Counts that would typically match up for a day, such as
                              CallsOffered and CallsHandled, might not always match up over specific intervals. This discrepancy occurs because the counts
                              for some data
                              elements might be increased across boundaries.

Consider this example: at 8:55, a call comes in to the contact
                              center and is answered by an agent. The agent completes the call at
                              9:05.

In the historical database, the call is counted
                                    as offered in the 8:30:00 to 8:59:59 interval.

The call
                                    is counted as handled in the 9:00:00 to 9:29:59 interval.

If you run a report for the 9:00:00 to 9:29:59 interval, it appears that
                                    tasks handled does not equal tasks offered for the interval.

You also might notice that tasks offered does not equal task abandoned +
                              tasks handled for an interval. Tasks offered reflects the number of
                              calls and tasks that were offered to agents in this interval, while tasks
                              handled and tasks abandoned might include calls that were offered in the last
                              interval and completed in this interval. Some historical report templates group
                              statistics into "Completed Tasks" to indicate that the statistics represent all
                              calls and tasks that completed in this interval.

In
                              general, interval boundary issues are reduced if you run daily reports.
                              However, if your contact center runs 24 hours a day, you might still notice
                              discrepancies for intervals such as  the 11:30:00 to 11:59:59 and 12:00:00 to 12:29:59
                              intervals.

## Skill Group and Enterprise Skill Group Reports

You can expect double
                              counting in Enterprise Skill Group reports when a call is queued to multiple
                              skill groups on the same peripheral and those skill groups  are associated with
                              the same Enterprise Skill Group.

## Call Type, Skill Group, Precision Queue, and Service Reports

Do not compare Call Type reports to Skill Group, Precision Queue, or Service reports. Skill Group, Precision Queue, and Service
                              reports might have statistics for calls that were routed directly to the ACD and not routed by Unified CCE .

Certain statistics are computed differently when Enterprise queues
                              are used.

In Unified CCE with ACD environments, services define call treatment. All skill groups belong to specific services and, therefore, skill
                              group data rolls up to the service. Reports for services provide call treatment information for all of the skill groups assigned
                              to those services.

Call Type reports in Unified CCE primarily provide call routing statistics and contain no other call handing statistics, unless they used translation routing.
                              You might notice that data for a Call Type and the skill groups or Precision Queues related to the Call Type through a routing
                              script do not match. If a skill group or Precision Queue is used in multiple scripts, reporting for that skill group or Precision
                              Queue includes data for all of the Call Types to which it is assigned. If a Call Type routes to multiple skill groups or Precision
                              Queues, data for the Call Type is distributed among those skill groups or Precision Queues.

## Reports That Show
                        	 Base Skill and Sub-skill Groups

Some ACDs available to Unified CCE support the concept of prioritized skill groups (subskill groups). For these ACDs, Configuration Manager supports this concept
                              and allows you to distinguish priority levels (primary, secondary, and so forth) of a base Skill Group.

The Configuration Guide for Cisco Unified ICM/Contact Center Enterprise lists these ACDs.

When subskill groups are configured, Unified CCE configuration creates a base skill group for these subskills. If subskill groups exist, when you generate a report from the
                              Agent By Skill Group and Skill Group By Peripheral categories, select the sub-skill groups (and not the base skill groups)
                              from the Skill Groups item-selection list.

If you select both
                              		  the base skill group and the corresponding subskill groups from the Skill
                              		  Groups item-selection list, the reports display data for both base and
                              		  subskill groups, making the report summaries incorrect. (The data in the base
                              		  skill group is a roll-up of data from the subskills.)

If no subskill
                              		  groups are configured, select the base skill group from the Skill Groups
                              		  item-selection list.

For Skill Group By
                              		  Enterprise reports, determine which skill groups to include in the
                              		  Enterprise skill group. If you configured subskill groups from several
                              		  peripherals or from different media, group only the subskill groups into the
                              		  Enterprise Skill Group and not both base and subskill groups.

| Note | Subskill groups are not supported for Unified CCE . |
|---|---|