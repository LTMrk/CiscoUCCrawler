---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-systemconfig-cucm-b-system-configuration-guide-1251su3--5bc83b0552
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/systemConfig/cucm_b_system-configuration-guide-1251su3/cucm_m_configure-ipv6-stack-1201.html
retrieved_at: 2026-08-16T17:40:53.488917+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Configure IPv6 Stack

## Chapter: Configure IPv6 Stack

# Configure IPv6 Stack

## IPv6 Stack Overview

IPv6 is an expanded IP addressing protocol that uses 128 bits
                              instead of the 32 bits that IPv4 addresses use. IPv6 provides a
                              much broader range of IP address than IPv4, which greatly reduces
                              the risk of IP address exhaustion, which is among the main concerns
                              with IPv4 addressing.

By default, Cisco Unified Communications Manager is configured
                              to use IPv4 addressing. However, you can also configure the system
                              to support the IPv6 stack thereby allowing you to deploy a SIP
                              network with IPv6-only endpoints. In addition to reducing the risk
                              of IP address exhaustion, IPv6 provides some of the following
                              benefits:

Stateless address autoconfiguration

Simplified multicasting functionality

Simplified routing, minimizing the need for routing tables

Delivery of services optimization

Better handling of mobility

Greater privacy and security

### IPv6 at the System Level

If you are deploying an IPv6 network, the Cisco Unified
                              Communications Manager server still uses IPv4 for some internal
                              communications. This is because some internal system components and
                              applications support only IPv4. As a result, even if all of your
                              devices operate in IPv6-only mode, the Cisco Unified Communications
                              Manager server will still have both an IPv4 and IPv6 address as the
                              server must use IPv4 for some internal communications.

If you need your SIP devices to operate in both IPv4 and IPv6 networks, you will need to configure two stacks. After you complete
                                          the tasks in this chapter to enable the IPv6 stack in Cisco Unified Communications Manager, you will then have to also enable
                                          your SIP network for two stacks. See Two Stacks (IPv4 and IPv6) Overview .

## IPv6 Prerequisites

Before you configure Cisco Unified Communications Manager with  IPv6 support, you must configure the following network servers
                           and devices to support IPv6. For details, refer to your device user documentation:

Provision a DHCP and DNS server with IPv6 support. The Cisco Network Registrar server supports IPv6 for DHCP and DNS.

Configure the IOS for network devices such as gateways, routers, and MTPs with IPv6 support.

Configure your TFTP server to run IPv6.

## IPv6 Configuration Task Flow

Complete the following tasks to configure the system for IPv6.

Step 1

Configure IPv6 in Operating System

Configure the operating system with support for IPv6 addresses.

Step 2

Configure Server for IPv6

Configure the servers in your cluster with IPv6 addresses.

Step 3

Enable IPv6

Configure enterprise parameters that enable the system for IPv6.

Step 4

Perform any of the following:

- Configure IP Addressing Preference for Cluster

- Configure IP Addressing Preferences for Devices

You can configure an enterprise parameter to assign a clusterwide IP Addressing preference.

If you want to assign different preferences for different groups of endpoints, configure the addressing preference within
                                          a Common Device Configuration.

Configure cluster settings for which IP addressing method is preferred.

Step 5

Restart Services

Restart the following network services:

Cisco CallManager

Cisco CTIManager

Cisco IP Voice Media Streaming App

Cisco Certificate Authority Proxy Function

### What to do next

To configure dual stack trunks, refer to the chapters for configuring SIP trunks.

To configure dual stack for SIP devices, refer to the sections for the SIP devices that you want to configure.

### Configure IPv6 in Operating System

Use this procedure to set up Ethernet IPv6 in Cisco Unified OS Administration.

Use Cisco IOS IPv6 DHCP server because the IPv6 DHCP server configuration is not supported on Windows.

Step 1

From Cisco Unified OS Administration, choose Settings > IPv6 > Ethernet .

Step 2

Check the Enable IPv6 check box.

Step 3

From the Address Source drop-down list box, configure how the system acquires the IPv6 address:

- Router Advertisement —The system uses stateless autoconfiguration to acquire an IPv6 address.

- DHCP —The system acquires an IPv6 address from a DHCP server.

- Manual Entry —Choose this option if you want to enter the IPv6 address manually.

Step 4

If you have configured Manual Entry as the means of acquiring an IPv6 address, complete the following fields:

