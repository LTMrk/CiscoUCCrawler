---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-c174acb13d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1252-ipv6-configuration.html
retrieved_at: 2026-08-21T06:53:41.155178+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

Chapter: IPv6 Configuration

## Chapter: IPv6 Configuration

# IPv6 Configuration

## Configure IPv6 on
                        	 Unified CVP Call Server

For IPv6-enabled
                              		  deployments, you must add an IPv6 address to your Unified CVP Call Server's
                              		  existing network interface.

Step 1

On the
                                       			 Unified CVP Call Server, navigate to Control
                                             				  Panel > Network and Sharing .

Step 2

Click Ethernet .

Step 3

From the Ethernet Status window, select Properties .

Step 4

Check the Internet Protocol Version 6 (TCP/IPv6) check box,
                                       			 and choose Properties .

Step 5

Choose Use
                                          				the following IPv6 address radio button.

Step 6

Enter values
                                       			 in the IPv6
                                          				address , Subnet
                                          				prefix length , and Default gateway fields.

Step 7

Click OK and restart Windows when prompted.

## Configure IPv6 on Unified Communications Manager

### Enable IPv6 in
                           	 Unified Communications Manager

Perform the
                                 		  following procedure to enable IPv6 on all the Unified Communications Manager in
                                 		  your cluster.

Step 1

From Cisco
                                             				Unified Operating System Administration , navigate to Settings > IP > Ethernet
                                                				  IPv6 .

Step 2

Check the Enable
                                             				IPv6 check box.

Step 3

Enter the
                                          			 values in the IPv6
                                             				Address , Prefix
                                             				Length , and the Default Gateway fields.

Step 4

Click Save .

### Cluster-Wide
                           	 Configuration in Unified CM Administration

Perform the
                                 		  following procedure to set IPv6 as the addressing mode preference for media and
                                 		  signaling cluster-wide.

Step 1

From Cisco
                                             				Unified CM Administration , choose System > Enterprise Parameters > IPv6 Configuration Modes to configure
                                          			 the cluster-wide IPv6 settings for each Unified Communications Manager server.

Step 2

From the Enable
                                             				IPv6 drop-down list, choose True .

Step 3

From the IP
                                             				Addressing Mode Preference for Media drop-down list, choose IPv6 .

Step 4

From the IP
                                             				Addressing Mode Preference for Signaling drop-down list, choose IPv6 .

Step 5

From the Allow
                                             				Auto-configuration for Phones drop-down list, choose Off .

Step 6

Save your
                                          			 changes.

## Add a Common
                        	 Device Configuration Profile in Unified Communications Manager

In an IPv6-enabled environment, you may have both IPv4 and IPv6 devices.

Perform the
                              		  following procedure  to add an IPv4, IPv6, or dual stack common device configuration
                              		  profile in Unified Communications Manager.

Step 1

From Cisco
                                          				Unified CM Administration , choose Device > Device Settings > Common Device Configuration .

Step 2

Click Add
                                          				New and enter the name of the new common device configuration
                                       			 profile.

Step 3

From the IP
                                          				Addressing Mode drop-down list:

- To add an IPv6 common device configuration profile in Unified Communications Manager, choose IPv6
                                             				only .

- To add an IPv4 common device configuration profile in Unified Communications Manager, choose IPv4 only .

- To add a dual stack common device configuration profile in Unified Communications Manager, choose IPv4 and IPv6 . Then choose IPv4 from the IP Addressing Mode Preference for Signaling drop-down list.

Step 4

Save your
                                       			 changes.

### Associate the
                           	 Common Device Configuration Profile with Gateway Trunk

Perform the
                                 		  following procedure to associate the common device configuration profile
                                 		  with the Gateway trunk. 
                                 		This procedure applies to the Ingress Gateway.

Step 1

From Cisco
                                             				Unified CM Administration , choose Device > Trunk .

Step 2

Click Find .

Step 3

From the Common
                                             				Device Configuration drop-down list:

- To associate the IPv6 common device configuration profile with the Gateway trunk, choose the IPv6 common device configuration
                                             profile.

- To
                                             						associate the IPv4 common device configuration profile with the Gateway trunk,
                                             						choose the IPv4 common device configuration profile.

Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk.

Step 4

Enter the IPv6
                                          			 address in the Destination Address IPv6 field.

Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk.

Step 5

Save your
                                          			 changes.

