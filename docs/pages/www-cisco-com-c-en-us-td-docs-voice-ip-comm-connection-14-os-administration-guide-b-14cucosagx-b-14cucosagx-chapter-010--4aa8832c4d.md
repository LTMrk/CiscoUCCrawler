---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-os-administration-guide-b-14cucosagx-b-14cucosagx-chapter-010--4aa8832c4d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/os_administration/guide/b_14cucosagx/b_14cucosagx_chapter_010.html
retrieved_at: 2026-08-17T03:42:37.459910+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 14

# Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 14

Updated: November 28, 2025

Chapter: Status and Configuration

## Chapter: Status and Configuration

# Status and Configuration

This chapter provides information on administering the system and contains the following topics:

## Cluster
                        	 Node

To view information on the nodes in the cluster, follow this
                              		  procedure:

Step 1

From the Cisco Unified Communications Operating System
                                       			 Administration window navigate to Show > Cluster .

The Cluster Nodes window displays.

Step 2

For a description of the fields on the Cluster Nodes window, see Table 3-1 .

Field

Description

Hostname

Displays the complete hostname of the server.

IP Address

Displays the IP address of the server.

Alias

Displays the alias name of the server, when defined.

Type of Node

Indicates whether the server is a publisher node or a subscriber
                                                      						  node.

## Hardware
                        	 Status

To view the hardware status, follow this procedure:

Step 1

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Show > Hardware .

The Hardware status window displays.

Step 2

For descriptions of the fields on the Hardware Status window,
                                       			 see Table 3-2

Field

Description

Platform Type

Displays the model identity of the platform server.

Processor Speed

Displays the processor speed.

CPU Type

Displays the type of processor in the platform server.

Memory

Displays the total amount of memory in MBytes.

Object ID

Displays the object ID.

OS Version

Displays the operating system version.

RAID Details

Displays details about the RAID drive, including controller
                                                      						  information, logical drive information, and physical device information.

## Network
                        	 Configuration

The network status information that displays depends on whether
                              		  Network Fault Tolerance is enabled. When Network Fault Tolerance is enabled,
                              		  Ethernet port 1 automatically takes over network communications if Ethernet
                              		  port 0 fails. If Network Fault Tolerance is enabled, network status information
                              		  displays for the network ports Ethernet 0, Ethernet 1, and Bond 0. If Network
                              		  Fault Tolerance is not enabled, status information displays only for Ethernet
                              		  0.

To view the network status, follow this procedure:

Step 1

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Show > Network.

The Network Settings window displays.

Step 2

See Table 3-3 for
                                       			 descriptions of the fields on the Network Settings window.

Field

Description

Ethernet Details

DHCP

Indicates whether DHCP is enabled for Ethernet port 0.

Status

Indicates whether the port is Up or Down for Ethernet ports 0
                                                      						  and 1.

IP Address

Shows the IP address of Ethernet port 0 [and Ethernet port 1 if
                                                      						  Network Fault Tolerance (NFT) is enabled].

IP Mask

Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT
                                                      						  is enabled).

Link Detected

Indicates whether an active link exists.

Queue Length

Displays the length of the queue.

MTU

Displays the maximum transmission unit.

MAC Address

Displays the hardware address of the port.

Receive Statistics (RX)

Displays information on received bytes, packets, and errors, as
                                                      						  well as dropped and overrun statistics.

Transmit Statistics (TX)

Displays information on transmitted bytes, packets, and errors,
                                                      						  as well as dropped, carrier, and collision statistics.

DNS Details

Primary

Displays the IP address of the primary domain name server.

Secondary

Displays the IP address of the secondary domain name server.

Optionsosadmin-3-2

Displays the configured DNS options.

Domain

Displays the domain of the server.

Gateway

Displays the IP address of the network gateway on Ethernet port
                                                      						  0.

## Installed
                        	 Software

To view the software versions and installed software options,
                              		  follow this procedure:

Step 1

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Show > Software .

The Software Packages window displays.

Step 2

For a description of the fields on the Software Packages window,
                                       			 see Table 3-4 .

Field

Description

Partition Versions

Displays the software version that is running on the active and
                                                      						  inactive partitions.

Active Version Installed Software Options

Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the active version.

Inactive Version Installed Software Options

Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the inactive version.

