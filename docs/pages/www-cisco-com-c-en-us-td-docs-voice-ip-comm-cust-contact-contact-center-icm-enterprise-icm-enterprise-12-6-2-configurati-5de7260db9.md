---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-5de7260db9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_features-guide-1262/ucce_m_comm_mgr_extension_mobility-1261.html
retrieved_at: 2026-08-21T11:55:49.380889+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: April 30, 2025

Chapter: Unified Communications Manager Extension Mobility

## Chapter: Unified Communications Manager Extension Mobility

- Unified Communications Manager Extension Mobility

- Capabilities

- Configuration

# Unified Communications Manager Extension Mobility

## Capabilities

Extension Mobility is a Unified Communications Manager feature that you can use in Unified CCE . The feature enables users to temporarily configure a phone as their own by logging in to that phone. Once a user logs in,
                              the phone adopts the individual user device profile information, including line numbers, speed dials, services links, and
                              other user-specific properties of a phone.

Cisco Extension Mobility (EM) works on phones that are located within
                              		  the same Cisco Unified Communications Manager cluster. Cisco Extension Mobility
                              		  Cross Cluster (EMCC) works on phones that are located in different Cisco
                              		  Unified Communications Manager clusters.

The main documentation on this feature is in the Unified Communications Manager documentation. For more information, see the
                              following sources:

Information Type

Sources

Design considerations

Cisco Collaboration System
                                                   				  Solution Reference Network Designs at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html

Feature description and configuration

Feature Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

Extension Mobility API

https://developer.cisco.com/site/extension-mobility/

## Configuration

You configure EM and EMCC in the Cisco Unified Communications Manager. Take into account the following interactions between Unified CCE and Unified Communications Manager for successful implementation of EM and EMCC within a Unified CCE solution:

For Unified CCE configurations with multiline agent phone line control on the PG, configure all directory numbers for the user profile in
                                    Cisco Unified Communications Manager as follows:

Setting

Value

Maximum Number of Calls

2

Busy Trigger

1

For Unified CCE configurations with single-line agent phone line control on the PG, configure the secondary lines (but not the primary ACD
                                    line) for the directory number of the user profile in Cisco Unified Communications Manager as follows:

Setting

Value

Maximum Number of Calls

4

Busy Trigger

2

You cannot use phones with an IP Addressing Mode of IPv6 Only for Cisco Extension Mobility. If you want to use Cisco Extension Mobility with the phone, you must configure the phone with
                                    an IP Addressing Mode of IPv4 Only or IPv4 and IPv6 .

Agents can log in to multiple devices, depending on the Intra-cluster Multiple Login Behavior service parameter. You can set this parameter for EM implementations. EMCC implementations require that you set this parameter
                                    for multiple logins.

If an agent fails to log
                                    				out of a device, another agent  who attempts to access that device gets a "shared line" error. Follow these Unified Communications
                                    Manager
                                    				configuration guidelines to avoid shared line errors:

For EM implementations with hard phones, set the Intra-cluster Multiple Login Behavior Extension Mobility service parameter to "Auto Logout".

For EM implementations with a mix of hard and IP phones and
                                          					 for all EMCC implementations, limit the time that an agent can remain logged in to a device. Set the Intra-cluster Maximum LoginTime service
                                          					 parameter to the typical time that an agent
                                          					 remains logged in to a device during a shift.

For more information on Extension Mobility with Unified CCE , see UCCE Integration with CM Configuration Example at https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-enterprise/117777-config-ucce-00.html .

| Information Type | Sources |
|---|---|
| Design considerations | Cisco Collaboration System
                                                   				  Solution Reference Network Designs at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html |
| Feature description and configuration | Feature Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html |
| Extension Mobility API | https://developer.cisco.com/site/extension-mobility/ |

| Setting | Value |
|---|---|
| Maximum Number of Calls | 2 |
| Busy Trigger | 1 |

| Setting | Value |
|---|---|
| Maximum Number of Calls | 4 |
| Busy Trigger | 2 |