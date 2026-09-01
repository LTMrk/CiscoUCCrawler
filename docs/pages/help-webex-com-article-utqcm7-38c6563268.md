---
doc_id: help-webex-com-article-utqcm7-38c6563268
source_url: https://help.webex.com/article/utqcm7
retrieved_at: 2026-09-01T18:53:38.427899+00:00
---

Cisco Webex Contact Center (Webex CC) is a Contact Center as a Service (CCaaS), that enables organizations to enable smarter, proactive, and personalized interactions across the customer journey.

Webex CC is architected, designed, and developed, from ground up, as a cloud native solution, with the following core architectural principles.

Services : Independent set of services with each service supplying a small cohesive set of capabilities to its users.

Event Driven : All the services communicate to each other using messaging, except in web applications where the application uses https interfaces (REST APIs, Push Data via WebSocket interface) for specific use cases.

Stateless/Externalized State : The services are deployed in Kubernetes, running in docker containers, with the ability to automatically scale and be resilient to failures of one or more instances of the services.

Observable : All the services, and the infrastructure components that enables the deployment of such services, are observable with standard mechanisms to measure, detect and prevent situations affecting contact center capabilities as well as quickly troubleshoot and restore services in case of outages.

Isolated/Loosely Coupled : Every service can be built, validated, and deployed/updated independently with no downtime for contact center capabilities.

Webex CC services are deployed in AWS and is powered by a cloud native platform that enables the following:

Availability of infrastructure services and applications across multiple availability zones

Elasticity of infrastructure services and applications enabling dynamic scaling capabilities

Security natively built-in in the way the systems are built and deployed, data is protected in transit and at rest along with the security/compliance certifications that Webex CC has.

Scalable and secure edge infrastructure for Telephony/Voice integrations

Observability with proactive monitoring and alerting that enables High Availability of contact center services to its customers.

Integrated with rest of the Cisco Webex for user authentication/authorization, administration, and provisioning of contact center capabilities.

The further sections in this document expand on each of the above capabilities and how Webex CC architecture enables the same.

### Logical Architecture

The core capability that a contact center solution must have is enabling customers to easily reach out to the organization by commonly used means of communication and get the queries / issues addressed in fast and efficient manner.

However, to ensure that this basic tenet is achieved, there are multiple behind the scenes capabilities that the organization that uses the contact center must have access to. These are:

Mechanisms for customers to start an interaction

Published and Operational telephone numbers that connect telephony calls to contact center system

Email Addresses to which customers can send email to and mechanism to detect new incoming emails.

Ability for customers to reach out via various digital channels, including but not limited to

Chat from a website/App

Direct chat via popular messaging clients such as WhatsApp,
                                    Facebook Messenger, Apple Messages for Business.

Ability to detect new interactions and handle them efficiently

These would include automated IVR system, virtual agents for telephony / chats with programmability inbuilt to define the workflows involved in handling interactions.

Finally, if needed, the interaction must be escalated to an agent, who is optimally skilled to handle the interaction.

Ability for agents to indicate availability for handling interactions and supervisors to monitor, coach agents and obtain the operational metrics that enables efficient interactions.

Ability for administrators to configure and provision the various contact center capabilities that enables agents and supervisors to perform their tasks as expected.

Beyond these, modern enterprises need to have added capabilities to optimize the contact center operations with access to data and insights that visualize and track key operational metrics.

Further, ability to integrate with specialized contact center ecosystem capabilities such as running proactive automated outbound calls, enhancing agent and supervisor experiences using AI, detecting, and understanding the customer journey to proactively supply data upfront to agents are clear differentiators in the way contact center solutions are evolving.

Regarding the consumption model, where contact center offerings are consumed as a cloud delivered software service, the ability to ensure availability, reliability and automated ad-hoc scale requirements requires state of the art monitoring and alerting mechanisms, which enables continuous validation and detection of impending issues and preventing / minimizing impacts to customer operations.