### Associate the
                           	 Common Device Configuration Profile with an IPv4 or IPv6 Phone

Step 1

From Cisco
                                             				Unified CM Administration , choose Device > Phone .

Step 2

Click Find .

Step 3

From the Common
                                             				Device Configuration drop-down list: choose the IPv6 common device
                                          			 configuration profile.

- To associate the IPv6 common device configuration profile to an IPv6 phone, choose the IPv6 common device configuration profile.

- To associate the IPv4 common device configuration profile to an IPv4 phone, choose the IPv4 common device configuration profle.

Step 4

Save your
                                          			 changes.

## Configure SIP
                        	 trunk from Unified Communications Manager to Unified CVP

The following sections describe the steps to configure the SIP trunk
                           		from Unified Communications Manager to Unified CVP.

### Add a SIP Profile
                           	 in Unified CM

This option allows
                                 		  a dual-stack SIP trunk to offer both IPv4 and IPv6 media. 
                                 		Perform this procedure for IPv6-enabled deployments only.

Step 1

From Cisco
                                             				Unified CM Administration , choose Device > Device
                                                				  Settings > SIP Profile .

Step 2

Click Add
                                             				New and enter the name of the SIP profile.

Step 3

Check the Enable
                                             				ANAT check box on the SIP Profile.

Step 4

Save your
                                          			 changes.

### Associate the Dual
                           	 Stack Common Device Configuration Profile with SIP Trunk

You only need to perform this procedure if you have an IPv6 enabled
                                 		  deployment.

Step 1

From Cisco
                                             				Unified CM Administration , choose Device > Trunk .

Step 2

Click Find . Choose the trunk profile that you want to
                                          			 view.

Step 3

From the Common
                                             				Device Configuration drop-down list, choose the Dual Stack Common
                                          			 Device Configuration Profile.

For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager .

Step 4

Save your
                                          			 change.

## Gateway Configuration

### Configure an
                           	 Interface to Support IPv6 Protocol Stack

This procedure applies to both the Ingress and the VXML gateway .

Configure the following on the Gateway:

```
>Enable
>configure terminal
>interface type number
>ipv6 address{ ipv6-address / prefix-length | prefix-name sub-bits / prefix-length}
>ipv6 enable
```

### Enable ANAT in
                           	 Ingress Gateway

Configure the following on the Gateway:

```
>conf t
>voice service voip
>SIP
>ANAT
>bind control source-interface GigabitEthernet0/2
>bind media source-interface GigabitEthernet0/2
```

### Enable Dual Stack
                           	 in the Ingress Gateway

Configure the following on the Gateway:

```
>conf t
>sip-ua
>protocol mode dual-stack preference ipv6
```

## Transcoder
                        	 Configuration in Unified CM and IOS Gateway

A transcoder is
                           		required in the following scenarios

An agent logged in to an IPv6 endpoint needs to send or receive transfers from an agent logged in to an IPv4 endpoint.

An agent logged in to an IPv6 endpoint needs to connect to a VXML Gateway for self service.

A multicodec
                                 			 scenario to convert a stream from a G.711 codec to G.729 codec.

For more information about transcoder configuration in Unified Communications Manager and gateway, see the section "Configure
                           Transcoders and Media Termination Points" in the System Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

### Configure the CVP Call Server Dial Peers in Ingress Gateway

The Ingress Gateway to
                              		Unified CVP outbound dial peer configuration uses the IPv4 address of
                              		Unified CVP as the session target.

| Step 1 | On the
                                       			 Unified CVP Call Server, navigate to Control
                                             				  Panel > Network and Sharing . |
|---|---|
| Step 2 | Click Ethernet . |
| Step 3 | From the Ethernet Status window, select Properties . |
| Step 4 | Check the Internet Protocol Version 6 (TCP/IPv6) check box,
                                       			 and choose Properties . |
| Step 5 | Choose Use
                                          				the following IPv6 address radio button. |
| Step 6 | Enter values
                                       			 in the IPv6
                                          				address , Subnet
                                          				prefix length , and Default gateway fields. |
| Step 7 | Click OK and restart Windows when prompted. |

| Step 1 | From Cisco
                                             				Unified Operating System Administration , navigate to Settings > IP > Ethernet
                                                				  IPv6 . |
|---|---|
| Step 2 | Check the Enable
                                             				IPv6 check box. |
| Step 3 | Enter the
                                          			 values in the IPv6
                                             				Address , Prefix
                                             				Length , and the Default Gateway fields. |