- Enter an IPv6 Address . For example, fd62:6:96:2le:bff:fecc:2e3a .

- Enter an IPv6 Mask . for example, 64 .

Step 5

Check the Update with Reboot check box to ensure that the system reboots after you save.

Step 6

Click Save .

### Configure Server for IPv6

Configure the servers in your cluster with IPv6 addresses.

Step 1

From Cisco Unified CM Administration, choose System > Server .

Step 2

In the IPv6 Address (for dual IPv4/IPv6) field, enter one of the following values:

- If you have DNS configured, and your DNS server supports IPv6, enter the server IP address.

- Otherwise, enter the non-link local IPv6 address.

Step 3

Click Save .

Step 4

Repeat these steps for each cluster node.

### Enable IPv6

If you want to set up IPv6 support in your system, you must enable the system to support IPv6 devices.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

Set the value of the Enable IPv6 enterprise parameter to True .

Step 3

Click Save .

#### What to do next

Configure IP addressing preferences for the devices in your cluster. You can apply settings via a clusterwide enterprise parameter
                                 or you can use a Common Device Configuration to apply settings to a group of devices that uses that configuration:

Configure IP Addressing Preference for Cluster

Configure IP Addressing Preferences for Devices

### Configure IP Addressing Preference for Cluster

Use this procedure
                                 		  to use enterprise parameters to configure clusterwide IP addressing preferences
                                 		  for  IPv6. The system applies these settings to all SIP trunks and
                                 		  devices unless an overriding Common Device Configuration is applied
                                 		  to a specific trunk or device.

The IP address preferences in a Common Device Configuration override the clusterwide enterprise parameter settings for the
                                             devices that use that Common Device Configuration.

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Enterprise
                                                				  Parameters .

Step 2

Set the value
                                          			 of the IP
                                             				Addressing Mode Preference for Media enterprise parameter to IPv4 or IPv6

Step 3

Set the value
                                          			 of the IP
                                             				Addressing Mode Preference for Signaling enterprise parameter to IPv4 or IPv6 .

Step 4

Click Save .

### Configure IP Addressing Preferences for Devices

You can configure IP addressing preferences for individual devices by configuring a Common Device Configuration with the preference
                                 settings. You can apply the Common Device Configuration to SIP and SCCP devices that support IPv6 addressing such as trunks,
                                 phones, conferences bridges, and transcoders.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration .

Step 2

Click Add New .

Step 3

For SIP trunks, SIP Phones or SCCP phones, choose a value for the IP Addressing Mode drop-down list:

- IPv4 Only —The device uses only an IPv4 address for media and signaling.

- IPv6 Only —The device uses only an IPv6 address for media and signaling.

- IPv4 and IPv6 (Default) —The device is a dual-stack device and uses whichever IP address type is available. If both IP address types are configured
                                             on the device, for signaling the device uses the IP Addressing Mode Preference for Signaling setting and for media the device uses the IP Addressing Mode Preference for Media enterprise parameter setting.

Step 4

If you configure IPv6 in your previous step, then configure an IP addressing preference for the IP Addressing Mode for Signaling drop-down list:

- IPv4 —The dual stack device prefers IPv4 address for signaling.

- IPv6 —The dual stack device prefers IPv6 address for signaling.

- Use System Default —The device uses the setting for the IP Addressing Mode Preference for Signaling enterprise parameter.

Step 5

Configure the remaining fields in the Common Device Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 6

Click Save .

#### What to do next

If your IPv6 configuration is complete, Restart Services .

If you want your SIP devices to support both IPv4 and IPv6 networks simultaneously, you must configure the system to support
                                 both stacks at the device level. For details, see Two Stacks (IPv4 and IPv6) Overview .

### Restart Services

After configuring your system for IPv6, restart essential services.

Step 1

Log into Cisco Unified Serviceability and choose Tools > Control Center - Feature Services .

Step 2

Check the check box corresponding to each of the following services:

- Cisco CallManager

- Cisco CTIManager

- Cisco Certificate Authority Proxy Function

- Cisco IP Voice Media Streaming App

Step 3

Click Restart .

Step 4

Click OK .

| Note | If you need your SIP devices to operate in both IPv4 and IPv6 networks, you will need to configure two stacks. After you complete
                                          the tasks in this chapter to enable the IPv6 stack in Cisco Unified Communications Manager, you will then have to also enable
                                          your SIP network for two stacks. See Two Stacks (IPv4 and IPv6) Overview . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure IPv6 in Operating System | Configure the operating system with support for IPv6 addresses. |