The following figure illustrates the logical architecture of Webex CC.

Webex CC Logical Architecture

### Functional Components

The following sections describe various functional components of Webex CC.

#### Interaction Management

Webex CC supports telephony, email, and messaging (social channels) as various channels by which users can interact with the contact center.

For all the channels, the initial handling can be done by the system and then the interaction can be escalated to an agent.

#### Media Types

##### Telephony

For Telephony, the inbound Voice Call handling is decided by how the call entered the contact center (see Ingress Mechanisms below) and the Webex CC Flow that’s associated with the entry point.

The call gets answered and further actions are done as per the Webex CC Flow definition – which is a programmatic representation of the actions to be performed while handling the call either prior to queueing and routing to an agent or the Flow itself can handle the call with no transfer to an agent.

The Flow Builder in Webex CC allows developers to define the flow and assign it to the entry point via which the call arrives in Webex CC.

These configuration entities and their usage are covered in Configuration Entities .

More information on Flow Builder is covered in the upcoming section on IVR System .

##### Email and Messaging

From Webex CC perspective, Webex Connect provides the ingress and egress capabilities for all digital channels - email, messaging channels, that end users can use to reach out to contact center.

Webex Connect Flow

Decides the handling of such interactions until the interactions are queued and routed to agents. This includes automatic handling and BOT treatments for all forms of messaging and email interactions.

Applies business logic to incoming interaction.

Handles contact prior to queuing.

Flow itself can handle the interaction with no transfer to live agent.

The messaging channels supported by Webex CC are:

Web App / Mobile App Chat

WhatsApp

Facebook Messenger

SMS

Apple Messages for Business

The email channels supported by Webex CC are:

Gmail

Office365

##### Ingress Mechanisms

This section covers the mechanisms by which an interaction can enter Webex CC. Based on the media type, the mechanisms by which an interaction reaches Webex CC are different.

For example, in telephony there is physical infrastructure provisioning needed to enable PSTN connectivity, configuration of the phone numbers, and routing the calls to Webex CC.

For email / messaging channels, the ingress configuration must be done in Webex Connect and it involves email/messaging account provisioning and Webex Connect flow configuration.

##### Inbound Voice

For voice calls, a typical scenario is where users dial a PSTN phone number which then gets connected to the contact center. From an ingress perspective, this needs a mechanism to route calls from PSTN to Webex CC.

The following figure illustrates the voice call ingestion to Webex CC.

Ingress Options for Inbound Voice

The Voice Ingress Services in Webex CC performs third party call control using SIP and answers the incoming call as well as perform transfer, conference, and other call control operations.

The logical entry point for calls in the Webex CC is the configuration entity named ‘Entrypoint’. For Voice ingress, the key configuration of Entrypoint is the phone number associated with it, which is typically a valid PSTN phone number obtained from chosen PSTN provider.

This enables detecting incoming calls on the phone number, associate the call to Entrypoint and use other configuration parameters of the entry point to handle the call as per the Webex CC Flow definition that should be triggered for the interaction.

Webex Contact Center and Webex Calling share a global network of edge access services for routing calls into Webex Cloud.

Calls are routed into Webex Contact center using Webex Calling PSTN services. This service allows you to route calls to your contact center without a Webex Calling subscription.

All new Webex Contact Center subscriptions include Webex Calling PSTN services that are automatically added to all orders.

For more details on the PSTN connectivity options, click here .

##### Security considerations with voice edge infrastructure

It is recommended that Webex Calling customers deploy PSTN services according to best practices and guidelines published as part of the Cisco Preferred Architecture for Webex Calling document.

##### IVR System

Every voice call that comes into a phone number that’s associated with an Entrypoint, gets answered by Webex CC and execution of a Webex CC Flow associated with the Entrypoint, gets started.

Webex CC Flow Builder supplies the programming constructs/operators and functional blocks, termed activities, so that administrators or anyone designing and implementing the IVR logic can combine these building blocks and create the Flow definition.