## System
                        	 Status

To view the system status, follow this procedure:

Step 1

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Show > System .

The System Status window displays.

Step 2

See Table 3-5 for
                                       			 descriptions of the fields on the Platform Status window.

Field

Description

Host Name

Displays the name of the Cisco MCS host where Cisco Unified
                                                      						  Communications Operating System is installed.

Date

Displays the date and time based on the continent and region
                                                      						  that were specified during operating system installation.

Time Zone

Displays the time zone that was chosen during installation.

Locale

Displays the language that was chosen during operating system
                                                      						  installation.

Product Version

Displays the operating system version.

Platform Version

Displays the platform version.

Uptime

Displays system uptime information.

CPU

Displays the percentage of CPU capacity that is idle, the
                                                      						  percentage that is running system processes, and the percentage that is running
                                                      						  user processes.

Memory

Displays information about memory usage, including the amount of
                                                      						  total memory, free memory, and used memory in KBytes.

Disk/active

Displays the amount of total, free, and used disk space on the
                                                      						  active disk.

Disk/inactive

Displays the amount of total, free, and used disk space on the
                                                      						  inactive disk.

Disk/logging

Displays the amount of total, free, and disk space that is used
                                                      						  for disk logging.

## IP
                        	 Preferences

You can use the IP Preferences window to display a list of
                              		  registered ports that the system can use. The IP Preferences window contains
                              		  the following information:

Application

Protocol

Port Number

Type

Translated Port

Status

Description

To access the IP Preferences window, follow this procedure.

Step 1

From the Cisco Unified Communications Operating System
                                       			 Administration window, select Show > IP Preferences .

The IP Preferences window displays. Records from an active
                                          				(prior) query may also display in the window.

Step 2

To find all records in the database, ensure the dialog box is
                                       			 empty; go to Step 3 .

To filter or search records

From the first drop-down list box, select a search parameter.

From the second drop-down list box, select a search pattern.

Specify the appropriate search text, if applicable.

To add additional search criteria, click the + button. When you add criteria, the system searches for a
                                                            						record that matches all criteria that you specify. To remove criteria, click
                                                            						the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria.

Step 3

Click Find .

All matching records display. You can change the number of items
                                          				that display on each page by choosing a different value from the Rows per Page
                                          				drop-down list box.

For a description of the IP Preferences fields, see

Field

Description

Application

Name of the application using (listening on) the port.

Protocol

Protocol used on this port (TCP, UDP, and so on).

Port Number

Numeric port number.

Type

Type of traffic allowed on this port:

Public—All traffic allowed

Translated—All traffic
                                                            								allowed but forwarded to a different port

Private—Traffic only
                                                            								allowed from a defined set of remote servers, for example, other nodes in the
                                                            								cluster

Translated Port

Traffic destined for this port get forwarded to the port listed
                                                      						  in the Port Number column. This field applies to Translated type ports only.

Status

Status of port usage:

Enabled—In use by the
                                                            								application and opened by the firewall

Disabled—Blocked by the
                                                            								firewall and not in use

Description

Brief description of how the port is used.

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window navigate to Show > Cluster . The Cluster Nodes window displays. |
|---|---|
| Step 2 | For a description of the fields on the Cluster Nodes window, see Table 3-1 . Table 1. Cluster Nodes Field Descriptions Field Description Hostname Displays the complete hostname of the server. IP Address Displays the IP address of the server. Alias Displays the alias name of the server, when defined. Type of Node Indicates whether the server is a publisher node or a subscriber
                                                      						  node. | Field | Description | Hostname | Displays the complete hostname of the server. | IP Address | Displays the IP address of the server. | Alias | Displays the alias name of the server, when defined. | Type of Node | Indicates whether the server is a publisher node or a subscriber
                                                      						  node. |
| Field | Description |
| Hostname | Displays the complete hostname of the server. |
| IP Address | Displays the IP address of the server. |
| Alias | Displays the alias name of the server, when defined. |
| Type of Node | Indicates whether the server is a publisher node or a subscriber
                                                      						  node. |

