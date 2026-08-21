---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-solution-design-guide-hcscc-b-sold-6f9c672cc7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Solution_Design_Guide/hcscc_b_soldg-for-hcs-cc-12_5/hcscc_b_soldg-for-hcs-cc-12_5_chapter_01100.html
retrieved_at: 2026-08-21T23:55:00.686087+00:00
---

Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

# Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

Updated: February 16, 2020

Chapter: Small Contact Center Agent Deployment Model

## Chapter: Small Contact Center Agent Deployment Model

- Small Contact Center Agent Deployment Model

- Small Contact Center Deployment Considerations

# Small Contact Center Agent Deployment Model

## Small Contact Center Deployment

The Small Contact Center (SCC) deployment model splits your contact center into shared and dedicated components. It provides
                           several options to serve specific customer needs. You provision the Central Controller and other core components in the shared
                           layer. You can deploy the customer peripherals as either customer-dedicated or as shared. The SCC supports both dedicated
                           and shared peripherals being used on a single instance, subject to aggregate solution capacity limits:

Dedicated components sub-customer option – Dedicated Cisco Unified CM, Peripheral Gateway, and Cisco Finesse sized for either 100 or 500 agents.

Shared components sub-customer option – Shared Cisco Unified CM, Peripheral Gateway, and Cisco Finesse support up to 2000 agents across 100 Department enabled
                                 sub-customers.

For Cisco Finesse installation to dedicated sub-customer instances, you can use a local DNS server or shared DNS. For more
                                             information, see the section on creating DNS servers for Cisco Finesse in SCC deployments in the Installing and Configuring Cisco HCS for Contact Center Guide .

The shared components sub-customer option can support 100 sub-customers on each Unified CM cluster and a maximum of 200 sub-customers
                                             per SCC. The 4000 Agents Reference Design uses a single Unified CM cluster for up to 4000 agents. Splitting this cluster in
                                             two requires application of the Oversubscription Resource Provisioning policy to account for the extra Unified CM Publisher
                                             VM.

### Small Contact Center Deployment Considerations

Components

Design Considerations

Unified Contact Center Domain Manager

Parameters moved to respective folders by administrator. System Configuration limits enforced at solution level, not at sub-customer
                                          level.

The service provider configures the Outbound configuration and administration for each sub-customer.

ISE users have these options:

CCDM domain users

CCE domain users

Sub-customer domain users

Single Sign-On does not support ISE users.

Cisco Unified Communications Domain Manager

In Network > Contact Center Server , add a dummy CVP Server for each sub-customer. Associate the same CVP server in the sub-customer hardware group.

Agent Extension across sub-customer must be unique. Overlapping of agent extension or dial plan is not supported. Example:
                                          If sub_cust1 uses 801xxxxxx extension, sub_cust2 cannot use the same extension.

Each sub-customer must have a unique internal help desk number.

Session Border Controller

This SBC provides for SIP signaling and media aggregation ingress and egress to the PSTN.

For more details on the aggregation SBC, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/11_5/HCS_Solution/Flexibility/chcs_b_hcs-115-flexibility-guide.html .

ASA/NAT

All data traffic to and from sub-customers passes through the ASA. The ASA uses NAT for dedicated sub-customers with overlapping
                                          IP subnets.

ASA is required for shared and dedicated sub-customers. Do not enable SIP ALG in ASA.

Cisco Prime Collaboration Assurance

Static mapping of internal IP to an external IP is required for Prime to work with SCC.

Microsoft Active Directory

Used for SCC administration, and hosted or customer domain (through trust) for AD user authentication.

Microsoft AD FS 2012 R2

Required for Single Sign-On. Provides for hosted domain or federated trust to customer IdPs for user authentication.

Components

Design Considerations

Unified CCE Router

Logger

System Configuration limits enforced at solution level, not at sub-customer level.

AW-HDS-DDS

VRU Peripheral Gateways

Unified CVP Call Server

Dialed number patterns across sub-customers must be unique. Example: If sub_cust1 uses 801xxxxxx dial number pattern, sub_cust2
                                          cannot use the same dial number pattern.

CVP Reporting Server

Use Exony VIM for multi tenant reporting.

Cisco Unified Intelligence Center

Unified Intelligence Center  is used for simple collections using the department ID of Unified CCE.  You can also use Exony
                                          VIM for multi-tenant reporting.

CUBE- Enterprise

In addition to standard comprehensive call treatment and survivability for the SCC deployment, the CUBE Enterprise multi-VRF
                                          feature is required to support SIP adjacency for the dedicated sub-customer PG option with overlapping IP subnets.

