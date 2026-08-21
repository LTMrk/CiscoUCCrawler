---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-maintenance-guide-pcce-b-1501-f-3e23ff7ca3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/maintenance/guide/pcce_b_1501_features-guide/rcct_m_1501_task-routing.html
retrieved_at: 2026-08-21T12:11:09.621573+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Task Routing

## Chapter: Task Routing

# Task Routing

## Introduction

Task Routing describes the system's ability to route requests from different media channels to any agents in a contact center.

You can configure agents to handle a combination of voice calls, emails, chats, and so on. For example, you can configure
                              an agent as a member of skill groups or precision queues in three different Media Routing Domains (MRD) if the agent handles
                              voice, e-mail, and chat. You can design routing scripts to send requests to these agents based on business rules, regardless
                              of the media. Agents signed into multiple MRDs may switch media on a task-by-task basis.

Enterprise Chat and Email provides universal queue out of the box. Third-party multichannel applications can use the universal
                              queue by integrating with CCE through the Task Routing APIs.

Task Routing APIs provide a standard way to request, queue, route, and handle third-party multichannel tasks in CCE.

Contact Center customers or partners can develop applications using Customer Collaboration Platform and Finesse APIs in order
                              to use Task Routing. The Customer Collaboration Platform Task API enables applications to submit nonvoice task requests to
                              CCE. The Finesse APIs enable agents to sign into different types of media and handle the tasks. Agents sign into and manage
                              their state in each media independently.

