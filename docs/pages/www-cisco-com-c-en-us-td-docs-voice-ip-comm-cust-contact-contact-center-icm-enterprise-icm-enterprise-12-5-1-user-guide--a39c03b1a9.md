---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--a39c03b1a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting-concepts-for-cisco-unified12_5/ucce_b_reporting-concepts-for-cisco-unified12_5_chapter_010001.html
retrieved_at: 2026-08-22T00:03:32.617715+00:00
---

Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Operational Reporting

## Chapter: Operational Reporting

- Operational Reporting

- Trunks and Trunk Groups

# Operational Reporting

## Trunks and Trunk Groups

Every peripheral has one or more associated trunk groups, with
                              each trunk group containing one, or more physical trunks.

You
                              configure trunks and trunk groups with the Configuration Manager.

You can
                              report on data such as the number of trunks in service, number of trunks idle,
                              and the time during which all trunks in a trunk group were simultaneously busy
                              (All Trunks Busy).

The following report
                              contains operational information on trunk groups:

Unified Intelligence Center IVR Ports Performance Historical Report

| Note | Not all ACDs support trunk configuration. If your ACD does, make sure that the
                                       PG is accurately configured in Configuration Manager. For the ICM software to
                                       properly monitor ACD calls, all individual trunks and their corresponding trunk
                                       group assignments must be configured in the ICM database. |
|---|---|