| Field | Description |
|---|---|
| Hostname | Displays the complete hostname of the server. |
| IP Address | Displays the IP address of the server. |
| Alias | Displays the alias name of the server, when defined. |
| Type of Node | Indicates whether the server is a publisher node or a subscriber
                                                      						  node. |

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Show > Hardware . The Hardware status window displays. |
|---|---|
| Step 2 | For descriptions of the fields on the Hardware Status window,
                                       			 see Table 3-2 Table 2. Hardware Status Field
                                                   				  Descriptions Field Description Platform Type Displays the model identity of the platform server. Processor Speed Displays the processor speed. CPU Type Displays the type of processor in the platform server. Memory Displays the total amount of memory in MBytes. Object ID Displays the object ID. OS Version Displays the operating system version. RAID Details Displays details about the RAID drive, including controller
                                                      						  information, logical drive information, and physical device information. | Field | Description | Platform Type | Displays the model identity of the platform server. | Processor Speed | Displays the processor speed. | CPU Type | Displays the type of processor in the platform server. | Memory | Displays the total amount of memory in MBytes. | Object ID | Displays the object ID. | OS Version | Displays the operating system version. | RAID Details | Displays details about the RAID drive, including controller
                                                      						  information, logical drive information, and physical device information. |
| Field | Description |
| Platform Type | Displays the model identity of the platform server. |
| Processor Speed | Displays the processor speed. |
| CPU Type | Displays the type of processor in the platform server. |
| Memory | Displays the total amount of memory in MBytes. |
| Object ID | Displays the object ID. |
| OS Version | Displays the operating system version. |
| RAID Details | Displays details about the RAID drive, including controller
                                                      						  information, logical drive information, and physical device information. |

| Field | Description |
|---|---|
| Platform Type | Displays the model identity of the platform server. |
| Processor Speed | Displays the processor speed. |
| CPU Type | Displays the type of processor in the platform server. |
| Memory | Displays the total amount of memory in MBytes. |
| Object ID | Displays the object ID. |
| OS Version | Displays the operating system version. |
| RAID Details | Displays details about the RAID drive, including controller
                                                      						  information, logical drive information, and physical device information. |

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Show > Network. The Network Settings window displays. |
|---|---|
| Step 2 | See Table 3-3 for
                                       			 descriptions of the fields on the Network Settings window. Table 3. Network
                                                   				  Configuration Field Descriptions Field Description Ethernet Details DHCP Indicates whether DHCP is enabled for Ethernet port 0. Status Indicates whether the port is Up or Down for Ethernet ports 0
                                                      						  and 1. IP Address Shows the IP address of Ethernet port 0 [and Ethernet port 1 if
                                                      						  Network Fault Tolerance (NFT) is enabled]. IP Mask Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT
                                                      						  is enabled). Link Detected Indicates whether an active link exists. Queue Length Displays the length of the queue. MTU Displays the maximum transmission unit. MAC Address Displays the hardware address of the port. Receive Statistics (RX) Displays information on received bytes, packets, and errors, as
                                                      						  well as dropped and overrun statistics. Transmit Statistics (TX) Displays information on transmitted bytes, packets, and errors,
                                                      						  as well as dropped, carrier, and collision statistics. DNS Details Primary Displays the IP address of the primary domain name server. Secondary Displays the IP address of the secondary domain name server. Optionsosadmin-3-2 Displays the configured DNS options. Domain Displays the domain of the server. Gateway Displays the IP address of the network gateway on Ethernet port
                                                      						  0. | Field | Description | Ethernet Details | DHCP | Indicates whether DHCP is enabled for Ethernet port 0. | Status | Indicates whether the port is Up or Down for Ethernet ports 0
                                                      						  and 1. | IP Address | Shows the IP address of Ethernet port 0 [and Ethernet port 1 if
                                                      						  Network Fault Tolerance (NFT) is enabled]. | IP Mask | Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT
                                                      						  is enabled). | Link Detected | Indicates whether an active link exists. | Queue Length | Displays the length of the queue. | MTU | Displays the maximum transmission unit. | MAC Address | Displays the hardware address of the port. | Receive Statistics (RX) | Displays information on received bytes, packets, and errors, as
                                                      						  well as dropped and overrun statistics. | Transmit Statistics (TX) | Displays information on transmitted bytes, packets, and errors,
                                                      						  as well as dropped, carrier, and collision statistics. | DNS Details | Primary | Displays the IP address of the primary domain name server. | Secondary | Displays the IP address of the secondary domain name server. | Optionsosadmin-3-2 | Displays the configured DNS options. | Domain | Displays the domain of the server. | Gateway | Displays the IP address of the network gateway on Ethernet port
                                                      						  0. |