The programming constructs that Flow supports are:

Declaration and Setting variables – state associated with a flow execution

Pebble Expressions to set value of variables

Conditional Checks

Looping – using Conditionals and Go To (ability to chain activities together)

Invoke REST APIs

Parse Data – JSON, TOML, XML typically used for parsing API response.

Composing activities

A representative set of activities that Flow supplies are:

Play Messages

Collect User Data

Transfer the call to another destination/phone number

Send the call to a Virtual Agent

Queue the call so that it can be answered by an agent.

For every call that is active, an instance of flow execution too is active, until the call ends, resulting in concurrent executions of flows.

Each instance of flow execution provides isolated environment for data / state associated with the flow and there by the call.

During the entire lifecycle of the call, flow also enables responding to certain events that happens and handling them – for example, when a call gets answered by an agent, an event handler can trigger a screen pop in agent desktop interface.

For more information on Webex CC Flow, see Cisco Webex Contact Center Setup and Administration Guide .

##### Virtual Agent Support

Flow supplies an activity to hand off the interaction to a virtual agent, that’s preconfigured in Webex Control Hub.

Once the call is connected to a virtual agent, it provides a conversational IVR experience to the user and the activity either ends with termination of the call or with escalating the call to an agent.

In case of escalation, the flow can be configured to queue the call which then gets answered by an agent.

##### Inbound Digital Interactions

For email, and messaging channel of incoming interactions, Webex CC utilizes Webex Connect for provisioning the assets, flow to handle the incoming interactions and then route the interaction to Webex CC when the Webex Connect flow explicitly queues the interaction so that it can be handled by an agent.

The following figure illustrates the ingestion of email, messaging interactions in Webex CC.

Ingress Options for Email and Messaging

##### Virtual Agent / BOT Integrations

For email and messaging / social channel interactions, the virtual agent/ BOT treatments are configured in the Webex Connect flow.

As with the Virtual Agents for Voice, if the BOT treatment ends with escalating as the result, then the interaction is queued and routed to an agent.

#### Routing and Queueing

Webex CC treats the incoming contact with automated handlers as defined in the Flow and the flow may decide to queue the contact to a queue / directly to an agent (agent specific queue – supported only for telephony/voice interactions).

On queueing, if an agent is available, the agent is reserved, and interaction is routed to the agent. If there are no agents available, the interaction is parked on the queue, and Flow will continue to treat the customer with handler attached to the queueing activity.

When an agent becomes available, the handler gets interrupted, and interaction is offered to agent.

The following figure illustrates the queueing and routing architecture.

Queuing and Routing Architecture

##### Agent Selection

Queues in Webex CC support the following agent selection algorithms:

Longest Available Agent Routing

Skilled Based Routing

Longest Available Agent (LAA)

Best Available Agent (BAA)

Agents are associated with the Queues through Teams.

A queue can be assigned multiple Call Distribution Groups (with each group having one or more teams) , in a sequential manner with configured wait for Call Distribution Group to be added to the queue, so that the search space for a matching agent expands to additional Call Distribution Groups as time progresses.

For Skill based routing, among the skill requirements matching agents associated with the queue, an agent is selected based on LAA or BAA configuration.

##### Voice/Telephony Specific Additional Capabilities

Agent based routing (only for voice/telephony channel)

Webex CC Flow, using the activity QueueToAgent, can route interactions directly to the chosen agent based on the agent Id.

If the agent is not available to handle interactions, interaction can be parked, in an agent specific queue, waiting for the agent to become available

Advanced queue information

Webex CC Flow, using the activity GetQueueInfo, can fetch real-time information for a queue like Position in Queue (PIQ), Estimated Wait Time (EWT), number of agents available in the queue, and can be used to decide whether to queue the contact or not.

Courtesy callback

Webex CC Flow, using activity Callback, lets the customer disconnect from the call while maintaining the position in queue and receive a callback when the virtual interaction in queue gets routed to an agent.

Overflow handling

Webex CC supports overflow handling using Capacity Based Teams (CBT).

CBT is like a regular team with a capacity and an associated external DN that serves that capacity. It can be configured along with other teams in the Queue Call Distribution Cycles.

Usually, this is configured as the last cycle so that it acts as an overflow if no agent is available even after all the configured Call Distribution Groups fail to find an available matching agent for handling the interaction.

##### Agent Desktop Operations

When an agent logs in to Webex CC Agent Desktop, the agent specifies a phone number to which incoming calls to the agent can be connected. This can be a PSTN phone, Mobile phone or an extension if Agent is a Cisco Webex Calling user.

Note that this number must be a valid phone number to which calls can be routed. In case it is not, the agent cannot receive incoming calls.

Based on the type of interaction that the agent is handling, the widgets in the agent desktop supply the ability to perform certain media-control operations.

For example, once a call is answered, the agent can perform the following operations related to the call.

Place the call on hold

Initiate consult call and

Transfer the call to another phone number (say agent phone number) / Entry point

Conference another agent to the call

Transfer the call to another Queue

End the call

Agent desktop allows administrators to add custom widgets there by extending the desktop capabilities and making it a unified collection of widgets that agents need to get their work done in an efficient manner.

##### Desktop Architecture

Agent desktop is a micro frontend based single page application that hosts widgets built based on web components architecture. All the standard / stock widgets are powered by data that’s retrieved by APIs or server side push mechanisms.

These are typically, asynchronous APIs, where the response for an invocation, comes to desktop via a WebSocket connection.

Webex CC Agent Desktop authenticates users with Cisco Common Identity (CI) and the token is passed along to all API invocations. For custom widgets too, based on the authentication model, it provides a single sign-on experience to agents if the custom widget’s authentication model is integrated with CI.

Once an agent is part of an interaction, all updates to that interactions state or associated data too are pushed to desktop over the WebSocket connection.

##### Resiliency of desktop to connectivity and latency

The asynchronous API and server-side push enables scale and any connectivity loss to the WebSocket interface is detected and desktop attempts to re-connect and re-login.

The following figure illustrates the agent desktop architecture in Webex CC.

Agent Desktop Architecture

#### Administration and Configuration

##### Onboarding Customers

Webex Control Hub is the primary interface used by partners and customers for onboarding customers and enabling or configuring features.

Once the organization and contact center features are provisioned in Control Hub, it will trigger a workflow in Webex CC which does rest of the steps in the provisioning all of contact center capabilities as per the offerings chosen by the customer.

All the contact center provisioning is done using a BPM workflow engine which enables a declarative way to define the steps involved and makes the entire provisioning steps resilient to failures and ensures data integrity.

The following figure illustrates the provisioning workflow in Webex CC.

Customer Onboarding Workflow

##### Configuration Entities

The key configuration entities in Webex CC, scoped within an organization, are:

Site

Site stands for a location where one or more teams, users (agents / supervisors) are located.

Every user and team must belong to a site.

Team

A group of users. Teams are used to distribute interactions to agents via queues.

Every team must belong to a site.

Agents

Users who can login to Agent Desktop and handle interactions across the media types that are configured in the Webex CC.

Supervisors

Supervisors are assigned to teams and can monitor/ coach the agent and have access to team level status and agent statistics for those belonging to the teams that the supervisor is assigned to.

Queue

A queue is a logical entity where interactions can be held, while waiting for agents to be available, which then gets routed to the agent.

Queues are mapped to teams, as the search space for agents, with ability to expand the search space based on the elapsed time threshold, by adding other teams to the search space.

Entrypoint

Entrypoint is a logical entity representing the ingress point for interactions to come in to Webex CC. For telephony this primarily maps to the phone number to which calls arrive and for email / messaging channels, the Entrypoint points to asset configuration in Webex Connect.

Flow

The flow associated with entry point (via Routing Strategy), which decides the steps involved in handling interactions.

