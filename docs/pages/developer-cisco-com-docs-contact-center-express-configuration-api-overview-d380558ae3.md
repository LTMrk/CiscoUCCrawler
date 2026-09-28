---
doc_id: developer-cisco-com-docs-contact-center-express-configuration-api-overview-d380558ae3
source_url: https://developer.cisco.com/docs/contact-center-express/configuration-api-overview/
retrieved_at: 2026-09-07T14:05:59.158644+00:00
---

# What is the Unified Contact Center Express Configuration API?

The Unified CCX configuration Application Programming Interface (API) allows customers to integrate provisioning applications similar to what is provided by the Unified CCX Application Administration interface for Unified CCX for configuration of inbound and outbound applications.

Unified CCX exposes sophisticated control of the contact center application management via its Configuration REST APIs. These REST APIs are easy to use, modeled after HTTP, and works in thick and thin client integrations. The Unified CCX Configuration API Developer Guide explains the details for each of the API's, but here is a preview of some of the API functionality available:

- Agent Statistics - Provides agent state reports about the resources

- Get Agent Statistics (e.g. number of logged in, ready, not ready, and talking resources)

- Application - Provides information of the application (Script, Busy, Ring-No-Answer)

- Get List of Applications

- Get/Create/Modify/Delete Application

- Area Code : Represents an area code which determines the geographical location of the phone number you dial

- Get List of Area Codes

- Get/Create/Modify/Delete Area Code

- Call Control Group : Allows you to control the use of CTI ports

- Get List of Call Control Groups

- Get/Create/Modify/Delete Call Control Group

- Check Status of POST/PUT/DELETE

- Campaign : Logical entities that group a set of contacts together in a dialing list that deliver outgoing calls to agents

- Get list of Campaigns

- Get/Create/Modify/Delete Campaign

- Modify Campaign state

- Campaign Contacts - Contacts that are associated with the campaigns as campaign members

- Get list of pending contacts for campaign

- Add contacts to a campaign

- Delete all contacts from a campaign

- Channel Provider - Used to configure the noninteractive channels in Unified CCX

- Get List of Channel Providers

- Get/Create/Modify/Delete a Channel Provider

- Contact Service Queue (Voice & Web Chat) - Controls incoming calls by determining where an incoming call is placed in the queue and to which agent the call is sent

- Get List of CSQ

- Get/Create/Modify/Delete CSQ

- Data Source (EDBS) - Represents the databases that are configured to communicate with the Unified CCX system

- Get List of Data Sources

- Get/Create/Modify/Delete Data Source

- Test Connection for Data Source

- DB Purge - DB Purge configuration that will automatic purge at a given time stamp.

- Get Purge Configuration Information

- Update Purge Configuration Information

- Update Purge Now Configuration

- Get Purge Configuration Status

- Dialog Group - A pool of dialog channels in which each channel is used to perform dialog interactions with a caller

- Get List of Dialog Groups

- Get/Create/Modify/Delete Dialog Group

- HTTP Trigger - The relative URL a user enters into the client browser to start the application.

- Get List of HTTP Triggers

- Get/Create/Modify/Delete HTTP Trigger

- Resource - Represents a Unified CCX agent, supervisor, or administrator

- Get List of Resources

- Get/Modify Resource

- Resource Group - Collections of agents that the CSQ uses to handle incoming calls

- Get List of Resource Groups

- Get/Create/Modify/Delete Resource Group

- Skill - Customer-definable labels that are assigned to agents

- Get List of Skills

- Get/Create/Modify/Delete Skill

- Team - Represents the group of agents who report to the same supervisor

- Get List of Teams

- Get/Create/Modify/Delete Team

- Trigger - Represents a Unified CM Telephony trigger that responds to calls that arrive on a specific route point

- Get list of Triggers

- Get/Create/Modify/Delete a Trigger

# Technical Overview

The Unified CCX Administration Web Application exposes configuration REST APIs , that can be used to perform all Day 1 and Day 2 configuration of the UCCX system. All of the initial configuration of the system and configuration tasks normally done after installation can be performed using these configuration APIs.

The standard structure of the URL of the configuration APIs and the typical operations that are supported are outlined in the diagrams below.

The typical flow of operations involved in updating an entity has to be:

- Retrieval all instances of the entity

- Choose the instance to be modified, get the instanceId

- Retrieve the information on the specific instance, using instanceId of the entity

- Make the required modifications to the entity payload

- Update the specific entity using the updated entity payload

# What can a developer build with the Configuration API?

The configuration REST APIs were built for developers to incorporate administrative and configuration operations into their existing applications or to build an administrator application.

Some of the example applications that can be built using the Unified CCX Configuration APIs are:

- Advanced Campaign Management Applications

- Agent Reskilling Applications

- Custom Administrator Application similar to the UCCX Administration web interface

Please see the Configuration API Developer Guide for more details.

# What programming languages do I need to use the Configuration APIs?

Since the Configuration API are just REST APIs, your application can be in any programming language that supports HTTP/HTTPS requests/responses. Most programming languages have a library that provide wrappers that enable you to issue REST API calls from your native programming environment, parse the result that the server returns, and make that result available in the native programming environment.

# What license level is needed to use the Configuration API?

The Configuration APIs are available for all Unified CCX license packages:

- Unified CCX Standard (designed for entry-level users) :  Includes the steps necessary for creating basic Unified CCX applications, including IP Phone Agent (IPPA) and skills-based routing. The standard license is only available for CCX versions 11.0 and below.

- Unified CCX Enhanced (designed for enterprise-level users) : Includes all functions of Unified CCX Standard, plus support for priority queuing. Includes a license to enable custom Java extensions.

- Unified CCX Premium : Adds full Unified IP IVR support (except for Unified ICM integration) including database integration, Voice eXtensible Markup Language (VoiceXML), HTML web integration, custom Java extensions, and e-Notification services. The outbound feature is now bundled with the Premium package. You will receive one outbound seat free with each premium seat. The maximum number of outbound seats supported will be based on the hardware type.

# Next Steps

The best way to really understand the Unified CCX Configuration APIs is to try it for yourself. Please proceed to the Getting Started page to learn just how easy it is.

Next