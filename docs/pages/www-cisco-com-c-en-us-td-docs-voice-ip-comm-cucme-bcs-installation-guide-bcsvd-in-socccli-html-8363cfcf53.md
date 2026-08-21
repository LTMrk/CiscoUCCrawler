---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-bcs-installation-guide-bcsvd-in-socccli-html-8363cfcf53
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/bcs/installation/guide/bcsvd_in/SOCCcli.html
retrieved_at: 2026-08-21T22:58:47.047253+00:00
---

Installing Cisco Business Communications Solution Verified Designs

# Installing Cisco Business Communications Solution Verified Designs

Updated: November 2, 2007

Chapter: Continuing Cisco BCS Verified Designs Configuration Using CLI

## Chapter: Continuing Cisco BCS Verified Designs Configuration Using CLI

## Continuing the Cisco BCS Verified Designs Configuration Using CLI

This chapter describes the procedures using the command line interface (CLI) to continue Cisco Business Communications Solution Verified Designs configuration. Perform the procedures in this chapter using a terminal emulation utility such as Hyperterminal through the console port of your router.

Each procedure provides a list of summary and detailed steps that you can follow. Follow the detailed steps if you need examples and explanations of each CLI entry.

## Contents

This chapter provides the following sections:

• Configuring Subinterfaces for VLANs

• Configuring a DHCP IP Address Pool for the Data Network

• Configuring Separate Data and Voice VLANs

• What to Do Next

## Configuring Subinterfaces for VLANs

This task creates subinterfaces for a Cisco LAN switch that will be carry voice and data on the network.

Summary steps (see Figure 110 ) list the steps necessary to configure the subinterfaces. For detailed steps including examples, see Table 6 .

Figure 110 CLI for Configuring Subinterfaces for VLANs

### Summary Steps

1. enable

2. configure terminal

3. interface gigabitethernet slot/port

4. no ip address

5. interface gigabitethernet slot/port.subinterface

6. encapsulation dot1q vlan-id

7. ip address subnet mask

8. interface gigabitethernet slot/port.subinterface

9. encapsulation dot1q vlan-id

10. ip address subnet mask

11. exit

12. interface service-engine slot/port

13. ip unnumbered gigabitethernet slot/port.subinterface

14. exit

15. exit

16. wr

Note It is recommended to save a copy of the router configuration for backup purposes.

### Detailed Steps

Table 6 Detailed Steps for Configuring Subinterfaces for VLANs

Step 1

enable

Router>

Enters privileged EXEC mode.

Step 2

configure terminal

Router# configure terminal

Enters global configuration mode.

Step 3

interface gigabitethernet slot/port

Router(config)# interface gigabitethernet 0/0

Configures the interface and enters interface configuration mode.

Step 4

no ip address

Router(config-if)# no ip address

Disables IP processing for the specified interface.

Step 5

interface gigabitethernet slot/port.subinterface

Router(config)# interface gigabitethernet 0/0.10

Configures the subinterface and enters subinterface configuration mode. It is recommended to set the subinterface to the same value as the vlan-id .

Step 6

encapsulation dot1q vlan-id

```
Router(config-subif)# encapsulation dot1q 10
```

Sets 802.1q encapsulation for the subinterface.

Step 7

ip address ip-address subnet mask

```
Router(config-subif)# ip address 10.1.10.1 
255.255.255.0
```

Sets the IP address for the subinterface.

Step 8

interface gigabitethernet slot/port.subinterface

Router(config-subif)# interface gigabitethernet 0/0.20

Configures the subinterface. It is recommended to set the subinterface to the same value as the vlan-id .

Step 9

encapsulation dot1q vlan-id

```
Router(config-subif)# encapsulation dot1q 20
```

Sets 802.1q encapsulation for the subinterface.

Step 10

ip address ip-address subnet mask

```
Router(config-subif)# ip address 10.1.20.1 
255.255.255.0
```

Sets the IP address for the subinterface.

Step 11

exit

Router(config)# exit

Exits subinterface configuration mode.

Step 12

interface service-engine slot/port

Router(config)# interface service-engine 0/1

Enters interface configuration mode for a network module (NM) or an advanced integration module (AIM) in slot 0, port 1.

Step 13

