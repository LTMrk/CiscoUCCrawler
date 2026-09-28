---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-supported-platforms-b-15cucspl-html-e97433eb82
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/supported_platforms/b_15cucspl.html
retrieved_at: 2026-08-16T18:50:50.746720+00:00
---

Cisco Unity Connection 15 Supported Platforms List

# Cisco Unity Connection 15 Supported Platforms List

### Download Options

Updated: September 24, 2025

# Cisco Unity Connection 15 Supported Platforms List

This document provides information about the platforms supported for Cisco Unity Connection 15. The Unity Connection installation
               application prevents installation on servers that do not meet the exact specifications or models listed in this document.

## Platform Overlays
               	 for Unity Connection

Unity Connection 15 supports only virtual machines for installation. The Specifications for Virtual Platform Overlays for Currently Shipping Unity Connection lists the virtualization specifications, and the user and port limits when you install Unity Connection 15 on a virtual machine.

Unity
                              		  Connection is not pre-installed on any platform. Unity Connection can only be
                              		  installed on virtual machines.

### Specifications for
                  	 Virtual Platform Overlays for Currently Shipping Unity Connection
                  	 Servers

This section describes specifications and limits for Unity
                        		  Connection installed on a virtual machine.

For information on system requirements for a virtual environment, see the “ Requirements for Installing Unity Connection on a Virtual Machine ” section in the System Requirements for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

For platform part number, see the link: http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unity-connection.html

Virtual Platform Overlay for up to 1000 Users 1

Virtual Platform Overlay for up to 5000 Users

Virtual Platform Overlay for up to 10,000 Users

Virtual Platform Overlay for up to 20,000 Users

vCPU (Number of Virtual Processors)  Cores and Speed per Core 2

For virtual machine using ESXi 7.0 and later see section, Steps to update CPU Reservation for Virtual machine Hardware Version 17 and above for additional settings.

2 @
                                    					 minimum of 1.8 GHz each (3.6 GHz reserved)

2@a minimum of 2.50 GHz each (5.00 GHz reserved)

4@a minimum of 2.50 GHz each(10 GHz reserved)

7@a minimum of 2.50 GHz each (17.5 GHz reserved)

vRAM (Amount of Virtual RAM)

10 GB reserved

12 GB reserved

12  GB reserved

16 GB reserved

vDisk (Size of Virtual Hard Disks) 3

1 x 160GB, file system aligned at 64KB blocks

1 x 200 GB, file system aligned at 64KB blocks

Select the required OVA configuration from the drop-down list
                                    					 available for up to 10,000 users:

2 x 146 GB

2 x 300 GB

2 x 500 GB

File system aligned at 64KB blocks

Select the required OVA configuration from the drop-down list
                                    					 available for up to 20,000 users:

2 x 300 GB

2 x 500 GB

File system aligned at 64KB blocks

Total number of Tenants supported on Unity Connection

5

20

30

60

Total number of available ports per virtual machine: Voice + TTS
                                    					  + Voice recognition

24

100

150

250

Total number of available ports in a cluster 4

48

200

300

500

