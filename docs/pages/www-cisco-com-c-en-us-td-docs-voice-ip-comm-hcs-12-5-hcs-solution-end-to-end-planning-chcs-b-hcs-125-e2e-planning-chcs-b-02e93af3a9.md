---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-end-to-end-planning-chcs-b-hcs-125-e2e-planning-chcs-b-02e93af3a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/End_to_End_Planning/chcs_b_hcs-125-e2e-planning/chcs_b_hcs-125-e2e-planning_chapter_011.html
retrieved_at: 2026-09-01T20:56:39.050025+00:00
---

Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

# Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

Updated: June 25, 2019

Chapter: Data Center

## Chapter: Data Center

# Data Center

## Prerequisites

Before you plan the
                           		data center for your Cisco HCS installation, make sure that you:

Review and have access to the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide .

- Initial system requirements
                                       				and planned growth

## Data Center
                        	 Workflow

## Determine Data
                        	 Center Requirements

The following
                              		  procedures lists the high-level steps required to determine your data center
                              		  requirements.

Gather Data for Initial Data Center Planning .

Determine the Data Center Deployment Model .

Determine Details About Applications .

Identify the Various Networking Resources .

Determine Virtual Machine Distribution and Connectivity .

Determine DMZ Requirements .

Investigate Storage Planning .

## Gather Data for
                        	 Initial Data Center Planning

Collect and
                                       			 estimate the type of tenants using detailed information about your system. You
                                       			 should have already done this as part of Complete Tenant Matrix .

Gather
                                          				information about customers, customer average sizes, future growth, security
                                          				requirements, local versus central break out, regulatory requirements, and
                                          				access models.

Determine if
                                       			 there are any other services that are offered from the same data center as
                                       			 Cisco HCS.

Determine the
                                       			 locations and the number of data centers that you plan to deploy for Cisco HCS.

Locations and
                                          				number of data centers are determined based on target market proximity
                                          				requirements, redundancy requirements, size, and access models. All of these
                                          				factors can affect your costs. For UC applications, for example, you should
                                          				determine whether all of your customers will have the same redundancy or
                                          				whether the redundancy is determined on a per-customer basis.

Determine
                                       			 whether you have a single or multiple data center setup.

Choose your
                                       			 site deployment type.

Hosted

Extender

Remote
                                                					 managed

Hosted
                                                					 Private Cloud/Large Enterprise

## Determine the Data
                        	 Center Deployment Model

Using the
                              		  information collected about the locations, the number of data centers and the
                              		  capital expenditure determines your deployment model. Deployment models are:
                              		  Large PoD, Small PoD, or Micro Node. You may have already done this in Determine Your HCS Data Center Deployment Model .

For further information, see the Cisco Hosted Collaboration Solution Release 12.5 Capacity Planning Guide

Examine key
                                       			 attributes to determine the data center deployment model:

Number of
                                                   					 tenants

Average
                                                   					 tenant size

Total
                                                   					 dedicated UC instances

Total
                                                   					 shared UC instances

Total UC
                                                   					 instances and clusters

Supported
                                                   					 applications

Use the data
                                       			 and capacity requirements to determine the data center deployment model across
                                       			 one or more data centers.

## Determine Details
                        	 About Applications

Determine
                                       			 whether the management applications will be NATted into a Customer Domain.

Review the Cisco Hosted Collaboration
                                             			 Solution Compatibility Matrix to determine the required application versions for the current release.

For the most
                                          				recent compatibility information, see the compatibility matrix from the Cisco
                                          				HCS documentation page http://www.cisco.com/en/US/partner/products/ps11363/tsd_products_support_series_home.html

## Identify the
                        	 Various Networking Resources

Build your network
                              		  infrastructure with consideration of the following networking resources:

Virtual
                                    				machine templates: Details about these templates and other sizing
                                    				considerations can be found in the Unified Communications
                                       				  Virtualization Sizing Guidelines .

Service
                                    				profiles on Cisco Unified Computing System (UCS) Manager: Decide how many
                                    				service profiles you want for your system. From a hardware perspective, the
                                    				best service profile choice is two profiles when you compare upgrade reduction
                                    				versus hardware required. If hardware is not an issue, four service profiles is
                                    				the best choice.

Addressing
                                    				scheme for the UC applications: For more details, refer to IP Addressing for HCS Applications .

Management
                                    				domain addressing.

NATted
                                    				address pools in management domain for UC applications: For more details, refer
                                    				to NAT Planning Considerations .

VLANs: Use
                                    				the recommended numbering scheme. For more details, refer to Grouping VLANs and VLAN Numbering .

PSTN connectivity: For more details, refer to Identify Trunking Services .

Remote site access: Consider the following options for remote site access:

Site-to-Site VPN

Line Side access or Over-the-Top (OTT) VPN

SBC as a session border controller for SIP trunking

