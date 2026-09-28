---
doc_id: developer-cisco-com-docs-packaged-contact-center-2a5fed015d
source_url: https://developer.cisco.com/docs/packaged-contact-center/
retrieved_at: 2026-08-24T22:12:36.007995+00:00
---

# What is Packaged Contact Center Enterprise?

Cisco Packaged Contact Center Enterprise (Packaged CCE or PCCE) provides an enterprise-class contact center deployment model that’s easy to install, configure, and administer. It is also predesigned and bounded. As a result, it similfies deployment, operation and maintenance but still provides a complete omni-channel solution for contact centers with up to 12,000 agents.

PCCE provides rich contact center functionality:

- Call routing & processing

- Prompts and rich VXML scripting

- Built-in omnichannel (voice, chat, email)

- Voice response collection

- Agent selection

- Queuing

- Reporting

It offers the following on-box features:

- Precision Routing

- Whisper Announcement

- Agent Greeting

- Courtesy Callback

- Outbound

- Mobile Agents

Packaged CCE contains the following products:

- Cisco Unified Communications Manager (CUCM)

- Unified Customer Voice Portal (CVP)

- Unified Contact Center Enterprise (UCCE)

- Cisco Unified Intelligence Center (CUIC)

- Cisco Finesse

With its simplified install, deployment and management interface, Packaged CCE delivers a streamlined user experience.

# Technical Overview

## PCCE REST APIs

Packaged Contact Center Enterprise provides REST APIs for viewing and updating configuration programatically. These REST APIs are easy to use, modeled after HTTP, and works in thick and thin client integrations. The PCCE Developer Guide explains the details for each of the API's, but here is a high-level description of the API functionality:

- User Configuration and Management

- Create users based on role (administrators and agents)

- Get a list of users of a particular role

- View and update user information

- Delete users

- Create, view, update or delete agent desk settings

- Skill Group Management

- Team Configuration and Management

- Create an agent team

- Get a list of agent teams

- View and update team information

- Delete an agent team

- Outbound Option campaign configuration and management

- Define new Outbound Option campaigns

- View, edit or delete existing campaigns

- Get the real-time status of running Outbound Option campaigns

- Set the Do Not Call (DNC) import rule configuration for Outbound Option

- Import customer contact information for an Outbound Option campaign

- Configure your Outbound Option campaign to handle personal callbacks

- List all available time zones and to get information about a specified time zone

- Call Configuration and Management

- Create, view, list, update or delete Dialed Numbers

- Create, view, list, update or delete Call Types

- Create, view, list, update or delete Expanded Call Variables

- Bulk create or update functionality

- Agents and their Skills, Attributes, and Teams

- Dialed Numbers and their associated Call Type

- System configuration

- Define, view, update or delete business hours

- Configure the timezone

- View and update the hostname of the CVP Reporting Server

- Create, view, list, update or delete remote data centers in the inventory

- Get the deployment type and capacity

# What can a developer do with PCCE?

The PCCE APIs allows developers to build custom applications for day to day management of agents, skills, calls, and the PCCE system. It also allows developers to integrate this functionality into existing applications whether it is a thin or thick client.

Documentation can be found in the Packaged Contact Center Enterprise Developers Guide .

# Next Steps

The best way to really understand the Packaged Contact Center Enterprise REST APIs is to try it for yourself. Reserve a PCCE sandbox to try out the APIs and learn how easy it is to use!

Next