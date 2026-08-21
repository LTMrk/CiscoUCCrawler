---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-maintenance-guide-pcce-b-1501-f-8ce52fc5d4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/maintenance/guide/pcce_b_1501_features-guide/pcce_m_1501_optional-features-in-packaged-cce.html
retrieved_at: 2026-08-21T12:10:02.986516+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Optional Features in Packaged CCE

## Chapter: Optional Features in Packaged CCE

# Optional Features in Packaged CCE

## Features Descriptions

You can choose to enable these features at any time after your Packaged CCE system is installed, configured, and operational.

Agent Greeting manages the recording and playing of greeting messages from agents. An agent's recorded greeting plays automatically
                                 to callers when they connect to that agent. Agents can set up different greetings for different types of callers, if the call
                                 center supports that option.

Courtesy Callback offers customers the option to hang up and then receive a callback when an agent is close to being available,
                                 rather than having to wait for an extended time on hold. Customers do not lose their place in the queue. The system collects
                                 callback information from the caller, monitors agent availability, and calls the customer when the agent is close to available.

Enterprise Chat and Email (ECE) is an optional feature that provides chat and email functionality to the contact center. The
                                 ECE server routes chat and email contacts to agents on their Cisco Finesse desktops. The ECE server can be installed on the
                                 Packaged CCE Side B host or on an external server.

ECE includes the following features:

Email—Email is supported by ECE to create a communication channel between a customer and an agent. There are various steps
                                       involved in efficiently responding to emails from customers. Emails are first retrieved into the system and routed to appropriate
                                       users or queues. After a response is created, it is processed through the system and sent to the customer.

Chat—A chat is a real-time interaction between an agent and a customer during which they exchange text messages. As part of
                                       a chat, agents can also push web pages to customers. Based on how chat activities are routed to agents, they can be categorized
                                       as standalone chats or integrated chats. An integrated chat is routed to an integrated queue and a message is sent to Packaged
                                       CCE. The system processes the activity and assigns the chat to an available agent.

Web Callback—The Web Callback feature allows the user to request a callback by submitting a form on a website. ECE processes
                                       the submitted information and connects the user with an agent. ECE then sends a request to Packaged CCE to route the callback
                                       request to the agent.

Delayed Callback—The Delayed Callback feature is similar to Web Callback, but when ECE receives the delayed callback request,
                                       it adds the request in the Delayed Callback table. ECE sends the HTML page to the customer, indicating that the customer will
                                       receive a callback within a specified time. When the specified time arrives, ECE moves the request to the Packaged CCE queue
                                       for routing to Unified CCE.

For more information about this feature, see the Cisco Enterprise Chat and Email documentation.

Extension Mobility and Extension Mobility Cross Cluster are Cisco Unified Communications Manager features that allow agents
                                 to temporarily access their Cisco Unified IP Phone configuration, such as line appearances, services, and speed dials, from
                                 other Unified IP Phones.

Extension Mobility works on phones that are located within the same Unified Communications Manager cluster. Extension Mobility
                                 Cross Cluster works on phones that are located in different Unified Communications Manager clusters.

As part of the configuration in Unified Communications Manager Administration , you create a device profile for each agent that will use Extension Mobility, and associate each device profile with the
                                 appropriate agent. You can add either all of the device profiles to the pguser, or all of the phones that the agents use to
                                 the pguser. You do not need to add both the profiles and phones to the pguser.

For more information, see the Extension Mobility section of the Feature Configuration Guide for Cisco Unified Communications Manager .

Mobile Agent supports call center agents who are using phones that are not directly controlled by Packaged CCE. A mobile agent
                                 can be located outside of the contact center, using an analog phone or a mobile phone. Mobile agents may also be located in
                                 the contact center using an IP phone connection that is not controlled by Packaged CCE. All mobile agents use broadband connection
                                 to access the same Agent desktop and agent state controls as non-mobile agents.

Packaged CCE supports both Call by Call and Nailed Connection mode.

Outbound Option manages and performs outbound dialing campaigns. You configure the system to automatically dial numbers using
                                 imported contact lists and filtering rules. When a call connects to a live person, the system transfers the call to an agent
                                 skilled in handling that calling campaign.

Post-Call Survey sends a caller to an automated survey after the agent disconnects. A Post-Call Survey is typically used to
                                 determine whether customers are satisfied with their call center experiences.

Single sign-on (SSO) is an authentication and authorization process. (Authentication proves you are the user you say that
                                 you are, and authorization verifies that you are allowed to do what you are trying to do.) SSO allows users to sign in to
                                 one application and then securely access other authorized applications without a prompt to resupply user credentials. SSO
                                 permits Cisco supervisors or agents to sign on only once with a username and password to gain access to all of their Cisco
                                 browser-based applications and services within a single browser instance. By using SSO, Cisco administrators can manage all
                                 users from a common user directory and enforce password policies for all users consistently.

Task Routing application programming interfaces (APIs) provide a standard way to request, queue, route, and handle third-party
                                 multichannel tasks in CCE.

Contact Center customers or partners must develop Customer Collaboration Platform and Finesse applications using these APIs to use the Task Routing feature. The Customer Collaboration Platform application submits nonvoice task requests to CCE. The Finesse application enables agents to sign in to different types of
                                 media and handle the tasks. Agents log in to and manage their state in each media independently.

Whisper Announcement plays a brief message to an agent before connecting a caller to the agent. The message may include information
                                 about the caller or choices the caller made from menu options.

Video Contact Center provides high-quality video collaboration between customers and agents. Depending on how Video Contact
                                 Center is deployed, customers may connect with agents either from within the enterprise network or from devices outside the
                                 enterprise.

## Integrations with Other Cisco Products

You can extend Packaged CCE functionality by integrating it with other Cisco products.

Cisco Customer Collaboration Platform is a customer-care system that provides capture, filtering, workflow, queuing, and reporting for social media engagement
                                 teams. Internet postings captured by Customer Collaboration Platform are referred to as Social Contacts. Customer Collaboration Platform stores the social contacts and groups them into user-defined Campaigns. Each Campaign obtains social contacts from one or
                                 more Feeds. Customer Collaboration Platform presents the social contacts to social media customer care personnel who can search, review, categorize, and respond to the
                                 postings. Customer Collaboration Platform also produces reporting metrics on the handling of the social contacts.

Customer Collaboration Platform is also used for the following contact center features:

Agent Request

Task Routing

For information about Customer Collaboration Platform , see https://www.cisco.com/en/US/products/ps11349/index.html .

## Assumptions for Proceeding with Optional Features

This document makes the following assumptions about the state of your Packaged CCE system and the system administrator's knowledge
                           of Packaged CCE:

Your Packaged CCE system must be installed, configured, and operational.

System administrators must have access to the following interfaces:

Cisco Packaged Contact Center Enterprise (CCE) Administration

Script Editor

Cisco Customer Collaboration Platform

Cisco Finesse

Cisco Unified Communications Manager (CUCM) reporting interface

Enterprise Chat and Email

System administrators must be familiar with the following procedures or have access to the Cisco documentation that describes
                                 them:

Expanded call variables—Know how to use Unified CCE Administration to set variable values and add new variables.

Scripting—Know how to use the Script Editor to create new Packaged CCE call routing scripts and modify existing scripts. Understand
                                       the scripting technology.

CVP scripting—Know how to use the CVP Script Editor to create new or modify existing voice scripts.

For more details, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide .