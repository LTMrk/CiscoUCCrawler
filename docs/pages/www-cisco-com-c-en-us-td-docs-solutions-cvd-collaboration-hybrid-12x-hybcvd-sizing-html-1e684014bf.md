---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-hybrid-12x-hybcvd-sizing-html-1e684014bf
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/hybrid/12x/hybcvd/sizing.html
retrieved_at: 2026-08-16T18:25:41.963915+00:00
---

Preferred Architecture for Cisco Webex Hybrid Services, CVD

# Preferred Architecture for Cisco Webex Hybrid Services, CVD

Updated: December 21, 2017

Chapter: Sizing Cisco Webex Hybrid Services

## Chapter: Sizing Cisco Webex Hybrid Services

## Sizing Cisco Webex Hybrid Services

Revised: May 31, 2019

Sizing the components of the Preferred Architecture for Cisco Webex Hybrid Services is an important part of the overall solution design. As in the latest version of the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments , this chapter contains simplified sizing recommendations based on a number of assumptions. It is important to note that the assumptions in this chapter change some of the simplified sizing assumptions for the on-premises deployment. Therefore, it is important to be aware of these changes in order to size the on-premises deployment correctly.

For products deployed with virtualization, sizing corresponds to the selection of the virtual machine (VM) hardware specification defined in the VM configuration or Open Virtual Archive (OVA) template and the number of virtual machines. For the products that are not deployed with virtualization, sizing corresponds to the type and number of appliances or blades.

Sizing can be a complex exercise because of numerous parameters to take into considerations. To simplify the sizing exercise, this chapter provides some sizing examples with corresponding assumptions. We refer to these sizing examples as simplified sizing deployments. If the requirements for your particular deployment are within the limits of those assumptions, then you can use the simplified sizing deployments in this document as a reference. If not, then you will need to perform the normal sizing calculations as described in the Sizing chapter in the latest version of the Cisco Collaboration System Solution Reference Network Design (SRND) guide and related product documentation available at https://www.cisco.com/go/srnd.

As mentioned, sizing the components of the Preferred Architecture for Webex Hybrid Services is very similar to that of the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments . One main difference is the addition of the Webex Hybrid Services Connectors and Video Mesh Nodes. The Cisco Expressway-C and Expressway-E pairs in this chapter are sized to handle Webex Hybrid Services. The other main difference is that the average busy hour call attempts (BHCA) is assumed to be 3; average BHCA below 3 fits within these recommendations, but average BHCA over 3 would require the sizing to be modified accordingly. The goal of this document is to provide simplified sizing guidance for those components.

For a given deployment, the goal of the sizing process is to determine:

- The type of platform to use

- The specifications and number of instances to deploy for each Cisco Collaboration product

## Cisco Unified CM Sizing

For the most part, the sizing of Cisco Unified Communications Manager (Unified CM) for Webex Hybrid Services does not change compared to the sizing of Unified CM in the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments. The main differences are:

- The Jabber clients are replaced with Webex Teams applications.

- The sizing assumes that each user has 2 devices: one Webex Teams application and one SIP endpoint.

- The average BHCA is 3.

Other than the differences mentioned above, all other assumptions for the sizing of the on-premises deployment remain unchanged.

Table 7-1 and Figure 7-1 describe the simplified sizing deployments. For more details, refer to the latest version of the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments, CVD , available at https://www.cisco.com/go/pa .

Table 7-1 Cisco Unified CM Simplified Sizing Deployments

Up to 1,000 users (2,000 devices)

2 nodes (1k-user VM configuration on Cisco Business Edition 6000H):

- 1 primary node (publisher, TFTP, and call processing node)

- 1 backup node (TFTP and call processing node)

Up to 2,500 users (5,000 devices)

5 nodes (7.5k-user VM configuration):

- 1 publisher node

- 2 TFTP node

- 1 call processing pair (2 call processing subscriber nodes)

Up to 5,000 users (10,000 devices)

7 nodes (7.5k-user VM configuration):

- 1 publisher node

- 2 TFTP node

- 2 call processing pairs (4 call processing subscriber nodes)

Figure 7-1 Cisco Unified CM Simplified Sizing Deployments

## Webex Hybrid Services Connectors and Expressway Sizing

This section covers sizing Webex Hybrid Services connectors as well as the Expressway-C and Expressway-E sizing for Webex Hybrid Services. Expressway sizing with business-to-business and mobile and remote access (MRA) services is covered in the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments CVD .

With Webex Hybrid Services, the Calendar and Call connectors are hosted on the Expressway-C servers. The Expressway-C and Expressway-E pairs are used for firewall traversal for SIP endpoints connecting to Webex. This occurs when a SIP endpoint is involved in a point-to-point call with a Webex Teams application or Webex device, or in a conference overflow scenario where the Webex Video Mesh cluster is full and a new SIP endpoint joins the conference. The Expressway-C and Expressway-E pairs are also used for the Call Service Aware and Call Service Connect services.

For simplicity, this section covers sizing for deployments where the Expressway-C servers are deployed with co-resident hosting of all three call, calendar, and firewall traversal services. This section does not cover sizing for configurations where there is a dedicated Expressway-C server for the call or calendar hybrid services. Moreover, the large Expressway VM configuration is also not considered in this section because it is not supported on Cisco Business Edition 6000 or 7000. If you are interested in other deployment and co-residency options, or in deployments leveraging the large Expressway VM configuration because you have a large deployment, refer to the information on User Capacity Limits for Expressway-Based Hybrid Services available at https://collaborationhelp.cisco.com/article/en-us/nv5p67g .

Table 7-2 and Figure 7-2 provide sizing guidance, with some assumptions that are listed below. As mentioned above, this information assumes that the large VM configuration, which is not supported on Cisco BE6000 or BE7000, is not used.

Table 7-2 Sizing for the Cisco Expressway Servers

Up to 500

2 Expressway-C and 2 Expressway-E (includes redundancy)

Requires Expressway small VM configuration and Cisco BE6000

Up to 2,000

2 Expressway-C and 2 Expressway-E (includes redundancy)

Requires medium VM configuration and Cisco BE7000

Up to 4,000

4 Expressway-C and 4 Expressway-E (includes redundancy)

Expressway medium VM configuration (for Cisco BE7000)

Up to 6,000

6 Expressway-C and 6 Expressway-E (includes redundancy)

Expressway medium VM configuration (for Cisco BE7000)

Figure 7-2 Sizing for the Webex Hybrid Services Connectors and Cisco Expressway

Assumptions

The following assumptions apply to the information in Table 7-2 and Figure 7-2 .

- Microsoft Exchange is deployed on-premises.

- Mobile and remote access (MRA) and business-to-business services, if deployed, do not use the Expressway servers.

- Each user has 2 devices: one desk phone registered to Cisco Unified CM and one Webex Teams application.

- Each user makes an average of 3 busy hour call attempts (BHCA), with an average call hold time of 3 minutes.

- 50% of calls are on-network, 25% of calls are outgoing to the PSTN, and 25% of calls are incoming from the PSTN.

- The number of concurrent video calls and audio-only calls per Expressway server does not exceed the numbers in Table 7-3 . In this table, the weight of video calls is effectively twice the weight of audio calls. For example, with a mix of audio and video calls, if there are 50 video calls, then the remaining capacity for the audio calls is 100 audio calls. Note that this is not something that can be controlled, but it is a function of user calling, and it is important to understand for capacity considerations and for determining when more resources are necessary.

Table 7-3 Expressway Server Call Capacity

Virtual machine with small or medium VM configuration or Cisco Expressway CE1100 Appliance with 1 Gb small form-factor pluggable (SFP) transceivers

100

200

## Directory Connector Sizing

The Directory Connector is installed on a dedicated Windows Server and requires 8 GB of RAM. One CPU or vCPU is sufficient. For redundancy purposes, we recommend deploying two servers. For more details, refer to the latest version of the Deployment Guide for Cisco Directory Connector , available at

https://www.cisco.com/c/en/us/support/unified-communications/spark/products-installation-guides-list.html

## Video Mesh Node Sizing