| Field | Description |
| Ethernet Details |
| DHCP | Indicates whether DHCP is enabled for Ethernet port 0. |
| Status | Indicates whether the port is Up or Down for Ethernet ports 0
                                                      						  and 1. |
| IP Address | Shows the IP address of Ethernet port 0 [and Ethernet port 1 if
                                                      						  Network Fault Tolerance (NFT) is enabled]. |
| IP Mask | Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT
                                                      						  is enabled). |
| Link Detected | Indicates whether an active link exists. |
| Queue Length | Displays the length of the queue. |
| MTU | Displays the maximum transmission unit. |
| MAC Address | Displays the hardware address of the port. |
| Receive Statistics (RX) | Displays information on received bytes, packets, and errors, as
                                                      						  well as dropped and overrun statistics. |
| Transmit Statistics (TX) | Displays information on transmitted bytes, packets, and errors,
                                                      						  as well as dropped, carrier, and collision statistics. |
| DNS Details |
| Primary | Displays the IP address of the primary domain name server. |
| Secondary | Displays the IP address of the secondary domain name server. |
| Optionsosadmin-3-2 | Displays the configured DNS options. |
| Domain | Displays the domain of the server. |
| Gateway | Displays the IP address of the network gateway on Ethernet port
                                                      						  0. |

| Field | Description |
|---|---|
| Ethernet Details |
| DHCP | Indicates whether DHCP is enabled for Ethernet port 0. |
| Status | Indicates whether the port is Up or Down for Ethernet ports 0
                                                      						  and 1. |
| IP Address | Shows the IP address of Ethernet port 0 [and Ethernet port 1 if
                                                      						  Network Fault Tolerance (NFT) is enabled]. |
| IP Mask | Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT
                                                      						  is enabled). |
| Link Detected | Indicates whether an active link exists. |
| Queue Length | Displays the length of the queue. |
| MTU | Displays the maximum transmission unit. |
| MAC Address | Displays the hardware address of the port. |
| Receive Statistics (RX) | Displays information on received bytes, packets, and errors, as
                                                      						  well as dropped and overrun statistics. |
| Transmit Statistics (TX) | Displays information on transmitted bytes, packets, and errors,
                                                      						  as well as dropped, carrier, and collision statistics. |
| DNS Details |
| Primary | Displays the IP address of the primary domain name server. |
| Secondary | Displays the IP address of the secondary domain name server. |
| Optionsosadmin-3-2 | Displays the configured DNS options. |
| Domain | Displays the domain of the server. |
| Gateway | Displays the IP address of the network gateway on Ethernet port
                                                      						  0. |

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Show > Software . The Software Packages window displays. |
|---|---|
| Step 2 | For a description of the fields on the Software Packages window,
                                       			 see Table 3-4 . Table 4. Software Packages Field
                                                   				  Descriptions Field Description Partition Versions Displays the software version that is running on the active and
                                                      						  inactive partitions. Active Version Installed Software Options Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the active version. Inactive Version Installed Software Options Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the inactive version. | Field | Description | Partition Versions | Displays the software version that is running on the active and
                                                      						  inactive partitions. | Active Version Installed Software Options | Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the active version. | Inactive Version Installed Software Options | Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the inactive version. |
| Field | Description |
| Partition Versions | Displays the software version that is running on the active and
                                                      						  inactive partitions. |
| Active Version Installed Software Options | Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the active version. |
| Inactive Version Installed Software Options | Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the inactive version. |

| Field | Description |
|---|---|
| Partition Versions | Displays the software version that is running on the active and
                                                      						  inactive partitions. |
| Active Version Installed Software Options | Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the active version. |
| Inactive Version Installed Software Options | Displays the versions of installed software options, including
                                                      						  locales and dial plans, that are installed on the inactive version. |

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Show > System . The System Status window displays. |
|---|---|
| Step 2 | See Table 3-5 for
                                       			 descriptions of the fields on the Platform Status window. Table 5. System Status
                                                   				  Field Descriptions Field Description Host Name Displays the name of the Cisco MCS host where Cisco Unified
                                                      						  Communications Operating System is installed. Date Displays the date and time based on the continent and region
                                                      						  that were specified during operating system installation. Time Zone Displays the time zone that was chosen during installation. Locale Displays the language that was chosen during operating system
                                                      						  installation. Product Version Displays the operating system version. Platform Version Displays the platform version. Uptime Displays system uptime information. CPU Displays the percentage of CPU capacity that is idle, the
                                                      						  percentage that is running system processes, and the percentage that is running
                                                      						  user processes. Memory Displays information about memory usage, including the amount of
                                                      						  total memory, free memory, and used memory in KBytes. Disk/active Displays the amount of total, free, and used disk space on the
                                                      						  active disk. Disk/inactive Displays the amount of total, free, and used disk space on the
                                                      						  inactive disk. Disk/logging Displays the amount of total, free, and disk space that is used
                                                      						  for disk logging. | Field | Description | Host Name | Displays the name of the Cisco MCS host where Cisco Unified
                                                      						  Communications Operating System is installed. | Date | Displays the date and time based on the continent and region
                                                      						  that were specified during operating system installation. | Time Zone | Displays the time zone that was chosen during installation. | Locale | Displays the language that was chosen during operating system
                                                      						  installation. | Product Version | Displays the operating system version. | Platform Version | Displays the platform version. | Uptime | Displays system uptime information. | CPU | Displays the percentage of CPU capacity that is idle, the
                                                      						  percentage that is running system processes, and the percentage that is running
                                                      						  user processes. | Memory | Displays information about memory usage, including the amount of
                                                      						  total memory, free memory, and used memory in KBytes. | Disk/active | Displays the amount of total, free, and used disk space on the
                                                      						  active disk. | Disk/inactive | Displays the amount of total, free, and used disk space on the
                                                      						  inactive disk. | Disk/logging | Displays the amount of total, free, and disk space that is used
                                                      						  for disk logging. |
| Field | Description |
| Host Name | Displays the name of the Cisco MCS host where Cisco Unified
                                                      						  Communications Operating System is installed. |
| Date | Displays the date and time based on the continent and region
                                                      						  that were specified during operating system installation. |
| Time Zone | Displays the time zone that was chosen during installation. |
| Locale | Displays the language that was chosen during operating system
                                                      						  installation. |
| Product Version | Displays the operating system version. |
| Platform Version | Displays the platform version. |
| Uptime | Displays system uptime information. |
| CPU | Displays the percentage of CPU capacity that is idle, the
                                                      						  percentage that is running system processes, and the percentage that is running
                                                      						  user processes. |
| Memory | Displays information about memory usage, including the amount of
                                                      						  total memory, free memory, and used memory in KBytes. |
| Disk/active | Displays the amount of total, free, and used disk space on the
                                                      						  active disk. |
| Disk/inactive | Displays the amount of total, free, and used disk space on the
                                                      						  inactive disk. |
| Disk/logging | Displays the amount of total, free, and disk space that is used
                                                      						  for disk logging. |

| Field | Description |
|---|---|
| Host Name | Displays the name of the Cisco MCS host where Cisco Unified
                                                      						  Communications Operating System is installed. |
| Date | Displays the date and time based on the continent and region
                                                      						  that were specified during operating system installation. |
| Time Zone | Displays the time zone that was chosen during installation. |
| Locale | Displays the language that was chosen during operating system
                                                      						  installation. |
| Product Version | Displays the operating system version. |
| Platform Version | Displays the platform version. |
| Uptime | Displays system uptime information. |
| CPU | Displays the percentage of CPU capacity that is idle, the
                                                      						  percentage that is running system processes, and the percentage that is running
                                                      						  user processes. |
| Memory | Displays information about memory usage, including the amount of
                                                      						  total memory, free memory, and used memory in KBytes. |
| Disk/active | Displays the amount of total, free, and used disk space on the
                                                      						  active disk. |
| Disk/inactive | Displays the amount of total, free, and used disk space on the
                                                      						  inactive disk. |
| Disk/logging | Displays the amount of total, free, and disk space that is used
                                                      						  for disk logging. |

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, select Show > IP Preferences . The IP Preferences window displays. Records from an active
                                          				(prior) query may also display in the window. |
