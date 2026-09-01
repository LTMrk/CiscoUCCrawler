---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-end-to-end-planning-chcs-b-hcs-125-e2e-planning-chcs-b-aa2c4d28dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/End_to_End_Planning/chcs_b_hcs-125-e2e-planning/chcs_b_hcs-125-e2e-planning_chapter_0100.html
retrieved_at: 2026-09-01T20:56:43.507107+00:00
---

Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

# Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

Updated: June 25, 2019

Chapter: License Planning

## Chapter: License Planning

# License Planning

## Prerequisite

This chapter
                           		provides a high-level overview of the planning that must be done prior to
                           		acquiring and activating licenses for applications and management components
                           		running on HCS. This plan covers:

- Identifying licenses that
                              		  must be ordered for HCS

- Planning for other
                              		  components or pieces that are not supported by Cisco Prime License Manager

- Determining the costs of
                              		  licensing, and how those costs impact decision-making

License planning
                           		involves the following steps:

- Determine data center
                              		  infrastructure licenses.

- Determine data center
                              		  storage licenses.

- Determine VMware licenses.

- Determine UC Application
                              		  licenses.

- Determine HCS for Contact
                              		  Center licenses.

- Determine Third Party
                              		  software licenses.

- Determine HCS Management
                              		  licenses.

- Determine Cisco Expressway
                              		  licenses.

- Determine Rich Media
                              		  Session licenses.

- Determine Cisco Jabber
                              		  Guest Server licenses.

- License activation
                              		  considerations.

For more information on Licensing for Cisco HCS, see Cisco Hosted Collaboration Solution Release 12.5 License Management

## License Planning
                        	 Workflow

## Related
                        	 Documentation

Refer to the
                           		following document for further information about related licensing applications
                           		and products:

- Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide

## License Planning
                        	 Considerations

This section describes about the different license manager.

### HCS License
                           	 Manager (HLM) Planning Considerations

HCS License
                                 		  Manager (HLM) is an HCM-F service that provides centralized license management
                                 		  for HCS. HLM extends the functionality of Prime License Manager beyond the
                                 		  scope of one enterprise for use by service providers. HLM is used to assign
                                 		  each customer and its clusters to an Prime License Manager. HLM aggregates
                                 		  license usage by each cluster from each Prime License Manager into a License
                                 		  Summary report. In HCS 10.0(1) and later, Unified Communications Manager and Cisco Unity
                                 		  Connection are the only UC applications supported by HLM.

Consider the steps
                                 		  in the following procedure for HLM planning:

Use one HLM for each installation of HCS.

Set up each Prime License Manager in the HLM.

Load HCS licenses on a Prime License Manager before configuring the Prime License Manager on an HLM

When new customers are onboarded, they and their clusters must be assigned to an Prime License Manager through the HLM. Do
                                       not use the native management interface of Prime License Manager to assign a cluster. Always use the HLM to assign clusters
                                       to a Prime License Manager.

### Prime License
                           	 Manager Planning Considerations

Prime License Manager manages licensing for Unified Communications Manager clusters, and Cisco Unity Connection servers for
                                 multiple customers deployed in HCS. Typically, multiple customers are assigned to the same Prime License Manager server. If
                                 you have multiple clusters, all the clusters must be assigned to the same Prime License Manager server. That is, you cannot
                                 assign some of the clusters to one Prime License Manager and the rest to another Prime License Manager.

HCS licenses are registered to and loaded and activated onto the Prime License Managers deployed in HCS. The Prime License
                                 Managers deploy the HCS licenses to the UCM clusters and Unity Connection servers those are assigned by the HLM.

Take the following
                                 		  actions for Prime License Manager planning:

Determine if you need multiple instances of Prime License Manager, which can be the case in either of the following scenarios:

- If a Service Provider has
                                                				  resellers and wants to segregate the HCS licenses it provides to each reseller

- If there are more than 1000 Unified Communications application clusters in the HCS deployment

Install the
                                          			 Prime License Manager on the same management network as HCM-F so that Prime
                                          			 License Manager can access all Unified Communications application clusters. Prime License Manager can be coresiding with CUCM or can be installed as a stand-alone Prime License Manager residing at
                                             Application Space. If Prime License Manager   is coresiding with CUCM, then that Prime License Manager can be dedicated for
                                             a customer.

Install
                                          			 standalone Prime License Managers in the HCS Management domain. Set up each
                                          			 customer domain firewall to allow Prime License Manager to connect to UCM and
                                          			 Unity Connection through the HTTPS port 443 from the HCS management domain.

Plan for
                                          			 appropriate usage of the Prime License Manager web interface:

- For initial configuration,
                                                				  to generate license requests, to load license files, and to display license
                                                				  usage by cluster if desired.

- To assign a cluster, when using only the HLM, to a Prime License Manager instance so that the HLM can aggregate license usage
                                                for all customers and clusters.

## Determine Data Center Infrastructure Licenses

The following data
                           		center infrastructure components require specific licensing with the hardware
                           		feature capabilities:

Nexus switches (5500, 5600, 7000)

Session Border Controller

SAN

UCS Manager

ACS

VNMC

Prime Network Services Controller

Adaptive
                                 			 Security Device Manager (ASDM) Device Manager

Cisco Prime
                                 			 Network Registrar (formerly CNR)

