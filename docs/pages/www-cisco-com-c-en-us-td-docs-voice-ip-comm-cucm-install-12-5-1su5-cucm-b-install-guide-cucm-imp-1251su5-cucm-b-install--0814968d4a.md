---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-install-12-5-1su5-cucm-b-install-guide-cucm-imp-1251su5-cucm-b-install--0814968d4a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/install/12_5_1SU5/cucm_b_install-guide-cucm-imp-1251su5/cucm_b_install-guide-cucm-imp-14_chapter_01.html
retrieved_at: 2026-08-17T00:07:48.470746+00:00
---

Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU5

# Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU5

Updated: January 17, 2025

Chapter: Preinstallation Tasks

## Chapter: Preinstallation Tasks

# Preinstallation Tasks

## Preinstall Tasks for Unified Communications Manager

Step 1

Planning the Installation

Review the Planning chapter. Make sure to review the following:

Decide on your installation method.

Decide on your cluster topology.

For IM and Presence Service, decide whether you are installing a standard deployment or an IM and Presence Service central
                                                cluster.

Review the Requirements and Limitations.

Step 2

Required Installation Information

Review the installation requirements and record the configurations settings for each server that you plan to install.

Step 3

Create virtual machines.

Get base OVA.

Run the Collab Sizing Tool to get the required virtual machine count and specs of each virtual machine. If you don't want
                                                to run the Collab Sizing Tool, follow the guidance in the OVA readme and the OVA wizard to select a predefined starting point,
                                                which can be changed later if needed.

If you are installing from a skip-install OVA from the factory preload of a Business Edition appliance, see Installation Guide for Cisco Business Edition 6000 and 7000 .

Step 4

Mount the installation ISO file.

Place the installation ISO file in a location where the virtual machine can access it and edit the virtual machine's DVD drive
                                          to map to the file. Select the option to mount the DVD drive when you power on the virtual machine.

When you power on the virtual machine, it mounts the ISO file and start the installation process. Do not begin the installation
                                          process until you have completed all the steps in this procedure.

Step 5

Verify that the links between servers meet the 80-ms round-trip time (RTT) requirement and that you have enough bandwidth
                                       to support database replication.

For more information on the 80-ms RTT requirement, see the Cisco Unified Communications Solutions Reference Network Design .

Step 6

Verify the NTP status on the publisher node.

If the publisher node fails to synchronize with an NTP server, subscriber node installation can fail. On the Unified Communications
                                          Manager publisher node, run the utils ntp status CLI command.

Step 7

Complete the following firewall updates:

- If a firewall is in the routing path between nodes, disable the firewall.

- Increase the firewall timeout settings until after you complete the installation.

Temporarily allowing network traffic in and out of the nodes (for example, setting the firewall rule for these nodes to IP
                                          any/any) does not always suffice. The firewall might still close necessary network sessions between nodes due to timeouts.

Step 8

Do not run Network Address Translation (NAT) or Port Address Translation (PAT) between servers where you are installing Unified
                                       Communications Manager.

Step 9

Verify the NIC speed and duplex settings.

Ensure that the network interface card (NIC) speed and duplex settings on the switch port are the same as those that you plan
                                          to set on the new server.

For GigE (1000/FULL), you should set NIC and switch port settings to Auto/Auto ; do not set hard values.

Step 10

Enable PortFast on all switch ports that are connected to Cisco servers.

With PortFast enabled, the switch immediately brings a port from the blocking state into the forwarding state by eliminating
                                          the forwarding delay [the amount of time that a port waits before changing from its Spanning-Tree Protocol (STP) learning
                                          and listening states to the forwarding state].

Step 11

If you use DNS, verify that all servers on which you plan to install Unified Communications Manager are properly registered
                                       in DNS.

For details, see Verify DNS Registration .

Step 12

Licensing Requirements

Make sure that your system has adequate licensing.

## Preinstall Tasks for the IM and Presence Service

Step 1

Planning the Installation

Review the Planning chapter. Make sure to review the following:

Decide on your installation method and cluster topology.

For IM and Presence Service, decide whether you are installing a standard deployment or an IM and Presence Service central
                                                cluster.

Review the Requirements and Limitations.

Step 2

Supported Version

Make sure that the Unified Communications Manager and IM and Presence Service software versions are compatible.

