---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-basic-config-exwy-b-cisco-expressway-e-and-exp-9c66d0416c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/basic_config/exwy_b_cisco-expressway-e-and-expressway-c-basic-configuration-deployment-guide-x14-0/exwy_m_firewall-and-nat-settings.html
retrieved_at: 2026-08-16T15:28:09.697890+00:00
---

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

# Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

Updated: April 14, 2021

Chapter: Firewall and NAT Settings

## Chapter: Firewall and NAT Settings

# Firewall and NAT Settings

## Firewall and NAT Settings

Port reference information is now maintained in a separate document.

See the Cisco Expressway IP Port Usage Configuration Guide , for your version, on the Cisco Expressway Series Configuration Guides page.

## Internal Firewall Configuration

Ensure that any SIP or H.323 "fixup" ALG or awareness functionality is disabled on the NAT firewall – if enabled this will adversely interfere with the Expressway
                           functionality.

As Expressway-C to Expressway-E communications are always initiated from the Expressway-C to the Expressway-E (Expressway-E
                           sending messages by responding to Expressway-C’s messages) no ports need to be opened from DMZ to Internal for call handling.

However, if the Expressway-E needs to communicate with local services, such as a Syslog server, some firewall configuration
                           may be required.

Traffic destined for logging or management server addresses (using specific destination ports) must be routed to the internal
                           network.

## External Firewall Configuration Requirement

Ensure that any SIP or H.323 "fixup" ALG or awareness functionality is disabled on the NAT firewall – if enabled this will adversely interfere with the Expressway
                           functionality.

If you want to restrict communications from the DMZ to the wider Internet, see the connection maps and port reference tables
                           in the Cisco Expressway IP Port Usage Guide to make sure you allow legitimate traffic.