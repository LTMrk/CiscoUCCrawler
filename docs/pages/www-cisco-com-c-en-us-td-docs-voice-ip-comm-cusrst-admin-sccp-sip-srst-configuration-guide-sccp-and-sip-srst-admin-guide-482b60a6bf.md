---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-482b60a6bf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_monitoring_and_maintaining.html
retrieved_at: 2026-08-21T02:49:39.020271+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Monitoring and Maintaining Cisco Unified SRST

## Chapter: Monitoring and Maintaining Cisco Unified SRST

- Monitoring and Maintaining Cisco Unified SRST

# Monitoring and Maintaining Cisco Unified SRST

## Monitoring and Maintaining Cisco Unified SRST

To monitor and maintain Cisco Unified Survivable Remote Site Telephony (SRST), use the following commands in privileged EXEC
                              mode.

Command

Purpose

Displays the detailed configuration of all the Cisco Unified IP phones, voice ports, and dial peers of the Cisco Unified SRST
                                       Router.

Displays the output of the dial peers of the Cisco Unified SRST Router.

Displays Cisco Unified IP Phone destination numbers when in Cisco Unified Communications Manager fallback mode.

Displays output for the voice ports.

Displays a summary of all voice dial peers.

Displays Cisco Unified IP Phone status.

Displays Cisco Unified IP Phone status for all phones that are off hook.

Displays Cisco Unified IP Phone status for all phones that are currently registered.

Displays Cisco Unified IP Phone status for all nonlocal phones (phones that have no Address Resolution Protocol [ARP] entry).

Displays Cisco Unified IP Phone status for all phones that are ringing.

Displays a summary of all Cisco Unified IP Phones.

Displays Unified IP Phone status for a specific phone number.

Displays Unified IP Phone status for all unregistered phones.

Displays Unified IP Phone destination numbers.

Displays a summary of all Cisco Unified IP Phone destination numbers.

Displays Cisco Unified IP Phone destination numbers in loopback mode.

Display the configuration.

Display SIP registrar clients.

Displays a summary of all voice ports.

Displays all SIP SRST configurations, SIP phone registrations, and dial peer information.

Displays voice register global config.

Displays all config SIP phone voice register Pool detail information.

Displays specific SIP phone voice register Pool detail information.

Displays SIP-SRST created dial peer.

Displays all config voice register directory number detail information.

Displays specific voice register directory number detail information.

| Command | Purpose |
|---|---|
| Router# show call-manager-fallback all | Displays the detailed configuration of all the Cisco Unified IP phones, voice ports, and dial peers of the Cisco Unified SRST
                                       Router. |
| Router# show call-manager-fallback dial-peer | Displays the output of the dial peers of the Cisco Unified SRST Router. |
| Router# show call-manager-fallback ephone-dn | Displays Cisco Unified IP Phone destination numbers when in Cisco Unified Communications Manager fallback mode. |
| Router# show call-manager-fallback voice-port | Displays output for the voice ports. |
| Router# show dial-peer voice summary | Displays a summary of all voice dial peers. |
| Router# show ephone phone | Displays Cisco Unified IP Phone status. |
| Router# show ephone offhook | Displays Cisco Unified IP Phone status for all phones that are off hook. |
| Router# show ephone registered | Displays Cisco Unified IP Phone status for all phones that are currently registered. |
| Router# show ephone remote | Displays Cisco Unified IP Phone status for all nonlocal phones (phones that have no Address Resolution Protocol [ARP] entry). |
| Router# show ephone ringing | Displays Cisco Unified IP Phone status for all phones that are ringing. |
| Router# show ephone summary | Displays a summary of all Cisco Unified IP Phones. |
| Router# show ephone telephone-number phone-number | Displays Unified IP Phone status for a specific phone number. |
| Router# show ephone unregistered | Displays Unified IP Phone status for all unregistered phones. |
| Router# show ephone-dn tag | Displays Unified IP Phone destination numbers. |
| Router# show ephone-dn summary | Displays a summary of all Cisco Unified IP Phone destination numbers. |
| Router# show ephone-dn loopback | Displays Cisco Unified IP Phone destination numbers in loopback mode. |
| Router# show running-config | Display the configuration. |
| Router# show sip-ua status registrar | Display SIP registrar clients. |
| Router# show voice port summary | Displays a summary of all voice ports. |
| Router# show voice register all | Displays all SIP SRST configurations, SIP phone registrations, and dial peer information. |
| Router# show voice register global | Displays voice register global config. |
| Router# show voice register pool all | Displays all config SIP phone voice register Pool detail information. |
| Router# show voice register pool tag | Displays specific SIP phone voice register Pool detail information. |
| Router# show voice register dial-peers | Displays SIP-SRST created dial peer. |
| Router# show voice register dn all | Displays all config voice register directory number detail information. |
| Router# show voice register dn tag | Displays specific voice register directory number detail information. |