|---|---|
| Step 2 | To find all records in the database, ensure the dialog box is
                                       			 empty; go to Step 3 . To filter or search records From the first drop-down list box, select a search parameter. From the second drop-down list box, select a search pattern. Specify the appropriate search text, if applicable. Note To add additional search criteria, click the + button. When you add criteria, the system searches for a
                                                            						record that matches all criteria that you specify. To remove criteria, click
                                                            						the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria. | Note | To add additional search criteria, click the + button. When you add criteria, the system searches for a
                                                            						record that matches all criteria that you specify. To remove criteria, click
                                                            						the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria. |
| Note | To add additional search criteria, click the + button. When you add criteria, the system searches for a
                                                            						record that matches all criteria that you specify. To remove criteria, click
                                                            						the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria. |
| Step 3 | Click Find . All matching records display. You can change the number of items
                                          				that display on each page by choosing a different value from the Rows per Page
                                          				drop-down list box. For a description of the IP Preferences fields, see Table 6. IP Preferences Field Descriptions Field Description Application Name of the application using (listening on) the port. Protocol Protocol used on this port (TCP, UDP, and so on). Port Number Numeric port number. Type Type of traffic allowed on this port: Public—All traffic allowed Translated—All traffic
                                                            								allowed but forwarded to a different port Private—Traffic only
                                                            								allowed from a defined set of remote servers, for example, other nodes in the
                                                            								cluster Translated Port Traffic destined for this port get forwarded to the port listed
                                                      						  in the Port Number column. This field applies to Translated type ports only. Status Status of port usage: Enabled—In use by the
                                                            								application and opened by the firewall Disabled—Blocked by the
                                                            								firewall and not in use Description Brief description of how the port is used. | Field | Description | Application | Name of the application using (listening on) the port. | Protocol | Protocol used on this port (TCP, UDP, and so on). | Port Number | Numeric port number. | Type | Type of traffic allowed on this port: Public—All traffic allowed Translated—All traffic
                                                            								allowed but forwarded to a different port Private—Traffic only
                                                            								allowed from a defined set of remote servers, for example, other nodes in the
                                                            								cluster | Translated Port | Traffic destined for this port get forwarded to the port listed
                                                      						  in the Port Number column. This field applies to Translated type ports only. | Status | Status of port usage: Enabled—In use by the
                                                            								application and opened by the firewall Disabled—Blocked by the
                                                            								firewall and not in use | Description | Brief description of how the port is used. |
| Field | Description |
| Application | Name of the application using (listening on) the port. |
| Protocol | Protocol used on this port (TCP, UDP, and so on). |
| Port Number | Numeric port number. |
| Type | Type of traffic allowed on this port: Public—All traffic allowed Translated—All traffic
                                                            								allowed but forwarded to a different port Private—Traffic only
                                                            								allowed from a defined set of remote servers, for example, other nodes in the
                                                            								cluster |
| Translated Port | Traffic destined for this port get forwarded to the port listed
                                                      						  in the Port Number column. This field applies to Translated type ports only. |
| Status | Status of port usage: Enabled—In use by the
                                                            								application and opened by the firewall Disabled—Blocked by the
                                                            								firewall and not in use |
| Description | Brief description of how the port is used. |

| Note | To add additional search criteria, click the + button. When you add criteria, the system searches for a
                                                            						record that matches all criteria that you specify. To remove criteria, click
                                                            						the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria. |
|---|---|

| Field | Description |
|---|---|
| Application | Name of the application using (listening on) the port. |
| Protocol | Protocol used on this port (TCP, UDP, and so on). |
| Port Number | Numeric port number. |
| Type | Type of traffic allowed on this port: Public—All traffic allowed Translated—All traffic
                                                            								allowed but forwarded to a different port Private—Traffic only
                                                            								allowed from a defined set of remote servers, for example, other nodes in the
                                                            								cluster |
| Translated Port | Traffic destined for this port get forwarded to the port listed
                                                      						  in the Port Number column. This field applies to Translated type ports only. |
| Status | Status of port usage: Enabled—In use by the
                                                            								application and opened by the firewall Disabled—Blocked by the
                                                            								firewall and not in use |
| Description | Brief description of how the port is used. |