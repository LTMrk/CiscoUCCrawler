---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-srnd-design-guide-cmesrnd-endpts-html-cda0efa13d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/srnd/design/guide/cmesrnd/endpts.html
retrieved_at: 2026-08-21T22:58:30.714706+00:00
---

Cisco Unified CallManager Express Solution Reference Network Design Guide

# Cisco Unified CallManager Express Solution Reference Network Design Guide

Updated: November 2, 2007

Chapter: IP Telephony Endpoints for Cisco Unified CallManager Express

## Chapter: IP Telephony Endpoints for Cisco Unified CallManager Express

## IP Telephony Endpoints for Cisco Unified CallManager Express

This chapter summarizes various types of Cisco Unified IP Telephony endpoints along with their features, related design considerations, and QoS recommendations. The following sections provide information relevant to implementing Cisco Unified IP Telephony endpoints in a Cisco Unified CallManager Express (Cisco Unified CME) environment:

• Analog Gateway

• Cisco Unified IP Phone

• Wireless Endpoint

• Cisco Unified IP Conference Station

• QoS Recommendations

• Endpoint Features Summary

Note For additional information, see the "Related Documents and References" section on page xii .

## Analog Gateway

The Cisco Unified CallManager Express (Cisco Unified CME) provides support for analog phones using Cisco Analog Telephone Adapter (ATA) or VG 224 gateway in SCCP mode. The analog gateway is usually used to connect analog devices, such as fax machines, modems, TDD/TTYs, and analog phones, to the VoIP network so that the analog signal can be packetized and transmitted over the IP network.

### Cisco VG224 Gateway

The Cisco VG224 analog gateway is a Cisco IOS software-based, high-density 24-port gateway for connecting analog devices to the IP telephony network. It supports Cisco IOS Release 12.3.4-XD and higher. The Cisco VG224 connects with Cisco Unified CallManager using MGCP, and it has built-in MGCP failover to an H.323 connection to an Cisco Unified SRST router. The Cisco VG224 integrates with Cisco Unified CME using either H.323 or SIP. The Cisco VG224 supports Cisco Unified CME 3.1 and later releases. The Cisco VG224 is best used with high-density analog devices connecting to the IP network with limited call features, and it is more cost-effective than the Cisco VG248 for deployments of up to 24 analog ports.

### Cisco Analog Telephone Adaptor

The Cisco Analog Telephone Adaptor (Cisco ATA) 186 (or Cisco ATA 188) is an analog telephony adapter that can connect two analog devices to the IP telephony network. The difference between the Cisco ATA 186 and Cisco ATA 188 is that the former has only one 10BaseT Ethernet connection while the later has an integrated Ethernet switch providing two 10BaseT/100BaseT Ethernet connections for itself and a co-located PC or other Ethernet-based device. The Cisco ATA 186 or Cisco ATA 188 supports only unicast Music on Hold (MoH).

The Cisco ATA 186 and Cisco ATA 188 can be configured in any of the following ways:

• Cisco ATA web configuration page

• Cisco ATA voice configuration menu

• Configuration file downloaded from the TFTP server

The SCCP-based ATA behaves like an SCCP IP phone. The Cisco ATA 186 or Cisco ATA 188 can be configured as an H.323 client to Cisco Unified CME or as an H.323 terminal to an H.323 gatekeeper. When the Cisco ATA registers with the gatekeeper as an H.323 terminal, the H.323 proxy must be disabled for the zone in which the ATA is located.

The Cisco ATA 186 or Cisco ATA 188 can also be configured as a SIP client that registers with the SIP server to make phone calls with another endpoint. The Cisco ATA 186 or Cisco ATA 188 can act as either a user agent client (UAC) when it initiates SIP requests or as a user agent server (UAS) when it responds to requests. The Cisco ATA 186 and Cisco ATA 188 are best used with low-density analog devices connecting to the IP network. In H.323 mode, the Cisco ATA 186 and Cisco ATA 188 do not mark the voice bearer packets correctly by default. You must manually configure the ATA to mark voice bearer traffic with a Differentiated Services Code Point (DSCP) value of EF by changing the Type of Service (ToS) field from its default value to a ToS value of 0x000000B8. This configuration change is no longer necessary with Cisco ATA 3.1 and later releases.

## Cisco Unified IP Phone

The Cisco Unified IP Phones include low-end, mid-range, and high-end IP phones. The applicable Cisco Unified IP Phones for a Cisco Unified CME environment are described in the following sections:

• Low-End Cisco Unified IP Phones

• Mid-Range Cisco Unified IP Phones

• High-End Cisco Unified IP Phones

Note For information about support for different protocols and features associated with your specific endpoints, refer to your Cisco Unified CME documentation addressing this topic.

### Low-End Cisco Unified IP Phones

The low-end units are used for low-traffic situations with limited call feature and budget requirements. The low-end Cisco Unified IP Phones include the Cisco Unified IP Phone 7902G, Cisco Unified IP Phone 7905G, Cisco Unified IP Phone 7910G, Cisco Unified IP Phone 7910G+SW, Cisco Unified IP Phone 7911G, and Cisco Unified IP Phone 7912G.

### Cisco Unified IP Phone 7902G

The Cisco Unified IP Phone 7902G supports a single line, and it has a single 10BaseT Ethernet port on the back of the phone. The Cisco Unified IP Phone 7902G does not have a liquid crystal display (LCD) screen.

### Cisco Unified IP Phone 7905G

The Cisco Unified IP Phone 7905G supports a single line, and it has a single 10BaseT Ethernet port on the back of the phone. The speaker operates in one-way listen mode only.

### Cisco Unified IP Phone 7910G and Cisco Unified IP Phone 7910G+SW

The Cisco Unified IP Phone 7910G supports a single line, and the speaker operates in one-way listen mode only. The Cisco Unified IP Phone 7910G also has six fixed-feature access keys that can be configured in the customized phone button template by the administrator to provide various end-user call features. Because there are only six fixed-feature keys, the model Cisco Unified IP Phone 7910G cannot provide end users with all of the call features through one phone button template.

The only difference between the Cisco Unified IP Phone 7910G and Cisco Unified IP Phone 7910G+SW is that the former has a single 10BaseT Ethernet port and the latter has two 10BaseT/100BaseT Ethernet ports.

### Cisco Unfied IP Phone 7911G

The Cisco Unified IP Phone 7911G supports a single line. It is similar to the Cisco Unified IP Phone 7912G, but supports IEEE 802.3af Power over Ethernet, advanced security, and an extended software roadmap to support advanced IP features.

### Cisco Unified IP Phone 7912G

The Cisco Unified IP Phone 7912G supports a single line, and it has two 10BaseT/100BaseT Ethernet connections. The speaker operates in one-way listen mode only.

### Mid-Range Cisco Unified IP Phones

The midrange Cisco Unified IP Phone used for high-traffic situations with extensive call features, such as speakers, headset, and so forth. The mid-range Cisco Unified IP Phones include the Cisco Unified IP Phone 7940G, Cisco Unified IP Phone 7941G, Cisco Unified IP Phone 7960G, and Cisco Unified IP Phone 7961G.

The Cisco Unified IP Phone 7940G and Cisco Unified IP Phone 7941G can each have up to two directory numbers, and the Cisco IP Phone 7960G and Cisco Unified IP Phone 7961G can each have a total of six directory numbers. All four phone models are compatible with Cisco VT Advantage video-enabled endpoints for making video calls.

