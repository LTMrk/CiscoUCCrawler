---
doc_id: developer-cisco-com-docs-enterprise-chat-and-email-5461198a6a
source_url: https://developer.cisco.com/docs/enterprise-chat-and-email/
retrieved_at: 2026-08-24T22:12:05.302092+00:00
---

# Enterprise Chat and Email (ECE) Overview

Enterprise Chat and Email (ECE) offers powerful email, chat and web callback capabilities for Cisco Unified Contact Center Enterprise (UCCE) , Packaged Contact Center Enterprise (PCCE) and Hosted Collaboration Solution for Contact Center (HCS-CC) solutions. ECE is integrated into UCCE/PCCE/HCS, providing a multichannel customer engagement across email, chat, and phone interaction channels as a blended experience to the agent. Using a rich set of capabilities with CCE routing logic (skill group or precision queue), the best agent is selected to handle the email or chat session based upon customer information, information in the chat or email (header or body) and business Service Level Agreement (SLA) levels.

## What are the business benefits?

- Helps businesses set up multichannel customer engagement hubs to provide consistent high-quality service across all interaction channels such as email, chat, and phone.

- Enables a blended agent for handling of web chat, email and voice interactions.

- Provides a service console that is designed specifically for use by customer service agents to handle service interactions by providing the agent with all the tools and information that they need to complete activities.

# Technical Overview

## Enterprise Chat and Email Architecture

### File Server

The file server handles startup scripts, reports templates, reports outputs, and license files.

- There is generally one file server per configuration.

- File servers can be installed in a cluster for failover.

### Database Server

The database server consists of four different databases:

- Master Database : Stores system configuration information to manage services

- Active Database : Stores business and interaction data (Also considered the partition database)

- Reports Database : Stores data used by the reports module

- Archive Database : Stores archived data

### Messaging Server

The messaging server is a centralized location for exchange of information between application’s components.

- Handles sending and receiving of messages

- One messaging server per deployment

Messaging server is used for the following functions:

- Communication between multiple application servers

- Communication between services server and application server

### Application Server

The application server contains the business logic responsible for interactive responses to all user-interface requests.

- Handles and interprets requests for operations

- Delivers responses as dynamically constructed web pages

### Web Server

The web server serves static content to the browser, such as HTML pages, images, Java applets, and client-side JavaScript code.

- Routes all requests for .jsp files to application server for content generation

### Services Server

The services server houses business functionality, including fetching emails from POP3 or IMAP, sending emails through SMTP, processing workflows, and assigning chats to agents.

- Services run on the services server and are managed by the Distributed Service Manager (DSM)

# Why should you use the Enterprise Chat and Email APIs?

The ECE REST API provides a simple and powerful way to interact with resources, such as Article, Case, Activity, or Customer in ECE Platform using the standard HTTP methods (GET, PUT, POST, and DELETE).
GET method allows retrieving a resource
POST method allows creating a new resource
PUT method allows updating a resource
DELETE method allows deleting or removing a resource
Since ECE REST API operates over HTTP(s), it makes it easy to use it with any programming language or framework. The API can be used for many purposes, including:
Building mobile apps and modern web applications.
Integrating ECE platform with other applications.

The Enterprise Chat and Email APIs provides partners and customers with a powerful way to interact with ECE resources, such as Case, Activity, or Customers using standard HTTP methods (GET, PUT, POST, and DELETE) and can be used for many purposes, including modern web applications as well as Integrating platform with other applications. This allows the ability to customize ECE to address specific customer needs and to add value beyond the core product capabilities.

# What can a developer do with Enterprise Chat and Email APIs?

Enterprise Chat and Email provides 3 types of APIs:

- Interaction REST APIs : These APIs can be used for many purposes, including:

- Building mobile apps and modern web applications.

- Integrating ECE platform with other applications.

With the Interaction REST APIs, a developer can:

- Retrieve a resource

- Create a new resource

- Update a resource

- Delete or remove a resource

- Web Services API for Chat : These APIs can be used to show the Chat link on a web sites based on the availability of agents to handle new chats. The APIs can be used for following purposes:

- To enable or disable the Chat button on web sites depending on available agents.

- To get the amount of time a customer might have to wait before an agent is available to chat.

- To find the position of customer in a queue to estimate how long a customer might have to wait before an agent is available to chat.

- Write new custom surveys for chat sessions to capture additional data.

Data Adapter : The data adapters is a quick and easy way to integrate with external sources of information residing within your enterprise, or on the web. It is a flexible integration tool for accessing data from external sources such as local and remote databases, HTTP or HTTPS services, XML files, etc. The data is then available through XML APIs for automated processing and display.

Data Dictionary : With the data dictionary, a developer can use SQL queries to build custom reports using the data from the Enterprise Chat and Email database.

Next