ip unnumbered gigabitethernet slot/port.subinterface

Router(config-if)# ip unnumbered gigabitethernet 0/0.20

Enables IP processing on the gigabitethernet subinterface without assigning an explicit IP address to the subinterface. This subinterface represents the IP address of the Cisco CME router.

Step 14

exit

Router(config-if)# exit

Exits interface configuration mode.

Step 15

exit

Router(config)# exit

Exits global configuration mode.

Step 16

wr

Router# wr

Writes the changes to the configuration file.

### Testing the Installation

At this point, IP phones should no longer be connected to Cisco CME. No dial tone should be present if the speaker button is pressed.

Note If the IP phones seem as if they still have a configuration, the phones have not timed out yet.

### What to Do Next

Once you configure subinterfaces for a Cisco LAN switch using Summary or Detailed Steps, proceed to configure your DHCP IP address pool for the data network (see the "Configuring a DHCP IP Address Pool for the Data Network" section ).

## Configuring a DHCP IP Address Pool for the Data Network

This section describes the configuration of a DHCP IP address pool for your data network. If you do not already have a DHCP pool setup for your data, use this section to set up the data IP subnet.

This procedure creates a large shared pool of IP addresses, in which all DHCP clients receive the same information.

Summary steps (see Figure 111 ) list the steps necessary to set up a DHCP IP address pool for the data network. For detailed steps with examples, see Table 7 .

Figure 111 Configuring DHCP IP Address Pool for Data

### Summary Steps

1. enable

2. configure terminal

3. ip dhcp excluded-address low - ip-address [ high-ip-address ]

4. ip dhcp pool pool-name

5. network ip-address [ mask | / prefix-length ]

6. default-router ip-address

7. exit

8. exit

9. wr

Note It is recommended to save a copy of the router configuration for backup purposes.

### Detailed Steps

Table 7 Detailed Steps for Configuring a DHCP IP Address Pool

Step 1

enable

Router>enable

Enters privileged EXEC mode.

Step 2

configure terminal

Router# configure terminal

Enters global configuration mode.

Step 3

ip dhcp excluded-address low - ip-address [ high-ip address ]

Router(config)# dhcp excluded-address 10.1.10.1 10.1.10.10

Specifies IP addresses that should not be assigned to clients.

Step 4

ip dhcp pool pool-name

Router(config)# ip dhcp pool data

Creates a name for the DHCP server address pool and enters DHCP pool configuration mode.

Step 5

network ip-address [ mask | / prefix-length ]

```
Router(dhcp-config)# network 10.1.10.1 255.255.255.0
```

Specifies the IP address of the DHCP address pool and the optional mask or number of bits in the address prefix, preceded by a forward slash.

Step 6

default-router ip-address

```
Router(dhcp-config)# default-router 10.1.10.1
```

Specifies the router to which the IP phones are connected. This router is either a Cisco CME router or any Cisco router attached to the Cisco CME router.

Note As long as the Cisco IP phones have connection to the Cisco CME router, the Cisco IP phones can get the required network details.

Step 7

exit

Router(dhcp-config)# exit

Exits DHCP pool configuration mode.

Step 8

exit

Router(config)# exit

Exits global configuration mode.

Step 9

wr

Router# wr

Writes the changes to the configuration file.

### Testing the Installation

The DHCP server is now set up for the data side of the network. Perform the following steps to ensure that DHCP is properly set up.

Step 1 Enter the show ip dhcp server stat command to ensure that the DHCP server is running and to display any queries made to it.

Step 2 Enter the show ip dhcp pool command to display configured DHCP pools.

### What to Do Next

Once you configure a DHCP IP pool for the data network using the Summary or Detailed Steps, proceed to configure separate voice and data VLANs for the data network (see the "Configuring Separate Data and Voice VLANs" section ).

## Configuring Separate Data and Voice VLANs

It is recommended that you create separate VLANs for voice and data on your switch.

Summary steps (see Figure 112 ) list the steps necessary to set up separate VLANs for your voice and data networks. For detailed steps with examples, see Table 8 .

Figure 112 Configuring Separate Data and Voice VLANs

### Summary Steps

1. enable

2. vlan data

3. vlan vlan-number name vlan-name (for data)

4. vlan vlan-number name vlan-name (for voice)

