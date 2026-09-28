---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-design-guide-new-html-ind-ba36fd8913
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/design/guide_new/html/index/Cisco-UCCX-in-HCS-UCCX-12-5-1-SU1.html
retrieved_at: 2026-08-16T21:06:03.973312+00:00
---

Solution Design Guide for Cisco Unified Contact Center Express Release 12-5-1 SU1

# Solution Design Guide for Cisco Unified Contact Center Express Release 12-5-1 SU1

Updated: January 16, 2024

Chapter: Cisco UCCX in HCS UCCX 12.5(1) SU1

## Chapter: Cisco UCCX in HCS UCCX 12.5(1) SU1

## Overview

The Cisco Hosted Collaboration Solution (HCS) enables service providers to offer managed and hosted Unified Communications (UC) and collaboration services to multiple autonomous business customers by hosting UC applications. Using this solution, service providers can manage and deploy new highly reliable and scalable collaboration services to small- or medium-sized businesses and enterprises. This capability allows a service provider to offer differentiated services.

The following sections detail the various deployment models, bandwidth requirements and limitations if any for HCS.

The HCS deployment of Unified CCX is combination of HCS-Unified CM deployment and HCS-Unified CCX deployment. Thus, the bandwidth and security considerations are a combination of both these types of deployments. These are as per the values tabulated in the Bandwidth, Latency, and QoS Considerations section. Thus for example, the total bandwidth that need to be provisioned is sum of bandwidth that need to be provisioned for Unified CM/IP Telephony and Unified CCX.

## Hosted Unified CCX Deployment

Dependent Cisco HCS elements

Cisco Unified Communications Manager and other related components

Deploy a Single node of Unified CCX

Deploy the two nodes of Unified CCX in the same data center in High Availability (HA) over LAN model (Software Redundancy only available)

Deploy the two nodes of Unified CCX in two different geographical locations in HA over WAN model (Software Redundancy and Network Redundancy available)

The HA over WAN deployment model is shown in the following illustration.

Figure 1. Hosted Unified CCX Deployment in Cisco HCS

1

2

Maximum Latency (RTT)

80 milli seconds

Minimum Assured Bandwidth

See, Cisco Unified Contact Center Express Bandwidth Calculator

Maximum Latency (RTT)

80 milli seconds

Minimum Assured Bandwidth

