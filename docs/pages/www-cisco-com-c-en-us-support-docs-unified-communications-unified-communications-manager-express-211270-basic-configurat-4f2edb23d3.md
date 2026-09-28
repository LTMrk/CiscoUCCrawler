---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-express-211270-basic-configurat-4f2edb23d3
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-express/211270-Basic-Configuration-Guide-for-CUCME-CME.html
retrieved_at: 2026-08-21T09:46:56.745340+00:00
---

Configuration Guide for Cisco Unified Communications Manager Express

# Configuration Guide for Cisco Unified Communications Manager Express

### Download Options

Updated: February 28, 2020

Document ID: 211270

Contents

## Contents

## Introduction

This document describes the steps in order to configure Cisco Unified Communications Manager Express (CUCME/CME).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco IOS ® Router

- IP Phones

- Connection to the PSTN (Optional)

### Components Used

The information in this document is based on these software and hardware versions:

- Any CUCME version

- Any IP Phone

The information in this document was created from the devices in a specific lab environment. All of the devices used in here started with cleared (default) configurations. If your network is live, make sure that you understand the potential impact of any command.

## Configure

Refer to this image and the steps that are documented in order to configure the Cisco Call Manager Express.

### Step 1. Configure a Switch Trunk Port

```
SwitchA(config-if)#switchport trunk encapsulation dot1q SwitchA(config-if)# switchport mode trunk
```

#### Step 1.1. Create VLAN

```
SwitchA# configure terminal SwitchA(config)# vlan 10 SwitchA(config-vlan)# name VOICE SwitchA(config-vlan)# exit SwitchA(config)# vlan 50 SwitchA(config-vlan)# name DATA
```

#### Step 1.2. Assign Switchport to a VLAN

```
SwitchA# configure terminal SwitchA(config)# interface fa0/10 SwitchA(config-if)# switchport mode access SwitchA(config-if)# switchport access vlan 50
```

#### Step 1.3. Assign Voice and Data VLANs

```
SwitchA# configure terminal SwitchA(config)#interfac range fa0/1 - 4 SwitchA(config-if-range)# switchport mode access SwitchA(config-if-range)# switchport access vlan 50 SwitchA(config-if-range)# switchport voice vlan 10
```

#### Step 1.4. Configure a Trunk to the CME Router

```
SwitchA# configure terminal SwitchA(config)# interface fa0/20 SwitchA(config-if)# description CONNECTION TO ROUTER-ON-A-STICK CME ROUTER SwitchA(config-if)# switchport trunk encapsulation dot1q SwitchA(config-if)# switchport mode trunk
```

### Step 2. Configure Inter-VLAN Routing

```
Router# configure terminal Router(config)# interface fa0/0 Router(config-if)# no ip address Router(config-if)#exit Router(config)# interface fa0/0.10 Router(config-subif)# description ROUTER INTERFACE FOR VOICE VLAN Router(config-subif)# encapsulation dot1q 10 Router(config-subif)# ip address 172.16.1.1 255.255.255.0 Router(config-subif)# ip helper-address 172.16.2.5 Router(config-subif)#exit Router(config)# interface fa0/0.50 Router(config-subif)# description ROUTER INTERFACE FOR DATA VLAN Router(config-subif)# encapsulation dot1q 50 Router(config-subif)# ip address 172.16.2.1 255.255.255.0
```

### Step 3. Configure a Router-Based DHCP Server

```
RTR# configure terminal RTR(config)# ip dhcp excluded-address 172.16.1.1 172.16.1.9 RTR(config)# ip dhcp excluded-address 172.16.2.1 172.16.2.9 RTR(config)# ip dhcp pool DATA_SCOPE RTR(dhcp-config)# network 172.16.2.0 255.255.255.0 RTR(dhcp-config)# default-router 172.16.2.1 RTR(dhcp-config)# dns-server 4.2.2.2 RTR(dhcp-config)# exit RTR(config)# ip dhcp pool VOICE_SCOPE RTR(dhcp-config)#netowrk 172.16.1.0 255.255.255.0 RTR(dhcp-config)# default-router 172.16.1.1 RTR(dhcp-config)# option 150 ip 172.16.1.1 RTR(dhcp-config)# dns-server 4.2.2.2
```

### Step 4. Set the Clock of a Cisco Device with NTP

```
RTR# configure terminal RTR(config)# ntp server 64.209.210.20 RTR(config)# clock timezone Cairo +2
```

### Step 5. Install CME Files into Flash Memory

```
CME_Voice# archive tar /xtract tftp://172.16.2.5/<file name> flash:
```

### Step 6. Configure Router-Based TFTP Services for IP Phone Firmware Files

```
CME_Voice# configure terminal CME_Voice(config)# tftp-server flash:/phone/<file name>
```

### Step 7. Configure the Cisco Unified CME System-Level Functions

Provision CME Phone and Directory Number:

```
CME_Voice# configure terminal CME_Voice(config)# telephony-service CME_Voice(config-telephony)# max ephone x CME_Voice(config-telephony)# max dn x
```

Configure CME for Firmware Loads:

```
CME_Voice# configure terminal CME_Voice(config)# tftp-server flash:/phone/<phone model>/<file name>
```

Set the firmware load for each phone:

```
CME_Voice# configure terminal CME_Voice(config)# load <phone model> <firmware load>
```

### Step 8. Source IP Address Information

```
CME_Voice# configure terminal CME_Voice(config)# telephony-service CME_Voice(config-telephony)# ip souerce address 172.16.1.1
```

### Step 9. Generation IP Phone Configuration File

```
CME_Voice# configure terminal CME_Voice(config)# telephony-service CME_Voice(config-telephony)# creat cnf-files
```

### Step 10. Verify Files Served by the CME TFTP Service

```
CME_Voice# show telephony-service tftp-bindings
```

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.