| Step 2 | Configure Server for IPv6 | Configure the servers in your cluster with IPv6 addresses. |
| Step 3 | Enable IPv6 | Configure enterprise parameters that enable the system for IPv6. |
| Step 4 | Perform any of the following: Configure IP Addressing Preference for Cluster Configure IP Addressing Preferences for Devices | You can configure an enterprise parameter to assign a clusterwide IP Addressing preference. If you want to assign different preferences for different groups of endpoints, configure the addressing preference within
                                          a Common Device Configuration. Configure cluster settings for which IP addressing method is preferred. |
| Step 5 | Restart Services | Restart the following network services: Cisco CallManager Cisco CTIManager Cisco IP Voice Media Streaming App Cisco Certificate Authority Proxy Function |

| Note | Use Cisco IOS IPv6 DHCP server because the IPv6 DHCP server configuration is not supported on Windows. |
|---|---|

| Step 1 | From Cisco Unified OS Administration, choose Settings > IPv6 > Ethernet . |
|---|---|
| Step 2 | Check the Enable IPv6 check box. |
| Step 3 | From the Address Source drop-down list box, configure how the system acquires the IPv6 address: Router Advertisement —The system uses stateless autoconfiguration to acquire an IPv6 address. DHCP —The system acquires an IPv6 address from a DHCP server. Manual Entry —Choose this option if you want to enter the IPv6 address manually. |
| Step 4 | If you have configured Manual Entry as the means of acquiring an IPv6 address, complete the following fields: Enter an IPv6 Address . For example, fd62:6:96:2le:bff:fecc:2e3a . Enter an IPv6 Mask . for example, 64 . |
| Step 5 | Check the Update with Reboot check box to ensure that the system reboots after you save. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Server . |
|---|---|
| Step 2 | In the IPv6 Address (for dual IPv4/IPv6) field, enter one of the following values: If you have DNS configured, and your DNS server supports IPv6, enter the server IP address. Otherwise, enter the non-link local IPv6 address. |
| Step 3 | Click Save . |
| Step 4 | Repeat these steps for each cluster node. |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | Set the value of the Enable IPv6 enterprise parameter to True . |
| Step 3 | Click Save . |

| Note | The IP address preferences in a Common Device Configuration override the clusterwide enterprise parameter settings for the
                                             devices that use that Common Device Configuration. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Enterprise
                                                				  Parameters . |
|---|---|
| Step 2 | Set the value
                                          			 of the IP
                                             				Addressing Mode Preference for Media enterprise parameter to IPv4 or IPv6 |
| Step 3 | Set the value
                                          			 of the IP
                                             				Addressing Mode Preference for Signaling enterprise parameter to IPv4 or IPv6 . |
| Step 4 | Click Save . |

| Note | The IP address preferences in a Common Device Configuration override the clusterwide enterprise parameter settings for the
                                          devices that use that Common Device Configuration. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | For SIP trunks, SIP Phones or SCCP phones, choose a value for the IP Addressing Mode drop-down list: IPv4 Only —The device uses only an IPv4 address for media and signaling. IPv6 Only —The device uses only an IPv6 address for media and signaling. IPv4 and IPv6 (Default) —The device is a dual-stack device and uses whichever IP address type is available. If both IP address types are configured
                                             on the device, for signaling the device uses the IP Addressing Mode Preference for Signaling setting and for media the device uses the IP Addressing Mode Preference for Media enterprise parameter setting. |
| Step 4 | If you configure IPv6 in your previous step, then configure an IP addressing preference for the IP Addressing Mode for Signaling drop-down list: IPv4 —The dual stack device prefers IPv4 address for signaling. IPv6 —The dual stack device prefers IPv6 address for signaling. Use System Default —The device uses the setting for the IP Addressing Mode Preference for Signaling enterprise parameter. |
| Step 5 | Configure the remaining fields in the Common Device Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 6 | Click Save . |

| Step 1 | Log into Cisco Unified Serviceability and choose Tools > Control Center - Feature Services . |
|---|---|
| Step 2 | Check the check box corresponding to each of the following services: Cisco CallManager Cisco CTIManager Cisco Certificate Authority Proxy Function Cisco IP Voice Media Streaming App |
| Step 3 | Click Restart . |
| Step 4 | Click OK . |