| Step 4 | Click Save . |

| Step 1 | From Cisco
                                             				Unified CM Administration , choose System > Enterprise Parameters > IPv6 Configuration Modes to configure
                                          			 the cluster-wide IPv6 settings for each Unified Communications Manager server. |
|---|---|
| Step 2 | From the Enable
                                             				IPv6 drop-down list, choose True . |
| Step 3 | From the IP
                                             				Addressing Mode Preference for Media drop-down list, choose IPv6 . |
| Step 4 | From the IP
                                             				Addressing Mode Preference for Signaling drop-down list, choose IPv6 . |
| Step 5 | From the Allow
                                             				Auto-configuration for Phones drop-down list, choose Off . |
| Step 6 | Save your
                                          			 changes. |

| Step 1 | From Cisco
                                          				Unified CM Administration , choose Device > Device Settings > Common Device Configuration . |
|---|---|
| Step 2 | Click Add
                                          				New and enter the name of the new common device configuration
                                       			 profile. |
| Step 3 | From the IP
                                          				Addressing Mode drop-down list: To add an IPv6 common device configuration profile in Unified Communications Manager, choose IPv6
                                             				only . To add an IPv4 common device configuration profile in Unified Communications Manager, choose IPv4 only . To add a dual stack common device configuration profile in Unified Communications Manager, choose IPv4 and IPv6 . Then choose IPv4 from the IP Addressing Mode Preference for Signaling drop-down list. |
| Step 4 | Save your
                                       			 changes. |

| Step 1 | From Cisco
                                             				Unified CM Administration , choose Device > Trunk . |
|---|---|
| Step 2 | Click Find . Choose
                                          			 the trunk profile that you want to view. |
| Step 3 | From the Common
                                             				Device Configuration drop-down list: To associate the IPv6 common device configuration profile with the Gateway trunk, choose the IPv6 common device configuration
                                             profile. To
                                             						associate the IPv4 common device configuration profile with the Gateway trunk,
                                             						choose the IPv4 common device configuration profile. Note Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk. | Note | Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk. |
| Note | Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk. |
| Step 4 | Enter the IPv6
                                          			 address in the Destination Address IPv6 field. Note Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk. | Note | Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk. |
| Note | Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk. |
| Step 5 | Save your
                                          			 changes. |

| Note | Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk. |
|---|---|

| Note | Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk. |
|---|---|

| Step 1 | From Cisco
                                             				Unified CM Administration , choose Device > Phone . |
|---|---|
| Step 2 | Click Find . Choose
                                          			 the trunk profile that you want to view. |
| Step 3 | From the Common
                                             				Device Configuration drop-down list: choose the IPv6 common device
                                          			 configuration profile. To associate the IPv6 common device configuration profile to an IPv6 phone, choose the IPv6 common device configuration profile. To associate the IPv4 common device configuration profile to an IPv4 phone, choose the IPv4 common device configuration profle. |
| Step 4 | Save your
                                          			 changes. |

| Step 1 | From Cisco
                                             				Unified CM Administration , choose Device > Device
                                                				  Settings > SIP Profile . |
|---|---|
| Step 2 | Click Add
                                             				New and enter the name of the SIP profile. |
| Step 3 | Check the Enable
                                             				ANAT check box on the SIP Profile. |
| Step 4 | Save your
                                          			 changes. |

| Step 1 | From Cisco
                                             				Unified CM Administration , choose Device > Trunk . |
|---|---|
| Step 2 | Click Find . Choose the trunk profile that you want to
                                          			 view. |
| Step 3 | From the Common
                                             				Device Configuration drop-down list, choose the Dual Stack Common
                                          			 Device Configuration Profile. Note For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager . | Note | For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager . |
| Note | For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager . |
| Step 4 | Save your
                                          			 change. |

| Note | For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager . |
|---|---|

| Configure the following on the Gateway: >Enable
>configure terminal
>interface type number
>ipv6 address{ ipv6-address / prefix-length \| prefix-name sub-bits / prefix-length}
>ipv6 enable |
|---|---|

| Configure the following on the Gateway: >conf t
>voice service voip
>SIP
>ANAT
>bind control source-interface GigabitEthernet0/2
>bind media source-interface GigabitEthernet0/2 |
|---|

| Configure the following on the Gateway: >conf t
>sip-ua
>protocol mode dual-stack preference ipv6 |
|---|