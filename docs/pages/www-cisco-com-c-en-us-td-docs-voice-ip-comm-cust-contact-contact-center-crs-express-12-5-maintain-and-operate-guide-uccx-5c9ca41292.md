---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-maintain-and-operate-guide-uccx-5c9ca41292
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_unified-ccx-operating-system-125/uccx_b_unified-ccx-operating-system-125_chapter_011.html
retrieved_at: 2026-08-16T21:41:43.263678+00:00
---

Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1)

# Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1)

Updated: February 6, 2020

Chapter: Status and Configuration

## Chapter: Status and Configuration

# Status and Configuration

## View Cluster Node
                        	 Information

To view
                              		  information on the nodes in the cluster, follow this procedure:

From the Cisco Unified Operating System Administration window navigate to Show > Cluster .

## View Hardware
                        	 Status

To view the hardware
                              		  status, follow this procedure:

From the Cisco Unified Operating System Administration window, navigate to Show > Hardware .

Displays the model identity of the platform server.

Displays the serial number of the platform server.

Displays the status of the virtual hardware configured.

Displays the status of the virtual support available.

Displays the processor speed.

Displays the type of processor in the platform server.

Displays the total amount of memory in MB.

Displays the object ID.

Displays the operating system version.

Displays details about the RAID drive, including controller information, logical drive information, and physical device information.

## Display Network
                        	 Status

The network
                              		  status information that appears depends on if Network Fault Tolerance is
                              		  enabled. When Network Fault Tolerance is enabled, Ethernet port 1 automatically
                              		  takes over network communications if Ethernet port 0 fails. If Network Fault
                              		  Tolerance is enabled, network status information appears for the network ports
                              		  Ethernet 0, Ethernet 1, and Bond 0. If Network Fault Tolerance is not enabled,
                              		  status information appears only for Ethernet 0.

To view the network
                              		  status, follow this procedure:

From the Cisco Unified System Administration window, navigate to Show > Network .

Disabled for Unified CCX .

Indicates whether the port is Up or Down for Ethernet ports 0 and 1.

Shows the IP address of Ethernet port 0 [and Ethernet port 1 if Network Fault Tolerance (NFT) is enabled].

Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT is enabled).

Indicates whether an active link exists.

Displays the length of the queue.

Displays the maximum transmission unit.

Displays the hardware address of the port.

Displays information on received bytes, packets, and errors, as well as dropped, overrun and multicast statistics.

Displays information on transmitted bytes, packets, and errors, as well as dropped, carrier, and collision statistics.

Displays the IP address of the primary domain name server.

Displays the IP address of the secondary domain name server.

Displays the configured DNS options.

Displays the domain of the server.

Displays the IP address of the network gateway on Ethernet port 0.

## Verify Installed Software

To view the software versions and installed software
                              		  options, follow this procedure:

From the Cisco Unified Operating System Administration window, navigate to Show > Software .

Displays the software version that is running on the active and inactive partitions.

Displays the versions of installed software options, including Cisco Options Package (COP) patch files that are installed
                                                         on the active version.

Displays the versions of installed software options, including COP patch files that are installed on the inactive version.

## View System
                        	 Status

To view
                              		  the system status, follow this procedure:

From the Cisco Unified Operating System Administration window, navigate to Show > System .

Displays the name of the Cisco MCS host where Cisco Unified Operating System is installed.

Displays the date and time based on the continent and region that were specified during operating system installation.

Displays the time zone that was chosen during installation.

Displays the language that was chosen during operating system installation.

Displays the operating system version.

Displays the platform version.

Displays the license MAC.

Displays system uptime information.

Displays the percentage of CPU capacity that is idle, the percentage that is running system processes, and the percentage
                                                         that is running user processes.

Displays information about memory usage, including the amount of total memory, free memory, used memory, cached memory, shared
                                                         memory, and buffers in KBytes.

Displays the amount of total, free, and used disk space on the active disk.

Displays the amount of total, free, and used disk space on the inactive disk.

Displays the amount of total, free, and disk space that is used for disk logging.

## Display Registered Ports