For non-telephony channels (email, messaging/social), Flow is chosen as part of Asset configuration in Webex Connect.

##### Access control for multi-sites contact centers

Webex CC Administrators can configure user profiles with access rights to specific sites, teams, queues, and entry points. Further, due to the hierarchical nature of sites and teams, once access to specific sites are provided, only the teams or date pertaining to the teams, belonging to those sites or an explicitly specified subset of such teams, can be accessed by the user.

For queues and entry points, they are global at organization level, so for different geographical locations (sites where specific agents and teams are located) separate entry points and queues can be configured, and supervisors / users can have access to those entities that are appliable for specific sites.

The following figure illustrates the key configuration entities and user profile that references these entities.

Configuration Entities Mapped to User Profile

Apart from restricting access to these entities, the Webex CC administrators can control the specific capabilities/modules that a user can access in the administration interface, thereby having users with administration /configuration rights to specific entities as well as sections/ capabilities of the Webex CC administration interface.

#### Reporting and Analytics

Webex CC processes the discrete events generated by various services during the life cycle of interactions, using a series of real-time stream processing services and generates a defined set of real-time datasets that are published to subscribed clients.

Further, these events are further processed, transformed, and aggregated and resulting datasets are persisted, which then gets retrieved via the data consumption APIs and the reporting and data visualization interface – Analyzer.

The following figure illustrates the data processing and consumption interfaces in Webex CC

Webex CC data processing pipeline and consumption interfaces

### Integrations

All external integrations to WxCC to augment and enhance the capabilities that customers can use, is using standard published APIs.

The type of API interfaces that are available in Webex CC are:

REST API

Server-Side Push using

Webhooks

WebSocket messages

#### CRM Integrations

Webex CC supports two modes of integration with Customer Relationship Management (CRM) systems.

Desktop Embedded Connectors

Flow integrations via HTTP(S) Connectors in the IVR

##### Desktop embedded connectors: CRM application as the primary interface

In this mode of operation, agent login into the CRM console as the primary application.

Webex CC is an embedded application (also called an embedded desktop application or embedded softphone) which is primarily used to login to the contact center and receive Webex CC routed contact center interactions.

Upon receiving a call or a conversation request, the CRM integration performs the following actions on the CRM console

Screen pop the Customer record tied to the ANI or other call associated data.

Post Call Metadata as Activity Notes on the Customer Record

Allow the agent to “Click to Call” by clicking on the Contact inside the CRM and initiating an outbound call to the customer

Posting Call Records into the CRM Reporting tables for Primary Reporting on the CRM.

Provides the full functionality of the Agent Desktop and call controls (embedded and minified version of the desktop app)

The primary mode of integration with the CRMs is by embedding Webex CC Desktop application in a separate iFrame.

Further the Webex CC Desktop application runs a custom headless widget (no user interface) runs in the background, interacting with the underlying CRM system to perform automated actions on behalf of the Agent.

The interactions are powered by two SDKs that the headless widget uses.

Webex CC Desktop JS SDK: This is the JavaScript SDK provided by Webex CC to register event listeners for agent and contact actions.

CRM JS SDK: This is the CRM client SDK applicable per CRM that abstracts REST API calls with the CRM. For example, for Salesforce, the CTI JS library provided by Salesforce is used to perform actions and listen for events inside the CRM.

The following figure illustrates the CRM embedded Webex CC desktop and connector architecture

CRM Connector Embedded Desktop Connector Architecture

Webex CC supports the following CRM solutions for the above mentioned integration:

For more information about configuring the Webex CC desktop layouts for enabling the CRM connector, feature sets, and changelogs, visit https://github.com/Ciscodevnet/webex-contact-center-crm-integrations .

##### Global availability of CRM connectors

The CRM Connectors are available in all geographies and regions where Webex CC is operational.

##### Elastic scale and performance

Webex CC hosts the custom widget that enables bidirectional communication between the CRM application and the Webex CC desktop in AWS CloudFront CDN ensuring high availability of the widget AWS across availability zones and regions.

