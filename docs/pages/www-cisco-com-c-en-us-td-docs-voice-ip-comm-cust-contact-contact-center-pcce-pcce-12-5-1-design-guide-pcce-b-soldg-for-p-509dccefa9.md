---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-design-guide-pcce-b-soldg-for-p-509dccefa9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/design/guide/pcce_b_soldg-for-packaged-cce-12_5/pcce_b_soldg-for-packaged-cce-12_5_chapter_01001.html
retrieved_at: 2026-08-21T16:38:31.547072+00:00
---

Solution Design Guide for Cisco Packaged Contact Center Enterprise, 12.5(1) & 12.5(2)

# Solution Design Guide for Cisco Packaged Contact Center Enterprise, 12.5(1) & 12.5(2)

Updated: May 20, 2021

Chapter: Avaya and ICM-to-ICM Gateway Support

## Chapter: Avaya and ICM-to-ICM Gateway Support

# Avaya and ICM-to-ICM Gateway Support

## Introduction

Packaged CCE supports Avaya PG and ICM-to-ICM Gateway as a Non-Reference Design solution. You must deploy Avaya PG on a separate
                              VM.

Packaged CCE offers several call flows to support different needs. Use the following in a Non-Reference Design:

Pre-route call flows

Translation route

Post-route call flows

For more information , see the Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Unified CVP Type 10 is the supported Network VRU.

## Configuration Limits and Scalability Constraints

The following table specifies the configuration limits and scalability constraints for the Non-Reference parameters that are
                              supported in the Packaged CCE 4000 and 12000 Agents Deployment.

When you design your contact center, ensure that your design is deployed within these limits. Consult Cisco if you have special
                              configuration requirements that might exceed specific parameters.

System configuration limits are defined in the Reference Designs. For more information, see Reference Design Configuration Limits .

Multiple PIMs on a PG affect performance. Compared to a single PIM on each PG, multiple PIMs lower the total number of agents,
                                          VRU ports, and supported call volume. There is a maximum of one PIM on each Avaya PG with CTI OS coresident.

Maximum number of CTI servers per PG

1

### Additional Sizing Factors

Many variables in the Packaged CCE configuration and deployment options can affect the server requirements and capacities. This section describes the major
                              sizing variables and how they affect the capacity of the various Packaged CCE components.

#### Average Skill Groups Per Agent

The number of skill groups per agent (which is independent of the total number of skills per system) significantly affects
                                 the CTI OS servers.

Limit the number of skill groups per agent to 5 or fewer, when possible. Periodically remove unused skill groups so that they
                                 do not affect the system's performance. You can also manage the effects on the CTI OS Server by increasing the value for the
                                 frequency of statistical updates.

CTI OS monitor mode applications are supported only at 20 or lower skill groups per agent.

#### CTI OS Monitor Mode Applications

A CTI OS Monitor Mode application can affect the performance of the CTI OS Server. CTI OS supports only two such applications
                                 per server pair. Depending on the filter specified, the impact on the CPU utilization might degrade the performance of the
                                 Agent PG.

#### CTI OS Skill Group Statistics Refresh Rate

The skill group statistics refresh rate can also affect the performance of CTI OS Server. Cisco requires that you do not lower
                                 the refresh rate below the default value of 10 seconds.

#### Translation Route Pool

Sizing the translation route pool depends on the expected call arrival rate. Use the following formula to size the translation
                                 route pool:

Translation route pool = 20 * (Calls per second)

This calculation is specific to Packaged CCE . For more general Packaged CCE deployments, consult your Cisco Account Team or Partner.

## ACD Call Deployments and Sizing Implications

The information in this section applies to ACD integrations that use Unified CVP. The ACD device shares the following characteristics:

Manage agents and transfer calls to the destination.

Route requests and be switch leg devices. However, the device cannot handle Correlation ID and more than one transfer.

An ACD user issues a Route Request for one of the following reasons:

Connect to another agent in a particular skill group

Reach a self-service application

Blind-transfer a previously received call to one of the above entities

Each of the above calls invokes a routing script. The script searches for an available destination agent or service and if
                           an appropriate destination is found, it sends the corresponding label either back to the ACD or, if blind-transferring an
                           existing call, to the original caller's Switch leg device. If it needs to queue the call or if the ultimate destination is
                           intended to be a self-service application rather than an agent or service, the script sends a VRU translation route label
                           either back to the ACD or, if transferring an existing call through blind-transfer, to the original caller's Switch leg device.

If the above sequence results in transferring the call to Unified CVP's VRU leg device, a second transfer is done to deliver
                           it to a Voice Browser. To ensure that these events take place, the following configuration elements are required:

For new calls from the ACD or warm transfers of existing calls:

Configure the Unified CVP peripheral to be associated with a Type 10 Network VRU.

Associate the dialed number that the ACD dialed with a Customer Instance that is associated with a Type 10 Network VRU.

When an ACD is not configured , the routing script that is invoked by the ACD dialed number must contain a TranslationRouteToVRU
                                       node to get the call to Unified CVP's Switch leg, followed by a SendToVRU node to get the call to the Voice Browser and Unified
                                       CVP's VRU leg.

