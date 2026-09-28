---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--24552c27af
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/ucce_b_ucce_b_outbound-option-guide-for-unified_1261/ucce_m_maintenance-mode.html
retrieved_at: 2026-08-16T20:39:46.368961+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(1)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(1)

Updated: August 22, 2023

Chapter: Graceful Shutdown

## Chapter: Graceful Shutdown

- Graceful Shutdown

- Dialer Behavior During Graceful Shutdown

# Graceful Shutdown

## Dialer Behavior During Graceful Shutdown

The graceful shutdown feature allows you to perform firmware upgrades, apply security patches, and apply engineering specials
                           (ES) without the need for a maintenance window. With this feature, actively used processes can be brought down while the backup
                           processes take over, with minimal impact to the contact center. When you place the Unified CCE Outbound Option Dialer into
                           maintenance mode, dialer calls and reporting are not impacted.

When you place the Dialer into maintenance mode, it temporarily pauses new dialing while it transitions responsibility to
                           the standby dialer. The standby dialer activates when all calls ringing at the customer have been transferred to an agent
                           or IVR, or terminated due to customer busy or no answer. The amount of time it takes for the active dialer to shut down is
                           generally the time configured for the longest Ring No Answer.

For predictive and progressive campaigns, any reserved agents are unreserved after the dialer attempts in progress are completed
                           or transferred to agents or IVR.

For preview campaigns or personal callbacks, the dialer waits for agents to accept or reject the last contact in progress.

The maintenance mode dialer continues to monitor dialer calls that are connected to agents until completion, for up to 90
                           minutes. After the calls are complete, the maintenance mode dialer shuts down.

When the Unified CCE Enterprise Media Routing PG or Agent PG is placed into maintenance mode and shuts down, dialer calls
                           and reporting are not impacted. For more information, see the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .