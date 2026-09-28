---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-coresidency-12-x-be6k-b-be6000-and-be7000-coresidency-1251-be6k--bec8918aa6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/Coresidency/12-x/be6k_b_be6000-and-be7000-coresidency-1251/be6k_b_be6000-and-be7000-coresidency-1251_chapter_00.html
retrieved_at: 2026-08-25T11:01:07.991702+00:00
---

Cisco BE6000 and Cisco BE7000 Coresidency Policy Requirements

# Cisco BE6000 and Cisco BE7000 Coresidency Policy Requirements

Find Matches in This Book

## Results

Updated: April 15, 2019

Chapter: Introduction to Coresidency

## Chapter: Introduction to Coresidency

# Introduction to Coresidency

## Coresidency
                        	 Inclusions

Coresident means “running different Collaboration applications in dedicated virtual machines on the same virtualized Business
                           Edition physical server or host”.

In addition to Cisco Unified Communications (UC) applications that are sold with Cisco Business Edition 6000 (BE6000M, BE6000H , and BE6000S ) and Cisco Business Edition 7000 (BE7000M and BE7000H), Cisco also allows the installation of a broader range of Cisco and
                           third-party virtualized applications, subject to the conditions that are detailed in this document.

This policy applies to all new and previously supplied BE6000S, BE6000M, BE6000H, BE7000M, and BE7000H appliances with embedded
                           virtualization software licenses (Cisco UC Virtualization Hypervisor, Cisco UC VirtualizationHypervisor Plus, Cisco UC Virtualization
                           Foundation or Cisco Collaboration Virtualization Standard) and any nonappliance generic Cisco UCS server running a permitted
                           embedded virtualization software license (older releases of Cisc UC Virtualization Standard).

### BE6000M, BE6000H,
                           	 BE7000M, and BE7000H

Cisco Prime Collaboration Provisioning (10.0 and later releases only)

Cisco Unified Provisioning Manager Business Edition (8.x and 9.x releases only)

Cisco Prime Collaboration Deployment

Cisco TelePresence Management Suite

Cisco Unified Communications Manager

Cisco Unity Connection

Cisco Unified Communications Manager IM and Presence Service

Cisco Paging Server

Cisco Expressway

Cisco Emergency Responder

Cisco Unified Attendant Console

Cisco Unified Contact Center Express

Cisco TelePresence Video Communication Server (CSR 11.5 and earlier releases only)

Cisco TelePresence Conductor (CSR 10.x and 11.x releases only)

Cisco TelePresence Server Virtual Machine (CSR 10.x and 11.x releases only)

Cisco TelePresence Content Server (10.6 through 11.5 releases only)

Cisco supports all Business Edition applications that are in the preceding list.

Non-Business Edition applications are allowed if all rules in this document are followed. Cisco TAC support is only for products
                                       that are purchased from Cisco with a valid, active maintenance contract. Refer to the Non-Business Edition Applications .

Not all UC applications support coresidency, or they may have limited support of coresidency. See each product's page on
                              the www.cisco.com/go/uc-virtualized for its coresidency policy.

All other general UC virtualization rules apply; for example, VMware feature support and supported ESXi versions. For more
                              information, see the www.cisco.com/go/uc-virtualized.

### BE6000S

Cisco Prime
                                       			 Collaboration Provisioning

Cisco Unified
                                       			 Communications Manager

Cisco Unity
                                       			 Connection

Cisco Unified
                                       			 Communications Manager IM and Presence Service

Cisco Paging
                                       			 Server

Cisco only supports
                              		the Core Business Edition applications listed above for BE6000S appliances. No
                              		other applications (either Cisco or third party) are supported with BE6000S
                              		currently, even if other virtualization software licenses are substituted.

### Non-Business
                           	 Edition Applications

In a BE6000 or BE7000 deployment with one physical server, up to three third-party virtual machines may run on the server.
                              For larger deployments, a maximum of three times the number of physical servers is permitted. The allowed quantity of third-party
                              virtual machines can be deployed across physical servers in any combination. For example, with two physical servers, the six
                              virtual machines can be distributed evenly across both, all, or one physical server.

Other Cisco Collaboration applications that are listed at www.cisco.com/go/virtualized-collaboration (such as MediaSense) that are not explicitly listed as part of the BE6000 or BE7000 solutions. This includes Microsoft Windows,
                                       SQL Server, or ActiveDirectory dedicated to a Cisco application (such as Unified Contact Center Enterprise, TelePresence Media
                                       Server, or Spark Hybrid Service connectors).

You may only use third-party applications from the
                                                      				  Collaboration category with the Business Edition embedded Hypervisor licenses.

Virtualized third-party applications that are offered through the Cisco SolutionsPlus Program and complementary to Collaboration
                                       are described at the http://www.cisco.com/web/partners/pr46/solutions_plus/index.html .

Cisco Smart Software Manager satellite

For more details on supported Non-Business Edition applications, see
                              		the application links in the “At a Glance - Cisco Collaboration Virtualization
                              		Support” table at www.cisco.com/go/virtualized-collaboration .

For permitted third-party applications, there is a maximum number of virtual machines that are allowed in a BE6000, BE7000,
                              and Cisco UCS server deployments running an embedded virtualization license (Cisco UC Virtualization Hypervisor, Cisco UC Virtualization Hypervisor Plus, Cisco
                                 UC Virtualization Foundation or Cisco Collaboration Virtualization Standard) .

All non-Business Edition applications must be qualified to run virtualized on VMware and must align with the virtualization
                              software requirements for Cisco Collaboration that are outlined at the http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html .

- All applications must
                                                			 support ESXi 6.5 as a minimum and align with supported versions of Business
                                                			 Edition and Non-Business Edition Collaboration applications.

If you run a coresident deployment that includes third-party
                                                   				non-Business Edition applications, you must agree to temporarily reduce the
                                                   				number of virtual machines that are running on a host if we deem it necessary
                                                   				for debugging purposes.

You must permanently reduce the number of virtual machines that
                                                   				are running on a host if we determine that the host is overloaded.

If you are unwilling to agree to these requirements, Cisco TAC
                                                   				will not support the coresident deployment.

Support for third-party applications is provided by the vendor of
                                                   				the individual application.

| Note | You may only use third-party applications from the
                                                      				  Collaboration category with the Business Edition embedded Hypervisor licenses. |
|---|---|

| Important | All applications must
                                                			 support ESXi 6.5 as a minimum and align with supported versions of Business
                                                			 Edition and Non-Business Edition Collaboration applications. If you run a coresident deployment that includes third-party
                                                   				non-Business Edition applications, you must agree to temporarily reduce the
                                                   				number of virtual machines that are running on a host if we deem it necessary
                                                   				for debugging purposes. You must permanently reduce the number of virtual machines that
                                                   				are running on a host if we determine that the host is overloaded. If you are unwilling to agree to these requirements, Cisco TAC
                                                   				will not support the coresident deployment. Support for third-party applications is provided by the vendor of
                                                   				the individual application. |
|---|---|