You can use the IP Preferences window to display a list of
                              		  registered ports that the system can use. The IP Preferences window contains the following
                              		  information:

Application

- Protocol

- Port Number

- Type

- Translated Port

- Status

- Description

To access the IP Preferences window,
                              		  follow this procedure.

From the Cisco Unified System Administration window, choose Show > IP Preferences .

To find all
                                       				records in the database, ensure the dialog box is empty and go to Step 4.

To filter or search records, do the following:

From the first
                                             					 drop-down list box, select a search parameter.

From the second
                                             					 drop-down list box, select a search pattern.

Specify the
                                             					 appropriate search text, if applicable.

To add additional search criteria, click the + button. When you add criteria, the
                                                      						  system searches for a record that matches all criteria that you specify. To
                                                      						  remove criteria, click the – button to remove the last added
                                                      						  criterion or click the Clear Filter button to remove all
                                                      						  added search criteria.

Click Find .

All matching records appear. You can change the number of items
                                          				that appear on each page by choosing a different value from the Rows per Page
                                          				drop-down list box.

Name of the application using (listening on) the port.

Protocol used on this port (TCP, UDP).

Numeric port number.

Public—All traffic allowed

Translated—All traffic allowed but forwarded to a
                                                                  								different port

Private—Traffic only allowed from a defined set of
                                                                  								remote servers, for example, other nodes in the cluster

Traffic destined for this port is forwarded to the port
                                                         						  listed in the Port Number column. This field applies to Translated type ports
                                                         						  only.

Enabled—In use by the application and opened by the
                                                                  								firewall

Disabled—Blocked by the firewall and not in use

Brief description of how the port is used.

| From the Cisco Unified Operating System Administration window navigate to Show > Cluster . The following table contains descriptions of the fields on the Cluster window. Table 1. Cluster Nodes Field Descriptions Field Description Hostname Displays the complete host name of the server. IP Address Displays the IP address of the server. Alias Displays the alias name of the server, when defined. Server Type Displays the type of server. Database Replication Indicates whether the server is a publisher node or a subscriber node. | Field | Description | Hostname | Displays the complete host name of the server. | IP Address | Displays the IP address of the server. | Alias | Displays the alias name of the server, when defined. | Server Type | Displays the type of server. | Database Replication | Indicates whether the server is a publisher node or a subscriber node. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Hostname | Displays the complete host name of the server. |
| IP Address | Displays the IP address of the server. |
| Alias | Displays the alias name of the server, when defined. |
| Server Type | Displays the type of server. |
| Database Replication | Indicates whether the server is a publisher node or a subscriber node. |

| Field | Description |
|---|---|
| Hostname | Displays the complete host name of the server. |
| IP Address | Displays the IP address of the server. |
| Alias | Displays the alias name of the server, when defined. |
| Server Type | Displays the type of server. |
| Database Replication | Indicates whether the server is a publisher node or a subscriber node. |

| From the Cisco Unified Operating System Administration window, navigate to Show > Hardware . The following table contains descriptions of the fields on the Hardware status window. Table 2. Hardware Status Field Descriptions Field Description Platform Type Displays the model identity of the platform server. Serial Number Displays the serial number of the platform server. Virtual Hardware Displays the status of the virtual hardware configured. Virtual Support Displays the status of the virtual support available. Processor Speed Displays the processor speed. CPU Type Displays the type of processor in the platform server. Memory Displays the total amount of memory in MB. Object ID Displays the object ID. OS Version Displays the operating system version. RAID Details Displays details about the RAID drive, including controller information, logical drive information, and physical device information. | Field | Description | Platform Type | Displays the model identity of the platform server. | Serial Number | Displays the serial number of the platform server. | Virtual Hardware | Displays the status of the virtual hardware configured. | Virtual Support | Displays the status of the virtual support available. | Processor Speed | Displays the processor speed. | CPU Type | Displays the type of processor in the platform server. | Memory | Displays the total amount of memory in MB. | Object ID | Displays the object ID. | OS Version | Displays the operating system version. | RAID Details | Displays details about the RAID drive, including controller information, logical drive information, and physical device information. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Platform Type | Displays the model identity of the platform server. |
| Serial Number | Displays the serial number of the platform server. |
| Virtual Hardware | Displays the status of the virtual hardware configured. |
| Virtual Support | Displays the status of the virtual support available. |
| Processor Speed | Displays the processor speed. |
| CPU Type | Displays the type of processor in the platform server. |
| Memory | Displays the total amount of memory in MB. |
| Object ID | Displays the object ID. |
| OS Version | Displays the operating system version. |
| RAID Details | Displays details about the RAID drive, including controller information, logical drive information, and physical device information. |

| Field | Description |
|---|---|
| Platform Type | Displays the model identity of the platform server. |
| Serial Number | Displays the serial number of the platform server. |
| Virtual Hardware | Displays the status of the virtual hardware configured. |
| Virtual Support | Displays the status of the virtual support available. |
| Processor Speed | Displays the processor speed. |
| CPU Type | Displays the type of processor in the platform server. |
| Memory | Displays the total amount of memory in MB. |
| Object ID | Displays the object ID. |
| OS Version | Displays the operating system version. |
| RAID Details | Displays details about the RAID drive, including controller information, logical drive information, and physical device information. |

| From the Cisco Unified System Administration window, navigate to Show > Network . The following table contains descriptions of the fields on the Network Settings window. Table 3. Network Settings Field Descriptions Field Description Ethernet Details DHCP Disabled for Unified CCX . Status Indicates whether the port is Up or Down for Ethernet ports 0 and 1. IP Address Shows the IP address of Ethernet port 0 [and Ethernet port 1 if Network Fault Tolerance (NFT) is enabled]. IP Mask Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT is enabled). Link Detected Indicates whether an active link exists. Queue Length Displays the length of the queue. MTU Displays the maximum transmission unit. MAC Address Displays the hardware address of the port. Receive Statistics (RX) Displays information on received bytes, packets, and errors, as well as dropped, overrun and multicast statistics. Transmit Statistics (TX) Displays information on transmitted bytes, packets, and errors, as well as dropped, carrier, and collision statistics. DNS Details Primary Displays the IP address of the primary domain name server. Secondary Displays the IP address of the secondary domain name server. Options Displays the configured DNS options. Domain Displays the domain of the server. Gateway Displays the IP address of the network gateway on Ethernet port 0. | Field | Description | Ethernet Details | DHCP | Disabled for Unified CCX . | Status | Indicates whether the port is Up or Down for Ethernet ports 0 and 1. | IP Address | Shows the IP address of Ethernet port 0 [and Ethernet port 1 if Network Fault Tolerance (NFT) is enabled]. | IP Mask | Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT is enabled). | Link Detected | Indicates whether an active link exists. | Queue Length | Displays the length of the queue. | MTU | Displays the maximum transmission unit. | MAC Address | Displays the hardware address of the port. | Receive Statistics (RX) | Displays information on received bytes, packets, and errors, as well as dropped, overrun and multicast statistics. | Transmit Statistics (TX) | Displays information on transmitted bytes, packets, and errors, as well as dropped, carrier, and collision statistics. | DNS Details | Primary | Displays the IP address of the primary domain name server. | Secondary | Displays the IP address of the secondary domain name server. | Options | Displays the configured DNS options. | Domain | Displays the domain of the server. | Gateway | Displays the IP address of the network gateway on Ethernet port 0. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Ethernet Details |
| DHCP | Disabled for Unified CCX . |
| Status | Indicates whether the port is Up or Down for Ethernet ports 0 and 1. |
| IP Address | Shows the IP address of Ethernet port 0 [and Ethernet port 1 if Network Fault Tolerance (NFT) is enabled]. |
| IP Mask | Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT is enabled). |
| Link Detected | Indicates whether an active link exists. |
| Queue Length | Displays the length of the queue. |
| MTU | Displays the maximum transmission unit. |
| MAC Address | Displays the hardware address of the port. |
| Receive Statistics (RX) | Displays information on received bytes, packets, and errors, as well as dropped, overrun and multicast statistics. |
| Transmit Statistics (TX) | Displays information on transmitted bytes, packets, and errors, as well as dropped, carrier, and collision statistics. |
| DNS Details |
| Primary | Displays the IP address of the primary domain name server. |
| Secondary | Displays the IP address of the secondary domain name server. |
| Options | Displays the configured DNS options. |
| Domain | Displays the domain of the server. |
| Gateway | Displays the IP address of the network gateway on Ethernet port 0. |

| Field | Description |
|---|---|
| Ethernet Details |
| DHCP | Disabled for Unified CCX . |
| Status | Indicates whether the port is Up or Down for Ethernet ports 0 and 1. |
| IP Address | Shows the IP address of Ethernet port 0 [and Ethernet port 1 if Network Fault Tolerance (NFT) is enabled]. |
| IP Mask | Shows the IP mask of Ethernet port 0 (and Ethernet port 1 if NFT is enabled). |
| Link Detected | Indicates whether an active link exists. |
| Queue Length | Displays the length of the queue. |
| MTU | Displays the maximum transmission unit. |
| MAC Address | Displays the hardware address of the port. |
| Receive Statistics (RX) | Displays information on received bytes, packets, and errors, as well as dropped, overrun and multicast statistics. |
| Transmit Statistics (TX) | Displays information on transmitted bytes, packets, and errors, as well as dropped, carrier, and collision statistics. |
| DNS Details |
| Primary | Displays the IP address of the primary domain name server. |
| Secondary | Displays the IP address of the secondary domain name server. |
| Options | Displays the configured DNS options. |
| Domain | Displays the domain of the server. |
| Gateway | Displays the IP address of the network gateway on Ethernet port 0. |

| From the Cisco Unified Operating System Administration window, navigate to Show > Software . The following table contains descriptions of the fields in the Software Packages window. Table 4. Software Packages Field Descriptions Field Description Partition Versions Displays the software version that is running on the active and inactive partitions. Installed Software Options Active Version Installed Software Options Displays the versions of installed software options, including Cisco Options Package (COP) patch files that are installed
                                                         on the active version. Inactive Version Installed Software Options Displays the versions of installed software options, including COP patch files that are installed on the inactive version. | Field | Description | Partition Versions | Displays the software version that is running on the active and inactive partitions. | Installed Software Options | Active Version Installed Software Options | Displays the versions of installed software options, including Cisco Options Package (COP) patch files that are installed
                                                         on the active version. | Inactive Version Installed Software Options | Displays the versions of installed software options, including COP patch files that are installed on the inactive version. |
|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Partition Versions | Displays the software version that is running on the active and inactive partitions. |
| Installed Software Options |
| Active Version Installed Software Options | Displays the versions of installed software options, including Cisco Options Package (COP) patch files that are installed
                                                         on the active version. |
| Inactive Version Installed Software Options | Displays the versions of installed software options, including COP patch files that are installed on the inactive version. |

| Field | Description |
|---|---|
| Partition Versions | Displays the software version that is running on the active and inactive partitions. |
| Installed Software Options |
| Active Version Installed Software Options | Displays the versions of installed software options, including Cisco Options Package (COP) patch files that are installed
                                                         on the active version. |
| Inactive Version Installed Software Options | Displays the versions of installed software options, including COP patch files that are installed on the inactive version. |

| From the Cisco Unified Operating System Administration window, navigate to Show > System . See the following table for descriptions of the fields on the System Status window. Table 5. System Status Field Descriptions Field Description Host Name Displays the name of the Cisco MCS host where Cisco Unified Operating System is installed. Date Displays the date and time based on the continent and region that were specified during operating system installation. Time Zone Displays the time zone that was chosen during installation. Locale Displays the language that was chosen during operating system installation. Product Version Displays the operating system version. Platform Version Displays the platform version. License MAC Displays the license MAC. Uptime Displays system uptime information. CPU Displays the percentage of CPU capacity that is idle, the percentage that is running system processes, and the percentage
                                                         that is running user processes. Memory Displays information about memory usage, including the amount of total memory, free memory, used memory, cached memory, shared
                                                         memory, and buffers in KBytes. Disk/active Displays the amount of total, free, and used disk space on the active disk. Disk/inactive Displays the amount of total, free, and used disk space on the inactive disk. Disk/logging Displays the amount of total, free, and disk space that is used for disk logging. | Field | Description | Host Name | Displays the name of the Cisco MCS host where Cisco Unified Operating System is installed. | Date | Displays the date and time based on the continent and region that were specified during operating system installation. | Time Zone | Displays the time zone that was chosen during installation. | Locale | Displays the language that was chosen during operating system installation. | Product Version | Displays the operating system version. | Platform Version | Displays the platform version. | License MAC | Displays the license MAC. | Uptime | Displays system uptime information. | CPU | Displays the percentage of CPU capacity that is idle, the percentage that is running system processes, and the percentage
                                                         that is running user processes. | Memory | Displays information about memory usage, including the amount of total memory, free memory, used memory, cached memory, shared
                                                         memory, and buffers in KBytes. | Disk/active | Displays the amount of total, free, and used disk space on the active disk. | Disk/inactive | Displays the amount of total, free, and used disk space on the inactive disk. | Disk/logging | Displays the amount of total, free, and disk space that is used for disk logging. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Host Name | Displays the name of the Cisco MCS host where Cisco Unified Operating System is installed. |
| Date | Displays the date and time based on the continent and region that were specified during operating system installation. |
| Time Zone | Displays the time zone that was chosen during installation. |
| Locale | Displays the language that was chosen during operating system installation. |
| Product Version | Displays the operating system version. |
| Platform Version | Displays the platform version. |
| License MAC | Displays the license MAC. |
| Uptime | Displays system uptime information. |
| CPU | Displays the percentage of CPU capacity that is idle, the percentage that is running system processes, and the percentage
                                                         that is running user processes. |
| Memory | Displays information about memory usage, including the amount of total memory, free memory, used memory, cached memory, shared
                                                         memory, and buffers in KBytes. |
| Disk/active | Displays the amount of total, free, and used disk space on the active disk. |
| Disk/inactive | Displays the amount of total, free, and used disk space on the inactive disk. |
| Disk/logging | Displays the amount of total, free, and disk space that is used for disk logging. |

| Field | Description |
|---|---|
| Host Name | Displays the name of the Cisco MCS host where Cisco Unified Operating System is installed. |
| Date | Displays the date and time based on the continent and region that were specified during operating system installation. |
| Time Zone | Displays the time zone that was chosen during installation. |
| Locale | Displays the language that was chosen during operating system installation. |
| Product Version | Displays the operating system version. |
| Platform Version | Displays the platform version. |
| License MAC | Displays the license MAC. |
| Uptime | Displays system uptime information. |
| CPU | Displays the percentage of CPU capacity that is idle, the percentage that is running system processes, and the percentage
                                                         that is running user processes. |
| Memory | Displays information about memory usage, including the amount of total memory, free memory, used memory, cached memory, shared
                                                         memory, and buffers in KBytes. |
| Disk/active | Displays the amount of total, free, and used disk space on the active disk. |
| Disk/inactive | Displays the amount of total, free, and used disk space on the inactive disk. |
| Disk/logging | Displays the amount of total, free, and disk space that is used for disk logging. |

| Step 1 | From the Cisco Unified System Administration window, choose Show > IP Preferences . The IP Preferences window appears. Records from an active (prior) query may also appear in the window. |
|---|---|
| Step 2 | To find all
                                       				records in the database, ensure the dialog box is empty and go to Step 4. |
| Step 3 | To filter or search records, do the following: From the first
                                             					 drop-down list box, select a search parameter. From the second
                                             					 drop-down list box, select a search pattern. Specify the
                                             					 appropriate search text, if applicable. Note To add additional search criteria, click the + button. When you add criteria, the
                                                      						  system searches for a record that matches all criteria that you specify. To
                                                      						  remove criteria, click the – button to remove the last added
                                                      						  criterion or click the Clear Filter button to remove all
                                                      						  added search criteria. | Note | To add additional search criteria, click the + button. When you add criteria, the
                                                      						  system searches for a record that matches all criteria that you specify. To
                                                      						  remove criteria, click the – button to remove the last added
                                                      						  criterion or click the Clear Filter button to remove all
                                                      						  added search criteria. |
