---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-ucce-b-eb37a0a1f7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/ucce_b_1262_outbound_options_guide/ucce_m_1262_outbound-option-installation-preliminary-steps.html
retrieved_at: 2026-08-16T20:32:39.470797+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

Updated: August 19, 2025

Chapter: Outbound Option Installation Preliminary Steps

## Chapter: Outbound Option Installation Preliminary Steps

# Outbound Option Installation Preliminary Steps

## Before You Begin

Review Cisco Outbound Option Description in the Solution Design Guide for Cisco Unified Contact Center Enterprise to learn about  deployment options and other design considerations.

The following sections discuss considerations for Outbound Option installations.

### System Requirements

System requirements
                                 		  for Outbound Option include the following:

Choose a Region on Windows Server that includes a 12-hour time format. Outbound Option assumes that times are in a 12-hour
                                       format. If you choose a Region that only has a 24-hour format, such as Spanish (Spain), the Outbound Option configuration
                                       tools do not work properly.

A working
                                       				Unified CCE system that has the following:

Router and Logger

Administration & Data Server

Agent PG , Unified CCE Generic PG, or System PG

MR PG

CTI Server

Unified CM connectivity with agents and CTI Route Points

If you plan to use the transfer to VRU feature, configure a VRU deployment that supports transfer to VRU. See your Unified
                                       CVP, Unified CCX, or third-party VRU documentation for instructions.

Your system must
                                       				meet the hardware and software requirements as listed in the following
                                       				documents:

Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html

Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html

Only T1 PRI and E1 PRI interfaces to the PSTN are supported for Outbound Option SIP dialers.

T1 PRI, E1 PRI and CUBE interfaces to the PSTN are supported for Outbound Option SIP dialers. BRI, FXO, E1R2 will not work
                                       with Dialer.

### Outbound Option Database

If you enable Outbound Option High Availability, ensure that the Logger virtual machine datastore is large enough to accommodate
                              both the Logger database and the Outbound Option database on Logger Side A and Logger Side B. For more information on drive
                              space, see Outbound Option High Availability

### VRU Integration

The Dialer uses the VRU for unassisted treatment of customer calls depending on campaign configuration for abandoned calls,
                                 answering machine treatment in an agent campaign, or for unassisted transfer to VRUcampaigns.

Unified CVP deployments might require Media Termination Point (MTP) resource allocations for calls that are transferred to
                                 the VRU from the dialer.

### Auto Answer Settings

Outbound Option is flexible when configuring auto-answer, depending on the
                                 system requirements. The main determining factor is whether the business requires
                                 the Outbound Option agent to hear a zip tone. Using an agent zip tone increases the transfer time line by almost one second.