### High-End Cisco Unified IP Phones

The Cisco Unified IP Phone 7970G and Cisco Unified IP Phone 7971G, the high-end Cisco Unified IP Phones, are used for high-traffic situations with extensive call features. The Cisco Unified IP Phone 7970G has a high-resolution, color touch-screen display, more function keys, and more security features than the midrange Cisco Unified IP phones. The Cisco Unified IP Phone 7970G can also have up to eight directory numbers.

The Cisco Unified IP Phone 7970G is also compatible with Cisco VT Advantage video-enabled endpoints for making video calls. The Cisco Unified IP Phone 7970G is the only Cisco Unified IP phone that supports both Cisco prestandard Power-over-Ethernet (PoE) and the IEEE 802.3af PoE. For the Cisco Unified IP Phone 7970G to have full display brightness, you must use the external power adapter (CP-PWR-CUBE2) with both inline power and IEEE 802.3af PoE.

The Cisco Unified IP Phone 7971G can have up to eight directory numbers and is the equivalent of the Cisco Unified IP Phone 7970G with the exception that it includes two 10/100/1000 BaseT Ethernet connections. The addition of gigabit throughput capability allows for high bit-rate and bandwidth-intensive applications on a co-located PC.

## Wireless Endpoint

Cisco wireless endpoints use a wireless LAN (WLAN) infrastructure through wireless access points (APs) to provide telephony functionality and features. This type of endpoint is ideal for environments with the need for mobile users within a area where traditional wired phones are undesirable or problematic. (See the "Wireless LAN Infrastructure" section on page 3-33 , for more information about wireless network design.)

The Cisco Unified Wireless IP Phone 7920G is a hardware-based phone with a built-in radio antenna that enables 802.1b wireless LAN connectivity to the network. These phones register with Cisco Unified CallManager using Skinny Client Control Protocol (SCCP).

The following sections summarizes wireless endpoint considerations in a Cisco CME environment:

• Site Survey

• Authentication

• Capacity

• Phone Configuration

• Roaming

• AP Call Admission Control

### Site Survey

Before deploying the Cisco Unified Wireless IP Phone 7920G, you must perform a complete site survey to determine the appropriate number and location of APs required to provide radio frequency (RF) coverage. Your site survey should take into consideration which types of antennas will provide the best coverage and where sources of RF interference might exist. A site survey requires the use of the Site Survey tool on the Cisco Unified Wireless IP Phone 7920G (accessed through the Menu > Network Config > Site Survey windows path) and the Aironet Client Utility Site Survey Tool used with a Cisco Aironet NIC card on a laptop or PC. Additional third-party tools can also be used for site surveys; however, we highly recommend that you conduct a final site survey using the Cisco Unified Wireless IP Phone 7920G because each endpoint or client radio can behave differently depending on antenna sensitivity and survey application limitations.

### Authentication

To connect to the wireless network, the Cisco Unified Wireless IP Phone 7920G must first use one of the following authentication methods to associate and communicate with the AP:

• Cisco LEAP

This method allows the Cisco Unified Wireless IP Phone 7920G and AP to be authenticated mutually based on a username and password. Upon authentication, the dynamic key is generated and used for encrypting traffic between the Cisco Unified Wireless IP Phone 7920G and the AP. A Cisco LEAP-compliant Radius authentication server, such as the Cisco Secure Access Control Server (ACS), is required to provide access to the user database.

• Static Wired Equivalent Privacy (WEP)

This method involves the configuration of static 10 (40-bit) or 26 (128-bit) character keys on the Cisco Unified Wireless IP Phone 7920G and the AP. This method is AP-based authentication in which access to the network is gained if the device has a matching key.

• Open Authentication

This method requires no exchange of identifying information between the Cisco Unified Wireless IP Phone 7920G and the AP. We do not recommend this method because it provides no secure exchange of voice or signaling, and it allows any rouge device to associate to the AP.

### Capacity

Each AP can support a maximum of seven active G.711 voice calls or eight G.729 calls. If these numbers are exceeded, poor quality can result due to dropped or delayed voice packets or dropped calls. AP rates set lower than 11 Mbps will result in lower call capacity per AP.

Based on these active call capacity limits, and using Erlang ratios, you can calculate the number of Cisco Unified Wireless 7920G IP Phones that each AP can support. For example, given a typical user-to-call capacity ratio of 3:1, a single AP can support 21 to 24 Cisco Unified Wireless 7920G IP Phones, depending whether the codec used is G.711 or G.729. However, this number does not take into consideration the possibility that other Cisco Unified Wireless 7920G IP Phones could roam to this AP, so a lower number of phones per AP is more realistic.

The number of APs per VLAN or Layer 2 subnet should also be considered. To optimize memory and performance on the APs we recommend deploying no more than 30 APs on a single VLAN or subnet. This recommendation, taken with typical user-to-call capacity ratios, limits the number of Cisco Unified Wireless 7920G IP Phones per Layer 2 subnet to approximately 500 (or about 15 to 17 Cisco Unified Wireless 7920G IP Phones per AP).

These capacities were calculated with voice activity detection (VAD) disabled and a packetization sample size of 20 milliseconds (ms). VAD is a mechanism for conserving bandwidth by not sending RTP packets while no speech is occurring during the call. We recommend leaving VAD (Silence Suppression) disabled to provide better overall voice quality.

At a sampling rate of 20 ms, a voice call will generate 50 packets per second (pps) in either direction. We recommend setting the sample rate to 20 ms for almost all cases. By using a larger sample size (for example, 30 or 40 ms), you can increase the number of simultaneous calls per AP, but a larger end-to-end delay will result. In addition, the percentage of acceptable voice packet loss within a wireless environment decreases dramatically with a larger sample size because more of the conversation is missing when a packet is lost. For more information about voice sampling size, see the "Bandwidth Provisioning" section on page 3-19 .

### Phone Configuration

You can configure the Cisco Unified Wireless IP Phone 7920G either through the phone's keypad or with the Cisco Unified Wireless IP Phone 7920 Configuration Utility running on a PC that is attached to the phone using a USB cable. In either case, you must configure the following parameters:

• Network Configuration

Configure either the DHCP server address or static settings such as IP address, subnet mask, default gateway, TFTP server, and DNS server, as appropriate for the network. These settings can be found on the Cisco Unified Wireless IP Phone 7920G under Menu > Network Config > Current Config .

• Wireless Configuration

Configure the service set identifier (SSID) for the voice VLAN and the authentication type, including the WEP key and/or LEAP username and password when appropriate. These settings can be found on the Cisco Unified Wireless IP Phone 7920G under Menu > Network Config > 802.11b Configuration .

### Roaming

The Cisco Unified Wireless IP Phone 7920G is able to roam at Layer 2 (within the same VLAN or subnet) and still maintain an active call.

Layer 2 roaming occurs in the following situations:

• During the initial boot-up of the Cisco Unified Wireless IP Phone 7920G, the phone roams to a new AP for the first time.

• If the Cisco Unified Wireless IP Phone 7920G receives no beacons or responses from the AP to which it is associated, the phone assumes that the current AP is unavailable and it attempts to roam and associate with a new AP.

