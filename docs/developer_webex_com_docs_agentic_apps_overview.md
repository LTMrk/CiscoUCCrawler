[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/create/docs/agentic-apps-overview)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/create/docs/agentic-apps-overview)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/create/docs/agentic-apps-overview)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Agentic Apps Overview
Getting Started
  * [Getting Started](https://developer.webex.com/create/docs)
  * [Authentication](https://developer.webex.com/create/docs/authentication)
  * [Login with Webex](https://developer.webex.com/create/docs/login-with-webex)
  * [AI Assistant for Developers](https://developer.webex.com/create/docs/webex-aI-assistant-for-developers)
  * Agentic Apps
    * [Agentic Apps Overview](https://developer.webex.com/create/docs/agentic-apps-overview)
    * [Onboard Your MCP Server](https://developer.webex.com/create/docs/onboard-your-mcp-server)
    * [Onboard Your Agent](https://developer.webex.com/create/docs/onboard-your-agent)
    * [Submit to App Hub & Badging](https://developer.webex.com/create/docs/agentic-apps-app-hub)
    * [Provisioning on Control Hub](https://developer.webex.com/create/docs/provisioning-on-control-hub)
  * Bots
  * Embedded Apps
  * Integrations
  * Service Apps
  * Instant Connect
  * Workspace Integrations
  * Bring Your Own Datasource
  * [Suite Sandbox](https://developer.webex.com/create/docs/developer-sandbox-guide)
  * [Contact Center Sandbox](https://developer.webex.com/create/docs/sandbox_cc)
  * [Guest to Guest Sandbox](https://developer.webex.com/create/docs/g2g-sandbox)
  * [Submit Your App](https://developer.webex.com/create/docs/app-hub-submission-process)
  * [Tutorials](https://developer.webex.com/create/docs/tutorials)


## Getting Started
### Agentic Apps Overview
Learn the key concepts, terminology, and components of agentic apps and the Model Context Protocol (MCP) for building AI-powered integrations.
This guide introduces the foundational concepts behind agentic apps and the Model Context Protocol (MCP), including key terminology, server capabilities, and schema definitions.
####  anchorTerminology
anchor
**Agentic App** - An Agentic App is a service that exposes structured capabilities, such as actions, data sources, or prompts, that an AI agent can invoke to perform tasks. It is not tied to a specific protocol but is analogous to an MCP server when using the MCP standard.
**MCP** - MCP (Model Context Protocol) is an open standard enabling LLMs to discover and use external data and tools. It provides a standardized way for AI agents to access server capabilities without custom integrations.
**Agents** - An AI agent is a software program that can autonomously perform tasks on behalf of a user by using reasoning, planning, and action to achieve goals. It typically consists of code and one or more prompts and interacts with one or more LLMs to perform its function.
**User** – The user who interacts with the agent to perform a task. The user may invoke specific actions, fetch and attach resources to the context used by the agent, and provide consent to risky interactions. A user may not be present in all agent interactions.
**MCP Server** - A server program that exposes tools, resources, prompts, and configuration of metadata using the MCP specification. It acts as the provider of capabilities that the LLM can invoke.
**MCP Client** - A component, often embedded in the agent runtime or AI application, that discovers MCP servers, reads their capability metadata, validates schemas, and sends execution requests to them. It acts as the consumer side of MCP.
**A2A** - A2A (Agent2Agent) is an open communication standard that enables multiple agents potentially using different LLMs, runtimes, or toolsets to exchange messages, delegate tasks, and collaborate. Unlike MCP, which connects one agent to external capabilities, A2A connects multiple agents to each other.
####  anchorWhat an MCP Server Provides
anchor
MCP servers expose capabilities (also called functions) that AI agents can discover and invoke:
**Tools** - Executable actions exposed by the server that the LLM can invoke via an MCP client. A tool typically has an input schema that represents arguments the agent can provide, and an output schema which represents the structure of the returned result. Tools behave like RPC functions, API calls, or commands.
**Resources** - Read-only data entities such as documents, configurations, or database-backed views, that an agent or a user can request or subscribe to for context.
**Prompts** - Structured, reusable instruction templates provided by the server to help the agent instruct the LLM to perform specific tasks. Prompts may include placeholders that can be populated by the agent based on the context or user input.
**Custom Parameters** - Additional configuration values which the user can provide to the MCP client so that it can connect to an MCP server.
####  anchorWhat is Schema?
anchor
**Schema** - A formal description of the structure, data types, and constraints of information exchanged between an MCP server and client.
**Input Schema** - Defines the required and optional arguments a tool accepts, enabling the agent to construct valid tool calls. Ensures type safety and argument validation.
**Output Schema** - Describes the expected structure of data returned by a tool, allowing the agent to parse and act on tool results predictably.
**Annotations** - Metadata fields attached to tools or schemas that extend functionality beyond standard schema defined by MCP or A2A protocol. They can include UI hints, privacy indicators, categorization tags, or execution constraints.
####  anchorAdditional Resources
anchor
  * [A2A Documentation](https://a2a-protocol.org/latest/) - The official documentation for the Agent2Agent protocol.
  * [MCP Documentation](https://modelcontextprotocol.io/docs/getting-started/intro) - The official documentation for the Model Context Protocol.


##### In This Article
  * [Terminology](https://developer.webex.com/create/docs/agentic-apps-overview#terminology)
  * [What an MCP Server Provides](https://developer.webex.com/create/docs/agentic-apps-overview#what-an-mcp-server-provides)
  * [What is Schema?](https://developer.webex.com/create/docs/agentic-apps-overview#what-is-schema)
  * [Additional Resources](https://developer.webex.com/create/docs/agentic-apps-overview#additional-resources)


##### Related Resources
  * [MCP Documentation](https://modelcontextprotocol.io/docs/getting-started/intro "MCP Documentation")
  * [A2A Documentation](https://a2a-protocol.org/latest/ "A2A Documentation")


## Connect
[Support](https://developer.webex.com/support)
[Developer Community](https://community.cisco.com/t5/webex-for-developers/bd-p/disc-webex-developers)
[Developer Events](https://developer.webex.com/blog/categories/events)
[Contact Sales](https://www.webex.com/contact-sales.html?TrackID=1017639&hbxref=&goid=us_contact_sales)
## Handy Links
[Webex Ambassadors](https://www.essentials.webex.com/programs/ambassadors)
[Webex App Hub](https://www.essentials.webex.com/programs/ambassadors)
## Resources
[Open Source Bot Starter Kits](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[Download Webex](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[DevNet Learning Labs](https://www.webex.com)
[Terms of Service](https://developer.webex.com/terms-of-service)
[Privacy Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html)
[Cookie Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html#cookies)
[Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
© 2026 Cisco and/or its affiliates. All rights reserved.
[](https://github.com/webex)[](https://www.facebook.com/CiscoCollab/)[](https://twitter.com/webexdevs)[](https://www.youtube.com/playlist?list=PL2k86RlAekM_bIUrvVw4Haq_0xxTez9zU)[](https://www.linkedin.com/company/webex/)
By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
