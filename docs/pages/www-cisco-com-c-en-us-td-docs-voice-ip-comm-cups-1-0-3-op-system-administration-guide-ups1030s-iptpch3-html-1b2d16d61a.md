---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-3-op-system-administration-guide-ups1030s-iptpch3-html-1b2d16d61a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_3/op_system/administration/guide/ups1030s/iptpch3.html
retrieved_at: 2026-08-21T02:48:15.419484+00:00
---

Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

# Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

Updated: February 21, 2007

Chapter: Platform Status and Configuration

## Chapter: Platform Status and Configuration

## Platform Status and Configuration

This chapter provides information on administering the system and contains the following topics:

• Cluster Nodes

• Hardware Status

• Logs

• Network Status

• Installed Software

• System Status

You can view the status of the operating system, platform hardware, or the network.

## Cluster Nodes

To view information on the nodes in the cluster, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Show>Cluster .

The Cluster Nodes window displays.

Step 2 For a description of the fields on the Cluster Nodes window, see Table 3-1 .

Table 3-1 Cluster Nodes Field Descriptions

Hostname

Displays the complete hostname of the server.

IP Address

Displays the IP address of the server.

Alias

Displays the alias name of the server, when defined.

Type of Node

Indicates whether the server is a publisher node or a subscriber node.

## Hardware Status

To view the hardware status, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Show>Hardware .

The Platform Hardware status window displays.

Step 2 For descriptions of the fields on the Platform Hardware status window, see Table 3-2 .

Table 3-2 Platform Hardware Status Field Descriptions

Hardware Platform

Displays the model identity of the platform server.

Number of Processors

Displays the number of processors in the platform server.

CPU Type

Displays the type of processor in the platform server.

Memory

Displays the total amount of memory in MBytes.

Detailed Report

Displays a detailed summary of the platform hardware.

## Logs

To view system logs, you must install the Cisco Unified Presence Server Real-Time Monitoring Tool (RTMT). For more information on installing and using the RTMT, see the Cisco Unified Presence Server Serviceability Administration Guide .

## Network Status

The network status information that displays depends on whether Network Fault Tolerance is enabled. When Network Fault Tolerance is enabled, Ethernet port 1 automatically takes over network communications if Ethernet port 0 fails. If Network Fault Tolerance is enabled, network status information displays for the network ports Ethernet 0, Ethernet 1, and Bond 0. If Network Fault Tolerance is not enabled, status information displays only for Ethernet 0.

To view the network status, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Show>Network.

The Network Settings window displays.

Step 2 See Table 3-3 for descriptions of the fields on the Network Settings window.

Table 3-3 Network Settings Field Descriptions

Status

Indicates whether the port is Up or Down for Ethernet ports 0 and 1.

DHCP

Indicates whether DHCP is enabled for Ethernet port 0.

MAC Address

Displays the hardware address of the port.

Speed

Displays the speed of the connection.

Duplex

Displays the duplex mode.

IP Address

Shows the IP address of Ethernet port 0 (and Ethernet port 1 if Network Fault Tolerance (NFT) is enabled).

IP Mask

Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT is enabled).

Link Detected

Indicates whether there is an active link.

Auto Negotiation

Indicates whether auto negotiation is active.

MTU

Displays the maximum transmission unit.

Queue Length

Displays the length of the queue.

Receive Statistics

Displays information on received bytes and packets.

Transmit Statistics

Displays information on transmitted bytes and packets.

Primary DNS

Displays the IP address of the primary domain name server.

Secondary DNS

Displays the IP address of the secondary domain name server.

Domain

Displays the domain of the server.

Gateway

Displays the IP address of the network gateway on Ethernet port 0.

## Installed Software

To view the software versions and installed software options, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Show>Software .

The Software Packages window displays.

Step 2 For a description of the fields on the Software Packages window, see Table 3-4 .

Table 3-4 Software Packages Field Descriptions

Partition Versions

Displays the software version that is running on the active and inactive partitions.

Active Version Installed Software Options

Displays the versions of installed software options, including locales and dial plans, that are installed on the active version.

Inactive Version Installed Software Options

Displays the versions of installed software options, including locales and dial plans, that are installed on the inactive version.

