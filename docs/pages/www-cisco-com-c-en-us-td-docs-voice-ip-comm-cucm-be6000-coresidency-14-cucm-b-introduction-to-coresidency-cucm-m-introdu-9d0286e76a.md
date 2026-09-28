---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-coresidency-14-cucm-b-introduction-to-coresidency-cucm-m-introdu-9d0286e76a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/Coresidency/14/cucm_b_introduction-to-coresidency/cucm_m_introduction-to-coresidency.html
retrieved_at: 2026-08-25T11:01:24.679488+00:00
---

Cisco BE6000 and Cisco BE7000 (CSR 14) Coresidency Policy Requirements

# Cisco BE6000 and Cisco BE7000 (CSR 14) Coresidency Policy Requirements

Find Matches in This Book

## Results

Updated: June 14, 2021

Chapter: Introduction to Coresidency

## Chapter: Introduction to Coresidency

# Introduction to Coresidency

## Coresidency Inclusions

Coresident means “running different Collaboration applications in dedicated virtual machines on the same virtualized Business
                              Edition physical server or host”.

In addition to Cisco Unified Communications appliance (UC) applications that are sold with Cisco Business Edition appliance
                              6000 (BE6000M, BE6000H, and BE6000S) and Cisco Business Edition 7000 (BE7000M and BE7000H), Cisco also allows the installation
                              of a broader range of Cisco and third-party virtualized applications, subject to the conditions that are detailed in this
                              document.

Cisco Business Edition Embedded Virtualization Basic 7.x

Cisco Business Edition Embedded Virtualization Basic Plus 7.x

Cisco Business Edition Embedded Virtualization Enhanced 7.x

Cisco UC Virtualization Hypervisor Plus 6.x

Cisco UC Virtualization Foundation 6.x

Cisco Collaboration Virtualization Standard 6.x

End of Support embedded virtualization offers (Cisco UC Virtualization Hypervisor 4x/5x, license-only Cisco UC Virtualization
                                    Foundation 4x/5x)

### BE6000M, BE6000H, BE7000M, and BE7000H

Business Edition applications include the Collaboration applications that are explicitly integrated in the BE6000 and BE7000
                                 Solutions. These applications are factory-preloaded on the appliance and many are integrated with BE6000 starter licensing.
                                 Business Edition applications that are preloaded on BE6000M, BE6000H, BE7000M, and BE7000H servers are as follows:

Cisco Prime Collaboration Provisioning (10.0 and later releases only)

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

On BE6000M, BE6000H, BE7000M, BE7000H servers with embedded virtualization software licenses:

Cisco supports all Business Edition applications that are in the preceding list.

Non-Business Edition applications are allowed if all rules in this document are followed. Cisco TAC

support is only for products that are purchased from Cisco with a valid, active maintenance contract. Refer to the Non-Business Edition Applications .

Not all UC applications support coresidency, or they may have limited support of coresidency. See each product's page on the http://www.cisco.com/go/virtualized-collaboration for its coresidency policy.

All other general UC virtualization rules apply; for example, VMware feature support and supported ESXi versions. For more
                                 information, see the http://www.cisco.com/go/virtualized-collaboration

### BE6000S

BE6000S supports only the following Core Business Edition applications that are preloaded on a BE6000S appliance:

Cisco Prime Collaboration Provisioning

Cisco Unified Communications Manager

Cisco Unity Connection

Cisco Unified Communications Manager IM and Presence Service

Cisco Paging Server

Cisco only supports the Core Business Edition applications listed above for BE6000S appliances. No other applications (either
                                 Cisco or third party) are supported with BE6000S currently, even if other virtualization software licenses are substituted.

### Non-Business Edition Applications

In a BE6000 or BE7000 deployment with one physical server, up to three third-party virtual machines may run on the server.
                                 For larger deployments, a maximum of three times the number of physical servers is permitted. The allowed quantity of third-party
                                 virtual machines can be deployed across physical servers in any combination. For example, with two physical servers, the six
                                 virtual machines can be distributed evenly across both, all, or one physical server.

Non-Business Edition applications include the following:

Other Cisco Collaboration applications that are listed at www.cisco.com go virtualized-collaboration (such as MediaSense) that are not explicitly listed as part of the BE6000 or BE7000 solutions. This includes Microsoft Windows,
                                       SQL Server, or ActiveDirectory dedicated to a Cisco application (such as Unified Contact Center Enterprise, TelePresence Media
                                       Server, or Spark Hybrid Service connectors).

Virtualized third-party applications that are included in the Solution Partner Program (SPP), formerly known as Cisco Developer
                                       Network (CDN) Marketplace Solutions Catalog for Collaboration. A list of all permitted third-party Collaboration applications
                                       can be found here . Select Technology = Collaboration.

You may only use third-party applications from the Collaboration category with the Business Edition embedded Hypervisor licenses.

Virtualized third-party applications that are offered through the Cisco SolutionsPlus Program and complementary to Collaboration
                                       are described at the http://www.cisco.com/web/partners/pr46/solutions_plus/index.html.

Cisco Smart Software Manager satellite

For more details on supported Non-Business Edition applications, see the application links in the “Cisco Collaboration Virtualization
                                 Support” table at www.cisco.com go virtualized-collaboration .

Regardless of virtulization license, all non-Business Edition applications must be qualified to run virtualized on VMware
                                 and must align with the virtualization software requirements for Cisco Collaboration that are outlined at the http://www.cisco.com/go/virtualized-collaboration/

All applications must support the version of VMware vSphere ESXi on the Business Edition appliance and align with supported
                                                   versions of Business Edition and Non-Business Edition Collaboration applications.

If you run a coresident deployment that includes third-party non-Business Edition applications, you must agree to temporarily
                                                   reduce the number of virtual machines that are running on a host if we deem it necessary for debugging purposes.

You must permanently reduce the number of virtual machines that are running on a host if we determine that the host is overloaded.

If you are unwilling to agree to these requirements, Cisco TAC will not support the coresident deployment.

Support for third-party applications is provided by the vendor of the individual application.

| Note | You may only use third-party applications from the Collaboration category with the Business Edition embedded Hypervisor licenses. |
|---|---|

| Important | All applications must support the version of VMware vSphere ESXi on the Business Edition appliance and align with supported
                                                   versions of Business Edition and Non-Business Edition Collaboration applications. If you run a coresident deployment that includes third-party non-Business Edition applications, you must agree to temporarily
                                                   reduce the number of virtual machines that are running on a host if we deem it necessary for debugging purposes. You must permanently reduce the number of virtual machines that are running on a host if we determine that the host is overloaded. If you are unwilling to agree to these requirements, Cisco TAC will not support the coresident deployment. Support for third-party applications is provided by the vendor of the individual application. |
|---|---|