MPLS VPN

AnyConnect

FlexVPN

Plan for Expressway Deployment to allow roaming users to connect remotely.

### IP Addressing for
                           	 HCS Applications

One VLAN for each customer must be dedicated for each Cisco HCS Enterprise customer. Overlapping addresses for customer UC
                              infrastructure applications of each customer is supported.

The option to select the address pool from which addresses will be assigned for the customer's UC infrastructure applications
                              (Cisco HCS Instance) is also supported. This option is necessary to avoid any conflicts with customer-premises addressing
                              schemes.

When deploying
                                          		  Cisco HCS in the hosted environment, you must not have NAT
                                          		  between any end device (phone) and the Cisco Unified Communications Manager (UC
                                          		  application) on the line side, because some of the mid-call features may not
                                          		  function properly. However, when Over The Top access is supported (using
                                          		  Expressway, etc.), there can be NAT in front of the endpoint. It is also
                                          		  recommended that the HCS Management applications not be
                                          		  deployed within a NAT. Using NAT between the vCenter Server system and ESXi/ESX
                                          		  hosts is an unsupported configuration. For more details, see http://kb.vmware.com/kb/1010652

### NAT Planning
                           	 Considerations

For an HCS-LE
                                 		  deployment (single customer only), implementing Network Address Translation
                                 		  (NAT) between your management applications and Unified Communications
                                 		  applications is not required. If you implement NAT in this scenario, the
                                 		  synthetic call feature of Cisco Unified Operations Manager is not available.

### Grouping VLANs and
                           	 VLAN Numbering

Cisco recommends that when you design Layer 2 for a Cisco HCS deployment, you group the VLANs based on their usage. The current
                                 Service Provider Cisco HCS data center design assumes that each end customer consumes only two VLANs; however, it is possible
                                 to configure four VLANs for each end customer.

Use the following
                                 		  VLAN numbering scheme if four VLANs are configured for each end customer:

0100 to 0999:
                                       				UC Apps (100 to 999 are the customer IDs)

1100 to 1999:
                                       				outside VLANs (100 to 999 are the customer IDs)

2100 to 2999:
                                       				hcs-mgmt ( 100 to 999 are the customer IDs)

3100 to 3999:
                                       				Services ( 100 to 999 are the customer IDs)

Use all the
                                       				unused VLANs x000 to x099 (where x is 1, 2, or 3) and VLANS 4000 to 4095 for
                                       				other purposes

Use the following
                                 		  number scheme if only two VLANs are configured for each end customer:

0100 to 1999:
                                       				UC Apps (100 to 999 are the customer IDs for Group 1)

2100 to 3999:
                                       				outside VLANs (100 to 999 are the customer IDs for Group 1)

Use the following
                                 		  numbering scheme for additional end customers:

2100 to 2999:
                                       				UC Apps (100 to 999 are the customer IDs for Group 2)

3100 to 3999:
                                       				outside (100 to 999 are the customer IDs for Group 2)

Use the
                                       				unused VLANs for other purposes

While this is the
                                 		  recommended grouping of VLANS to help you scale the number of customers that
                                 		  can be hosted on a Cisco HCS platform, you may reach the upper limit of
                                 		  customers due to limitations in other areas of the Cisco HCS solution.

## Determine Virtual
                        	 Machine Distribution and Connectivity

Determine the virtual machine distribution. For more information on recommendations, refer to the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide .

Oversubscribed clusters

Nonoversubscribed clusters

Analyze the
                                       			 available bandwidth.

Based on the
                                          				deployment model, estimate:

The
                                                					 bandwidth needed between data centers.

The
                                                					 aggregate bandwidth needed between the data center and CPEs.

The
                                                					 aggregate bandwidth needed between the datacenter and PSTN network.

Determine the MPLS VPN peering arrangement between the Service Provider Cisco HCS Data Center and MPLS provider.

Determine
                                       			 whether to use Over-The-Top access or site-to-site VPN for remote access
                                       			 through the Internet.

## Determine DMZ
                        	 Requirements

For information on
                           		determining DMZ requirements for Expressway configuration see Data Center Configuration Overview .

### Data Center
                           	 Configuration Overview

This section
                              		provides guidance for configuring Collaboration Edge OTT in the Service
                              		Provider Cisco HCS data center. Use this information with, but not as a
                              		replacement for, the Cisco Expressway documentation.

Two more VLANs are required to accommodate ASA contexts, global DMZ inside and outside. The customer inside and outside VLANs
                              are also required. Configuration is required in the Nexus 7000, vSphere Distributed Switch (VDS) (and in the Nexus 5000, if deployed), UCS Manager, and ASA. The global DMZ inside VLAN (after Firewall) and the customer
                              outside VLAN extend into the DC. These VLANs are used on the virtualized Cisco Expressway-E.

