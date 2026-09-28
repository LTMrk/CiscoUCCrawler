---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-admin-guide-at9x-b-ata191-192-admin-mp-at9x-b-ata191-1-f872e2e329
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/admin-guide/at9x_b_ata191-192-admin-mp/at9x_b_ata191-192-admin-mp_chapter_0101.html
retrieved_at: 2026-08-22T01:03:45.427739+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: Status and Statistics

## Chapter: Status and Statistics

# Status and Statistics

## System Information

Use the Status > System Information page to view information about the ATA and its current settings.

Field

Description

Model

The model number and product description.

Product ID

The product ID of the ATA.

VID

The VID of the ATA

Serial Number

The serial number of the ATA.

Hardware Revision

The hardware version number.

Boot Version

The boot firmware version number.

Boot Partition

The boot partition of the ATA.

Firmware Version

The current firmware version.

Internet MAC Address

The MAC address of the WAN interface.

Host Name

The host name of the ATA.

Domain Name

The domain name of the ATA.

Current Time

Time that is set on the ATA.

Time Zone

Time zone that is set on the ATA.

## Interface Information

Use the Status > Interface Information page to view information for the WAN interface (INTERNET port) and on ATA 192 only, the LAN interface (ETHERNET port).

### IPv4 Interface List

Field

Description

Interface

The name of the interface: WAN or LAN (ATA 192 only).

Connect Type

The type of connection configured for the interface.

IP Address

The IPv4 address of the interface.

Subnet Mask

The subnet mask of the interface.

MAC Address

The MAC address of the interface.

### IPv6 Interface List

Field

Description

Interface

The name of the interface: WAN or LAN (ATA 192 only).

Connect Type

The type of connection configured for the interface.

IP Address

The IPv6 address of the interface.

Prefix Length

The Prefix length of the interface.

MAC Address

The MAC address of the interface.

### Port List (ATA 192 only)

Field

Description

Interface

The name of the interface: WAN or LAN.

TX (pkts)

The number of packets transmitted from this port.

RX (pkts)

The number of packets received by this port.

Status

The status of the port, showing whether the port is connected to a device or disconnected.

Clear TX & RX

Click this button to reset the count of TX and RX packets to zero.

## Network Status

Use the Status > Network Status page to view information about the WAN interface (INTERNET port).

Field

Description

Link Status

The status of the INTERNET (WAN) interface, showing whether the port is connected or disconnected.

Host Name

The host name of the ATA.

Domain

The domain name of the ATA.

Field

Description

IP Address

The IPv4 address of the INTERNET (WAN) interface.

Subnet Mask

The subnet mask for the INTERNET (WAN) interface.

Gateway

The IPv4 address of the default gateway.

MTU Type

The method for setting the MTU: Auto or Manual

MTU Size

The largest protocol data unit (in bytes) permitted for network transmission

DNS 1-3 (if applicable)

IPv4 addresses for up to three DNS servers that are used for name resolution.

Field

Description

IP Address

The IPv6 address of the INTERNET (WAN) interface.

Prefix Length

The Prefix Length for the INTERNET (WAN) interface.

Gateway

The IPv6 address of the default gateway.

DNS 1-2 (if applicable)

IPv6 addresses for up to three DNS servers that are used for name resolution.

Field

Description

CDP

The CDP status is enable or disable.

CDP VLAN ID

The CDP VLAN ID of the ATA.

IVR VLAN ID

The IVR VLAN ID of the ATA.

Active Vlan ID

The Active VLAN ID of the ATA.

## Port Statistics (ATA 192 Only)

Use the Status > Port Statistics page to view information about the port activity on the WAN interface (INTERNET port) and the LAN interface (ETHERNET port).

Field

Description

Input (pkts)

The number of packets received by the port.

Output (pkts)

The number of packets transmitted by the port.

Input Errors

The number of receive errors for incoming traffic.

Input Broadcasts

The number of broadcast messages received by the interface.

Output Broadcasts

The number of broadcast messages sent by the interface.

Input Multicasts

The number of multicast messages received by the interface.

Output Multicasts

The number of multicast messages sent by the interface.

## Memory Information

Use the Status > Memory Information page to view information about memory use.

Field

Description

MemTotal

The total memory of ATA.

MemFree

The free memory of ATA.

refresh

Refresh the latest memory information.

## DHCP Server Information (ATA 192 Only)

Use the Status > DHCP Server Information page to view information about the DHCP server and clients.

### IPv4 DHCP Pool Information

Field

Description

Client Name