• The Cisco Unified Wireless IP Phone 7920G maintains a list of eligible AP roam targets. If conditions change on the current AP, the phone consults the list of available AP roam targets. If one of the roam targets is determined to be a better choice, then the phone attempts to roam to the new AP.

• If the configured SSID or authentication type on the Cisco Unified Wireless IP Phone 7920G is changed, the phone must roam to reassociate with an AP.

In trying to determine eligible AP roam targets for Layer 2 roaming, the wireless IP phone uses the following variables to determine the best AP to associate with:

• Relative Signal Strength Indicator (RSSI)

Used by the wireless IP phone to determine the signal strength and quality of available APs within an RF coverage area. The phone will attempt to associate with the AP that has the highest RSSI value and matching authentication/encryption type.

• QoS Basis Service Set (QBSS)

Enables the AP to communicate channel utilization information to the wireless phone. The phone will use the QBSS value to determine if it should attempt to roam to another AP, because APs with high channel utilization might not be able to handle VoIP traffic effectively.

• RSSI-Differential Threshold

The wireless IP phone will roam if the next AP RSSI is higher than the current AP RSSI by at least this threshold amount. The default threshold is 15.

• QBSS-Differential Threshold

The wireless IP phone will roam if the next AP QBSS is lower than the current AP QBSS by at least this threshold amount. The default threshold is 15.

The wireless IP phone uses the following steps to determine which AP it should roam to:

1. Find APs that are advertising QBSS in their beacons. If any of these APs meet the QBSS-differential threshold criteria, then begin the roaming process to one of them.

2. If no APs are advertising QBSS, or if the advertising APs do not meet the differential threshold criteria, then look for APs that are not advertising QBSS but that have acceptable RSSI levels, and begin the roaming process to one of them.

Layer 2 roaming times for the wireless IP phone depend on the type of authentication used. If static WEP keys are used for authentication between the phone and the AP, Layer 2 roaming occurs in less than 100 ms. If LEAP (with local Cisco Secure ACS authentication) is used, Layer 2 roaming occurs in 200 to 400 ms. Use of Fast Secure Roaming can decrease the LEAP authentication time to less than 150 ms for Layer 2 roams.

Layer 3 roaming occurs when the Cisco Unified Wireless IP Phone 7920 moves from one AP to another AP and crosses a subnet boundary. With the release of the new Cisco Catalyst 6500 Series Wireless LAN Services Module (WLSM), the Cisco Unified Wireless IP Phone 7920 now supports Layer 3 mobility with survivable calls while using Static WEP. Cisco Centralized Key Management (Cisco CKM) enables the Cisco Unified Wireless IP Phone 7920 to achieve full Layer 3 mobility while using LEAP.

### AP Call Admission Control

Call admission control mechanisms in Cisco Unified CallManager or in a gatekeeper can control WAN bandwidth utilization and provide QoS for existing calls, but both mechanisms are applied only at the beginning of a call. For calls between static devices, this type of call admission control is sufficient. However, for a call between two mobile wireless devices such the Cisco Unified Wireless IP Phone 7920G, there must also be a call admission control mechanism at the AP level because the wireless devices may roam from one AP to another.

The AP mechanism for call admission control is QBSS, which is the beacon information element that enables the AP to communicate channel utilization information to the wireless IP phone. As previously mentioned, this QBSS value helps the phone determine whether it should roam to another AP. A lower QBSS value indicates that the AP is a good candidate to roam to, while a higher QBSS value indicates that the phone should not roam to this AP.

While this QBSS information is useful, it does not provide a 100 percent guarantee that calls will retain proper QoS during roaming. When a Cisco Unified Wireless 7920 IP Phone is associated to an AP with a high QBSS, the AP will prevent a call from being initiated or received by rejecting the call setup and sending a Network Busy message to the initiating phone. However, when a call is set up between a wireless IP phone and another endpoint, the phone may roam and associate with an AP with a high QBSS, thus resulting in an oversubscription of the available bandwidth on that AP.

## Cisco Unified IP Conference Station

The Cisco Unified IP Conference Station combines conference room speaker-phone technology with Cisco Unified IP Communications technology. The Cisco Unified IP Conference Station is used in conferencing environments providing 360-degree room coverage.

The Cisco Unified IP Conference Station 7936 has an external speaker and three built-in microphones. The Cisco Unified IP Conference Station 7936 also features a pixel-based LCD display with backlighting, and optional extension microphones can be connected to it for extended microphone coverage in larger rooms.

## QoS Recommendations

This section provides the basic QoS guidelines and configurations for the Cisco Catalyst switches most commonly deployed with IP Telephony endpoints. QoS is summarized in the following sections:

• Cisco VG224

• Cisco ATA 186 and Conference Station

• Cisco ATA 188 and Cisco Unified IP Phones

• Cisco Unified Wireless IP Phone 7920G

### Cisco VG224

Analog gateways are trusted endpoints. For Cisco VG224 gateway, configure the switch to trust the DSCP value of the VG224 packets. The following sections list the commands to configure the most common Cisco Catalyst switches for the Cisco VG224 analog gateways.

Note In the following sections, vvlan_id is the voice VLAN ID and dvlan_id is the data VLAN ID.

Cisco 2950

```
CAT2950(config)# interface interface-id
```

```
CAT2950(config-if)# mls qos trust dscp
```

```
CAT2950(config-if)# switchport mode access
```

```
CAT2950(config-if)# switchport access vlan vvlan_id
```

Note The mls qos trust dscp command is available only with Enhanced Image (EI).

Cisco 2970 or 3750

```
CAT2970(config)# mls qos
```

```
CAT2970(config)# interface interface-id
```

```
CAT2970(config-if)# mls qos trust dscp
```

```
CAT2970(config-if)# switchport mode access
```

```
CAT2970(config-if)# switchport access vlan vvlan_id
```

Cisco 3560

```
CAT3560(config)# mls qos
```

```
CAT3560(config)# interface interface-id
```

```
CAT3560(config-if)# mls qos trust dscp
```

```
CAT3560(config-if)# switchport mode access
```

```
Cat3560(config-if)# switchport access vlan vvlan_id
```

Cisco 4500 with SUPIII, IV, or V

```
CAT4500(config)# qos
```

```
CAT4500(config)# interface interface-id
```

```
CAT4500(config-if)# qos trust dscp
```

```
CAT4500(config-if)# switchport mode access
```

```
CAT4500(config-if)# switchport access vlan vvlan_id
```

Cisco 6500

```
CAT6500>(enable) set qos enable
```

```
CAT6500>(enable) set port qos 2/1 vlan-based
```

```
CAT6500>(enable) set vlan vvlan_id mod/port
```

```
CAT6500>(enable) set port qos mod/port trust trust-dscp
```

### Cisco ATA 186 and Conference Station

Because the Cisco Analog Telephone Adaptor (ATA) 186 and IP Conference Station are trusted endpoints, their QoS configurations are identical to those described in the "Cisco VG224" section .

### Cisco ATA 188 and Cisco Unified IP Phones