All the CRM integration specific compute happens on the browser where agents are using the CRM application with Webex CC desktop embedded in the CRM application.

##### Security

The CRM connectors are invoked via the Webex CC agent desktop layout and optional parameters are passed via the desktop layout into the widget to toggle features on and off.

For example, to enable the Salesforce actions widget, the administrator can turn on the desktop layout parameter setting sfdcWidgetEnabled to true.

##### Package Installation

For the integration to work bi-directionally, the CRM Console needs the embedded application installed. This is to support loading the Desktop application inside of an iFrame.

All the Desktop Embedded connectors are available on the CRM marketplace.

for example,

ServiceNow: https://store.servicenow.com/sn_appstore_store.do#!/store/application/6c8e2a4edbc73410e1c75e25ca961947/1.0.5?

Zendesk: https://www.zendesk.com/marketplace/apps/support/202570/webex-contact-center/

The marketplace application installation activates the required plugins and imports the required XML files into the CRM console to support the reporting of call records on the CRM.

##### Flow integrations via HTTP(S) connectors in the IVR

The Webex CC Flow builder supports bi-directional data flows between Webex CC and the CRM system using HTTP(S) connectors configured in Webex Control Hub and used on the Webex CC Flow.

These are primarily used for personalization within the voice interactions and customized routing within the IVR.

By default, Webex CC supports the Salesforce HTTP Connector on Control Hub. The other CRM connectors can be added as Custom Connectors on Webex Control Hub.

For more information on the HTTP Connectors, visit https://github.com/CiscoDevNet/webex-contact-center-crm-integrations .

IVR HTTP Connectors :

Salesforce IVR HTTP Connector (In-built): https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/Salesforce/salesforce-ivr-http-connector

Zendesk IVR HTTP Connector (Custom): https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/Zendesk/zendesk-ivr-http-connector

ServiceNow IVR HTTP Connector (Custom): https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/ServiceNow/servicenow-ivr-http-connector

#### Outbound Campaign Management

Webex CC supports outbound preview campaigns using campaign management solution by Acqueon.

For more information, see Configure Voice Outbound Campaign Modes in Webex
                Contact Center .

#### Workforce Optimization

Webex CC supports workflow optimization and quality management solutions from leading industry vendors.

#### Extending Agent Desktop

Webex CC agent and supervisor desktop enables extension of the desktop capabilities by developing and running custom widgets with in the desktop.

For more details, visit https://developer.webex-cx.com/documentation/guides/desktop .

#### Other APIs

For details on the other API integrations that can be performed in Webex CC, visit https://developer.webex-cx.com/documentation/getting-started/ .

### Deployment and Connectivity

Webex CC is deployed in AWS and is currently available in the following regions

US

US-East N Virginia

US-West N California (Voice Media Ingress only)

Canada

Central

UK

London

Europe

Frankfurt

Asia Pac

Tokyo

Sydney

- Singapore

Connection to AWS hosted Webex Contact Center can be established either using Internet or
            using Amazon Web Services (AWS) Direct Connect. With AWS Direct Connect, data is
            delivered through a private network connection between customers on-premise network and
            Webex Contact Center thus improving the connection. For more details, refer to AWS Direct Connect for Webex Contact Center .

#### Multi Region Connectivity for Telephony

To enable global organizations, with agents and customers at multiple geographical locations, Webex CC supports keeping the media within the local region, for those regions where the voice media edge and ingress services are running.

The following figure illustrates multi region deployment with regional media.

Multi Region deployment with regional media

The media edge and ingress services are deployed in the following regions.

Geo Region

Webex CC Services (AWS Region)

Media Edge (Webex Calling Edge)

Next Generation Media Services (AWS Region)*

US

N Virginia

Chicago

Dallas

Los Angeles

New Jersey

N Virginia

N California

Canada

Central

Vancouver

Toronto

Central

Brazil

Sao Paulo

Europe

Frankfurt

Frankfurt