Step 3

Required Installation Information

Gather all the information you need to complete the installation and configuration of the IM and Presence Service.

Step 4

Create your virtual machines.

For every node in your cluster, create virtual machines using the Virtual Server Template (OVA file) that is recommended for
                                          your release.

Different OVA files are available; choose the correct OVA file based on the environment in which you are deploying Unified
                                          Communications Manager. For more information, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-communications-manager.html .

Step 5

Verify network connectivity.

Make sure that each IM and Presence Service server has network access to the Unified Communications Manager publisher server.
                                          Ping the Unified Communications Manager publisher node from the other IM and Presence Service servers.

Step 6

Enable the Cisco AXL Web Service

Make sure that the Cisco AXL Web Service is enabled.

Step 7

Verify DNS Registration

If you use DNS, ensure that you have configured the hostname of the new IM and Presence Service server on the DNS server and
                                          that the DNS server can resolve the hostname of the Unified Communications Manager publisher server and of other IM and Presence
                                          Service servers (if any).

We recommend that you use the same DNS servers between IM and Presence Service and Unified Communications Manager. If you
                                                      use different DNS servers, it is likely to cause abnormal system behavior. Both Unified Communications Manager and IM and
                                                      Presence Service must either use DNS, or not use DNS, because it does not support mixed-mode deployments.

## Enable the Cisco AXL Web Service

Verify that the Cisco AXL Web Service is running.

Step 1

Log in to the Cisco Unified Serviceability interface.

Step 2

Choose Tools > Service Activation .

Step 3

Under Database and Admin Services , make sure that the Cisco AXL Web Service status indicates Activated .

Step 4

If the status says Deactivated , activate it by checking the adjacent check box and clicking Save .

## Verify DNS
                        	 Registration

Follow
                              		  this procedure if you use a DNS in your topology. You must verify that all
                              		  servers to be added are registered in DNS properly by performing the following
                              		  actions:

Step 1

Open a command
                                       			 prompt.

Step 2

To ping each
                                       			 server by its DNS name, enter ping
                                          				DNS_name .

Step 3

To look up each
                                       			 server by IP address, enter nslookup IP_address .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Planning the Installation | Review the Planning chapter. Make sure to review the following: Decide on your installation method. Decide on your cluster topology. For IM and Presence Service, decide whether you are installing a standard deployment or an IM and Presence Service central
                                                cluster. Review the Requirements and Limitations. |
| Step 2 | Required Installation Information | Review the installation requirements and record the configurations settings for each server that you plan to install. |
| Step 3 | Create virtual machines. | Get base OVA. Run the Collab Sizing Tool to get the required virtual machine count and specs of each virtual machine. If you don't want
                                                to run the Collab Sizing Tool, follow the guidance in the OVA readme and the OVA wizard to select a predefined starting point,
                                                which can be changed later if needed. If you are installing from a skip-install OVA from the factory preload of a Business Edition appliance, see Installation Guide for Cisco Business Edition 6000 and 7000 . |
| Step 4 | Mount the installation ISO file. | Place the installation ISO file in a location where the virtual machine can access it and edit the virtual machine's DVD drive
                                          to map to the file. Select the option to mount the DVD drive when you power on the virtual machine. When you power on the virtual machine, it mounts the ISO file and start the installation process. Do not begin the installation
                                          process until you have completed all the steps in this procedure. |
| Step 5 | Verify that the links between servers meet the 80-ms round-trip time (RTT) requirement and that you have enough bandwidth
                                       to support database replication. | For more information on the 80-ms RTT requirement, see the Cisco Unified Communications Solutions Reference Network Design . |
| Step 6 | Verify the NTP status on the publisher node. | If the publisher node fails to synchronize with an NTP server, subscriber node installation can fail. On the Unified Communications
                                          Manager publisher node, run the utils ntp status CLI command. |
| Step 7 | Complete the following firewall updates: If a firewall is in the routing path between nodes, disable the firewall. Increase the firewall timeout settings until after you complete the installation. | Temporarily allowing network traffic in and out of the nodes (for example, setting the firewall rule for these nodes to IP
                                          any/any) does not always suffice. The firewall might still close necessary network sessions between nodes due to timeouts. |
