---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-installandupgrade-g-a00b722ec2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/installandupgrade/guide/ccvp_b_1262-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal_chapter_011.html
retrieved_at: 2026-08-21T11:56:37.533033+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Unified CVP Licensing

## Chapter: Unified CVP Licensing

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

## Specific License Reservation

Devices (product instances of Unified CVP ) that register with Smart Licensing have to share the license information with Cisco Smart Software Manager ( Cisco SSM ) at regular intervals. Your deployments that cannot periodically share license utilization data with Cisco SSM or due to regulatory reasons can use the Specific License Reservation feature. Cisco offers license reservation as an on-request configuration for such product instances.

You can reserve licenses (including add-on licenses) for your product instance on Cisco SSM . Specific License Reservation is enabled through the option License Management in the Unified CVP NOAMP portal.

The reserved licenses require no renewal or reauthorization unless there is a license usage change on the device. License
                                       reservation provides limited functionality to certain Smart Licensing features such as transfer of licenses between products,
                                       license usage, and asset management.

The Specific License Reservation (SLR) feature does not offer the following benefits that are available as part of the Smart
                                       Licensing feature:

Dynamic movement of license consumption between products

Real-time license usage visibility and asset management

Simplified product registration

Before uninstalling Cisco Unified Customer Voice Portal 12.6(2) to base versions 12.6(1) or 12.5(1), always make sure to return
                                       the license reservation if registered with SLR.

For more information, refer to the Smart Licensing section in the Administration Guide for Cisco Unified Customer Voice Portal 12.6(2) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

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

| Note | The reserved licenses require no renewal or reauthorization unless there is a license usage change on the device. License
                                       reservation provides limited functionality to certain Smart Licensing features such as transfer of licenses between products,
                                       license usage, and asset management. The Specific License Reservation (SLR) feature does not offer the following benefits that are available as part of the Smart
                                       Licensing feature: Dynamic movement of license consumption between products Real-time license usage visibility and asset management Simplified product registration Before uninstalling Cisco Unified Customer Voice Portal 12.6(2) to base versions 12.6(1) or 12.5(1), always make sure to return
                                       the license reservation if registered with SLR. |
|---|---|

| Note | For all Microapp-based applications (except GS Microapp), when the VXML/IVR ports usage exceeds the system capacity, the call
                                       gets disconnected gracefully. The GS Microapp puts the call on hold until license is available. |
|---|---|