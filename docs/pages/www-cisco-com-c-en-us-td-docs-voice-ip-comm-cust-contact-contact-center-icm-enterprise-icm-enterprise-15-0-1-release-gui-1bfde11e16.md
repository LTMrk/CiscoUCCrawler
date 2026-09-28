---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-1bfde11e16
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct_b_1501_cce-solutions-rns/rcct_m_1501_ccmp.html
retrieved_at: 2026-08-16T19:37:03.562128+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

# Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

Updated: April 30, 2025

Chapter: Cisco Unified Contact Center Management Portal

## Chapter: Cisco Unified Contact Center Management Portal

# Cisco Unified Contact Center Management Portal

## New Features

None.

## Updated Features

### Resource Manager Enhancements

The Resource Manager gadget now supports controlled provisioning of agents with disabled Active Directory (AD) accounts through the newly introduced 'AllowDisabledADUser' setting.

By default, provisioning an agent with a disabled AD user is not allowed, and the system displays the error message: “Supplied Domain Login Name Does Not Exist or It Is Disabled on Active Directory.”

Enabling the 'AllowDisabledADUser' setting in the Exony.Reporting.Application.Server.exe.config file allows provisioning even if the AD user is disabled.

### Improved ISE User Provisioning Handling

Provisioning an ISE user with a read-only admin account (configured in ICE for Unified Config Web Service API calls) in Unified
                              CCE now correctly enters an error state without affecting other provisioning requests. Previously, this caused errors without
                              logs, but now, other objects (for example, Agent, Agent Desktop) proceed to a ready state instead of getting stuck in a pending
                              active state.

### Provisioning Server Updates

The delete and update membership methods have been updated to use the Cluster Resource Type, ensuring consistency with the
                              existing create membership methods.

### Enhancements for Unified CCE 15 Schema Changes

Unified CCMP has been updated to incorporate schema changes introduced in Unified CCE 15.0(1) across all supported versions,
                              including Unified CCMP 12.5(x), 12.6(x), and 15.0(1). Key changes include:

Mapping Person to Webex Control Hub using WebexCiUUID to ensure seamless access to Webex services.

The following fields have been added to the Create and Edit Person and Agents pages in the legacy Resource Manager and the
                                    Resource Manager gadget: EmailAddress, DigitalChannelEnabled) .

### Cache Updates

The system has been optimized to reduce string duplicates in the memory cache.

### Support for 48000 Agent CCE Deployment

Unified CCMP now supports deployments of up to 48000 Agents, available for CCMP 12.6(1) and CCMP 15.0(1).

For CCMP 12.6(1), an update to ES13 is required, along with ensuring that hardware and software specifications meet the enhanced
                              scalability requirements.

## Important Notes

### Resolution for BSOD Issue

Users encountering a Blue Screen of Death (BSOD) issue after installing or upgrading to Contact Center Management Portal (CCMP)
                              15.0(1) must apply ES202508 or a later ES, which includes a fix for this issue.

## Deprecated Features

None.

## Removed and Unsupported Features

None.