10 Mbps (This value is valid for a contact center's day to day operations only. This does not include the bandwidth required for other operations like, upgrades, backups or file transfers.)

All bandwidth and latency calculations mentioned here for Hosted Collaboration deployment over ride any other values mentioned elsewhere in this document.

The following table outlines the various Unified CCX solution components and their supported deployment location.

IP Telephony

Finesse IP Phone Agent (Finesse IPPA)

Outbound IVR - Progressive and Predictive Campaigns

Agent IVR - Progressive and Predictive Campaigns

SMTP integration with Unified CCX including for sending email using a Unified CCX script, for sending email updates regarding an update, and for Cisco Unified Intelligence Center scheduled reports.

MS Exchange Server/Office 365/ Gmail

For Finesse email.

Customer Premise (MS Exchange), Office 365, Gmail

Automatic Speech Recognition and Text-to-Speech

Third-Party Wallboard Application

Finesse Chat and Email

For Single Sign-On

In a Single Sign-On enabled environment, to use a hosted Identity Provider (IdP) that is federated to the Enterprise IdP see, https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/200612-Configure-the-Identity-Provider-for-UCCX.html .

Unified CM cluster can not be shared across multiple Unified CCX.

Every customer must have one dedicated instance of Unified CCX as multi-tenancy is not supported.

Workforce Optimization solutions for deployment in an HCS environment are provided by Cisco Solutions Plus partners.

Creation of CTI Port

Creation of Trigger

Finesse IPPA login

The number or partitions and calling search spaces on Unified CM doesn't impact Unified CCX. Ensure that the agent phones and the CTI ports belong to the same calling search space to enable consult transfer from CTI port to agent phone.

The SFTP location used as backup device must be located in the service provider network locally.

## Bandwidth and Latency Considerations

For bandwidth and latency requirements see section in the guide. For email and chat depending on the location of the email server (Cloud based Gmail/Office 365 or MS Exchange server at customer premises), the bandwidth must be provisioned as per the Unified CCX Bandwidth Calculator . The clients described in the bandwidth calculator are located in the customer premises in an HCS deployment. The contact center in the data center is in the service provider network in an HCS deployment.

In addition to HCS-Unified CM bandwidth provisioning, that is between phone-phone (internal or external call) additional bandwidth must be provisioned for IVR streaming from Unified CCX to customer phone depending on the type of breakout.

In case of Ingress Local Breakout the bandwidth required for IVR streaming from service provider to customer premises must be provisioned in addition to Unified CM provisioning (similar to Music on Hold (MoH)).

In case of Ingress Central Breakout there is no extra provisioning of bandwidth required for IVR streaming as IVR is directly streamed from service provider to the user.

## Security Considerations

The following section details the firewall rules and other external system requirements.

The connectivity from the customer premises to service provider is a VPN where all ports are enabled without any restrictions, the same conditions listed in the Solution Port Utilization for Unified CCX guide are applicable here. See the Port Utilization Guide for Cisco Unified Contact Center Express Solution at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html for information on the ports that must be used for this deployment.

For external interactions from the contact center, the edge firewall must be configured to allow the network traffic.

1 The colored lines are used to denote the different connections between the Unified CCX solution components in the hosted environment.

2 The dotted lines indicate the connections to the standby Unified CCX and Unified CM sever.

| Maximum Latency (RTT) | 80 milli seconds |
|---|---|
| Minimum Assured Bandwidth | See, Cisco Unified Contact Center Express Bandwidth Calculator |

| Maximum Latency (RTT) | 80 milli seconds |
|---|---|
| Minimum Assured Bandwidth | 10 Mbps (This value is valid for a contact center's day to day operations only. This does not include the bandwidth required for other operations like, upgrades, backups or file transfers.) |

| Note | All bandwidth and latency calculations mentioned here for Hosted Collaboration deployment over ride any other values mentioned elsewhere in this document. |
|---|---|

| Unified CCX Solution Element | Functionality | Deployment Location |
|---|---|---|
| Agent phones | IP Telephony Finesse IP Phone Agent (Finesse IPPA) | Customer premises |
| SIP Gateway for Outbound Campaigns | Outbound IVR - Progressive and Predictive Campaigns Agent IVR - Progressive and Predictive Campaigns | Hosted |
| Microsoft Exchange Server | SMTP integration with Unified CCX including for sending email using a Unified CCX script, for sending email updates regarding an update, and for Cisco Unified Intelligence Center scheduled reports. | Customer premises |
| MS Exchange Server/Office 365/ Gmail | For Finesse email. | Customer Premise (MS Exchange), Office 365, Gmail |
| ASR/TTS Servers | Automatic Speech Recognition and Text-to-Speech | Hosted |
| Wallboard Server | Third-Party Wallboard Application | Customer premises |
| Cisco Customer Collaboration Platform | Finesse Chat and Email | Hosted in DMZ |
| Enterprise Identity Provider (IdP) | For Single Sign-On | Customer premises |

| Note | In a Single Sign-On enabled environment, to use a hosted Identity Provider (IdP) that is federated to the Enterprise IdP see, https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/200612-Configure-the-Identity-Provider-for-UCCX.html . Unified CM cluster can not be shared across multiple Unified CCX. Every customer must have one dedicated instance of Unified CCX as multi-tenancy is not supported. Workforce Optimization solutions for deployment in an HCS environment are provided by Cisco Solutions Plus partners. In an HA over WAN deployment a few of the configurations done in Unified CCX Administration on the secondary node may take longer time: Creation of CTI Port Creation of Trigger Finesse IPPA login The number or partitions and calling search spaces on Unified CM doesn't impact Unified CCX. Ensure that the agent phones and the CTI ports belong to the same calling search space to enable consult transfer from CTI port to agent phone. The SFTP location used as backup device must be located in the service provider network locally. |
|---|---|