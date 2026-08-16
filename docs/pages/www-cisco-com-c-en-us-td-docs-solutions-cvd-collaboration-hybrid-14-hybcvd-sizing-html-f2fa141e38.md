---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-hybrid-14-hybcvd-sizing-html-f2fa141e38
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/hybrid/14/hybcvd/sizing.html
retrieved_at: 2026-08-16T18:24:03.322478+00:00
---

Preferred Architecture for Cisco Webex Hybrid Services, CVD

# Preferred Architecture for Cisco Webex Hybrid Services, CVD

Updated: April 27, 2020

Chapter: Sizing Cisco Webex Hybrid Services

## Chapter: Sizing Cisco Webex Hybrid Services

## Sizing Cisco Webex Hybrid Services

Revised: October 22, 2021

Sizing the components of the Preferred Architecture for Webex Hybrid Services is an important part of the overall solution design. As in the latest version of the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments , this chapter contains simplified sizing recommendations based on several assumptions. It is important to note that the assumptions in this chapter change some of the simplified sizing assumptions for the on-premises deployment. Therefore, it is important to be aware of these changes in order to size the on-premises deployment correctly.

For products deployed with virtualization, sizing corresponds to the selection of the virtual machine (VM) hardware specification defined in the VM configuration or Open Virtual Archive (OVA) template and the number of virtual machines. For the products that are not deployed with virtualization, sizing corresponds to the type and number of appliances or blades.

Sizing can be a complex exercise because of numerous parameters to take into considerations. To simplify the sizing exercise, this chapter provides some sizing examples with corresponding assumptions. We refer to these sizing examples as simplified sizing deployments. If the requirements for your particular deployment are within the limits of those assumptions, then you can use the simplified sizing deployments in this document as a reference. If not, then you will need to perform the normal sizing calculations as described in the latest version of the Collaboration Sizing Guide available at https://www.cisco.com/go/srnd.

As mentioned, sizing the components of the Preferred Architecture for Webex Hybrid Services is very similar to that of the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments . One main difference is the addition of the Webex Hybrid Services Connectors and Video Mesh Nodes. The Cisco Expressway-C and Expressway-E pairs in this chapter are sized to handle Webex Hybrid Services. The goal of this document is to provide simplified sizing guidance for those components.

For a given deployment, the goal of the sizing process is to determine:

- The type of platform to use

- The specifications and number of instances to deploy for each Cisco Collaboration product

## Cisco Unified CM Sizing

For the most part, the sizing of Cisco Unified Communications Manager (Unified CM) for Webex Hybrid Services does not change compared to the sizing of Unified CM in the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments. The main differences are:

- The Jabber clients are replaced with the Webex App.

- The sizing assumes that each user has 2 devices: one Webex App and one SIP endpoint.

- The average BHCA is 4.

Other than the differences mentioned above, all other assumptions for the sizing of the on-premises deployment remain unchanged.

Table 5-1 and Figure 5-1 describe the simplified sizing deployments. For more details, refer to the latest version of the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments, CVD , available at https://www.cisco.com/go/pa .

Table 5-1 Cisco Unified CM Simplified Sizing Deployments

Up to 2,500 users (5,000 devices)

5 nodes (Medium OVA VM configuration):

- 1 publisher node

- 2 TFTP node

- 1 call processing pair (2 call processing subscriber nodes)

Up to 5,000 users (10,000 devices)

7 nodes (Medium OVA VM configuration):

- 1 publisher node

- 2 TFTP node

- 2 call processing pairs (4 call processing subscriber nodes)

Figure 5-1 Cisco Unified CM Simplified Sizing Deployments

## Expressway Sizing

This section covers Expressway-C and Expressway-E sizing for Webex Hybrid Services. The sizing is very similar to the Expressway sizing covered in the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments CVD with business-to-business and mobile and remote access (MRA) services and the capacity limits are the same. For example, similarly to the hardware endpoints and Jabber in the enterprise on-premises deployment, the hardware endpoints and Webex App in the Hybrid Services deployment register to Unified CM when they are inside the corporate network. When they are outside the corporate network over the Internet they need to be counted as MRA devices in the Expressway sizing.

In the Hybrid Services Preferred Architecture the Webex Room devices may be registered to Unified CM or to the Webex cloud. If a Webex Room device is registered to Webex, it needs to be counted as a B2B device when it is engaged in a point-to-point call with an on-premises endpoint and the call needs to be counted against the maximum number of concurrent audio or video calls. Similarly, it also needs to be counted as a B2B device when it is in a call through the PSTN.

The Webex Video Mesh nodes do not use Expressway when they connect to the Webex cloud. Therefore, when Unified CM-registered endpoints connect to a Webex conference call through the Video Mesh, there is no impact on Expressway unless the Video Mesh node becomes full and the endpoints bypass the Video Mesh node, connecting to Webex through Expressway. In that case, each endpoint connecting to the Webex cloud, going through Expressway, would need to be counted as a B2B device in the Expressway sizing.

## Webex Hybrid Services Connectors

This section covers sizing for the Webex Hybrid Services connectors. Expressway sizing with business-to-business and mobile and remote access (MRA) services is covered in the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments CVD .

The Hybrid Calendar Connector runs on an Expressway-C server. It is recommended to deploy a dedicated Expressway-C for the Hybrid Calendar connector as well as another node for redundancy. A small OVA can support up to 5,000 users. In cases where the enterprise calendar is fully cloud-based, the on-premises Cloud Connector and therefore the Expressway-C Connector Host servers are not required.

The Directory Hybrid Connector runs on a dedicated Microsoft Windows server and requires 8 GB of RAM. One CPU or vCPU is sufficient. Two servers are recommended for redundancy.

## Virtual Machine Placement and Platforms

The virtual machine placement for this solution is similar to the one for the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments. The main differences are:

- Deployment of Windows Servers for Cisco Directory Connector, and Expressway-C Connector Hosts for Cisco Hybrid Calendar.

- Deployment of Webex Video Mesh Nodes on Cisco Meeting Server 1000.

The virtual machine placement process is performed with the Quote Collab tool, which requires a cisco.com login account and is available at https://www.cqc.cloudapps.cisco.com/ .

Figure 5-2 shows an example of a server diagram from the Quote Collab tool for a deployment with 2,500 users and 5,000 endpoints (including 2,500 hardware endpoints and 2,500 Webex App). This example assumes that Cisco Business Edition 7000M is deployed. It does not show the Cisco Video Mesh Nodes, which would be deployed on the Cisco Meeting Server 1000 platform for this example.

Figure 5-2 Virtual Machine Placement Example Using Quote Collab

Note To better summarize the overall VM requirements and placement for this simplified sizing example in Figure 7-2 the Expressway-E VMs have been included on the same set of BE7000 servers as all the other VMs. In a production deployment the Expressway-E VMs would instead reside on separate host servers in the DMZ (BE7000 or other hardware). Likewise, if enterprise calendar is fully cloud-based, then Expressway-C Connector Host VMs for on-premises Calendar Connector are not required.

| Deployment Size | Cisco Unified CM Nodes to be Deployed |
|---|---|
| Up to 2,500 users (5,000 devices) | 5 nodes (Medium OVA VM configuration): 1 publisher node 2 TFTP node 1 call processing pair (2 call processing subscriber nodes) |
| Up to 5,000 users (10,000 devices) | 7 nodes (Medium OVA VM configuration): 1 publisher node 2 TFTP node 2 call processing pairs (4 call processing subscriber nodes) |