Open Source
                                 			 TACACS (alternate for ACS Appliance)

For more information on these components, refer to the Cisco Hosted Collaboration Solution Release 12.5 License Management .

## Determine Data
                        	 Center Storage Licenses

The following data
                           		center storage components require specific licensing:

- SAN

- Nexus switches (5000, 5500, 7000)

- MDS switches

- UCS Manager

For more
                           		information, contact your Cisco sales engineer.

## Determine VMware
                        	 Licenses

For VMware licensing
                           		information, refer to the License Management for Cisco Hosted Collaboration Solution .

## Determine UC
                        	 Applications

The following UC
                           		applications require specific licensing:

HCS software
                                 			 licensing bundles

- HCS end customer license

- Cisco Telepresence

Jabber clients

Jabber server

Add-On licenses:

CUAC (server
                                       				  based and serverless)

CER

Cisco Expressway
                                       		  Server, Jabber Guest and Cisco Expressway Rich Media Session Licenses are
                                       		  add-on, session based licenses. They are managed separately from HLM/PLM and
                                       		  installed in Cisco Expressway. For more information see http://www.cisco.com/c/en/us/support/unified-communications/expressway-series/tsd-products-support-series-home.html

For information on determining licensing requirements for HCS License Manager and Prime License Manager, see License Planning Considerations .

## Determine HCS for
                        	 Contact Center

HCS for Contact
                           		Center is an Add On license. For more information, see http://www.cisco.com/en/US/products/ps12796/prod_installation_guides_list.html .

## Third-Party
                        	 Software Licenses

The following
                           		third-party software requires licensing:

- CUAC

- Cisco Paging Server (also
                              		  known as Singlewire - InformaCast Basic Paging)

- Prime Collaboration
                              		  Assurance

- VMware Virtual Center
                              		  (vCenter)

- HCS for Contact Center

Identity
                                 			 Providers - CA SiteMinder, Shibboleth, Microsoft AD FS, OpenAM, Oracle Identity
                                 			 Manager

For more information on Third-Party Software Licenses, see Cisco Hosted Collaboration Solution Release 12.5 License Management .

## Determine HCS
                        	 Management Licenses

The following HCS
                           		Management components require specific licensing:

Fulfillment
                                 			 licenses

CCDM

Cisco Unified CDM

HCM-F - HLM

Assurance
                                 			 licenses

- Cisco Prime Collaboration
                                    				Assurance

For more
                           		information, see the License Ordering
                              		  for Cisco Hosted Collaboration Solution guide.

## License Activation
                        	 Considerations

The following must
                           		be considered for license activation:

eFulfillment
                                 			 uses an Enterprise License Manager or Prime License Manager to connect directly
                                 			 to the Cisco License website to fulfill licenses from a PAK. Therefore, the
                                 			 Enterprise License Manager or Prime License Manager must have access to the
                                 			 Internet. If the Enterprise License Manager or Prime License Manager does not
                                 			 have direct access to the Cisco License website, then offline fulfillment can
                                 			 be used. For details on both methods, see Cisco Hosted Collaboration Solution Release 12.5 License Management .

Unified
                                 			 Communications Software Subscription (UCSS) activation - In HCS there are ways
                                 			 to purchase licenses and delay autoactivation. Consider UCSS activation when
                                 			 you are adding customers.

For more information
                           		on license activation, refer to the Cisco Hosted Collaboration Solution Release 12.5 License Management

|  |
|---|

| Step 1 | Determine if you need multiple instances of Prime License Manager, which can be the case in either of the following scenarios: If a Service Provider has
                                                				  resellers and wants to segregate the HCS licenses it provides to each reseller If there are more than 1000 Unified Communications application clusters in the HCS deployment |
|---|---|
| Step 2 | Install the
                                          			 Prime License Manager on the same management network as HCM-F so that Prime
                                          			 License Manager can access all Unified Communications application clusters. Prime License Manager can be coresiding with CUCM or can be installed as a stand-alone Prime License Manager residing at
                                             Application Space. If Prime License Manager   is coresiding with CUCM, then that Prime License Manager can be dedicated for
                                             a customer. |
| Step 3 | Install
                                          			 standalone Prime License Managers in the HCS Management domain. Set up each
                                          			 customer domain firewall to allow Prime License Manager to connect to UCM and
                                          			 Unity Connection through the HTTPS port 443 from the HCS management domain. |
| Step 4 | Plan for
                                          			 appropriate usage of the Prime License Manager web interface: For initial configuration,
                                                				  to generate license requests, to load license files, and to display license
                                                				  usage by cluster if desired. To assign a cluster, when using only the HLM, to a Prime License Manager instance so that the HLM can aggregate license usage
                                                for all customers and clusters. |

| Note | If you are
                                       		  using SAN-based storage, you must have storage access licensing for your Cisco
                                       		  components and for your SAN-based storage. |
|---|---|

| Note | Cisco Expressway
                                       		  Server, Jabber Guest and Cisco Expressway Rich Media Session Licenses are
                                       		  add-on, session based licenses. They are managed separately from HLM/PLM and
                                       		  installed in Cisco Expressway. For more information see http://www.cisco.com/c/en/us/support/unified-communications/expressway-series/tsd-products-support-series-home.html |
|---|---|