Cisco partners can use the sample code available on Cisco DevNet as a guide for building these applications ( https://developer.cisco.com/site/task-routing/ ).

### Customer Collaboration Platform and Task Routing

Third-party multichannel applications use Customer Collaboration Platform'sTask API to submit nonvoice tasks to CCE.

The API works in conjunction with Customer Collaboration Platform task feeds, campaigns, and notifications to pass task requests
                                 to the contact center for routing.

The Task API supports the use of Call variables and ECC variables for task requests. Use these variables to send customer-specific
                                 information with the request, including attributes of the media such as the chat room URL or the email handle.

CCE solutions support only the Latin 1 character set for Expanded Call Context variables and Call variables when used with
                                             Finesse and Customer Collaboration Platform. Arrays are not supported.

### CCE and Task Routing

CCE provides the following functionality as part of  Task Routing:

Processes the task request.

Provides estimated wait time for the task request.

Notifies Customer Collaboration Platform when an agent has been selected.

Routes the task request to an agent, using either skill group or precision queue based routing.

Reports on contact center activity across media.

### Finesse and Task Routing

Finesse provides Task Routing functionality via the Media API and Dialog API.

With the Media API, agents using third-party multichannel applications can:

Sign into different MRDs.

Change state in different MRDs.

With the Dialog API, agents using third-party multichannel applications can handle tasks from different MRDs.

## Task Routing Deployment Requirements

Task Routing for third-party multichannel applications deployment requirements:

Finesse and Customer Collaboration Platform are required. Install and configure Finesse and Customer Collaboration Platform
                                 before configuring the system for Task Routing.

See the Finesse documentation and Customer Collaboration Platform documentation .

By default, access to the Customer Collaboration Platform administration user interface is restricted. Administrator can provide
                                 access by unblocking the IP addresses of the clients. For more details, see the Control Customer Collaboration Platform Application Access topic in the Cisco Customer Collaboration Platform Installation and Upgrade Guide guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-guides-list.html .

You can install only one Customer Collaboration Platform machine in the deployment.

Customer Collaboration Platform must be geographically co-located with one side of the Media Routing Peripheral Gateway (MR
                                 PG).

Install Customer Collaboration Platform in a location from which CCE, Finesse, and the third-party multichannel Customer Collaboration
                                 Platform Task Routing application can access it over the network.

If you install Customer Collaboration Platform in the DMZ, open a port for CCE and Finesse to connect to it. The default port
                                 for CCE to connect to Customer Collaboration Platform is port 38001. Finesse connects to Customer Collaboration Platform over
                                 HTTPS, port 443.

Install the third-party multichannel application locally with Customer Collaboration Platform, or open a port on the Customer
                                 Collaboration Platform server for the application to connect to it.

### Supported Functionality for Third-Party Multichannel Tasks

Blind transfer is supported for third-party multichannel tasks submitted through the Task Routing APIs.

We do not support the following functionality for these types of tasks:

Agent-initiated tasks.

Direct transfer.

Consult and conference.

### Plan Task Routing Media Routing Domains

Media Routing Domains (MRDs) organize how requests for each communication medium, such as voice and email, are routed to agents.
                              You configure an MRD for each media channel in your deployment.

Finesse agents can sign in to any of the multichannel MRDs you create for Task Routing.

Consider the following important factors when planning your MRDs:

Whether the MRD is interactive

The maximum number of concurrent tasks that an agent can handle in an MRD

Whether the MRDs are interruptible

For interruptible MRDs, whether Finesse accepts or ignores interrupt events

To configure the settings and parameters described in the following sections, see the following documents:

Cisco Customer Collaboration Platform Developer Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html

Cisco Finesse Web Services Developer and JavaScript Guide

Packaged CCE— Unified CCE Administration and Configuration Manager Tools

#### Interactive and Non-interactive MRDs

Interactive tasks are tasks in which an agent and customer communicate in real time with each other, such as chats and SMS
                                 messages. The customer usually engages with the agent through an application, like a chat window, and leaves this application
                                 open while waiting to be connected to an agent. Non-interactive tasks are asynchronous, such as email. The customer submits
                                 the request and then may close the application, checking later for a response from an agent.

API Parameter or Setting

API/Tool

Possible Values

Interactive Task/MRD

Non-interactive Task/MRD

requeueOnRecovery

Whether Customer Collaboration Platform re-queues  re-queues or discards the task when Customer Collaboration Platform  recovers
                                             from a failure.

Set this parameter when submitting a task request.

Customer Collaboration Platform Task Submission API

False — customers are waiting at an interface for an agent and can be notified if there is a problem. You don't need to resubmit
                                             these tasks.

True — customers are not waiting at an interface for an agent, and there is no way to alert them that there was a problem. You
                                             need to resubmit these tasks.

dialogLogoutAction

Whether active tasks are closed or transferred when an agent signs out or loses presence.

Set this parameter when an agent signs in to a Media Routing Domain.

Finesse Media Sign In API

Close — customers are engaged with an agent, and can be notified that the task has ended.

Transfer — customers are not engaged with an agent, and there is no way to alert them that the task has ended.

Start Timeout

The amount of time that the system waits for an agent to accept an offered task. When this time is reached, the system makes
                                             the agent not routable and re-queues the task.

Set this parameter when configuring an MRD.

Media Routing Domains tool in Unified CCE Administration

Shorter duration — customer is waiting at an interface for the agent

Longer duration — customer is not waiting at an interface for an agent

Monitoring status of submitted tasks

You can monitor status of submitted and queued tasks using either the Customer Collaboration Platform  Task API to poll for
                                             status or Customer Collaboration Platform  XMPP BOSH eventing.

Customer Collaboration Platform Task API or XMPP BOSH eventing

Use Customer Collaboration Platform Task API status polling for MRDs when you want to monitor the status of a single contact/task.

Use Customer Collaboration Platform XMPP BOSH eventing to receive updates on all contacts/tasks in the campaign supporting
                                             Universal Queue over one channel.

#### Maximum Concurrent Tasks Per Agent

You can specify the maximum number of concurrent tasks for an agent in an MRD signing into the Finesse application, using
                                 the maxDialogLimit parameter in the Finesse Media — Sign In API .

For agents handling interactive tasks, consider how many concurrent tasks an agent can handle reasonably. How many simultaneous
                                 chat sessions, for example, can an agent handle and provide good customer care? If you are using precision queue routing,
                                 keep in mind that CCE assigns tasks to agents who match attributes for step one, up to their task limit , until all of those agents are busy. CCE then assigns tasks to agents who match attributes for step two, up to their task
                                 limit, and so on.

#### Interruptible and Non-Interruptible MRDs

When you create an MRD in the Unified CCE Administration Media Routing Domains tool, you select whether the MRD is interruptible.

Interruptible: Agents handling tasks in the MRD can be interrupted by tasks from other MRDs. Non-interactive MRDs, such as an email MRD,
                                       are typically interruptible.

Non-interruptible: Agents handling tasks in the MRD cannot be interrupted by tasks from other MRDs. The agents can be assigned tasks in the
                                       same MRD, up to their maximum task limits. For example, an agent can handle up to three non-interruptible chat tasks; if the
                                       agent is currently handling two chat tasks, CCE can assign the agent another chat, but cannot interrupt the agent with a voice
                                       call. Interactive MRDs, such as a chat MRD, are typically non-interruptible. Voice is non-interruptible.

When an agent is working on a non-interruptible task, CCE does not assign a task in any other MRD to the agent. Any application
                                 handling the non-voice MRDs must follow the same rule. In certain cases, it is possible that a task from another media routing
                                 domain gets assigned to an agent who is working on a non-interruptible task in an MRD.

For example, if an agent is working on a non-interruptible chat MRD and makes an outbound call (internal or external) using
                                 the desktop or phone, CCE cannot prevent the agent from making that call. Instead, the system handles this situation differently.
                                 CCE marks the agent temp not routable across all media domains until the agent has completed all non-interruptible tasks the
                                 agent is currently working on. Because of this designation, the agent is not assigned any new tasks from any MRDs until finishing
                                 all current tasks. Even if the agent tries to go ready or routable, the agent's temp not routable status is cleared only after
                                 all tasks are complete.

If you change the MRD from interruptible to non-interruptible or vice versa, the change takes effect once the agent logs out
                                             and then logs back in on that MRD.

#### Accept and Ignore Interrupts

### SUMMARY STEPS

- Specify whether an MRD accepts or ignores interrupt events when an agent signs into the Finesse application, using the interruptAction parameter in the Finesse Media - Sign In API . This setting controls the agent's state in an interrupted MRD and ability to work on interrupted tasks. The setting applies
                                    only when a task from a non-interruptible MRD interrupts the agent.

### DETAILED STEPS

Specify whether an MRD accepts or ignores interrupt events when an agent signs into the Finesse application, using the interruptAction parameter in the Finesse Media - Sign In API . This setting controls the agent's state in an interrupted MRD and ability to work on interrupted tasks. The setting applies
                                             only when a task from a non-interruptible MRD interrupts the agent.

Accept: When an agent is interrupted by a task from a non-interruptible MRD while working on a task in an interruptible MRD, Finesse
                                                accepts the interrupt event.

The agent, CCE task, and Finesse dialog state in the interrupted MRD change to INTERRUPTED.

The agent cannot perform dialog actions while a task is interrupted.

Important

The application is responsible for disabling all dialog-related activities in the interface when an agent's state changes
                                                                  to INTERRUPTED.

The agent's time on task stops while the agent is interrupted.

Example: An agent has an email task for 20 minutes, and is interrupted for 3 of those minutes with a chat task. The handled
                                                      time for the email task is 17 minutes, and the handled time for the chat task is 3 minutes.

Ignore: When an agent is interrupted by another task while working on a task in an interruptible MRD, Finesse ignores the interrupt
                                                      event.

The new task does not affect any of the agent's other assigned tasks. The agent, CCE task, and Finesse dialog state in the
                                                      interrupted MRDs do not change.

The agent can perform dialog actions on original task and the interrupting task at the same time. The agent's time on the
                                                      original task does not stop while the agent is handling the interrupting task.

Example: An agent has an email task for 20 minutes, and is interrupted for 3 of those minutes with a chat task. The handled
                                                      time for the email task is 20 minutes, and the handled time for the chat task is 3 minutes. This means that during a 20-minute
                                                      interval, the agent handled tasks for 23 minutes.

If an agent is working on a task in an interruptible MRD and is routed a task in another interruptible MRD, CCE does not send
                                                an interrupt event. Therefore, the interruptAction setting does not apply.

### Plan Dialed Numbers

Dialed numbers, also called script selectors, are the strings or numbers submitted with Task Routing task requests through
                              Customer Collaboration Platform. Each dialed number is associated with a call type, and determines which routing script CCE
                              uses to route the request to an agent.

Dialed numbers are media-specific; you associate each one with a Media Routing Domain.

For Task Routing, plan which dialed numbers the custom Customer Collaboration Platform application will use when submitting
                              new task requests. Consider whether you will use the same dialed numbers for transfer and tasks that are requeued on RONA,
                              or if you need more dialed numbers.

Important

You must associate each Task Routing dialed number with a call type. The default call type is not supported for Task Routing.

### Skill Group and Precision Queue Routing for Nonvoice Tasks

Routing to skill groups and precision queues is largely the same for voice calls and nonvoice tasks. However, the way that
                              contact center enterprise distributes tasks has the following implications for agents who can handle multiple concurrent tasks:

Precision queues —In precision queue routing, Unified CCE assigns tasks to agents in order of the precision queue steps. Unified CCE assigns
                                    tasks to agents who match the attributes for step one, up to their task limit, until all those agents are busy. Unified CCE
                                    then assigns tasks to agents who match attributes for step two, and so on. If you configure agents to handle three concurrent
                                    tasks, Unified CCE assigns three tasks to each agent in the first step. It then moves on to the second step and assigns any
                                    remaining tasks to those agents.

Overflow skill groups —Routing scripts can specify a preferred skill group and an overflow skill group. Unified CCE assigns tasks to all agents
                                    in the preferred skill group, up to their task limit, before assigning any tasks in the overflow skill group. If you configure
                                    agents to handle three concurrent tasks, Unified CCE assigns three tasks to each agent in the preferred skill group. It then
                                    moves on to the overflow skill group and assigns any remaining tasks to those agents.

The number of available slots is an important factor in the Longest Available Agent (LAA) calculation.

The number of available slots = The maximum concurrent task limit for the MRD that an Agent has logged into - Current tasks being handled by the Agent or routed to the Agent.

If there are multiple skill groups that are part of the queue node, then the skill group that has the higher LAA is picked.
                                                Then, the agents within the picked skill group (or the Precision Queue) who have the highest number of available slots for
                                                non-voice tasks get prioritised.

Agents with the same number of available slots get prioritized based on the time in the available state or the LAA mechanism.

### Agent State and Agent Mode

An agent's state and routable mode in an MRD work together to determine whether CCE routes tasks to the agent in that MRD.

#### Agent Routable Mode

The agent's routable mode controls whether CCE can assign the agent tasks in that MRD. If the agent is routable, CCE can assign
                                 tasks to the agent. If the agent is not routable, CCE cannot assign tasks to the agent.

The agent changes to routable/not routable through Finesse Media - Change Agent to Routable/Not Routable API calls.

#### Agent State

The agent's state in an MRD indicates the agent's current status and whether the agent is available to handle a task:

Ready: The agent is available to handle a task.

Reserved/Active/Paused/Work Ready/Interrupted: The agent is available to handle a task if the agent has not reached their
                                       maximum task limit in the MRD.

Not Ready: The agent is not available to handle a task.

The agent changes to Ready and Not Ready through calls to the Finesse Media - Change Agent State API. The agent's state while
                                 working on a task depends on the actions the agent performs on the Finesse dialog related to the task, through calls to the
                                 Finesse Dialog - Take Action on Participant API.

#### How Mode and State Work Together to Determine if an Agent Receives Tasks

CCE will route an agent a task in the MRD if ALL of the following are true:

The agent's mode is routable, and

The agent is in any state other than NOT_READY, and

The agent has not reached the maximum task limit in the MRD, and

The agent is not working on a task in a different and non-interruptible MRD.

CCE will NOT route an agent a task in the MRD if ANY of the following are true:

The agent's mode is not routable, or

The agent is NOT_READY, or

The agent has reached the maximum task limit in the MRD, or

The agent is working on a task in a different and non-interruptible MRD.

#### Why Change the Agent's Mode to Not Routable?

By changing the agent's mode to not routable, you stop sending tasks to the agent without changing the agent's state to Not
                                 Ready. You may want to make an agent not routable if the agent is close to ending the shift, and needs to complete in progress
                                 tasks before signing out.

If an agent changes to Not Ready state while still working on tasks, CCE reports show those tasks as ended; time spent working
                                 on the tasks after going Not Ready is not counted. By making the agent not routable instead of Not Ready, the agent's time
                                 on task continues to be counted.

In RONA situations, in which agents do not accept tasks within the Start Timeout threshold for the MRD, Finesse automatically
                                 makes agents not routable. Finesse resubmits the tasks through for routing through Customer Collaboration Platform. The application
                                 must make the agent routable in order for the agent to receive tasks again.

### Customer Collaboration Platform and Finesse Task States

In most cases, Customer Collaboration Platform social contact states do not map directly to Finesse dialog states. For Customer
                              Collaboration Platform, social contacts are created when the customer submits a task request. For Finesse, the dialog with
                              which the agent engages with the customer is created when the task is routed to the agent.

This table shows the relationships between Customer Collaboration Platform social contact task states and Finesse dialog states.

Customer Collaboration Platform Social Contact Task State

Finesse Dialog State

Unread: The task request has not been submitted to the contact center.

None

Queued: The task request is successfully submitted to the contact center as a result of creating a new task or resubmitting a task
                                          due to agent transfer, automatic transfer on agent logout, or automatic transfer for RONA.

None

Reserved: The task is assigned to an agent. This state includes all work on a task.

Offered: The dialog is being offered to the agent.

Accepted: The agent accepted the dialog but has not started working on it.

Active: The agent is working on the dialog.

Paused: The agent paused the dialog.

Wrapping Up: The agent is performing wrap up activity on the dialog.

Interrupted: The agent is interrupted with a task from a non-interruptible Media Routing Domain. The agent cannot work on this task until
                                          the interrupting task is complete.

Handled: Customer Collaboration Platform receives a handled notification from Finesse indicating that the task ended.

Closed: The agent ended the task. Finesse sends a handled notification to Customer Collaboration Platform.

## Task Routing API Request Flows

### Task Routing API Basic Task Flow

This topic provides the Customer Collaboration Platform and Finesse API calls and events when an active email task is interrupted by a chat request.

In this scenario, the email MRD is interruptible. When the agent signs into the email MRD, the application uses the Finesse
                              Media API to accept interrupts. The chat MRD is non-interruptible.

The email application submits a new email task request to CCE, and polls for status and Estimated Wait Time (EWT).

An agent signs in to the email MRD and changes state to Ready.

3. CCE assigns the agent the email task. The Call and ECC variables used to create the task are included in the dialog's media
                                    properties, and contain information such as the handle to the email. The variables can be used to reply to the email. The
                                    agent starts work on the email dialog in Finesse.

The chat application submits a new chat request, and polls for status and EWT. The same agent logs into the chat MRD.

The agent changes state to Ready in the chat MRD. CCE assigns the chat task to the agent. The Call and ECC variables used
                                    to create the task are included in the dialog's media properties, and contain information such as the chat room URL. The variables
                                    can be used to join the chat room with the customer. The agent starts the chat dialog in Finesse. The Email dialog is interrupted.

The agent completes work on the chat dialog and closes the dialog. Finesse sends a handled event to Customer Collaboration Platform for the chat task. The application is responsible for closing the chat room. The agent is not handling other non-interruptible
                                    dialogs, and the email dialog becomes active.

The agent continues working on the email dialog, including pausing, resuming, and wrapping up the dialog. The agent closes
                                    the dialog. Finesse sends a handle event to Customer Collaboration Platform for the email task. The application is responsible for sending the email reply to the customer.

### Task Routing API Agent Transfer Flow

This illustration provides the Customer Collaboration Platform and Finesse API calls and events when an agent transfers a
                              task.

The agent transfers the dialog from the Finesse application, selecting the script selector to which to transfer the task.

Finesse resubmits the task to Customer Collaboration Platform, and the task is queued to the script selector as a new task.

Finesse puts the original dialog in the CLOSED state, with the disposition code CD_TASK_TRANSFERRED. Finesse does not send
                                    a handled notification to Customer Collaboration Platform.

### Task Routing API RONA Flow

This illustration provides the Customer Collaboration Platform and Finesse API calls and events in a RONA scenario, in which
                              an agent does not accept an offered task within the Start Timeout threshold for the MRD.

The task is routed to an agent, and the dialog is offered to the agent.

The Media Routing Domain's Start Timeout threshold expires.

CCE instructs Finesse to end the dialog. Finesse puts the dialog in the CLOSED state, with the disposition code CD_RING_NO_ANSWER.
                                    Finesse does not send a handled notification to Customer Collaboration Platform.

The Finesse server on which the agent was last signed in resubmits the task to Customer Collaboration Platform with the original
                                    script selector. The task is queued to the script selector as a new task.

CCE instructs Finesse to make the agent not routable in that Media Routing Domain, so that the agent is not routed more tasks.

### Task Routing API Agent Sign Out with Tasks Flows

The Finesse Media - Sign Out API allows agents to sign out with assigned tasks. The dialogLogoutAction parameter set by the
                              Media - Sign In API determines whether those tasks are closed or transferred when the agent signs out.

#### Close Tasks on Sign Out

This illustration provides the Customer Collaboration Platform and Finesse API calls and events when agents are set to have
                                 assigned tasks closed on sign out.

The agent requests to sign out of the MRD with an active task.

CCE instructs Finesse to end the task. Finesse puts the dialog in CLOSED state, with the disposition code CD_AGENT_LOGGED_OUT_DURING_DIALOG.

The agent is signed out of the MRD.

#### Transfer Tasks on Sign Out

This illustration provides the Customer Collaboration Platform and Finesse API calls and events when agents are set to have
                                 assigned tasks transferred on sign out.

The agent requests to sign out of the MRD with an active task.

CCE instructs Finesse to end the dialog. Finesse puts the dialog in the CLOSED state, with the disposition code CD_TASK_TRANSFERRED_ON_AGENT_LOGOUT.
                                       Finesse does not send a handled notification to Customer Collaboration Platform.

The Finesse server on which the agent was signed in resubmits the task to Customer Collaboration Platform with the original
                                       script selector. The task is queued to the script selector as a new task.

The agent is signed out of the MRD.

## Failover and Failure Recovery

Component

Failover/Failure Scenario

New Task Request Impact

Queued, Offered, and Active Task Impact

Customer Collaboration Platform

MR connection fails. For example, there is a networking problem, the PG loses connection, or Customer Collaboration Platform
                                       loses connection.

Finesse loses connection with Customer Collaboration Platform.

New task requests from Customer Collaboration Platform application : New task requests fail, and the failures are delivered back to the application. Details of these failures are described
                                       in the next column.

Automatic transfer request from Finesse (for transfer on sign out or RONA): Results in a lost transfer request.

Agent transfer request: The request fails, and Finesse sends an error back to the application. Finesse retains the task.

Queued tasks: When tasks are submitted, they can be set to requeue on recovery. Typically, non-interactive tasks, such as email, are set
                                       to requeue on recovery because there is not a way to alert the customer that there was a problem while in queue. Interactive
                                       tasks, such as chat, are set not to requeue on recovery because the customer is waiting at an interface for an agent, and
                                       there is a way to alert the customer that there is a problem.

If tasks are set to requeue on recovery, the task is resubmitted when the MR connection is reestablished. The status and statusReason
                                       of the contact does not change.

If tasks are set NOT to requeue on recovery, the task's contact's status is marked discarded. The task's contact's statusReason
                                       is marked as follows:

Customer Collaboration Platform failure:

NOTIFICATION_CCE_

CUSTOMERCOLLABORATIONPLATFORM_ SYSTEM_FAILURE

MR connection failure: NOTIFICATION_CCE_CONNECTION_LOST

Offered and active tasks: No impact.

Customer Collaboration Platform

Customer Collaboration Platform overruns the new task queue limit.

See the Cisco Customer Collaboration Platform Developer Guide for the limit ( https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html ).

New task requests from Customer Collaboration Platform application: New task requests are discarded with the statusReason NOTIFICATION_RATE_LIMITED.

Automatic or agent transfer requests: No impact

Queued, offered, and active tasks: No impact.

Finesse

Finesse loses connection with Agent PG or CTI Server

New task request from Customer Collaboration Platform application: No impact

Automatic transfer requests from Finesse (for transfer on logout or RONA): Automatic transfers are initiated on the Finesse server on which the agent was signed in.
                                       Any outage on that Finesse server can result in lost transfer requests.

Agent transfer request: The request fails because Finesse is out of service, and Finesse retains the task.

Agents signed into media on the failed Finesse server are put into WORK_NOT_READY state and made not routable. Tasks on that
                                       server are preserved in their current state, and time continues to accrue towards the maximum task lifetime. The agent fails
                                       over to the secondary Finesse server, and must sign in to the media again. The agent is put into the previous state. If the
                                       agent doesn't have tasks, the agent is put in NOT_READY state.

Queued tasks: No impact.

Offered tasks: These tasks RONA because the agent cannot accept them.

Active tasks: These tasks fail over to the other Finesse server and are recovered on that server.

Any active tasks that were in INTERRUPTED state at the time of the lost connection change are recovered. However, these tasks
                                                   change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent can only close tasks when they are in the UNKNOWN
                                                   state.

Finesse

Agent logs out, or presence is lost while agent has active tasks

New task request from Customer Collaboration Platform application: No impact

Automatic or agent transfer requests: No impact

Queued tasks: No impact.

Offered tasks: These tasks fail over to the other Finesse server and are recovered on that server. If a task's Start Timeout threshold is
                                       exceeded during failover, the task RONAs.

Active tasks: If an agent logs out with active tasks, or agent presence is lost with active tasks, the tasks are either closed or transferred
                                       to the original script selector depending on how the agent was configured when signing into the MRD.

If the tasks are transferred, the disposition code is CD_TASK_TRANSFERRED_AGENT_LOGOUT.

If the tasks are closed, the disposition code is CD_AGENT_LOGGED_OUT_DURING_ DIALOG.

Finesse application

Finesse application fails

New task request from Customer Collaboration Platform  application: No impact

Automatic or agent transfer requests: No impact

Queued tasks: No impact.

Offered tasks: These tasks may RONA depending on how the application is structured. A Task Routing application may prevent an agent from
                                       accepting a dialog when the application down because the agent cannot handle the dialog while the application is down. In
                                       this case, the dialog RONAs.

Active tasks: Varies by application. Applications are responsible for managing the tasks while the application is down. Finesse retains
                                       the tasks, and the tasks are recovered once the application is restored.

CTI Server or OPC

One CTI Server or one OPC fails

New task request from Customer Collaboration Platform application: No impact

Automatic transfer requests from Finesse (for transfer on logout or RONA): Results in lost transfer requests.

Agent transfer request: The request fails, and Finesse retains the task.

Queued tasks: No impact.

Offered tasks: These tasks fail over to the other Finesse server and are recovered on that server. If a task's Start Timeout threshold is
                                       exceeded during failover, the task RONAs.

Active tasks: These tasks fail over to the other Finesse server and are recovered on that server.

Any active tasks that were in INTERRUPTED state at the time of the lost connection change are also recovered. However, these
                                                   tasks change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent only can only close tasks when they are
                                                   in the UNKNOWN state.

OPC

Both OPCs fail

New task request from Customer Collaboration Platform application: No impact

Automatic or agent transfer requests: Results in lost transfers.

Queued tasks: No impact

Offered and active tasks: These tasks are lost

## Task Routing Setup

### Initial Setup

Step

Task

Notes

Set up CCE

4

Set up the MR PG and PIM for Customer Collaboration Platform .

See Set up the Media Routing PG and PIM .

5

Add Customer Collaboration Platform as an External Machine in the System Inventory.

See Add Customer Collaboration Platform as an External Machine .

The system configures the following settings automatically in Customer Collaboration Platform Administration:

Enables and configures the CCE Multichannel Routing settings .

Configures the Task feed and the associated campaign and Connection to CCE notification needed for the Task Routing feature.

6

Configure the following in Unified CCE Administration:

Media Routing Domains

Call types

Dialed numbers

Skill groups or precision queues

ECC variables

Agent desk settings

See Unified CCE Administration and Configuration Manager Tools .

7

Increase the TCDTimeout registry key value, if you are using precision queues and will be submitting potentially long tasks,
                                          like email.

See Increase TCDTimeout Value .

8

Create routing scripts

See Create Routing Scripts for Task Routing .

Create Custom Customer Collaboration Platform and Finesse Applications

9

Create the Customer Collaboration Platform multichannel application to begin task requests.

See Sample Customer Collaboration Platform HTML Task Application .

10

Create the Finesse applications to manage nonvoice agent and dialog states.

See Sample Finesse Code for Task Routing.

Set up Finesse

11

Upload the Finesse applications to the desktop layout (optional).

See the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html .

### Set up the Media Routing PG and PIM

Caution

Before performing the step to enable the secured connection between the components, ensure that the security certificate management
                                             process is completed.

Set up the Media Routing PG and PIM

### SUMMARY STEPS

- Navigate to Unified CCE Administration > Overview > Infrastructure Settings > Peripheral Gateways . Determine the Peripheral ID for a Multichannel peripheral that is unused.

- From Cisco Unified CCE Tools, select Peripheral Gateway Setup .

- On the Components Setup screen, in the Instance Components panel, select the PG Instance component. Click Edit .

- On the Components Setup screen, in the Instance Components panel, select the PG Instance component. If the PG does not exist,
                                 click Add . If it exists, click Edit .

- In the Peripheral Gateways Properties screen, click Media Routing . Click Next .

- Click Yes at the prompt to stop the service.

- From the Peripheral Gateway Component Properties screen, click Add , select the next PIM, and configure with the Client Type of Media Routing as follows.

- On the Peripheral Gateway Component Properties screen, enter the Logical Controller ID that you recorded when you configured
                                 the Media Routing PG and PIM (applicable to Unified CCE).

- Accept defaults and click Next until the Setup Complete screen opens.

- At the Setup Complete screen, check Yes to start the service. Click Finish .

- Click Exit Setup .

- Repeat this procedure for Side B.

### DETAILED STEPS

Step 1

Navigate to Unified CCE Administration > Overview > Infrastructure Settings > Peripheral Gateways . Determine the Peripheral ID for a Multichannel peripheral that is unused.

Step 2

From Cisco Unified CCE Tools, select Peripheral Gateway Setup .

Step 3

On the Components Setup screen, in the Instance Components panel, select the PG Instance component. Click Edit .

Step 4

On the Components Setup screen, in the Instance Components panel, select the PG Instance component. If the PG does not exist,
                                          click Add . If it exists, click Edit .

Step 5

In the Peripheral Gateways Properties screen, click Media Routing . Click Next .

Step 6

Click Yes at the prompt to stop the service.

Step 7

From the Peripheral Gateway Component Properties screen, click Add , select the next PIM, and configure with the Client Type of Media Routing as follows.

Check Enabled .

In the Peripheral Name field, enter MR .

In the Peripheral ID field, enter the Peripheral ID for the unused Multichannel peripheral that you identified in Step 1 (applicable to Packaged
                                                CCE).

For Application Hostname (1) , enter the hostname or IP address.

By default, Customer Collaboration Platform accepts the MR connection on Application Connection Port 38001. The Application Connection Port setting on Customer Collaboration Platform must match the setting on the MR PG. If
                                                you change the port on one side of the connection, you must change it on the other side.

Leave the Application Hostname (2) field blank.

Keep all other values.

Check the Enable Secured Connection option.

This establishes a secured connectionbetween MR PIM and Application Server.

Ensure that you provide the correct information in the Application Hostname (1) and Application Connection Port (1) fields.

Click OK .

Step 8

On the Peripheral Gateway Component Properties screen, enter the Logical Controller ID that you recorded when you configured
                                          the Media Routing PG and PIM (applicable to Unified CCE).

Step 9

Accept defaults and click Next until the Setup Complete screen opens.

Step 10

At the Setup Complete screen, check Yes to start the service. Click Finish .

Step 11

Click Exit Setup .

Step 12

Repeat this procedure for Side B.

### Add Customer Collaboration Platform as an External Machine

When you add Customer Collaboration Platform as an External Machine in the Unified CCE Administration System Inventory, the
                                 system automatically performs the following Customer Collaboration Platform configuration:

Enables and completes the CCE Configuration for Multichannel Routing settings in Customer Collaboration Platform Administration.

These settings include the hostnames of the Unified CCE PGs and the Application Connection Port you specified when setting
                                       up the MR PG and PIM (applicable to Packaged CCE).

Configures the Task feed and the associated campaign and Connection to CCE notification needed for the Customer Collaboration
                                       Platform feature, with the following names:

Task feed: Cisco_Default_Task_Feed

Campaign: Cisco_Default_Task_Campaign

Notification: Cisco_Default_Task_Notification

Tag: cisco_task_tag

If the Task feed has been configured to use a different tag, the Connection to CCE notification is configured to use that
                                                   tag.

Step 1

In Unified CCE Administration , click Inventory from the left navigation.

Step 2

Click the Main or RemoteSite tab

Step 3

Click the New button that appears on top of the grid.

Step 4

Select Customer Collaboration Platform from the drop-down list.

Step 5

Enter the fully qualified domain name (FQDN), hostname or IP address in the Hostname field.

The system attempts to convert the value you enter to FQDN.

Step 6

Enter the Customer Collaboration Platform Administration username and password.

Step 7

Click Save .

### Unified CCE Administration and Configuration Manager Tools

This topic explains the Unified CCE Administration and Configuration Manager tools you need to configure Task Routing.

For details on the procedures for these steps, refer to the Unified Contact Center Enterprise (Unified CCE) Administration
                                 online help and the Configuration Manager online help.

### SUMMARY STEPS

- Sign in to Unified CCE Administration.

- Configure the following:

### DETAILED STEPS

Step 1

Sign in to Unified CCE Administration.

Step 2

Configure the following:

Item to Configure

Details

Media Routing Domains

Create an MRD for each type of task that the custom application submits to CCE (email, chat, and so on).

Call Types

Create call types for Task Routing.

Dialed Numbers

Create dialed numbers for Task Routing. Add the numbers or strings that the custom application will use when submitting task
                                                         requests.

On the Attributes tab, select a Task Routing MRD from the Media routing domain drop-down list box.

On the Dialed Number Mapping tab, map the script selector to a call type you created for Task Routing.

Important

Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs.

Skill Groups

Configure either skill groups or precision queues.

If you configure skill groups:

For Media Routing Domain , select one of the Task Routing MRDs you created.

Assign agents to the skill group.

Precision Queues

Configure either skill groups or precision queues.

If you configure precision queues:

For Media Routing Domain , select one of the Task Routing MRDs you created.

Associate agents with attributes that are part of the precision queue steps.

Expanded Call Variable

You can use an existing Expanded Call Variable, or you can create an Expanded Call Variable for Task Routing, depending on
                                                         the needs of your third-party multichannel application.

Arrays are not supported with the Task Routing feature.

CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform.

Network VRU Script

Create a Network VRU Script that references the Network VRU (MR_Network_VRU). The Network VRU Script is used to return estimated
                                                         wait time to customers.

You can accept the default values.

When you configure the Network VRU Script, you specify whether it is interruptible. The Interruptible setting for the Network VRU Script controls whether the script can be interrupted (for example if an agent becomes available).
                                                         This setting is not related to the Media Routing Domain Interruptible setting, which controls whether an agent working on a task in that MRD can be interrupted by a task from a non-interruptible
                                                         MRD.

For more information on writing scripts to return estimated wait time, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Agent Desk Settings

If agents will use a Task Routing gadget in the Finesse desktop, leave the Logout inactivity time setting for those agents blank, or remove the existing value.

Otherwise, if the agent exceeds the Logout inactivity time in the voice MRD, the agent is logged out of the Cisco Finesse desktop, even if the agent is actively working on tasks from
                                                         nonvoice MRDs. The agent needs log into the desktop again to continue working on the nonvoice tasks.

### Increase TCDTimeout Value

Complete this procedure only if you are using precision queues and routing tasks with potentially long durations, like emails.

Several precision queue fields in the Termination_Call_Detail record are not completed until the end of a task. These precision
                                 queue fields are blank for tasks whose durations exceed the TCDTimeout registry key value. The default value of theTCDTimeout
                                 registry key is 9,000 seconds (2.5 hours).

If you are configuring a system to handle email or other long tasks, you can increase the TCDTimeout registry key value to
                                 a maximum of 86,400 seconds (24 hours).

Change the registry key on either the Side A or B Unified CCE Rogger in Packaged CCE.

### SUMMARY STEPS

- Modify the following registry key: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\Icm\<instance name>\Router<A/B>\Router\CurrentVersion\Configuration\Global\TCDTimeout .

### DETAILED STEPS

Modify the following registry key: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\Icm\<instance name>\Router<A/B>\Router\CurrentVersion\Configuration\Global\TCDTimeout .

### Create Routing Scripts for Task Routing

For complete multichannel scripting information in Packaged CCE, see https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Important

Ensure that the routing scripts include skill groups or precision queues from the appropriate Media Routing Domains to handle
                                          all of the types of tasks that can be routed with the scripts. For example, if a script is used to route email tasks, be sure
                                          that the script includes skill groups or precision queues from an email MRD.

## Sample Code for Task Routing

Cisco Systems has made sample Task Routing application code for Customer Collaboration Platform and Finesse available to
                           use as baselines in building your own applications.

### Sample Customer Collaboration Platform HTML Task Application

The sample Customer Collaboration Platform HTML Task application:

Submits task requests to CCE.

Retrieves and displays the estimated wait time, if it has been configured in CCE.

You cannot copy and paste this code to achieve a working application. It is only a guideline.

The sample application uses the Task API. For more information about how to use the Task API, see the Cisco Customer Collaboration Platform Developer Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html .

### SUMMARY STEPS

- Download the sample HTML Task application from DevNet: https://developer.cisco.com/site/task-routing/ .

- Read the sample application's readme.txt file to complete the prerequisites and use the sample application.

### DETAILED STEPS

Step 1

Download the sample HTML Task application from DevNet: https://developer.cisco.com/site/task-routing/ .

Step 2

Read the sample application's readme.txt file to complete the prerequisites and use the sample application.

### Sample Finesse Code for Task Routing

The Finesse sample Task Management Gadget application lets agents perform the following actions in individual nonvoice Media
                                 Routing Domains:

Sign in and out.

Change state.

Handle tasks.

The sample gadget also signals the Customer Context gadget to display a customer record.

You cannot copy and paste this code to achieve a working application. It is only a guideline.

For more information about how to use the APIs available for Task Routing , see the Cisco Finesse Web Services Developer Guide at https://developer.cisco.com/site/finesse/ .

Step 1

Download the sample Task Management Gadget application (TaskManagementGadget-x.x.zip) from DevNet: https://developer.cisco.com/site/task-routing/ .

Step 2

Read the sample application's readme.txt file to complete the prerequisites and use the sample application.

For more information about uploading third-party gadgets to the Finesse server, see the "Third Party Gadgets" chapter in the Cisco Finesse Web Services Developer Guide at https://developer.cisco.com/site/finesse/ .

For more information about adding third-party gadgets to the Finesse desktop, see the "Manage Third-Party Gadgets" chapter
                                             in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html .

## Task Routing Reporting

Cisco Unified Intelligence Center CCE reports include data for voice calls and nonvoice Task Routing tasks.

You can filter these All Fields and Live Data report templates by Media Routing Domain:

Agent Real Time

Agent Skill Group Real Time

Peripheral Skill Group Real Time All Fields

Precision Queue Real Time All Fields

Agent Precision Queue Historical All Fields

Agent Skill Group Historical All Fields

Peripheral Skill Group Historical All Fields

Precision Queue Abandon Answer Distribution Historical

Precision Queue Interval All Fields

Skill Group Abandon—Answer Distribution Historical

Precision Queue — Live Data

Skill Group — Live Data

| Note | CCE solutions support only the Latin 1 character set for Expanded Call Context variables and Call variables when used with
                                             Finesse and Customer Collaboration Platform. Arrays are not supported. |
|---|---|

| API Parameter or Setting | API/Tool | Possible Values |
|---|---|---|
| Interactive Task/MRD | Non-interactive Task/MRD |
| requeueOnRecovery Whether Customer Collaboration Platform re-queues  re-queues or discards the task when Customer Collaboration Platform  recovers
                                             from a failure. Set this parameter when submitting a task request. | Customer Collaboration Platform Task Submission API | False — customers are waiting at an interface for an agent and can be notified if there is a problem. You don't need to resubmit
                                             these tasks. | True — customers are not waiting at an interface for an agent, and there is no way to alert them that there was a problem. You
                                             need to resubmit these tasks. |
| dialogLogoutAction Whether active tasks are closed or transferred when an agent signs out or loses presence. Set this parameter when an agent signs in to a Media Routing Domain. | Finesse Media Sign In API | Close — customers are engaged with an agent, and can be notified that the task has ended. | Transfer — customers are not engaged with an agent, and there is no way to alert them that the task has ended. |
| Start Timeout The amount of time that the system waits for an agent to accept an offered task. When this time is reached, the system makes
                                             the agent not routable and re-queues the task. Set this parameter when configuring an MRD. | Media Routing Domains tool in Unified CCE Administration | Shorter duration — customer is waiting at an interface for the agent | Longer duration — customer is not waiting at an interface for an agent |
| Monitoring status of submitted tasks You can monitor status of submitted and queued tasks using either the Customer Collaboration Platform  Task API to poll for
                                             status or Customer Collaboration Platform  XMPP BOSH eventing. | Customer Collaboration Platform Task API or XMPP BOSH eventing | Use Customer Collaboration Platform Task API status polling for MRDs when you want to monitor the status of a single contact/task. | Use Customer Collaboration Platform XMPP BOSH eventing to receive updates on all contacts/tasks in the campaign supporting
                                             Universal Queue over one channel. |

| Note | If you change the MRD from interruptible to non-interruptible or vice versa, the change takes effect once the agent logs out
                                             and then logs back in on that MRD. |
|---|---|

| Command or Action | Purpose |
|---|---|
| Specify whether an MRD accepts or ignores interrupt events when an agent signs into the Finesse application, using the interruptAction parameter in the Finesse Media - Sign In API . This setting controls the agent's state in an interrupted MRD and ability to work on interrupted tasks. The setting applies
                                             only when a task from a non-interruptible MRD interrupts the agent. | Accept: When an agent is interrupted by a task from a non-interruptible MRD while working on a task in an interruptible MRD, Finesse
                                                accepts the interrupt event. The agent, CCE task, and Finesse dialog state in the interrupted MRD change to INTERRUPTED. The agent cannot perform dialog actions while a task is interrupted. Important The application is responsible for disabling all dialog-related activities in the interface when an agent's state changes
                                                                  to INTERRUPTED. The agent's time on task stops while the agent is interrupted. Example: An agent has an email task for 20 minutes, and is interrupted for 3 of those minutes with a chat task. The handled
                                                      time for the email task is 17 minutes, and the handled time for the chat task is 3 minutes. Ignore: When an agent is interrupted by another task while working on a task in an interruptible MRD, Finesse ignores the interrupt
                                                      event. The new task does not affect any of the agent's other assigned tasks. The agent, CCE task, and Finesse dialog state in the
                                                      interrupted MRDs do not change. The agent can perform dialog actions on original task and the interrupting task at the same time. The agent's time on the
                                                      original task does not stop while the agent is handling the interrupting task. Example: An agent has an email task for 20 minutes, and is interrupted for 3 of those minutes with a chat task. The handled
                                                      time for the email task is 20 minutes, and the handled time for the chat task is 3 minutes. This means that during a 20-minute
                                                      interval, the agent handled tasks for 23 minutes. If an agent is working on a task in an interruptible MRD and is routed a task in another interruptible MRD, CCE does not send
                                                an interrupt event. Therefore, the interruptAction setting does not apply. | Important | The application is responsible for disabling all dialog-related activities in the interface when an agent's state changes
                                                                  to INTERRUPTED. |
| Important | The application is responsible for disabling all dialog-related activities in the interface when an agent's state changes
                                                                  to INTERRUPTED. |

| Important | The application is responsible for disabling all dialog-related activities in the interface when an agent's state changes
                                                                  to INTERRUPTED. |
|---|---|

| Important | You must associate each Task Routing dialed number with a call type. The default call type is not supported for Task Routing. |
|---|---|

| Note | The number of available slots is an important factor in the Longest Available Agent (LAA) calculation. The number of available slots = The maximum concurrent task limit for the MRD that an Agent has logged into - Current tasks being handled by the Agent or routed to the Agent. If there are multiple skill groups that are part of the queue node, then the skill group that has the higher LAA is picked.
                                                Then, the agents within the picked skill group (or the Precision Queue) who have the highest number of available slots for
                                                non-voice tasks get prioritised. Agents with the same number of available slots get prioritized based on the time in the available state or the LAA mechanism. |
|---|---|

| Customer Collaboration Platform Social Contact Task State | Finesse Dialog State |
|---|---|
| Unread: The task request has not been submitted to the contact center. | None |
| Queued: The task request is successfully submitted to the contact center as a result of creating a new task or resubmitting a task
                                          due to agent transfer, automatic transfer on agent logout, or automatic transfer for RONA. | None |
| Reserved: The task is assigned to an agent. This state includes all work on a task. | Offered: The dialog is being offered to the agent. |
| Accepted: The agent accepted the dialog but has not started working on it. |
| Active: The agent is working on the dialog. |
| Paused: The agent paused the dialog. |
| Wrapping Up: The agent is performing wrap up activity on the dialog. |
| Interrupted: The agent is interrupted with a task from a non-interruptible Media Routing Domain. The agent cannot work on this task until
                                          the interrupting task is complete. |
| Handled: Customer Collaboration Platform receives a handled notification from Finesse indicating that the task ended. | Closed: The agent ended the task. Finesse sends a handled notification to Customer Collaboration Platform. |

| Component | Failover/Failure Scenario | New Task Request Impact | Queued, Offered, and Active Task Impact |
|---|---|---|---|
| Customer Collaboration Platform | MR connection fails. For example, there is a networking problem, the PG loses connection, or Customer Collaboration Platform
                                       loses connection. Finesse loses connection with Customer Collaboration Platform. | New task requests from Customer Collaboration Platform application : New task requests fail, and the failures are delivered back to the application. Details of these failures are described
                                       in the next column. Automatic transfer request from Finesse (for transfer on sign out or RONA): Results in a lost transfer request. Agent transfer request: The request fails, and Finesse sends an error back to the application. Finesse retains the task. | Queued tasks: When tasks are submitted, they can be set to requeue on recovery. Typically, non-interactive tasks, such as email, are set
                                       to requeue on recovery because there is not a way to alert the customer that there was a problem while in queue. Interactive
                                       tasks, such as chat, are set not to requeue on recovery because the customer is waiting at an interface for an agent, and
                                       there is a way to alert the customer that there is a problem. If tasks are set to requeue on recovery, the task is resubmitted when the MR connection is reestablished. The status and statusReason
                                       of the contact does not change. If tasks are set NOT to requeue on recovery, the task's contact's status is marked discarded. The task's contact's statusReason
                                       is marked as follows: Customer Collaboration Platform failure: NOTIFICATION_CCE_ CUSTOMERCOLLABORATIONPLATFORM_ SYSTEM_FAILURE MR connection failure: NOTIFICATION_CCE_CONNECTION_LOST Offered and active tasks: No impact. |
| Customer Collaboration Platform | Customer Collaboration Platform overruns the new task queue limit. See the Cisco Customer Collaboration Platform Developer Guide for the limit ( https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html ). | New task requests from Customer Collaboration Platform application: New task requests are discarded with the statusReason NOTIFICATION_RATE_LIMITED. Automatic or agent transfer requests: No impact | Queued, offered, and active tasks: No impact. |
| Finesse | Finesse loses connection with Agent PG or CTI Server | New task request from Customer Collaboration Platform application: No impact Automatic transfer requests from Finesse (for transfer on logout or RONA): Automatic transfers are initiated on the Finesse server on which the agent was signed in.
                                       Any outage on that Finesse server can result in lost transfer requests. Agent transfer request: The request fails because Finesse is out of service, and Finesse retains the task. | Agents signed into media on the failed Finesse server are put into WORK_NOT_READY state and made not routable. Tasks on that
                                       server are preserved in their current state, and time continues to accrue towards the maximum task lifetime. The agent fails
                                       over to the secondary Finesse server, and must sign in to the media again. The agent is put into the previous state. If the
                                       agent doesn't have tasks, the agent is put in NOT_READY state. Queued tasks: No impact. Offered tasks: These tasks RONA because the agent cannot accept them. Active tasks: These tasks fail over to the other Finesse server and are recovered on that server. Note Any active tasks that were in INTERRUPTED state at the time of the lost connection change are recovered. However, these tasks
                                                   change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent can only close tasks when they are in the UNKNOWN
                                                   state. | Note | Any active tasks that were in INTERRUPTED state at the time of the lost connection change are recovered. However, these tasks
                                                   change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent can only close tasks when they are in the UNKNOWN
                                                   state. |
| Note | Any active tasks that were in INTERRUPTED state at the time of the lost connection change are recovered. However, these tasks
                                                   change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent can only close tasks when they are in the UNKNOWN
                                                   state. |
| Finesse | Agent logs out, or presence is lost while agent has active tasks | New task request from Customer Collaboration Platform application: No impact Automatic or agent transfer requests: No impact | Queued tasks: No impact. Offered tasks: These tasks fail over to the other Finesse server and are recovered on that server. If a task's Start Timeout threshold is
                                       exceeded during failover, the task RONAs. Active tasks: If an agent logs out with active tasks, or agent presence is lost with active tasks, the tasks are either closed or transferred
                                       to the original script selector depending on how the agent was configured when signing into the MRD. If the tasks are transferred, the disposition code is CD_TASK_TRANSFERRED_AGENT_LOGOUT. If the tasks are closed, the disposition code is CD_AGENT_LOGGED_OUT_DURING_ DIALOG. |
| Finesse application | Finesse application fails | New task request from Customer Collaboration Platform  application: No impact Automatic or agent transfer requests: No impact | Queued tasks: No impact. Offered tasks: These tasks may RONA depending on how the application is structured. A Task Routing application may prevent an agent from
                                       accepting a dialog when the application down because the agent cannot handle the dialog while the application is down. In
                                       this case, the dialog RONAs. Active tasks: Varies by application. Applications are responsible for managing the tasks while the application is down. Finesse retains
                                       the tasks, and the tasks are recovered once the application is restored. |
| CTI Server or OPC | One CTI Server or one OPC fails | New task request from Customer Collaboration Platform application: No impact Automatic transfer requests from Finesse (for transfer on logout or RONA): Results in lost transfer requests. Agent transfer request: The request fails, and Finesse retains the task. | Queued tasks: No impact. Offered tasks: These tasks fail over to the other Finesse server and are recovered on that server. If a task's Start Timeout threshold is
                                       exceeded during failover, the task RONAs. Active tasks: These tasks fail over to the other Finesse server and are recovered on that server. Note Any active tasks that were in INTERRUPTED state at the time of the lost connection change are also recovered. However, these
                                                   tasks change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent only can only close tasks when they are
                                                   in the UNKNOWN state. | Note | Any active tasks that were in INTERRUPTED state at the time of the lost connection change are also recovered. However, these
                                                   tasks change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent only can only close tasks when they are
                                                   in the UNKNOWN state. |
| Note | Any active tasks that were in INTERRUPTED state at the time of the lost connection change are also recovered. However, these
                                                   tasks change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent only can only close tasks when they are
                                                   in the UNKNOWN state. |
| OPC | Both OPCs fail | New task request from Customer Collaboration Platform application: No impact Automatic or agent transfer requests: Results in lost transfers. | Queued tasks: No impact Offered and active tasks: These tasks are lost |

| Note | Any active tasks that were in INTERRUPTED state at the time of the lost connection change are recovered. However, these tasks
                                                   change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent can only close tasks when they are in the UNKNOWN
                                                   state. |
|---|---|

| Note | Any active tasks that were in INTERRUPTED state at the time of the lost connection change are also recovered. However, these
                                                   tasks change to the UNKNOWN state when the task is no longer INTERRUPTED. The agent only can only close tasks when they are
                                                   in the UNKNOWN state. |
|---|---|

| Step | Task | Notes |
|---|---|---|
| Set up CCE |
| 4 | Set up the MR PG and PIM for Customer Collaboration Platform . See Set up the Media Routing PG and PIM . |  |
| 5 | Add Customer Collaboration Platform as an External Machine in the System Inventory. See Add Customer Collaboration Platform as an External Machine . | The system configures the following settings automatically in Customer Collaboration Platform Administration: Enables and configures the CCE Multichannel Routing settings . Configures the Task feed and the associated campaign and Connection to CCE notification needed for the Task Routing feature. |
| 6 | Configure the following in Unified CCE Administration: Media Routing Domains Call types Dialed numbers Skill groups or precision queues ECC variables Agent desk settings See Unified CCE Administration and Configuration Manager Tools . |  |
| 7 | Increase the TCDTimeout registry key value, if you are using precision queues and will be submitting potentially long tasks,
                                          like email. See Increase TCDTimeout Value . |  |
| 8 | Create routing scripts See Create Routing Scripts for Task Routing . |  |
| Create Custom Customer Collaboration Platform and Finesse Applications |
| 9 | Create the Customer Collaboration Platform multichannel application to begin task requests. See Sample Customer Collaboration Platform HTML Task Application . |  |
| 10 | Create the Finesse applications to manage nonvoice agent and dialog states. See Sample Finesse Code for Task Routing. |  |
| Set up Finesse |
| 11 | Upload the Finesse applications to the desktop layout (optional). See the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . |  |

| Caution | Before performing the step to enable the secured connection between the components, ensure that the security certificate management
                                             process is completed. |
|---|---|

| Step 1 | Navigate to Unified CCE Administration > Overview > Infrastructure Settings > Peripheral Gateways . Determine the Peripheral ID for a Multichannel peripheral that is unused. |
|---|---|
| Step 2 | From Cisco Unified CCE Tools, select Peripheral Gateway Setup . |
| Step 3 | On the Components Setup screen, in the Instance Components panel, select the PG Instance component. Click Edit . |
| Step 4 | On the Components Setup screen, in the Instance Components panel, select the PG Instance component. If the PG does not exist,
                                          click Add . If it exists, click Edit . |
| Step 5 | In the Peripheral Gateways Properties screen, click Media Routing . Click Next . |
| Step 6 | Click Yes at the prompt to stop the service. |
| Step 7 | From the Peripheral Gateway Component Properties screen, click Add , select the next PIM, and configure with the Client Type of Media Routing as follows. Check Enabled . In the Peripheral Name field, enter MR . In the Peripheral ID field, enter the Peripheral ID for the unused Multichannel peripheral that you identified in Step 1 (applicable to Packaged
                                                CCE). For Application Hostname (1) , enter the hostname or IP address. By default, Customer Collaboration Platform accepts the MR connection on Application Connection Port 38001. The Application Connection Port setting on Customer Collaboration Platform must match the setting on the MR PG. If
                                                you change the port on one side of the connection, you must change it on the other side. Leave the Application Hostname (2) field blank. Keep all other values. Check the Enable Secured Connection option. This establishes a secured connectionbetween MR PIM and Application Server. Ensure that you provide the correct information in the Application Hostname (1) and Application Connection Port (1) fields. Click OK . |
| Step 8 | On the Peripheral Gateway Component Properties screen, enter the Logical Controller ID that you recorded when you configured
                                          the Media Routing PG and PIM (applicable to Unified CCE). |
| Step 9 | Accept defaults and click Next until the Setup Complete screen opens. |
| Step 10 | At the Setup Complete screen, check Yes to start the service. Click Finish . |
| Step 11 | Click Exit Setup . |
| Step 12 | Repeat this procedure for Side B. |

| Note | If the Task feed has been configured to use a different tag, the Connection to CCE notification is configured to use that
                                                   tag. |
|---|---|

| Step 1 | In Unified CCE Administration , click Inventory from the left navigation. |
|---|---|
| Step 2 | Click the Main or RemoteSite tab |
| Step 3 | Click the New button that appears on top of the grid. The Add Machine dialog box appears. |
| Step 4 | Select Customer Collaboration Platform from the drop-down list. |
| Step 5 | Enter the fully qualified domain name (FQDN), hostname or IP address in the Hostname field. Note The system attempts to convert the value you enter to FQDN. | Note | The system attempts to convert the value you enter to FQDN. |
| Note | The system attempts to convert the value you enter to FQDN. |
| Step 6 | Enter the Customer Collaboration Platform Administration username and password. |
| Step 7 | Click Save . |

| Note | The system attempts to convert the value you enter to FQDN. |
|---|---|

| Step 1 | Sign in to Unified CCE Administration. |
|---|---|
| Step 2 | Configure the following: Item to Configure Details Media Routing Domains Create an MRD for each type of task that the custom application submits to CCE (email, chat, and so on). Call Types Create call types for Task Routing. Dialed Numbers Create dialed numbers for Task Routing. Add the numbers or strings that the custom application will use when submitting task
                                                         requests. On the Attributes tab, select a Task Routing MRD from the Media routing domain drop-down list box. On the Dialed Number Mapping tab, map the script selector to a call type you created for Task Routing. Important Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. Skill Groups Configure either skill groups or precision queues. If you configure skill groups: For Media Routing Domain , select one of the Task Routing MRDs you created. Assign agents to the skill group. Precision Queues Configure either skill groups or precision queues. If you configure precision queues: For Media Routing Domain , select one of the Task Routing MRDs you created. Associate agents with attributes that are part of the precision queue steps. Expanded Call Variable You can use an existing Expanded Call Variable, or you can create an Expanded Call Variable for Task Routing, depending on
                                                         the needs of your third-party multichannel application. Note Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. Network VRU Script Create a Network VRU Script that references the Network VRU (MR_Network_VRU). The Network VRU Script is used to return estimated
                                                         wait time to customers. You can accept the default values. When you configure the Network VRU Script, you specify whether it is interruptible. The Interruptible setting for the Network VRU Script controls whether the script can be interrupted (for example if an agent becomes available).
                                                         This setting is not related to the Media Routing Domain Interruptible setting, which controls whether an agent working on a task in that MRD can be interrupted by a task from a non-interruptible
                                                         MRD. For more information on writing scripts to return estimated wait time, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . Agent Desk Settings If agents will use a Task Routing gadget in the Finesse desktop, leave the Logout inactivity time setting for those agents blank, or remove the existing value. Otherwise, if the agent exceeds the Logout inactivity time in the voice MRD, the agent is logged out of the Cisco Finesse desktop, even if the agent is actively working on tasks from
                                                         nonvoice MRDs. The agent needs log into the desktop again to continue working on the nonvoice tasks. | Item to Configure | Details | Media Routing Domains | Create an MRD for each type of task that the custom application submits to CCE (email, chat, and so on). | Call Types | Create call types for Task Routing. | Dialed Numbers | Create dialed numbers for Task Routing. Add the numbers or strings that the custom application will use when submitting task
                                                         requests. On the Attributes tab, select a Task Routing MRD from the Media routing domain drop-down list box. On the Dialed Number Mapping tab, map the script selector to a call type you created for Task Routing. Important Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. | Important | Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. | Skill Groups | Configure either skill groups or precision queues. If you configure skill groups: For Media Routing Domain , select one of the Task Routing MRDs you created. Assign agents to the skill group. | Precision Queues | Configure either skill groups or precision queues. If you configure precision queues: For Media Routing Domain , select one of the Task Routing MRDs you created. Associate agents with attributes that are part of the precision queue steps. | Expanded Call Variable | You can use an existing Expanded Call Variable, or you can create an Expanded Call Variable for Task Routing, depending on
                                                         the needs of your third-party multichannel application. Note Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. | Note | Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. | Network VRU Script | Create a Network VRU Script that references the Network VRU (MR_Network_VRU). The Network VRU Script is used to return estimated
                                                         wait time to customers. You can accept the default values. When you configure the Network VRU Script, you specify whether it is interruptible. The Interruptible setting for the Network VRU Script controls whether the script can be interrupted (for example if an agent becomes available).
                                                         This setting is not related to the Media Routing Domain Interruptible setting, which controls whether an agent working on a task in that MRD can be interrupted by a task from a non-interruptible
                                                         MRD. For more information on writing scripts to return estimated wait time, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . | Agent Desk Settings | If agents will use a Task Routing gadget in the Finesse desktop, leave the Logout inactivity time setting for those agents blank, or remove the existing value. Otherwise, if the agent exceeds the Logout inactivity time in the voice MRD, the agent is logged out of the Cisco Finesse desktop, even if the agent is actively working on tasks from
                                                         nonvoice MRDs. The agent needs log into the desktop again to continue working on the nonvoice tasks. |
| Item to Configure | Details |
| Media Routing Domains | Create an MRD for each type of task that the custom application submits to CCE (email, chat, and so on). |
| Call Types | Create call types for Task Routing. |
| Dialed Numbers | Create dialed numbers for Task Routing. Add the numbers or strings that the custom application will use when submitting task
                                                         requests. On the Attributes tab, select a Task Routing MRD from the Media routing domain drop-down list box. On the Dialed Number Mapping tab, map the script selector to a call type you created for Task Routing. Important Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. | Important | Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. |
| Important | Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. |
| Skill Groups | Configure either skill groups or precision queues. If you configure skill groups: For Media Routing Domain , select one of the Task Routing MRDs you created. Assign agents to the skill group. |
| Precision Queues | Configure either skill groups or precision queues. If you configure precision queues: For Media Routing Domain , select one of the Task Routing MRDs you created. Associate agents with attributes that are part of the precision queue steps. |
| Expanded Call Variable | You can use an existing Expanded Call Variable, or you can create an Expanded Call Variable for Task Routing, depending on
                                                         the needs of your third-party multichannel application. Note Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. | Note | Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. |
| Note | Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. |
| Network VRU Script | Create a Network VRU Script that references the Network VRU (MR_Network_VRU). The Network VRU Script is used to return estimated
                                                         wait time to customers. You can accept the default values. When you configure the Network VRU Script, you specify whether it is interruptible. The Interruptible setting for the Network VRU Script controls whether the script can be interrupted (for example if an agent becomes available).
                                                         This setting is not related to the Media Routing Domain Interruptible setting, which controls whether an agent working on a task in that MRD can be interrupted by a task from a non-interruptible
                                                         MRD. For more information on writing scripts to return estimated wait time, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
| Agent Desk Settings | If agents will use a Task Routing gadget in the Finesse desktop, leave the Logout inactivity time setting for those agents blank, or remove the existing value. Otherwise, if the agent exceeds the Logout inactivity time in the voice MRD, the agent is logged out of the Cisco Finesse desktop, even if the agent is actively working on tasks from
                                                         nonvoice MRDs. The agent needs log into the desktop again to continue working on the nonvoice tasks. |

| Item to Configure | Details |
|---|---|
| Media Routing Domains | Create an MRD for each type of task that the custom application submits to CCE (email, chat, and so on). |
| Call Types | Create call types for Task Routing. |
| Dialed Numbers | Create dialed numbers for Task Routing. Add the numbers or strings that the custom application will use when submitting task
                                                         requests. On the Attributes tab, select a Task Routing MRD from the Media routing domain drop-down list box. On the Dialed Number Mapping tab, map the script selector to a call type you created for Task Routing. Important Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. | Important | Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. |
| Important | Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. |
| Skill Groups | Configure either skill groups or precision queues. If you configure skill groups: For Media Routing Domain , select one of the Task Routing MRDs you created. Assign agents to the skill group. |
| Precision Queues | Configure either skill groups or precision queues. If you configure precision queues: For Media Routing Domain , select one of the Task Routing MRDs you created. Associate agents with attributes that are part of the precision queue steps. |
| Expanded Call Variable | You can use an existing Expanded Call Variable, or you can create an Expanded Call Variable for Task Routing, depending on
                                                         the needs of your third-party multichannel application. Note Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. | Note | Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. |
| Note | Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. |
| Network VRU Script | Create a Network VRU Script that references the Network VRU (MR_Network_VRU). The Network VRU Script is used to return estimated
                                                         wait time to customers. You can accept the default values. When you configure the Network VRU Script, you specify whether it is interruptible. The Interruptible setting for the Network VRU Script controls whether the script can be interrupted (for example if an agent becomes available).
                                                         This setting is not related to the Media Routing Domain Interruptible setting, which controls whether an agent working on a task in that MRD can be interrupted by a task from a non-interruptible
                                                         MRD. For more information on writing scripts to return estimated wait time, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
| Agent Desk Settings | If agents will use a Task Routing gadget in the Finesse desktop, leave the Logout inactivity time setting for those agents blank, or remove the existing value. Otherwise, if the agent exceeds the Logout inactivity time in the voice MRD, the agent is logged out of the Cisco Finesse desktop, even if the agent is actively working on tasks from
                                                         nonvoice MRDs. The agent needs log into the desktop again to continue working on the nonvoice tasks. |

| Important | Each dialed number must be associated with a call type. Default call type is not supported for tasks submitted with Task Routing
                                                                           APIs. |
|---|---|

| Note | Arrays are not supported with the Task Routing feature. CCE solutions support the Latin 1 character set only for Expanded Call Context variables and Call variables when used with
                                                                     Finesse and Customer Collaboration Platform. |
|---|---|

| Modify the following registry key: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\Icm\<instance name>\Router<A/B>\Router\CurrentVersion\Configuration\Global\TCDTimeout . |
|---|

| Important | Ensure that the routing scripts include skill groups or precision queues from the appropriate Media Routing Domains to handle
                                          all of the types of tasks that can be routed with the scripts. For example, if a script is used to route email tasks, be sure
                                          that the script includes skill groups or precision queues from an email MRD. |
|---|---|

| Note | You cannot copy and paste this code to achieve a working application. It is only a guideline. |
|---|---|

| Step 1 | Download the sample HTML Task application from DevNet: https://developer.cisco.com/site/task-routing/ . |
|---|---|
| Step 2 | Read the sample application's readme.txt file to complete the prerequisites and use the sample application. |

| Note | You cannot copy and paste this code to achieve a working application. It is only a guideline. |
|---|---|

| Step 1 | Download the sample Task Management Gadget application (TaskManagementGadget-x.x.zip) from DevNet: https://developer.cisco.com/site/task-routing/ . |
|---|---|
| Step 2 | Read the sample application's readme.txt file to complete the prerequisites and use the sample application. For more information about uploading third-party gadgets to the Finesse server, see the "Third Party Gadgets" chapter in the Cisco Finesse Web Services Developer Guide at https://developer.cisco.com/site/finesse/ . For more information about adding third-party gadgets to the Finesse desktop, see the "Manage Third-Party Gadgets" chapter
                                             in the Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/tsd-products-support-series-home.html . |