Components

Design Considerations

Cisco Unified CM

Dedicated sub-customer options require the use of Unified CM software-based resources, unless a dedicated gateway in the
                                          customer context provides the resources.

Peripheral Gateways

Follow any of these domain considerations to configure peripheral gateway:

PG can install on sub-customer domain. Both sub-customer domain and service provider (UCCE) domain instance number and name
                                                should be same.

Configure static NAT between UCCE domain and PG machine that is installed on service provider (UCCE) domain.

Cisco Finesse

Each dedicated sub-customer should have local DNS.

Components

Design considerations

Enterprise Chat and Email

Enterprise Chat and Email may be deployed per sub-customer, not exceeding 50 sub-customers.

Shared sub-customer Components option is not supported.

Do not enable a Media classes on the common outbound dial-peer. Create an Inbound Dial-peer for each sub-customer and enable
                                          the Media class there.

Shared sub-customer Components option is not supported.

SPAN Based Monitoring

Span from CUBE is supported for Mobile Agents.

Not supported for Shared components sub-customer option. Dedicated sub-customers can deploy Customer Collaboration Platform as dedicated within the customer context without Agent Request or callback.

Components

Design considerations

Agent Greeting

Whisper Announcement

Courtesy Call Back

Outbound Dialer

Maximum of 32 Dialers are supported and Maximum 4000 ports are supported.

There is no solution for sub-customers to manage outbound campaigns. Provide services or custom solutions to manage outbound
                                                      campaigns for each sub-customer.

Mobile Agents

A-law and mu-law support

Post Call Survey

Application Gateway

Not supported in  Small Contact Center.

Database Integration

ICM DB lookup is not supported.

Local Trunk PSTN Local Breakout

Local Trunk Location based CAC

Not supported for dedicated components sub-customer option.

Unified CM-based Silent Monitoring

Task Routing

The Task Routing API does not provide for multi-tenant interface to the SCC.

Precision Routing

Enabling Precision Routing on SCC limits the deployment to a maximum of 12 Agent PGs.

Single Sign-On

SCC uses a single IdS registered to the hosted AD FS 2012 R2 IdP for all customer authentication. All SSO Agents and Supervisor
                                          sign-in names must be in Email (UPN) format.

| Note | For Cisco Finesse installation to dedicated sub-customer instances, you can use a local DNS server or shared DNS. For more
                                             information, see the section on creating DNS servers for Cisco Finesse in SCC deployments in the Installing and Configuring Cisco HCS for Contact Center Guide . The shared components sub-customer option can support 100 sub-customers on each Unified CM cluster and a maximum of 200 sub-customers
                                             per SCC. The 4000 Agents Reference Design uses a single Unified CM cluster for up to 4000 agents. Splitting this cluster in
                                             two requires application of the Oversubscription Resource Provisioning policy to account for the extra Unified CM Publisher
                                             VM. |
|---|---|

| Components | Design Considerations |
|---|---|
| Unified Contact Center Domain Manager | Parameters moved to respective folders by administrator. System Configuration limits enforced at solution level, not at sub-customer
                                          level. The service provider configures the Outbound configuration and administration for each sub-customer. |
| ISE users have these options: CCDM domain users CCE domain users Sub-customer domain users Note Single Sign-On does not support ISE users. | Note | Single Sign-On does not support ISE users. |
| Note | Single Sign-On does not support ISE users. |
| Cisco Unified Communications Domain Manager | In Network > Contact Center Server , add a dummy CVP Server for each sub-customer. Associate the same CVP server in the sub-customer hardware group. |
| Agent Extension across sub-customer must be unique. Overlapping of agent extension or dial plan is not supported. Example:
                                          If sub_cust1 uses 801xxxxxx extension, sub_cust2 cannot use the same extension. |
| Each sub-customer must have a unique internal help desk number. |
| Session Border Controller | This SBC provides for SIP signaling and media aggregation ingress and egress to the PSTN. For more details on the aggregation SBC, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/11_5/HCS_Solution/Flexibility/chcs_b_hcs-115-flexibility-guide.html . |
| ASA/NAT | All data traffic to and from sub-customers passes through the ASA. The ASA uses NAT for dedicated sub-customers with overlapping
                                          IP subnets. ASA is required for shared and dedicated sub-customers. Do not enable SIP ALG in ASA. |