Webex Teams applications, Webex Teams endpoints, and SIP endpoints can connect to a local Webex Video Mesh Node during a conference, as described in the chapter on Cisco Webex Video Mesh . The sizing of the Video Mesh Nodes depends on the number of simultaneous calls going through the Video Mesh Nodes, the type of endpoints joining the conference, the video resolution on those endpoints, and the platform used for the Video Mesh Nodes.

For more information and for actual capacity limits, refer to the latest version of the Deployment Guide for Cisco Webex Video Mesh , available at

https://www.cisco.com/c/en/us/support/unified-communications/spark/products-installation-guides-list.html

When deploying Webex Video Mesh Nodes, we recommend monitoring the usage on those nodes via the Webex Control Hub. If more capacity is needed, you can add Video Mesh Nodes to the Webex Video Mesh cluster. Adding nodes to a cluster not only increases the capacity but also provides redundancy in case a single node becomes unavailable for any reason. There is no maximum limit to the number of nodes in a Video Mesh cluster.

As described in the chapter on Cisco Webex Video Mesh , if the Webex Video Mesh cluster becomes full, the meeting will cascade to the Webex cloud media services to handle the overflow. When this happens, Webex Teams applications and Webex devices joining the meeting will connect directly to the cloud, while SIP endpoints joining the meeting will connect to the cloud via an Expressway-C and Expressway-E pair. Again, monitor your system to understand how often this occurs and if this is acceptable to your users. If you want to reduce those occurrences of cascade links, add more Video Mesh Nodes as needed.

## Virtual Machine Placement and Platforms

The virtual machine placement for this solution is similar to the one for the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments. The main differences are:

- Deployment of Windows Servers for Cisco Directory Connector, and Expressway-C Connector Hosts for Cisco Calendar and Call Connector nodes

- Deployment of Expressway-C and Expressway-E nodes that handle Webex Hybrid Services calls

- Deployment of Webex Video Mesh Nodes on Cisco Meeting Server 1000

The virtual machine placement process is performed with the Collaboration Virtual Machine Placement Tool (VMPT), which requires a cisco.com login account and which is available at https://www.cisco.com/go/vmpt .

Figure 7-3 shows an example of using the VMPT for a deployment with 4,000 users and 8,000 endpoints (including 4,000 hardware endpoints and 4,000 Webex Teams applications). This example assumes that Cisco Business Edition 7000M is deployed. It does not show the Cisco Video Mesh Nodes, which would be deployed on the Cisco Meeting Server 1000 platform for this example.

Figure 7-3 Virtual Machine Placement Example Using the VMPT

| Deployment Size | Cisco Unified CM Nodes to be Deployed |
|---|---|
| Up to 1,000 users (2,000 devices) | 2 nodes (1k-user VM configuration on Cisco Business Edition 6000H): 1 primary node (publisher, TFTP, and call processing node) 1 backup node (TFTP and call processing node) |
| Up to 2,500 users (5,000 devices) | 5 nodes (7.5k-user VM configuration): 1 publisher node 2 TFTP node 1 call processing pair (2 call processing subscriber nodes) |
| Up to 5,000 users (10,000 devices) | 7 nodes (7.5k-user VM configuration): 1 publisher node 2 TFTP node 2 call processing pairs (4 call processing subscriber nodes) |

| Number of Users | Expressway-C and Expressway-E for Calendar, Call, and Firewall Traversal | Notes |
|---|---|---|
| Up to 500 | 2 Expressway-C and 2 Expressway-E (includes redundancy) | Requires Expressway small VM configuration and Cisco BE6000 |
| Up to 2,000 | 2 Expressway-C and 2 Expressway-E (includes redundancy) | Requires medium VM configuration and Cisco BE7000 |
| Up to 4,000 | 4 Expressway-C and 4 Expressway-E (includes redundancy) | Expressway medium VM configuration (for Cisco BE7000) |
| Up to 6,000 | 6 Expressway-C and 6 Expressway-E (includes redundancy) | Expressway medium VM configuration (for Cisco BE7000) |

| VM Configuration Template | Video Calls Capacity per Node | Audio-Only Calls Capacity per Node |
|---|---|---|
| Virtual machine with small or medium VM configuration or Cisco Expressway CE1100 Appliance with 1 Gb small form-factor pluggable (SFP) transceivers | 100 | 200 |