The host name of the DHCP client.

IP Address

The IP address leased to the client.

MAC Address

The MAC address of the DHCP client.

Expires Time

The remaining time in the current DHCP lease, shown in HH:MM:SS (hours:minutes:seconds) format. The page is periodically updated
                                          with the new value as the timer counts down.

Interface

The interface through which the client is connected.

### IPv6 DHCP Pool Information

Field

Description

Client Name

The host name of the DHCP client.

IP Address

The IP address leased to the client.

MAC Address

The MAC address of the DHCPv6 client.

Expires Time

The remaining time in the current DHCP lease, shown in HH:MM:SS (hours:minutes:seconds) format. The page is periodically updated
                                          with the new value as the timer counts down.

Interface

The interface through which the client is connected.

### IPv4 DHCP Server Details

Field

Description

DHCP Server

The status of the DHCP server: Enabled or Disabled.

IP Address / Mask

The IP address and subnet mask for the ETHERNET (LAN) interface.

DNS Proxy

The setting for the DNS proxy service: Enabled or Disabled.

Maximum DHCP Users

The maximum number of clients that can lease an IP address from the DHCP server.

IP Address Range

The range of IP addresses that can be dynamically assigned by the DHCP server.

Client Lease Time

The maximum amount of time, in minutes, that a client can lease a dynamically assigned IP address.

Static DNS

The IP addresses of up to three DNS servers to be used by DHCP clients.

Option 66

The setting for Option 66, which provides provisioning server address information to hosts requesting this option. The ATA
                                          may be set to None (internal), Remote TFTP Server, or Manual TFTP Server.

TFTP Server

The IP address, hostname, or URL of the TFTP server used for provisioning.

Option 67

The configuration/bootstrap filename that is provided to hosts that request this option.

Option 159

The configuration URL that is provided to clients that request this option.

Option 160

The configuration URL that is provided to clients that request this option.

### IPv6 DHCP Server Details

Field

Description

DHCPv6 Server

Display the DHCPv6 Server status.

Address Assign Type

Display the DHCPv6 Server Address assign type.

DHCPv6 Delegation

Display the DHCPv6 Server delegation is yes or no.

IPv6 Address Prefix

Display the DHCPv6 address prefix.

IPv6 Address Prefix Length

Display the DHCPv6 address prefix length.

IPv6 Static DNS

Display the DHCPv6 Static DNS.

IPv6 Active DNS1

Display the DHCPv6 Active DNS1.

IPv6 Active DNS2

Display the DHCPv6 Active DNS2.

IPv6 LAN Address

Display the DHCPv6 LAN address.

| Field | Description |
|---|---|
| Model | The model number and product description. |
| Product ID | The product ID of the ATA. |
| VID | The VID of the ATA |
| Serial Number | The serial number of the ATA. |
| Hardware Revision | The hardware version number. |
| Boot Version | The boot firmware version number. |
| Boot Partition | The boot partition of the ATA. |
| Firmware Version | The current firmware version. |
| Internet MAC Address | The MAC address of the WAN interface. |
| Host Name | The host name of the ATA. |
| Domain Name | The domain name of the ATA. |
| Current Time | Time that is set on the ATA. |
| Time Zone | Time zone that is set on the ATA. |

| Field | Description |
|---|---|
| Interface | The name of the interface: WAN or LAN (ATA 192 only). |
| Connect Type | The type of connection configured for the interface. |
| IP Address | The IPv4 address of the interface. |
| Subnet Mask | The subnet mask of the interface. |
| MAC Address | The MAC address of the interface. |

| Field | Description |
|---|---|
| Interface | The name of the interface: WAN or LAN (ATA 192 only). |
| Connect Type | The type of connection configured for the interface. |
| IP Address | The IPv6 address of the interface. |
| Prefix Length | The Prefix length of the interface. |
| MAC Address | The MAC address of the interface. |

| Field | Description |
|---|---|
| Interface | The name of the interface: WAN or LAN. |
| TX (pkts) | The number of packets transmitted from this port. |
| RX (pkts) | The number of packets received by this port. |
| Status | The status of the port, showing whether the port is connected to a device or disconnected. |
| Clear TX & RX | Click this button to reset the count of TX and RX packets to zero. |

| Field | Description |
|---|---|
| Link Status | The status of the INTERNET (WAN) interface, showing whether the port is connected or disconnected. |
| Host Name | The host name of the ATA. |
| Domain | The domain name of the ATA. |