For the Cisco ATA 188 and Cisco Unified IP Phones, we recommend segregating the voice VLAN from the data VLAN. For the Cisco ATA 186, Cisco Unified IP Phone 7902, Cisco Unified IP Phone 7905, Cisco Unified IP Phone 7910, and Cisco Unified IP Conference Station, we still recommend configuring voice and data VLAN segregation and an auxiliary voice VLAN. In this way, the same access-layer configurations can be used with different Cisco Unified IP Phone models and Cisco ATA units, and end users can plug their IP phones or Cisco AT units into different access ports on the switch and get the same treatment. For the Cisco ATA 186, Cisco Unified IP Phone 7902, Cisco Unified IP Phone 7905, Cisco Unified IP Phone 7910, and Cisco Unified IP Conference Stations, the command to override the CoS value of the frames from the attached PC has no effects because these devices do not have a PC connected to them.

The following sections list the configuration commands for IP phones on the most commonly deployed Cisco Catalyst switches.

Cisco 2950

```
CAT2950(config)#
```

```
CAT2950(config)# class-map VVLAN
```

```
CAT2950(config-cmap)# match access-group name VVLAN
```

```
CAT2950(config-cmap)# class-map VLAN
```

```
CAT2950(config-cmap)# match access-group name DVLAN
```

```
CAT2950(config-cmap)# exit
```

```
CAT2950(config)#
```

```
CAT2950(config)# policy-map IPPHONE-PC
```

```
CAT2950(config-pmap)# class VVLAN
```

```
CAT2950(config-pmap-c0# set ip dscp 46
```

```
CAT2950(config-pmap-c)# police 1000000 8192 exceed-action-drop
```

```
CAT2950(config-pmap)# class DVLAN
```

```
CAT2950(config-pmap-c0# set ip dscp 0
```

```
CAT2950(config-pmap-c)# police 5000000 8192 exceed-action-drop
```

```
CAT2950(config-pmap-c)# exit
```

```
CAT2950(config-pmap)# exit
```

```
CAT2950(config)#
```

```
CAT2950(config)# interface interface-id
```

```
CAT2950(config-if)# mls qos trust device cisco-phone
```

```
CAT2950(config-if)# mls qos trust cos
```

```
CAT2950(config-if)# switchport mode access
```

```
CAT2950(config-if)# switchport voice vlan vvlan_id
```

```
CAT2950(config-if)# s witchport access vlan dvlan_id
```

```
CAT2950(config-if)# service-policy input IPPHONE-PC
```

```
CAT2950(config-if)# exit
```

```
CAT2950(config)#
```

```
CAT2950(config)# ip access-list standard VVLAN
```

```
CAT2950(config-std-nacl)# permit voice_IP_subnet wild_card_mask
```

```
CAT2950(config-std-nacl)# exit
```

```
CAT2950(config)# ip access-list standard DVLAN
```

```
CAT2950(config-std-nacl)# permit data_IP_subnet wild_card_mask
```

```
CAT2950(config-std-nacl)# end
```

Note The mls qos map cos-dscp command is available only with Enhanced Image (EI). With Standard Image (SI), this command is not available and the default CoS-to-DSCP mapping is as follows:

Cos Value

0

1

2

3

4

5

6

7

DSCP Value

0

8

16

24

32

40

48

56

Cisco 2970 or 3750

```
CAT2970(config)# mls qos map cos-dscp 0 8 16 24 34 46 48 56
```

```
CAT2970(config)# mls qos map policed-dscp 0 24 to 8
```

```
CAT2970(config)#
```

```
CAT2970(config)# class-map match-all VVLAN-VOICE
```

```
CAT2970(config-cmap)# match access-group name VVLAN-VOICE
```

```
CAT2970(config-cmap)#
```

```
CAT2970(config-cmap)# class-map match-all VVLAN-CALL-SIGNALING
```

```
CAT2970(config-cmap)# match access-group name VVLAN-CALL-SIGNALING
```

```
CAT2970(config-cmap)#
```

```
CAT2970(config-cmap)# class-map match-all VVLAN-ANY
```

```
CAT2970(config-cmap)# match access-group name VVLAN-ANY
```

```
CAT2970(config-cmap)#
```

```
CAT2970(config-cmap)# policy-map IPPHONE-PC
```

```
CAT2970(config-pmap)# class VVLAN-VOICE
```

```
CAT2970(config-pmap-c)# set ip dscp 46
```

```
CAT2970(config-pmap-c)# police 128000 8000 exceed-action drop
```

```
CAT2970(config-pmap-c)# class VVLAN-CALL-SIGNALING
```

```
CAT2970(config-pmap-c)# set ip dscp 24
```

```
CAT2970(config-pmap-c)# police 32000 8000 exceed-action policed-dscp-transmit
```

```
CAT2970(config-pmap-c)# class VVLAN-ANY
```

```
CAT2970(config-pmap-c)# set ip dscp 0
```

```
CAT2970(config-pmap-c)# police 32000 8000 exceed-action policed-dscp-transmit
```

```
CAT2970(config-pmap-c)# class class-default
```

```
CAT2970(config-pmap-c)# set ip dscp 0
```

```
CAT2970(config-pmap-c)# police 5000000 8000 exceed-action policed-dscp-transmit
```

```
CAT2970(config-pmap-c)# exit
```

```
CAT2970(config-pmap)# exit
```

```
CAT2970(config)#
```

```
CAT2970(config)#
```

```
CAT2970(config)# interface interface-id
```

```
CAT2970(config-if)# switchport voice vlan vvlan_id
```

```
CAT2970(config-if)# switchport access vlan dvlan_id
```

```
CAT2970(config-if)# mls qos trust device cisco-phone
```

```
CAT2970(config-if)# service-policy input IPPHONE-PC
```

```
CAT2970(config-if)# exit
```

```
CAT2970(config)#
```

```
CAT2970(confiig)# ip access list extended VVLAN-VOICE
```

```
CAT2970(config-ext-nacl)# permit udp Voice_IP_Subnet Subnet_Mask any range 16384 32767 
dscp ef
```

```
CAT2970(config-ext-nacl)# exit
```

```
CAT2970(config)# ip access list extended VVLAN-CALL-SIGNALING
```

```
CAT2970(config-ext-nacl)# permit tcp Voice_IP_Subnet Subnet_Mask any range 2000 2002 dscp 
cs3
```

```
CAT2970(config-ext-nacl)# exit
```

```
CAT2970(config)# ip access list extended VVLAN-ANY
```

```
CAT2970(config-ext-nacl)# permit ip Voice_IP_Subnet Subnet_Mask any
```

```
CAT2970(config-ext-nacl)# end
```

```
CAT2970#
```

Cisco 3560

```
CAT3560(config)# mls qos map cos-dscp 0 8 16 24 34 46 48 56
```

```
CAT3560(config)# mls qos map policed-dscp 0 24 to 8
```

```
CAT3560(config)# class-map match-all VOICE
```

```
CAT3560(config-cmap)# match ip dscp 46
```

```
CAT3560(config-cmap)# class-map match-any CALL SIGNALING
```

```
CAT3560(config-cmap)# match ip dscp 26
```

```
CAT3560(config-cmap)# match ip dscp 24
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all VVLAN-VOICE
```

```
CAT3560(config-cmap)# match vlan vvlan_id
```

```
CAT3560(config-cmap)# match class-map VOICE
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all VVLAN-CALL-SIGNALING
```

```
CAT3560(config-cmap)# match vlan vvlan_id
```

```
CAT3560(config-cmap)# match class-map CALL SIGNALING
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all ANY
```

```
CAT3560(config-cmap)# match access-group name ACL_Name
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all VVLAN-ANY
```

