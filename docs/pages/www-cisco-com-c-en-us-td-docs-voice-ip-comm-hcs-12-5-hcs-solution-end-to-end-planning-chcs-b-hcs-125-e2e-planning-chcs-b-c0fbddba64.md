---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-end-to-end-planning-chcs-b-hcs-125-e2e-planning-chcs-b-c0fbddba64
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/End_to_End_Planning/chcs_b_hcs-125-e2e-planning/chcs_b_hcs-125-e2e-planning_chapter_01001.html
retrieved_at: 2026-09-01T20:57:03.591379+00:00
---

Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

# Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

Updated: June 25, 2019

Chapter: Unified Communications Application Planning

## Chapter: Unified Communications Application Planning

# Unified Communications Application Planning

## Prerequisites

Before you plan the
                           		UC applications processes for your Cisco HCS installation, make sure that you:

- Review the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide .

- Initial system requirements
                                    				and planned growth

- Data center requirements

- Licensing

- Customer premise equipment

- Service fulfillment

- Service assurance

- Customer-specific dial plan

## UC Applications
                        	 Workflow

## Determine UC
                        	 Applications Requirements

Identify
                                       			 customer size.

This size
                                          				relies on the choice of deployment model.

For instance,
                                          				if you anticipate a low usage for voicemail, for example, consider partitioning
                                          				Cisco Unity Connection while keeping Cisco Unified
                                             		  Communications Manager and Cisco Unified
                                             		  Communications Manager IM and Presence Service dedicated to one server.

Based on
                                       			 criteria collected, determine if the system requires central aggregation or if
                                       			 only local breakout is required.

Determine
                                       			 redundancy consideration based on your data center.

Based on
                                          				previous steps, you should have made some decisions about redundancy for your
                                          				system. You will also need to take these factors into consideration specific to
                                          				your customers. To streamline your processes, you may decide to have every
                                          				customer set up the same. Alternatively, if you need more flexibility, you may
                                          				decide to address each customer and each customer site on a case-by-case basis.
                                          				For local sites, be sure to consider using SRST.

Determine
                                       			 requirements for applications and services

Detailed background information about each of these applications is described in the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide .

Cisco Unified
                                                		  Communications Manager

You can set up your Cisco Unified
                                                   		  Communications Manager in a number of different ways, depending on your deployment model. Consider the following:

Decide if you want the Cisco Unified
                                                         		  Communications Manager to reside on a dedicated server or a shared server. For more information on the different deployment models and the differences,
                                                      see Determine Your HCS Data Center Deployment Model .

Call admissions control

Dial Plan

Voice gateways

SIP trunks

Media resources

Consider these factors concerning media resources:

The various resources for either local Customer Premise Equipment (ISR based), data center-based or software-based system
                                                            deployment.

Conference Hardware for ad-hoc video conferencing.

Bandwidth considerations for non-local resources.

LDAP

Decide if you plan to have LDAP synchronization enabled. With synchronization, consider what information you want to synchronize
                                                      initially and what information comes across in the subsequent synchs. If the LDAP server does not have synchronization enabled,
                                                      then the administrator should ensure consistent configurations across Unified Communications Manager and LDAP when configuring
                                                      user directory number associations. You also need to consider LDAP for endpoints as well as authentication purpose, and location
                                                      of LDAP, whether on premises provided by customers or in your data center. There are also NAT considerations for location
                                                      of LDAP.

Extension Mobility

Attendant Console

Cisco Paging Server - also known as Singlewire - InformaCast Basic Paging

Cisco Unity Connection

You can set up your Unity Connection in a number of different ways, depending on your deployment model. Consider the following:

Decide if you want the Unity Connection to reside on a dedicated server or a shared server. For more information on the different
                                                      deployment models and the differences, Determine Your HCS Data Center Deployment Model .

Partitioned Unity Connection

Decide if you want to partition Unity Connection to support multiple small medium businesses as tenants on a single Cisco
                                                      Unity Connection installation. For more information on partitioned Unity Connection, see Partitioned Unity Connection .

Voice messaging.

Depending on how flexible you want the system to be, consider integrated messaging versus unified messaging.

Cisco Unified
                                                		  Communications Manager IM and Presence Service

Your Cisco Unified
                                                   		  Communications Manager IM and Presence Service can be set up in a number of different ways, depending on your deployment
                                                					 model. You will want to consider aspects such as compliance and logging. Also,
                                                					 consider the following:

- Cisco Unified
                                                      		  Communications Manager IM and Presence Service and federation consideration for MSFT .

Cisco Unified
                                                         		  Communications Manager IM and Presence Service inter-domain federation.

Cisco
                                             				  Emergency Responder.

Attendant
                                             				  Console (CUAC).

Determine
                                       			 requirements for software endpoints, such as Jabber.

Determine E911 support for mobile clients, factoring in capacity impacts. You can find more details about capacity in the Cisco Hosted Collaboration Solution Capacity Planning Guide .

You have two different choices for determining the support for E911:

Inform users if 911 will not work.

Force users to identify the location. With the location information, the system can either find an location to connect the
                                                      emergency services or have the phone alert the user that they are not allowed to place the call.

