---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-design-guide-b-15cucdg-b-15cucdg-chapter-010010-html-9d8334ed45
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg/b_15cucdg_chapter_010010.html
retrieved_at: 2026-08-17T02:15:05.584748+00:00
---

Design Guide for Cisco Unity Connection 15

# Design Guide for Cisco Unity Connection 15

Updated: August 12, 2025

Chapter: Virtualization

## Chapter: Virtualization

# Virtualization

## Virtualization
                        	 Requirements

Detailed requirements for installing Unity Connection on a virtual machine are listed in the “ Requirements for Installing Unity Connection on a Virtual Machine ” section of System Requirements for Cisco Unity Connection, Release 15 , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

## Scalability
                        	 Differences between Physical and Virtual Configurations

The maximum number of ports, the maximum number of users with mailboxes, and other scalability specifications differ between
                           comparable physical and virtual configurations. For detailed information, see the Cisco Unity Connection 15 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html .

## Installing Unity
                        	 Connection Cluster on Virtual Machines

Note the following about Unity Connection clusters and
                           		virtualization:

You can install a Unity Connection cluster on two virtual
                                 			 machines, or you can install a cluster on one virtual machine and one physical
                                 			 machine.

If you install a Unity Connection cluster on two virtual
                                 			 machines, the virtual machines must not be on the same blade. Ideally, the
                                 			 virtual machines are on separate chassis.

If you install a Unity Connection cluster on one virtual machine
                                 			 and one physical machine, you should configure the virtual machine to match the
                                 			 specifications of the physical server for CPU, memory, and disk space. If disk
                                 			 space on the physical server and virtual machine do not match, Unity Connection
                                 			 uses the smaller disk size to determine when the disk on which messages are
                                 			 stored has reached maximum capacity.

For information on installing Unity Connection on physical hosts and on virtual machines, see the “ Installing Cisco Unity Connection ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html

.

## Migrating Unity
                        	 Connection from Physical Servers to Virtual Machines

Note the following about migrating Unity Connection from a
                           		physical server to a virtual machine:

The physical hosts that are supported for use in a physical environment and those that are supported in a virtual environment
                                 are mutually exclusive. If you are currently running Unity Connection in a physical environment, you must replace the server.
                                 For information on physical hosts that are supported in a virtual environment, see the Cisco Unity Connection 15 Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html .

For information on migrating from physical servers to virtual machines, see the Migrating a Physical Server to a Virtual Machine section of the “Maintaining Cisco Unity Connection Server” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html