| Field | Description |
|---|---|
| IP Address | The IPv4 address of the INTERNET (WAN) interface. |
| Subnet Mask | The subnet mask for the INTERNET (WAN) interface. |
| Gateway | The IPv4 address of the default gateway. |
| MTU Type | The method for setting the MTU: Auto or Manual |
| MTU Size | The largest protocol data unit (in bytes) permitted for network transmission |
| DNS 1-3 (if applicable) | IPv4 addresses for up to three DNS servers that are used for name resolution. |

| Field | Description |
|---|---|
| IP Address | The IPv6 address of the INTERNET (WAN) interface. |
| Prefix Length | The Prefix Length for the INTERNET (WAN) interface. |
| Gateway | The IPv6 address of the default gateway. |
| DNS 1-2 (if applicable) | IPv6 addresses for up to three DNS servers that are used for name resolution. |

| Field | Description |
|---|---|
| CDP | The CDP status is enable or disable. |
| CDP VLAN ID | The CDP VLAN ID of the ATA. |
| IVR VLAN ID | The IVR VLAN ID of the ATA. |
| Active Vlan ID | The Active VLAN ID of the ATA. |

| Field | Description |
|---|---|
| Input (pkts) | The number of packets received by the port. |
| Output (pkts) | The number of packets transmitted by the port. |
| Input Errors | The number of receive errors for incoming traffic. |
| Input Broadcasts | The number of broadcast messages received by the interface. |
| Output Broadcasts | The number of broadcast messages sent by the interface. |
| Input Multicasts | The number of multicast messages received by the interface. |
| Output Multicasts | The number of multicast messages sent by the interface. |

| Field | Description |
|---|---|
| MemTotal | The total memory of ATA. |
| MemFree | The free memory of ATA. |
| refresh | Refresh the latest memory information. |

| Field | Description |
|---|---|
| Client Name | The host name of the DHCP client. |
| IP Address | The IP address leased to the client. |
| MAC Address | The MAC address of the DHCP client. |
| Expires Time | The remaining time in the current DHCP lease, shown in HH:MM:SS (hours:minutes:seconds) format. The page is periodically updated
                                          with the new value as the timer counts down. |
| Interface | The interface through which the client is connected. |

| Field | Description |
|---|---|
| Client Name | The host name of the DHCP client. |
| IP Address | The IP address leased to the client. |
| MAC Address | The MAC address of the DHCPv6 client. |
| Expires Time | The remaining time in the current DHCP lease, shown in HH:MM:SS (hours:minutes:seconds) format. The page is periodically updated
                                          with the new value as the timer counts down. |
| Interface | The interface through which the client is connected. |

| Field | Description |
|---|---|
| DHCP Server | The status of the DHCP server: Enabled or Disabled. |
| IP Address / Mask | The IP address and subnet mask for the ETHERNET (LAN) interface. |
| DNS Proxy | The setting for the DNS proxy service: Enabled or Disabled. |
| Maximum DHCP Users | The maximum number of clients that can lease an IP address from the DHCP server. |
| IP Address Range | The range of IP addresses that can be dynamically assigned by the DHCP server. |
| Client Lease Time | The maximum amount of time, in minutes, that a client can lease a dynamically assigned IP address. |
| Static DNS | The IP addresses of up to three DNS servers to be used by DHCP clients. |
| Option 66 | The setting for Option 66, which provides provisioning server address information to hosts requesting this option. The ATA
                                          may be set to None (internal), Remote TFTP Server, or Manual TFTP Server. |
| TFTP Server | The IP address, hostname, or URL of the TFTP server used for provisioning. |
| Option 67 | The configuration/bootstrap filename that is provided to hosts that request this option. |
| Option 159 | The configuration URL that is provided to clients that request this option. |
| Option 160 | The configuration URL that is provided to clients that request this option. |

| Field | Description |
|---|---|
| DHCPv6 Server | Display the DHCPv6 Server status. |
| Address Assign Type | Display the DHCPv6 Server Address assign type. |
| DHCPv6 Delegation | Display the DHCPv6 Server delegation is yes or no. |
| IPv6 Address Prefix | Display the DHCPv6 address prefix. |
| IPv6 Address Prefix Length | Display the DHCPv6 address prefix length. |
| IPv6 Static DNS | Display the DHCPv6 Static DNS. |
| IPv6 Active DNS1 | Display the DHCPv6 Active DNS1. |
| IPv6 Active DNS2 | Display the DHCPv6 Active DNS2. |
| IPv6 LAN Address | Display the DHCPv6 LAN address. |