Expressway in OTT
                                 		  Deployments Expressway-E hosts the public IP address. The client accesses
                              		this address by way of the public Internet. Expressway-E typically sits in the
                              		DMZ of the enterprise network. In the HCS DC, Expressway-E runs on UCS behind
                              		the ASA. Expressway-C sits in the same IP address space as Cisco Unified
                                 		  Communications Manager .
                              		Communication between Expressway-C and Expressway-E is through the ASA, which
                              		provides the NAT and firewall functions.

Shared Expressway for
                                 		  Business-to-Business Dialing : Expressway-E hosts the public IP address. The
                              		non-HCS businesses access this address by way of the public Internet.
                              		Expressway-E typically sits in the DMZ of the shared network, between the
                              		common outside and shared inside firewall contexts on ASA, to create a DMZ. The
                              		Expressway-E is connected to the Expressway-C through the shared internal
                              		firewall context. Communication between Expressway-C and Expressway-E is
                              		through the ASA, which provides the NAT and firewall functions. The
                              		Expressway-C is peered with the session border controller (as a neighbor). For
                              		more information, see the Cisco Hosted Collaboration Solution Solution Reference Network Design Guide .

## Investigate
                        	 Storage Planning

Consider the
                              		  following for storage planning.

Determine
                                       			 capacity needs.

See Cisco Hosted Collaboration Solution Release 12.5 Capacity Planning Guide for more information about capacity.

Determine
                                       			 storage connectivity options such as such as FCOE (Fiber Channel over
                                       			 Ethernet), FC (Fiber Channel) or NAS. Micro Node deployments must use local
                                       			 storage.

Determine
                                       			 approved storage vendors for UCS with SAN or NAS.

See UCS
                                             				  Hardware and Software Interoperability Technical References at http://www.cisco.com/c/en/us/support/servers-unified-computing/unified-computing-system/products-technical-reference-list.html for details on approved
                                          				storage vendors for UCS with SAN or NAS.

Determine
                                       			 storage tier, either multi-tier or single tier.

Using tiers
                                          				lets you distribute capacity across multiple tiers. Larger deployments should
                                          				consider their capacity distribution carefully.

Consider storage raid array recommendations. For more details, see Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide for more details.

Determine LUN sizing. For more details, see Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide .

|  |
|---|

| Step 1 | Gather Data for Initial Data Center Planning . |
|---|---|
| Step 2 | Determine the Data Center Deployment Model . |
| Step 3 | Determine Details About Applications . |
| Step 4 | Identify the Various Networking Resources . |
| Step 5 | Determine Virtual Machine Distribution and Connectivity . |
| Step 6 | Determine DMZ Requirements . |
| Step 7 | Investigate Storage Planning . |

| Step 1 | Collect and
                                       			 estimate the type of tenants using detailed information about your system. You
                                       			 should have already done this as part of Complete Tenant Matrix . Gather
                                          				information about customers, customer average sizes, future growth, security
                                          				requirements, local versus central break out, regulatory requirements, and
                                          				access models. |
|---|---|
| Step 2 | Determine if
                                       			 there are any other services that are offered from the same data center as
                                       			 Cisco HCS. |
| Step 3 | Determine the
                                       			 locations and the number of data centers that you plan to deploy for Cisco HCS. Locations and
                                          				number of data centers are determined based on target market proximity
                                          				requirements, redundancy requirements, size, and access models. All of these
                                          				factors can affect your costs. For UC applications, for example, you should
                                          				determine whether all of your customers will have the same redundancy or
                                          				whether the redundancy is determined on a per-customer basis. |
| Step 4 | Determine
                                       			 whether you have a single or multiple data center setup. |
| Step 5 | Choose your
                                       			 site deployment type. Based on
                                       			 decisions made in Determine Your HCS Data Center Deployment Model , decide the type of
                                       			 site for your data center: Hosted Extender Remote
                                                					 managed Hosted
                                                					 Private Cloud/Large Enterprise |

| Step 1 | Examine key
                                       			 attributes to determine the data center deployment model: Number of
                                                   					 tenants Average
                                                   					 tenant size Total
                                                   					 dedicated UC instances Total
                                                   					 shared UC instances Total UC
                                                   					 instances and clusters Supported
                                                   					 applications |
|---|---|
| Step 2 | Use the data
                                       			 and capacity requirements to determine the data center deployment model across
                                       			 one or more data centers. |

| Step 1 | Determine
                                       			 whether the management applications will be NATted into a Customer Domain. |
|---|---|
| Step 2 | Review the Cisco Hosted Collaboration
                                             			 Solution Compatibility Matrix to determine the required application versions for the current release. For the most
                                          				recent compatibility information, see the compatibility matrix from the Cisco
                                          				HCS documentation page http://www.cisco.com/en/US/partner/products/ps11363/tsd_products_support_series_home.html |