```
CAT3560(config-cmap)# match vlan vvlan_id
```

```
CAT3560(config-cmap)# match class-map ANY
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all DVLAN-ANY
```

```
CAT3560(config-cmap)# match vlan dvlan_id
```

```
CAT3560(config-cmap)# match class-map ANY
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# policy-map IPPHONE-PC
```

```
CAT3560(config-pmap)# class VVLAN-VOICE
```

```
CAT3560(config-pmap-c)# set ip dscp 46
```

```
CAT3560(config-pmap-c)# police 128000 8000 exceed-action drop
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class VVLAN-CALL-SIGNALING
```

```
CAT3560(config-pmap-c)# set ip dscp 24
```

```
CAT3560(config-pmap-c)# police 32000 8000 exceed-action drop
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class VVLAN-ANY
```

```
CAT3560(config-pmap-c)# set ip dscp 0
```

```
CAT3560(config-pmap-c)# police 32000 8000 exceed-action drop
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class DVLAN-VOICE
```

```
CAT3560(config-pmap-c)# set ip dscp 0
```

```
CAT3560(config-pmap-c)# police 5000000 8000 exceed-action drop
```

```
CAT3560(config-pmap-c)# exit
```

```
CAT3560(config-pmap)# exit
```

```
CAT3560(config)# interface interface-id
```

```
CAT3560(config-if)# switchport voice vlan vvlan_id
```

```
CAT3560(config-if)# switchport access vlan dvlan_id
```

```
CAT3560(config-if)# mls qos trust device cisco-phone
```

```
CAT3560(config-if)# service-policy input IPPHONE-PC
```

```
CAT3560(config-if)# exit
```

```
CAT3560(config)#
```

```
CAT3560(confiig)# ip access list standard ACL_ANY
```

```
CAT3560(config-std-nacl)# permit any
```

```
CAT3560(config-std-nacl)# end
```

```
CAT3560#
```

Cisco 4500 with SUPIII, IV, or V

```
CAT4500(config)# qos map cos 5 to dscp 46
```

```
CAT4500(config)# qos map cos 0 24 to dscp 8
```

```
CAT4500(config)#
```

```
CAT4500(config)# class-map match-all VVLAN-VOICE
```

```
CAT4500(config-cmap)# match access-group name VVLAN-VOICE
```

```
CAT4500(config-cmap)#
```

```
CAT4500(config-cmap)# class-map match-all VVLAN-CALL-SIGNALING
```

```
CAT4500(config-cmap)# match access-group name VVLAN-CALL-SIGNALING
```

```
CAT4500(config-cmap)#
```

```
CAT4500(config-cmap)# class-map match-all VVLAN-ANY
```

```
CAT4500(config-cmap)# match access-group name VVLAN-ANY
```

```
CAT4500(config-cmap)#
```

```
CAT4500(config-cmap)# policy-map IPPHONE-PC
```

```
CAT4500(config-pmap)# class VVLAN-VOICE
```

```
CAT4500(config-pmap-c)# set ip dscp 46
```

```
CAT4500(config-pmap-c)# police 128 kps 8000 byte exceed-action drop
```

```
CAT4500(config-pmap-c)# class VVLAN-CALL-SIGNALING
```

```
CAT4500(config-pmap-c)# set ip dscp 24
```

```
CAT4500(config-pmap-c)# police 32 kps 8000 byte exceed-action policed-dscp-transmit
```

```
CAT4500(config-pmap-c)# class VVLAN-ANY
```

```
CAT4500(config-pmap-c)# set ip dscp 0
```

```
CAT4500(config-pmap-c)# police 32 kps 8000 byte exceed-action policed-dscp-transmit
```

```
CAT4500(config-pmap-c)# class class-default
```

```
CAT4500(config-pmap-c)# set ip dscp 0
```

```
CAT4500(config-pmap-c)# police 5 mpbs 8000 byte exceed-action policed-dscp-transmit
```

```
CAT4500(config-pmap-c)# exit
```

```
CAT4500(config-pmap)# exit
```

```
CAT4500(config)#
```

```
CAT4500(config)#
```

```
CAT4500(config)# interface interface-id
```

```
CAT4500(config-if)# switchport voice vlan vvlan_id
```

```
CAT4500(config-if)# switchport access vlan dvlan_id
```

```
CAT4500(config-if)# qos trust device cisco-phone
```

```
CAT4500(config-if)# service-policy input IPPHONE-PC
```

```
CAT4500(config-if)# exit
```

```
CAT4500(config)#
```

```
CAT4500(confiig)# ip access list extended VVLAN-VOICE
```

```
CAT4500(config-ext-nacl)# permit udp Voice_IP_Subnet Subnet_Mask any range 16384 32767 
dscp ef
```

```
CAT4500(config-ext-nacl)# exit
```

```
CAT4500(config)# ip access list extended VVLAN-CALL-SIGNALING
```

```
CAT4500(config-ext-nacl)# permit tcp Voice_IP_Subnet Subnet_Mask any range 2000 2002 dscp 
cs3
```

```
CAT4500(config-ext-nacl)# exit
```

```
CAT4500(config)# ip access list extended VVLAN-ANY
```

```
CAT4500(config-ext-nacl)# permit ip Voice_IP_Subnet Subnet_Mask any
```

```
CAT4500(config-ext-nacl)# end
```

```
CAT4500#
```

Cisco 6500

```
CAT6500> (enable) set qos cos-dscp-map 0 8 16 24 32 46 48 56
```

```
CAT6500> (enable) set qos policed-dscp-map 0, 24, 46:8
```

```
CAT6500> (enable)
```

```
CAT6500> (enable) set qos policer aggregate VVLAN-VOICE rate 128 burst 8000 drop
```

```
CAT6500> (enable) set qos policer aggregate VVLAN-CALL-SIGNALING rate 32 burst 8000 
policed-dscp
```

```
CAT6500> (enable) set qos policer aggregate VVLAN-ANY rate 5000 burst 8000 policed-dscp
```

```
CAT6500> (enable) set qos policer aggregate PC-DATA rate 5000 burst 8000 policed-dscp
```

```
CAT6500> (enable)
```

```
CAT6500> (enable) set qos acl ip IPPHONE-PC dscp 46 aggregate VVLAN-VOICE udp Voice_IP_Subnet Subnet_Mask any range 16384 32767
```

```
CAT6500> (enable) set qos acl ip IPPHONE-PC dscp 24 aggregate VVLAN-CALL-SIGNALING tcp Voice_IP_Subnet Subnet_Mask any range 2000 2002
```

```
CAT6500> (enable) set qos acl ip IPPHONE-PC dscp 0 aggregate VVLAN-ANY Voice_IP_Subnet 
Subnet_Mask any
```

```
CAT6500> (enable) set qos acl ip IPPHONE-PC dscp 0 aggregate PC-DATA any
```

```
CAT6500> (enable) commit qos acl IPPHONE-PC
```

```
CAT6500> (enable) set vlan vvlan_id mod/port
```

```
CAT6500> (enable) set port qos mod/port trust-device ciscoipphone
```

```
CAT6500> (enable) set qos acl map IPPHONE-PC mod/port
```

```
CAT6500> (enable)
```

### Cisco Unified Wireless IP Phone 7920G