| Step 8 | Do not run Network Address Translation (NAT) or Port Address Translation (PAT) between servers where you are installing Unified
                                       Communications Manager. |  |
| Step 9 | Verify the NIC speed and duplex settings. | Ensure that the network interface card (NIC) speed and duplex settings on the switch port are the same as those that you plan
                                          to set on the new server. For GigE (1000/FULL), you should set NIC and switch port settings to Auto/Auto ; do not set hard values. |
| Step 10 | Enable PortFast on all switch ports that are connected to Cisco servers. | With PortFast enabled, the switch immediately brings a port from the blocking state into the forwarding state by eliminating
                                          the forwarding delay [the amount of time that a port waits before changing from its Spanning-Tree Protocol (STP) learning
                                          and listening states to the forwarding state]. |
| Step 11 | If you use DNS, verify that all servers on which you plan to install Unified Communications Manager are properly registered
                                       in DNS. | For details, see Verify DNS Registration . |
| Step 12 | Licensing Requirements | Make sure that your system has adequate licensing. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Planning the Installation | Review the Planning chapter. Make sure to review the following: Decide on your installation method and cluster topology. For IM and Presence Service, decide whether you are installing a standard deployment or an IM and Presence Service central
                                                cluster. Review the Requirements and Limitations. |
| Step 2 | Supported Version | Make sure that the Unified Communications Manager and IM and Presence Service software versions are compatible. |
| Step 3 | Required Installation Information | Gather all the information you need to complete the installation and configuration of the IM and Presence Service. |
| Step 4 | Create your virtual machines. | For every node in your cluster, create virtual machines using the Virtual Server Template (OVA file) that is recommended for
                                          your release. Different OVA files are available; choose the correct OVA file based on the environment in which you are deploying Unified
                                          Communications Manager. For more information, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-communications-manager.html . |
| Step 5 | Verify network connectivity. | Make sure that each IM and Presence Service server has network access to the Unified Communications Manager publisher server.
                                          Ping the Unified Communications Manager publisher node from the other IM and Presence Service servers. |
| Step 6 | Enable the Cisco AXL Web Service | Make sure that the Cisco AXL Web Service is enabled. |
| Step 7 | Verify DNS Registration | If you use DNS, ensure that you have configured the hostname of the new IM and Presence Service server on the DNS server and
                                          that the DNS server can resolve the hostname of the Unified Communications Manager publisher server and of other IM and Presence
                                          Service servers (if any). Note We recommend that you use the same DNS servers between IM and Presence Service and Unified Communications Manager. If you
                                                      use different DNS servers, it is likely to cause abnormal system behavior. Both Unified Communications Manager and IM and
                                                      Presence Service must either use DNS, or not use DNS, because it does not support mixed-mode deployments. | Note | We recommend that you use the same DNS servers between IM and Presence Service and Unified Communications Manager. If you
                                                      use different DNS servers, it is likely to cause abnormal system behavior. Both Unified Communications Manager and IM and
                                                      Presence Service must either use DNS, or not use DNS, because it does not support mixed-mode deployments. |
| Note | We recommend that you use the same DNS servers between IM and Presence Service and Unified Communications Manager. If you
                                                      use different DNS servers, it is likely to cause abnormal system behavior. Both Unified Communications Manager and IM and
                                                      Presence Service must either use DNS, or not use DNS, because it does not support mixed-mode deployments. |

| Note | We recommend that you use the same DNS servers between IM and Presence Service and Unified Communications Manager. If you
                                                      use different DNS servers, it is likely to cause abnormal system behavior. Both Unified Communications Manager and IM and
                                                      Presence Service must either use DNS, or not use DNS, because it does not support mixed-mode deployments. |
|---|---|

| Step 1 | Log in to the Cisco Unified Serviceability interface. |
|---|---|
| Step 2 | Choose Tools > Service Activation . |
| Step 3 | Under Database and Admin Services , make sure that the Cisco AXL Web Service status indicates Activated . |
| Step 4 | If the status says Deactivated , activate it by checking the adjacent check box and clicking Save . |

| Step 1 | Open a command
                                       			 prompt. |
|---|---|
| Step 2 | To ping each
                                       			 server by its DNS name, enter ping
                                          				DNS_name . |
| Step 3 | To look up each
                                       			 server by IP address, enter nslookup IP_address . |