| Note | To add additional search criteria, click the + button. When you add criteria, the
                                                      						  system searches for a record that matches all criteria that you specify. To
                                                      						  remove criteria, click the – button to remove the last added
                                                      						  criterion or click the Clear Filter button to remove all
                                                      						  added search criteria. |
| Step 4 | Click Find . All matching records appear. You can change the number of items
                                          				that appear on each page by choosing a different value from the Rows per Page
                                          				drop-down list box. The following table contains descriptions of the IP Preferences
                                          				fields. Table 6. IP Preferences Field Descriptions Field Description Application Name of the application using (listening on) the port. Protocol Protocol used on this port (TCP, UDP). Port Number Numeric port number. Type Type of traffic allowed on this port: Public—All traffic allowed Translated—All traffic allowed but forwarded to a
                                                                  								different port Private—Traffic only allowed from a defined set of
                                                                  								remote servers, for example, other nodes in the cluster Translated Port Traffic destined for this port is forwarded to the port
                                                         						  listed in the Port Number column. This field applies to Translated type ports
                                                         						  only. Status Status of port usage: Enabled—In use by the application and opened by the
                                                                  								firewall Disabled—Blocked by the firewall and not in use Description Brief description of how the port is used. | Field | Description | Application | Name of the application using (listening on) the port. | Protocol | Protocol used on this port (TCP, UDP). | Port Number | Numeric port number. | Type | Type of traffic allowed on this port: Public—All traffic allowed Translated—All traffic allowed but forwarded to a
                                                                  								different port Private—Traffic only allowed from a defined set of
                                                                  								remote servers, for example, other nodes in the cluster | Translated Port | Traffic destined for this port is forwarded to the port
                                                         						  listed in the Port Number column. This field applies to Translated type ports
                                                         						  only. | Status | Status of port usage: Enabled—In use by the application and opened by the
                                                                  								firewall Disabled—Blocked by the firewall and not in use | Description | Brief description of how the port is used. |
| Field | Description |
| Application | Name of the application using (listening on) the port. |
| Protocol | Protocol used on this port (TCP, UDP). |
| Port Number | Numeric port number. |
| Type | Type of traffic allowed on this port: Public—All traffic allowed Translated—All traffic allowed but forwarded to a
                                                                  								different port Private—Traffic only allowed from a defined set of
                                                                  								remote servers, for example, other nodes in the cluster |
| Translated Port | Traffic destined for this port is forwarded to the port
                                                         						  listed in the Port Number column. This field applies to Translated type ports
                                                         						  only. |
| Status | Status of port usage: Enabled—In use by the application and opened by the
                                                                  								firewall Disabled—Blocked by the firewall and not in use |
| Description | Brief description of how the port is used. |

| Note | To add additional search criteria, click the + button. When you add criteria, the
                                                      						  system searches for a record that matches all criteria that you specify. To
                                                      						  remove criteria, click the – button to remove the last added
                                                      						  criterion or click the Clear Filter button to remove all
                                                      						  added search criteria. |
|---|---|

| Field | Description |
|---|---|
| Application | Name of the application using (listening on) the port. |
| Protocol | Protocol used on this port (TCP, UDP). |
| Port Number | Numeric port number. |
| Type | Type of traffic allowed on this port: Public—All traffic allowed Translated—All traffic allowed but forwarded to a
                                                                  								different port Private—Traffic only allowed from a defined set of
                                                                  								remote servers, for example, other nodes in the cluster |
| Translated Port | Traffic destined for this port is forwarded to the port
                                                         						  listed in the Port Number column. This field applies to Translated type ports
                                                         						  only. |
| Status | Status of port usage: Enabled—In use by the application and opened by the
                                                                  								firewall Disabled—Blocked by the firewall and not in use |
| Description | Brief description of how the port is used. |