Amsterdam

Frankfurt

United Kingdom

London

Manchester

London

London

India

Mumbai

Mumbai

Singapore

Singapore

Singapore

Japan

Tokyo

Tokyo

Osaka

Tokyo

Australia

Sydney

Melbourne

Sydney

Sydney

Middle East and Africa

South Africa (Cape Town)

UAE

Saudi Arabia

South Africa (Cape Town)

UAE

Saudi Arabia

### Security and Privacy

#### Infrastructure Security

##### Compute infrastructure security

Webex CC compute instances are provisioned in AWS and services run as pods in Kubernetes cluster which has multiple namespaces and access to each namespace is restricted with separate credentials.

All the infrastructure provisioning is done using code – no manual steps – and none of the credentials can be accessed manually.

There is a central credential store with specific paths configured for specific set of services / teams and the access to the credential store itself is restricted and configured as secrets in the build and deployment systems.

None of the infrastructure components / services are directly exposed outside of the AWS VPC and only publicly exposed interfaces are APIs and WebSocket Servers which are controlled and managed using api gateway,

Apart from this, there are certain internal systems and interfaces used by developers that are used for viewing logs, metrices, deployment details, build status and test results, which are secured using roles and groups and integrated with Cisco internal authentication systems.

##### Authentication and authorization for user interfaces

All the user interfaces used by various contact center users (agents, supervisors, administrators, analysts) are protected by Cisco Common Identity based bearer token authentication (OAuth flows).

The authorization is done using roles for the user who obtained the token and scopes assigned to the token.

#### Data Security

##### Data in transit

None of the interfaces of the services / infrastructure component deployed are directly exposed to external incoming traffic.

Select services, with http APIs expose those interfaces via a gateway and all incoming https (including those of WebSocket) are terminated in the ALB and internal traffic over http is routed to the services.

All outgoing interactions are over https / TLS (for non http protocols).

Inside of the VPC, the internal communication between services – over http / custom TCP protocol – are over plain TCP socket.

##### Data at rest

All data that gets stored are encrypted at storage layer. Further those data stores that are outside of VPC, are protected and access control and authorizations with credentials securely stored and managed in a secret store.

The following figure illustrates the data flow and security model for transit as well as at rest.

Data Security in Transit and at Rest

#### Data Privacy

##### End user PII data

The Webex CC Flow, which is the programmatic controller for handling interactions, can be used to collect user data, which can be assigned to flow variables specially tagged as ‘Contains Sensitive Data’. The values for such data are encrypted and no services in the transit path of the data will have access to this data.

Further, such data is never persisted in Webex CC reporting data store and the logs / messaging infrastructure will have encrypted data and clear text data is not stored anywhere within Webex CC.

##### Contact Center Agent/Supervisor PII data

The contact center user related data is redacted in logs but available for data analytics and visualization in the Webex CC data store.

#### Scalability

##### Factors for scale

For Webex CC the factors that impact the scale are:

Concurrent number of agents logged in

Concurrent number of interactions in progress

Actions performed on those interactions

Concurrent number of actions that supervisors / agents perform, outside of handling the interactions

Volume of the data generated and persisted

##### Architectural aspects enabling scale

The principles based on which Webex CC is architected and designed enables the solution to scale dynamically as needed within the limits enforced by the infrastructure provisioned for the various services and platform components.

Event driven architecture

The services in Webex CC communicate using messages and the critical message processing flows does not involve any blocking IO operations and the state required for processing messages is localized to the instance of the service that’s processing the message.

Stateless services (or externalized state)

Stateless services enable elasticity by easily adding /removing additional instances of the services. There are certain services that are inherently stateful in nature and those have externalized state store and the infrastructure supports dynamic changes to the number of instances of such services too with automatic rebalancing / state transfer / localizing the state to the instance that needs the state.

Elastic infrastructure

All the services run in Kubernetes and the infrastructure aka Kubernetes nodes scale automatically based on the usage and this enables dynamically adding more compute nodes up to a maximum high threshold that’s pre-configured.

