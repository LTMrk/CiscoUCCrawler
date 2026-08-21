---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-solution-design-guide-hcscc-b-sold-496bac47c8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Solution_Design_Guide/hcscc_b_soldg-for-hcs-cc-12_5/hcscc_b_soldg-for-hcs-cc-12_5_chapter_01011.html
retrieved_at: 2026-08-21T23:54:56.609277+00:00
---

Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

# Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

Updated: February 16, 2020

Chapter: Shared Management and Aggregation

## Chapter: Shared Management and Aggregation

# Shared Management and Aggregation

## Unified Contact
                        	 Center Domain Manager

Cisco Unified Contact Center Domain Manager (Unified CCDM) is a browser-based management application that is designed for
                              use by Contact Center/system administrators, business users, and supervisors. It is a dense, multi-tenanted provisioning platform
                              that overlays the Contact Center equipment. The Contact Center equipment consists of configuration items, generally known
                              as resources, such as agents or skill groups, and events that are logged when the resources are used by the equipment, such
                              as call record statistics. CCDM also manages CVP Day 2 operations ( Media files and VXML applications ).

Unified CCDM partitions the resources in the equipment using a familiar folder paradigm. These folders are then secured using
                              a sophisticated security structure that allows administrators to specify which users can perform which actions within the
                              specified folders. Unified CCDM supplies a number of tools that operate on the configuration and statistics data and allow
                              users to modify both the Contact Center and Unified CCDM itself. The tools are all inherently multi-tenanted and the following
                              tools are currently supported:

Information Notices tool provides a "Message of the Day" functionality

Resource Manager tool enables users to create and modify resources such as agents or call types and organize them into a hierarchical folder
                                    structure

Security Manager tool enables administrators to set up and manage security permissions

Unified CCDM focuses on supplying multi-tenancy functionality, playing to the business plans of hosts and large enterprises
                              by enabling distributed or disparate Contact Center equipment to be partitioned:

Unified CCDM abstracts and virtualizes the underlying Contact Center equipment, thereby allowing centralized deployment and
                                    decentralized control, which in turn gives economies of scale while supporting multi-level user command and control.

Unified CCDM allows the powerful and flexible primary provisioning operations to be abstracted into simple, high-level tasks
                                    that enable business users to rapidly add and maintain Contact Center services across the virtualized enterprise (or portion
                                    thereof).

Unified CCDM users can see only the resources in the platform that they are entitled to see, thereby giving true multi-tenancy.

Unified CCDM users can only manipulate resources visible to them, by using the tools and features they are authorized to use,
                                    thereby giving role-based task control.

The advantages of CCDM are :

Provides Northbound APIs (SOAP and REST).

Can be used at the shared management level across multiple customer instances.

OVAs are sized for 50000 active and 300000 configured agents across multiple customer instances.

Unified CCDM maintains a complete data model of the Contact Center equipment to which it is connected. This data model is
                              periodically synchronized with the equipment. In addition to the configuration information such as agent and skill groups,
                              Unified CCDM records the events logged by the equipment, such as call records, for management information and reporting.

Unified CCDM provisions multiple Contact Center customer instances. It also provides the northbound REST and SOAP interfaces
                              for multiple instances from a shared Unified CCDM.

Install the Unified CCDM servers on a Service Provider Management AD domain and create a trust relationship with the Unified
                              CCDM domain and each customer instance domain.

## Unified
                        	 Communication Domain Manager

In HCS, Unified Communications Domain Manager provisions Unified Communications applications and devices, such as Cisco Unified
                           Communications Manager (Unified Communications Manager).

Unified
                           		Communications Domain Manager is a multi-tenant application, so you can use the
                           		Unified Communications Domain Manager server to provision all HCS customers.
                           		HCS supports multinode Unified Communications Domain Manager instance per HCS
                           		installation.

Unified Communications Domain Manager is optional for HCS for Contact Center solutions. (Unified CM can provide management
                                       on a by instance or customer basis.), You can replace Unified Communications Domain Manager with third-party provisioning
                                       solutions. See the Hosted Collaboration Solution documentation for guidance.

## Session Border Controller

The Cisco Hosted Collaboration Solution (HCS) uses Session Border Controllers in an aggregation layer for centralized management
                           and call distribution to customer instances. Cisco HCS for Contact
                                 						Center can use the HCS aggregation SBC. It can also use supported direct-to-PSTN solutions, such as Local Branch Office gateways
                           for call ingress and egress.

For more information on aggregation, see chapter on system architecture in Cisco Hosted Collaboration Solution Solution Reference Network Design Guide at https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/products-implementation-design-guides-list.html document.

| Note | Unified Communications Domain Manager is optional for HCS for Contact Center solutions. (Unified CM can provide management
                                       on a by instance or customer basis.), You can replace Unified Communications Domain Manager with third-party provisioning
                                       solutions. See the Hosted Collaboration Solution documentation for guidance. |
|---|---|