---
doc_id: developer-cisco-com-docs-task-routing-task-routing-overview-ca08b7d524
source_url: https://developer.cisco.com/docs/task-routing/task-routing-overview/
retrieved_at: 2026-09-01T17:34:40.404812+00:00
---

SocialMiner Product Name Change

Starting 12.5(1), SocialMiner has been renamed to Customer Collaboration Platform and the software is available under Unified Contact Center Express (https://software.cisco.com/download/home/270569179). All behavior and functionalities of the component with respect to Task Routing APIs remain the same.

# What is Task Routing?

Task Routing constitutes the ability to route tasks of any nature to human experts in a Customer Care center or even bots and programs.

Tasks are actionable events which require the attention of human experts or other intelligent agents. Examples of tasks are:

## Why should you use the Task Routing APIs?

Task Routing APIs bring the power of Cisco Contact Center Enterprise (CCE) to third-party multichannel applications. It enables these applications to send task requests to experts based on business rules, regardless of the media.

Task Routing APIs provide a standard way to request, queue, route, and handle third-party multichannel tasks in the CCE environment.

## What you get as part of the Enterprise platform?

The Cisco Contact Center Enterprise system provides the mechanism to:

- administer the routing

- manage agents

- draw reports

The APIs enables the integration of the third-party application with the underlying CCE platform. These APIs are logically split into two parts.

- submit task requests to CCE

- get expected wait time(s)

- get the status of route request(s)

- get the assigned agent ID

- cancel task(s)

- login/logout

- change state (Ready/Not Ready)

- accept

- pause/resume

- complete

- transfer a task

## What Are The Business Benefits?

- Task Routing APIs brings you the Contact Center as a packaged service which frees you to focus on providing the integration and media handling for any arbitrary channel type.

- Out of the box, it provides routing, reporting, and administration.

- Third-Party developers can cater to the specific needs of end customers and also region specific channel types.

- Due to technology rapidly changing, end customers now expect ubiquitous, contextual, and extremely proactive customer service. Alongside the full power of the Cisco customer care platform, the Task Routing APIs will fulfill these customer's needs.

Here are some specific use cases where Task Routing APIs solve the problem:

## As a developer, what can I build using the Task Routing APIs?

Contact Center customers or partners can use the Task Routing APIs to develop specialized applications that was not built by Cisco as part of the platform.

There are various types of applications that can be built:

- Person to person: end customer getting support from a human agent

- Person to machine: end customer getting support from a powerful self-service mechanism such as bots and machine learning

- Machine to person: an industrial device that is remote debugged by a skilled technician using multichannel media (video and device API results show up on a neatly designed web interface)

- Machine to machine: an assembly line controller gets queued to a central controller for necessary reconfiguration data

Example applications can be:

- A web or mobile application that is used by the end customer to request support.

- An application on a device that automatically informs the service or support department when issues occur.

- A web or mobile application, or even a Finesse gadget that can be used by the agents who are handling these tasks.

In all of these examples, we have a third-party built applications enabling expert entities to handle tasks of multiple medias while seamlessly switching between tasks.

# Technical Overview

The above schematic diagram provides a bird’s eye view of a simple Enterprise deployment along with proposed third-party multichannel applications. The Task Routing REST APIs is the basis for the integration between the Unified CCE platform and the third-party application.

### Cisco Contact Center Enterprise

The Cisco Contact Center Enterprise platform is comprised of the following components:

- Customer Collaboration Platform

- Finesse

- Routing

- Administration

- Reporting

Note : Starting 12.5(1), SocialMiner has been renamed to Customer Collaboration Platform and the software is available under Unified Contact Center Express . All behavior and functionalities of the component with respect to Task Routing APIs remain the same.

#### Customer Collaboration Platform

The Unified CCE Enterprise deployment of any nature or scale must include Customer Collaboration Platform.

The Task Route Request APIs are served by Customer Collaboration Platform on the ingress side. If the third-party application needs to be on the internet to service requests from customers, then Customer Collaboration Platform is recommended to be put in the demilitarized zone (DMZ).

#### Finesse

The Task Control APIs are served by Cisco Finesse on behalf of the Agent. Agents usually are within the enterprise. Finesse is a mandatory part of the CCE deployment.

### Third-Party Multichannel Application

Third-party developed applications can take various shape and form, but it always has an ingress side and an egress side.

Ingress side is where tasks are initiated. The developer is responsible for providing the interface via which the task is submitted or the mechanism by which the event is pushed. Besides forming and pushing the task, the ingress side also provides the necessary feedback to the initiating entity (human or machine) such as:

- expected wait time before an agent is assigned to the task

- status of route request

- display the assigned Agent ID (if applicable)

- cancel the task for situations where the submitter decides to abort the request

Egress side is where third-party application provides the Agent (or expert entity) all the necessary means to handle or service the Task.

The steps taken by an Agent are typically as follows:

- login/logout on the agent desktop or for a particular channel

- change state (Ready/Not Ready) on the agent desktop or for the particular channel

- accept a task signaling his/her willingness to handle the task

- pause/resume

- complete a task to signal that work is done

- transfer a task to some other queue or Agent

## Task Routing REST APIs

Task Routing API set can be grouped along these subsets:

Task Submission APIs

- Create Request API - sends multichannel route requests to CCE

- Request Status API - polls status of a route request, gets the EWT, Agent/Task IDs once agent is assigned

- Cancel Request API - cancels task requests that are in Queue

Agent State Control APIs

- Login/Logout API - logs in / logs out agents on different media channels

- State control API - changes agent states on different media channels

Task Control APIs

- Accept API - accepts tasks reserved to an agent

- Complete API - finishes/closes tasks the agent is working on

- Pause API - pauses tasks the agent is working on

- Resume API - resumes paused tasks

- Transfer API - transfers a task to another agent specified queue

Other list APIs

- Get Media List API - retrieves the list of all media channels for a specific agent or across all Media Routing Domains configured in CCE

- Get Dialog List API - retrieves the list of non-voice dialogs for a user

For more details and a full list of Task Routing APIs, please see the Task Routing Developer Guide .

## XMPP Notifications

As shown in the API listing above, there are APIs to get the task request status. Similarly, there are APIs which provide the Agent state change information or Agent action on the task. However, the only way to use these API is via periodic polling.

All will agree that polling is not the best approach beyond the minimalist implementation. Hence the provision of XMPP notifications.

On the ingress or customer side, Customer Collaboration Platform subscription provides task change events for:

- Task status change - Queued, Reserved, Handled, Discarded, EWT

- Task operations - Re-queue, Re-notify

In order to receive these events, the application will need to subscribe to ccp.campaign.updates.Cisco_Default_Task_Campaign.

And on the egress or Agent side, Finesse subscription provides Agent & task change events for:

- Agent changes - Add, Delete, State, Name, Role

- Task/Call updates - Accept, Complete, Pause, Resume, Transfer

For more information about the Finesse subscription, please visit Cisco Finesse Notification Service .

# What can a developer do with Task Routing APIs?

Task Routing APIs help connect entities which need care to entities which can provide care – not limited to humans. The request for care is encapsulated as a task.

The platform provides the skills based and precision routing capabilities to assign the task to an agent. As a developer, you need to build the integration and provide the media handling mechanism necessary to dispense the care.

The steps involved are:

- Create a task on behalf of the care seeker (‘customer’) and inject it into the Enterprise platform.

- Check the status and update the care seeker – visually or otherwise

- Accept the task by the agent

- Upon acceptance, establish the media channel between the customer and the agent

- Provide all the facility to the agent to provide the necessary care to the customer

- Provide information about the business logic scripts, configurations, and all other supporting data for the Task Routing scenario to work.

# Next Steps

Without further ado, lets dive in to get our hands dirty. Please proceed to the Getting Started page to learn how to use the Task Routing APIs to implement a cool use case.

Next

| On the consumer side, the Task route request APIs enable applications to: submit task requests to CCE get expected wait time(s) get the status of route request(s) get the assigned agent ID cancel task(s) | On the Agent side, the Task control APIs enable agents to: login/logout change state (Ready/Not Ready) accept pause/resume complete transfer a task |
|---|---|

| Use Case | Solution |
|---|---|
| A Contact Center Enterprise customer gets a request from their largest client base that they want to provide chat as a customer service option. Their client already uses a popular app for chat - personal use as as well as business. | A developer can integrate this particular chat app via the Task Routing APIs to route the tasks to the clients' care agents. This allows the customer to extend care via the same app while not needing to re-train their care agents to use a different tool. |
| A manufacturing firm in an emerging market has acquired a bunch of units located in different areas. Their technicians are finding it difficult to manage the newly acquired units effectively. | A developer can help build an application that continuously checks each unit, then analyzes the issue(s) and automatically assigns a technician based on expertise and location. This allows each technician to focus only on the units with issues, which will free up their time. Also, they would be able to efficiently resolve these issues since they have the most knowledge. |
| A banking system monitors transactions by consumers for the purpose of fraud detection and alleviation. Obviously, speed is of the essence here. While the monitoring mechanism can be made more intelligent, how fast the company reaches out to the customer is integral to the success of the fraud detection. | Task routing can allow an efficient routing mechanism instead of experts staring at dashboards. The bank can integrate automatic user preference based contact/notification to the customer via text message or mobile app notification. |