Total number of concurrent video calls on each virtual machine (cluster/standalone deployment 4

2

2

2

20

Total number of users with mailboxes

1,000

5,000

10,000

20,000

Number of Cisco Personal Communications Assistant users

1,000

5,000

10,000

20,000

1,000

5,000

10,000

20,000

Total number of LDAP Corporate Directory Users

1,000

5,000

10,000

20,000

Approximate message storage, G-711 codec, minutes

72,944

137,298

Depends on the .ova file:

2 x 146 GB: 252,831

2 x 300 GB: 514,287

2 x 500 GB: 919,992

Depends on the .ova file:

2 x 300 GB: 514,287

2 x 500 GB: 919,992

Unity Connection locations in the HTTPS network

3

10

10

25

Total number of Unity Connection SRSV branches supported

10

35

35

35

Maximum number of Unified Messaging(SIB) users supported on Microsoft Office 365 5

For 2 vCPU - 1000 6

3500

7500

15000

Maximum number of Unified Messaging(SIB) users supported on Microsoft Exchange

For 2 vCPU - 1000

5000

10000

20000

Maximum number of Unified Messaging(SIB) users supported on Google Workspace

For 2 vCPU - 1000

2000

4000

8000

1 Virtual Platform Overlay for up to 200 Users is no longer supported. It is advised to follow the specifications of virtual
                           platform overlay for up to 1000 users on Release 15.

2 For Spec- based processor requirements, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unity-connection.html

3 Opus
                           						codec doubles the Disk size when used as line codec with PCM linear as
                           						recording codec.

4 Cisco Media Sense is now end of life and end of support, hence Unity Connection will no longer provide the Video Messaging
                           feature for users.For more information on Cisco Media Sense EOL, see https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/mediasense/eos-eol-notice-c51-738857.html .

5 For information on configuring Unified Messaging, see Task List for Configuring Unified Messaging with Office 365 section of "Configuring Unified Messaging" chapter of the Unified Messaging Guide for Cisco Unity Connection Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html .

6 To change the number of CPUs(1vCPU to 2vCPU) for 1000 users overlay, see "Modifying the CPU" section in the ReadMe of the
                           applicable OVAs at https://software.cisco.com/download/home/283062758/type/282074348/release

### Steps to update CPU Reservation for Virtual machine Hardware Version 17 and above

If a virtual machine uses ESXi 7.0 U3 or 8.0 U1 (VM version 17) then 100% CPU reservation is a mandatory requirement to power
                     it on. This is required for exclusive assignment of the CPU cores.

For more information, see VMWare documents available at https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/vmc-aws-performance/ .

To power on virtual machine, you need to manually set the CPU reservation. Follow below steps to update the CPU reservation:

After OVA deployment open the virtual machine in VMWare.

Go to Advanced in the VM Option of Edit Settings and manually choose the Latency Sensitivity as "High"

Select Edit Settings > CPU > Reservation .

Manually update the CPU reservation value to (Speed per Core * Number of Cores). For example, if you pick a 2.6 GHz CPU the
                           VM will not power on unless the CPU reservation is manually altered. If you have a 7 core 2.6 GHz CPU, the CPU reservation
                           need to be set as (Speed per Core * Number of Cores). In this case the CPU reservation should be set to (2.6*7) = 18.2 GHz.

### Additional
                  	 Information Related to Platform-Overlay Specifications

#### Unity Connection
                     	 Cluster

The Unity Connection cluster feature provides high-availability
                        		voice messaging with two Unity Connection servers that are configured in a
                        		cluster. In this configuration, also known as active-active high availability,
                        		a single node consists of two servers, and the number of ports depends on the
                        		server model. The total number of node ports is additive (meaning a single node
                        		can support up to 500 ports, but the total number of users supported is
                        		applicable only to the primary server. The primary and secondary servers in a
                        		cluster must match in CPU and amount of memory, or the configuration is not
                        		supported.

If the hard disk space does not match on the two servers that you are using for a cluster, the smaller amount of disk space
                        determines the storage capacity for each server in the cluster. See also, section “ Requirements for Installing Unity Connection on a Virtual Machine ” in System Requirements for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

#### IMAP Idle Clients

The calculations for the total number of active clients assume the use of IMAP clients that support IMAP Idle. Cisco Unified
                        Personal Communicator 7.0 and earlier, Cisco Unified Mobility Advantage, and Cisco Unified Mobile Communicator do not support
                        IMAP Idle. As a result, each active instance of each of these clients (that does not support IMAP Idle) that is accessing
                        Unity Connection voice messages counts as four active clients.

#### Scaling Platform

Below is the list of supported clients on Unity Connection:

Cisco Jabber

Cisco Webex

Other clients are also supported on Unity Connection but below qualification numbers are specific to Jabber and Webex.

The table contains information on the number of endpoints of supported clients that Unity Connection supports with single
                           inbox users for specific OVA.

Total Endpoints Per CUC Cluster (Load Balancing) 7

HA Endpoints Per CUC HA Pair 8

0

2,000

4,000

2,000

0

500

1,000

500

In Load Balancing, clients are statically configured on either publisher server or subscriber server. If any of the server
                                 stops functioning, the services of the clients configured on the server go down.

In HA pair, clients are configured on publisher server. If publisher server stops functioning, the subscriber server provides
                                 services to the configured clients.

The table contains information on the number of endpoints of supported clients that Unity Connection supports with office
                           365 users for specific OVA.

Virtual Platform Overlay

vCPU (Number of Virtual Processors) Cores and Speed per Core

Office 365 Users

Endpoints on a Standalone Server

Total Endpoints Per CUC Cluster (Load Balancing) 9

HA Endpoints Per CUC HA Pair 10

20,000 Users

7vCPU

8,000

12,000

16,000

12,000

Non secure endpoints of supported clients for Office 365 users are yet not qualified with lower end OVAs

The table contains information on the number of secure endpoints of supported clients that Unity Connection supports along
                           with single inbox users.

Total Secure Endpoints Per CUC Cluster (Load Balancing) 9

HA Secure Endpoints

Per CUC HA Pair 10

Total Secure Endpoints Per CUC Cluster (Load Balancing) 9

HA Secure Endpoints

Per CUC HA Pair 10

20,000

5,000

10,000

5,000

15,000

7,500

15,000

7,500

10,000

8,000

16,000

8,000

5,000

8,500

17,000

8,500

0

10,000

20,000

10,000

The performance numbers qualified given are based on the assumptions that while user is using different clients for voice
                                             messaging operation the user is having less telephony usage.

Secure endpoints of supported clients for Single Inbox users are yet not qualified with lower end OVAs.

## Configuring vCPU,
               	 vRAM, and vDisk for Unity Connection on Virtual Machines

To simplify deployment of Unity Connection on a virtual machine,
                  		Cisco provides OVA templates for the virtual platform overlays defined in Table 1 .

Caution

Cisco Unity Connection supports changes in hardware configuration without rebuilding the servers. If virtual RAM is increased
                              to 10GB on supported OVA then you should execute CLI command utils cuc hwconfig update after modification. For CLI details, see "Utils Commands" chapter of Command Line Interface Reference Guide for Cisco Unified Communications Solutions available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-command-reference-list.html .

For changing the hardware configurations you must follow the workaround instructions mentioned at https://cdetsng.cisco.com/webui/#view=CSCvy86441 .

In addition, the OVA templates align the file system on the
                  		virtual disk(s) in the virtual machine at 64-KB blocks, which results in
                  		improved storage input/output operations per second (IOPS).

For information on downloading the latest OVA files, see the
                  		“Installation and Upgrade Information” section in the applicable Release Notes for
                     		  Cisco Unity Connection at http://www.cisco.com/en/US/products/ps6509/prod_release_notes_list.html .

For information on deploying an OVA file while installing a new Unity Connection virtual server, see chapter “ Installing Cisco Unity Connection ” in Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

For information on deploying an OVA file while migrating from a physical server to a virtual server, see the section “ Migrating a Physical Server to Virtual Machine ” of chapter “Maintaining Cisco Unity Connection Server” in Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

For information on deploying other Unified Communication
                  		applications on the same physical server with Unity Connection, see the Unified
                  		Communications Virtualization wiki at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unity-connection.html .

## Additional
               	 Platform Information

### Replacing a Unity Connection Server as You Upgrade to Unity Connection 15

MCS servers are not supported for use with Unity Connection 15, and an attempt to install or upgrade to Unity Connection 15
                     on these servers will fail. For more information on migrating a physical server to a virtual machine as you upgrade to Unity
                     Connection 15, see the chapter “ Maintaining Cisco Unity Connection Server ” of Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

## Platform Overlays
               	 for Unity Connection SRSV

For hardware specifications and support limits on each platform, see
                  		the Specification for Hardware Platforms and Cisco IOS
                     		  Software Releases Supported by Unity Connection SRSV .

The Specifications for Virtual Platform Overlays
                        			 Supported by Unity Connection SRSV table lists the virtualization
                  		specifications, the user limit, and the port limit when you install Unity
                  		Connection SRSV on a virtual machine.

### Specification for
                  	 Hardware Platforms and Cisco IOS Software Releases Supported by Unity
                  	 Connection SRSV

This section lists the supported hardware platforms and the
                        		  minimum Cisco IOS software release required to support the hardware platform
                        		  Unity Connection SRSV.

Cisco Platform

Unity Connection SRSV on SM-SRE-900-K9

Unity Connection SRSV on SM-SRE-910-K9

Cisco 2911

Cisco 2921

Cisco 2951

15.2(4)M4

15.2(4)M4

Cisco 3925

Cisco 3945

15.4(1)T

15.4(1)T

Cisco 3925E

Cisco 3945E

15.1(3)T

15.1(3)T

Cisco 4300

-

-

Cisco 4400

-

-

A
                                 		  different Cisco IOS software release may be required depending on the version
                                 		  of Cisco Unified Communications Manager Express or Cisco Unified Survivable
                                 		  Remote Site Telephony (SRST) being used. For more information refer to Cisco
                                 		  Unified Communications Manager Express documentation available at http://www.cisco.com/en/US/products/sw/voicesw/ps4625/index.html .

### Specifications for
                  	 Virtual Platform Overlays Supported by Unity Connection SRSV

This section lists the specifications for virtual platform overlays supported by Cisco Unity Connection SRSV.

Virtual Platform Overlay

vCPU (Number of Virtual Processors) Cores and Speed per Core

2@a minimum of 1.8 GHz

vRAM (Amount of Virtual RAM)

4 GB

vDisk (Size of Virtual Hard Disks)

1x160GB

Total number of available voice ports

12

Total number of users with mailboxes

500

Approximate message storage, G-711 codec, minutes

72,944

Number of public distribution lists

500

Number of Call Handlers

500

Number of languages supported

2

| Note | Unity
                              		  Connection is not pre-installed on any platform. Unity Connection can only be
                              		  installed on virtual machines. |
|---|---|

|  | Virtual Platform Overlay for up to 1000 Users 1 | Virtual Platform Overlay for up to 5000 Users | Virtual Platform Overlay for up to 10,000 Users | Virtual Platform Overlay for up to 20,000 Users |
|---|---|---|---|---|
| vCPU (Number of Virtual Processors)  Cores and Speed per Core 2 For virtual machine using ESXi 7.0 and later see section, Steps to update CPU Reservation for Virtual machine Hardware Version 17 and above for additional settings. | 2 @
                                    					 minimum of 1.8 GHz each (3.6 GHz reserved) | 2@a minimum of 2.50 GHz each (5.00 GHz reserved) | 4@a minimum of 2.50 GHz each(10 GHz reserved) | 7@a minimum of 2.50 GHz each (17.5 GHz reserved) |
| vRAM (Amount of Virtual RAM) | 10 GB reserved | 12 GB reserved | 12  GB reserved | 16 GB reserved |
| vDisk (Size of Virtual Hard Disks) 3 | 1 x 160GB, file system aligned at 64KB blocks | 1 x 200 GB, file system aligned at 64KB blocks | Select the required OVA configuration from the drop-down list
                                    					 available for up to 10,000 users: 2 x 146 GB 2 x 300 GB 2 x 500 GB File system aligned at 64KB blocks | Select the required OVA configuration from the drop-down list
                                    					 available for up to 20,000 users: 2 x 300 GB 2 x 500 GB File system aligned at 64KB blocks |
| Total number of Tenants supported on Unity Connection | 5 | 20 | 30 | 60 |
| Total number of available ports per virtual machine: Voice + TTS
                                    					  + Voice recognition | 24 | 100 | 150 | 250 |
| Total number of available ports in a cluster 4 | 48 | 200 | 300 | 500 |
| Total number of concurrent video calls on each virtual machine (cluster/standalone deployment 4 | 2 | 2 | 2 | 20 |
| Total number of users with mailboxes | 1,000 | 5,000 | 10,000 | 20,000 |
| Number of Cisco Personal Communications Assistant users | 1,000 | 5,000 | 10,000 | 20,000 |
| Total number of active
                                 				  clients: Cisco Unified Personal Communicator + Third-party IMAP + Cisco Unity
                                 				  conferencing + Cisco Unified Mobile Advantage + RSS + Phone View users (assumes
                                 				  all IMAP Idle clients) | 1,000 | 5,000 | 10,000 | 20,000 |
| Total number of LDAP Corporate Directory Users | 1,000 | 5,000 | 10,000 | 20,000 |
| Approximate message storage, G-711 codec, minutes | 72,944 | 137,298 | Depends on the .ova file: 2 x 146 GB: 252,831 2 x 300 GB: 514,287 2 x 500 GB: 919,992 | Depends on the .ova file: 2 x 300 GB: 514,287 2 x 500 GB: 919,992 |
| Unity Connection locations in the HTTPS network | 3 | 10 | 10 | 25 |
| Total number of Unity Connection SRSV branches supported | 10 | 35 | 35 | 35 |
| Maximum number of Unified Messaging(SIB) users supported on Microsoft Office 365 5 | For 2 vCPU - 1000 6 | 3500 | 7500 | 15000 |
| Maximum number of Unified Messaging(SIB) users supported on Microsoft Exchange | For 2 vCPU - 1000 6 | 5000 | 10000 | 20000 |
| Maximum number of Unified Messaging(SIB) users supported on Google Workspace | For 2 vCPU - 1000 6 | 2000 | 4000 | 8000 |

| Note | Other clients are also supported on Unity Connection but below qualification numbers are specific to Jabber and Webex. |
|---|---|

| Virtual Platform Overlay | vCPU (Number of Virtual Processors) Cores and Speed per Core | Single Inbox Users | Endpoints on a Standalone Server | Total Endpoints Per CUC Cluster (Load Balancing) 7 | HA Endpoints Per CUC HA Pair 8 |
|---|---|---|---|---|---|
| 20,000 Users | 7 vCPU | 20,000 | 5,000 | 10,000 | 5,000 |
| 15,000 | 7,500 | 15,000 | 7,500 |
| 10,000 | 8,000 | 16,000 | 8,000 |
| 5,000 | 8,500 | 17,000 | 8,500 |
| 0 | 10,000 | 20,000 | 10,000 |
| 10,000 Users | 4 vCPU | 10,000 | 2,000 | 4,000 | 2,000 |
| 0 | 4,000 | 8,000 | 4,000 |
| 5,000 Users | 2 vCPU | 5,000 | 1,000 | 2,000 | 1,000 |
| 0 | 2,000 | 4,000 | 2,000 |
| 1,000 Users | 2 vCPU | 1,000 | 200 | 400 | 200 |
| 0 | 500 | 1,000 | 500 |

| Virtual Platform Overlay | vCPU (Number of Virtual Processors) Cores and Speed per Core | Office 365 Users | Endpoints on a Standalone Server | Total Endpoints Per CUC Cluster (Load Balancing) 9 | HA Endpoints Per CUC HA Pair 10 |
|---|---|---|---|---|---|
| 20,000 Users | 7vCPU | 8,000 | 12,000 | 16,000 | 12,000 |

| Note | Non secure endpoints of supported clients for Office 365 users are yet not qualified with lower end OVAs |
|---|---|

| Virtual Platform Overlay | vCPU (Number of Virtual Processors) Cores and Speed per Core | Single Inbox Users | Secure Endpoints on a Standalone Server | Total Secure Endpoints Per CUC Cluster (Load Balancing) 9 | HA Secure Endpoints Per CUC HA Pair 10 |
|---|---|---|---|---|---|
| 20,000 Users | 7 vCPU(with 8GB RAM) | 20,000 | 2,500 | 5,000 | 2,500 |
| 15,000 | 5,000 | 10,000 | 5,000 |

| Virtual Platform Overlay | vCPU (Number of Virtual Processors) Cores and Speed per Core | Single Inbox Users | Secure Endpoints on a Standalone Server | Total Secure Endpoints Per CUC Cluster (Load Balancing) 9 | HA Secure Endpoints Per CUC HA Pair 10 |
|---|---|---|---|---|---|
| 20,000 Users | 7 vCPU(with 10GB RAM) | 20,000 | 5,000 | 10,000 | 5,000 |
| 15,000 | 7,500 | 15,000 | 7,500 |
| 10,000 | 8,000 | 16,000 | 8,000 |
| 5,000 | 8,500 | 17,000 | 8,500 |
| 0 | 10,000 | 20,000 | 10,000 |

| Note | The performance numbers qualified given are based on the assumptions that while user is using different clients for voice
                                             messaging operation the user is having less telephony usage. Secure endpoints of supported clients for Single Inbox users are yet not qualified with lower end OVAs. |
|---|---|

| Caution | Modification in the number of virtual CPUs and the amount of virtual RAM is allowed based on the configuration of the supported
                           OVAs. However change in the number or size of virtual disks is not supported. Cisco Unity Connection supports changes in hardware configuration without rebuilding the servers. If virtual RAM is increased
                              to 10GB on supported OVA then you should execute CLI command utils cuc hwconfig update after modification. For CLI details, see "Utils Commands" chapter of Command Line Interface Reference Guide for Cisco Unified Communications Solutions available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-command-reference-list.html . For changing the hardware configurations you must follow the workaround instructions mentioned at https://cdetsng.cisco.com/webui/#view=CSCvy86441 . |
|---|---|

| Cisco Platform | Unity Connection SRSV on SM-SRE-900-K9 | Unity Connection SRSV on SM-SRE-910-K9 |
|---|---|---|
| Cisco 2911 Cisco 2921 Cisco 2951 | 15.2(4)M4 | 15.2(4)M4 |
| Cisco 3925 Cisco 3945 | 15.4(1)T | 15.4(1)T |
| Cisco 3925E Cisco 3945E | 15.1(3)T | 15.1(3)T |
| Cisco 4300 | - | - |
| Cisco 4400 | - | - |

| Note | A
                                 		  different Cisco IOS software release may be required depending on the version
                                 		  of Cisco Unified Communications Manager Express or Cisco Unified Survivable
                                 		  Remote Site Telephony (SRST) being used. For more information refer to Cisco
                                 		  Unified Communications Manager Express documentation available at http://www.cisco.com/en/US/products/sw/voicesw/ps4625/index.html . |
|---|---|

|  | Virtual Platform Overlay |
|---|---|
| vCPU (Number of Virtual Processors) Cores and Speed per Core | 2@a minimum of 1.8 GHz |
| vRAM (Amount of Virtual RAM) | 4 GB |
| vDisk (Size of Virtual Hard Disks) | 1x160GB |
| Total number of available voice ports | 12 |
| Total number of users with mailboxes | 500 |
| Approximate message storage, G-711 codec, minutes | 72,944 |
| Number of public distribution lists | 500 |
| Number of Call Handlers | 500 |
| Number of languages supported | 2 |