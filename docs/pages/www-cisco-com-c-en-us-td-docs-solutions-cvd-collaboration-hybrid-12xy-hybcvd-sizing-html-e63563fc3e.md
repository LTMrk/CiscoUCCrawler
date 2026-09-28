---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-hybrid-12xy-hybcvd-sizing-html-e63563fc3e
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/hybrid/12xy/hybcvd/sizing.html
retrieved_at: 2026-08-16T18:26:18.004342+00:00
---

Preferred Architecture for Cisco Webex Hybrid Services, CVD

# Preferred Architecture for Cisco Webex Hybrid Services, CVD

Updated: April 27, 2020

Chapter: Sizing Cisco Webex Hybrid Services

## Chapter: Sizing Cisco Webex Hybrid Services

## Sizing Cisco Webex Hybrid Services

Revised: November 7, 2019

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

## Expressway Sizing

This section covers Expressway-C and Expressway-E sizing for Webex Hybrid Services. The sizing is very similar to the Expressway sizing covered in the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments CVD with business-to-business and mobile and remote access (MRA) services and the capacity limits are the same. For example, similarly to the hardware endpoints and Jabber in the Enterprise On-Premises deployment, the hardware endpoints and Webex Teams application in the Hybrid Services deployment register to Unified CM when they are inside the corporate network. When they are outside the corporate network over the Internet they need to be counted as MRA devices in the Expressway sizing.

In the Hybrid Services Preferred Architecture the Cisco Webex Room devices could be registered to Unified CM or to the Webex cloud. If a Cisco Webex Room is registered to Cisco Webex Cloud, it needs to be counted as a B2B device when it is engaged in a point-to-point call with an on-premises endpoint and the call needs to be counted against the maximum number of concurrent audio or video calls. Similarly, it also needs to be counted as a B2B device when it is in a call through the PSTN.

The Webex Video Mesh nodes do not use Expressway when they connect to the Webex cloud. Therefore when Unified CM-registered endpoints connect to a Webex conference call through the Video Mesh, there is no impact on Expressway unless the Video Mesh node becomes full and the endpoints bypass the Video Mesh node, connecting to Cisco Webex through Expressway. In that case, each endpoint connecting to the Webex cloud, going through Expressway, would need to be counted as a B2B device in the Expressway sizing.

## Webex Hybrid Services Connectors

This section covers sizing for the Webex Hybrid Services connectors. Expressway sizing with business-to-business and mobile and remote access (MRA) services is covered in the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments CVD .

The Calendar Hybrid Connector runs on an Expressway-C server. It is recommended to deploy a dedicated Expressway-C for the Hybrid Calendar connector as well as another node for redundancy. A small OVA can support up to 5,000 users.

The Directory Hybrid Connector runs on a dedicated Microsoft Windows server and requires 8 GB of RAM. One CPU or vCPU is sufficient. Two servers are recommended for redundancy.

## Video Mesh Node Sizing

Webex Teams applications, Webex Teams endpoints, and SIP endpoints can connect to a local Webex Video Mesh Node during a conference, as described in the chapter on Cisco Webex Video Mesh . The sizing of the Video Mesh Nodes depends on the number of simultaneous calls going through the Video Mesh Nodes, the type of endpoints joining the conference, the video resolution on those endpoints, and the platform used for the Video Mesh Nodes.

For more information and for actual capacity limits, refer to the latest version of the Deployment Guide for Cisco Webex Video Mesh , available at

https://www.cisco.com/c/en/us/support/unified-communications/spark/products-installation-guides-list.html

When deploying Webex Video Mesh Nodes, we recommend monitoring the usage on those nodes via the Webex Control Hub. If more capacity is needed, you can add Video Mesh Nodes to the Webex Video Mesh cluster. Adding nodes to a cluster not only increases the capacity but also provides redundancy in case a single node becomes unavailable for any reason. There is no maximum limit to the number of nodes in a Video Mesh cluster.

As described in the chapter on Cisco Webex Video Mesh , if the Webex Video Mesh cluster becomes full, the meeting will cascade to the Webex cloud media services to handle the overflow. When this happens, Webex Teams applications and Webex devices joining the meeting will connect directly to the cloud, while SIP endpoints joining the meeting will connect to the cloud via an Expressway-C and Expressway-E pair. Again, monitor your system to understand how often this occurs and if this is acceptable to your users. If you want to reduce those occurrences of cascade links, add more Video Mesh Nodes as needed.

## Virtual Machine Placement and Platforms

The virtual machine placement for this solution is similar to the one for the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments. The main differences are:

- Deployment of Windows Servers for Cisco Directory Connector, and Expressway-C Connector Hosts for Cisco Hybrid Calendar.

- Deployment of Webex Video Mesh Nodes on Cisco Meeting Server 1000.

The virtual machine placement process is performed with the Collaboration Virtual Machine Placement Tool (VMPT), which requires a cisco.com login account and which is available at https://www.cisco.com/go/vmpt .

Figure 7-2 shows an example of using the VMPT for a deployment with 5,000 users and 10,000 endpoints (including 5,000 hardware endpoints and 5,000 Webex Teams applications). This example assumes that Cisco Business Edition 7000M is deployed. It does not show the Cisco Video Mesh Nodes, which would be deployed on the Cisco Meeting Server 1000 platform for this example.

Figure 7-2 Virtual Machine Placement Example Using the VMPT

| Deployment Size | Cisco Unified CM Nodes to be Deployed |
|---|---|
| Up to 1,000 users (2,000 devices) | 2 nodes (1k-user VM configuration on Cisco Business Edition 6000H): 1 primary node (publisher, TFTP, and call processing node) 1 backup node (TFTP and call processing node) |
| Up to 2,500 users (5,000 devices) | 5 nodes (7.5k-user VM configuration): 1 publisher node 2 TFTP node 1 call processing pair (2 call processing subscriber nodes) |
| Up to 5,000 users (10,000 devices) | 7 nodes (7.5k-user VM configuration): 1 publisher node 2 TFTP node 2 call processing pairs (4 call processing subscriber nodes) |