Associate all the VRU scripts that are run by that routing script with the Type 10 Network VRU.

For blind transfers of existing calls:

The Unified CVP peripheral can be associated with any Network VRU.

The dialed number that the ACD dialed must be associated with a Customer Instance that is associated with a Type 10 Network
                                       VRU.

The routing script that is invoked by the ACD dialed number must contain a SendToVRU node to send the call to the Voice Browser
                                       and Unified CVP's VRU leg.

All the VRU scripts that are run by that routing script must be associated with the Type 10 Network VRU.

When Packaged CCE chooses an agent or ACD destination label for a call, it tries to find one that lists a routing client that can accept that
                           label. For calls originated by an ACD  that are not blind transfers of existing calls, the only routing client is the ACD
                           , after the call is transferred to Unified CVP, because of the handoff operation, the only routing client is the Unified CVP
                           Switch leg. However, in the case of blind transfers of existing calls, two routing clients are possible:

The Call Server switch leg that delivered the original call.

The ACD . For calls that originate through Unified CVP, you can prioritize Unified CVP labels above ACD labels by checking
                                 the Network Transfer Preferred check box in the Packaged CCE screen for the Unified CVP peripheral.

## Agent Desktops

A Packaged CCE deployment requires an agent desktop application. The agent uses this desktop for agent state control and call control. In
                              addition to these required features, the desktop can provide other useful features.

Cisco offers the following agent desktop application for Avaya agents:

CTI Toolkit Desktop: An agent desktop application built with the CTI Toolkit. The desktop supports full customization and
                                    integration with other applications, customer databases, and Customer Relationship Management (CRM) applications.

Cisco partners offer the following types of agent desktop applications:

Partner agent desktops: Custom agent desktop applications are available through Cisco Technology Partners. These applications
                                    are based on the CTI Toolkit and are not discussed individually in this document. The Finesse REST API also enables partner
                                    desktop integration.

Prepackaged CRM integrations: CRM integrations are available through Cisco Unified CRM Technology Partners. These integrations
                                    are based on the CTI Toolkit and are not discussed individually in this document.

Desktop applications typically run on agent desktops, Administration & Data servers, or administration clients. Services that
                                 support the desktop applications can run on the Avaya Peripheral Gateway (PG) server or on their own server. For each PG,
                                 there is one set of active desktop services.

## CTI Object Server

The CTI Object server (CTI OS) is a high-performance, scalable, fault-tolerant, server-based solution for deploying CTI applications.
                              CTI OS is a required component for the CTI Toolkit Desktop. The CTI OS server runs as a redundant pair, one server on each
                              VM that hosts an Avaya PG .

Desktop applications pass communications, such as agent state change requests and call control, to the CTI OS server. CTI
                              OS is a single point of integration for CTI Toolkit Desktops and third-party applications, such as Customer Relationship Management
                              (CRM) systems, data mining, and workflow solutions.

The CTI Object server connects to the CTI server over TCP/IP and forwards call control and agent requests to the CTI server.

The CTI OS server also manages CTI Toolkit desktop configuration and behavior information, simplifying customization, updates,
                              and maintenance, and supporting remote management.

### CTI Object Server Services

Desktop security: Supports secure socket connections between the CTI Object server on the PG and the agent, supervisor, or
                                    administrator desktop PC. Any CTI application built using the CTI OS Desktop Toolkit (CTI Toolkit) C++/COM CIL SDK can use
                                    the desktop security feature.

Desktop Security is not currently available in the .NET and Java CILs.

Quality of Service (QoS): Supports packet prioritization with the network for desktop call control messages.

QoS is not currently available in the .NET and Java CILs.

Failover recovery: Supports automatic agent sign-in upon failover.

Chat: Supports message passing and the text chat feature between agents and supervisors.

You deploy the CTI Object server in redundant pairs, one on Avaya PG A and one on Avaya PG B . Both CTI OS servers are active simultaneously. The CTI Toolkit desktop applications randomly connect to one of the two servers.
                              If the connection to the original server fails, the desktops automatically fail over to the alternate server.

The CTI OS server interfaces to any desktop application built using the CTI Toolkit SDK.

| Note | System configuration limits are defined in the Reference Designs. For more information, see Reference Design Configuration Limits . |
|---|---|

| Parameter | Limit Value | Comments |
|---|---|---|
| >450 - <=12,000 agents |
| Avaya PIMs on each Avaya Peripheral Gateway (PG) | 5 | Multiple PIMs on a PG affect performance. Compared to a single PIM on each PG, multiple PIMs lower the total number of agents,
                                          VRU ports, and supported call volume. There is a maximum of one PIM on each Avaya PG with CTI OS coresident. |
| Maximum number of CTI servers per PG | 1 |  |
| Skill groups on each Avaya PG | 4000 |  |

| Note | CTI OS monitor mode applications are supported only at 20 or lower skill groups per agent. |
|---|---|

| Note | Desktop Security is not currently available in the .NET and Java CILs. |
|---|---|

| Note | QoS is not currently available in the .NET and Java CILs. |
|---|---|

| Note | The CTI OS server interfaces to any desktop application built using the CTI Toolkit SDK. |
|---|---|