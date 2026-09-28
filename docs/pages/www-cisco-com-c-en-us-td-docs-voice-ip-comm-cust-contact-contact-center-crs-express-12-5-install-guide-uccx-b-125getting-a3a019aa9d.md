---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-a3a019aa9d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_010.html
retrieved_at: 2026-08-16T21:14:56.688071+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: Unified IP IVR Architecture

## Chapter: Unified IP IVR Architecture

# Unified IP IVR Architecture

## Available Deployment
                        	 Models

Unified IP IVR can be deployed in
                              		  your IP network on any Cisco approved virtual servers.

The
                              		  following four figures illustrate the different ways you might deploy Unified
                              		  IP IVR:

The first two
                                    				figures show how you can deploy Unified IP IVR, without Unified CCE.

The second two
                                    				figures show how you can deploy Unified IP IVR with Unified CCE.

For more information on Unified IP IVR deployment models, see the design guide for Unified Customer Contact Express, which
                              includes information for Unified IP IVR Design Guides at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_implementation_design_guides_list.html .

## Standalone
                        	 Deployment

The following Unified IP IVR deployment models show Unified IP IVR deployed apart from Unified CCE.

The following figure shows Unified IP IVR installed on a separate server. The following are brief descriptions of key items
                              in the figure:

Gateway . Connects the enterprise Unified Communications network to the Public Switched Telephone Network (PSTN) and to other private
                                    telephone systems such as Public Branch Exchange (PBX). You purchase gateways separately. Both voice and web correspondence
                                    travel through the gateway.

Unified CM Server . Provides the features that are required to implement IP phones, manage gateways, provides failover and redundancy service
                                    for the telephony system, and directs voice over IP traffic to the Cisco Unified Contact Center Express system. You must purchase
                                    Unified CM separately.

Unified IP IVR and CM have to be installed on separate servers.

Cisco Unified CCX Server . Contains the Unified CCX Engine that runs Unified IP IVR.

The figure below shows how you can deploy Unified IP IVR apart from Unified CCE. This figure expands the focus to a Unified
                              CM cluster and depicts the possibility of having a single Unified CCX server with optional ASR and TTS servers.

## Cisco Unified Contact Center Enterprise Deployment

The following figure shows how one or more Unified IP IVR servers fit into an Unified CCE system.

The following figure shows a Unified CCE deployment model, but focuses on the Unified CM, Unified IP IVR, and Unified CCE
                              servers. In a Unified CCE system, there is the Unified CM server or servers, the Unified CCX server or servers, optional Unified
                              CCX subsystem servers such as MRCP ASR or MRCP TTS servers, and the Unified CCE servers.

The optional MRCP ASR and TTS software cannot be on the same server as the Unified CCX engine and is 3rd party software, not
                                          Cisco software.

Unified IP IVR supports high availability failover between two Unified CCX servers but not between a cluster of servers. You
                              can also deploy multiple Unified CCX servers (with Unified IP IVR) and let Unified CCE manage the load balancing and failover
                              between them. If one of the IVRs fails, the Unified CCE system will detect the failure, stop sending calls to the failed system,
                              and instead send those calls to other Unified IP IVRs.

## Services From Partners

Ordering from a Cisco-authorized online partner provides
                           		convenience for those customers that know which products best fit their needs
                           		and require immediate delivery. If your needs require onsite design,
                           		installation and ongoing support, a local reseller in your area could provide
                           		those value-added services. There are multiple places to order Cisco products
                           		online. Customers with Direct Purchasing agreements can order direct from
                           		Cisco. There are also numerous channel partners that transact e-commerce on
                           		their website for Cisco products. A full list of global Cisco Partners can be
                           		found on Cisco's Partner Locator website. Customers at small and
                           		medium sized business who want the convenience of online ordering can use
                           		Cisco's Online Partners.

## Support Services

Depending on individual operational, maintenance, and network
                           		level requirements, each installation has unique support requirements
                           		throughout the network life cycle of planning, designing, implementing,
                           		operating, and optimizing a network.

A full list of the Cisco support services available to you can
                           		be found at Voice and IP Communications Services .

| Note | Unified IP IVR and CM have to be installed on separate servers. |
|---|---|

| Note | The optional MRCP ASR and TTS software cannot be on the same server as the Unified CCX engine and is 3rd party software, not
                                          Cisco software. |
|---|---|