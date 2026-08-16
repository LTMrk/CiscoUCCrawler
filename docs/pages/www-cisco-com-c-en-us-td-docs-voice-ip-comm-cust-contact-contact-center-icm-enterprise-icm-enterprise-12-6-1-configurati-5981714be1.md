---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-5981714be1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/configuration-guide-for-cisco-unified-icm-contact-center-enterprise-release-12-6-1/ucce_b_1251-configuration-guide-unified-cce_chapter_01.html
retrieved_at: 2026-08-16T14:42:14.492507+00:00
---

Configuration Guide for Cisco Unified ICM Enterprise-Release 12.6(1)

# Configuration Guide for Cisco Unified ICM Enterprise-Release 12.6(1)

Updated: May 14, 2021

Chapter: Configuration Overview

## Chapter: Configuration Overview

# Configuration Overview

## Software Overview

### Cisco Unified
                           	 Intelligent Contact Management Overview

Unified Intelligent Contact Management provides
                              		enterprise-wide distribution of multichannel contacts across geographically separated contact centers. 
                              		Such multichannel contacts are inbound or outbound
                              		telephone calls, web collaboration requests, e-mail messages, and chat requests. Unified ICM is an
                              		open standards-based solution whose capabilities include routing, queuing,
                              		monitoring, and fault tolerance. Unified ICM forms
                              		the basis for the Cisco Unified Communications family of products.

The system software
                              		functions across environments and across channels.

The system software
                              		functions in the older environment of telephone calls delivered over
                              		Time-division multiplexing (TDM) lines, of hardware automatic call
                              		distributions (ACDs) and interactive voice responses (IVRs), and of call
                              		centers centralized around the hardware. The system software can route calls
                              		for a single 800 number or for several different numbers. The system software reads information about each incoming call
                              from the public network. The system software also determines the best destination for that call, and returns information to
                              the public network instructing it where to route the call. This process is known as call-by-call
                                 		  routing .

The system software
                              		makes routing decisions by executing scripts that can easily be modified. These
                              		scripts can use real-time information about activity at the contact centers to
                              		find the destination best able to handle the call. You can monitor how the
                              		system is handling calls. You can also observe how the system modifies  scripts when needed.

The system software functions in the newer environment of multichannel contact delivered through IP connections. These IP
                              connections are of software ACDs and IVRs. The connections are also of contact centers that can be as decentralized as the
                              Internet or as centralized as business practices requirements, not hardware necessities requirements.

The system software
                              		functions in the mixed transition environment that involves all of the above.

For detailed
                              		information about Unified ICM, refer to the Pre-installation Planning Guide for Cisco Unified ICM and the Administration Guide for Cisco Unified Contact Center Enterprise .

### Cisco Unified Contact Center Enterprise Overview

Cisco Unified Contact Center Enterprise ( Unified CCE ) delivers intelligent contact routing, call
                                 		  treatment, network-to-desktop computer telephony integration (CTI), and
                                 		  multichannel contact management over an IP infrastructure. It combines
                                 		  multichannel ACD functionality with IP telephony
                                 		  in a unified solution, enabling your company to rapidly deploy a distributed
                                 		  contact center infrastructure.

Unified CCE provides:

Segmentation of customers and monitoring of resource availability

Delivery of each contact to the most appropriate resource anywhere
                                       				in the enterprise

Comprehensive customer profiles using contact-related data, such
                                       				as dialed number (DN), and calling line ID

Routing to the most appropriate resource to meet customer needs
                                       				based on real-time conditions (such as agent skills, availability, and queue
                                       				lengths)

Presence integration to increase caller satisfaction through
                                       				improved agent performance and knowledge-worker expertise

Unified CCE allows you to smoothly integrate inbound and outbound voice
                                 		  applications with Internet applications such as real-time chat, web
                                 		  collaboration, and email. This integration enables a single agent to support
                                 		  multiple interactions simultaneously regardless of which communications channel
                                 		  the customer has chosen. Because each interaction is unique and may require
                                 		  individualized service, Cisco provides contact center solutions to manage
                                 		  customer interactions based on almost any contact attribute.

For detailed information about Unified CCE, refer to the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide and the Administration Guide for Cisco Unified Contact Center Enterprise .

## Configuration
                        	 Management

Unified ICM configuration information is permanently stored in the Central Controller database. The system software configuration consists
                              of hardware entities, call targets, announcements, routes, dialed numbers, and regions. Use the tools of the Unified ICM/ CCE Configuration Manager (referred to as "Configuration Manager" in this guide) to create and modify configuration data. When you apply a change in Configuration Manager, it is immediately
                              applied to the central database.

Note

You cannot have more than 60 active configuration connections at the same time. If more than 60 connections are required,
                                          you must add another distributor. These connections include:

Configuration Manager windows: Each open window establishes a connection to the backend.

Script Editor/ISE sessions: Each instance creates its own connection to the system.

Web configuration applications: Includes Tomcat-based web sessions such as cceadmin, unifiedconfig, and other admin web interfaces.

Other Manager Tools: Any UCCE admin tool launched from the AW that communicates with backend services.

To get started
                              		  setting up and maintaining your configuration, see Access Configuration Manager .

## Script Management

After you have set up your configuration, you can write routing
                              		  scripts and administrative scripts:

A routing script processes a call routing request from a
                                    				routing client and determines the best destination for that call. The system
                                    				software then passes a label associated with the destination back to the
                                    				routing client.

An administrative script runs periodically to perform a
                                    				task, such as setting variables.

Use the Script Editor to create, maintain, and monitor scripts.

You can set up different routing scripts to run for different types of tasks. You can define call types in terms of the telephone
                              number the caller dialed, the number the caller is calling from, and additional digits entered by the caller. For each call
                              type, you can schedule different routing scripts to run on different days or at different times of the day. The figure below
                              shows a sample ICM routing script, including longest available agent (LAA), and minimum expected delay (MED).

A routing script typically examines several targets and applies
                              		  selection rules to find an available qualified agent or a target with the
                              		  shortest expected delay. You can use any of several predefined selection rules
                              		  or you can set up your own selection criteria.

Within the Script Editor, you can open a script for browsing,
                              		  monitoring, or editing. When you open a script for editing, the Script Editor
                              		  automatically obtains the lock for that script.

To get started using the Script Editor to create or maintain scripts,
                              		  refer to the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise .

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | You cannot have more than 60 active configuration connections at the same time. If more than 60 connections are required,
                                          you must add another distributor. These connections include: Configuration Manager windows: Each open window establishes a connection to the backend. Script Editor/ISE sessions: Each instance creates its own connection to the system. Web configuration applications: Includes Tomcat-based web sessions such as cceadmin, unifiedconfig, and other admin web interfaces. Other Manager Tools: Any UCCE admin tool launched from the AW that communicates with backend services. |
|---|---|