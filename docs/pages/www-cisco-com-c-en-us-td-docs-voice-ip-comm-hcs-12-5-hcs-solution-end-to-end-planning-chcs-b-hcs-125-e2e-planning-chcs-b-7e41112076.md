---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-end-to-end-planning-chcs-b-hcs-125-e2e-planning-chcs-b-7e41112076
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/End_to_End_Planning/chcs_b_hcs-125-e2e-planning/chcs_b_hcs-125-e2e-planning_chapter_0101.html
retrieved_at: 2026-09-01T20:56:47.615083+00:00
---

Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

# Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

Updated: June 25, 2019

Chapter: Customer Premise Equipment

## Chapter: Customer Premise Equipment

# Customer Premise Equipment

## Prerequisites

Before you plan the customer premise equipment, make sure that you:

Review and have access to the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide .

Complete the actions outlined in previous sections of this guide including:

Initial system requirements and planned growth

Data center requirements

## Customer Premise
                        	 Equipment Workflow

## Determine the Type
                        	 of Site(s)

Determine the
                              		  type of site(s) that you plan to deploy. For detailed information on the
                              		  different sites, refer to Determine Your HCS Data Center Deployment Model .

### Dedicated
                           	 Server

Dedicated server
                              		refers to an Cisco HCS model of applications available for Micro Node deployments
                              		where one C-series server contains only one customer, but may have one or more
                              		UC applications running on the same server for that customer (for example Cisco
                              		Unified Communications Manager or Cisco Unity Connection).

## Determine Customer
                        	 Premise Equipment Router Model

Determine your
                                       			 router model based on the following UC application criteria:

Cisco Unified Survivable Remote Site Telephony (SRST)

Session Border Controller

PSTN Local Breakout - VoiceXML gateway

Cisco Unified Communications Domain Manager media resources such as conferencing, transcoding and Media Termination Point

Your HCS
                                          				system needs a router, such as ISR G2 series. Make sure you have accurate
                                          				cards, licensing and so forth for this router. You should take all of these
                                          				considerations into the type of router you choose as this device does many of
                                          				the key functions of your customer premise system. Many different models are
                                          				available with a wide range of performance and scale capacities. For more
                                          				details, refer to http://www.cisco.com/go/isr .

## Determine Services
                        	 on Router Model and Location of Services

Determine what
                                       			 services you need to run on your router model:

Session Border Controller

SRST

Determine if
                                       			 these services will reside on your router model, typically ISR G2, or on other
                                       			 standalone routers.

Determine
                                       			 customer premise conferencing resources.

## Determine Analog
                        	 Gateways

Determine the
                                       			 analog gateways that you need based on the devices that will be used:

ATA series

VG series

ISR router models

## Determine
                        	 Endpoints

Determine the
                                       			 TelePresence and video endpoints that will be used:

Desktop hard phones

Desktop clients

Mobile clients

Video endpoints

## Determine Access
                        	 Methods

Determine
                                       			 access methods:

MPLS: This
                                                					 is typical preferred choice for an HCS deployment.

Site-to-Site VPN: The customer premise router must be enabled
                                                					 and capable of supporting IPsec VPN.

Flex VPN: FlexVPN is deployed in HCS as a site-to-site VPN, between the customer site and the hosted HCS datacenter.

AnyConnect: Cisco AnyConnect VPN Client provides secure SSL connections for remote users.

Expressway OTT

## Determine
                        	 Standalone Firewalls

Determine your
                                       			 standalone firewalls. Consider the following for customer premise equipment:

- NATting is or is not
                                             				  performed at the customer premise

- Multiple routers or single
                                             				  router at customer premise

- IP addressing at customer
                                             				  premise

Make sure that whatever set up you choose, that all ports are open for the Cisco HCS system, refer to Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide .

## Determine Networks
                        	 for Customer Premise Equipment

Determine LAN
                                       			 network, refer to http://www.cisco.com/en/US/partner/tech/tk722/tk809/tsd_technology_support_protocol_home.html for more information.

Determine
                                       			 wireless LAN (WLAN) network including Access Points (APs), refer to http://docwiki.cisco.com/wiki/Internetworking_Technology_Handbook#LAN_Technologies for more information.

| Note | Make sure to
                                    		review the Cisco Hosted Collaboration
                                          			 Solution Compatibility Matrix for a full list of licensing details. |
|---|---|

|  |
|---|

| Determine your
                                       			 router model based on the following UC application criteria: Cisco Unified Survivable Remote Site Telephony (SRST) Session Border Controller PSTN Local Breakout - VoiceXML gateway Cisco Unified Communications Domain Manager media resources such as conferencing, transcoding and Media Termination Point Your HCS
                                          				system needs a router, such as ISR G2 series. Make sure you have accurate
                                          				cards, licensing and so forth for this router. You should take all of these
                                          				considerations into the type of router you choose as this device does many of
                                          				the key functions of your customer premise system. Many different models are
                                          				available with a wide range of performance and scale capacities. For more
                                          				details, refer to http://www.cisco.com/go/isr . |
|---|

| Step 1 | Determine what
                                       			 services you need to run on your router model: Session Border Controller SRST |
|---|---|
| Step 2 | Determine if
                                       			 these services will reside on your router model, typically ISR G2, or on other
                                       			 standalone routers. |
| Step 3 | Determine
                                       			 customer premise conferencing resources. |

| Determine the
                                       			 analog gateways that you need based on the devices that will be used: ATA series VG series ISR router models |
|---|

| Determine the
                                       			 TelePresence and video endpoints that will be used: Desktop hard phones Desktop clients Mobile clients Video endpoints |
|---|

| Determine
                                       			 access methods: MPLS: This
                                                					 is typical preferred choice for an HCS deployment. Site-to-Site VPN: The customer premise router must be enabled
                                                					 and capable of supporting IPsec VPN. Flex VPN: FlexVPN is deployed in HCS as a site-to-site VPN, between the customer site and the hosted HCS datacenter. AnyConnect: Cisco AnyConnect VPN Client provides secure SSL connections for remote users. Expressway OTT |
|---|

| Determine your
                                       			 standalone firewalls. Consider the following for customer premise equipment: NATting is or is not
                                             				  performed at the customer premise Multiple routers or single
                                             				  router at customer premise IP addressing at customer
                                             				  premise Make sure that whatever set up you choose, that all ports are open for the Cisco HCS system, refer to Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide . |
|---|

| Step 1 | Determine LAN
                                       			 network, refer to http://www.cisco.com/en/US/partner/tech/tk722/tk809/tsd_technology_support_protocol_home.html for more information. |
|---|---|
| Step 2 | Determine
                                       			 wireless LAN (WLAN) network including Access Points (APs), refer to http://docwiki.cisco.com/wiki/Internetworking_Technology_Handbook#LAN_Technologies for more information. |