By default, the Cisco Unified Wireless IP Phone 7920 marks its SCCP signaling messages using a Per-Hop Behavior (PHB) value of AF31 or a Differentiated Services Code Point (DSCP) value of 26 (this corresponds to a ToS value of 0x68), and it marks RTP voice packets using a PHB value of EF or a DSCP value of 46 (ToS of 0xB8). With proper queueing on the AP and configuration on the upstream first-hop switch to trust the AP's port, the wireless IP phone traffic will receive the same treatment as wired IP phone traffic. This practice allows the QoS settings to be consistent from LAN to WLAN environments.

In addition, the Cisco Unified Wireless IP Phone 7920 will automatically announce its presence to the AP using the Cisco Discovery Protocol (CDP). The CDP packets are sent from the wireless IP phone to the AP, and they identify the phone so that the AP can place all traffic to the phone in the high-priority queue.

While Ethernet switch ports can typically transmit and receive at 100 Mbps, 802.11b APs have a lower throughput rate that allows for a maximum data rate of 11 Mbps. Furthermore, wireless LANs are a shared medium and, due to contention for this medium, the actual throughput is substantially lower. This throughput mismatch means that, with a burst of traffic, the AP will drop packets, thus adding excessive processor burden to the unit and affecting performance.

By taking advantage of the policing and rate limiting capabilities of the Cisco Catalyst 3560 and 6500 Series switches, you can eliminate the need for the AP to drop excessive packets by configuring the upstream switch port to rate-limit or police traffic going to the AP. The switch port configurations in the following sections rate-limit the port(s) to a practical throughput of 7 Mbps for 802.11b and guarantee 1 Mbps for high-priority voice and control traffic. Furthermore, as indicated in the configuration examples, packets coming from the AP should be trusted and, based on the VLAN tag of each packet, the DSCP marking should either be maintained or marked down. Thus, packets sourced from the Cisco Unified Wireless IP Phone 7920 on the voice VLAN should maintain the appropriate DSCP marking, and packets source from data devices on the data VLAN should be remarked to a DSCP value of 0.

Cisco 3560

```
CAT3560(config)# mls qos
```

```
CAT3560(config)# mls qos map cos-dscp 0 8 16 24 32 46 48 56
```

```
CAT3560(config)# mls qos map policed-dscp 24 26 46 to 8
```

```
CAT3560(config)# mls qos aggregate-policer AGG-POL-1M-VOICE-OUT 1000000 8000 exceed-action 
policed-dscp-transmit
```

```
CAT3560(config)# mls qos aggregate-policer AGG-POL-6M-DEFAULT-OUT 6000000 8000 
exceed-action drop
```

```
CAT3560(config)#
```

```
CAT3560(config)# class-map match-all EGRESS-DSCP-0
```

```
CAT3560(config-cmap)# match ip dscp 0
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all EGRESS-DSCP-8
```

```
CAT3560(config-cmap)# match ip dscp 8
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all EGRESS-DSCP-16
```

```
CAT3560(config-cmap)# match ip dscp 16
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all EGRESS-DSCP-32
```

```
CAT3560(config-cmap)# match ip dscp 32
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all EGRESS-DSCP-48
```

```
CAT3560(config-cmap)# match ip dscp 48
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all EGRESS-DSCP-56
```

```
CAT3560(config-cmap)# match ip dscp 56
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-any VOICE-SIGNALING
```

```
CAT3560(config-cmap)# match ip dscp 24
```

```
CAT3560(config-cmap)# match ip dscp 26
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all VOICE
```

```
CAT3560(config-cmap)# match ip dscp 46
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all INGRESS-DATA
```

```
CAT3560(config-cmap)# match any
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all INGRESS-VVLAN-VOICE
```

```
CAT3560(config-cmap)# match vlan vvlan-id
```

```
CAT3560(config-cmap)# match class-map VOICE
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all INGRESS-VVLAN-VOICE-SIGNALING
```

```
CAT3560(config-cmap)# match vlan vvlan-id
```

```
CAT3560(config-cmap)# match class-map VOICE-SIGNALING
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# class-map match-all INGRESS-DVLAN
```

```
CAT3560(config-cmap)# match vlan dvlan-id
```

```
CAT3560(config-cmap)# match class-map INGRESS-DATA
```

```
CAT3560(config-cmap)#
```

```
CAT3560(config-cmap)# policy-map EGRESS-RATE-LIMITER
```

```
CAT3560(config-pmap)# class EGRESS-DSCP-0
```

```
CAT3560(config-pmap-c)# police aggregate AGG-POL-6M-DEFAULT-OUT
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class EGRESS-DSCP-8
```

```
CAT3560(config-pmap-c)# police aggregate AGG-POL-6M-DEFAULT-OUT
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class EGRESS-DSCP-16
```

```
CAT3560(config-pmap-c)# police aggregate AGG-POL-6M-DEFAULT-OUT
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class EGRESS-DSCP-32
```

```
CAT3560(config-pmap-c)# police aggregate AGG-POL-6M-DEFAULT-OUT
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class EGRESS-DSCP-48
```

```
CAT3560(config-pmap-c)# police aggregate AGG-POL-6M-DEFAULT-OUT
```

```
CAT3560(config-pmap-c)# class EGRESS-DSCP-56
```

```
CAT3560(config-pmap-c)# police aggregate AGG-POL-6M-DEFAULT-OUT
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class EGRESS-VOICE
```

```
CAT3560(config-pmap-c)# police aggregate AGG-POL-1M-VOICE-OUT
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class EGRESS-VOICE-SIGNALING
```

```
CAT3560(config-pmap-c)# police aggregate AGG-POL-1M-VOICE-OUT
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# policy-map INGRESS-QOS
```

```
CAT3560(config-pmap)# class INGRESS-VVLAN-VOICE
```

```
CAT3560(config-pmap-c)# set ip dscp 46
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class INGRESS-VVLAN-CALL-SIGNALING
```

```
CAT3560(config-pmap-c)# set ip dscp 24
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class INGRESS-DVLAN
```

```
CAT3560(config-pmap-c)# set ip dscp 0
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# class class-default
```

```
CAT3560(config-pmap-c)# set ip dscp 0
```

```
CAT3560(config-pmap-c)#
```

```
CAT3560(config-pmap-c)# interface interface id
```

```
CAT3560(config-if)# description 11Mb towards Wireless Access Point
```

```
CAT3560(config-if)# switchport access dvlan-id
```

```
CAT3560(config-if)# switchport voice vvlan-id
```

```
CAT3560(config-if)# mls qos trust dscp
```

```
CAT3560(config-if)# service-policy output EGRESS-RATE-LIMITER
```

```
CAT3560(config-if)# service-policy input INGRESS-QOS
```

Cisco 6500

```
CAT6500> (enable) set qos enable
```

```
CAT6500> (enable) set qos cos-dscp-map 0 8 16 24 32 46 48 56
```

```
CAT6500> (enable) set qos policed-dscp-map 24,26,46:0
```

```
CAT6500> (enable)
```

```
CAT6500> (enable) set qos policer microflow VOICE-OUT rate 1000 burst 32 policed-dscp
```

```
CAT6500> (enable) set qos policer microflow DATA-OUT rate 6000 burst 32 drop
```

```
CAT6500> (enable)
```

```
CAT6500> (enable) set qos acl ip AP-VOICE-EGRESS dscp 24 microflow VOICE-OUT ip any any 
dscp-field 24
```