## System Status

To view the system status, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Show>System .

The System Status window displays.

Step 2 See Table 3-5 for descriptions of the fields on the Platform Status window.

Table 3-5 Platform Status Field Descriptions

Host Name

Displays the name of the Cisco MCS host where Cisco Unified Communications Operating System is installed.

Date/Time

Displays the date and time based on the continent and region that were specified during operating system installation.

Time Zone

Displays the time zone that was chosen during installation.

Locale

Displays the language that was chosen during operating system installation.

Product Ver

Displays the operating system version.

Platform Ver

Displays the platform version.

Uptime

Displays system uptime information.

CPU

Displays the percentage of CPU capacity that is idle, the percentage that is running system processes, and the percentage that is running user processes.

Memory

Displays information about memory usage, including the amount of total memory, free memory, and used memory in KBytes.

Disk/active

Displays the amount of total, free, and used disk space on the active disk.

Disk/inactive

Displays the amount of total, free, and used disk space on the inactive disk.

Disk/logging

Displays the amount of total, free, and disk space that is used for disk logging.

| Field | Description |
|---|---|
| Hostname | Displays the complete hostname of the server. |
| IP Address | Displays the IP address of the server. |
| Alias | Displays the alias name of the server, when defined. |
| Type of Node | Indicates whether the server is a publisher node or a subscriber node. |

| Field | Description |
|---|---|
| Hardware Platform | Displays the model identity of the platform server. |
| Number of Processors | Displays the number of processors in the platform server. |
| CPU Type | Displays the type of processor in the platform server. |
| Memory | Displays the total amount of memory in MBytes. |
| Detailed Report | Displays a detailed summary of the platform hardware. |

| Field | Description |
|---|---|
| Status | Indicates whether the port is Up or Down for Ethernet ports 0 and 1. |
| DHCP | Indicates whether DHCP is enabled for Ethernet port 0. |
| MAC Address | Displays the hardware address of the port. |
| Speed | Displays the speed of the connection. |
| Duplex | Displays the duplex mode. |
| IP Address | Shows the IP address of Ethernet port 0 (and Ethernet port 1 if Network Fault Tolerance (NFT) is enabled). |
| IP Mask | Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT is enabled). |
| Link Detected | Indicates whether there is an active link. |
| Auto Negotiation | Indicates whether auto negotiation is active. |
| MTU | Displays the maximum transmission unit. |
| Queue Length | Displays the length of the queue. |
| Receive Statistics | Displays information on received bytes and packets. |
| Transmit Statistics | Displays information on transmitted bytes and packets. |
| Primary DNS | Displays the IP address of the primary domain name server. |
| Secondary DNS | Displays the IP address of the secondary domain name server. |
| Domain | Displays the domain of the server. |
| Gateway | Displays the IP address of the network gateway on Ethernet port 0. |

| Field | Description |
|---|---|
| Partition Versions | Displays the software version that is running on the active and inactive partitions. |
| Active Version Installed Software Options | Displays the versions of installed software options, including locales and dial plans, that are installed on the active version. |
| Inactive Version Installed Software Options | Displays the versions of installed software options, including locales and dial plans, that are installed on the inactive version. |

| Field | Description |
|---|---|
| Host Name | Displays the name of the Cisco MCS host where Cisco Unified Communications Operating System is installed. |
| Date/Time | Displays the date and time based on the continent and region that were specified during operating system installation. |
| Time Zone | Displays the time zone that was chosen during installation. |
| Locale | Displays the language that was chosen during operating system installation. |
| Product Ver | Displays the operating system version. |
| Platform Ver | Displays the platform version. |
| Uptime | Displays system uptime information. |
| CPU | Displays the percentage of CPU capacity that is idle, the percentage that is running system processes, and the percentage that is running user processes. |
| Memory | Displays information about memory usage, including the amount of total memory, free memory, and used memory in KBytes. |
| Disk/active | Displays the amount of total, free, and used disk space on the active disk. |
| Disk/inactive | Displays the amount of total, free, and used disk space on the inactive disk. |
| Disk/logging | Displays the amount of total, free, and disk space that is used for disk logging. |