Make sure that you understand what you are required to do from a legal perspective. Your requirements will depend on the size
                                                of company, type of service, and so forth.

Determine support for software install and upgrade of mobile and
                                             				  desktop clients.

Phone support: Determine the clients that you plan to support, such as user downloading clients from the Apple app store or
                                                      Google Play.

Desktop client support: Determine the software applications that you plan to support. These applications are stored on servers,
                                                      and will factor into your data center planning. For more details on data center requirements, see Determine Data Center Requirements .

|  |
|---|

| Step 1 | Identify
                                       			 customer size. This size
                                          				relies on the choice of deployment model. For instance,
                                          				if you anticipate a low usage for voicemail, for example, consider partitioning
                                          				Cisco Unity Connection while keeping Cisco Unified
                                             		  Communications Manager and Cisco Unified
                                             		  Communications Manager IM and Presence Service dedicated to one server. |
|---|---|
| Step 2 | Based on
                                       			 criteria collected, determine if the system requires central aggregation or if
                                       			 only local breakout is required. |
| Step 3 | Determine
                                       			 redundancy consideration based on your data center. Based on
                                          				previous steps, you should have made some decisions about redundancy for your
                                          				system. You will also need to take these factors into consideration specific to
                                          				your customers. To streamline your processes, you may decide to have every
                                          				customer set up the same. Alternatively, if you need more flexibility, you may
                                          				decide to address each customer and each customer site on a case-by-case basis.
                                          				For local sites, be sure to consider using SRST. |
| Step 4 | Determine
                                       			 requirements for applications and services Detailed background information about each of these applications is described in the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide . Cisco Unified
                                                		  Communications Manager You can set up your Cisco Unified
                                                   		  Communications Manager in a number of different ways, depending on your deployment model. Consider the following: Decide if you want the Cisco Unified
                                                         		  Communications Manager to reside on a dedicated server or a shared server. For more information on the different deployment models and the differences,
                                                      see Determine Your HCS Data Center Deployment Model . Call admissions control Dial Plan Voice gateways SIP trunks Media resources Consider these factors concerning media resources: The various resources for either local Customer Premise Equipment (ISR based), data center-based or software-based system
                                                            deployment. Conference Hardware for ad-hoc video conferencing. Bandwidth considerations for non-local resources. LDAP Decide if you plan to have LDAP synchronization enabled. With synchronization, consider what information you want to synchronize
                                                      initially and what information comes across in the subsequent synchs. If the LDAP server does not have synchronization enabled,
                                                      then the administrator should ensure consistent configurations across Unified Communications Manager and LDAP when configuring
                                                      user directory number associations. You also need to consider LDAP for endpoints as well as authentication purpose, and location
                                                      of LDAP, whether on premises provided by customers or in your data center. There are also NAT considerations for location
                                                      of LDAP. Extension Mobility Attendant Console Cisco Paging Server - also known as Singlewire - InformaCast Basic Paging Cisco Unity Connection You can set up your Unity Connection in a number of different ways, depending on your deployment model. Consider the following: Decide if you want the Unity Connection to reside on a dedicated server or a shared server. For more information on the different
                                                      deployment models and the differences, Determine Your HCS Data Center Deployment Model . Partitioned Unity Connection Decide if you want to partition Unity Connection to support multiple small medium businesses as tenants on a single Cisco
                                                      Unity Connection installation. For more information on partitioned Unity Connection, see Partitioned Unity Connection . Voice messaging. Depending on how flexible you want the system to be, consider integrated messaging versus unified messaging. Cisco Unified
                                                		  Communications Manager IM and Presence Service Your Cisco Unified
                                                   		  Communications Manager IM and Presence Service can be set up in a number of different ways, depending on your deployment
                                                					 model. You will want to consider aspects such as compliance and logging. Also,
                                                					 consider the following: Cisco Unified
                                                      		  Communications Manager IM and Presence Service and federation consideration for MSFT . Cisco Unified
                                                         		  Communications Manager IM and Presence Service inter-domain federation. Cisco
                                             				  Emergency Responder. Attendant
                                             				  Console (CUAC). |
| Step 5 | Determine
                                       			 requirements for software endpoints, such as Jabber. Determine E911 support for mobile clients, factoring in capacity impacts. You can find more details about capacity in the Cisco Hosted Collaboration Solution Capacity Planning Guide . You have two different choices for determining the support for E911: Inform users if 911 will not work. Force users to identify the location. With the location information, the system can either find an location to connect the
                                                      emergency services or have the phone alert the user that they are not allowed to place the call. Make sure that you understand what you are required to do from a legal perspective. Your requirements will depend on the size
                                                of company, type of service, and so forth. Determine support for software install and upgrade of mobile and
                                             				  desktop clients. Phone support: Determine the clients that you plan to support, such as user downloading clients from the Apple app store or
                                                      Google Play. Desktop client support: Determine the software applications that you plan to support. These applications are stored on servers,
                                                      and will factor into your data center planning. For more details on data center requirements, see Determine Data Center Requirements . |