```
CAT6500> (enable) set qos acl ip AP-VOICE-EGRESS dscp 24 microflow VOICE-OUT ip any any 
dscp-field 26
```

```
CAT6500> (enable) set qos acl ip AP-VOICE-EGRESS dscp 46 microflow VOICE-OUT ip any any 
dscp-field 46
```

```
CAT6500> (enable) set qos acl ip AP-DATA-EGRESS dscp 0 microflow DATA-OUT ip any any
```

```
CAT6500> (enable)
```

```
CAT6500> (enable) set qos acl ip AP-VOICE-INGRESS dscp 24 ip any any dscp-field 26
```

```
CAT6500> (enable) set qos acl ip AP-VOICE-INGRESS trust-dscp ip any any
```

```
CAT6500> (enable) set qos acl ip AP-DATA-INGRESS dscp 0 ip any any
```

```
CAT6500> (enable)
```

```
CAT6500> (enable) set qos acl map AP-VOICE-EGRESS vvlan-id output
```

```
CAT6500> (enable) set qos acl map AP-DATA-EGRESS dvlan-id output
```

```
CAT6500> (enable) set qos acl map AP-VOICE-INGRESS vvlan-id input
```

```
CAT6500> (enable) set qos acl map AP-DATA-INGRESS dvlan-id input
```

```
CAT6500> (enable)
```

```
CAT6500> (enable) set port qos mod/port vlan-based
```

```
CAT6500> (enable)
```

```
CAT6500> (enable) set port qos mod/port trust trust-dscp
```

```
CAT6500> (enable)
```

## Endpoint Features Summary

Table 12-1 summarizes the Cisco IP Telephony features for Cisco analog gateways and Table 12-2 summarizes the features for Cisco IP Phones.

Table 12-1 Analog Gateway Features

Ethernet Connection

Y 2

Y 3

Maximum number of Analog Ports

24

2

Caller ID

Y

N

Call Waiting

Y

Y

Caller ID on Call Waiting

N

N

Call Hold

Y 4

Y

Call Transfer

Y 5

Y

Call Forward

Y

Y

Auto-Answer

N

N

Ad Hoc Conference

Y

Y

Meet-Me Conference

Y

Y

Call Pickup

Y

Y

Group Pickup

Y

Y

Redial

Y

Y

Speed Dial

Y

Y

On-hook Dialing

N

N

Voice Mail Access

Y 6

Y 7

Message Waiting Indicator (MWI)

Y 7

Y 7

Music on Hold (MoH)

Y 8

Y 9

Mute

N

N

Call Preservation

N

N

Call Admission Control

N

N

Local Voice Busy-Out

N

N

Private Line Automatic Ringdown (PLAR)

Y

Y

Hunt Group

Y

Y

Dial Plan Mapping

N

N

Supervisory Disconnect

N

N

Signaling Packet ToS Value Marking

0x68

0x68

Media Packet ToS Value Marking

0xA0

0xA0

Fax Pass-Through

Y

Y

Fax Relay

N

N

Skinny Client Control Protocol (SCCP)

Y

Y

Session Initiation Protocol (SIP)

Y

Y

H.323

Y

Y

G.711

Y

Y

G.729

Y

Y

Voice Activity Detection (VAD)

Y

Y

Comfort Noise Generation (CNG)

Y

Y

1 SCCP call control

2 Two 10BaseT/100BaseT

3 Two 10BaseT/100BaseT for Cisco ATA 188; one 10BaseT for Cisco ATA 186

4 SCCP call control

5 SCCP call control

6 Only on SCCP and SIP version

7 Only on SCCP and SIP version

8 Supports only unicast MoH

9 Supports only unicast MoH

Table 12-2 Cisco Unified IP Phone Features

Ethernet Connection

Y 2

Y 2

Y 2

Y 3

Y 3

N

Y 4

Y 3

Y 3

Y 3

Ethernet Switch

N

N

N

Y

Y

N

N

Y

Y

Y

Cisco Power-Over-Ethernet (PoE)

Y

Y

Y

Y

Y

N

N

Y

Y

Y

IEEE 802.3af Power-Over-Ethernet (PoE)

N

N

N

N

N

N

N

N

N

Y

Localization

N

Y

N

N

Y

N

N

Y

Y

Y

Directory Number

1

1

1

1

1

6

1

2

6

8

Liquid Crystal Display

N

Y

Y

Y

Y

Y

Y

Y

Y

Y

Caller ID

N

Y

Y

Y

Y

Y

Y

Y

Y

Y

Call Waiting

N

Y

Y

Y

Y

Y

Y

Y

Y

Y

Caller ID on Call Waiting

N

Y

Y

Y

Y

Y

Y

Y

Y

Y

Call Hold

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Call Transfer

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Call Forward

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Auto-Answer

Y

Y

N

N

Y

Y

N

Y

Y

Y

Ad Hoc Conference

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Meet-Me Conference

N

Y

Y

Y

Y

Y

Y

Y

Y

Y

Call Pickup

N

Y

Y

Y

Y

Y

Y

Y

Y

Y

Group Pickup

N

Y

Y

Y

Y

Y

Y

Y

Y

Y

Redial

5 Y

Y 5

Y 5

Y 5

Y 5

Y

Y

Y

Y

Y

Speed Dial

Y

Y

Y

Y

Y

Y

N

Y

Y

Y

On-hook Dialing

N

Y

Y

Y

Y

Y

Y

Y

Y

Y

Voice Mail Access

Y

Y

Y

Y

Y

Y

N

Y

Y

Y

Message Waiting Indicator (MWI)

Y

Y

Y

Y

Y

Y

N

Y

Y

Y

Video call

N

N

N

N

N

N

N

Y

Y

Y

Music on Hold (MoH)

Y

Y

Y

Y

Y

Y 6

Y

Y

Y

Y

Speaker

N

Y 7

Y 7

Y 7

Y 7

N

Y

Y

Y

Y

Headset Jack

N

N

N

N

N

Y 8

N

Y

Y

Y

Mute

N

N

Y

Y

N

Y

Y

Y

Y

Y

Disable General Attribute Registration Protocol (GARP)

Y

Y

Y

Y

Y

N

N

Y

Y

Y

Signaling and Media Encryption

N

N

N

N

N

Y 9

N

Y

Y

Y

Signaling Integrity

N

N

N

N

N

N

N

Y

Y

Y

Manufacturing-Install ed Certificate (X.509v3)

N

N

N

N

N

N

N

N

N

Y

Field-Installed Certificate

N

N

N

N

N

N

N

Y

Y

N

Third-Party XML Service

N

Y

N

N

Y

N

N

Y

Y

Y

External Microphone and Speaker

N

N

N

N

N

N

N

N

N

Y

Hunt Group

Y

Y

Y

Y

Y

YN

Y

Y

Y

Y

Dial Plan Mapping

N

N

N

N

N

N

N

N

N

N

Signaling Packet ToS Value Marking

0x60

0x68

0x68

0x68

0x60

0x68

0x68

0x60

0x60

0x60

Media Packet ToS Value Marking

0xB8

0xB8

0xB8

0xB8

0xB8

0xB8

0xB8

0xB8

0xB8

0xB8

Skinny Client Control Protocol (SCCP)

Y

Y

Y

Y

Y

Y

N

Y

Y

Y

