---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-aa59554724
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_1251-configuration-guide-unified-cce/ucce_b_1251-configuration-guide-unified-cce_chapter_01110.html
retrieved_at: 2026-08-16T14:51:45.048417+00:00
---

Configuration Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Configuration Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Peripheral Terminology

## Chapter: Peripheral Terminology

- Peripheral Terminology

- Mapping to                              	 ACD-Specific Terminology

- Peripheral                              	 Terminology

# Peripheral Terminology

## Mapping to
                        	 ACD-Specific Terminology

The following table
                              		  summarizes the mapping of Unified Intelligent Contact Management (Unified ICM) terminology to ACD-specific terminology.

Unified ICM term

Peripheral-specific
                                             						equivalent

Agent

Agent

Peripheral
                                          					 target

Trunk group
                                          					 and DNIS

Service

Aspect Contact Center :
                                          					 Application

Avaya Communication
                                             						Manager : Vector Directory Number (VDN)

Skill group

Aspect Contact Center: Agent group

Avaya Communication Manager: Skill group or hunt group 3

Trunk group
                                          					 and DNIS

Trunk

Aspect Contact Center: Instrument 4

Trunk

Trunk
                                          					 group

Trunk
                                          					 group

In some cases the Unified ICM concept is very close to the corresponding ACD feature. For example, the Unified ICM concept of a service is very similar to the Aspect concept of an application.
                              		  In other cases, the ACD does not have a feature that maps exactly to the Unified ICM feature. In these cases, you might choose a different mapping than shown in the
                              		  above table. For example, although it might make sense to associate each VDN on
                              		  an Avaya Communication Manager with a Unified ICM service, you could also map each hunt group to a service.

On an Avaya
                              		  Communication Manager running in EAS mode, each skill group has primary and
                              		  secondary subgroups. The system software emulates this by automatically
                              		  creating additional skill groups for these peripheral types. For example, when
                              		  you configure the Sales skill group for an Avaya Communication Manager ACD, the
                              		  system software automatically creates the Sales.pri and Sales.sec skill groups
                              		  in addition to the base Sales group. In monitoring and scripts, you can
                              		  reference the .pri and .sec skill groups directly or you can refer to the base
                              		  skill group.

Some ACDs have
                              		  limitations that prevent them from making full use of specific features of the
                              		  system software.

Refer to the Pre-installation Planning Guide for Cisco Unified ICM for the current list of supported peripherals with any
                              		  peripheral-specific limitations.

## Peripheral
                        	 Terminology

Different peripheral
                              		  manufacturers use different terminology for agents, skill groups, and services.
                              		  For example, a service might be called an application, split, or gate. A skill
                              		  group might be called an agent group or hunt group.

For example, note
                              		  the following about using peripherals with Unified ICM :

The Aspect
                                    				contact center maps a trunk group and DNIS to a Call Control Table (CCT). The
                                    				DEFINITY ECS uses the trunk group and DNIS for incoming calls.

Without customer
                                    				controlled routing (CCR), one or more services map to an ACD DN. With CCR, one
                                    				or more services map to an ACD CDN.

If an ECS is
                                    				running in expert agent selection (EAS) mode, a skill group maps to an ECS
                                    				skill group; otherwise, it maps to a hunt group.

A contact center
                                    				instrument can be a trunk, a teleset, or a workstation.

| Unified ICM term | Peripheral-specific
                                             						equivalent |
|---|---|
| Agent | Agent |
| Peripheral
                                          					 target | Trunk group
                                          					 and DNIS |
| Service | Aspect Contact Center :
                                          					 Application Avaya Communication
                                             						Manager : Vector Directory Number (VDN) |
| Skill group | Aspect Contact Center: Agent group Avaya Communication Manager: Skill group or hunt group 3 Trunk group
                                          					 and DNIS |
| Trunk | Aspect Contact Center: Instrument 4 Trunk |
| Trunk
                                          					 group | Trunk
                                          					 group |

| Note | Multi-channel
                                       		  applications function as application instances. |
|---|---|