| Note | When deploying
                                          		  Cisco HCS in the hosted environment, you must not have NAT
                                          		  between any end device (phone) and the Cisco Unified Communications Manager (UC
                                          		  application) on the line side, because some of the mid-call features may not
                                          		  function properly. However, when Over The Top access is supported (using
                                          		  Expressway, etc.), there can be NAT in front of the endpoint. It is also
                                          		  recommended that the HCS Management applications not be
                                          		  deployed within a NAT. Using NAT between the vCenter Server system and ESXi/ESX
                                          		  hosts is an unsupported configuration. For more details, see http://kb.vmware.com/kb/1010652 |
|---|---|

| Step 1 | Determine the virtual machine distribution. For more information on recommendations, refer to the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide . Oversubscribed clusters Nonoversubscribed clusters |
|---|---|
| Step 2 | Analyze the
                                       			 available bandwidth. Based on the
                                          				deployment model, estimate: The
                                                					 bandwidth needed between data centers. The
                                                					 aggregate bandwidth needed between the data center and CPEs. The
                                                					 aggregate bandwidth needed between the datacenter and PSTN network. |
| Step 3 | Determine the MPLS VPN peering arrangement between the Service Provider Cisco HCS Data Center and MPLS provider. |
| Step 4 | Determine
                                       			 whether to use Over-The-Top access or site-to-site VPN for remote access
                                       			 through the Internet. |

| Step 1 | Determine
                                       			 capacity needs. See Cisco Hosted Collaboration Solution Release 12.5 Capacity Planning Guide for more information about capacity. |
|---|---|
| Step 2 | Determine
                                       			 storage connectivity options such as such as FCOE (Fiber Channel over
                                       			 Ethernet), FC (Fiber Channel) or NAS. Micro Node deployments must use local
                                       			 storage. Important There is no shared storage array switch interoperability
                                                   				requirement for a Micro Node deployment. Micro Node leverages local
                                                   				Direct-attached storage (DAS) within the UCS C-series. Currently only UC on UCS
                                                   				Tested Reference Configuration servers are supported within HCS. Therefore, a
                                                   				shared storage array is not applicable for a Micro Node installation. A VMware
                                                   				Virtual SAN (VSAN), software-defined shared storage using the local DAS within
                                                   				the C-Series server for virtual machines, is not a supported deployment model
                                                   				and should not be implemented. | Important | There is no shared storage array switch interoperability
                                                   				requirement for a Micro Node deployment. Micro Node leverages local
                                                   				Direct-attached storage (DAS) within the UCS C-series. Currently only UC on UCS
                                                   				Tested Reference Configuration servers are supported within HCS. Therefore, a
                                                   				shared storage array is not applicable for a Micro Node installation. A VMware
                                                   				Virtual SAN (VSAN), software-defined shared storage using the local DAS within
                                                   				the C-Series server for virtual machines, is not a supported deployment model
                                                   				and should not be implemented. |
| Important | There is no shared storage array switch interoperability
                                                   				requirement for a Micro Node deployment. Micro Node leverages local
                                                   				Direct-attached storage (DAS) within the UCS C-series. Currently only UC on UCS
                                                   				Tested Reference Configuration servers are supported within HCS. Therefore, a
                                                   				shared storage array is not applicable for a Micro Node installation. A VMware
                                                   				Virtual SAN (VSAN), software-defined shared storage using the local DAS within
                                                   				the C-Series server for virtual machines, is not a supported deployment model
                                                   				and should not be implemented. |
| Step 3 | Determine
                                       			 approved storage vendors for UCS with SAN or NAS. See UCS
                                             				  Hardware and Software Interoperability Technical References at http://www.cisco.com/c/en/us/support/servers-unified-computing/unified-computing-system/products-technical-reference-list.html for details on approved
                                          				storage vendors for UCS with SAN or NAS. |
| Step 4 | Determine
                                       			 storage tier, either multi-tier or single tier. Using tiers
                                          				lets you distribute capacity across multiple tiers. Larger deployments should
                                          				consider their capacity distribution carefully. |
| Step 5 | Consider storage raid array recommendations. For more details, see Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide for more details. |
| Step 6 | Determine LUN sizing. For more details, see Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide . |

| Important | There is no shared storage array switch interoperability
                                                   				requirement for a Micro Node deployment. Micro Node leverages local
                                                   				Direct-attached storage (DAS) within the UCS C-series. Currently only UC on UCS
                                                   				Tested Reference Configuration servers are supported within HCS. Therefore, a
                                                   				shared storage array is not applicable for a Micro Node installation. A VMware
                                                   				Virtual SAN (VSAN), software-defined shared storage using the local DAS within
                                                   				the C-Series server for virtual machines, is not a supported deployment model
                                                   				and should not be implemented. |
|---|---|