5. apply

6. exit

7. configure terminal

8. interface vlan vlan-number

9. ip address ip-address subnet mask

10. exit

11. interface vlan vlan-number

12. ip address ip-address subnet mask

13. exit

14. exit

15. wr

Note It is recommended to save a copy of the switch configuration for backup purposes.

### Detailed Steps

Table 8 Detailed Steps for Configuring Separate Data and Voice VLANs

Step 1

enable

Switch> enable

Enters privileged EXEC mode.

Step 2

vlan data

Switch# vlan data

Enters VLAN configuration mode and defines a string used to name the VLAN.

Step 3

vlan vlan-number name vlan-name

Switch(vlan)# vlan 10 name DATA

VLAN 10 modified

Name: DATA

Configures the specified VLAN and defines a text string used as the name of the VLAN.

Step 4

vlan vlan-number name vlan-name

Switch(vlan)# vlan 20 name VOICE

VLAN 20 modified

Name: VOICE

Configures the specified VLAN and defines a text string used as the name of the VLAN.

Step 5

apply

Switch(vlan)# apply

APPLY completed.

Saves changed configuration parameters.

Step 6

exit

Switch(vlan)# exit

APPLY completed

Exiting....

Exits VLAN configuration mode.

Step 7

configure terminal

Switch# configure terminal

Enters global configuration mode.

Step 8

interface vlan-number

Switch(config)# interface vlan 10

Configures the specified interface type and enters interface configuration mode.

Step 9

ip address ip-address subnet mask

Switch(config-if)# ip address 10.1.10.10 255.255.255.0

Assigns an IP address to the VLAN.

Step 10

exit

Switch(config-if)# exit

Exits interface configuration mode.

Step 11

interface vlan-number

Switch(config)# interface vlan 20

Configures the specified interface type and enters interface configuration mode.

Step 12

ip address ip-address subnet mask

Switch(config-if)# ip address 10.1.20.10 255.255.255.0

Assigns an IP address to the VLAN.

Step 13

exit

Switch(config-if)# exit

Exits interface configuration mode.

Step 14

exit

Switch(config)# exit

Exits global configuration mode.

Step 15

wr

Switch# wr

Writes the changes to the configuration file.

Figure 113 summarizes the LAN switch interface configuration.

Figure 113 LAN Switch Interface Configuration

This completes the voice network configuration.

### Testing the Installation

VLANs are now configured on the switch. Use the show interface command to verify that the VLANs are configured. IP addresssing will not appear in any routing table until the interfaces are running.

Once the switch is configured, IP phones and stations should connect using different IP addressing.

Step 1 Enter the ipconfig command to see the IP configuration.

Step 2 Press settings on the IP phone and look for IP addressing under Network Configuration.

Step 3 Plug in multiple IP phones and initiate a call.

## What to Do Next

