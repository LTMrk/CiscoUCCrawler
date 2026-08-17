---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be7000-installationguide-12-5-be7k-b-installation-guide-m5-1251-be7k-b--00d2dd2f78
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE7000/installationguide/12_5/be7k_b_installation-guide-M5-1251/be7k_b_installation-guide-1251_appendix_011.html
retrieved_at: 2026-08-17T01:47:24.966385+00:00
---

Installation Guide for Cisco Business Edition 7000H/M (M5), Release 12.5

# Installation Guide for Cisco Business Edition 7000H/M (M5), Release 12.5

Updated: February 19, 2021

Chapter: Example of Configuring NIC Teaming for the Business Edition 7000H/M

## Chapter: Example of Configuring NIC Teaming for the Business Edition 7000H/M

# Example of Configuring NIC Teaming for the Business Edition 7000H/M

## NIC Teaming

This section is an example only; it is not prescriptive guidance and is not the only recommendation you may see in Cisco documentation.
                                          This particular example may not be suitable or optimal for your specific networking environment. Consult Cisco network documentation
                                          and https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-qos-designs-considerations.html to devise the best way to interconnect your appliance with your network."

The Hypervisor NIC teaming feature allows multiple physical adapters to be associated with a vSwitch to provide load sharing
                              and failover connectivity to the external network.

### Failover and Load Balancing

When more physical adapters are assigned to a vSwitch, they may be assigned as either active or standby. Depending on how
                              the appliance is connected to the physical network, traffic from virtual machines may be load balanced across active connections and, in
                              the event of a link failure, a standby adapter is made active to take over.

### Switched Network Topologies

To maximize resiliency to failure, teamed interfaces are typically connected to different switching equipment. This might
                              involve connecting to separate line cards in a chassis, switches in a stack, or to independent devices.

Where independent physical switches are used, teamed interfaces should be set to active, allowing the Ethernet Spanning Tree
                              protocol to block connections that create a loop. In the event of a link or switch failure, the Spanning Tree protocol reconverges
                              to use a serviceable connection to the appliance . Where VLAN trunking is used, the Spanning Tree protocol can typically be configured per VLAN to prefer different connections
                              for DMZ and internal network traffic under normal operation.

If connections are made to a common logical switch (chassis or cluster) that supports IEEE 802.3ad link aggregation, it is
                              possible to load balance traffic across all active members of the link group under normal operation. Link aggregation can
                              accommodate link failures more quickly than Spanning Tree and is transparent to VLANs, so may be used with either dedicated
                              network, or VLAN trunk connections.

The following table illustrates how Business Edition appliance s may accommodate the network separation and NIC teaming.

## Configure NIC Teaming in ESXi

Step 1

Log in to VMware Embedded Host Client.

Step 2

Navigate to the Networking > Virtual Switches .

Step 3

Select Vswitch0 and click Edit settings tab.

Step 4

Select the Physical Adapters that should be added to the switch and click Next .

Step 5

Select the NIC Teaming tab.

Step 6

Use the Move Up and Move Down buttons to adjust the failover policy for the added ports. If you want to use an adapter for failover, move the adapter from
                                       the Active Adapter list to the Standby Adapter list.

Step 7

Click Save .

Step 8

Configure IEEE 802.3 link aggregation:

Select Vswitch0 and click Edit settings tab.

Edit the vSwitch Name

Select the NIC Teaming tab.

From the Load Balancing drop-down menu, select Route based on IP hash .

Click Save .

## Configure NIC
                        	 Teaming on Switch

When aggregating appliance interfaces, the switch ports to which they are connected must be configured to use 802.3ad link aggregation. The following
                              example illustrates how this may be configured using VLAN trunking to a Cisco Catalyst switch:

```
vlan 1
	name default
!
vlan 30
	name DMZ
!
interface GigabitEthernet1/1	
	description BE Server Network Interface 1 (Internal/DMZ trunk group)	
	switchport trunk allowed vlan 1,30
	switchport mode trunk
	spanning-tree portfast trunk
	channel-group 1 mode passive
!
interface GigabitEthernet1/5
	description BE Server Network Interface 2 (Internal/DMZ trunk group)
	switchport trunk allowed vlan 1,30
	switchport mode trunk	
	spanning-tree portfast trunk
	channel-group 1 mode passive
!
```

When connecting appliance interfaces to separate switches, use standard trunk port configuration (no channel-group). Do not use Spanning-Tree Portfast.

```
vlan 1
	name default
!
vlan 30
	name DMZ
!
interface GigabitEthernet1/1
	description BE Server Network Interface 1 (Internal/DMZ trunk)
	switchport trunk allowed vlan 1,30
	switchport mode trunk
!
```

The Spanning Tree VLAN cost command may be used balance traffic between links, if necessary.

| Note | This section is an example only; it is not prescriptive guidance and is not the only recommendation you may see in Cisco documentation.
                                          This particular example may not be suitable or optimal for your specific networking environment. Consult Cisco network documentation
                                          and https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-qos-designs-considerations.html to devise the best way to interconnect your appliance with your network." |
|---|---|

| Step 1 | Log in to VMware Embedded Host Client. |
|---|---|
| Step 2 | Navigate to the Networking > Virtual Switches . |
| Step 3 | Select Vswitch0 and click Edit settings tab. |
| Step 4 | Select the Physical Adapters that should be added to the switch and click Next . Note We recommend that you team a mix of motherboard and PCI card network adapters. | Note | We recommend that you team a mix of motherboard and PCI card network adapters. |
| Note | We recommend that you team a mix of motherboard and PCI card network adapters. |
| Step 5 | Select the NIC Teaming tab. |
| Step 6 | Use the Move Up and Move Down buttons to adjust the failover policy for the added ports. If you want to use an adapter for failover, move the adapter from
                                       the Active Adapter list to the Standby Adapter list. |
| Step 7 | Click Save . |
| Step 8 | Configure IEEE 802.3 link aggregation: Select Vswitch0 and click Edit settings tab. Edit the vSwitch Name Select the NIC Teaming tab. From the Load Balancing drop-down menu, select Route based on IP hash . Click Save . |

| Note | We recommend that you team a mix of motherboard and PCI card network adapters. |
|---|---|