| Cisco Prime Collaboration Assurance | Static mapping of internal IP to an external IP is required for Prime to work with SCC. |
| Microsoft Active Directory | Used for SCC administration, and hosted or customer domain (through trust) for AD user authentication. |
| Microsoft AD FS 2012 R2 | Required for Single Sign-On. Provides for hosted domain or federated trust to customer IdPs for user authentication. |

| Note | Single Sign-On does not support ISE users. |
|---|---|

| Components | Design Considerations |
|---|---|
| Unified CCE Router |  |
| Logger | System Configuration limits enforced at solution level, not at sub-customer level. |
| AW-HDS-DDS |  |
| VRU Peripheral Gateways |  |
| Unified CVP Call Server | Dialed number patterns across sub-customers must be unique. Example: If sub_cust1 uses 801xxxxxx dial number pattern, sub_cust2
                                          cannot use the same dial number pattern. |
| CVP Reporting Server | Use Exony VIM for multi tenant reporting. |
| Cisco Unified Intelligence Center | Unified Intelligence Center  is used for simple collections using the department ID of Unified CCE.  You can also use Exony
                                          VIM for multi-tenant reporting. |
| CUBE- Enterprise | In addition to standard comprehensive call treatment and survivability for the SCC deployment, the CUBE Enterprise multi-VRF
                                          feature is required to support SIP adjacency for the dedicated sub-customer PG option with overlapping IP subnets. |

| Components | Design Considerations |
|---|---|
| Cisco Unified CM | Dedicated sub-customer options require the use of Unified CM software-based resources, unless a dedicated gateway in the
                                          customer context provides the resources. |
| Peripheral Gateways | Follow any of these domain considerations to configure peripheral gateway: PG can install on sub-customer domain. Both sub-customer domain and service provider (UCCE) domain instance number and name
                                                should be same. Configure static NAT between UCCE domain and PG machine that is installed on service provider (UCCE) domain. |
| Cisco Finesse | Each dedicated sub-customer should have local DNS. |

| Components | Design considerations |
|---|---|
| Enterprise Chat and Email | Enterprise Chat and Email may be deployed per sub-customer, not exceeding 50 sub-customers. Note Shared sub-customer Components option is not supported. | Note | Shared sub-customer Components option is not supported. |
| Note | Shared sub-customer Components option is not supported. |
| Do not enable a Media classes on the common outbound dial-peer. Create an Inbound Dial-peer for each sub-customer and enable
                                          the Media class there. Note Shared sub-customer Components option is not supported. | Note | Shared sub-customer Components option is not supported. |
| Note | Shared sub-customer Components option is not supported. |
| SPAN Based Monitoring | Span from CUBE is supported for Mobile Agents. |
| Customer Collaboration Platform | Not supported for Shared components sub-customer option. Dedicated sub-customers can deploy Customer Collaboration Platform as dedicated within the customer context without Agent Request or callback. |

| Note | Shared sub-customer Components option is not supported. |
|---|---|

| Note | Shared sub-customer Components option is not supported. |
|---|---|

| Components | Design considerations |
|---|---|
| Agent Greeting |  |
| Whisper Announcement |  |
| Courtesy Call Back |  |
| Outbound Dialer | Maximum of 32 Dialers are supported and Maximum 4000 ports are supported. Note There is no solution for sub-customers to manage outbound campaigns. Provide services or custom solutions to manage outbound
                                                      campaigns for each sub-customer. | Note | There is no solution for sub-customers to manage outbound campaigns. Provide services or custom solutions to manage outbound
                                                      campaigns for each sub-customer. |
| Note | There is no solution for sub-customers to manage outbound campaigns. Provide services or custom solutions to manage outbound
                                                      campaigns for each sub-customer. |
| Mobile Agents |  |
| A-law and mu-law support |  |
| Post Call Survey |  |
| Application Gateway | Not supported in  Small Contact Center. |
| Database Integration | ICM DB lookup is not supported. |
| Local Trunk PSTN Local Breakout |  |
| Local Trunk Location based CAC | Not supported for dedicated components sub-customer option. |
| Unified CM-based Silent Monitoring |  |
| Task Routing | The Task Routing API does not provide for multi-tenant interface to the SCC. |
| Precision Routing | Enabling Precision Routing on SCC limits the deployment to a maximum of 12 Agent PGs. |
| Single Sign-On | SCC uses a single IdS registered to the hosted AD FS 2012 R2 IdP for all customer authentication. All SSO Agents and Supervisor
                                          sign-in names must be in Email (UPN) format. |

| Note | There is no solution for sub-customers to manage outbound campaigns. Provide services or custom solutions to manage outbound
                                                      campaigns for each sub-customer. |
|---|---|