Session Initiation Protocol (SIP)

N

Y

N

N

Y

N

N

Y

Y

N

H.323

N

Y

N

N

N

N

Y

N

N

N

G.711

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

G.729

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Voice Activity Detection (VAD)

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Comfort Noise Generation (CNG)

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

1 Note that the complete names of these products have been truncated to save space in this table (each product number is preceded by the phrase "Cisco Unified IP Phone."

2 One 10BaseT

3 Two 10BaseT/100BaseT

4 One 10BaseT/100BaseT

5 Last Number Redial

6 Supports only unicast MoH

7 One-way listen mode

8 The only supported headset for the Cisco Unified IP Phone 7920 is one with a 2.5 mm jack.

9 Signaling and Media Encryption are available with Static WEP and LEAP security configurations.

| Cos Value | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| DSCP Value | 0 | 8 | 16 | 24 | 32 | 40 | 48 | 56 |

| Feature | Cisco VG224 1 | Cisco ATA 186 and Cisco ATA 188 |
|---|---|---|
| Ethernet Connection | Y 2 | Y 3 |
| Maximum number of Analog Ports | 24 | 2 |
| Caller ID | Y | N |
| Call Waiting | Y | Y |
| Caller ID on Call Waiting | N | N |
| Call Hold | Y 4 | Y |
| Call Transfer | Y 5 | Y |
| Call Forward | Y | Y |
| Auto-Answer | N | N |
| Ad Hoc Conference | Y | Y |
| Meet-Me Conference | Y | Y |
| Call Pickup | Y | Y |
| Group Pickup | Y | Y |
| Redial | Y | Y |
| Speed Dial | Y | Y |
| On-hook Dialing | N | N |
| Voice Mail Access | Y 6 | Y 7 |
| Message Waiting Indicator (MWI) | Y 7 | Y 7 |
| Music on Hold (MoH) | Y 8 | Y 9 |
| Mute | N | N |
| Call Preservation | N | N |
| Call Admission Control | N | N |
| Local Voice Busy-Out | N | N |
| Private Line Automatic Ringdown (PLAR) | Y | Y |
| Hunt Group | Y | Y |
| Dial Plan Mapping | N | N |
| Supervisory Disconnect | N | N |
| Signaling Packet ToS Value Marking | 0x68 | 0x68 |
| Media Packet ToS Value Marking | 0xA0 | 0xA0 |
| Fax Pass-Through | Y | Y |
| Fax Relay | N | N |
| Skinny Client Control Protocol (SCCP) | Y | Y |
| Session Initiation Protocol (SIP) | Y | Y |
| H.323 | Y | Y |
| G.711 | Y | Y |
| G.729 | Y | Y |
| Voice Activity Detection (VAD) | Y | Y |
| Comfort Noise Generation (CNG) | Y | Y |

| 1 SCCP call control 2 Two 10BaseT/100BaseT 3 Two 10BaseT/100BaseT for Cisco ATA 188; one 10BaseT for Cisco ATA 186 4 SCCP call control 5 SCCP call control 6 Only on SCCP and SIP version 7 Only on SCCP and SIP version 8 Supports only unicast MoH 9 Supports only unicast MoH |
|---|

| Feature | 7902G 1 | 7905G | 7910G | 7910 +SW | 7912G | 7920G | 7935G, 7936G | 7940G | 7960G | 7970G |
|---|---|---|---|---|---|---|---|---|---|---|
| Ethernet Connection | Y 2 | Y 2 | Y 2 | Y 3 | Y 3 | N | Y 4 | Y 3 | Y 3 | Y 3 |
| Ethernet Switch | N | N | N | Y | Y | N | N | Y | Y | Y |
| Cisco Power-Over-Ethernet (PoE) | Y | Y | Y | Y | Y | N | N | Y | Y | Y |
| IEEE 802.3af Power-Over-Ethernet (PoE) | N | N | N | N | N | N | N | N | N | Y |
| Localization | N | Y | N | N | Y | N | N | Y | Y | Y |
| Directory Number | 1 | 1 | 1 | 1 | 1 | 6 | 1 | 2 | 6 | 8 |
| Liquid Crystal Display | N | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Caller ID | N | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Call Waiting | N | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Caller ID on Call Waiting | N | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Call Hold | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Call Transfer | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Call Forward | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Auto-Answer | Y | Y | N | N | Y | Y | N | Y | Y | Y |
| Ad Hoc Conference | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Meet-Me Conference | N | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Call Pickup | N | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Group Pickup | N | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Redial | 5 Y | Y 5 | Y 5 | Y 5 | Y 5 | Y | Y | Y | Y | Y |
| Speed Dial | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| On-hook Dialing | N | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Voice Mail Access | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| Message Waiting Indicator (MWI) | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| Video call | N | N | N | N | N | N | N | Y | Y | Y |
| Music on Hold (MoH) | Y | Y | Y | Y | Y | Y 6 | Y | Y | Y | Y |
| Speaker | N | Y 7 | Y 7 | Y 7 | Y 7 | N | Y | Y | Y | Y |
| Headset Jack | N | N | N | N | N | Y 8 | N | Y | Y | Y |
| Mute | N | N | Y | Y | N | Y | Y | Y | Y | Y |
| Disable General Attribute Registration Protocol (GARP) | Y | Y | Y | Y | Y | N | N | Y | Y | Y |
| Signaling and Media Encryption | N | N | N | N | N | Y 9 | N | Y | Y | Y |
| Signaling Integrity | N | N | N | N | N | N | N | Y | Y | Y |
| Manufacturing-Install ed Certificate (X.509v3) | N | N | N | N | N | N | N | N | N | Y |
| Field-Installed Certificate | N | N | N | N | N | N | N | Y | Y | N |
| Third-Party XML Service | N | Y | N | N | Y | N | N | Y | Y | Y |
| External Microphone and Speaker | N | N | N | N | N | N | N | N | N | Y |
| Hunt Group | Y | Y | Y | Y | Y | YN | Y | Y | Y | Y |
| Dial Plan Mapping | N | N | N | N | N | N | N | N | N | N |
| Signaling Packet ToS Value Marking | 0x60 | 0x68 | 0x68 | 0x68 | 0x60 | 0x68 | 0x68 | 0x60 | 0x60 | 0x60 |
| Media Packet ToS Value Marking | 0xB8 | 0xB8 | 0xB8 | 0xB8 | 0xB8 | 0xB8 | 0xB8 | 0xB8 | 0xB8 | 0xB8 |
| Skinny Client Control Protocol (SCCP) | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| Session Initiation Protocol (SIP) | N | Y | N | N | Y | N | N | Y | Y | N |
| H.323 | N | Y | N | N | N | N | Y | N | N | N |
| G.711 | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| G.729 | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Voice Activity Detection (VAD) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Comfort Noise Generation (CNG) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |

| 1 Note that the complete names of these products have been truncated to save space in this table (each product number is preceded by the phrase "Cisco Unified IP Phone." 2 One 10BaseT 3 Two 10BaseT/100BaseT 4 One 10BaseT/100BaseT 5 Last Number Redial 6 Supports only unicast MoH 7 One-way listen mode 8 The only supported headset for the Cisco Unified IP Phone 7920 is one with a 2.5 mm jack. 9 Signaling and Media Encryption are available with Static WEP and LEAP security configurations. |
|---|