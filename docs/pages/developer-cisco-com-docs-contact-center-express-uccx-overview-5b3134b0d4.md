---
doc_id: developer-cisco-com-docs-contact-center-express-uccx-overview-5b3134b0d4
source_url: https://developer.cisco.com/docs/contact-center-express/uccx-overview/
retrieved_at: 2026-08-25T21:01:28.817957+00:00
---

# What is Unified Contact Center Express?

Cisco Unified Contact Center Express (UCCX) is a "contact center in a box" that provides a secure and easy to deploy customer interaction management solution for up to 400 agents. It is an IP-based Automated Call Distribution (ACD) system that queues and distributes incoming calls destined for groups of Cisco Unified Communications Manager users (agents). Unified CCX provides a multimedia (voice, data, and web) customer-care application environment that enhances the efficiency of contact centers by simplifying business integration, easing agent administration, increasing agent flexibility, and enhancing network hosting.

Unified CCX provides options to address multiple contact center functional areas such as:

- Inbound voice

- Outbound campaign

- Agent email

- Web chat

- Next-generation historical and real-time reports and dashboards

The Unified CCX can be used to route calls to specific agents or even to integrate with Unified IP IVR to gather caller data and classify incoming calls.

Developers can integrate with Unified CCX through:

- Computer Telephony Integration (CTI) Protocol : Allows customers to develop custom 3rd party agent and supervisor desktops as well as reporting applications.

- Configuration REST API : Allows customers to access administrator configuration to build a custom administration interface or to automate the configuration of Unified CCX.

- Cisco Unified CCX Editor : Allows customers to create telephony and multimedia application scripts using a visual programming environment.

- Cisco Identity Service Client SDK : Allows end users to seemlessly use various web applications and applications built with the REST APIs within the Cisco Contact Center solution after a single login.

Cisco Unified Contact Center Express is available in three packages (Standard - available for 11.0 and below, Enhanced, Premium) tailored to meet your customer contact requirements.

## What are the Business Benefits?

- Improved customer satisfaction and loyalty with comprehensive contact management

- Improved workforce productivity so you can do more with less

- Significant cost optimization with an easy-to-deploy, easy-to-use, all-in-one solution

For more information about the Unified CCX product, see https://www.cisco.com/c/en/us/products/contact-center/unified-contact-center-express/index.html

# Technical Overview

The Unified CCX system comprises of the following components that provides programmable interfaces to other applications:

- Unified CCX Engine

- Administration API Web Application

- Finesse

In addition to these components running on UCCX, Customer Collaboration Platform , which is used in the UCCX solution for chat and email channels of customer collaboration, provides interfaces to build custom web chat clients.

The above diagram outlines these core components and the interfaces that are available for developers/applications to interact with.

Note : The UCCX system comprises of other components and subsystems that are significant in terms of architecture, but it is not relevant from developer interface point of view. Those are omitted in the diagram and the subsequent documentation.

## Unified CCX Engine

The Unified CCX Engine performs the core functions of the Contact Center Express, which includes:

- IVR functionalities for voice calls

- Programmable Scripting

- Agent and Contact management

- Contact Queue and routing

- Computer Telephony Integration (CTI) Messaging

- Data generation for Live Data and Historical Reports

The CTI Server and the Programmable Scripting Engine are the two interfaces that provides ability for external applications to interact with Unified CCX Engine.

### CTI Server

The CTI Server is responsible for keeping track of calls, agent states, and maintaining socket connections to all CTI clients to name a few. It also processes the requests made by the CTI clients and sends updates when there are changes. The CTI clients connect and interact to the CTI Server/CCX Engine via the Unified CCX CTI Protocol . Using the CTI Protocol, applications are able to:

- make agent login requests

- manage state

- make/answer/drop calls

- receive agent and team configuration events

- silent monitor calls

- and many more operations

To build a custom client that can connect to Unified CCX engine using the CCX CTI Protocol, refer to the CTI Protocol Developer Guide for more details.

