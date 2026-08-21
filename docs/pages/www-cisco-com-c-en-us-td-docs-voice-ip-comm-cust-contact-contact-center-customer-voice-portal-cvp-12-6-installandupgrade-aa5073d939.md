---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-installandupgrade-aa5073d939
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/installandupgrade/guide/ccvp_b_1261-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal_chapter_011.html
retrieved_at: 2026-08-21T17:04:02.464210+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: May 14, 2021

Chapter: Unified CVP Licensing

## Chapter: Unified CVP Licensing

- Unified CVP Licensing

- License Plan

- Unified CVP Redundant Port

# Unified CVP Licensing

## License Plan

Unified CVP now supports Smart Licensing which is a flexible software licensing model that streamlines the way you activate
                              and manage Cisco software licenses across your organization. For detailed feature overview on Smart Licensing, see Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

All Unified CVP servers, including Unified CVP server and VoiceXML server, need to register with Cisco SSM . Unified CVP OAMP and CVP Reporting server do not need any licensing registration.

### Upgrading from Classic License

After purchasing, the product licenses will be visible in your Smart Account. If you have a classic license, you will need
                              to convert the PAKs to Smart Account. For more information on converting your classic license to Smart Account, see https://software.cisco.com/web/fw/softwareworkspace/smartlicensing/ssmcompiledhelps/c_conversion_settings.html .

Unified CVP Call Server/VXML Server

Self Service Ports

Unified CVP Server license

The licenses for the ports on the Unified CVP Call Server and the Unified CVP VXML Server. A Unified CVP VXML Server license
                                          is for the number of self-service ports plus queued sessions.

Unified CVP Reporting Server

No License is required for the Unified CVP Reporting Server.

Unified CVP OAMP Server

No License is required for the Unified CVP OAMP Server.

Whenever Unified CVP is installed or upgraded, the Web Service Manager certificate from Unified CVP Call Server/Unified CVP
                                          VXML Server needs to be imported into the keystore of the Unified CVP OAMP/PCCE Server.

For information on the detailed steps, see the Unified CVP Security > Secure Communication between CVP and OAMP Server section of the Cisco CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

## Unified CVP Redundant Port

The Redundant Port supports a redundancy model in which one or more failover servers are available to take calls when the
                           primary servers are unavailable.

For example, if a customer has purchased 1500 Self-Service ports, these ports can be used across devices or locations or
                           servers. The customer is entitled to run only 1500 ports simultaneously. The total number of calls that receive queuing or
                           self-service treatment cannot exceed 1500.

For all Microapp-based applications (except GS Microapp), when the VXML/IVR ports usage exceeds the system capacity, the call
                                       gets disconnected gracefully. The GS Microapp puts the call on hold until license is available.

| Unified CVP Component | Required License |
|---|---|
| Unified CVP Call Server/VXML Server | Self Service Ports Unified CVP Server license The licenses for the ports on the Unified CVP Call Server and the Unified CVP VXML Server. A Unified CVP VXML Server license
                                          is for the number of self-service ports plus queued sessions. |
| Unified CVP Reporting Server | No License is required for the Unified CVP Reporting Server. |
| Unified CVP OAMP Server | No License is required for the Unified CVP OAMP Server. |

| Note | Whenever Unified CVP is installed or upgraded, the Web Service Manager certificate from Unified CVP Call Server/Unified CVP
                                          VXML Server needs to be imported into the keystore of the Unified CVP OAMP/PCCE Server. For information on the detailed steps, see the Unified CVP Security > Secure Communication between CVP and OAMP Server section of the Cisco CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
|---|---|

| Note | For all Microapp-based applications (except GS Microapp), when the VXML/IVR ports usage exceeds the system capacity, the call
                                       gets disconnected gracefully. The GS Microapp puts the call on hold until license is available. |
|---|---|