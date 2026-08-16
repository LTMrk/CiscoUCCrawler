---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--d01dd589fc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/reporting-concepts-for-cisco-unified-icm-contact-center-enterprise-release-12-6-1/operational-reporting.html
retrieved_at: 2026-08-16T20:42:17.809190+00:00
---

Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

# Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

Updated: June 27, 2023

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