### Programmable Scripting Engine

Unified CCX provides an ability for developers to program the business logic of how to handle a Voice Call or an Http Contact (Web Action performed by a user) by the engine. The scripting involves building the business workflow using a proprietary domain specific programming tool, the Unified CCX Editor, and save the defined workflow as a file to be uploaded to UCCX via the administration web and REST interface.

The Unified CCX Editor provides the graphical user interface to create and test the script either offline or by directly triggering a voice call or http action on the UCCX server that the Editor is connected to.

The individual programming steps of the script must be selected from an existing pool of steps. If the available steps are not sufficient, custom steps can be implemented using the Java programming language.

To build a custom script, refer to the Scripting and Development Series Guides for more details.

## Unified CCX Administration Web Application

The Unified CCX Administration Web Application exposes configuration REST APIs , that can be used to perform all Day 1 and Day 2 configuration of the UCCX system. All of the initial configuration of the system and configuration tasks normally done after installation can be performed using these configuration APIs.

The standard structure of the URL of the configuration APIs and the typical operations that are supported are outlined in the diagrams below.

The typical flow of operations involved in updating an entity has to be:

- Retrieval all instances of the entity

- Choose the instance to be modified, get the instanceId

- Retrieve the information on the specific instance, using instanceId of the entity

- Make the required modifications to the entity payload

- Update the specific entity using the updated entity payload

Some of the example applications that can be built using Configuration/Administration APIs are:

- Advanced Campaign Management

- Agent Reskilling

To build an application using the configuration APIs, refer to the Configuration API Developer Guide for more details.

## Finesse

Finesse provides REST APIs to perform voice call control and agent state management. Finesse uses the CTI Protocol to connect to the Unified CCX Engine. In a Unified CCX solution, Finesse is co-resident with UCCX, meaning it is part of the Unified CCX installer.

When using the Finesse REST APIs, the clients will be agnostic of the CTI protocol. All call control operations and agent state management operations performed traditionally using CTI messages are abstracted using REST APIs.

To build an application using the Finesse APIs, refer to the Finesse REST API Developer guide for more details.

## Customer Collaboration Platform

Cisco Customer Collaboration Platform (CCP), in a UCCX solution, acts as the ingress point for chat and email channels. It handles the chat and email media flow from the agent desktop to the customer who initiated the chat or email.

CCP exposes REST APIs which can be used for custom web clients for UCCX web chat.

To build a custom web chat client, refer to the Customer Collaboration Platform Developer Guide for more details.

# What can a developer do with Unified CCX?

Unified CCX allows developers has three points of integration:

- CTI Protocol : The CTI protocol can be used to build an agent desktop, a reporting application and/or integrate into an existing application. Documentation can be found in the CTI Protocol Developer Guide .

- Configuration APIs : These APIs can be used to build a custom administrator application and/or automate the configuration of the Unified CCX system. Documentation can be found in the Configuration API Developer Guide .

- Scripting : Scripting allows customers to create telephony and multimedia application scripts using a visual programming environment. Documentation can be found in the Scripting and Development Series Guide .

- Identity Service : The Identity service client SDK allows end users to seemlessly use various web applications and applications built with the REST APIs within the Cisco Contact Center solution after a single login.  Documentation can be found in the Cisco Identity Service Client SDK Guide

In addition to the above points of integration with Unified CCX, the Unified CCX solution contains two additional points of integration:

- Finesse REST APIs: The Finesse REST APIs can be used to perform agent operations such as login, change state, and make calls. Documentation can be found in the Finesse Developers Guide .

- Customer Collaboration Platform REST APIs: The Customer Collaboration Platform REST APIs can be used to build custom web clients for UCCX web chat. Documentation can be found in the Customer Collaboration Platform Developer Guide .

# Next Steps

The best way to really understand Cisco UCCX is to try it for yourself. Please proceed to the Getting Started page to learn just how easy it is.

Next