To configure security on the voice network, see the "Configuring Security on the Voice Network" section .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> | Enters privileged EXEC mode. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | interface gigabitethernet slot/port Example: Router(config)# interface gigabitethernet 0/0 | Configures the interface and enters interface configuration mode. |
| Step 4 | no ip address Example: Router(config-if)# no ip address | Disables IP processing for the specified interface. |
| Step 5 | interface gigabitethernet slot/port.subinterface Example: Router(config)# interface gigabitethernet 0/0.10 | Configures the subinterface and enters subinterface configuration mode. It is recommended to set the subinterface to the same value as the vlan-id . |
| Step 6 | encapsulation dot1q vlan-id Example: Router(config-subif)# encapsulation dot1q 10 | Sets 802.1q encapsulation for the subinterface. |
| Step 7 | ip address ip-address subnet mask Example: Router(config-subif)# ip address 10.1.10.1 
255.255.255.0 | Sets the IP address for the subinterface. |
| Step 8 | interface gigabitethernet slot/port.subinterface Example: Router(config-subif)# interface gigabitethernet 0/0.20 | Configures the subinterface. It is recommended to set the subinterface to the same value as the vlan-id . |
| Step 9 | encapsulation dot1q vlan-id Example: Router(config-subif)# encapsulation dot1q 20 | Sets 802.1q encapsulation for the subinterface. |
| Step 10 | ip address ip-address subnet mask Example: Router(config-subif)# ip address 10.1.20.1 
255.255.255.0 | Sets the IP address for the subinterface. |
| Step 11 | exit Example: Router(config)# exit | Exits subinterface configuration mode. |
| Step 12 | interface service-engine slot/port Example: Router(config)# interface service-engine 0/1 | Enters interface configuration mode for a network module (NM) or an advanced integration module (AIM) in slot 0, port 1. |
| Step 13 | ip unnumbered gigabitethernet slot/port.subinterface Example: Router(config-if)# ip unnumbered gigabitethernet 0/0.20 | Enables IP processing on the gigabitethernet subinterface without assigning an explicit IP address to the subinterface. This subinterface represents the IP address of the Cisco CME router. |
| Step 14 | exit Example: Router(config-if)# exit | Exits interface configuration mode. |
| Step 15 | exit Example: Router(config)# exit | Exits global configuration mode. |
| Step 16 | wr Example: Router# wr | Writes the changes to the configuration file. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router>enable | Enters privileged EXEC mode. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ip dhcp excluded-address low - ip-address [ high-ip address ] Example: Router(config)# dhcp excluded-address 10.1.10.1 10.1.10.10 | Specifies IP addresses that should not be assigned to clients. |
| Step 4 | ip dhcp pool pool-name Example: Router(config)# ip dhcp pool data | Creates a name for the DHCP server address pool and enters DHCP pool configuration mode. |
| Step 5 | network ip-address [ mask \| / prefix-length ] Example: Router(dhcp-config)# network 10.1.10.1 255.255.255.0 | Specifies the IP address of the DHCP address pool and the optional mask or number of bits in the address prefix, preceded by a forward slash. |
| Step 6 | default-router ip-address Example: Router(dhcp-config)# default-router 10.1.10.1 | Specifies the router to which the IP phones are connected. This router is either a Cisco CME router or any Cisco router attached to the Cisco CME router. Note As long as the Cisco IP phones have connection to the Cisco CME router, the Cisco IP phones can get the required network details. |
| Step 7 | exit Example: Router(dhcp-config)# exit | Exits DHCP pool configuration mode. |
| Step 8 | exit Example: Router(config)# exit | Exits global configuration mode. |
| Step 9 | wr Example: Router# wr | Writes the changes to the configuration file. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Switch> enable | Enters privileged EXEC mode. |
| Step 2 | vlan data Example: Switch# vlan data | Enters VLAN configuration mode and defines a string used to name the VLAN. |
| Step 3 | vlan vlan-number name vlan-name Example: Switch(vlan)# vlan 10 name DATA VLAN 10 modified Name: DATA | Configures the specified VLAN and defines a text string used as the name of the VLAN. |
| Step 4 | vlan vlan-number name vlan-name Example: Switch(vlan)# vlan 20 name VOICE VLAN 20 modified Name: VOICE | Configures the specified VLAN and defines a text string used as the name of the VLAN. |
| Step 5 | apply Example: Switch(vlan)# apply APPLY completed. | Saves changed configuration parameters. |
| Step 6 | exit Example: Switch(vlan)# exit APPLY completed Exiting.... | Exits VLAN configuration mode. |
| Step 7 | configure terminal Example: Switch# configure terminal | Enters global configuration mode. |
| Step 8 | interface vlan-number Example: Switch(config)# interface vlan 10 | Configures the specified interface type and enters interface configuration mode. |
| Step 9 | ip address ip-address subnet mask Example: Switch(config-if)# ip address 10.1.10.10 255.255.255.0 | Assigns an IP address to the VLAN. |
| Step 10 | exit Example: Switch(config-if)# exit | Exits interface configuration mode. |
| Step 11 | interface vlan-number Example: Switch(config)# interface vlan 20 | Configures the specified interface type and enters interface configuration mode. |
| Step 12 | ip address ip-address subnet mask Example: Switch(config-if)# ip address 10.1.20.10 255.255.255.0 | Assigns an IP address to the VLAN. |
| Step 13 | exit Example: Switch(config-if)# exit | Exits interface configuration mode. |
| Step 14 | exit Example: Switch(config)# exit | Exits global configuration mode. |
| Step 15 | wr Example: Switch# wr | Writes the changes to the configuration file. |