Load projection and regular validation

All the services are benchmarked for the performance characteristics and scaling pattern is validated at the service level.

Further continuous validation, peak load and endurance tests are conducted with test parameters tuned for projected growth in the scale impacting attributes, which enables to identify bottlenecks, plan to the update the high threshold for infrastructure resource usage and be ready for the game day.

### Reliability and Availability

The event driven architecture and stateless services enables resiliency and elasticity. However, to ensure that failures are detected and acted upon before functionalities are impacted, Webex CC employs the following strategy.

Infrastructure Availability and Reliability

All Webex CC services, and infrastructure components are always deployed across three AWS availability zones.

This enables Webex CC to be resilient to availability zone failures and in case of failures, the failed instances are replaced with newer ones automatically.

Continuous Monitoring and Alerting

Internal and External Probes for Services and Infrastructure components, which on failure trigger alerts.

Metrics captured from services and infrastructure components and processed through a rule engine which detects matching rules and trigger alerts.

Continuous Validation and Alerting

Periodic Tests are run and any failures results in triggering alerts

These alerts create proactive incidents and are handled as a real incident that impacts customer.

This pre-empts impacts to customer and contributes towards system availability and reliability.

Continuous Integration and Delivery

This is the engineering process and delivery pipeline and enables quick and reliable build, validation, and deployment of services / changes to services in Webex CC.

The ability to do completely automated deployment – from code to production environment, with all the required validations, reduces risk and minimizes the time to resolution, if a change needs to be deployed in response to a failure.

Circuit Breakers and Kill Switches

Various parts of the system / certain capabilities of Webex CC can be selectively disabled for all customers or select customers, to minimize cascading effects of a failure.

This enables to minimize the failure surface and achieve availability of core contact center capabilities to customers.

#### Monitoring and Failure Detection

The following figure indicates the continuous monitoring, validation, and alerting mechanisms in place for Webex CC.

Continuous Monitoring and Failure Detection

#### Business Continuity and Disaster Recovery

The Disaster Recovery and Business Continuity process ensures to detect any large-scale outage within a region and required steps are put in place to ensure recovery of the services to customers that are on board in the region.

The steps for recovery are documented, validated, and kept updated regularly as per the Disaster Recovery and Management processes.

Webex Contact Center services are deployed in three separate availability zones within an
            AWS region. Each availability zone is a different physical location in the region, with
            independent utilities.

### Compliance and Certifications

Webex Contact has an extensive list of security certifications. These certifications are kept up to date at regular intervals.

PCI DSS QSA

CAIQ

HIPAA & HITECH

CSA Star Level 1

CSA Star Level 2 (3rd party independent assessment)

SOC2

ISO27001 (International standard for information security)

ISO27017 (Security standard for cloud service providers)

ISO27018 (Security standard focused on protecting personal data in the cloud)

ISO27701 (Data privacy extension)

C5 German standard, demonstrating operational security against cyber-attacks

Refer to Webex Contact Center Service Privacy Data Sheet for more details.

| Geo Region | Webex CC Services (AWS Region) | Media Edge (Webex Calling Edge) | Next Generation Media Services (AWS Region)* |
|---|---|---|---|
| US | N Virginia | Chicago Dallas Los Angeles New Jersey | N Virginia N California |
| Canada | Central | Vancouver Toronto | Central |
| Brazil |  | Sao Paulo |  |
| Europe | Frankfurt | Frankfurt Amsterdam | Frankfurt |
| United Kingdom | London | Manchester London | London |
| India |  | Mumbai | Mumbai |
| Singapore |  | Singapore | Singapore |
| Japan | Tokyo | Tokyo Osaka | Tokyo |
| Australia | Sydney | Melbourne Sydney | Sydney |
| Middle East and Africa |  | South Africa (Cape Town) UAE Saudi Arabia | South Africa (Cape Town) UAE Saudi Arabia |